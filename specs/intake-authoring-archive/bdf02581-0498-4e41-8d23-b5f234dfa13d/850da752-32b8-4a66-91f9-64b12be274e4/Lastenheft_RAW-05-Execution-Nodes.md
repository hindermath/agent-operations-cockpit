<!-- intake-authoring:begin -->
# RAW-05 – Execution Nodes / Execution Nodes

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** grundlegende Host-, WSL-, Container- und Sandbox-Begriffe; keine interne Projektgeschichte / basic host, WSL, container, and sandbox terms; no internal project history
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Host, WSL, Container und ABS-DD-Sandbox können heute als Ausführungsorte
auftreten, ohne dass Identität, Trust Zone, Mounts, Capabilities, Freshness und
Authority einheitlich belegt sind. Das kann einen eingeschränkten oder nicht
erreichbaren Node fälschlich als verfügbar erscheinen lassen. RAW-05 definiert
deshalb einen versionierten, transportneutralen Execution-Node-Vertrag und
deterministische read-only Probes. / *Hosts, WSL, containers, and the ABS-DD
sandbox can currently act as execution locations without common evidence for
identity, trust zone, mounts, capabilities, freshness, and authority. This can
make a limited or unavailable node appear usable. RAW-05 therefore defines a
versioned, transport-neutral Execution Node contract and deterministic
read-only probes.*

RAW-05 besitzt Node Descriptor, lokale Endpoint-Grenze, Attestation,
Mount-Authority, Health/Freshness und fail-closed Recovery. Ein Node ist niemals
automatisch Owner einer Produkt-Working-Copy, Home Baseline, CLI-Semantik,
Produktentscheidung oder Delivery Authority. / *RAW-05 owns the Node
Descriptor, local endpoint boundary, attestation, mount authority,
health/freshness, and fail-closed recovery. A node never automatically owns a
product working copy, Home Baseline, CLI semantics, product decisions, or
delivery authority.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Execution Node / Ausführungsknoten:** ein ausdrücklich erkanntes lokales
  Ziel wie Host, WSL, Container oder ABS-DD-Sandbox. Spätere Remote Nodes sind
  in diesem Vertrag deaktiviert. / *An explicitly recognised local target such
  as a host, WSL, container, or ABS-DD sandbox. Later remote nodes are disabled
  by this contract.*
- **Node Descriptor / Node-Beschreibung:** der versionierte Datensatz mit
  stabiler Node-ID, Typ, Plattform, Trust Zone, Capabilities, Mounts, Authority,
  Zeit, Freshness, Health, Attestation und Reason Codes. / *The versioned
  record containing stable node ID, type, platform, trust zone, capabilities,
  mounts, authority, time, freshness, health, attestation, and reason codes.*
- **Node Endpoint:** die transportneutrale Vertragsgrenze für einen lokalen
  read-only Probe. Konkrete Betriebssystem- oder Sandbox-Adapter bleiben
  dahinter verborgen. / *The transport-neutral contract boundary for a local
  read-only probe. Operating-system and sandbox adapters remain behind it.*
- **WSL:** Windows Subsystem for Linux; es ist ein eigener Node und nicht mit
  dem Windows-Host identisch. / *Windows Subsystem for Linux; it is a distinct
  node and not the Windows host itself.*
- **ABS-DD-Sandbox:** die isolierte Agentensandbox mit eigener Node-ID,
  Trust Zone und Mount-Evidence; sie ist nicht Owner des eingebundenen
  Checkouts. / *The isolated agent sandbox with its own node ID, trust zone,
  and mount evidence; it does not own the mounted checkout.*
- **Trust Zone / Vertrauenszone:** die belegte Sicherheitsgrenze, in der ein
  Node beobachtet wird. Sie erteilt allein keine Schreib- oder Delivery-
  Berechtigung. / *The evidenced security boundary in which a node is
  observed. It grants no write or delivery authority by itself.*
- **Mount / Einbindung:** eine Zuordnung von logischer Quelle zu logischem Ziel
  mit Modus, Write-Authority und Vergleich zwischen deklarierter und
  beobachteter Lage. / *A mapping from logical source to logical target with
  mode, write authority, and comparison of declared and observed state.*
- **Attestation / Vertrauensnachweis:** die fail-closed Auswertung mehrerer
  Evidence-Quellen. Ergebnisse sind `Verified`, `Limited`, `Untrusted` oder
  `Unknown`. / *The fail-closed evaluation of multiple evidence sources. Its
  results are Verified, Limited, Untrusted, or Unknown.*
