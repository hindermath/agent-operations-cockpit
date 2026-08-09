# Programmquellenpaket / Program Source Pack

## Zweck und Autorität / Purpose and authority

Dieses Paket ist die eigenständige fachliche Quelle für das
Agent-Operations-Cockpit-(AOC)-Lastenheftprogramm.
Level-0-Issues bleiben Provenienz, sind aber keine notwendige Lese- oder
Laufzeitabhängigkeit. Bei Konflikten gelten bestätigte Level-2-Decisions vor
diesem Paket und dieses Paket vor älteren Entwürfen. Ein neueres Datum oder ein
neuer Kommentar ersetzt keine Quelle ohne ausdrückliche Decision mit
Revisionsgrund. / *This pack is the self-contained domain source for the Agent
Operations Cockpit (AOC) requirements programme. Level-0 issues remain
provenance, not a required reading or runtime dependency. Confirmed level-2
decisions precede this pack,
and this pack precedes older drafts. A newer date or comment supersedes no
source without an explicit decision and revision rationale.*

Die Fachbegriffe Level 0, Provenienz, Laufzeitabhängigkeit, Program Charter,
ADE, Field Evidence, Presentation Fabric, Workspace Orchestrator, State
Truthfulness, Bootstrap und Multi-Device-Steuerung werden im
[Glossar](glossary.md) erklärt. / *The specialist terms Level 0, provenance,
runtime dependency, programme charter, ADE, field evidence, presentation
fabric, workspace orchestrator, state truthfulness, bootstrap, and
multi-device control are explained in the [glossary](glossary.md).*

## Quelleninventur / Source inventory

Jede zugelassene Quelle steht genau einmal in einer eigenen Zeile. Die
numerischen Lücken `SRC-158`, `SRC-160`, `SRC-176`, `SRC-178` und `SRC-179`
sind keine Quellen. / *Every permitted source has exactly one individual row.
The five named numeric gaps are not sources.*

