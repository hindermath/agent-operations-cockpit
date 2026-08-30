# Datenmodell: Portfolio-Ownership / Data Model: Portfolio Ownership

## Zweck und Grenze / Purpose and boundary

Dieses Modell beschreibt die dokumentarischen Entitaeten und Evidence-Zustaende des Features. Es ist kein Produktdatenmodell, erzeugt keine Datenbank und erweitert weder Maschinenvertrag noch Decision Map. / *This model describes the documentary entities and evidence states of the feature. It is not a product data model, creates no database, and extends neither the machine contract nor the Decision Map.*

## Entitaet: Concern / Entity: Concern

| Feld / Field | Regel / Rule |
|---|---|
| `id` | Exakt `C-01` bis `C-09`; eindeutig. / Exactly `C-01` through `C-09`; unique. |
| `name` | Zweisprachig in der lesbaren Uebersicht; maschinenlesbarer englischer Name im JSON-Vertrag. / Bilingual in the readable overview; machine-readable English name in the JSON contract. |
| `ownerSeries` | Genau eine Reihe `RAW-01` bis `RAW-09`; keine Mehrfach- oder Nullzuordnung. / Exactly one series; no duplicate or missing owner. |
| `nonOwnership` | Mindestens eine pruefbare Grenze der Owner-Reihe. / At least one testable owner-series boundary. |
| `decisionPresentation` | Ab `C-05` getrennte Gruppen fuer `Open`, `Answered` und, falls vorhanden, `Superseded`; leere Gruppen werden nicht erfunden. / From `C-05`, separate groups for `Open`, `Answered`, and, where present, `Superseded`; empty groups are not invented. |

### Validierungsregeln / Validation rules

1. Die Ownership-Menge bleibt exakt `C-01 -> RAW-01` bis `C-09 -> RAW-09`. / The ownership set remains exact.
2. Nur `decisionPresentation` der Zeilen `C-05` bis `C-09` darf sich durch den fachlichen Delta aendern. / Only the decision presentation of rows `C-05` through `C-09` may change in the domain delta.
3. Die Darstellung muss dem aktuellen Zustand in `docs/decisions/open-decisions.md` entsprechen, ohne diese Datei zu aendern. / The presentation must match the current Decision Map without changing it.

## Entitaet: Owner-Reihe / Entity: Owner series

| Feld / Field | Regel / Rule |
|---|---|
| `id` | Exakt `RAW-01` bis `RAW-09`. / Exactly `RAW-01` through `RAW-09`. |
| `purpose` | Klarer fachlicher Zweck. / Clear domain purpose. |
| `systemBoundary` | Eigener Scope und Consumer-Grenze. / Owned scope and consumer boundary. |
| `expectedChildIntakes` | Nichtleere geplante Child-Intakes. / Non-empty planned child intakes. |
| `decisionIntakes` | Traceable Decision IDs; Status kommt aus der Decision Map. / Traceable decision IDs; status comes from the Decision Map. |
| `inputs`, `outputs`, `dependencies` | Explizite Vertragsbeziehungen. / Explicit contract relations. |
| `reviewEvidenceGates` | Mindestens ein pruefbarer Gate-Hinweis. / At least one reviewable gate. |
| `modes` | Geeignete Modi, keine Lieferautoritaet. / Suitable modes, not delivery authority. |
| `nonOwnership` | Mindestens eine ausdrueckliche Nicht-Zustaendigkeit. / At least one explicit non-ownership statement. |

## Entitaet: Decision-Referenz / Entity: Decision reference

| Feld / Field | Regel / Rule |
|---|---|
| `id` | ID aus `docs/decisions/open-decisions.md`. / ID from the Decision Map. |
| `domainOwner` | RAW-Reihe; gemeinsame Ownership wie `RAW-06/RAW-05` bleibt textlich erhalten. / RAW series; shared domain notation remains explicit. |
| `statusClass` | Genau `Open`, `Answered` oder `Superseded`. / Exactly one named status class. |
| `blockedExecution` | Pflicht fuer `Open`; nur die benannte RAW-Arbeit wird blockiert. / Required for `Open`; only the named RAW work is blocked. |
| `evidenceOrSupersession` | Pflicht fuer `Answered` und `Superseded`. / Required for closed states. |