- **Freshness / Aktualität:** die getrennte Altersklasse `Fresh`, `Aging`,
  `Stale`, `Expired` oder `Unknown` nach dem RAW-03-Modell `0,5T / T / 2T`. /
  *The separate age class Fresh, Aging, Stale, Expired, or Unknown under the
  RAW-03 0.5T/T/2T model.*
- **Health / Nutzbarkeit:** `Healthy`, `Degraded`, `Unavailable` oder
  `Unknown` beschreibt die technische Nutzbarkeit; der fachliche Node-State
  bleibt eine eigene Achse. / *Healthy, Degraded, Unavailable, or Unknown
  describes technical usability; domain node state remains a separate axis.*
- **Fail-closed / sicher geschlossen:** fehlende, veraltete oder
  widersprüchliche Evidence wird nie als stärkerer Zustand oder zusätzliche
  Authority geraten. / *Missing, stale, or contradictory evidence is never
  guessed as a stronger state or additional authority.*
- **read-only Research:** ausschließlich beobachtende Erhebung ohne Mount-,
  Prozess-, Credential-, Netzwerk-, Checkout- oder Remote-Write-Side-Effects.
  / *Observation-only research without mount, process, credential, network,
  checkout, or remote-write side effects.*
- **Single-autonomous:** ein möglicher späterer, einzeln autorisierter Lauf;
  der Begriff startet keinen Lauf. / *A possible later run with separate
  explicit authority; the term starts nothing.*
- **MergeAndSync:** ein historisch gespeicherter Delivery-Modus. Er ist keine
  aktuelle Start-, Remote-, Merge- oder Bypass-Autorität. / *A historically
  stored delivery mode. It is not current start, remote, merge, or bypass
  authority.*
- **WCAG 2.2 AA und CEFR B2:** die anwendbare Accessibility-Basis und das
  verständliche Sprachniveau für nutzerseitige Evidence. / *The applicable
  accessibility baseline and understandable language level for user-facing
  evidence.*

Weitere Begriffe erklärt das
[zweisprachige Glossar](../../baseline/glossary.md). Der vollständige
maschinenlesbare Vertrag steht in
[`execution-node-contract.json`](../../baseline/execution-node-contract.json).
/ *The [bilingual glossary](../../baseline/glossary.md) explains further
terms. The complete machine-readable contract is stored in the linked JSON
file.*

## Scope und Non-Goals / Scope and non-goals

Im Scope liegen Node Descriptor, stabile lokale Node-Identitäten,
transportneutrale lokale Endpoints, read-only Probes, Mehrquellen-Attestation,
Mount Authority, Capability-Evidence, versionierte Timeout-/Freshness-Profile,
Health-Ableitung und side-effect-freie Recovery. / *In scope are the Node
Descriptor, stable local node identities, transport-neutral local endpoints,
read-only probes, multi-source attestation, mount authority, capability
evidence, versioned timeout/freshness profiles, health derivation, and
side-effect-free recovery.*

Außerhalb liegen Produktimplementierung, Working-Copy-Ownership, Home-Sync,
CLI-Semantik, Prozessstart oder -abbruch, Credential-Nutzung, automatische
Mount-Änderungen, Remote Transport, Remote Write, Workflow-Ausführung,
Produkt-Scaffolding und Preset-Arbeit. Die konkrete spätere Remote-
Transportwahl bleibt bei RAW-06 `IAD604`. / *Out of scope are product
implementation, working-copy ownership, Home sync, CLI semantics, process
start or termination, credential use, automatic mount changes, remote
transport, remote write, workflow execution, product scaffolding, and preset
work. The later concrete remote-transport choice remains with RAW-06 IAD604.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

Kanonische Quellen sind SRC-177 und SRC-181; das zugeordnete Finding ist RF-07.
RAW-02 → RAW-05 ist ausschließlich `PreferredSerialOrder` und nicht bindend.
RAW-05 besitzt deshalb keinen bindenden fachlichen Vorgänger. Die aktuelle
Serienreihenfolge bleibt unverändert. / *Canonical sources are SRC-177 and
SRC-181, with RF-07 as the assigned finding. RAW-02 to RAW-05 is only
PreferredSerialOrder and is not binding. RAW-05 therefore has no binding
domain predecessor. The current Series order remains unchanged.*

