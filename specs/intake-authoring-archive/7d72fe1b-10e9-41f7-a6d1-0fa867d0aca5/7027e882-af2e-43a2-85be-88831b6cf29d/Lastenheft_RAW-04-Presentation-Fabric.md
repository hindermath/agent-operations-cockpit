<!-- intake-authoring:begin -->
# RAW-04 – Presentation Fabric / Presentation Fabric

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** grundlegende UI-, JSON- und Accessibility-Begriffe; keine interne Projektgeschichte / basic UI, JSON, and accessibility terms; no internal project history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Heute können Console, JSON und interaktive Oberflächen denselben Zustand mit
abweichenden Bedeutungen, Labels oder Ausfallreaktionen darstellen. RAW-04
definiert deshalb eine gemeinsame, frameworkneutrale Presentation Fabric. Sie
projiziert belegten State auf Console, JSON, eine Referenz-TUI und spätere
Capability-Adapter, ohne den kanonischen State zu verändern. / *Console, JSON,
and interactive surfaces can currently present the same state with different
meaning, labels, or failure behaviour. RAW-04 therefore defines one
framework-neutral Presentation Fabric. It projects evidenced state to Console,
JSON, a reference TUI, and later capability adapters without changing canonical
state.*

RAW-04 besitzt Darstellungsvertrag, Layoutprofile, Fokusreihenfolge,
Lokalisierungsformat und sichtbares Degraded-Verhalten. Workspace Discovery,
State-Semantik, Orchestration, Commands, Hardwareprotokolle und Produktlogik
bleiben bei ihren jeweiligen Ownern. / *RAW-04 owns the presentation contract,
layout profiles, focus order, localization format, and visible degraded
behaviour. Workspace discovery, state semantics, orchestration, commands,
hardware protocols, and product logic remain with their respective owners.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Presentation Fabric / Darstellungsgewebe:** die gemeinsame Schicht, die
  denselben belegten Zustand auf mehrere Oberflächen projiziert. / *The shared
  layer that projects the same evidenced state to multiple surfaces.*
- **Presentation Contract / Darstellungsvertrag:** der versionierte,
  frameworkneutrale Vertrag für Status, Labels, Reason Codes, Nachrichten,
  Fokus und Capabilities. / *The versioned, framework-neutral contract for
  status, labels, reason codes, messages, focus, and capabilities.*
- **Projektion / projection:** eine Darstellung kanonischer Daten; sie darf
  deren Bedeutung oder Wert nicht verändern. / *A view of canonical data; it
  must not change the data's meaning or value.*
- **TUI:** eine interaktive textbasierte Oberfläche im Terminal. / *An
  interactive text-based terminal user interface.*
- **Referenzadapter / reference adapter:** die erste belegte technische
  Abbildung des neutralen Vertrags. Sie ist kein Teil des Vertrags selbst. /
  *The first evidenced technical mapping of the neutral contract. It is not
  part of the contract itself.*
- **Capability Routing:** die Auswahl einer geeigneten Oberfläche anhand
  belegter Terminal- und Gerätefähigkeiten. / *Selection of a suitable surface
  from evidenced terminal and device capabilities.*
- **Linear, Compact, Enhanced:** deterministische Layoutprofile für schmale,
  mittlere und breite interaktive Terminals. / *Deterministic layout profiles
  for narrow, medium, and wide interactive terminals.*
- **Message ID / Nachrichtenkennung:** eine stabile maschinenlesbare Kennung,
  die auf deutsche und englische Texte im versionierten JSON-Katalog verweist.
  / *A stable machine-readable identifier mapped to German and English text in
  the versioned JSON catalog.*
- **BCP 47:** Standard für Sprachkennungen; RAW-04 verlangt `de` und `en`. /
  *The standard for language tags; RAW-04 requires `de` and `en`.*
- **Degraded / eingeschränkt:** die Oberfläche oder ihr Input ist nur teilweise
  nutzbar; Grund und Status bleiben sichtbar. / *The surface or its input is
  only partly usable; reason and status remain visible.*
