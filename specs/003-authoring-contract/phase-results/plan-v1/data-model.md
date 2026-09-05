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

### META-LH-03-Erneuerung / META-LH-03 Renewal

| Feld / Field | Wert oder Regel / Value or rule |
|---|---|
| Stabile Intake-ID / stable intake ID | Aus dem aktuellen Receipt unverändert übernehmen. / Preserve from the current receipt. |
| Neue Operation / new operation | Reserviert `9a3586f4-a375-475c-b44f-bdc7c39d9d3d`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Neues Receipt / new receipt | Reserviert `0997f398-a986-437a-b091-87da3da83e9f`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Neuer Review / new review | Reserviert `e69644e1-adc7-4f1f-857b-bce390ae8764`; vor Nutzung Eindeutigkeit prüfen. / Reserved value; verify uniqueness before use. |
| Vorgänger / predecessor | Exakte aktuelle META-LH-03-Datei nach Abschluss der Reparatur; byte-identische Archivkopie. / Exact current META-LH-03 file after repair completion; byte-identical archive copy. |
| Fachquellen / domain sources | Finale normalisierte Hashes aller fünf kanonischen Fachartefakte. / Final normalized hashes of all five canonical domain artefacts. |
| Reviewzustand / review state | Vollständiger neuer Single-Review; nur `Ready` mit übereinstimmendem Hash kann gebunden werden. / Complete new Single review; only `Ready` with matching hash can be bound. |

### Evidence Binding Leaf / Evidence-Binding-Blatt

Ein Blatt besteht aus `logicalTargetId`, Zielpfad und Zielhash, Receipt-Pfad und Receipt-Rohhash sowie Ready-Single-Review-Pfad und Review-Rohhash; optional kommt der lesbare Reviewbericht hinzu. Beim neuen Binding darf ausschließlich das Blatt `META-LH-03` wechseln. Die geordnete Zielmenge bleibt exakt 14 und alle IDs bleiben eindeutig.

A leaf consists of `logicalTargetId`, target path and target hash, receipt path and receipt raw hash, plus Ready Single review path and review raw hash; the readable review report is optional. In the new binding, only leaf `META-LH-03` may change. The ordered target set remains exactly 14 and all IDs remain unique.

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

Gate Evidence bindet Requirements-Hash, geprüften HEAD, Ausführungszeit, Befehl, Runner, Exitcode, Ergebnis, Evidence-Rolle und Reviewer. `Primary` ist pro Gate eindeutig. `Supplemental` benennt das zugehörige Primary-Element. Geplante Befehle oder erwartete Ergebnisse erfüllen kein Gate.

Gate Evidence binds requirements hash, reviewed HEAD, execution time, command, runner, exit code, result, evidence role, and reviewer. `Primary` is unique per gate. `Supplemental` names its related Primary item. Planned commands or expected results do not satisfy a gate.

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
historische Reparatur validiert
  -> Reparatur als unveränderlicher Commit eingefroren
  -> fünf Fachartefakte final
  -> fokussierte Validatoren, Fixtures und Reviews bestanden
  -> META-LH-03-Vorgänger byte-identisch archiviert
  -> neue Operation + neues Receipt
  -> vollständiger neuer Single-Review = Ready
  -> current-evidence-binding: nur META-LH-03-Blatt ersetzt
  -> additiver Binding-Validator bestanden
  -> exakte Liefermenge committet
  -> Statistik auf sauberem HEAD gerendert und separat committet
  -> PreMerge-Gates + Review + Approval am exakten HEAD
  -> normaler Merge und Fast-forward-Sync 0/0
  -> eigener Lifecycle-Merge und Fast-forward-Sync 0/0
  -> kausaler Evidence-only-Abschluss, falls erforderlich
  -> endgültiger Sync, sauber und 0/0
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
