# Programmquellenpaket / Program Source Pack

## Zweck und Autorität / Purpose and authority

Dieses Paket ist die eigenständige fachliche Quelle für das AOC-Lastenheftprogramm.
Die genannten Level-0-Issues bleiben Provenienz, sind aber keine notwendige
Laufzeit- oder Leseabhängigkeit. Bei Konflikten gilt: bestätigte Level-2-Decisions
vor diesem Paket, dieses Paket vor älteren Entwürfen; ein neuerer Text ersetzt
einen älteren nur mit ausdrücklicher Supersession.

*This pack is the self-contained domain source for the AOC requirements
programme. The named level-0 issues remain provenance, not a runtime or reading
dependency. Confirmed level-2 decisions take precedence over this pack, and
this pack takes precedence over older drafts. Newer text supersedes older text
only when explicitly declared.*

## Quelleninventur / Source inventory

| Source-ID | Rolle / Role | Autorität und Inhalt / Authority and content | Aktualität und Supersession / Currency and supersession | Phase-2-Verwendung / Use |
|---|---|---|---|---|
| SRC-156 | Meta-Initiative | Fachlicher Ursprung: agentische Entwicklungsumgebungen als zusammenhängendes Programm. / Domain origin for an integrated agentic-development programme. | Historische Leitquelle; durch Charter und Verträge präzisiert. / Historical guide refined by charter and contracts. | Programmabsicht und Scope. |
| SRC-157 | Program Charter | Zweck, Nutzen, Zielarchitektur und Programmgrenzen. / Purpose, value, target architecture, and programme boundaries. | Autoritativ für fachliche Ziele, soweit spätere Decisions nicht abweichen. / Authoritative for goals unless later decisions differ. | Alle Reihen. |
| SRC-159 | Execution Contract | Lastenheft-Authoring, Traceability, Review, Evidence und Receipts. / Requirements authoring, traceability, review, evidence, and receipts. | Operativer Authoring-Vertrag; kein Bootstrap-Einstieg. / Authoring contract, not bootstrap entry. | META-03 bis META-05. |
| SRC-161 | Development Workspace | IDE, Terminal, Git, Agenten und Werkzeuge als beobachtbarer Workspace. / IDE, terminal, Git, agents, and tools as an observable workspace. | Detailquelle. | RAW-01 und RAW-02. |
| SRC-162 | ADE/IDE/CLI Orchestration | CLI-first Capability- und Environment-Orchestrierung. / CLI-first capability and environment orchestration. | Detailquelle. | RAW-02 und RAW-06. |
| SRC-163–167 | Zwischenentwürfe / Intermediate drafts | Frühere Teilideen zu Workspace, UI und Bedienung. / Earlier partial workspace, UI, and operation ideas. | Nur Provenienz; konsolidiert durch SRC-172, SRC-177 und dieses Paket. / Provenance only; consolidated by later sources. | Konfliktprüfung, keine eigene Owner-Reihe. |
| SRC-168 | Engineering Knowledge Loop | Rückführung von Evidence und Retrospektiven in Wissen. / Feedback from evidence and retrospectives into knowledge. | Fachliche Quelle. | RAW-08 und RAW-09. |
| SRC-169 | Vendor-neutral Physical Console | Herstellerneutrale Capability-Abstraktion. / Vendor-neutral capability abstraction. | Durch SRC-172/175 präzisiert. | RAW-04 und RAW-07. |
| SRC-170 | Preset Gap Analysis | Lücken und Evolution der Governance-Presets. / Governance preset gaps and evolution. | Evidence-/Preset-Evolution-Quelle. | RAW-09. |
| SRC-171 | NI F1 Field Evaluation | Hardwarebeobachtungen und Grenzen; kein Architekturvertrag. / Hardware observations and limits, not an architecture contract. | Field Evidence. | RAW-07 Decision Inputs. |
| SRC-172 | AOC and Presentation Fabric | Cockpit, Presentation Fabric, Manager, Projektion und Routing. / Cockpit, presentation fabric, manager, projection, and routing. | Kanonische Detailquelle für Darstellung. | RAW-03 und RAW-04. |
| SRC-173 | Xbox Field Evaluation | Controller-Evidence und plattformbezogene Einschränkungen. / Controller evidence and platform constraints. | Field Evidence. | RAW-07 Decision Inputs. |
| SRC-174 | Program-to-Knowledge Pipeline | Workflow vom Programmauftrag bis zu Evidence und Retrospektive. / Workflow from programme intent to evidence and retrospective. | Kanonische Pipeline-Quelle. | RAW-08 und RAW-09. |
| SRC-175 | Hardware Capability Reference Lab | Reproduzierbare, herstellerneutrale Hardwareevaluation. / Reproducible vendor-neutral hardware evaluation. | Hardware-/Field-Evaluation-Quelle. | RAW-07. |
| SRC-177 | Bootstrap and Reference Workspace | Programmeinstieg, Repositoryebenen, Reference Agentic Workspace und Bootstrap-Kontext. / Programme entry, repository levels, reference workspace, and bootstrap context. | Ersetzt #159 als Bootstrap-Einstieg. / Supersedes #159 as bootstrap entry. | Repository und RAW-01. |
| SRC-180 | Phase-1 Readiness Gate | Autorität, reine Wissensphase, Stop-Grenze und Übergabepaket. / Authority, knowledge-only phase, stop boundary, and handoff. | Phase 1 abgeschlossen; Inhalte hier konserviert. / Phase 1 completed; content preserved here. | Provenienz und Gate-Nachweis. |
| SRC-181 | Review Findings Register | RF-01 bis RF-18 mit Severity und erwarteter Auflösung. / RF-01 through RF-18 with severity and expected resolution. | Kanonische Findings-Quelle. | Findings Ledger und Coverage. |
| SRC-182 | Phase-2 Contract | Öffentliches Level-2-Repository, Meta-Reihe und erste fachliche Welle. / Public level-2 repository, meta series, and first domain wave. | Aktueller Phase-2-Zielvertrag. / Current Phase-2 target contract. | Gesamtes Programm. |
| SRC-ES-01 | Engineering Session 2026-07-30 | Konsolidierte Architektur- und Governance-Erkenntnisse. / Consolidated architecture and governance knowledge. | Wissensquelle, nicht selbst Ausführungsautorität. / Knowledge source, not execution authority. | De-Duplizierung und Begriffe. |

