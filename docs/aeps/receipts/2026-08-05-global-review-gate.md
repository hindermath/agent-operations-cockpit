# AEPS-Erfassungsreceipt globale Review-Sperre / AEPS Capture Receipt Global Review Gate

## Identität und Ergebnis / Identity and outcome

- Receipt-ID: `AEPS-RECEIPT-AOC-2026-08-05-009`
- Datum / Date: `2026-08-05`
- Trigger: ausdrücklich autorisierte AOC-weite Governance-Entscheidung /
  *explicitly authorised AOC-wide governance decision*
- Repository-Base-HEAD: `b69079623e41918dd8ad6db4572c070534cbad88`
- Ergebnis / Outcome: `StrengthenedLocalEvidence`
- Upstream-Status: `PendingPublication`

Thorsten hat als konservative Projektentscheidung festgelegt, dass vor dem
ersten nachgelagerten Spec-Kit-Lauf alle 14 aktiven AOC-Lastenhefte aktuelle,
formal validierte `Ready`-Single-Reviews besitzen müssen. Erst danach darf
`META-LH-01` mit einem neuen ausdrücklichen Startauftrag das erste Ziel sein.
`ReadyWithAcceptedRisks`, supersedierte Ergebnisse, Lifecycle-Werte oder
historische Authority öffnen das Gate nicht; Drift schließt es erneut. /
*The explicit project decision requires current, formally validated Ready
Single reviews for all 14 active AOC intakes before the first downstream Spec
Kit run. `META-LH-01` is then the first target and still needs a new explicit
start instruction. Accepted-risk or superseded results, lifecycle values, and
historic authority do not open the gate; drift closes it again.*

## Aktueller Gate-Zustand / Current gate state

Das Gate ist `Closed`. Zielhashaktuelle `Ready`-Review-Ergebnisse liegen für
`META-LH-01` bis `META-LH-05`, `RAW-01`, `RAW-02` und `RAW-03` vor und bestehen
jeweils Bash und PowerShell. Den vollständigen Review-plus-Receipt-Vertrag
erfüllen derzeit jedoch nur fünf Ziele: `META-LH-01`, `META-LH-03` sowie
`RAW-01` bis `RAW-03`.

Die Authoring Receipts von `META-LH-02`, `META-LH-04` und `META-LH-05`
scheitern auf beiden Validatoroberflächen an gebundener Source-Hash-Drift. Für
`RAW-04` bis `RAW-09` fehlt außerdem die formale Ready-Coverage. Diese
Zustandsaussage erteilt keine Review-, Repair-, Specify-, Autonomous-,
Implementierungs- oder Delivery-Authority. / *The gate is Closed. Eight review
results remain target-hash-current and pass both validators, but only five
targets satisfy the full review-plus-receipt contract. Three META receipts have
bound-source hash drift, and RAW-04 through RAW-09 lack formal Ready coverage.
This state grants no downstream authority.*

## Validierungsevidence / Validation evidence

- Acht aktuelle Single-Review-Ergebnisse: Bash `Passed`, PowerShell `Passed`.
- Fünf aktuelle Authoring Receipts: Bash `Passed`, PowerShell `Passed`.
- `META-LH-02`: Bash/PowerShell `Failed`; Drift in
  `requirements/baseline/portfolio-ownership.md`,
  `requirements/baseline/portfolio-ownership.json`,
  `docs/decisions/open-decisions.md` und
  `specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1`.
- `META-LH-04`: Bash/PowerShell `Failed`; Drift in
  `specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.py`.
- `META-LH-05`: Bash/PowerShell `Failed`; Drift in
  `requirements/baseline/portfolio-ownership.json` und
  `requirements/baseline/portfolio-ownership.md`.

*Both validator surfaces agree: all eight review results pass; five Authoring
Receipts pass; the three named META receipts fail because their bound sources
have drifted. No receipt was repaired in this change.*

## AEPS-Einordnung / AEPS assessment

