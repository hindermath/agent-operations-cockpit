<!-- intake-authoring:begin -->
# RAW-03 – Zustandswahrheit / State Truthfulness

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** grundlegende Zustandsmodelle und JSON-Strukturen; keine Spec-Kit- oder interne Projektgeschichte / basic state models and JSON structures; no Spec Kit or internal project history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Heute können verschiedene Oberflächen denselben Zustand unterschiedlich als
aktuell, sicher oder verfügbar darstellen. RAW-03 definiert deshalb eine
gemeinsame, belegbare Zustandswahrheit zu Wert oder Abwesenheit, Quelle,
Zeitbezug, Aktualität, Authority und Unsicherheit. Die Reihe besitzt diese
Semantik, aber nicht Workspace- oder Node-Discovery, Darstellung,
Orchestration oder Commands. / *Different surfaces can currently describe the
same state differently as current, trustworthy, or available. RAW-03 defines
one provable state truth for value or absence, source, time, freshness,
authority, and uncertainty. It owns these semantics, but not workspace or node
discovery, presentation, orchestration, or commands.*

## Begriffe für den Einstieg / Terms for first-time readers

- **State Envelope / Zustandsumschlag:** ein versionierter Datensatz, der den
  Zustand und seine Herkunft, Zeit, Freshness, Authority, Confidence und
  Reason Codes gemeinsam überträgt. / *A versioned record carrying state plus
  its provenance, time, freshness, authority, confidence, and reason codes.*
- **State-Status / state status:** `Known`, `Unknown`, `Stale`, `Unavailable`
  oder `Degraded` beschreibt die fachliche Nutzbarkeit des Zustands. / *Known,
  Unknown, Stale, Unavailable, or Degraded describes the domain usability of
  the state.*
- **Execution Node / Ausführungsknoten:** der autorisierte Host, die Sandbox,
  der Container oder der Remote-Knoten, der eine Beobachtung erzeugt. Seine
  Erkennung und sein Vertrag bleiben bei RAW-05. / *The authorised host,
  sandbox, container, or remote node producing an observation. RAW-05 retains
  its discovery and contract.*
- **Authority / Berechtigung:** der belegte Umfang, in dem eine Quelle eine
  Zustandsaussage machen darf. / *The evidenced scope in which a source may
  make a state claim.*
- **Freshness / Aktualitätsklasse:** eine deterministisch berechnete
  Altersklasse `Fresh`, `Aging`, `Stale`, `Expired` oder `Unknown`. Sie ist
  eine andere Achse als der fachliche State-Status. / *A deterministically
  calculated age class. It is separate from the domain state status.*
- **Confidence / Vertrauensklasse:** `High`, `Medium`, `Low` oder `Unknown`,
  abgeleitet aus Freshness, Source-, Authority- und Konflikt-Evidence. Sie ist
  keine subjektive Prozentzahl. / *A deterministic trust class derived from
  freshness, source, authority, and conflict evidence; never a subjective
  percentage.*
- **Reason Code / Begründungscode:** eine stabile maschinenlesbare Kennung,
  die erklärt, warum Status, Freshness und Confidence gelten. / *A stable
  machine-readable identifier explaining the derived status, freshness, and
  confidence.*
- **`observed-at`:** UTC-Zeitstempel nach RFC 3339 von der Uhr des
  beobachtenden Execution Nodes. / *An RFC 3339 UTC timestamp from the clock of
  the observing execution node.*
- **`freshness-as-of`:** UTC-Zeitstempel nach RFC 3339 von der Uhr des
  bewertenden AOC-Prozesses. / *An RFC 3339 UTC timestamp from the clock of the
  evaluating AOC process.*
- **Monotone Uhr / monotonic clock:** eine Laufzeituhr für verstrichene Dauer,
  die bei einer Änderung der Kalenderzeit nicht zurückspringt. / *A runtime
  clock for elapsed duration that does not move backwards when wall time
  changes.*
- **Fail-closed / sicher geschlossen:** fehlende oder widersprüchliche
  Evidence wird nicht als `Known` geraten. / *Missing or contradictory evidence
  is never guessed as Known.*
- **Projection Parity / Projektionsparität:** JSON und Text übertragen dieselben
  Felder und Bedeutungen; nur das Layout darf abweichen. / *JSON and text carry
  the same fields and meanings; only layout may differ.*
