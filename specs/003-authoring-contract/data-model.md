# Datenmodell: Nachweisbarer Intake-Authoring-Vertrag

## Zweck / Purpose

Dieses Modell beschreibt die fachlichen Entitäten und ihre Beweisbeziehungen. Es ist kein neues Produktdatenmodell und führt keine Datenbank ein. Alle Pfade sind repository-relativ. Die einzige Dokumentationsauswirkungsentscheidung bleibt `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

This model describes domain entities and their evidence relationships. It is not a new product data model and introduces no database. All paths are repository-relative. The sole Documentation Impact decision remains `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

## Entitäten / Entities

### Kanonisches Fachartefakt / Canonical Domain Artefact

| Feld / Field | Typ / Type | Regel / Rule |
|---|---|---|
| `artifactId` | feste Zeichenfolge / fixed string | Eindeutig in der Menge aus genau fünf Einträgen. / Unique in the set of exactly five. |
| `path` | Repository-Pfad / repository path | Liegt exakt in der genehmigten Positivliste. / Exactly in the approved allowlist. |
| `order` | Ganzzahl / integer | Stabil `1..5`; bestimmt Änderungs- und Bindungsreihenfolge. / Stable `1..5`; defines change and binding order. |
| `currentNormalizedSha256` | SHA-256 | Vor der Änderung erfasster normalisierter Hash. / Pre-change normalized hash. |
| `finalNormalizedSha256` | SHA-256 | Erst nach dem letzten Byte berechnet; vorher nicht Evidence. / Computed only after final bytes; not evidence before then. |
| `contractDelta` | Liste / list | Konkrete neue Regeln, keine hypothetischen Features. / Concrete new rules, no hypothetical features. |
| `requiredConsumers` | Pfadliste / path list | Nur Verbraucher, die wegen des Deltas geändert oder neu validiert werden müssen. / Only consumers that must change or be revalidated because of the delta. |

Die fünf IDs sind `intake-template`, `receipt-template`, `project-profile-template`, `aoc-governance-config` und `field-validation-summary`.

The five IDs are `intake-template`, `receipt-template`, `project-profile-template`, `aoc-governance-config`, and `field-validation-summary`.

### Intake-Authoring-Vertrag / Intake Authoring Contract

| Feld / Field | Regel / Rule |
|---|---|
| Stabile Identität / stable identity | Intake-ID bleibt über Revisionen gleich; Operation-, Receipt- und Review-ID sind je Ereignis neu und eindeutig. / Intake ID persists across revisions; operation, receipt, and review IDs are new and unique per event. |
| Titel / titles | Deutsch zuerst und Englisch danach; beide bezeichnen denselben Scope. / German first and English second; both name the same scope. |
| Kontext / context | Zweck, Istzustand, Zielzustand, Zielgruppe und Vorwissen sind explizit. / Purpose, current state, target state, audience, and prior knowledge are explicit. |
| Traceability und Scope / traceability and scope | Quellenanforderungen, Scope, Non-Goals und Abhängigkeiten sind nachvollziehbar verbunden. / Source requirements, scope, non-goals, and dependencies are traceably connected. |
| Quellen / sources | Geordnet, typisiert, hashgebunden und mit Vertrauensgrenze; öffentliche URLs nur HTTPS. / Ordered, typed, hash-bound, and trust-bounded; public URLs use HTTPS only. |
| Grenzen / boundaries | Eingaben, Ausgaben, ausgeschlossene Wirkung und Nicht-Autorität sind explizit. / Inputs, outputs, excluded effects, and non-authority are explicit. |
| Anforderungen / requirements | Funktionale und nichtfunktionale Anforderungen sind atomar und eindeutig identifiziert. / Functional and non-functional requirements are atomic and uniquely identified. |
| Entscheidungen und Risiken / decisions and risks | Getrennte Felder mit Owner, Status, Evidenz und Re-Evaluation-Trigger. / Separate fields with owner, status, evidence, and re-evaluation trigger. |
| Lieferung und Akzeptanz / delivery and acceptance | Erwartete Artefakte und messbare Kriterien sind eindeutig benannt. / Expected artefacts and measurable criteria are named unambiguously. |
| Positive Evidenz / positive evidence | Belegt einen gültigen Pfad. / Proves a valid path. |
| Negative Evidenz / negative evidence | Belegt, dass ein ungültiger oder nicht autorisierter Pfad fail-closed scheitert. / Proves that an invalid or unauthorized path fails closed. |
| Folgeschritt / follow-up | Genau eine nächste sichere Aktion; nur bei expliziter Autorität ausführbar. Gesperrte Platzhalter sind nicht ausführbar. / Exactly one next safe action; executable only with explicit authority. Blocked placeholders are non-executable. |

