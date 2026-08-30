#Requires -Version 7

[CmdletBinding()]
param(
    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$Repo = '.',

    [Parameter()]
    [ValidateSet('post-global-ready')]
    [string]$Mode = 'post-global-ready',

    [Parameter()]
    [switch]$Help
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-AocMetaLh02Snapshot {
    <#
    .SYNOPSIS
    Prueft den read-only META-LH-02-Programme-Snapshot. / Validates the read-only META-LH-02 programme snapshot.

    .DESCRIPTION
    Prueft Run, Branch, aktiven oder terminal abgeschlossenen Zustand, Lifecycle, 14 Ziele, unveraenderte
    Receipts und Ready-Reviews sowie beide installierten Review-Oberflaechen.
    Lokal bleibt die Git-Branchpruefung strikt. In GitHub Actions wird eine
    logische PR-/Push-Branchidentitaet nur bei exaktem Event-, Repository- und
    HEAD-Beweis akzeptiert. Zieltexte werden UTF-8-/zeilenendennormalisiert,
    unveraenderliche Rohbelege dagegen aus den exakten Git-Blobs geprueft.
    Das Cmdlet schreibt nicht in das Repository und bietet keinen Stage-Override.

    Validates the run, branch, active or terminal completed state, lifecycle, fourteen targets,
    immutable receipts and Ready reviews, and both installed review surfaces.
    Local Git branch checks stay strict. GitHub Actions admits logical PR/push
    identity only with exact event, repository, and checked-out HEAD proof.
    Target text is UTF-8/line-ending normalized while immutable raw evidence is
    checked from exact Git blobs.
    The cmdlet does not write to the repository and provides no stage override.

    .PARAMETER Repo
    Repository-Wurzel. / Repository root.

    .PARAMETER Mode
    Exakt post-global-ready. / Exactly post-global-ready.

    .EXAMPLE
    Test-AocMetaLh02Snapshot -Repo . -Mode post-global-ready

    .OUTPUTS
    Eine PASS-Zeile oder eine fail-closed Fehlermeldung. / One PASS line or a fail-closed diagnostic.

    .NOTES
    Unix-Handbuch / Unix manual: docs/man/validate-meta-lh02-snapshot.1
    #>
    [CmdletBinding()]
    param(
        [Parameter()]
        [ValidateNotNullOrEmpty()]
        [string]$Repo = '.',

        [Parameter()]
        [ValidateSet('post-global-ready')]
        [string]$Mode = 'post-global-ready'
    )

    $core = Join-Path -Path $PSScriptRoot -ChildPath 'validate_meta_lh02_snapshot.py'
    & python3 -B -- $core --repo $Repo $Mode
    $script:SnapshotExitCode = $LASTEXITCODE
}

if ($MyInvocation.InvocationName -ne '.') {
    if ($Help) {
        Get-Help Test-AocMetaLh02Snapshot -Full
        exit 0
    }
    Test-AocMetaLh02Snapshot -Repo $Repo -Mode $Mode
    exit $script:SnapshotExitCode
}
