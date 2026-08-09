# Datenmodell: Programmquellen-Baseline / Data Model: Program Sources Baseline

## Zweck / Purpose

Dieses logische Modell beschreibt die bereits vorhandenen Markdown-Entitaeten und ihre Validierungsregeln. Es fuehrt keine Datenbank, Runtime, Schema-Migration oder Produktklasse ein. / This logical model describes existing Markdown entities and their validation rules. It introduces no database, runtime, schema migration, or product class.

## Entitaet: Programmquelle / Entity: Programme Source

| Feld / Field | Regel / Rule |
|---|---|
| `sourceId` | Genau eine ID aus der 23-teiligen zugelassenen Menge im Validierungsvertrag. / Exactly one ID from the permitted 23-item set in the validation contract. |
| `role` | Fachliche Rolle der Quelle; DE zuerst, EN danach. / Domain role; German first, English second. |
| `contentDescription` | Eigenstaendige Inhaltsbeschreibung ohne notwendige Level-0-Lektuere. / Self-contained description without required level-0 reading. |
| `authority` | Expliziter Rang oder belegte Nicht-Autoritaet. / Explicit precedence or evidenced non-authority. |
| `currency` | Aktuell, historisch, Field Evidence oder andere nachvollziehbare Aktualitaet. / Current, historical, field evidence, or another traceable currency state. |
| `supersessionStatus` | Explizite Ablösung, Praezisierung, Provenienz-only oder keine Ablösung. Neueres Datum allein reicht nicht. / Explicit supersession, refinement, provenance-only, or no supersession. Newer date alone is insufficient. |
| `targetUse` | Repository- oder Owner-Ziel ohne implizite Produktautoritaet. / Repository or ownership target without implied product authority. |

**Beziehungen / Relationships**: Eine Programmquelle hat mindestens eine Coverage-Zuordnung; sie kann Decisions oder Supersession-Evidence begruenden. / A programme source has at least one coverage mapping and may support decisions or supersession evidence.

## Entitaet: Prueffeststellung / Entity: Review Finding

| Feld / Field | Regel / Rule |
|---|---|
| `findingId` | Genau eine ID `RF-01` bis `RF-21`. / Exactly one ID from `RF-01` through `RF-21`. |
| `severity` | Vorhandener nachvollziehbarer Severity-Wert; blocking bleibt textlich sichtbar. / Existing traceable severity; blocking remains textually visible. |
| `statementAndSource` | Praezise Aussage und Quelle, DE/EN. / Precise statement and source, German/English. |
| `ownerAndTarget` | Genau benannte Meta-/Fach-Owner und Zielartefakte. / Explicit meta/domain owners and targets. |
| `acceptanceCriterion` | Messbares oder eindeutig reviewbares Ergebnis. / Measurable or unambiguously reviewable outcome. |
| `positiveEvidence` | Bestandener Nachweis und erwartete Aussage. / Passing evidence and expected statement. |
| `negativeEvidence` | Gegenbeispiel oder fail-closed Fehlerfall. / Counterexample or fail-closed failure case. |
| `coverageStatus` | Fuer diese Baseline `Covered`; nie `Uncovered` bei blocking. / `Covered` for this baseline; never `Uncovered` for a blocking finding. |
| `residualGap` | Restluecke oder begruendetes `N/A`; `Covered` behauptet keine Implementierung. / Residual gap or justified `N/A`; `Covered` does not claim implementation. |

**Beziehungen / Relationships**: Jedes Finding besitzt genau eine Einzelzeile im Ledger und genau eine Einzelzeile in der Coverage Matrix. / Every finding has exactly one individual row in the ledger and one in the coverage matrix.

## Entitaet: Verbindliche Vorgabe / Entity: Constraint

| Feld / Field | Regel / Rule |
|---|---|
| `constraintId` | Bestehende stabile ID `CON-01` bis `CON-25`. / Existing stable ID from `CON-01` through `CON-25`. |
| `bindingStatement` | Verbindliche Anforderung, DE zuerst und EN danach. / Binding requirement, German first and English second. |
| `applicabilityAndEvidence` | Geltung, Evidence-Pfad oder Pruefart sowie Neubewertung bei phasenbezogenem `N/A`. / Applicability, evidence path or review method, and re-evaluation for phase-specific `N/A`. |

