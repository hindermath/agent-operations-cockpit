<!-- intake-authoring:begin -->
# RAW-06 – CLI Capability und Environment Orchestration / CLI Capability and Environment Orchestration

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** Terminal, Prozess, Exitcode und Umgebungsvariable; keine interne AOC-Entstehungsgeschichte / terminal, process, exit code, and environment-variable basics; no internal AOC history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

CLI-Werkzeuge besitzen plattformspezifische Prozess-, Exit-, Signal- und
Environment-Eigenschaften. Ohne gemeinsamen Vertrag könnten Shell-Injection,
unterschiedliche Fehlerbedeutungen, unbeabsichtigte Environment-Vererbung oder
unautorisierte Remote-Ausführung entstehen. Ziel ist ein typisierter,
shell-freier und plattformneutraler CLI-Capability-Vertrag mit fail-closed
Authority. / *CLI tools have platform-specific process, exit, signal, and
environment behaviour. Without a common contract, shell injection, divergent
failure meaning, unintended environment inheritance, or unauthorised remote
execution could result. The target is a typed, shell-free, platform-neutral
CLI capability contract with fail-closed authority.*

Dieses Lastenheft beschreibt Requirements und reproduzierbare Contract-
Evidence. Es startet keinen Prozess, öffnet keine SSH-Verbindung und erteilt
keine Command-, Remote- oder Produktautorität. / *This intake defines
requirements and reproducible contract evidence. It starts no process, opens
no SSH connection, and grants no command, remote, or product authority.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Capability / Fähigkeit:** eine versionierte, typisierte Beschreibung einer
  erlaubten Werkzeugaktion mit Input, Output, Authority und Fehlervertrag. /
  *A versioned, typed description of an allowed tool action with input,
  output, authority, and failure contract.*
- **Process API / Prozessschnittstelle:** der Vertrag für Startanfrage,
  Ergebnis, Output, Timeout und Abbruch eines Prozesses. Die konkrete
  Betriebssystem-API bleibt Implementierungsdetail. / *The contract for a
  process start request, result, output, timeout, and cancellation. The actual
  operating-system API remains an implementation detail.*
- **Shell-Evaluation:** Auswertung eines zusammengesetzten Befehlsstrings durch
  eine Shell. RAW-06 verbietet sie für Capability-Aufrufe. / *Evaluation of a
  combined command string by a shell. RAW-06 forbids it for capability calls.*
- **Environment Allowlist / Umgebungs-Allowlist:** eine versionierte Liste der
  für eine Capability und einen Node ausdrücklich erlaubten Variablen samt
  Quelle und Zweck. / *A versioned list of variables explicitly allowed for a
  capability and node, including source and purpose.*
- **Native Details / native Details:** unverändert erfasster Exitcode oder
  Signalwert der Plattform zusätzlich zur normalisierten Bedeutung. /
  *The platform exit code or signal value preserved alongside the normalised
  meaning.*
- **Partial Output / Teilausgabe:** bis zu Timeout, Abbruch oder Fehler
  beobachtete, als unvollständig gekennzeichnete Standard- und Fehlerausgabe. /
  *Standard and error output observed before timeout, cancellation, or failure
  and marked as incomplete.*
- **Remote Endpoint / Remote-Endpunkt:** ein fester AOC-Endpunkt, der eine
  strukturierte Anfrage annimmt. Er ist keine allgemeine Remote-Shell. /
  *A fixed AOC endpoint that accepts a structured request. It is not a general
  remote shell.*
- **Authority / Autorität:** aktuelle ausdrückliche Erlaubnis für den genauen
  Node, die Capability und die Side-Effect-Klasse. Review- oder Lifecycle-
  Status ersetzen sie nicht. / *Current explicit permission for the exact
  node, capability, and side-effect class. Review or lifecycle status does not
  replace it.*

Weitere Begriffe erklärt das [zweisprachige Glossar](../../baseline/glossary.md).
/ *The [bilingual glossary](../../baseline/glossary.md) explains additional
terms.*

## Scope, Systemgrenze und Non-Goals / Scope, system boundary, and non-goals