Die typisierten Handoffs lauten: / *The typed handoffs are:*

1. **RAW-05 → RAW-02, `Node Descriptor`, `requirements-v1`:** nicht bindender
   read-only Orchestration Context. Ungültige oder fehlende Deskriptoren bleiben
   `Unknown` und autorisieren keinen Command. / *Non-binding read-only
   orchestration context. Invalid or missing descriptors remain Unknown and
   authorize no command.*
2. **RAW-05 → RAW-06, `Node Capability and Authority Contract`,
   `requirements-v1`:** bindender `HardCompletionGate` für read-only Node-,
   Capability-, Mount- und Attestation-Evidence. `Unknown`, `Untrusted`,
   `Stale` oder `Unavailable` autorisiert keine CLI-Ausführung. / *A binding
   HardCompletionGate for read-only node, capability, mount, and attestation
   evidence. Unknown, Untrusted, Stale, or Unavailable evidence authorizes no
   CLI execution.*
3. **RAW-05 → RAW-08, `Node Health and Freshness Assessment`,
   `requirements-v1`:** bindende `AssessmentBaseline` als read-only
   Workflow-Input. Fehlende `Known`-Evidence blockiert oder degradiert einen
   späteren Workflow sichtbar. / *A binding AssessmentBaseline as read-only
   workflow input. Missing Known evidence visibly blocks or degrades a later
   workflow.*

Producer, Consumer, Version, Authority, Failure Behavior und Serienrelation
sind im maschinenlesbaren Vertrag gebunden. Kein Handoff überträgt Working-
Copy-, CLI-, Command- oder Delivery-Ownership. / *Producer, consumer, version,
authority, failure behaviour, and Series relation are bound in the
machine-readable contract. No handoff transfers working-copy, CLI, command, or
delivery ownership.*

## Querschnittsanforderungen / Cross-cutting requirements

- **Security / Sicherheit:** Node-Evidence MUSS fail-closed ausgewertet
  werden. Secrets, Credentials und unerlaubte Authority DÜRFEN nicht erhoben
  oder abgeleitet werden. Remote Nodes bleiben deaktiviert. / *Node evidence
  MUST be evaluated fail closed. Secrets, credentials, and unauthorized
  authority MUST NOT be collected or inferred. Remote nodes remain disabled.*
- **Privacy und Datenminimierung / Privacy and data minimisation:** Node- und
  Mount-Evidence MUSS pseudonyme stabile IDs und logische Referenzen verwenden.
  Persönliche absolute Hostpfade, Benutzernamen und unnötige Gerätedaten DÜRFEN
  nicht erscheinen. / *Node and mount evidence MUST use stable pseudonymous
  IDs and logical references. Personal absolute host paths, user names, and
  unnecessary device data MUST NOT appear.*
- **Public Content / Öffentliche Inhalte:** Öffentliche Evidence DARF nur
  reviewte Reason Codes, redigierte logische Referenzen und nicht geheime
  Capability-Metadaten enthalten. / *Public evidence MUST contain only
  reviewed reason codes, redacted logical references, and non-secret
  capability metadata.*
- **Accessibility / Barrierefreiheit:** Nutzerseitige Evidence MUSS
  anwendbares WCAG 2.2 AA unterstützen. Status benötigt sichtbaren Text und
  stabile Codes; Bedeutung darf nicht nur von Farbe, Position, Animation oder
  Klang abhängen. / *User-facing evidence MUST support applicable WCAG 2.2 AA.
  Status requires visible text and stable codes; meaning must not depend only
  on colour, position, animation, or sound.*
- **DE/EN und Verständlichkeit:** Deutsche Texte sind zuerst maßgeblich,
  englische Texte folgen. Beide Fassungen MÜSSEN semantisch gleichwertig und auf
  CEFR-B2-Niveau selbständig verständlich sein. / *German text is
  authoritative and first; English follows. Both versions MUST be semantically
  equivalent and independently understandable at CEFR B2.*
- **Plattform und Containergrenzen:** Dieselben Inputs und Profile MÜSSEN auf
  macOS, Linux und Windows dieselben Ergebnisse liefern. Host, WSL, Container
  und ABS-DD bleiben getrennte Nodes mit eigener ID, Trust Zone und Mount-
  Evidence. / *Identical inputs and profiles MUST produce identical results on
  macOS, Linux, and Windows. Host, WSL, container, and ABS-DD remain separate
  nodes with their own ID, trust zone, and mount evidence.*
