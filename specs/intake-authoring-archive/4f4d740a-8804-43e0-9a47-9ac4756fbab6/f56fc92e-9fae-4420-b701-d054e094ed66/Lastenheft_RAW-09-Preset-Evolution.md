<!-- intake-authoring:begin -->
# RAW-09 – Preset Evolution / Preset Evolution

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** Git- und Review-Grundlagen; keine Preset-, Promotion-, AEPS- oder Spec-Kit-Erfahrung / Git and review basics; no preset, promotion, AEPS, or Spec Kit experience
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

RAW-09 bewertet wiederholbare AOC-Evidence und erstellt daraus höchstens ein
de-identifiziertes Preset Proposal. Der bisherige Stand nannte Proposal-
Qualität, aber keinen prüfbaren Unterschied zwischen Proposal-Erstellung,
Eignung für ein Promotion Review und tatsächlicher Promotion. Dadurch könnten
ein einzelnes Projekt, historische Delivery-Daten oder eine gute Idee
fälschlich als Preset-Freigabe gelesen werden. / *RAW-09 assesses repeatable
AOC evidence and may create only a de-identified preset proposal. The previous
state did not provide a testable distinction between drafting a proposal,
eligibility for a promotion review, and actual promotion. A single project,
historic delivery data, or a good idea could therefore be mistaken for preset
approval.*

Der Zielzustand ist ein versionierter, maschinenlesbarer Proposal-Vertrag mit
deterministischen Reifezuständen, typisierten Handoffs, positiver und negativer
Offline-Evidence sowie fail-closed Authority-Grenzen. RAW-09 besitzt Analyse
und Proposal Evidence. Es besitzt weder Preset Write noch Promotion. / *The
target is a versioned machine-readable proposal contract with deterministic
maturity states, typed handoffs, positive and negative offline evidence, and
fail-closed authority boundaries. RAW-09 owns analysis and proposal evidence,
not preset write or promotion.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Preset:** wiederverwendbarer Engineering-Vertrag oder eine
  Konfigurationsschicht; kein AOC-Produktfeature. / *A reusable engineering
  contract or configuration layer, not an AOC product feature.*
- **Proposal / Vorschlag:** reviewbares Paket aus Zweck, Anwendbarkeit,
  Evidence, Risiken, Tests und Migration. Ein Proposal ist keine Freigabe. /
  *A reviewable package of purpose, applicability, evidence, risks, tests, and
  migration. A proposal is not approval.*
- **Promotion:** ausdrücklich autorisierte Übernahme eines geprüften Proposals
  in einen höheren Reife- oder Kanonizitätszustand. / *An explicitly
  authorised move of a reviewed proposal to a higher maturity or canonical
  state.*
- **Promotion Review:** getrennte Qualitäts- und Evidence-Prüfung vor einer
  möglichen Promotion; ihre Eignung ist noch keine Promotion. / *A separate
  quality and evidence review before possible promotion; eligibility is not
  promotion.*
- **Applicability / Anwendbarkeit:** begründete Aussage, für welche Projekte,
  Plattformen und Grenzen eine Regel gilt. / *A reasoned statement of the
  projects, platforms, and boundaries to which a rule applies.*
- **Generalisation / Verallgemeinerung:** Übertragung eines Musters über sein
  Ursprungsprojekt hinaus. Sie benötigt Cross-Project-Evidence. / *Transfer of
  a pattern beyond its source project; it requires cross-project evidence.*
- **Positive Evidence:** Nachweis, dass die erwartete Grenze besteht. /
  *Evidence that an expected boundary holds.*
- **Negative Evidence:** Gegenbeispiel oder erwartete Ablehnung, die eine
  falsche Freigabe verhindert. / *A counterexample or expected rejection that
  prevents false approval.*
- **ProviderFailure:** externer Tool- oder Dienstfehler; er ist kein
  Produktfehler und keine erfolgreiche Evidence. / *An external tool or
  service failure; it is neither a product failure nor successful evidence.*
- **Compatibility, Migration und Rollback:** Verträglichkeit, Übergang und
  überprüfbare Rückkehr zur vorherigen Version. / *Compatibility, transition,
  and verifiable return to the previous version.*
- **Deferred:** zurückgestellt, weil Evidence oder aktuelle Authority fehlt. /
  *Deferred because evidence or current authority is missing.*
- **RejectedWithRationale:** abgelehnt mit nachvollziehbarer Begründung;
  Evidence wird nicht gelöscht. / *Rejected with a traceable rationale;
  evidence is retained.*
