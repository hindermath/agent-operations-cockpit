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

## Technischer Kontext / Technical Context

**Sprachen und Laufzeiten**: C#/.NET bleibt der primäre Level-2-Projektkontext, wird in diesem Feature aber nicht geändert. Markdown und JSON bilden die Verträge; Python 3 trägt fokussierte read-only Validatorlogik; Bash 5+ und PowerShell Core 7+ sind gleichwertige Oberflächen.

**Primäre Abhängigkeiten**: Git, `jq`, Python-Standardbibliothek, bestehende Intake-Authoring-Skripte, PSScriptAnalyzer 1.25.0, Gitleaks und die kanonischen Statistik-Renderer.

**Speicherung**: Nur repository-gebundene Text-, JSON- und Evidence-Dateien; keine Datenbank und kein Agentenlaufzeit-Speicher.

**Tests**: Drei vorhandene PowerShell-Fixture-Suiten, neue gezielte Negativ-Fixtures, der neue feature-lokale Binding-Validator, direkte Receipt-Validierung für META-LH-03 und alle 14 aktuellen Receipts auf Bash und PowerShell sowie semantische Reviews.

**Zielplattformen**: `ubuntu-22.04`, `macos-14` und `windows-2022`; auf Windows ist die geprüfte Git-for-Windows-Bash maßgeblich, nicht WSL.

**Projekttyp**: Governance- und Vertragsänderung in einem bestehenden Repository; keine Laufzeit-Anwendung.

**Leistungsziel**: Deterministische, read-only Validierung der kleinen Vertragsmenge; keine throughput- oder latenzeabhängige Produktanforderung.

**Randbedingungen**: Exakte Liefermenge, fail-closed, keine Secrets, keine absoluten lokalen Pfade in öffentlichen Artefakten, kein Admin-Bypass, keine fremden Änderungen, keine Run-State-Änderung in dieser Planphase.

**Umfang**: Fünf kanonische Fachartefakte, ihre zwingenden Konsumenten und Nachweise sowie genau eine spätere META-LH-03-Erneuerung.

**Languages and runtimes**: C#/.NET remains the primary Level 2 project context but is not changed by this feature. Markdown and JSON form the contracts; Python 3 carries focused read-only validator logic; Bash 5+ and PowerShell Core 7+ are equivalent surfaces.

**Primary dependencies**: Git, `jq`, the Python standard library, existing Intake Authoring scripts, PSScriptAnalyzer 1.25.0, Gitleaks, and the canonical statistics renderers.

**Storage**: Repository-bound text, JSON, and evidence files only; no database or agent runtime store.

**Testing**: Three existing PowerShell fixture suites, new focused negative fixtures, the new feature-local binding validator, direct receipt validation for META-LH-03 and all 14 current receipts on Bash and PowerShell, plus semantic reviews.

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
- **Agenten-Guidance**: Die fünf gemeinsamen Agentenflächen sind nicht betroffen und werden nicht geändert.
- **Dokumentationsauswirkung**: Es gilt genau die Entscheidung `UpdateRequired` aus `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`. Dieses Dokument bleibt alleiniger Owner der Entscheidung. Dieser Plan und alle weiteren Feature-Artefakte referenzieren sie nur. Kein Home-Sync ist erforderlich.

