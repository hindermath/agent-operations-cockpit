<!-- intake-authoring:begin -->
# META-LH-05 – Generierung der ersten vollständigen Lastenheft-Welle / Generation of the First Complete Requirements Wave

**Status:** ReadyForReview
**Zielgruppe / Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IT apprentices and experienced professionals
**Vorkenntnisse / Assumed prior knowledge:** Grundverständnis der AOC-Schichten aus dem Source Pack; keine Spec-Kit- oder Autonomous-Erfahrung / basic understanding of AOC layers from the source pack; no Spec Kit or autonomous-run experience
**Profil / Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Dieses Lastenheft definiert eine erste vollständige Wave, also ein atomar
behandeltes Paket, aus genau einem eigenständigen Intake je fachlicher
Owner-Reihe RAW-01 bis RAW-09. Ein Intake ist hier ein prüfbares Lastenheft;
eine Owner-Reihe bündelt genau einen fachlichen Concern, also einen klar
abgegrenzten Verantwortungsbereich. Jeder Intake wird an Findings, Decisions,
Evidence und einen Ausführungsmodus gebunden. / *This intake defines the first
complete wave, an atomically handled package containing exactly one
self-contained intake for each domain-owner series RAW-01 through RAW-09. An
intake is a reviewable requirements document; an owner series owns one
bounded domain concern. Each intake is bound to findings, decisions, evidence,
and an execution mode.*

## Quellen und Findings / Sources and findings

Verbindlich sind alle Source-IDs und Constraints des Source Packs, RF-01 bis
RF-21, META-LH-01 bis META-LH-04, die Portfolio-Ownership-Verträge, die
Coverage Matrix, das aktuelle Series-Manifest und der ausführbare
First-Wave-Vertrag. RF bezeichnet eine Zeile im Review Findings Ledger;
Coverage ist die nachvollziehbare Zuordnung von Quelle oder Finding zu Owner,
Anforderung, Akzeptanz und Evidence. / *Binding inputs are all source IDs and
constraints in the source pack, RF-01 through RF-21, META-LH-01 through
META-LH-04, the portfolio-ownership contracts, the coverage matrix, the
current series manifest, and the executable first-wave contract. RF means one
row in the Review Findings Ledger; coverage is the traceable mapping from a
source or finding to owner, requirement, acceptance, and evidence.*

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Eingaben sind die freigegebene Quellenbaseline, das Portfolio, die
Ownership-Matrix, die Decision Map und die Series-Evidence. Ausgaben eines
autorisierten Erstlaufs sind genau neun neue aktive RAW-Intakes, ihre
Authoring Receipts, die Coverage-Bindung und ihre Series-Einträge. Ein Receipt
ist der hashgebundene Herkunfts- und Operationsnachweis. Atomare Publikation
bedeutet, dass kein Teilbestand als vollständige Wave veröffentlicht wird. /
*Inputs are the accepted source baseline, portfolio, ownership matrix,
decision map, and series evidence. Outputs of an authorised first run are
exactly nine new active RAW intakes, their Authoring Receipts, coverage
bindings, and series entries. A Receipt is the hash-bound provenance and
operation record. Atomic publication means a partial set is never published
as a complete wave.*

Nicht im Scope sind Review-Akzeptanz, Specify, Plan, Tasks, Produktcode,
Hardwareentwicklung, Produktmanifest oder Preset-Promotion. Ein
Produkt-Scaffold ist eine erzeugte Runtime-, Build- oder Teststruktur und wird
von diesem Authoring-Vertrag nicht erzeugt. / *Review acceptance, Specify,
Plan, Tasks, product code, hardware development, product manifests, and preset
promotion are out of scope. A product scaffold is generated runtime, build,
or test structure; this authoring contract creates none.*

## Aktueller Status und nächste Aktion / Current status and next action

