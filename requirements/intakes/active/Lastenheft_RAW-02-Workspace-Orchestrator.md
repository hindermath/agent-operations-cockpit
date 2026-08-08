<!-- intake-authoring:begin -->
# RAW-02 – Workspace Orchestrator / Workspace Orchestrator

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** Prozesse und Grundlagen von Befehlszeilen-Schnittstellen (CLI); keine Spec-Kit- oder interne Projektgeschichte / processes and command-line interface (CLI) basics; no Spec Kit or internal project history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Einzelwerkzeuge besitzen heute keinen gemeinsamen, wahrheitsgetreuen Kontext.
Der Workspace Orchestrator (Arbeitsbereichs-Koordinator) soll Snapshot, State,
Node und Capability verbinden, ohne deren fachliche Verantwortung zu
übernehmen. / *Individual tools currently have no shared, truthful context. The
Workspace Orchestrator coordinates snapshot, state, node, and capability
contracts without taking ownership of their concerns.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Session Context / Sitzungskontext:** die an eine Sitzung gebundene Menge aus
  bestätigten Fokus- und Routingauswahlen sowie flüchtigen Laufzeitdaten. /
  *The session-bound set of confirmed focus and routing choices plus volatile
  runtime data.*
- **Interprozesskommunikation (IPC) / inter-process communication (IPC):** der
  Austausch von Aufrufen, Antworten und Ereignissen zwischen getrennten
  Prozessen. RAW-02 beschreibt nur den logischen Vertrag. / *The exchange of
  invocations, responses, and events between separate processes. RAW-02 defines
  only the logical contract.*
- **Correlation ID / Korrelationskennung:** eine eindeutige Kennung, die Aufruf,
  Ereignisse und Antwort derselben Operation verbindet. / *A unique identifier
  that links the invocation, events, and response of one operation.*
- **Idempotency Key / Idempotenzschlüssel:** eine Kennung, mit der eine erlaubte
  Wiederholung erkannt wird, ohne denselben Seiteneffekt doppelt auszuführen. /
  *An identifier used to recognise an allowed retry without applying the same
  side effect twice.*
- **Fail-closed / sicher geschlossen:** unbekannter oder ungültiger Kontext wird
  verworfen oder abgewiesen, statt mit vermuteten Rechten weiterzuarbeiten. /
  *Unknown or invalid context is discarded or rejected instead of continuing
  with assumed authority.*
- **Cancellation Handle / Abbruchreferenz:** eine flüchtige Referenz, über die
  ein laufender Befehl einen Abbruch anfordern und dessen Ergebnis beobachten
  kann. / *A volatile reference through which an in-flight command can request
  cancellation and observe its outcome.*
- **Capability / Fähigkeit** bezeichnet eine geräteunabhängige Aktion;
  **Node / Ausführungsknoten** bezeichnet den autorisierten Ausführungsort. /
  *A capability is a device-independent action; a node is its authorised
  execution location.*
- **Routing / Weiterleitung:** die Auswahl eines autorisierten Zielnodes für
  eine Capability. Ein **Descriptor / Beschreibungsdatensatz** und ein
  **Envelope / Umschlag** übertragen versionierte Daten mit Herkunft und
  Status. / *Routing selects an authorised target node for a capability. A
  descriptor and an envelope carry versioned data with provenance and status.*
- **Read-only-Slice / Nur-Lese-Funktionsausschnitt:** ein kleiner
  durchgängiger Ablauf, der Zustand liest und darstellt, aber nichts außerhalb
  der Abfrage verändert. / *A small end-to-end flow that reads and presents
  state without changing anything outside the query.*
- **Spec Kit:** der kontrollierte Arbeitsablauf für Spezifikation und spätere
  Entwicklungsphasen. `Specify` erstellt eine Spezifikation; `Autonomous`
  koordiniert nur nach separater Freigabe weitere Phasen. / *The controlled
  workflow for specification and later development phases. `Specify` creates a
  specification; `Autonomous` coordinates later phases only after separate
  approval.*
- **CEFR B2:** das Sprachniveau B2 des Gemeinsamen Europäischen
  Referenzrahmens für verständliche Dokumentation. / *Language level B2 of the
  Common European Framework of Reference for understandable documentation.*