- **Software-Lieferkette / Software supply chain:** Für diesen reinen
  Requirements-Vertrag und dependency-freie Fixtures ist die Prüfung `N/A`.
  Ein späterer Adapter oder eine Transportabhängigkeit MUSS SBOM- und
  Schwachstellennachweis binden. / *Supply-chain validation is N/A for this
  requirements-only contract and dependency-free fixtures. A later adapter or
  transport dependency MUST bind SBOM and vulnerability evidence.*

Neue Node-Typen, Trust Zones, Datenkategorien, Write Authority,
Recovery-Side-Effects, Remote-Aktivierung, `IAD604` oder neue
Implementierungsabhängigkeiten erzwingen eine erneute Querschnittsprüfung. /
*New node types, trust zones, data categories, write authority, recovery side
effects, remote enablement, IAD604, or implementation dependencies trigger a
new cross-cutting assessment.*

## Anforderungen / Requirements

- **FR-001 – stabile Identität:** Host, WSL, Container und ABS-DD MÜSSEN
  jeweils eine stabile pseudonyme Node-ID besitzen. Host und Sandbox DÜRFEN
  niemals dieselbe Identität tragen. / *Host, WSL, container, and ABS-DD MUST
  each have a stable pseudonymous node ID. Host and sandbox MUST never share an
  identity.*
- **FR-002 – Node Descriptor:** Jeder Deskriptor MUSS Schemaversion, Node-ID,
  Typ, Plattform, Trust Zone, Runtime-Identität, Capabilities, Mounts,
  Authority, `observed-at`, `freshness-as-of`, Freshness, Node-State, Health,
  Attestation, Reason Codes und Policy-Version enthalten. / *Every descriptor
  MUST contain schema version, node ID, type, platform, trust zone, runtime
  identity, capabilities, mounts, authority, observed-at, freshness-as-of,
  freshness, node state, health, attestation, reason codes, and policy
  version.*
- **FR-003 – Endpoint-Grenze:** Lokale Adapter für Host, WSL, Container und
  ABS-DD MÜSSEN denselben transportneutralen read-only Probe-Vertrag erfüllen.
  Remote Nodes MÜSSEN bis zu einem separat reviewten `IAD604`-Vertrag
  deaktiviert bleiben und `REMOTE_DISABLED` liefern. / *Local adapters for
  host, WSL, container, and ABS-DD MUST implement the same transport-neutral
  read-only probe contract. Remote nodes MUST remain disabled until a
  separately reviewed IAD604 contract exists and return REMOTE_DISABLED.*
- **FR-004 – Mehrquellen-Attestation:** Node-Typ, Plattform, Trust Zone,
  Runtime-Identität, deklarierte und beobachtete Mounts, Capability-Probe,
  Policy-Version und Beobachtungszeit MÜSSEN gemeinsam ausgewertet werden.
  Ergebnisse sind ausschließlich `Verified`, `Limited`, `Untrusted` oder
  `Unknown`. / *Node type, platform, trust zone, runtime identity, declared and
  observed mounts, capability probe, policy version, and observation time MUST
  be evaluated together. Results are only Verified, Limited, Untrusted, or
  Unknown.*
- **FR-005 – fail-closed Trust:** Fehlende oder ungültige Evidence MUSS
  `Unknown`, widersprüchliche Evidence `Untrusted` ergeben. Beide Ergebnisse
  bleiben höchstens read-only und dürfen keine zusätzliche Authority ableiten.
  / *Missing or invalid evidence MUST yield Unknown, and contradictory evidence
  Untrusted. Both remain read-only at most and may infer no additional
  authority.*
- **FR-006 – Mount Authority:** Jeder Mount MUSS logische Quelle, logisches
  Ziel, Modus, Write Authority und Gleichheit von deklarierter und beobachteter
  Lage ausweisen. In read-only Research sind ausschließlich `ReadOnly` und
  Write Authority `None` zulässig. Drift MUSS `Degraded` und `MOUNT_DRIFT`
  liefern. / *Every mount MUST state logical source, logical target, mode,
  write authority, and equality of declared and observed state. Read-only
  research permits only ReadOnly and write authority None. Drift MUST yield
  Degraded and MOUNT_DRIFT.*
