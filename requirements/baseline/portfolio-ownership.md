# Lastenheft-Portfolio und Ownership / Requirements Portfolio and Ownership

## Zweck und Begriffe / Purpose and terms

Diese lesbare Matrix ordnet jeden fachlichen Concern genau einer Owner-Reihe
zu. `Owner` bedeutet Änderungsautorität für den benannten Vertrag;
`Non-Ownership` nennt die ausdrückliche Grenze. Der vollständige
maschinenprüfbare FR-002-/FR-003-Vertrag steht in
[portfolio-ownership.json](portfolio-ownership.json). / *This readable matrix
assigns every domain concern to exactly one owner series. `Owner` means change
authority for the named contract; `Non-Ownership` states the explicit
boundary. The complete machine-checkable FR-002/FR-003 contract is stored in
[portfolio-ownership.json](portfolio-ownership.json).*

## Ownership Matrix / Ownership matrix

| ID | Concern / Concern | Kanonische Owner-Reihe / Canonical owner | Quellen / Sources | Abhängige Reihen / Dependents | Handoff / Handoff | Explizite Non-Ownership / Explicit non-ownership | Offene Decisions / Open decisions | Parallelitätsrisiko / Concurrency risk |
|---|---|---|---|---|---|---|---|---|
| C-01 | Referenz-Workspace, Discovery und Snapshot / reference workspace, discovery, and snapshot | RAW-01 Reference Agentic Workspace | SRC-161, SRC-177 | RAW-02, RAW-03, RAW-05, RAW-06 | Workspace Snapshot Contract | Keine UI und keine Commands. / No UI or commands. | DEC-T02: nur Solution-/Projektzuschnitt; IAD101–IAD103 sind bestätigt. / Solution and project layout only; IAD101–IAD103 are confirmed. | Hoch am gemeinsamen Snapshot-Schema. / High at the shared snapshot schema. |
| C-02 | Orchestration, Fokus und Routing / orchestration, focus, and routing | RAW-02 Workspace Orchestrator | SRC-162, SRC-177 | RAW-03, RAW-04, RAW-05, RAW-06 | Orchestration Context Contract | Keine Zustandssemantik und keine Geräteprotokolle. / No state semantics or device protocols. | Keine; IAD201–IAD203 sind bestätigt. / None; IAD201–IAD203 are confirmed. | Hoch am Command-Bus. / High at the command bus. |
| C-03 | State, Authority und Freshness / state, authority, and freshness | RAW-03 State Truthfulness | SRC-172, SRC-180, SRC-181 | RAW-02, RAW-04, RAW-05 | State Envelope Contract | Keine Darstellung und keine Discovery. / No presentation or discovery. | Keine; IAD301–IAD303 supersedieren DEC-T03 vollständig und bestätigen duale Zeit, relative Freshness-Profile sowie deterministische Confidence-Klassen. / None; IAD301-IAD303 fully supersede DEC-T03 and confirm dual time, relative freshness profiles, and deterministic confidence classes. | Hoch wegen zentraler Semantik. / High because semantics are central. |
| C-04 | Surfaces und Presentation Manager / surfaces and presentation manager | RAW-04 Presentation Fabric | SRC-169, SRC-172 | RAW-07 | Presentation Contract | Keine Workspace-Domainlogik. / No workspace domain logic. | DEC-T04: TUI/UI, Responsiveness und Lokalisierung. / TUI/UI, responsiveness, and localisation. | Mittel bei Contract-Änderungen. / Medium when the contract changes. |
| C-05 | Host, Sandbox, Container und Remote Node / host, sandbox, container, and remote node | RAW-05 Execution Nodes | SRC-177, SRC-181 | RAW-02, RAW-06, RAW-08 | Node Capability and Authority Contract | Kein Owner der Produkt-Working-Copy und keine CLI-Semantik. / No product working-copy ownership or CLI semantics. | Answered: IAD604 für Remote Transport. Open: DEC-T06 für Node Attestation/Timeout. / Answered: IAD604 for remote transport. Open: DEC-T06 for node attestation/timeout. | Mittel an Trust- und Mount-Grenzen. / Medium at trust and mount boundaries. |
| C-06 | CLI- und Environment-Capabilities / CLI and environment capabilities | RAW-06 CLI Capability and Environment Orchestration | SRC-162 | RAW-02, RAW-05, RAW-08 | CLI Capability Contract | Keine UI und keine Hardware. / No UI or hardware. | Answered: IAD601, IAD602, IAD603 und IAD604. / Answered: IAD601, IAD602, IAD603, and IAD604. | Mittel bei Prozess- und Environment-Verträgen. / Medium at process and environment contracts. |
| C-07 | Gerätefähigkeiten und Adapter / hardware capabilities and adapters | RAW-07 Hardware Capability Layer | SRC-169, SRC-171, SRC-173, SRC-175 | RAW-04 | Hardware Capability Contract | Keine Domänenlogik und kein State-Owner. / No domain logic or state ownership. | Answered: IAD701, IAD702, IAD703 und IAD704. / Answered: IAD701, IAD702, IAD703, and IAD704. | Niedrig je Adapter, hoch am gemeinsamen Contract. / Low per adapter, high at the shared contract. |
| C-08 | Program-to-Knowledge Workflow / program-to-knowledge workflow | RAW-08 Workflow Engine | SRC-168, SRC-174 | RAW-09 | Evidence and Retrospective Contract | Keine Produktzustandslogik. / No product-state logic. | Answered: IAD801, IAD802 und IAD803. Superseded: DEC-T05. / Answered: IAD801, IAD802, and IAD803. Superseded: DEC-T05. | Mittel am Evidence-Schema. / Medium at the evidence schema. |
| C-09 | Preset-Gap und Promotion / preset gaps and promotion | RAW-09 Preset Evolution | SRC-170, SRC-174 | keine Produktreihe / no product series | Proposal Evidence Contract | Keine Produkt- oder Delivery-Autorität. / No product or delivery authority. | Answered: IAD901, IAD902 und AUTH-RAW09-PROMOTION; letzteres bestätigt, dass jede Promotion eine neue menschliche Freigabe benötigt und keine Preset-Promotion erteilt. / Answered: IAD901, IAD902, and AUTH-RAW09-PROMOTION; the latter confirms that every promotion requires new human approval and grants no preset promotion. | Niedrig bei read-only Analyse. / Low for read-only analysis. |

