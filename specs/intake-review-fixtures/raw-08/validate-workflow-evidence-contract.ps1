<#
.SYNOPSIS
Validiert den RAW-08-Workflow-Evidence-Vertrag ohne Produktaktionen.

.DESCRIPTION
Fuehrt den dependency-freien Python-Validator ueber PowerShell aus. Der Lauf
startet keinen Prozess, schreibt keine Evidence und fuehrt keine Remote-,
Merge-, Bypass-, Preset- oder Level-0-Aktion aus. Validates the RAW-08
requirements contract without starting a process, writing evidence, or
performing downstream actions.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Contract,
    [Parameter(Mandatory)][string]$Fixture
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

& python3 (Join-Path $PSScriptRoot 'validate-workflow-evidence-contract.py') --contract $Contract --fixture $Fixture
exit $LASTEXITCODE
