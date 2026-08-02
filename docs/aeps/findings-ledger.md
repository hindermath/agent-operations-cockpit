# AEPS Findings Ledger – AOC

## Zweck, Leseschlüssel und Ausgangsstand / Purpose, reading key, and baseline

Dieses Ledger enthält die initiale AOC-Bestandsaufnahme vom `2026-08-01`.
Kanonischer Upstream-Anker ist
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196).
Die Erfassungs- und Reifezustände folgen dem
[AEPS-Evidence-Vertrag](README.md). / *This ledger contains the initial AOC
baseline. Capture and maturity states follow the AEPS Evidence Contract.*

Die geprüfte Ready-Menge umfasst: / *The assessed Ready set contains:*

| Lastenheft / Intake | Review-ID | Zielhash / target hash | Evidence-Commit |
|---|---|---|---|
| META-LH-01 | `7715d4e3-c116-43ba-a029-a2197dca2233` | `99eab2565a73b3f1fe836feb89b543392360d3a5d56063c13fd28cf2f0a16704` | `ddba7482163c7e61161ad0b90f4e019844335898` |
| META-LH-02 | `d61e9502-00e7-4cb5-8ecd-deca90ee1a97` | `7965323e2981472fd061bfb9ca20fd10d6a6217df53fd0300127de74b0b9c14b` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| META-LH-03 | `cd2c3f92-2db3-4a34-b16a-5c34c304221c` | `8b1a0b37c7938d8ff5577bfb9daaedc710990e95e5470edf65b0761724c668c4` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| RAW-01 | `f9f08f54-95eb-4abd-8ce1-bac180a6f742` | `c61d9786b27ea09e0e954363a1b4335d3255ea55b0f8a5167ee52c25c583f9b6` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| RAW-02 | `b1ffb007-f963-4f0f-b787-492f1b4b6717` | `7b2f4241e92c9dba5eb6b420d98d587b34ffe6a6ee5e607762125687a334c4e6` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| META-LH-04 | `d7451834-8b5d-446c-a88e-658cae7a8c5f` | `f16026d37b04bdf7fa492e41e0a83a8f67b3719497dba5f185bfb35d0b068ea6` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| META-LH-05 | `a37b14c0-2eaf-4ce8-b8e2-ac4e7280652f` | `533ecf072fc81a08c43c7c9a794d30e3ea9237e0e8d75602251373881dfc6ec0` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |

`PendingPublication` ist kein fehlender Nachweis: Review-ID, Base-HEAD und
normalisierter Zielhash binden den lokalen Zustand, aber ein Upstream-Handoff
bleibt bis zum stabilen Commit gesperrt. / *PendingPublication binds the local
state without pretending that unpublished evidence is a stable upstream
artifact.*

## Bereits in #196 verankerte Kandidaten / Candidates already anchored in #196

