<!-- intake-authoring:begin -->
# RAW-01 – Reference Agentic Workspace / Reference Agentic Workspace

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Git- und Terminal-Grundlagen; keine AOC-Geschichte / basic Git and terminal; no AOC history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Der heutige Workspace ist nur über einzelne Werkzeuge sichtbar. Ziel ist ein
read-only Referenzvertrag für Discovery (Erkennung) und Snapshot ohne versteckte
Writes. / *The current workspace is visible only through separate tools. The
target is a read-only discovery and snapshot reference contract without hidden writes.*

## Systemgrenze, Scope und Non-Goals / Boundary, scope, and non-goals

Im Scope: registrierte Repositories, Branch/HEAD, Working-Tree-Klasse,
Toolverfügbarkeit, Hostidentität und Zeitstempel. Nicht im Scope: Commands,
Dateiinhalte, UI, Hardware, Credentials oder technische Runtimefestlegung.

## Quellen, Findings, Inputs und Outputs / Sources, findings, inputs, and outputs

SRC-157, 161, 177, 181; RF-05, RF-06, RF-10, RF-15. Input sind explizite
Workspace Roots und öffentliche Repositorymetadaten; Output ist ein
versioniertes `WorkspaceSnapshot`-Konzept für RAW-02/03/05/06.

## Anforderungen / Requirements

- **FR-001:** Discovery MUSS Roots, Repository, Branch, HEAD und Status ohne Write erkennen.
- **FR-002:** Snapshot MUSS Quelle, Zeitpunkt, Host/Node und Erkennungsfehler binden.
- **FR-003:** Fehlende oder unlesbare Daten werden `Unknown`/`Unavailable`, nie erfunden.
- **NFR-001:** Console und JSON müssen semantisch dieselben Fakten tragen.
- **NFR-002:** DE/EN, CEFR B2, WCAG 2.2 AA und sichere Fehlerausgabe gelten.

## Trust, Authority, Decisions und Dependencies / Trust, authority, decisions, and dependencies

Dateisystem und Prozessausgaben sind untrusted. Read-only Authority endet an
den benannten Roots. Paket A beantwortet die drei technischen Vertragsfragen:

- **IAD101 – TFM:** Der Referenzvertrag verwendet `net10.0` als
  plattformneutrales Target Framework. Domain- und Core-Verträge dürfen keine
  Windows-spezifische Abhängigkeit erhalten. Die technische Runtime-Realisierung
  bleibt außerhalb dieses Intakes. / *The reference contract uses `net10.0` as
  its platform-neutral target framework. Domain and core contracts must not gain
  a Windows-specific dependency. Runtime implementation remains outside this intake.*
- **IAD102 – Snapshotformat:** `WorkspaceSnapshot` ist ein versioniertes,
  kanonisches JSON-Dokument mit expliziter Schemaversion und JSON Schema. Die
  Konsolenausgabe ist ausschließlich eine Projektion desselben Modells. /
  *`WorkspaceSnapshot` is a versioned canonical JSON document with an explicit
  schema version and JSON Schema. Console output is only a projection of the
  same model.*
- **IAD103 – Testframework:** Der Testvertrag verwendet xUnit.net v3 mit
  Microsoft Testing Platform v2, ausschließlich stabile Pakete und den
  plattformneutralen Aufruf `dotnet test`. / *The test contract uses xUnit.net
  v3 with Microsoft Testing Platform v2, stable packages only, and the portable
  `dotnet test` invocation.*

RAW-01 bleibt Root der Domain-Reihe; der Handoff führt unverändert zu RAW-03
vor RAW-02. / *RAW-01 remains the domain-series root; its handoff still leads
to RAW-03 before RAW-02.*

## Erwartete Child-Intakes und Modus / Expected child intakes and mode

Discovery Contract; Snapshot Schema; Read-only CLI Projection; Error Fixtures.
Modus `manual-assisted`, danach `single-autonomous`; niemals parallel auf dem
gemeinsamen Snapshot-Schema.

## Akzeptanz und Evidence / Acceptance and evidence

- **AC-001:** Drei gültige Repositories werden deterministisch erkannt.
- **AC-002:** Nicht-Repo, fehlendes Tool, Permission Denied und staler Snapshot
  liefern strukturierte negative Evidence ohne Write.
- **AC-003:** Host und Sandbox werden nicht verwechselt.
- **AC-004:** Vertragsartefakte binden `net10.0` und bleiben in Domain und Core
  frei von Windows-spezifischen Abhängigkeiten. / *Contract artifacts bind
  `net10.0`; domain and core remain free of Windows-specific dependencies.*
- **AC-005:** JSON Schema, kanonisches JSON und Konsolenprojektion tragen
  dieselben Snapshot-Felder und dieselbe Schemaversion. / *JSON Schema,
  canonical JSON, and the console projection carry the same snapshot fields
  and schema version.*
- **AC-006:** Stabile xUnit.net-v3-Tests werden über Microsoft Testing Platform
  v2 mit `dotnet test` auf macOS, Linux und Windows erkannt und ausgeführt. /
  *Stable xUnit.net v3 tests are discovered and run through Microsoft Testing
  Platform v2 with `dotnet test` on macOS, Linux, and Windows.*

Revision bei Registry-, Snapshot- oder Authority-Vertrag. Keine Autorität für
Commands, Scaffold oder Implementierung. / *No command, scaffold, or implementation authority.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