- **Last-Writer-Wins / letzter Wert gewinnt:** ein Konfliktverfahren, das
  frühere Quellen durch den zuletzt eingegangenen Wert verdeckt; RAW-03
  verbietet dieses stille Verhalten. / *A conflict policy that hides earlier
  sources behind the latest value; RAW-03 forbids this silent behaviour.*
- **Spec Kit:** der kontrollierte Ablauf für Spezifikation und spätere
  Entwicklungsphasen. Ein eingebetteter Prompt ist eine Vorlage und keine
  Startfreigabe. / *The controlled workflow for specification and later
  engineering phases. An embedded prompt is a template, not start authority.*
- **CEFR B2:** Sprachniveau B2 des Gemeinsamen Europäischen Referenzrahmens
  für verständliche Dokumentation. / *Language level B2 of the Common European
  Framework of Reference for understandable documentation.*

Weitere Begriffe erklärt das
[zweisprachige Glossar](../../baseline/glossary.md). Der vollständige
maschinenlesbare Vertrag steht in
[`state-truthfulness-contract.json`](../../baseline/state-truthfulness-contract.json).
/ *The [bilingual glossary](../../baseline/glossary.md) explains further terms.
The complete machine-readable contract is stored in the linked JSON file.*

## Scope und Non-Goals / Scope and non-goals

Im Scope liegen der versionierte State Envelope Contract, Freshness- und
Confidence-Ableitung, Authority-Projektion, Reason Codes sowie semantische
Parität zwischen JSON und Text. Außerhalb liegen Discovery, Node-Erkennung,
UI-/TUI-Layout, Orchestration, Prozessstart, Commands und Produkt-Side-Effects.
/ *In scope are the versioned State Envelope Contract, freshness and confidence
derivation, authority projection, reason codes, and semantic parity between
JSON and text. Discovery, node detection, UI or TUI layout, orchestration,
process launch, commands, and product side effects are out of scope.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

Quellen sind SRC-172, SRC-180 und SRC-181; zugeordnete Findings sind RF-06 und
RF-10. Einziger bindender Input ist der `Workspace Snapshot Contract` aus
RAW-01. RAW-03 erzeugt den versionierten `State Envelope Contract` für RAW-02
und RAW-04. Node Evidence ist kein RAW-03-Input; RAW-05 bleibt Owner der
Node-Verträge und folgt ohne neue Abhängigkeitskante. / *Sources are SRC-172,
SRC-180, and SRC-181; assigned findings are RF-06 and RF-10. The sole binding
input is the RAW-01 Workspace Snapshot Contract. RAW-03 emits the versioned
State Envelope Contract for RAW-02 and RAW-04. Node evidence is not a RAW-03
input; RAW-05 retains node-contract ownership and no dependency is added.*

## Querschnittsanforderungen / Cross-cutting requirements

- **Security / Sicherheit:** Fehlende oder widersprüchliche Authority MUSS
  fail-closed behandelt werden. Value, Reason Codes und Quellenmetadaten DÜRFEN
  keine Secrets, Zugangsdaten oder unnötigen Host-Interna offenlegen. / *Missing
  or conflicting authority MUST fail closed. Values, reason codes, and source
  metadata MUST NOT expose secrets, credentials, or unnecessary host details.*
- **Privacy / Datenschutz:** State Envelopes DÜRFEN keine unnötigen
  Personendaten enthalten. Benutzer-, Host- und Repository-Kennungen werden auf
  den belegten Zustandszweck minimiert; neue Datenkategorien erzwingen eine
  erneute Privacy-Prüfung. / *State envelopes MUST NOT contain unnecessary
  personal data. User, host, and repository identifiers are minimised to the
  evidenced state purpose; a new data category triggers renewed privacy
  review.*
- **Accessibility / Barrierefreiheit:** Dieses lernendenorientierte
  Lastenheft und alle textuellen Zustandsprojektionen MÜSSEN die Web Content
  Accessibility Guidelines (WCAG) 2.2 Level AA, Screenreader, verständliche
  DE/EN-Paare und eine nicht nur farbliche Statusvermittlung unterstützen.
  UI-/TUI-Verhalten bleibt bei RAW-04. / *This learner-facing intake and all
  textual state projections MUST support WCAG 2.2 Level AA, screen readers,
  understandable German/English pairs, and status meaning independent of
  colour. UI and TUI behaviour remains with RAW-04.*