Beim damaligen Authoring galt als historischer Snapshot: META-LH-01 bis
META-LH-04 waren `Completed`, META-LH-05 war der einzige deklarierte
`Eligible`-Kandidat und alle RAW-Ziele samt Receipts existierten. Dieser
Snapshot ist keine aktuelle Lifecycle-Quelle. Der aktuelle kanonische Zustand
steht ausschließlich im
[`manifest.json`](../../../specs/intake-series/aoc-phase-2/manifest.json) und
in der [`order.md`](../series/order.md). Für META-LH-05 ist keine materielle
Decision offen. Re-Entry wird bei jedem Aufruf neu aus dem gebundenen Bestand
ermittelt; ein Intake-lokaler Snapshot erteilt keine Operation. / *At authoring
time, the historical snapshot recorded META-LH-01 through META-LH-04 as
Completed, META-LH-05 as the sole Eligible candidate, and all RAW targets and
receipts as present. This snapshot is not a current lifecycle source. Only the
linked manifest and order document define the current canonical state. No
material META-LH-05 decision is open. Re-entry is recalculated from the bound
inventory on every invocation; an intake-local snapshot grants no operation.*

## Re-Entry, Kollision und Ownership / Re-entry, collision, and ownership

Re-Entry ist ein erneuter Aufruf nach einem früheren Wave-Lauf. Bei
`AllAbsent` darf `CreateAtomic` nur mit aktueller, ausdrücklicher
New-Target-Autorität beginnen. `AllMatching` führt ausschließlich zu
`VerifyOnly`. `Partial` und `Collision` blockieren fail-closed. Partial
bedeutet Teilbestand; Collision bedeutet, dass Pfad, Identität oder Hash eines
vorhandenen Ziels nicht zum gebundenen Vertrag passt. Adoption, Supersession,
Repair oder Update benötigen jeweils einen getrennten aktuellen Auftrag. /
*Re-entry is a repeated invocation after an earlier wave run. `AllAbsent`
permits `CreateAtomic` only with current explicit new-target authority.
`AllMatching` permits `VerifyOnly` only. `Partial` and `Collision` block
fail-closed. Partial means an incomplete existing set; collision means an
existing path, identity, or hash disagrees with the bound contract. Adoption,
supersession, repair, or update each requires separate current authority.*

Jeder fachliche Concern besitzt genau einen Concern Owner. Zusätzliche
Meta-Governance-Owner sind zulässig und für RF-Coverage erforderlich, sind
aber keine zweiten fachlichen Owner. Doppelte Concern Owner blockieren. /
*Every domain concern has exactly one concern owner. Additional
meta-governance owners are allowed and required for RF coverage, but they are
not second domain owners. Duplicate concern owners block.*

## Trust-, Modus- und Authority-Grenzen / Trust, mode, and authority boundaries

`serial-autonomous` bleibt die vorgesehene sichere Reihenfolge für einen
autorisierten Erstlauf. Jeder Modus MUSS genau die neun Kriterien Authority,
Side Effects, Reversibilität, Write Scope, Decisions, Integration, Review,
Abort und Recovery aus dem META-LH-04-Vertrag binden. Paralleles Authoring ist
nur mit separater aktueller Wave-Autorität, disjunkten Writes, ohne gemeinsame
offene Decisions, mit geplantem Consolidation Review und definierten Abort-
und Recovery-Regeln zulässig. Fehlt eine Bedingung, lautet das Ergebnis
`Blocked`. / *`serial-autonomous` remains the intended safe order for an
authorised first run. Every mode MUST bind exactly the nine META-LH-04
criteria: authority, side effects, reversibility, write scope, decisions,
integration, review, abort, and recovery. Parallel authoring additionally
requires separate current wave authority, disjoint writes, no shared open
decisions, a planned consolidation review, and defined abort and recovery
rules. If any condition is missing, the outcome is `Blocked`.*

Eligibility, `Ready`, gespeicherter Delivery-Modus und historischer
Admin-Bypass sind keine aktuelle Start-, Schreib-, Remote-, Merge- oder
Bypass-Autorität. Fail-closed bedeutet, dass fehlende oder widersprüchliche
Evidence blockiert statt eine Freigabe anzunehmen. / *Eligibility, `Ready`, a
stored delivery mode, and historic admin bypass are not current start, write,
remote, merge, or bypass authority. Fail-closed means missing or conflicting
evidence blocks rather than implying permission.*

## Anforderungen / Requirements