- **Fail-closed / sicher geschlossen:** fehlende oder widersprüchliche Evidence
  wird nicht als stärkerer oder verfügbarer Zustand geraten. / *Missing or
  contradictory evidence is never guessed as a stronger or available state.*
- **WCAG 2.2 AA:** die anwendbare Accessibility-Basis einschließlich
  Tastaturbedienung, Fokus, Lesereihenfolge und nicht nur farblicher Bedeutung.
  / *The applicable accessibility baseline, including keyboard use, focus,
  reading order, and meaning independent of colour.*
- **CEFR B2:** Sprachniveau B2 für verständliche, selbständige Dokumentation. /
  *B2 language level for understandable, self-contained documentation.*
- **Spec Kit:** der kontrollierte Ablauf für Spezifikation und spätere
  Entwicklungsphasen. Ein eingebetteter Prompt ist nur eine Vorlage. / *The
  controlled workflow for specification and later engineering phases. An
  embedded prompt is only a template.*

Weitere Begriffe erklärt das
[zweisprachige Glossar](../../baseline/glossary.md). Der vollständige
maschinenlesbare Vertrag steht in
[`presentation-contract.json`](../../baseline/presentation-contract.json). /
*The [bilingual glossary](../../baseline/glossary.md) explains further terms.
The complete machine-readable contract is stored in the linked JSON file.*

## Scope und Non-Goals / Scope and non-goals

Im Scope liegen der Presentation Contract, semantische Console-/JSON-Parität,
der Spectre.Console-Referenzadapter als spätere Abbildung, responsives
Capability Routing, Fokusreihenfolge, der versionierte DE/EN-Nachrichtenkatalog
und sichtbare Ausfallprojektionen. / *In scope are the Presentation Contract,
semantic Console/JSON parity, the later Spectre.Console reference-adapter
mapping, responsive capability routing, focus order, the versioned German and
English message catalog, and visible failure projections.*

Außerhalb liegen die Implementierung einer Oberfläche, Auswahl weiterer
Frameworks, State-Ermittlung, State-Mutation, Workspace- oder Node-Discovery,
Prozesssteuerung, Command Queue, Hardwareprotokolle, Telemetrie-Pipelines und
Produkt-Scaffolding. / *Out of scope are surface implementation, selection of
additional frameworks, state collection, state mutation, workspace or node
discovery, process control, command queues, hardware protocols, telemetry
pipelines, and product scaffolding.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

Quellen sind SRC-169, SRC-172 und SRC-181; zugeordnete Findings sind RF-08 und
RF-17. Der einzige bindende Serienvorgänger ist RAW-03 mit dem versionierten
`State Envelope Contract`. RAW-02 stellt nach seinem unabhängigen Abschluss
einen `Orchestration Context Contract` für Fokus und Routing bereit; dieser
fachliche Handoff erzeugt keine neue bindende Serienkante zu RAW-04. RAW-04
liefert den versionierten `Presentation Contract` an RAW-07. / *Sources are
SRC-169, SRC-172, and SRC-181; assigned findings are RF-08 and RF-17. RAW-03
and its versioned State Envelope Contract are the sole binding series
predecessor. Once independently complete, RAW-02 provides an Orchestration
Context Contract for focus and routing; this domain handoff does not create a
new binding series edge to RAW-04. RAW-04 supplies the versioned Presentation
Contract to RAW-07.*

Jeder Handoff nennt Producer, Consumer, Vertragsname, Version, Authority und
fail-closed Ausfallverhalten. Ungültiger State wird sichtbar als `Unknown` oder
`Degraded` projiziert. Ein inkompatibler Adapter wird sichtbar deaktiviert;
Console und JSON bleiben die kanonischen Referenzprojektionen. / *Every handoff
names producer, consumer, contract, version, authority, and fail-closed failure
behaviour. Invalid state is visibly projected as Unknown or Degraded. An
incompatible adapter is visibly disabled while Console and JSON remain the
canonical reference projections.*

## Querschnittsanforderungen / Cross-cutting requirements

