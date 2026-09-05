<!-- intake-authoring:begin -->
# META-LH-03 – Lastenheft-Generator und Authoring Contract / Requirements Generator and Authoring Contract

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Markdown und Git-Grundlagen; keine Spec-Kit-Erfahrung / basic Markdown and Git; no Spec Kit experience
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Dieses Lastenheft definiert die einheitliche, validierbare Struktur für neue
AOC-Lastenhefte und ihre Receipts. Es macht Quellen, Entscheidungen,
Prompt-Grenzen und Review-Evidence reproduzierbar, ohne einen nachgelagerten
Lauf zu starten. / *This intake defines the uniform, validatable structure for
new AOC intakes and their receipts. It makes sources, decisions, prompt
boundaries, and review evidence reproducible without starting downstream work.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Lastenheft / requirements intake:** beschreibt Bedarf, Grenzen und
  messbare Ergebnisse, nicht die technische Umsetzung. / *Describes needs,
  boundaries, and measurable outcomes rather than technical implementation.*
- **Receipt / Nachweis:** maschinenlesbare Bindung von Identität, Quellen,
  normalisierten Hashes, Entscheidungen, Autorität und nächster Aktion. /
  *Machine-readable binding of identity, sources, normalised hashes, decisions,
  authority, and next action.*
- **Provenienz / provenance:** nachvollziehbare Herkunft und Reihenfolge der
  verwendeten Quellen. / *Traceable origin and order of the sources used.*
- **Normalisierter SHA-256 / normalised SHA-256:** Hash nach Entfernung eines
  UTF-8-BOM und Vereinheitlichung der Zeilenenden auf LF, ohne weitere
  Inhaltsänderung. / *Hash after removing one UTF-8 BOM and normalising line
  endings to LF without another content change.*
- **Review-Handoff:** ausdrückliche Übergabe an ein unabhängiges Intake-Review;
  sie startet das Review nicht. / *Explicit handoff to independent Intake
  Review; it does not start the review.*
- **Prompt-Bindung / prompt binding:** sichtbarer Befehl und Receipt verweisen
  auf dasselbe exakte Lastenheft und dieselbe Authority-Grenze. / *Visible
  command and Receipt point to the same exact intake and authority boundary.*
- **Materialentscheidung / material decision:** menschliche Wahl, die Scope,
  Security, Delivery oder Akzeptanz verändert. / *Human choice that changes
  scope, security, delivery, or acceptance.*
- **Stop-Marker aus `BLOCKED` und `DO NOT RUN` / stop marker:** normativer
  Abbruchhinweis; bei einer offenen Materialentscheidung enthält der Prompt
  keine ausführbare Befehlszeile. / *Normative stop notice made from the two
  named tokens; an open material decision leaves no executable command line in
  the prompt.*
- **`serial-autonomous` / `manual-assisted`:** Reihenmodus mit serieller
  Ausführung beziehungsweise menschlicher Bestätigung bei Konflikten. Beide
  Modi sind keine Start- oder Lieferautorität. / *Serial execution mode or
  human-assisted conflict mode. Neither grants start or delivery authority.*
- **Operation Receipt und sauberer Arbeitsbaum / operation receipt and clean
  working tree:** letzter gebundener Vorgangsnachweis und Git-Zustand ohne
  unerklärte Änderungen. / *Last bound operation evidence and a Git state
  without unexplained changes.*

Weitere Begriffe stehen im [zweisprachigen Glossar](../../baseline/glossary.md).
/ *The [bilingual glossary](../../baseline/glossary.md) explains additional
terms.*

## Quellen und Finding-Traceability / Sources and finding traceability

Die fachlichen Quellen sind SRC-159, SRC-174, SRC-181 und SRC-182 aus dem
[Source Pack](../../baseline/source-pack.md). Der [Findings
Ledger](../../baseline/review-findings-ledger.md) und die [Coverage
Matrix](../../baseline/coverage-matrix.md) binden die Review-Findings: /
*Domain sources are SRC-159, SRC-174, SRC-181, and SRC-182 from the Source
Pack. The Findings Ledger and Coverage Matrix bind the review findings.*

