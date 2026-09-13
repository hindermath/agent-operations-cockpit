# Feature-Prüfschnittstelle / Feature Validation Interface

## Grenze und Herkunft / Boundary and provenance

Diese Schnittstelle ist **implementiert** und ergänzt interne Prüfwerkzeuge für META-LH-04. Bestehende gebundene Aufrufe unter `specs/intake-review-fixtures/meta-lh-04/` behalten ihre Bedeutung als Kompatibilitätsbelege. / *This interface is implemented and adds internal META-LH-04 validation tooling. Existing bound fixture commands retain their role as compatibility evidence.*

## Aufrufe / Invocations

Neue Dateien sind `contracts/validate-series-eligibility.sh`, `.ps1` und `validate_series_eligibility.py` im Feature. Alle Aufrufe übergeben die Repository-Wurzel ausdrücklich. / *New files reside in this feature's contracts directory. Every invocation passes the repository root explicitly.*

```bash
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --repo . --fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json --json
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --repo . --series specs/intake-series/aoc-phase-2/manifest.json --action status --json
bash specs/004-series-eligibility/contracts/validate-series-eligibility.sh --repo . --series specs/intake-series/aoc-phase-2/manifest.json --action next --json
```

```powershell
pwsh -NoProfile -File specs/004-series-eligibility/contracts/validate-series-eligibility.ps1 -Repo . -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json -Json
pwsh -NoProfile -File specs/004-series-eligibility/contracts/validate-series-eligibility.ps1 -Repo . -Series specs/intake-series/aoc-phase-2/manifest.json -Action status -Json
pwsh -NoProfile -File specs/004-series-eligibility/contracts/validate-series-eligibility.ps1 -Repo . -Series specs/intake-series/aoc-phase-2/manifest.json -Action next -Json
```

Die Paare prüfen dasselbe; `--fixture` und `--series` schließen sich aus. Ohne `--json` erscheint DE-first/EN-second Klartext mit Modus, Kriterien, Ergebnis, Gründen, Nicht-Autorität und genau einer nächsten Aktion. JSON verwendet stabile Schlüssel und zweisprachige Textfelder. / *Pairs assess the same input; fixture and series arguments are mutually exclusive. Without JSON, display bilingual plain text with mode, criteria, result, reasons, non-authority, and one next action. JSON uses stable keys and bilingual text fields.*

PowerShell bietet `Test-AocSeriesEligibility` als Advanced Function mit denselben Parametern; Dot-Sourcing lädt die Funktion ohne Ausführung. Manpage: `docs/man/validate-series-eligibility.1`; Bash `--help`/`-h`, PowerShell `-Help` und `Get-Help Test-AocSeriesEligibility -Full` erklären Beispiele und Exitcodes zweisprachig. Kein Write-, Start-, Repair-, Netzwerk- oder Providerparameter. `-WhatIf` ist für diese immer lesenden Abfragen N/A. / *PowerShell exposes the advanced function with equivalent parameters; dot-sourcing loads without execution. Help and the man page explain examples and exits bilingually. No write, start, repair, network, or provider parameter; WhatIf is N/A for inherently read-only queries.*

## Fachliches Ergebnis und Exitcode / Domain result and exit code

| Situation / Situation | Ergebnis / Outcome | Exit |
|---|---|---|
| Vollständige gültige Fixture, Erwartung erfüllt / Complete valid fixture, expectation met | `Eligible` oder `Blocked`, `failureClass=null` / Either domain outcome | 0 |
| Vollständig lesbare negative Fixture, erwarteter ungültiger Kriterien-/Authoritywert / Readable negative fixture with expected invalid value | `Blocked`, `ProductFailure`, sichere Diagnose; Erwartung muss explizit `Blocked` sein / Safe diagnostic, explicit expected Blocked required | 0 |
| Tatsächliches Ergebnis passt nicht zu `expectedOutcome` / Actual outcome mismatches expectation | `ProductFailure`; nie Erfolg / Never success | 2 |
| Ungültiges JSON, doppelte Schlüssel, fehlende Datei, Pfadausbruch, fehlerhaftes Manifest / Invalid JSON, duplicate keys, missing file, path escape, invalid manifest | `Blocked`, `ProductFailure`; kein Bewertungs-Pass / No assessment pass | 2 |
| Nachweislicher Runner-/Interpreterausfall / Proven runner or interpreter failure | `Blocked`, `ProviderFailure`; nicht durch erwartetes Blocked heilbar / Expected Blocked cannot turn this into a pass | 3 |
| Gültiger Status/Next ohne Kandidaten, einschließlich `Idle` oder vollständig abgeschlossener Serie / Valid query with no candidates | Kein Kandidat, konkreter Textgrund; keine automatische Folgeaktion / No candidate, textual reason, no follow-on action | 0 |

Die ursprünglichen drei Fixture-Kommandos bleiben bei korrektem erwarteten Ergebnis Exit 0. Die neue Testsuite endet ebenfalls mit 0, wenn negative Kindprozesse den erwarteten Fehlercode und Grund liefern; sie muss deren echte Codes separat protokollieren. Ein `expectedOutcome` darf keine Providerstörung oder Parserabweichung in Erfolg umwandeln. / *The three original fixture commands retain exit zero for correct expectations. The new test suite also returns zero when negative child processes produce expected errors, but must log those actual child exits separately. Expected outcome cannot convert a provider fault or parse failure into success.*