| Upstream-ID | Kurzname / short name | Initiale Einordnung / initial classification |
|---|---|---|
| `CAND-AEPS-01` | Development Readiness Gate | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-02` | Review Findings Ledger und Coverage Gate | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-03` | Selbsttragender Level-2-Handoff | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-04` | Meta-Lastenheft-Programm | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-05` | Single Ownership und azyklische Series | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-06` | Decision-Resolution vor Specify | `AlreadyRecorded`; `candidate` |
| `CAND-AEPS-07` | Kontrollierte Autonomie je Workitem | `AlreadyRecorded`; `candidate` |
| `CAND-AEPS-08` | Evidence- und Receipt-Vertrag | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-09` | Maintenance als getrennte Level-2-Arbeit | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-10` | Public-Readiness- und Multi-Platform-Baseline | `AlreadyRecorded`; `pilot-pattern` |
| `CAND-AEPS-11` | Accessibility-, Ausbildungs- und Sprachbaseline | `AlreadyRecorded`; `candidate` |
| `CAND-AEPS-12` | Engineering Session als Knowledge-Quelle | `AlreadyRecorded`; `candidate` |

Die folgenden AOC-Findings duplizieren diese Kandidaten nicht. Sie präzisieren
Evidence, Grenzen oder mögliche Lücken. / *The following AOC findings do not
duplicate these candidates. They refine evidence, limits, or possible gaps.*

## AEPS-FIND-AOC-001 – Ready und Series-Lifecycle sind getrennte Wahrheiten

- **Quelle und Lastenheft / Source and intake:** RAW-02-Re-Review
  `b1ffb007-f963-4f0f-b787-492f1b4b6717`; Series-Manifest.
- **Datum und Commit / Date and commit:** `2026-08-01`;
  `PendingPublication`, Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem / Problem:** Ein erfolgreiches Single Review kann fälschlich als
  Ausführbarkeit gelesen werden, obwohl bindende Vorgänger den Series-Status
  weiterhin `Blocked` halten. / *A successful Single review may be mistaken
  for executability while binding predecessors still keep the Series state
  Blocked.*
- **Kontext / Context:** RAW-02 ist formal `Ready`, aber wegen RAW-01 und
  RAW-03 nicht startfähig.
- **Positive Evidence:** Review-Validatoren bestehen; das Review nennt den
  Lifecycle-Blocker ausdrücklich.
- **Negative Evidence:** Ein Workflow, der allein auf `status == Ready`
  startet, würde das Sequencing-Gate umgehen. / *A workflow starting on Ready
  alone would bypass sequencing.*
- **Grenzen / Limits:** Belegt die Trennung für Intake Review und Series;
  andere Lifecycle-Systeme sind nicht validiert.
- **AOC-spezifisch / generisch:** Pfade und RAW-Namen sind AOC-spezifisch; die
  Trennung von Qualitätsfreigabe und Ausführbarkeit ist wahrscheinlich
  generisch.
- **Domäne, Reifegrad / Domain, maturity:** Review and Evidence / Agent
  Authority; `pilot-pattern`.
- **Preset-Bezug / Related presets:** Intake Review, Intake Sequencing,
  Autonomous Run; `CAND-AEPS-07`.
- **Nächste Validierung / Next validation:** In einem zweiten Projekt prüfen,
  ob Ready und Eligibility ebenfalls unabhängig modelliert werden.
- **Promotion-Blocker:** keine Cross-Project-Evidence; kein gemeinsamer
  maschinenlesbarer Ready-to-Eligibility-Vertrag.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-002 – Reparaturautorität muss fachliche Entscheidungen bewahren

- **Quelle und Lastenheft:** META-LH-02, META-LH-03, RAW-01 und RAW-02;
  jeweilige Vorgänger- und Ready-Re-Reviews.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Eine Finding-Reparatur kann unbeabsichtigt bestätigte Decisions,
  Scope, Abhängigkeiten oder Delivery Authority neu entscheiden. / *A finding
  repair can accidentally reopen decisions, scope, dependencies, or delivery
  authority.*
- **Kontext:** Alle vier Reparaturen waren auf benannte IR-IDs begrenzt und
  verlangten danach ein vollständiges Re-Review.
- **Positive Evidence:** IAD101–IAD103 und IAD201–IAD203 blieben unverändert;
  alle Re-Reviews endeten `Ready`.
- **Negative Evidence:** Eine breite Neuformulierung ohne Diff- und
  Authority-Grenze hätte fachliche Entscheidungen stillschweigend verändern
  können.
- **Grenzen:** Die Evidence betrifft dokumentbasierte Intakes, nicht
  Datenbankmigrationen oder Produktcode.
- **AOC-spezifisch / generisch:** IDs sind AOC-spezifisch; begrenzte Reparatur
  plus vollständige Re-Validierung ist generisch.
- **Domäne, Reifegrad:** Review and Evidence / Agent Authority;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Repair, Intake Authoring, Intake Review;
  `CAND-AEPS-06`, `CAND-AEPS-08`.
- **Nächste Validierung:** Repair-Diff in einem weiteren Intake-Programm gegen
  ausdrücklich geschützte Felder prüfen.
- **Promotion-Blocker:** keine Cross-Project-Fixture für geschützte fachliche
  Felder.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-003 – Historische Delivery Authority ist keine aktuelle Authority

- **Quelle und Lastenheft:** META-LH-01 bis META-LH-03 und RAW-01; Ready-
  Re-Reviews und Authoring Receipts.
- **Datum und Commit:** `2026-08-01`; gemischte Evidence: META-LH-01 unter
  `ddba7482163c7e61161ad0b90f4e019844335898`, übrige `PendingPublication`.
- **Problem:** Ein gespeicherter Modus wie `MergeAndSync` oder historischer
  Bypass kann später fälschlich als aktuelle Start- oder Remote-Autorität
  interpretiert werden. / *A stored delivery ceiling or historic bypass can be
  mistaken for current execution authority.*
- **Kontext:** Die reparierten Prompts verlangen eine separate aktuelle
  Entscheidung für Scope, Start, Implementierung, Remote, Merge und Bypass.
- **Positive Evidence:** Fail-closed Prompt-Grenzen und Receipt-Texte bestehen
  die unabhängigen Reviews.
- **Negative Evidence:** Die Vorgängerreviews zeigten, dass ein enabled Prompt
  ohne solche Vorbedingung missverständlich bleibt.
- **Grenzen:** Belegt die Dokument- und Prompt-Semantik, nicht die Runtime-
  Durchsetzung eines Providers.
- **AOC-spezifisch / generisch:** Modusnamen sind implementierungsspezifisch;
  zeitgebundene Authority und least privilege sind generisch.
- **Domäne, Reifegrad:** Agent Authority and Execution; `pilot-pattern`.
- **Preset-Bezug:** Autonomous Run, Parallel Autonomous Run, Intake Authoring;
  `CAND-AEPS-01`, `CAND-AEPS-07`.
- **Nächste Validierung:** Negative Runtime-Fixture für veraltete Authority
  ergänzen und in einem zweiten Projekt anwenden.
- **Promotion-Blocker:** derzeit überwiegend textuelle, keine Ende-zu-Ende-
  Provider-Evidence.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-004 – Prompt-State und Stop-Marker benötigen einen eindeutigen Vertrag

- **Quelle und Lastenheft:** META-LH-03, Review
  `cd2c3f92-2db3-4a34-b16a-5c34c304221c`; Authoring-Validator-Fixtures.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Ein `Enabled`-Ziel darf den vollständigen Blocked-Marker nicht
  enthalten; bereits die erklärende Nennung kann vom Validator als
  Widerspruch erkannt werden. / *An Enabled target cannot contain the complete
  blocked marker; even explanatory use can be interpreted as contradictory.*
- **Kontext:** Das Lastenheft musste die beiden Markerbestandteile getrennt
  erklären, ohne den normativen vollständigen Marker zu emittieren.
- **Positive Evidence:** Beide Receipt-Validatoren bestehen nach der
  eindeutigen Formulierung.
- **Negative Evidence:** Der erste Validatorlauf wies das Enabled-Ziel mit
  vollständigem Marker korrekt ab.
- **Grenzen:** Die konkrete Zeichenfolge gehört zum installierten Preset
  `0.3.0`; eine andere Repräsentation kann das Problem verändern.
- **AOC-spezifisch / generisch:** Die Zeichenfolge ist Preset-spezifisch; die
  Notwendigkeit disjunkter Zustandsrepräsentationen ist generisch.
- **Domäne, Reifegrad:** Requirements Engineering / Agent Authority;
  `observation`.
- **Preset-Bezug:** Intake Authoring, Intake Review.
- **Nächste Validierung:** Template und Validator gegen erklärende
  Dokumentation, blockierte Prompts und Enabled-Prompts gemeinsam testen.
- **Promotion-Blocker:** keine Cross-Project-Evidence; mögliche
  Template-/Validatoränderung benötigt eigenen Level-0-Auftrag.
- **Status:** `PotentialCandidate`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-005 – Secret-Negativfixture darf Evidence, aber keine Provenienzquelle sein

- **Quelle und Lastenheft:** META-LH-03; RF-20; Authoring-Receipt-Validator.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Eine synthetische Secret-Fixture ist notwendige negative
  Evidence, wird aber als gebundene Receipt-Quelle zu Recht als Credential-
  Risiko abgewiesen. / *A synthetic secret fixture is useful negative evidence
  but is correctly rejected as a bound provenance source.*
- **Kontext:** Die Fixture bleibt als benannter Testbefehl im Intake, wurde
  jedoch aus der Receipt-Quellenliste entfernt.
- **Positive Evidence:** Drei Fixture-Suiten sowie alle 14 Receipts bestehen;
  vollständiger Gitleaks-Scan ist grün.
- **Negative Evidence:** Der erste Receipt-Lauf meldete die Fixture als
  Credential-/Private-Key-Pattern.
- **Grenzen:** Gilt für gebundene Quelldateien; eine eng begrenzte, begründete
  Scan-Ausnahme bleibt ein anderer Vertrag.
- **AOC-spezifisch / generisch:** Pfad und Testdaten sind AOC-spezifisch; die
  Trennung von Testinput und Provenienz ist generisch.
- **Domäne, Reifegrad:** Review and Evidence / Security; `pilot-pattern`.
- **Preset-Bezug:** Intake Authoring, Security Governance;
  `CAND-AEPS-08` und RF-20.
- **Nächste Validierung:** Fixture-Rollen explizit als `test-evidence` versus
  `provenance-source` in einem zweiten Preset prüfen.
- **Promotion-Blocker:** keine portable Rollen-Taxonomie und keine
  Cross-Project-Evidence.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-006 – Querschnittsanwendbarkeit braucht Evidence und Re-Evaluation

- **Quelle und Lastenheft:** Ready-Re-Reviews META-LH-01 bis META-LH-03,
  RAW-01 und RAW-02.
- **Datum und Commit:** `2026-08-01`; META-LH-01 committed, übrige
  `PendingPublication`.
- **Problem:** Security, Privacy, A11Y, Plattform und Supply Chain können als
  Schlagworte vorhanden sein, ohne messbare Einstufung oder Trigger. / *Cross-
  cutting topics can be named without measurable applicability or triggers.*
- **Kontext:** Alle fünf Reviews verlangten explizite Anwendbarkeit, positive
  und negative Evidence sowie Re-Evaluation bei Drift.
- **Positive Evidence:** WCAG 2.2 AA, Datenminimierung, Plattformparität und
  begründete Supply-Chain-Einstufungen sind jetzt prüfbar.
- **Negative Evidence:** Die Vorgängerreviews bewerteten unvollständige oder
  unbegründete Einstufungen als High beziehungsweise Medium.
- **Grenzen:** Review beweist Vertragsvollständigkeit, nicht spätere
  Produktwirksamkeit.
- **AOC-spezifisch / generisch:** Konkrete .NET-/IPC-Details sind spezifisch;
  Applicability plus Re-Evaluation ist generisch.
- **Domäne, Reifegrad:** Accessibility and Communication / Repository
  Governance; `pilot-pattern`.
- **Preset-Bezug:** Security, A11Y, Cross-Platform, Architecture;
  `CAND-AEPS-10`, `CAND-AEPS-11`.
- **Nächste Validierung:** dieselbe Matrix an implementierter UI und Runtime
  mit Feldevidence prüfen.
- **Promotion-Blocker:** bislang Requirements-Evidence, keine vollständige
  Produkt- oder Cross-Project-Evidence.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-007 – Reparatur eines Targets invalidiert abhängige Review-Evidence

- **Quelle und Lastenheft:** alle fünf Ready-Re-Reviews; Series-Archive und
  -Receipts.
- **Datum und Commit:** `2026-08-01`; gemischter Publikationsstand.
- **Problem:** Ein fachlich begrenzter Target-Edit ändert Hashbindungen und
  macht ältere Single- und Series-Reviews historisch, auch wenn Reihenfolge und
  Lifecycle unverändert bleiben. / *A bounded target edit changes hash bindings
  and makes older Single and Series reviews historical even when order and
  lifecycle stay unchanged.*
- **Kontext:** Vorgänger wurden bytegleich archiviert, Receipts erneuert und
  vollständige Single-Re-Reviews ausgeführt.
- **Positive Evidence:** Manifestdiffs änderten jeweils nur den Zielhash;
  aktuelle Validatoren bestehen.
- **Negative Evidence:** Ein älteres grünes Review gegen den Vorgängerhash ist
  für das Nachfolgeziel nicht aktuell.
- **Grenzen:** Ein Single Review ersetzt kein neues Series Review.
- **AOC-spezifisch / generisch:** Pfade und Manifest sind AOC-spezifisch;
  transitive Evidence-Invalidierung ist generisch.
- **Domäne, Reifegrad:** Review and Evidence / Requirements Engineering;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Update, Repair, Review und Sequencing;
  `CAND-AEPS-05`, `CAND-AEPS-08`.
- **Nächste Validierung:** maschinenlesbare Impact-Berechnung über Single- und
  Series-Review-Lineage als Fixture erproben.
- **Promotion-Blocker:** kein gemeinsamer Evidence-Abhängigkeitsgraph über
  Preset-Grenzen.
- **Status:** `PotentialCandidate`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-008 – Ownership benötigt Positiv- und Negativgraphen

- **Quelle und Lastenheft:** META-LH-02-Re-Review; Portfoliovertrag,
  Doppelowner- und Zyklus-Fixtures.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Eine lesbare Ownership-Tabelle allein beweist weder eindeutige
  Owner noch Zyklenfreiheit. / *A readable ownership table alone proves neither
  unique ownership nor an acyclic graph.*
- **Kontext:** Neun Owner-Reihen und Handoffs wurden durch einen JSON-Vertrag
  sowie positive und negative Bash-/PowerShell-Fixtures geprüft.
- **Positive Evidence:** gültiger Vertrag besteht auf beiden Oberflächen.
- **Negative Evidence:** Doppelowner löst `PO002`, Zyklus `PO007` aus.
- **Grenzen:** Belegt den aktuellen AOC-Graphen, nicht beliebige dynamische
  Organisationsmodelle.
- **AOC-spezifisch / generisch:** Reihenbezeichnungen sind spezifisch;
  Single Ownership plus DAG ist generisch.
- **Domäne, Reifegrad:** Requirements Engineering / Multi-Agent Work;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Sequencing und potenzielles Ownership-Preset;
  `CAND-AEPS-05`.
- **Nächste Validierung:** komplexere parallele Serie in einem zweiten Projekt.
- **Promotion-Blocker:** Cross-Project-Evidence und Kompatibilitätsregeln
  fehlen.
- **Status:** `AlreadyRecorded`; Upstream `PendingPublication` für neue
  Fixture-Evidence.

## AEPS-FIND-AOC-009 – Evidence-Zahlen ohne benannte Artefakte sind nicht reproduzierbar

- **Quelle und Lastenheft:** META-LH-03-Vorgängerreview IR303 und Ready-
  Re-Review.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Aussagen wie „14 Receipts und Validatorprotokolle“ sind ohne
  Templates, Schemas, Pfade, Befehle, erwartete Exitcodes und RF-Traceability
  nicht reproduzierbar. / *Counts without named artifacts, commands, expected
  codes, and traceability are not reproducible evidence.*
- **Kontext:** META-LH-03 bindet jetzt kanonische Templates, Profil, drei
  Fixture-Suiten, beide Validatorfamilien und RF-zu-AC-Zuordnung.
- **Positive Evidence:** alle 14 Receipts und die gebundenen Suiten bestehen.
- **Negative Evidence:** das Vorgängerreview stufte den reinen Zählnachweis als
  High Finding ein.
- **Grenzen:** Pfadbindung kann semantische Wahrheit nicht allein beweisen.
- **AOC-spezifisch / generisch:** Pfade sind spezifisch; reproduzierbarer
  Evidence-Vertrag ist generisch.
- **Domäne, Reifegrad:** Review and Evidence; `pilot-pattern`.
- **Preset-Bezug:** Intake Authoring, Intake Review; `CAND-AEPS-02`,
  `CAND-AEPS-08`.
- **Nächste Validierung:** Evidence-Vertrag in einem zweiten Repository mit
  abweichender Toolchain anwenden.
- **Promotion-Blocker:** keine projektübergreifende Pfad-/Command-Abstraktion.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-010 – Schema-Validation ersetzt kein Sprach- und A11Y-Review

- **Quelle und Lastenheft:** alle fünf Vorgänger- und Ready-Re-Reviews.
- **Datum und Commit:** `2026-08-01`; gemischter Publikationsstand.
- **Problem:** Vollständige Felder können trotzdem unvollständig übersetzt,
  begrifflich unzugänglich oder nur implizit geordnet sein. / *Structurally
  complete fields may still be partially translated, inaccessible, or only
  implicitly ordered.*
- **Kontext:** Wiederkehrende Findings verlangten DE-first/EN-second,
  Erstbegriffserklärungen, CEFR B2, semantische Überschriften und text-first
  Status.
- **Positive Evidence:** alle Ready-Re-Reviews bestehen die zehn semantischen
  Prüffelder.
- **Negative Evidence:** die Vorgängerreviews enthielten wiederholt High-
  Findings trotz strukturell vorhandener Abschnitte.
- **Grenzen:** Menschliches Review bleibt teilweise urteilsabhängig.
- **AOC-spezifisch / generisch:** Sprachpolicy ist Flottenkontext; die Grenze
  deterministischer Validatoren ist generisch.
- **Domäne, Reifegrad:** Accessibility and Communication / Review and
  Evidence; `pilot-pattern`.
- **Preset-Bezug:** A11Y Governance, Intake Review; `CAND-AEPS-11`.
- **Nächste Validierung:** konsistente semantische Review-Checkliste in einem
  weiteren Projekt und an realer UI anwenden.
- **Promotion-Blocker:** keine Cross-Project-Interrater-Evidence.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-011 – Ready ist keine nachgelagerte Startfreigabe

- **Quelle und Lastenheft:** META-LH-01 bis META-LH-03, RAW-01 und RAW-02;
  exakte nächste Aktionen der Ready-Re-Reviews.
- **Datum und Commit:** `2026-08-01`; gemischter Publikationsstand.
- **Problem:** Ein formal erfolgreiches Intake Review kann als impliziter
  Auftrag für Specify, Autonomous oder Implementierung fehlgedeutet werden. /
  *A successful Intake review can be misread as an implicit downstream start
  instruction.*
- **Kontext:** Jedes Review benennt ausschließlich den read-only Series-Status
  als nächste Aktion und schließt nachgelagerte Aktionen aus.
- **Positive Evidence:** Review-Ergebnisse und Reports enthalten explizite
  Nicht-Autorität.
- **Negative Evidence:** Enabled Copy-ready Prompts bleiben ohne separate
  aktuelle Authority nicht ausführbar.
- **Grenzen:** Belegt Governance-Texte; Runtime muss Authority zusätzlich
  technisch erzwingen.
- **AOC-spezifisch / generisch:** Befehlsnamen sind spezifisch;
  phasenbezogene Authority ist generisch.
- **Domäne, Reifegrad:** Program Governance / Agent Authority;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Review, Autonomous Run; `CAND-AEPS-01`,
  `CAND-AEPS-06`, `CAND-AEPS-07`.
- **Nächste Validierung:** automatisierte Stop-Fixture vom Ready-Ergebnis bis
  zum Ausführungs-Preflight.
- **Promotion-Blocker:** keine Ende-zu-Ende-Authority-Evidence.
- **Status:** `PartiallyRecorded`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-012 – Fachliche Technologieentscheidungen bleiben beim Produkt

- **Quelle und Lastenheft:** RAW-01 IAD101–IAD103 sowie RAW-02 IAD201–IAD203.
- **Datum und Commit:** `2026-08-01`; `PendingPublication`, Base-HEAD
  `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem:** Konkrete TFM-, JSON-, Testframework-, IPC-, Persistenz- und
  Queue-Entscheidungen könnten ungeprüft zu AEPS-Preset-Regeln werden. /
  *Concrete product technology decisions could be generalised into AEPS rules
  without justification.*
