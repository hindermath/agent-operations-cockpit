#Requires -Version 7
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string] $WorkspaceName,

    [switch] $Backup,
    [switch] $KeepRemote,
    [switch] $Recursive,
    [switch] $Force,
    [switch] $Yes
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$forgejoLib = Join-Path $PSScriptRoot 'lib/hg-forgejo.ps1'
$sourceResolver = Join-Path $PSScriptRoot 'lib/resolve-home-baseline-source.ps1'
if (Test-Path $forgejoLib) {
    . $forgejoLib
}
if (Test-Path $sourceResolver) {
    . $sourceResolver
}

$script:ExitCode = 0
$script:Results = [System.Collections.Generic.List[object]]::new()
$script:Level2Projects = [System.Collections.Generic.List[string]]::new()
$script:ApprovedRemoteIdentities = @{}
$script:ApprovedGitMarkers = @{}
$script:DryRun = [bool]$WhatIfPreference
$script:HomeDir = ''
$script:WorkspaceDir = ''
$script:NormalizedName = ''
$script:ReadmePath = ''
$script:GitignorePath = ''
$script:GitconfigPath = ''
$script:GitconfigD = ''
$script:IncFile = ''

function Show-Usage {
    @'
Verwendung / Usage:
  teardown-workspace.ps1 -WorkspaceName <Name> [OPTIONEN / OPTIONS]

WorkspaceName:
  Einfacher Name eines echten direkten Home-Unterverzeichnisses /
  Simple name of a real direct Home child directory

Optionen / Options:
  -Backup         Erstellt vor der Löschung ein Backup-Archiv / Create backup archive before deletion
  -KeepRemote     Überspringt das Remote-Repository / Skip remote repository deletion
  -Recursive      Verarbeitet Level-2-Repositories vor dem Workspace / Process Level-2 repositories first
  -Force          Überspringt Sicherheitsprüfungen / Skip safety checks
  -Yes            Überspringt die Rückfrage / Skip confirmation prompt
  -WhatIf         Zeigt alle Aktionen ohne Ausführung / Show all actions without executing
'@
}

function Set-WarningExit {
    if ($script:ExitCode -lt 1) {
        $script:ExitCode = 1
    }
}

function Add-Result([string]$Status, [string]$Message) {
    $script:Results.Add([pscustomobject]@{
        Status  = $Status
        Message = $Message
    })
}

function Set-FileLines([string]$Path, [string[]]$Lines) {
    $encoding = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllLines($Path, $Lines, $encoding)
}

function Show-Box {
    param(
        [string] $Title,
        [string[]] $Lines
    )

    Write-Host '╔════════════════════════════════════════════════════════════════════╗'
    Write-Host ("║ {0,-66} ║" -f "  $Title")
    Write-Host '╠════════════════════════════════════════════════════════════════════╣'
    foreach ($line in $Lines) {
        $text = if ($line.Length -gt 66) { $line.Substring(0, 66) } else { $line }
        Write-Host ("║ {0,-66} ║" -f $text)
    }
    Write-Host '╚════════════════════════════════════════════════════════════════════╝'
}

function ConvertTo-NormalizedName([string]$Name) {
    $Name.ToLower() -replace '[^a-z0-9]', '-' -replace '-+', '-' -replace '^-|-$', ''
}

function Resolve-HomeDirectory {
    $candidate = if ($env:HOME) { $env:HOME } elseif ($env:USERPROFILE) { $env:USERPROFILE } else { '~' }
    (Resolve-Path -LiteralPath $candidate).Path
}

function Assert-ValidWorkspaceName([string]$Name) {
    if ([System.IO.Path]::IsPathFullyQualified($Name) -or
        $Name -in @('.', '..') -or
        $Name.Contains('/') -or
        $Name.Contains('\')) {
        throw 'Fehler: Workspace-Name muss ein einzelnes direktes Unterverzeichnis von Home sein / Error: Workspace name must be one direct child directory of Home'
    }
}

function Test-PathValueEqual([string]$Left, [string]$Right) {
    $comparison = if ($IsWindows) {
        [System.StringComparison]::OrdinalIgnoreCase
    }
    else {
        [System.StringComparison]::Ordinal
    }
    [string]::Equals($Left, $Right, $comparison)
}

function Test-GitMarker([string]$Dir) {
    $gitPath = Join-Path $Dir '.git'
    if ($null -ne (Get-Item -LiteralPath $gitPath -Force -ErrorAction SilentlyContinue)) {
        return $true
    }
    $entries = @(Get-ChildItem -LiteralPath $Dir -Force -Name -ErrorAction Stop)
    if ($IsWindows) { return ($entries -contains '.git') }
    return ($entries -ccontains '.git')
}

function Assert-GitMetadata([string]$Dir) {
    $inside = ((& git -C $Dir rev-parse --is-inside-work-tree 2>$null) | Out-String).Trim()
    if ($LASTEXITCODE -ne 0 -or $inside -cne 'true') {
        throw "Git-Metadaten nicht pruefbar / Git metadata unavailable: $Dir"
    }
    & git -C $Dir config --local --list *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "Git-Konfiguration nicht pruefbar / Git configuration unavailable: $Dir"
    }
}