- **Plattform und Cross-Platform:** Dieselben Inputs und Policy-Profile MÜSSEN
  auf macOS, Linux und Windows dieselben Status-, Freshness-, Confidence- und
  Reason-Code-Ergebnisse liefern. Locale oder lokale Zeitzone dürfen das
  Ergebnis nicht verändern. / *Identical inputs and policy profiles MUST
  produce identical status, freshness, confidence, and reason codes on macOS,
  Linux, and Windows. Locale or local time zone must not change the result.*
- **Software-Lieferkette / Software supply chain:** Für dieses reine
  Requirements-Update und seine dependency-freien Review-Fixtures ist die
  Lieferkettenprüfung `N/A`. Eine spätere Implementierung oder neue
  Abhängigkeit MUSS die Einstufung neu bewerten und Software-Stückliste (SBOM)
  sowie Schwachstellennachweis binden. / *Supply-chain validation is N/A for
  this requirements-only update and its dependency-free review fixtures. A
  later implementation or dependency MUST trigger reassessment with a software
  bill of materials and vulnerability evidence.*

## Anforderungen / Requirements

- **FR-001:** Jeder `StateEnvelope` MUSS Schemaversion, State-ID, Wert oder
  ausdrücklich bestätigte Abwesenheit, alle Quellen, `observed-at`,
  `freshness-as-of`, Freshness, Status, Authority, Confidence und mindestens
  einen Reason Code enthalten. / *Every StateEnvelope MUST contain the schema
  version, state ID, value or explicitly confirmed absence, every source,
  observed-at, freshness-as-of, freshness, status, authority, confidence, and
  at least one reason code.*
- **FR-002:** `Unknown` DARF weder als leerer Normalwert noch als `Known`
  projiziert werden. / *Unknown MUST NOT be projected as an empty normal value
  or as Known.*
- **FR-003:** Konfliktquellen MÜSSEN vollständig sichtbar bleiben; stilles
  Last-Writer-Wins ist verboten. / *Conflicting sources MUST remain fully
  visible; silent last-writer-wins is forbidden.*
- **FR-004:** JSON, Text und spätere Präsentationsoberflächen MÜSSEN dieselben
  fachlichen Felder und Bedeutungen projizieren. / *JSON, text, and later
  presentation surfaces MUST project the same domain fields and meanings.*
- **FR-005:** Freshness MUSS mit einem versionierten Profil je Source und
  Capability berechnet werden. Das Profil enthält ein positives
  Basisschwellenintervall `T` und eine nichtnegative Clock-Skew-Grenze; freie
  unbelegte Runtime-Overrides sind verboten. / *Freshness MUST use a versioned
  profile per source and capability. The profile contains a positive base
  threshold T and a non-negative clock-skew allowance; unevidenced runtime
  overrides are forbidden.*
- **FR-006:** Die relativen Altersklassen lauten: `Fresh` für Alter bis
  einschließlich `0,5T`, `Aging` für mehr als `0,5T` bis einschließlich `T`,
  `Stale` für mehr als `T` bis einschließlich `2T`, `Expired` für mehr als
  `2T` und `Unknown`, wenn kein gültiges Alter berechnet werden kann. / *The
  relative age classes are Fresh through 0.5T inclusive, Aging above 0.5T
  through T inclusive, Stale above T through 2T inclusive, Expired above 2T,
  and Unknown when no valid age can be calculated.*
- **FR-007:** Confidence MUSS deterministisch `High`, `Medium`, `Low` oder
  `Unknown` sein und einen maschinenlesbaren Reason Code besitzen. Numerische
  oder prozentuale Confidence ist verboten. / *Confidence MUST be
  deterministically High, Medium, Low, or Unknown with a machine-readable
  reason code. Numeric or percentage confidence is forbidden.*