- **research-only:** Analyse ohne Preset Write, Promotion oder Produktaktion. /
  *Analysis without preset write, promotion, or product action.*
- **Spec Kit:** dokumentorientierter Workflow für Spezifikation, Planung und
  Tasks. Dieses Lastenheft startet ihn nicht. / *A document-oriented workflow
  for specification, planning, and tasks. This intake does not start it.*
- **Delivery Authority:** historische Obergrenze eines Lieferwegs; sie ist
  keine aktuelle Start-, Write-, Merge-, Bypass- oder Promotion-Freigabe. /
  *A historic delivery ceiling, not a current execution permission.*

## Scope und Non-Goals / Scope and non-goals

Im Scope liegen Proposal-Reifezustände, Evidence-Schwellen, Repository-
Auswahl, Generalisation Review, Proposal Package, offline Field-Validation-
Evidence, Handoffs, Reason Codes und Authority-Gates. / *Scope includes
proposal maturity states, evidence thresholds, repository selection,
generalisation review, proposal packaging, offline field-validation evidence,
handoffs, reason codes, and authority gates.*

Nicht im Scope liegen Produktcode, Preset-Erstellung oder -Änderung, Promotion,
Providerzugriff, tatsächliche Repository Writes, Community-Submission,
Specify, Implementierung, Remote Write, Merge, Bypass, GitHub- oder Level-0-
Mutation. / *Non-goals include product code, preset creation or modification,
promotion, provider access, repository writes, community submission, Specify,
implementation, remote write, merge, bypass, GitHub, or Level-0 mutation.*

## Quellen, Findings und typisierte Handoffs / Sources, findings, and typed handoffs

Quellen sind SRC-168, SRC-170 und SRC-174 aus dem
[Source Pack](../../baseline/source-pack.md), RF-16 sowie RF-19 bis RF-21 aus
der Baseline, der [Workflow-Evidence-Vertrag](../../baseline/workflow-evidence-contract.json),
das [Decision Register](../../../docs/decisions/open-decisions.md), das initiale
RAW-09-Review und der neue
[Preset-Evolution-Vertrag](../../baseline/preset-evolution-contract.json). /
*Sources are the named baseline records, the workflow contract, Decision
Register, initial RAW-09 review, and the versioned preset-evolution contract.*

1. `H-RAW08-RAW09`: RAW-08 liefert ein attestiertes, de-identifiziertes
   Knowledge Package `requirements-v1` mit Source-, Decision-, Finding-,
   Evidence- und Retrospective-IDs sowie Traceability-Root-Hash. Fehlende
   Provenienz, Privacy oder Kompatibilität ergibt `Deferred`. / *RAW-08
   provides the versioned knowledge package; invalid provenance, privacy, or
   compatibility defers the proposal.*
2. `H-RAW09-HOME-BASELINE`: RAW-09 liefert ausschließlich ein Proposal an
   `hindermath/home-baseline`. Der Handoff benötigt alle Evidence-, Quality-
   und Authority-Felder und erteilt keine Level-0-Write-Authority. / *RAW-09
   hands only a proposal to home-baseline and grants no Level-0 write
   authority.*
3. `H-RAW09-SPEC-KIT`: Erst Level 0 darf bei nachgewiesener Community-
   Allgemeingültigkeit und freier serieller Einzelwarteschlange ein Proposal
   an `github/spec-kit` vorbereiten. Parallele Einreichungen sind verboten. /
   *Only Level 0 may prepare a github/spec-kit proposal after community-general
   applicability and the serial single-item queue are proven.*

Vier Child-Boundaries bleiben getrennt: Gap Detection erzeugt Evidence-bound
Gap Records; Generalisation Review klassifiziert Anwendbarkeit; Proposal
Package erstellt das de-identifizierte Paket; Field Validation liefert
positive, negative und Provider-Failure-Evidence. Keine Boundary schreibt oder
promotet ein Preset. / *The four child boundaries remain separate and none
writes or promotes a preset.*

## Security, Privacy, A11Y, Plattform und Lieferkette / Security, privacy, A11Y, platform, and supply chain

- **Security:** Secrets, Credentials, private Schlüssel, unreviewte
  ausführbare Payloads und private Registry-Daten sind verboten. Ein Treffer
  blockiert das Proposal. / *Secrets, credentials, private keys, unreviewed
  executable payloads, and private registry data are forbidden.*
