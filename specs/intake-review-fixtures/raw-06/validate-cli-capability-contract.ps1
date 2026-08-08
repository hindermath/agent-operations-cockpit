<#
.SYNOPSIS
Validiert den RAW-06-CLI-Capability-Vertrag und eine Evidence-Fixture.

.DESCRIPTION
Fuehrt den dependency-freien Python-Validator ueber PowerShell aus. Der Lauf
startet keine Prozesse ausser dem lokalen Validator und oeffnet keine
Remote-Verbindung. Validates the RAW-06 requirements contract and one fixture
without executing a product command or opening a remote connection.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Contract,
    [Parameter(Mandatory)][string]$Fixture
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

& python3 (Join-Path $PSScriptRoot 'validate-cli-capability-contract.py') --contract $Contract --fixture $Fixture
exit $LASTEXITCODE