function Get-OriginForDir([string]$Dir) {
    $remotes = @(& git -C $Dir remote 2>$null)
    if ($LASTEXITCODE -ne 0) {
        throw "Git-Remotes nicht pruefbar / Git remotes unavailable: $Dir"
    }
    if ($remotes -ccontains 'origin') {
        $origin = ((& git -C $Dir remote get-url origin 2>$null) | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or -not $origin) {
            throw "Git-Origin nicht pruefbar / Git origin unavailable: $Dir"
        }
        return $origin
    }
    return ''
}

function Get-OptionalGitConfig([string]$Dir, [string]$Key) {
    $value = ((& git -C $Dir config --local --get $Key 2>$null) | Out-String).Trim()
    if ($LASTEXITCODE -eq 1) { return '' }
    if ($LASTEXITCODE -ne 0) {
        throw "Git-Konfiguration nicht pruefbar / Git configuration unavailable: $Dir"
    }
    return $value
}

function Resolve-SafeDirectChildDirectory {
    param(
        [Parameter(Mandatory)]
        [string] $Path,
        [Parameter(Mandatory)]
        [string] $ExpectedParent,
        [Parameter(Mandatory)]
        [string] $ExpectedName
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw "Fehler: Workspace '$Path' nicht gefunden / Error: Workspace '$Path' not found"
    }

    $item = Get-Item -LiteralPath $Path -Force
    if ($item.LinkType -or (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw 'Fehler: Workspace muss ein echtes direktes Unterverzeichnis sein; Links und Pfadumgehungen sind unzulässig / Error: Workspace must be a real direct child directory; links and path escapes are not allowed'
    }

    $resolved = [System.IO.Path]::GetFullPath($item.FullName)
    $resolvedParent = [System.IO.Path]::GetDirectoryName($resolved)
    $resolvedName = [System.IO.Path]::GetFileName($resolved)
    if (-not (Test-PathValueEqual -Left $resolvedParent -Right $ExpectedParent) -or
        -not (Test-PathValueEqual -Left $resolvedName -Right $ExpectedName)) {
        throw 'Fehler: Workspace muss ein echtes direktes Unterverzeichnis sein; Links und Pfadumgehungen sind unzulässig / Error: Workspace must be a real direct child directory; links and path escapes are not allowed'
    }

    $gitDirectory = Join-Path $resolved '.git'
    $gitItem = Get-Item -LiteralPath $gitDirectory -Force -ErrorAction SilentlyContinue
    if ($null -ne $gitItem) {
        if ($gitItem.LinkType -or
            (($gitItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)) {
            throw 'Fehler: Git-Metadatenverzeichnis darf kein Link sein / Error: Git metadata directory must not be a link'
        }
    }

    $resolved
}

function Initialize-Context {
    $script:HomeDir = Resolve-HomeDirectory
    Assert-ValidWorkspaceName -Name $WorkspaceName
    $candidate = Join-Path $script:HomeDir $WorkspaceName
    $script:NormalizedName = ConvertTo-NormalizedName $WorkspaceName
    $script:ReadmePath = Join-Path $script:HomeDir 'README.md'
    $script:GitignorePath = Join-Path $script:HomeDir '.gitignore'
    $script:GitconfigPath = Join-Path $script:HomeDir '.gitconfig'
    $script:GitconfigD = Join-Path $script:HomeDir '.gitconfig.d'
    $script:IncFile = Join-Path $script:GitconfigD "$($script:NormalizedName).inc"

    if ($WorkspaceName -in @('home-baseline', 'home-baseline-source')) {
        throw 'Fehler: Level-0-Quelle ist geschützt / Error: Level 0 source is protected'
    }

    $script:WorkspaceDir = Resolve-SafeDirectChildDirectory `
        -Path $candidate `
        -ExpectedParent $script:HomeDir `
        -ExpectedName $WorkspaceName

    if (Get-Command Resolve-HBSourceRepository -ErrorAction SilentlyContinue) {
        try {
            $protectedSource = Resolve-HBSourceRepository -StartPath $script:HomeDir -AllowLegacy
            if (Test-PathValueEqual -Left $script:WorkspaceDir -Right $protectedSource) {
                throw 'Fehler: Konfigurierte Level-0-Quelle ist geschützt / Error: Configured Level 0 source is protected'
            }
        }
        catch {
            if ($_.Exception.Message -match 'Configured Level 0 source is protected') {
                throw
            }
        }
    }
}

function Get-Level2Projects {
    $script:Level2Projects.Clear()
    $children = Get-ChildItem -LiteralPath $script:WorkspaceDir -Directory -ErrorAction SilentlyContinue
    foreach ($child in $children) {
        $gitDirectory = Join-Path $child.FullName '.git'
        if (Test-GitMarker $child.FullName) {
            $resolvedChild = Resolve-SafeDirectChildDirectory `
                -Path $child.FullName `
                -ExpectedParent $script:WorkspaceDir `
                -ExpectedName $child.Name
            $gitItem = Get-Item -LiteralPath $gitDirectory -Force
            if ($gitItem.LinkType -or
                (($gitItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)) {
                throw 'Fehler: Level-2-Git-Verzeichnis darf kein Link sein / Error: Level 2 Git directory must not be a link'
            }
            $script:Level2Projects.Add($resolvedChild)
        }
    }
}

function Get-RemotePlatform([string]$Dir) {
    if (-not (Test-GitMarker $Dir)) {
        return 'kein Remote / no remote'
    }
    if ($KeepRemote) {
        return 'bewusst behalten / intentionally kept'
    }

    $approved = $script:ApprovedRemoteIdentities[$Dir]
    if ($approved -eq 'none') { return 'kein Remote / no remote' }
    return $approved.Replace('|', ' ')
}

function Get-ForgejoTargetForDir([string]$Dir) {
    $origin = ((& git -C $Dir remote get-url origin 2>$null) | Out-String).Trim()
    $platform = ((& git -C $Dir config --local --get home-baseline.remote-platform 2>$null) | Out-String).Trim()
    $baseUrl = ((& git -C $Dir config --local --get home-baseline.remote-base-url 2>$null) | Out-String).Trim()
    $owner = ((& git -C $Dir config --local --get home-baseline.remote-owner 2>$null) | Out-String).Trim()
    $repository = ((& git -C $Dir config --local --get home-baseline.remote-repository 2>$null) | Out-String).Trim()
    return Get-ForgejoTargetFromValues $origin $baseUrl $platform $owner $repository
}

function Get-ForgejoTargetFromValues(
    [string]$Origin, [string]$BaseUrl, [string]$Platform,
    [string]$Owner, [string]$Repository
) {
    $pythonCommand = Get-Command python3 -ErrorAction SilentlyContinue
    if (-not $pythonCommand) { $pythonCommand = Get-Command python -ErrorAction SilentlyContinue }
    if (-not $pythonCommand) { return $null }
    $parser = Join-Path $PSScriptRoot 'lib/validate_forgejo_teardown_remote.py'
    $identity = & $pythonCommand.Source $parser $Origin $BaseUrl $Platform $Owner $Repository 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $identity) { return $null }
    return ([string] $identity).Trim()
}

