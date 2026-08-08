<!-- intake-authoring:begin -->
# RAW-08 – Workflow Engine und Program-to-Knowledge / Workflow Engine and Program-to-Knowledge

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** Git- und Review-Grundlagen; keine Spec-Kit-, Workflow-Engine-, Attestation- oder Governance-Erfahrung / Git and review basics; no Spec Kit, workflow-engine, attestation, or governance experience
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

RAW-08 verbindet Charter, Quellen, Decisions, Lastenhefte, Spezifikationen,
Pläne, Tasks, Evidence und Retrospektiven zu einem nachvollziehbaren
Program-to-Knowledge-Workflow. Der aktuelle Bestand besitzt diese Artefakte,
aber ohne einen gemeinsamen Lifecycle-, Traceability-, Evidence-,
Attestation- und Retention-Vertrag könnten unvollständige oder widersprüchliche
Nachweise fälschlich als abgeschlossen gelten. / *RAW-08 connects charters,
sources, decisions, intakes, specifications, plans, tasks, evidence, and
retrospectives into a traceable program-to-knowledge workflow. Without one
common lifecycle, traceability, evidence, attestation, and retention contract,
incomplete or contradictory evidence could be mistaken for completion.*

Ziel ist ein versionierter, maschinenlesbarer Workflow-Evidence-Vertrag mit
deterministischen Übergängen, hashgebundener Herkunft, positiver, negativer und
Provider-Failure-Evidence sowie einem prüfbaren Knowledge Package für RAW-09.
RAW-08 besitzt diese Governance-Artefakte, aber keine AOC-Produktzustandslogik,
keine Produktcommands und keine Preset-Promotion. / *The target is a versioned,
machine-readable workflow-evidence contract with deterministic transitions,
hash-bound provenance, positive, negative, and provider-failure evidence, and
a reviewable knowledge package for RAW-09. RAW-08 owns these governance
artifacts, not AOC product-state logic, product commands, or preset promotion.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Charter / Programmauftrag:** legt Zweck, Grenzen und Autorität eines
  Programms fest. / *Defines a programme's purpose, boundaries, and authority.*
- **Source / Quelle:** benanntes Ursprungsartefakt, aus dem eine Anforderung
  oder Beobachtung stammt. / *A named origin artifact for a requirement or
  observation.*
- **Decision / Entscheidung:** ausdrücklich bestätigte fachliche Festlegung;
  ein Agent darf sie nicht raten. / *An explicitly confirmed domain choice; an
  agent must not guess it.*
- **Intake / Lastenheft:** reviewbares Anforderungsartefakt vor Specify oder
  Implementierung. / *A reviewable requirements artifact before Specify or
  implementation.*
- **Spec, Plan und Task:** Spezifikation, Lösungsplan und ausführbare
  Arbeitseinheit. Sie entstehen erst in separat autorisierten Spec-Kit-
  Schritten. / *Specification, solution plan, and executable work item. They
  are created only by separately authorised Spec Kit steps.*
- **Evidence / Nachweis:** reproduzierbares Artefakt mit Quelle, Ergebnis,
  Reason Code und Hash. Positive Evidence belegt Erfolg, negative Evidence
  eine erwartete Ablehnung und Provider-Failure-Evidence einen externen
  Werkzeug- oder Dienstausfall. / *A reproducible artifact with source,
  outcome, reason code, and hash. Positive evidence proves success, negative
  evidence an expected rejection, and provider-failure evidence an external
  tool or service failure.*
- **Receipt / Empfangs- und Abschlussnachweis:** hashgebundener Beleg für
  Operation, Authority, Inputs und Ergebnis. / *A hash-bound record of an
  operation, its authority, inputs, and outcome.*
- **Traceability Graph / Nachverfolgungsgraph:** gerichtete Beziehungen von
  Quellen bis zu Evidence und Retrospektive. / *Directed relationships from
  sources to evidence and retrospective.*
