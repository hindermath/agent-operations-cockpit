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
den benannten Roots. Offene Decisions: TFM, Manifest-/Snapshotformat,
Testframework. Root der Domain-Reihe; Handoff zu RAW-03 vor RAW-02.

## Erwartete Child-Intakes und Modus / Expected child intakes and mode

Discovery Contract; Snapshot Schema; Read-only CLI Projection; Error Fixtures.
Modus `manual-assisted`, danach `single-autonomous`; niemals parallel auf dem
gemeinsamen Snapshot-Schema.

## Akzeptanz und Evidence / Acceptance and evidence

- **AC-001:** Drei gültige Repositories werden deterministisch erkannt.
- **AC-002:** Nicht-Repo, fehlendes Tool, Permission Denied und staler Snapshot
  liefern strukturierte negative Evidence ohne Write.
- **AC-003:** Host und Sandbox werden nicht verwechselt.

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
