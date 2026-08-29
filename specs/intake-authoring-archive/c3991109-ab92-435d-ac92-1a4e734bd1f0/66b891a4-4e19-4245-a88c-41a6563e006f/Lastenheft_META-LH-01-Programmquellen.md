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

## Begriffe für den Einstieg / Terms for first-time readers

- **Level 0 / Level 2:** Level 0 ist die persönliche kanonische Quelle; Level 2
  ist dieses eigenständige Projekt-Repository. / *Level 0 is the personal
  canonical source; Level 2 is this self-contained project repository.*
- **Constraint / verbindliche Vorgabe:** eine Grenze, die spätere Arbeit
  einhalten muss. / *A boundary that later work must respect.*
- **Finding / Prüffeststellung:** ein nachvollziehbarer Befund mit Owner,
  Kriterium und Nachweis. / *A traceable review observation with an owner,
  criterion, and evidence.*
- **Decision / Entscheidung:** eine ausdrücklich bestätigte Festlegung;
  **Supersession** ist ihre nachvollziehbare Ablösung. / *A Decision is an
  explicitly confirmed choice; Supersession is its traceable replacement.*
- **Coverage / Abdeckung:** Zuordnung einer Quelle oder Feststellung zu ihrem
  verantwortlichen Ziel. Ein **Authority Gate** begrenzt, welche Aktion aktuell
  erlaubt ist. / *Coverage maps a source or finding to its responsible target.
  An Authority Gate limits which action is currently allowed.*
- **Scaffold:** erzeugtes Projektgrundgerüst. **Specify**, **Plan** und **Tasks**
  sind getrennte Spec-Kit-Schritte für Spezifikation, Planung und Aufgaben.
  **Preset-Promotion** überführt nur generalisierbare Evidence in einen getrennt
  freigegebenen Governance-Vorschlag. / *A scaffold is a generated project
  skeleton. Specify, Plan, and Tasks are separate Spec Kit steps. Preset
  promotion transfers only generalisable evidence into a separately approved
  governance proposal.*
- **`manual-assisted` / `single-autonomous`:** Im ersten Modus bestätigt ein
  Mensch materielle Schritte; im zweiten darf genau ein eng begrenzter,
  separat freigegebener Lauf arbeiten. / *In the first mode, a human confirms
  material steps; in the second, exactly one narrowly scoped and separately
  authorised run may work.*

Weitere Begriffe wie Evidence, Owner, Receipt und Stop-Gate erklärt das
[zweisprachige Glossar](../../baseline/glossary.md). / *The
[bilingual glossary](../../baseline/glossary.md) explains additional terms such
as evidence, owner, receipt, and stop gate.*

## Quellen und Nachverfolgbarkeit / Sources and traceability

Inputs sind SRC-156 bis SRC-182 und SRC-ES-01 aus `source-pack.md`; Owner für
RF-01, RF-04, RF-11 bis RF-17 sowie RF-21. / *Inputs are the source inventory;
this intake owns coverage for RF-01, RF-04, RF-11 through RF-17, and RF-21.
Only the source identifiers explicitly listed in the source pack are included;
the numeric range does not invent missing identifiers.*

## Scope und Non-Goals / Scope and non-goals

Im Scope: Quelleninventur, nachvollziehbare Ablösung, Vorgabenregister,
Findings-Ledger, Abdeckungsmatrix, Glossar und Authority Gates. Außerhalb:
Produktarchitekturentscheidung, Scaffold, Specify, Plan, Tasks, Code und
Preset-Promotion. / *In scope are the source inventory, supersession,
constraint register, findings ledger, coverage matrix, glossary, and authority
gates. Product-architecture decisions, scaffolding, Specify, Plan, Tasks, code,
and preset promotion are out of scope.*

## Inputs und Outputs / Inputs and outputs

- Input: freigegebenes Phase-1-Übergabepaket und bestätigte
  Repository-Decisions. / *Input: the approved Phase-1 handoff package and
  confirmed repository decisions.*
- Output: `requirements/baseline/*` mit eindeutiger Authority und Revision. /
  *Output: `requirements/baseline/*` with explicit authority and revision.*

## System-, Daten-, Trust- und Authority-Grenzen / Boundaries

Level-0-Issues sind unveränderliche Provenienz. Nur öffentlich geeignete,
de-duplizierte Inhalte gelangen in Level 2. Dieses Intake darf Level 0 lesen,
aber weder dort noch an Produktcode oder Remotes schreiben. / *Level-0 issues
are immutable provenance. This intake grants no write authority outside its
level-2 requirements paths.*

Security (Sicherheit) und Privacy (Datenschutz) verlangen ausschließlich
öffentlich geeignete Inhalte ohne Secrets, private Pfade oder unnötige
Personendaten. WCAG 2.2 AA ist der verbindliche Standard für zugängliche
Dokumentstruktur; auch die zweisprachige Textstruktur ist auf alle Dokumente
anwendbar. Plattform- und
Software-Lieferkettenanforderungen sind für dieses reine Dokumentations-Intake
`N/A`, weil es weder ausführbaren Code noch Build- oder Paketabhängigkeiten
erzeugt; diese Einstufung wird bei einem Generator- oder Dependency-Handoff
neu geprüft. / *Security and privacy permit only public-suitable content without
secrets, private paths, or unnecessary personal data. WCAG 2.2 AA and the
bilingual text structure apply to every document. Platform and software
supply-chain requirements are `N/A` for this documentation-only intake because
it creates no executable code, build, or package dependency; applicability is
re-evaluated when a generator or dependency is introduced.*

