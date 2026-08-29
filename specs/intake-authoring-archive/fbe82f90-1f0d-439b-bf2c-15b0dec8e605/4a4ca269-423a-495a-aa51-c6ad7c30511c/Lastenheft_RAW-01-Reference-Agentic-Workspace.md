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

## Begriffe für den Einstieg / Terms for first-time readers

- **Reference Agentic Workspace / agentischer Referenz-Workspace:** die
  verbindliche Nur-Lese-Sicht auf registrierte Repositories und verfügbare
  Werkzeuge; er führt selbst keine Befehle aus. / *The binding read-only view of
  registered repositories and available tools; it does not execute commands.*
- **Read-only / nur lesend:** Eine Prüfung beobachtet Daten, verändert aber
  weder Dateien noch Prozesse oder Repositoryzustände. **Discovery / Erkennung**
  findet die ausdrücklich benannten Workspace Roots und ihre Repositories. /
  *A read-only check observes data without changing files, processes, or
  repository state. Discovery finds the explicitly named workspace roots and
  their repositories.*
- **Snapshot / Momentaufnahme:** ein datierter Zustandsnachweis. Der
  `WorkspaceSnapshot` ist das gemeinsame, versionierte Datenmodell. **Kanonisch**
  bedeutet, dass eine festgelegte Darstellung für Vergleiche und Hashes gilt. /
  *A snapshot is time-bound state evidence. `WorkspaceSnapshot` is the shared,
  versioned data model. Canonical means that one defined representation is used
  for comparisons and hashes.*
- **JSON und JSON Schema:** JSON ist ein textuelles Datenformat; ein JSON
  Schema beschreibt erlaubte Felder, Typen und die Schemaversion. / *JSON is a
  textual data format; JSON Schema defines allowed fields, types, and the schema
  version.*
- **Target Framework Moniker (TFM):** die kurze Kennung der .NET-Zielplattform;
  `net10.0` bezeichnet hier den plattformneutralen Vertrag. **Domain und Core**
  sind die fachlichen, betriebssystemunabhängigen Schichten. / *A Target
  Framework Moniker is the short identifier for a .NET target platform;
  `net10.0` identifies the platform-neutral contract. Domain and core are the
  operating-system-independent business layers.*
- **xUnit.net v3 und Microsoft Testing Platform v2:** xUnit.net ist das
  Testframework; Microsoft Testing Platform erkennt und startet die Tests.
  `dotnet test` ist der gemeinsame Kommandozeilenaufruf. Eine **Fixture** ist ein
  vorbereiteter positiver oder negativer Testfall. / *xUnit.net is the test
  framework; Microsoft Testing Platform discovers and runs the tests. `dotnet
  test` is the shared command-line invocation. A fixture is a prepared positive
  or negative test case.*
- **Spec Kit:** der kontrollierte Ablauf für Spezifikation und spätere
  Entwicklungsphasen. `Specify` erstellt eine Spezifikation; `Autonomous`
  koordiniert weitere Phasen nur nach separater aktueller Freigabe. / *Spec Kit
  is the controlled workflow for specification and later development phases.
  `Specify` creates a specification; `Autonomous` coordinates later phases only
  after separate current authorisation.*
- **CEFR B2:** das Sprachniveau B2 des Gemeinsamen Europäischen
  Referenzrahmens für verständliche Dokumentation. / *Language level B2 of the
  Common European Framework of Reference for understandable documentation.*

Weitere Begriffe wie Authority, Evidence, Host, Node, Repository und
Working Tree erklärt das [zweisprachige Glossar](../../baseline/glossary.md). /
*The [bilingual glossary](../../baseline/glossary.md) explains additional terms
such as authority, evidence, host, node, repository, and working tree.*

## Systemgrenze, Scope und Non-Goals / Boundary, scope, and non-goals

Im Scope: registrierte Repositories, Branch/HEAD, Working-Tree-Klasse,
Toolverfügbarkeit, Hostidentität und Zeitstempel. Nicht im Scope: Commands,
Dateiinhalte, UI, Hardware, Credentials oder technische Runtimefestlegung. /
*In scope are registered repositories, branch and HEAD, working-tree class,
tool availability, host identity, and timestamp. Commands, file contents,
user-interface (UI) behaviour, hardware, credentials, and technical runtime
implementation are out of scope.*

## Quellen, Findings, Inputs und Outputs / Sources, findings, inputs, and outputs