## Entitaet: Decision und Supersession / Entity: Decision and Supersession

| Feld / Field | Regel / Rule |
|---|---|
| `decisionId` | Stabile vorhandene ID, zum Beispiel `DEC-001`. / Existing stable ID, for example `DEC-001`. |
| `status` | `Confirmed` oder `Open`; nie implizit aus Datum oder Kommentar. / `Confirmed` or `Open`; never inferred from date or comments. |
| `statement` | Bestaetigte Festlegung oder offene Frage. / Confirmed choice or open question. |
| `revisionReason` | Pflicht, wenn Authority oder eine fruehere Decision geaendert wird. / Required when authority or an earlier decision changes. |
| `supersedes` | Explizite Vorgaengerquelle/-Decision oder `N/A`. / Explicit predecessor source/decision or `N/A`. |

**Zustandsuebergang / State transition**: `Open -> Confirmed` nur durch menschlich bestaetigte Decision; `Confirmed -> Superseded` nur durch neue bestaetigte Decision mit Revisionsgrund. / `Open -> Confirmed` only through a human-confirmed decision; `Confirmed -> Superseded` only through a new confirmed decision with a revision reason.

## Entitaet: Coverage-Zuordnung / Entity: Coverage Mapping

| Feld / Field | Regel / Rule |
|---|---|
| `subjectId` | Genau eine Source-ID oder Finding-ID; keine Bereichszeile als Ersatz. / Exactly one source or finding ID; no range row as a substitute. |
| `metaOwner` | Explizites Meta-Lastenheft oder begruendete Menge. / Explicit meta intake or justified set. |
| `domainOwnerSeries` | Explizite fachliche Owner-Reihe(n). / Explicit domain owner series or series. |
| `coverageStatus` | `Covered` oder `Uncovered`; diese Baseline darf kein blocking `Uncovered` enthalten. / `Covered` or `Uncovered`; this baseline may contain no blocking `Uncovered`. |
| `directMetaLh01` | `Yes` exakt fuer `RF-01`, `RF-04`, `RF-11`, `RF-12`, `RF-13`, `RF-14`, `RF-15`, `RF-16`, `RF-17`, `RF-21`; sonst `No`. / `Yes` exactly for the listed ten findings; otherwise `No`. |

## Entitaet: Authority- oder Stop-Gate / Entity: Authority or Stop Gate

| Feld / Field | Regel / Rule |
|---|---|
| `gateId` | Bestehende ID `G-00` bis `G-08`. / Existing ID from `G-00` through `G-08`. |
| `allowedAction` | Engste erlaubte Aktion; erzeugt keine implizite Folgeautoritaet. / Narrowest permitted action; creates no implied downstream authority. |
| `stopCondition` | Fail-closed Bedingung bei fehlender, veralteter oder widerspruechlicher Evidence. / Fail-closed condition for missing, stale, or contradictory evidence. |
| `requiredEvidence` | Konkrete Pfade, Hashes, Reviews, Validatoren oder Gates. / Concrete paths, hashes, reviews, validators, or gates. |
| `humanDecision` | Getrennte menschliche Start-, Implementierungs-, Remote- oder Promotion-Entscheidung. / Separate human start, implementation, remote, or promotion decision. |
| `nextSafeAction` | Genau eine Aktion oder `Stop`, vollstaendig als Text. / Exactly one action or `Stop`, fully represented as text. |

**Relevante Zustaende / Relevant states**:

- `G-01`: offen bis exakte Quellen- und Findings-Baseline mit Review-Evidence besteht. / Open until the exact source and finding baseline passes review evidence.
- `G-05`: fail-closed bei irgendeiner Drift der 14 Ready-Single-Reviews; nach Erfuellung braucht META-LH-01 einen separaten Startauftrag. / Fail closed on any drift across the fourteen Ready Single reviews; after fulfilment META-LH-01 needs a separate start instruction.
- `G-06`: getrennt von G-05; fuer dieses Feature nur dokumentarische Umsetzung gemaess Spec/Plan/Tasks, nie Produktcode oder Produktarchitektur. / Separate from G-05; for this feature it permits only documentation implementation under spec, plan, and tasks, never product code or architecture.