- **Privacy und Public Content:** Evidence MUSS de-identifiziert und
  datenminimiert sein. Private Pfade, Personen- oder Kundendaten dürfen AOC
  nicht verlassen. Community-Handoffs benötigen public-safe Content. /
  *Evidence must be de-identified, data-minimised, and safe for its target.*
- **A11Y und Sprache:** Dokumente sind DE-first, EN-second, CEFR B2,
  text-first und tastaturtauglich. WCAG 2.2 AA gilt, soweit anwendbar. Farbe,
  Klang, Bewegung oder Position dürfen nie die einzige Information tragen. /
  *Documents are bilingual, CEFR B2, text-first, keyboard-usable, and meet
  WCAG 2.2 AA where applicable.*
- **Plattformen und Nodes:** macOS, Linux und Windows liefern dieselben
  logischen Outcomes und Reason Codes. Container- und Remote-Evidence bindet
  Node-, Trust-Zone-, Provider- und Provenienzfelder; fehlende Provenienz
  blockiert. / *All platforms share logical outcomes; node evidence retains
  provenance and trust boundaries.*
- **Supply Chain:** Dieser Requirements-Vertrag führt keine neue Dependency
  ein. Jede spätere Dependency benötigt Lizenz-, Herkunfts-, SBOM-,
  Vulnerability-, Plattform- und Wartungsevidence. / *Any future dependency
  needs complete supply-chain evidence.*

## Funktionale Anforderungen / Functional requirements

- **FR-001 – Proposal Draft:** Ein Proposal Draft MUSS mindestens zwei
  unabhängige Evidence-Ereignisse besitzen. Eine systemische Einzelquelle ist
  nur mit ausdrücklicher Begründung als Draft-Input zulässig und erfüllt nie
  allein den Promotion-Review-Schwellenwert. / *A proposal draft needs two
  independent events; a reasoned systemic source never satisfies promotion
  review alone.*
- **FR-002 – Promotion-Review-Schwelle:** IAD901 MUSS mindestens zwei reviewte
  Findings aus zwei unabhängigen Projekten, positive und negative Evidence,
  mindestens eine Retrospektive, Cross-Project-Bewertung, Kompatibilität,
  Migration, Rollback, Tests, Security, A11Y, Dokumentation und null blocking
  Findings verlangen. / *IAD901 binds the complete reviewed, cross-project
  threshold.*
- **FR-003 – Keine Einzelprojekt-Kanonisierung:** Ein einzelnes erfolgreiches
  Projekt DARF nie allein ein kanonisches Preset begründen. / *A single
  successful project can never establish a canonical preset.*
- **FR-004 – Repository-Auswahl:** IAD902 MUSS `hindermath/home-baseline` als
  erstes Ziel festlegen. `github/spec-kit` ist nur bei Community-
  Allgemeingültigkeit und serieller Einzelwarteschlange zulässig. / *IAD902
  binds Level 0 first and a conditional serial community handoff.*
- **FR-005 – Promotion Authority:** Es DARF keine dauerhafte Promotion-
  Authority und keinen automatischen oder administrativen Bypass geben. Jedes
  Proposal benötigt eine neue aktuelle menschliche Freigabe. / *Every proposal
  needs a new current human promotion approval with no standing or bypass
  grant.*
- **FR-006 – Lifecycle:** Nur die im Vertrag genannten Zustände und Übergänge
  sind zulässig. Fehlende Evidence oder Authority ergibt `Deferred`; Provider-
  Failure ergibt `DeferredWithPartialEvidence`. / *Only declared lifecycle
  transitions are allowed; missing evidence or authority defers.*
- **FR-007 – Produktspezifische Grenze:** AOC-spezifische Produktentscheidungen
  MÜSSEN als spezifisch markiert bleiben und dürfen nicht als generische
  Preset-Regel ausgegeben werden. / *Product-specific decisions must not be
  generalised as preset rules.*
- **FR-008 – Handoffs:** Alle drei Handoffs MÜSSEN Producer, Consumer, Version,
  Required Fields, Authority, Compatibility, Failure Behavior und Relation
  binden. / *Every handoff must be fully typed and versioned.*
- **FR-009 – Evidence-Klassen:** Positive, negative und Provider-Failure-
  Evidence MÜSSEN getrennt bleiben. Provider-Failure darf keine fachliche
  Freigabe erzeugen. / *Evidence classes remain separate and provider failure
  cannot create approval.*