- **Knowledge Package / Wissenspaket:** de-identifiziertes, attestiertes Paket
  aus Traceability, Evidence und Retrospektiven für RAW-09. / *A de-identified,
  attested package of traceability, evidence, and retrospectives for RAW-09.*
- **Retrospective Handoff / Retrospektivenübergabe:** übergibt Beobachtungen,
  Learnings und Gegenbeispiele, erzeugt aber keine normative Decision. / *Passes
  observations, learning, and counterexamples without creating a normative
  decision.*
- **Attestation Envelope / Attestationsumschlag:** versioniertes Dokument mit
  signiertem Inhaltshash, Key-ID und Trust-Policy-Referenz. / *A versioned
  document with a signed content hash, key ID, and trust-policy reference.*
- **Trust Policy / Vertrauensrichtlinie:** versionierte Allowlist zulässiger
  Signaturprofile, Schlüssel-IDs und Trust Roots. / *A versioned allowlist of
  signature profiles, key IDs, and trust roots.*
- **Legal Hold / Aufbewahrungssperre:** dokumentierte Ausnahme, die eine
  fällige Löschung bis zur Freigabe aussetzt. / *A documented exception that
  suspends due deletion until release.*
- **Stop-Gate:** fail-closed Grenze; fehlende Preconditions, Authority oder
  Evidence ergeben `Blocked`, nie angenommenen Erfolg. / *A fail-closed
  boundary where missing preconditions, authority, or evidence result in
  Blocked, never assumed success.*
- **`research-only`:** erlaubt ausschließlich Requirements-, Vertrags- und
  Offline-Fixture-Arbeit ohne Produkt- oder Provideraktionen. / *Allows only
  requirements, contract, and offline-fixture work without product or provider
  actions.*
- **`serial-autonomous`:** möglicher späterer serieller Modus, der nur nach
  vollständigem Review und separater aktueller Authority starten darf. / *A
  possible later serial mode that may start only after complete review and
  separate current authority.*
- **Spec Kit:** getrennte Befehlsfolge für Specify, Plan, Tasks und
  Implementierung; dieses Lastenheft startet keinen dieser Schritte. / *A
  separate command sequence for Specify, Plan, Tasks, and implementation; this
  intake starts none of them.*
- **MergeAndSync:** historische Delivery-Obergrenze, keine aktuelle Merge-
  oder Bypass-Autorität. / *A historical delivery ceiling, not current merge or
  bypass authority.*

Weitere Begriffe erklärt das [zweisprachige Glossar](../../baseline/glossary.md).
/ *The [bilingual glossary](../../baseline/glossary.md) explains additional
terms.*

## Scope, Systemgrenze und Non-Goals / Scope, system boundary, and non-goals

Im Scope liegen Artifact Lifecycle, Traceability Graph, Evidence-/Receipt-
Vertrag, Retrospective Handoff, Knowledge Package, die bestätigte JSON-
Persistenz, Attestation, Retention, typisierte RAW-05/06/09-Handoffs,
Reason Codes und dependency-freie Offline-Evidence. / *Scope includes artifact
lifecycle, traceability graph, evidence and receipt contract, retrospective
handoff, knowledge package, the confirmed JSON persistence, attestation,
retention, typed RAW-05/06/09 handoffs, reason codes, and dependency-free
offline evidence.*

Nicht im Scope sind AOC-Produktzustand, Produktcommands, Prozessstart,
Hardware-I/O, Provideraufrufe, Credential-Zugriff, echte Signaturoperationen,
Produktimplementierung, Remote Writes, Merge, Bypass, Preset-Änderung oder
-Promotion, GitHub-Write und Level-0-Mutation. Dieses Requirements-Repair
erzeugt keine Spec-, Plan-, Task- oder Produktdatei. / *AOC product state,
product commands, process start, hardware I/O, provider calls, credential
access, real signing operations, implementation, remote writes, merge, bypass,
preset change or promotion, GitHub writes, and Level-0 mutation are out of
scope. This requirements repair creates no spec, plan, task, or product file.*

