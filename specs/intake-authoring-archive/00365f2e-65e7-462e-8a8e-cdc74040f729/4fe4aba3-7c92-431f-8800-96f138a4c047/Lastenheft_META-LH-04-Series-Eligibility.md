<!-- intake-authoring:begin -->
# META-LH-04 – Series-Planung, Eligibility und kontrollierte Parallelität / Series Planning, Eligibility, and Controlled Parallelism

**Status:** ReadyForReview
**Zielgruppe / Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IT apprentices and experienced professionals
**Vorkenntnisse / Assumed prior knowledge:** Git-Branch-Grundlagen; keine autonome Laufpraxis / basic Git branches; no autonomous-run experience
**Profil / Profile:** `aoc-bilingual-requirements`

## Zweck / Purpose

Dieses Lastenheft definiert, wie eine Intake-Serie als prüfbarer gerichteter
Graph ohne Zyklus (Directed Acyclic Graph, DAG) geplant wird, wie startfähige
Kandidaten ermittelt werden und wie ihre zulässige Autonomiestufe ohne
Ausführung klassifiziert wird. / *This intake defines how an intake series is
planned as a verifiable directed acyclic graph (DAG), how eligible candidates
are identified, and how their permitted autonomy level is classified without
starting execution.*

## Quellen und Findings / Sources and findings

Verbindliche Quellen sind SRC-159, SRC-174 und SRC-180 bis SRC-182 aus dem
AOC-Quellenpaket sowie RF-02, RF-09, RF-18 und RF-19. Der ausführbare
Eligibility-Vertrag steht in `requirements/baseline/series-eligibility-contract.json`.
/ *Binding sources are SRC-159, SRC-174, and SRC-180 through SRC-182 from the
AOC source pack, plus RF-02, RF-09, RF-18, and RF-19. The executable
eligibility contract is stored in the named baseline file.*

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Eingaben sind reviewfähige Intakes, aktuelle Ownership-Zuordnungen und
dokumentierte Decisions. Ausgaben sind ein per SHA-256 gebundenes
Series-Manifest, typisierte Kanten, explizite Wurzeln, eine stabile Reihenfolge,
Lifecycle-Werte, Eligibility-Ergebnisse, Stop-/Recovery-Regeln und ein Receipt.
SHA-256 ist hier der Prüfsummenalgorithmus für unveränderte Dateibindung;
Lifecycle bezeichnet den erklärten Zustand eines Serienmitglieds. / *Inputs are
reviewable intakes, current ownership assignments, and documented decisions.
Outputs are a SHA-256-bound series manifest, typed edges, explicit roots, a
stable order, lifecycle values, eligibility results, stop/recovery rules, and
a receipt. SHA-256 is the checksum algorithm used for immutable file binding;
lifecycle is the declared state of a series member.*

Nicht im Scope sind Workerstart, Worktree-Erzeugung, Produktänderung, Specify,
Implementierung, Remote Write, Merge, Bypass, Provider-Administration oder
Preset-Promotion. / *Worker start, worktree creation, product changes, Specify,
implementation, remote writes, merge, bypass, provider administration, and
preset promotion are out of scope.*

## Begriffe / Terms

Ein Side Effect ist eine Zustandsänderung außerhalb reiner Analyse.
Reversibilität beschreibt, ob sie kontrolliert zurückgenommen werden kann.
Write Scope ist die Menge veränderbarer Pfade oder Ressourcen. Eine Shared
Decision ist eine offene materielle Entscheidung, die mehrere Kandidaten
beeinflusst. Ein Consolidation Review prüft getrennte Ergebnisse vor ihrer
Integration. Fail-closed bedeutet: fehlende oder widersprüchliche Evidence
führt zu `Blocked`, nicht zu einer angenommenen Freigabe. Eine Fixture ist ein
reproduzierbarer Testdatensatz. / *A side effect is a state change beyond
read-only analysis. Reversibility states whether it can be undone safely.
Write scope is the set of paths or resources that may change. A shared
decision is an open material decision affecting multiple candidates. A
consolidation review checks separate results before integration. Fail-closed
means missing or conflicting evidence produces `Blocked`, never assumed
permission. A fixture is a reproducible test data set.*