## Entitaet: Evidence-Datensatz / Entity: Evidence Record

| Feld / Field | Regel / Rule |
|---|---|
| `evidenceType` | Hash-Bindung, Validatorausgabe, semantischer Review, Documentation Impact, AEPS Receipt, Statistik, exact-head Gate-Evidence oder Causal Closeout. / Hash binding, validator output, semantic review, documentation impact, AEPS receipt, statistics, exact-head gate evidence, or causal closeout. |
| `pathOrReference` | Repository-relativer Pfad oder unveraenderliche Remote-Referenz. / Repository-relative path or immutable remote reference. |
| `result` | `Pass`, `Fail`, `N/A` mit Begruendung oder definierter Domainstatus. / `Pass`, `Fail`, justified `N/A`, or defined domain status. |
| `owner` | Verantwortliche Rolle. / Responsible role. |
| `reviewer` | Unabhaengige pruefende Rolle, wo erforderlich. / Independent reviewing role where required. |
| `reevaluationTrigger` | Hash-, Scope-, Authority-, Inhalts-, Plattform- oder Evidence-Drift. / Hash, scope, authority, content, platform, or evidence drift. |

### Strukturierte unabhaengige Review-Evidence / Structured independent review evidence

- `reviewer.independent` ist `true`; Rolle und Unabhaengigkeitserklaerung sind nicht leer. / The reviewer is explicitly independent and names role and independence statement.
- `semanticReviews` enthaelt genau eine Zeile je gebundenem Domain-Pfad plus `causal-closeout-evidence.json` und getrennte Kriterien fuer DE/EN, CEFR B2, Erstnutzungsbegriffe, fachliche Wahrheit und Authority-Auslegung. / Semantic reviews cover each domain path plus the readable causal-closeout anchor.
- `accessibilityReviews` enthaelt getrennt genau eine Zeile je Domain-Pfad plus `causal-closeout-evidence.json` fuer Heading-Hierarchie beziehungsweise strukturierte Lesereihenfolge, beschreibende Felder, Text-first, Status ohne Nur-Farbe und WCAG-2.2-AA-Anwendbarkeit; die Reviewer-Rolle ist ausdruecklich A11Y-unabhaengig. / Accessibility reviews cover each domain path plus the readable causal-closeout anchor with their own zero-blocking boundary.
- `publicContentReviews` enthaelt genau eine Zeile je Pfad der eingefrorenen normalen Kandidatenliste plus Lifecycle-Datensatz, Original- und Archivpfad und getrennte Kriterien fuer Secret-Muster, private Pfade, unnoetige Personendaten und Publikationseignung. / Public-content reviews cover every frozen normal-candidate path plus the lifecycle record and both rename paths with separate criteria.
- Der Validator beweist Vollstaendigkeit, `Pass`-/`Fail`-Werte und Begruendungen. Er beweist nicht selbst die semantische Wahrheit. / The validator proves completeness, values, and rationales, not semantic truth itself.

## Entitaet: Globaler Ready-Nachweis / Entity: Global Ready Evidence