RAW-05 besitzt Execution Nodes, Health, Freshness und Node Attestation. RAW-06
besitzt CLI-, Process-, Exit-, Environment- und Remote-Transport-Verträge.
RAW-08 konsumiert nur deren Evidence und besitzt weder Node- noch
Prozessautorität. RAW-09 konsumiert das Knowledge Package, erhält dadurch aber
keine Preset-Write- oder Promotion-Authority. / *RAW-05 retains execution-node
ownership and RAW-06 retains CLI and process ownership. RAW-08 consumes only
their evidence and owns neither node nor process authority. RAW-09 consumes the
knowledge package without gaining preset-write or promotion authority.*

## Quellen, Findings und typisierte Handoffs / Sources, findings, and typed handoffs

Quellen sind SRC-159, SRC-168 und SRC-174 aus dem
[Source Pack](../../baseline/source-pack.md), RF-03, RF-12 und RF-14 aus dem
[Findings Ledger](../../baseline/review-findings-ledger.md), der
[Execution Node Contract](../../baseline/execution-node-contract.json), der
[CLI Capability Contract](../../baseline/cli-capability-contract.json) und der
maschinenlesbare
[Workflow Evidence Contract](../../baseline/workflow-evidence-contract.json).
/ *Sources are the named Source Pack and Findings Ledger entries plus the
versioned RAW-05, RAW-06, and RAW-08 machine-readable contracts.*

Die Handoffs sind: / *The handoffs are:*

1. `H-RAW05-RAW08`: RAW-05 → RAW-08, `Node Health and Freshness Assessment`,
   `requirements-v1`, bindende Assessment Baseline. Required sind Node-ID,
   State, Health, Freshness, Attestation, Reason Codes, Zeitpunkte und
   Policy-Version. Unknown, Untrusted, Stale, Expired oder Unavailable blockiert
   oder degradiert sichtbar und erteilt nie Execution Authority. / *A binding
   read-only assessment input; incomplete or untrusted node evidence never
   authorises execution.*
2. `H-RAW06-RAW08`: RAW-06 → RAW-08, `CLI Execution Evidence`,
   `requirements-v1`, bindendes Hard-Completion-Gate. Required sind
   Correlation-/Capability-/Node-ID, Outcome, Zeiten, getrennte Output Records,
   Partial-Flag, Reason Code und Inhaltshash. Fehlende, unbekannte, abgebrochene
   oder fehlgeschlagene Evidence bleibt partial oder negativ. / *A binding CLI
   evidence input; incomplete or failed evidence cannot become successful
   execution evidence.*
3. `H-RAW08-RAW09`: RAW-08 → RAW-09, `Evidence and Retrospective Knowledge
   Package`, `requirements-v1`, bindender Final-Audit-Input. Required sind
   Source-, Decision-, Evidence- und Retrospective-IDs, Traceability-Root-Hash,
   Attestation und Compatibility-Version. Fehlende Traceability, ungültige
   Attestation, private Inhalte oder inkompatible Version blockieren Proposal
   Completion. / *A binding final-audit input; invalid provenance or private
   content blocks proposal completion.*

Die vier später möglichen Child-Intakes besitzen jeweils RAW-08 als Owner und
genau einen Output: Lifecycle Transition Receipt, hashgebundener Traceability
Graph, Evidence/Receipt Contract oder nichtnormatives Retrospective Package.
Sie werden hier nur als reviewbare Grenzen beschrieben und nicht erstellt. /
*The four possible child intakes retain RAW-08 ownership and one output each.
They are reviewable boundaries only and are not created here.*

## Security, Privacy, A11Y, Plattform und Lieferkette / Security, privacy, A11Y, platform, and supply chain

