<!-- intake-authoring:begin -->
# RAW-02 – Workspace Orchestrator / Workspace Orchestrator

**Status:** ReadyForReview
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

Die drei Materialentscheidungen sind bestätigt: / *The three material
decisions are confirmed:*

1. **IAD201 – logischer IPC-/Prozessvertrag:** RAW-02 besitzt den
   transportneutralen Vertrag für Aufruf, Antwort, Ereignis, Abbruch und
   Lebenszyklus. Konkrete Process API und Transportwahl bleiben bei RAW-06 und
   dürfen nicht in den Orchestration Contract durchsickern. / *RAW-02 owns the
   transport-neutral invocation, response, event, cancellation, and lifecycle
   contract. RAW-06 retains the concrete process API and transport choice.*
2. **IAD202 – Persistenz des Session Context:** Jedes Context-Feld wird als
   flüchtig oder persistent klassifiziert. Nur ausdrücklich bestätigte Fokus-
   und Routingauswahlen mit ihrer Schemaversion dürfen persistieren. Laufende
   Commands, Cancellation Handles sowie abgeleitete State-, Node- und
   Capability-Projektionen bleiben flüchtig und werden aus ihren Owner-
   Verträgen neu aufgebaut. Unbekannte Version oder invalidierte Abhängigkeit
   verwirft den Context fail-closed; die State-Semantik bleibt bei RAW-03. /
   *Every context field is classified as volatile or persistent. Only explicit
   focus and routing choices plus their schema version may persist. In-flight
   commands, cancellation handles, and derived projections remain volatile.
   Unknown versions or invalidated dependencies discard the context
   fail-closed; RAW-03 retains state semantics.*
3. **IAD203 – Command Queue und Idempotenz:** Commands werden pro Session
   geordnet und an Correlation ID sowie Idempotency Key gebunden. Deduplizierung
   und automatische Wiederholung sind nur für ausdrücklich idempotente Aktionen
   zulässig. Abbruch liefert einen sichtbaren Endzustand; nicht-idempotente
   Aktionen werden nie automatisch wiederholt. Mutierende Commands bleiben bis
   nach dem abgeschlossenen Read-only-Slice gesperrt. / *Commands are ordered
   per session and bind correlation and idempotency keys. Deduplication and
   automatic retry apply only to explicitly idempotent actions. Cancellation
   has a visible terminal state, non-idempotent actions are never replayed
   automatically, and mutating commands remain disabled until the read-only
   slice is complete.*

Der Authoring-Status ist `ReadyForReview`. Der Serien-Lifecycle bleibt
`Blocked`, bis RAW-01 und RAW-03 in der bindenden Reihenfolge abgeschlossen und
ihre Reviews aktuell sind. Danach ist `serial-autonomous` nur mit einer neuen,
ausdrücklichen Start- und Scope-Autorität zulässig. Recovery verwirft
unbestätigten Context, behält den letzten gültigen Snapshot und rät weder
Migration noch Wiederholung. / *The authoring status is `ReadyForReview`; the
Series lifecycle remains blocked until RAW-01 and RAW-03 are completed in the
binding order with current reviews. Any later run needs separate current start
and scope authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Context Contract; Focus Routing; Capability Routing; Cancellation/Recovery.
**AC-001:** dieselbe Correlation ID ist durch alle Handoffs sichtbar.
**AC-002:** fehlende Authority, verlorener Node und Timeout blockieren Side Effects.
**AC-003:** Ein Wechsel von Process API oder Transport in RAW-06 verändert den
logischen RAW-02-Vertrag nicht.
**AC-004:** Restart-, Versions- und Invalidierungs-Fixtures unterscheiden
persistente Auswahl von flüchtigem Laufzeitkontext und übernehmen keine
State-Semantik aus RAW-03.
**AC-005:** Queue-Fixtures belegen Reihenfolge, Deduplizierung, erlaubte
idempotente Wiederholung, Abbruch und die ausbleibende automatische Wiederholung
nicht-idempotenter Aktionen; vor Abschluss des Read-only-Slices entsteht kein
mutierender Side Effect.
Positiv: deterministisches read-only Routing. Negativ: stale Context und
unautorisierter Zielnode, inkompatible Context-Version, doppelter Command und
Retry einer nicht-idempotenten Aktion werden abgewiesen. / *Positive evidence
proves deterministic read-only routing. Negative fixtures reject stale or
incompatible context, an unauthorised node, duplicate commands, and replay of
non-idempotent actions.*

Revision bei Handoff- oder Authority-Änderung. Keine UI-, State- oder Adapterautorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md --bind-exact-intake --no-implementation --no-remote-writes
VORBEDINGUNG / PRECONDITION: Erst nach aktuellem RAW-02-Review und erfüllter bindender Reihenfolge RAW-01 -> RAW-03 verwenden; dieser Prompt erteilt keine Start- oder Implementierungsautorität. / Use only after a current RAW-02 review and the binding RAW-01 -> RAW-03 order are satisfied; this prompt grants no start or implementation authority.
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md --delivery-mode LocalImplementation --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange RAW-01 und RAW-03 nicht abgeschlossen und aktuell reviewt sind und keine separate aktuelle Benutzerentscheidung Scope, Start und Implementierung ausdrücklich autorisiert. Remote Writes, Merge und Bypass sind nicht autorisiert. / Do not start until RAW-01 and RAW-03 are completed with current reviews and a separate current user decision explicitly authorises scope, start, and implementation. Remote writes, merge, and bypass are not authorised.
```
<!-- intake-authoring:end -->
