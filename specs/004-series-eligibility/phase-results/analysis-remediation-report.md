# Begrenzte Plan-Remediation / Bounded Plan Remediation

**Datum / Date:** 2026-09-13. **Feature:** `004-series-eligibility`.
**Run:** `8b306e28-51eb-4510-afbc-5056b9aee328`. **Phase:** `analysis-remediation`.

Die acht beauftragten Findings sind lokal in den Planungsartefakten korrigiert. Der Abschluss dieser Phase bedeutet keine Implementierungsfreigabe: Der Runner muss die neue Taskbindung übernehmen und `analyze-2` mit aktuellem Input-/Payloadhash prüfen. Der ursprüngliche [Analyze-Bericht](analyze-report.md) und sämtliche früheren Phase-Ergebnisse bleiben unverändert. / *The eight authorized findings are corrected in local planning artifacts. Phase completion is not implementation approval: the runner must adopt the new task binding and run analyze-2 against current inputs and payload. Preserve the original analysis and every previous phase result.*

## Dispositionen / Dispositions

| Finding | Korrektur und konkrete Evidence / Correction and evidence |
|---|---|
| C001 | `constitution.md` und `.specify/memory/constitution.md` bytegleich; lokale AOC-Zeile unter Prinzip X mit Python 3.9+/Bash 5+/PowerShell 7+, vorhandenen Tests, Docs/A11Y, Statistik 80/125 Methodik v2 und allen fünf Agentenflächen plus Spec-Kit. CR-001, Plan und T003 daran gebunden. / Identical copies and factual local registry row bind spec, plan and preflight. |
| C002 | T005, Plan und Research R4/R5 verwenden bereits etabliertes `unittest` nach Feature 003 und bestehende Sequencing-/CI-Flächen; nur zusätzliche Testfälle, kein neues Framework, Paket oder Harness-/CI-Familie. / Reuse established tooling for additional cases only. |
| C003 | Research R8 und T051–T057: Feature-Merge, gepaarte Preview/Validierung, genau ein Lifecycle-Rename-PR mit nötigen aktuellen Bindungen, danach Retrospektiv-/Closeout-PR und finaler Sync. Historie, Intake-Inhalt und Series-Semantik bleiben erhalten. / Proven predecessor delivery order, preserved content and lineage. |
| C004 | Neue T008 direkt nach T007; Hilfe beider Renderer, gepaarte Vorschau, einmal Rendern und beide Check-Modi mit tatsächlicher Git-Quellrevision. 57 fortlaufende ungeprüfte Implementierungs-/Lieferaufgaben. / Immediate statistics boundary with real source revision; 57 pending tasks. |
| I001 | T001 bindet `phase-results/analyze-report.md` und den aktuellen `analyze-2.result.json`-Runner-Pass mit Outcome, Gates, Attempt und Input-/Payloadhashes. / Exact current passing analysis binding is mandatory. |
| I002 | Fünf unveränderte Evidence-Ziele haben Produzenten: T007/T050, T049, T038, T008/T016/T022/T031/T040/T055 und T042/T055. Rohlogs ergänzen die kanonischen Reviews, ersetzen sie nicht. / Explicit producers retain all five canonical review destinations alongside raw logs. |
| O001 | Alle Katalog-IDs haben Ausführungsklasse, Aufgaben, Phase und Plattformen. T029/T048 nur native automatisierte Gates; Render ausschließlich Statistikgrenzen; Providerlogs T049 erst mit beobachteten IDs. Alle bisherigen Befehle und Pflicht-Tokens erhalten. / Explicit execution placement preserves every original command and gate token. |
| L001 | Tasks und Traceability nennen CR-001–014; siebenteilige Retrospektive und Hash-/Quelltrend unverändert. / Complete range with unchanged retrospective obligations. |

## Amendment und Umfang / Amendment and scope

