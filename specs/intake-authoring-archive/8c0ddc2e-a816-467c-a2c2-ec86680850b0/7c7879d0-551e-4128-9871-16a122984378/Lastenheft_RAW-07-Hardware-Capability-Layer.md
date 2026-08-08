<!-- intake-authoring:begin -->
# RAW-07 – Hardware Capability Layer / Hardware Capability Layer

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** Ein-/Ausgabegeräte und Adapter; keine MIDI-, SDK- oder Lab-Erfahrung / input/output devices and adapter basics; no MIDI, SDK, or lab experience
**Profile:** `aoc-bilingual-requirements`

## Zweck, Ist- und Zielzustand / Purpose, current, and target state

Hardwaregeräte besitzen hersteller- und protokollspezifische Eigenschaften.
Ohne gemeinsame Grenze könnten Raw MIDI, SysEx, Control-Change-Nummern,
Elgato-SDK-Details oder Gerätezustand in das AOC-Domainmodell gelangen. Ziel
ist ein herstellerneutraler Capability-Vertrag mit dünnen Adaptern,
reproduzierbarer Reference-Lab-Evidence und fail-closed Hardware-I/O. /
*Hardware devices have vendor- and protocol-specific properties. Without a
common boundary, raw MIDI, SysEx, control-change numbers, Elgato SDK details,
or device state could leak into the AOC domain model. The target is a
vendor-neutral capability contract with thin adapters, reproducible reference
lab evidence, and fail-closed hardware I/O.*

Dieses Lastenheft beschreibt ausschließlich Requirements und offline
auswertbare JSON-Fixtures. Es entdeckt, verbindet oder steuert kein Gerät und
erteilt keine Hardware-, Produktcommand- oder State-Authority. / *This intake
defines requirements and offline JSON fixtures only. It discovers, connects,
or controls no device and grants no hardware, product-command, or state
authority.*

## Begriffe für den Einstieg / Terms for first-time readers

- **Capability / Fähigkeit:** herstellerneutrale Nutzerfunktion wie Button,
  Encoder, Fader, Pad, Text, Icon oder Feedback. / *A vendor-neutral user
  function such as a button, encoder, fader, pad, text, icon, or feedback.*
- **Thin Adapter / dünner Adapter:** Übersetzung zwischen Geräteprotokoll und
  Capability-Vertrag ohne AOC-Domänenlogik oder State-Ownership. / *A
  translation between device protocol and capability contract without AOC
  domain logic or state ownership.*
- **Raw MIDI:** unverarbeitete MIDI-Nachrichten einschließlich SysEx und
  Control-Change-Nummern. Sie bleiben im MIDI-Adapter. / *Unprocessed MIDI
  messages including SysEx and control-change numbers. They remain in the
  MIDI adapter.*
- **SDK Bridge:** isolierte Anbindung an ein Hersteller-SDK. Nur normalisierte
  Capability Events verlassen die Bridge. / *An isolated connection to a
  vendor SDK. Only normalised capability events leave the bridge.*
- **Reference Wave / Referenzwelle:** kleine, ausdrücklich freigegebene
  Gerätemenge für reproduzierbare Contract-Evidence. / *A small, explicitly
  approved device set for reproducible contract evidence.*
- **Lab Approval / Lab-Freigabe:** dokumentierte Entscheidung nach Inventar,
  Risiko-/Safety-Prüfung, Kill-Switch-Nachweis und beaufsichtigtem Testplan. /
  *A documented decision after inventory, risk and safety assessment,
  kill-switch evidence, and a supervised test plan.*
- **Kill Switch:** separat erreichbare Stop-Funktion, die Geräte-I/O beendet,
  ohne Erfolg oder wiederhergestellten Zustand zu behaupten. / *A separately
  reachable stop function that ends device I/O without claiming success or
  restored state.*
