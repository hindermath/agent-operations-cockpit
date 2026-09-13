# Plattform- und Agentenreview / Platform and Agent Review

## Prüfstand und Scope / Review baseline and scope

`manual:parity`, T035/T037, 2026-09-13. Reviewer: Codex, lokale semantische Review-Rolle; Owner: AOC Repository Owner. [Quality-Evidence](../phase-results/quality-validation.json) bindet alle gelesenen Flächen mit Rohhashes und protokolliert aktuelle lokale Ausführungen. [US3](../phase-results/us3-tests.json) und [Runner-Evidence](../phase-results/runner-tests.json) werden als vorhandene Nachweise wiederverwendet. Keine erneute fachliche Gesamtsuite in diesem Dokumentationsschritt. / *Bound source review and actual local execution, reusing previous US3 and runner evidence without an unrelated full-suite repeat.*

## Gemeinsame Regeln / Shared rules

| Gelesene Fläche / Reviewed surface | Semantischer Befund / Semantic finding |
|---|---|
| `AGENTS.md` | Read/Status/Next bleiben lesend; Ready, Lifecycle und Ausführungsautorität getrennt. / Read-only queries and separate axes. |
| `CLAUDE.md` | Gleiche Grenze für Sequencing und explizite aktuelle Schreibautorität. / Same sequencing and current-write-authority bounds. |
| `GEMINI.md` | Gleiche Nicht-Autorität aus Installation, Ready und Reihenfolge. / Same non-authority from installation, readiness and order. |
| `.github/copilot-instructions.md` | Next meldet Ziele/Blocker und startet nichts. / Next reports candidates/blockers and starts nothing. |
| `.github/agents/copilot-instructions.md` | Gleiche Query-/Deliverygrenze und fail-closed Driftregel. / Same query/delivery and drift bounds. |
| `.specify/presets/intake-sequencing-governance/commands/speckit.intake-series-status.md` | Hashes/Status vor und nach Prüfung; beide Validatoren; Identität, Blocker, Lineage und Drift; keine Reparatur oder Ausführung. / Before/after hashes, both validators, identity/lineage/drift, no repair or execution. |
| `.specify/presets/intake-sequencing-governance/commands/speckit.intake-series-next.md` | Erst Statusvertrag; alle Kandidaten in sichtbarer Reihenfolge; höchstens ein deklarierter bevorzugter Eligible-Kandidat; bei null Kandidaten konkrete Blocker/Idle; Folgeprüfung und Autorität erst separat. / Status first, all ordered candidates, constrained preference, blockers/Idle, separate downstream authority. |
| `.specify/templates/tasks-template.md` und installierte Templates / and installed templates | Keine neue gemeinsame Regel erforderlich; tatsächliche Feature-Tasks präzisieren die akzeptierte Ausführungsgrenze. / No new shared rule required; feature tasks carry the accepted scope. |
| `constitution.md`, `.specify/memory/constitution.md` | Bytegleicher Spiegel; lokale MSL-/Python-/Shell-Basis und Atomic-Surface-Vertrag bleiben. / Byte-identical mirror, unchanged environment and atomic-surface contract. |

Disposition: Paritätsreview `Applicable / Fulfilled` im benannten Scope. Synchronisation `N/A / Not Assessed`, weil keine gemeinsame Regel geändert wurde. Alle fünf Guidance-Dateien, installierte Presets, Templates und Constitution bleiben bytegleich zum Phasenbeginn; Hashvergleich statt schreibender Paritätswerkzeuge. Trigger: neue gemeinsame Regel, neuer Agentenbefehl oder Consumer-Drift; dann Owner und exakte betroffene Flächen separat autorisieren. / *Parity review is fulfilled for this scope; synchronization is inapplicable because no shared rule changed. All protected consumers remain byte-identical. A future rule, command or consumer change triggers separately scoped owner review.*

## Abfrageaussagen und Autorität / Query statements and authority

Die tatsächlichen Agentenverträge wurden als Anweisungsdokumente gelesen; keine Agenten wurden gestartet. Status fordert mehr als die technische Adapterprojektion: unter anderem aktuelle Review-/Receipt- und Governanceprüfung. Der Adapter behauptet diesen menschlichen Gesamtstatus nicht und meldet `reviewState=NotAssessed`. Next fordert zuerst Status, danach Kandidaten und eine einzige vorgeschlagene Aktion; daraus entsteht kein ausführbarer Auftrag. / *Actual agent instruction texts were reviewed without starting agents. The full status procedure exceeds the adapter projection; NotAssessed avoids claiming that full review. Next requires status first and proposes one action without executing it.*

