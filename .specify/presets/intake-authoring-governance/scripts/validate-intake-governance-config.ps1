<#
.SYNOPSIS
Prueft die sprachbewusste Requirements-Intake-Konfiguration.

Validates the language-aware requirements intake configuration.

.PARAMETER Config
Repository-relativer oder absoluter Konfigurationspfad.

Repository-relative or absolute configuration path.

.PARAMETER Journal
Repository-relativer oder absoluter Migrationsjournalpfad.

Repository-relative or absolute migration-journal path.

.PARAMETER Repo
Repository-Wurzel zur Aufloesung konfigurierter Pfade.

Repository root used to resolve configured paths.

.PARAMETER Json
Gibt maschinenlesbares JSON aus.

Returns machine-readable JSON.
.EXAMPLE
pwsh -NoProfile -File scripts/validate-intake-governance-config.ps1 -Config requirements/intake-governance.json -Repo . -Json
#>
[CmdletBinding(DefaultParameterSetName = 'Config')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Config')]
    [string]$Config,
    [Parameter(Mandatory, ParameterSetName = 'Journal')]
    [string]$Journal,
    [string]$Repo = '.',
    [switch]$Json
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScriptDirectory = Split-Path -Parent $PSCommandPath
$Arguments = @()
if ($PSCmdlet.ParameterSetName -eq 'Config') {
    $Arguments += @('--config', $Config)
} else {
    $Arguments += @('--journal', $Journal)
}
$Arguments += @('--repo', $Repo)
if ($Json) {
    $Arguments += '--json'
}
& python3 (Join-Path $ScriptDirectory 'validate-intake-governance-config.py') @Arguments
exit $LASTEXITCODE