SRC-157, 161, 177, 181; RF-05, RF-06, RF-10, RF-15. Input sind explizite
Workspace Roots und öffentliche Repositorymetadaten; Output ist ein
versioniertes `WorkspaceSnapshot`-Konzept für RAW-02/03/05/06. / *Sources are
SRC-157, SRC-161, SRC-177, and SRC-181; assigned findings are RF-05, RF-06,
RF-10, and RF-15. Inputs are explicit workspace roots and public-suitable
repository metadata. The output is a versioned `WorkspaceSnapshot` concept for
RAW-02, RAW-03, RAW-05, and RAW-06.*

## Anforderungen / Requirements

- **FR-001:** Discovery MUSS Roots, Repository, Branch, HEAD und Status ohne
  Write erkennen. / *Discovery MUST identify roots, repository, branch, HEAD,
  and status without a write.*
- **FR-002:** Snapshot MUSS Quelle, Zeitpunkt, Host/Node und Erkennungsfehler
  binden. / *The snapshot MUST bind source, time, host or node, and discovery
  failures.*
- **FR-003:** Fehlende oder unlesbare Daten werden `Unknown` oder `Unavailable`,
  nie erfunden. / *Missing or unreadable data becomes `Unknown` or
  `Unavailable`; it is never invented.*
- **NFR-001:** Konsole und JSON MÜSSEN semantisch dieselben Fakten tragen. /
  *Console output and JSON MUST carry semantically identical facts.*
- **NFR-002:** Deutsch zuerst, Englisch danach, CEFR B2, WCAG 2.2 AA und
  sichere Fehlerausgabe sind verbindlich. / *German first, English second,
  CEFR B2, WCAG 2.2 AA, and safe error output are binding.*

## Querschnittsanforderungen / Cross-cutting requirements

- **Security / Sicherheit:** Discovery und Snapshot MÜSSEN innerhalb der
  benannten Roots read-only bleiben. Fehlerausgaben DÜRFEN keine Secrets,
  Zugangstoken, Credentials oder nicht erforderliche private Pfadsegmente
  enthalten. Fehlende Authority wird sicher abgewiesen. / *Discovery and
  snapshot creation MUST remain read-only within the named roots. Error output
  MUST NOT contain secrets, access tokens, credentials, or unnecessary private
  path segments. Missing authority is rejected safely.*
- **Privacy / Datenschutz:** Hostidentität MUSS auf eine für Zuordnung und
  Freshness erforderliche, opake Kennung minimiert werden; Benutzername,
  Home-Pfad, Hardware-Seriennummer und unnötige Personendaten bleiben
  ausgeschlossen. Eine neue Datenkategorie erzwingt vor ihrer Nutzung eine
  erneute Privacy-Prüfung. / *Host identity MUST be minimised to an opaque
  identifier needed for attribution and freshness. User name, home path,
  hardware serial number, and unnecessary personal data remain excluded. A new
  data category requires a renewed privacy review before use.*
- **Accessibility / Barrierefreiheit:** Dieses lernendenorientierte Lastenheft
  und jede textuelle Snapshot-Projektion MÜSSEN WCAG 2.2 Level AA,
  verständliche DE/EN-Paare und eine nicht nur farbliche Zustandsvermittlung
  unterstützen. UI-Verhalten bleibt außerhalb des Scopes. / *This
  learner-facing intake and every textual snapshot projection MUST support WCAG
  2.2 Level AA, understandable German/English pairs, and status meaning that
  does not rely on colour alone. UI behaviour remains out of scope.*
- **Plattform und Cross-Platform:** Discovery, Schema, Status und
  Fehlerbedeutung MÜSSEN auf macOS, Linux und Windows gleich sein.
  Betriebssystemspezifische Adapter bleiben außerhalb von Domain und Core. /
  *Discovery, schema, status, and failure meanings MUST be identical on macOS,
  Linux, and Windows. Operating-system-specific adapters remain outside domain
  and core.*
- **Software-Lieferkette / Software supply chain:** Für diese reine
  Intake-Reparatur ohne Code, Build oder Paketinstallation ist die
  Lieferkettenprüfung `N/A`. Vor der Übernahme von xUnit.net, Microsoft Testing
  Platform oder einer anderen Abhängigkeit MUSS die Anwendbarkeit neu bewertet
  und durch stabile Versionsauflösung, Restore-, Schwachstellen- und, soweit
  anwendbar, SBOM-Nachweise belegt werden. / *Supply-chain validation is `N/A`
  for this intake-only repair, which adds no code, build, or package install.
  Before adopting xUnit.net, Microsoft Testing Platform, or another dependency,
  applicability MUST be reassessed and evidenced by stable version resolution,
  restore and vulnerability checks, and an SBOM where applicable.*

## Trust, Authority, Decisions und Dependencies / Trust, authority, decisions, and dependencies

