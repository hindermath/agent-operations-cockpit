#Requires -Version 7.0
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string] $Source,
    [Parameter(Mandatory)][string] $Destination
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# The shipped entry point always rejects execution. Deterministic tests run a
# disposable copy with only that exact guard removed; no runtime bypass exists.
$guard = @'
if ($Action -in @('Start', 'Resume', 'Consolidate')) {
    throw 'Produktive Parallel-Kampagnen sind bis zur isolierten Worker-Laufzeit gesperrt. / Production parallel campaigns are suspended until workers are isolated.'
}
'@
$sourceText = [IO.File]::ReadAllText([IO.Path]::GetFullPath($Source))
if ($sourceText.Split($guard).Count -ne 2) {
    throw 'The production suspension guard is missing or ambiguous.'
}
$scriptDirectory = (Split-Path -Parent ([IO.Path]::GetFullPath($Source))).Replace("'", "''")
$fixtureText = $sourceText.Replace($guard, '# Deterministic fixture execution only.')
$fixtureText = $fixtureText.Replace('$PSScriptRoot', "'$scriptDirectory'")
[IO.File]::WriteAllText(
    [IO.Path]::GetFullPath($Destination),
    $fixtureText,
    [Text.UTF8Encoding]::new($false)
)
Write-Output ([IO.Path]::GetFullPath($Destination))