Im Scope liegen Capability Descriptor, sichere Prozessanfrage, normalisierte
Ergebnisse, native Exit-/Signaldetails, Output, Timeout, Cancellation,
Environment-Policy sowie der deaktivierte SSH-v2-Referenzadapter. RAW-06
konsumiert den RAW-05-Node-Vertrag und liefert Capability Descriptor an RAW-02
sowie de-identifizierte Execution Evidence an RAW-08. / *Scope includes the
capability descriptor, safe process request, normalised outcomes, native exit
and signal details, output, timeout, cancellation, environment policy, and the
disabled SSHv2 reference adapter. RAW-06 consumes the RAW-05 node contract and
provides capability descriptors to RAW-02 plus de-identified execution
evidence to RAW-08.*

Nicht im Scope sind UI, Hardware, Workspace Discovery, State-Ownership,
Produktcommand-Policy, Credential-Speicherung, eine allgemeine Shell,
Remote-Aktivierung, Produktimplementierung, Preset- oder Level-0-Arbeit. /
*UI, hardware, workspace discovery, state ownership, product command policy,
credential storage, a general shell, remote activation, product
implementation, presets, and Level-0 work are out of scope.*

RAW-02 besitzt weiterhin den transportneutralen logischen Orchestration-
Vertrag. RAW-05 besitzt Node-Identität, Trust, Mounts und Freshness. RAW-06
besitzt ausschließlich konkrete Prozess-, Environment- und Transportadapter-
Requirements. / *RAW-02 retains the transport-neutral logical orchestration
contract. RAW-05 owns node identity, trust, mounts, and freshness. RAW-06 owns
only concrete process, environment, and transport-adapter requirements.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

Quellen sind SRC-162 und SRC-177 aus dem
[Source Pack](../../baseline/source-pack.md), RF-07 und RF-10 aus dem
[Findings Ledger](../../baseline/review-findings-ledger.md), der RAW-02-
Orchestration Contract sowie der RAW-05
[Execution Node Contract](../../baseline/execution-node-contract.json). Der
maschinenlesbare RAW-06-Vertrag liegt in
[`cli-capability-contract.json`](../../baseline/cli-capability-contract.json).
/ *Sources are the named Source Pack entries and findings, the RAW-02
orchestration contract, and the RAW-05 execution-node contract. The linked
JSON file is the machine-readable RAW-06 contract.*

Die Handoffs sind: / *The handoffs are:*

1. `H-RAW05-RAW06`: RAW-05 → RAW-06, `Node Capability and Authority Contract`,
   `requirements-v1`, bindendes Hard-Completion-Gate. Fehlende, unbekannte,
   untrusted, stale oder unavailable Node-Evidence autorisiert keine
   Ausführung. / *Binding node and authority input; insufficient evidence
   authorises no execution.*
2. `H-RAW06-RAW02`: RAW-06 → RAW-02, `CLI Capability Descriptor`,
   `requirements-v1`, funktionaler Handoff. Fehlende oder ungültige Capability
   bleibt unavailable und autorisiert keinen Command. / *A functional handoff;
   a missing or invalid capability remains unavailable and authorises no
   command.*
3. `H-RAW06-RAW08`: RAW-06 → RAW-08, `CLI Execution Evidence`,
   `requirements-v1`, bindender Folge-Handoff. Unvollständige Evidence bleibt
   sichtbar partial und gilt nicht als erfolgreiche Ausführung. / *A binding
   downstream handoff; incomplete evidence stays visibly partial and is not a
   successful execution.*

## Security, Privacy, A11Y, Plattform und Lieferkette / Security, privacy, A11Y, platform, and supply chain

- **Security:** Executable und Argumentarray MÜSSEN getrennt sein. Untrusted
  Input DARF nie Shell-Evaluation, Executable-Auswahl oder Environment-
  Erweiterung auslösen. Fehlende Node-, Capability- oder Authority-Evidence
  MUSS fail-closed blockieren. / *Executable and argument array MUST be
  separate. Untrusted input MUST never trigger shell evaluation, executable
  selection, or environment expansion. Missing node, capability, or authority
  evidence MUST block fail closed.*
- **Secrets:** Secrets DÜRFEN nur als opake Referenz übergeben werden. Werte
  DÜRFEN nicht in Descriptor, Argumentdarstellung, Output, Log, Review oder
  Receipt erscheinen. / *Secrets may be passed only as opaque references.
  Values MUST NOT appear in descriptors, rendered arguments, output, logs,
  reviews, or receipts.*
