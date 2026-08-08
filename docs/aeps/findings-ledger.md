# AEPS Findings Ledger – AOC

## Zweck, Leseschlüssel und Ausgangsstand / Purpose, reading key, and baseline

Dieses Ledger enthält die initiale AOC-Bestandsaufnahme vom `2026-08-01`.
Kanonischer Upstream-Anker ist
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196).
Die Erfassungs- und Reifezustände folgen dem
[AEPS-Evidence-Vertrag](README.md). / *This ledger contains the initial AOC
baseline. Capture and maturity states follow the AEPS Evidence Contract.*

Die Menge der aktuell zielhashgültigen `Ready`-Review-Ergebnisse umfasst: /
*The set of target-hash-current Ready review results contains:*

| Lastenheft / Intake | Review-ID | Zielhash / target hash | Evidence-Commit |
|---|---|---|---|
| META-LH-01 | `7715d4e3-c116-43ba-a029-a2197dca2233` | `99eab2565a73b3f1fe836feb89b543392360d3a5d56063c13fd28cf2f0a16704` | `ddba7482163c7e61161ad0b90f4e019844335898` |
| META-LH-02 | `56da6c85-f3ca-4557-86a1-035c42f0b754` | `7965323e2981472fd061bfb9ca20fd10d6a6217df53fd0300127de74b0b9c14b` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| META-LH-03 | `cd2c3f92-2db3-4a34-b16a-5c34c304221c` | `8b1a0b37c7938d8ff5577bfb9daaedc710990e95e5470edf65b0761724c668c4` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| RAW-01 | `f9f08f54-95eb-4abd-8ce1-bac180a6f742` | `c61d9786b27ea09e0e954363a1b4335d3255ea55b0f8a5167ee52c25c583f9b6` | `PendingPublication`; Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898` |
| RAW-02 | `b5b1c9d3-9248-4703-9d7f-358dd4ae8398` | `7b2f4241e92c9dba5eb6b420d98d587b34ffe6a6ee5e607762125687a334c4e6` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| META-LH-04 | `c9ea6131-9680-40d7-a50e-c9bcd0c2393c` | `87b454f82e40288625d5613099795a39fc236d514f8868fd17d3907930ccd8bc` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| META-LH-05 | `a9e9f685-0287-4048-8ea8-97f1d67701c6` | `533ecf072fc81a08c43c7c9a794d30e3ea9237e0e8d75602251373881dfc6ec0` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-03 | `d868f04f-cfe3-4393-98ab-6f4451526d0d` | `7c6248efe4bb77bc8767d0b0302dcd968c3da95c5fa3c428681f1e2968c9fb22` | `PendingPublication`; Base-HEAD `60706c5dc6d96996fd7b4b4780c0b736a643dbb0` |
| RAW-04 | `3fd458f6-7d86-4961-a03d-05ae4bb89662` | `d3b4240276767a2cd67e86292ccc3b00f7d1aae32b583e081c0fc02751dcbc10` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-05 | `e81d7013-defc-4649-9f08-ff839f48301b` | `69eb3cc6c4aa43c3472f2c7f976d19de935ee28562b4eb4cb15a1bc205248659` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-06 | `bcf426d0-4b2b-4add-86e6-ff6bf3f1dfbe` | `957e8c5a6607f900d88d4e854eee3373410142735e4b8b8eb893c9e0a65bf3fb` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-07 | `b4e3bed0-6002-4110-b378-01de9f3d040e` | `319a704fcb875f3996ce5aba182c0878718a21d011b38c5af09e81998ca6a7ed` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-08 | `fbcfda58-7c07-417b-9eb9-6167fbd78dc7` | `e9c39efd55e9ca5646eaf0c6e52b4bcf8d50b3ead10ea494b0499594251d1f55` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |
| RAW-09 | `fdf2a68c-ab87-462c-9622-3e7cd39bd164` | `640af2a4eb49b0c0dbb966e82f7bd06e1006dea4aa46fba66b368d59b577ce56` | `PendingPublication`; Base-HEAD `a3629bd20c3596579dfa7f333e6cc8e24ca5963a` |

`PendingPublication` ist kein fehlender Nachweis: Review-ID, Base-HEAD und
normalisierter Zielhash binden den lokalen Zustand, aber ein Upstream-Handoff
bleibt bis zum stabilen Commit gesperrt. / *PendingPublication binds the local
state without pretending that unpublished evidence is a stable upstream
artifact.*

Die strengere formale Ready-Grenze und die globale Review-Sperre verlangen
zusätzlich ein aktuell validierbares Authoring Receipt. Der Abgleich vom
`2026-08-08` ergibt vierzehn vollständig gate-konforme Ziele: `META-LH-01` bis
`META-LH-05` sowie `RAW-01` bis `RAW-09`. Alle Authoring Receipts und alle
aktuellen, nicht supersedierten Single Reviews bestehen auf Bash und
PowerShell. Das vollständige RAW-09-Ersatzreview ist `Ready`; `IR901` bis
`IR906` sowie `IRQ901` bis `IRQ903` sind erledigt. Das globale Review-Gate ist
damit `OpenForSeparateAuthorization`. Es erteilt selbst weder Start-, Specify-,
Implementierungs-, Remote-, Merge-, Bypass-, Preset- noch Promotion-Authority.
/ *The stricter Ready boundary also requires a currently valid Authoring
Receipt. The 2026-08-08 comparison now has fourteen fully gate-compliant
targets: META-LH-01 through META-LH-05 and RAW-01 through RAW-09. Every current
Receipt and non-superseded Single review passes Bash and PowerShell. The
complete RAW-09 replacement review is Ready and resolves IR901 through IR906
and IRQ901 through IRQ903. The global review gate is therefore open for a
separate authorisation; it grants no downstream or promotion authority by
itself.*

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
  begründete Supply-Chain-Einstufungen sind jetzt prüfbar. Das Copilot-
  Follow-up zu AOC-PR #9 führte zusätzlich zu portablen PowerShell-
  Entrypoints mit geprüftem `python3`-zu-`python`-Fallback.
- **Negative Evidence:** Die Vorgängerreviews bewerteten unvollständige oder
  unbegründete Einstufungen als High beziehungsweise Medium. Die in PR #9
  gemergten Wrapper setzten `python3` direkt voraus und waren damit auf
  Windows-Umgebungen mit ausschließlich `python` nicht reproduzierbar.
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

## AEPS-FIND-AOC-007 – Target- oder Source-Drift invalidiert abhängige Evidence

- **Quelle und Lastenheft:** alle fünf Meta-Ready-Re-Reviews, Series-Archive und
  -Receipts sowie die Receipt-Revalidierung vom `2026-08-05`.
- **Datum und Commit:** `2026-08-01` bis `2026-08-05`; neue
  Validierungsevidence `PendingPublication` auf Base-HEAD
  `b69079623e41918dd8ad6db4572c070534cbad88`.
- **Problem:** Ein fachlich begrenzter Target-Edit oder spätere Drift einer
  gebundenen Quelle ändert Hashbindungen und macht abhängige Evidence
  unvollständig oder historisch, auch wenn Zielhash, Reihenfolge und Lifecycle
  unverändert bleiben. / *A bounded target edit or later drift in a bound source
  can invalidate dependent evidence even while target hash, order, and
  lifecycle remain unchanged.*
- **Kontext:** Vorgänger wurden bytegleich archiviert, Receipts erneuert und
  vollständige Single-Re-Reviews ausgeführt.
- **Positive Evidence:** Manifestdiffs änderten jeweils nur den Zielhash;
  alle acht aktuellen Ready-Review-Ergebnisse bestehen weiterhin Bash und
  PowerShell. Fünf zugehörige Authoring Receipts sind vollständig aktuell.
- **Negative Evidence:** Die Authoring Receipts von `META-LH-02`, `META-LH-04`
  und `META-LH-05` scheitern auf beiden Oberflächen an gebundener
  Source-Hash-Drift, obwohl ihre Target-Hashes und Ready-Ergebnisse aktuell sind.
- **Grenzen:** Ein Single Review ersetzt weder ein neues Series Review noch die
  aktuelle Revalidierung aller gebundenen Authoring-Quellen.
- **AOC-spezifisch / generisch:** Pfade und Manifest sind AOC-spezifisch;
  transitive Evidence-Invalidierung ist generisch.
- **Domäne, Reifegrad:** Review and Evidence / Requirements Engineering;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Update, Repair, Review und Sequencing;
  `CAND-AEPS-05`, `CAND-AEPS-08`.
- **Nächste Validierung:** maschinenlesbare Impact-Berechnung über
  Authoring-Quellen, Single- und Series-Review-Lineage als Fixture erproben und
  die drei driftenden Receipts nur nach ausdrücklicher Repair-Autorität erneuern.
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
  Prüffelder. Das unabhängige Copilot-Follow-up erkannte zusätzlich ein nicht
  nummeriertes Statistik-Phasenlabel und eine nicht DE-first formulierte
  historische Receipt-Überschrift.
- **Negative Evidence:** die Vorgängerreviews enthielten wiederholt High-
  Findings trotz strukturell vorhandener Abschnitte. Das Phasenlabel wurde
  korrigiert; das historische Receipt bleibt gemäß seinem späteren
  Provenienz-Supersession-Receipt byte-identisch und wird nicht nachträglich
  umgeschrieben.
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

- **Quelle und Lastenheft:** META-LH-01 bis META-LH-05 und RAW-01 bis RAW-09;
  exakte nächste Aktionen der Ready-Re-Reviews sowie die am `2026-08-05`
  ausdrücklich autorisierte AOC-weite Review-Sperre.
- **Datum und Commit:** `2026-08-01` bis `2026-08-05`; neue Gate-Evidence
  `PendingPublication` auf Base-HEAD
  `b69079623e41918dd8ad6db4572c070534cbad88`.
- **Problem:** Ein formal erfolgreiches Intake Review kann als impliziter
  Auftrag für Specify, Autonomous oder Implementierung fehlgedeutet werden. /
  *A successful Intake review can be misread as an implicit downstream start
  instruction.*
- **Kontext:** Jedes Review benennt ausschließlich den read-only Series-Status
  als nächste Aktion und schließt nachgelagerte Aktionen aus. Zusätzlich
  blockiert die neue globale Regel alle 14 Ziele, bis alle gleichzeitig aktuelle
  formal validierte `Ready`-Evidence besitzen; danach bleibt `META-LH-01` das
  erste Ziel mit separatem Startauftrag.
- **Positive Evidence:** Review-Ergebnisse und Reports enthalten explizite
  Nicht-Autorität. Kanonische Authority-Gates, Programmindex, Reihenfolge,
  Autonomiemodell, README, AEPS-Vertrag und alle fünf Agentenflächen spiegeln
  dieselbe fail-closed Gesamtregel.
- **Negative Evidence:** Aktuell bestehen acht Review-Ergebnisse, aber nur fünf
  Ziele den vollständigen Review-plus-Receipt-Vertrag. Die Source-Hash-Drift in
  drei Receipts und sechs noch fehlende Ready-Reviews halten das Gate konkret
  geschlossen. Eine ausführbare Ende-zu-Ende-Preflight-Fixture fehlt noch.
- **Grenzen:** Belegt Governance-Texte und bewusste menschliche
  Portfolio-Authority; Runtime muss die Sperre zusätzlich technisch erzwingen.
- **AOC-spezifisch / generisch:** Die vollständige 14er-Sperre und
  `META-LH-01` als erstes Ziel sind AOC-spezifisch. Die Trennung von Review,
  Portfolio-Gate und aktueller Startautorität ist generisch.
- **Domäne, Reifegrad:** Program Governance / Agent Authority;
  `pilot-pattern`.
- **Preset-Bezug:** Intake Review, Autonomous Run; `CAND-AEPS-01`,
  `CAND-AEPS-06`, `CAND-AEPS-07`.
- **Nächste Validierung:** automatisierte Stop-Fixture vom Portfoliozustand
  `13/14 Ready`, von Drift und von vollständiger Coverage bis zum
  Ausführungs-Preflight.
- **Promotion-Blocker:** keine Ende-zu-Ende-Authority- oder
  Cross-Project-Evidence; AOC-spezifische Zielmenge.
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
  `d7451834-8b5d-446c-a88e-658cae7a8c5f`; Eligibility-Vertrag, drei Fixtures
  und Copilot-Follow-up zu AOC-PR #9.
- **Datum und Commit / Date and commit:** `2026-08-01`;
  `PendingPublication`, Base-HEAD `ddba7482163c7e61161ad0b90f4e019844335898`.
- **Problem / Problem:** Eine Modusbezeichnung wie `parallel-autonomous`
  beweist nicht, dass Authority, Side Effects, Reversibilität, Write Scope,
  Decisions, Integration, Review, Abort und Recovery vollständig geprüft
  wurden. Ein Validator, der diese Regeln nochmals fest eincodiert, kann trotz
  maschinenlesbarem Vertrag unbemerkt davon abweichen. / *A mode label does
  not prove complete assessment. A validator that hard-codes the rules again
  can silently drift even when a machine-readable contract exists.*
- **Kontext / Context:** META-LH-04 bindet genau neun Kriterien in einem
  maschinenlesbaren Vertrag und trennt Eligibility, Review, historischen
  Delivery-Modus und aktuelle Authority. / *META-LH-04 binds exactly nine
  criteria in a machine-readable contract and separates eligibility, review,
  historic delivery mode, and current authority.*
- **Positive Evidence:** Die gültige Parallel-Fixture ergibt auf Bash und
  PowerShell `Eligible`; beide Oberflächen enden mit Exitcode 0. Der lokale
  Follow-up-Validator wertet nun alle `requires*`- und `allows*`-Regeln aus dem
  Vertrag aus; Tests für geänderte Allowance und ein neues Required Gate
  bestehen.
- **Negative Evidence:** Gemeinsamer Write Scope und eine gemeinsame offene
  Decision ergeben jeweils reproduzierbar `Blocked`. Die gemergte
  Vorgängerversion prüfte dieselben Flags jedoch als duplizierte feste
  Bedingung und hätte bei Vertragsänderungen driften können. / *Shared write
  scope and a shared open decision reproducibly block. The merged predecessor
  duplicated the flags in code and could drift when the contract changed.*
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
- **Nächste Validierung / Next validation:** Den vertragsgetriebenen Validator
  in einem zweiten Projekt sowie mit Contract-Mutation-Fixtures anwenden und
  einen Runtime-Preflight nachweisen, der Shared Write, Shared Decision und
  veraltete Authority technisch verweigert.
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

## AEPS-FIND-AOC-015 – Receipt-Decision-State muss der Target-Semantik entsprechen

- **Quelle und Lastenheft / Source and intake:** RAW-03-Single-Review
  `1159da03-43fd-41ae-9876-f3df2633af12`, Finding IR301; vollständiges
  Ready-Re-Review `d868f04f-cfe3-4393-98ab-6f4451526d0d`; erneuertes Authoring
  Receipt `ad3b1035-4206-414b-bf06-f852cae916da`. / *Initial Single review,
  finding IR301, complete Ready re-review, and renewed Authoring Receipt.*
- **Datum und Commit / Date and commit:** `2026-08-02`;
  `PendingPublication`, Base-HEAD
  `60706c5dc6d96996fd7b4b4780c0b736a643dbb0`, Ergebnis-Hash
  `10c1b13052d919f6d3d612135dbba359e0296f85a0985636df41d7c65aaf4931`,
  Ready-Ergebnis-Hash
  `d95f10682ee1ea21b505ed53f74e800ec4e8b468a4bb26d7435afdf67bed31e6`.
- **Problem / Problem:** Ein schema- und hashgültiges Authoring Receipt kann
  `decisions=[]`, `openDecisionIds=[]` und `questionCount=0` ausweisen, obwohl
  das gebundene Target eine materielle offene Entscheidung nennt. Automatisierung
  könnte dadurch fachliche Klärungsbedarfe übersehen. / *A schema-valid and
  hash-current authoring Receipt can claim no decisions or questions while its
  bound target declares a material open decision. Automation may therefore
  overlook required domain clarification.*
- **Kontext / Context:** Das Vorgänger-RAW-03 nannte Zeitquelle,
  Freshness-Schwellen und Confidence-Modell als offen; Portfoliovertrag und
  Decision Register banden sie an `DEC-T03`. Das damalige Receipt führte keine
  offene Decision und bestand trotzdem beide Validatoren. Das begrenzte Update
  brachte Target, Decision Register und Receipt manuell wieder in semantische
  Parität. / *The predecessor target bound three open questions to DEC-T03
  while its Receipt recorded none and still passed both validators. The bounded
  update manually restored semantic parity across target, decision register,
  and Receipt.*
- **Positive Evidence:** Das erste Single Review erkannte den Widerspruch und
  endete korrekt `NeedsClarification`. Nach den ausdrücklichen Entscheidungen
  IAD301 bis IAD303 bestehen erneuertes Receipt und vollständiges Re-Review auf
  Bash und PowerShell; das Re-Review ist `Ready` mit null Findings und null
  offenen Fragen. / *The initial review detected the conflict. After explicit
  IAD301 through IAD303, the renewed Receipt and complete re-review pass on both
  surfaces, and the re-review is Ready with no findings or questions.*
- **Negative Evidence:** Bash und PowerShell akzeptieren das widersprüchliche
  Authoring Receipt, weil die aktuelle Prüfung Hash, Schema und Feldform, aber
  nicht die semantische Decision-Parität zum Target nachweist. / *Both
  authoring validators accept the contradictory Receipt because current checks
  prove hashes, schema, and field shape but not semantic decision parity with
  the target.*
- **Grenzen / Limits:** Die positive Evidence belegt eine manuelle, reviewte
  Reparatur, aber keine automatische semantische Validatorprüfung. Sie betrifft
  dokumentbasierte Decision-Metadaten und beweist weder einen portablen Parser
  für beliebige natürlichsprachliche Decision-Abschnitte noch Cross-Project-
  Wirkung. / *The positive evidence proves a manually reviewed repair, not an
  automated semantic validator or cross-project effect.*
- **AOC-spezifisch / generisch:** `DEC-T03` und die State-Fragen sind
  AOC-spezifisch; die semantische Übereinstimmung von Target und Receipt ist
  projektübergreifend wahrscheinlich relevant. / *The State decision is
  AOC-specific; semantic agreement between target and Receipt is likely
  cross-project relevant.*
- **Domäne, Reifegrad / Domain, maturity:** Review and Evidence / Requirements
  Engineering; `observation`.
- **Preset-Bezug / Related presets:** Intake Authoring und Intake Review;
  `CAND-AEPS-06`, `CAND-AEPS-08`.
- **Nächste Validierung / Next validation:** Positive und negative Fixtures
  für konsistent offene, konsistent geschlossene sowie widersprüchliche
  Decision-Felder in einem zweiten Intake-Programm prüfen. / *Validate
  consistent-open, consistent-resolved, and contradictory decision metadata in
  a second intake programme.*
- **Promotion-Blocker:** keine allgemeine Decision-Extraktion, keine
  Cross-Project-Fixture und keine Level-0-Authority für Validatoränderungen.
- **Status:** `PotentialCandidate`; Upstream `PendingPublication`.

**Ergänzende Evidence vom 2026-08-08 / Additional evidence from 2026-08-08:**
RAW-08 bestätigt dasselbe Muster ein zweites Mal innerhalb des AOC. Das
begrenzte Update bindet `IAD801` bis `IAD803` konsistent in Target, Decision
Register und Authoring Receipt. Das vollständige Single Review
`5d0b7069-0a37-4339-88ba-a512409fd8f6` besteht auf Bash und PowerShell,
erledigt `IR801` und meldet null offene Fragen. Ergebnis-Hash ist
`83874c4c89cf635f384f6d7705122be4f511131cb35916f8acdf38d7df25febe`;
Evidence bleibt `PendingPublication` auf Base-HEAD
`a3629bd20c3596579dfa7f333e6cc8e24ca5963a`. Das Review bleibt wegen der
unabhängigen Findings `IR802` bis `IR806` bei `NeedsRemediation`. Damit ist
belegt, dass hergestellte Decision-Parität genau ihr Finding schließt, aber
keine pauschale Ready-Freigabe erzeugt. / *RAW-08 confirms the same pattern a
second time inside AOC. IAD801 through IAD803 are consistent across target,
Decision Register, and Authoring Receipt; the validated Single review resolves
IR801 with zero questions. Independent IR802 through IR806 still produce
NeedsRemediation, proving that restored decision parity closes its own finding
without implying overall Ready.*

**Ergänzende Ready-Evidence vom 2026-08-08 / Additional Ready evidence from
2026-08-08:** Das autorisierte Repair bewahrt IAD801 bis IAD803 und schließt
`IR802` bis `IR806` durch einen versionierten Workflow-Evidence-Vertrag,
positive und negative Offline-Fixtures, typisierte Handoffs, Cross-Cutting-
Evidence sowie acht fail-closed Authority-Gates. Das vollständige Ersatzreview
`fbcfda58-7c07-417b-9eb9-6167fbd78dc7` besteht auf Bash und PowerShell mit
`Ready`, null Findings und null offenen Fragen; Ergebnis-Hash ist
`2c338c9410e7184ad68d924999395eccc95837af2e2351c7dda6bd5b652379ed`.
Diese weitere AOC-interne Evidence stärkt `AEPS-FIND-AOC-002`, `003`, `006`,
`009`, `010`, `011` und `015`, erzeugt aber keine neue Finding-Klasse und
keine Cross-Project- oder Runtime-Evidence. / *The authorised repair preserves
IAD801 through IAD803 and resolves IR802 through IR806 with a versioned
contract, positive and negative offline fixtures, typed handoffs,
cross-cutting evidence, and eight fail-closed authority gates. The complete
replacement review passes both validators as Ready with no findings or open
questions. This additional AOC-local evidence strengthens existing findings
without creating a new finding class, cross-project evidence, or runtime
evidence.*

**Ergänzende RAW-09-Evidence vom 2026-08-08 / Additional RAW-09 evidence from
2026-08-08:** Das erste vollständige Single Review
`90d504e8-88d1-4d68-8d1c-1c647478ad8b` meldete sechs High-Findings und drei
offene Entscheidungen. Das begrenzte Update schloss IAD901 und IAD902,
definierte Promotion Authority als neue menschliche Einzelfreigabe ohne
Standing Grant oder Bypass und band einen versionierten Vertrag sowie positive
und negative Offline-Fixtures. Das vollständige Ersatzreview
`fdf2a68c-ab87-462c-9622-3e7cd39bd164` besteht auf Bash und PowerShell mit
`Ready`, null Findings und null offenen Fragen; Ergebnis-Hash ist
`60eb98213111a767d9f9c655529850b6b425871fa8cb2380e1e07fcdf85de6aa`.
Alle vierzehn aktiven Lastenhefte erfüllen damit gleichzeitig die formale
Ready-Grenze. Diese AOC-interne Evidence stärkt `AEPS-FIND-AOC-002`, `003`,
`006`, `007`, `009`, `010`, `011` und `015`, erzeugt aber keine neue
Finding-Klasse, keine Cross-Project-Evidence und keine Promotion Authority. /
*The initial complete RAW-09 review reported six High findings and three open
decisions. The bounded update closed both decisions, made promotion a fresh
per-proposal human approval without a standing grant or bypass, and added a
versioned contract with positive and negative offline fixtures. The complete
replacement review passes both validators as Ready with no findings or open
questions. All fourteen active intakes now meet the formal Ready boundary at
the same time. This remains AOC-local evidence and grants no promotion.*

**Ergänzende Abschluss-Serienreview-Evidence vom 2026-08-08 / Additional
completion Series-review evidence from 2026-08-08:** Das vollständige aktuelle
Series Review `35f4d174-cef2-4293-8994-a0263bc10b3f` bestätigt 14 aktuelle
`Ready`-Single-Reviews und 14 gültige Authoring Receipts, endet aber wegen zwei
neuer High-Governance-Inkonsistenzen mit `NeedsRemediation`. `IR005` zeigt,
dass IAD601 bis IAD604 in RAW-06, Receipt und Review beantwortet, im zentralen
Decision Register jedoch weiterhin offen sind. `IR006` zeigt, dass zwölf
Lastenhefte frühere `Eligible`- oder `Blocked`-Snapshots noch als aktuellen
Lifecycle beschreiben, während Manifest und Order alle 14 Ziele als
`Completed` binden. Ergebnis-Hash ist
`11a42bd28136bf82c4dc0f36ac6e4d69b5ad8bfed6422d98d9cdb9be7c603345`.
Die Evidence stärkt `AEPS-FIND-AOC-001`, `007`, `010` und `015`, erzeugt aber
keine neue Finding-Klasse und keine Produkt-, Cross-Project- oder
Promotion-Evidence. / *The complete current Series review confirms fourteen
current Ready reviews and valid Authoring Receipts but reports two High
governance inconsistencies. Decision and human-readable lifecycle truths do
not yet agree with their canonical evidence. This strengthens existing AOC
findings without creating a new finding class or downstream authority.*


## Ergänzende IR005-/IR006-Repair-Evidence vom 2026-08-08 / Additional IR005/IR006 repair evidence from 2026-08-08

Der ausdrücklich begrenzte Repair verschiebt IAD601 bis IAD604 ohne
inhaltliche Änderung aus der offenen in die bestätigte Decision-Tabelle und
ersetzt in zwölf Intakes gegenwärtig formulierte alte Lifecycle-Aussagen durch
klar gekennzeichnete historische Authoring-Snapshots mit stabilen Verweisen
auf Manifest und Order. Zwölf erneuerte Authoring Receipts und zwölf
vollständige Ersatz-Single-Reviews bestehen auf Bash und PowerShell mit
`Ready`, null Findings und null offenen Fragen. / *The explicitly bounded
repair moves IAD601 through IAD604 unchanged into the confirmed decision table
and replaces present-tense old lifecycle wording in twelve intakes with clearly
historical authoring snapshots linked to the canonical manifest and order
document. Twelve renewed receipts and twelve complete replacement Single
reviews pass both validator surfaces as Ready with no findings or questions.*

| Review-ID | Ziel / Target | Normalisierter Zielhash / Normalised target hash |
|---|---|---|
| `722d1188-c961-47a1-b149-afef548791ed` | `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md` | `9fc31a833421915b68b85c7dd499dc5b97a81152a8cf668599bb243ef3e17503` |
| `7667b091-eb3d-42e8-b3dd-cf52cc1175d1` | `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md` | `f6d57cacc954b4899fc5bd8ddcc235570ec20470094feec506e1b8e9ea07e3e9` |
| `fc33bdf1-5857-45c1-a5d4-f89d3a4fdca9` | `requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md` | `eff68253a12129859ae75696cb4a8b8b009f7436d7b7c9df89238255aa5bf6ce` |
| `82c61d7f-9bb3-4adf-90d8-92ffeef25c76` | `requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md` | `cb255e60b49237f8cc655486b6529536b831b5b942f89f838678386bc31f930f` |
| `393d5c45-2a01-4d20-8246-232060761c8e` | `requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md` | `6a41e6ae6447ff0192a03af7940362e05e48bff48a5fd21f39e9b6e670eade20` |
| `609edc9a-96b7-4b5d-8ddf-3eb89cd1d067` | `requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md` | `31d31e82ab1857182d1201192438e5c91abfc3190ba47a2f68b9543034ab0cfd` |
| `101da312-394f-48e7-9ad0-ad3f718e7374` | `requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md` | `ce89a73e9e1d0bdeadcc166a0f4a7b3b94052037cabb8225ceb4ef2ebd345ec4` |
| `f9f84045-d19c-486b-8813-e30c195ef205` | `requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md` | `3fd7c5fbf4f419ed6131c4984a948f26d0b6b8c6ab3a5b068cdadce501c3fbad` |
| `d6cea7b3-724d-4715-b2b8-7d73ac2019c8` | `requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md` | `dde4a283ac2c761373085beea976dcd927d813e17aa2b1ad76ceab800c1d604a` |
| `14c10979-84c5-4451-957d-b34e65f111ec` | `requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md` | `ade666e411ed9a81b9736e628adb8613be0d9d732295c7e5470d90f0c64f513a` |
| `97d2c9fc-2c5e-4852-8ee5-5ccbb3cee8e0` | `requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md` | `623451757149794556a9f4efef73c13c6894244476b7fd484f0eaaa9fdba7f1a` |
| `2190e2cd-16cf-4afc-8d8e-12eba5bdd71f` | `requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md` | `c3da0eec782279678b1599e0e2365e409fbfe9e0e6f40e5f2e1b768e385f3b83` |

Das vollständige Series-Ersatzreview `86763944-9aab-4178-81b7-40dff7c1af51` ist `Ready`, umfasst
14 Ziele, einen Root und 14 azyklische Abhängigkeiten und schließt `IR005` und
`IR006` ohne Risikoakzeptanz. Ergebnis-Hash ist `c511ea75ac1fe67ee4701cd45c9d9e9876bb3c39c0a84dcd7debdac647c1238b`. Der im
Manifest weiterhin deklarierte Status `NeedsClarification` wird dadurch nicht
automatisch geändert; der formale Lifecycle-Abschluss benötigt einen neuen
ausdrücklichen Series-Update-Auftrag. / *The complete replacement Series review
is Ready and resolves IR005 and IR006 without risk acceptance. It does not
automatically change the declared manifest status; formal lifecycle completion
requires a new explicit Series update.*

Die Evidence stärkt `AEPS-FIND-AOC-001`, `007`, `010` und `015`, erzeugt
aber keine neue Finding-Klasse. Besonders bestätigt wird das Muster, dass
maschinenlesbare kanonische Zustände und menschenlesbare Intakes nur dann
dauerhaft konsistent bleiben, wenn lokale Lifecycle-Texte keine zweite
gegenwärtige Wahrheit duplizieren. Dies ist weiterhin nur AOC-interne
Requirements-Governance-Evidence: keine Cross-Project-, Runtime-, Preset- oder
Promotion-Evidence. / *This strengthens existing findings without creating a
new class. Human-readable intakes remain durable when they do not duplicate a
second current lifecycle truth. The evidence remains AOC-local and grants no
cross-project, runtime, preset, or promotion claim.*

## Ergänzende RIG017-Terminal-Evidence vom 2026-08-09 / Additional RIG017 terminal evidence from 2026-08-09

Der autorisierte Series-Abschluss zeigte eine zustandsunabhängige
Kardinalitätsannahme im lokalen Governance-Validator: `RIG017` verlangte auch
für eine vollständig abgeschlossene Serie genau ein `Eligible`-Ziel. Das
positive Terminal-Fixture bestätigt nun `Completed` mit vierzehn
`Completed`-Zielen und genau null `Eligible`; das negative Fixture weist einen
gemischten Zustand mit `Completed`-Serie und verbleibendem `Eligible`-Ziel
weiterhin fail-closed als `RIG017` zurück. Die Bash- und PowerShell-Oberflächen
melden den aktuellen AOC-Zustand als `Aligned` und geben
`eligibleCandidate: N/A` aus. / *The authorised Series completion exposed a
state-independent cardinality assumption in the local governance validator:
RIG017 required exactly one Eligible target even for a fully completed Series.
The positive terminal fixture now accepts Completed with fourteen Completed
targets and zero Eligible targets; the negative fixture keeps a mixed
Completed/Eligible state fail-closed as RIG017. Both validator surfaces report
the current AOC state as Aligned with no eligible candidate.*

Es entsteht keine neue Finding-ID. Die reparierte Terminalinvariante stärkt
`AEPS-FIND-AOC-001`, `007` und `010`: Reviewstatus, Series-Lifecycle und
Eligibility bleiben getrennte Wahrheiten; terminale Zustände benötigen
zustandsabhängige, explizit negativ getestete Invarianten. Candidate-Matrix,
Gap-Analyse und Handoff bleiben unverändert, weil dies ausschließlich
AOC-lokale Governance-Evidence ohne Cross-Project-, Preset- oder
Promotion-Aussage ist. / *No new finding is created. The repaired terminal
invariant strengthens the existing lifecycle, drift, and validation findings.
Derived candidate artifacts remain unchanged because this is AOC-local
governance evidence only.*