Weitere Begriffe wie Authority, Evidence, Recovery, Side Effect und Snapshot
erklärt das [zweisprachige Glossar](../../baseline/glossary.md). / *The
[bilingual glossary](../../baseline/glossary.md) explains additional terms such
as authority, evidence, recovery, side effect, and snapshot.*

## Grenze, Scope und Non-Goals / Boundary, scope, and non-goals

Im Scope liegen Fokus, Session Context, Capability Routing und später die
reversible Command-Koordination. Außerhalb liegen State-Semantik,
Workspace-Discovery, Darstellung, Rohprotokolle und die Verantwortung für die
Product Working Copy. / *In scope are focus, session context, capability
routing, and later reversible command coordination. State semantics, workspace
discovery, presentation, raw protocols, and product working-copy ownership are
out of scope.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

Quellen sind SRC-157, SRC-162 und SRC-177; zugeordnete Findings sind RF-07 und
RF-09. Inputs sind der RAW-01 Snapshot, das RAW-03 State Envelope, der RAW-05
Node Descriptor und der RAW-06 Capability Descriptor. Output ist ein
versionierter Orchestration Context für RAW-04. / *Sources are SRC-157,
SRC-162, and SRC-177; assigned findings are RF-07 and RF-09. Inputs are the
RAW-01 snapshot, RAW-03 state envelope, RAW-05 node descriptor, and RAW-06
capability descriptor. The output is a versioned orchestration context for
RAW-04.*

## Querschnittsanforderungen / Cross-cutting requirements

- **Security / Sicherheit:** Jede Route MUSS die nachgewiesene Authority an
  Capability, Zielnode und Correlation ID binden. Fehlende oder widersprüchliche
  Authority wird fail-closed abgewiesen; Secrets und Zugangstoken gehören nicht
  in den Session Context. / *Every route MUST bind proven authority to the
  capability, target node, and correlation ID. Missing or conflicting
  authority is rejected fail-closed; secrets and access tokens do not belong in
  the session context.*
- **Privacy / Datenschutz:** Der Session Context DARF keine unnötigen
  Personendaten enthalten. Persistenz bleibt exakt auf die in IAD202 genannten
  bestätigten Auswahlen und ihre Schemaversion begrenzt. Eine neue Datenkategorie
  erzwingt vor ihrer Nutzung eine erneute Privacy-Prüfung. / *The session
  context MUST NOT contain unnecessary personal data. Persistence remains
  limited exactly to the confirmed choices and schema version named by IAD202.
  A new data category requires a renewed privacy review before use.*
- **Accessibility / Barrierefreiheit:** Dieses lernendenorientierte Lastenheft
  und jeder durch RAW-02 ausgegebene textuelle Status MÜSSEN die Web Content
  Accessibility Guidelines (WCAG) 2.2 Level AA, verständliche DE/EN-Paare und
  eine nicht nur farbliche Zustandsvermittlung unterstützen. Darstellung und
  Verhalten der Benutzeroberfläche (UI) bleiben bei RAW-04. / *This
  learner-facing intake and every textual status exposed by RAW-02 MUST support
  the Web Content Accessibility Guidelines (WCAG) 2.2 Level AA,
  understandable German/English pairs, and status meaning that does not rely
  on colour alone. Presentation and user-interface (UI) behaviour remain with
  RAW-04.*
- **Plattform und Cross-Platform:** Der logische Vertrag MUSS auf macOS, Linux
  und Windows dieselben Zustands- und Fehlerbedeutungen besitzen. Betriebssystem-
  APIs, Prozessstart und Transportadapter bleiben bei RAW-06. / *The logical
  contract MUST preserve the same state and failure meanings on macOS, Linux,
  and Windows. Operating-system APIs, process launch, and transport adapters
  remain with RAW-06.*
- **Software-Lieferkette / Software supply chain:** Für diese reine
  Lastenheft-Reparatur ohne Code, Build oder Paketabhängigkeit ist die
  Lieferkettenprüfung `N/A`. Sobald eine Implementierung oder Abhängigkeit
  eingeführt wird, MUSS die Anwendbarkeit neu bewertet und durch eine Software
  Bill of Materials (SBOM / Software-Stückliste) sowie Schwachstellennachweise
  belegt werden. / *Supply-chain validation is `N/A`
  for this intake-only repair, which adds no code, build, or package dependency.
  Introducing an implementation or dependency MUST trigger renewed
  applicability assessment with a software bill of materials (SBOM) and
  vulnerability evidence.*

