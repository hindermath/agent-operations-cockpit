<!-- intake-authoring:begin -->
# RAW-05 – Execution Nodes / Execution Nodes

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Host-, Container- und Sandbox-Grundlagen / host, container, and sandbox basics
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Die Reihe beschreibt lokale Hosts, WSL, Container, ABS-DD-Sandbox und spätere
Remote Nodes als ausführende, klar autorisierte Ziele. Ein Node ist niemals
automatisch Owner von Working Copy, Home Baseline oder Produktentscheidungen.

*The series describes hosts, WSL, containers, the ABS-DD sandbox, and later
remote nodes as explicitly authorised execution targets. A node never
automatically owns a working copy, Home Baseline, or product decisions.*

## Quellen, Findings, Inputs und Outputs / Sources, findings, inputs, and outputs

SRC-177, 181; RF-07. Input: explizite Node-Konfiguration und read-only Probe.
Output: Node Descriptor mit Platform, Capabilities, Trust Zone, Mounts,
Authority, Freshness und Health an RAW-02/06/08.

## Anforderungen / Requirements

- **FR-001:** Host und Sandbox MÜSSEN unterschiedliche stabile Node-Identitäten haben.
- **FR-002:** Mounts MÜSSEN Quelle, Ziel, Modus und Write-Authority ausweisen.
- **FR-003:** Probe-Fehler MÜSSEN `Unavailable`/`Degraded` statt falscher Defaults liefern.
- **FR-004:** Secrets und persönliche Hostpfade dürfen nicht in Evidence gelangen.
- **NFR-001:** macOS und Windows sind verbindlich; Linux/WSL/Container nach Applicability.

## Decisions, Mode und Recovery / Decisions, mode, and recovery

Offen: Remote Transport, Node Attestation und Timeout. `research-only`, danach
`single-autonomous`. Abbruch bei Authority-/Mount-Drift; Recovery unmountet
nicht eigenmächtig und verändert kein kanonisches Checkout.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Node Descriptor; Host/Sandbox Authority; Mount Policy; Health/Freshness.
**AC-001:** Host und Sandbox werden korrekt differenziert.
**AC-002:** read-only Mount, fehlender Node und verweigerter Zugriff liefern
strukturierte Evidence ohne Write.

Revision bei Node- oder Trust-Modell. Keine Workspace-, CLI- oder Remote-Write-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
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