- **Security / Sicherheit:** Nicht vertrauenswürdige Labels und Nachrichten
  MÜSSEN escaped werden. Fehlende Authority oder ungültiges Routing MUSS
  fail-closed bleiben. Secrets, Zugangsdaten und unnötige Host-Interna DÜRFEN
  nicht gerendert werden. / *Untrusted labels and messages MUST be escaped.
  Missing authority or invalid routing MUST fail closed. Secrets, credentials,
  and unnecessary host details MUST NOT be rendered.*
- **Privacy / Datenschutz:** Presentation Records DÜRFEN keine unnötigen
  Personendaten enthalten. Benutzer-, Host- und Repository-Kennungen MÜSSEN auf
  den belegten Darstellungszweck minimiert werden. Eine neue Datenkategorie
  erzwingt eine erneute Privacy-Prüfung. / *Presentation records MUST NOT
  contain unnecessary personal data. User, host, and repository identifiers
  MUST be minimised to the evidenced presentation purpose. A new data category
  triggers renewed privacy review.*
- **Public Content / Öffentliche Inhalte:** Öffentliche Ausgaben DÜRFEN nur
  reviewte Labels, Reason Codes, freigegebene Pfade und redigierte operative
  Details enthalten. / *Public output MUST contain only reviewed labels,
  reason codes, approved display paths, and redacted operational details.*
- **Accessibility / Barrierefreiheit:** Anwendbare Oberflächen MÜSSEN WCAG 2.2
  AA unterstützen: vollständige Tastaturbedienung, sichtbarer Fokus, lineare
  Lesereihenfolge, Screenreader-Text und Statusbedeutung ohne Farbe oder
  räumliche Anordnung. Eine Maus DARF nie erforderlich sein. / *Applicable
  surfaces MUST support WCAG 2.2 AA: complete keyboard operation, visible
  focus, linear reading order, screen-reader text, and status meaning without
  colour or spatial position. A mouse MUST never be required.*
- **DE/EN und Verständlichkeit:** Deutsche Texte sind zuerst maßgeblich,
  englische Texte folgen. Beide Fassungen MÜSSEN semantisch gleichwertig und auf
  CEFR-B2-Niveau selbständig verständlich sein. / *German text is authoritative
  and first; English follows. Both versions MUST be semantically equivalent and
  independently understandable at CEFR B2.*
- **Plattform und Cross-Platform:** Dieselben Inputs und Capabilities MÜSSEN
  auf macOS, Linux und Windows dieselben Presentation Records, Statuswerte,
  Message IDs und Sprachreihenfolgen ergeben. / *Identical inputs and
  capabilities MUST produce the same presentation records, statuses, message
  IDs, and language order on macOS, Linux, and Windows.*
- **Software-Lieferkette / Software supply chain:** Für dieses reine
  Requirements-Update und seine dependency-freien Fixtures ist die Prüfung
  `N/A`. Eine spätere Adapterimplementierung oder neue Abhängigkeit MUSS die
  Einstufung neu bewerten und SBOM- sowie Schwachstellennachweis binden. /
  *Supply-chain validation is N/A for this requirements-only update and its
  dependency-free fixtures. A later adapter implementation or dependency MUST
  trigger reassessment with SBOM and vulnerability evidence.*

## Anforderungen / Requirements

- **FR-001 – kanonische Parität:** Console und JSON MÜSSEN dieselben fachlichen
  Felder, Statuswerte, Reason Codes, Message IDs, Capabilities und
  Ausfallbedeutungen projizieren. Nur Layout und Dekoration dürfen abweichen. /
  *Console and JSON MUST project the same domain fields, statuses, reason codes,
  message IDs, capabilities, and failure meaning. Only layout and decoration
  may differ.*
- **FR-002 – frameworkneutrale Grenze:** Der Presentation Contract MUSS
  frameworkneutral sein. Spectre.Console ist ausschließlich der vorgesehene
  Referenz-TUI-Adapter; keine Spectre.Console-Typen oder andere Frameworktypen
  DÜRFEN die Vertragsgrenze überschreiten. / *The Presentation Contract MUST be
  framework neutral. Spectre.Console is only the intended reference TUI
  adapter; no Spectre.Console or other framework types may cross the contract
  boundary.*