function Initialize-ApprovedRemoteTargets {
    foreach ($dir in @($script:Level2Projects.ToArray()) + @($script:WorkspaceDir)) {
        $script:ApprovedGitMarkers[$dir] = 'none'
        $script:ApprovedRemoteIdentities[$dir] = 'none'
        if (-not (Test-GitMarker $dir)) { continue }
        $script:ApprovedGitMarkers[$dir] = 'git'
        if ($KeepRemote) { continue }
        Assert-GitMetadata $dir
        $origin = Get-OriginForDir $dir
        if (-not $origin) { continue }
        $platform = ((& git -C $dir config --local --get home-baseline.remote-platform 2>$null) | Out-String).Trim()
        if ($platform -in @('forgejo', 'codeberg')) {
            $identity = Get-ForgejoTargetForDir $dir
            if (-not $identity) {
                throw "Forgejo/Codeberg-Ziel stimmt nicht mit origin ueberein / target does not match origin: $dir"
            }
            $script:ApprovedRemoteIdentities[$dir] = "$platform|$identity"
        }
        else {
            $parsed = Get-ParsedRemote $origin
            if ($null -eq $parsed) {
                throw "Remote-Ziel ist ungueltig / remote target is invalid: $dir"
            }
            $script:ApprovedRemoteIdentities[$dir] = "$($parsed.Platform)|$($parsed.OwnerRepo)"
        }
    }
}

function Get-PlannedBackupPath([string]$TargetName) {
    Join-Path $script:HomeDir "$TargetName-backup-$(Get-Date -Format 'yyyy-MM-dd').tar.gz"
}

function Get-UniqueBackupPath([string]$TargetName) {
    $base = Join-Path $script:HomeDir "$TargetName-backup-$(Get-Date -Format 'yyyy-MM-dd')"
    $archivePath = "$base.tar.gz"
    $index = 1

    while ($null -ne (Get-Item -LiteralPath $archivePath -Force -ErrorAction SilentlyContinue)) {
        $archivePath = "$base-$index.tar.gz"
        $index++
    }

    $archivePath
}