### Gebundene Darstellung fuer den Delta / Bound delta presentation

| Concern | Answered / Beantwortet | Open / Offen | Superseded / Supersediert |
|---|---|---|---|
| `C-05` | `IAD604` | `DEC-T06` | keine / none |
| `C-06` | `IAD601`, `IAD602`, `IAD603`, `IAD604` | keine / none | keine / none |
| `C-07` | `IAD701`, `IAD702`, `IAD703`, `IAD704` | keine / none | keine / none |
| `C-08` | `IAD801`, `IAD802`, `IAD803` | keine / none | `DEC-T05` |
| `C-09` | `IAD901`, `IAD902`, `AUTH-RAW09-PROMOTION` | keine / none | keine / none |

Die Tabelle ist die Planungsprojektion der aktuellen Decision Map, keine neue Decision. Jede Decision-Drift stoppt den Edit und erzwingt Re-Planung. / *The table is a planning projection of the current Decision Map, not a new decision. Any decision drift stops the edit and requires replanning.*

## Entitaet: Handoff / Entity: Handoff

| Feld / Field | Regel / Rule |
|---|---|
| `id` | Exakt `H-01` bis `H-10`. / Exactly `H-01` through `H-10`. |
| `producer`, `consumer` | Gerichtete RAW-Reihen. / Directed RAW series. |
| `contract`, `version` | Benannter, versionierter Uebergabevertrag. / Named, versioned handoff contract. |
| `kind`, `binding` | Neun `BindingContract`/`true`; nur `H-06` ist `PreferredSerialOrder`/`false`. / Nine binding contracts; only `H-06` is non-binding preferred order. |
| `failureBehavior` | Fail-closed Verhalten bei fehlender oder inkompatibler Evidence. / Fail-closed behaviour for missing or incompatible evidence. |

Der Graph bleibt azyklisch. Dieses Feature aendert keinen Handoff. / *The graph remains acyclic. This feature changes no handoff.*

## Entitaet: Gate-Requirement / Entity: Gate requirement

| Feld / Field | Regel / Rule |
|---|---|
| `gateId` | Stabile eindeutige `PO-*`-ID. / Stable unique `PO-*` ID. |
| `applicability` | `Applicable` oder `N/A`; kein stilles Weglassen. / `Applicable` or `N/A`; no silent omission. |
| `requiredScope` | Exakter fachlicher oder technischer Proof. / Exact domain or technical proof. |
| `requiredCommandTokens` | Fuer `Applicable` alle im Evidence-Command erwarteten Token. / For applicable gates, every expected evidence-command token. |
| `requiredRunnerOrPlatformTokens` | Fuer `Applicable` alle erwarteten Runner-/Plattformtoken. / Every expected runner/platform token for applicable gates. |
| `owner`, `reviewer`, `plannedEvidence` | Verantwortliche Rolle, unabhaengige Review-Rolle und exakter Evidence-Pfad. / Responsible role, independent reviewer, and exact evidence path. |
| `rationale`, `reevaluationTrigger` | Fuer `N/A` beide nichtleer; fuer `Applicable` ist die Begruendung im Scope enthalten. / Both non-empty for `N/A`; applicable rationale is carried by scope. |

### Zustandsfolge / State sequence

`Drafted -> SchemaChecked -> IndependentlyReviewed -> BoundToTasks -> Executed -> NormalPreMergeValidated -> NormalMerged -> TerminalRenamePreMergeValidated -> TerminalRenameMerged -> PostMergeValidated`

Ein fehlender oder rueckwaerts driftender Zustand stoppt die Folgephase. `PreMergeValidated` erteilt keine Merge- oder Bypass-Authority. / *A missing or regressed state stops the downstream phase. `PreMergeValidated` grants no merge or bypass authority.*

## Entitaet: Evidence-Snapshot / Entity: Evidence snapshot

