# Implementierungsplan: Nachweisbarer Intake-Authoring-Vertrag

**Branch**: `003-authoring-contract` | **Datum**: 2026-09-05 | **Spezifikation**: `specs/003-authoring-contract/spec.md`
**Eingabe**: Der aktuelle Intake `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md`, die akzeptierte Spezifikation, beide formalen Checklisten, `specs/003-authoring-contract/binding-approval.md` und `specs/003-authoring-contract/current-evidence-binding.json`.

**Branch**: `003-authoring-contract` | **Date**: 2026-09-05 | **Specification**: `specs/003-authoring-contract/spec.md`
**Input**: The current intake `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md`, the accepted specification, both formal checklists, `specs/003-authoring-contract/binding-approval.md`, and `specs/003-authoring-contract/current-evidence-binding.json`.

## Zusammenfassung / Summary

Der Plan stärkt genau fünf kanonische Fachartefakte des Intake-Authoring-Vertrags: Intake-Vorlage, Receipt-Vorlage, Projektprofil-Vorlage, AOC-Governance-Konfiguration und Feldvalidierungszusammenfassung. Er ergänzt nur die dafür zwingend erforderlichen Validator-, Negativ-Fixture-, Dokumentations-, Workflow- und Evidence-Anpassungen. Der Vertrag wird standardmäßig gesperrt, bindet Quellen, Grenzen, Entscheidungen, Risiken und Nachweise eindeutig und bleibt für andere Repositories portabel. Es gibt keine Produktimplementierung, keinen neuen Intake, keine Level-0-Änderung sowie keine Installation, Versionsänderung oder Promotion eines Presets.

The plan strengthens exactly five canonical domain artefacts of the Intake Authoring contract: the intake template, receipt template, project-profile template, AOC governance configuration, and field-validation summary. It adds only the validator, negative-fixture, documentation, workflow, and evidence changes strictly required for those artefacts. The contract is blocked by default, binds sources, boundaries, decisions, risks, and evidence unambiguously, and remains portable to other repositories. There is no product implementation, new intake, Level 0 change, or preset installation, version change, or promotion.

Die bereits separat genehmigte Binding-Reparatur ist eine unveränderliche Voraussetzung, nicht Teil der späteren Fachänderung: vier erneuerte Receipts, vier vollständige `Ready`-Single-Reviews, 23 fokussierte Tests sowie die unveränderliche Vorgänger- und Series-Brücke. Ihre Dateien und der abgeschlossene Checker werden nicht überschrieben. Nach der Fachänderung wird ausschließlich META-LH-03 mit einer byte-identischen Vorgängerkopie, einer neuen Operation, einem neuen Receipt und einem vollständigen neuen Single-Review erneuert. Die übrigen 13 Zielbindungen, die abgeschlossene Series und der META-LH-02-Lifecycle bleiben unverändert.

The separately approved binding repair is an immutable prerequisite, not part of the later domain change: four renewed receipts, four complete `Ready` Single reviews, 23 focused tests, and the immutable predecessor and Series bridge. Its files and completed checker will not be overwritten. After the domain change, only META-LH-03 will be renewed with a byte-identical predecessor copy, a new operation, a new receipt, and a complete new Single review. The other 13 target bindings, the completed Series, and the META-LH-02 lifecycle remain unchanged.

Der aktuelle Berichtsauftrag ergänzt die Lieferung um genau die 19 Pfade aus `specs/003-authoring-contract/reporting-contract-addendum.md`. Die fünf Agentenflächen und fünf Agenten-Templates erhalten einen byte-identischen gemeinsamen Guidance-Block; Constitution sowie Spec-, Plan- und Tasks-Templates binden denselben Lifecycle-Vertrag. Der Feature-Bericht enthält in dieser Reihenfolge `Output`, `Findings`, `confirmed rules`, `interventions/repairs`, `efficiency observations` und `AEPS relevance`, danach `Completion/Retrospective Evidence`. Erst nach abgeschlossenem META-LH-03 wird ein quellengebundener Trend `META-LH-01 -> META-LH-02 -> META-LH-03` ergänzt; fehlende vergleichbare Werte bleiben ausdrücklich `Nicht vergleichbar / Not comparable` und werden nicht erfunden. Dies erteilt keine Level-0-, Preset-Promotions- oder zusätzliche Delivery-Autorität.

The current reporting instruction adds exactly the 19 paths from `specs/003-authoring-contract/reporting-contract-addendum.md` to delivery. The five agent surfaces and five agent templates receive one byte-identical shared guidance block; the constitution and Spec, Plan, and Tasks templates bind the same lifecycle contract. The feature report contains, in order, `Output`, `Findings`, `confirmed rules`, `interventions/repairs`, `efficiency observations`, and `AEPS relevance`, followed by `Completion/Retrospective Evidence`. A source-bound `META-LH-01 -> META-LH-02 -> META-LH-03` trend is added only after META-LH-03 completes; missing comparable values remain explicitly `Nicht vergleichbar / Not comparable` and are never invented. This grants no Level 0, preset-promotion, or additional delivery authority.

