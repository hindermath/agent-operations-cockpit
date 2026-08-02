<!-- intake-authoring:begin -->
# RAW-02 – Workspace Orchestrator / Workspace Orchestrator

**Status:** NeedsClarification
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Prozesse und CLI-Grundlagen; keine interne Historie / process and CLI basics; no internal history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Einzelwerkzeuge besitzen heute keinen gemeinsamen, wahrheitsgetreuen Kontext.
Der Orchestrator soll Snapshot, State, Node und Capability verbinden, ohne deren
Concerns zu übernehmen. / *The orchestrator connects snapshot, state, node, and
capability contracts without owning their concerns.*

## Grenze, Scope und Non-Goals / Boundary, scope, and non-goals

Scope: Fokus, Session Context, Capability Routing und später reversible
Command-Koordination. Non-Goals: State-Semantik, Workspace-Discovery,
Darstellung, Rohprotokolle und Product Working Copy Ownership.

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-157, 162, 177; RF-07, RF-09. Inputs: RAW-01 Snapshot, RAW-03 State Envelope,
RAW-05 Node Descriptor, RAW-06 Capability Descriptor. Output: versionierter
Orchestration Context an RAW-04.

## Anforderungen / Requirements

- **FR-001:** Routing MUSS Capability, Zielnode, Authority und Correlation ID binden.
- **FR-002:** Fokuswechsel MUSS beobachtbar, atomar und reversibel beschrieben sein.
- **FR-003:** Read-only Phase DARF keinen Prozess oder Agenten starten.
- **NFR-001:** Timeout, Cancellation und Partial Failure sind explizit.
- **NFR-002:** Security, DE/EN, B2 und textuelle Statusparität gelten.

## Decisions, Dependencies, Mode und Recovery

Offen: **IAD201** IPC/Prozessvertrag, **IAD202** Persistenz des Session Context
und **IAD203** Command Queue.
Blockiert bis RAW-01 und RAW-03 reviewt sind. Modus `blocked`, danach
`serial-autonomous`. Recovery verwirft unbestätigten Context und behält letzten
gültigen Snapshot; keine automatische Wiederholung nicht-idempotenter Aktionen.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Context Contract; Focus Routing; Capability Routing; Cancellation/Recovery.
**AC-001:** dieselbe Correlation ID ist durch alle Handoffs sichtbar.
**AC-002:** fehlende Authority, verlorener Node und Timeout blockieren Side Effects.
Positiv: deterministisches read-only Routing. Negativ: stale Context und
unautorisierter Zielnode werden abgewiesen.

Revision bei Handoff- oder Authority-Änderung. Keine UI-, State- oder Adapterautorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
BLOCKED - DO NOT RUN: IAD201, IAD202, and IAD203 require human decisions.
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
BLOCKED - DO NOT RUN: IAD201, IAD202, IAD203, RAW-01, and RAW-03 are required.
```
<!-- intake-authoring:end -->