## Anforderungen / Requirements

- **FR-001:** Routing MUSS Capability, Zielnode, Authority und Correlation ID
  binden. / *Routing MUST bind capability, target node, authority, and
  correlation ID.*
- **FR-002:** Fokuswechsel MUSS beobachtbar, atomar und reversibel beschrieben
  sein. / *Focus changes MUST be described as observable, atomic, and
  reversible.*
- **FR-003:** Die Read-only-Phase DARF keinen Prozess oder Agenten starten. /
  *The read-only phase MUST NOT start a process or agent.*
- **NFR-001:** Timeout, Cancellation und Partial Failure MÜSSEN ausdrücklich
  beschrieben sein. / *Timeout, cancellation, and partial failure MUST be
  explicit.*
- **NFR-002:** Security, Privacy, DE/EN-Parität, CEFR B2, WCAG 2.2 AA,
  Plattformparität und Lieferketten-Anwendbarkeit MÜSSEN nach den oben genannten
  Grenzen entschieden und nachweisbar sein. / *Security, privacy,
  German/English parity, CEFR B2, WCAG 2.2 AA, platform parity, and
  supply-chain applicability MUST be decided and evidenced within the stated
  boundaries.*

## Decisions, Dependencies, Mode und Recovery / Decisions, dependencies, mode, and recovery

Die drei Materialentscheidungen sind bestätigt: / *The three material
decisions are confirmed:*

1. **IAD201 – logischer IPC-/Prozessvertrag:** RAW-02 besitzt den
   transportneutralen Vertrag für Aufruf, Antwort, Ereignis, Abbruch und
   Lebenszyklus. Konkrete Process API und Transportwahl bleiben bei RAW-06 und
   dürfen nicht in den Orchestration Contract durchsickern. / *RAW-02 owns the
   transport-neutral invocation, response, event, cancellation, and lifecycle
   contract. RAW-06 retains the concrete process API and transport choice,
   which must not leak into the orchestration contract.*
2. **IAD202 – Persistenz des Session Context:** Jedes Context-Feld wird als
   flüchtig oder persistent klassifiziert. Nur ausdrücklich bestätigte Fokus-
   und Routingauswahlen mit ihrer Schemaversion dürfen persistieren. Laufende
   Commands, Cancellation Handles sowie abgeleitete State-, Node- und
   Capability-Projektionen bleiben flüchtig und werden aus ihren Owner-
   Verträgen neu aufgebaut. Unbekannte Version oder invalidierte Abhängigkeit
   verwirft den Context fail-closed; die State-Semantik bleibt bei RAW-03. /
   *Every context field is classified as volatile or persistent. Only explicit
   focus and routing choices plus their schema version may persist. In-flight
   commands, cancellation handles, and derived state, node, and capability
   projections remain volatile and are rebuilt from their owning contracts.
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

Beim damaligen Authoring galt als historischer Snapshot: RAW-02 war bis zum
Abschluss von RAW-01 und RAW-03 `Blocked`. Dieser Snapshot ist keine aktuelle
Lifecycle-Quelle. Der aktuelle kanonische Zustand steht ausschließlich im
[`manifest.json`](../../../specs/intake-series/aoc-phase-2/manifest.json) und
in der [`order.md`](../series/order.md). Ein späterer `serial-autonomous`-Lauf
benötigt weiterhin eine neue ausdrückliche Start- und Scope-Autorität. Recovery
verwirft unbestätigten Context, behält den letzten gültigen Snapshot und rät
weder Migration noch Wiederholung. / *At authoring time, the historical
snapshot recorded RAW-02 as Blocked until RAW-01 and RAW-03 were completed.
This snapshot is not a current lifecycle source. Only the linked manifest and
order document define the current canonical state. A later serial-autonomous
run still requires separate current start and scope authority. Recovery
discards unconfirmed context, retains the last valid snapshot, and does not
guess a migration or retry.*

