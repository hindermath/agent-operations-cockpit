# AOC Phase-2 Lastenheft-Abarbeitungsreihenfolge / AOC Phase 2 Intake Processing Order

## Begriffe und Status / Terms and status

- **Root:** Intake ohne eingehende Kante; hier `META-LH-01`.
- **Bindende Kante / binding edge:** Vorgänger muss `Completed` sein.
- **Bevorzugte Reihenfolge / preferred order:** Empfehlung ohne fachliches Blockieren.
- **Eligible:** formal nächster Kandidat; startet keine Arbeit.
- **Blocked:** offene Decision, Authority oder Evidence verhindert den Start.

*The ordered text and dependency list are normative. Eligibility never starts work.*

## Globale Review-Sperre / Global review gate

Für die gesamte AOC-Programmreihe gilt vor jeder nachgelagerten Ausführung eine
zusätzliche fail-closed Sperre. Alle 14 `orderedTargets` müssen jeweils ein
aktuelles, formal validiertes `Ready`-Single-Review besitzen. Zielpfad,
normalisierter Zielhash, Authoring Receipt sowie Bash- und
PowerShell-Validierung müssen aktuell sein. `ReadyWithAcceptedRisks`,
supersedierte Ergebnisse und die Lifecycle-Werte `Pending`, `Eligible`,
`Blocked` oder `Completed` ersetzen diese Gesamtprüfung nicht.

Solange auch nur ein Ziel diese Bedingungen nicht erfüllt, bleiben
`speckit specify`, Autonomous, Parallel Autonomous und Implementierung für alle
14 Ziele gesperrt. Nach vollständiger Review-Coverage ist `META-LH-01` das erste
erlaubte Ziel und benötigt weiterhin einen neuen ausdrücklichen Startauftrag.
Jede spätere Ziel- oder Evidence-Drift schließt die Sperre erneut. Die älteren
Root-Lastenhefte gehören nicht zu dieser AOC-Programmreihe.

*Before any downstream execution, every one of the 14 ordered targets requires
a current, formally validated `Ready` Single review with matching target,
normalised hash, Authoring Receipt, and Bash and PowerShell validation.
Accepted-risk or superseded results and lifecycle values do not pass. One
missing or stale result blocks Specify, autonomous, parallel-autonomous, and
implementation work for the whole programme. Once all 14 pass, `META-LH-01` is
the first target and still needs a new explicit start instruction. Any later
drift closes the gate again. Legacy root intakes are out of scope.*

## Reihenfolge / Order

| Position | Intake | Status | Zweck / Purpose |
|---:|---|---|---|
| 1 | `Lastenheft_META-LH-01-Programmquellen.md` | Completed | eigenständige Quellenbaseline |
| 2 | `Lastenheft_META-LH-02-Portfolio-Ownership.md` | Completed | Owner und Handoffs |
| 3 | `Lastenheft_META-LH-03-Authoring-Contract.md` | Completed | Authoring-/Receipt-Vertrag |
| 4 | `Lastenheft_META-LH-04-Series-Eligibility.md` | Completed | DAG und Autonomie |
| 5 | `Lastenheft_META-LH-05-Erste-Welle.md` | Completed | neun fachliche Intakes |
| 6 | `Lastenheft_RAW-01-Reference-Agentic-Workspace.md` | Completed | read-only Referenzslice |
| 7 | `Lastenheft_RAW-03-State-Truthfulness.md` | Completed | Zustandssemantik |
| 8 | `Lastenheft_RAW-02-Workspace-Orchestrator.md` | Completed | Orchestration; IAD201–203 bestätigt |
| 9 | `Lastenheft_RAW-04-Presentation-Fabric.md` | Completed | zugängliche Projektionen |
| 10 | `Lastenheft_RAW-05-Execution-Nodes.md` | Completed | Host-/Sandbox-Grenzen |
| 11 | `Lastenheft_RAW-06-CLI-Environment-Orchestration.md` | Completed | CLI; IAD601–604 |
| 12 | `Lastenheft_RAW-07-Hardware-Capability-Layer.md` | Completed | Hardware; IAD701–704 bestätigt |
| 13 | `Lastenheft_RAW-08-Workflow-Engine.md` | Completed | Knowledge Workflow |
| 14 | `Lastenheft_RAW-09-Preset-Evolution.md` | Completed | Preset Proposal; IAD901–902 bestätigt |

Alle logischen Pfade liegen unter `requirements/intakes/active/`. Der logische
Pfad von META-LH-01 wird über den eindeutigen, hashgebundenen Lifecycle-Vertrag
`specs/001-programmquellen-baseline/intake-lifecycle.json` auf den physischen
Archivpfad aufgelöst. Die fachliche Nummerierung benennt Owner-Reihen; die
Verarbeitungsposition folgt dem Abhängigkeitsgraphen und kann deshalb RAW-03
vor RAW-02 führen.

*All logical paths are below `requirements/intakes/active/`. The logical
META-LH-01 path is resolved to its physical archive path through the unique,
hash-bound lifecycle contract. Domain numbering identifies owner series;
processing order follows dependencies and may therefore place RAW-03 before
RAW-02.*

## Bindende Abhängigkeiten / Binding dependencies

1. META-01 → META-02 → META-03 → META-04 → META-05.
2. META-05 → RAW-01 → RAW-03.
3. RAW-03 → RAW-02 und RAW-04.
4. RAW-05 → RAW-06.
5. RAW-04 → RAW-07.
6. RAW-05 und RAW-06 → RAW-08 → RAW-09.

