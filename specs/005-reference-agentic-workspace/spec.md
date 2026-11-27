# Feature-Spezifikation · RAW-01 Reference Agentic Workspace / Feature specification

**Feature** `005-reference-agentic-workspace`

**Erstellt / Created** 2026-11-27

**Status** Entwurf für Specify / Specify draft

**Quelle / Input** [Aktiver RAW-01-Intake / Active RAW-01 intake](../../requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) · [Ready-Einzelreview / Ready Single review](../../docs/reviews/raw-01-reference-agentic-workspace-2026-11-27-dotnet11.md)

## Nutzungsszenarien und Prüfung / User scenarios and testing

DE: IT-Auszubildende ab dem ersten Lehrjahr und erfahrene Fachkräfte sollen
sehen können, welche registrierten Repositories und benötigten Werkzeuge an
einem bestimmten Ort verfügbar sind. **Discovery** bedeutet hier die lesende
Erkennung in ausdrücklich benannten Workspace-Wurzeln. Eine Wurzel ist ein
freigegebenes Startverzeichnis. Ein **Snapshot** ist eine Momentaufnahme
der belegten Beobachtungen. Grundkenntnisse in Git und Terminal reichen aus.

EN: First-year IT apprentices and experienced professionals need to see which
registered repositories and required tools are available in a given workspace.
**Discovery** means inspecting explicitly named workspace roots. A root is
an authorised starting directory. A **snapshot** is a point-in-time record
of supported observations. Basic Git and terminal knowledge is sufficient.

DE: CEFR B2 bezeichnet ein Sprachniveau für verständliche Fachtexte.
WCAG 2.2 AA bezeichnet die hier geltende Stufe der Richtlinien für
Barrierefreiheit, soweit ihre Kriterien auf den Text anwendbar sind.

EN: CEFR B2 is the target language level for understandable technical
writing. WCAG 2.2 AA is the accessibility standard used here wherever
its criteria apply to the text.

### US-1 · Workspace erfassen / Inspect a workspace (P1)

DE: Als Person, die einen Workspace prüft, möchte ich registrierte
Repositories und ihren Git-Zustand innerhalb der freigegebenen Wurzeln
erkennen. Ein verlässlicher Überblick ist Voraussetzung für jede spätere
Nutzung der Momentaufnahme. Die Prüfung ist mit einem vorbereiteten Workspace
und einem Vorher-Nachher-Vergleich unabhängig durchführbar.

EN: As a workspace reviewer, I want to identify registered repositories and
their Git state within authorised roots. A reliable inventory is the basis for
later use of the snapshot. A prepared workspace and a before-and-after
comparison make this journey independently testable.

1. Drei gültige registrierte Repositories in freigegebenen Wurzeln liefern bei
   wiederholter Erkennung dieselbe Reihenfolge und dieselben unveränderten
   Git-Fakten. Die Prüfumgebung belegt null Schreibzugriffe. /
   *Three valid registered repositories in authorised roots produce the same
   order and unchanged Git facts on repeated discovery. The test environment
   verifies zero writes.*
2. Eine fehlende Freigabe oder ein Verweis aus einer freigegebenen Wurzel
   hinaus führt zu einer verständlichen Ablehnung. Der externe Zielort bleibt
   ungelesen und sein Pfad erscheint in keiner Ausgabe. /
   *Missing authority or a reference outside an authorised root yields a clear
   denial. Discovery leaves the external target unread and omits its path from
   all output.*

### US-2 · Momentaufnahme verstehen und weitergeben / Read and share a snapshot (P2)

DE: Als lesende Person oder nachgelagertes Werkzeug möchte ich dieselben
belegten Fakten aus der Konsole oder einer maschinenlesbaren Momentaufnahme
entnehmen. Damit kann ich Ergebnisse vergleichen und der richtigen Umgebung
zuordnen. Ein vorbereiteter Snapshot reicht als Eingabe für diese Prüfung.

EN: As a reader or downstream tool, I want the same supported facts from the
console and the machine-readable snapshot. I can then compare results and
attribute them to the correct environment. A prepared snapshot is sufficient
to test this journey.