## Konsolidiertes Zielbild / Consolidated target

Das AOC ist die zugängliche Interaktions- und Beobachtungsschicht über einem
Workspace Orchestrator. Der Start-Slice liest Workspace- und Repositoryzustand,
bestimmt Authority und Freshness und projiziert dieselbe Zustandswahrheit in
Console, JSON und später TUI. Reversible Commands, Hardwareadapter und
Multi-Device-Steuerung folgen erst nach eigenen Decisions und Gates.

*AOC is the accessible interaction and observation layer above a workspace
orchestrator. The first slice reads workspace and repository state, establishes
authority and freshness, and projects the same truthful state to console, JSON,
and later TUI. Reversible commands, hardware adapters, and multi-device control
follow only after their own decisions and gates.*

## Verbindliche Schichten / Binding layers

```text
Presentation Fabric
  -> Workspace Orchestrator
    -> State Truthfulness
      -> Reference Agentic Workspace
        -> Execution Nodes and CLI Capabilities

Hardware Capability Layer -> Presentation Fabric (thin adapters only)
Workflow Engine -> requirements, decisions, evidence, retrospectives
Preset Evolution <- measured evidence, never product authority
```

Die Textdarstellung ist normativ. Pfeile bedeuten Daten- oder Vertragsübergabe,
nicht automatisch Schreibautorität. / *The text representation is normative.
Arrows mean data or contract handoff, not automatic write authority.*

## Bestätigte Decisions / Confirmed decisions

- DEC-001: Product `Agent Operations Cockpit`, Repository
  `hindermath/agent-operations-cockpit`, Public, `main`, MIT.
- DEC-002: C#/.NET ist Primärplattform; konkrete Runtime- und Frameworkdetails
  bleiben offen. / C#/.NET is primary; runtime and framework details remain open.
- DEC-003: CLI-first; Oberflächen projizieren und orchestrieren Capabilities.
- DEC-004: Fünf Meta-Lastenhefte bleiben getrennt, weil Source Governance,
  Ownership, Authoring, Scheduling und Wave Generation unterschiedliche
  Review- und Authority-Grenzen besitzen.
- DEC-005: Der erste Produktslice ist read-only; Commands und Hardware sind
  nachgelagert. / The first product slice is read-only.
- DEC-006: `MergeAndSync` mit Admin-Bypass ist nur ausdrücklich genehmigten
  Lieferungen erlaubt; es ersetzt keine Qualitäts- oder Reviewnachweise.

## Supersession / Supersession

- #177 ist Bootstrap- und Programmeinstieg; #159 bleibt Authoring-Vertrag.
- #180 war das Phase-1-Gate; #182 und die freigegebenen Level-2-Artefakte regeln
  Phase 2.
- Dieses Paket ersetzt verstreute Kommentare als operative Inhaltsquelle, ohne
  deren Provenienz zu löschen.
- Feldtests #171/#173 liefern Evidence, aber keine Produkt- oder
  Architekturautorität.
