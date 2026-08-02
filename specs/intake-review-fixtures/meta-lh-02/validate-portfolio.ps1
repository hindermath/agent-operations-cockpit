<#
.SYNOPSIS
Runs the portable META-LH-02 portfolio validator from PowerShell.
#>
[CmdletBinding(DefaultParameterSetName = 'Contract')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Contract')][string]$Contract,
    [Parameter(Mandatory, ParameterSetName = 'Contract')][string]$Markdown,
    [Parameter(Mandatory, ParameterSetName = 'Fixture')][string]$Fixture
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$Validator = Join-Path $PSScriptRoot 'validate-portfolio.py'
$ValidatorArguments = if ($PSCmdlet.ParameterSetName -eq 'Fixture') {
    @('--fixture', $Fixture)
}
else {
    @('--contract', $Contract, '--markdown', $Markdown)
}
$Python = Get-Command python3 -ErrorAction SilentlyContinue
if ($null -eq $Python) {
    $Python = Get-Command python -ErrorAction Stop
}
& $Python.Source $Validator @ValidatorArguments
exit $LASTEXITCODE
