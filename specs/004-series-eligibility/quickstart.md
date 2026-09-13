# Validierungsanleitung / Quickstart Validation Guide

## Zweck und Voraussetzungen / Purpose and prerequisites

Diese Anleitung beschreibt den implementierten lesenden META-LH-04-Prüfadapter mit sechs Modi und den Abfragen `status`/`next`. Sie ist für Lernende ab Jahr 1 und Maintainer gedacht. Eignung bedeutet geprüfte Passung, **keine Startfreigabe**. Die Abschnitte zu früheren Implementierungs- und späteren Liefergates sind Referenzverfahren, kein Auftrag, sie jetzt auszuführen. / *This guide describes the implemented six-mode read-only adapter and status/next queries for first-year learners and maintainers. Eligibility is assessed suitability, not permission to start. Historical implementation and future delivery procedures below are references, not instructions to execute them now.*

Beginne im Repository-Root. Benötigt werden Git, rg, Python 3.9+, Bash 5+ und PowerShell Core 7+; PSScriptAnalyzer 1.25.0 ist für die statische Prüfung erforderlich. Lokal werden keine Pakete oder Provider eingerichtet. Der `macos-14`-CI-Job darf nach dem bestätigten Providerbefund Bash 5 ephemer per Homebrew bereitstellen; dies ist kein allgemeiner Installationsfallback. In Windows muss `bash` auf Git-for-Windows zeigen. Setze `PYTHONDONTWRITEBYTECODE=1`; `python3 -B` muss dieselbe geprüfte Python-Runtime aufrufen, unter Windows gegebenenfalls ein dokumentierter Alias auf `python`. Nie stillschweigend einen ausgefallenen Interpreter ersetzen. / *Start at repository root with the required existing tools. Do not install local packages or configure providers. Following the confirmed provider finding, the `macos-14` CI job may provision Bash 5 ephemerally through Homebrew; this is not a general installation fallback. Use Git Bash on Windows, disable bytecode writes, and bind python3 to the verified Python runtime. Never silently replace a failed interpreter.*

```bash
git rev-parse HEAD
bash --version
python3 --version
pwsh -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
```

Versionen und tatsächlich aufgelöste ausführbare Pfade im lokalen Evidence-Protokoll nennen; keine persönlichen absoluten Pfade in getrackte Berichte kopieren. / *Record versions and actual executable resolution locally; do not copy personal absolute paths into tracked reports.*

## Finale Schnittstelle und Leserpfad / Final interface and reader path

Leserpfad: [Spec](spec.md) → Voraussetzungen oben → dieser Abschnitt → [Manpage](../../docs/man/validate-series-eligibility.1) → [Schnittstellenvertrag](contracts/series-eligibility-interface.md) und [Datenmodell](data-model.md). Ein **Kriterium** ist ein benannter Prüfpunkt; eine **Fixture** ein Testdatensatz; ein **Manifest** beschreibt Ziele und Vorgänger. Ein **Receipt** belegt die Herkunft früherer Arbeit. / *Reader path: specification → prerequisites → this section → manual → interface and data model. A criterion is a named check, a fixture is test data, a manifest describes targets and predecessors, and a receipt records historical provenance.*

Genau eine Eingabe wählen: `--fixture`/`-Fixture` oder `--series`/`-Series`. Repository-Wurzel: `--repo`/`-Repo`; Datenpfade sind repositoryrelativ. `--action`/`-Action` gilt nur für Series und ist `status` (Standard) oder `next`. `--json`/`-Json` gibt JSON aus; sonst erscheint DE/EN-Klartext. Hilfe: Bash `--help`/`-h`, PowerShell `-Help`. / *Choose exactly one fixture or series input. Set the repository root and relative data path. Action is series-only, status by default or next. JSON is optional; default output is bilingual text. Both shells expose help.*

| Fixture-Modus / Fixture mode | Bedeutung / Meaning |
|---|---|
| `manual-assisted` | Mit menschlicher Begleitung. / Human-assisted work. |
| `single-autonomous` | Ein separat autorisierter Lauf. / One separately authorized run. |
| `serial-autonomous` | Ziele nacheinander bearbeiten. / Handle targets in sequence. |
| `parallel-autonomous` | Getrennte Writes und keine gemeinsamen offenen Entscheidungen erforderlich. / Disjoint writes and no shared open decisions required. |
| `research-only` | Eignung für Recherche; startet keine Recherche. / Research eligibility; starts no research. |
| `blocked` | Eignung gesperrt. / Eligibility blocked. |

Der Modus steht in der Fixture und ist kein `--action`-Wert. Alle Modi benötigen genau neun Kriterien: `authority` (Berechtigung), `sideEffects` (Nebenwirkungen), `reversibility` (Rücknehmbarkeit), `writeScope` (Schreibbereich), `decisions` (Entscheidungen), `integration` (Zusammenführung), `review` (Prüfung), `abort` (Abbruch), `recovery` (Wiederherstellung). `currentAuthority=true` ist erforderliche Fixture-Evidence, keine neu erteilte Berechtigung. Außerhalb Parallelität sind die fünf Parallelflags optional; vorhandene Werte müssen echte Booleans und konsistent sein. / *Mode is fixture data, not an action value. Every mode needs the nine criteria in the stated order and currentAuthority=true as existing evidence. Five parallel flags are optional in nonparallel modes; supplied values must be actual consistent booleans. The checker grants no new permission.*

Beispiele für dieselbe lesende Abfrage; nur die passende Shell wählen: / *Equivalent read-only examples; choose the appropriate shell:*

```text
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --repo . --series specs/intake-series/aoc-phase-2/manifest.json --action next
pwsh -NoProfile -File specs/004-series-eligibility/contracts/validate-series-eligibility.ps1 -Repo . -Series specs/intake-series/aoc-phase-2/manifest.json -Action next
```

`status` und `next` verwenden dieselbe deterministische Projektion. Sie zeigen deklarierte Lifecycle-Werte, `reviewState=NotAssessed`, alle Kandidaten, bevorzugten Kandidaten, Blocker, `deliveryMode=NotAssessed`, `currentStartAuthority=NotGrantedByQuery` und historische Receipt-Herkunft (`HistoricalOnly`) getrennt. Ein Series-`Completed` schließt diesen autonomen Lauf nicht ab. `Idle` ohne Ziele ist gültig. Eine leere Kandidatenliste ist kein Parserfehler. / *Both queries use the same deterministic projection. Declared lifecycle, unassessed review/delivery, all candidates, preference, blockers, absent query-granted authority and historical provenance stay separate. Completed series data does not complete this run; Idle and no-candidate results can be valid.*