- **FR-010 – Cross-Cutting:** Jedes Proposal MUSS Security, Privacy, Public
  Content, A11Y, Plattform, Nodes und Supply Chain messbar bewerten. /
  *Every proposal must assess all cross-cutting concerns measurably.*
- **FR-011 – Reason Codes:** Validatoren MÜSSEN die stabilen `PEV001` bis
  `PEV014` Codes verwenden. Erwartete Negativfälle gelten nur bei exakt
  erwarteter Ablehnung als bestanden. / *Validators use stable reason codes;
  an expected rejection is a passing negative test.*
- **FR-012 – Authority:** Ein später enabled Delivery Prompt MUSS zehn aktuelle
  Authority-Gates prüfen. Historisches `MergeAndSync`, `Ready`, `Eligible`
  oder ein Receipt genügt nie. / *Any later enabled delivery prompt must check
  ten current authority gates; historical data never suffices.*

## Nichtfunktionale Anforderungen / Non-functional requirements

- **NFR-001 – Nachvollziehbarkeit:** Jede Schwellenentscheidung bindet IDs,
  Hashes, Review, Evidence und Reason Code. / *Every threshold decision binds
  traceable IDs, hashes, review, evidence, and reason code.*
- **NFR-002 – Determinismus:** Gleiche Inputs und Vertragsversion ergeben auf
  Bash und PowerShell dieselben Outcomes. / *Equal inputs yield equal outcomes
  on both shells.*
- **NFR-003 – Sprache und A11Y:** Nutzerseitige Artefakte erfüllen DE-first,
  EN-second, CEFR B2 und WCAG 2.2 AA. / *User-facing artifacts meet the
  language and accessibility contract.*
- **NFR-004 – Plattformparität:** macOS, Linux und Windows verwenden dieselben
  Zustände und Reason Codes. / *All supported platforms use the same states and
  reason codes.*
- **NFR-005 – Keine neue Dependency:** Die Offline-Fixtures verwenden nur
  vorhandene Bash-, PowerShell- und Python-Runtimes. / *Offline fixtures add no
  dependency.*

## Bestätigte Decisions / Confirmed decisions

1. **IAD901 – Promotion Threshold:** Ein Proposal wird erst für ein getrenntes
   Promotion Review qualifiziert, wenn die vollständige Zwei-Projekt-,
   Review-, Positiv-/Negativ-, Retrospektiven-, Cross-Project- und Quality-
   Evidence vorliegt. Eignung ist keine Promotion. / *The complete reviewed
   two-project evidence threshold grants only promotion-review eligibility.*
2. **IAD902 – Zielrepository:** Zuerst `hindermath/home-baseline`;
   `github/spec-kit` nur bei nachgewiesener Community-Allgemeingültigkeit und
   in der vorgeschriebenen seriellen Einzelwarteschlange. / *Target Level 0
   first; use github/spec-kit only under the community and queue contract.*
3. **Promotion Authority:** Keine dauerhafte Authority, kein automatischer
   oder administrativer Bypass. Jedes Proposal benötigt eine neue aktuelle
   menschliche Freigabe; ohne sie bleibt es `Deferred`. / *No standing or
   bypass authority; every proposal needs new current human approval.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Die positive Fixture erfüllt alle Schwellen, bindet Level 0 als
  Ziel, beansprucht keine Promotion und ergibt `PEV001_VALID_PROPOSAL`. /
  *The positive fixture returns PEV001.*
- **AC-002:** Eine Ein-Projekt-Kanonisierung ergibt
  `PEV002_INSUFFICIENT_PROJECTS`. / *A single-project canonical claim is
  rejected.*
- **AC-003:** Fehlende negative Evidence ergibt
  `PEV004_NEGATIVE_EVIDENCE_MISSING`. / *Missing negative evidence defers.*
- **AC-004:** Produktspezifische Verallgemeinerung ergibt
  `PEV006_PRODUCT_SPECIFIC_REJECTED`. / *Product-specific generalisation is
  rejected.*
- **AC-005:** `github/spec-kit` ohne Community-Allgemeingültigkeit ergibt
  `PEV008_COMMUNITY_APPLICABILITY_MISSING`. / *Missing community applicability
  defers.*
- **AC-006:** Zwei parallele Community-Submissions ergeben
  `PEV009_SERIAL_QUEUE_VIOLATION`. / *Parallel queue use defers.*
- **AC-007:** Fehlende aktuelle Authority trotz Promotion-Claim ergibt
  `PEV010_AUTHORITY_MISSING`. / *Missing authority defers.*