1. Für denselben Snapshot liefern beide Darstellungen dieselben fachlichen
   Felder, Werte, Fehlerstatus und dieselbe Schemaversion. Die lesbare Ausgabe
   vermittelt Zustände durch Text und erklärt die Begriffe auf Deutsch und
   Englisch. / *For the same snapshot, both views expose the same domain fields,
   values, error states and schema version. The readable view conveys states
   in text and explains terms in German and English.*
2. Momentaufnahmen eines Hosts und seiner Sandbox (isolierten Umgebung)
   weisen verschiedene opake Kennungen auf. Opak bedeutet, dass die Kennung
   keine persönlichen Merkmale offenlegt. / *Snapshots from a host and its
   sandbox (isolated environment) have distinct opaque identifiers. An opaque
   identifier reveals no personal attributes.*

### US-3 · Fehlende oder veraltete Fakten erkennen / Recognise missing or stale facts (P3)

DE: Als Person, die eine Momentaufnahme bewertet, möchte ich erkennen, welche
Beobachtungen fehlen oder veraltet sind. So kann ich entscheiden, welche Fakten
ich noch verwenden kann. Vorbereitete Fehlerfälle prüfen das unabhängig von
einer echten Arbeitsumgebung.

EN: As a snapshot reviewer, I want to identify missing or stale observations
so that I can decide which facts are still usable. Prepared failure cases test
this independently of a real workspace.

1. Ein Nicht-Repository, ein fehlendes Werkzeug und ein verweigerter Zugriff
   liefern unterscheidbare, strukturierte Fehler oder Verfügbarkeitszustände.
   Nachweisbare Fakten aus anderen freigegebenen Quellen bleiben sichtbar. /
   *A non-repository, a missing tool and denied access yield distinct
   structured issues or availability states. Supported facts from other
   authorised sources remain visible.*
2. Liegt die Aufnahmezeit außerhalb der für die Prüfung vorgegebenen
   Gültigkeit, kennzeichnet die Prüfung die Momentaufnahme als veraltet.
   Eine unbekannte Schemaversion wird erkennbar zurückgewiesen. /
   *If the capture time is outside the validity defined for the check, the
   check marks the snapshot as stale. It explicitly rejects an unknown
   schema version.*
3. Enthalten die Testdaten ein Geheimnis, einen privaten Pfad oder unnötige
   Personendaten, bleiben diese Werte in beiden Darstellungen verborgen.
   / *If a fixture contains a secret, a private path or unnecessary personal
   data, both views suppress those values.*

### Grenzfälle / Edge cases

- **Keine freigegebene Wurzel / No authorised root.** Die Erkennung endet mit
  einer strukturierten Ablehnung. Das Home- oder Arbeitsverzeichnis dient
  nicht als Ersatz. / *Discovery returns a structured denial. It does not
  fall back to the home or working directory.*
- **Git-Fakt nicht ermittelbar / Git fact cannot be determined.** `Unknown`
  bezeichnet einen unbelegten Wert. `Unavailable` bezeichnet eine fehlende
  oder unzugängliche Quelle oder Fähigkeit. Ein eindeutig festgestellter
  abgelöster HEAD ist eine belegte Beobachtung. / *Unknown means a value could
  not be established. Unavailable means a source or capability is missing
  or inaccessible. A demonstrably detached HEAD is a supported observation.*
- **Unerwarteter Schreibversuch / Unexpected write attempt.** Die Prüfung
  muss den Versuch erkennen, bevor eine Änderung erfolgt, und einen sicheren
  Fehler melden. / *The check must detect the attempt before a change occurs
  and report a safe error.*

## Anforderungen / Requirements

### Funktionale Anforderungen / Functional requirements

- **FR-001 · Autorisierte Eingabe / Authorised input.** Discovery MUSS auf die
  ausdrücklich benannten und zum Lesen freigegebenen Workspace-Wurzeln und
  die dort registrierten Repositories begrenzt bleiben. Verweise oder
  Repository-Metadaten dürfen keine zusätzliche Leseberechtigung begründen.
  / *Discovery MUST stay within explicitly named and read-authorised workspace
  roots and the repositories registered there. References or repository
  metadata cannot grant additional read authority.*