- **FR-003 – Layoutprofile:** Interaktive Terminals unter 40 Spalten MÜSSEN
  `Linear`, Terminals von 40 bis 99 Spalten `Compact` und Terminals ab 100
  Spalten `Enhanced` wählen. `TERM=dumb`, umgeleitete Ein-/Ausgabe, fehlende
  Terminalfähigkeit oder ein nicht verfügbarer TUI-Adapter MÜSSEN unabhängig
  von der Breite `Linear` wählen. / *Interactive terminals below 40 columns
  MUST select Linear, terminals from 40 through 99 columns Compact, and
  terminals from 100 columns Enhanced. TERM=dumb, redirected input or output,
  missing terminal capability, or an unavailable TUI adapter MUST select
  Linear regardless of width.*
- **FR-004 – semantische Breitenunabhängigkeit:** Profilwechsel DÜRFEN Labels,
  Statusbedeutung, Reason Codes, Fokusreihenfolge, verfügbare Aktionen oder
  kanonische Daten nicht entfernen, verkürzen oder umdeuten. Referenzbreiten
  sind 39, 79 und 120 Spalten. / *Profile changes MUST NOT remove, truncate, or
  reinterpret labels, status meaning, reason codes, focus order, available
  actions, or canonical data. Reference widths are 39, 79, and 120 columns.*
- **FR-005 – Lokalisierung:** Ein versionierter, frameworkneutraler JSON-Katalog
  mit `schemaVersion: 1` MUSS stabile `messageId`-Werte sowie vollständige
  BCP-47-Sprachen `de` und `en` enthalten. Die Anzeige ist Deutsch zuerst,
  Englisch danach. / *A versioned, framework-neutral JSON catalog with schema
  version 1 MUST contain stable message IDs and complete BCP-47 languages de
  and en. Display order is German first and English second.*
- **FR-006 – Fallback:** Eine nicht unterstützte Sprache MUSS auf `de`
  zurückfallen. Fehlt `de` oder `en`, MUSS die Validierung fehlschlagen. Eine
  unbekannte Message ID MUSS die stabile ID sowie einen sicheren generischen
  DE/EN-Text zeigen; sie darf nicht leer bleiben. / *An unsupported language
  MUST fall back to de. Missing de or en MUST fail validation. An unknown
  message ID MUST show the stable ID plus safe generic German and English text;
  it must never be blank.*
- **FR-007 – sichtbarer Zustand:** `Known`, `Unknown`, `Stale`, `Unavailable`
  und `Degraded` MÜSSEN mit sichtbarem Textlabel und maschinenlesbaren Reason
  Codes erscheinen. Status darf nicht ausschließlich über Farbe, Position,
  Animation oder Klang vermittelt werden. / *Known, Unknown, Stale,
  Unavailable, and Degraded MUST appear with visible text labels and
  machine-readable reason codes. Status must not be conveyed only through
  colour, position, animation, or sound.*
- **FR-008 – Fokus und Bedienung:** Fokuspositionen MÜSSEN positiv, eindeutig
  und linear sein. Alle Funktionen MÜSSEN ohne Maus erreichbar sein; Surface-
  oder Fokusausfall MUSS sichtbar degradieren. / *Focus positions MUST be
  positive, unique, and linear. Every function MUST be reachable without a
  mouse; surface or focus failure MUST degrade visibly.*
- **FR-009 – State-Grenze:** Rendering und Capability Routing DÜRFEN weder
  kanonischen State verändern noch Commands ausführen. / *Rendering and
  capability routing MUST NOT mutate canonical state or execute commands.*
- **NFR-001 – deterministische Evidence:** Vertrag und Fixtures MÜSSEN mit
  denselben Inputs auf Bash und PowerShell reproduzierbar dieselben Ergebnisse
  und stabilen Fehlercodes liefern. / *The contract and fixtures MUST produce
  the same results and stable error codes from the same inputs through Bash and
  PowerShell.*
