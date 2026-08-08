<!-- intake-authoring:begin -->
# RAW-08 – Workflow Engine und Program-to-Knowledge / Workflow Engine and Program-to-Knowledge

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Git- und Review-Grundlagen; keine Governance-Engine-Erfahrung / Git and review basics; no governance-engine experience
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Die Reihe verbindet Charter, Sources, Decisions, Intakes, Specs, Plans, Tasks,
Evidence und Retrospektiven als nachvollziehbaren Workflow. Sie besitzt deren
Lifecycle und Traceability, aber keine AOC-Produktzustandslogik. / *The series
connects programme artifacts into a traceable workflow and owns lifecycle, not
product-state semantics.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-159, 168, 174; RF-03, RF-12, RF-14. Inputs: RAW-05/06 Execution Evidence
und alle Governance Receipts. Output: prüfbare Knowledge Package an RAW-09.

## Anforderungen / Requirements

- **FR-001:** Jedes Artefakt MUSS stabile ID, Quelle, Status, Owner und Revision besitzen.
- **FR-002:** Übergänge MÜSSEN Preconditions, Authority, Output Hash und Stop-Gate binden.
- **FR-003:** Evidence MUSS positive, negative und Provider-Failure-Klassen trennen.
- **FR-004:** Retrospektive darf Beobachtung nicht still in normative Decision verwandeln.
- **NFR-001:** JSON-/Textnachweis ist reproduzierbar, secret-free und B2-erklärbar.

## Decisions, Mode und Recovery / Decisions, mode, and recovery

Offen: Persistenzformat, Signatur/Attestation und Retention. Abhängig von
RAW-05/06 Evidence Contracts. `serial-autonomous` nach Decisions. Recovery
setzt am letzten hash-validierten Receipt fort; keine Statusannahme.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Artifact Lifecycle; Traceability Graph; Evidence/Receipt Contract;
Retrospective Handoff. **AC-001:** ein End-to-End-Beispiel ist von Source bis
Retrospektive lückenlos. **AC-002:** fehlende Authority, Hash-Drift und
ProviderFailure blockieren falsche Completion.

Revision bei Lifecycle-/Receipt-Schema. Keine Produkt-, Delivery- oder Preset-Promotion-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
