<#
.SYNOPSIS
Validiert den RAW-07-Hardware-Capability-Vertrag ohne Hardware-I/O.

.DESCRIPTION
Fuehrt den dependency-freien Python-Validator ueber PowerShell aus. Der Lauf
entdeckt, verbindet oder steuert kein Geraet. Validates the RAW-07 requirements
contract and one fixture without discovering, connecting, or controlling a
device.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Contract,
    [Parameter(Mandatory)][string]$Fixture
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

& python3 (Join-Path $PSScriptRoot 'validate-hardware-capability-contract.py') --contract $Contract --fixture $Fixture
exit $LASTEXITCODE