Version 1.21.4 ist eine lokale Tatsachenklarstellung nach bestehendem Prinzip X, keine neue gemeinsame Regel und keine Ausnahme für Testwerkzeuge. Der Sync Impact Report dokumentiert Autorität, Quellen, geprüfte Templates und Agentenflächen. `Last Amended` bleibt bis zur tatsächlichen Lieferung beim letzten beobachteten Amendment-Mergedatum 2026-09-12. T054 ergänzt nach beobachtetem Feature-Merge dessen tatsächliches Datum in beiden Kopien. Ein heutiger PR oder Merge wird nicht behauptet. / *The local patch clarifies facts under existing Principle X without changing shared rules or granting a testing exception. Sync metadata records authority and reviewed surfaces; retain the last observed amendment date until actual delivery and record the observed feature-merge date at T054. No PR or merge happened in this phase.*

Genau neun Kriterien, sechs Modi, akzeptierte Intake-Entscheidungen und Quellhashes bleiben unverändert. `MergeAndSync` und der bereits begrenzte Admin-Bypass bleiben Lieferbedingungen: ausschließlich verbleibende menschliche Approval-Barriere, technisch grüne Gates, null bearbeitbare Threads und aktuelle Autorität. Keine Feature-Codeänderung, Implementierung, Commit, Push, Merge, Preset-Promotion, Level-0-Mutation, Provider-Administration oder neuer Lauf. / *Preserve all domain and delivery constraints, including the narrowly bounded human-approval bypass. No implementation or delivery action is performed.*

## Validierung und Grenzen / Validation and limits

Die [Ausführungsprotokolle](analysis-remediation-execution.json) erfassen Befehle und unmittelbare Exits. Die [Vertragsprüfung](analysis-remediation-validation.json) bindet Artefakte, Quellen, Aufgaben, Gate-Tokens, Evidence-Produzenten und Ausführungsklassen. Die [Checkliste](../checklists/analysis-remediation.md) dokumentiert den lokalen semantischen Abgleich. Native Linux-/Windows-Feature-Abnahme, Statistik-Rendering und Remote-Evidence gehören weiterhin zur späteren Implementierung/Lieferung. / *Execution records contain commands and immediate exits; contract validation binds artifacts, inputs, tasks, tokens, producers and execution placement. The checklist records local semantic review. Native feature acceptance, rendering and remote evidence remain future work.*

Run-State-Strukturprüfungen sind keine automatische Taskhash-Reparatur: Der unveränderte Runner-State enthält noch 0/54 und den früheren Taskhash. Die aktuelle Datei hat 0/57; `runnerHandoff` in der Vertragsprüfung liefert ihre neue Bindung. Der State-Owner muss sie vor der nächsten Analyze-Bewertung übernehmen. Die bekannte Statistikdrift wird nicht als bestanden ausgegeben und bleibt an den geplanten Statistikgrenzen zu schließen; diese reine Planphase rendert keine Implementierungsstatistik. / *State schema validation does not repair task hashes. The state still has the prior 0/54 binding while current tasks are 0/57; runnerHandoff supplies the new binding for the state owner before renewed analysis. Known statistics drift remains a future gate; planning does not render implementation statistics.*

## Dokumentation und AEPS / Documentation and AEPS

Die einzige Entscheidung bleibt `UpdateRequired` im bestehenden [Dokumentationsvertrag](../contracts/documentation-impact.json). Owner: AOC Repository Owner; Quellen sind akzeptiertes Intake, bestehende Verfassung und tatsächliche lokale Test-/Governanceflächen. DE-first/EN-second, CEFR B2, textuelle Zustände und bestehende WCAG-2.2-AA-Basis bleiben unverändert. / *Retain the single documentation decision, owner, canonical sources and accessible bilingual baseline.*

Das [lokale AEPS-Handoff](analysis-remediation-aeps-receipt.md) ordnet die Korrektur bestehender Findings ein, ohne neue Candidate-ID oder Promotion. Bereits vorhandene AEPS-Arbeitsbaumänderungen bleiben unberührt; der koordinierende Owner übernimmt diesen Nachweis beim autorisierten Capture vor Feature-Abnahme. / *Local AEPS handoff classifies the existing finding corrections without a new candidate or promotion; preserve prior AEPS edits and require coordinator capture before feature acceptance.*

Nächste sichere Aktion: Der koordinierende Runner übernimmt Taskhash/57er-Anzahl und validiertes Phasenergebnis, danach `analyze-2` im selben Lauf. / *Next safe action: the coordinator adopts the updated task binding and validated phase result, then runs analyze-2 in the same run.*