- **Authority / Autorität:** aktuelle ausdrückliche Erlaubnis für genaues
  Gerät, I/O-Klasse und Testzweck. Review oder Lifecycle ersetzt sie nicht. /
  *Current explicit permission for the exact device, I/O class, and test
  purpose. Review or lifecycle does not replace it.*

Weitere Begriffe erklärt das [zweisprachige Glossar](../../baseline/glossary.md).
/ *The [bilingual glossary](../../baseline/glossary.md) explains additional
terms.*

## Scope, Systemgrenze und Non-Goals / Scope, system boundary, and non-goals

Im Scope liegen Capability Model, Adapterzustände, deklarative Geräteprofile,
MIDI-Bibliotheksgrenze, Elgato-SDK-Bridge, erste Referenzwelle, Lab-/Safety-
Gate, Kill Switch und Offline-Evidence. RAW-07 konsumiert den RAW-04-
Presentation Contract und liefert normalisierte Capability Events und Feedback
ohne Domänencommands. / *Scope includes the capability model, adapter states,
declarative profiles, MIDI library boundary, Elgato SDK bridge, first reference
wave, lab and safety gate, kill switch, and offline evidence. RAW-07 consumes
the RAW-04 Presentation Contract and emits normalised capability events and
feedback without domain commands.*

Nicht im Scope sind echte Hardware-I/O, Gerätesuche, Verbindungen, MIDI-Senden
oder -Empfangen, SDK-Aufrufe, UI, Workspace- oder State-Ownership,
Produktcommand-Policy, Produktimplementierung, Presets, Level 0 und Remote-
Arbeit. / *Actual hardware I/O, discovery, connections, MIDI send or receive,
SDK calls, UI, workspace or state ownership, product command policy,
implementation, presets, Level 0, and remote work are out of scope.*

RAW-04 besitzt weiterhin Darstellung und Accessibility-Projektion. RAW-07
besitzt ausschließlich Hardware-Capabilities und dünne Adaptergrenzen. Ein
Adapter darf nie Domain Command, State-Owner oder Autoritätsquelle werden. /
*RAW-04 retains presentation and accessibility projection. RAW-07 owns only
hardware capabilities and thin-adapter boundaries. An adapter must never
become a domain-command, state, or authority owner.*

## Quellen, Finding und Handoffs / Sources, finding, and handoffs

Quellen sind SRC-169, SRC-171, SRC-173 und SRC-175 aus dem
[Source Pack](../../baseline/source-pack.md), RF-08 aus dem
[Findings Ledger](../../baseline/review-findings-ledger.md), der
[Presentation Contract](../../baseline/presentation-contract.json) und der
maschinenlesbare
[Hardware Capability Contract](../../baseline/hardware-capability-contract.json).
/ *Sources are the named Source Pack entries, RF-08, the Presentation Contract,
and the machine-readable Hardware Capability Contract.*

Die Handoffs sind: / *The handoffs are:*

1. `H-RAW04-RAW07`: RAW-04 → RAW-07, `Presentation Contract`,
   `requirements-v1`, bindendes Hard-Completion-Gate. Eine inkompatible oder
   unavailable Presentation Capability deaktiviert den Adapter sichtbar. /
   *A binding input; an incompatible or unavailable presentation capability
   visibly disables the adapter.*
2. `H-RAW07-AOC`: RAW-07 → AOC Presentation und Orchestration,
   `Hardware Capability Events and Feedback`, `requirements-v1`, funktionaler
   Handoff. Ungültige, unsupported, disconnected, degraded oder nicht
   freigegebene Geräte bleiben unavailable und emittieren keinen
   Produktcommand. / *A functional output; invalid, unsupported, disconnected,
   degraded, or unapproved devices stay unavailable and emit no product
   command.*

## Security, Privacy, A11Y, Plattform und Lieferkette / Security, privacy, A11Y, platform, and supply chain