- **FR-002 · Beobachtungen / Observations.** Discovery MUSS je freigegebenem
  Repository die Zuordnung zur Wurzel, den Branch (Entwicklungszweig), den
  HEAD (aktuell ausgewählten Git-Stand) und die Working-Tree-Klasse
  (Änderungszustand des Arbeitsbaums) lesen. Sie MUSS die Verfügbarkeit
  benötigter Werkzeuge als eigene Beobachtung erfassen. Die Ausgabe MUSS
  für dieselben Beobachtungen deterministisch geordnet sein. /
  *Discovery MUST read each authorised repository's root association,
  branch, HEAD (selected Git revision) and working-tree class (local change
  state). It MUST record required tool availability as a separate observation.
  Output order MUST be deterministic for the same observations.*
- **FR-003 · Nur lesend / Read-only.** Discovery und Snapshot-Erzeugung
  MÜSSEN Dateien, Git-Zustand und laufende Prozesse unverändert lassen.
  Beobachtete Werkzeuge dürfen durch die Erkennung keine Arbeitsaufträge
  erhalten. / *Discovery and snapshot creation MUST leave files, Git state
  and running processes unchanged. Discovery must not dispatch work to
  discovered tools.*
- **FR-004 · Herkunft und Zeit / Source and time.** Jeder `WorkspaceSnapshot`
  MUSS Quelle, Aufnahmezeit, eine opake Host- oder Node-Kennung und
  Erkennungsfehler an seine Beobachtungen binden. Die Angaben MÜSSEN eine
  Gültigkeitsprüfung und die Unterscheidung von Host und Sandbox ermöglichen.
  / *Every WorkspaceSnapshot MUST associate observations with their source,
  capture time, an opaque host or node identifier and discovery issues.
  These facts MUST support freshness checks and distinguish host and sandbox.*
- **FR-005 · Sichere Fehler / Safe failures.** Fehlende Belege MÜSSEN je
  nach Ursache `Unknown` oder `Unavailable` ergeben. Ablehnungen,
  unbekannte Schemaversionen und veraltete Daten MÜSSEN erkennbar sein.
  Die Prüfung DARF fehlende Fakten weder erfinden noch als Erfolg ausgeben.
  / *Depending on the cause, missing evidence MUST produce Unknown or
  Unavailable. Denials, unknown schema versions and stale data MUST be
  identifiable. The check MUST neither invent missing facts nor report
  them as successful observations.*
- **FR-006 · Austausch und Anzeige / Exchange and display.** Ein
  `WorkspaceSnapshot` MUSS als versioniertes, kanonisches JSON vorliegen.
  Kanonisch bedeutet eine festgelegte Darstellung für Vergleiche. Das
  JSON-Dokument MUSS seine Schemaversion ausdrücklich nennen und mit dem
  zugehörigen JSON Schema prüfbar sein. Das Schema beschreibt die erlaubten
  Felder und Datentypen. Die Konsolenausgabe MUSS dieselben
  Felder, Werte, Status und dieselbe Schemaversion wiedergeben. /
  *A WorkspaceSnapshot MUST have a versioned canonical JSON form. Canonical
  means a defined representation for comparisons. The document MUST state
  its schema version and be verifiable against the corresponding JSON Schema.
  The schema describes allowed fields and data types. Console output MUST
  present the same fields, values, states and schema version.*
- **FR-007 · Datensparsamkeit / Data minimisation.** Die Erfassung MUSS
  austauschgeeignete Metadaten auf den Vertragszweck begrenzen. Ausgaben
  DÜRFEN keine Geheimnisse, Zugangsdaten, Benutzernamen, Home-Pfade,
  Hardware-Seriennummern, unnötige private Pfadsegmente oder Personendaten
  enthalten. Eine neue Datenkategorie erfordert vor ihrer Aufnahme eine
  Datenschutzprüfung. / *Discovery MUST minimise exchangeable metadata to
  what the contract needs. Outputs MUST exclude secrets, credentials, user
  names or home paths, hardware serial numbers, unnecessary private path
  segments and unnecessary personal data. A new data category requires
  privacy review before adoption.*