- **FR-007 – Profile:** Jedes Node-Typ-/Capability-Paar MUSS ein reviewtes,
  versioniertes Profil mit positivem `probeTimeoutSeconds` und positivem
  `freshnessTSeconds` besitzen. Freie unbelegte Runtime-Overrides sind
  verboten. / *Every node-type/capability pair MUST have a reviewed versioned
  profile with positive probeTimeoutSeconds and freshnessTSeconds. Free
  unevidenced runtime overrides are prohibited.*
- **FR-008 – Freshness:** Alter bis einschließlich `0,5T` ist `Fresh`, mehr
  als `0,5T` bis einschließlich `T` ist `Aging`, mehr als `T` bis
  einschließlich `2T` ist `Stale`, mehr als `2T` ist `Expired`; ohne gültiges
  Alter gilt `Unknown`. / *Age through 0.5T inclusive is Fresh, above 0.5T
  through T inclusive is Aging, above T through 2T inclusive is Stale, above
  2T is Expired, and missing valid age is Unknown.*
- **FR-009 – Health und State:** Erfolgreiche `Fresh`- oder `Aging`-Evidence
  darf nur mit `Verified` und ohne Konflikt `Known`/`Healthy` ergeben. `Stale`
  ergibt `Stale`/`Degraded`; `Expired`, ein fehlender Node oder
  `PROBE_TIMEOUT` ergibt `Unavailable`; Mount-/Authority-Konflikt ergibt
  `Degraded`; fehlende Evidence ergibt `Unknown`. / *Successful Fresh or Aging
  evidence may yield Known/Healthy only when Verified and conflict-free. Stale
  yields Stale/Degraded; Expired, a missing node, or PROBE_TIMEOUT yields
  Unavailable; mount or authority conflict yields Degraded; missing evidence
  yields Unknown.*
- **FR-010 – Recovery:** Nach Timeout, verweigertem Zugriff oder Mount-Drift
  ist ausschließlich ein neuer read-only Probe zulässig. Automatisches Mount,
  Unmount, Remount, Prozessstart/-abbruch, Credential-Zugriff,
  Netzwerkänderung, Checkout-Mutation und Remote Write sind verboten. / *After
  timeout, refused access, or mount drift, only a new read-only probe is
  allowed. Automatic mount, unmount, remount, process start or termination,
  credential access, network change, checkout mutation, and remote write are
  prohibited.*
- **FR-011 – strukturierte Ausfälle:** Timeout, fehlender Node, verweigerter
  Zugriff, Drift, veraltete und fehlende Evidence MÜSSEN stabile Reason Codes
  und strukturierte Ergebnisse statt leerer oder erfolgreicher Defaults
  liefern. / *Timeout, missing node, refused access, drift, stale evidence, and
  missing evidence MUST yield stable reason codes and structured results rather
  than empty or successful defaults.*
- **NFR-001 – deterministische Evidence:** Vertrag und Fixtures MÜSSEN mit
  denselben Inputs auf Bash und PowerShell dieselben Ergebnisse, Reason Codes
  und Exitcodes liefern. / *The contract and fixtures MUST produce identical
  results, reason codes, and exit codes from the same inputs through Bash and
  PowerShell.*
- **NFR-002 – zugängliche Sprache:** Lastenheft und nutzerseitige Evidence
  MÜSSEN DE-first, EN-second, semantisch gleichwertig und auf CEFR B2
  verständlich sein. / *The intake and user-facing evidence MUST be German
  first, English second, semantically equivalent, and understandable at CEFR
  B2.*
- **NFR-003 – Re-Evaluation:** Die genannten Security-, Privacy-, Public-
  Content-, Accessibility-, Plattform-, Container- und Supply-Chain-Trigger
  MÜSSEN vor einer Erweiterung neu geprüft werden. / *The named security,
  privacy, public-content, accessibility, platform, container, and supply-chain
  triggers MUST be reassessed before an extension.*

## Bestätigte Decisions, Lifecycle und Mode / Confirmed decisions, lifecycle, and mode

Die drei materiellen Reviewfragen sind ohne offenen Rest beantwortet: / *The
three material review questions are answered without an open remainder:*