| Finding | Anforderung / Requirement | Akzeptanz und Evidence / Acceptance and evidence |
|---|---|---|
| RF-03 | FR-002, FR-004 | AC-001, AC-004; versioniertes Receipt und Prompt-Bindung / versioned Receipt and prompt binding |
| RF-10 | FR-005 | AC-002; positive und negative Validatorfälle / positive and negative validator cases |
| RF-12 | FR-001, FR-002 | AC-001, AC-003; strukturierte Templates und Receipts / structured templates and Receipts |
| RF-14 | FR-001 bis FR-005 | diese Matrix und AC-001 bis AC-005 / this matrix and AC-001 through AC-005 |
| RF-17 | NFR-001 | AC-004; DE/EN-, B2- und WCAG-Review / German/English, B2, and WCAG review |
| RF-20 | NFR-002 | AC-002, AC-005; Secret-Negativfall und vollständiger Scan / secret-negative case and full scan |

## Scope und Out of Scope / Scope and out of scope

Im Scope: Naming, Pflichtfelder, Provenienz, Hashes, Review-Handoff, Prompt-
Bindung und Validierung für genau einen neuen Intake oder eine ausdrücklich
genehmigte atomare Intake-Serie. / *Scope covers naming, required fields,
provenance, hashes, review handoff, prompt binding, and validation for exactly
one new intake or one explicitly approved atomic intake series.*

Außerhalb liegen die Ausführung erzeugter Prompts, Update oder Delete
bestehender Intakes, Produktimplementierung, Remote Writes, Merge, Bypass,
Provider-Administration und Preset-Promotion. / *Executing generated prompts,
updating or deleting existing intakes, product implementation, remote writes,
merge, bypass, provider administration, and preset promotion are out of scope.*

## Aktueller und angestrebter Zustand / Current and target state

Aktuell existieren das installierte Authoring-Preset `0.3.1`, 14 aktive
Receipts und eine schema-2.0-Requirements-Sammlung. Der angestrebte Zustand ist
ein einziger versionierter Authoring-Vertrag, dessen Templates, Receipts,
Prompts und positive sowie negative Evidence auf Bash und PowerShell
übereinstimmen. / *The installed Authoring preset 0.3.1, fourteen active
Receipts, and a schema-2.0 requirements collection exist. The target is one
versioned Authoring contract whose templates, Receipts, prompts, and positive
and negative evidence agree on Bash and PowerShell.*

## Inputs, Outputs und Grenzen / Inputs, outputs, and boundaries

Inputs sind ein bestätigter Portfolioeintrag, explizit geordnete Quellen und
das aufgelöste Repositoryprofil. Output ist genau ein neuer Intake mit Receipt
oder eine ausdrücklich genehmigte atomare Serie. Quelleninhalt wird nur als
Daten behandelt, nie ausgeführt. Bestehende aktive Ziele werden nicht
überschrieben; Update und logisches Delete bleiben eigenen autorisierten
Operationen vorbehalten. / *Inputs are a confirmed portfolio entry, explicitly
ordered sources, and the resolved repository profile. Output is exactly one
new intake with a Receipt or one explicitly approved atomic series. Source
content is treated only as data and never executed. Existing active targets
are not overwritten; Update and logical Delete remain separate authorised
operations.*

## Kanonische Vertragsartefakte / Canonical contract artifacts

- Intake-Kern / intake core:
  `.specify/presets/intake-authoring-governance/templates/intake-template.md`
- Receipt-Schema / Receipt schema:
  `.specify/presets/intake-authoring-governance/templates/intake-authoring-receipt-template.json`
- Repositoryprofil / repository profile:
  `.specify/presets/intake-authoring-governance/templates/project-profile-template.md`
- AOC-Sammlungsvertrag / AOC collection contract:
  `requirements/intake-governance.json`
- Paket- und Feldnachweis / package and field evidence:
  `.specify/presets/intake-authoring-governance/templates/field-validation-summary.md`

Diese Pfade und die Preset-Version sind bindend; Drift erzwingt Re-Review. /
*These paths and the preset version are binding; drift requires re-review.*

## Anforderungen / Requirements