### Projektprofil-Bindung / Project Profile Binding

| Feld / Field | Regel / Rule |
|---|---|
| `profilePath` | Für AOC exakt `requirements/baseline/intake-authoring-profile.md`; muss innerhalb der Repository-Grenze existieren. / For AOC exactly the listed path; must exist within the repository boundary. |
| `profileId` | Muss mit der Identität im aufgelösten Profil übereinstimmen. / Must match the identity in the resolved profile. |
| `documentationLanguage` | `de-DE`; muss mit AOC-Governance und Profil übereinstimmen. / `de-DE`; must agree with AOC governance and profile. |
| `trustPolicy` | Definiert erlaubte Quellentypen und Grenzen. / Defines allowed source types and boundaries. |
| `authorityPolicy` | Trennt Authoring, Review, Ausführung, Merge, Sync und Promotion. / Separates authoring, review, execution, merge, sync, and promotion. |
| `findingTraceability` | Verlangt stabile Finding-ID, Status, Owner, Evidenz und Trigger. / Requires stable finding ID, status, owner, evidence, and trigger. |
| `autonomyMode` | Muss explizit sein; erzeugt keine zusätzliche Autorität. / Must be explicit; grants no additional authority. |
| `revisionPolicy` | Vorgänger, Änderungsgrund und neue Receipt-/Operation-ID sind gebunden. / Predecessor, reason for change, and new receipt/operation ID are bound. |

### Authoring Receipt

| Feld / Field | Regel / Rule |
|---|---|
| `receiptId` | UUID, pro Veröffentlichung eindeutig. / UUID, unique per publication. |
| `operationId` | UUID, verweist auf genau eine Authoring-Operation. / UUID, references exactly one authoring operation. |
| `target.path` | Repository-relativer Intake-Pfad. / Repository-relative intake path. |
| `target.normalizedSha256` | Muss den publizierten Intake exakt binden. / Must bind the published intake exactly. |
| `sources[]` | Geordnet; jede Quelle trägt Provenienz, Hash und Beweisgrenze. / Ordered; each source carries provenance, hash, and proof boundary. |
| `outcome` | Zulässiger Authoring-Ausgang; Default `NeedsClarification`. / Allowed authoring outcome; default `NeedsClarification`. |
| `promptState` | `Blocked` oder `Enabled`; `Blocked` verbietet ausführbare Folgeaufrufe. / `Blocked` or `Enabled`; `Blocked` forbids executable follow-up calls. |
| `agentSurface` | Bei `Blocked` enthalten beide Blöcke `BLOCKED` und `DO NOT RUN`, stabile Decision-IDs und keine ausführbare Invocation. Bei `ReadyForReview` binden Specify und Autonomous dasselbe exakte Lastenheft, ohne automatische Ausführung oder historische Authority-Ableitung. / With `Blocked`, both blocks contain `BLOCKED`, `DO NOT RUN`, stable decision IDs, and no executable invocation. At `ReadyForReview`, Specify and Autonomous bind the exact same intake without automatic execution or historical authority inference. |
| `nonAuthority` | Erklärt ausdrücklich, was Receipt und Review nicht erlauben. / Explicitly states what receipt and review do not authorize. |

### Reparatur-Checkpoint / Repair checkpoint