## Typisierter Handoff-Graph / Typed handoff graph

```text
BindingContract:
  RAW-01 -> RAW-03
  RAW-01 -> RAW-02
  RAW-03 -> RAW-02
  RAW-03 -> RAW-04
  RAW-04 -> RAW-07
  RAW-05 -> RAW-06
  RAW-05 -> RAW-08
  RAW-06 -> RAW-08
  RAW-08 -> RAW-09

PreferredSerialOrder (nicht bindend / non-binding):
  RAW-02 -> RAW-05
```

`BindingContract` verlangt einen gültigen Producer-Vertrag; fehlt er oder
passt seine Version nicht, stoppt der Consumer fail-closed.
`PreferredSerialOrder` koordiniert nur die Reihenfolge und ist keine
funktionale Voraussetzung. Eine gültige sichtbare topologische Reihenfolge ist
`RAW-01, RAW-03, RAW-02, RAW-04, RAW-05, RAW-06, RAW-07, RAW-08, RAW-09`.
Die Serialisierung entspricht der Series-Sicht; der zusätzliche direkte
RAW-01→RAW-02-Handoff dokumentiert den konsumierten Workspace Snapshot, ohne
eine zweite Series-Kante zu erfinden. / *A binding contract requires a valid
producer contract; a missing or incompatible version stops the consumer
fail-closed. Preferred serial order coordinates delivery only. The listed
visible order is valid. The direct RAW-01-to-RAW-02 handoff records snapshot
consumption without inventing another Series edge.*

## Vollständiger Vertrag und Decision-Aktualität / Complete contract and decision currency

Der JSON-Vertrag nennt für jede Reihe Systemgrenze, Child-Intakes, Decision
Intakes, Inputs/Outputs, Dependencies, Review-/Evidence-Gates, Modi und
Non-Ownership. Jeder Handoff nennt Producer, Consumer, Version, Kantentyp,
Binding-Status und Fehlerverhalten. Die
[Decision Map](../../docs/decisions/open-decisions.md) trennt offene von
bestätigten beziehungsweise supersedierten Decisions. / *The JSON contract
contains every FR-002 field per series and every FR-003 field per handoff. The
[Decision Map](../../docs/decisions/open-decisions.md) separates open decisions
from confirmed or superseded decisions.*

## Prüfnachweis / Validation evidence

```text
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --contract requirements/baseline/portfolio-ownership.json --markdown requirements/baseline/portfolio-ownership.md
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Contract requirements/baseline/portfolio-ownership.json -Markdown requirements/baseline/portfolio-ownership.md
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
```

Der erste Lauf bestätigt neun Reihen, neun eindeutige Concerns, vollständige
Vertragsfelder, Markdown-/JSON-Owner-Parität und einen azyklischen Graphen. Die
beiden Fixture-Läufe bestehen nur, wenn der erwartete Doppelowner- oder
Zyklusfehler erkannt wird. / *The positive run validates the complete portfolio.
Each fixture run succeeds only when the expected duplicate-owner or cycle
defect is detected.*
