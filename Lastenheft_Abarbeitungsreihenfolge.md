# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

## AOC-Programmreihe / AOC programme series

Für das eigenständige AOC-Lastenheftprogramm ist die kanonische,
SHA-gebundene Reihenfolge unter
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md)
festgelegt. Der Index [`Pflichtenheft.md`](Pflichtenheft.md) führt Features,
Authoring und Backlog. Die Tabelle unten zeigt die abgeschlossene Feature-Serie.

*The canonical, hash-bound AOC programme order is defined in
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md).
[`Pflichtenheft.md`](Pflichtenheft.md) indexes features, authoring and backlog.
The table below lists the completed feature series.*

RAW-01 ist der einzige ausgewählte Kandidat der neuen RAW-Serie. / *RAW-01 is the sole selected candidate of the new RAW series.*

Vor RAW-01 müssen die neun Einzelreviews und Authoring-Receipts der
RAW-Serie an ihren aktuellen Pfaden bestehen. Weitere Läufe benötigen
ihre bindenden Vorgänger, aktuelle Nachweise und einen eigenen Auftrag.
Ein `Eligible`-Eintrag bezeichnet nur den ausgewählten Kandidaten.

*Before RAW-01, all nine single reviews and authoring receipts must pass
at their current paths. Later runs also require completed binding
predecessors, current evidence and a separate request. Eligible identifies
the selected candidate.*

<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Eligible | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) | — (Root / keine direkte Abhängigkeit) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 2 | Blocked | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 3 | Blocked | [Lastenheft_RAW-02-Workspace-Orchestrator.md](requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md) | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 4 | Blocked | [Lastenheft_RAW-04-Presentation-Fabric.md](requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md) | [Lastenheft_RAW-03-State-Truthfulness.md](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 5 | Pending | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) | [Lastenheft_RAW-02-Workspace-Orchestrator.md](requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md) → current (`PreferredSerialOrder`, binding: false) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 6 | Blocked | [Lastenheft_RAW-06-CLI-Environment-Orchestration.md](requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 7 | Blocked | [Lastenheft_RAW-07-Hardware-Capability-Layer.md](requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md) | [Lastenheft_RAW-04-Presentation-Fabric.md](requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 8 | Blocked | [Lastenheft_RAW-08-Workflow-Engine.md](requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md) | [Lastenheft_RAW-05-Execution-Nodes.md](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`AssessmentBaseline`, binding: true)<br>[Lastenheft_RAW-06-CLI-Environment-Orchestration.md](requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 9 | Blocked | [Lastenheft_RAW-09-Preset-Evolution.md](requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md) | [Lastenheft_RAW-08-Workflow-Engine.md](requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md) → current (`FinalAuditInput`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->