Die exakte Reporting-Pfadmenge / The exact reporting path set is:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.github/copilot-instructions.md
.github/agents/copilot-instructions.md
constitution.md
.specify/memory/constitution.md
.specify/templates/agent-file-template.md
.specify/templates/plan-template.md
.specify/templates/spec-template.md
.specify/templates/tasks-template.md
scripts/templates/AGENTS.md.tmpl
scripts/templates/CLAUDE.md.tmpl
scripts/templates/GEMINI.md.tmpl
scripts/templates/copilot-instructions.tmpl
docs/governance/engineering-retrospective.md
specs/003-authoring-contract/reporting-contract-addendum.md
specs/003-authoring-contract/engineering-retrospective.md
specs/003-authoring-contract/autonomous-run-evidence.md
```

## Technischer Kontext / Technical Context

**Sprachen und Laufzeiten**: C#/.NET bleibt der primäre Level-2-Projektkontext, wird in diesem Feature aber nicht geändert. Markdown und JSON bilden die Verträge; Python 3 trägt fokussierte read-only Validatorlogik; Bash 5+ und PowerShell Core 7+ sind gleichwertige Oberflächen.

**Primäre Abhängigkeiten**: Git, `jq`, Python-Standardbibliothek, bestehende Intake-Authoring-Skripte, PSScriptAnalyzer 1.25.0, Gitleaks und die kanonischen Statistik-Renderer.

**Speicherung**: Nur repository-gebundene Text-, JSON- und Evidence-Dateien; keine Datenbank und kein Agentenlaufzeit-Speicher.

**Tests**: Vor Tasks ein exakt validierter lokaler 48-Pfade-Reparatur-Checkpoint; danach Tests-first-Vertikalschnitt, additiver Validator, feature-lokaler Gate-Evidence-Pre-Validator mit zwei positiven und vier getrennten negativen Fixtures, Global-Ready-Dispatcher samt Tests, drei vorhandene PowerShell-Fixture-Suiten, fail-closed 14-Receipt- und PSScriptAnalyzer-Negativfälle, beide installierten Operation-Artefaktvalidatoren sowie semantische Reviews.

**Zielplattformen**: `ubuntu-22.04`, `macos-14` und `windows-2022`; auf Windows ist die geprüfte Git-for-Windows-Bash maßgeblich, nicht WSL.

**Projekttyp**: Governance- und Vertragsänderung in einem bestehenden Repository; keine Laufzeit-Anwendung.

**Leistungsziel**: Deterministische, read-only Validierung der kleinen Vertragsmenge; keine throughput- oder latenzeabhängige Produktanforderung.

**Randbedingungen**: Exakte Liefermenge, fail-closed, keine Secrets, keine absoluten lokalen Pfade in öffentlichen Artefakten, kein Admin-Bypass, keine fremden Änderungen, keine Run-State-Änderung in dieser Planphase.

**Umfang**: Fünf kanonische Fachartefakte, ihre zwingenden Konsumenten und Nachweise sowie genau eine spätere META-LH-03-Erneuerung.

**Languages and runtimes**: C#/.NET remains the primary Level 2 project context but is not changed by this feature. Markdown and JSON form the contracts; Python 3 carries focused read-only validator logic; Bash 5+ and PowerShell Core 7+ are equivalent surfaces.

**Primary dependencies**: Git, `jq`, the Python standard library, existing Intake Authoring scripts, PSScriptAnalyzer 1.25.0, Gitleaks, and the canonical statistics renderers.

**Storage**: Repository-bound text, JSON, and evidence files only; no database or agent runtime store.

**Testing**: An exact local 48-path repair checkpoint before Tasks, then the test-first vertical slice, additive validator, feature-local Gate Evidence pre-validator with two positive and four separate negative fixtures, Global-Ready tests, existing suites, both installed operation artefact validators, negative harnesses, and semantic reviews.

**Target platforms**: `ubuntu-22.04`, `macos-14`, and `windows-2022`; on Windows, validated Git-for-Windows Bash is authoritative, not WSL.

**Project type**: Governance and contract change in an existing repository; no runtime application.

**Performance goal**: Deterministic read-only validation of the small contract set; no throughput or latency product requirement.

**Constraints**: Exact delivery set, fail-closed behaviour, no secrets, no absolute local paths in public artefacts, no admin bypass, no foreign changes, and no run-state change during this Plan phase.

**Scale**: Five canonical domain artefacts, their necessary consumers and evidence, and exactly one later META-LH-03 renewal.

## Forschungsentscheidung / Research Decision

Die Bestandsverträge, akzeptierten Artefakte, Validatoren, Fixtures, Workflows und Templates beantworten alle umsetzungsrelevanten Fragen. Deshalb besteht keine echte technische Unbekannte und es wird kein unabhängiger Forschungsauftrag ausgelöst. Die verbindlichen Entscheidungen und verworfenen Alternativen stehen in `specs/003-authoring-contract/research.md`.

The existing contracts, accepted artefacts, validators, fixtures, workflows, and templates answer every implementation-relevant question. Therefore no real technical unknown remains and no independent research assignment is dispatched. Binding decisions and rejected alternatives are recorded in `specs/003-authoring-contract/research.md`.

## Verfassungsprüfung / Constitution Check

### Prüfung vor Phase 0 / Pre-Phase 0 check

- **Level 2 und MSL**: Das AOC ist ein Level-2-Referenzprojekt, aber nicht als Laufzeitprojekt in der gemeinsamen Level-2-Registry geführt. Python 3, Bash 5+ und PowerShell Core 7+ sind für die vorhandenen Validatoroberflächen vorgegeben; Python und PowerShell sind Memory-Safe Languages (MSL, speichersichere Sprachen). Bash bleibt auf kurze, quotierte Adapter begrenzt.
- **Sichere Erzeugung und Architektur**: Eingaben bleiben Daten. Der Vertrag trennt vertrauenswürdige Repository-Dateien, öffentliche HTTPS-Quellen und nicht vertrauenswürdige Nutzlasten. Er nutzt Positivlisten, Pfadgrenzen, normalisierte Hashes, unveränderliche Vorgänger, geringste Rechte und gesperrte Standardzustände. Shell-Variablen werden quotiert; keine dynamische Codeausführung und keine Credentials sind vorgesehen.
- **Sicherheitsdokumentation und Standards**: NIST SSDF und CWE Top 25 sind anwendbar und werden in `specs/003-authoring-contract/security-review-evidence.md` bewertet. OWASP ASVS, Release-SBOM/VEX/SLSA, CAPEC, AI-SBOM, Zero Trust, C3A, C5, SAMM und regulatorische Produktnachweise sind für die reine Dokument-/Validatoränderung `N/A`; Trigger sind eine Laufzeit-, Release-, Cloud-, KI-Komponenten- oder regulierte Produktänderung. Ein Produkt-Bedrohungsmodell, S-ADR oder arc42-Abschnitt ist deshalb nicht erforderlich. Die fokussierte Vertrauensgrenzenbewertung steht in `specs/003-authoring-contract/architecture-review-evidence.md`.
- **Lieferkette und Secrets**: Keine Dependency wird ergänzt. Der vollständige Befehl `gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100` muss den exakten geprüften HEAD abdecken. Die Konfiguration darf die aktiven Authoring-Tests nicht ausschließen.
- **Presets**: Die installierte Governance-Matrix einschließlich der drei Intake-Presets bleibt unverändert. Es gibt keine Installation, keine Versionsänderung, keine Promotion und keine Level-0-Verteilung.
- **A11Y und Sprache**: Alle betroffenen nutzerseitigen Markdown- und JSON-Beispiele sind Deutsch zuerst, Englisch danach, text-first und auf WCAG 2.2 AA, semantische Überschriften, CEFR B2 sowie Erklärungen beim ersten Fachbegriff zu prüfen. Ergebnisse stehen in `specs/003-authoring-contract/accessibility-review-evidence.md`.
- **Plattformparität**: Identische fachliche Regeln werden auf Ubuntu, macOS und Windows mit Bash und PowerShell ausgeführt. Die Belege stehen in `specs/003-authoring-contract/cross-platform-parity-evidence.md`.
- **Statistik**: `docs/project-statistics.md` benötigt nach der fertigen Feature-Lieferung eine generierte Aktualisierung nach Methodik v2; als C#/.NET-Repository gilt der dokumentierte Thorsten-Solo-Wert von 125 Zeilen pro sichtbarem Git-Aktivtag, zusätzlich zur konservativen Basis 80. Der Writer darf erst auf einem sauberen echten Feature-HEAD laufen.
- **Agenten-Guidance**: Das akzeptierte Reporting-Addendum hebt die frühere Nichtänderungsgrenze ausschließlich für `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` und `.github/agents/copilot-instructions.md` auf. Genau ein markierter gemeinsamer Block muss in allen fünf Dateien byte-identisch sein; übrige Inhalte bleiben unberührt. ACG-026 ist deshalb anwendbar.
- **Dokumentationsauswirkung**: Es gilt genau die Entscheidung `UpdateRequired` aus `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`. Dieses Dokument bleibt alleiniger Owner der Entscheidung. Dieser Plan und alle weiteren Feature-Artefakte referenzieren sie nur. Kein Home-Sync ist erforderlich.

- **Level 2 and MSL**: AOC is a Level 2 reference project but is not registered as a runtime project in the shared Level 2 registry. Python 3, Bash 5+, and PowerShell Core 7+ are prescribed for the existing validator surfaces; Python and PowerShell are memory-safe languages (MSLs). Bash remains limited to small, quoted adapters.
- **Secure generation and architecture**: Inputs remain data. The contract separates trusted repository files, public HTTPS sources, and untrusted payloads. It uses allowlists, path boundaries, normalized hashes, immutable predecessors, least privilege, and blocked defaults. Shell variables are quoted; no dynamic code execution or credentials are planned.
- **Security documentation and standards**: NIST SSDF and CWE Top 25 apply and will be assessed in `specs/003-authoring-contract/security-review-evidence.md`. OWASP ASVS, release SBOM/VEX/SLSA, CAPEC, AI-SBOM, Zero Trust, C3A, C5, SAMM, and regulatory product evidence are `N/A` for this document/validator-only change; triggers are runtime, release, cloud, AI component, or regulated-product changes. A product threat model, S-ADR, or arc42 section is therefore not required. The focused trust-boundary assessment belongs in `specs/003-authoring-contract/architecture-review-evidence.md`.
- **Supply chain and secrets**: No dependency is added. The full command `gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100` must cover the exact reviewed HEAD. The configuration must not exclude active Authoring tests.
- **Presets**: The installed governance matrix, including the three Intake presets, remains unchanged. There is no installation, version change, promotion, or Level 0 distribution.
- **A11Y and language**: Every affected user-facing Markdown and JSON example is reviewed as German first and English second, text-first, and against WCAG 2.2 AA, semantic headings, CEFR B2, and first-use explanations. Results belong in `specs/003-authoring-contract/accessibility-review-evidence.md`.
- **Platform parity**: Identical domain rules run on Ubuntu, macOS, and Windows with Bash and PowerShell. Evidence belongs in `specs/003-authoring-contract/cross-platform-parity-evidence.md`.
- **Statistics**: `docs/project-statistics.md` needs a generated Methodology v2 update after feature delivery; as a C#/.NET repository, the documented Thorsten-solo value of 125 lines per visible Git activity day applies in addition to the conservative baseline of 80. The writer may run only on a clean, real feature HEAD.
- **Agent guidance**: The accepted reporting addendum supersedes the earlier no-change boundary only for `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, and `.github/agents/copilot-instructions.md`. Exactly one marked shared block must be byte-identical in all five files; all other content remains untouched. ACG-026 is therefore applicable.
- **Documentation impact**: Exactly the `UpdateRequired` decision in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact` applies. That document remains the sole owner of the decision. This plan and all later feature artefacts only reference it. No Home sync is required.

### Erneute Prüfung nach Phase 1 / Post-Phase 1 re-check

Das Datenmodell hält Identitäten, Hashes, Zustände, Rollen und Beweisgrenzen explizit. Das deklarative Design begrenzt die fünf Fachartefakte und listet jeden zwingenden Konsumenten. Die Gate-Anforderungen verlangen reale Befehls-, Plattform-, HEAD-, Review- und Approval-Belege; ein grüner Jobname allein genügt nicht. Es bleibt keine Verfassungsabweichung und kein Eintrag in der Komplexitätstabelle ist nötig.

The data model makes identities, hashes, states, roles, and proof boundaries explicit. The declarative design limits the five domain artefacts and lists every necessary consumer. Gate requirements demand real command, platform, HEAD, review, and approval evidence; a green job name alone is insufficient. No constitutional deviation remains, so no complexity entry is required.

## Projektstruktur / Project Structure

### Planungsartefakte dieses Features / Planning artefacts for this feature

```text
specs/003-authoring-contract/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── authoring-contract-design.json
│   ├── autonomous-run-gate-requirements.json   # nur PreMerge
│   └── postmerge-gate-requirements.json        # nur PostMerge
└── phase-results/
    ├── plan-v1/                                 # byte-identisch eingefroren
    ├── plan-remediation-report.md
    ├── plan-review-r2-report.md
    └── plan-remediation-r3-report.md
