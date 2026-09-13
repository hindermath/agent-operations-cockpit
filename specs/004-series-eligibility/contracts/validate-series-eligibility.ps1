<#
.SYNOPSIS
Prüft die Eignung einer Series ohne Startfreigabe.

Assesses Series eligibility without granting authority to start.
.DESCRIPTION
Lädt die Advanced Function Test-AocSeriesEligibility und delegiert eine
read-only Prüfung an den Python-Kern. Die Oberfläche schreibt keine Dateien
und startet keinen nachgelagerten Lauf.

Loads the advanced function Test-AocSeriesEligibility and delegates a
read-only assessment to the Python core. The surface writes no files and does
not start a downstream run.
.PARAMETER Repo
Repository-Wurzel. / Repository root.
.PARAMETER Fixture
Relativer Fixture-Pfad. / Relative fixture path.
.PARAMETER Series
Series-Manifest statt Fixture, relativ zum Repo. / Series manifest instead of fixture, relative to repo.
.PARAMETER Action
status (Standard) oder next, nur Series. / status (default) or next, series only.
.PARAMETER Json
Maschinenlesbare Ausgabe. / Machine-readable output.
.PARAMETER Help
Vollständige Hilfe anzeigen. / Show complete help.
.EXAMPLE
./validate-series-eligibility.ps1 -Repo . -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json -Json
.EXAMPLE
./validate-series-eligibility.ps1 -Help
.EXAMPLE
Test-AocSeriesEligibility -Repo . -Series specs/intake-series/aoc-phase-2/manifest.json -Action next -Json
.INPUTS
Keine Pipeline-Eingabe. / No pipeline input.
.OUTPUTS
Text oder JSON vom lesenden Validator. / Text or JSON from the read-only validator.
.NOTES
Modi aus der Fixture / Modes from the fixture: manual-assisted, single-autonomous,
serial-autonomous, parallel-autonomous, research-only, blocked.
Fixture und Series schliessen sich aus. / Fixture and series are mutually exclusive.
Lifecycle, Review, Kandidaten, Praeferenz, Blocker, Delivery und Authority bleiben getrennt.
Lifecycle, review, candidates, preference, blockers, delivery and authority remain separate.
Historische Receipt-Herkunft ist keine aktuelle Authority. / Historical provenance is not current authority.
Exit 0: gueltiges Assessment, auch Blocked. / Valid assessment, including Blocked.
Exit 2: ProductFailure, ungueltige Eingabe/Erwartung. / Invalid input/expectation.
Exit 3: ProviderFailure, Laufzeitfehler. / Runtime failure.
Eligibility ist keine Ausführungsautorität. / Eligibility is not execution authority.
.LINK
../../../docs/man/validate-series-eligibility.1
#>
[CmdletBinding()]
param(
    [string]$Repo,
    [string]$Fixture,
    [string]$Series,
    [string]$Action,
    [switch]$Json,
    [switch]$Help
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

<#
.SYNOPSIS
Prüft die Eignung einer Series ohne Startfreigabe.

Assesses Series eligibility without granting authority to start.
.DESCRIPTION
Test-AocSeriesEligibility ruft den vorhandenen Python-Kern mit expliziter
Repository-Wurzel und entweder Fixture oder Series auf. Die Funktion liest nur. Ein Ergebnis
Eligible oder Blocked erteilt keine Ausführungs-, Schreib- oder Merge-Rechte.

Test-AocSeriesEligibility invokes the existing Python core with an explicit
repository root and either fixture or series. The function is read-only. An Eligible or Blocked
result grants no execution, write, or merge authority.
.PARAMETER Repo
Repository-Wurzel. / Repository root.
.PARAMETER Fixture
Fixture relativ zum Repository. / Fixture relative to the repository.
.PARAMETER Series
Series-Manifest statt Fixture, relativ zum Repo. / Series manifest instead of fixture, relative to repo.
.PARAMETER Action
status (Standard) oder next, nur Series. / status (default) or next, series only.
.PARAMETER Help
Vollstaendige Funktionshilfe ohne Pruefung. / Complete function help without assessment.
.PARAMETER Json
Gibt das strukturierte Ergebnis als JSON aus. / Emits the structured result as JSON.
.EXAMPLE
Test-AocSeriesEligibility -Repo . -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json -Json
.EXAMPLE
Test-AocSeriesEligibility -Repo . -Series specs/intake-series/aoc-phase-2/manifest.json -Action next -Json
.INPUTS
Keine Pipeline-Eingabe. / No pipeline input.
.OUTPUTS
Text oder JSON vom lesenden Validator. / Text or JSON from the read-only validator.
.NOTES
Modi aus der Fixture / Modes from the fixture: manual-assisted, single-autonomous,
serial-autonomous, parallel-autonomous, research-only, blocked.
Fixture und Series schliessen sich aus. / Fixture and series are mutually exclusive.
Lifecycle, Review, Kandidaten, Praeferenz, Blocker, Delivery und Authority bleiben getrennt.
Lifecycle, review, candidates, preference, blockers, delivery and authority remain separate.
Historische Receipt-Herkunft ist keine aktuelle Authority. / Historical provenance is not current authority.
Exit 0: gueltiges Assessment, auch Blocked. / Valid assessment, including Blocked.
Exit 2: ProductFailure, ungueltige Eingabe/Erwartung. / Invalid input/expectation.
Exit 3: ProviderFailure, Laufzeitfehler. / Runtime failure.
Die Funktion kann durch Dot-Sourcing geladen werden, ohne eine Prüfung zu
starten. / Dot-sourcing loads the function without starting an assessment.
.LINK
../../../docs/man/validate-series-eligibility.1
#>
function Test-AocSeriesEligibility {
    [CmdletBinding()]
    param(
        [AllowEmptyString()][string]$Repo,
        [string]$Fixture,
        [string]$Series,
        [string]$Action,
        [switch]$Help,
        [switch]$Json
    )

    if ($Help) { Get-Help Test-AocSeriesEligibility -Full; return }

    $Core = Join-Path $PSScriptRoot 'validate_series_eligibility.py'
    $PythonApplications = @(Get-Command python3 -CommandType Application -All -ErrorAction SilentlyContinue |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_.Source) })
    if ($PythonApplications.Count -eq 0) {
        $PythonApplications = @(Get-Command python -CommandType Application -All -ErrorAction SilentlyContinue |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_.Source) })
    }
    if ($PythonApplications.Count -eq 0) {
        $global:LASTEXITCODE = 3
        if ($Json) {
            '{"schemaVersion":"1.0","mode":null,"criteria":{},"outcome":"Blocked","reasons":[{"code":"EL_PROVIDER","criterion":null,"de":"Die Laufzeitprüfung ist fehlgeschlagen.","en":"The runtime check failed."}],"failureClass":"ProviderFailure","authorityGranted":false,"nextAction":{"de":"Eingaben und Nachweise erneut prüfen; nichts starten.","en":"Reassess inputs and evidence; start nothing."}}'
        }
        else {
            'Modus / Mode: NotAssessed'
            'Ergebnis / Outcome: Blocked'
            'Die Laufzeitprüfung ist fehlgeschlagen. / The runtime check failed.'
            'Nächste Aktion / Next action: Eingaben und Nachweise erneut prüfen; nichts starten. / Reassess inputs and evidence; start nothing.'
            'Keine Startfreigabe. / No start authority granted.'
        }
        return
    }
    $PythonExecutable = $PythonApplications[0].Source
    $CoreArguments = @('-B', $Core, '--repo', $Repo)
    if ($PSBoundParameters.ContainsKey('Fixture')) { $CoreArguments += @('--fixture', $Fixture) }
    if ($PSBoundParameters.ContainsKey('Series')) { $CoreArguments += @('--series', $Series) }
    if ($PSBoundParameters.ContainsKey('Action')) { $CoreArguments += @('--action', $Action) }
    if ($Json) { $CoreArguments += '--json' }
    # Keine Rohdiagnosen des Interpreters ausgeben. / Do not emit raw interpreter diagnostics.
    $CoreExit = 3
    $CoreOutput = @()
    $PreviousPythonIoEncoding = [Environment]::GetEnvironmentVariable('PYTHONIOENCODING', 'Process')
    try {
        # Native Python-Ausgabe ist an dieser PowerShell-Grenze immer UTF-8.
        # Native Python output is always UTF-8 at this PowerShell boundary.
        [Environment]::SetEnvironmentVariable('PYTHONIOENCODING', 'utf-8:strict', 'Process')
        $CoreOutput = @(& $PythonExecutable @CoreArguments 2>$null)
        $CoreExit = $LASTEXITCODE
    }
    catch {
        $CoreExit = 3
    }
    finally {
        [Environment]::SetEnvironmentVariable('PYTHONIOENCODING', $PreviousPythonIoEncoding, 'Process')
    }
    $OutputText = $CoreOutput -join "`n"
    $KnownOutput = $OutputText.StartsWith('{"schemaVersion": "1.0", "mode": ') -or
        $OutputText.StartsWith('Modus / Mode: ')
    if ($CoreExit -in @(0, 2) -and $KnownOutput) {
        $global:LASTEXITCODE = $CoreExit
        $CoreOutput
        return
    }
    $global:LASTEXITCODE = 3
    if ($Json) {
        '{"schemaVersion":"1.0","mode":null,"criteria":{},"outcome":"Blocked","reasons":[{"code":"EL_PROVIDER","criterion":null,"de":"Die Laufzeitprüfung ist fehlgeschlagen.","en":"The runtime check failed."}],"failureClass":"ProviderFailure","authorityGranted":false,"nextAction":{"de":"Eingaben und Nachweise erneut prüfen; nichts starten.","en":"Reassess inputs and evidence; start nothing."}}'
    }
    else {
        'Modus / Mode: NotAssessed'
        'Ergebnis / Outcome: Blocked'
        'Die Laufzeitprüfung ist fehlgeschlagen. / The runtime check failed.'
        'Nächste Aktion / Next action: Eingaben und Nachweise erneut prüfen; nichts starten. / Reassess inputs and evidence; start nothing.'
        'Keine Startfreigabe. / No start authority granted.'
    }
}

if ($MyInvocation.InvocationName -eq '.') {
    return
}

if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Full
    exit 0
}

Test-AocSeriesEligibility @PSBoundParameters
$CoreExit = $LASTEXITCODE
exit $CoreExit