| Source-ID | Rolle / Role | Inhaltsbeschreibung / Content description | Autorität / Authority | Aktualität / Currency | Supersession-Status / Supersession status | Zielverwendung / Target use |
|---|---|---|---|---|---|---|
| SRC-156 | Meta-Initiative / Meta initiative | Ursprung eines zusammenhängenden Programms für agentische Entwicklungsumgebungen. / Origin of an integrated agentic-development programme. | Historische Leitquelle / Historical guiding source | Historisch, weiterhin als Provenienz gültig. / Historical and still valid as provenance. | Durch Charter und Verträge präzisiert, nicht gelöscht. / Refined by charter and contracts, not removed. | Programmabsicht und Scope. / Programme intent and scope. |
| SRC-157 | Programmcharta / Programme charter | Zweck, Nutzen, Zielbild und Programmgrenzen. / Purpose, value, target vision, and programme boundaries. | Autoritativ für fachliche Ziele, sofern keine spätere Decision abweicht. / Authoritative for domain goals unless a later decision differs. | Aktuelle Charter-Grundlage / Current charter baseline | Keine bestätigte Ablösung. / No confirmed supersession. | Alle Owner-Reihen. / All owner series. |
| SRC-159 | Ausführungs- und Authoring-Vertrag / Execution and authoring contract | Lastenheft-Authoring, Traceability, Review, Evidence und Receipts. / Requirements authoring, traceability, review, evidence, and receipts. | Autoritativ für Authoring, nicht für Bootstrap. / Authoritative for authoring, not bootstrap. | Aktueller operativer Authoring-Vertrag / Current operational authoring contract | Als Bootstrap-Einstieg durch SRC-177 abgelöst; Authoring-Rolle bleibt. / Superseded as bootstrap entry by SRC-177; authoring role remains. | META-03 bis META-05. / META-03 through META-05. |
| SRC-161 | Entwicklungs-Workspace / Development workspace | IDE, Terminal, Git, Agenten und Werkzeuge als beobachtbarer Workspace. / IDE, terminal, Git, agents, and tools as an observable workspace. | Fachliche Detailquelle / Domain detail source | Aktuell als Detailquelle / Current as a detail source | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-01 und RAW-02. / RAW-01 and RAW-02. |
| SRC-162 | ADE-/IDE-/CLI-Orchestrierung / ADE, IDE, and CLI orchestration | CLI-first Capability- und Environment-Orchestrierung. / CLI-first capability and environment orchestration. | Fachliche Detailquelle / Domain detail source | Aktuell als Detailquelle / Current as a detail source | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-02 und RAW-06. / RAW-02 and RAW-06. |
| SRC-163 | Zwischenentwurf Workspace / Intermediate workspace draft | Frühe Teilidee zum Workspace. / Early partial workspace idea. | Nur Provenienz / Provenance only | Historisch / Historical | Durch SRC-172, SRC-177 und dieses Paket konsolidiert. / Consolidated by SRC-172, SRC-177, and this pack. | Konfliktprüfung, keine eigene Owner-Reihe. / Conflict review, no separate owner series. |
| SRC-164 | Zwischenentwurf Oberfläche / Intermediate interface draft | Frühe Teilidee zur Oberfläche. / Early partial interface idea. | Nur Provenienz / Provenance only | Historisch / Historical | Durch SRC-172, SRC-177 und dieses Paket konsolidiert. / Consolidated by SRC-172, SRC-177, and this pack. | Konfliktprüfung, keine eigene Owner-Reihe. / Conflict review, no separate owner series. |
| SRC-165 | Zwischenentwurf Bedienung / Intermediate operation draft | Frühe Teilidee zur Bedienung. / Early partial operation idea. | Nur Provenienz / Provenance only | Historisch / Historical | Durch SRC-172, SRC-177 und dieses Paket konsolidiert. / Consolidated by SRC-172, SRC-177, and this pack. | Konfliktprüfung, keine eigene Owner-Reihe. / Conflict review, no separate owner series. |
| SRC-166 | Zwischenentwurf Projektion / Intermediate projection draft | Frühe Teilidee zur Zustandsprojektion. / Early partial state-projection idea. | Nur Provenienz / Provenance only | Historisch / Historical | Durch SRC-172, SRC-177 und dieses Paket konsolidiert. / Consolidated by SRC-172, SRC-177, and this pack. | Konfliktprüfung, keine eigene Owner-Reihe. / Conflict review, no separate owner series. |
| SRC-167 | Zwischenentwurf Integration / Intermediate integration draft | Frühe Teilidee zur Integration. / Early partial integration idea. | Nur Provenienz / Provenance only | Historisch / Historical | Durch SRC-172, SRC-177 und dieses Paket konsolidiert. / Consolidated by SRC-172, SRC-177, and this pack. | Konfliktprüfung, keine eigene Owner-Reihe. / Conflict review, no separate owner series. |
| SRC-168 | Engineering-Wissenskreislauf / Engineering knowledge loop | Rückführung von Evidence und Retrospektiven in Wissen. / Feedback from evidence and retrospectives into knowledge. | Fachliche Quelle / Domain source | Aktuell / Current | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-08 und RAW-09. / RAW-08 and RAW-09. |
| SRC-169 | Herstellerneutrale physische Konsole / Vendor-neutral physical console | Herstellerneutrale Capability-Abstraktion für physische Bedienflächen. / Vendor-neutral capability abstraction for physical controls. | Fachliche Quelle / Domain source | Aktuell, durch spätere Details präzisiert. / Current and refined by later detail sources. | Durch SRC-172 und SRC-175 präzisiert. / Refined by SRC-172 and SRC-175. | RAW-04 und RAW-07. / RAW-04 and RAW-07. |
| SRC-170 | Preset-Lückenanalyse / Preset gap analysis | Lücken und Evolution der Governance-Presets. / Gaps and evolution of governance presets. | Evidence-Quelle, keine Produkt-Authority / Evidence source, not product authority | Aktuell als Evidence / Current as evidence | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-09. / RAW-09. |
| SRC-171 | NI-F1-Feldevaluation / NI F1 field evaluation | Hardwarebeobachtungen und Grenzen. / Hardware observations and limits. | Field Evidence, kein Architekturvertrag / Field evidence, not an architecture contract | Feldnachweis / Field evidence | Keine Ablösung; durch Capability-Verträge eingeordnet. / Not superseded; bounded by capability contracts. | RAW-07 Decision Inputs. / RAW-07 decision inputs. |
| SRC-172 | AOC und Presentation Fabric / AOC and presentation fabric | Cockpit, Presentation Fabric, Manager, Projektion und Routing. / Cockpit, presentation fabric, manager, projection, and routing. | Kanonische Detailquelle für Darstellung / Canonical presentation detail source | Aktuell / Current | Konsolidiert ältere UI-Entwürfe. / Consolidates earlier interface drafts. | RAW-03 und RAW-04. / RAW-03 and RAW-04. |
| SRC-173 | Xbox-Feldevaluation / Xbox field evaluation | Controller-Evidence und Plattformgrenzen. / Controller evidence and platform constraints. | Field Evidence, keine Produkt-Authority / Field evidence, not product authority | Feldnachweis / Field evidence | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-07 Decision Inputs. / RAW-07 decision inputs. |
| SRC-174 | Programm-zu-Wissen-Pipeline / Programme-to-knowledge pipeline | Workflow vom Programmauftrag bis zu Evidence und Retrospektive. / Workflow from programme intent to evidence and retrospective. | Kanonische Pipeline-Quelle / Canonical pipeline source | Aktuell / Current | Keine bestätigte Ablösung. / No confirmed supersession. | RAW-08 und RAW-09. / RAW-08 and RAW-09. |
| SRC-175 | Hardware-Fähigkeits-Referenzlabor / Hardware capability reference lab | Reproduzierbare, herstellerneutrale Hardwareevaluation. / Reproducible vendor-neutral hardware evaluation. | Hardware- und Feldevaluationsquelle / Hardware and field-evaluation source | Aktuell / Current | Präzisiert SRC-169. / Refines SRC-169. | RAW-07. / RAW-07. |
| SRC-177 | Bootstrap und Reference Workspace / Bootstrap and reference workspace | Programmeinstieg, Repositoryebenen, Reference Agentic Workspace und Bootstrap-Kontext. / Programme entry, repository levels, reference workspace, and bootstrap context. | Autoritativ für Bootstrap und Programmeinstieg / Authoritative for bootstrap and programme entry | Aktuell / Current | Ersetzt SRC-159 nur als Bootstrap-Einstieg. / Supersedes SRC-159 only as bootstrap entry. | Repository und RAW-01. / Repository and RAW-01. |
| SRC-180 | Phase-1-Readiness-Gate / Phase-1 readiness gate | Authority, reine Wissensphase, Stop-Grenze und Übergabepaket. / Authority, knowledge-only phase, stop boundary, and handoff package. | Historische Gate-Evidence / Historical gate evidence | Phase 1 abgeschlossen / Phase 1 completed | Durch SRC-182 für Phase 2 fortgeschrieben; Evidence bleibt erhalten. / Continued by SRC-182 for Phase 2; evidence remains. | Provenienz und Gate-Nachweis. / Provenance and gate evidence. |
| SRC-181 | Review-Findings-Register / Review findings register | RF-01 bis RF-18 mit Severity und erwarteter Auflösung. / RF-01 through RF-18 with severity and expected resolution. | Kanonische Findings-Quelle / Canonical findings source | Aktuell für die gebundenen Findings / Current for bound findings | Durch neue bestätigte Findings ergänzt, nicht ersetzt. / Extended by newly confirmed findings, not superseded. | Findings Ledger und Coverage. / Findings ledger and coverage. |
| SRC-182 | Phase-2-Vertrag / Phase-2 contract | Öffentliches Level-2-Repository, Meta-Reihe und erste fachliche Welle. / Public level-2 repository, meta series, and first domain wave. | Aktueller Phase-2-Zielvertrag / Current Phase-2 target contract | Aktuell / Current | Schreibt SRC-180 für Phase 2 fort. / Continues SRC-180 for Phase 2. | Gesamtes Programm. / Entire programme. |
| SRC-ES-01 | Engineering-Sitzung 2026-07-30 / Engineering session 2026-07-30 | Konsolidierte Architektur- und Governance-Erkenntnisse. / Consolidated architecture and governance knowledge. | Wissensquelle, keine Ausführungsautorität / Knowledge source, not execution authority | Aktuelle Wissensprovenienz / Current knowledge provenance | Keine bestätigte Ablösung. / No confirmed supersession. | De-Duplizierung und Begriffe. / Deduplication and terminology. |