- **NFR-002 – zugängliche Sprache:** Das Lastenheft, alle Labels und generischen
  Fehler MÜSSEN DE-first, EN-second, semantisch gleichwertig und auf CEFR B2
  verständlich sein. / *The intake, all labels, and generic errors MUST be
  German first, English second, semantically equivalent, and understandable at
  CEFR B2.*
- **NFR-003 – Re-Evaluation:** Neue Plattformen, Frameworkadapter,
  Datenkategorien, Eingabemethoden, Implementierungsabhängigkeiten oder
  grafische Oberflächen MÜSSEN Security, Privacy, Accessibility,
  Cross-Platform und Supply Chain neu bewerten. / *New platforms, framework
  adapters, data categories, input methods, implementation dependencies, or
  graphical surfaces MUST trigger renewed security, privacy, accessibility,
  cross-platform, and supply-chain assessment.*

## Bestätigte Decisions, Abhängigkeit und Mode / Confirmed decisions, dependency, and mode

`DEC-T04` ist ohne offenen Rest durch drei bestätigte Einzelentscheidungen
supersediert: / *DEC-T04 is superseded without an open remainder by three
confirmed individual decisions:*

1. **IAD401 (beantwortet IRQ401) – Frameworkgrenze:** Der Presentation Contract
   bleibt frameworkneutral; Console und JSON sind kanonisch. Spectre.Console
   ist ausschließlich der Referenz-TUI-Adapter. Keine Frameworktypen
   überschreiten die Vertragsgrenze. / *The Presentation Contract remains
   framework neutral, with Console and JSON canonical. Spectre.Console is only
   the reference TUI adapter. No framework types cross the contract boundary.*
2. **IAD402 (beantwortet IRQ402) – Responsiveness:** Die Profile sind `Linear`
   unter 40, `Compact` von 40 bis 99 und `Enhanced` ab 100 Spalten. Fehlende
   Interaktivität oder Capability erzwingt `Linear`. Evidence verwendet 39, 79
   und 120 Spalten auf macOS, Linux und Windows; Status darf nie nur farblich,
   räumlich oder durch Kürzung vermittelt werden. / *Profiles are Linear below
   40, Compact from 40 through 99, and Enhanced from 100 columns. Missing
   interactivity or capability forces Linear. Evidence uses widths 39, 79, and
   120 on macOS, Linux, and Windows; status must never depend only on colour,
   position, or truncation.*
3. **IAD403 (beantwortet IRQ403) – Lokalisierung:** Ein versionierter,
   frameworkneutraler JSON-Katalog mit Schema 1 und stabiler Message ID fordert
   `de` und `en`. Anzeige ist DE-first und EN-second. Nicht unterstützte
   Sprachen fallen auf `de` zurück; fehlende Pflichtübersetzungen sind ein
   Validierungsfehler; unbekannte IDs zeigen eine sichere zweisprachige
   Generik plus ID. / *A versioned, framework-neutral JSON catalog with schema
   1 and stable message IDs requires de and en. Display is German first and
   English second. Unsupported languages fall back to de; missing required
   translations are validation errors; unknown IDs show a safe bilingual
   generic message plus the ID.*

RAW-01, RAW-03 und RAW-02 sind im aktuellen Series-Lifecycle `Completed`.
RAW-04 ist der einzige deklarierte `Eligible`-Kandidat; sein einziger bindender
Vorgänger bleibt RAW-03. RAW-05 bleibt `Pending` und auf read-only Research
begrenzt. Diese Feststellungen ändern weder Reihenfolge noch Abhängigkeiten. /
*RAW-01, RAW-03, and RAW-02 are Completed in the current series lifecycle.
RAW-04 is the sole declared Eligible candidate and RAW-03 remains its only
binding predecessor. RAW-05 remains Pending and limited to read-only research.
These facts change neither order nor dependencies.*