- **Privacy:** Benutzername, private absolute Pfade, Hostname und Remote-
  Endpunktdetails werden auf den belegten Zweck minimiert oder redigiert.
  Public Evidence enthält keine Registry-Daten oder Credentials. / *User
  names, private absolute paths, host names, and remote endpoint details are
  minimised or redacted. Public evidence contains no registry data or
  credentials.*
- **Accessibility:** Nutzerseitige Zustände, Fehler und Abbruchergebnisse
  MÜSSEN sichtbare DE/EN-Textlabels und stabile Reason Codes besitzen. Farbe,
  Klang oder räumliche Position allein genügen nicht. / *User-facing states,
  failures, and cancellation results MUST have visible DE/EN text labels and
  stable reason codes. Colour, sound, or position alone is insufficient.*
- **Sprache:** Deutsch ist zuerst maßgeblich, Englisch folgt semantisch
  gleichwertig. Zielniveau ist CEFR B2. / *German is authoritative and first;
  semantically equivalent English follows. The target level is CEFR B2.*
- **Cross-Platform:** Dieselbe Anfrage MUSS auf macOS, Linux und Windows
  dieselbe normalisierte Ergebnis- und Fehlerbedeutung besitzen. Native Codes
  und Signale bleiben zusätzlich sichtbar, ohne die gemeinsame Semantik zu
  ersetzen. / *The same request MUST have the same normalised outcome and
  failure meaning on macOS, Linux, and Windows. Native codes and signals stay
  visible without replacing the shared semantics.*
- **Software-Lieferkette:** Für dieses Requirements-Update und seine
  dependency-freien Fixtures ist die Einstufung `N/A`. Jede spätere Process-
  oder SSH-Abhängigkeit erzwingt Lizenz-, Provenienz-, SBOM- und
  Vulnerability-Evidence. / *Supply-chain assessment is N/A for this
  requirements-only update and its dependency-free fixtures. A later process
  or SSH dependency requires licence, provenance, SBOM, and vulnerability
  evidence.*

## Anforderungen / Requirements

- **FR-001 – Capability Descriptor:** Jede Capability MUSS stabile ID,
  Schemaversion, Executable Identity, Versionsevidence, Node-Typen,
  Argument- und Outputschema, Environment- und Timeout-Profil, Cancellation,
  Side-Effect-Klasse und Authority-Anforderungen enthalten. / *Every
  capability MUST contain the listed identity, schema, execution, policy, and
  authority fields.*
- **FR-002 – Shell-freie Anfrage:** Executable Identity und Argumentarray
  MÜSSEN getrennt sein. Zusammengesetzte Command-Strings und Shell-Evaluation
  aus untrusted Input sind verboten. / *Executable identity and argument array
  MUST be separate. Combined command strings and shell evaluation from
  untrusted input are forbidden.*
- **FR-003 – Prozessanfrage:** Eine Anfrage MUSS Capability, Executable, Node,
  Argumente, logische Working-Directory-Referenz, Environment- und Timeout-
  Profil, Cancellation Handle, Correlation ID und Side-Effect-Klasse binden. /
  *A request MUST bind the capability, executable, node, arguments, logical
  working-directory reference, environment and timeout profiles,
  cancellation handle, correlation ID, and side-effect class.*
- **FR-004 – Ergebnissemantik:** Ergebnisse sind genau `Succeeded`,
  `ExitedNonZero`, `StartFailed`, `TimedOut`, `Cancelled`, `Signaled` oder
  `ToolMissing`. Nativer Exitcode oder Signalwert wird zusätzlich erhalten. /
  *Outcomes are exactly the named values. A native exit code or signal is
  preserved in addition.*
- **FR-005 – Output:** Standard- und Fehlerausgabe MÜSSEN getrennte Records in
  beobachteter Stream-Reihenfolge liefern. Eine totale Reihenfolge zwischen
  beiden Streams DARF nicht erfunden werden. Teilausgabe bleibt erhalten und
  wird als partial markiert. / *Standard and error output MUST use separate
  records in observed per-stream order. A total cross-stream order MUST NOT be
  invented. Partial output is preserved and marked partial.*
- **FR-006 – Abbruch und Retry:** Cancellation betrifft nur die gebundene
  Prozessinstanz. Prozessbaum-Terminierung ist nicht implizit. Unbekannte oder
  nicht-idempotente Aktionen werden nie automatisch wiederholt. / *Cancellation
  applies only to the bound process instance. Process-tree termination is not
  implicit. Unknown or non-idempotent actions are never retried automatically.*