- **FR-008 · Text und Plattform / Text and platform.** Konsolentext und
  nutzerseitige Dokumentation MÜSSEN Deutsch zuerst und Englisch danach
  liefern. Sie MÜSSEN auf CEFR-B2-Niveau verständlich sein, Zustände ohne
  Farbe vermitteln und die einschlägigen Kriterien von WCAG 2.2 AA
  berücksichtigen. Discovery, Schema, Status und Fehler MÜSSEN auf macOS,
  Linux und Windows dieselbe Bedeutung haben. / *Console text and user
  documentation MUST be German-first, English-second, understandable at
  CEFR B2, convey states without colour and meet applicable WCAG 2.2 AA
  criteria. Discovery, schema, states and errors MUST mean the same thing
  on macOS, Linux and Windows.*

### Konstitution und verbindliche Randbedingungen / Constitution and binding constraints

- **Vertragsplattform / Contract platform** · IAD101 und AC-004 binden
  plattformneutrales `net11.0` und C# 15. Domain und Core, die fachlichen
  Schichten, bleiben frei von Windows-spezifischen Abhängigkeiten. /
  *IAD101 and AC-004 bind platform-neutral net11.0 and C# 15. Domain and
  core, the business layers, stay free of Windows-specific dependencies.*
- **Testvertrag / Test contract** · IAD103 und AC-006 verlangen xUnit.net v3
  mit Microsoft Testing Platform v2, stabile Pakete und `dotnet test`
  auf macOS, Linux und Windows. AC-009 verlangt vor der ersten Paketübernahme
  stabile Versionsauflösung, erfolgreichen Restore, Schwachstellenprüfung
  und eine begründete Entscheidung zur Software-Stückliste (SBOM). /
  *IAD103 and AC-006 require xUnit.net v3 with Microsoft Testing Platform v2,
  stable packages and dotnet test on macOS, Linux and Windows. AC-009 requires
  stable version resolution, successful restore, vulnerability checking and
  a reasoned software bill of materials (SBOM) decision before first adoption.*
- **Vertrauensgrenzen / Trust boundaries** · Dateisystemdaten und beobachtete
  Werkzeugausgaben sind nicht vertrauenswürdig. Verantwortungsgrenzen
  verlaufen zwischen der expliziten Benennung einer Wurzel, dem Lesen der
  lokalen Quellen und der Ausgabe freigegebener Fakten. Eingabe, Status
  und Fehler müssen auf die erteilte Berechtigung und den Zweck beschränkt
  bleiben. / *File-system data and observed tool output are untrusted.
  Trust boundaries separate explicit root selection, local source inspection
  and the presentation of safe facts. Input, states and errors must stay
  within granted authority and purpose.*
- **Projektumgebung / Project environment** · Es gilt der AOC-Eintrag der
  [Projektkonstitution / project constitution](../../.specify/memory/constitution.md).
  C# steht auf der Liste speichersicherer Sprachen. Ausnahme oder
  Hardwarebindung sind für diesen Vertrag nicht erforderlich. /
  *The AOC registry entry applies. C# is on the approved memory-safe language
  list. This contract requires no language exception or hardware dependency.*
- **Nachweispfad / Evidence path** · Die
  [Specify-Checkliste / Specify checklist](checklists/requirements.md)
  hält Preset-Anwendbarkeit, Nachweisgrenzen und Folgeprüfungen fest.
  Plattformnachweise folgen dem macOS-zuerst-Vertrag der Konstitution
  und belegen Plattform, Revision, Befehl, Exit-Code, Hashes und null
  Schreibzugriffe. / *The checklist records preset applicability, evidence
  boundaries and later checks. Platform evidence follows the macOS-first
  constitutional rule and binds the platform, revision, command, exit code,
  hashes and zero writes.*

### Zentrale Begriffe im Vertrag / Key entities

| Entität / Entity | Vertragsinhalt / Contract meaning |
|---|---|
| Workspace-Wurzel / Workspace root | Explizit benannter und freigegebener Rahmen für die Erkennung. / Explicitly named and authorised scope for discovery. |
| Repository-Beobachtung / Repository observation | Zuordnung zur Wurzel, Repository-Kennung, Branch, HEAD und Arbeitsbaumklasse. / Root association, repository identifier, branch, HEAD and working-tree class. |
| Werkzeug-Beobachtung / Tool observation | Verfügbarkeit eines benötigten Werkzeugs. / Availability of a required tool. |
| `WorkspaceSnapshot` | Versionierte Momentaufnahme mit Quelle, Zeitpunkt, opaker Kennung, Beobachtungen und strukturierten Fehlern. / Versioned record of source, time, opaque identity, observations and structured issues. |

