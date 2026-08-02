<!-- intake-authoring:begin -->
# META-LH-02 – Lastenheft-Portfolio und Ownership / Requirements Portfolio and Ownership

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** allgemeine IT-Systemgrenzen; keine Spec-Kit- oder Projektgeschichte / general IT system boundaries; no Spec Kit or project history
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Das Portfolio weist jedem fachlichen Concern genau eine kanonische Owner-Reihe
zu und macht Handoffs, Non-Ownership, Decisions und Parallelitätsrisiken
sichtbar. Dadurch bleibt klar, wer einen Vertrag ändern darf und welche
Consumer ihn nur verwenden. / *The portfolio assigns each domain concern to
exactly one canonical owner series and exposes handoffs, non-ownership,
decisions, and concurrency risks. This makes it clear who may change a contract
and which consumers may only use it.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Concern / fachlicher Belang:** ein klar abgegrenztes Thema wie
  Zustandswahrheit oder Gerätefähigkeit. / *A bounded topic such as state
  truthfulness or hardware capability.*
- **Owner-Reihe / owner series:** die einzige Reihe, die den fachlichen Vertrag
  eines Concerns ändern darf. / *The only series allowed to change a concern's
  domain contract.*
- **Handoff / Übergabevertrag:** versionierter Vertrag von einem Producer zu
  einem Consumer. Fehlt er oder ist er ungültig, stoppt der Consumer
  fail-closed. / *A versioned contract from a producer to a consumer. A missing
  or invalid handoff stops the consumer fail-closed.*
- **Non-Ownership:** ausdrückliche Grenze dessen, was eine Owner-Reihe nicht
  definiert. / *The explicit boundary of what an owner series does not define.*
- **Decision Intake:** nachvollziehbar benannte, menschlich zu bestätigende
  Entscheidung. / *A traceably named decision that requires human confirmation.*
- **DAG / gerichteter azyklischer Graph:** gerichtete Abhängigkeiten ohne
  Rückweg zum Ausgangspunkt. / *Directed dependencies without a path back to
  their starting point.*
- **`manual-assisted`:** Ein Mensch bestätigt materielle Ownership- oder
  Decision-Änderungen; der Modus erteilt keine Lieferautorität. / *A human
  confirms material ownership or decision changes; the mode grants no delivery
  authority.*

Weitere Begriffe stehen im [zweisprachigen Glossar](../../baseline/glossary.md).
/ *The [bilingual glossary](../../baseline/glossary.md) explains additional
terms.*

## Quellen und Finding-Traceability / Sources and finding traceability

Inputs sind SRC-157, SRC-161, SRC-162, SRC-168 bis SRC-175, SRC-177, SRC-181
und SRC-182 aus dem [Source Pack](../../baseline/source-pack.md). META-LH-02
koordiniert die Portfolioabdeckung von RF-06 bis RF-08 und ist kanonischer
Owner von RF-09; die fachlichen Owner von RF-06 bis RF-08 bleiben die im
[Findings-Ledger](../../baseline/review-findings-ledger.md) genannten
RAW-Reihen. META-LH-02 trägt außerdem zu RF-16 und RF-18 bei. / *Inputs are the
listed Source Pack entries. META-LH-02 coordinates portfolio coverage for RF-06
through RF-08 and canonically owns RF-09; the domain owners of RF-06 through
RF-08 remain the RAW series named in the Findings Ledger. META-LH-02 also
contributes to RF-16 and RF-18.*

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Im Scope liegen die neun fachlichen Reihen, die Ownership Matrix, die Series
Map, die Decision Map und der azyklische Handoff-Graph. Inputs sind Source Pack,
Constraints und Findings. Outputs sind die lesbare
[Portfolioübersicht](../../baseline/portfolio-ownership.md), ihr
[maschinenprüfbarer Vertrag](../../baseline/portfolio-ownership.json), die
[Decision Map](../../../docs/decisions/open-decisions.md) und gebundene
Validierungsevidence. Technische Implementierung und der Start einer Reihe
bleiben außerhalb des Scopes. / *Scope covers the nine domain series, ownership
matrix, series map, decision map, and acyclic handoff graph. Inputs are the
Source Pack, constraints, and findings. Outputs are the readable portfolio,
machine-checkable contract, decision map, and bound validation evidence.
Technical implementation and starting a series remain out of scope.*