`serial-autonomous` bedeutet hier nur einen späteren, einzeln ausgeführten und
separat autorisierten autonomen Lauf; der Begriff erteilt selbst keine
Startfreigabe. / *Here, `serial-autonomous` means only a later, individually
executed and separately authorised autonomous run; the term itself grants no
start authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Vorgesehene Child-Intakes sind Context Contract, Focus Routing, Capability
Routing und Cancellation/Recovery. / *Planned child intakes are context
contract, focus routing, capability routing, and cancellation/recovery.*

- **AC-001:** Dieselbe Correlation ID ist durch alle Handoffs sichtbar. / *The
  same correlation ID is visible through every handoff.*
- **AC-002:** Fehlende Authority, verlorener Node und Timeout blockieren Side
  Effects. / *Missing authority, a lost node, and timeout block side effects.*
- **AC-003:** Ein Wechsel von Process API oder Transport in RAW-06 verändert
  den logischen RAW-02-Vertrag nicht. / *Changing the process API or transport
  in RAW-06 does not change the logical RAW-02 contract.*
- **AC-004:** Restart-, Versions- und Invalidierungs-Fixtures unterscheiden
  persistente Auswahl von flüchtigem Laufzeitkontext und übernehmen keine
  State-Semantik aus RAW-03. / *Restart, version, and invalidation fixtures
  distinguish persistent choices from volatile runtime context and do not take
  state semantics from RAW-03.*
- **AC-005:** Queue-Fixtures belegen Reihenfolge, Deduplizierung, erlaubte
  idempotente Wiederholung, Abbruch und die ausbleibende automatische
  Wiederholung nicht-idempotenter Aktionen; vor Abschluss des Read-only-Slices
  entsteht kein mutierender Side Effect. / *Queue fixtures prove ordering,
  deduplication, allowed idempotent retry, cancellation, and the absence of
  automatic replay for non-idempotent actions; no mutating side effect occurs
  before the read-only slice is complete.*
- **AC-006:** Review-Evidence weist Security- und Privacy-Negativfälle,
  WCAG-konforme Textstatus, identische logische Ergebnisse auf macOS, Linux und
  Windows sowie die aktuelle Lieferketten-Einstufung `N/A` mit
  Re-Evaluation-Trigger einzeln nach. / *Review evidence separately proves
  security and privacy negative cases, WCAG-conformant textual status,
  identical logical outcomes on macOS, Linux, and Windows, and the current
  supply-chain `N/A` decision with its re-evaluation trigger.*

Positive Evidence belegt deterministisches read-only Routing, gültige
Authority, erlaubte persistente Auswahl, zugängliche Textstatus und
plattformgleiche Vertragsresultate. Negative Fixtures weisen stale oder
inkompatiblen Context, einen unautorisierten Zielnode, unnötige Personendaten,
einen doppelten Command und den Retry einer nicht-idempotenten Aktion ab. /
*Positive evidence proves deterministic read-only routing, valid authority,
allowed persistent choices, accessible textual status, and platform-equivalent
contract results. Negative fixtures reject stale or incompatible context, an
unauthorised target node, unnecessary personal data, duplicate commands, and
replay of a non-idempotent action.*

## Risiken, Revision und Nicht-Autorität / Risks, revision, and non-authority

Risiko ist eine unbemerkte Vermischung des logischen Vertrags mit Transport-,
State- oder UI-Details. Die Owner- und Handoff-Grenzen sowie Cross-Platform-
Fixtures erkennen diese Vermischung. Revision ist bei Handoff-, Authority-,
Schema-, Datenkategorie-, Plattform- oder Abhängigkeitsänderung erforderlich. /
*The risk is accidental mixing of the logical contract with transport, state,
or UI details. Owner and handoff boundaries plus cross-platform fixtures detect
that mixing. Revision is required for a handoff, authority, schema, data
category, platform, or dependency change.*

Dieses Intake erteilt keine UI-, State- oder Adapterautorität und genehmigt
weder Specify noch Implementierung, Remote Writes, Merge oder Bypass. / *This
intake grants no UI, state, or adapter authority and approves neither Specify
nor implementation, remote writes, merge, or bypass.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts

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
