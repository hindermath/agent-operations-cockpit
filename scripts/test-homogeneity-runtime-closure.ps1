#Requires -Version 7
<#
.SYNOPSIS
Prueft den Fail-closed-Vertrag des Homogeneity-Hilfspakets.

.DESCRIPTION
Erzeugt eine absichtlich unvollstaendige temporaere Installation und erwartet
Exitcode 2. Danach wird das vollstaendige Paket gegen ein Repository geprueft.

Validates the Homogeneity helper package with an intentionally incomplete
temporary installation and then with the complete repository-owned package.

.PARAMETER RepoRoot
Expliziter Repository-Root fuer den vollstaendigen Dry-Run.

.EXAMPLE
pwsh -NoProfile -File scripts/test-homogeneity-runtime-closure.ps1 -RepoRoot .
#>
[CmdletBinding()]
param(
    [string]$RepoRoot = (Split-Path $PSScriptRoot -Parent)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path -LiteralPath $RepoRoot).Path
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("homogeneity-runtime-{0}" -f [guid]::NewGuid())

try {
    $tempScripts = Join-Path $tempRoot 'scripts'
    $tempLib = Join-Path $tempScripts 'lib'
    New-Item -ItemType Directory -Path $tempLib -Force | Out-Null
    Copy-Item (Join-Path $PSScriptRoot 'check-homogeneity.ps1') $tempScripts
    Copy-Item (Join-Path $PSScriptRoot 'lib/hg-stats.ps1') $tempLib

    $partialScript = Join-Path $tempScripts 'check-homogeneity.ps1'
    $partialOutput = & pwsh -NoProfile -File $partialScript -TargetDir $repo -DryRun -NoPatch 2>&1
    $partialExit = $LASTEXITCODE
    if ($partialExit -ne 2) {
        throw "Incomplete helper package returned exit $partialExit instead of 2."
    }
    if (($partialOutput | Out-String) -notmatch 'incomplete helper package') {
        throw 'The incomplete helper package did not produce an explicit diagnostic.'
    }

    $completeScript = Join-Path $PSScriptRoot 'check-homogeneity.ps1'
    $completeOutput = & pwsh -NoProfile -File $completeScript -TargetDir $repo -DryRun -NoPatch 2>&1
    $completeExit = $LASTEXITCODE
    if ($completeExit -eq 2) {
        throw "Complete helper package was rejected as fatal:`n$($completeOutput | Out-String)"
    }
    if (($completeOutput | Out-String) -match 'CommandNotFoundException|incomplete helper package') {
        throw 'Complete run contains a helper-package error.'
    }

    Write-Host 'PASS: Homogeneity-Runtime-Abschluss (PowerShell) ist fail-closed und vollstaendig.'
}
finally {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
}