- **Security und Safety:** Hardware-I/O MUSS blockiert bleiben, solange
  Inventar, gerätespezifische Risiko-/Safety-Prüfung, Kill Switch,
  beaufsichtigter Testplan oder dokumentierte Freigabe fehlen, abgelaufen oder
  unbekannt sind. / *Hardware I/O MUST stay blocked while any required lab or
  safety evidence is missing, expired, or unknown.*
- **Protokollgrenze:** Raw MIDI, SysEx, CC-Nummern, Vendor IDs und
  Hersteller-SDK-Objekte DÜRFEN den Adapter nicht verlassen. / *Raw MIDI,
  SysEx, control-change numbers, vendor IDs, and vendor SDK objects MUST NOT
  leave the adapter.*
- **Privacy:** Seriennummern, private Hostnamen, Benutzernamen und absolute
  Pfade werden aus öffentlichen Profilen, Logs, Reviews und Receipts entfernt.
  / *Serial numbers, private host names, user names, and absolute paths are
  excluded from public profiles, logs, reviews, and receipts.*
- **Accessibility:** Jede nutzerseitige Hardwarefunktion MUSS eine Tastatur-
  oder Textalternative besitzen, soweit sie als Nutzerfunktion angeboten wird.
  Status und Fehler benötigen sichtbare DE/EN-Labels und stabile Reason Codes.
  / *Every user-facing hardware function needs a keyboard or text alternative
  where offered. Status and failures need visible bilingual labels and stable
  reason codes.*
- **Sprache:** Deutsch ist zuerst maßgeblich, Englisch folgt semantisch
  gleichwertig. Zielniveau ist CEFR B2. / *German is authoritative and first;
  semantically equivalent English follows. The target level is CEFR B2.*
- **Cross-Platform:** macOS, Linux und Windows verwenden dieselben
  normalisierten Capabilities, Adapterzustände und Fehlerbedeutungen. Ein
  fehlender Plattformadapter ergibt `Unsupported`, niemals geratenen Erfolg. /
  *macOS, Linux, and Windows use the same normalised capabilities, adapter
  states, and failure meaning. A missing platform adapter is Unsupported,
  never guessed success.*
- **Software-Lieferkette:** Für dieses Requirements-Update und seine
  dependency-freien Offline-Fixtures ist die Einstufung `N/A`. Jede spätere
  MIDI-Bibliothek oder Elgato-SDK-Abhängigkeit erzwingt Lizenz-, Provenienz-,
  SBOM-, Vulnerability-, Plattform- und Wartungs-Evidence. / *Supply-chain
  assessment is N/A for this requirements-only update and its dependency-free
  offline fixtures. Later dependencies require the listed evidence.*

## Anforderungen / Requirements

- **FR-001 – Capability Model:** Der Vertrag MUSS `Button`, `Encoder`,
  `Fader`, `Pad`, `Text`, `Icon` und `Feedback` herstellerneutral beschreiben.
  Domain Contracts dürfen keine Raw-Protokoll- oder Vendor-ID verlangen. /
  *The contract MUST describe the listed vendor-neutral capabilities; domain
  contracts must not require raw protocol or vendor identifiers.*
- **FR-002 – Adapterzustände:** Adapter MÜSSEN `Connected`, `Disconnected`,
  `Reconnecting`, `Degraded` und `Unsupported` unterscheiden. / *Adapters MUST
  distinguish the listed states.*
- **FR-003 – Profile:** Geräteprofile MÜSSEN deklarativ, versioniert und ohne
  Seriennummern veröffentlichbar sein. / *Profiles MUST be declarative,
  versioned, and publishable without serial numbers.*
- **FR-004 – Baseline-Unabhängigkeit:** Hardwareausfall DARF Console- oder
  JSON-Baseline nicht beeinträchtigen. / *Hardware failure MUST NOT degrade the
  console or JSON baseline.*