## System-, Trust- und Authority-Grenzen / System, trust, and authority boundaries

Owner bedeutet Änderungsautorität für genau den eigenen Concern, nicht
Schreibzugriff auf abhängige Reihen. Handoffs sind versionierte Verträge;
Consumer dürfen sie nicht einseitig umdefinieren. Portfolio-Evidence darf nur
öffentliche, repository-relative Inhalte ohne Secrets, private Pfade oder
unnötige Personendaten enthalten. / *Ownership is change authority for exactly
one concern, not write access to dependent series. Consumers may not redefine
versioned handoffs. Portfolio evidence permits only public, repository-relative
content without secrets, private paths, or unnecessary personal data.*

WCAG 2.2 AA, Deutsch-zuerst/Englisch-danach und CEFR B2 gelten für alle
lesbaren Artefakte. Plattformanwendbarkeit gilt für den Python-Validator: Er
verwendet nur die Python-3-Standardbibliothek und dieselben repository-relativen
Pfade auf macOS, Linux und Windows. Software-Supply-Chain-Evidence ist derzeit
`N/A`, weil keine externen Pakete oder Generatorabhängigkeiten eingeführt
werden; bei einer externen Abhängigkeit oder einem anderen Runtime-Handoff wird
diese Einstufung neu geprüft. / *WCAG 2.2 AA, German-first/English-second, and
CEFR B2 apply to every readable artifact. Platform applicability covers the
Python validator, which uses only the Python 3 standard library and the same
repository-relative paths on macOS, Linux, and Windows. Software supply-chain
evidence is currently `N/A` because no external package or generator
dependency is introduced; reassess this decision when such a dependency or
runtime handoff appears.*

## Anforderungen / Requirements

- **FR-001:** Jeder Concern MUSS genau eine kanonische Owner-Reihe besitzen. /
  *Every concern MUST have exactly one canonical owner series.*
- **FR-002:** Jede Reihe MUSS Zweck, Systemgrenze, erwartete Child-Intakes,
  Decision Intakes, Inputs/Outputs, Dependencies, Review-/Evidence-Gates,
  geeignete Modi und Non-Ownership besitzen. / *Every series MUST state its
  purpose, system boundary, expected child intakes, decision intakes,
  inputs/outputs, dependencies, review/evidence gates, suitable modes, and
  non-ownership.*
- **FR-003:** Jeder Handoff MUSS Producer, Consumer, Version, Kantentyp,
  Binding-Status und Fehlerverhalten nennen. / *Every handoff MUST name its
  producer, consumer, version, edge type, binding status, and failure
  behaviour.*
- **FR-004:** Der Graph MUSS azyklisch sein; bindende Contract-Handoffs und
  `PreferredSerialOrder` MÜSSEN getrennt sein. / *The graph MUST be acyclic;
  binding contract handoffs and `PreferredSerialOrder` MUST remain separate.*
- **NFR-001:** Tabellen und Graphen MÜSSEN vollständige Textalternativen
  besitzen; Status darf nicht nur durch Farbe oder Position vermittelt werden.
  / *Tables and graphs MUST have complete text alternatives; status must not
  rely only on colour or position.*
- **NFR-002:** Fachbegriffe und Abkürzungen MÜSSEN den B2- und Glossarregeln
  folgen. / *Domain terms and abbreviations MUST follow the B2 and glossary
  rules.*

## Abhängigkeiten, Decisions, Status und Modus / Dependencies, decisions, status, and mode

META-LH-01 ist der bindende Vorgänger und im Serienmanifest `Completed`.
Der Authoring-Status von META-LH-02 ist `ReadyForReview`; der Serien-Lifecycle
ist `Eligible`. META-LH-02 besitzt keine offene materielle Portfolio-Decision.
Offene Domain-Decisions bleiben in der Decision Map bei ihren RAW-Ownern und
blockieren nur die dort benannte Ausführung. / *META-LH-01 is the binding
predecessor and is `Completed` in the Series manifest. META-LH-02 has authoring
status `ReadyForReview` and Series lifecycle `Eligible`. It has no open
material portfolio decision. Open domain decisions remain assigned to their
RAW owners and block only the named downstream work.*