| Exit | Bedeutung / Meaning |
|---|---|
| `0` | Gültige Auswertung oder passende Fixture-Erwartung, auch `Blocked`. Bei ungültigem Kriterienwert und erwarteten `Blocked` kann `ProductFailure` mit Exit 0 auftreten. / Valid assessment or matching fixture assertion, including Blocked; a semantic criterion defect can be ProductFailure with exit zero when correctly expected. |
| `2` | `ProductFailure`: ungültige Struktur/Pfad/Eingabe oder abweichende Fixture-Erwartung. / Invalid structure, path, input or mismatched fixture expectation. |
| `3` | `ProviderFailure`: Runtime/Interpreter ausgefallen; kein fachlicher Test-Pass. / Runtime failure, never a semantic pass. |

Das JSON enthält genau ein `nextAction`-Objekt mit gleichwertigem `de`-/`en`-Text. `authorityGranted` bleibt false. Kriterien und Gründe stehen als Text, ohne Farbcodierung. Keine Schreib-, Stop-, Neustart- oder Teilmerge-Aktion folgt automatisch. PowerShell-Dot-Sourcing lädt nur `Test-AocSeriesEligibility`; die Funktion setzt `LASTEXITCODE`, das Skript beendet seinen Prozess. / *One nextAction object carries equivalent German/English wording; authorityGranted stays false. Criteria and reasons use text, no colour. No write, cancellation, restart or partial merge follows automatically. Dot-sourcing only loads the function; the function sets LASTEXITCODE, while script execution exits its process.*

Lokale Nachweise: [Security](../../docs/security/series-eligibility.md), [Architektur](../../docs/architecture/series-eligibility.md), [A11Y](../../docs/accessibility/series-eligibility.md), [Plattform-/Agentenreview](checklists/cross-platform.md). Die native Provider-Matrix und Assistenztechnik bleiben dort ausdrücklich offen. / *Local evidence is linked here; native provider-matrix and assistive-technology gaps remain explicit.*

**Nächste sichere Aktion:** Die gültige lokale Fixture lesend prüfen: `bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --repo . --fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json`. / ***Next safe action:** assess the named valid local fixture read-only.*

## Bestehende Baseline / Existing baseline

Die folgenden neun Befehle existieren bereits. Alle müssen mit 0 enden; `shared-write` und `shared-decision` sind gerade dann erfolgreich, wenn `Blocked` ausgegeben wird. Die Sequencing-Suite führt beide Shells aus und erwartet bei negativen Kindprozessen Exit 2 mit passender ISG-Klasse. / *These nine commands exist already. Each must exit zero; negative fixtures succeed by producing Blocked. The sequencing suite runs both shells and expects exit two and the correct ISG class from negative child processes.*

```text
bash .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.sh --file specs/intake-series/aoc-phase-2/manifest.json --repo .
pwsh -NoProfile -File .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.ps1 -File specs/intake-series/aoc-phase-2/manifest.json -Repo .
pwsh -NoProfile -File .specify/presets/intake-sequencing-governance/tests/test-intake-sequencing-validator.ps1
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/valid-parallel.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/shared-write.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/shared-write.json
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/shared-decision.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/shared-decision.json
```


## Historische minimale Einheit vor T008 / Historical minimal unit before T008

**Implementierte Voraussetzung für T008.** T001–T007 und historische Red/Green-/Blocked-Nachweise bleiben erhalten. Die minimale Adaptereinheit umfasst die beiden Hilfeflächen, sicheres PowerShell-Dot-Sourcing, die Manpage und die unveränderten `surface`-/`empty-integration`-Tests. Der aktuelle Nachweis steht unter `phase-results/atomic-surface-t008-verification.json`. / ***Implemented prerequisite for T008.** Preserve T001–T007 and all historical evidence. The minimal adapter unit includes both help surfaces, safe PowerShell dot-sourcing, the manual, and the unchanged `surface`/`empty-integration` tests. Current evidence is stored in the named phase-result file.*

