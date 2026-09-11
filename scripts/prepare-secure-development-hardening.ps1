<#
.SYNOPSIS
Bereitet MSL-basierte Level-2-Repositories fuer spaetere Secure-Development-Haertung vor.

Prepares MSL-based level-2 repositories for later secure-development hardening runs.

.DESCRIPTION
Dieses Skript findet Level-2-Repositories unter dem Home-Verzeichnis, prueft die
Primaersprache gegen die MSL-Allowlist, synchronisiert bei MSL-Repositories
`docs/secure-development/`, erzeugt ein Intake-Lastenheft und pflegt die
sichtbare Reihenfolge der `Lastenheft*.md`-Dateien.

Bei einem eindeutigen kanonischen Series-Manifest rendert es den exakten
Fuenf-Spalten-Vertrag mit den Feldern
Position, Status, vollstaendig verlinkter Intake-Dateiname, direkte eingehende
Abhaengigkeiten und Spec-Kit-Feature. Ein Feature-Link benoetigt genau eine
ausdrueckliche Bindung; sonst erscheint der exakte zweisprachige Fallback.
`-WhatIf` prueft denselben Vertrag ohne Zielwrites.

Es startet keinen Spec-Kit-Lauf, erzeugt keine Feature-Branches und befuellt
keine projektspezifischen `docs/security/`-Nachweise.

This script discovers level-2 repositories below the home directory, checks the
primary language against the MSL allow-list, synchronizes `docs/secure-development/`
for MSL repositories, creates an intake requirements document, and maintains the
visible order of `Lastenheft*.md` files.

With one unambiguous canonical series manifest, it renders the exact five-column
contract: position, status, linked complete intake filename, direct incoming
dependencies, and Spec Kit feature. A feature link requires exactly one explicit binding;
otherwise the exact bilingual fallback is rendered. `-WhatIf` checks the same
contract without target writes. Write mode rechecks the complete consumed input
set and rejects generated outputs that overlap canonical inputs.

It does not start a Spec Kit run, does not create feature branches, and does not
populate project-specific `docs/security/` evidence files.

.PARAMETER HomeDir
Home-Verzeichnis, unter dem Level-1- und Level-2-Repositories gesucht werden.

Home directory below which level-1 and level-2 repositories are discovered.

.PARAMETER Repo
Explizite Level-2-Repositories, die vorbereitet werden sollen. Kann mehrfach
oder als Array uebergeben werden.

Explicit level-2 repositories to prepare. Can be passed multiple times or as an
array.

.PARAMETER PrimaryLanguage
Explizite Primaersprache, wenn Auto-Erkennung aus Constitution oder Dateien
nicht ausreichend ist.

Explicit primary language when auto-detection from constitution or files is not
sufficient.

.PARAMETER OrderOnly
Fuehrt nur die begrenzte Intake-Reihenfolgeprojektion aus. Erfordert genau ein
explizites Repo und Manifest; Secure-Development-Templates, Commit und Push
bleiben ausgeschlossen.

Runs only the bounded intake-order projection. Requires exactly one explicit
repository and manifest; secure-development templates, commit, and push remain
excluded.

.PARAMETER Manifest
Kanonischer Manifestpfad relativ zum expliziten Repository fuer `-OrderOnly`.

Canonical manifest path relative to the explicit repository for `-OrderOnly`.

.PARAMETER OrderOutput
Owned Ausgabepfad relativ zum Repository; fuer atomare Multi-Output-Publikation
wiederholbar beziehungsweise als Array uebergebbar.

Owned repository-relative output path; repeat or pass an array for atomic
multi-output publication.

.PARAMETER Commit
Commitet geaenderte Dateien pro Repository.

Commits changed files per repository.

.PARAMETER Push
Pusht den aktuellen Branch nach dem Commit. Aktiviert Commit automatisch.

Pushes the current branch after the commit. Implies Commit.

.PARAMETER AllowDirty
Erlaubt vorhandene lokale Aenderungen in Ziel-Repositories.

Allows existing local changes in target repositories.

.PARAMETER Help
Zeigt die vollstaendige zweisprachige Hilfe und beendet das Skript ohne Writes.

Shows the complete bilingual help and exits without writes.

.EXAMPLE
pwsh scripts/prepare-secure-development-hardening.ps1 -WhatIf

.EXAMPLE
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo /path/to/workspace/TuiVision -WhatIf