- **FR-007 – Environment:** Jede erlaubte Variable MUSS je Capability und Node
  versioniert mit Name, Quelle und Zweck deklariert sein. Das Eltern-
  Environment wird nicht standardmäßig übernommen; unbekannte Variablen und
  gefährliche Loader-, Shell-, Suchpfad- oder Hook-Kategorien werden
  abgelehnt. / *Every allowed variable MUST be versioned per capability and
  node with name, source, and purpose. The parent environment is not inherited
  by default; unknown variables and dangerous loader, shell, search-path, or
  hook categories are rejected.*
- **FR-008 – Secret Injection:** Nur Secret-Referenzen sind zulässig. Fehlende
  Referenzauflösung blockiert, ohne Wert oder Metadaten offenzulegen. /
  *Only secret references are allowed. Failed resolution blocks without
  exposing the value or metadata.*
- **FR-009 – Capability-Klassen:** `ReadOnlyProbe`, `ReversibleMutation` und
  `IrreversibleMutation` sind getrennt. Der erste Slice bleibt read-only;
  mutierende Klassen benötigen spätere eigene Requirements und Authority. /
  *Read-only, reversible, and irreversible classes are separate. The first
  slice remains read-only; mutating classes require later requirements and
  authority.*
- **FR-010 – Remote-Vertrag:** Der Remote-Vertrag bleibt transportneutral;
  SSHv2 ist nur der erste optionale Referenzadapter und standardmäßig
  deaktiviert. Eine fehlende Aktivierung ergibt `CLI009_REMOTE_DISABLED`. /
  *The remote contract remains transport neutral; SSHv2 is only the first
  optional reference adapter and is disabled by default. Missing activation
  yields CLI009_REMOTE_DISABLED.*
- **FR-011 – SSH-Grenze:** Aktivierung erfordert geprüfte Hostidentität,
  Schlüssel- oder Zertifikatsauthentifizierung, Credential-Referenzen, einen
  festen Remote-Endpunkt und strukturierte Requests. Allgemeine Remote-Shell,
  Agent Forwarding, Remote Write und automatisch abgeleitete Prozessautorität
  sind verboten. / *Activation requires verified host identity, key or
  certificate authentication, credential references, a fixed remote endpoint,
  and structured requests. A general remote shell, agent forwarding, remote
  write, and inferred process authority are forbidden.*
- **FR-012 – Parität und Failure:** Erfolg, Nonzero Exit, Startfehler, Timeout,
  Abbruch, Signal und Tool Missing MÜSSEN plattformgleich unterscheidbar sein.
  Fehlende oder ungültige Evidence bleibt blockiert oder unavailable und wird
  nie als Erfolg geraten. / *Success, nonzero exit, start failure, timeout,
  cancellation, signal, and missing tool MUST be distinguishable with equal
  meaning across platforms. Missing or invalid evidence remains blocked or
  unavailable and is never guessed as success.*
- **NFR-001 – Reproduzierbarkeit:** Vertrag und Fixtures MÜSSEN über Bash und
  PowerShell dieselben Ergebnisse, Reason Codes und Exitcodes liefern. /
  *The contract and fixtures MUST produce the same results, reason codes, and
  exit codes through Bash and PowerShell.*
- **NFR-002 – Auditierbarkeit:** Correlation ID, Capability-, Policy- und
  Schemaversion sowie Node- und Authority-Evidence MÜSSEN ohne Secret- oder
  Personendaten bis zur RAW-08-Evidence nachvollziehbar sein. / *Correlation,
  capability, policy, schema, node, and authority evidence MUST remain
  traceable to RAW-08 evidence without secrets or personal data.*

## Bestätigte Decisions, Mode und Authority / Confirmed decisions, mode, and authority

Die vier materiellen Entscheidungen sind bestätigt: / *The four material
decisions are confirmed:*

1. **IAD601 – Process API:** Typisierte, shell-freie Process API mit getrenntem
   Executable und Argumentarray sowie Node, Working Directory, Environment,
   Timeout, Cancellation, Correlation ID und getrenntem Output. Konkrete OS-
   Adapter bleiben austauschbar. / *A typed, shell-free API with separate
   executable and argument array plus the listed execution fields; OS adapters
   remain replaceable.*