| Feld / Field | Regel / Rule |
|---|---|
| `candidatePaths` | Exakt 48 eindeutige, existente, literal benannte Reparaturpfade; keine Globs, Plan-, Reporting- oder Fachpfade. / Exactly 48 unique existing literal repair paths; no globs or Plan/reporting/domain paths. |
| `stagedPaths` | Nach literalem `git add --` mengenidentisch mit `candidatePaths`; fremde Änderungen bleiben unstaged. / Set-equal after literal staging; foreign changes remain unstaged. |
| `repairCommit` | Genau ein lokaler Commit vor Tasks; kein Push und nicht der spätere Feature-Commit. / One local pre-Tasks commit; no push and not the later feature commit. |
| `repairTree` | Tree-OID des lokalen Reparatur-Commits. / Tree OID of the local repair commit. |
| `manifestPath` | `specs/003-authoring-contract/repair-checkpoint-manifest.json`, erst im späteren Feature-Commit. / Exact path, created only in the later feature commit. |
| `pathHashes` | Ein Roh-SHA-256 je Reparaturpfad, gegen den Reparatur-Tree geprüft. / One raw SHA-256 per repair path, validated against the repair tree. |
| Selbstreferenz / self-reference | Das Manifest ist kein Mitglied des Reparatur-Commits und behauptet dies nicht. / The manifest is not a member of the repair commit and makes no such claim. |

### META-LH-03-Erneuerung / META-LH-03 Renewal