`serial-autonomous` beschreibt nur einen möglichen späteren, einzeln
autorisierten Lauf. `ReadyForReview`, `Eligible`, ein späteres `Ready`, der im
Receipt gespeicherte Delivery-Modus und die eingebetteten Prompts sind getrennte
Informationen. Die historische Delivery Authority `MergeAndSync` ist nur eine
gespeicherte Obergrenze und keine aktuelle Start-, Remote-, Merge- oder
Bypass-Autorität. / *Serial-autonomous only describes a possible later,
individually authorised run. ReadyForReview, Eligible, a later Ready result,
the stored delivery mode, and embedded prompts are separate facts. Historical
MergeAndSync delivery authority is only a stored ceiling and grants no current
start, remote, merge, or bypass authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Vorgesehene Child-Intakes sind Console/JSON Baseline, TUI A11Y, Focus Model und
Surface Capability Contract. Sie werden durch dieses Requirements-Update nicht
erstellt oder gestartet. / *Planned child intakes are Console/JSON Baseline,
TUI A11Y, Focus Model, and Surface Capability Contract. This requirements
update neither creates nor starts them.*

- **AC-001:** Die positive Fixture beweist `Linear` bei 39, `Compact` bei 79,
  `Enhanced` bei 120 und erzwungenes `Linear` ohne interaktives Terminal. /
  *The positive fixture proves Linear at 39, Compact at 79, Enhanced at 120,
  and forced Linear without an interactive terminal.*
- **AC-002:** Dieselbe positive Fixture beweist semantisch identische Console-
  und JSON-Projektionen für `Known`, `Unknown`, `Stale` und `Degraded`. /
  *The same positive fixture proves semantically identical Console and JSON
  projections for Known, Unknown, Stale, and Degraded.*
- **AC-003:** Fehlendes sichtbares Label wird ausschließlich mit `PR007` als
  erwartete Ablehnung akzeptiert. / *A missing visible label passes only as the
  expected PR007 rejection.*
- **AC-004:** Fehlende deutsche oder englische Übersetzung wird ausschließlich
  mit `PR008` als erwartete Ablehnung akzeptiert. / *A missing German or English
  translation passes only as the expected PR008 rejection.*
- **AC-005:** Abweichende Console-/JSON-Semantik wird ausschließlich mit
  `PR009` als erwartete Ablehnung akzeptiert. / *Divergent Console and JSON
  semantics pass only as the expected PR009 rejection.*
- **AC-006:** Doppelte, nichtpositive oder nichtlineare Fokuspositionen werden
  ausschließlich mit `PR010` als erwartete Ablehnung akzeptiert. / *Duplicate,
  non-positive, or non-linear focus positions pass only as the expected PR010
  rejection.*
- **AC-007:** Der Vertrag belegt Security-, Privacy-, Public-Content-,
  Accessibility-, DE/EN-, Plattform- und Supply-Chain-Grenzen samt
  Re-Evaluation-Triggern. / *The contract evidences security, privacy, public
  content, accessibility, German/English, platform, and supply-chain boundaries
  with re-evaluation triggers.*
- **AC-008:** Bash und PowerShell liefern für jede Fixture Exitcode `0` und den
  exakt benannten Validierungs- oder erwarteten Ablehnungsstatus. / *Bash and
  PowerShell return exit code 0 and the named validation or expected rejection
  status for every fixture.*

Der kanonische Requirements-Vertrag und die Fixtures liegen unter
`requirements/baseline/presentation-contract.json` und
`specs/intake-review-fixtures/raw-04/`. Die folgenden Befehle MÜSSEN mit
Exitcode `0` enden: / *The canonical requirements contract and fixtures are
stored at the named paths. The following commands MUST exit with code 0:*