function Show-Preamble {
    $title = 'teardown-workspace - Workspace-Entfernung / Workspace Removal'
    if ($script:DryRun) {
        $title = "[DRY-RUN] $title"
    }

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add("  Workspace:   $WorkspaceName")
    $lines.Add("  Pfad / Path: $script:WorkspaceDir")
    $lines.Add('')
    $lines.Add('  Geplante Aktionen / Planned actions:')

    foreach ($project in $script:Level2Projects) {
        $projectName = Split-Path $project -Leaf
        if ($Force) {
            $lines.Add("    L2 ${projectName}: --force überspringt Safety / --force skips safety")
        } else {
            $lines.Add("    L2 ${projectName}: Sicherheitsprüfung / Safety")
        }
        if ($Backup) {
            $lines.Add("      Backup / backup: $(Split-Path (Get-PlannedBackupPath $projectName) -Leaf)")
        }
        $lines.Add("      Remote / remote: $(Get-RemotePlatform $project)")
        $lines.Add('      Lokal löschen / delete local directory')
    }

    if ($Backup) {
        $lines.Add("    1. Backup / backup: $(Split-Path (Get-PlannedBackupPath $WorkspaceName) -Leaf)")
    }

    if ($Force) {
        $lines.Add('    2. --force: Sicherheitsprüfungen übersprungen / safety checks skipped')
    } else {
        $lines.Add('    2. Sicherheitsprüfung / safety check')
    }

    $lines.Add("    3. Remote / remote: $(Get-RemotePlatform $script:WorkspaceDir)")
    $lines.Add('    4. Verzeichnis löschen / delete directory')
    $lines.Add('    5. Artefakte bereinigen / clean up artifacts')
    $lines.Add('       - ~/README.md')
    $lines.Add('       - ~/.gitignore')
    $lines.Add('       - ~/.gitconfig')
    $lines.Add("       - ~/.gitconfig.d/$($script:NormalizedName).inc")

    Show-Box -Title $title -Lines $lines
    foreach ($dir in @($script:Level2Projects.ToArray()) + @($script:WorkspaceDir)) {
        if ($script:ApprovedRemoteIdentities.ContainsKey($dir) -and
            $script:ApprovedRemoteIdentities[$dir] -ne 'none') {
            Write-Host "Remote-Loeschziel / Remote deletion target ($dir): $($script:ApprovedRemoteIdentities[$dir])"
        }
    }
}

function Confirm-OrAbort {
    if ($script:DryRun -or $Yes) {
        return
    }

    $answer = Read-Host 'Fortfahren? / Proceed? [y/N]'
    if ($answer -notmatch '^(?i:y)$') {
        throw 'Abgebrochen / Aborted.'
    }
}

function Test-Safety([string]$Label, [string]$Dir, [switch]$Preflight) {
    if ($Force) {
        if (-not $Preflight) {
            Add-Result 'skip' "Sicherheitsprüfung übersprungen / Safety check skipped: $Label"
        }
        return $true
    }

    $marker = Test-GitMarker $Dir
    if ($script:ApprovedGitMarkers[$Dir] -eq 'git' -and -not $marker) {
        Add-Result 'fail' "Git-Metadaten seit Vorschau entfernt / Git metadata removed after preview: $Label"
        Set-WarningExit
        return $false
    }
    if ($script:ApprovedGitMarkers[$Dir] -eq 'none' -and $marker) {
        Add-Result 'fail' "Git-Metadaten seit Vorschau hinzugefuegt / Git metadata added after preview: $Label"
        Set-WarningExit
        return $false
    }
    if (-not $marker) {
        if (-not $Preflight) {
            Add-Result 'skip' "Kein Git-Repository für Sicherheitsprüfung / No git repository for safety check: $Label"
        }
        return $true
    }

    Assert-GitMetadata $Dir
    $statusOutput = (& git -C $Dir status --porcelain 2>$null)
    if ($LASTEXITCODE -ne 0) {
        Add-Result 'fail' "Git-Status nicht pruefbar / Git status unavailable: $Label"
        Set-WarningExit
        return $false
    }
    if ($statusOutput) {
        Add-Result 'fail' "Uncommittete Änderungen erkannt / Uncommitted changes detected: $Label"
        Set-WarningExit
        return $false
    }

    $stash = @(& git -C $Dir for-each-ref --format='%(refname)' refs/stash 2>$null)
    if ($LASTEXITCODE -ne 0) {
        Add-Result 'fail' "Git-Stash nicht pruefbar / Git stash unavailable: $Label"
        Set-WarningExit
        return $false
    }
    if ($stash.Count -gt 0) {
        Add-Result 'fail' "Git-Stash enthaelt lokale Arbeit / Git stash contains local work: $Label"
        Set-WarningExit
        return $false
    }

    & git -C $Dir symbolic-ref --quiet HEAD *> $null
    if ($LASTEXITCODE -ne 0) {
        Add-Result 'fail' "Git-HEAD ohne pruefbaren Branch / Git HEAD has no verifiable branch: $Label"
        Set-WarningExit
        return $false
    }
    $branchRows = @(& git -C $Dir for-each-ref --format='%(refname)%09%(upstream)' refs/heads 2>$null)
    if ($LASTEXITCODE -ne 0) {
        Add-Result 'fail' "Git-Branches nicht pruefbar / Git branches unavailable: $Label"
        Set-WarningExit
        return $false
    }
    foreach ($row in $branchRows) {
        if (-not $row) { continue }
        $parts = $row -split "`t", 2
        if ($parts.Count -ne 2 -or -not $parts[0].StartsWith('refs/heads/', [StringComparison]::Ordinal)) {
            Add-Result 'fail' "Git-Branch nicht pruefbar / Git branch unavailable: $Label"
            Set-WarningExit
            return $false
        }
        $branchRef = $parts[0]
        $branchName = $branchRef.Substring('refs/heads/'.Length)
        $upstream = $parts[1]
        $remote = Get-OptionalGitConfig $Dir "branch.$branchName.remote"
        if (-not $remote -or $remote -eq '.' -or
            -not $upstream.StartsWith("refs/remotes/$remote/", [StringComparison]::Ordinal)) {
            Add-Result 'fail' "Git-Branch ohne pruefbaren Remote-Upstream / Git branch has no verifiable remote upstream: $Label"
            Set-WarningExit
            return $false
        }
        $remoteUrl = ((& git -C $Dir remote get-url $remote 2>$null) | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or -not $remoteUrl) {
            Add-Result 'fail' "Git-Remote nicht pruefbar / Git remote unavailable: $Label"
            Set-WarningExit
            return $false
        }
        $ahead = ((& git -C $Dir rev-list --count "$upstream..$branchRef" 2>$null) | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or $ahead -notmatch '^0+$') {
            Add-Result 'fail' "Ungepushte Commits erkannt / Unpushed commits detected: $Label"
            Set-WarningExit
            return $false
        }
    }

    if (-not $Preflight) {
        Add-Result 'done' "Sicherheitsprüfung bestanden / Safety check passed: $Label"
    }
    $true
}