- **Security:** Hashes, Attestation, Trust Policy, Übergänge und aktuelle
  Authority prüfen fail-closed. Secret-Werte, private Schlüssel und Credentials
  sind verboten. / *Hashes, attestation, trust policy, transitions, and current
  authority fail closed. Secret values, private keys, and credentials are
  prohibited.*
- **Privacy und Public Content:** Evidence wird minimiert und de-identifiziert.
  Private Hostpfade, Benutzernamen, Geräteseriennummern und unnötige
  Personendaten sind verboten. Öffentliche Knowledge Packages enthalten nur
  reviewte Inhalte und logische repository-relative Referenzen. / *Evidence is
  data-minimised and de-identified. Public packages contain only reviewed
  content and logical repository-relative references.*
- **Accessibility:** Nutzerseitige Status-, Reason-, Evidence- und Workflow-
  Projektionen benötigen stabile Codes, vollständige deutsche und englische
  Texte sowie Tastatur- und Textalternativen. Bedeutung darf nicht nur von
  Farbe, Klang, Bewegung oder Position abhängen. WCAG 2.2 AA gilt, soweit auf
  das Artefakt anwendbar. / *User-facing projections require stable codes,
  complete German and English text, keyboard and text alternatives, and WCAG
  2.2 AA where applicable. Meaning must not rely on colour, sound, motion, or
  position alone.*
- **Plattformen und Nodes:** macOS, Linux und Windows verwenden dieselben
  logischen Zustände und Reason Codes. Container, WSL, ABS-DD und Remote Nodes
  behalten eigene Identität, Trust Zone, Mount-, Freshness- und Provider-
  Evidence. Fehlende Provenienz blockiert Completion. / *macOS, Linux, and
  Windows share logical outcomes. Container and remote evidence retains node
  identity and trust boundaries; missing provenance blocks completion.*
- **Sprache:** Deutsch steht zuerst und ist maßgeblich; Englisch folgt
  semantisch gleichwertig. Zielniveau ist CEFR B2. / *German is authoritative
  and first; semantically equivalent English follows at CEFR B2.*
- **Software-Lieferkette:** Für den Requirements-Vertrag und die
  dependency-freien Offline-Fixtures ist die Einstufung `N/A`. Jede spätere
  Implementierungsdependency verlangt Lizenz-, Provenienz-, SBOM-,
  Vulnerability-, Plattform- und Wartungsnachweis. / *Supply-chain assessment
  is N/A for this requirements contract and dependency-free fixtures. Any
  later dependency requires the listed evidence.*

## Anforderungen / Requirements

- **FR-001 – Artifact Model:** Jedes Artefakt MUSS Schema-Version, stabile ID,
  Typ, Source-IDs, Status, Owner, Revision und SHA-256 besitzen. / *Every
  artifact MUST contain the listed stable identity and hash fields.*
- **FR-002 – Lifecycle:** Ein Übergang MUSS im versionierten Allowed-
  Transition-Set liegen und Transition-ID, From/To, Preconditions, aktuelle
  Authority, Input-Hashes, Output-Hash, Receipt, Zeitpunkt und Reason Code
  binden. Unbekannte Übergänge, fehlende Preconditions, fehlende Authority und
  Hash-Drift ergeben `Blocked`. / *Every transition MUST be allowed and bind
  the listed evidence. Unknown transitions or missing evidence are Blocked.*
- **FR-003 – Evidence Classes:** Evidence MUSS `Positive`, `Negative` oder
  `ProviderFailure` sein. Provider Failure darf keine Completion behaupten und
  MUSS vorhandene Partial Evidence bewahren. / *Evidence MUST use one of the
  three classes. Provider failure cannot claim completion and preserves partial
  evidence.*
- **FR-004 – Retrospective Boundary:** Eine Retrospektive DARF Beobachtungen
  und Learnings übergeben, aber keine normative Decision oder Preset-Promotion
  erzeugen. / *A retrospective MAY pass observations but MUST NOT create a
  normative decision or preset promotion.*