- **Kontext:** Die Decisions sind für AOC bestätigt und wurden durch die
  Reparaturen ausdrücklich nicht verändert.
- **Positive Evidence:** RAW-01 und RAW-02 sind mit diesen Decisions `Ready`.
- **Negative Evidence:** Es gibt keine Evidence, dass `net10.0`, xUnit v3 oder
  die konkrete Session-Persistenz für andere Projekte passend sind.
- **Grenzen:** Die Entscheidungen bleiben fachliche AOC-Wahrheit.
- **AOC-spezifisch / generisch:** Technologieinhalt ist AOC-spezifisch; nur der
  Decision-/Preservation-Prozess ist potenziell generisch.
- **Domäne, Reifegrad:** fachliche Owner-Reihen / Requirements Engineering;
  `observation`.
- **Preset-Bezug:** keine Technologie-Promotion; Prozessbezug zu Intake Repair
  und `CAND-AEPS-06`.
- **Nächste Validierung:** keine Preset-Validierung für den Technologieinhalt;
  ausschließlich Prozess-Learning aus AEPS-FIND-AOC-002 verwenden.
- **Promotion-Blocker:** fehlende Allgemeingültigkeit; Produkt-Ownership.
- **Status:** `AocSpecific`; Upstream `NotApplicable` für Technologieinhalte.