- **AC-008:** Private Pfade oder unvollständige Cross-Cutting-Evidence ergeben
  `PEV011_PRIVATE_DATA_REJECTED`. / *Private or incomplete evidence is
  rejected.*
- **AC-009:** Alle acht Fixtures liefern auf Bash und PowerShell identische
  Zeilen und Exitcode `0`; Validatorfehler liefern Exitcode `2`. / *Both shell
  surfaces agree; validator errors return 2.*
- **AC-010:** Contract, Target, Decision Register, Receipt, Series-Bindung und
  Re-Review besitzen übereinstimmende Decisions und Hashes. / *All governance
  artifacts agree on decisions and hashes.*

## Reproduzierbare Evidence / Reproducible evidence

Für jede Datei unter `specs/intake-review-fixtures/raw-09/*.json` werden beide
Befehle ausgeführt: / *Run both commands for every RAW-09 JSON fixture:*

```text
bash specs/intake-review-fixtures/raw-09/validate-preset-evolution-contract.sh --contract requirements/baseline/preset-evolution-contract.json --fixture <fixture.json>
pwsh -NoProfile -File specs/intake-review-fixtures/raw-09/validate-preset-evolution-contract.ps1 -Contract requirements/baseline/preset-evolution-contract.json -Fixture <fixture.json>
```

Die Sollausgaben sind `RAW09-<ID>: <Outcome> (<PEV-Code>)`. Erwartete
Negativfälle und die positive Fixture enden mit Exitcode `0`; ungültiges JSON,
unbekannte Cases oder Vertragsdrift enden mit `ERROR: PEV000...` und Exitcode
`2`. / *Expected positive and negative fixtures return 0; invalid validator
input returns PEV000 and exit code 2.*

## Status, Abhängigkeiten und nächste Aktion / Status, dependencies, and next action

RAW-08 ist der einzige `Eligible`-Kandidat und besitzt ein aktuelles Ready-
Review; RAW-09 bleibt im Series-Manifest `Blocked`, bis der RAW-08-Lifecycle
`Completed` ist und dieses erneuerte RAW-09 ein aktuelles Ready-Review besitzt.
IAD901 und IAD902 sind beantwortet. / *RAW-08 remains the sole Eligible target.
RAW-09 remains Blocked until its predecessor lifecycle and its own Ready review
are complete. Both decisions are answered.*

Die globale Review-Sperre bleibt bis zu 14 aktuellen Ready-Reviews und
Receipts geschlossen. Die nächste Aktion dieses Updates ist ausschließlich
das vollständige RAW-09-Single-Re-Review. / *The global review gate remains
closed until all 14 reviews and receipts are current. The only next action of
this update is the complete RAW-09 re-review.*

## Re-Evaluation und Nicht-Autorität / Re-evaluation and non-authority

Neu bewertet werden MUSS bei geänderter Evidence-Taxonomie, Promotion-
Schwelle, Repository- oder Community-Queue-Policy, RAW-08-Kompatibilität,
Cross-Cutting-Policy oder vorgeschlagener stehender, automatischer,
administrativer, Preset-Write- oder Promotion-Authority. / *Reassessment is
required when any named contract or authority boundary changes.*

`ReadyForReview`, ein späteres `Ready`, `Eligible`, historisches
`MergeAndSync`, ein Receipt oder eine gute Evidence-Lage erteilt keine
aktuelle Scope-, Start-, Implementierungs-, Governance-Write-, Remote-Write-,
Merge-, Bypass-, Provider-, Preset-Write-, Promotion-, GitHub- oder Level-0-
Authority. / *No quality, lifecycle, delivery, or evidence state grants
current downstream authority.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md --bind-exact-intake --no-implementation --no-remote-writes --no-preset-write --no-promotion --require-current-scope-authority --require-current-start-authority --require-current-implementation-authority --require-current-governance-write-authority --require-current-remote-write-authority --require-current-merge-authority --require-current-bypass-authority --require-current-provider-authority --require-current-preset-write-authority --require-current-promotion-authority
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md --delivery-mode MergeAndSync --require-current-review --no-preset-write --no-promotion --require-current-scope-authority --require-current-start-authority --require-current-implementation-authority --require-current-governance-write-authority --require-current-remote-write-authority --require-current-merge-authority --require-current-bypass-authority --require-current-provider-authority --require-current-preset-write-authority --require-current-promotion-authority
```
<!-- intake-authoring:end -->