- **FR-008:** Die Ableitung MUSS fail-closed erfolgen: fehlende oder ungültige
  Zeit-, Source-, Authority- oder Wert-/Abwesenheits-Evidence ergibt `Unknown`;
  eine nicht erreichbare Quelle oder `Expired` ergibt `Unavailable`;
  verwertbare Konflikte ergeben `Degraded`; `Stale` ergibt State-Status
  `Stale`; nur `Fresh` oder `Aging` mit gültiger Source und Authority ohne
  Konflikt darf `Known` ergeben. / *Derivation MUST fail closed: missing or
  invalid time, source, authority, or value-or-absence evidence yields Unknown;
  an unavailable source or Expired yields Unavailable; usable conflicts yield
  Degraded; Stale yields state status Stale; only Fresh or Aging with valid
  source and authority and no conflict may yield Known.*
- **NFR-001:** Zeit-, Locale- und Zeitzonenbehandlung MUSS deterministisch
  sein. In einem laufenden Prozess wird verstrichene Dauer monoton gemessen;
  serialisierte oder neu geladene Evidence verwendet die Differenz aus
  `freshness-as-of` und `observed-at`. / *Time, locale, and time-zone handling
  MUST be deterministic. Elapsed duration in one running process uses a
  monotonic clock; serialised or reloaded evidence uses freshness-as-of minus
  observed-at.*
- **NFR-002:** DE/EN-Parität, CEFR B2, WCAG 2.2 AA, Security, Privacy,
  Plattformparität und Lieferketten-Anwendbarkeit MÜSSEN nach den oben
  genannten Grenzen prüfbar bleiben. / *German/English parity, CEFR B2, WCAG
  2.2 AA, security, privacy, platform parity, and supply-chain applicability
  MUST remain testable within the stated boundaries.*

## Bestätigte Decisions, Abhängigkeit und Mode / Confirmed decisions, dependency, and mode

`DEC-T03` ist ohne offenen Rest durch drei bestätigte Einzelentscheidungen
supersediert: / *DEC-T03 is superseded without an open remainder by three
confirmed individual decisions:*

1. **IAD301 (beantwortet IRQ301) – dualer Zeitvertrag:** `observed-at` stammt als UTC/RFC-3339-Wert
   von der Uhr des beobachtenden Execution Nodes; `freshness-as-of` stammt als
   UTC/RFC-3339-Wert von der Uhr des bewertenden AOC-Prozesses. Innerhalb eines
   laufenden Prozesses schützt eine monotone Uhr die Altersmessung vor
   Wall-Clock-Sprüngen. Zukunftszeit jenseits der profilgebundenen
   Clock-Skew-Grenze ergibt `Unknown`; tolerierter Skew begrenzt Confidence auf
   `Medium`. / *Observed-at comes from the observing execution node and
   freshness-as-of from the evaluating AOC process, both as UTC RFC 3339.
   Monotonic elapsed time protects in-process evaluation from wall-clock jumps.
   Future time beyond the profile allowance yields Unknown; tolerated skew
   caps confidence at Medium.*
2. **IAD302 (beantwortet IRQ302) – versionierte Freshness-Profile:** Jedes Source-/Capability-Paar
   erhält ein reviewtes Profil mit `T` und Clock-Skew-Grenze. Die Klassen sind
   `Fresh`, `Aging`, `Stale`, `Expired` und `Unknown` nach dem relativen Modell
   `0,5T / T / 2T`. / *Each source/capability pair receives a reviewed profile
   containing T and a clock-skew allowance. Freshness uses Fresh, Aging, Stale,
   Expired, and Unknown under the relative 0.5T/T/2T model.*
3. **IAD303 (beantwortet IRQ303) – deterministische Confidence-Klassen:** Confidence ist
   `High`, `Medium`, `Low` oder `Unknown`, wird ausschließlich aus belegter
   Freshness, Source, Authority und Konfliktlage abgeleitet und trägt eine
   maschinenlesbare Begründung. Prozentwerte sind ausgeschlossen. Diese
   präzisierte bestätigte Entscheidung ersetzt die frühere Gesprächsoption
   „kein Confidence-Feld“. / *Confidence is High, Medium, Low, or Unknown,
   derived only from evidenced freshness, source, authority, and conflicts,
   with a machine-readable reason. Percentages are excluded. This refined
   confirmed decision supersedes the earlier conversational no-field option.*