.EXAMPLE
pwsh scripts/prepare-secure-development-hardening.ps1 -HomeDir /path/to/home -Commit -Push

.EXAMPLE
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo . -OrderOnly -Manifest requirements/intakes/series/home-baseline-delivery/manifest.json -WhatIf
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$HomeDir = $(if ($env:HOME) { $env:HOME } else { $env:USERPROFILE }),
    [string[]]$Repo = @(),
    [string]$PrimaryLanguage = '',
    [switch]$OrderOnly,
    [string]$Manifest = '',
    [string[]]$OrderOutput = @(),
    [switch]$Commit,
    [switch]$Push,
    [switch]$AllowDirty,
    [switch]$Help
)

try {
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($Help) {
    $helpText = Get-Help -Name $MyInvocation.MyCommand.Path -Full | Out-String -Width 120
    $helpText = $helpText.Replace(
        $MyInvocation.MyCommand.Path,
        'scripts/prepare-secure-development-hardening.ps1',
        [StringComparison]::Ordinal
    )
    [Console]::Out.Write($helpText)
    return
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LibFile = Join-Path $ScriptDir 'lib/secure-development-hardening.ps1'
if (-not (Test-Path $LibFile)) {
    throw "Hilfsbibliothek nicht gefunden / helper library not found: $LibFile"
}
. $LibFile

if ($Push) { $Commit = $true }

if ($OrderOnly) {
    $explicitOrderRepos = @(
        $Repo |
            ForEach-Object { $_ -split ',' } |
            ForEach-Object { $_.Trim() } |
            Where-Object { $_ }
    )
    if ($explicitOrderRepos.Count -ne 1) { throw '-OrderOnly erfordert genau ein explizites -Repo.' }
    if ([string]::IsNullOrWhiteSpace($Manifest)) { throw '-OrderOnly erfordert -Manifest.' }
    if ($Commit -or $Push) { throw '-OrderOnly erlaubt weder -Commit noch -Push.' }
    if ($PrimaryLanguage) { throw '-OrderOnly verwendet keine -PrimaryLanguage.' }
    $orderRepo = $explicitOrderRepos[0]
    if (-not (Test-Path -LiteralPath (Join-Path $orderRepo '.git') -PathType Container)) { throw '-Repo ist kein Git-Repository.' }
    if (-not $WhatIfPreference -and -not $AllowDirty) {
        $orderStatus = ((git -C $orderRepo status --short) | Out-String).Trim()
        if ($orderStatus) { throw "Repo hat lokale Aenderungen; fuer einen begrenzten Write explizit -AllowDirty verwenden: ${orderRepo}" }
    }
    $outputs = if ($OrderOutput.Count -gt 0) { @($OrderOutput) } else { @('Lastenheft_Abarbeitungsreihenfolge.md') }
    $mode = if ($WhatIfPreference) { 'Check' } else { 'Write' }
    $projectionResult = Invoke-SdhLinkedIntakeProjection -Repo $orderRepo -ManifestPath $Manifest -Mode $mode -OutputPaths $outputs
    Write-Host "Intake-Projektion / intake projection: $projectionResult"
    return
}
if ($Manifest -or $OrderOutput.Count -gt 0) {
    throw '-Manifest und -OrderOutput sind nur mit -OrderOnly erlaubt.'
}

function Test-Level2Repo {
    param([string]$Repo)
    if (-not (Test-Path (Join-Path $Repo '.git'))) { return $false }
    if (Test-Path (Join-Path $Repo '.specify')) { return $true }
    if (Test-Path (Join-Path $Repo 'AGENTS.md')) { return $true }
    if (Test-Path (Join-Path $Repo 'CLAUDE.md')) { return $true }
    return $false
}

function Get-Level2Repos {
    param([string]$Root)
    $repos = [System.Collections.Generic.List[string]]::new()
    Get-ChildItem -Path $Root -Directory -ErrorAction SilentlyContinue | ForEach-Object {
        $workspace = $_.FullName
        if (-not (Test-Path (Join-Path $workspace '.git'))) { return }
        Get-ChildItem -Path $workspace -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            if (Test-Level2Repo $_.FullName) {
                $repos.Add($_.FullName)
            }
        }
    }
    return $repos
}

function Invoke-CommitAndPush {
    param([string]$Repo)

    if (-not $Commit -and -not $Push) { return }

    if ($WhatIfPreference) {
        if ($Commit) { Write-Host '  [WhatIf] git add docs/secure-development Lastenheft_Secure-Development-Hardening.md Lastenheft_Abarbeitungsreihenfolge.md && git commit' }
        if ($Push) { Write-Host '  [WhatIf] git push origin <branch>' }
        return
    }

    git -C $Repo add docs/secure-development Lastenheft_Secure-Development-Hardening.md Lastenheft_Abarbeitungsreihenfolge.md
    git -C $Repo diff --cached --check
    if ($LASTEXITCODE -ne 0) { throw "git diff --cached --check fehlgeschlagen in $Repo" }

    git -C $Repo diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
        git -C $Repo commit -m 'docs: prepare secure development hardening'
        if ($LASTEXITCODE -ne 0) { throw "git commit fehlgeschlagen in $Repo" }
    }

    if ($Push) {
        $branch = ((git -C $Repo branch --show-current) | Out-String).Trim()
        if (-not $branch) { throw "Kein aktueller Branch in $Repo" }
        git -C $Repo push origin $branch
        if ($LASTEXITCODE -ne 0) { throw "git push fehlgeschlagen in $Repo" }
    }
}