## AEPS-FIND-AOC-013 – Parallele Eligibility braucht eine vollständige Prüfachse und Negativ-Evidence

- **Quelle und Lastenheft / Source and intake:** META-LH-04-Re-Review
  `d7451834-8b5d-446c-a88e-658cae7a8c5f`; Eligibility-Vertrag und drei
  Fixtures.
- **Datum und Commit / Date and commit:** `2026-08-01`;
  `PendingPublication`, Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem / Problem:** Eine Modusbezeichnung wie `parallel-autonomous`
  beweist nicht, dass Authority, Side Effects, Reversibilität, Write Scope,
  Decisions, Integration, Review, Abort und Recovery vollständig geprüft
  wurden. / *A mode label such as `parallel-autonomous` does not prove that
  authority, side effects, reversibility, write scope, decisions,
  integration, review, abort, and recovery were fully assessed.*
- **Kontext / Context:** META-LH-04 bindet genau neun Kriterien in einem
  maschinenlesbaren Vertrag und trennt Eligibility, Review, historischen
  Delivery-Modus und aktuelle Authority. / *META-LH-04 binds exactly nine
  criteria in a machine-readable contract and separates eligibility, review,
  historic delivery mode, and current authority.*
- **Positive Evidence:** Die gültige Parallel-Fixture ergibt auf Bash und
  PowerShell `Eligible`; beide Oberflächen enden mit Exitcode 0.
