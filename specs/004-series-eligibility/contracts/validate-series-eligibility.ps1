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
.PARAMETER Json
Maschinenlesbare Ausgabe. / Machine-readable output.
.PARAMETER Help
Vollständige Hilfe anzeigen. / Show complete help.
.EXAMPLE
./validate-series-eligibility.ps1 -Repo . -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json -Json
.EXAMPLE
./validate-series-eligibility.ps1 -Help
.INPUTS
Keine Pipeline-Eingabe. / No pipeline input.
.OUTPUTS
Text oder JSON vom lesenden Validator. / Text or JSON from the read-only validator.
.NOTES
Eligibility ist keine Ausführungsautorität. / Eligibility is not execution authority.
.LINK
../../../docs/man/validate-series-eligibility.1
#>
[CmdletBinding()]
param(
    [string]$Repo,
    [string]$Fixture,
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
Repository-Wurzel und Fixture auf. Die Funktion liest nur. Ein Ergebnis
Eligible oder Blocked erteilt keine Ausführungs-, Schreib- oder Merge-Rechte.

Test-AocSeriesEligibility invokes the existing Python core with an explicit
repository root and fixture. The function is read-only. An Eligible or Blocked
result grants no execution, write, or merge authority.
.PARAMETER Repo
Repository-Wurzel. / Repository root.
.PARAMETER Fixture
Fixture relativ zum Repository. / Fixture relative to the repository.
.PARAMETER Json
Gibt das strukturierte Ergebnis als JSON aus. / Emits the structured result as JSON.
.EXAMPLE
Test-AocSeriesEligibility -Repo . -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json -Json
.INPUTS
Keine Pipeline-Eingabe. / No pipeline input.
.OUTPUTS
Text oder JSON vom lesenden Validator. / Text or JSON from the read-only validator.
.NOTES
Die Funktion kann durch Dot-Sourcing geladen werden, ohne eine Prüfung zu
starten. / Dot-sourcing loads the function without starting an assessment.
.LINK
../../../docs/man/validate-series-eligibility.1
#>
function Test-AocSeriesEligibility {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Repo,
        [Parameter(Mandatory)][string]$Fixture,
        [switch]$Json
    )

    $Core = Join-Path $PSScriptRoot 'validate_series_eligibility.py'
    $CoreArguments = @('-B', $Core, '--repo', $Repo, '--fixture', $Fixture)
    if ($Json) { $CoreArguments += '--json' }
    & python3 @CoreArguments
}

if ($MyInvocation.InvocationName -eq '.') {
    return
}

if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Full
    exit 0
}

if ([string]::IsNullOrWhiteSpace($Repo) -or [string]::IsNullOrWhiteSpace($Fixture)) {
    Write-Error 'Repo und Fixture sind erforderlich. / Repo and Fixture are required.'
    exit 2
}

Test-AocSeriesEligibility -Repo $Repo -Fixture $Fixture -Json:$Json
$CoreExit = $LASTEXITCODE
exit $CoreExit