## Erfolgskriterien / Success criteria

| ID | Beobachtbares Ergebnis / Observable outcome | Intake |
|---|---|---|
| SC-001 | Zwei Erkennungen unter gleichen Testbedingungen finden dieselben drei erwarteten Repositories in derselben Reihenfolge mit denselben Git-Fakten. / Two discovery runs under equal test conditions find the same three expected repositories in the same order with the same Git facts. | AC-001 |
| SC-002 | Alle vorbereiteten Fälle für Nicht-Repository, fehlendes Werkzeug, Zugriff verweigert und veraltete Daten liefern die jeweils erwartete Bedeutung. Ein unbekanntes Austauschformat wird als solches erkannt. / Every prepared case for a non-repository, missing tool, denied access and stale data reports the expected meaning. An unknown exchange format is recognised. | AC-002, negative evidence |
| SC-003 | Eine Testaufnahme vom Host und eine aus seiner Sandbox sind trotz gleicher Arbeitsdaten eindeutig zuzuordnen. / A test snapshot from the host and one from its sandbox remain attributable even when workspace data is identical. | AC-003 |
| SC-004 | Beide Darstellungen enthalten bei allen positiven und negativen Testaufnahmen dieselben fachlichen Informationen und dieselbe Version. / Both views convey the same domain information and version for all positive and negative test snapshots. | AC-005 |
| SC-005 | Jede positive und negative Erkennungsprüfung verursacht null Schreibzugriffe. Ein Verweis aus der Wurzel hinaus führt zu null Lesezugriffen am fremden Ziel. Kein vorbereiteter sensibler Testwert erscheint in einer der Ausgaben. / Every positive and negative discovery case causes zero writes. An escaping reference causes zero reads at the external target. No planted sensitive value appears in either output. | AC-007 |
| SC-006 | Dieselben Testfälle zeigen auf den drei benannten Plattformen dieselben Status und Fehler. Ein Textreview bestätigt DE/EN, CEFR B2, anwendbare WCAG-2.2-AA-Kriterien und verständliche Zustände ohne Farbe. / The same test cases show the same states and errors on all three named platforms. A text review confirms German and English, CEFR B2, applicable WCAG 2.2 AA criteria and states understandable without colour. | AC-008 |

Die technologischen Akzeptanzvorgaben AC-004, AC-006 und AC-009 stehen bei
den verbindlichen Randbedingungen. / *The binding constraints carry the
technology acceptance conditions AC-004, AC-006 and AC-009.*

## Annahmen und Abgrenzung / Assumptions and boundaries

- DE: Die aufrufende Stelle liefert Wurzeln und Berechtigung. Der Vertrag
  liefert den Aufnahmezeitpunkt und setzt kein allgemeines Ablaufintervall.
  Verbraucher können die für ihre Prüfung vorgegebene Gültigkeit anwenden.
  / *EN: The caller supplies roots and authority. The contract carries capture
  time and sets no universal expiry interval. Consumers can apply the validity
  rule defined for their check.*
- DE: Der Umfang endet bei Beobachtung und Ausgabe von Metadaten. Befehls- und
  Workflow-Ausführung, Arbeitsdateiinhalte, grafische UI, Hardwareerkennung,
  Zugangsdatenverwaltung, Fernzugriff und automatische Snapshot-Speicherung
  gehören nicht zum Vertrag. / *EN: Scope stops at metadata observation and
  output. Command and workflow execution, working-file contents, graphical
  UI, hardware discovery, credential management, remote access and automatic
  snapshot storage are outside this contract.*
- DE: RAW-03 folgt in der Serie vor RAW-02. Übergaben an RAW-02, RAW-03,
  RAW-05 und RAW-06 verwenden den Snapshot-Vertrag. Dieser Text dokumentiert
  die Schnittstelle und die Prüfanforderungen. / *EN: RAW-03 precedes RAW-02
  in the series. Handoffs to RAW-02, RAW-03, RAW-05 and RAW-06 use the snapshot
  contract. This document records the interface and its acceptance conditions.*
