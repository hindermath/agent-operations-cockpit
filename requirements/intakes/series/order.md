# AOC Phase-2 Lastenheft-Abarbeitungsreihenfolge / AOC Phase 2 Intake Processing Order

## Begriffe und Status / Terms and status

- **Root:** Intake ohne eingehende Kante; hier `META-LH-01`.
- **Bindende Kante / binding edge:** Vorgänger muss `Completed` sein.
- **Bevorzugte Reihenfolge / preferred order:** Empfehlung ohne fachliches Blockieren.
- **Eligible:** formal nächster Kandidat; startet keine Arbeit.
- **Blocked:** offene Decision, Authority oder Evidence verhindert den Start.

*The ordered text and dependency list are normative. Eligibility never starts work.*

## Reihenfolge / Order

| Position | Intake | Status | Zweck / Purpose |
|---:|---|---|---|
| 1 | `Lastenheft_META-LH-01-Programmquellen.md` | Completed | eigenständige Quellenbaseline |
| 2 | `Lastenheft_META-LH-02-Portfolio-Ownership.md` | Completed | Owner und Handoffs |
| 3 | `Lastenheft_META-LH-03-Authoring-Contract.md` | Completed | Authoring-/Receipt-Vertrag |
| 4 | `Lastenheft_META-LH-04-Series-Eligibility.md` | Completed | DAG und Autonomie |
| 5 | `Lastenheft_META-LH-05-Erste-Welle.md` | Completed | neun fachliche Intakes |
| 6 | `Lastenheft_RAW-01-Reference-Agentic-Workspace.md` | Eligible | read-only Referenzslice |
| 7 | `Lastenheft_RAW-03-State-Truthfulness.md` | Pending | Zustandssemantik |
| 8 | `Lastenheft_RAW-02-Workspace-Orchestrator.md` | Blocked | Orchestration; IAD201–203 bestätigt, wartet auf RAW-01/03 |
| 9 | `Lastenheft_RAW-04-Presentation-Fabric.md` | Pending | zugängliche Projektionen |
| 10 | `Lastenheft_RAW-05-Execution-Nodes.md` | Pending | Host-/Sandbox-Grenzen |
| 11 | `Lastenheft_RAW-06-CLI-Environment-Orchestration.md` | Blocked | CLI; IAD601–604 |
| 12 | `Lastenheft_RAW-07-Hardware-Capability-Layer.md` | Blocked | Hardware; IAD701–704 |
| 13 | `Lastenheft_RAW-08-Workflow-Engine.md` | Pending | Knowledge Workflow |
| 14 | `Lastenheft_RAW-09-Preset-Evolution.md` | Blocked | Preset Proposal; IAD901–902 |

Alle Pfade liegen unter `requirements/intakes/active/`. Die fachliche
Nummerierung benennt Owner-Reihen; die Verarbeitungsposition folgt dem
Abhängigkeitsgraphen und kann deshalb RAW-03 vor RAW-02 führen.

*All paths are below `requirements/intakes/active/`. Domain numbering identifies
owner series; processing order follows dependencies and may therefore place
RAW-03 before RAW-02.*

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

META-LH-01 bis META-LH-05 sind nach aktueller `Ready`-Single-Review-Evidence im
Manifest `Completed`. RAW-01 ist der einzige ausdrücklich als `Eligible`
markierte Kandidat. RAW-05 besitzt keine bindende Vorgängerkante und ist
strukturell ebenfalls eligible, bleibt aber `Pending` und auf read-only
Research begrenzt. Das ist eine Auskunft, keine Review-, Specify- oder
Ausführungsfreigabe. IAD201–203 sind für RAW-02 bestätigt; dessen
Serien-Lifecycle bleibt bis zum Abschluss von RAW-01 und RAW-03 blockiert.
RAW-06, RAW-07 und RAW-09 bleiben bis zu den im jeweiligen Intake genannten
IAD-Decisions blockiert.

*META-LH-01 through META-LH-05 are `Completed` after current `Ready`
Single-review evidence. RAW-01 is the only explicitly declared `Eligible`
candidate.
RAW-05 has no binding predecessor and is structurally eligible but remains
pending and research-only. IAD201 through IAD203 are confirmed; RAW-02 remains
blocked by the binding RAW-01 and RAW-03 sequence. This is information, not
authority.*
