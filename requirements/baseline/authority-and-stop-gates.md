# Authority- und Stop-Gates / Authority and Stop Gates

Jedes Gate ist fail-closed: Fehlende oder veraltete Evidence ist keine
Freigabe. Ein Admin-Bypass ändert nur den Liefermechanismus und erfüllt kein
Qualitätsgate. / *Every gate is fail-closed: missing or stale evidence is not
approval. An admin bypass changes delivery mechanics only and satisfies no
quality gate.*

SHA, Ruleset, Traceability, DAG, Authoring Receipt, Eligibility, Global-ready,
Analyze, Allowlist, Domain-Vertrag, Pre-Rename-Fixpunkt und AEPS werden beim
ersten Auftreten über das [Glossar](glossary.md) erklärt. / *SHA, ruleset,
traceability, DAG, authoring receipt, eligibility, global-ready, Analyze,
allowlist, domain contract, pre-rename fixed point, and AEPS are explained at
first use through the [glossary](glossary.md).*

| Gate | Erlaubte Aktion / Allowed action | Stop-Bedingung / Stop condition | Erforderliche Evidence / Required evidence | Menschliche Entscheidung / Human decision | Genau eine sichere nächste Aktion / Exactly one safe next action |
|---|---|---|---|---|---|
| G-00 Public Readiness | Exakten geprüften Basis-SHA veröffentlichen. / Publish the exact reviewed baseline SHA. | Scan-, Lizenz-, Pfad-, Ruleset- oder Freigabelücke. / Scan, licence, path, ruleset, or approval gap. | Public-Readiness-Receipt für den exakten SHA. / Public-readiness receipt for the exact SHA. | Freigabe des Basis-SHA. / Approval of the baseline SHA. | Bei Drift stoppen und Public Readiness erneut prüfen. / Stop on drift and reassess public readiness. |
| G-01 Source Baseline | Quellen, Constraints und Findings nur in den sechs gebundenen Baseline-Dokumenten bearbeiten und prüfen. / Edit and review sources, constraints, and findings only in the six bound baseline documents. | Blocking Finding ist `Uncovered`, eine Source-ID fehlt oder ist doppelt, oder eine versteckte Level-0-Abhängigkeit entsteht. / A blocking finding is `Uncovered`, a source ID is missing or duplicated, or a hidden level-0 dependency appears. | Exakte 23-Source-, CON-01-bis-CON-25-, RF-01-bis-RF-21- und 10-Owner-Prüfung plus unabhängiger Leser- und Traceability-Test. / Exact 23-source, CON-01-through-CON-25, RF-01-through-RF-21, and ten-owner checks plus independent reader and traceability tests. | Der Mensch akzeptiert oder korrigiert die Baseline; das Gate erteilt keine Folgeautorität. / A human accepts or corrects the baseline; the gate grants no downstream authority. | Den vollständigen Level-2-Leserpfad prüfen. / Review the complete level-2 reader path. |
| G-02 Portfolio | Owner, Handoffs und DAG festlegen. / Define owners, handoffs, and the DAG. | Mehrfachowner, Zyklus oder unklare Decision. / Duplicate owner, cycle, or unclear decision. | Ownership-Matrix und DAG-Validation. / Ownership matrix and DAG validation. | Portfolio bestätigen. / Confirm the portfolio. | Bei bestandener Matrix das Portfolio-Review anfordern. / Request portfolio review after the matrix passes. |
| G-03 Authoring | Neue Intakes mit Receipts erzeugen. / Create new intakes with receipts. | Bestehendes Ziel, Secret, offene Materialentscheidung oder Validatorfehler. / Existing target, secret, open material decision, or validator failure. | Hashgebundenes Authoring-Receipt und Validator-Pass. / Hash-bound authoring receipt and validator pass. | Create- oder Update-Autorität getrennt erteilen. / Grant create or update authority separately. | Den erzeugten Intake unabhängig reviewen lassen. / Submit the created intake for independent review. |
| G-04 Series Eligibility | Reihenfolge und Autonomiemodus empfehlen. / Recommend order and autonomy mode. | Gemeinsame Writes, Decision-Abhängigkeit oder fehlendes Review beziehungsweise Recovery. / Shared writes, decision dependency, or missing review or recovery. | Eligibility-Receipt und azyklischer Graph. / Eligibility receipt and acyclic graph. | Parallelität ausdrücklich freigeben. / Explicitly approve parallelism. | Das nächste eligible Ziel nur melden. / Report only the next eligible target. |
| G-05 Global Review / Specify | Erst nach aktueller `Ready`-Coverage aller 14 AOC-Lastenhefte genau META-LH-01 als erstes Ziel an Specify übergeben. / Only after current `Ready` coverage of all 14 AOC intakes, pass exactly META-LH-01 as the first target to Specify. | Mindestens ein Ziel ist nicht `Ready`, Target, Hash, Receipt oder Bash-/PowerShell-Evidence driftet, ein Review ist supersediert, oder der ausdrückliche Startauftrag fehlt. / Any target is not `Ready`, target, hash, receipt, or Bash/PowerShell evidence drifts, a review is superseded, or the explicit start instruction is missing. | Frischer `global-ready`-Pass für 14 logische Ziele mit META-LH-01 zuerst sowie aktuelle Receipts und Single-Reviews. / Fresh `global-ready` pass for 14 logical targets with META-LH-01 first plus current receipts and Single reviews. | Nach vollständiger Coverage erteilt ein Mensch einen separaten Startauftrag; G-05 erteilt keine G-06-Autorität. / After full coverage, a human grants a separate start instruction; G-05 grants no G-06 authority. | Den ausdrücklich autorisierten META-LH-01-Workflow starten. / Start the explicitly authorised META-LH-01 workflow. |
| G-06 Implementation | Ausschließlich die dokumentarische META-LH-01-Baseline und feature-lokale Workflow-Evidence nach akzeptiertem Plan und Tasks umsetzen. / Implement only the documentary META-LH-01 baseline and feature-local workflow evidence under the accepted plan and tasks. | Security-, A11Y-, Sprach-, Scope-, Input-Binding-, Review- oder Evidence-Gate ist offen oder driftet. / A security, accessibility, language, scope, input-binding, review, or evidence gate is open or drifts. | Aktuelle Benutzerautorität, Analyze `Ready`, frischer Global-Ready-Pass, exakte Allowlist, Domain-Vertrag und unabhängige Reviews. / Current user authority, Analyze `Ready`, fresh global-ready pass, exact allowlist, domain contract, and independent reviews. | Ein separater Implementierungsauftrag begrenzt die Writes; Produktcode, Produktarchitektur, Scaffold, Preset-Promotion und implizite Remote-Autorität bleiben ausgeschlossen. / A separate implementation instruction bounds writes; product code, product architecture, scaffolding, preset promotion, and implicit remote authority remain excluded. | Bis zum lokalen Pre-Rename-Fixpunkt implementieren und dort stoppen. / Implement through the local pre-rename fixed point and stop there. |
| G-07 Command/Hardware | Reversible Commands oder Geräteadapter entwickeln. / Develop reversible commands or device adapters. | Read-only Slice ist nicht stabil oder Trust und Recovery sind offen. / The read-only slice is unstable or trust and recovery remain open. | Eigene Produkt-Decision und positive sowie negative Tests. / Separate product decision and positive and negative tests. | Eigene Lastenheftfreigabe. / Separate intake approval. | Die erforderliche Produkt-Decision vorbereiten. / Prepare the required product decision. |
| G-08 Preset Evolution | Generalisierbare Evidence in einen Preset-Vorschlag übergeben. / Transfer generalisable evidence into a preset proposal. | Evidence ist nur projektspezifisch oder enthält eine Produktentscheidung. / Evidence is only project-specific or contains a product decision. | Wiederholbare Cross-Project-Evidence und aktuelle Upstream-Autorität. / Repeatable cross-project evidence and current upstream authority. | Separate Preset-Promotion und Level-0-Handoff-Freigabe. / Separate preset-promotion and level-0-handoff approval. | Ohne separate Freigabe nur ein lokales AEPS-Receipt erfassen. / Without separate approval, record only a local AEPS receipt. |