- **FR-005 – Persistenz:** IAD801 MUSS als versioniertes kanonisches JSON unter
  `evidence/workflow/<workflow-id>/`, same-directory Temporary Write,
  Validierung, atomarem Replace, Receipt-last und Recovery vom letzten vollständig
  validierten hashgebundenen Receipt gelten. Eine Datenbank darf nur
  ableitbarer Index sein. / *IAD801 MUST govern canonical JSON, atomic
  publication, receipt-last ordering, and receipt-bound recovery. A database
  may only be a derived index.*
- **FR-006 – Attestation:** IAD802 MUSS ein versioniertes standardisiertes
  Attestation Envelope mit abgetrennter Signatur über den kanonischen
  SHA-256-Inhaltshash und separat versionierter Trust Policy binden. Fehlende
  oder ungültige Signatur, unbekannter Key/Trust Root, Hash-Drift oder
  abgelaufene Policy ergeben `Blocked`. / *IAD802 MUST bind a detached
  attestation envelope and versioned trust policy. Every invalid trust state is
  Blocked.*
- **FR-007 – Retention:** IAD803 MUSS Governance-/Decision-/Completion-
  Receipts für die Projektlebensdauer archivieren, operative Evidence nach 90
  Tagen und Security-/Failure-Evidence nach zwölf Monaten behandeln. Legal
  Hold setzt Löschung aus; jede Löschung benötigt ein Receipt. / *IAD803 MUST
  apply project-lifetime, 90-day, and twelve-month retention as confirmed,
  including legal hold and deletion receipts.*
- **FR-008 – Traceability und Knowledge Package:** Jede Knowledge Package MUSS
  die versionierten IDs von Source bis Retrospektive, Traceability-Root-Hash,
  Attestation und Compatibility-Version binden. / *Every knowledge package
  MUST bind the complete traceability chain, hash, attestation, and version.*
- **FR-009 – Handoffs:** RAW-05-, RAW-06- und RAW-09-Handoffs MÜSSEN Producer,
  Consumer, Version, Required Fields, Authority, Compatibility, Failure
  Behavior und bindende Series-Relation enthalten. / *Every handoff MUST bind
  producer, consumer, version, fields, authority, compatibility, failure
  behaviour, and Series relation.*
- **FR-010 – Authority:** Autonomous Execution MUSS separate aktuelle Scope-,
  Start-, Implementierungs-, Governance-Write-, Remote-Write-, Merge-, Bypass-
  und Provider-Authority prüfen. Historisches MergeAndSync, `Eligible` oder
  `Ready` genügt nie. Fehlt ein Gate, ist das Ergebnis `Blocked`. / *Autonomous
  execution MUST verify all eight separate current authorities. Historical
  delivery, Eligible, or Ready is never sufficient.*
- **FR-011 – Fehlervertrag:** Validator und spätere Projektionen MÜSSEN stabile
  `WFE001` bis `WFE014` Reason Codes verwenden. Erwartete Negativ-Evidence ist
  bestanden, wenn der gebundene Ablehnungs- oder Blockstatus mit Exitcode `0`
  erkannt wird; Validator-, Schema- oder Fixturefehler enden mit Exitcode `2`.
  / *Validation MUST use stable WFE reason codes. Expected rejection is passing
  negative evidence with exit code 0; validator errors use exit code 2.*
- **NFR-001 – Reproduzierbarkeit und Parität:** Vertrag und Fixtures MÜSSEN
  offline, dependency-frei und auf Bash sowie PowerShell mit identischen
  Status, Reason Codes und Exitcodes prüfbar sein. / *Contract and fixtures
  MUST be offline, dependency-free, and identical across both shell surfaces.*
