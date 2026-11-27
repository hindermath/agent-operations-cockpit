# AOC · Feature-Reihenfolge und Nachweise / Feature order and evidence

## Abgeschlossene Phase 2 / Completed Phase 2

| Rang / Rank | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Completed | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](../archive/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) | — (Root / keine direkte Abhängigkeit) | [001-programmquellen-baseline](../../../specs/001-programmquellen-baseline/) |
| 2 | Completed | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](../archive/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](../archive/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) → current (`RequirementsGovernanceGate`, binding: true) | [002-portfolio-ownership](../../../specs/002-portfolio-ownership/) |
| 3 | Completed | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](../archive/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](../archive/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) → current (`RequirementsGovernanceGate`, binding: true) | [003-authoring-contract](../../../specs/003-authoring-contract/) |
| 4 | Completed | [Lastenheft_META-LH-04-Series-Eligibility.004-series-eligibility.md](../archive/Lastenheft_META-LH-04-Series-Eligibility.004-series-eligibility.md) | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](../archive/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) → current (`HardCompletionGate`, binding: true) | [004-series-eligibility](../../../specs/004-series-eligibility/) |

[META-LH-05](../history/Lastenheft_META-LH-05-Erste-Welle.md) dokumentiert die Erstellung der RAW-Welle und
ist als bindende Authoring-Voraussetzung für RAW-01 erfüllt.
*The META-LH-05 authoring milestone satisfies the RAW-01 prerequisite.*

## RAW-Feature-Serie / RAW feature series

Vor RAW-01 müssen die neun Einzelreviews und Authoring-Receipts der
RAW-Serie an ihren aktuellen Pfaden bestehen. Weitere Läufe benötigen
ihre bindenden Vorgänger, aktuelle Nachweise und einen eigenen Auftrag.
Ein `Eligible`-Eintrag bezeichnet nur den ausgewählten Kandidaten.

*Before RAW-01, all nine single reviews and authoring receipts must pass
at their current paths. Later runs also require completed binding
predecessors, current evidence and a separate request. Eligible identifies
the selected candidate.*

RAW-01 verwendet als plattformneutralen Vertrag .NET 11 (`net11.0`) mit C# 15. /
*RAW-01 uses .NET 11 (`net11.0`) with C# 15 for its platform-neutral contract.*

[Neun Einzelreviews und Receipts / Nine single reviews and receipts](../../../specs/intake-series/aoc-raw-features/review-gate.json)

Die lesende Prüfung für RAW-01 verwendet Python, Bash und PowerShell. /
*The read-only RAW-01 check uses Python, Bash and PowerShell.*

```sh
python3 scripts/validate-aoc-raw-review-gate.py
```

Die [geprüfte RAW-01-Spezifikation](../../../specs/005-reference-agentic-workspace/spec.md)
und die [Specify-Checkliste](../../../specs/005-reference-agentic-workspace/checklists/requirements.md)
dokumentieren den Specify-Stand. Die Tabelle unten zeigt die Zuordnung
abgeschlossener Features. RAW-01 bleibt `Eligible`.

*The [reviewed RAW-01 specification](../../../specs/005-reference-agentic-workspace/spec.md)
and [Specify checklist](../../../specs/005-reference-agentic-workspace/checklists/requirements.md)
record the Specify stage. The table below maps completed features. RAW-01
remains Eligible.*

RAW-05 ist `Pending`. RAW-02 → RAW-05 ist nur bevorzugt.
*RAW-05 is Pending. RAW-02 → RAW-05 is a preferred order only.*

<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Eligible | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](../active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) | — (Root / keine direkte Abhängigkeit) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 2 | Blocked | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](../active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 3 | Blocked | [Lastenheft_RAW-02-Workspace-Orchestrator.md](../active/Lastenheft_RAW-02-Workspace-Orchestrator.md) | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 4 | Blocked | [Lastenheft_RAW-04-Presentation-Fabric.md](../active/Lastenheft_RAW-04-Presentation-Fabric.md) | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 5 | Pending | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) | [Lastenheft_RAW-02-Workspace-Orchestrator.md](../active/Lastenheft_RAW-02-Workspace-Orchestrator.md) → current (`PreferredSerialOrder`, binding: false) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 6 | Blocked | [Lastenheft_RAW-06-CLI-Environment-Orchestration.md](../active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 7 | Blocked | [Lastenheft_RAW-07-Hardware-Capability-Layer.md](../active/Lastenheft_RAW-07-Hardware-Capability-Layer.md) | [Lastenheft_RAW-04-Presentation-Fabric.md](../active/Lastenheft_RAW-04-Presentation-Fabric.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 8 | Blocked | [Lastenheft_RAW-08-Workflow-Engine.md](../active/Lastenheft_RAW-08-Workflow-Engine.md) | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`AssessmentBaseline`, binding: true)<br>[Lastenheft_RAW-06-CLI-Environment-Orchestration.md](../active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 9 | Blocked | [Lastenheft_RAW-09-Preset-Evolution.md](../active/Lastenheft_RAW-09-Preset-Evolution.md) | [Lastenheft_RAW-08-Workflow-Engine.md](../active/Lastenheft_RAW-08-Workflow-Engine.md) → current (`FinalAuditInput`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->