- **FR-001:** Bei `AllAbsent` MUSS ein autorisierter Erstlauf genau neun neue
  fachliche Intakes RAW-01 bis RAW-09 erzeugen; jeder Pfad und jede Intake-ID
  kommt genau einmal vor. / *For `AllAbsent`, an authorised first run MUST
  create exactly nine new domain intakes RAW-01 through RAW-09; every path and
  intake ID occurs exactly once.*
- **FR-002:** Jeder Intake MUSS Zweck, Systemgrenze, erwartete Children,
  Decisions, Inputs/Outputs, Dependencies, Review-/Evidence-Gates und Modus
  enthalten. / *Every intake MUST contain purpose, system boundary, expected
  children, decisions, inputs/outputs, dependencies, review/evidence gates,
  and mode.*
- **FR-003:** Jeder Concern MUSS genau einen fachlichen Concern Owner besitzen.
  Jede RF-Zeile MUSS zusätzlich mindestens einen Meta-Governance-Owner und
  einen fachlichen Owner besitzen oder begründet rein meta-governed sein. /
  *Every concern MUST have exactly one domain concern owner. Every RF row MUST
  additionally have at least one meta-governance owner and one domain owner,
  or be justified as meta-governed only.*
- **FR-004:** Alle neuen Ziele und Receipts MÜSSEN vor atomarer
  Series-Publikation auf beiden Validatoroberflächen bestehen. / *All new
  targets and Receipts MUST pass both validator surfaces before atomic Series
  publication.*
- **FR-005:** Re-Entry MUSS deterministisch `CreateAtomic`, `VerifyOnly` oder
  `Blocked` liefern. Partial, Collision, Hash-Drift oder unklare Authority
  MÜSSEN blockieren und dürfen nichts überschreiben. / *Re-entry MUST
  deterministically produce `CreateAtomic`, `VerifyOnly`, or `Blocked`.
  Partial state, collision, hash drift, or unclear authority MUST block and
  overwrite nothing.*
- **FR-006:** Jede serielle oder parallele Moduseinstufung MUSS genau die neun
  META-LH-04-Kriterien enthalten; Parallelität erfüllt zusätzlich alle dort
  definierten Gates. / *Every serial or parallel mode classification MUST
  provide exactly the nine META-LH-04 criteria; parallelism additionally
  satisfies every gate defined there.*
- **NFR-001:** Alle neun Intakes MÜSSEN DE-first/EN-second, CEFR B2,
  Erstbegriffserklärungen, text-first Status und WCAG-2.2-AA-Regeln erfüllen,
  soweit anwendbar. / *All nine intakes MUST satisfy DE-first/EN-second, CEFR
  B2, first-use explanations, text-first status, and WCAG 2.2 AA where
  applicable.*
- **NFR-002:** Bash und PowerShell MÜSSEN für Vertrag, Inventar, Receipts und
  Fixtures semantisch gleiche Ergebnisse liefern. / *Bash and PowerShell MUST
  produce equivalent results for contract, inventory, Receipts, and fixtures.*

## Cross-Cutting-Anwendbarkeit / Cross-cutting applicability

- **Sicherheit / Security:** Anwendbar auf Quellen, Pfade, Hashes und
  Authority-Evidence. Secrets, Tokens, ausführbare Fremdinhalte und implizite
  Remote-Befehle sind verboten; ein Fund blockiert. / *Applicable to sources,
  paths, hashes, and authority evidence. Secrets, tokens, executable external
  content, and implicit remote commands are forbidden; discovery blocks.*
- **Privacy und personenbezogene Daten / Privacy and personal data:** Für die
  Wave nicht erforderlich. Intakes und Fixtures dürfen keine unnötigen
  personenbezogenen Daten enthalten; ein Fund löst Stop und Re-Evaluation
  aus. / *Not required for the wave. Intakes and fixtures must contain no
  unnecessary personal data; discovery triggers stop and re-evaluation.*
- **Öffentliche Inhalte / Public content:** Repository-Dokumente können
  öffentlich werden, enthalten aber keine Veröffentlichungsvollmacht. Links,
  Lizenz, Security- und Contribution-Grenzen werden vor Veröffentlichung
  geprüft. / *Repository documents may become public but grant no publication
  authority. Links, licence, security, and contribution boundaries are
  checked before publication.*
