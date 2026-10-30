#Requires -Version 7
<#
.SYNOPSIS
Prueft die Teardown-Pfadgrenze fuer Bash und PowerShell. / Validates the teardown path boundary for Bash and PowerShell.

.DESCRIPTION
Fuehrt Dry-Run-Proben und eine isolierte lokale Backup-Probe in einem temporaeren Home-Verzeichnis aus. Traversal, absolute Pfade, Links und geschuetzte Level-0-Quellen muessen scheitern; ein echtes direktes Kind muss funktionieren. Es werden keine Remotes veraendert. / Runs dry-run probes and one isolated local backup probe in a temporary Home directory. Traversal, absolute paths, links, and protected Level 0 sources must fail while a real direct child must work. No remotes are changed.

.EXAMPLE
pwsh -NoProfile -File scripts/tests/test-teardown-workspace-path-safety.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$bashScript = Join-Path $repositoryRoot 'scripts/teardown-workspace.sh'
$powerShellScript = Join-Path $repositoryRoot 'scripts/teardown-workspace.ps1'
$bashBootstrap = Join-Path $repositoryRoot 'scripts/bootstrap-workspace.sh'
$powerShellBootstrap = Join-Path $repositoryRoot 'scripts/bootstrap-workspace.ps1'
$testRoot = Join-Path ([System.IO.Path]::GetTempPath()) "teardown-path-safety-$([guid]::NewGuid().ToString('N'))"
$testHome = Join-Path $testRoot 'home'
$outside = Join-Path $testRoot 'outside'
$originalHome = $env:HOME
$originalHomeBaselineSource = $env:HOME_BASELINE_SOURCE
$failures = [System.Collections.Generic.List[string]]::new()

function Invoke-TeardownProbe {
    param(
        [Parameter(Mandatory)]
        [ValidateSet('bash', 'pwsh')]
        [string] $Shell,
        [Parameter(Mandatory)]
        [string] $WorkspaceName
    )

    $output = if ($Shell -eq 'bash') {
        & bash $bashScript $WorkspaceName --dry-run --keep-remote 2>&1 | Out-String
    }
    else {
        & pwsh -NoProfile -File $powerShellScript -WorkspaceName $WorkspaceName -WhatIf -KeepRemote 2>&1 | Out-String
    }
    [pscustomobject]@{
        ExitCode = $LASTEXITCODE
        Output = $output
    }
}

function Assert-Probe {
    param(
        [string] $Label,
        [pscustomobject] $Probe,
        [int] $ExpectedExitCode,
        [string] $ExpectedText
    )

    if ($Probe.ExitCode -ne $ExpectedExitCode -or $Probe.Output -notmatch [regex]::Escape($ExpectedText)) {
        $failures.Add("${Label}: exit=$($Probe.ExitCode), output=$($Probe.Output.Trim())")
    }
}

function Initialize-TestSourceRepository {
    param([Parameter(Mandatory)][string] $Path)

    New-Item -ItemType Directory -Path (Join-Path $Path 'scripts') -Force | Out-Null
    Set-Content -LiteralPath (Join-Path $Path 'scripts/sync-home.sh') -Value '#!/usr/bin/env bash'
    Set-Content -LiteralPath (Join-Path $Path 'scripts/sync-home.ps1') -Value '#Requires -Version 7'
    & git -C $Path init --quiet
    & git -C $Path remote add origin 'https://example.invalid/home-baseline.git'
}