- **Negative Evidence:** Gemeinsamer Write Scope und eine gemeinsame offene
  Decision ergeben jeweils reproduzierbar `Blocked`, ebenfalls mit Exitcode 0
  für den erwarteten Negativnachweis. / *Shared write scope and a shared open
  decision reproducibly produce `Blocked`.*
- **Grenzen / Limits:** Die Evidence prüft Requirements- und Fixture-Semantik,
  nicht den tatsächlichen Start, Worker-Isolation oder Provider-Abbruch.
- **AOC-spezifisch / generisch:** Pfade und Lifecycle-Werte sind AOC-spezifisch;
  vollständige Kriterienkardinalität und Negativ-Evidence für Parallelität
  sind wahrscheinlich projektübergreifend. / *Paths and lifecycle values are
  AOC-specific; complete criteria cardinality and negative parallelism
  evidence are likely cross-project concerns.*
- **Domäne, Reifegrad / Domain, maturity:** Multi-Agent Work / Agent Authority
  and Execution; `pilot-pattern`.
- **Preset-Bezug / Related presets:** Intake Sequencing, Parallel Autonomous
  Run und Intake Review; `CAND-AEPS-05`, `CAND-AEPS-07`.
- **Nächste Validierung / Next validation:** Den Vertrag in einem zweiten
  Projekt anwenden und einen Runtime-Preflight nachweisen, der Shared Write,
  Shared Decision und veraltete Authority technisch verweigert.
