<!-- intake-authoring:begin -->
# META-LH-05 – Generierung der ersten vollständigen Lastenheft-Welle / Generation of the First Complete Requirements Wave

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Grundverständnis der AOC-Schichten aus dem Source Pack / basic AOC layer understanding from the source pack
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Dieses Lastenheft erzeugt je fachlicher Owner-Reihe einen ersten eigenständigen
Intake und bindet ihn an Findings, Decisions, Evidence und Ausführungsmodus.
*This intake creates one first self-contained intake for every domain owner
series and binds it to findings, decisions, evidence, and execution mode.*

## Quellen und Findings / Sources and findings

Alle Source-IDs, Constraints, RF-01..21, META-01..04 und die bestätigte
Ownership Matrix.

## Scope, Inputs und Outputs / Scope, inputs, and outputs

Input: freigegebene Baseline und Portfolio. Output: RAW-01..RAW-09 als neue
aktive Intakes, Receipts, Coverage und Series-Einträge. Out of Scope: Review als
`Approved`, Specify, Plan, Tasks, Code oder Hardwareentwicklung.

## Grenzen / Boundaries

Wave Generation darf nur neue Ziele schreiben, atomar validieren und
`ReadyForReview` melden. Jede Reihe bleibt alleiniger Concern-Owner. / *Wave
generation may write only new targets, validate atomically, and report
ReadyForReview; each series remains its concern owner.*

## Anforderungen / Requirements

- **FR-001:** Genau neun erste fachliche Intakes MÜSSEN erzeugt werden.
- **FR-002:** Jeder Intake MUSS Zweck, Systemgrenze, erwartete Children,
  Decisions, I/O, Dependencies, Review/Evidence Gates und Modus enthalten.
- **FR-003:** Jede RF-Zeile MUSS mindestens einen Meta- und fachlichen Owner
  besitzen oder begründet rein meta-governed sein.
- **FR-004:** Alle Ziele und Receipts MÜSSEN vor Series-Publikation validiert sein.
- **FR-005:** Fehler MUSS die aktive Welle fail-closed stoppen.
- **NFR-001:** Alle neun Intakes erfüllen DE/EN, B2, Erstbegriff und WCAG-Textregeln.

## Dependencies, Mode und Recovery

Abhängig von META-01..04. `serial-autonomous` als sichere Voreinstellung;
paralleles Authoring nur für disjunkte Dateien nach expliziter Wave-Freigabe.
Recovery entfernt keine aktiven Ziele, sondern verwendet Operation Receipt und
separate Repair-/Update-Autorität.

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** RAW-01..09 existieren genau einmal und bestehen beide Validatoren.
- **AC-002:** Ownership und Coverage enthalten keine Lücke oder Mehrfachowner.
- **AC-003:** Kein Prompt wurde ausgeführt und kein Produktmanifest erzeugt.
- **AC-004:** Jede Reihe besitzt positive und negative Evidence vor Implementierung.

## Evidence / Evidence

Positiv: neun Intakes, Receipts, Hashes, Series-Manifest, 100-%-Validatorlauf.
Negativ: fehlender Intake, Owner-Duplikat, ungültiger Hash oder Produkt-Scaffold
blockiert Completion.

## Revision und Nicht-Autorität / Revision and non-authority

Revision bei Portfolio- oder Source-Baseline-Änderung. Keine Authority für
Review-Freigabe, Specify, Implementierung, Hardware oder Preset-Promotion.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