1. **IAD501 (beantwortet IRQ501) – Transportgrenze:** RAW-05 definiert einen
   transportneutralen lokalen Node Endpoint und lokale read-only Adapter für
   Host, WSL, Container und ABS-DD. Remote Nodes bleiben standardmäßig
   deaktiviert. Die konkrete Remote-Transportwahl bleibt ausdrücklich bei
   RAW-06 `IAD604`; RAW-05 erteilt keine Remote-Write-, Prozess- oder
   Credential-Authority. / *RAW-05 defines a transport-neutral local Node
   Endpoint and local read-only adapters for host, WSL, container, and ABS-DD.
   Remote nodes remain disabled by default. The concrete remote-transport
   choice remains explicitly with RAW-06 IAD604; RAW-05 grants no remote-write,
   process, or credential authority.*
2. **IAD502 (beantwortet IRQ502) – Attestation:** Node-Typ, Plattform, Trust
   Zone, Runtime-Identität, deklarierte und beobachtete Mounts, Capability-
   Probe, Policy-Version und Zeit werden gemeinsam fail-closed geprüft.
   Ergebnisse sind `Verified`, `Limited`, `Untrusted` oder `Unknown`; fehlende
   beziehungsweise widersprüchliche Evidence ergibt `Unknown` beziehungsweise
   `Untrusted` und höchstens read-only Verhalten. / *Node type, platform, trust
   zone, runtime identity, declared and observed mounts, capability probe,
   policy version, and time are evaluated together and fail closed. Results are
   Verified, Limited, Untrusted, or Unknown; missing or contradictory evidence
   yields Unknown or Untrusted respectively and read-only behaviour at most.*
3. **IAD503 (beantwortet IRQ503) – Timeout, Freshness und Recovery:**
   Versionierte Profile je Node-Typ und Capability definieren positive Probe-
   Timeouts und `T`. Freshness folgt `0,5T / T / 2T`. Timeout ergibt
   `Unavailable`/`PROBE_TIMEOUT`, veraltete Evidence `Stale`, Konflikt
   `Degraded` und fehlende Evidence `Unknown`. Recovery ist ausschließlich ein
   neuer read-only Probe ohne Side-Effects. / *Versioned profiles per node type
   and capability define positive probe timeouts and T. Freshness follows
   0.5T/T/2T. Timeout yields Unavailable/PROBE_TIMEOUT, stale evidence Stale,
   conflict Degraded, and missing evidence Unknown. Recovery is only a new
   read-only probe without side effects.*

`IAD502` und `IAD503` supersedieren `DEC-T06` vollständig. `IAD501` begrenzt
RAW-05, ohne die weiterhin offene RAW-06-Entscheidung `IAD604` vorwegzunehmen.
/ *IAD502 and IAD503 fully supersede DEC-T06. IAD501 bounds RAW-05 without
pre-empting the still-open RAW-06 decision IAD604.*

META-LH-01 bis META-LH-05 sowie RAW-01 bis RAW-04 sind im aktuellen
Series-Lifecycle `Completed`. RAW-05 ist der einzige deklarierte `Eligible`-
Kandidat und bleibt auf read-only Research begrenzt. RAW-02 → RAW-05 ist nur
bevorzugte Reihenfolge. Die einzige aktuelle nächste Aktion ist das vollständige
RAW-05-Single-Re-Review. / *META-LH-01 through META-LH-05 and RAW-01 through
RAW-04 are Completed in the current Series lifecycle. RAW-05 is the sole
declared Eligible candidate and remains limited to read-only research. RAW-02
to RAW-05 is preferred order only. The only current next action is the complete
RAW-05 Single re-review.*

`ReadyForReview`, `Eligible`, ein späteres `Ready`, `single-autonomous`, der
historische Modus `MergeAndSync` und kopierbare Prompts sind getrennte
Informationen. Keine davon erteilt aktuelle Scope-, Start-, Specify-,
Implementierungs-, Remote-, Merge-, Bypass-, Provider-, Preset- oder Level-0-
Autorität. / *ReadyForReview, Eligible, a later Ready result,
single-autonomous, historical MergeAndSync mode, and copy-ready prompts are
separate facts. None grants current scope, start, Specify, implementation,
remote, merge, bypass, provider, preset, or Level-0 authority.*

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Vorgesehene Child-Intakes sind Node Descriptor, Host/Sandbox Authority, Mount
Policy und Health/Freshness. Dieses Requirements-Update erstellt oder startet
sie nicht. / *Planned child intakes are Node Descriptor, Host/Sandbox
Authority, Mount Policy, and Health/Freshness. This requirements update neither
creates nor starts them.*

