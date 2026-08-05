# Agent Operations Cockpit

## Zweck und Status / Purpose and status

Agent Operations Cockpit (AOC) ist ein öffentliches C#/.NET-Level-2-Projekt zur
nachvollziehbaren Beobachtung und späteren Steuerung agentischer
Entwicklungsumgebungen. „Agentisch“ bedeutet hier: KI-Werkzeuge bearbeiten klar
begrenzte Aufgaben mit dokumentierter Autorität, Evidence (prüfbaren
Nachweisen) und menschlichen Stop-Gates.

Der aktuelle Stand enthält ausschließlich die Wissens-, Governance- und
Lastenheftgrundlage. Es gibt noch keinen Produktcode. Eine konkrete
.NET-Version, ein Testframework, Logging, IPC (Kommunikation zwischen
Prozessen), Native AOT und Hardwareadapter sind bewusst nicht festgelegt.

*Agent Operations Cockpit (AOC) is a public C#/.NET level-2 project for the
traceable observation and later control of agentic development environments.
Here, “agentic” means that AI tools work on clearly bounded tasks with
documented authority, evidence, and human stop gates.*

*The current state contains only the knowledge, governance, and requirements
baseline. No product code exists yet. The exact .NET version, test framework,
logging, inter-process communication (IPC), Native AOT, and hardware adapters
are intentionally undecided.*

## Zielgruppe und Barrierefreiheit / Audience and accessibility

Die Dokumentation richtet sich an Auszubildende der IHK-IT-Berufe ab dem ersten
Ausbildungsjahr und an erfahrene Fachkräfte. Inhalte werden auf CEFR-B2-Niveau
verfasst: Deutsch zuerst, danach terminologisch konsistentes Englisch.
Fachbegriffe werden bei ihrem ersten relevanten Auftreten erklärt oder in einem
zweisprachigen Glossar verankert.

Für anwendbare Oberflächen und Dokumentationsmuster gilt WCAG 2.2 AA. Dazu
gehören semantische Struktur, Tastaturbedienbarkeit, sichtbare Fokusführung,
ausreichender Kontrast, Textalternativen und keine ausschließlich farbcodierte
Bedeutung.

*The documentation serves apprentices in German IHK IT occupations from their
first training year as well as experienced professionals. Content targets CEFR
B2: German first, followed by terminologically consistent English. Technical
terms are explained when first relevant or anchored in a bilingual glossary.*

*WCAG 2.2 AA applies to relevant interfaces and documentation patterns. This
includes semantic structure, keyboard operation, visible focus, sufficient
contrast, text alternatives, and no meaning conveyed by colour alone.*

## Aktueller Scope / Current scope

Phase 2 erstellt zunächst:

- eine eigenständige Programmquellen- und Constraint-Basis,
- ein vollständiges Review-Findings-Ledger,
- die Meta-Lastenhefte `META-LH-01` bis `META-LH-05`,
- ein de-dupliziertes fachliches Lastenheft-Portfolio,
- nachvollziehbare Reihenfolge-, Autonomie-, Review- und Evidence-Regeln.

Specify-, Plan-, Tasks- und Implementierungsläufe sowie Produktcode sind bis zu
den jeweiligen späteren Freigaben außerhalb dieses Scopes.

*Phase 2 first creates a self-contained source and constraint baseline, a full
review-findings ledger, meta requirements `META-LH-01` through `META-LH-05`, a
deduplicated domain requirements portfolio, and traceable sequencing,
autonomy, review, and evidence rules. Specify, plan, task, and implementation
runs, as well as product code, remain out of scope until separately approved.*

### Globale Review-Sperre / Global review gate

Für die kanonische AOC-Programmreihe gilt zusätzlich eine konservative,
fail-closed Review-Sperre: Bevor irgendein `speckit specify`-, Autonomous-,
Parallel-Autonomous- oder Implementierungslauf beginnen darf, müssen alle 14
aktiven Lastenhefte `META-LH-01` bis `META-LH-05` und `RAW-01` bis `RAW-09`
jeweils ein aktuelles, formal validiertes `Ready`-Single-Review besitzen.
Zielpfad, normalisierter Zielhash, Authoring Receipt sowie Bash- und
PowerShell-Validierung müssen aktuell sein; `ReadyWithAcceptedRisks`,
supersedierte Ergebnisse oder ein bloßer Series-Status genügen nicht.

Erst wenn diese Gesamtmenge vollständig `Ready` ist, darf nach einem neuen,
ausdrücklichen Startauftrag der erste Spec-Kit-Lauf für `META-LH-01` beginnen.
Jede spätere Drift eines Lastenhefts oder seiner Review-Evidence schließt die
Sperre erneut. Die älteren Root-Lastenhefte außerhalb der AOC-Programmreihe sind
nicht Teil dieser 14er-Gesamtmenge.