Der reale lokale Next-Text zeigt eine deklarierte Completed-Serie, null Kandidaten, null Präferenz, keine Blocker, Delivery/Review NotAssessed und historische Herkunft. Die Aktion verlangt erneute Prüfung mit einer verantwortlichen Person und startet nichts. Dies ist konsistent mit dem separaten Statusverfahren, aber kein Ersatz dafür. Mehrere Kandidaten, Vorgängerreihenfolge und Idle sind durch US3-Tests belegt; die aktuelle kanonische Abfrage wird nicht als Beleg für all diese Varianten umetikettiert. / *Actual local output is consistent with the separate procedure but does not replace it. US3 tests cover variants; current canonical output is not relabeled as evidence for every scenario.*

## Native Matrix / Native matrix

| Ziel / Target | Bash 5+ Help/CLI | PowerShell 7+ Help/Funktion/Dot-Sourcing | Status und Follow-up / Status and follow-up |
|---|---|---|---|
| Lokaler macOS-26.6.2-arm64-Host / Local host | Tatsächlich ausgeführt, Exit 0 / Executed, exit 0 | Tatsächlich ausgeführt, Exit 0; stiller Import, CmdletBinding, Aufrufer lebt / Silent import and surviving caller | Lokal erfüllt; Python 3.14.7, Bash 5.3.15, PowerShell 7.6.5. / Locally fulfilled. |
| Linux ubuntu-22.04 | Pass, Job 103715801136 | Pass, Job 103715801136 | Lauf 34754238229: Python 3.14.7, Bash /bin/bash, PowerShell 7.6.5; 36/36 unmittelbare Exits 0. / Run and exact versions bound; 36/36 immediate exits zero. |
| macOS macos-14 | Pass, Job 103715801045 | Pass, Job 103715801045 | Lauf 34754238229: Homebrew Bash /opt/homebrew/bin/bash, Python 3.14.7, PowerShell 7.6.4; 36/36 Exits 0. / Ephemeral Homebrew Bash and all native gates passed. |
| Windows windows-2022 | Pass, Job 103715801117 | Pass, Job 103715801117 | Lauf 34754238229: Git-for-Windows Bash, Python 3.14.7, PowerShell 7.6.5; 36/36 Exits 0. / Git Bash, strict PowerShell UTF-8 boundary and all gates passed. |

Alle sechs Shell-/OS-Kombinationen sind am Quellen-Head 02a9399536c46497c34cee840e5ae2c4fc090574 geschlossen. Die Workflows checken für die Feature-Matrix ausdrücklich den PR-Quellen-Head aus. Native Help-, Symlink-, Query-, Sequencing-, Runner-Kardinalitäts- und Analyzer-Proben wurden nicht übersprungen. Re-Evaluation bei Skript-, Pfad-, Runtime- oder Head-Drift. / *All six shell/OS combinations are closed at the named source head. The workflow explicitly checks out the PR source head, and no native help, symlink, query, sequencing, runner-cardinality, or analyzer proof was skipped. Re-evaluate on source or environment drift.*

Lokale Help-Aufrufe sind ohne Pflichtparameter erfolgreich. Dot-Sourcing erzeugt keine Ausgabe; Funktion und Skript liefern dieselbe Series-Ausgabe. Vorhandene US3-No-write/Core-Prozess-Audits und aktueller Schutzdatei-Hashvergleich stützen die Lesegrenze. Shells dürfen den Python-Prüfer delegieren; sie starten keinen Spec-Kit-/Workerprozess. / *Argument-free help succeeds; loading is silent and function/script query output matches. Existing side-effect audits and current protected-file hashes support read-only behavior; Python delegation is permitted, downstream work is not.*

[A11Y-Review](../../../docs/accessibility/series-eligibility.md) benennt Text-/Browser-/AT-Grenzen getrennt. Die native Evidence ist in [ci-evidence.json](../phase-results/ci-evidence.json) gebunden; Browser- und Assistive-Technology-Grenzen bleiben unverändert transparent. / *Accessibility review separates text, browser and assistive-technology limits. Native evidence is bound in the CI record; browser and assistive-technology limits remain explicitly unclaimed.*