Der Modus bleibt `manual-assisted`, weil Mehrfachowner, Decision-
Supersession oder neue Handoffs materielle menschliche Bestätigung benötigen.
`Eligible`, ein historischer Delivery-Modus und ein erfolgreiches Review
erteilen keine Implementierungs-, Remote-, Merge- oder Bypass-Autorität. Die
einzige nächste Aktion ist das unabhängige Single-Intake-Review. / *The mode
remains `manual-assisted` because duplicate ownership, decision supersession,
or new handoffs require material human confirmation. Eligibility, a historic
delivery mode, and a successful review grant no implementation, remote, merge,
or bypass authority. The only next action is the independent single-intake
review.*

## Risiken und Annahmen / Risks and assumptions

Ein Zyklus kann durch State↔Orchestrator oder Node↔CLI entstehen. Mehrfachowner
können zudem konkurrierende Vertragsänderungen auslösen. Gerichtete,
versionierte Handoffs, typisierte Kanten und positive sowie negative
DAG-/Ownership-Validierung begrenzen diese Risiken. Es wird angenommen, dass
die neun bestehenden RAW-Reihen die aktuelle fachliche Welle vollständig
abbilden; ein neuer Concern löst eine Revision aus. / *Cycles can arise between
state and orchestration or between nodes and CLI capabilities. Duplicate
owners may cause competing contract changes. Directed versioned handoffs,
typed edges, and positive and negative validation bound these risks. The nine
existing RAW series are assumed to cover the current domain wave; a new concern
triggers revision.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Der Validator bestätigt neun Reihen und neun eindeutige Concerns
  ohne Mehrfachowner. / *The validator confirms nine series and nine unique
  concerns without duplicate ownership.*
- **AC-002:** Die automatische DAG-Prüfung akzeptiert den positiven Vertrag und
  weist die benannte Zyklus-Fixture zurück. / *The automatic DAG check accepts
  the positive contract and rejects the named cycle fixture.*
- **AC-003:** Jede Reihe besitzt mindestens eine prüfbare Non-Ownership-Grenze
  und alle Felder aus FR-002. / *Every series has at least one testable
  non-ownership boundary and every FR-002 field.*
- **AC-004:** Die Decision Map trennt offene und bestätigte Decisions; offene
  Decisions blockieren die betroffene Ausführung sichtbar. / *The decision map
  separates open and confirmed decisions; open decisions visibly block the
  affected execution.*

## Evidence / Evidence

Positive Evidence sind die bestandenen Bash- und PowerShell-Befehle:

```text
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --contract requirements/baseline/portfolio-ownership.json --markdown requirements/baseline/portfolio-ownership.md
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Contract requirements/baseline/portfolio-ownership.json -Markdown requirements/baseline/portfolio-ownership.md
```

Negative Evidence sind zwei ausdrücklich gebundene Fixtures:

```text
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
```

Alle sechs Befehle MÜSSEN mit Exitcode `0` enden: Die positiven Läufe bestätigen
den Vertrag; jeder Fixture-Lauf bestätigt, dass genau der erwartete Fehler
erkannt wurde. Target-, Receipt-, Serien-, Governance- und Secret-Validatoren
bleiben zusätzliche Review-Evidence. / *All six commands MUST exit with code
`0`: the positive runs validate the contract, while each fixture run proves
that the expected defect was detected. Target, receipt, Series, governance, and
secret validators remain additional review evidence.*

## Revisionsbedingungen und Nicht-Autorität / Revision and non-authority

Revision ist bei einem neuen Concern, Owner-Wechsel, neuen oder geänderten
Contract-Handoff, Decision-Supersession oder Evidence-Drift erforderlich.
Dieses Intake erteilt keine Implementierungs-, Scheduling-, Parallelitäts-,
Remote-, Merge-, Bypass- oder Provider-Autorität. / *Revise this intake for a
new concern, owner change, new or changed contract handoff, decision
supersession, or evidence drift. This intake grants no implementation,
scheduling, parallelism, remote, merge, bypass, or provider authority.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung den nachgelagerten Scope, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. Eligibility, Review und historische Receipt-Autorität reichen nicht aus. / Do not start unless a separate current user decision explicitly authorises downstream scope, implementation, remote writes, merge, and bypass. Eligibility, review, and historic receipt authority are insufficient.
```
<!-- intake-authoring:end -->
