<#
.SYNOPSIS
Prueft den additiven META-LH-03-Authoring-Vertrag.

Validates the additive META-LH-03 authoring contract.
.PARAMETER Repo
Repository-Wurzel. / Repository root.
.PARAMETER Json
Gibt maschinenlesbares JSON aus. / Emits machine-readable JSON.
.EXAMPLE
pwsh -NoProfile -File validate-authoring-contract.ps1 -Repo . -Json
#>
[CmdletBinding()]
param(
    [string]$Repo = '.',
    [switch]$Json,
    [switch]$Unknown
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($Unknown) {
    [Console]::Error.WriteLine('Unbekannte Option / unknown option: -Unknown')
    exit 64
}

$Core = Join-Path $PSScriptRoot 'validate_authoring_contract.py'
$Arguments = @('-B', $Core, '--repo', $Repo)
if ($Json) { $Arguments += '--json' }
& python3 @Arguments
$CoreExit = $LASTEXITCODE
exit $CoreExit