- **AC-001:** Positive Fixtures belegen getrennte stabile Identitäten für Host,
  WSL, Container und ABS-DD auf macOS, Linux und Windows. / *Positive fixtures
  prove distinct stable identities for host, WSL, container, and ABS-DD on
  macOS, Linux, and Windows.*
- **AC-002:** Lokale Adapter liefern strukturierte read-only Deskriptoren;
  Remote Nodes liefern ausschließlich `Unavailable`, `Unknown` und
  `REMOTE_DISABLED`. / *Local adapters yield structured read-only descriptors;
  remote nodes yield only Unavailable, Unknown, and REMOTE_DISABLED.*
- **AC-003:** Ein gültiger ReadOnly-Mount besteht; Write-Authority und
  persönlicher absoluter Hostpfad werden mit `EN008` abgelehnt. Mount-Drift
  ergibt `Degraded`/`MOUNT_DRIFT` ohne Side-Effect. / *A valid read-only mount
  passes; write authority and a personal absolute host path are rejected with
  EN008. Mount drift yields Degraded/MOUNT_DRIFT without a side effect.*
- **AC-004:** Vollständige Evidence ergibt reproduzierbar `Verified`; fehlende,
  verweigerte und widersprüchliche Evidence ergibt `Unknown`, `Limited` oder
  `Untrusted` und nie unbelegtes `Known`. / *Complete evidence reproducibly
  yields Verified; missing, refused, or contradictory evidence yields Unknown,
  Limited, or Untrusted and never unsupported Known.*
- **AC-005:** Die Grenzwerte `0,5T`, `T` und `2T`, `Expired`, Timeout,
  fehlender Node und verweigerter Zugriff ergeben die festgelegten Freshness-,
  State-, Health- und Reason-Code-Werte. / *The 0.5T, T, and 2T boundaries,
  Expired, timeout, missing node, and refused access yield the specified
  freshness, state, health, and reason-code values.*
- **AC-006:** Unerlaubter Remote-Transport, Write-Mount, Default-Trust und
  Timeout-Remount werden reproduzierbar mit `EN007`, `EN008`, `EN009` und
  `EN010` abgelehnt. / *Unauthorized remote transport, write mount, default
  trust, and timeout remount are reproducibly rejected with EN007, EN008,
  EN009, and EN010.*
- **AC-007:** Alle drei Handoffs besitzen Producer, Consumer, Vertrag, Version,
  Authority, Failure Behavior und bindende beziehungsweise nicht bindende
  Serienrelation. / *All three handoffs identify producer, consumer, contract,
  version, authority, failure behaviour, and binding or non-binding Series
  relation.*
- **AC-008:** Beide Shell-Oberflächen liefern für jede Fixture dieselbe
  Sollausgabe und Exitcode `0`; erwartete Ablehnung gilt als bestandene
  Negativ-Evidence. / *Both shell surfaces yield the same expected output and
  exit code 0 for every fixture; an expected rejection counts as passing
  negative evidence.*

Reproduzierbare Befehle und Sollausgaben: / *Reproducible commands and expected
outputs:*

```text
bash specs/intake-review-fixtures/raw-05/validate-execution-node-contract.sh --contract requirements/baseline/execution-node-contract.json --fixture specs/intake-review-fixtures/raw-05/valid-execution-node-cases.json
# RAW05-VALID-EXECUTION-NODES: Gültig / Valid
bash specs/intake-review-fixtures/raw-05/validate-execution-node-contract.sh --contract requirements/baseline/execution-node-contract.json --fixture specs/intake-review-fixtures/raw-05/negative-remote-enabled.json
# RAW05-NEGATIVE-REMOTE-ENABLED: Abgelehnt / Rejected (EN007: ...)
bash specs/intake-review-fixtures/raw-05/validate-execution-node-contract.sh --contract requirements/baseline/execution-node-contract.json --fixture specs/intake-review-fixtures/raw-05/negative-unsafe-mount.json
# RAW05-NEGATIVE-UNSAFE-MOUNT: Abgelehnt / Rejected (EN008: ...)
bash specs/intake-review-fixtures/raw-05/validate-execution-node-contract.sh --contract requirements/baseline/execution-node-contract.json --fixture specs/intake-review-fixtures/raw-05/negative-default-trust.json
# RAW05-NEGATIVE-DEFAULT-TRUST: Abgelehnt / Rejected (EN009: ...)
bash specs/intake-review-fixtures/raw-05/validate-execution-node-contract.sh --contract requirements/baseline/execution-node-contract.json --fixture specs/intake-review-fixtures/raw-05/negative-timeout-side-effect.json
# RAW05-NEGATIVE-TIMEOUT-SIDE-EFFECT: Abgelehnt / Rejected (EN010: ...)
pwsh -NoProfile -File specs/intake-review-fixtures/raw-05/validate-execution-node-contract.ps1 -Contract requirements/baseline/execution-node-contract.json -Fixture specs/intake-review-fixtures/raw-05/valid-execution-node-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-05/validate-execution-node-contract.ps1 -Contract requirements/baseline/execution-node-contract.json -Fixture specs/intake-review-fixtures/raw-05/negative-remote-enabled.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-05/validate-execution-node-contract.ps1 -Contract requirements/baseline/execution-node-contract.json -Fixture specs/intake-review-fixtures/raw-05/negative-unsafe-mount.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-05/validate-execution-node-contract.ps1 -Contract requirements/baseline/execution-node-contract.json -Fixture specs/intake-review-fixtures/raw-05/negative-default-trust.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-05/validate-execution-node-contract.ps1 -Contract requirements/baseline/execution-node-contract.json -Fixture specs/intake-review-fixtures/raw-05/negative-timeout-side-effect.json
```