- **Level 2 and MSL**: AOC is a Level 2 reference project but is not registered as a runtime project in the shared Level 2 registry. Python 3, Bash 5+, and PowerShell Core 7+ are prescribed for the existing validator surfaces; Python and PowerShell are memory-safe languages (MSLs). Bash remains limited to small, quoted adapters.
- **Secure generation and architecture**: Inputs remain data. The contract separates trusted repository files, public HTTPS sources, and untrusted payloads. It uses allowlists, path boundaries, normalized hashes, immutable predecessors, least privilege, and blocked defaults. Shell variables are quoted; no dynamic code execution or credentials are planned.
- **Security documentation and standards**: NIST SSDF and CWE Top 25 apply and will be assessed in `specs/003-authoring-contract/security-review-evidence.md`. OWASP ASVS, release SBOM/VEX/SLSA, CAPEC, AI-SBOM, Zero Trust, C3A, C5, SAMM, and regulatory product evidence are `N/A` for this document/validator-only change; triggers are runtime, release, cloud, AI component, or regulated-product changes. A product threat model, S-ADR, or arc42 section is therefore not required. The focused trust-boundary assessment belongs in `specs/003-authoring-contract/architecture-review-evidence.md`.
- **Supply chain and secrets**: No dependency is added. The full command `gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100` must cover the exact reviewed HEAD. The configuration must not exclude active Authoring tests.
- **Presets**: The installed governance matrix, including the three Intake presets, remains unchanged. There is no installation, version change, promotion, or Level 0 distribution.
- **A11Y and language**: Every affected user-facing Markdown and JSON example is reviewed as German first and English second, text-first, and against WCAG 2.2 AA, semantic headings, CEFR B2, and first-use explanations. Results belong in `specs/003-authoring-contract/accessibility-review-evidence.md`.
- **Platform parity**: Identical domain rules run on Ubuntu, macOS, and Windows with Bash and PowerShell. Evidence belongs in `specs/003-authoring-contract/cross-platform-parity-evidence.md`.
- **Statistics**: `docs/project-statistics.md` needs a generated Methodology v2 update after feature delivery; as a C#/.NET repository, the documented Thorsten-solo value of 125 lines per visible Git activity day applies in addition to the conservative baseline of 80. The writer may run only on a clean, real feature HEAD.
- **Agent guidance**: The five shared agent surfaces are unaffected and remain unchanged.
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
│   └── autonomous-run-gate-requirements.json
└── phase-results/
    └── plan-report.md
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
├── contracts/                         # additiver Feature-Validator
├── *-review-evidence.md                # vier fokussierte Reviewberichte
├── current-evidence-binding.json       # nur spätere META-LH-03-Blattänderung
├── autonomous-run-gate-evidence.json
└── causal-closeout-evidence.json

.github/workflows/powershell-analysis.yml # nur falls die bestehende Matrix
                                         # die neuen exakten Befehle noch nicht ausführt