2. **IAD602 – Exit-/Signalmodell:** Normalisierte Zustände bewahren native
   Details und Partial Output. Cancellation ist pro Prozessinstanz; unbekannte
   und nicht-idempotente Aktionen werden nicht automatisch wiederholt. /
   *Normalised outcomes preserve native details and partial output.
   Cancellation is per process instance; unknown and non-idempotent actions
   are not retried automatically.*
3. **IAD603 – Environment Allowlist:** Versionierte, fail-closed Allowlist je
   Capability und Node; keine pauschale Elternvererbung; Secrets nur als
   Referenz; gefährliche Variablenkategorien standardmäßig gesperrt. /
   *A versioned, fail-closed allowlist per capability and node; no blanket
   parent inheritance; secret references only; dangerous variable categories
   blocked by default.*
4. **IAD604 – Remote Transport:** Transportneutraler Vertrag mit SSHv2 als
   erstem optionalen Referenzadapter. Remote bleibt deaktiviert, bis ein
   separates Security Review, positive und negative Transport-Evidence sowie
   aktuelle Node-, Capability- und Remote-Authority vorliegen. / *A
   transport-neutral contract with SSHv2 as the first optional reference
   adapter. Remote stays disabled until separate security review, positive and
   negative evidence, and current node, capability, and remote authority exist.*

Beim damaligen Authoring galt als historischer Snapshot: RAW-05 war
`Completed`, RAW-06 war `Blocked` und es gab keinen `Eligible`-Kandidaten.
Dieser Snapshot ist keine aktuelle Lifecycle-Quelle. Der aktuelle kanonische
Zustand steht ausschließlich im
[`manifest.json`](../../../specs/intake-series/aoc-phase-2/manifest.json) und
in der [`order.md`](../series/order.md). Der erlaubte Mode bleibt
`research-only`; `single-autonomous` beschreibt nur einen möglichen späteren,
separat autorisierten Lauf. / *At authoring time, the historical snapshot
recorded RAW-05 as Completed, RAW-06 as Blocked, and no Eligible candidate.
This snapshot is not a current lifecycle source. Only the linked manifest and
order document define the current canonical state. The allowed mode remains
research-only; single-autonomous only describes a possible later, separately
authorised run.*

`ReadyForReview`, ein späteres `Ready`, Lifecycle, kopierbare Prompts und die
historische Delivery-Obergrenze `MergeAndSync` erteilen keine aktuelle Scope-,
Start-, Process-, SSH-, Remote-, Specify-, Implementierungs-, Merge-, Bypass-,
Provider-, Hardware-, Preset- oder Level-0-Autorität. / *ReadyForReview, a
later Ready result, lifecycle, copy-ready prompts, and the historical
MergeAndSync delivery ceiling grant no current scope, start, process, SSH,
remote, Specify, implementation, merge, bypass, provider, hardware, preset, or
Level-0 authority.*

## Akzeptanz und Evidence / Acceptance and evidence

- **AC-001:** Positive Fixtures belegen eine shell-freie Read-only-Anfrage und
  einen Nonzero Exit mit erhaltenem nativen Exitcode. / *Positive fixtures
  prove a shell-free read-only request and a nonzero exit with its native exit
  code preserved.*
- **AC-002:** Shell-Evaluation aus untrusted Input wird mit
  `CLI007_SHELL_EVAL_FORBIDDEN` abgelehnt. / *Shell evaluation from untrusted
  input is rejected with the named code.*
- **AC-003:** Eine nicht allowlistete Environment-Variable ohne Zweck wird mit
  `CLI008_ENVIRONMENT_REJECTED` abgelehnt. / *An unallowlisted environment
  variable without purpose is rejected with the named code.*
- **AC-004:** Remote-Aktivierung ohne separates Review und Authority wird mit
  `CLI009_REMOTE_DISABLED` abgelehnt. / *Remote activation without separate
  review and authority is rejected with the named code.*
- **AC-005:** Secret-Werte in Descriptor oder Log werden mit
  `CLI010_SECRET_MATERIAL_REJECTED` abgelehnt. / *Secret values in a descriptor
  or log are rejected with the named code.*
- **AC-006:** Automatischer Retry einer nicht-idempotenten Aktion wird mit
  `CLI011_RETRY_FORBIDDEN` abgelehnt. / *Automatic retry of a non-idempotent
  action is rejected with the named code.*