RAW-02 → RAW-05 ist nur bevorzugte Reihenfolge: read-only Node Research darf
vor der Orchestrator-Implementierung Erkenntnisse erzeugen. / *RAW-02 to RAW-05
is preferred only, so read-only node research may proceed earlier.*

## Nächster Kandidat und Blocker / Next candidate and blockers

META-LH-01 bis META-LH-05 sowie RAW-01 bis RAW-09 sind nach aktueller
`Ready`-Single-Review-Evidence im Manifest `Completed`. Es gibt keinen
`Eligible`-Kandidaten und keinen Lifecycle-Blocker. Das vollständige aktuelle
Series Review `ed06821a-bf3d-438a-96ca-d85eb5f8cb8a` ist `Ready`; der
ausdrücklich autorisierte Statuswechsel setzt deshalb auch den deklarierten
Serienstatus auf `Completed`. Dieser Abschluss startet keine Folgearbeit und
erteilt keine Review-, Specify-, Implementierungs-, Remote-, Merge-, Bypass-,
Preset- oder Promotion-Authority.

*META-LH-01 through META-LH-05 and RAW-01 through RAW-09 are `Completed` after
current Ready Single-review evidence. No Eligible candidate or lifecycle
blocker remains. Complete current Series review
`ed06821a-bf3d-438a-96ca-d85eb5f8cb8a` is `Ready`; the explicitly authorised
transition therefore also sets the declared Series status to `Completed`.
This completion starts no downstream work and grants no downstream or
promotion authority.*


<!-- secure-development-hardening-order:start -->
## Verlinkte Lastenheft-Reihenfolge / Linked Requirements Order

Diese Tabelle wird aus dem kanonischen Series-Manifest und ausdruecklicher Feature-Evidence erzeugt. Vollstaendige Dateinamen, direkte eingehende Kanten und sichtbare Positionen bleiben erhalten. Manuelle Abschnitte ausserhalb dieses Markers bleiben unberuehrt.

*This table is generated from the canonical series manifest and explicit feature evidence. Complete filenames, direct incoming edges, and visible positions are preserved. Manual sections outside this marker remain unchanged.*

| Position | Status | Lastenheft/Intake | Abhängigkeiten / Dependencies | Spec-Kit-Feature |
|---:|---|---|---|---|
| 1 | Completed | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](../active/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) | — (Root / keine direkte Abhängigkeit) | [001-programmquellen-baseline](../../../specs/001-programmquellen-baseline/) |
| 2 | Completed | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](../active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) | [Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md](../active/Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md) → current (`RequirementsGovernanceGate`, binding: true) | [002-portfolio-ownership](../../../specs/002-portfolio-ownership/) |
| 3 | Completed | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](../active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) | [Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md](../active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md) → current (`RequirementsGovernanceGate`, binding: true) | [003-authoring-contract](../../../specs/003-authoring-contract/) |
| 4 | Completed | [Lastenheft_META-LH-04-Series-Eligibility.md](../active/Lastenheft_META-LH-04-Series-Eligibility.md) | [Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md](../active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 5 | Completed | [Lastenheft_META-LH-05-Erste-Welle.md](../active/Lastenheft_META-LH-05-Erste-Welle.md) | [Lastenheft_META-LH-04-Series-Eligibility.md](../active/Lastenheft_META-LH-04-Series-Eligibility.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 6 | Completed | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](../active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) | [Lastenheft_META-LH-05-Erste-Welle.md](../active/Lastenheft_META-LH-05-Erste-Welle.md) → current (`RequirementsGovernanceGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 7 | Completed | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) | [Lastenheft_RAW-01-Reference-Agentic-Workspace.md](../active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 8 | Completed | [Lastenheft_RAW-02-Workspace-Orchestrator.md](../active/Lastenheft_RAW-02-Workspace-Orchestrator.md) | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 9 | Completed | [Lastenheft_RAW-04-Presentation-Fabric.md](../active/Lastenheft_RAW-04-Presentation-Fabric.md) | [Lastenheft_RAW-03-State-Truthfulness.md](../active/Lastenheft_RAW-03-State-Truthfulness.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 10 | Completed | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) | [Lastenheft_RAW-02-Workspace-Orchestrator.md](../active/Lastenheft_RAW-02-Workspace-Orchestrator.md) → current (`PreferredSerialOrder`, binding: false) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 11 | Completed | [Lastenheft_RAW-06-CLI-Environment-Orchestration.md](../active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 12 | Completed | [Lastenheft_RAW-07-Hardware-Capability-Layer.md](../active/Lastenheft_RAW-07-Hardware-Capability-Layer.md) | [Lastenheft_RAW-04-Presentation-Fabric.md](../active/Lastenheft_RAW-04-Presentation-Fabric.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 13 | Completed | [Lastenheft_RAW-08-Workflow-Engine.md](../active/Lastenheft_RAW-08-Workflow-Engine.md) | [Lastenheft_RAW-05-Execution-Nodes.md](../active/Lastenheft_RAW-05-Execution-Nodes.md) → current (`AssessmentBaseline`, binding: true)<br>[Lastenheft_RAW-06-CLI-Environment-Orchestration.md](../active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) → current (`HardCompletionGate`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
| 14 | Completed | [Lastenheft_RAW-09-Preset-Evolution.md](../active/Lastenheft_RAW-09-Preset-Evolution.md) | [Lastenheft_RAW-08-Workflow-Engine.md](../active/Lastenheft_RAW-08-Workflow-Engine.md) → current (`FinalAuditInput`, binding: true) | — (kein Spec-Kit-Feature / no Spec Kit feature) |
<!-- secure-development-hardening-order:end -->