| Feld / Field | PreMerge | PostMerge |
|---|---|---|
| `schemaVersion` | `2.0` | `2.0` |
| `snapshotType` | `PreMerge` | `PostMerge` |
| `requirementsSha256` | Normalisierter Hash der reviewten Requirements. / Normalized reviewed requirements hash. | Derselbe Hash. / Same hash. |
| `reviewedHead` | Exakter reviewter terminaler Rename-Head; der normale Feature-Head besitzt nur einen vorlaeufigen Execution Record, weil `PO-G32` dort noch nicht erfuellt ist. / Exact reviewed terminal-rename head; the normal head has only a preliminary execution record. | Derselbe akzeptierte terminale Rename-Head. / Same accepted terminal-rename head. |
| `acceptedPreMergePath`, `acceptedPreMergeSha256` | leer / empty | Bindet den akzeptierten temporaeren Snapshot. / Binds accepted temporary snapshot. |
| `mergeCommit` | leer / empty | Tatsaechlicher Merge-Commit. / Actual merge commit. |
| `changedPaths` | Exakte reviewte Pfade. / Exact reviewed paths. | leer / empty |

## Entitaet: Delivery-Transaktion / Entity: Delivery transaction

Eine Transaktion besitzt `transactionId`, `timing`, `requiredPaths`, `conditionalPaths`, `forbiddenPaths`, `authorityBoundary` und `freezeRule`. Die konkrete Pfadmenge wird vor dem jeweiligen Commit aus [contracts/delivery-allowlist.json](contracts/delivery-allowlist.json) eingefroren; Bedingungen duerfen nicht als pauschale Erlaubnis gelesen werden. / *A transaction carries the named fields. Its concrete path set is frozen before its commit; conditional paths are not blanket permission.*

## Entitaet: Intake-Lifecycle-Datensatz / Entity: Intake lifecycle record

Der normale Feature-Kandidat enthaelt genau einen Datensatz und genau einen historischen Programmevidence-Snapshot unter `specs/002-portfolio-ownership/intake-lifecycle.json`; der terminale Rename konsumiert beide read-only. / *The normal feature candidate contains one lifecycle record and one historical programme snapshot; the terminal rename consumes both read-only.*

| Feld / Field | Regel / Rule |
|---|---|
| `schemaVersion` | Exakt `1.1`. / Exactly `1.1`. |
| `recordVersion` | Exakt `1.0`. / Exactly `1.0`. |
| `logicalTargetId` | Exakt `META-LH-02`. / Exactly `META-LH-02`. |
| `originalPath` | `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md`. |
| `archivedPath` | `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md`. |
| `originalRawSha256`, `originalNormalizedSha256` | Binden die unveraenderten akzeptierten Intake-Bytes beziehungsweise deren normalisierte Form; der Normalhash bleibt `9fc31a833421915b68b85c7dd499dc5b97a81152a8cf668599bb243ef3e17503`. / Bind unchanged accepted bytes and normalized content. |
| `authoringReceipt` | `specs/intake-authoring-receipts/META-LH-02-Portfolio-Ownership.json` plus unveraenderter Roh-SHA-256 `4c468df900e62c7d1c7927c86fda894afdbb4a8c97f092c215311b08dc209876`. / Exact immutable current receipt binding. |
| `readySingleReview` | `specs/intake-review-results/meta-lh-02-portfolio-ownership-2026-08-29-r6.json` plus unveraenderter Roh-SHA-256 `2807c8be25b4127e8a1182b2ae0d35303cc1b6c71add37c238db1b3e91f4ff90`. / Exact immutable Ready review binding. |
| `runId`, `branch` | Exakt `aa60069e-ded5-463f-a737-9b5aa96070c7` und `002-portfolio-ownership`. |

### `programmeEvidenceSnapshot`

Der Snapshot besitzt exakt `snapshotVersion`, `runId`, `branch` und `orderedLogicalTargets`. `snapshotVersion` ist `1.0`; Run und Branch entsprechen dem Lifecycle-Datensatz. Die Liste enthaelt genau 14 eindeutige Ziele in der Reihenfolge `META-LH-01` bis `META-LH-05`, danach `RAW-01` bis `RAW-09`. / *The snapshot has an exact four-field shape and fourteen uniquely ordered programme targets bound to the lifecycle run and branch.*

Jeder Ziel-Eintrag besitzt ausschliesslich `logicalTargetId`, `target { path, normalizedSha256 }`, `authoringReceipt { path, rawSha256 }` und `readySingleReview { path, rawSha256 }`. Die Zielhashes sind die akzeptierten Vor-Implementierungs-Normalhashes; Receipt- und Review-Hashes binden unveraenderliche Bytes. Der Snapshot speichert keinen Commit, PR, Merge, Providerstatus oder anderen Zukunftsfakt. / *Each entry binds only the accepted pre-implementation target hash and immutable receipt/review bytes; it records no future Git or provider fact.*

