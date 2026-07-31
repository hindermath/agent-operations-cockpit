<!-- intake-authoring:begin -->
# RAW-06 – CLI Capability und Environment Orchestration / CLI Capability and Environment Orchestration

**Status:** NeedsClarification
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Terminal, Exitcode und Umgebungsvariable / terminal, exit code, and environment variable basics
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

CLI-Werkzeuge werden als typisierte Capabilities mit Input, Output, Timeout,
Authority und Fehlerklasse beschrieben. Diese Reihe besitzt keine UI,
Workspace-Discovery oder Hardware. / *CLI tools are described as typed
capabilities with inputs, outputs, timeout, authority, and failure class.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-162, 177; RF-07, RF-10. Inputs: RAW-01 Tool Snapshot und RAW-05 Node
Descriptor. Output: Capability Descriptor an RAW-02 und Evidence an RAW-08.

## Anforderungen / Requirements

- **FR-001:** Capability MUSS executable identity, version, node, arguments schema,
  timeout, cancellation, output schema und side-effect class enthalten.
- **FR-002:** Command-Strings aus untrusted Input werden nie über Shell-Eval ausgeführt.
- **FR-003:** Secrets werden referenziert, nie in Descriptor, Log oder Receipt kopiert.
- **FR-004:** Read-only Probes und mutierende Commands sind getrennte Capability-Klassen.
- **NFR-001:** PowerShell/Bash-Parität gilt, soweit Skripte beide Plattformen bedienen.

## Decisions, Mode und Recovery / Decisions, mode, and recovery

Offen: **IAD601** Process API, **IAD602** Exit-/Signalmodell, **IAD603**
Environment Allowlist und **IAD604** Remote Transport. `research-only`, bis
diese Decisions und RAW-05 stabil sind; danach
`single-autonomous`. Recovery beendet nur den gebundenen Prozess und berichtet
Partial Output, ohne unbekannte Wiederholung.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Capability Schema; Safe Process Execution; Environment Policy; Cross-platform
Parity. **AC-001:** Erfolg, Nonzero Exit, Timeout, Cancellation und Tool Missing
sind unterscheidbar. **AC-002:** Injection-Fixture wird nicht ausgeführt.

Revision bei Process-/Node-Vertrag. Keine UI-, Hardware- oder Produktcommand-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
BLOCKED - DO NOT RUN: IAD601, IAD602, IAD603, and IAD604 require decisions.
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
BLOCKED - DO NOT RUN: IAD601, IAD602, IAD603, IAD604, and RAW-05 are required.
```
<!-- intake-authoring:end -->