- **AC-007:** Beide Validatoroberflächen liefern für alle Fixtures denselben
  sichtbaren DE/EN-Status und Exitcode `0`; erwartete Ablehnung ist bestandene
  negative Evidence. / *Both validator surfaces yield the same visible DE/EN
  status and exit code 0 for all fixtures; expected rejection is passing
  negative evidence.*
- **AC-008:** Die drei Handoffs weisen Producer, Consumer, Vertrag, Version,
  Authority, Failure Behavior und Series Relation nach. / *All three handoffs
  prove producer, consumer, contract, version, authority, failure behaviour,
  and series relation.*

Reproduzierbare Befehle: / *Reproducible commands:*

```text
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/valid-cli-capability-cases.json
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/negative-shell-eval.json
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/negative-environment-injection.json
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/negative-remote-enabled.json
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/negative-secret-material.json
bash specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.sh --contract requirements/baseline/cli-capability-contract.json --fixture specs/intake-review-fixtures/raw-06/negative-nonidempotent-retry.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/valid-cli-capability-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/negative-shell-eval.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/negative-environment-injection.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/negative-remote-enabled.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/negative-secret-material.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-06/validate-cli-capability-contract.ps1 -Contract requirements/baseline/cli-capability-contract.json -Fixture specs/intake-review-fixtures/raw-06/negative-nonidempotent-retry.json
```

## Risiken, Revision und Nichtautorität / Risks, revision, and non-authority

Risiken sind Shell- und Environment-Injection, Secret-Leakage, falsche
plattformübergreifende Semantik, verlorener Partial Output, unbeabsichtigter
Retry, zu breite Prozessbeendigung, unverified SSH-Hostidentität und die
Verwechslung von Evidence mit Authority. Vertrag, Fixtures und Re-Review
begrenzen diese Risiken; sie beweisen keine Produkt-Runtime. / *Risks include
shell and environment injection, secret leakage, incorrect cross-platform
semantics, lost partial output, unintended retry, overbroad process
termination, unverified SSH host identity, and confusion of evidence with
authority. Contract, fixtures, and re-review bound these risks; they do not
prove a product runtime.*

Revision ist erforderlich bei Änderungen an Process API, Outcome, Signal,
Timeout, Cancellation, Retry, Output, Environment, Secret-Auflösung, Node-
Vertrag, Plattform, SSH-Adapter, Remote-Endpunkt, Datenkategorie oder
Implementierungsabhängigkeit sowie bei jeder neuen Side-Effect- oder Remote-
Authority. RAW-06 erteilt keine UI-, Hardware-, State-, Workspace-, Product-
Command-, Credential-, Prozess-, Remote-, Specify-, Implementierungs-, Merge-,
Bypass-, Provider-, Preset- oder Level-0-Autorität. / *Revision is required for
changes to any named contract or authority boundary. RAW-06 grants none of the
listed downstream or external authority.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle sind die ausdrücklich bestätigten
Optionen A für IAD601 bis IAD604; Owner ist RAW-06. Aktualisiert werden dieses
Lastenheft, der maschinenlesbare CLI-Capability-Vertrag, seine Review-Fixtures,
Authoring Receipt, Series-Hashbindung und vollständige Single-Re-Review-
Evidence. / *Decision: UpdateRequired. The explicitly confirmed options A for
IAD601 through IAD604 are the source and RAW-06 is the owner. This intake, its
machine-readable contract, review fixtures, Authoring Receipt, Series hash
binding, and complete Single re-review evidence are updated.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

Die folgenden Befehle sind nur kopierbare Vorlagen. Vor jeder Ausführung
MÜSSEN exakter Zielhash, Authoring Receipt, aktuelles `Ready`-Single-Review,
die AOC-weite globale Review-Sperre und neue ausdrückliche menschliche Scope-,
Start- und Delivery Authority fail-closed geprüft werden. Process-, SSH-,
Remote-, Merge-, Bypass- und Provider-Autorität müssen separat und aktuell
vorliegen. / *The following commands are copy-ready templates only. Before
execution, the exact target hash, Authoring Receipt, current Ready Single
review, AOC-wide global review gate, and fresh explicit human scope, start, and
delivery authority MUST be checked fail closed. Process, SSH, remote, merge,
bypass, and provider authority must be separate and current.*

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md --delivery-mode MergeAndSync --require-current-review
```

<!-- intake-authoring:end -->
