<!-- intake-authoring:begin -->
# META-LH-04 – Series-Planung, Eligibility und kontrollierte Parallelität / Series Planning, Eligibility, and Controlled Parallelism

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Git-Branch-Grundlagen; keine autonome Laufpraxis / basic Git branches; no autonomous-run experience
**Profile:** `aoc-bilingual-requirements`

## Zweck / Purpose

Das Lastenheft erzeugt einen prüfbaren DAG (gerichteten Graph ohne Zyklus),
bestimmt nächste Kandidaten und klassifiziert Autonomie ohne Ausführung zu
starten. / *This intake creates a verifiable directed acyclic graph, identifies
next candidates, and classifies autonomy without starting execution.*

## Quellen und Findings / Sources and findings

SRC-159, SRC-174, SRC-180–182; RF-02, RF-09, RF-18, RF-19.

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Input: reviewfähige Intakes, Ownership und Decisions. Output: SHA-gebundenes
Series-Manifest, typisierte Kanten, Roots, Eligibility, Stop-/Recovery-Regeln
und Receipt. Out of Scope: Workerstart, Merge und Produktänderung.

## Trust- und Authority-Grenzen / Trust and authority boundaries

`Eligible` ist keine Startautorität. Runner, Worktree und Remote brauchen einen
separaten aktuellen Auftrag. ProviderFailure darf nicht als ProductFailure
klassifiziert werden. / *Eligibility is not start authority. Provider and
product failures remain distinct.*

## Anforderungen / Requirements

- **FR-001:** Modus ist einer von manual-assisted, single-autonomous,
  serial-autonomous, parallel-autonomous, research-only oder blocked.
- **FR-002:** Bewertung MUSS Authority, Side Effects, Reversibilität,
  Schreibscope, Decisions, Integration, Review, Abort und Recovery enthalten.
- **FR-003:** Parallelität ist nur bei disjunkten Writes, keinen gemeinsamen
  offenen Decisions und geplantem Consolidation Review zulässig.
- **FR-004:** Manifest MUSS Hashes, Roots, Order, Lifecycle und typisierte Kanten binden.
- **FR-005:** Ein Zyklus oder Hash-Drift MUSS fail-closed blockieren.
- **NFR-001:** Status und nächste Aktion sind als Text verfügbar, nicht nur Diagramm/Farbe.

## Dependencies und Risiken / Dependencies and risks

Abhängig von META-01..03. `manual-assisted`, weil Parallelfreigaben materielle
Authority-Entscheidungen sind. Risiko: falsche Parallelität auf gemeinsamen
Schemas; Recovery: Worker stoppen, keine Teilmerge, Manifest erneut prüfen.

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** DAG-Validator besteht in Bash und PowerShell.
- **AC-002:** Cycle-, Shared-Write- und Shared-Decision-Fixtures blockieren.
- **AC-003:** Jeder Intake besitzt vollständige Acht-Kriterien-Einstufung.
- **AC-004:** Next-Candidate-Auskunft startet keine Arbeit.

## Evidence und Revision / Evidence and revision

Positiv: Manifest, Order View und Eligibility Matrix. Negativ: Zyklus,
staler Hash, fehlende Root und unzulässige Parallelgruppe. Revision bei
Intake-Hash, Decision-, Edge- oder Governance-Änderung.

## Nicht-Autorität / Non-authority

Keine Autorität für Workerstart, Worktree, Merge, Remote oder Implementierung.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