docs/man/validate-authoring-contract.1
docs/project-statistics.md
```

**Strukturentscheidung**: Der Fachvertrag bleibt in den vorhandenen Preset- und `requirements/`-Pfaden. Neue Bindungslogik ist feature-lokal und additiv, damit der historische Reparatur-Checker unverändert bleibt. Die bestehende Drei-Plattform-Matrix wird erweitert, statt einen neuen Workflow oder neue Provider-Konfiguration einzuführen.

**Structure decision**: The domain contract remains in the existing preset and `requirements/` paths. New binding logic is feature-local and additive so the historical repair checker stays unchanged. The existing three-platform matrix is extended instead of creating a new workflow or provider configuration.

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

### 1. Voraussetzung einfrieren / Freeze the prerequisite

Vor der Fachänderung wird die bereits abgeschlossene Binding-Reparatur als exakt begrenzter Kandidat geprüft und separat normal committet. Die Liefermenge entspricht den in `specs/003-authoring-contract/binding-repair-validation.json` gebundenen Reparaturdateien einschließlich vier Renewals, vier Reviews, unveränderlicher Archive, Brücken-Receipts und des bestehenden Checkers. `git diff --cached --check`, Statusabgleich und der dokumentierte 23-Test-Nachweis müssen zum Kandidaten passen. Keine Planungsdatei oder fremde Änderung wird versehentlich aufgenommen. Dieser Schritt wiederholt weder die vier Reviews noch Global 14.

Before the domain change, the already completed binding repair is checked as an exactly bounded candidate and committed separately through normal policy. Its delivery set is the repair file set bound by `specs/003-authoring-contract/binding-repair-validation.json`, including four renewals, four reviews, immutable archives, bridge receipts, and the existing checker. `git diff --cached --check`, status reconciliation, and the documented 23-test evidence must match the candidate. No planning file or foreign change is accidentally included. This step reruns neither the four reviews nor Global 14.

### 2. Fünf Fachartefakte und zwingende Konsumenten / Five domain artefacts and necessary consumers

Die fünf Fachartefakte werden in ihrer festgelegten Reihenfolge geändert. Danach werden nur Konsumenten angepasst, die eine neue Regel maschinell oder lesbar abbilden müssen: Receipt-Validator Bash/PowerShell und Manpage, Governance-Konfigurationsvalidator und Manpage, drei vorhandene Fixture-Suiten, der feature-lokale additive Contract-Validator mit Bash-/PowerShell-Adapter und Tests, vier fokussierte Reviewberichte sowie bei nachgewiesenem Bedarf ein einzelner Schritt in `.github/workflows/powershell-analysis.yml`.

The five domain artefacts are changed in their fixed order. Only consumers that must represent a new rule in machine-readable or human-readable form are then changed: receipt validators for Bash/PowerShell and their man page, the governance configuration validator and man page, three existing fixture suites, the feature-local additive contract validator with Bash/PowerShell adapters and tests, four focused review reports, and, if proven necessary, one step in `.github/workflows/powershell-analysis.yml`.

### 3. Lokale und Matrix-Prüfung / Local and matrix validation

Die exakten Befehle stehen in `specs/003-authoring-contract/quickstart.md`; die maschinenlesbaren Gates stehen in `specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json`. Die drei kanonischen Fixture-Suiten, META-LH-03 und ein aus `current-evidence-binding.json` abgeleitetes, auf exakt 14 eindeutige Ziel-IDs geprüftes Receipt-Inventar laufen sowohl über Bash als auch PowerShell. Auf `ubuntu-22.04`, `macos-14` und `windows-2022` müssen die Logs Befehl, unmittelbaren Exitcode, Runner und geprüften HEAD zeigen. Auf Windows wird der validierte Pfad zu Git-for-Windows-Bash an Kindprozesse weitergegeben. Ein bloß grüner Workflow- oder Jobname ist nur ergänzender Nachweis.

Exact commands are in `specs/003-authoring-contract/quickstart.md`; machine-readable gates are in `specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json`. The three canonical fixture suites, META-LH-03, and a receipt inventory derived from `current-evidence-binding.json` and checked for exactly 14 unique target IDs run through both Bash and PowerShell. On `ubuntu-22.04`, `macos-14`, and `windows-2022`, logs must show the command, immediate exit code, runner, and verified HEAD. On Windows, the validated Git-for-Windows Bash path is propagated to child processes. A merely green workflow or job name is supplemental evidence only.

### 4. Nur META-LH-03 neu binden / Rebind only META-LH-03

Nach dem letzten Fachartefakt-Byte wird der aktuelle META-LH-03-Vorgänger byte-identisch in einen neuen Archivpfad kopiert. Die stabile Intake-ID bleibt erhalten. Reservierte neue Identitäten sind Operation `9a3586f4-a375-475c-b44f-bdc7c39d9d3d`, Receipt `0997f398-a986-437a-b091-87da3da83e9f` und Review `e69644e1-adc7-4f1f-857b-bce390ae8764`. Sie werden nur verwendet, wenn sie beim Ausführungszeitpunkt noch eindeutig sind. Das neue Receipt bindet die finalen Hashes aller fünf Fachartefakte, den unmittelbaren Vorgänger und die Genehmigung. Danach wird ein vollständiger neuer Single-Review für exakt diesen Zielhash erstellt und mit Bash und PowerShell validiert.

After the final domain-artefact byte, the current META-LH-03 predecessor is copied byte-identically to a new archive path. The stable intake ID remains unchanged. Reserved new identities are operation `9a3586f4-a375-475c-b44f-bdc7c39d9d3d`, receipt `0997f398-a986-437a-b091-87da3da83e9f`, and review `e69644e1-adc7-4f1f-857b-bce390ae8764`. They are used only if still unique at execution time. The new receipt binds the final hashes of all five domain artefacts, the immediate predecessor, and the approval. A complete new Single review for exactly that target hash is then produced and validated with Bash and PowerShell.

Der neue feature-lokale Validator behandelt `binding-repair-validation.json`, den bisherigen Binding-Hash und den vorhandenen Reparatur-Checker als unveränderlichen Vorgänger. Er erlaubt genau ein neues META-LH-03-Blatt, verlangt Gleichheit für die übrigen 13 Blätter und bewahrt die Series-Brücke. `current-evidence-binding.json` wird erst nach dem neuen `Ready`-Review auf das neue META-LH-03-Blatt aktualisiert. Fehlende menschliche Genehmigung ist ein Blocker; sie wird nicht aus Schweigen oder Toolzustand abgeleitet.

The new feature-local validator treats `binding-repair-validation.json`, the previous binding hash, and the existing repair checker as immutable predecessors. It permits exactly one new META-LH-03 leaf, requires equality for the other 13 leaves, and preserves the Series bridge. `current-evidence-binding.json` is updated to the new META-LH-03 leaf only after the new `Ready` review. Missing human approval is a blocker; it is not inferred from silence or tool state.

### 5. Reviews, Liefermenge und Statistik / Reviews, delivery set, and statistics

Die vier Reviewberichte prüfen Sicherheit/Quellenautorität, Architektur/Vertrauensgrenzen, Barrierefreiheit/Sprache und Plattformparität. Sie verweisen auf die einzige Dokumentationsauswirkungsentscheidung und enthalten tatsächliche Befehle, Ergebnisse, Reviewer und HEAD statt Prognosen. Danach wird die exakte Feature-Liefermenge aus dem deklarativen Design aufgelöst, jeder Pfad gegen `git status` und `git diff` abgeglichen, ausschließlich diese Menge gestaged und mit `git diff --cached --check` read-only geprüft. Fremde oder nicht freigegebene Dateien bleiben unberührt. Erst danach entsteht ein normaler Implementierungs-Checkpoint-Commit ohne Statistik-Ledger.

The four review reports assess security/source authority, architecture/trust boundaries, accessibility/language, and platform parity. They reference the sole Documentation Impact decision and contain actual commands, results, reviewer, and HEAD instead of forecasts. The exact feature delivery set is then resolved from the declarative design, every path reconciled with `git status` and `git diff`, only that set staged, and the staged candidate checked read-only with `git diff --cached --check`. Foreign or unauthorized files remain untouched. Only then is a normal implementation checkpoint commit created without the statistics ledger.

Auf dem danach sauberen echten Feature-Branch läuft `bash scripts/render-project-statistics.sh --repo .`. Anschließend müssen Bash- und PowerShell-`--check-only`/`-CheckOnly` jeweils JSON-Erfolg melden. Nur `docs/project-statistics.md` wird separat committet. Weil Ledger und Ledger-Commit in Methodik v2 ausgeschlossen sind, wird kein weiterer Writer-Zyklus erzeugt. Die beiden Check-only-Läufe werden am sauberen endgültigen Feature-HEAD wiederholt. Meldet der Writer unerwartet keine Änderung, wird kein leerer Commit erzeugt; die Ursache wird dokumentiert.

On the then-clean real feature branch, `bash scripts/render-project-statistics.sh --repo .` runs. Bash and PowerShell `--check-only`/`-CheckOnly` must then each report JSON success. Only `docs/project-statistics.md` is committed separately. Because the ledger and ledger commit are excluded by Methodology v2, no further writer cycle is created. Both check-only commands run again on the clean final feature HEAD. If the writer unexpectedly reports no change, no empty commit is created; the cause is recorded.

### 6. Merge, Lifecycle und kausaler Abschluss / Merge, lifecycle, and causal closeout

Der temporäre Runner-Nachweis `premerge-gate-evidence.json` ist ein Runner-Artefakt und kein Repository-Pfad. Er bindet Schema 2, finalen Requirements-Hash, exakten geprüften HEAD, reale Befehle, Runner, unmittelbare Exitcodes, Reviews, Checks und die verfügbare Approval. Der Feature-PR wird ohne Admin-Bypass nach normaler Policy gemergt; danach wird `main` ausschließlich fast-forward synchronisiert und `0/0` Ahead/Behind nachgewiesen.

The temporary runner evidence `premerge-gate-evidence.json` is a runner artefact, not a repository path. It binds schema 2, the final requirements hash, exact reviewed HEAD, real commands, runners, immediate exit codes, reviews, checks, and available approval. The feature PR is merged under normal policy without admin bypass; `main` is then synchronized by fast-forward only and `0/0` ahead/behind is proven.

Die verfassungsgemäße Lastenheft-Umbenennung folgt erst nach dem Feature-Merge über die vorhandenen gepaarten Skripte in einem eigenen normal geprüften PR. `specs/003-authoring-contract/intake-lifecycle.json` ordnet dabei den unveränderten logischen META-LH-03-Pfad dem physischen umbenannten Pfad zu. Der abgeschlossene Series-Manifestpfad und der META-LH-02-Lifecycle werden nicht geändert. Danach wird erneut fast-forward synchronisiert und `0/0` belegt.

The constitution-required Lastenheft rename follows only after the feature merge through the existing paired scripts in its own normally reviewed PR. `specs/003-authoring-contract/intake-lifecycle.json` maps the unchanged logical META-LH-03 path to the physical renamed path. The completed Series manifest path and META-LH-02 lifecycle are not changed. Fast-forward synchronization and `0/0` proof follow again.

Erst nach realem Merge und Sync darf `specs/003-authoring-contract/causal-closeout-evidence.json` diese Fakten festhalten. Falls Run-State und Tasks wegen ihrer eigenen Kausalität erst danach terminal gesetzt werden können, ist genau ein Evidence-only-Closeout auf dem vorbenannten Branch `003-authoring-contract-closeout` zulässig. Seine Menge ist auf `specs/003-authoring-contract/tasks.md`, `specs/003-authoring-contract/autonomous-run-state.json` und `specs/003-authoring-contract/causal-closeout-evidence.json` begrenzt. Auch dieser PR benötigt normale Checks, Review und verfügbare Approval; danach folgt der endgültige fast-forward-Sync mit sauberem Worktree und `0/0`.

Only after real merge and synchronization may `specs/003-authoring-contract/causal-closeout-evidence.json` record those facts. If run state and tasks can become terminal only afterwards because of their own causal ordering, exactly one evidence-only closeout is permitted on the pre-named branch `003-authoring-contract-closeout`. Its set is limited to `specs/003-authoring-contract/tasks.md`, `specs/003-authoring-contract/autonomous-run-state.json`, and `specs/003-authoring-contract/causal-closeout-evidence.json`. That PR also needs normal checks, review, and available approval; final fast-forward synchronization then proves a clean worktree and `0/0`.

Die Statistik bildet den sauberen finalen Feature-HEAD vor den nachgelagerten Lifecycle- und Evidence-only-Textcommits ab. Diese späteren, ebenfalls textwirksamen Commits werden beim nächsten regulären Methodik-v2-Trigger berücksichtigt; sie lösen in diesem Lauf keine spekulative Rückprojektion und keinen Endloszyklus aus.

The statistics snapshot represents the clean final feature HEAD before later lifecycle and evidence-only text commits. Those later text-affecting commits are included at the next regular Methodology v2 trigger; they do not cause speculative back-projection or an endless cycle in this run.

## Liefermengenvertrag / Delivery-Set Contract

Die konkrete Positivliste wird aus `specs/003-authoring-contract/contracts/authoring-contract-design.json` aufgelöst. Zulässig sind ausschließlich:

- die fünf benannten Fachartefakte;
- direkt benannte Validatoren, Adapter, Manpages und die drei Fixture-Suiten;
- der additive Feature-Validator und seine Tests;
- die vier benannten Review-Evidence-Dateien, Gate-Evidence und Lifecycle-/Closeout-Evidence;
- `current-evidence-binding.json` sowie ausschließlich die neue META-LH-03-Operation, das Receipt, Archiv, Review-Request, Review-Result und den Reviewbericht;
- bei nachgewiesenem Bedarf der eine vorhandene Workflow;
- `docs/project-statistics.md` ausschließlich im separaten Ledger-Commit.

The concrete allowlist is resolved from `specs/003-authoring-contract/contracts/authoring-contract-design.json`. Only the following are allowed:

- the five named domain artefacts;
- directly named validators, adapters, man pages, and the three fixture suites;
- the additive feature validator and its tests;
- the four named review-evidence files, gate evidence, and lifecycle/closeout evidence;
- `current-evidence-binding.json` and only the new META-LH-03 operation, receipt, archive, review request, review result, and review report;
- the one existing workflow if proven necessary;
- `docs/project-statistics.md` only in the separate ledger commit.

Vor jedem Commit erzeugt ein read-only Vergleich die Mengen `planned`, `changed`, `staged` und `foreign`. `changed - planned` und `staged - intended` müssen leer sein; fehlende geplante Dateien benötigen eine begründete `N/A`-Entscheidung. Pfade werden einzeln und repository-relativ gestaged. Es gibt kein `git add -A`, keinen Reset, keinen Stash, kein Force, kein Amend, keine Löschung fremder Daten und keinen absoluten Pfad in einem veröffentlichten Nachweis.

Before every commit, a read-only comparison produces the sets `planned`, `changed`, `staged`, and `foreign`. `changed - planned` and `staged - intended` must be empty; missing planned files require a justified `N/A` decision. Paths are staged individually and repository-relatively. There is no `git add -A`, reset, stash, force, amend, deletion of foreign data, or absolute path in published evidence.

## Gate- und Approval-Vertrag / Gate and Approval Contract

`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json` ist die verbindliche maschinenlesbare Gate-Liste. Je Gate gibt es genau einen Primärnachweis; ergänzende Nachweise verweisen auf diesen. Befehls- und Runner-Tokens sind Mindestanforderungen und müssen in realen Logs vorkommen. Die Prüfung ist HEAD-genau. Reviewberichte und aktueller Checkstatus sind Pflicht. Delivery Authority `MergeAndSync` erlaubt normale lokale Commits, Push, PR, Merge und Sync im genehmigten Scope, aber keinen Admin-Bypass, keine Ausweitung und keine Level-0-/Provider-Änderung. Eine nicht verfügbare Approval bleibt fehlend und blockiert den betreffenden Merge.

`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json` is the binding machine-readable gate list. Each gate has exactly one Primary proof; Supplemental proof points to it. Command and runner tokens are minimum requirements and must appear in real logs. Validation is HEAD-exact. Review reports and current check status are mandatory. Delivery Authority `MergeAndSync` permits normal local commits, push, PR, merge, and sync within the approved scope, but no admin bypass, scope expansion, Level 0 change, or provider mutation. Unavailable approval remains missing and blocks the relevant merge.

## Komplexitätsverfolgung / Complexity Tracking

Keine Verfassungsabweichung. Der additive Validator ist erforderlich, weil der abgeschlossene Reparatur-Checker einen historischen Bindungszustand absichtlich unveränderlich festschreibt; seine Änderung würde genau den Beweis zerstören, den die neue Kette als Vorgänger benötigt.

No constitutional deviation exists. The additive validator is necessary because the completed repair checker intentionally freezes a historical binding state; changing it would destroy the very proof that the new chain needs as its predecessor.
