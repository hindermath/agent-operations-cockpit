[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Contract,
    [Parameter(Mandatory = $true)][string]$Fixture
)

$ErrorActionPreference = 'Stop'
$scriptDirectory = Split-Path -Parent $PSCommandPath
$arguments = @(
    (Join-Path $scriptDirectory 'validate-presentation-contract.py'),
    '--contract',
    $Contract,
    '--fixture',
    $Fixture
)
$python = Get-Command python3 -ErrorAction SilentlyContinue
if ($null -eq $python) {
    $python = Get-Command python -ErrorAction Stop
}
& $python.Source @arguments
exit $LASTEXITCODE
