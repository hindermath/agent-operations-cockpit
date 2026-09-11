# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

## AOC-Programmreihe / AOC programme series

Für das eigenständige AOC-Lastenheftprogramm ist die kanonische,
SHA-gebundene Reihenfolge unter
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md)
festgelegt. Der Einstieg und Status aller Meta- und Fachreihen steht in
[`Pflichtenheft.md`](Pflichtenheft.md). Die unten automatisch ermittelte
Root-Tabelle betrifft ausschließlich ältere Root-Intakes und besitzt keine
Authority über die AOC-Series.

*The canonical, hash-bound AOC programme order is defined in
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md).
[`Pflichtenheft.md`](Pflichtenheft.md) is the programme index. The automatically
generated root table below covers legacy root intakes only and has no authority
over the AOC series.*

Für diese AOC-Programmreihe gilt eine globale Review-Sperre: Alle 14 Meta- und
Fachlastenhefte müssen aktuelle, formal validierte `Ready`-Single-Reviews
besitzen, bevor ein `speckit specify`-, Autonomous-, Parallel-Autonomous- oder
Implementierungslauf starten darf. Danach bleibt `META-LH-01` das erste Ziel und
benötigt einen neuen ausdrücklichen Startauftrag. Drift schließt die Sperre
erneut. Die zwei älteren Root-Intakes in der generierten Tabelle sind nicht Teil
dieser 14er-Gesamtmenge.

*The AOC programme has a global review gate: all 14 META and RAW intakes require
current formally validated Ready Single reviews before downstream Spec Kit work
may start. `META-LH-01` remains the first target and needs a new explicit start
instruction. Drift closes the gate again. The two generated legacy root intakes
are outside this fourteen-intake set.*

<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Completed | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) | — (Root / keine direkte Abhängigkeit) | [001-programmquellen-baseline](specs/001-programmquellen-baseline/) |
| 2 | Completed | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) → current (`RequirementsGovernanceGate`, binding: true) | [002-portfolio-ownership](specs/002-portfolio-ownership/) |
| 3 | Completed | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) → current (`RequirementsGovernanceGate`, binding: true) | [003-authoring-contract](specs/003-authoring-contract/) |
| 4 | Completed | [Lastenheft_META-LH-04-Series-Eligibility.md](requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md) | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 5 | Completed | [Lastenheft_META-LH-05-Erste-Welle.md](requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md) | [Lastenheft_META-LH-04-Series-Eligibility.md](requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 6 | Completed | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) | [Lastenheft_META-LH-05-Erste-Welle.md](requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md) → current (`RequirementsGovernanceGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 7 | Completed | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 8 | Completed | [Lastenheft_RAW-02-Workspace-Orchestrator.md](requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md) | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 9 | Completed | [Lastenheft_RAW-04-Presentation-Fabric.md](requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md) | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 10 | Completed | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) | [Lastenheft_RAW-02-Workspace-Orchestrator.md](requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md) → current (`PreferredSerialOrder`, binding: false) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 11 | Completed | [Lastenheft_RAW-06-CLI-Environment-Orchestration.md](requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 12 | Completed | [Lastenheft_RAW-07-Hardware-Capability-Layer.md](requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md) | [Lastenheft_RAW-04-Presentation-Fabric.md](requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 13 | Completed | [Lastenheft_RAW-08-Workflow-Engine.md](requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md) | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`AssessmentBaseline`, binding: true)<br>[Lastenheft_RAW-06-CLI-Environment-Orchestration.md](requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 14 | Completed | [Lastenheft_RAW-09-Preset-Evolution.md](requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md) | [Lastenheft_RAW-08-Workflow-Engine.md](requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md) → current (`FinalAuditInput`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->