## Konsolidiertes Zielbild / Consolidated target

Das AOC ist die zugängliche Interaktions- und Beobachtungsschicht über einem
Workspace Orchestrator. Der erste Produktslice liest Workspace- und
Repositoryzustand, bestimmt Authority und Freshness und projiziert dieselbe
Zustandswahrheit in Console, JSON und später TUI. Reversible Commands,
Hardwareadapter und Multi-Device-Steuerung folgen erst nach eigenen Decisions
und Gates. / *AOC is the accessible interaction and observation layer above a
workspace orchestrator. The first product slice reads workspace and repository
state, establishes authority and freshness, and projects the same truthful
state to console, JSON, and later TUI. Reversible commands, hardware adapters,
and multi-device control follow only after their own decisions and gates.*

## Verbindliche Schichten / Binding layers

```text
Darstellungsschicht / Presentation Fabric
  -> Arbeitsbereichs-Orchestrator / Workspace Orchestrator
    -> Wahrheitsgetreuer Zustand / State Truthfulness
      -> Referenz-Arbeitsbereich / Reference Agentic Workspace
        -> Ausfuehrungsknoten und CLI-Faehigkeiten / Execution Nodes and CLI Capabilities

Hardware-Faehigkeitsschicht / Hardware Capability Layer
  -> Darstellungsschicht / Presentation Fabric (nur duenne Adapter / thin adapters only)
Workflow-Engine / Workflow Engine
  -> Anforderungen, Entscheidungen, Nachweise, Retrospektiven / requirements, decisions, evidence, retrospectives
Preset-Evolution / Preset Evolution
  <- gemessene Nachweise, niemals Produktautoritaet / measured evidence, never product authority
```

