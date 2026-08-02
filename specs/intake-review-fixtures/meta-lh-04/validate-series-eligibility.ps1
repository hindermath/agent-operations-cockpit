param(
    [Parameter(Mandatory = $true)]
    [string]$Fixture
)

$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $PSCommandPath
$repoDir = (Resolve-Path (Join-Path $scriptDir '../../..')).Path
$python = Get-Command python3 -ErrorAction SilentlyContinue
if ($null -eq $python) {
    $python = Get-Command python -ErrorAction Stop
}
& $python.Source (Join-Path $scriptDir 'validate-series-eligibility.py') `
    --contract (Join-Path $repoDir 'requirements/baseline/series-eligibility-contract.json') `
    --fixture $Fixture
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