## Reuse und Ausgabe / Reuse and output

Die Feature-Oberfläche prüft zuerst Pfade, doppelte Schlüssel, Typen und Werte. Danach nutzt sie die bestehenden Regeln/Validatoren ohne kopierte Graphlogik. Semantische Ergebnisbildung hängt nicht von `expectedOutcome` ab; dieses Feld prüft ausschließlich die Fixture-Erwartung. / *Validate paths, duplicate keys, types, and values first, then reuse existing rules/validators without copying graph logic. Expected outcome is only a fixture assertion and never an input to classification.*

Bei Series-Aufrufen bleibt die Bedeutung des vorhandenen Summary erhalten; Listen werden nach dem Datenmodell deterministisch geordnet. Der Prüfadapter kann `reviewState=NotAssessed` berichten; das tatsächliche Status-Verfahren validiert vorhandene Review-/Receiptbindungen gesondert. Er behauptet keinen vollständigen menschlichen Statusreview. / *Series calls preserve existing summary semantics and order lists deterministically as specified in the data model. The adapter may report NotAssessed for review state; the actual status procedure validates existing review/receipt bindings separately. It does not claim a complete human status review.*

Dateien, Run-State, Manifest, Receipts und Lifecycle bleiben bytegleich; keine automatisch geschriebenen Logs, Cachedateien oder Bytecode. Temporäre Fixtures entstehen nur im Testharness und werden vom Abfrageprozess getrennt bilanziert. Fehlertexte zeigen keine Secrets, personenbezogenen Daten, Rohbefehle oder Stacktraces. Einzig akzeptierter Umgang mit unsicherer Evidence ist Stop und erneute Prüfung. / *Files and states stay byte-identical; no automatic logs, caches, or bytecode. Temporary fixtures belong to the test harness and are accounted separately. Errors reveal no secrets, personal data, raw commands, or stack traces. Unsafe evidence triggers stop and reassessment.*

## Sichere Wiederverwendung / Safe reuse

Die Pfadgrenze gilt für **jeden gelesenen Pfad**, nicht nur `--fixture` oder `--series`: Kriterienvertrag, Manifestziele, Lifecycle-Dateien und deren `archivedPath`, sowie tatsächlich gelesene Receipt-/Review-/Evidence-Verweise. Vor dem Lesen relative Pfade plattformneutral prüfen; absolute POSIX-/Windows-/UNC-Pfade, Laufwerksrelative Pfade, `..`, NUL und Symlink-Ausbruch ablehnen. Aufgelöste Dateien müssen regulär und innerhalb der expliziten Repository-Wurzel bleiben. Unbekannte Fixture-Felder und freie sensible Rohwerte werden abgewiesen, nicht angezeigt oder ausgeführt. / *The boundary covers every file read, including nested targets, lifecycle archives and any consumed receipt/review/evidence reference. Before reading, reject absolute POSIX/Windows/UNC paths, drive-relative paths, traversal, NUL and escaping symlinks. Resolved files must be regular and inside the explicit repository root. Reject unknown fixture fields and unsafe free-form values without echoing or executing them.*

Technisch wiederverwendbar sind `meets_parallel_eligibility` und `validate_manifest`. Die Series-Engine wird als isolierte Modulinstanz ohne Bytecode geladen. Ihr zentraler `normalized_bytes`-Lesepunkt und JSON-Lader müssen durch die geprüfte Lesegrenze laufen, bevor `validate_manifest` Daten konsumiert; Metadatenpfade werden vor Dateiabfragen geprüft. Dadurch bleiben Graph-/Hashregeln unverändert und transitive Reads können die Grenze nicht umgehen. Kein ungeschützter externer Aufruf für nicht vorgeprüfte Eingaben, keine Mutation des installierten Moduls auf Platte. Parserfehler, Typfehler oder bekannte Validator-Ausnahmen werden zu sicheren `ProductFailure`-Diagnosen, echte Prozess-/Runtimeausfälle zu `ProviderFailure`. / *Reuse the named functions in an isolated module instance without bytecode. Route the central byte reader and JSON loader through the guarded boundary before validation; check metadata paths before file queries. Preserve graph/hash rules and prevent nested reads from bypassing containment. Do not invoke an unguarded child for unchecked inputs or change installed files. Parse/type/known validation failures produce safe product diagnostics; actual runtime/process failures produce provider diagnostics.*

Die Negativsuite prüft zusätzlich Symlinks in Targets und Lifecycle-Archiven, Windows-Pfadformen auch auf POSIX, doppelte Schlüssel in transitiv gelesenem JSON und sensible Sentinel-Werte. Sie weist nach, dass kein externer Dateiinhalt gelesen und kein Sentinel ausgegeben wird. Bei einer Plattform ohne nutzbare Symlinks bleibt dieser native Teilbeleg offen; er darf nicht als Pass übersprungen werden. / *Add nested target/archive symlinks, Windows path forms on POSIX, duplicate keys in transitively read JSON and sensitive sentinels. Prove no external contents are read or echoed. If native symlinks are unavailable, expose that proof gap rather than marking a skip as pass.*