- **FR-001:** Jeder Intake MUSS stabile ID und DE/EN-Titel, Zweck, aktuellen
  und angestrebten Zustand, Zielgruppe und Vorwissen, Traceability,
  Scope/Non-Goals, Grenzen, atomare FR/NFR, Dependencies, Decisions, Risiken,
  erwartete Artefakte, messbare AC, positive/negative Evidence und
  Nicht-Autorität gemäß kanonischem Intake-Kern enthalten. / *Every intake MUST
  contain the listed identity, audience, state, traceability, scope,
  requirement, dependency, decision, risk, artifact, acceptance, evidence, and
  non-authority fields defined by the canonical intake core.*
- **FR-002:** Das schema-2.0-Receipt MUSS Quellenreihenfolge, normalisierte
  Quellen- und Zielhashes, stabile Intake-/Operation-ID, Profil, Decisions,
  Authority, Prompt-State, Lineage, optionale Serienbindung und genau eine
  nächste Aktion binden. / *The schema-2.0 Receipt MUST bind ordered sources,
  normalised source and target hashes, stable intake and operation identity,
  profile, decisions, authority, prompt state, lineage, optional Series
  membership, and exactly one next action.*
- **FR-003:** Eine offene Materialentscheidung MUSS `NeedsClarification`,
  stabile Decision-IDs und in beiden Prompt-Blöcken den aus `BLOCKED` und
  `DO NOT RUN` gebildeten Stop-Marker ohne ausführbare Invocation erzeugen. /
  *An open material decision MUST produce NeedsClarification, stable decision
  IDs, and the stop marker made from the two named tokens without executable
  invocations in both prompt blocks.*
- **FR-004:** `ReadyForReview`-Ziele MÜSSEN auf dasselbe exakte Lastenheft
  gebundene Specify-/Autonomous-Prompts enthalten. Kein Authoring-Schritt darf
  sie automatisch ausführen oder aus einem historischen Delivery-Modus
  aktuelle Authority ableiten. / *Ready-for-review targets MUST contain
  Specify and Autonomous prompts bound to the same exact intake. Authoring
  MUST neither execute them automatically nor infer current authority from a
  historic delivery mode.*
- **FR-005:** Bash- und PowerShell-Validatoren MÜSSEN für dieselben positiven
  und negativen Fixtures dieselben Exitcode-Klassen melden. / *Bash and
  PowerShell validators MUST report the same exit-code classes for the same
  positive and negative fixtures.*
- **NFR-001:** Generierte Sprache MUSS Deutsch zuerst und Englisch danach auf
  CEFR-B2-Niveau verwenden, Fachbegriffe beim Erstgebrauch erklären,
  semantische Überschriften und stabile Lesereihenfolge bieten und
  Informationen nie nur über Farbe oder Position vermitteln. WCAG 2.2 AA gilt,
  soweit auf das Artefakt anwendbar. / *Generated language MUST be
  German-first/English-second at CEFR B2, explain first-use terms, use semantic
  headings and stable reading order, and never rely only on colour or
  position. WCAG 2.2 AA applies where relevant.*
- **NFR-002:** Secrets, Credentials, private Pfade und unnötige Personendaten
  MÜSSEN Authoring blockieren. Der eingebettete Secret-Negativfall bleibt eine
  synthetische Testeingabe; aktuell ist kein Authoring-Testpfad in Gitleaks
  ausgenommen. Eine spätere Ausnahme MUSS genau einen benannten Fixture-Pfad
  begrenzen und der vollständige Scan bleibt Pflicht. / *Secrets,
  credentials, private paths, and unnecessary personal data MUST block
  authoring. The embedded secret-negative case is synthetic; no Authoring test
  path is currently allowlisted. A future exception MUST be limited to one
  named fixture path and the full scan remains mandatory.*

## Querschnittsanwendbarkeit / Cross-cutting applicability

- **Security und Privacy:** anwendbar; Quellen werden nicht ausgeführt,
  Credentials und unnötige Personendaten werden abgewiesen, öffentliche
  Evidence verwendet nur repository-relative Pfade oder ausdrücklich benannte
  sichere HTTPS-Snapshots. / *Applicable; sources are never executed,
  credentials and unnecessary personal data are rejected, and public evidence
  uses repository-relative paths or explicitly named safe HTTPS snapshots.*