function Invoke-PrepareRepo {
    param([string]$Repo)

    $projectName = Split-Path -Leaf $Repo
    Write-Host "## $Repo"

    if (-not $WhatIfPreference -and -not $AllowDirty) {
        $status = ((git -C $Repo status --short) | Out-String).Trim()
        if ($status) {
            throw "Repo hat lokale Aenderungen: $Repo"
        }
    }

    $ok = Invoke-SdhPrepareRepo `
        -Repo $Repo `
        -ProjectName $projectName `
        -PrimaryLanguage $PrimaryLanguage `
        -ScriptDir $ScriptDir `
        -WhatIfMode:$WhatIfPreference

    if (-not $ok) {
        throw $script:SdhPrepareReason
    }

    switch ($script:SdhPrepareResult) {
        'prepared' {
            Write-Host "  vorbereitet: $script:SdhPrepareReason"
            Invoke-CommitAndPush -Repo $Repo
        }
        'skipped' {
            Write-Host "  uebersprungen: $script:SdhPrepareReason"
        }
        default {
            Write-Host "  Status: $script:SdhPrepareResult $script:SdhPrepareReason"
        }
    }
}

if ($Repo.Count -gt 0) {
    $explicitRepos = @(
        $Repo |
            ForEach-Object { $_ -split ',' } |
            ForEach-Object { $_.Trim() } |
            Where-Object { $_ }
    )
    $repos = @($explicitRepos | Where-Object { Test-Level2Repo $_ } | Select-Object -Unique)
} else {
    $repos = @(Get-Level2Repos -Root $HomeDir)
}

Write-Host 'Secure-Development-Hardening Vorbereitung'
Write-Host "  Home             : $HomeDir"
if ($Repo.Count -gt 0) { Write-Host "  Repos            : $($repos.Count) explizit" }
Write-Host "  Primaersprache   : $(if ($PrimaryLanguage) { $PrimaryLanguage } else { 'auto' })"
Write-Host "  Commit           : $Commit"
Write-Host "  Push             : $Push"
Write-Host "  WhatIf           : $WhatIfPreference"
Write-Host ''

if ($repos.Count -eq 0) {
    throw 'Keine Level-2-Repos gefunden'
}

foreach ($repo in $repos) {
    Invoke-PrepareRepo -Repo $repo
}

Write-Host ''
Write-Host 'Secure-Development-Hardening Vorbereitung abgeschlossen.'
}
catch {
    # A top-level ErrorRecord includes source and stack context. Public CLI
    # diagnostics need only the stable, bounded message and must not echo a
    # private repository root or credential-shaped argument.
    if (Get-Command ConvertTo-SdhPublicDiagnostic -CommandType Function -ErrorAction SilentlyContinue) {
        $safeMessage = ConvertTo-SdhPublicDiagnostic `
            -Message ([string]$_.Exception.Message) `
            -PrivatePath (@($HomeDir) + @($Repo))
    } else {
        $safeMessage = [regex]::Replace(
            [string]$_.Exception.Message,
            '[\x00-\x1f\x7f]',
            '?'
        )
        $safeMessage = [regex]::Replace($safeMessage, '(?i)(?:/Users/|/home/)[^\s:;,]+', '[private-path]')
    }
    [Console]::Error.WriteLine($safeMessage)
    exit 1
}