- **NFR-002 – Sprache und A11Y:** Nutzerseitiger Text MUSS DE-first,
  EN-second, CEFR B2 und WCAG 2.2 AA erfüllen und Text-/Tastaturalternativen
  besitzen. / *User-facing text MUST meet the language and accessibility
  contract.*
- **NFR-003 – Datenschutz:** Secrets, Credentials, private Schlüssel, private
  Hostpfade und unnötige Personendaten DÜRFEN nicht in Evidence, Logs,
  Receipts oder Knowledge Packages erscheinen. / *Sensitive or unnecessary
  personal data MUST NOT enter evidence.*
- **NFR-004 – Plattformparität:** macOS, Linux und Windows MÜSSEN dieselben
  logischen Zustände und Reason Codes liefern; fehlende Node-Provenienz ergibt
  `Blocked`, nicht geratenen Erfolg. / *All three platforms MUST share logical
  outcomes; missing node provenance is Blocked.*
- **NFR-005 – Supply Chain:** Neue Implementierungsdependencies MÜSSEN vor
  Nutzung Lizenz, Provenienz, SBOM und Vulnerability Evidence besitzen. / *New
  implementation dependencies MUST have the named supply-chain evidence.*

## Bestätigte Decisions, Lifecycle, Mode und Recovery / Confirmed decisions, lifecycle, mode, and recovery

Die drei materiellen Decisions bleiben unverändert bestätigt: / *The three
material decisions remain confirmed without change:*

1. **IAD801 – Persistenz:** Versionierte kanonische JSON-Artefakte liegen
   unter `evidence/workflow/<workflow-id>/`; atomare Veröffentlichung schreibt
   und validiert temporär im selben Verzeichnis, ersetzt das Ziel und publiziert
   das Receipt zuletzt. Recovery verwendet nur das letzte vollständig
   validierte hashgebundene Receipt. / *Versioned canonical JSON, same-directory
   atomic publication, receipt-last ordering, and last-valid-receipt recovery.*
2. **IAD802 – Signatur und Attestation:** Versioniertes standardisiertes
   Attestation Envelope mit abgetrennter Signatur über den kanonischen
   Inhaltshash; Key-ID, Signaturprofil und Trust Roots stehen in einer separat
   versionierten Trust Policy. Ungültige oder fehlende Evidence blockiert. /
   *A detached standard attestation envelope and separately versioned trust
   policy fail closed.*
3. **IAD803 – Retention:** Governance-, Decision- und Completion-Receipts
   bleiben für die Projektlebensdauer; operative Evidence bleibt 90 Tage,
   Security-/Failure-Evidence zwölf Monate. Legal Hold setzt Löschung aus und
   jede Löschung erzeugt ein Receipt. / *Project-lifetime receipts, 90-day
   operational evidence, twelve-month security or failure evidence, legal
   hold, and deletion receipts.*

Die Lifecycle-Zustände sind `Draft`, `Validated`, `Approved`, `InProgress`,
`Blocked`, `Completed`, `Superseded` und `Expired`. Erlaubt sind ausschließlich
die acht Übergänge des Workflow Evidence Contract. Der aktuelle Mode bleibt
`research-only`. `serial-autonomous` ist nur eine spätere Möglichkeit nach
vollständigem Review und allen separaten aktuellen Authority-Gates. Recovery
erfindet keinen Zustand, verwirft keine Provider-Failure-Evidence und setzt nur
am letzten validierten Receipt fort. / *The lifecycle and eight allowed
transitions are contract-bound. The current mode remains research-only.
Serial autonomous is only a later possibility after review and all current
authority gates. Recovery never invents state or discards provider-failure
evidence.*

## Akzeptanzkriterien und ausführbare Offline-Evidence / Acceptance criteria and executable offline evidence

- **AC-001:** Die positive Fixture enthält alle elf Artefakttypen, drei
  Evidence-Klassen, drei kompatible Handoffs, vollständige Traceability,
  gültige Hashes und Attestation sowie die bestätigten Retention-Werte. Sie
  ergibt `WFE001_VALID`. / *The positive fixture covers the complete
  source-to-retrospective path and returns WFE001_VALID.*