`ProviderFailure` bezeichnet den Ausfall eines externen Dienstes oder Runners;
`ProductFailure` bezeichnet einen Fehler des geprüften Produkts oder Artefakts.
Beide Klassen dürfen nicht vertauscht werden. / *`ProviderFailure` means an
external service or runner failed; `ProductFailure` means the reviewed product
or artifact failed. The classes must not be substituted for each other.*

## Trust- und Authority-Grenzen / Trust and authority boundaries

`Eligible`, ein gespeicherter Delivery-Modus und ein aktuelles Review sind
getrennte Achsen. Keine davon ist allein Startautorität. Jeder Runner,
Worktree, Remote Write, Merge oder Bypass benötigt einen separaten, aktuellen
und ausdrücklich passenden Auftrag. Historische Receipt-Autorität ist nur
Provenienz. Fehlt aktuelle Autorität, ist das Ergebnis fail-closed `Blocked`.
/ *`Eligible`, a stored delivery mode, and a current review are separate axes.
None alone grants start authority. Every runner, worktree, remote write, merge,
or bypass requires a separate, current, explicitly matching instruction.
Historic receipt authority is provenance only. Without current authority, the
fail-closed outcome is `Blocked`.*

## Aktueller Serienkontext / Current series context

Im gebundenen Manifest sind META-LH-01 bis META-LH-03 `Completed` und
META-LH-04 ist der einzige deklarierte `Eligible`-Kandidat. RAW-05 bleibt
`Pending` und auf read-only Research beschränkt. Für META-LH-04 ist keine
materielle Decision offen. Die einzige nächste zulässige Aktion dieses
Authoring-Schritts ist ein vollständiges Single Review; es startet keine
Folgearbeit. / *In the bound manifest, META-LH-01 through META-LH-03 are
`Completed`, and META-LH-04 is the sole declared `Eligible` candidate. RAW-05
remains `Pending` and limited to read-only research. No material decision is
open for META-LH-04. The only next action permitted by this authoring step is
a complete Single review; it starts no downstream work.*

## Anforderungen / Requirements

- **FR-001:** Der Modus MUSS genau einer der Klassen `manual-assisted`,
  `single-autonomous`, `serial-autonomous`, `parallel-autonomous`,
  `research-only` oder `blocked` entsprechen. / *The mode MUST be exactly one
  of the six named classes.*
- **FR-002:** Jede Einstufung MUSS genau neun Kriterien vollständig enthalten:
  Authority, Side Effects, Reversibilität, Write Scope, Decisions,
  Integration, Review, Abort und Recovery. / *Every classification MUST fully
  provide exactly nine criteria: authority, side effects, reversibility, write
  scope, decisions, integration, review, abort, and recovery.*
- **FR-003:** `parallel-autonomous` ist nur mit aktueller Authority, disjunkten
  Writes, ohne gemeinsame offene Decisions, mit geplantem Consolidation
  Review sowie definierten Abort- und Recovery-Regeln zulässig. Sonst MUSS das
  Ergebnis `Blocked` sein. / *`parallel-autonomous` is allowed only with
  current authority, disjoint writes, no shared open decisions, a planned
  consolidation review, and defined abort and recovery rules. Otherwise the
  outcome MUST be `Blocked`.*
- **FR-004:** Das Manifest MUSS normalisierte SHA-256-Hashes, explizite Roots,
  die exakte Reihenfolge, Lifecycle-Werte und typisierte Kanten binden. / *The
  manifest MUST bind normalized SHA-256 hashes, explicit roots, exact order,
  lifecycle values, and typed edges.*
- **FR-005:** Zyklus, Hash-Drift, fehlende Root, mehrfach deklarierte
  Eligibility, unvollständige Kriterien oder fehlende Authority MÜSSEN
  fail-closed blockieren. / *A cycle, hash drift, missing root, multiple
  declared eligibility, incomplete criteria, or missing authority MUST block
  fail-closed.*
- **FR-006:** Status- und Next-Abfragen MÜSSEN read-only bleiben und dürfen
  keine Folgeaktion starten. / *Status and next queries MUST remain read-only
  and must not start downstream action.*