- **Barrierefreiheit / Accessibility:** Text-first, farbunabhängig, stabile
  Überschriften und WCAG 2.2 AA gelten für Markdown, Prompts und CLI-Ausgaben,
  soweit anwendbar. / *Text-first, colour-independent, stable headings, and
  WCAG 2.2 AA apply to Markdown, prompts, and CLI output where applicable.*
- **Plattformen / Platforms:** Bash und PowerShell müssen auf macOS, Linux und
  Windows semantisch gleich entscheiden. Fehlende Parität blockiert. / *Bash
  and PowerShell must decide equivalently on macOS, Linux, and Windows.
  Missing parity blocks.*
- **Supply Chain:** Es werden keine neuen Abhängigkeiten eingeführt; verwendet
  werden vorhandene Bash-, PowerShell- und Python-Laufzeiten. Neue
  Abhängigkeiten oder Versionsdrift lösen Re-Evaluation aus. / *No new
  dependency is introduced; existing Bash, PowerShell, and Python runtimes
  are used. New dependencies or version drift trigger re-evaluation.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Der aktuelle AOC-Bestand enthält RAW-01 bis RAW-09 und genau neun
  zugehörige aktive Receipts. Der Wave-Validator meldet `VerifyOnly`; alle
  neun Receipts bestehen Bash und PowerShell mit Exitcode 0. / *The current
  AOC inventory contains RAW-01 through RAW-09 and exactly nine active
  Receipts. The wave validator reports `VerifyOnly`; all nine Receipts pass
  Bash and PowerShell with exit code zero.*
- **AC-002:** Portfoliovertrag und Markdown-View bestehen; Doppel-Concern-
  Owner und Zyklus werden durch die gebundenen Negativfixtures blockiert.
  Meta-Governance-Owner zählen nicht als zweite Concern Owner. / *The
  portfolio contract and Markdown view pass; bound negative fixtures block a
  duplicate concern owner and a cycle. Meta-governance owners do not count as
  second concern owners.*
- **AC-003:** Die Re-Entry-Fixtures liefern `CreateAtomic` für autorisiertes
  `AllAbsent`, `VerifyOnly` für `AllMatching` und `Blocked` für `Partial` und
  `Collision`; Bash und PowerShell enden jeweils mit Exitcode 0. / *Re-entry
  fixtures produce `CreateAtomic` for authorised `AllAbsent`, `VerifyOnly`
  for `AllMatching`, and `Blocked` for `Partial` and `Collision`; Bash and
  PowerShell each exit zero.*
- **AC-004:** Coverage Matrix, Findings Ledger und Source Pack ordnen SRC- und
  RF-Evidence den Meta- und fachlichen Ownern zu; keine RF-Zeile ist
  `Uncovered`. / *The coverage matrix, findings ledger, and source pack map
  SRC and RF evidence to meta and domain owners; no RF row is `Uncovered`.*
- **AC-005:** Kein Prompt, Specify, Autonomous, Produktmanifest oder
  Produkt-Scaffold wird durch Authoring, VerifyOnly oder Review ausgeführt. /
  *Authoring, VerifyOnly, and review execute no prompt, Specify, Autonomous,
  product manifest, or product scaffold.*
- **AC-006:** Semantisches Single Review bestätigt DE/EN, Terminologie,
  text-first Status, Authority-Grenzen und Cross-Cutting-Anwendbarkeit. /
  *Semantic Single review confirms language, terminology, text-first status,
  authority boundaries, and cross-cutting applicability.*

## Reproduzierbare Evidence und Traceability / Reproducible evidence and traceability

Alle folgenden Befehle MÜSSEN mit Exitcode 0 enden. Die negativen Fixtures
bestehen, wenn sie den erwarteten Status `Blocked` beziehungsweise den
erwarteten Portfolio-Fehler erkennen. / *Every command below MUST exit zero.
Negative fixtures pass when they detect the expected `Blocked` status or
portfolio error.*

