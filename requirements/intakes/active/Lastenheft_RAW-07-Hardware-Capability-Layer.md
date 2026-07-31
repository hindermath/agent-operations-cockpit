<!-- intake-authoring:begin -->
# RAW-07 – Hardware Capability Layer / Hardware Capability Layer

**Status:** NeedsClarification
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Ein-/Ausgabegeräte; keine MIDI- oder SDK-Erfahrung / input/output devices; no MIDI or SDK experience
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Geräte werden über herstellerneutrale Capabilities wie Button, Encoder, Fader,
Pad, Text, Icon und Feedback integriert. Raw MIDI, SysEx, CC-Nummern und
Elgato-SDK-Details bleiben in dünnen Adaptern. / *Devices are integrated through
vendor-neutral capabilities; raw protocols stay in thin adapters.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-169, 171, 173, 175; RF-08. Input: RAW-04 Presentation Contract. Output:
normalisierte Capability Events und Feedback; keine Domänencommands.

## Anforderungen / Requirements

- **FR-001:** Domain Contracts dürfen keine Vendor-ID oder Raw-Protokolldaten verlangen.
- **FR-002:** Adapter MUSS Connect, Disconnect, Reconnect, Degraded und Unsupported melden.
- **FR-003:** Profile sind deklarativ, versioniert und ohne Seriennummern veröffentlichbar.
- **FR-004:** Hardwareausfall darf Console/JSON-Baseline nicht beeinträchtigen.
- **NFR-001:** Jede Hardwarefunktion besitzt Tastatur-/Textalternative, soweit Nutzerfunktion.
- **NFR-002:** Thin TypeScript ist nur für verpflichtendes Elgato SDK zulässig.

## Decisions, Mode und Recovery / Decisions, mode, and recovery

Offen: **IAD701** MIDI-Bibliothek, **IAD702** Elgato Transport, **IAD703**
Geräteauswahl und **IAD704** Lab-Freigaben.
`research-only`; Adapter dürfen nach eingefrorenem Contract in disjunkten
Worktrees `parallel-autonomous` werden. Kill Switch stoppt Geräte-I/O;
Recovery reconnectet explizit und stellt State neu her.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Capability Model; Reference Lab; MIDI Adapter Evaluation; Stream Deck Adapter;
Xbox Adapter. **AC-001:** zwei Geräteklassen nutzen denselben Domain Contract.
**AC-002:** Disconnect, unbekannte Control und malformed MIDI bleiben im Adapter.

Revision bei Capability- oder SDK-Vertrag. Keine Workspace-, State- oder Produktcommand-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
BLOCKED - DO NOT RUN: IAD701, IAD702, IAD703, and IAD704 require decisions.
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
BLOCKED - DO NOT RUN: IAD701, IAD702, IAD703, IAD704, and RAW-04 are required.
```
<!-- intake-authoring:end -->