| Feld / Field | Wert oder Regel / Value or rule |
|---|---|
| Stabile Intake-ID / stable intake ID | Aus dem aktuellen Receipt unverändert übernehmen. / Preserve from the current receipt. |
| Neue Operation / new operation | Reserviert `986c1d6c-d485-460b-8d8d-7cf5816a2c36`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Neues Receipt / new receipt | Reserviert `f41328cd-b301-4533-89dc-02aab758ab1f`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Neuer Review / new review | Reserviert `b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Vorgänger / predecessor | Exakte r1-Zieldatei und exaktes r1-Receipt nach Abschluss der Reparatur; beide erhalten je eine byte-identische Archivkopie. / Exact r1 target and exact r1 receipt after repair completion; each receives a byte-identical archive copy. |
| Fachquellen / domain sources | Finale normalisierte Hashes aller fünf kanonischen Fachartefakte. / Final normalized hashes of all five canonical domain artefacts. |
| Reviewzustand / review state | Vollständiger neuer Single-Review; nur `Ready` mit übereinstimmendem Hash kann gebunden werden. / Complete new Single review; only `Ready` with matching hash can be bound. |

### Update-Operation und Supersession / Update operation and supersession

| Feld / Field | Regel / Rule |
|---|---|
| `type` | Exakt `Update`. / Exactly `Update`. |
| `proposal` | Exakter JSON-Pfad `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/proposal.json`, strikter UTF-8-Normalhash und aktuelle Approval mit Person, UTC-Zeit und Evidence. / Exact JSON path, strict UTF-8 normalized hash, and current approval with person, UTC time, and evidence. |
| `authorityPreflight` | Aktuelle ausdrückliche Update-Autorität, Ziel, Receipt, Quellen, aktueller Review-Link, Git-Zustand, keine Tombstone- oder unvollständige Operation; alles vor Mutation. / Current explicit update authority, target, receipt, sources, current review link, Git state, no tombstone or incomplete operation; all before mutation. |
| `sources[]` | Exakt: byte-identisch archivierter r1-Intake; danach Intake-Vorlage, Receipt-Vorlage, Projektprofil-Vorlage, AOC-Governance-Konfiguration und Feldvalidierungszusammenfassung. / Exactly: byte-identically archived r1 intake; then intake template, receipt template, project-profile template, AOC governance configuration, and field-validation summary. |
| `supersedes.target` | Aktiver r1-Pfad, Archivpfad, identischer Rohhash, normalisierter Zielhash. / Active r1 path, archive path, identical raw hash, normalized target hash. |
| `supersedes.receipt` | Aktiver r1-Receipt-Pfad, Archivpfad und identischer Rohhash. / Active r1 receipt path, archive path, and identical raw hash. |
| `archives` | Ziel und Receipt liegen byte-identisch unter `specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/`; die R1-Rohhashes sind `ca159a03a91a19c3f2812a1a638604ca29dab816a20a9a67b7c5d06b3281f5eb` und `392d893407ee5441e5f9d33f04e0df5365fc985e85f619dedeb47f3bea25bb0b`. / Target and receipt are byte-identical at the exact paths and bind the listed R1 raw hashes. |
| `stagingDirectory` | Exakt `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/staging`; enthält den literal benannten Ziel- und Receipt-Kandidaten. / Exact path containing the literally named target and receipt candidates. |
| Zielmengen / target sets | `intendedTargets`, `validatedTargets` und `publishedTargets` sind identisch und enthalten exakt beide Archive, aktives Ziel und aktives Receipt. / All three arrays are equal and contain exactly both archives, active target, and active receipt. |
| `publication` | Ziel, Receipt, Operation und abhängige Bindungen werden atomar publiziert. / Target, receipt, operation, and dependent bindings publish atomically. |
| `rollback` | Fehler lässt aktive R1-Artefakte unverändert; Reparaturdetails stehen in `failure`, `nextAction` und `rollbackBoundary`. / Failure leaves active R1 artefacts unchanged; repair details use the listed fields. |
| `status` | Zulässig sind nur `Proposed`, `Approved`, `Applying`, `Completed` und `Failed`. `Completed` ist Erfolg; `Failed` ist der einzige terminale Fehler. / Only the validator-accepted statuses are allowed; success and failure are exact. |
| Artefaktvalidierung / artefact validation | Beide installierten Validatoren prüfen das Operation-Journal vor `Completed`. / Both installed validators check the operation journal before `Completed`. |
| Review-Supersession | R1-Request, -Ergebnis und -Bericht werden mit Pfad und Rohhash explizit durch das neue R2-Tripel supersediert. / The R1 request, result, and report are explicitly superseded by the new R2 triple with paths and raw hashes. |

### Evidence Binding Leaf / Evidence-Binding-Blatt

Ein Blatt besteht aus `logicalTargetId`, Zielpfad und Zielhash, Receipt-Pfad und Receipt-Rohhash sowie Ready-Single-Review-Pfad und Review-Rohhash; optional kommt der lesbare Reviewbericht hinzu. Beim neuen Binding darf ausschließlich das Blatt `META-LH-03` wechseln. Die geordnete Zielmenge bleibt exakt 14 und alle IDs bleiben eindeutig.

A leaf consists of `logicalTargetId`, target path and target hash, receipt path and receipt raw hash, plus Ready Single review path and review raw hash; the readable review report is optional. In the new binding, only leaf `META-LH-03` may change. The ordered target set remains exactly 14 and all IDs remain unique.

### Historischer Checkpoint und aktuelle Bridge / Historical checkpoint and current bridge

Der historische Checkpoint bindet genau 48 literal benannte Reparaturpfade in einem lokalen Commit und Tree. Das spätere `repair-checkpoint-manifest.json` liegt nur im Feature-Commit, bindet Commit, Tree und Rohhash je Reparaturpfad und behauptet keine eigene Anwesenheit im früheren Tree. Die aktuelle `Primary` Bridge läuft am finalen Feature-HEAD, beweist den Reparatur-Commit als Ancestor, vergleicht jeden Manifestpfad und Hash gegen dessen Tree, bindet R1-Ziel und R1-Receipt an ihre byte-identischen Archive, belegt die R2-Supersession und hält die übrigen 13 Blätter sowie die Series-Brücke identisch.

The historical checkpoint binds exactly 48 literal repair paths in one local commit and tree. The later manifest exists only in the feature commit, binds commit/tree and every raw path hash, and makes no self-referential claim. The final Primary bridge proves ancestry and validates every manifest path/hash against that repair tree before checking direct R1-to-R2 supersession and unchanged remaining leaves.

### Gate Requirement / Gate-Anforderung

| Feld / Field | Regel / Rule |
|---|---|
| `gateId` | Stabil und eindeutig. / Stable and unique. |
| `applicability` | `Applicable` oder `N/A`, jeweils mit Begründung und Trigger. / `Applicable` or `N/A`, each with rationale and trigger. |
| `requiredScope` | Exakte fachliche Beweisgrenze. / Exact domain proof boundary. |
| `requiredCommandTokens` | Tokens, die im realen Primärnachweis vorkommen müssen. / Tokens that must occur in real Primary proof. |
| `requiredRunnerOrPlatformTokens` | Reale Runner/Interpreter, nicht nur Jobnamen. / Real runners/interpreters, not job names alone. |
| `owner` und `reviewer` | Verantwortliche Rollen; Selbstbehauptung ersetzt kein Review. / Responsible roles; self-assertion does not replace review. |
| `primaryProof` | Genau eine geplante Primärquelle pro anwendbarem Gate. / Exactly one planned Primary source per applicable gate. |
| `supplementalProof` | Optionale Zusatzquelle, die auf Primary verweist. / Optional additional source that points to Primary. |
| `reevaluationTrigger` | Ereignis, das `N/A` oder einen bestandenen Nachweis erneut öffnet. / Event that reopens `N/A` or passed proof. |

### Gate Evidence / Gate-Nachweis

Gate Evidence bindet Requirements-Hash, geprüften HEAD, Ausführungszeit, Befehl, Runner, Exitcode, Ergebnis, Evidence-Rolle und Reviewer. `Primary` ist pro Gate eindeutig. Jedes `Supplemental` benennt das eindeutige Primary-Element desselben Gates. Der feature-lokale Pre-Validator prüft diese Referenz sowie in PostMerge den exakt konfigurierten PreMerge-Pfad und dessen Normalhash, bevor der unveränderte installierte Evidence Core läuft. Der Core selbst wird nicht als Prüfer dieser zusätzlichen Invarianten dargestellt.

Gate Evidence binds requirements hash, reviewed head, command evidence, role, and reviewer. Every Supplemental item references the unique Primary item for its gate. The feature-local pre-validator enforces this relation and the exact configured PostMerge-to-PreMerge path/hash before the unchanged installed Evidence Core; the Core is not credited with those extra checks.

### PreMerge- und PostMerge-Snapshot / PreMerge and PostMerge snapshot

| Feld / Field | PreMerge | PostMerge |
|---|---|---|
| Requirements / requirements | `contracts/autonomous-run-gate-requirements.json`; nur vor Merge wissbare Fakten. / Pre-merge facts only. | `contracts/postmerge-gate-requirements.json`; nur nach realen Ereignissen wissbare Fakten. / Post-event facts only. |
| `reviewedHead` | Exakter final geprüfter Feature-HEAD. / Exact final reviewed feature head. | Derselbe akzeptierte Feature-HEAD. / Same accepted feature head. |
| `acceptedPreMergePath` / `acceptedPreMergeSha256` | Beide leer. / Both empty. | Exakter erhaltener Runner-Pfad und sein normalisierter Hash; Abweichung blockiert. / Exact retained runner path and normalized hash; mismatch blocks. |
| `mergeCommit` | Leer; Merge ist nicht ausgeführt. / Empty; merge has not executed. | Tatsächlicher normaler Feature-Merge-Commit. / Actual normal feature merge commit. |
| `changedPaths` | Nach Evidence-Core-Vertrag. / Per evidence-core contract. | Exakt leere Liste. / Exactly empty list. |
| Inhalt / content | Aktueller HEAD, technische Gates, Reviews, Threads, Approval, normale Merge-Bereitschaft. / Current head, technical gates, reviews, threads, approval, normal merge readiness. | Merge/PR, Lifecycle, kausaler Closeout, finaler Bericht, Retrospektive, Trend, Sync. / Merge/PR, lifecycle, causal closeout, final report, retrospective, trend, sync. |

Beide Snapshots sind exakt benannte Runner-Artefakte. Der PostMerge-Snapshot entsteht erst nach tatsächlichem Closeout-Merge und finalem Sync. Repository-Artefakte dokumentieren die vor dem Closeout-PR bereits realen Fakten und dessen exakten Kandidaten; erst der nachgelagerte Runner-Snapshot kann wahrheitsgemäß den Closeout-Merge und End-Sync binden.

Both snapshots are exactly named runner artefacts. The PostMerge snapshot is created only after the actual closeout merge and final sync. Repository artefacts record facts already real before the closeout PR and its exact candidate; only the later runner snapshot can truthfully bind the closeout merge and final sync.

### Reporting-Vertrag / Reporting contract

Die Pfadmenge besteht exakt aus den 19 Pfaden in `reporting-contract-addendum.md`: fünf Agentenflächen, fünf Agenten-Templates, Constitution und Mirror, drei Spec-Kit-Templates sowie Policy, Addendum, Feature-Retrospektive und Laufnachweis. Zwischen eindeutigen Start-/Endmarkern ist der Guidance-Block auf allen zehn Agentenflächen/-Templates byte-identisch. Der Feature-Bericht besitzt genau sieben geordnete Teile: Output, Findings, bestätigte Regeln, Interventionen/Reparaturen, Effizienzbeobachtungen, AEPS-Relevanz und `Completion/Retrospective Evidence`. Sein Trend vergleicht META-LH-01, META-LH-02 und META-LH-03 nur über zitierte Quellen, identische Metrikdefinitionen und belegte Werte; fehlende Vergleichbarkeit bleibt explizit.

The path set consists exactly of the 19 paths in `reporting-contract-addendum.md`: five agent surfaces, five agent templates, the constitution and mirror, three Spec Kit templates, policy, addendum, feature retrospective, and run evidence. Between unique markers, the guidance block is byte-identical across all ten agent surfaces/templates. The feature report has exactly seven ordered parts: Output, Findings, confirmed rules, interventions/repairs, efficiency observations, AEPS relevance, and `Completion/Retrospective Evidence`. Its trend compares META-LH-01, META-LH-02, and META-LH-03 only through cited sources, identical metric definitions, and supported values; missing comparability stays explicit.

### Liefermengensnapshot / Delivery-Set Snapshot

| Menge / Set | Bedeutung / Meaning |
|---|---|
| `planned` | Aufgelöste Positivliste aus dem deklarativen Design. / Resolved allowlist from the declarative design. |
| `changed` | Tatsächlich geänderte/unverfolgte Repository-Pfade. / Actually changed/untracked repository paths. |
| `staged` | Exakt für den nächsten Commit vorgemerkte Pfade. / Paths staged exactly for the next commit. |
| `foreign` | `changed - planned`; muss leer oder bewusst außerhalb des Kandidaten bleiben. / `changed - planned`; must be empty or deliberately remain outside the candidate. |
| `missing` | Erwartete, aber nicht erzeugte Pfade; nur mit explizitem `N/A` zulässig. / Expected but absent paths; allowed only with explicit `N/A`. |

### Lifecycle Evidence / Lifecycle-Nachweis

Der logische Pfad bleibt der in Series und Binding verwendete META-LH-03-Pfad. Der physische Pfad nach Abschluss lautet `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md`. Das feature-lokale Lifecycle-Artefakt bindet beide Pfade, Run-ID, Branch, Receipt und Review, ohne den abgeschlossenen Series-Manifest oder META-LH-02 zu ändern.

The logical path remains the META-LH-03 path used by Series and binding. The physical completion path is `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.003-authoring-contract.md`. The feature-local lifecycle artefact binds both paths, run ID, branch, receipt, and review without changing the completed Series manifest or META-LH-02.

## Zustandsübergänge / State Transitions

```text
baseline (einzige Wurzel: vollständige bestehende Ausführungsoberfläche)
  -> vertical-red (Evidence-Pfad zuerst; kleinstes Positiv-/Negativpaar rot)
  -> vertical-green (kleinste Domain-/Validator-Scheibe grün)
  -> domain-expansion (fünf Fachartefakte und Konsumenten)
  -> fokussierte Validatoren, Fixtures und Reviews bestanden
  -> renewal (r1-Ziel und r1-Receipt byte-identisch archiviert)
  -> Update-Operation terminal + neues Receipt
  -> vollständiger neuer Single-Review = Ready
  -> current-evidence-binding: nur META-LH-03-Blatt ersetzt
  -> global-ready (additive Primary Bridge über realen Dispatcher bestanden)
  -> reviews
  -> exakte Liefermenge committet
  -> Statistik auf sauberem HEAD gerendert und separat committet
  -> premerge (nur aktuell wissbare Gates + Review + Approval)
  -> feature-merge (normal, tatsächlicher PR/Commit)
  -> lifecycle (eigener normaler Merge)
  -> closeout (fünf Evidence-Pfade; finaler Bericht, Retrospektive, Trend)
  -> postmerge (bindet akzeptierte PreMerge-Evidence, Closeout-Merge und Sync 0/0)