## Risiken, Revision und Nichtautorität / Risks, revision, and non-authority

Risiken sind Identitätskollision, unbelegtes Default-Trust, persönliche
Hostpfade, Mount-Drift, falsche Freshness, versteckte Timeout-Recovery,
vorweggenommener Remote Transport und die Verwechslung historischer Delivery-
Daten mit aktueller Authority. Vertrag, Fixtures und vollständiges Re-Review
begrenzen diese Risiken; sie beweisen keine spätere Produkt-Runtime. / *Risks
include identity collision, unsupported default trust, personal host paths,
mount drift, incorrect freshness, hidden timeout recovery, pre-empted remote
transport, and confusion of historical delivery data with current authority.
The contract, fixtures, and complete re-review bound these risks; they do not
prove a later product runtime.*

Revision ist erforderlich bei Änderungen an Node-Typ, Trust Zone, Mount-,
Attestation-, State-, Capability-, Plattform- oder Zeitvertrag, bei
Remote-Aktivierung oder `IAD604`, bei Write Authority, Side-Effects, neuen
Datenkategorien oder Implementierungsabhängigkeiten. RAW-05 erteilt keine
Workspace-, Home-Sync-, CLI-, Command-, Credential-, Prozess-, Specify-,
Implementierungs-, Remote-, Merge-, Bypass-, Provider-, Preset- oder Level-0-
Autorität. / *Revision is required for changes to node type, trust zone,
mount, attestation, state, capability, platform, or time contracts; remote
enablement or IAD604; write authority; side effects; new data categories; or
implementation dependencies. RAW-05 grants no workspace, Home-sync, CLI,
command, credential, process, Specify, implementation, remote, merge, bypass,
provider, preset, or Level-0 authority.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist die ausdrücklich autorisierte,
auf IR501 bis IR506 begrenzte Reparatur; Owner ist RAW-05. Aktualisiert werden
dieses Lastenheft, sein maschinenlesbarer Vertrag, die Review-Fixtures,
Authoring Receipt, Serien-Hashbindung und vollständige Re-Review-Evidence. /
*Decision: UpdateRequired. The explicitly authorized repair bounded to IR501
through IR506 is the source and RAW-05 is the owner. This intake, its
machine-readable contract, review fixtures, Authoring Receipt, Series hash
binding, and complete re-review evidence are updated.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

Die folgenden Befehle sind ausschließlich kopierbare Vorlagen. Vor jeder
Ausführung MÜSSEN Zielhash, Authoring Receipt, aktuelles `Ready`-Single-Review,
globale Review-Sperre sowie neue ausdrückliche menschliche Scope-, Start- und
Delivery Authority fail-closed geprüft werden. Remote-, Merge-, Bypass- und
Provider-Autorität müssen jeweils separat und aktuell vorliegen. / *The
following commands are copy-ready templates only. Before execution, the target
hash, Authoring Receipt, current Ready Single review, global review gate, and
fresh explicit human scope, start, and delivery authority MUST be checked fail
closed. Remote, merge, bypass, and provider authority must each be separate and
current.*

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md --delivery-mode MergeAndSync --require-current-review
```

<!-- intake-authoring:end -->