- **FR-005 – MIDI-Grenze:** Eine plattformübergreifende MIDI-Bibliothek MUSS
  hinter einem dünnen Adapter liegen. Raw MIDI, SysEx und CC-Nummern bleiben
  dort; konkrete Paketwahl ist Implementierungsdetail innerhalb dieser
  Grenzen. / *A cross-platform MIDI library MUST sit behind a thin adapter.
  Raw MIDI remains there; package selection is an implementation detail within
  these constraints.*
- **FR-006 – Elgato-Grenze:** Die offizielle SDK-Bridge MUSS isoliert bleiben.
  TypeScript ist nur zulässig, wenn das SDK es verlangt. Nur normalisierte
  Capability Events und Feedback verlassen die Bridge. / *The official SDK
  bridge MUST stay isolated. TypeScript is allowed only when required by the
  SDK. Only normalised capability events and feedback leave the bridge.*
- **FR-007 – Erste Referenzwelle:** Die erste Welle enthält genau ein
  repräsentatives MIDI-Gerät und ein Stream Deck. Xbox bleibt separater
  Adapterkandidat und benötigt eigene Evidence. / *The first wave contains
  exactly one representative MIDI device and one Stream Deck. Xbox remains a
  separate adapter candidate requiring its own evidence.*
- **FR-008 – Lab-/Safety-Gate:** Vor jedem Feldtest MÜSSEN versioniertes
  Lab-Inventar, gerätespezifische Risiko-/Safety-Prüfung, verifizierter Kill
  Switch, beaufsichtigter Testplan und dokumentierte Freigabe vorliegen. /
  *Every field test requires the listed lab and safety evidence.*
- **FR-009 – Freigabezustand:** Freigabe ist genau `Approved`, `Rejected`,
  `Expired` oder `Unknown`. Nur `Approved` kann zusammen mit separater aktueller
  I/O-Authority einen Feldtest zulassen; Freigabe allein erteilt keine
  Produktcommand-Authority. / *Approval is exactly one of the named states.
  Only Approved plus separate current I/O authority may allow a field test;
  approval alone grants no product-command authority.*
- **FR-010 – Fehlergrenze:** Disconnect wird `Disconnected`, unbekannte
  Control wird `Unsupported`, malformed MIDI wird im Adapter mit
  `RejectedInAdapter` abgelehnt. Reconnect ist explizit und baut State neu auf.
  / *Disconnect, unknown control, malformed MIDI, and reconnect use the stated
  fail-closed behaviour.*
- **FR-011 – Keine Domain Commands:** Adapter emittieren ausschließlich
  normalisierte Events und Feedback. Sie besitzen keinen Produktzustand,
  treffen keine Command-Entscheidung und erweitern keine Authority. /
  *Adapters emit only normalised events and feedback and own no state, command
  decision, or authority.*
- **NFR-001 – Parität:** Vertrag und Fixtures MÜSSEN über Bash und PowerShell
  dieselben Ergebnisse, Reason Codes und Exitcodes liefern. / *The contract and
  fixtures MUST produce the same outcomes, reason codes, and exit codes through
  Bash and PowerShell.*
- **NFR-002 – A11Y:** Jede nutzerseitige Hardwarefunktion besitzt eine
  Tastatur-/Textalternative; Farbe, Klang, Haptik oder Gerät allein genügen
  nicht. / *Every user-facing hardware function has a keyboard or text
  alternative; colour, sound, haptics, or hardware alone is insufficient.*

## Bestätigte Decisions, Mode und Authority / Confirmed decisions, mode, and authority

Die vier materiellen Entscheidungen sind bestätigt: / *The four material
decisions are confirmed:*

1. **IAD701 – MIDI-Bibliothek:** Eine plattformübergreifende MIDI-Bibliothek
   liegt hinter einem dünnen, herstellerneutralen Adapter. Raw MIDI bleibt aus
   dem Domain Contract. / *A cross-platform MIDI library sits behind a thin,
   vendor-neutral adapter; raw MIDI stays out of the domain contract.*