Beim damaligen Authoring galt als historischer Snapshot: RAW-01 war
`Completed` und RAW-03 der einzige deklarierte `Eligible`-Kandidat. Dieser
Snapshot ist keine aktuelle Lifecycle-Quelle. Der aktuelle kanonische Zustand
steht ausschließlich im
[`manifest.json`](../../../specs/intake-series/aoc-phase-2/manifest.json) und
in der [`order.md`](../series/order.md). RAW-01 bleibt der bindende Vorgänger;
RAW-02 und RAW-04 benötigen den gültigen RAW-03-Handoff. `serial-autonomous`
bezeichnet nur einen späteren, einzeln ausgeführten und separat autorisierten
Lauf; parallele State-Schema-Änderungen sind unzulässig. / *At authoring time,
the historical snapshot recorded RAW-01 as Completed and RAW-03 as the sole
Eligible candidate. This snapshot is not a current lifecycle source. Only the
linked manifest and order document define the current canonical state. RAW-01
remains the binding predecessor; RAW-02 and RAW-04 require the valid RAW-03
handoff. Serial-autonomous only describes a later, separately authorised run;
parallel State-schema changes are prohibited.*

`IAD301` bis `IAD303` sind bestätigt; `DEC-T03` besitzt keine offene
Teilfrage. Authoring-, Review- und Lifecycle-Zustand sowie der gespeicherte
Delivery-Modus sind getrennte Informationen und erteilen keine Start- oder
Delivery Authority. / *IAD301 through IAD303 are confirmed and DEC-T03 has no
open sub-question. Authoring, review, lifecycle, and stored delivery state are
separate facts and grant no start or delivery authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Vorgesehene Child-Intakes sind State Envelope, Freshness Policy, Authority
Projection und Projection Parity. / *Planned child intakes are State Envelope,
Freshness Policy, Authority Projection, and Projection Parity.*

- **AC-001:** Positive Fixtures belegen die Grenzwerte `0,5T`, `T` und `2T`
  sowie die erwarteten Freshness-, State-, Confidence- und Reason-Code-Werte. /
  *Positive fixtures prove the 0.5T, T, and 2T boundaries and the expected
  freshness, state, confidence, and reason-code values.*
- **AC-002:** Zukunftszeit außerhalb der Skew-Grenze, fehlende Source,
  nicht erreichbare Source und widersprüchliche Authority ergeben
  reproduzierbar fail-closed Zustände und niemals unbelegtes `Known`. /
  *Future time outside the skew allowance, missing or unavailable sources, and
  conflicting authority reproducibly fail closed and never yield unsupported
  Known.*
- **AC-003:** Tolerierter Clock Skew ergibt `Fresh`, höchstens `Medium` und den
  Reason Code `CLOCK_SKEW_TOLERATED`. / *Tolerated clock skew yields Fresh,
  confidence no higher than Medium, and CLOCK_SKEW_TOLERATED.*
- **AC-004:** JSON-/Text-Parität ist feldweise prüfbar; die negative Fixture
  wird ausschließlich mit `ST007` als erwarteter Abweichung akzeptiert. /
  *JSON/text parity is field-testable; the negative fixture passes only by
  producing expected mismatch ST007.*
- **AC-005:** Der Vertrag lehnt numerische Confidence ab, fordert mindestens
  einen Reason Code und erhält Konfliktquellen ohne stilles
  Last-Writer-Wins. / *The contract rejects numeric confidence, requires at
  least one reason code, and preserves conflicting sources without silent
  last-writer-wins.*
- **AC-006:** Review-Evidence weist Secret- und Datenminimierungsgrenzen,
  WCAG-konforme Textstatus, identische logische Ergebnisse auf macOS, Linux und
  Windows sowie die aktuelle Lieferketten-Einstufung `N/A` mit
  Re-Evaluation-Trigger nach. / *Review evidence covers secret and data
  minimisation boundaries, WCAG-conformant text status, identical logical
  results on macOS, Linux, and Windows, and the current supply-chain N/A
  decision with a re-evaluation trigger.*

Der kanonische Requirements-Vertrag und die Fixtures liegen unter
`requirements/baseline/state-truthfulness-contract.json` und
`specs/intake-review-fixtures/raw-03/`. Alle folgenden Befehle MÜSSEN mit
Exitcode `0` und den benannten Ergebnissen enden: / *The canonical requirements
contract and fixtures are stored at the named paths. Every following command
MUST exit with code 0 and the stated outcome:*