| Feld / Field | Regel / Rule |
|---|---|
| `logicalTarget` | Exakt eines der 14 logischen META-/RAW-Lastenhefte; META-LH-01 ist das erste Ziel. / Exactly one of the fourteen logical targets; META-LH-01 is first. |
| `physicalPath` | Fuer unaufgeloeste Ziele der Originalpfad; fuer abgeschlossenes META-LH-01 ausschliesslich der durch den eindeutigen Lifecycle-Datensatz validierte Archivpfad. / The original path for unresolved targets; for completed META-LH-01 only the archive path proven by the unique lifecycle record. |
| `targetNormalizedSha256` | Aktueller normalisierter Datei-Hash. / Current normalized file hash. |
| `receiptPath` | Genau ein aktuelles Authoring Receipt mit gleichem Ziel und Hash. / Exactly one current receipt with the same target and hash. |
| `reviewPath` | Genau ein nicht-supersedierter `Ready`-Leaf im Modus `Single`, ohne Findings, Fragen oder Risiken. / Exactly one non-superseded Ready Single leaf without findings, questions, or risks. |
| `validatorSurfaces` | Vor Implement bestehen Receipt und Review jeweils Bash und PowerShell. Im exakt qualifizierten Implement-Zustand ersetzt der vollstaendige Snapshot nur die Receipt-Quellenfrische; beide installierten Review-Oberflaechen und beide Input-Binding-Run-State-Oberflaechen bleiben verpflichtend. / Before Implement, receipt and review each pass Bash and PowerShell. In the exact qualified Implement state, the complete snapshot replaces only receipt source freshness; both review and run-state surfaces remain mandatory. |

Der Nachweis wird vor Tasks, jedem Analyze-Lauf und Implement sowie nach terminalem Rename auf dem synchronisierten Default-Branch neu erzeugt. Fehlende oder gleichzeitig vorhandene Pfade, falscher Branch-Stempel, Hash-Drift, stale Evidence oder Mehrdeutigkeit fuehren zu `Stop`. / The evidence is regenerated at every named boundary and after terminal archival; any missing, simultaneous, wrongly stamped, drifted, stale, or ambiguous state results in `Stop`.

## Entitaet: Lifecycle-Datensatz und Programmevidence-Snapshot / Entity: Lifecycle Record and Programme Evidence Snapshot

`specs/001-programmquellen-baseline/intake-lifecycle.json` verwendet Schema 1.1. Es bewahrt genau einen `recordVersion: 1.0`-Datensatz unveraendert und enthaelt genau einen `programmeEvidenceSnapshot`. / The lifecycle file uses schema 1.1, preserves exactly one recordVersion-1.0 record unchanged, and contains exactly one programmeEvidenceSnapshot.

| Feld / Field | Regel / Rule |
|---|---|
| `recordVersion`, `logicalTargetId` | Exakt `1.0` und `META-LH-01`. / Exactly `1.0` and `META-LH-01`. |
| `originalPath` | Exakt der akzeptierte aktive Originalpfad. / Exactly the accepted active original path. |
| `archivedPath` | Exakt derselbe Stamm mit Suffix `.001-programmquellen-baseline.md`; aus dem gebundenen Branch deterministisch ableitbar. / Exactly the same stem with the bound branch suffix. |
| `originalRawSha256`, `originalNormalizedSha256` | Hashes der akzeptierten bytes und des normalisierten UTF-8-Inhalts; beide muessen am jeweils existierenden physischen Pfad bestehen. / Hashes of accepted bytes and normalized content, valid at the one existing physical path. |
| `authoringReceipt`, `readySingleReview` | Jeweils akzeptierter Pfad und roher SHA-256; beide Artefakte bleiben unveraendert auf das originale logische Ziel und dessen normalisierten Hash gebunden. / Accepted path and raw SHA-256 for each immutable evidence artefact, still bound to the original logical target. |
| `runId`, `branch` | Exakt gleich dem schema-1.1-Run-State. / Exactly equal to schema-1.1 run state. |

Der `programmeEvidenceSnapshot` besitzt exakt `snapshotVersion`, `runId`, `branch` und `orderedLogicalTargets`. Die Liste enthaelt exakt 14 eindeutige Ziele in der kanonischen Reihenfolge META-LH-01 bis META-LH-05, danach RAW-01 bis RAW-09. Jeder Eintrag besitzt exakt `logicalTargetId`, `target { path, normalizedSha256 }`, `authoringReceipt { path, rawSha256 }` und `readySingleReview { path, rawSha256 }`. Alle Hashes sind lowercase SHA-256. Zielbytes/-hash, unveraenderte Receipt-/Review-Bytes, Receipt `ReadyForReview`, Review `Single`/`Primary`/`Ready`, leere Findings/Fragen/Risiken und eindeutige aktuelle Leaves muessen bestehen. / The snapshot has an exact four-field shape and fourteen ordered entries. Every target, immutable receipt, Ready Single review, empty blocker set, unique leaf, and lowercase hash must validate.