- **Promotion-Blocker:** keine Cross-Project- oder Runtime-Evidence; keine
  projektneutrale Rollen- und Pfadabstraktion.
- **Status:** `PotentialCandidate`; Upstream `PendingPublication`.

## AEPS-FIND-AOC-014 – Intake-Wellen brauchen eine deterministische Re-Entry- und Kollisionssemantik

- **Quelle und Lastenheft / Source and intake:** META-LH-05-Single-Review
  `23ebacb2-5e80-4928-b654-673d33693f31`, Finding IR501, sowie Ready-Re-Review
  `a37b14c0-2eaf-4ce8-b8e2-ac4e7280652f` und First-Wave-Fixtures.
- **Datum und Commit / Date and commit:** `2026-08-01`;
  `PendingPublication`, Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem / Problem:** Ein Wave-Authoring-Vertrag, der ausschließlich neue
  Ziele schreiben darf, bleibt bei vollständigem oder teilweisem Vorbestand
  unbestimmt, wenn Verify, Adopt, Supersede, Repair und Collision nicht
  getrennt sind. / *A wave-authoring contract limited to new targets is
  indeterminate for complete or partial pre-existence unless verification,
  adoption, supersession, repair, and collision are distinct outcomes.*
- **Kontext / Context:** META-LH-05 verlangt neun neue RAW-Ziele; alle neun
  Ziele und Receipts existieren bereits und bestehen aktuell beide
  Authoring-Validatoren. Das Lastenheft definiert dennoch keine
  Wiederholungs- oder Teilbestandsregel.