Der geplante Validator loest den historischen Zielpfad archivbewusst ueber den eindeutigen Lifecycle-Vertrag auf, verlangt die exakte Lifecycle-/Snapshot-Feldform, genau einen existierenden Original- oder Archivpfad, jeden akzeptierten Zielhash, rohe Receipt-/Review-Bytegleichheit, `ReadyForReview`, genau einen aktuellen `Single`/`Primary`/`Ready`-Review-Leaf ohne Findings, Fragen oder akzeptierte Risiken und fuehrt beide installierten Review-Oberflaechen aus. Er qualifiziert nur denselben Run, Branch und Lifecycle bei `status=Active` und Stage `Plan`, `Implement`, `Validate`, `Publish`, `Review`, `MergeAndSync` oder `Retrospective`; `Plan` ist dabei ausschliesslich der runner-owned post-Delta Analyze-Retry dieses Vertrags. Ein anderer Run, Branch, Lifecycle, inaktiver State, Stage, Hash, doppelter Leaf oder der Ausfall einer der beiden Review-Oberflaechen ist ungueltig. / *The validator is archive-aware and admits Plan only for the exact bound runner-owned post-delta analysis retry; every other shape, path, immutable-byte, accepted-hash, active-state, unique-Ready-leaf, and review-peer invariant remains fail-closed.*

### Lifecycle-Invarianten / Lifecycle invariants

1. Vor dem Rename existiert nur `originalPath`; danach nur `archivedPath`. Beide oder keiner sind ungueltig. / Before rename only the original exists; afterwards only the archive exists. Both or neither are invalid.
2. Der Rename ist inhaltlich byteidentisch und in Git exakt ein `R100`-Commit des vorhandenen Skripts. / The script commit is one byte-identical `R100` rename.
3. Receipt, Review, Series, Lifecycle-Datensatz und Intake-Inhalt bleiben unveraendert. Vor dem Domain-Delta pruefen die generischen Eingangsgates Source-Freshness; danach loest nur der Feature-002-Snapshot-Vertrag den historischen physischen Pfad archivbewusst auf. / Immutable evidence and content remain unchanged; generic freshness is pre-delta evidence and only the Feature-002 contract qualifies the post-delta historical binding.
4. Der normale Feature-Head wird zuerst reviewt und gemergt. Der Rename besitzt danach einen eigenen unveraenderten reviewten Head. Erst dessen Merge und Fast-forward-Sync erlauben kausales PostMerge. / Normal delivery precedes a separately reviewed rename; causal PostMerge follows only after its merge and synchronization.

## Entitaet: Feature-lokales Validierungswerkzeug / Entity: Feature-local validation tool