**Zustandsuebergaenge / State transitions**:

1. `Active`: Original existiert, Archiv fehlt; beide Hashformen stimmen. / Original exists, archive is absent, and both hashes match.
2. `Archived`: Original fehlt, exakter Archivpfad existiert; bytes und normalisierter Inhalt stimmen weiterhin, Receipt und Review bleiben immutable Evidence. / Original is absent, exact archive exists, hashes still match, and receipt/review remain immutable evidence.
3. Jeder andere Zustand ist ungueltig. Der Datensatz enthaelt absichtlich keinen SHA des Commits, der ihn selbst enthaelt. / Every other state is invalid. The record intentionally contains no SHA of the commit containing itself.

**Phasenqualifikation / Phase qualification**: `stage == Implement`, `status == Active`, `lastPassingGate == GlobalReadyBeforeImplement`, aktuelle Git-Branch-/Run-/Lifecycle-Bindungen und ein vollstaendig gueltiger Snapshot sind gemeinsam erforderlich. Fehlt eine Bedingung, gilt wieder die generische Receipt-Quellenfrische; wegen echter Shared-Source-Drift schliesst sie fail-closed. / The exact stage, status, last gate, current branch/run/lifecycle bindings, and complete snapshot are jointly required. Otherwise generic receipt source freshness applies and fails closed on real shared-source drift.

## Entitaet: Lieferkandidat / Entity: Delivery Candidate

| Feld / Field | Regel / Rule |
|---|---|
| `maximumAllowlist` | Feature-lokaler Vertrag `contracts/candidate-paths.json`; keine pauschale Verzeichnisfreigabe. / Feature-local maximum contract, not a directory-wide permission. |
| `expectedPaths` | Vor dem Staging erzeugte, reviewte und fuer den Lauf eingefrorene exakte Teilmenge. / Exact reviewed subset frozen before staging. |
| `fixedPoint` | Nach Erzeugung aller Pfadanker werden Sollmenge eins und zwei bytegleich verglichen; `candidate-fixpoint` bindet dieselbe Worktree-Menge. / Candidate sets one and two must be byte-identical and match the worktree. |
| `porcelainStatus` | Maschinenlesbare staged, unstaged und untracked Zustaende; fremde unstaged Pfade bleiben unberuehrt. / Machine-readable states; unrelated unstaged paths remain untouched. |
| `stagedPaths` | Exakt gleich `expectedPaths`; kein zusaetzlicher oder fehlender Pfad. / Exactly equal to expected paths. |
| `whitespaceResult` | `git diff --cached --check` besteht. / The staged whitespace check passes. |
| `terminalRename` | Nach dem normalen Kandidaten-Commit genau ein byteidentischer `R100`-Rename vom Original- zum Archivpfad; vom Script als letzter Feature-Branch-Commit erzeugt und mit `terminal-rename` validiert. / After the normal candidate commit, exactly one byte-identical R100 rename created by the script as the final branch commit. |

## Entitaet: Kausaler Closeout-Datensatz / Entity: Causal Closeout Record

`causal-closeout-evidence.json` ist im normalen Feature-Kandidaten bereits mit `status: Pending` vorhanden. Nur die spaetere Closeout-Transaktion setzt ihn auf `Completed`. / The causal evidence anchor is already present as Pending in the normal feature candidate and is completed only by the later closeout transaction.