function Get-ParsedRemote([string]$RemoteUrl) {
    $pythonCommand = Get-Command python3 -ErrorAction SilentlyContinue
    if (-not $pythonCommand) { $pythonCommand = Get-Command python -ErrorAction SilentlyContinue }
    if (-not $pythonCommand) { return $null }
    $parser = Join-Path $PSScriptRoot 'lib/parse_teardown_remote.py'
    $parsed = & $pythonCommand.Source $parser $RemoteUrl 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $parsed) { return $null }
    $fields = ([string] $parsed).Split("`t")
    if ($fields.Count -ne 2) { return $null }
    return [pscustomobject]@{ Platform = $fields[0]; OwnerRepo = $fields[1] }
}

function Invoke-Backup([string]$Label, [string]$Dir, [string]$TargetName) {
    if (-not $Backup) {
        return $true
    }

    if (-not (Get-Command tar -ErrorAction SilentlyContinue)) {
        Add-Result 'fail' "Backup nicht erstellt, tar fehlt / Backup not created, tar missing: $Label"
        Set-WarningExit
        return $false
    }

    $archivePath = Get-UniqueBackupPath $TargetName
    & tar czf $archivePath -C (Split-Path $Dir -Parent) "./$(Split-Path $Dir -Leaf)" *> $null
    if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $archivePath -PathType Leaf) -and
        (Get-Item -LiteralPath $archivePath).Length -gt 0) {
        Add-Result 'done' "Backup erstellt / Backup created: $(Split-Path $archivePath -Leaf)"
        return $true
    } else {
        Add-Result 'fail' "Backup fehlgeschlagen / Backup failed: $Label"
        Set-WarningExit
        return $false
    }
}