- **NFR-001:** Status, Gründe und nächste Aktion MÜSSEN als Text verfügbar und
  ohne Farbe verständlich sein. / *Status, reasons, and next action MUST be
  available as text and understandable without colour.*
- **NFR-002:** Normative DE/EN-Inhalte MÜSSEN paarig, Deutsch zuerst und
  Englisch danach auf CEFR-B2-Niveau vorliegen. / *Normative DE/EN content MUST
  be paired, German first and English second, at CEFR B2.*

## Cross-Cutting-Anwendbarkeit / Cross-cutting applicability

- **Sicherheit / Security:** Anwendbar auf Authority-, Pfad- und
  Hash-Metadaten. Secrets, Tokens und ausführbare Remote-Befehle sind verboten;
  unsichere Evidence blockiert. / *Applicable to authority, path, and hash
  metadata. Secrets, tokens, and executable remote commands are forbidden;
  unsafe evidence blocks.*
- **Privacy und personenbezogene Daten / Privacy and personal data:** Für die
  Eligibility-Entscheidung nicht erforderlich. Fixtures dürfen keine
  personenbezogenen Daten enthalten; Auftreten löst Stop und Re-Evaluation
  aus. / *Not required for eligibility decisions. Fixtures must contain no
  personal data; discovery triggers stop and re-evaluation.*
- **Öffentliche Inhalte / Public content:** Nicht anwendbar; die Artefakte sind
  interne Repository-Evidence. Eine Veröffentlichung benötigt eine separate
  Entscheidung. / *Not applicable; artifacts are internal repository evidence.
  Publication requires a separate decision.*
- **Barrierefreiheit / Accessibility:** Text-first, farbunabhängig, stabile
  Überschriften und WCAG 2.2 AA, soweit auf Markdown und CLI-Ausgaben
  anwendbar. / *Text-first, colour-independent, stable headings, and WCAG 2.2
  AA where applicable to Markdown and CLI output.*
- **Plattformen / Platforms:** Bash und PowerShell müssen auf macOS, Linux und
  Windows semantisch gleich entscheiden; fehlende Laufzeitparität blockiert.
  / *Bash and PowerShell must decide equivalently across macOS, Linux, and
  Windows; missing runtime parity blocks.*
- **Supply Chain:** Es werden keine neuen Abhängigkeiten eingeführt; verwendet
  werden nur vorhandene Bash-, PowerShell- und Python-Laufzeiten. Eine neue
  Abhängigkeit löst Re-Evaluation aus. / *No new dependency is introduced;
  only existing Bash, PowerShell, and Python runtimes are used. A new
  dependency triggers re-evaluation.*

## Dependencies und Risiken / Dependencies and risks

META-LH-01, META-LH-02 und META-LH-03 sind verpflichtende Vorgänger. Die
fachliche Einstufung dieses Lastenhefts bleibt `manual-assisted`, weil
Parallelfreigaben materielle Authority-Entscheidungen sind. Hauptrisiko ist
falsche Parallelität auf gemeinsamen Schemas oder Decisions. Recovery:
Worker nicht starten beziehungsweise stoppen, keinen Teilmerge durchführen,
Manifest und Eligibility erneut prüfen. / *META-LH-01, META-LH-02, and
META-LH-03 are mandatory predecessors. This intake remains `manual-assisted`
because parallel approval is a material authority decision. The primary risk
is incorrect parallelism across shared schemas or decisions. Recovery: do not
start, or stop, workers; perform no partial merge; validate the manifest and
eligibility again.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Die Series-Validatoren bestehen in Bash und PowerShell und prüfen
  Root, Reihenfolge, Kanten, Lifecycle und Hashbindung. / *The series
  validators pass in Bash and PowerShell and check roots, order, edges,
  lifecycle, and hash binding.*