```

Jeder Pfeil ist fail-closed: fehlende Hashgleichheit, negative Fixture, fehlender Runner, veralteter HEAD, offener Review-Thread oder nicht verfügbare Approval stoppt die Folgeaktion. `Ready`, Series-Lifecycle und Ausführungsautorität bleiben getrennte Achsen.

Every arrow fails closed: hash mismatch, failing negative fixture, missing runner, stale HEAD, unresolved review thread, or unavailable approval stops the next action. `Ready`, Series lifecycle, and execution authority remain separate axes.

## Invarianten / Invariants

1. Genau fünf kanonische Fachartefakte; Reihenfolge `1..5` bleibt stabil.
2. Genau 14 geordnete Evidence-Blätter; nur META-LH-03 darf nach der Fachänderung wechseln.
3. Die alte Binding-Reparatur und ihr Checker bleiben byte- und hashgebundene Vorgänger.
4. Eine Erneuerung hat neue Operation-, Receipt- und Review-ID bei stabiler Intake-ID.
5. Ein `Blocked`-Receipt enthält keinen ausführbaren Folgeaufruf.
6. Öffentliche Quellen sind HTTPS; lokale Pfade bleiben innerhalb des Repositorys.
7. Ein Gate ist nur mit realer, HEAD-genauer Primary Evidence erfüllt.
8. Eine fehlende Approval wird nie als Approval interpretiert.
9. Kein Lifecycle-Ereignis ändert die abgeschlossene Series oder META-LH-02 rückwirkend.
10. Öffentliche Artefakte enthalten nur repository-relative Pfade; Runner-Artefakte werden ausdrücklich als nicht getrackte logische Namen bezeichnet.
11. Die Phasenkette hat genau eine Wurzel (`baseline`), keine Zyklen und je Nichtwurzel genau einen unmittelbaren Vorgänger.
12. PreMerge verlangt weder ausgeführten Merge noch Merge-Commit; PostMerge bindet einen akzeptierten PreMerge-Pfad und -Hash.
13. Der eingefrorene Checker wird nicht gegen das finale geänderte META-LH-03-Blatt ausgeführt; aktuelle Gültigkeit liefert die additive Primary Bridge.
14. Ziel- und Receipt-Archiv sind byte-identisch und vollständig in `supersedes` gebunden; nur terminale Update-Operationen sind zulässig.
15. Der gemeinsame Guidance-Block ist auf fünf Agentenflächen byte-identisch; Trendwerte werden nicht erfunden.

1. Exactly five canonical domain artefacts; order `1..5` remains stable.
2. Exactly 14 ordered evidence leaves; only META-LH-03 may change after the domain update.
3. The old binding repair and its checker remain byte- and hash-bound predecessors.
4. A renewal has new operation, receipt, and review IDs with a stable intake ID.
5. A `Blocked` receipt contains no executable follow-up call.
6. Public sources use HTTPS; local paths remain within the repository.
7. A gate passes only with real, HEAD-exact Primary evidence.
8. Missing approval is never interpreted as approval.
9. No lifecycle event retroactively changes the completed Series or META-LH-02.
10. Public artefacts contain repository-relative paths only; runner artefacts are explicitly described as untracked logical names.
11. The phase chain has exactly one root (`baseline`), no cycle, and exactly one immediate predecessor for every non-root phase.
12. PreMerge requires neither executed merge nor merge commit; PostMerge binds an accepted PreMerge path and hash.
13. The frozen checker does not run against the final changed META-LH-03 leaf; the additive Primary bridge provides current validity.
14. Target and receipt archives are byte-identical and fully bound in `supersedes`; only terminal Update operations qualify.
15. The shared guidance block is byte-identical across five agent surfaces; trend values are never invented.