function Remove-RemoteRepo([string]$Label, [string]$Dir) {
    if ($KeepRemote) {
        Add-Result 'skip' "Remote bewusst behalten / Remote intentionally kept: $Label"
        return $true
    }

    if (-not $script:ApprovedRemoteIdentities.ContainsKey($Dir)) {
        Add-Result 'fail' "Remote-Vorschau fehlt / Remote preview is missing: $Label"
        Set-WarningExit
        return $false
    }
    $approved = $script:ApprovedRemoteIdentities[$Dir]

    $marker = Test-GitMarker $Dir
    if ($script:ApprovedGitMarkers[$Dir] -eq 'git' -and -not $marker) {
        Add-Result 'fail' "Git-Metadaten seit Vorschau entfernt / Git metadata removed after preview: $Label"
        Set-WarningExit
        return $false
    }
    if ($script:ApprovedGitMarkers[$Dir] -eq 'none' -and $marker) {
        Add-Result 'fail' "Git-Metadaten seit Vorschau hinzugefuegt / Git metadata added after preview: $Label"
        Set-WarningExit
        return $false
    }
    if (-not $marker) {
        if ($approved -ne 'none') {
            Add-Result 'fail' "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $Label"
            Set-WarningExit
            return $false
        }
        Add-Result 'skip' "Kein Git-Repository, Remote-Schritt übersprungen / No git repository, remote step skipped: $Label"
        return $true
    }

    Assert-GitMetadata $Dir
    $remoteUrl = Get-OriginForDir $Dir
    if ($approved -ne 'none' -and -not $remoteUrl) {
        Add-Result 'fail' "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $Label"
        Set-WarningExit
        return $false
    }
    if (-not $remoteUrl) {
        Add-Result 'skip' "Kein Remote konfiguriert / No remote configured: $Label"
        return $true
    }
    if ($approved -eq 'none') {
        Add-Result 'fail' "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $Label"
        Set-WarningExit
        return $false
    }

    $configuredPlatform = ((& git -C $Dir config --local --get home-baseline.remote-platform 2>$null) | Out-String).Trim()
    if ($configuredPlatform -in @('forgejo', 'codeberg')) {
        if (-not (Test-Path $forgejoLib)) {
            Add-Result 'fail' "Forgejo-Bibliothek fehlt, Remote-Löschung abgebrochen / Forgejo library missing, remote deletion aborted: $Label"
            Set-WarningExit
            return $false
        }
        $baseUrl = ((& git -C $Dir config --local --get home-baseline.remote-base-url 2>$null) | Out-String).Trim()
        $owner = ((& git -C $Dir config --local --get home-baseline.remote-owner 2>$null) | Out-String).Trim()
        $repository = ((& git -C $Dir config --local --get home-baseline.remote-repository 2>$null) | Out-String).Trim()
        if (-not $baseUrl -or -not $owner -or -not $repository) {
            Add-Result 'fail' "Forgejo-Metadaten fehlen, bitte -KeepRemote verwenden / Forgejo metadata missing, use -KeepRemote: $Label"
            Set-WarningExit
            return $false
        }
        $verifiedIdentity = Get-ForgejoTargetFromValues $remoteUrl $baseUrl $configuredPlatform $owner $repository
        if (-not $verifiedIdentity -or
            "$configuredPlatform|$verifiedIdentity" -cne $approved) {
            Add-Result 'fail' "Forgejo/Codeberg-Ziel ungueltig oder seit Vorschau geaendert / target invalid or changed after preview: $Label"
            Set-WarningExit
            return $false
        }
        try {
            Remove-HBForgejoRepository -BaseUrl $baseUrl -Owner $owner -RepositoryName $repository
            Add-Result 'done' "$configuredPlatform-Remote gelöscht / remote deleted: $owner/$repository"
            return $true
        } catch {
            Add-Result 'fail' "$configuredPlatform-Remote konnte nicht gelöscht werden / remote could not be deleted: $owner/$repository"
            Set-WarningExit
            return $false
        }
    }

    $parsed = Get-ParsedRemote $remoteUrl
    if ($null -eq $parsed) {
        Add-Result 'fail' "Unbekanntes oder unsicheres Remote, bitte -KeepRemote verwenden / Unknown or unsafe remote, use -KeepRemote: $Label"
        Set-WarningExit
        return $false
    }
    $ownerRepo = $parsed.OwnerRepo
    if ("$($parsed.Platform)|$ownerRepo" -cne $approved) {
        Add-Result 'fail' "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $Label"
        Set-WarningExit
        return $false
    }
    if ($parsed.Platform -eq 'github') {
        if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
            Add-Result 'fail' "gh fehlt, Remote-Löschung abgebrochen / gh missing, remote deletion aborted: $Label"
            Set-WarningExit
            return $false
        }

        & gh repo delete $ownerRepo --yes *> $null
        if ($LASTEXITCODE -eq 0) {
            Add-Result 'done' "Remote-Repo gelöscht / Remote repo deleted: $ownerRepo"
            return $true
        }

        Add-Result 'fail' "GitHub-Remote konnte nicht gelöscht werden / GitHub remote could not be deleted: $ownerRepo"
        Set-WarningExit
        return $false
    }

    if ($parsed.Platform -eq 'gitlab') {
        if (-not (Get-Command glab -ErrorAction SilentlyContinue)) {
            Add-Result 'skip' "glab fehlt, GitLab-Remote übersprungen / glab missing, GitLab remote skipped: $ownerRepo"
            Set-WarningExit
            return $true
        }

        & glab repo delete $ownerRepo --yes *> $null
        if ($LASTEXITCODE -eq 0) {
            Add-Result 'done' "GitLab-Remote gelöscht / GitLab remote deleted: $ownerRepo"
            return $true
        }

        Add-Result 'fail' "GitLab-Remote konnte nicht gelöscht werden / GitLab remote could not be deleted: $ownerRepo"
        Set-WarningExit
        return $false
    }

    Add-Result 'fail' "Nicht unterstütztes Remote, bitte -KeepRemote verwenden / Unsupported remote, use -KeepRemote: $Label"
    Set-WarningExit
    $false
}

function Remove-LocalDirectory([string]$Label, [string]$Dir) {
    Remove-Item -LiteralPath $Dir -Recurse -Force
    Add-Result 'done' "Verzeichnis gelöscht / Directory deleted: $Label"
}

function Update-TextFile {
    param(
        [string] $Path,
        [scriptblock] $Transform,
        [string] $ChangedMessage,
        [string] $MissingMessage
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Add-Result 'skip' $MissingMessage
        return
    }

    $existing = Get-Content -LiteralPath $Path
    $updated = & $Transform $existing
    if ((@($existing) -join "`n") -eq (@($updated) -join "`n")) {
        Add-Result 'skip' $MissingMessage
        return
    }

    Set-FileLines -Path $Path -Lines @($updated)
    Add-Result 'done' $ChangedMessage
}