- **Positive Evidence:** Neun vorhandene RAW-Receipts bestehen Bash und
  PowerShell. `AllAbsent` ergibt `CreateAtomic`, `AllMatching` ergibt
  `VerifyOnly`, `Partial` und `Collision` ergeben auf beiden Oberflächen
  `Blocked`; das vollständige Re-Review ist `Ready`.
- **Negative Evidence:** IR501 blockiert `Ready`, weil eine erneute Ausführung
  ohne Kollisionsvertrag bestehende aktive Ziele überschreiben oder einen
  unvollständigen Bestand fälschlich als vollständige Welle melden könnte. /
  *IR501 blocks Ready because an ungoverned rerun could overwrite active
  targets or report a partial wave as complete.*
- **Grenzen / Limits:** Es wurde kein schreibender Authoring-Rerun ausgeführt;
  die Fixture-Evidence belegt den Vertrag, nicht atomare Runtime-Recovery oder
  Cross-Project-Kompatibilität.
- **AOC-spezifisch / generisch:** RAW-Namen und Wellenumfang sind
  AOC-spezifisch; deterministische Re-Entry- und Collision-Policies sind
  wahrscheinlich projektübergreifend. / *Names and cardinality are
  AOC-specific; deterministic re-entry and collision policies are likely
  cross-project concerns.*
- **Domäne, Reifegrad / Domain, maturity:** Requirements Engineering / Review
  and Evidence; `pilot-pattern`.
- **Preset-Bezug / Related presets:** Intake Authoring, Intake Sequencing und
  Intake Repair; möglicher Ausbau von `CAND-AEPS-04` und `CAND-AEPS-08`.
- **Nächste Validierung / Next validation:** Die vier Re-Entry-Klassen in
  einem zweiten Intake-Programm sowie mit atomarer Runtime-Recovery ausführen.
- **Promotion-Blocker:** keine Cross-Project- oder schreibende Runtime-Evidence
  und keine bestätigte Preset-Zuordnung.
- **Status:** `PotentialCandidate`; Upstream `PendingPublication`.