## Anforderungen / Requirements

- **FR-001:** Jede Quelle MUSS ID, Rolle, Inhalt, Authority, Aktualität,
  Supersession und Zielverwendung besitzen. / *Each source MUST have an ID,
  role, content description, authority, currency, supersession state, and
  target use.*
- **FR-002:** RF-01 bis RF-18 und neue Findings MÜSSEN Owner, Ziel,
  Akzeptanzkriterium, positive/negative Evidence, Status und Restlücke besitzen.
  / *RF-01 through RF-18 and every new finding MUST identify an owner, target,
  acceptance criterion, positive and negative evidence, status, and residual gap.*
- **FR-003:** Kein blocking Finding DARF `Uncovered` sein. / *A blocking
  finding MUST NOT remain `Uncovered`.*
- **FR-004:** Alle bestätigten Decisions und offenen Decisions MÜSSEN getrennt
  sein. / *Confirmed and open decisions MUST remain separate.*
- **NFR-001:** Deutsch zuerst, Englisch danach, CEFR B2 und Glossarregel sind
  verbindlich. / *German first, English second, CEFR B2, and the glossary rule
  are binding.*
- **NFR-002:** Die Textstruktur MUSS WCAG 2.2 AA unterstützen; Status darf nie
  nur farblich vermittelt werden. / *The text structure MUST support WCAG 2.2
  AA; status MUST never rely on colour alone.*

## Abhängigkeiten, Decisions und Modus / Dependencies, decisions, and mode

Root der Meta-Reihe. Keine offene Materialentscheidung. Empfohlen:
`single-autonomous` nur für gebundene Dokumentpfade; aktueller Authoring-Lauf
ist `manual-assisted`. Nächste Aktion ist ausschließlich das unabhängige
Single-Intake-Review. / *This is the root of the meta series and has no open
material decision. `single-autonomous` is recommended only for bound document
paths; the current authoring run is `manual-assisted`. The only next action is
the independent single-intake review.*

## Risiken und Annahmen / Risks and assumptions

Risiko: spätere Kommentare werden fälschlich als Supersession gelesen.
Gegenmaßnahme: nur explizite Decision mit Revisionsgrund ändert Authority.
Die Annahme ist, dass das freigegebene Phase-1-Paket vollständig in der
Level-2-Baseline vertreten ist. / *Risk: later comments may be mistaken for
supersession. Mitigation: only an explicit decision with a revision reason may
change authority. The approved Phase-1 package is assumed to be represented
completely in the Level-2 baseline.*

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Alle im Source Pack ausdrücklich genannten Source-IDs erscheinen
  genau einmal. / *Every source ID explicitly named in the source pack occurs
  exactly once.*
- **AC-002:** Das Ledger enthält RF-01 bis RF-18 lückenlos und keine blocking
  Restlücke. / *The ledger contains RF-01 through RF-18 without gaps and no
  blocking residual gap.*
- **AC-003:** Ein Reviewer kann Ziel, Grenzen und Stop-Gates ohne
  Level-0-Lektüre erklären. / *A reviewer can explain the goal, boundaries, and
  stop gates without reading Level 0.*
- **AC-004:** Bilingual-, B2- und A11Y-Review meldet keine blocking Abweichung.
  / *The bilingual, B2, and accessibility review reports no blocking deviation.*

## Nachweise / Evidence

Positiv: vollständige Inventur, Coverage Matrix, Glossar und Review-Receipt.
Negativ: absichtlich entfernte RF-Zeile, konkurrierender Einstieg oder
unerklärter Begriff wird erkannt. / *Positive evidence is complete baselines;
negative fixtures detect a missing finding, competing entry point, or
undefined term. A secret scan and explicit `N/A` applicability decisions cover
the security and supply-chain boundary.*

## Revisionsbedingungen und Nicht-Autorität / Revision and non-authority

Revision bei neuer bestätigter Quelle, Decision, Supersession oder Finding.
Dieses Intake genehmigt weder Produktcode noch nachgelagerte Spec-Kit-Läufe.
Jeder solche Lauf benötigt eine eigene aktuelle Start- und Scope-Autorität. /
*Revise this intake for a new confirmed source, decision, supersession, or
finding. This intake approves neither product code nor a downstream Spec Kit
run; every such run needs separate current start and scope authority.*

<!-- intake-authoring:prompts -->
## Direkt nutzbare Spec-Kit-Prompts / Copy-ready Spec Kit prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify

```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md --bind-exact-intake --no-implementation --no-remote-writes
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous

```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md --delivery-mode MergeAndSync --require-current-review
VORBEDINGUNG / PRECONDITION: Nicht starten, solange keine separate aktuelle Benutzerentscheidung Scope, Implementierung, Remote Writes, Merge und Bypass ausdrücklich autorisiert. / Do not start unless a separate current user decision explicitly authorizes the downstream scope, implementation, remote writes, merge, and bypass.
```
<!-- intake-authoring:end -->