```

`tasks.md` wird in dieser Phase nicht erzeugt. Die bereits vorhandenen Dateien unter `specs/003-authoring-contract/contracts/`, insbesondere der abgeschlossene Binding-Reparatur-Checker, sind Voraussetzung und werden nicht verändert.

`tasks.md` is not created in this phase. Existing files under `specs/003-authoring-contract/contracts/`, especially the completed binding-repair checker, are prerequisites and remain unchanged.

### Spätere Lieferstruktur / Later delivery structure

```text
.specify/presets/intake-authoring-governance/
├── templates/                         # genau vier betroffene Preset-Artefakte
├── scripts/                           # erforderliche Validator-Konsumenten
├── tests/                             # drei bestehende Fixture-Suiten
└── docs/man/                          # geändertes Validatorverhalten

requirements/
├── intake-governance.json             # fünftes Fachartefakt
└── intakes/active/                     # nur spätere META-LH-03-Erneuerung

specs/003-authoring-contract/
├── contracts/                         # additiver aktueller Validator
├── repair-checkpoint-manifest.json     # erst im spaeteren Feature-Commit
├── *-review-evidence.md                # vier fokussierte Reviewberichte
├── tests-first-evidence.md             # vor erster Implementierungsänderung
├── current-evidence-binding.json       # nur spätere META-LH-03-Blattänderung
├── autonomous-run-gate-evidence.json
├── causal-closeout-evidence.json
└── engineering-retrospective.md

