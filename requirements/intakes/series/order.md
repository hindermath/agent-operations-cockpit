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

META-LH-01 bis META-LH-05 sowie RAW-01 bis RAW-09 sind nach aktueller
`Ready`-Single-Review-Evidence im Manifest `Completed`. Es gibt keinen
`Eligible`-Kandidaten und keinen Lifecycle-Blocker. Das vollständige aktuelle
Series Review `86763944-9aab-4178-81b7-40dff7c1af51` ist `Ready`; der
ausdrücklich autorisierte Statuswechsel setzt deshalb auch den deklarierten
Serienstatus auf `Completed`. Dieser Abschluss startet keine Folgearbeit und
erteilt keine Review-, Specify-, Implementierungs-, Remote-, Merge-, Bypass-,
Preset- oder Promotion-Authority.

*META-LH-01 through META-LH-05 and RAW-01 through RAW-09 are `Completed` after
current Ready Single-review evidence. No Eligible candidate or lifecycle
blocker remains. Complete current Series review
`86763944-9aab-4178-81b7-40dff7c1af51` is `Ready`; the explicitly authorised
transition therefore also sets the declared Series status to `Completed`.
This completion starts no downstream work and grants no downstream or
promotion authority.*
