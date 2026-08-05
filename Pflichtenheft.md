# AOC Lastenheft- und Pflichtenheftindex / AOC Requirements Index

## Zweck / Purpose

Dieser Index ist der kanonische Einstieg in das AOC-Anforderungsprogramm. Ein
Lastenheft beschreibt Bedarf und Grenzen. Eine spätere Spezifikation oder ein
Pflichtenheft beschreibt die freigegebene Lösung. Der Dateiname bleibt aufgrund
der installierten Governance-Konvention `Pflichtenheft.md`; aktuell enthält er
noch keine Produktspezifikation. / *This index is the canonical entry into the
AOC requirements programme. It does not yet contain a product specification.*

## Verbindliche Baseline / Binding baseline

- [Source Pack](requirements/baseline/source-pack.md)
- [Constraint Register](requirements/baseline/constraint-register.md)
- [Review Findings Ledger](requirements/baseline/review-findings-ledger.md)
- [Coverage Matrix](requirements/baseline/coverage-matrix.md)
- [Glossar / Glossary](requirements/baseline/glossary.md)
- [Authority and Stop Gates](requirements/baseline/authority-and-stop-gates.md)
- [Portfolio and Ownership](requirements/baseline/portfolio-ownership.md)
- [Autonomy and Evidence Model](requirements/baseline/autonomy-and-evidence-model.md)

## Meta-Reihe / Meta series

1. [META-LH-01 Programmquellen](requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md)
2. [META-LH-02 Portfolio und Ownership](requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md)
3. [META-LH-03 Authoring Contract](requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md)
4. [META-LH-04 Series und Eligibility](requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md)
5. [META-LH-05 Erste Welle](requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md)

## Fachliche erste Welle / First domain wave

| ID | Reihe / Series | Status | Modus vor Review / Mode before review |
|---|---|---|---|
| RAW-01 | [Reference Agentic Workspace](requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) | ReadyForReview | manual-assisted |
| RAW-02 | [Workspace Orchestrator](requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md) | NeedsClarification | blocked |
| RAW-03 | [State Truthfulness](requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md) | ReadyForReview | serial-autonomous after decisions |
| RAW-04 | [Presentation Fabric](requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md) | ReadyForReview | serial-autonomous |
| RAW-05 | [Execution Nodes](requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md) | ReadyForReview | research-only |
| RAW-06 | [CLI and Environment](requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md) | NeedsClarification | blocked |
| RAW-07 | [Hardware Capability Layer](requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md) | NeedsClarification | blocked |
| RAW-08 | [Workflow Engine](requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md) | ReadyForReview | serial-autonomous after dependencies |
| RAW-09 | [Preset Evolution](requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md) | NeedsClarification | blocked / research-only |

## Series und nächste Aktion / Series and next action

- [Menschenlesbare Reihenfolge](requirements/intakes/series/order.md)
- Maschinenlesbares Manifest: `specs/intake-series/aoc-phase-2/manifest.json`
- Series-ID: `d51e831c-24fb-4a71-b316-f7ad1bfe99d0`

Vor dem ersten nachgelagerten Spec-Kit-Lauf müssen alle 14 AOC-Lastenhefte ein
aktuelles, formal validiertes `Ready`-Single-Review besitzen. Bis dahin sind nur
die noch erforderlichen Intake-Reviews, ausdrücklich autorisierte Reparaturen,
Series-Statusprüfungen und die vorgeschriebene AEPS-Evidence-Rückführung
zulässig. `Eligible`, `Completed` oder ein einzelnes `Ready` heben diese globale
Sperre nicht auf.

Nach vollständiger Review-Coverage ist `META-LH-01` das erste erlaubte Ziel;
auch dann beginnt kein `speckit specify`-, Autonomous-,
Parallel-Autonomous- oder Implementierungslauf ohne einen neuen ausdrücklichen
Startauftrag. Drift schließt die Sperre erneut. Dieser Index startet selbst
keinen Review- oder Spec-Kit-Lauf.

*All 14 AOC intakes require current, formally validated `Ready` Single reviews
before the first downstream Spec Kit run. Until then, work is limited to the
remaining reviews, explicitly authorised repairs, read-only series status, and
required AEPS evidence capture. Lifecycle status or one Ready result does not
open the global gate. Once full coverage is current, `META-LH-01` is the first
allowed target and still needs a new explicit start instruction. Drift closes
the gate again. This index starts no workflow.*