Es entsteht keine neue Finding-ID. Die Entscheidung stärkt
`AEPS-FIND-AOC-011`: Ein einzelnes `Ready` oder `Eligible` ist keine
Startfreigabe, und im AOC ist zusätzlich vollständige Portfolio-Coverage nötig.
Die lokale Evidence bleibt `pilot-pattern` beziehungsweise `PartiallyRecorded`.
Die konkrete 14er-Zielmenge und `META-LH-01` als erstes Ziel sind
AOC-spezifisch und dürfen nicht ohne Runtime- und Cross-Project-Evidence in ein
allgemeines Preset übernommen werden. / *No new finding ID is created. The
decision strengthens AEPS-FIND-AOC-011 while remaining AOC-specific local
evidence. Promotion requires runtime and cross-project validation.*

## Gebundene Quellen / Bound sources

| Quelle / Source | SHA-256 |
|---|---|
| `README.md` | `bbee6b7b2fcd7aa5ebd6f0dfbe4af48b473ecb3f17aed814ef51a55486c36018` |
| `Pflichtenheft.md` | `faedeb0980f1d9f3a5db95b3cf8cd5502451ee39e6300ca8bc033da912f4e72a` |
| `Lastenheft_Abarbeitungsreihenfolge.md` | `5e0d38daac22c89368e4277e13df7e47811cd9bbbee2dcf7060e36bb128f2147` |
| `requirements/baseline/authority-and-stop-gates.md` | `e64ce59770bb3c82d95f860cf2b7ed8de8d53250b8c6b6f77b260a5b075f3c99` |
| `requirements/baseline/autonomy-and-evidence-model.md` | `529e4421dd72764ae354792ca7feed73dab390dc683e20ec4b22a4ea2f8d7e64` |
| `requirements/intakes/series/order.md` | `8d4213862d2b5327b410ddc2db2ab2e9c87389ef3d1739d78497ec356958e7b0` |
| `docs/documentation-governance.md` | `23e6f61ad819440978172211b527b0b0f2d9e86df040748d8b9e74adfee39f59` |
| `docs/aeps/README.md` | `1de14c4faaf5c46223260a7581b42989262cc7bbf1bb3c1e124fa91529c07f93` |

Die fünf Agentenflächen wurden gemeinsam aktualisiert; beide Copilot-Flächen
sind bytegleich. Die gebundenen Quellen sind bis zu einem Commit
`PendingPublication`. / *All five agent surfaces were updated together; both
Copilot surfaces are byte-identical. Bound sources remain PendingPublication
until committed.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist Thorstens ausdrückliche Entscheidung
vom `2026-08-05`; Owner ist das AOC-Anforderungsprogramm. Aktualisiert wurden die
kanonischen Authority-Gates, Navigation und Reihenfolge, das Autonomiemodell,
README, alle fünf Agentenflächen sowie die lokale AEPS-Evidence. Produktcode,
Lastenheftinhalte, Single-Review-Ergebnisse, Series-Lifecycle, Presets und
Level-0-Artefakte bleiben unverändert. / *Decision: `UpdateRequired`. The
explicit project decision is the source and the AOC requirements programme is
the owner. Product code, intake contents, review results, lifecycle, presets,
and level-0 artifacts remain unchanged.*

## Grenzen und Nicht-Autorität / Boundaries and non-authority

- Kein Spec-Kit-, Autonomous-, Parallel-Autonomous- oder Implementierungslauf.
- Keine Review- oder Repair-Ausführung und keine Änderung eines Lastenhefts.
- Keine Series-Lifecycle-, Manifest-, Intake-Authoring-Receipt-,
  Series-Receipt- oder Preset-Änderung.
- Keine Remote-, Merge-, Bypass-, Level-0- oder Promotion-Aktion.

*No downstream run, review, repair, lifecycle, intake or series receipt,
preset, remote, merge, bypass, level-0, or promotion action was performed.*