- **AC-002:** `Draft->Completed` ohne Preconditions wird mit
  `WFE002_INVALID_TRANSITION` abgelehnt. / *The invalid transition is
  rejected with WFE002.*
- **AC-003:** Historisches MergeAndSync, Eligibility und Ready ohne alle acht
  aktuellen Authorities ergibt `Blocked` und `WFE003_AUTHORITY_MISSING`. /
  *Missing current authority returns Blocked and WFE003.*
- **AC-004:** Provider Failure bleibt `BlockedWithPartialEvidence`, behauptet
  keine Completion und ergibt `WFE005_PROVIDER_FAILURE`. / *Provider failure
  preserves partial evidence and returns WFE005.*
- **AC-005:** Ungültige Signatur, Key/Trust Root oder Policy ergibt `Blocked`
  und `WFE006_SIGNATURE_INVALID`. / *Invalid attestation returns WFE006.*
- **AC-006:** Operative Evidence nach 91 Tagen ohne Legal Hold oder
  Lösch-Receipt wird mit `WFE007_RETENTION_VIOLATION` abgelehnt. / *The
  retention violation returns WFE007.*
- **AC-007:** Ein inkompatibler RAW-06-Handoff wird mit
  `WFE008_HANDOFF_INCOMPATIBLE` blockiert. / *The incompatible handoff returns
  WFE008.*
- **AC-008:** Private Daten, fehlende A11Y-Alternativen, Plattformdrift und
  neue Dependency ohne SBOM/Vulnerability Evidence ergeben gemeinsam
  `WFE009`, `WFE010`, `WFE011` und `WFE012`. / *The cross-cutting fixture
  returns WFE009 through WFE012.*
- **AC-009:** Bash und PowerShell liefern je Fixture dieselbe sichtbare DE/EN-
  Zeile und Exitcode `0`; erwartete Ablehnung oder Blockierung ist bestandene
  Negativ-Evidence. / *Both surfaces produce identical bilingual output and
  exit code 0 for positive and expected negative evidence.*
- **AC-010:** Vertrag, Fixtures, Python-, Bash- und PowerShell-Oberflächen
  enthalten keine Produkt-, Netzwerk-, Signatur- oder sonstige Side Effect. /
  *The contract and validators perform no product, network, signing, or other
  side effect.*

Die acht Prüfungen werden auf beiden Oberflächen ausgeführt: / *The eight
checks run on both surfaces:*

```text
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/valid-source-to-retrospective.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-invalid-transition.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-missing-authority.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-provider-failure.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-invalid-attestation.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-retention-violation.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-incompatible-handoff.json
bash specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.sh --contract requirements/baseline/workflow-evidence-contract.json --fixture specs/intake-review-fixtures/raw-08/negative-cross-cutting.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/valid-source-to-retrospective.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-invalid-transition.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-missing-authority.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-provider-failure.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-invalid-attestation.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-retention-violation.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-incompatible-handoff.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-08/validate-workflow-evidence-contract.ps1 -Contract requirements/baseline/workflow-evidence-contract.json -Fixture specs/intake-review-fixtures/raw-08/negative-cross-cutting.json
```

Die Sollausgabe nennt jeweils Fixture-ID, bilingualen Status und gebundenen
`WFE`-Code; jeder erwartete Lauf endet mit Exitcode `0`. Unbekannte Fixture,
ungültiges JSON oder Vertragsdrift endet mit `ERROR: WFE000...` und Exitcode
`2`. / *Expected output names fixture ID, bilingual status, and bound WFE code
with exit code 0. Invalid input returns WFE000 and exit code 2.*

## Status, Reihenfolge, Authority und nächste Aktion / Status, order, authority, and next action