function Cleanup-Readme {
    Update-TextFile `
        -Path $script:ReadmePath `
        -Transform {
            param($Lines)
            $Lines | Where-Object { $_ -notmatch [regex]::Escape("~/$WorkspaceName/") }
        } `
        -ChangedMessage 'README.md bereinigt / README.md cleaned up' `
        -MissingMessage 'README.md-Eintrag nicht vorhanden / README.md entry not present'
}

function Cleanup-Gitignore {
    Update-TextFile `
        -Path $script:GitignorePath `
        -Transform {
            param($Lines)
            $Lines | Where-Object { $_ -ne "$WorkspaceName/" }
        } `
        -ChangedMessage '.gitignore bereinigt / .gitignore cleaned up' `
        -MissingMessage '.gitignore-Eintrag nicht vorhanden / .gitignore entry not present'
}

function Cleanup-Gitconfig {
    if (-not (Test-Path -LiteralPath $script:GitconfigPath -PathType Leaf)) {
        Add-Result 'skip' '.gitconfig fehlt / .gitconfig missing'
        return
    }

    $header1 = "[includeIf `"gitdir:~/$WorkspaceName/`"]"
    $header2 = "[includeIf `"gitdir:$script:WorkspaceDir/`"]"
    $lines = Get-Content -LiteralPath $script:GitconfigPath
    $updated = [System.Collections.Generic.List[string]]::new()
    $skip = $false

    foreach ($line in $lines) {
        if ($line -eq $header1 -or $line -eq $header2) {
            $skip = $true
            continue
        }
        if ($skip -and $line -match '^\s') {
            continue
        }
        $skip = $false
        $updated.Add($line)
    }

    if ((@($lines) -join "`n") -eq (@($updated) -join "`n")) {
        Add-Result 'skip' '.gitconfig includeIf-Block nicht vorhanden / .gitconfig includeIf block not present'
        return
    }

    Set-FileLines -Path $script:GitconfigPath -Lines @($updated)
    Add-Result 'done' '.gitconfig bereinigt / .gitconfig cleaned up'
}

function Cleanup-IncludeFile {
    if (-not (Test-Path -LiteralPath $script:GitconfigD -PathType Container)) {
        Add-Result 'skip' '~/.gitconfig.d fehlt / ~/.gitconfig.d missing'
        return
    }

    if (-not (Test-Path -LiteralPath $script:IncFile -PathType Leaf)) {
        Add-Result 'skip' ".inc-Datei nicht vorhanden / .inc file not present: $($script:NormalizedName).inc"
        return
    }

    Remove-Item -LiteralPath $script:IncFile -Force
    Add-Result 'done' ".inc-Datei gelöscht / .inc file deleted: $($script:NormalizedName).inc"
}

function Commit-Artifacts {
    $insideWorkTree = (& git -C $script:HomeDir rev-parse --is-inside-work-tree 2>$null | Out-String).Trim()
    if (-not $insideWorkTree) {
        Add-Result 'skip' 'Artefakt-Commit übersprungen, ~/ ist kein Git-Repo / Artifact commit skipped, ~/ is not a git repo'
        Set-WarningExit
        return
    }

    $artifactPaths = @()
    if (Test-Path -LiteralPath $script:ReadmePath -PathType Leaf) {
        $artifactPaths += 'README.md'
        & git -C $script:HomeDir add --update -- README.md *> $null
        if ($LASTEXITCODE -ne 0) {
            Add-Result 'fail' 'README-Commit-Vorbereitung fehlgeschlagen / README commit preparation failed'
            Set-WarningExit
            return
        }
    }
    if (Test-Path -LiteralPath $script:GitignorePath -PathType Leaf) {
        $artifactPaths += '.gitignore'
        & git -C $script:HomeDir add --update -- .gitignore *> $null
        if ($LASTEXITCODE -ne 0) {
            Add-Result 'fail' 'Gitignore-Commit-Vorbereitung fehlgeschlagen / gitignore commit preparation failed'
            Set-WarningExit
            return
        }
    }

    & git -C $script:HomeDir diff --cached --quiet -- README.md .gitignore *> $null
    if ($LASTEXITCODE -eq 0) {
        Add-Result 'skip' 'Kein Artefakt-Commit nötig / No artifact commit needed'
        return
    }

    $subject = "chore: teardown $WorkspaceName - Artefakte bereinigt / artifacts cleaned up"
    & git -C $script:HomeDir commit --only -m $subject -m 'Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>' -- @artifactPaths *> $null
    if ($LASTEXITCODE -eq 0) {
        Add-Result 'done' 'Artefakte committed / Artifacts committed'
    } else {
        Add-Result 'fail' 'Artefakt-Commit fehlgeschlagen / Artifact commit failed'
        Set-WarningExit
    }
}