```text
bash specs/intake-review-fixtures/raw-04/validate-presentation-contract.sh --contract requirements/baseline/presentation-contract.json --fixture specs/intake-review-fixtures/raw-04/valid-presentation-cases.json
# RAW04-VALID-PRESENTATION-CASES: Valid
bash specs/intake-review-fixtures/raw-04/validate-presentation-contract.sh --contract requirements/baseline/presentation-contract.json --fixture specs/intake-review-fixtures/raw-04/negative-missing-label.json
# RAW04-NEGATIVE-MISSING-LABEL: Rejected (PR007: ...)
bash specs/intake-review-fixtures/raw-04/validate-presentation-contract.sh --contract requirements/baseline/presentation-contract.json --fixture specs/intake-review-fixtures/raw-04/negative-missing-translation.json
# RAW04-NEGATIVE-MISSING-TRANSLATION: Rejected (PR008: ...)
bash specs/intake-review-fixtures/raw-04/validate-presentation-contract.sh --contract requirements/baseline/presentation-contract.json --fixture specs/intake-review-fixtures/raw-04/negative-projection-mismatch.json
# RAW04-NEGATIVE-PROJECTION-MISMATCH: Rejected (PR009: ...)
bash specs/intake-review-fixtures/raw-04/validate-presentation-contract.sh --contract requirements/baseline/presentation-contract.json --fixture specs/intake-review-fixtures/raw-04/negative-focus-order.json
# RAW04-NEGATIVE-FOCUS-ORDER: Rejected (PR010: ...)
pwsh -NoProfile -File specs/intake-review-fixtures/raw-04/validate-presentation-contract.ps1 -Contract requirements/baseline/presentation-contract.json -Fixture specs/intake-review-fixtures/raw-04/valid-presentation-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-04/validate-presentation-contract.ps1 -Contract requirements/baseline/presentation-contract.json -Fixture specs/intake-review-fixtures/raw-04/negative-missing-label.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-04/validate-presentation-contract.ps1 -Contract requirements/baseline/presentation-contract.json -Fixture specs/intake-review-fixtures/raw-04/negative-missing-translation.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-04/validate-presentation-contract.ps1 -Contract requirements/baseline/presentation-contract.json -Fixture specs/intake-review-fixtures/raw-04/negative-projection-mismatch.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-04/validate-presentation-contract.ps1 -Contract requirements/baseline/presentation-contract.json -Fixture specs/intake-review-fixtures/raw-04/negative-focus-order.json
```

## Risiken, Revision und Nichtautorität / Risks, revision, and non-authority

Risiken sind unbeabsichtigte Frameworkkopplung, semantische Drift zwischen
Projektionen, abgeschnittene Statusbedeutung, Fokusverlust, unvollständige
Übersetzungen und das Verwechseln eines gespeicherten Delivery-Modus mit
aktueller Autorität. Die Vertrags- und Fixture-Evidence begrenzt diese Risiken;
eine Implementierung benötigt trotzdem ein neues Review ihrer konkreten
Abhängigkeiten und Oberflächen. / *Risks include accidental framework coupling,
semantic drift between projections, truncated status meaning, lost focus,
incomplete translations, and confusing a stored delivery mode with current
authority. Contract and fixture evidence bound these risks; an implementation
still requires renewed review of its concrete dependencies and surfaces.*

Revision ist erforderlich bei Änderungen an State-, Orchestration-, A11Y-,
Lokalisierungs-, Capability- oder Plattformverträgen sowie bei neuen
Frameworks, Eingabemethoden, Datenkategorien oder Produktoberflächen. RAW-04
erteilt keine Command-, State-, Hardware-, Specify-, Implementierungs-,
Remote-, Merge-, Bypass-, Preset- oder Level-0-Autorität. / *Revision is
required when state, orchestration, accessibility, localization, capability, or
platform contracts change, or when new frameworks, input methods, data
categories, or product surfaces appear. RAW-04 grants no command, state,
hardware, Specify, implementation, remote, merge, bypass, preset, or Level-0
authority.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

Die folgenden Befehle sind ausschließlich kopierbare Vorlagen. Vor jeder
Ausführung MÜSSEN Zielhash, Authoring Receipt, aktuelles `Ready`-Single-Review,
globale Review-Sperre und eine neue ausdrückliche menschliche Start- und
Delivery Authority fail-closed geprüft werden. / *The following commands are
copy-ready templates only. Before execution, the target hash, Authoring
Receipt, current Ready Single review, global review gate, and fresh explicit
human start and delivery authority MUST be checked fail closed.*

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md --delivery-mode MergeAndSync --require-current-review
```

<!-- intake-authoring:end -->
