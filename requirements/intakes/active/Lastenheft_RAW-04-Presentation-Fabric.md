<!-- intake-authoring:begin -->
# RAW-04 – Presentation Fabric / Presentation Fabric

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Grundbegriffe von UI und Accessibility / basic UI and accessibility terms
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Die Presentation Fabric projiziert denselben State auf Console, JSON, TUI und
spätere Geräteflächen. Sie besitzt Layout, Fokus und Capability-Angebot, aber
keine Workspace-, State- oder Produktdomänenlogik. / *The presentation fabric
projects the same state to console, JSON, TUI, and later device surfaces. It
owns layout, focus, and capability presentation, not product state logic.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-169, 172, 181; RF-08, RF-17. Inputs: RAW-03 State Envelope und RAW-02
Orchestration Context. Output: barrierefreier Presentation Contract an RAW-07.

## Anforderungen / Requirements

- **FR-001:** Console und JSON sind verpflichtende Referenzprojektionen.
- **FR-002:** TUI MUSS Tastatur, sichtbaren Fokus, lineare Lesereihenfolge und Textalternative bieten.
- **FR-003:** Capability Routing DARF nicht an ein Herstellergerät gekoppelt sein.
- **FR-004:** Degraded/Unknown/Stale sind explizit und nicht nur farblich erkennbar.
- **NFR-001:** WCAG 2.2 AA, DE/EN und CEFR B2 gelten.
- **NFR-002:** Rendering DARF kanonischen State nicht verändern.

## Decisions, Dependencies und Mode / Decisions, dependencies, and mode

Offen: TUI/UI-Framework, Responsiveness und Lokalisierungsformat. Abhängig von
RAW-03, später RAW-02. `serial-autonomous`; parallele Surface-Prototypen erst
nach eingefrorenem Presentation Contract.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Console/JSON Baseline; TUI A11Y; Focus Model; Surface Capability Contract.
**AC-001:** identische Fixture ergibt semantisch gleiche Console-/JSON-Ausgabe.
**AC-002:** vollständiger Ablauf ist ohne Maus und ohne Farbe verständlich.
Negativ: fehlendes Label, Fokusverlust und Surface-Ausfall erzeugen sichtbare
Degraded Evidence.

Revision bei State-/A11Y-/Surface-Vertrag. Keine Command-, State- oder Hardwareprotokollautorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
