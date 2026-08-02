[CmdletBinding(DefaultParameterSetName = 'Fixture')]
param(
    [Parameter(Mandatory = $true)][string]$Contract,
    [Parameter(Mandatory = $true, ParameterSetName = 'Fixture')][string]$Fixture,
    [Parameter(Mandatory = $true, ParameterSetName = 'Repository')][string]$Repo
)

$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $PSCommandPath
$arguments = @((Join-Path $scriptDir 'validate-first-wave.py'), '--contract', $Contract)
if ($PSCmdlet.ParameterSetName -eq 'Fixture') {
    $arguments += @('--fixture', $Fixture)
}
else {
    $arguments += @('--repo', $Repo)
}
$python = Get-Command python3 -ErrorAction SilentlyContinue
if ($null -eq $python) {
    $python = Get-Command python -ErrorAction Stop
}
& $python.Source @arguments
exit $LASTEXITCODE