*The canonical AOC programme uses an additional fail-closed global review gate.
All 14 active META and RAW intakes require current, formally validated `Ready`
Single-review evidence before any Specify, autonomous, parallel-autonomous, or
implementation run may start. Accepted-risk or superseded results and lifecycle
status alone do not pass. Once all 14 are current, `META-LH-01` remains the
first target and still requires a new explicit start instruction. Any later
intake or review-evidence drift closes the gate again. Legacy root intakes are
outside this fourteen-intake programme gate.*

## Governance und Spec-kit / Governance and Spec Kit

Das Repository verwendet das Preset-Profil
`intake-sequencing-eleven-governance-presets`. Es umfasst elf versionierte
Security-, Architecture-, iSAQB-, Accessibility-, Cross-Platform-, Agent-
Parity-, Intake- und Autonomie-Presets. `.specify/presets/.cache/` ist lokaler
Cache und darf nicht veröffentlicht werden.

Die Lastenheftreihenfolge steht in
[`Lastenheft_Abarbeitungsreihenfolge.md`](Lastenheft_Abarbeitungsreihenfolge.md).
Die Verfassung in [`constitution.md`](constitution.md) und die Agent-Guidance
definieren die verbindlichen Qualitäts- und Sicherheitsgrenzen.

*This repository uses the `intake-sequencing-eleven-governance-presets`
profile, containing eleven versioned security, architecture, iSAQB,
accessibility, cross-platform, agent-parity, intake, and autonomy presets. The
`.specify/presets/.cache/` directory is a local cache and must not be
published. The requirements order and repository constitution define the
binding quality and security boundaries.*

Der kanonische Einstieg in das neue Anforderungsprogramm ist
[`Pflichtenheft.md`](Pflichtenheft.md). Dort sind die eigenständige Baseline,
`META-LH-01` bis `META-LH-05`, die neun fachlichen Owner-Reihen, ihre Status und
die erlaubte nächste Aktion verlinkt.

*The canonical entry into the new requirements programme is
[`Pflichtenheft.md`](Pflichtenheft.md), linking the self-contained baseline, five
meta intakes, nine domain owner series, their status, and the allowed next action.*

## AEPS-Evidence und Learnings / AEPS evidence and learnings

Das AOC ist ein Level-2-Referenzprojekt für das **Agentic Engineering Preset
System (AEPS)**. Findings, Learnings, Patterns, Anti-Patterns sowie positive und
negative Evidence werden unter [`docs/aeps/`](docs/aeps/) gesammelt und gegen
das strategische Level-0-Anchor-Issue
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196)
eingeordnet. Der [AEPS-Evidence-Vertrag](docs/aeps/README.md) definiert
Erfassungszeitpunkte, Pflichtfelder, Reifegrade, Deduplizierung und den späteren
Upstream-Handoff.

AOC entdeckt, testet und härtet projektbezogene Evidence. Preset-
Konsolidierung, Versionierung und Promotion bleiben Aufgabe des Level-0-
System-of-Record. Ein formales `Ready`-Review ist weder Series-Eligibility noch
Ausführungs- oder Promotion-Authority. / *The AOC is a level-2 AEPS reference.
It discovers, tests, and hardens project evidence under `docs/aeps/`; level 0
retains consolidation, versioning, and promotion. A formal Ready review is
neither Series eligibility nor execution or promotion authority.*

## Für Auszubildende / For Apprentices

Auszubildende benötigen keine Kenntnis der internen Entstehungsgeschichte oder
früherer Level-0-Issues. Jedes freigegebene Lastenheft muss seine Quellen,
Begriffe, Grenzen, Entscheidungen, Akzeptanzkriterien und erwartete Evidence
selbständig erklären. Berufsschule, betriebliche Ausbildung,
Ausbilderentscheidungen und Prüfungsvorbereitung bleiben eigenständige
Autoritäten.

*Apprentices do not need knowledge of the project's internal history or earlier
level-0 issues. Every approved requirement must independently explain its
sources, terms, boundaries, decisions, acceptance criteria, and expected
evidence. Vocational school, workplace training, instructor decisions, and
exam preparation remain separate authorities.*

## Prüfen und beitragen / Validate and contribute

Vor einem Beitrag sind die Regeln in [`CONTRIBUTING.md`](CONTRIBUTING.md) und
[`SECURITY.md`](SECURITY.md) zu lesen. Der lokale Homogenitätscheck lautet:

```bash
bash scripts/check-homogeneity.sh --json --fail-fast .
```

Die CI meldet Restore, Build und Test ausdrücklich als `NotApplicable`, solange
kein freigegebenes Produktprojekt existiert. Sobald ein Produkt-Scaffold
hinzukommt, muss derselbe Workflow Restore, Build und Test tatsächlich
ausführen; ein stilles Überspringen ist dann unzulässig.

*Read `CONTRIBUTING.md` and `SECURITY.md` before contributing. CI reports
restore, build, and test as `NotApplicable` while no approved product project
exists. Once a product scaffold is added, the same workflow must actually run
restore, build, and test; silent skipping is then forbidden.*

## Lizenz / License

Dieses Repository steht unter der [MIT-Lizenz](LICENSE).

*This repository is licensed under the [MIT License](LICENSE).*