| Feld / Field | Regel / Rule |
|---|---|
| `runId`, `closeoutBranch` | Exakte Run-ID und `codex/001-programmquellen-baseline-closeout`. / Exact run ID and pre-named branch. |
| `closeoutPaths` | Exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`. / Exactly the three permitted paths. |
| `terminalFeatureHead`, `featurePullRequest`, `featureMergeSha`, `synchronizedMainSha` | Nur tatsaechliche, bereits bestehende Feature-PR-/Merge-/Sync-Fakten. / Only actual prior feature delivery facts. |
| `commands` | Exakte Command-/Result-Menge fuer Merge, Sync, Post-Merge, archivbewusste Gates, beide State-Validatoren, Task-Hash und Diff-Check. / Exact command/result inventory. |
| `documentationReview`, `publicContentReview` | Unabhaengige, vollstaendige Re-Reviews des exakten Drei-Pfad-Deltas mit null blocking Findings. / Independent complete re-reviews of the exact three-path delta. |
| `nonSelfReferentialBoundary` | `containingCommitSha`, `closeoutPullRequest` und `closeoutMergeSha` bleiben `N/A`; die spaetere Publikation wird extern berichtet. / Self-publication fields remain N/A and are reported externally. |

**Zustandsuebergaenge / State transitions**:

1. `Pending`: im normalen Feature-Head reviewter Pfadanker ohne Zukunftsbehauptung. / Pre-reviewed anchor with no future claim.
2. `Completed`: erst nach Feature-Merge, Fast-forward-Sync und bestandener Archivvalidierung; gleichzeitig sind alle T001-T066 geprueft, State `66/66`, Task-Hash real und Closeout terminal. / Only after actual merge, sync, and archive-aware validation, with 66/66 and terminal state.
3. Der einzelne Closeout-Commit ist der letzte lokale Akt von T066; spaetere Publikationsmechanik aendert ihn nicht. / The one closeout commit is T066's last local act and later publication does not mutate it.

## Entitaet: Documentation Impact und AEPS-Ausgang / Entity: Documentation Impact and AEPS Outcome

- Documentation Impact verwendet Schema 1.1, genau einen `UpdateRequired`-Eintrag und das Ready-gepruefte originale META-LH-01 als einzige logische kanonische fachliche Quelle. `documents` entspricht der eingefrorenen normalen Kandidatenliste einschliesslich Pending-Closeout-Anker plus Lifecycle-Datensatz sowie Original- und Archivpfad. Der spaetere Drei-Pfad-Delta erhaelt einen Re-Review, aber keine zweite Decision. / Documentation Impact covers the Pending closeout anchor and later re-reviews the exact three-path delta without a second decision.
- Der AEPS-Receipt enthaelt genau einen `aeps-outcome-json`-Block mit `Finding` oder `NoChange`, nie beides. Er bindet Quelle, Hash, Deduplizierung, Begruendung, maximal `candidate` sowie `presetPromotion: false` und `level0Handoff: false`. / The AEPS receipt contains exactly one bounded outcome block and no promotion or level-0 handoff claim.

## Globale Validierungsregeln / Global Validation Rules

1. Alle IDs entsprechen exakt den Mengen im [Validierungsvertrag](contracts/baseline-validation-contract.md). / All IDs exactly match the contract sets.
2. Jede Entity-Zeile besitzt alle Pflichtfelder und eine gleichwertige DE/EN-Aussage. / Every entity row has all required fields and equivalent German/English content.
3. Kein `Covered`-Status behauptet Produktimplementierung oder Wirksamkeit. / No `Covered` status claims product implementation or effectiveness.
4. Keine Quelle, Decision oder Evidence erweitert Produkt-, Remote-, Provider- oder Preset-Autoritaet. / No source, decision, or evidence expands product, remote, provider, or preset authority.
5. Fehlende oder veraltete Evidence fuehrt zu `Stop`, nicht zu impliziter Zustimmung. / Missing or stale evidence results in `Stop`, not implicit approval.
6. Nach dem terminalen Rename darf keine weitere Feature-Head-Mutation stattfinden; spaetere Fakten werden nur im separat reviewten Drei-Pfad-Closeout-Commit persistiert. / No feature-head mutation follows the terminal rename; later facts are persisted only in the separately reviewed three-path closeout commit.
7. `causal-closeout` verlangt exakt 66 gepruefte Tasks, State-Gleichheit, realen Task-Hash, terminale Closeout-Felder, exakte Drei-Pfad-Stage und keine Selbstreferenz. / Causal closeout requires exactly 66 checked tasks, matching state and hash, terminal fields, an exact three-path stage, and no self-reference.