function Test-HomeArtifactsClean {
    $insideWorkTree = (& git -C $script:HomeDir rev-parse --is-inside-work-tree 2>$null | Out-String).Trim()
    if ($LASTEXITCODE -ne 0 -or $insideWorkTree -cne 'true') {
        if (Test-GitMarker $script:HomeDir) {
            Add-Result 'fail' 'Home-Git-Metadaten nicht pruefbar / Home Git metadata unavailable'
            Set-WarningExit
            return $false
        }
        return $true
    }
    $status = & git -C $script:HomeDir status --porcelain -- README.md .gitignore 2>$null
    if ($LASTEXITCODE -ne 0) {
        Add-Result 'fail' 'Home-Artefaktstatus nicht pruefbar / Home artifact status unavailable'
        Set-WarningExit
        return $false
    }
    if ($status) {
        Add-Result 'fail' 'Vorhandene Home-Artefaktaenderungen blockieren Teardown / Existing Home artifact changes block teardown'
        Set-WarningExit
        return $false
    }
    return $true
}

function Cleanup-WorkspaceArtifacts {
    Cleanup-Readme
    Cleanup-Gitignore
    Cleanup-Gitconfig
    Cleanup-IncludeFile
    Commit-Artifacts
}

function Invoke-TargetTeardown {
    param(
        [string] $Label,
        [string] $Dir,
        [string] $BackupName,
        [switch] $IncludeArtifacts
    )

    $expectedParent = if ($IncludeArtifacts) { $script:HomeDir } else { $script:WorkspaceDir }
    $Dir = Resolve-SafeDirectChildDirectory `
        -Path $Dir `
        -ExpectedParent $expectedParent `
        -ExpectedName $BackupName

    if (-not (Invoke-Backup -Label $Label -Dir $Dir -TargetName $BackupName)) {
        return $false
    }

    if (-not (Test-Safety -Label $Label -Dir $Dir)) {
        return $false
    }

    $Dir = Resolve-SafeDirectChildDirectory `
        -Path $Dir `
        -ExpectedParent $expectedParent `
        -ExpectedName $BackupName

    if (-not (Remove-RemoteRepo -Label $Label -Dir $Dir)) {
        return $false
    }

    $Dir = Resolve-SafeDirectChildDirectory `
        -Path $Dir `
        -ExpectedParent $expectedParent `
        -ExpectedName $BackupName

    Remove-LocalDirectory -Label $Label -Dir $Dir

    if ($IncludeArtifacts) {
        Cleanup-WorkspaceArtifacts
    }

    $true
}

function Show-Level2Abort {
    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add('Level-2-Repositories erkannt / Level-2 repositories detected:')
    foreach ($project in $script:Level2Projects) {
        $lines.Add("  - $(Split-Path $project -Leaf)")
    }
    $lines.Add('')
    $lines.Add('-Recursive erforderlich / -Recursive required')
    Show-Box -Title 'Teardown abgebrochen / Teardown aborted' -Lines $lines
}

function Show-CompletionReport {
    $lines = [System.Collections.Generic.List[string]]::new()
    foreach ($result in $script:Results) {
        $symbol = switch ($result.Status) {
            'done' { '✓' }
            'skip' { '→' }
            'fail' { '✗' }
            default { '•' }
        }
        $lines.Add("  $symbol $($result.Message)")
    }
    Show-Box -Title 'Teardown abgeschlossen / Teardown complete' -Lines $lines
}

try {
    Initialize-Context
    Get-Level2Projects

    if ($script:Level2Projects.Count -gt 0 -and -not $Recursive) {
        Show-Level2Abort
        exit 1
    }

    Initialize-ApprovedRemoteTargets

    Show-Preamble

    if ($script:DryRun) {
        exit 0
    }

    Confirm-OrAbort

    if (-not (Test-HomeArtifactsClean)) {
        Show-CompletionReport
        exit $script:ExitCode
    }

    foreach ($project in $script:Level2Projects) {
        $projectName = Split-Path $project -Leaf
        if (-not (Test-Safety -Label "Level-2 $projectName" -Dir $project -Preflight)) {
            Show-CompletionReport
            exit $script:ExitCode
        }
    }
    if (-not (Test-Safety -Label "Workspace $WorkspaceName" -Dir $script:WorkspaceDir -Preflight)) {
        Show-CompletionReport
        exit $script:ExitCode
    }

    foreach ($project in $script:Level2Projects) {
        $projectName = Split-Path $project -Leaf
        if (-not (Invoke-TargetTeardown -Label "Level-2 $projectName" -Dir $project -BackupName $projectName)) {
            Show-CompletionReport
            exit $script:ExitCode
        }
    }

    if (-not (Invoke-TargetTeardown -Label "Workspace $WorkspaceName" -Dir $script:WorkspaceDir -BackupName $WorkspaceName -IncludeArtifacts)) {
        Show-CompletionReport
        exit $script:ExitCode
    }

    Show-CompletionReport
    exit $script:ExitCode
}
catch {
    $message = $_.Exception.Message
    if ($message -eq 'Abgebrochen / Aborted.') {
        Write-Host $message
        exit 1
    }
    [Console]::Error.WriteLine($message)
    exit 2
}