```text
bash specs/intake-review-fixtures/meta-lh-05/validate-first-wave.sh --contract requirements/baseline/first-wave-authoring-contract.json --repo .
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-05/validate-first-wave.ps1 -Contract requirements/baseline/first-wave-authoring-contract.json -Repo .
bash specs/intake-review-fixtures/meta-lh-05/validate-first-wave.sh --contract requirements/baseline/first-wave-authoring-contract.json --fixture specs/intake-review-fixtures/meta-lh-05/all-absent-authorized.json
bash specs/intake-review-fixtures/meta-lh-05/validate-first-wave.sh --contract requirements/baseline/first-wave-authoring-contract.json --fixture specs/intake-review-fixtures/meta-lh-05/all-matching.json
bash specs/intake-review-fixtures/meta-lh-05/validate-first-wave.sh --contract requirements/baseline/first-wave-authoring-contract.json --fixture specs/intake-review-fixtures/meta-lh-05/partial-existing.json
bash specs/intake-review-fixtures/meta-lh-05/validate-first-wave.sh --contract requirements/baseline/first-wave-authoring-contract.json --fixture specs/intake-review-fixtures/meta-lh-05/collision.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-05/validate-first-wave.ps1 -Contract requirements/baseline/first-wave-authoring-contract.json -Fixture specs/intake-review-fixtures/meta-lh-05/all-absent-authorized.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-05/validate-first-wave.ps1 -Contract requirements/baseline/first-wave-authoring-contract.json -Fixture specs/intake-review-fixtures/meta-lh-05/all-matching.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-05/validate-first-wave.ps1 -Contract requirements/baseline/first-wave-authoring-contract.json -Fixture specs/intake-review-fixtures/meta-lh-05/partial-existing.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-05/validate-first-wave.ps1 -Contract requirements/baseline/first-wave-authoring-contract.json -Fixture specs/intake-review-fixtures/meta-lh-05/collision.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --contract requirements/baseline/portfolio-ownership.json --markdown requirements/baseline/portfolio-ownership.md
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Contract requirements/baseline/portfolio-ownership.json -Markdown requirements/baseline/portfolio-ownership.md
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
```

Für alle neun RAW-Receipts werden zusätzlich beide installierten Intake-
Authoring-Validatoren in stabiler Namensreihenfolge ausgeführt. FR-001,
FR-004 und AC-001 binden Inventar und Receipts. FR-003 und AC-002 binden
Ownership. FR-005 und AC-003 binden Re-Entry. FR-002, AC-004 und die
Coverage Matrix binden Inhalts- und RF-Abdeckung. FR-006 bindet den
META-LH-04-Vertrag. NFR-001, NFR-002, AC-005 und AC-006 werden durch beide
Validatoroberflächen und vollständiges semantisches Single Review gebunden. /
*Both installed Intake Authoring validators additionally process all nine RAW
Receipts in stable name order. The named requirements and acceptance criteria
bind inventory, ownership, re-entry, content, RF coverage, the META-LH-04
contract, cross-platform parity, and semantic review.*

## Revision und Nicht-Autorität / Revision and non-authority

Revision ist bei Source-, RF-, Portfolio-, Coverage-, Decision-, Target-,
Receipt-, Series-, Modus-, Plattform- oder Supply-Chain-Drift erforderlich.
Dieses Lastenheft erteilt keine aktuelle Authority für Create, Adopt,
Supersede, Repair, Update, Review-Akzeptanz, Specify, Autonomous,
Implementierung, Remote Write, Merge, Bypass, Hardware oder Preset-Promotion.
/ *Revision is required for drift in sources, RFs, portfolio, coverage,
decisions, targets, Receipts, Series, mode, platform, or supply chain. This
intake grants no current authority for create, adopt, supersede, repair,
update, review acceptance, Specify, Autonomous, implementation, remote write,
merge, bypass, hardware, or preset promotion.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung den nachgelagerten Scope, Target Writes, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. Eligibility, Ready und historische Receipt-Autorität reichen nicht aus; Provider-Administration bleibt ausgeschlossen. / Do not start unless a separate current user decision explicitly authorises downstream scope, target writes, implementation, remote writes, merge, and bypass. Eligibility, Ready, and historic receipt authority are insufficient; provider administration remains excluded.
```
<!-- intake-authoring:end -->