```text
bash specs/intake-review-fixtures/raw-03/validate-state-truthfulness.sh --contract requirements/baseline/state-truthfulness-contract.json --fixture specs/intake-review-fixtures/raw-03/valid-state-cases.json
# RAW03-VALID-STATE-CASES: Valid
bash specs/intake-review-fixtures/raw-03/validate-state-truthfulness.sh --contract requirements/baseline/state-truthfulness-contract.json --fixture specs/intake-review-fixtures/raw-03/negative-state-cases.json
# RAW03-NEGATIVE-STATE-CASES: Valid
bash specs/intake-review-fixtures/raw-03/validate-state-truthfulness.sh --contract requirements/baseline/state-truthfulness-contract.json --fixture specs/intake-review-fixtures/raw-03/projection-parity.json
# RAW03-PROJECTION-PARITY: Valid
bash specs/intake-review-fixtures/raw-03/validate-state-truthfulness.sh --contract requirements/baseline/state-truthfulness-contract.json --fixture specs/intake-review-fixtures/raw-03/projection-mismatch.json
# RAW03-PROJECTION-MISMATCH: Rejected (ST007)
pwsh -NoProfile -File specs/intake-review-fixtures/raw-03/validate-state-truthfulness.ps1 -Contract requirements/baseline/state-truthfulness-contract.json -Fixture specs/intake-review-fixtures/raw-03/valid-state-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-03/validate-state-truthfulness.ps1 -Contract requirements/baseline/state-truthfulness-contract.json -Fixture specs/intake-review-fixtures/raw-03/negative-state-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-03/validate-state-truthfulness.ps1 -Contract requirements/baseline/state-truthfulness-contract.json -Fixture specs/intake-review-fixtures/raw-03/projection-parity.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-03/validate-state-truthfulness.ps1 -Contract requirements/baseline/state-truthfulness-contract.json -Fixture specs/intake-review-fixtures/raw-03/projection-mismatch.json
```

## Risiken, Revision und Nicht-Autorität / Risks, revision, and non-authority

Risiken sind Clock Drift zwischen Node und AOC, zu breite oder ungeprüfte
Source-/Capability-Profile, Scheingenauigkeit bei Confidence sowie
unvollständige Konfliktprojektion. Profilversion, Skew-Evidence,
Reason-Code-Pflicht und negative Fixtures begrenzen diese Risiken. Revision ist
bei State-, Zeit-, Source-, Capability-, Authority-, Datenkategorie-,
Plattform-, Projektion- oder Abhängigkeitsänderung erforderlich. / *Risks are
clock drift between node and AOC, broad or unreviewed profiles, false precision
in confidence, and incomplete conflict projection. Profile versions, skew
evidence, mandatory reason codes, and negative fixtures bound these risks.
Revision is required when state, time, source, capability, authority, data
category, platform, projection, or dependency contracts change.*

Dieses Intake und seine historischen Receipt-Daten genehmigen weder Specify
noch Implementierung, Produktänderung, Remote Writes, Merge, Bypass,
Provider-Nutzung, Preset-Änderung oder Level-0-Arbeit. / *This intake and its
historic Receipt data authorise neither Specify nor implementation, product
change, remote writes, merge, bypass, provider use, preset change, or Level-0
work.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md --bind-exact-intake --no-implementation --no-remote-writes
VORBEDINGUNG / PRECONDITION: Nur nach aktuellem Ready-Single-Review und separater aktueller Scope- und Startfreigabe verwenden. Dieser Prompt erteilt keine Specify-, Implementierungs- oder Delivery Authority. / Use only after a current Ready Single review and separate current scope and start authority. This prompt grants no Specify, implementation, or delivery authority.
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nur nach aktuellem Ready-Single-Review, erfülltem Series-Gate und separaten aktuellen Entscheidungen für Scope, Start, Implementierung, Remote Write, Merge, Bypass und Provider verwenden. Historische Delivery-Daten, Eligibility und Ready allein genügen nicht. / Use only after a current Ready Single review, satisfied Series gate, and separate current decisions for scope, start, implementation, remote write, merge, bypass, and provider use. Historic delivery data, Eligibility, and Ready alone are insufficient.
```
<!-- intake-authoring:end -->
