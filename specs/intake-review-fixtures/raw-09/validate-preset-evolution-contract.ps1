<#
.SYNOPSIS
Validiert den RAW-09-Preset-Evolution-Vertrag ohne Preset-Aktion.

.DESCRIPTION
Fuehrt den dependency-freien Python-Validator aus. Der Lauf schreibt oder
promotet kein Preset und fuehrt keine Remote-, Merge-, Bypass-, GitHub- oder
Level-0-Aktion aus. Validates the RAW-09 requirements contract without preset
write, promotion, or downstream action.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Contract,
    [Parameter(Mandatory)][string]$Fixture
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

& python3 (Join-Path $PSScriptRoot 'validate-preset-evolution-contract.py') --contract $Contract --fixture $Fixture
exit $LASTEXITCODE