2. **IAD702 – Elgato-Transport:** Die offizielle Elgato-SDK-Bridge bleibt
   isoliert; TypeScript ist nur bei SDK-Zwang zulässig; AOC erhält ausschließlich
   normalisierte Capability Events. / *The official SDK bridge remains
   isolated; TypeScript is allowed only when required; AOC receives only
   normalised capability events.*
3. **IAD703 – Gerätemenge:** Die erste Referenzwelle umfasst ein MIDI-Gerät
   und ein Stream Deck. Xbox bleibt separater späterer Kandidat. / *The first
   reference wave includes one MIDI device and one Stream Deck; Xbox remains a
   separate later candidate.*
4. **IAD704 – Lab-/Safety-Freigabe:** Feldtests erfordern Inventar,
   gerätespezifische Safety-Prüfung, Kill Switch, beaufsichtigten Testplan und
   dokumentierte Freigabe. / *Field tests require inventory, device-specific
   safety review, a kill switch, supervised plan, and documented approval.*

RAW-04 ist im aktuellen Series-Lifecycle `Completed`. RAW-07 bleibt dort
`Blocked`, bis dieses Update ein aktuelles validiertes `Ready`-Single-Review
besitzt und ein späterer ausdrücklicher Series-Update-Auftrag vorliegt. Es gibt
derzeit keinen `Eligible`-Kandidaten. Der erlaubte Mode bleibt `research-only`;
`parallel-autonomous` beschreibt nur mögliche spätere disjunkte Adapterläufe
nach eingefrorenem Contract, Lab Evidence und separater Authority. /
*RAW-04 is Completed. RAW-07 remains Blocked until this update has a current
validated Ready Single review and a later explicit Series update is authorised.
No target is currently Eligible. Research-only remains the allowed mode;
parallel autonomous only describes possible later isolated adapter runs after
a frozen contract, lab evidence, and separate authority.*

`ReadyForReview`, ein späteres `Ready`, Lifecycle, kopierbare Prompts und die
historische Delivery-Obergrenze `MergeAndSync` erteilen keine aktuelle Scope-,
Start-, Hardware-I/O-, Device-, SDK-, Remote-, Specify-, Implementierungs-,
Merge-, Bypass-, Provider-, Preset- oder Level-0-Autorität. / *ReadyForReview,
a later Ready result, lifecycle, copy-ready prompts, and the historical
MergeAndSync ceiling grant no current downstream authority.*

## Akzeptanz und Evidence / Acceptance and evidence

- **AC-001:** Positive Fixture belegt MIDI-Controller und Stream Deck auf
  demselben vendor-neutralen Capability-Vertrag mit Approved Lab Gate und Kill
  Switch. / *The positive fixture proves both device classes on one contract.*
- **AC-002:** Disconnect, unbekannte Control und malformed MIDI besitzen die
  erwarteten fail-closed Zustände. / *Failure cases use their expected
  fail-closed states.*
- **AC-003:** Raw-Protokoll im Domain Contract wird mit
  `HWC007_RAW_PROTOCOL_LEAK` abgelehnt. / *Raw-protocol leakage is rejected.*
- **AC-004:** Domain Command oder State-Ownership im Adapter wird mit
  `HWC008_DOMAIN_COMMAND_FORBIDDEN` abgelehnt. / *Adapter domain authority is
  rejected.*
- **AC-005:** Xbox in der ersten Welle ohne separate Evidence wird mit
  `HWC009_DEVICE_NOT_APPROVED` abgelehnt. / *An unapproved device is rejected.*
- **AC-006:** Feldtest ohne vollständige Lab-/Safety-Freigabe wird mit
  `HWC010_LAB_APPROVAL_REQUIRED` abgelehnt. / *A field test without complete
  approval is rejected.*
- **AC-007:** Feldtest ohne verifizierten Kill Switch wird mit
  `HWC011_KILL_SWITCH_REQUIRED` abgelehnt. / *A missing kill switch is
  rejected.*