1. RAW-05 und RAW-06 stehen in der Series auf `Completed` und liefern die
   bindenden Vorgängerverträge. / *RAW-05 and RAW-06 are Completed and provide
   the binding predecessor contracts.*
2. RAW-08 bleibt der einzige deklarierte `Eligible`-Kandidat. Eligibility
   beschreibt Reihenfolge, nicht Startautorität. / *RAW-08 remains the sole
   Eligible candidate; Eligibility is order, not start authority.*
3. IAD801 bis IAD803 sind beantwortet; es gibt keine offene RAW-08-Decision. /
   *IAD801 through IAD803 are answered with no open RAW-08 decision.*
4. Die einzige durch diesen Repair-Auftrag gestartete Folgeaktion ist das
   vollständige Single Review. / *The only downstream action started by this
   repair authority is the complete Single review.*
5. RAW-09 bleibt bis zu einem gültigen RAW-08-Handoff und seinen eigenen
   Decisions blockiert. / *RAW-09 remains blocked by the RAW-08 handoff and its
   own decisions.*

`ReadyForReview`, ein späteres `Ready`, `Eligible`, kopierbare Prompts oder die
historische Delivery-Obergrenze `MergeAndSync` erteilen keine aktuelle Scope-,
Start-, Implementierungs-, Governance-Write-, Remote-Write-, Merge-, Bypass-,
Provider-, Preset-, Promotion-, GitHub- oder Level-0-Autorität. Fehlt eine
benötigte aktuelle Authority oder ist sie abgelaufen, MUSS jeder Prompt
fail-closed stoppen. / *No review state, lifecycle value, prompt, or historical
delivery ceiling grants current downstream authority. Missing or expired
authority MUST fail closed.*

## Re-Evaluation und Nicht-Autorität / Re-evaluation and non-authority

Re-Review ist erforderlich, wenn Artefakttyp, Lifecycle, Transition,
Evidence-Klasse, Reason Code, Persistence, Attestation, Trust Policy,
Retention, Legal Hold, Handoff, Plattform, Node-Typ, Public-Data-Kategorie,
A11Y-Projektion, Dependency oder Authority-Gate geändert wird. Gleiches gilt,
wenn Produkt-, Remote-, Merge-, Bypass-, Provider-, Preset-, Promotion-,
GitHub- oder Level-0-Arbeit vorgeschlagen wird. / *Re-review is required when
any named contract, cross-cutting boundary, dependency, or authority gate
changes.*

Dieser Repair-Auftrag ändert keine IAD-Decision, keinen Zweck, Scope,
Non-Goal, Dependency Owner, Series-Lifecycle oder Delivery Authority. Er
erteilt keine Ausführung über Requirements-, Offline-Fixture- und vollständige
Review-Arbeit hinaus. / *This repair changes no confirmed decision, purpose,
scope, non-goal, dependency owner, Series lifecycle, or delivery authority and
grants no execution beyond requirements, offline fixtures, and the complete
review.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

Diese Vorlagen sind nur nach separater aktueller Authority kopierbar. Jeder
`--require-current-*`-Gate ist bindend; fehlt ein Gate, stoppt der Lauf vor
jeder Änderung. / *These templates are copy-ready only with separate current
authority. Every require-current gate is binding; a missing gate stops before
any change.*

<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --bind-exact-intake --no-implementation --no-remote-writes --require-current-scope-authority --require-current-start-authority --require-current-implementation-authority --require-current-governance-write-authority --require-current-remote-write-authority --require-current-merge-authority --require-current-bypass-authority --require-current-provider-authority
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md --delivery-mode MergeAndSync --require-current-review --require-current-scope-authority --require-current-start-authority --require-current-implementation-authority --require-current-governance-write-authority --require-current-remote-write-authority --require-current-merge-authority --require-current-bypass-authority --require-current-provider-authority
```
<!-- intake-authoring:end -->