function Assert-DanglingBackupLinkIsNotFollowed {
    param(
        [Parameter(Mandatory)]
        [ValidateSet('bash', 'pwsh')]
        [string] $Shell
    )

    $workspaceName = "Backup-$Shell"
    $workspacePath = Join-Path $testHome $workspaceName
    $outsideArchive = Join-Path $outside "$workspaceName-outside.tar.gz"
    $backupBase = Join-Path $testHome "$workspaceName-backup-$(Get-Date -Format 'yyyy-MM-dd')"
    $plannedArchive = "$backupBase.tar.gz"
    $collisionArchive = "$backupBase-1.tar.gz"
    New-Item -ItemType Directory -Path $workspacePath | Out-Null
    Set-Content -LiteralPath (Join-Path $workspacePath 'payload.txt') -Value 'temporary test payload'

    try {
        New-Item -ItemType SymbolicLink -Path $plannedArchive -Target $outsideArchive -ErrorAction Stop | Out-Null
    }
    catch {
        Write-Host "SKIP: $Shell dangling backup-link probe unavailable on this platform."
        return
    }

    if ($Shell -eq 'bash') {
        $output = & bash $bashScript $workspaceName --backup --keep-remote --force --yes 2>&1 | Out-String
    }
    else {
        $output = & pwsh -NoProfile -File $powerShellScript `
            -WorkspaceName $workspaceName -Backup -KeepRemote -Force -Yes 2>&1 | Out-String
    }

    if (Test-Path -LiteralPath $outsideArchive) {
        $failures.Add("$Shell followed dangling backup link outside Home: $outsideArchive")
    }
    if (-not (Test-Path -LiteralPath $collisionArchive -PathType Leaf)) {
        $failures.Add("${Shell} did not create collision-safe backup: exit=$LASTEXITCODE, output=$($output.Trim())")
    }
    if (Test-Path -LiteralPath $workspacePath) {
        $failures.Add("$Shell isolated backup probe did not remove temporary workspace: output=$($output.Trim())")
    }
}

try {
    New-Item -ItemType Directory -Path $testHome, $outside | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $testHome 'Valid Workspace') | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $testHome 'home-baseline') | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $testHome 'home-baseline-source') | Out-Null
    $env:HOME = $testHome

    $configuredSource = Join-Path $testHome 'ConfiguredSource'
    Initialize-TestSourceRepository -Path $configuredSource
    $env:HOME_BASELINE_SOURCE = $configuredSource

    foreach ($shell in @('bash', 'pwsh')) {
        foreach ($invalidName in @('../outside', 'nested/child', 'nested\child', '.', '..', $outside)) {
            Assert-Probe -Label "$shell rejects $invalidName" `
                -Probe (Invoke-TeardownProbe -Shell $shell -WorkspaceName $invalidName) `
                -ExpectedExitCode 2 `
                -ExpectedText 'Workspace name must be one direct child directory of Home'
        }

        foreach ($protectedName in @('home-baseline', 'Home-Baseline', 'home-baseline-source', 'HOME-BASELINE-SOURCE')) {
            Assert-Probe -Label "$shell protects $protectedName" `
                -Probe (Invoke-TeardownProbe -Shell $shell -WorkspaceName $protectedName) `
                -ExpectedExitCode 2 `
                -ExpectedText 'Level 0 source is protected'
        }

        Assert-Probe -Label "$shell accepts a direct child" `
            -Probe (Invoke-TeardownProbe -Shell $shell -WorkspaceName 'Valid Workspace') `
            -ExpectedExitCode 0 `
            -ExpectedText 'Valid Workspace'

        Assert-Probe -Label "$shell protects configured Level 0 source" `
            -Probe (Invoke-TeardownProbe -Shell $shell -WorkspaceName 'ConfiguredSource') `
            -ExpectedExitCode 2 `
            -ExpectedText 'Configured Level 0 source is protected'
    }

    $bashAliasOutput = & bash $bashBootstrap --teardown '../outside' --dry-run --keep-remote 2>&1 | Out-String
    Assert-Probe -Label 'bash bootstrap alias preserves path boundary' `
        -Probe ([pscustomobject]@{ ExitCode = $LASTEXITCODE; Output = $bashAliasOutput }) `
        -ExpectedExitCode 2 `
        -ExpectedText 'Workspace name must be one direct child directory of Home'

    $powerShellAliasOutput = & pwsh -NoProfile -File $powerShellBootstrap `
        -Teardown -WorkspaceName '../outside' -WhatIf -KeepRemote 2>&1 | Out-String
    Assert-Probe -Label 'pwsh bootstrap alias preserves path boundary' `
        -Probe ([pscustomobject]@{ ExitCode = $LASTEXITCODE; Output = $powerShellAliasOutput }) `
        -ExpectedExitCode 2 `
        -ExpectedText 'Workspace name must be one direct child directory of Home'

    $bashConfiguredAliasOutput = & bash $bashBootstrap `
        --teardown 'ConfiguredSource' --dry-run --keep-remote 2>&1 | Out-String
    Assert-Probe -Label 'bash bootstrap alias protects configured Level 0 source' `
        -Probe ([pscustomobject]@{ ExitCode = $LASTEXITCODE; Output = $bashConfiguredAliasOutput }) `
        -ExpectedExitCode 2 `
        -ExpectedText 'Configured Level 0 source is protected'

    $powerShellConfiguredAliasOutput = & pwsh -NoProfile -File $powerShellBootstrap `
        -Teardown -WorkspaceName 'ConfiguredSource' -WhatIf -KeepRemote 2>&1 | Out-String
    Assert-Probe -Label 'pwsh bootstrap alias protects configured Level 0 source' `
        -Probe ([pscustomobject]@{ ExitCode = $LASTEXITCODE; Output = $powerShellConfiguredAliasOutput }) `
        -ExpectedExitCode 2 `
        -ExpectedText 'Configured Level 0 source is protected'

    $linkPath = Join-Path $testHome 'LinkedWorkspace'
    try {
        New-Item -ItemType SymbolicLink -Path $linkPath -Target $outside -ErrorAction Stop | Out-Null
        foreach ($shell in @('bash', 'pwsh')) {
            Assert-Probe -Label "$shell rejects symbolic link" `
                -Probe (Invoke-TeardownProbe -Shell $shell -WorkspaceName 'LinkedWorkspace') `
                -ExpectedExitCode 2 `
                -ExpectedText 'links and path escapes are not allowed'
        }
    }
    catch {
        Write-Host 'SKIP: Symlink probe unavailable on this platform.'
    }

    $linkedGitWorkspace = Join-Path $testHome 'LinkedGitWorkspace'
    $externalGitRepository = Join-Path $outside 'ExternalGitRepository'
    New-Item -ItemType Directory -Path $linkedGitWorkspace, $externalGitRepository | Out-Null
    & git -C $externalGitRepository init --quiet
    try {
        New-Item -ItemType SymbolicLink `
            -Path (Join-Path $linkedGitWorkspace '.git') `
            -Target (Join-Path $externalGitRepository '.git') `
            -ErrorAction Stop | Out-Null

        Assert-Probe -Label 'bash rejects linked Git metadata' `
            -Probe (Invoke-TeardownProbe -Shell 'bash' -WorkspaceName 'LinkedGitWorkspace') `
            -ExpectedExitCode 2 `
            -ExpectedText 'links and path escapes are not allowed'
        Assert-Probe -Label 'pwsh rejects linked Git metadata' `
            -Probe (Invoke-TeardownProbe -Shell 'pwsh' -WorkspaceName 'LinkedGitWorkspace') `
            -ExpectedExitCode 2 `
            -ExpectedText 'Git metadata directory must not be a link'
    }
    catch {
        Write-Host 'SKIP: Linked Git metadata probe unavailable on this platform.'
    }

    $recursiveWorkspace = Join-Path $testHome 'RecursiveWorkspace'
    $externalRepository = Join-Path $outside 'ExternalRepo'
    New-Item -ItemType Directory -Path $recursiveWorkspace, (Join-Path $externalRepository '.git') | Out-Null
    try {
        New-Item -ItemType SymbolicLink `
            -Path (Join-Path $recursiveWorkspace 'LinkedRepo') `
            -Target $externalRepository `
            -ErrorAction Stop | Out-Null

        $bashRecursive = & bash $bashScript 'RecursiveWorkspace' --recursive --dry-run --keep-remote 2>&1 | Out-String
        if ($LASTEXITCODE -ne 0 -or $bashRecursive -match [regex]::Escape($externalRepository)) {
            $failures.Add("bash recursive link boundary: exit=$LASTEXITCODE, output=$($bashRecursive.Trim())")
        }

        Assert-Probe -Label 'pwsh rejects linked recursive repository' `
            -Probe (& {
                $output = & pwsh -NoProfile -File $powerShellScript `
                    -WorkspaceName 'RecursiveWorkspace' -Recursive -WhatIf -KeepRemote 2>&1 | Out-String
                [pscustomobject]@{ ExitCode = $LASTEXITCODE; Output = $output }
            }) `
            -ExpectedExitCode 2 `
            -ExpectedText 'links and path escapes are not allowed'
    }
    catch {
        Write-Host 'SKIP: Recursive symlink probe unavailable on this platform.'
    }

    Assert-DanglingBackupLinkIsNotFollowed -Shell 'bash'
    Assert-DanglingBackupLinkIsNotFollowed -Shell 'pwsh'

    if ($failures.Count -gt 0) {
        $failures | ForEach-Object { Write-Error $_ }
        exit 1
    }

    Write-Host 'PASS: teardown workspace path boundary (Bash and PowerShell).'
}
finally {
    $env:HOME = $originalHome
    $env:HOME_BASELINE_SOURCE = $originalHomeBaselineSource
    if (Test-Path -LiteralPath $testRoot) {
        Remove-Item -LiteralPath $testRoot -Recurse -Force
    }
}