## AOC-weite Review-Sperre / AOC-wide review gate

G-05 ist für die kanonische AOC-Programmreihe ein globales, fail-closed Gate.
Alle 14 Lastenhefte META-LH-01 bis META-LH-05 und RAW-01 bis RAW-09 müssen
gleichzeitig ein aktuelles, formal validiertes `Ready`-Single-Review besitzen.
Zielpfad und normalisierter Zielhash müssen dem logischen Lastenheft
entsprechen; Authoring Receipt und Bash- sowie PowerShell-Validierung müssen
aktuell sein. `ReadyWithAcceptedRisks`, supersedierte Ergebnisse und
Series-Lifecycle-Werte erteilen keine Ausnahme. / *G-05 is a global,
fail-closed gate for the canonical AOC programme. All 14 META and RAW intakes
must simultaneously have a current, formally validated `Ready` Single review
with matching logical target path, normalised hash, current Authoring Receipt,
and passing Bash and PowerShell validation. Accepted-risk or superseded results
and series lifecycle values grant no exception.*

Vor vollständiger Coverage bleiben Specify, Autonomous, Parallel Autonomous
und Implementierung gesperrt. Danach bleibt META-LH-01 das zwingende erste Ziel
und benötigt einen neuen ausdrücklichen Startauftrag. Änderungen an Ziel oder
Review-Evidence schließen das Gate erneut. Review, Series-Lifecycle,
Global-Gate-Status und konkrete Ausführungsautorität sind getrennte Wahrheiten.
/ *Before full coverage, Specify, autonomous, parallel-autonomous, and
implementation work remain blocked. Afterwards META-LH-01 is still the
mandatory first target and needs a new explicit start instruction. Any target
or review-evidence drift closes the gate again. Review, series lifecycle,
global-gate status, and execution authority remain separate truths.*

Der Leserpfad endet hier. Die einzige sichere nächste Aktion in dieser Phase
ist der lokale, ausdrücklich autorisierte Pre-Rename-Validierungsabschluss;
Staging, Commit, Rename und Remote-Aktionen gehören zu späteren Aufgaben. /
*The reader path ends here. The only safe next action in this phase is the
explicitly authorised local pre-rename validation closeout; staging, commit,
rename, and remote actions belong to later tasks.*