- **AC-002:** Die vorhandene Sequencing-Suite blockiert Cycle-, Hash-Drift-,
  Missing-Root- und Multiple-Eligible-Fälle. Die gebundenen META-LH-04-Fixtures
  berechnen `Eligible` für `valid-parallel.json` und `Blocked` für
  `shared-write.json` sowie `shared-decision.json`; alle Befehle enden bei
  korrektem erwarteten Ergebnis mit Exitcode 0. / *The existing sequencing
  suite blocks cycle, hash-drift, missing-root, and multiple-eligible cases.
  The bound META-LH-04 fixtures calculate `Eligible` for the valid fixture and
  `Blocked` for both negative fixtures; every command exits zero when the
  expected result is reproduced.*
- **AC-003:** Jede Fixture und jede künftige Einstufung enthält genau die neun
  Kriterien aus FR-002; keine Acht-Kriterien-Variante ist zulässig. / *Every
  fixture and future classification contains exactly the nine criteria from
  FR-002; no eight-criterion variant is allowed.*
- **AC-004:** `next` meldet ausschließlich Kandidat oder konkrete Blocker und
  startet keine Arbeit. / *`next` reports only a candidate or concrete blockers
  and starts no work.*
- **AC-005:** Semantisches Review bestätigt den DE/EN-, Terminologie-,
  Authority- und Cross-Cutting-Vertrag ohne Scope-Erweiterung. / *Semantic
  review confirms the language, terminology, authority, and cross-cutting
  contract without expanding scope.*

## Reproduzierbare Evidence / Reproducible evidence

Die folgenden Befehle und Exitcodes sind verbindlich. Jeder Befehl MUSS mit 0
enden; die negativen Fixtures sind erfolgreich, wenn sie den Textstatus
`Blocked` reproduzieren. / *The following commands and exit codes are binding.
Every command MUST exit zero; a negative fixture succeeds when it reproduces
the textual `Blocked` status.*

```text
bash .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.sh --file specs/intake-series/aoc-phase-2/manifest.json --repo .
pwsh -NoProfile -File .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.ps1 -File specs/intake-series/aoc-phase-2/manifest.json -Repo .
pwsh -NoProfile -File .specify/presets/intake-sequencing-governance/tests/test-intake-sequencing-validator.ps1
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/valid-parallel.json
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/shared-write.json
bash specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.sh specs/intake-review-fixtures/meta-lh-04/shared-decision.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/valid-parallel.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/shared-write.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.ps1 -Fixture specs/intake-review-fixtures/meta-lh-04/shared-decision.json
```

Die Matrix bindet FR-002 und AC-003. Die drei Eligibility-Fixtures binden
FR-003 und AC-002. Die installierte Sequencing-Suite bindet FR-004, FR-005,
AC-001 und den Cycle-Negativfall aus AC-002. Semantisches Single Review bindet
FR-006, NFR-001, NFR-002, AC-004 und AC-005. / *The matrix binds FR-002 and
AC-003. The three eligibility fixtures bind FR-003 and AC-002. The installed
sequencing suite binds FR-004, FR-005, AC-001, and AC-002's cycle case.
Semantic Single review binds FR-006, NFR-001, NFR-002, AC-004, and AC-005.*

## Revision und Nicht-Autorität / Revision and non-authority

Revision ist bei Intake-Hash-, Decision-, Edge-, Root-, Governance-, Fixture-,
Plattform- oder Supply-Chain-Drift erforderlich. Dieses Lastenheft erteilt
keine aktuelle Autorität für Workerstart, Worktree, Specify, Autonomous,
Implementierung, Remote Write, Merge, Bypass, Provider-Administration oder
Preset-Promotion. / *Revision is required for drift in an intake hash,
decision, edge, root, governance rule, fixture, platform, or supply chain.
This intake grants no current authority for worker start, worktree, Specify,
Autonomous, implementation, remote write, merge, bypass, provider
administration, or preset promotion.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung den nachgelagerten Scope, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. Eligibility, Modus, Review und historische Receipt-Autorität reichen nicht aus; Provider-Administration bleibt ausgeschlossen. / Do not start unless a separate current user decision explicitly authorises downstream scope, implementation, remote writes, merge, and bypass. Eligibility, mode, review, and historic receipt authority are insufficient; provider administration remains excluded.
```
<!-- intake-authoring:end -->