Die Textdarstellung ist normativ. Pfeile bedeuten Daten- oder Vertragsübergabe,
nicht automatisch Schreibautorität. / *The text representation is normative.
Arrows mean data or contract handoff, not automatic write authority.*

## Bestätigte und offene Decisions / Confirmed and open decisions

- DEC-001: Produkt `Agent Operations Cockpit`, Repository
  `hindermath/agent-operations-cockpit`, öffentlich, `main`, MIT. / *Product,
  `Agent Operations Cockpit`, repository `hindermath/agent-operations-cockpit`,
  public visibility, default branch `main`, and MIT licence are confirmed.*
- DEC-002: C#/.NET ist Primärplattform; Runtime- und Frameworkdetails bleiben
  offen. / *C#/.NET is primary; runtime and framework details remain open.*
- DEC-003: CLI-first; Oberflächen projizieren und orchestrieren Capabilities. /
  *Interfaces project and orchestrate capabilities.*
- DEC-004: Fünf Meta-Lastenhefte bleiben getrennt, weil sie unterschiedliche
  Review- und Authority-Grenzen besitzen. / *Five meta intakes remain separate
  because they have different review and authority boundaries.*
- DEC-005: Der erste Produktslice ist read-only; Commands und Hardware sind
  nachgelagert. / *The first product slice is read-only; commands and hardware
  are downstream.*
- DEC-006: `MergeAndSync` mit Admin-Bypass ist nur ausdrücklich genehmigten
  Lieferungen erlaubt und ersetzt keine Qualitäts- oder Reviewevidence. /
  *MergeAndSync with admin bypass requires explicit delivery authority and
  never replaces quality or review evidence.*

Es bestehen derzeit keine offenen materiellen Decisions für diese Baseline. /
*There are currently no open material decisions for this baseline.*

## Supersession / Supersession

- SRC-177 ist Bootstrap- und Programmeinstieg; SRC-159 bleibt
  Authoring-Vertrag. / *SRC-177 owns bootstrap entry; SRC-159 remains the
  authoring contract.*
- SRC-180 war das Phase-1-Gate; SRC-182 und die freigegebenen
  Level-2-Artefakte regeln Phase 2. / *SRC-180 was the Phase-1 gate; SRC-182 and
  accepted level-2 artefacts govern Phase 2.*
- Dieses Paket ersetzt verstreute Kommentare als operative Inhaltsquelle,
  ohne deren Provenienz zu löschen. / *This pack replaces scattered comments
  as the operational content source without deleting provenance.*
- Feldtests SRC-171 und SRC-173 liefern Evidence, aber keine Produkt- oder
  Architekturautorität. / *Field tests provide evidence but no product or
  architecture authority.*

## Leserpfad und nächste Aktion / Reader path and next action

Lies als Nächstes das [Constraint Register](constraint-register.md), danach das
[Findings Ledger](review-findings-ledger.md), die
[Coverage Matrix](coverage-matrix.md), das [Glossar](glossary.md) und zuletzt
die [Authority- und Stop-Gates](authority-and-stop-gates.md). Die einzige
sichere nächste Aktion ist, diesen Leserpfad vollständig zu prüfen; daraus
entsteht weder Produkt-, Preset- noch Remote-Autorität. / *Read the constraint
register, findings ledger, coverage matrix, glossary, and authority and stop
gates in that order. The only safe next action is to review the complete reader
path; it grants no product, preset, or remote authority.*