Dateisystem und Prozessausgaben sind untrusted. Read-only Authority endet an
den benannten Roots. / *File-system and process output is untrusted. Read-only
authority ends at the named roots.* Paket A beantwortet die drei technischen
Vertragsfragen: / *Package A answers the three technical contract questions:*

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
gemeinsamen Snapshot-Schema. / *Expected child intakes are the discovery
contract, snapshot schema, read-only command-line projection, and error
fixtures. The mode is `manual-assisted`, followed by one separately authorised
`single-autonomous` run; work on the shared snapshot schema is never parallel.*

## Akzeptanz und Evidence / Acceptance and evidence

- **AC-001:** Drei gültige Repositories werden deterministisch erkannt. /
  *Three valid repositories are discovered deterministically.*
- **AC-002:** Nicht-Repo, fehlendes Tool, Permission Denied und staler Snapshot
  liefern strukturierte negative Evidence ohne Write. / *A non-repository,
  missing tool, permission denial, and stale snapshot produce structured
  negative evidence without a write.*
- **AC-003:** Host und Sandbox werden nicht verwechselt. / *Host and sandbox
  identities are not confused.*
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
- **AC-007:** Positive und negative Fixtures belegen, dass Discovery und
  Snapshot keine Writes auslösen und dass Fehler Secrets, Credentials, private
  Pfadsegmente und unnötige Personendaten nicht ausgeben. / *Positive and
  negative fixtures prove that discovery and snapshots cause no writes and
  that failures do not expose secrets, credentials, private path segments, or
  unnecessary personal data.*
- **AC-008:** Ein DE/EN-, B2- und WCAG-Review sowie Plattform-Fixtures belegen
  textuelle Zugänglichkeit und dieselben Status- und Fehlerbedeutungen auf
  macOS, Linux und Windows. / *A German/English, B2, and WCAG review plus
  platform fixtures prove textual accessibility and identical status and
  failure meanings on macOS, Linux, and Windows.*
- **AC-009:** Vor der ersten Paketübernahme liegen stabile Versionsauflösung,
  erfolgreicher Restore, Schwachstellenprüfung und eine begründete SBOM-
  Anwendbarkeitsentscheidung vor. / *Before the first package adoption, stable
  version resolution, successful restore, vulnerability checking, and a
  reasoned SBOM applicability decision are available.*

## Evidence, Risiken und Annahmen / Evidence, risks, and assumptions

Positive Evidence umfasst deterministische Discovery-Fixtures, Schema- und
Konsolenparität, read-only Dateisystemnachweis, plattformübergreifende Testläufe
und die Querschnittsprüfungen aus AC-007 bis AC-009. Negative Evidence umfasst
Nicht-Repository, fehlendes Tool, Permission Denied, stale oder unbekannte
Schemaversion, simulierten Write-Versuch, Secret- und Personendatenmarker sowie
abweichende Plattformprojektion. / *Positive evidence covers deterministic
discovery fixtures, schema and console parity, read-only file-system evidence,
cross-platform test runs, and the cross-cutting checks from AC-007 through
AC-009. Negative evidence covers a non-repository, missing tool, permission
denial, stale or unknown schema version, a simulated write attempt, secret and
personal-data markers, and a divergent platform projection.*

Risiken sind ein veralteter Snapshot, die Verwechslung von Host und Sandbox
sowie sensible Details in Fehlerausgaben. Freshness, opake Identitäten,
strukturierte Fehler und Negativ-Fixtures begrenzen diese Risiken. Annahme:
Workspace Roots werden ausdrücklich bereitgestellt; untrusted Toolausgaben
bleiben Evidence und werden nie zu Authority. / *Risks are a stale snapshot,
confusing host and sandbox, and sensitive details in error output. Freshness,
opaque identities, structured failures, and negative fixtures mitigate these
risks. Workspace roots are assumed to be supplied explicitly; untrusted tool
output remains evidence and never becomes authority.*

## Revisionsbedingungen und Nicht-Autorität / Revision and non-authority

Revision erfolgt bei geändertem Registry-, Snapshot-, Datenkategorie-,
Dependency- oder Authority-Vertrag. Dieses Intake genehmigt weder Commands,
Scaffold noch Implementierung. Jeder nachgelagerte Lauf benötigt eine eigene
aktuelle Start- und Scope-Autorität. / *Revise this intake when the registry,
snapshot, data-category, dependency, or authority contract changes. This intake
approves no command, scaffold, or implementation. Every downstream run requires
separate current start and scope authority.*

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
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung Scope, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. Das gespeicherte `MergeAndSync` und ein aktuelles Review allein reichen nicht aus. / Do not start unless a separate current user decision explicitly authorises downstream scope, implementation, remote writes, merge, and bypass. Stored `MergeAndSync` and a current review alone are insufficient.
```
<!-- intake-authoring:end -->
