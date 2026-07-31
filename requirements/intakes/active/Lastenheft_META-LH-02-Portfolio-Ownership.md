<!-- intake-authoring:begin -->
# META-LH-02 – Lastenheft-Portfolio und Ownership / Requirements Portfolio and Ownership

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** allgemeine IT-Systemgrenzen; keine Projektgeschichte / general IT boundaries; no project history
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Das Portfolio weist jedem Concern genau eine Owner-Reihe zu und macht Handoffs,
Non-Ownership, Decisions und Parallelitätsrisiken sichtbar. / *The portfolio
assigns exactly one owner series to every concern and exposes handoffs,
non-ownership, decisions, and concurrency risks.*

## Quellen und Finding-Traceability / Sources and finding traceability

SRC-157, 161, 162, 168–175, 177, 181, 182; Owner von RF-06 bis RF-09 und
Beitrag zu RF-16/RF-18.

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Input: Source Pack, Constraints und Findings. Output: neun fachliche Reihen,
Ownership Matrix, Series Map, Decision Map und azyklischer Handoff-Graph.
Nicht im Scope: technische Implementierung und Reihenstart.

## Grenzen / Boundaries

Owner bedeutet Änderungsautorität für den Concern, nicht Schreibzugriff auf
abhängige Reihen. Handoffs sind versionierte Verträge; Consumer dürfen sie
nicht einseitig umdefinieren. / *Ownership is change authority for a concern,
not write access to dependent series.*

## Anforderungen / Requirements

- **FR-001:** Jeder Concern MUSS genau eine kanonische Owner-Reihe besitzen.
- **FR-002:** Jede Reihe MUSS Zweck, Systemgrenze, erwartete Child-Intakes,
  Decision Intakes, Inputs/Outputs, Dependencies, Review/Evidence Gates und
  geeignete Modi besitzen.
- **FR-003:** Jeder Handoff MUSS Producer, Consumer, Version und Fehlerverhalten nennen.
- **FR-004:** Graph MUSS azyklisch sein; bindende und bevorzugte Kanten sind getrennt.
- **NFR-001:** Tabellen und Graphen benötigen vollständige Textalternative.
- **NFR-002:** Fachbegriffe und Abkürzungen folgen B2- und Glossarregeln.

## Abhängigkeiten und Modus / Dependencies and mode

Abhängig von META-01. `manual-assisted`, weil Mehrfachowner und offene Decisions
materielle menschliche Entscheidungen sind. / *Depends on META-01 and remains
manual-assisted for material ownership decisions.*

## Risiken / Risks

Zyklus durch State↔Orchestrator oder Node↔CLI; Gegenmaßnahme sind einseitige
Contract-Handoffs und DAG-Validierung. / *Cycles are prevented through
directional contracts and DAG validation.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Neun Reihen und alle Concerns sind ohne Mehrfachowner erfasst.
- **AC-002:** Automatische DAG-Prüfung findet keinen Zyklus.
- **AC-003:** Jede Reihe nennt mindestens eine Non-Ownership-Grenze.
- **AC-004:** Offene Decisions blockieren betroffene Ausführung sichtbar.

## Evidence / Evidence

Positiv: Ownership-Tabelle, topologische Reihenfolge und Reviewer-Zustimmung.
Negativ: Fixture mit Doppelowner und Fixture `RAW-02 -> RAW-03 -> RAW-02`
werden abgewiesen.

## Revision und Nicht-Autorität / Revision and non-authority

Revision bei neuem Concern oder Contract-Handoff. Keine Implementierungs-,
Scheduling- oder Parallelitätsfreigabe.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