- **Accessibility:** anwendbar auf alle lesbaren Markdown-, Tabellen- und
  Prompt-Artefakte gemäß NFR-001. / *Applicable to every readable Markdown,
  table, and prompt artifact under NFR-001.*
- **Plattform:** anwendbar; dieselben relativen Pfade und Exitcode-Klassen
  gelten auf macOS, Linux und Windows. Die PowerShell-Fixture-Suites prüfen bei
  verfügbarem Bash beide Validatorfamilien. / *Applicable; the same relative
  paths and exit-code classes apply on macOS, Linux, and Windows. PowerShell
  fixture suites exercise both validator families when Bash is available.*
- **Software Supply Chain:** anwendbar auf das installierte Preset
  `intake-authoring-governance 0.3.1` und dessen Anforderung
  `Spec Kit >=0.8.3`. Dieses Intake installiert kein Paket; eine Preset-,
  Template-, Validator- oder Mindestversionsänderung erzwingt erneute
  Hashprüfung und Review. / *Applicable to the installed preset and its Spec
  Kit minimum version. This intake installs no package; preset, template,
  validator, or minimum-version drift requires renewed hash validation and
  review.*

## Abhängigkeiten, Decisions, Status und Modus / Dependencies, decisions, status, and mode

Beim damaligen Authoring galt als historischer Snapshot: META-LH-01 und
META-LH-02 waren abgeschlossene Vorgänger, META-LH-03 war `Eligible` und besaß
keine offene Materialentscheidung. Dieser Snapshot ist keine aktuelle
Lifecycle-Quelle. Der aktuelle kanonische Zustand steht ausschließlich im
[`manifest.json`](../../../specs/intake-series/aoc-phase-2/manifest.json) und
in der [`order.md`](../series/order.md). / *At authoring time, the historical
snapshot recorded META-LH-01 and META-LH-02 as completed predecessors and
META-LH-03 as Eligible with no open material decision. This snapshot is not a
current lifecycle source. Only the linked manifest and order document define
the current canonical state.*

`serial-autonomous` bleibt der geeignete Modus für später ausdrücklich
freigegebene disjunkte Ziele; bei Konflikten gilt `manual-assisted`. Eligibility
und Modus sind nur Ordnungsinformation. / *Serial-autonomous remains suitable
for later explicitly authorised disjoint targets; conflicts use
manual-assisted. Eligibility and mode are ordering information only.*

## Risiken und Recovery / Risks and recovery

Risiken sind Schema-Drift, teilweise Publikation, Prompt-/Authority-Drift,
Secret-Übernahme und konkurrierende Writes. Vor Publikation werden alle Ziele
gestaged und validiert; ein Fehler hinterlässt kein teilaktives Ziel. Recovery
beginnt mit Operation Receipt, letztem bestätigten Hash und sauberem
Arbeitsbaum. Unbekannte Authority oder Hash-Drift stoppt vor dem nächsten
Write. / *Risks include schema drift, partial publication, prompt/authority
drift, secret copying, and concurrent writes. Every target is staged and
validated before publication; failure leaves no partially active target.
Recovery starts from the operation Receipt, last confirmed hash, and clean
working tree. Unknown authority or hash drift stops before the next write.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Kanonischer Intake-Kern, Receipt-Template, Repositoryprofil,
  AOC-Sammlungsvertrag und Preset-Version sind vorhanden, hashbar und
  widerspruchsfrei; ein gültiges schema-2.0-Receipt besteht Bash und
  PowerShell. / *Canonical contract artifacts exist, are hashable and
  consistent, and one valid schema-2.0 Receipt passes Bash and PowerShell.*
- **AC-002:** Die drei gebundenen Fixture-Suites enden mit Exitcode `0` und
  bestätigen intern die erwarteten positiven sowie negativen Exitcodes für
  Hash-Drift, Secret, implizite Remote Authority, ausführbaren Blocked-Prompt,
  private URL, ungültigen Root, Teilpublikation, aktives Ziel nach Delete,
  Traversal und Mehrfach-Eligibility. / *All three bound fixture suites exit
  zero and verify the named positive and negative classes internally.*