.github/workflows/powershell-analysis.yml # Global-Ready und neue Negativfälle
docs/man/validate-authoring-contract.1
docs/governance/engineering-retrospective.md
docs/project-statistics.md
```

**Strukturentscheidung**: Der Fachvertrag bleibt in den vorhandenen Preset- und `requirements/`-Pfaden. Neue Bindungslogik ist feature-lokal und additiv, damit der historische Reparatur-Checker und seine 23-Test-Evidence als Supplemental Historie unverändert bleiben. Der reale Global-Ready-Dispatcher und sein Test werden auf eine fail-closed Auswahl zwischen genau dem eingefrorenen Reparaturzustand und der neuen Primary-Kette erweitert. Die bestehende Drei-Plattform-Matrix wird erweitert, statt einen neuen Workflow oder neue Provider-Konfiguration einzuführen.

**Structure decision**: The domain contract remains in the existing preset and `requirements/` paths. New binding logic is feature-local and additive so the historical repair checker and its 23-test evidence remain unchanged as Supplemental history. The real Global-Ready dispatcher and its test gain a fail-closed selection between exactly the frozen repair state and the new Primary chain. The existing three-platform matrix is extended instead of creating a new workflow or provider configuration.

## Tatsächliche Fachänderung / Actual Domain Delta

1. `intake-template.md` erhält portable Pflichtfelder für stabile ID, deutsch- und englischsprachigen Titel, Zweck, Ist-/Zielzustand, Zielgruppe und Vorwissen, Traceability, Scope/Non-Goals, Grenzen, atomare FR/NFR, Dependencies, getrennte Decisions und Risiken, erwartete Artefakte, messbare Akzeptanz, positive und negative Nachweise, Owner, genau eine nächste sichere Aktion sowie die Aussage, welche Autorität nicht erteilt wird.
2. `intake-authoring-receipt-template.json` bindet als Schema `2.0` Quellenreihenfolge, normalisierte Quellen- und Zielhashes, stabile Intake- und neue Operation-ID, Profil, Decisions, Authority, Prompt-State, Lineage, optionale Series und genau eine nächste Aktion. Bei offenen Materialentscheidungen bleibt es mit `NeedsClarification`, stabilen Decision-IDs sowie `BLOCKED`/`DO NOT RUN` in beiden Promptblöcken fail-closed und enthält keine ausführbare Invocation. Bei `ReadyForReview` binden beide kopierbaren Prompts exakt dasselbe Lastenheft, ohne Ausführung oder aktuelle Authority abzuleiten.
3. `project-profile-template.md` erhält portable Regeln für Vertrauens- und Autoritätsgrenzen, Findings-Nachverfolgung, Autonomiemodus, positive und negative Evidenz, Revision und Nicht-Autorität. AOC-spezifische Werte werden nicht in das Preset eingebaut.
4. `requirements/intake-governance.json` bindet das aufgelöste AOC-Profil `requirements/baseline/intake-authoring-profile.md` mit Profilidentität und Sprachvertrag. Der vorhandene Konfigurationsvalidator und seine Fixture-Suite prüfen diese Bindung bei unverändertem Schema `2.0`.
5. `field-validation-summary.md` dokumentiert erst nach erfolgreichen realen Prüfungen die tatsächlich erzielten Felder, Negativfälle, Plattformen und Grenzen. Geplante Erfolge werden nicht vorab eingetragen.

1. `intake-template.md` gains portable required fields for stable ID, German and English titles, purpose, current/target state, audience and prior knowledge, traceability, scope/non-goals, boundaries, atomic FR/NFR, dependencies, separate decisions and risks, expected artefacts, measurable acceptance, positive and negative evidence, owner, exactly one next safe action, and a statement of authority not granted.
2. `intake-authoring-receipt-template.json`, as schema `2.0`, binds source order, normalized source and target hashes, stable intake and new operation IDs, profile, decisions, authority, prompt state, lineage, optional Series, and exactly one next action. With open material decisions it remains fail-closed with `NeedsClarification`, stable decision IDs, and `BLOCKED`/`DO NOT RUN` in both prompt blocks and contains no executable invocation. At `ReadyForReview`, both copyable prompts bind the exact same intake without execution or current-authority inference.
3. `project-profile-template.md` gains portable rules for trust and authority boundaries, finding traceability, autonomy mode, positive and negative evidence, revision, and non-authority. AOC-specific values are not embedded in the preset.
4. `requirements/intake-governance.json` binds the resolved AOC profile `requirements/baseline/intake-authoring-profile.md` with profile identity and language contract. The existing configuration validator and its fixture suite verify this binding while schema `2.0` remains unchanged.
5. `field-validation-summary.md` records actually achieved fields, negative cases, platforms, and boundaries only after real checks pass. Planned successes are not written in advance.

## Umsetzungsreihenfolge / Implementation Sequence

### 1. Historischen Checkpoint binden / Bind the historical checkpoint

Vor der Tasks-Phase entsteht genau ein lokaler Reparatur-Checkpoint aus den 48 literal und ohne Glob aufgeführten Pfaden in `authoring-contract-design.json.preTasksRepairCheckpoint.candidatePaths`. Die Menge wurde aus aktuellem Git-Status, den vier R1-Review-Tripeln, `binding-repair-validation.json`, Operation `959e832f-be87-4f77-a0a9-478220708a6d` und ihren vier Staging-Dateien abgeleitet. Sie enthält die geänderte META-LH-03-Zieldatei, vier aktuelle Receipts, acht von ihnen benannte Archive, zwölf Reviewdateien, AEPS-Ledger und ausschließlich die Receipts `binding-renewal` und `binding-bridge`, beide Global-Ready-Dateien, Checker-Manpage, Approval, Scope-Entscheidung, Reparaturvalidierung, aktuelle Bindung, vier Checker-Oberflächen und vier Specify-Erhaltungsdateien. Plan-, Reporting- und Fachdateien sowie `2026-09-05-meta-lh03-contract-boundary.md` sind ausgeschlossen.

Vor dem lokalen Commit müssen alle 48 Pfade existieren, der unveränderte installierte Delivery-Validator jeden Pfad über ein eigenes literales `--intended` read-only prüfen, `git add --` genau diese 48 literalen Argumente ohne Shell-Expansion erhalten, das staged Inventar exakt übereinstimmen und `git diff --cached --check` bestehen. Fremde Änderungen bleiben unstaged. Der Commit ist weder Push noch späterer Feature-Commit. Erst im späteren Feature-Commit entsteht `specs/003-authoring-contract/repair-checkpoint-manifest.json`; es bindet Reparatur-Commit, Tree und Rohhash jedes der 48 Pfade, behauptet aber ausdrücklich nicht, selbst im Reparatur-Commit enthalten zu sein.

Die abgeschlossene Vier-Receipt-Reparatur bleibt damit am unveränderlichen Reparatur-Checkpoint historisch beweiskräftig. `binding-repair-validation.json`, der damalige `current-evidence-binding.json`-Hash, Checkpoint-Commit, Tree-OID und die dort gebundenen Checker-Hashes werden als **Supplemental** Evidence bewahrt; die 23 Tests oder der eingefrorene Checker werden am später veränderten META-LH-03-Blatt nicht erneut als aktueller Beweis missbraucht. Der finale Primary-Vertrag verlangt `git merge-base --is-ancestor <repair-checkpoint> <final-feature-head>` und prüft jeden Manifestpfad und Rohhash gegen den Reparatur-Tree. Fehlender Commit, falscher Tree, Hashdrift, Selbstreferenz oder fehlende Ancestry sperren.

Before Tasks, exactly one local repair checkpoint is created from the 48 literal, no-glob paths in `authoring-contract-design.json.preTasksRepairCheckpoint.candidatePaths`. The set is derived from current Git status, the four R1 review triples, `binding-repair-validation.json`, operation `959e832f-be87-4f77-a0a9-478220708a6d`, and its four staged files. It includes every required repair path and excludes Plan, reporting, domain files, and the unapproved `contract-boundary` AEPS receipt.

All 48 paths must exist before the unchanged installed delivery validator checks each as a separate literal `--intended` argument. `git add --` receives exactly those literal arguments without shell expansion; the staged inventory must match exactly and `git diff --cached --check` must pass, while foreign changes remain unstaged. This local commit is neither a push nor the later feature commit. The later feature commit creates `specs/003-authoring-contract/repair-checkpoint-manifest.json`, binding the repair commit, tree, and raw hash of each path without claiming that the manifest existed in the repair commit.

The completed four-receipt repair then remains historically valid at its immutable checkpoint. Its validation, binding hash, commit, tree, checker hashes, and 23-test record stay **Supplemental**. The final Primary contract requires checkpoint ancestry and validates every manifest path and raw hash against the repair tree. Missing commit, wrong tree, hash drift, self-reference, or failed ancestry blocks.

### 2. Tests-first-Vertikalschnitt / Test-first vertical slice

Die Reihenfolge ist verbindlich und besitzt genau eine Wurzel: `baseline -> vertical-red -> vertical-green -> domain-expansion -> renewal -> global-ready -> reviews -> checkpoint -> statistics -> premerge -> feature-merge -> lifecycle -> closeout -> postmerge`. Zuerst läuft die vollständige bestehende Ausführungsoberfläche aus Quickstart Abschnitt 1 am unveränderten Checkpoint. Danach wird `specs/003-authoring-contract/tests-first-evidence.md` **vor** jeder Implementierungsänderung angelegt. Als erste Änderung entsteht in `specs/003-authoring-contract/contracts/test_validate_authoring_contract.py` genau eine kleinste positive Fixture für die gültige r1-zu-r2-Bridge und eine negative Fixture für ein zweites geändertes Blatt. Ihr erwarteter Rotlauf muss ausschließlich dem noch fehlenden lokalen additiven Validator gehören; unerwartete Baseline-, Tool- oder Fremdfehler sind Blocker und dürfen nicht als erwartetes Rot etikettiert werden.

Danach wird nur die kleinste Domain-/Validator-Scheibe implementiert, bis beide Fixtures grün sind. Als nächste Tests-first-Scheibe entstehen `contracts/test_validate_gate_evidence_invariants.py` und die sechs exakt benannten Gate-Evidence-Fixtures: zwei positive Fälle sowie getrennte negative Fälle für fehlende und falsche Primary-Referenz, falschen PreMerge-Pfad und falschen normalisierten Hash. Erst danach wird `contracts/validate_gate_evidence_invariants.py` implementiert. Anschließend werden der vollständige Update-Vertrag, die fünf Fachartefakte in stabiler Reihenfolge `1..5`, Receipt-/Konfigurationskonsumenten, Global-Ready-Dispatcher, negative Harness-Fälle, Plattformworkflow, Guidance und Reporting verbreitert.

The ordering is binding and has exactly one root: `baseline -> vertical-red -> vertical-green -> domain-expansion -> renewal -> global-ready -> reviews -> checkpoint -> statistics -> premerge -> feature-merge -> lifecycle -> closeout -> postmerge`. First, the complete existing execution surface from Quickstart section 1 runs at the unchanged checkpoint. Next, `specs/003-authoring-contract/tests-first-evidence.md` is created **before** any implementation edit. The first change adds exactly one smallest positive valid r1-to-r2 bridge fixture and one negative second-changed-leaf fixture to `specs/003-authoring-contract/contracts/test_validate_authoring_contract.py`. Their expected red result must be owned solely by the not-yet-present local additive validator; unexpected baseline, tool, or foreign failures block and cannot be labelled expected red.

Only the smallest domain/validator slice is then implemented until both fixtures are green. The next tests-first slice creates `contracts/test_validate_gate_evidence_invariants.py` and the six exact Gate Evidence fixtures: two positive cases plus separate negative cases for missing and wrong Primary references, wrong PreMerge path, and wrong normalized hash. Only then is `contracts/validate_gate_evidence_invariants.py` implemented. The complete Update contract and remaining consumers broaden afterwards.

### 3. Fünf Fachartefakte und zwingende Konsumenten / Five domain artefacts and necessary consumers

Die fünf Fachartefakte werden nach dem grünen Vertikalschnitt in ihrer festgelegten Reihenfolge geändert. Zwingende Konsumenten sind zusätzlich der installierte Operation-Template-Pfad und beide unveränderten Artefaktvalidatoren, der feature-lokale Gate-Evidence-Pre-Validator samt exakt benanntem Test und sechs Fixtures, die Receipt-Validatoren mit Manpage, alle drei Governance-Konfigurationsoberflächen mit Manpage, drei vorhandene Fixture-Suiten, der additive Contract-Validator mit Bash-/PowerShell-Adapter und Tests, beide Global-Ready-Dateien, vier fokussierte Reviewberichte und `.github/workflows/powershell-analysis.yml`. Die Reporting-Ergänzung umfasst exakt die 19 im Design benannten Reporting-/Policy-Pfade.

After the green vertical slice, mandatory consumers additionally include the installed operation template and both unchanged artefact validators, the feature-local Gate Evidence pre-validator with its exact test and six fixtures, receipt/configuration surfaces, three existing suites, the additive contract validator and adapters, both Global-Ready files, four reviews, and the existing workflow. Reporting still covers exactly the 19 accepted reporting/policy paths.

### 4. Lokale und Matrix-Prüfung / Local and matrix validation

Die exakten Befehle stehen in `specs/003-authoring-contract/quickstart.md`; die maschinenlesbaren Gates stehen in `specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json`. Die drei kanonischen Fixture-Suiten, META-LH-03 und ein aus `current-evidence-binding.json` abgeleitetes, auf exakt 14 eindeutige Ziel-IDs geprüftes Receipt-Inventar laufen sowohl über Bash als auch PowerShell. Auf `ubuntu-22.04`, `macos-14` und `windows-2022` müssen die Logs Befehl, unmittelbaren Exitcode, Runner und geprüften HEAD zeigen. Auf Windows wird der validierte Pfad zu Git-for-Windows-Bash an Kindprozesse weitergegeben. Ein bloß grüner Workflow- oder Jobname ist nur ergänzender Nachweis.

Exact commands are in `specs/003-authoring-contract/quickstart.md`; machine-readable gates are in `specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json`. The three canonical fixture suites, META-LH-03, and a receipt inventory derived from `current-evidence-binding.json` and checked for exactly 14 unique target IDs run through both Bash and PowerShell. On `ubuntu-22.04`, `macos-14`, and `windows-2022`, logs must show the command, immediate exit code, runner, and verified HEAD. On Windows, the validated Git-for-Windows Bash path is propagated to child processes. A merely green workflow or job name is supplemental evidence only.

### 5. Nur META-LH-03 über vollständiges Update neu binden / Rebind only META-LH-03 through complete Update

Nach dem letzten Fachartefakt-Byte wird genau eine installierte Operation vom Typ `Update` ausgeführt. Sie basiert auf dem unveränderten installierten Template `.specify/presets/intake-authoring-governance/templates/intake-authoring-operation-template.json`. Die Proposal-Datei liegt exakt unter `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/proposal.json`; ihr strikter UTF-8-Normalhash steht in `proposalNormalizedSha256`, und die aktuelle ausdrückliche Approval wird mit Person, UTC-Zeit und Evidence gebunden. Vor jeder Mutation werden Ziel, Receipt, geordnete Quellen, R1-Review-Link, Git-Zustand, Tombstone- und Inflight-Zustand geprüft.

Die aktive R1-Zieldatei und das aktive R1-Receipt werden byte-identisch nach `specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/Lastenheft_META-LH-03-Authoring-Contract.md` und `specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/META-LH-03-Authoring-Contract.json` kopiert. `supersedes` bindet beide Original- und Archivpfade sowie Rohhashes; für das Ziel zusätzlich den Normalhash. Ziel- und Receipt-Kandidat entstehen isoliert unter `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/staging/Lastenheft_META-LH-03-Authoring-Contract.md` und `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/staging/META-LH-03-Authoring-Contract.json`. `intendedTargets`, `validatedTargets` und `publishedTargets` sind identisch mit der vierpfadigen Publikationsmenge aus beiden Archiven, aktivem Ziel und aktivem Receipt.

Die einzige Statusmenge lautet `Proposed`, `Approved`, `Applying`, `Completed` und `Failed`. Nur `Completed` ist Erfolg; `Failed` ist der einzige terminale Fehler. Reparatur- und Rollbackdetails stehen ausschließlich in `failure.class`, `failure.message`, `nextAction` und `rollbackBoundary`. Beide installierten Artefaktvalidatoren müssen das Operation-Journal unter `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/operation.json` vor `Completed` erfolgreich prüfen. Reservierte Identitäten sind Operation `986c1d6c-d485-460b-8d8d-7cf5816a2c36`, Receipt `f41328cd-b301-4533-89dc-02aab758ab1f` und Review `b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf`.

Der R1-Request, das R1-Ergebnis und der R1-Bericht werden mit ihren drei Rohhashes ausdrücklich durch die R2-Pfade `specs/intake-review-requests/meta-lh-03-authoring-contract-2026-09-05-r2.json`, `specs/intake-review-results/meta-lh-03-authoring-contract-2026-09-05-r2.json` und `docs/reviews/meta-lh-03-authoring-contract-intake-review-2026-09-05-r2.md` supersediert. Nur ein vollständig neu validiertes `Ready`-R2-Ergebnis darf anschließend gebunden werden.

After the final domain byte, exactly one installed `Update` operation uses the unchanged installed operation template. Its exact proposal path and normalized hash, current approval, operation journal, isolated staged target and receipt, both predecessor archives, complete `supersedes`, and equal four-path intended/validated/published sets are mandatory. The only operation statuses are `Proposed`, `Approved`, `Applying`, `Completed`, and `Failed`; only `Completed` succeeds, while repair details for `Failed` belong in `failure`, `nextAction`, and `rollbackBoundary`. Both installed artefact validators must pass before completion. The exact reserved operation, receipt, and review IDs and every literal path are fixed in the design contract.

The three hash-bound R1 review artefacts are explicitly superseded by the exact R2 request, result, and report paths. Only a newly validated `Ready` R2 result may enter the current binding.

Der neue feature-lokale Validator ist der **Primary**-Beweis am finalen Feature-HEAD: Er prüft die Ancestry, den Reparatur-Commit und -Tree sowie jeden Pfad und Rohhash aus `repair-checkpoint-manifest.json` gegen diesen Tree, ohne das Manifest selbst im Reparatur-Commit zu erwarten. Er prüft außerdem die unmittelbare R1-zu-R2-Supersession, den vollständigen `Completed`-Operationszustand, genau ein neues META-LH-03-Blatt, 13 unveränderte Blätter und die unveränderte Series-Brücke. Der alte Checker und seine 23 Tests bleiben ausschließlich **Supplemental** am historischen Checkpoint.

The new feature-local validator is **Primary** proof at final feature head. It validates ancestry plus every manifest path and raw hash against the repair tree, without expecting the later manifest in that earlier commit. It also proves direct R1-to-R2 supersession, the complete `Completed` operation, one changed META-LH-03 leaf, 13 unchanged leaves, and the unchanged Series bridge. Historical checker evidence remains **Supplemental** only.

### 6. Reviews, Liefermenge und Statistik / Reviews, delivery set, and statistics

Die vier Reviewberichte prüfen Sicherheit/Quellenautorität, Architektur/Vertrauensgrenzen, Barrierefreiheit/Sprache und Plattformparität. Sie verweisen auf die einzige Dokumentationsauswirkungsentscheidung und enthalten tatsächliche Befehle, Ergebnisse, Reviewer und HEAD statt Prognosen. Danach wird die exakte Feature-Liefermenge aus dem deklarativen Design aufgelöst, jeder Pfad gegen `git status` und `git diff` abgeglichen, ausschließlich diese Menge gestaged und mit `git diff --cached --check` read-only geprüft. Fremde oder nicht freigegebene Dateien bleiben unberührt. Erst danach entsteht ein normaler Implementierungs-Checkpoint-Commit ohne Statistik-Ledger.

The four review reports assess security/source authority, architecture/trust boundaries, accessibility/language, and platform parity. They reference the sole Documentation Impact decision and contain actual commands, results, reviewer, and HEAD instead of forecasts. The exact feature delivery set is then resolved from the declarative design, every path reconciled with `git status` and `git diff`, only that set staged, and the staged candidate checked read-only with `git diff --cached --check`. Foreign or unauthorized files remain untouched. Only then is a normal implementation checkpoint commit created without the statistics ledger.

Auf dem danach sauberen echten Feature-Branch läuft `bash scripts/render-project-statistics.sh --repo .`. Anschließend müssen Bash- und PowerShell-`--check-only`/`-CheckOnly` jeweils JSON-Erfolg melden. Nur `docs/project-statistics.md` wird separat committet. Weil Ledger und Ledger-Commit in Methodik v2 ausgeschlossen sind, wird kein weiterer Writer-Zyklus erzeugt. Die beiden Check-only-Läufe werden am sauberen endgültigen Feature-HEAD wiederholt. Meldet der Writer unerwartet keine Änderung, wird kein leerer Commit erzeugt; die Ursache wird dokumentiert.

On the then-clean real feature branch, `bash scripts/render-project-statistics.sh --repo .` runs. Bash and PowerShell `--check-only`/`-CheckOnly` must then each report JSON success. Only `docs/project-statistics.md` is committed separately. Because the ledger and ledger commit are excluded by Methodology v2, no further writer cycle is created. Both check-only commands run again on the clean final feature HEAD. If the writer unexpectedly reports no change, no empty commit is created; the cause is recorded.

### 7. PreMerge, Merge, Lifecycle und kausaler Abschluss / PreMerge, merge, lifecycle, and causal closeout

Vor jedem unveränderten Evidence-Core-Lauf wird zuerst `specs/003-authoring-contract/contracts/validate_gate_evidence_invariants.py` ausgeführt. Dieser feature-lokale Pre-Validator erzwingt, dass jedes Supplemental-Element auf das eindeutige Primary-Element desselben Gates verweist. Für PostMerge erzwingt er außerdem die exakte Gleichheit von `acceptedPreMergePath` mit dem in den Requirements konfigurierten Runner-Pfad sowie den dazu passenden normalisierten Hash. Der installierte Evidence Core wird unverändert danach ausgeführt; der Plan behauptet ausdrücklich nicht, dass der Core diese zwei feature-lokalen Invarianten selbst erzwingt.

Die Evidence-Core-Regel verlangt zusätzlich, dass jede `Applicable`-Anforderung des jeweiligen Snapshots bereits `Pass` ist. Deshalb enthält `contracts/autonomous-run-gate-requirements.json` ausschließlich vor dem Merge wissbare Fakten. Der erhaltene Runner-Nachweis `.specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json` ist ein Schema-2.0-`PreMerge`-Snapshot. Er bindet seinen normalisierten Requirements-Hash, den exakten geprüften Feature-HEAD, reale Befehle und unmittelbare Exitcodes, die vier Reviews, aktuelle Required Checks, geschlossene actionable Threads, tatsächlich verfügbare erforderliche Approval und normale Merge-Bereitschaft. `acceptedPreMergePath`, `acceptedPreMergeSha256` und `mergeCommit` bleiben leer. Weder ein ausgeführtes `gh pr merge` noch ein tatsächlicher Merge-Commit ist PreMerge-Anforderung.

Die Reihenfolge ist kausal fest: Zuerst werden alle Repository-Schreibvorgänge einschließlich Statistik abgeschlossen und der unveränderliche Feature-HEAD gepusht; danach werden PR, Checks, Threads, Review und erforderliche Approval für genau diesen HEAD konvergiert; erst dann wird der finale Runner-`PreMerge`-Snapshot erzeugt und zuerst feature-lokal, anschließend durch den unveränderten Evidence Core validiert. Zwischen dem Einfrieren des Feature-HEAD und dem Merge gibt es keinen Repository-Writer.

Before every unchanged Evidence Core invocation, the feature-local `validate_gate_evidence_invariants.py` runs first. It enforces Supplemental-to-unique-Primary references and, for PostMerge, exact equality of the accepted PreMerge path to the configured runner path plus its matching normalized hash. The unchanged installed Evidence Core runs only afterwards and is not credited with enforcing these two invariants. Its separate rule still requires every `Applicable` item to be `Pass`, so PreMerge contains only facts knowable before merge.

The order is causal: finish every repository write including statistics and push the immutable feature head first; converge the PR, checks, threads, review, and required approval for exactly that head second; create and validate the final runner `PreMerge` snapshot third, with the feature-local validator before the unchanged Evidence Core. No repository writer runs between freezing the feature head and merging it.

Der Feature-PR wird danach ohne Admin-Bypass nach normaler Policy gemergt. Erst `contracts/postmerge-gate-requirements.json` verlangt den ausgeführten normalen Merge, tatsächliche PR- und Merge-Commit-Fakten, Lifecycle, kausalen Closeout, finalen Bericht, Retrospektive, META-LH-01-bis-03-Trend und Synchronisierung. Der exakte Runner-Pfad `.specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/postmerge-gate-evidence.json` ist ein separater Schema-2.0-`PostMerge`-Snapshot und entsteht erst nach dem tatsächlichen Closeout-Merge und finalen Sync, damit kein Repository-Artefakt seinen eigenen späteren Merge vorwegnimmt. Er bindet den akzeptierten PreMerge-Snapshot durch `acceptedPreMergePath` und `acceptedPreMergeSha256`; `reviewedHead` bleibt der akzeptierte Feature-HEAD, `mergeCommit` ist der tatsächliche Feature-Merge-Commit und `changedPaths` ist leer.

The feature PR is then merged under normal policy without admin bypass. Only `contracts/postmerge-gate-requirements.json` requires the executed normal merge, actual PR and merge-commit facts, lifecycle, causal closeout, final report, retrospective, META-LH-01-through-03 trend, and synchronization. The exact runtime PostMerge evidence path is a separate schema-2.0 runner snapshot created only after the actual closeout merge and final sync, so no repository artefact preclaims its own later merge. It binds accepted PreMerge evidence through `acceptedPreMergePath` and `acceptedPreMergeSha256`; `reviewedHead` stays the accepted feature head, `mergeCommit` is the actual feature merge commit, and `changedPaths` is empty.

Die verfassungsgemäße Lastenheft-Umbenennung folgt erst nach dem Feature-Merge über die vorhandenen gepaarten Skripte in einem eigenen normal geprüften PR. `specs/003-authoring-contract/intake-lifecycle.json` ordnet dabei den unveränderten logischen META-LH-03-Pfad dem physischen umbenannten Pfad zu. Der abgeschlossene Series-Manifestpfad und der META-LH-02-Lifecycle werden nicht geändert. Danach wird erneut fast-forward synchronisiert und `0/0` belegt.

The constitution-required Lastenheft rename follows only after the feature merge through the existing paired scripts in its own normally reviewed PR. `specs/003-authoring-contract/intake-lifecycle.json` maps the unchanged logical META-LH-03 path to the physical renamed path. The completed Series manifest path and META-LH-02 lifecycle are not changed. Fast-forward synchronization and `0/0` proof follow again.

Erst nach realem Feature- und Lifecycle-Merge samt Sync dürfen `specs/003-authoring-contract/causal-closeout-evidence.json` und der finale Feature-Bericht diese bekannten Fakten festhalten. Genau ein Evidence-only-Closeout auf dem vorbenannten Branch `003-authoring-contract-closeout` ist für die im deklarativen Design exakt aufgelisteten fünf PostMerge-Pfade zulässig. Der Closeout-Kandidat enthält die terminale Tasks-/Run-State-Transition als transaktionalen Zielzustand: Sie wird erst durch den normalen Merge des geprüften Kandidaten auf `main` kanonisch und behauptet weder ihren eigenen Merge-Commit noch einen bereits erfolgten finalen Sync. Auch dieser PR benötigt normale Checks, Review und verfügbare Approval.

Nach dem tatsächlichen Closeout-Merge synchronisiert der äußere Orchestrator `main` per Fast-forward und erzeugt den Runner-`PostMerge`-Snapshot außerhalb des Repository-Kandidaten. Dieser Snapshot bindet den realen Closeout-Merge und den sauberen `0/0`-Stand und wird zuerst feature-lokal, danach durch den unveränderten Evidence Core validiert. Erst das erfolgreiche Runner-Ergebnis beendet die geroutete Implement-Phase. Die anschließend genau einmal vom Runner geschriebene Phasenresultat-Bindung darf der äußere Orchestrator in einem letzten, auf `tasks.md` und `autonomous-run-state.json` begrenzten normalen Persistence-PR liefern; dieser Zustand bindet nicht den eigenen Persistence-Merge. Danach folgen ausschließlich externer Fast-forward-/Clean-/`0/0`-Nachweis und Prozessende. Damit gibt es keinen weiteren Repository-Writer und keinen selbstreferenziellen Abschlusszyklus.

Only after the real feature and lifecycle merges and synchronization may `specs/003-authoring-contract/causal-closeout-evidence.json` and the final feature report record those known facts. Exactly one evidence-only closeout on the pre-named branch `003-authoring-contract-closeout` is allowed for the five exact PostMerge paths listed by the declarative design. Its terminal tasks/run-state transition is a transactional target state that becomes canonical only when the reviewed candidate is normally merged to `main`; it does not claim its own merge commit or a final synchronization that has not happened.

After the actual closeout merge, the outer orchestrator fast-forwards `main` and creates the runner `PostMerge` snapshot outside the repository candidate. That snapshot binds the real closeout merge and clean `0/0` state and passes the feature-local validator before the unchanged Evidence Core. Only that successful runner result ends the routed Implement phase. The outer orchestrator may then deliver the runner's one-time phase-result binding through one final normal persistence PR limited to `tasks.md` and `autonomous-run-state.json`; that state does not bind its own persistence merge. Only an external fast-forward/clean/`0/0` proof and process exit follow, so no further repository writer or self-referential closeout cycle exists.

Die Statistik bildet den sauberen finalen Feature-HEAD vor den nachgelagerten Lifecycle- und Evidence-only-Textcommits ab. Diese späteren, ebenfalls textwirksamen Commits werden beim nächsten regulären Methodik-v2-Trigger berücksichtigt; sie lösen in diesem Lauf keine spekulative Rückprojektion und keinen Endloszyklus aus.

The statistics snapshot represents the clean final feature HEAD before later lifecycle and evidence-only text commits. Those later text-affecting commits are included at the next regular Methodology v2 trigger; they do not cause speculative back-projection or an endless cycle in this run.

## Liefermengenvertrag / Delivery-Set Contract

Die konkrete Positivliste wird aus `specs/003-authoring-contract/contracts/authoring-contract-design.json` aufgelöst. Zulässig sind ausschließlich:

- die Core-Feature-Artefakte `spec.md`, `plan.md`, `tasks.md`, Run-State und beide Checklisten sowie die im Design einzeln aufgeführten dauerhaften Phasenergebnisse und Payloads dieses Laufs;
- die fünf benannten Fachartefakte;
- direkt benannte Validatoren, Adapter, Manpages und die drei Fixture-Suiten;
- der additive Feature-Validator, seine Tests, der reale Global-Ready-Dispatcher und dessen Test;
- `specs/003-authoring-contract/tests-first-evidence.md` und die fail-closed Negativ-Harness-Fälle;
- die vier benannten Review-Evidence-Dateien, Gate-Evidence und Lifecycle-/Closeout-Evidence;
- `current-evidence-binding.json` sowie ausschließlich die neue META-LH-03-Update-Operation, beide Archive, Staging-Receipt, aktives Receipt, Review-Request, Review-Result und Reviewbericht;
- der eine vorhandene Workflow `.github/workflows/powershell-analysis.yml`;
- exakt die 19 Reporting-/Policy-Pfade aus dem akzeptierten Addendum, darunter der byte-identische Block auf fünf Agentenflächen und fünf Agenten-Templates, Constitution-/Projektvorlagen und der finalisierbare Feature-Bericht;
- `docs/project-statistics.md` ausschließlich im separaten Ledger-Commit.

The concrete allowlist is resolved from `specs/003-authoring-contract/contracts/authoring-contract-design.json`. Only the following are allowed:

- the core feature artefacts `spec.md`, `plan.md`, `tasks.md`, run state, both checklists, and the durable phase results and payloads of this run listed individually in the design;
- the five named domain artefacts;
- directly named validators, adapters, man pages, and the three fixture suites;
- the additive feature validator and its tests, the real Global-Ready dispatcher, and its test;
- `specs/003-authoring-contract/tests-first-evidence.md` and fail-closed negative harness cases;
- the four named review-evidence files, gate evidence, and lifecycle/closeout evidence;
- `current-evidence-binding.json` and only the new META-LH-03 Update operation, both archives, staging receipt, active receipt, review request, review result, and review report;
- the one existing workflow `.github/workflows/powershell-analysis.yml`;
- exactly the 19 reporting/policy paths from the accepted addendum, including the byte-identical block across five agent surfaces and five agent templates, constitution/project templates, and the finalizable feature report;
- `docs/project-statistics.md` only in the separate ledger commit.

Vor jedem Commit erzeugt ein read-only Vergleich die Mengen `planned`, `changed`, `staged` und `foreign`. `changed - planned` und `staged - intended` müssen leer sein; fehlende geplante Dateien benötigen eine begründete `N/A`-Entscheidung. Pfade werden einzeln und repository-relativ gestaged. Es gibt kein `git add -A`, keinen Reset, keinen Stash, kein Force, kein Amend, keine Löschung fremder Daten und keinen absoluten Pfad in einem veröffentlichten Nachweis.

Before every commit, a read-only comparison produces the sets `planned`, `changed`, `staged`, and `foreign`. `changed - planned` and `staged - intended` must be empty; missing planned files require a justified `N/A` decision. Paths are staged individually and repository-relatively. There is no `git add -A`, reset, stash, force, amend, deletion of foreign data, or absolute path in published evidence.

## Gate- und Approval-Vertrag / Gate and Approval Contract

`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json` ist ausschließlich die verbindliche PreMerge-Liste; `specs/003-authoring-contract/contracts/postmerge-gate-requirements.json` ist ausschließlich die PostMerge-Liste. Keine `Applicable`-Anforderung steht im zeitlich falschen Snapshot. Je Gate gibt es genau einen Primärnachweis; Supplemental-Nachweise verweisen darauf. Befehls- und Runner-Tokens müssen in realen Logs vorkommen. PreMerge verlangt den aktuellen geprüften HEAD, grüne technische Gates, geschlossene actionable Threads, verfügbare erforderliche Approval und normale Merge-Bereitschaft, aber keinen bereits ausgeführten Merge. PostMerge bindet PreMerge durch `acceptedPreMergePath` und `acceptedPreMergeSha256` und verlangt die realen Merge-, Lifecycle-, Reporting-, Retrospective-, Trend- und Sync-Fakten. Delivery Authority `MergeAndSync` erlaubt normale lokale Commits, Push, PR, Merge und Sync im genehmigten Scope, aber keinen Admin-Bypass, keine Ausweitung und keine Level-0-/Provider-Änderung.

`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json` is exclusively the binding PreMerge list; `specs/003-authoring-contract/contracts/postmerge-gate-requirements.json` is exclusively the PostMerge list. No `Applicable` requirement appears in the wrong temporal snapshot. Each gate has exactly one Primary proof; Supplemental proof points to it. Command and runner tokens must occur in real logs. PreMerge requires the current reviewed head, green technical gates, closed actionable threads, available required approval, and normal-policy merge readiness, but no already executed merge. PostMerge binds PreMerge through `acceptedPreMergePath` and `acceptedPreMergeSha256` and requires actual merge, lifecycle, reporting, retrospective, trend, and synchronization facts. Delivery Authority `MergeAndSync` permits normal local commits, push, PR, merge, and sync within the approved scope, but no admin bypass, scope expansion, Level 0 change, or provider mutation.

## Komplexitätsverfolgung / Complexity Tracking

Keine Verfassungsabweichung. Der additive Validator ist erforderlich, weil der abgeschlossene Reparatur-Checker einen historischen Bindungszustand absichtlich unveränderlich festschreibt; seine Änderung würde genau den Beweis zerstören, den die neue Kette als Vorgänger benötigt.

No constitutional deviation exists. The additive validator is necessary because the completed repair checker intentionally freezes a historical binding state; changing it would destroy the very proof that the new chain needs as its predecessor.