- **AC-008:** Bash und PowerShell liefern je Fixture identische sichtbare
  DE/EN-Ausgabe und Exitcode `0`; erwartete Ablehnung ist bestandene
  Negativ-Evidence. / *Both surfaces produce identical bilingual output and
  exit code 0 per fixture; an expected rejection is passing negative evidence.*

Die offline ausführbaren Prüfungen sind: / *The offline checks are:*

```text
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/valid-hardware-capability-cases.json
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/negative-raw-protocol-leak.json
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/negative-domain-command.json
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/negative-unapproved-device.json
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/negative-missing-lab-approval.json
bash specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.sh --contract requirements/baseline/hardware-capability-contract.json --fixture specs/intake-review-fixtures/raw-07/negative-kill-switch-missing.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/valid-hardware-capability-cases.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/negative-raw-protocol-leak.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/negative-domain-command.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/negative-unapproved-device.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/negative-missing-lab-approval.json
pwsh -NoProfile -File specs/intake-review-fixtures/raw-07/validate-hardware-capability-contract.ps1 -Contract requirements/baseline/hardware-capability-contract.json -Fixture specs/intake-review-fixtures/raw-07/negative-kill-switch-missing.json
```

Diese Prüfungen lesen nur JSON und starten kein Hardware-I/O. / *These checks
read JSON only and start no hardware I/O.*

## Risiken, Revision und Nicht-Autorität / Risks, revision, and non-authority

Risiken sind Protokollleakage, Vendor-Lock-in, SDK-/Bibliotheksdrift,
unvollständige Plattformabdeckung, Seriennummern in Evidence, falsche
Gerätefreigabe, fehlender Kill Switch und Verwechslung von Lab-Freigabe mit
Produkt- oder I/O-Authority. / *Risks include protocol leakage, vendor lock-in,
dependency drift, incomplete platform coverage, serial numbers in evidence,
incorrect device approval, missing kill switch, and authority confusion.*

Revision ist erforderlich bei Änderungen an Capability Model, MIDI- oder
Elgato-Grenze, Referenzwelle, Lab-Inventar, Safety-/Supervision-/Kill-Switch-
Policy, Plattform, Datenkategorie oder Dependency. Dieses Lastenheft erteilt
keine Hardware-I/O-, Produkt-, Remote-, Merge-, Bypass-, Provider-, Preset-
oder Level-0-Autorität. / *Revision is required when any named boundary
changes. This intake grants no downstream authority.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle sind Thorstens ausdrücklich bestätigte
Optionen A für IAD701 bis IAD704; Owner ist RAW-07. Aktualisiert werden dieses
Lastenheft, Decision Register, Hardware Capability Contract, Offline-Fixtures,
Authoring Receipt, Serien-Hashbindung und Review-Evidence. / *Decision:
UpdateRequired. Thorsten's explicitly confirmed option A for IAD701 through
IAD704 is the source and RAW-07 is the owner. The intake, decision register,
contract, offline fixtures, receipts, Series binding, and review evidence are
updated.*

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md --bind-exact-intake --no-implementation --no-hardware-io --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md --delivery-mode MergeAndSync --require-current-review
```

Vor jeder Nutzung MUSS der aktuelle Zielhash, ein aktuelles `Ready`-Review,
Series-Eligibility, Lab-/Safety-Evidence und eine neue ausdrückliche Start-,
Hardware-I/O- und Delivery Authority fail-closed geprüft werden. Review,
Lifecycle, kopierbarer Prompt oder historisches Delivery-Feld genügen nie. /
*Before use, the current target hash, current Ready review, Series eligibility,
lab and safety evidence, and new explicit start, hardware-I/O, and delivery
authority MUST be checked fail closed. Review, lifecycle, a copy-ready prompt,
or a historic delivery field is never sufficient.*
<!-- intake-authoring:end -->
