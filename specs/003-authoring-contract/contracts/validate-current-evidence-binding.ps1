#Requires -Version 7

[CmdletBinding()]
param(
    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$Repo = '.',

    [Parameter()]
    [string]$Mode,

    [Parameter()]
    [switch]$Help
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-AocCurrentEvidenceBinding {
    <#
    .SYNOPSIS
    Prueft die read-only Feature-003-Evidence-Bindung. / Validates the read-only Feature-003 evidence binding.

    .DESCRIPTION
    Bindet die unveraenderliche META-LH-02-Historie an genau vier genehmigte
    Receipt-/Review-Erneuerungen und die einzelne META-LH-03-Zielaenderung.
    Alle 14 aktuellen Ziele benoetigen frische Receipts und eindeutige Ready-
    Single-Review-Blaetter auf Bash und PowerShell. Das Cmdlet schreibt nicht.

    Binds immutable META-LH-02 history to exactly four authorised receipt/review
    renewals and the single META-LH-03 target change. All fourteen current
    targets require fresh receipts and unique Ready Single review leaves on Bash
    and PowerShell. The cmdlet does not write.

    .PARAMETER Repo
    Repository-Wurzel. / Repository root.

    .PARAMETER Mode
    Exakt current-evidence. / Exactly current-evidence.

    .OUTPUTS
    Eine PASS-Zeile oder eine fail-closed Fehlermeldung. / One PASS line or a fail-closed diagnostic.
    #>
    [CmdletBinding()]
    param(
        [Parameter()]
        [ValidateNotNullOrEmpty()]
        [string]$Repo = '.',

        [Parameter()]
        [ValidateSet('current-evidence')]
        [string]$Mode = 'current-evidence'
    )

    $core = Join-Path -Path $PSScriptRoot -ChildPath 'validate_current_evidence_binding.py'
    & python3 -B -- $core --repo $Repo $Mode
    $script:CurrentEvidenceExitCode = $LASTEXITCODE
}

if ($MyInvocation.InvocationName -ne '.') {
    if ($Help) {
        Get-Help Test-AocCurrentEvidenceBinding -Full
        exit 0
    }
    if ($Mode -ne 'current-evidence') {
        [Console]::Error.WriteLine(
            'Fehler / Error: exactly one mode, current-evidence, is required.'
        )
        exit 2
    }
    Test-AocCurrentEvidenceBinding -Repo $Repo -Mode $Mode
    exit $script:CurrentEvidenceExitCode
}
