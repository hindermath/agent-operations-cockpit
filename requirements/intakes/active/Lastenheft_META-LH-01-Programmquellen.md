<!-- intake-authoring:begin -->
# META-LH-01 – Programmquellen, Constraints und vollständige Inhaltsübernahme / Programme Sources, Constraints, and Complete Content Transfer

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year IHK IT apprentices and experienced professionals
**Assumed prior knowledge:** IT-Grundlagen; keine Spec-Kit- oder Level-0-Geschichte / basic IT; no Spec Kit or level-0 history
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Dieses Lastenheft überführt alle für AOC erforderlichen Programmquellen,
Constraints, Findings, Decisions und Begriffe in eine eigenständige
Level-2-Baseline. Dadurch kann jede spätere Arbeit ohne versteckte fachliche
Abhängigkeit zu Level 0 beginnen. / *This intake transfers all AOC programme
sources, constraints, findings, decisions, and terms into a self-contained
level-2 baseline so later work has no hidden level-0 dependency.*

## Quellen und Traceability / Sources and traceability

Inputs sind SRC-156 bis SRC-182 und SRC-ES-01 aus `source-pack.md`; Owner für
RF-01, RF-04, RF-11 bis RF-17 sowie RF-21. / *Inputs are the source inventory;
this intake owns coverage for RF-01, RF-04, RF-11 through RF-17, and RF-21.*

## Scope und Non-Goals / Scope and non-goals

Im Scope: Source Inventory, Supersession, Constraint Register, Findings Ledger,
Coverage, Glossar, Authority Gates. Außerhalb: Produktarchitekturentscheidung,
Scaffold, Specify, Plan, Tasks, Code und Preset-Promotion. / *In scope are the
source, supersession, constraint, findings, coverage, glossary, and authority
baselines. Product design and execution workflows are out of scope.*

## Inputs und Outputs / Inputs and outputs

- Input: freigegebenes Phase-1-Übergabepaket und bestätigte Repository-Decisions.
- Output: `requirements/baseline/*` mit eindeutiger Authority und Revision.

## System-, Daten-, Trust- und Authority-Grenzen / Boundaries

Level-0-Issues sind unveränderliche Provenienz. Nur öffentlich geeignete,
de-duplizierte Inhalte gelangen in Level 2. Dieses Intake darf Level 0 lesen,
aber weder dort noch an Produktcode oder Remotes schreiben. / *Level-0 issues
are immutable provenance. This intake grants no write authority outside its
level-2 requirements paths.*

## Anforderungen / Requirements

- **FR-001:** Jede Quelle MUSS ID, Rolle, Inhalt, Authority, Aktualität,
  Supersession und Zielverwendung besitzen. / Each source MUST have those fields.
- **FR-002:** RF-01 bis RF-18 und neue Findings MÜSSEN Owner, Ziel,
  Akzeptanzkriterium, positive/negative Evidence, Status und Restlücke besitzen.
- **FR-003:** Kein blocking Finding DARF `Uncovered` sein.
- **FR-004:** Alle bestätigten Decisions und offenen Decisions MÜSSEN getrennt sein.
- **NFR-001:** DE-first/EN-second, CEFR B2 und Glossarregel sind verbindlich.
- **NFR-002:** Textstruktur MUSS WCAG 2.2 AA unterstützen; Status nie nur farblich.

## Abhängigkeiten, Decisions und Modus / Dependencies, decisions, and mode

Root der Meta-Reihe. Keine offene Materialentscheidung. Empfohlen:
`single-autonomous` nur für gebundene Dokumentpfade; aktueller Authoring-Lauf
ist `manual-assisted`. / *Root of the meta series; no open material decision.*

## Risiken und Annahmen / Risks and assumptions

Risiko: spätere Kommentare werden fälschlich als Supersession gelesen.
Gegenmaßnahme: nur explizite Decision mit Revisionsgrund ändert Authority.

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Alle Source-IDs aus dem Source Pack erscheinen genau einmal.
- **AC-002:** Ledger enthält RF-01..18 lückenlos und keine blocking Restlücke.
- **AC-003:** Ein Reviewer kann Ziel, Grenzen und Stop-Gates ohne Level-0-Lektüre erklären.
- **AC-004:** Bilingual-, B2- und A11Y-Review meldet keine blocking Abweichung.

## Evidence / Evidence

Positiv: vollständige Inventur, Coverage Matrix, Glossar und Review-Receipt.
Negativ: absichtlich entfernte RF-Zeile, konkurrierender Einstieg oder
unerklärter Begriff wird erkannt. / *Positive evidence is complete baselines;
negative fixtures detect a missing finding, competing entry point, or undefined term.*

## Revisionsbedingungen und Nicht-Autorität / Revision and non-authority

Revision bei neuer bestätigter Quelle, Decision, Supersession oder Finding.
Dieses Intake genehmigt weder Produktcode noch nachgelagerte Spec-Kit-Läufe.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