Minimaler Leserpfad: [Plan](plan.md#c005-atomare-minimale-einheit-vor-t008--atomic-minimal-unit-before-t008) → dieser Abschnitt mit Voraussetzungen → Bash `--help`/`-h` oder PowerShell `-Help`/`Get-Help Test-AocSeriesEligibility -Full` → `docs/man/validate-series-eligibility.1` → genau eine sichere nächste Aktion: die gültige lokale Fixture lesend prüfen. Eligibility bedeutet Eignung, keine Startfreigabe. / *Minimal reader path: plan → prerequisites here → shell/function help → the named manpage → one safe next action: assess the valid local fixture read-only. Eligibility is suitability, not permission to start.*

1. Bash `--help` und `-h` sowie PowerShell `-Help` ohne Repo-/Fixture-Pflichtargumente manuell prüfen: Exit 0, vollständiger DE-first/EN-second-Text, interner Hilfetext oder Manpage-Verweis, keine Prüfung, Prompts oder Writes. Vollständige PowerShell-Comment-Help umfasst `.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER` für jeden vorhandenen Parameter einschließlich Help, `.EXAMPLE`, `.INPUTS`, `.OUTPUTS`, `.NOTES` und `.LINK`. / *Manually verify argument-free help, exit zero, complete bilingual content, help/manual navigation and no assessment, prompts or writes. Include every listed help section and every current parameter.*
2. In einer frischen `pwsh -NoProfile`-Sitzung ohne Argumente dot-sourcen: keine Ausgabe, Pflichtparameterabfrage, Prüfung, Prozessstarts oder Writes; der aufrufende Prozess läuft weiter. Danach `Get-Command Test-AocSeriesEligibility` als Advanced Function und deren vollständige Hilfe prüfen, dann Funktion und Skript auf derselben gültigen Fixture vergleichen. / *In a fresh NoProfile session, dot-source without arguments and verify silent load, no prompt, query, child process or writes, and caller survival. Then inspect the advanced function and complete help, and compare function/script results on the same valid fixture.*
3. Beide Varianten auf mindestens einem tatsächlichen Ziel-OS je Variante manuell verifizieren; OS, Runtime und Reviewer benennen. Bash-Syntax/Quoting/`set -euo pipefail`, PowerShell-Parser/`Set-StrictMode -Version Latest` und PSScriptAnalyzer prüfen. Vorhandene `surface`- und `empty-integration`-Tests in beiden Shells unverändert wiederholen; Green und unveränderte Testbytes bestätigen, historische Red-Quellen nicht neu schreiben. / *Manually verify each variant on at least one actual target OS, naming OS, runtime and reviewer. Check syntax, quoting, strict modes and PowerShell analysis; rerun both unchanged preparation cases through both shells. Confirm green and unchanged tests, preserving historic red sources.*
4. Die Manpage mit `man -l docs/man/validate-series-eligibility.1` lesen, Textnavigation und DE-first/EN-second CEFR B2 prüfen. Sie und die Hilfe erklären nur vorhandene T004–T007-Funktionen: Repo/Fixture/Json, delegierte Prüfung, Integration-Wertecheck, tatsächliche JSON/Klartext-Ausgabe, Exitcodes und Fehlerklassen, null Writes/Starts. Beispiele müssen das beobachtete Verhalten erklären, einschließlich des Unterschieds zwischen fachlichem `Blocked` und Fixture-Erwartungsvergleich. T027/T036 erweitern später auf sechs Modi/finale Schnittstelle; keine vorzeitige vollständige Feature-Zusage. / *Read the rendered manual, checking text navigation, bilingual B2 content and only existing T004–T007 behavior. Examples must explain observed outcomes and distinguish Blocked from the fixture expectation check. Later tasks expand final interfaces; do not claim full feature behavior now.*

Hilfebefehle; jeweils Ausgabe und unmittelbaren Exit erfassen: / *Help calls; record output and immediate exit for each:*

```text
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --help
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh -h
pwsh -NoProfile -File specs/004-series-eligibility/contracts/validate-series-eligibility.ps1 -Help
pwsh -NoProfile -Command '. ./specs/004-series-eligibility/contracts/validate-series-eligibility.ps1; Get-Command Test-AocSeriesEligibility; Get-Help Test-AocSeriesEligibility -Full'
man -l docs/man/validate-series-eligibility.1
```

Der zusammengesetzte PowerShell-Aufruf zeigt den Leserpfad; der tatsächliche Verifikationsnachweis erfasst Dot-Sourcing separat, damit nachfolgende Ausgabe keine unerwünschte Importausgabe verdeckt. Get-Command muss `CmdletBinding` bestätigen; der Import darf auch bei fehlenden Fixture-Argumenten nichts ausführen. / *The combined PowerShell example shows navigation; verification records dot-sourcing separately so later output cannot hide unwanted import output. Confirm CmdletBinding and no execution even without fixture arguments.*

Vor Delivery-Set/Staging neue Evidence in `specs/004-series-eligibility/phase-results/atomic-surface-t008-verification.json` schreiben: reale geprüfte Quell-/Testhashes, OS/Runtime/Reviewer, Befehle mit unmittelbaren Exits, beobachtete Ausgaben, semantische Hilfe-/Manpageprüfung, Funktions-/CLI-Parität, No-write/No-start samt unveränderten Eingabe-/State-/Gitstatus-Snapshots rund um die Leseaufrufe. Keine fehlende Beobachtung als Pass führen. Alle minimalen Oberflächen, Python-Kern, unveränderte Tests, Quickstart und diese neue Evidence gehören gemeinsam in den ersten T008-Quellencommit; historische Evidence bleibt bytegleich. Die Hashes müssen zu dessen geprüften Indexbytes passen. / *Before delivery validation/staging, write new evidence with actual source/test hashes, platform/runtime/reviewer, commands/exits, outputs, semantic help/manual review, function/CLI parity and no-write/no-start snapshots. Never mark an unobserved check passed. Commit the complete minimal surfaces, core, unchanged tests, quickstart and new verification together in the first T008 source commit, preserving history. Bind proof to validated index bytes.*

Fehlt ein Bestandteil oder scheitert eine Prüfung, bleibt T008 vor dem Quellencommit blockiert. Der äußere autonome Koordinator übernimmt danach unter aktueller Autorität die script-only Git-Checkpoints und den vollständigen folgenden Statistikvertrag. Modell-Sandboxes dürfen `.git` nicht schreiben; keine Sandboxkonfiguration oder Validatorregel ändern. / *Any missing component or failed check blocks T008 before the source commit. The outer coordinator then owns script-only Git checkpoints and the full statistics protocol under current authority. Model sandboxes may not write .git; change no sandbox configuration or validator rule.*

## Historisches Red/Green-Verfahren / Historical red/green procedure

Erst nach akzeptierter Planung und Implementierungsauftrag ausführen. `surface` prüft vollständige Python-ASTs, Bash-Syntax, PowerShell-Parser, Imports und Hilfe sowie einen gültigen delegierten Aufruf. Dann wird `empty-integration` einmal rot und nach der kleinen Werteprüfung grün ausgeführt. Rot wegen fehlender Datei, Runtime oder Syntax ist `ProviderFailure` bzw. Vorbereitungsfehler und kein Test-first-Beleg. / *Run only after plan acceptance and implementation authority. Surface checks all syntax, imports, help and one valid delegated invocation. Run empty-integration red once, add the narrow value check, and rerun green. Missing files/runtimes or syntax errors are preparation failures, not test-first proof.*

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case surface
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case surface
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case empty-integration
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case empty-integration
```

Erstes fachliches Red: nichtnull Testexit mit isolierter Abweichung für `integration=""`. Green: Tests Exit 0; negative Fixture `Blocked`, `ProductFailure`, Kriteriumsgrund, eine sichere Aktion, null Eingabewrites. Testname, Vorher-/Nachher-Quellhashes und echte Outputs in `phase-results/implementation-red-green.md` festhalten. / *First red is a nonzero test exit for the isolated empty-integration defect. Green is zero with the expected blocked diagnostic and no input writes. Record test name, source hashes and actual outputs in the named evidence file.*

## Referenz für weitergehende Prüfungen / Reference for broader checks

Erst nach Green und der unmittelbaren Statistikgrenze T008 folgen diese Fälle. Dieselbe zusätzliche `unittest`-Testdatei verwendet das bereits etablierte Werkzeug aus Feature 003, temporäre Daten und bestehende Validatoren; keine neue Testwerkzeug- oder CI-Familie. Die Szenarien werden in beiden Shells und auf allen drei nativen Runnern ausgeführt. `all` ist ein fachlicher Gesamtaufruf. Solange die Gate Requirements zusätzlich exakte Einzelaufrufe verlangen, müssen auch diese tatsächlich ausgeführt werden; ein interner Testgruppenname ersetzt keinen protokollierten Prozessaufruf. / *After green and the immediate T008 statistics boundary, use established unittest tooling for additional cases, without a new testing or CI framework; run broader cases using temporary data and existing validators, through both shells on all native runners. The all group is comprehensive. While gate requirements also demand exact individual invocations, execute those invocations too; an internal group name cannot replace an observed process command.*

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case all
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case all
```

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case criteria-cardinality
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case criteria-cardinality
```

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case runner-cardinality
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case runner-cardinality
```

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case series-negatives
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case series-negatives
```

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case status-next
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case status-next
```

```text
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell bash --case failure-taxonomy
python3 -B specs/004-series-eligibility/contracts/test_series_eligibility.py --repo . --shell pwsh --case failure-taxonomy
```


| Gruppe / Group | Konkrete Erwartung / Concrete expectation |
|---|---|
| `criteria-cardinality` | 9 gültige Schlüssel akzeptieren; 0/8/10, Duplikate im rohen JSON und Vertrag, fehlende/zusätzliche/gleichnamige Kriterien ablehnen. Kein achten Kriterien umfassender Ersatz. / Accept exact nine; reject all cardinality and duplicate variants. |
| `runner-cardinality` | Vorhandenen Workflow-Resolver extrahieren und mit null/einem/doppeltem Aliasfall ausführen; null blockiert, eine echte ausführbare Datei bleibt skalar, Aliasduplikate führen nicht zu falscher Array-Count-Logik. Windows-System32/WSL und unauflösbare Capability blockieren. / Exercise the actual resolver with zero/one/duplicate aliases, scalar resolution and Windows rejection cases. |
| `series-negatives` | Zyklus → `ISG007`, Hash-Drift → `ISG004`, isoliert fehlende Root → `ISG008`, mehrfach deklariertes Eligible → `ISG009`, je Kindprozess Exit 2. Originalsuite unverändert. / Expected native validator classes and exits; preserve original suite. |
| `status-next` | Wiederholung mit gültiger, blockierter, Idle- und Completed-Serie; ein bevorzugtes oder mehrere berechnete Ziele unterscheiden. Vorher-/Nachher-Bytes aller Eingaben, Receipts, Run-State und Gitstatus gleich; keine Worker-/Remote-/Write-Prozesse. / Repeat query scenarios; identical inputs and state, no downstream operations. |
| `failure-taxonomy` | Ungültiges Artefakt → ProductFailure; simuliertes Starten des erlaubten Validators scheitert technisch → ProviderFailure. Kein echter Provideraufruf nötig. Kein Stacktrace, Secret, Token, persönliches Datum oder ausführbarer Rohbefehl im Output. / Separate artifact and runtime failures without actual provider calls or sensitive output. |
| `all` | Ursprüngliche 3 Fixtures plus strikte Werte/Booleans, fehlende Authority, sechs Modi, Shared Write/Decision, Recovery, Pfade und Reader-Output. / Full accepted domain, boundary and safe-output coverage. |

`status-next` prüft zwei Ebenen: automatisiert den neuen deterministischen Prüfadapter; manuell die vorhandenen Agentenverträge `.specify/presets/intake-sequencing-governance/commands/speckit.intake-series-status.md` und `speckit.intake-series-next.md`. Kein automatisierter Test darf behaupten, damit jede zukünftige Agentenreaktion bewiesen zu haben. / *Verify the deterministic adapter automatically and the existing agent instructions manually; tests do not prove every future agent response.*

Für den No-write-Beleg: vor Aufruf Dateiliste plus rohe SHA-256-Werte der Eingaben, Manifest, Receipts und Laufzustände aufnehmen; unmittelbar danach dieselbe Menge vergleichen und neu entstandene Dateien erfassen. Gitstatus vorher/nachher ergänzen. Harness-Logs außerhalb der beobachteten Eingabemenge erzeugen und getrennt ausweisen. Nur erlaubte read-only Validator-Kindprozesse zulassen; ein fehlender Worker im Dateisystem allein beweist keinen Nichtstart. / *Capture input file lists and raw hashes before and after each query, detect additions, and compare Git status. Keep harness logs outside observed inputs and account for them separately. Allow only named read-only validator subprocesses; absence of worker files alone does not prove no start.*

## Native Runner und Fehlergrenzen / Native runners and failure boundaries

| Gate-Suffix / Gate suffix | Tatsächliche Plattform / Actual platform | Pflicht / Requirement |
|---|---|---|
| `linux` | `ubuntu-22.04` | `Bash 5+`, `PowerShell Core 7+`, `Python 3` |
| `macos` | `macos-14` | `Bash 5+`, `PowerShell Core 7+`, `Python 3`; System-Bash 3.2 genügt nicht. / System Bash 3.2 is insufficient. |
| `windows` | `windows-2022` | `Bash 5+` via Git-for-Windows, `PowerShell Core 7+`, `Python 3`; WSL-Launcher ausgeschlossen. / WSL launcher excluded. |

Die vorhandene `.github/workflows/powershell-analysis.yml` wird um die Befehle dieser Anleitung erweitert. Pfad und Version aus der Ausführung protokollieren; erforderliche Token stehen in den Gate Requirements. Die Versionsklasse ist ein Nachweislabel, kein frei erfundener Runtimewert. Get-Command/Bash-PATH muss die tatsächlich ausgeführte Datei belegen. Pro Befehl Exit sofort erfassen, bevor ein weiteres Kommando ihn überschreibt. / *Extend the existing workflow with these commands. Record actual paths/versions; requirement tokens are evidence labels, not invented runtime values. Prove the executable used and capture every exit immediately.*

Fehlendes Tool oder ausgefallener Job bleibt `ProviderFailure` und blockiert den jeweiligen Gateabschluss. Ein späterer echter nativer Lauf kann diese Lücke schließen. Ein grünes Matrix-Joblabel, macOS-PowerShell oder ein lokaler Simulationspass ersetzt keine native Windows-/Linux-Evidence. / *Missing tools or failed jobs remain provider failures and block the gate until a real native run supplies evidence. Labels and simulations do not replace native proof.*

## Bestehende Qualitätsbefehle / Existing quality commands

Diese vorhandenen Aufrufe prüfen Definitionen und das Repository. Neue ungetrackte PowerShell-Dateien müssen zusätzlich direkt mit denselben Analyzer-Einstellungen geprüft werden, da der gemeinsame Lauf ausschließlich Git-getrackte Dateien betrachtet. / *These existing commands check definitions and the repository. Also analyze new untracked PowerShell files directly with the same settings, because the shared runner covers tracked files only.*

```text
python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready
```

```text
pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1 -RepositoryRoot .
```

```text
bash scripts/check-homogeneity.sh --dry-run --verbose .
pwsh -NoProfile -File scripts/check-homogeneity.ps1 -TargetDir . -DryRun -Verbose
```

```text
bash scripts/scan-agent-secrets.sh --fail-on-high .
gitleaks dir specs/004-series-eligibility --no-banner --no-color --redact
git diff --check
```

```text
bash scripts/validate-documentation-impact.sh --evidence specs/004-series-eligibility/contracts/documentation-impact.json
pwsh -NoProfile -File scripts/validate-documentation-impact.ps1 -Evidence specs/004-series-eligibility/contracts/documentation-impact.json
```


```powershell
Import-Module PSScriptAnalyzer -RequiredVersion 1.25.0
$findings = @(Invoke-ScriptAnalyzer -Path specs/004-series-eligibility/contracts -Recurse -Settings scripts/config/PSScriptAnalyzerSettings.psd1)
$findings
if ($findings.Count -ne 0) { throw 'Feature analysis failed.' }
```

Ausführung in `pwsh -NoProfile`; nur nach Entstehung der geplanten Skripte. PSScriptAnalyzer löst keine native Funktionsprüfung ab. / *Run in PowerShell without profile after scripts exist; analysis does not replace native functional proof.*

### Public Readiness / Public Readiness

Der vorhandene Job `repository-baseline` in `.github/workflows/public-readiness.yml` läuft auf `ubuntu-latest`. Er führt den Secret-Scan oben aus und danach exakt folgende Pfadprüfung. Diese ist read-only; die tatsächliche Jobausgabe bindet später den exakten geprüften HEAD. / *The existing repository-baseline job runs on Ubuntu and performs the secret scan followed by this path check. It is read-only; actual job logs later bind the reviewed head.*

```powershell
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false
$tracked = @(git ls-files)
if ($tracked -match '^\.specify/presets/\.cache/') {
    throw 'The local Spec Kit preset cache must not be committed.'
}
$patterns = @(
    ('/Us' + 'ers/[[:alnum:]_.-]+/'),
    ('/ho' + 'me/[[:alnum:]_.-]+/'),
    '[A-Za-z]:\\Users\\[[:alnum:]_.-]+\\'
)
foreach ($pattern in $patterns) {
    $matches = git grep -n -I -E -- $pattern 2>$null
    $grepExitCode = $LASTEXITCODE
    if ($grepExitCode -eq 0) {
        $matches
        throw "Personal absolute path pattern found: ${pattern}"
    }
    if ($grepExitCode -ne 1) {
        throw "git grep failed for pattern: ${pattern}"
    }
}
exit 0
```

Vor Staging dieselben Muster zusätzlich auf die explizit benannten neuen Dateien prüfen; `git grep` allein sieht sie noch nicht. `dotnet-contract` bleibt N/A, solange kein genehmigtes Produktprojekt existiert. Kein Produktprojekt nur für einen grünen Job anlegen. / *Before staging, check the same patterns against explicitly named new files because git grep does not yet see them. The .NET job remains N/A without an approved product project; do not create a project to make a job green.*

### Statistik / Statistics

An T008 unmittelbar nach T007 sowie T016/T022/T031/T040/T055 gilt zuerst der [Checkpoint-Vertrag](contracts/statistics-checkpoints.json). In der aktuellen Plan-Remediation keine Befehle dieses Statistikabschnitts ausführen. / *At all six mandatory boundaries, complete the checkpoint prerequisites first. Execute none of this statistics section during the current planning remediation.*

1. Aktuelle lokale Commit-/Statistikautorität, akzeptierte Hashes, echten Feature-Branch und die seit dem vorherigen Checkpoint fertiggestellte exakte Liefermenge prüfen. Für T008 alle akzeptierten Vorarbeiten und T001–T007 kausal zuordnen; unklare/fremde Änderungen blockieren. T055 nutzt den realen autorisierten Closeout-Feature-Branch vom synchronisierten Lifecycle-Stand im selben Arbeitsbaum. / *Verify authority, inputs, real branch and exact completed increment. Attribute T008 preparation explicitly; unrelated changes block. T055 uses the actual authorized closeout branch from the synchronized lifecycle state.*
2. Hilfe beider Delivery-Set-Validatoren unter `.specify/presets/autonomous-run-governance/scripts/` lesen. Unstaged: Bash `validate-autonomous-delivery-set.sh --repo .` mit `--intended PFAD` je ungetrackter Lieferdatei; PowerShell `validate-autonomous-delivery-set.ps1 -Repo . -Intended $intendedUntracked` in einer `pwsh -NoProfile`-Sitzung mit echter String-Array-Variable. Die gesamte ausgegebene Menge einschließlich aller geänderten getrackten Dateien exakt mit der genehmigten Menge abgleichen. Platzhalter nicht blind ausführen; unmittelbare Exits speichern. / *Read validator help, run both unstaged surfaces with named untracked paths and compare the full reported set, including tracked changes, to the approved increment. Use a real PowerShell string array in a NoProfile session, not a comma-joined native CLI argument; record immediate exits.*
3. Nur diese Pfade mit `git add --` stagen. Bash mit `--staged` und `--intended PFAD` je Kandidatenpfad, PowerShell mit `-Staged -Intended $intendedAll` prüfen; beide Exits müssen 0 sein. Exakte Pfadmenge, physische Indexhashes und keine fremden Reständerungen belegen. Erst danach autorisierten lokalen Conventional Commit erstellen, Trailer exakt `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`. Commitbaum mit geprüften Indexbytes vergleichen. Jede Drift verlangt Revalidierung; historische Whitespace-Ausnahmen nur unter bestehender ausdrücklicher Autorität für exakt unveränderte Rohhashes. / *Stage only approved paths, validate both staged surfaces with every candidate path and index hashes, then create the authorized Conventional Commit with the exact trailer. Compare committed bytes to the validated index; revalidate on drift and preserve strict historical allowance rules.*
4. `git branch --show-current`, `git rev-parse HEAD` und `git status --porcelain=v1 --untracked-files=all` protokollieren: gebundener echter Feature-Branch, Status leer, Index sauber. Neue Logs/Taskmarken/State-Fakten jetzt ausschließlich im bereits ignorierten `checkpoints`-Unterverzeichnis des Runtime-Laufs speichern; Ignorierung vorher mit `git check-ignore` beweisen. Erst danach folgende Hilfe-/Preview-/Render-/Check-Sequenz ausführen; Vorschauen müssen äquivalent sein und dieselbe unveränderte Quelle verwenden. / *Prove the real bound feature branch, source head and clean tree/index. Keep new logs/completion/state facts in the existing ignored runtime checkpoint area, verifying its ignore rule first. Then execute both helps, equivalent previews at one unchanged source, one render and both checks.*

```text
bash scripts/render-project-statistics.sh --help
pwsh -NoProfile -Command "Get-Help ./scripts/render-project-statistics.ps1 -Full"
bash scripts/render-project-statistics.sh --repo . --dry-run
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -WhatIf
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo .
bash scripts/render-project-statistics.sh --repo . --check-only
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly
```

Danach nur bei geändertem `docs/project-statistics.md`: beide unstaged Delivery-Set-Prüfungen mit exaktem Mengenabgleich allein auf diese Datei, exakt stagen, beide staged Prüfungen/Indexhashes, gesonderter Conventional Commit mit demselben verpflichtenden Trailer. Keine Evidence/Taskmarken im Statistikcommit und kein leerer Commit bei unveränderter Ausgabe. Nach Commit beziehungsweise unverändertem Ergebnis erneut sauberen echten Feature-Arbeitsbaum und beide Check-only-Passes beweisen. Die vom unveränderten Renderer ermittelte `sourceRevision` getrennt von Quellen-HEAD und Statistikcommit festhalten. / *If and only if the ledger changed, validate it alone in both unstaged and staged surfaces, then create a separate Conventional Commit with the same trailer. No mixed evidence/task marks and no empty commit. Finish with clean-tree and both check-only proofs, recording the renderer source revision separately from source and statistics commit SHAs.*

Die gerade bestandene Grenze zunächst im hashgebundenen Runtime-Receipt abschließen; ihre Checkbox und kanonischen Review-Nachweise beim nächsten autorisierten Quellencheckpoint übernehmen, niemals vor dem Pass markieren. Vor T046/T056-Freeze/Push muss jedes versionierte Restdelta seit dem vorherigen Quellencheckpoint denselben vollständigen Vertrag einschließlich frischer Statistik durchlaufen. T051-Review-Reparaturen und T054-Lifecycle-Lieferung folgen bei Quelldrift ebenfalls diesem Verfahren vor ihren Head-Gates. Keine Pflichtgrenze verschieben; finale eigene Commit-/Merge-/Sync-Fakten bleiben außerhalb ihres Commitcontainers, ohne Selbsthash-/HEAD-Schleife. / *Complete the actual boundary in runtime evidence first and publish its checkbox/review at the next authorized source checkpoint. Before freeze/push, every residual versioned delta needs the full protocol and fresh statistics. Apply the same to review repair and lifecycle source drift before head gates. Never premark completion or defer a boundary; keep final self-container facts outside the commit.*

T044/T046 prüfen vollständige akkumulierte Eltern-/Commit-/Pfad-/Hash-/Trailerhistorie, nicht nur den aktuellen Diff. T047 pusht den eingefrorenen Feature-HEAD, T056 die Closeout-Historie. Neue Kopfstände invalidieren betroffene CI-/Review-/PreMerge-Nachweise. T045 bleibt ein separates aktuelles Remote-Gate; lokale Checkpoints verleihen keine Push-/PR-/Merge-Rechte. / *Audit full accumulated ancestry and per-commit scope/hash/trailer evidence; push only frozen feature/closeout history. Head changes invalidate affected CI/review/premerge evidence; local checkpoints never confer remote authority.*

## Manuelle Nachweise / Manual evidence procedures

Die folgenden `manual:*`-Token sind **Review-Verfahren, keine Shellbefehle**. Der Reviewer protokolliert Token, geprüfte Pfade/Hashes, Datum, tatsächliche Umgebung, Beobachtungen und offene Grenzen. Automatische Strukturprüfungen können diesen fachlichen Review nicht ersetzen. / *The manual tokens name review procedures, not shell commands. Record token, paths/hashes, date, actual environment, observations and limits. Automated structural validation does not replace semantic review.*

| Token | Verfahren und Ergebnisdatei / Procedure and output |
|---|---|
| `manual:security` | Alle Security-Matrixzeilen im Plan prüfen; Angriffspfade anhand der echten Positiv-/Negativfälle bewerten, Applicability/Implementation getrennt, STRIDE/CIA/CAPEC und Runtime-/Dependency-Audit festhalten. `docs/security/series-eligibility.md`. / Review all security rows against real cases with distinct applicability/implementation and audit evidence. |
| `manual:architecture` | Kontext, Input-/Outputgrenze und Reuse gegen tatsächlichen Code lesen; Qualitätsziele SC-001–005, Risiken/Schuld, ADR/S-ADR-Trigger prüfen. `docs/architecture/series-eligibility.md`. / Review context, boundary, reuse, quality scenarios and decisions against actual implementation. |
| `manual:accessibility` | Markdown gerendert und Klartextausgaben in benannter Umgebung lesen; Reihenfolge, Überschriften, Links, vollständige neun Kriterien, Gründe und eine Aktion prüfen; DE/EN gleicher Sinn, CEFR B2, keine alleinige Farbe. WCAG-Kriterien aus Plan einzeln disponieren; fehlenden Screenreader-Test sichtbar lassen. `docs/accessibility/series-eligibility.md`. / Review rendering, textual semantics and bilingual readability; expose assistive-technology proof limits. |
| `manual:parity` | Alle fünf Agentenflächen und vorhandene status/next-Anweisungen prüfen; neue Hilfe, Manpage und dot-gesourcte `Test-AocSeriesEligibility` auf jedem Zielsystem manuell testen; keine Mutation beim Laden. `checklists/cross-platform.md`. / Verify agent bounds and native help/cmdlet behavior, including no execution on load. |
| `manual:retrospective` | Sieben geordnete Perspektiven, Quellen/Hashes aus META01–03, Zählregeln und Vergleichbarkeit prüfen; tatsächlichen Abschluss von noch fehlenden Lieferfakten trennen. `engineering-retrospective.md`. / Verify ordered retrospective, bound comparisons and actual delivery limits. |
| `manual:aeps` | `docs/aeps/README.md` anwenden; Beobachtungen gegen vorhandene IDs deduplizieren, Ledger/Receipt pflegen, begründetes No-change erlauben, keine Promotion. / Apply capture/deduplication and retain authority bounds. |

## Gate- und Ergebnisbindung / Gate and result binding

Für diese Planphase genügen aktuelle Eingangsgates, vollständige geprüfte Planungsartefakte und der validierte Phasenergebnisvertrag. Spätere technische Gates bleiben `Not Assessed`. Der Plan-Report beschreibt diese Grenze ausdrücklich. / *This phase requires current input gates, complete checked planning artifacts and a validated phase result. Later technical gates remain Not Assessed; the report states this boundary.*

Bei separat autorisierter Lieferung vollständige Gate-Evidence aus tatsächlichen Befehlen und Joblogs erstellen. Die folgenden Aufrufe sind dann verbindlich; `HEAD_SHA` ist durch den vollständigen tatsächlich geprüften Commit zu ersetzen. Kein Selbsthash oder erfundener grün markierter Snapshot. / *Separately authorized delivery requires complete evidence derived from actual commands/logs. Substitute the full reviewed commit below; do not invent passing snapshots or self-hash loops.*

```text
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh --repo .
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh --requirements specs/004-series-eligibility/contracts/autonomous-run-gate-requirements.json --evidence .specify/runtime/autonomous-routing/8b306e28-51eb-4510-afbc-5056b9aee328/premerge-gate-evidence.json --head HEAD_SHA
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.ps1 -Requirements specs/004-series-eligibility/contracts/autonomous-run-gate-requirements.json -Evidence .specify/runtime/autonomous-routing/8b306e28-51eb-4510-afbc-5056b9aee328/premerge-gate-evidence.json -Head HEAD_SHA
```

Vor einem später genehmigten Commit `--staged` und wiederholtes `--intended PFAD` für genau die genehmigten Lieferdateien benutzen. Aktuell keine Staging-/Commit-Aktion. Der Runner darf Plan nicht aus einem Prozess-Exit allein abschließen; er muss Payloadhash, Aufgabenanzahl und Gateaussage prüfen. / *Before a later authorized commit, use staged mode and repeated intended paths for the exact approved delivery set. No staging/commit now. Phase completion requires payload hash, task count and gate proof, not exit alone.*

Aktuelle Implementierungsgrenze: T041–T045 lokal prüfen, T040 aus dem autoritativen Receipt übernehmen und vor T046 stoppen. Das [Closeout-Dokument](completion-closeout.md) benennt genau einen kausalen Pfad und getrennte Runtime-Snapshots. / *Current boundary: validate T041–T045 locally, carry T040 from the authoritative receipt, and stop before T046. The closeout document declares one causal path and separate runtime snapshots.*

## Verbindliche Review-Präzisierungen / Binding review clarifications

### Runner-Auflösung / Runner resolution

Der bestehende Resolver belegt eine ausführbare Bash, aber prüft keine Mindestversion. Sein unveränderter Regressionstest darf deshalb nicht behaupten, Bash 3.2 zurückzuweisen. Der neue Feature-004-Schritt prüft zusätzlich die tatsächliche Major-Version >= 5. Das offizielle `macos-14`-Image enthält nur Bash 3.2; deshalb darf genau dieser CI-Job nach menschlicher Freigabe Bash 5 ephemer per Homebrew bereitstellen und ihren Ordner für Kindprozesse voranstellen. Auf Linux bleibt die vorhandene Bash maßgeblich; auf Windows ausschließlich die geprüfte Git-for-Windows-Datei. Fehlt die passende Version nach diesem begrenzten macOS-Schritt, blockiert die Matrix. Die Feature-003-Policy bleibt unverändert. / *The existing resolver proves executability, not a minimum version. Feature 004 additionally checks major version 5 or newer. The official `macos-14` image only contains Bash 3.2, so this CI job alone may provision Bash 5 ephemerally through Homebrew after human approval and prepend its directory for child processes. Linux keeps its existing Bash and Windows permits checked Git Bash only. Missing capability after the bounded macOS step blocks the matrix; Feature 003 remains unchanged.*

`runner-cardinality` trennt daher zwei Prüfobjekte: den bestehenden null/eins/mehrfach-Resolver und die neue Feature-004-Versions-/PATH-Grenze mit Version 3 versus 5. `python3` muss auch aus einem neuen Kindprozess dieselbe geprüfte Python-Datei erreichen; ein nur in PowerShell definierter Alias reicht nicht für Bash oder Python-subprocess. Beide Shells protokollieren Auflösung und Version; Pfade mit Leerzeichen bleiben einzelne Argumente. / *Test the original resolver separately from the added version/PATH boundary. A fresh child process must resolve python3 to the checked Python executable; a PowerShell-only alias is insufficient for Bash or Python subprocesses. Both shells record executable/version and preserve spaced paths as single arguments.*

### Gate-Zeilen und zeitliche Bindung / Gate rows and time binding

Der installierte Validator verlangt **alle** `requiredCommandTokens` und `requiredRunnerOrPlatformTokens` in **jeder** Applicable-Zeile eines Gates, einschließlich Supplemental-Zeilen. Deshalb je Gate genau eine Primary-Zeile mit dem aus realen Logs belegten Befehlsblock und den real belegten Plattform-/Versionsklassen erstellen. Einzelne Befehle behalten im verlinkten Protokoll ihre unmittelbaren Exitcodes. Keine auf mehrere unvollständige Zeilen verteilten Tokens und keine nur zum Bestehen erfundenen Labels. Ein negativer Strukturtest entfernt ein Token aus dieser Zeile und muss `AEI202` ergeben. / *Every Applicable row, including Supplemental rows, must contain every required command and runner token. Use one Primary row per gate with the actual logged command block and verified platform/version classes. Preserve each command's immediate exit in linked logs. Do not distribute required tokens across incomplete rows or invent labels. A negative structural test removing one token must fail with AEI202.*

Red-Evidence ist historisch: Sie bindet die unfertigen Quellbytes und den fachlich erwarteten Testfehler. `EL-red-green` prüft am späteren Abnahme-HEAD die Vollständigkeit dieses historischen Protokolls mit `manual:red-green` sowie die grünen Wiederholungen. Ein alter roter Lauf wird niemals als erfolgreicher Lauf am neuen HEAD etikettiert. Manuelle Prüfung nennt Reviewer, geprüften Quellhash, Testhash, beobachtete Ausgaben und den Unterschied zwischen historischem Red und aktuellem Green. / *Red evidence is historical and binds pre-fix source bytes and the expected semantic test failure. At acceptance head, EL-red-green reviews this record with manual:red-green and runs green checks. Never relabel an old red run as a passing run at the new head. Record reviewer, source/test hashes, outputs and the historical-red/current-green distinction.*

Die Hashrichtung ist Eingaben → Ausführungsnachweis → Review-Bericht → Phasenergebnis. Kein Dokument bindet seinen eigenen Hash oder den Hash eines späteren Containers, der es selbst bindet. PreMerge-Evidence bleibt außerhalb des Commits, dessen HEAD sie prüft. Retrospektive und AEPS-Receipt vor Lieferung dürfen nur tatsächlich geschehene lokale Arbeit belegen; kausale Merge-Fakten gehören nach separater Autorisierung in den vorab benannten PostMerge-Closeout. / *Hashes point from inputs to execution evidence to review report to phase result. No self-hash or backward hash to a container that already binds the document. Keep premerge evidence outside the commit it verifies. Pre-delivery retrospective/AEPS evidence covers actual local work; later merge facts belong in separately authorised, predeclared postmerge closeout.*

### Prüfdaten und Modusabdeckung / Test data and mode coverage

Der Red-Slice darf `expectedOutcome=Blocked` setzen, aber muss die aus `meets_parallel_eligibility` berechnete Einstufung **vor** dem Legacy-Erwartungsvergleich erfassen. Ein Legacy-CLI-Exit wegen `expectedOutcome`-Abweichung ist nicht der alleinige fachliche Red-Nachweis. I1 liefert bereits stabile Ergebnisfelder und Sichere-Fehler-Abbildung; I2 ändert ausschließlich den fehlenden Wertecheck. / *The red fixture can expect Blocked, but capture classification before the legacy expectation assertion through the reusable function. A legacy CLI expectation-mismatch exit alone is insufficient red evidence. I1 supplies stable output/error mapping; I2 changes only the missing value check.*

Alle sechs Modi testen, darunter jede nichtparallele Klasse ohne die fünf optionalen Parallelflags, fehlende Authority sowie konsistente Shared-Writes/Decisions. Bei Status/Next sind mehrere Vorgänger und verschiedene Hash-Seeds erforderlich; Pfadtests prüfen auch transitive Reads gemäß Schnittstellenvertrag. / *Test every mode, including nonparallel inputs without optional parallel flags, absent authority and consistent shared writes/decisions. Query tests use multiple predecessors and hash seeds; path tests include nested reads as defined in the interface.*

## Ausführungsgrenzen nach Remediation / Execution boundaries after remediation

Vor Umsetzung gilt T001: `phase-results/analyze-report.md` plus das im Run-State aktuell gebundene `analyze-2.result.json` im bestehenden Runtime-Verzeichnis; Outcome `Completed`, `gatesSatisfied=true`, aktuelle Input-/Payloadhashes und beide Resultatvalidatoren müssen bestehen. Der historische Blocked-Bericht und dieses Dokument erteilen keine Freigabe. / *Before implementation, require the current runner-bound analyze-2 result, report, passing outcome/gates and current hashes with both result validators. Historical reports and this guide grant no authority.*

Der [Katalog](contracts/validation-commands.json) ist nach Ausführung getrennt: T029/T048 nur `native-automated-gate`, Qualitätsgates auf ihren benannten Plattformen, `stats-preview`/`stats-render` an den sechs Pflichtgrenzen sowie ausschließlich bei den im Katalog genannten bedingten Quellenaktualisierungen vor Freeze/Push. `public-readiness` ist ausschließlich T049-Liefer-Evidence: `gh run view RUN_ID --job JOB_ID --log` erst mit beobachteten IDs und exaktem PR-Head ausführen. `ubuntu-latest` benennt den beobachteten Providerjob, nicht den Client-Rechner. Ein einzelner fehlender Gate-Token bleibt ein Fehler; keine Gruppen-Pass-Abkürzung. / *Use catalog execution classes, tasks and platforms. Statistics writes belong to the six mandatory boundaries and catalogued conditional source-refresh checkpoints only; provider-log retrieval belongs only to T049 with observed IDs and the reviewed head. Ubuntu labels the provider job, not the retrieval client. Missing individual tokens still fail.*

Nach Feature-Merge ausschließlich T053/T054: gepaarte Rename-Preview/Fixture-Prüfung nach META-LH-03, ein unveränderter Content-Rename, nötige aktuelle Lineage-/Receipt-/Ready-/Global-Ready-/Manifest-Mappings, ein Lifecycle-PR. Danach T055/T056 Retrospektive/Closeout-PR und T057 finaler Sync. Legacy-Rename-Helfer committen selbst; erst Vertrag prüfen und bewährte isolierte Preview nutzen. Bei fehlender Autorität oder unbelegbarer Migration stoppen; keine Intake-Inhaltsänderung, Series-Semantikänderung oder META-LH-05. / *After feature merge only, use paired preview/validation, one content-preserving lifecycle rename and necessary current evidence rebindings in one PR, followed by retrospective closeout and final sync. Inspect self-committing legacy helpers before using the proven isolated preview; stop on missing authority or unprovable migration.*
