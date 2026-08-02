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
& python3 @arguments
exit $LASTEXITCODE