| Feld / Field | Regel / Rule |
|---|---|
| `core` | Exakt `specs/002-portfolio-ownership/contracts/validate_meta_lh02_snapshot.py`; Python 3 Standardbibliothek, read-only, sichere Grenzvalidierung, keine Shell-/dynamische Ausfuehrung und keine externe Dependency. / Exact standard-library Python core with safe boundary handling and no write or dynamic execution. |
| `bashSurface` | Exakt `specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.sh`; `#!/usr/bin/env bash`, `set -euo pipefail`, vollstaendig gequotete Variablen, `--`-Disziplin, `-h`/`--help` und gleichwertige Ausgabe/Exitcodes. / Exact strict Bash surface with help and equivalent behaviour. |
| `powerShellSurface` | Exakt `specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1`; PowerShell Core 7+, `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, validierte Parameter, vollstaendige bilinguale Comment Help, `Get-Help`, `-NoProfile`-Evidence und Advanced Function/Cmdlet `Test-AocMetaLh02Snapshot`. / Exact strict PowerShell surface with bilingual help and approved cmdlet. |
| `unixManual` | Exakt `docs/man/validate-meta-lh02-snapshot.1`; beschreibt Syntax, read-only Proof-Grenze, Exitcodes, Fehlerfaelle und Help-Verhalten. / Exact Unix manual covering syntax, proof boundary, exits, failures, and help. |
| `tests` | Exakt `contracts/test_validate_meta_lh02_snapshot.py`; positive und alle benannten Negativfaelle, Help, null Repository-Write, Peer-Paritaet und Fehler jeder installierten Review-Oberflaeche. Weitere Projektionen entstehen temporaer. / Exact test file with positive, all named negatives, help, no-write, peer parity, and individual review-surface failures; extra projections are temporary. |
| `parityEvidence` | Exakt `checklists/snapshot-tooling-parity.md`; manuelle Ergebnisse beider Varianten auf dem verfuegbaren macOS-Host, gleiche Ausgabe/Exitcodes, Help, strikte Regeln, Cmdlet/Man-Page, vollstaendige lokale Testsuite und Same-commit-Pfadmenge. Diese Entitaet behauptet keine Windows-Evidence. / Exact manual evidence for both variants on macOS, including equivalent output/exits, help, strictness, cmdlet/manual, full local suite, and same-commit paths; it does not claim Windows evidence. |
| `exactHeadPlatformEvidence` | Workflow, Job, Head-SHA, Runner, Log-URL und ausgefuehrter Command aus `PowerShell Static Analysis / PSScriptAnalyzer` fuer Linux, macOS und zwingend `windows-2022`; fehlender oder nicht erfolgreicher Windows-Beleg blockiert Merge und darf nicht durch Bypass ersetzt werden. / Workflow/job/head/runner/log/command evidence from the PowerShell Static Analysis matrix on Linux, macOS, and mandatory Windows; missing Windows proof blocks merge and cannot be bypassed. |

Alle sechs getrackten Werkzeug-/Evidence-Pfade und die bereits benannten sechs Fixture-Pfade werden gemeinsam in T052/T053 geliefert. Der normale Validatorbetrieb ist bereits read-only; ein separater mutierender Dry-run-Modus wird nicht erfunden. / *All tracked tooling/evidence paths and the six already named fixture paths are delivered together in T052/T053. Normal operation is inherently read-only, so no separate mutating dry-run mode is invented.*

## Entitaet: Review-Evidence / Entity: Review evidence

| Review | Pflichtinhalt / Required content | Geplanter Pfad / Planned path |
|---|---|---|
| First reader | Owner, Consumer-Grenze, Handoff-Typ, offener Blocker, Nicht-Ziele, naechste sichere Aktion; `6/6` korrekt. / Six named comprehension points, all correct. | `specs/002-portfolio-ownership/first-reader-review-evidence.md` |
| A11Y/B2 | DE-first/EN-second, CEFR B2, Erstgebrauch, Heading-Hierarchie, Links, lineare Lesereihenfolge, Textalternativen, Status ohne Nur-Farbe; null Blocker. / Named language and accessibility checks; zero blockers. | `specs/002-portfolio-ownership/accessibility-review-evidence.md` |
| Security/privacy | Public-Klassifikation, Secret-Muster, private Pfade, unnoetige Personendaten, Publikationseignung; null Blocker. / Public-content checks; zero blockers. | `specs/002-portfolio-ownership/security-privacy-review-evidence.md` |
| Documentation Impact | Genau eine `UpdateRequired`-Entscheidung mit Quelle, Owner, Dokumenten, Leserpfad, Sprache, Plattform, Distribution, Sync, Evidence und Trigger. / Exactly one complete decision. | `specs/002-portfolio-ownership/documentation-impact-evidence.md` |

## Globale Invarianten / Global invariants

1. Ownership, Handoffs und Decision-Status werden nicht aus Agentenpraeferenz abgeleitet. / Ownership, handoffs, and decision status are never inferred from agent preference.
2. Historische Evidence ersetzt keine aktuelle Red/Green-, Acceptance-, Review- oder Exact-head-Evidence. / Historical evidence replaces no current proof.
3. Alle Pfade bleiben repository-relativ und public-suitable. / All paths remain repository-relative and public-suitable.
4. Kein Artefakt erteilt Produkt-, RAW-, Level-0-, Preset-, Remote-, Merge-, Bypass- oder Provider-Authority. / No artefact grants the named authority.
5. Shared Writer werden seriell aktualisiert; Hash-Drift invalidiert nachgelagerte Snapshots und Pfadlisten. / Shared writers are updated serially; hash drift invalidates downstream snapshots and path lists.