- **AC-003:** Alle 14 aktiven Receipts bestehen beide Receipt-Validatoren;
  Pflichtfelder sind über Template und schema-2.0-Receipt maschinen- und
  menschenlesbar gebunden. / *All fourteen active Receipts pass both
  validators; required fields are bound through the template and schema-2.0
  Receipt.*
- **AC-004:** Semantisches Review bestätigt vollständige DE/EN-Paare,
  Erstbegriffserklärungen, stabile Überschriften, farbunabhängige Statusangaben
  und Prompt-Parität. Kein Authoring-Schritt startet Review, Specify,
  Autonomous, Implementierung oder Delivery. / *Semantic review confirms the
  language, terminology, structure, colour-independent status, and prompt
  contract. Authoring starts no downstream action.*
- **AC-005:** Der vollständige Gitleaks-Scan endet ohne Fund; keine
  Authoring-Testausnahme ist aktiv. Plattform- oder Supply-Chain-Drift löst
  Re-Evaluation aus. / *The full Gitleaks scan finds no leak and no Authoring
  test exception is active. Platform or supply-chain drift triggers
  re-evaluation.*

## Erwartete Artefakte und Evidence / Expected artifacts and evidence

Die portablen Fixture-Suites erzeugen temporäre Inputs, prüfen Bash- und
PowerShell-Parität und entfernen ihre temporären Verzeichnisse: / *The portable
fixture suites create temporary inputs, test Bash/PowerShell parity, and remove
their temporary directories:*

```text
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-validator.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-lifecycle.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-governance-config.ps1
```

Die aktuellen AOC-Verträge werden zusätzlich direkt geprüft: / *Current AOC
contracts are also checked directly:*

```text
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json --repo .
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json -Repo .
bash .specify/presets/intake-review-governance/scripts/validate-intake-governance-config.sh --config requirements/intake-governance.json --repo . --json
pwsh -NoProfile -File .specify/presets/intake-review-governance/scripts/validate-intake-governance-config.ps1 -Config requirements/intake-governance.json -Repo . -Json
gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100
```

Die Validator-Fixture-Suite bindet insbesondere den Secret-Negativfall und den
aus `BLOCKED` und `DO NOT RUN` gebildeten Stop-Marker. Die Lifecycle-Suite bindet URL-, Series-,
Transaktions- und Tombstone-Fälle. Die Governance-Suite bindet Sprache,
portable Rollen, Inventar, Hash-Drift, Traversal und genau eine deklarierte
Eligibility. / *The validator suite binds the secret and blocked-prompt cases;
the lifecycle suite binds URL, Series, transaction, and tombstone cases; the
governance suite binds language, portable roles, inventory, hash drift,
traversal, and exactly one declared Eligible target.*

## Revision und Nicht-Autorität / Revision and non-authority

Revision ist bei Preset-, Schema-, Template-, Profil-, Validator-,
Fixture-, Prompt-, Plattform- oder Supply-Chain-Drift erforderlich. Dieses
Lastenheft besitzt keine aktuelle Authority für Produktcode, Intake-
Update/Delete, Review-Start, Specify, Autonomous, Implementierung, Remote
Writes, Merge, Bypass, Provider-Administration oder Preset-Promotion. /
*Revision is required for drift in the preset, schema, template, profile,
validator, fixture, prompt, platform, or supply chain. This intake grants no
current authority for product code, Intake Update/Delete, review start,
Specify, Autonomous, implementation, remote writes, merge, bypass, provider
administration, or preset promotion.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung den nachgelagerten Scope, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. Eligibility, Modus, Review und historische Receipt-Autorität reichen nicht aus und Provider-Administration bleibt ausgeschlossen. / Do not start unless a separate current user decision explicitly authorises downstream scope, implementation, remote writes, merge, and bypass. Eligibility, mode, review, and historic Receipt authority are insufficient, and provider administration remains excluded.
```
<!-- intake-authoring:end -->
