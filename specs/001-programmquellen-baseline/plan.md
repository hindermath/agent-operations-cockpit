# Implementierungsplan: Programmquellen-Baseline / Implementation Plan: Program Sources Baseline

**Branch / Branch**: `001-programmquellen-baseline` | **Datum / Date**: 2026-08-09 | **Spezifikation / Spec**: [spec.md](spec.md)
**Eingabe / Input**: Formal geklaerte Feature-Spezifikation in `specs/001-programmquellen-baseline/spec.md` und die drei hashgebundenen akzeptierten Artefakte. / Formally clarified feature specification in `specs/001-programmquellen-baseline/spec.md` and the three hash-bound accepted artefacts.

## Zusammenfassung / Summary

META-LH-01 liefert ausschliesslich eine eigenstaendige Level-2-Dokumentations- und Governance-Baseline. Die Umsetzung beginnt mit einem Delta-Audit und bewahrt jede bereits richtige Aussage. Geaendert werden nur Luecken gegen die geklaerte Spezifikation: die exakte Einzelinventur von 23 Quellen, die lueckenlose Einzelabdeckung `RF-01` bis `RF-21`, die exakte direkte META-LH-01-Owner-Menge, vollstaendige DE-first/EN-second-Inhalte sowie praezise G-01-, G-05- und G-06-Evidence. / META-LH-01 delivers only a self-contained level-2 documentation and governance baseline. Implementation starts with a delta audit and preserves every correct statement. Only gaps against the clarified specification are changed: the exact individual inventory of 23 sources, complete individual coverage of `RF-01` through `RF-21`, the exact direct META-LH-01 owner set, complete German-first/English-second content, and precise G-01, G-05, and G-06 evidence.

Die sechs Domain-Artefakte bleiben unveraendert begrenzt. Schema 1.1 bewahrt den exakten META-LH-01-Lifecycle-Datensatz und ergaenzt einen deterministischen Snapshot der 14 geordneten akzeptierten Ziel-/Receipt-/Ready-Review-Bindungen. Vor Implement bleibt die generische Receipt-/Review-Frische zwingend; nur der aktuelle exakte Zustand `Implement`/`Active`/`GlobalReadyBeforeImplement` darf nach vollstaendiger Snapshot-, Run-, Branch- und Lifecycle-Pruefung die Receipt-Quellenfrische ersetzen, waehrend beide Review-Oberflaechen weiterlaufen. Der normale Kandidat enthaelt weiterhin den Pending-Closeout-Anker; Rename und Drei-Pfad-Closeout bleiben der einzige Lieferpfad. / Schema 1.1 preserves the exact META-LH-01 lifecycle record and adds one deterministic fourteen-target accepted-evidence snapshot. The substitution is limited to the exact qualified post-Implement state, and the existing delivery path remains unchanged.

## Technischer Kontext / Technical Context

**Sprache/Version / Language/version**: Markdown und UTF-8 fuer Domain-Inhalte; Python 3 Standardbibliothek fuer read-only Acceptance-Evidence, keine Produkt-Runtime. / Markdown and UTF-8 for domain content; Python 3 standard library for read-only acceptance evidence, not a product runtime.

**Primaere Abhaengigkeiten / Primary dependencies**: Keine neuen Abhaengigkeiten; vorhandene Repository-Validatoren, Git, `rg`, `gitleaks`, Bash und PowerShell 7 dienen nur der Pruefung. / No new dependencies; installed repository validators, Git, `rg`, `gitleaks`, Bash, and PowerShell 7 are validation tools only.

**Speicherung / Storage**: Git-getrackte Markdown- und JSON-Artefakte im Level-2-Repository. / Git-tracked Markdown and JSON artefacts in the level-2 repository.

**Pruefung / Testing**: Ein stabiler Python-Vertrag mit expliziten Modi und exakt 66 isolierten Faellen: die vorhandenen 43 bleiben erhalten; 23 neue Faelle pruefen drei positive Post-Implement-Oberflaechen sowie pre-Implement-Drift, gefaelschte Stage-/Status-/Gate-Werte, Zielmengen-/Reihenfolgefehler, falsche Pfade/Hashes/Bytes, non-Ready oder nicht eindeutige Reviews und falsche Run-/Branch-/Lifecycle-Bindungen. Intake-/Review-/Run-State-Validatoren, logisch aktuelles 14er-Gate und alle bisherigen Evidence-Klassen bleiben erhalten; keine Produkttests. / The contract now has exactly 66 isolated cases: all previous 43 plus 23 snapshot and fail-closed drift cases; no product tests.

**Zielplattform / Target platform**: Repository-lokale Markdown-Nutzung; plattformunabhaengiger Text. Die vorhandenen Bash- und PowerShell-Validatoroberflaechen werden dort paarweise ausgefuehrt, wo die akzeptierte Evidence beide verlangt. / Repository-local Markdown use with platform-neutral text. Existing Bash and PowerShell validator surfaces run as a pair where accepted evidence requires both.

**Projekttyp / Project type**: Reine Dokumentations- und Governance-Aenderung. / Documentation-and-governance-only change.

**Leistungsziele / Performance goals**: Fuer das Produkt `N/A`; keine Produkt-Runtime. Re-Evaluation bei ausfuehrbarem Produktartefakt. Der read-only Evidenzvertrag ist kein Performance- oder Produkt-Scope. / `N/A` for the product; there is no product runtime. Re-evaluate if an executable product artefact enters scope. The read-only evidence contract is outside product performance scope.

**Constraints**: DE zuerst und autoritativ, EN danach gleichwertig, etwa CEFR B2, WCAG 2.2 AA soweit anwendbar, text-first, nur oeffentlich geeignete Inhalte, fail-closed bei Hash-/Authority-/Evidence-Drift. / German first and authoritative, equivalent English second, approximately CEFR B2, WCAG 2.2 AA where applicable, text first, public-suitable content only, and fail closed on hash, authority, or evidence drift.
**Umfang / Scale/scope**: Sechs Domain-Dateien, Feature-Artefakte einschliesslich eines Pending-Closeout-Ankers, genau ein bewahrter Lifecycle-Datensatz plus ein 14-Ziel-Snapshot, ein beschreibender und ein ausfuehrbarer Validierungsvertrag, 66 Tests, eine unveraenderte maximale Feature-Allowlist, genau ein terminaler Original-zu-Archiv-Rename sowie eine separate exakte Drei-Pfad-Closeout-Transaktion. / Six domain files, one preserved lifecycle record plus a fourteen-target snapshot, 66 tests, the unchanged allowlist, terminal rename, and exact closeout transaction.

Es bestehen keine offenen Klaerungsmarker. / No unresolved clarification markers remain.

## Verfassungspruefung / Constitution Check

*Gate vor Phase 0: bestanden. Erneute Pruefung nach Phase 1: bestanden. / Gate before Phase 0: passed. Re-check after Phase 1: passed.*

Jede Zeile trennt Anwendbarkeit und Umsetzungsstatus. Owner ist der AOC Requirements Maintainer, Reviewer ist ein unabhaengiger Dokumentations-/Spec-Reviewer, sofern keine speziellere Rolle genannt ist. Evidence sind dieser Plan, [research.md](research.md), [data-model.md](data-model.md), [quickstart.md](quickstart.md), der [Validierungsvertrag](contracts/baseline-validation-contract.md) und die spaetere exakte Ausfuehrungsevidence. / Each row separates applicability and implementation status. The AOC Requirements Maintainer is owner and an independent documentation/spec reviewer is reviewer unless a more specific role is named. Evidence consists of this plan, the linked design artefacts, the validation contract, and later exact execution evidence.

| Pruefpunkt / Checkpoint | Anwendbarkeit / Applicability | Umsetzung / Implementation | Begruendung und Evidence / Rationale and evidence | Restluecke, Follow-up und Neubewertung / Residual gap, follow-up, and re-evaluation |
|---|---|---|---|---|
| Level-2-Umgebung / Level-2 environment | N/A | Not Assessed | In der gemeinsam gelesenen Registry fehlt ein AOC-Eintrag; fuer Markdown wird keine Runtime abgeleitet. / The shared registry has no AOC row; no runtime is inferred for Markdown. | Keine Restluecke fuer diesen Scope; neu bei Registry-Eintrag oder Runtime-Handoff. / No gap for this scope; re-evaluate for a registry entry or runtime handoff. |
| MSL und sichere Codeerzeugung / MSL and secure code generation | N/A fuer Produktartefakte | Not Assessed | Kein Produktcode, Generator, Runtime-Artefakt oder Sprach-Scaffold; C#/.NET bleibt nur spaetere bestaetigte Primaerplattform. Der feature-lokale Standardbibliothek-Python-Vertrag ist read-only Workflow-Evidence und durch isolierte Contract-Tests abgesichert. / No product code, generator, runtime artefact, or language scaffold. The feature-local Python contract is read-only workflow evidence covered by isolated contract tests. | Neu bei autorisiertem Produktcode oder Generator. / Re-evaluate for authorised product code or a generator. |
| NIST SSDF | Applicable | Partly Fulfilled | Hash-Bindung, geschuetzte Quellen, minimale Schreibflaeche, fail-closed Gates und geplante Evidence decken den dokumentarischen SDLC ab. / Hash binding, protected sources, minimal write scope, fail-closed gates, and planned evidence cover the documentation SDLC. | Umsetzungsevidence steht bis zur Implementierungsphase aus; danach Review. / Delivery evidence remains pending until implementation, then review. |
| CWE Top 25 | Applicable | Partly Fulfilled | Das Scope-Gate verhindert vorgezogene Produktlogik. Secret- und Pfadscans belegen ausschliesslich die geprueften Muster; positive und negative Contract-Tests pruefen die read-only Python-Evidenzlogik getrennt. / The scope gate prevents premature product logic. Scanners prove only their configured patterns; contract tests separately cover the read-only Python evidence logic. | Kein produktspezifischer Codebefund; neu bei Parser, Generator oder Produktcode. / No product-code finding; re-evaluate for a parser, generator, or product code. |
| Sichere Architektur, STRIDE/CIA/CAPEC, Zero Trust, S-ADR, arc42 / Secure architecture set | N/A | Not Assessed | Keine Struktur-, Interface-, Trust-, Datenfluss-, Deployment- oder Runtime-Aenderung. / No structural, interface, trust, data-flow, deployment, or runtime change. | Architecture Owner; neu bei einer solchen Grenze. / Re-evaluate when such a boundary changes. |
| OWASP ASVS | N/A | Not Assessed | Keine Web-, API-, HTTP-, Authentifizierungs- oder Autorisierungsfunktion. / No web, API, HTTP, authentication, or authorisation capability. | Security Owner; neu bei einer solchen Schnittstelle. / Re-evaluate for such an interface. |
| SBOM, VEX, SLSA, OpenSSF Scorecard | N/A | Not Assessed | Keine Komponente, Dependency, Build-, Paket-, Release- oder Publikationsausgabe. / No component, dependency, build, package, release, or publication output. | Security Owner; neu bei Dependency-, Build- oder Release-Handoff. / Re-evaluate at such a handoff. |
| AI-SBOM | N/A | Not Assessed | KI ist Entwicklungswerkzeug und kein Produkt- oder Runtime-Bestandteil. / AI is a development tool, not a product or runtime component. | Security Owner; neu bei AI-Produktbestandteil. / Re-evaluate for an AI product component. |
| BSI C3A, BSI C5 und Regulatory / BSI C3A, BSI C5, and regulatory | N/A | Not Assessed | Reine repository-lokale Governance ohne Cloud-Service-Auswahl, Marktprodukt, regulierten Kunden oder Provider-Runtime. / Repository-local governance without cloud-service selection, a market product, regulated customer, or provider runtime. | Security/Architecture Owner; neu bei Cloud-, Markt- oder Regulierungs-Trigger. / Re-evaluate for a cloud, market, or regulatory trigger. |
| OWASP SAMM und Cheat Sheets / OWASP SAMM and cheat sheets | N/A | Not Assessed | Keine programmweite Reifegradbewertung und keine Implementierungslogik in diesem Feature. / No programme-wide maturity assessment or implementation logic in this feature. | Security Owner; neu bei separatem Assessment oder Code. / Re-evaluate for a separate assessment or code. |
| Security-Dokumente unter `docs/security/` / Security documents under `docs/security/` | N/A | Not Assessed | Die geklaerte Spec ist die begruendete Evidence fuer code- und architekturbezogene `N/A`-Entscheidungen; neue Security-Dokumente waeren ausserhalb des Scopes. / The clarified spec records justified code- and architecture-related `N/A` decisions; new security documents would exceed scope. | Neu bei Security-, Trust-, Dependency-, Cloud- oder Release-Grenze. / Re-evaluate for such a boundary. |
| Oeffentliche Inhaltsgrenze und Security-first / Public-content boundary and security first | Applicable | Partly Fulfilled | Nur oeffentlich geeignete, repository-relative Inhalte; `gitleaks`, Repository-Scanner und expliziter Privatpfad-/Personendaten-Review sind geplant. / Public-suitable, repository-relative content only; `gitleaks`, the repository scanner, and explicit private-path/personal-data review are planned. | Ausfuehrungsevidence steht aus; jeder neue Inhalt triggert erneuten Scan. / Execution evidence remains pending; every new content item triggers a new scan. |
| WCAG 2.2 AA und Text-first / WCAG 2.2 AA and text first | Applicable | Partly Fulfilled | Die sechs Domain-Dateien, Planungsartefakte und der nutzerlesbare JSON-Closeout-Anker verwenden textliche Status- und Abhaengigkeitsdarstellung; der Anker wird in Semantik/A11Y aufgenommen. / The six domain files, planning artefacts, and readable JSON closeout anchor use textual status and dependency representations and are included in semantic/accessibility review. | Unabhaengige Review-Evidence steht bis nach den Edits aus; neu bei jeder Text- oder Schemaaenderung. / Independent review remains pending; re-evaluate for every text or schema change. |
| DE-first/EN-second und CEFR B2 / German-first/English-second and CEFR B2 | Applicable | Partly Fulfilled | Deutsche Aussage steht zuerst, gleichwertiges Englisch folgt; Erstnutzungsbegriffe verlinken das Glossar und setzen keine Spec-Kit-Erfahrung voraus. / German comes first and equivalent English follows; first-use terms link to the glossary and assume no Spec Kit experience. | Die Delta-Liste benennt vorhandene Sprachluecken; null blocking Abweichungen vor Abschluss. / The delta list identifies existing language gaps; zero blocking deviations before completion. |
| Plattform- und Bash/PowerShell-Paritaet / Platform and Bash/PowerShell parity | N/A | Not Assessed | Kein Bash-/PowerShell-Produkttool, Cmdlet, CLI, Man-Page oder Plattformverhalten. Der feature-lokale Python-Vertrag nutzt nur die Standardbibliothek und ruft vorhandene Validatorpaare read-only auf. / No Bash/PowerShell product tool or platform behaviour; the standard-library contract only consumes installed validator pairs read-only. | Platform Owner; neu bei Produkt-CLI, plattformspezifischem Verhalten oder Bash-/PowerShell-Aenderung. / Re-evaluate for such a change. |
| Agentenparitaet / Agent parity | N/A | Not Assessed | Keine gemeinsame Agenten-Guidance, Templates oder Constitution werden geaendert. / No shared agent guidance, templates, or constitution are changed. | Agent Guidance Owner; neu bei Guidance-Aenderung. / Re-evaluate for a guidance change. |
| Parallel-Ausfuehrung / Parallel execution | N/A | Not Assessed | Ein eng gebundener META-LH-01-Lauf mit ueberlappenden Domain-Dateien; keine Worker-Kampagne. / One bounded META-LH-01 run with overlapping domain files; no worker campaign. | Autonomous Run Operator; neu bei explizit autorisierter Kampagne mit disjunkten Writes. / Re-evaluate for an explicitly authorised campaign with disjoint writes. |
| Projektstatistik / Project statistics | Applicable | Not Fulfilled | Nach abgeschlossener Implementierungsphase muss `docs/project-statistics.md` ueber Profil 2 gerendert werden; Referenzen sind 80 konservativ und 125 Thorsten-Solo fuer C#/.NET. / After implementation, Profile 2 must render `docs/project-statistics.md`; baselines are 80 conservative and 125 Thorsten-solo for C#/.NET. | Renderer und `--check-only` erst nach Implementierung ausfuehren. / Run renderer and check-only only after implementation. |
| Documentation Impact | Applicable | Partly Fulfilled | Genau eine Entscheidung: `UpdateRequired`; das eingefrorene Inventar umfasst den Pending-Closeout-Anker. Der spaetere Drei-Pfad-Delta erhaelt einen vollstaendigen Documentation-Re-Review, ohne eine zweite Entscheidung zu erzeugen. / Exactly one UpdateRequired decision includes the Pending closeout anchor; the later three-path delta receives a complete documentation re-review without creating a second decision. | Feature-lokale Schema-1.1-Evidence und Closeout-Re-Review stehen bis zur Umsetzung aus. / Feature evidence and closeout re-review remain pending. |
| AEPS-Rueckfuehrung / AEPS feedback | Applicable | Not Fulfilled | Nach der wesentlichen Implementierung/Completion ist ein Ledger-Check plus Finding- oder begruendetes No-change-Receipt erforderlich. / After material implementation/completion, a ledger check plus finding or justified no-change receipt is required. | Kein Level-0-/Preset-Handoff in diesem Scope; neu bei belastbarer portabler Evidence. / No level-0 or preset handoff in scope; re-evaluate for stable portable evidence. |
| Lastenheft-Archivierung und akzeptierter Snapshot / Intake archival rename and accepted snapshot | Applicable | Partly Fulfilled | `intake-lifecycle.json` Schema 1.1 bewahrt den exakten Record und bindet zusaetzlich alle 14 geordneten Ziel-/Receipt-/Review-Snapshots. Der aktuelle qualifizierte Implement-Zustand ist gruen; Rename bleibt unveraendert terminal. / Schema 1.1 preserves the exact record and binds all fourteen ordered evidence snapshots; the qualified Implement state passes and the rename remains terminal. | Requirements Maintainer; Rename und `terminal-rename` stehen weiter aus; jede Stage-, Status-, Gate-, Pfad-, Branch-, Run-, Hash-, Receipt-, Review- oder Leaf-Drift schliesst fail-closed. / Rename remains pending; any bound drift fails closed. |
| Autonomous `MergeAndSync` | Applicable | Partly Fulfilled | Der Feature-PR bleibt auf dem terminalen Head unveraendert. Nach Merge/Sync darf nur `codex/001-programmquellen-baseline-closeout` genau Tasks, State und Causal Evidence aendern; sein einzelner Commit beendet T066 lokal. Spaetere PR-Publikation wird extern belegt. / The feature PR remains immutable; after merge/sync only the pre-named exact three-path closeout branch may persist completion, with later publication reported externally. | Vor jedem Commit, Push, Merge und Bypass Authority und Exact Head fail-closed neu pruefen. / Revalidate authority and exact head before each irreversible action. |

### Dokumentationswirkung / Documentation Impact

- **Entscheidung / Decision**: `UpdateRequired`.
- **Kanonische fachliche Quelle / Canonical domain source**: logisch ausschliesslich `requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md`, gebunden durch das aktuelle Ready-Single-Review; nach dem terminalen Rename wird dieselbe byteidentische Quelle nur ueber `intake-lifecycle.json` am exakten Archivpfad aufgeloest. / The sole logical canonical source remains the Ready-reviewed original target and resolves to the byte-identical archived path only through the lifecycle record after rename.
- **Vollstaendiges geplantes Dokumentinventar / Complete planned document inventory**: die sechs Domain-Dateien; alle tatsaechlich gelieferten Feature-Artefakte einschliesslich Lifecycle-Datensatz und vorbenanntem `causal-closeout-evidence.json`; genau eine Documentation-Impact-Evidence; AEPS und Statistik; ausserdem Original- und Archivpfad als kausale Rename-Transition. Die normale Kandidatenmenge wird vor Stage eingefroren. Der spaetere Closeout aendert exakt Tasks, State und den bereits reviewten Anker und erhaelt einen Documentation-/Public-Content-Re-Review. / The complete inventory includes the Pending causal anchor; the later exact three-path delta receives documentation and public-content re-review.
- **Leserpfad / Reader path**: Source Pack -> Constraint Register -> Findings Ledger -> Coverage Matrix -> Glossary -> Authority/Stop Gates -> genau eine sichere naechste Aktion. / Source Pack through authority gates to exactly one safe next action.
- **Navigation / Navigation**: Querverweise innerhalb dieses bestehenden Leserpfads werden ergaenzt oder korrigiert; kein neuer Repository-Einstieg. / Cross-links within the existing reader path are added or corrected; no new repository entry point.
- **Dokumentklasse und Sprache / Document class and language**: aktive semantische Level-2-Dokumentation, inline DE-first/EN-second, keine Partnerdateien. / Active semantic level-2 documentation, inline German-first/English-second, no companion files.
- **Plattform-/Beispielnachweis / Platform/example proof**: textorientierter Markdown-Review; plattformspezifische Produktbeispiele sind `N/A`. / Text-first Markdown review; platform-specific product examples are `N/A`.
- **Distribution und Sync / Distribution and sync**: repository-lokale `sourceOnly`-Aussagen ohne Home-Sync oder Level-0-Aenderung; Git-Default-Branch-Sync gehoert nur zum spaeteren `MergeAndSync`-Closeout. / Repository-local `sourceOnly` statements without Home Sync or level-0 changes; Git default-branch sync belongs only to later closeout.
- **Generated Update**: Der neue getrackte Python-Vertrag und sein Test sind eingebettete Skripte. `docs/scripts/embedded-scripts.md` wird nach Preview erzeugt und nennt den `causal-closeout`-Modus samt Eingabe `causal-closeout-evidence.json`; `docs/scripts/reference.md` bleibt unveraendert. / The generated embedded-script inventory names the causal-closeout mode and its evidence input; the canonical script reference remains unchanged.
- **Evidence**: `specs/001-programmquellen-baseline/documentation-impact-evidence.json` wird in der Umsetzungsphase erzeugt und mit beiden vorhandenen Validatoroberflaechen geprueft. / The feature-local evidence JSON is created during implementation and checked with both existing validator surfaces.

## Delta-Audit / Delta Audit

| Artefakt / Artefact | Bewahren / Preserve | Notwendige Aenderung / Necessary change |
|---|---|---|
| `source-pack.md` | Quellenrang, bestehende fachliche Rollen, Decisions und Supersession. / Source precedence, existing domain roles, decisions, and supersession. | `SRC-163` bis `SRC-167` als einzelne Inventurzeilen; alle 23 IDs exakt einmal im Inventurfeld; fehlende EN-Paritaet und Leserpfad ergaenzen. / Split the range into individual inventory rows; ensure all 23 IDs occur exactly once in the inventory field; complete English parity and reader path. |
| `constraint-register.md` | `CON-01` bis `CON-25` und ihre fachlichen Grenzen. / Existing constraints and boundaries. | EN-Paritaet fuer Evidence-Spalte, konsistente Begriffe und Text-first/A11Y-Pruefbarkeit; keine neuen Produktconstraints. / Complete English evidence, consistent terms, and text-first/accessibility reviewability; no new product constraints. |
| `review-findings-ledger.md` | `RF-01` bis `RF-21`, Severity, Owner-Intention, Status und Restluecken. / Existing findings, severity, ownership intent, status, and gaps. | Alle Pflichtfelder je Einzelzeile vollstaendig zweisprachig; direkte META-LH-01-Menge nicht durch Bereichs- oder Sammelnotation verwischen. / Make every required field fully bilingual per individual row; do not obscure the direct META-LH-01 set through ranges or aggregates. |
| `coverage-matrix.md` | Bestehende Owner-Beziehungen, `Covered`-Semantik und Nicht-Implementierungsgrenze. / Existing ownership relations, coverage meaning, and non-implementation boundary. | Je eine pruefbare Zeile fuer alle 23 Source-IDs und `RF-01..RF-21`; `SRC-ES-01` und `SRC-163..167` aufnehmen; exakte direkte Menge `RF-01`, `RF-04`, `RF-11..RF-17`, `RF-21` ausweisen. / Add one verifiable row per source and finding, including omitted IDs; state the exact direct set. |
| `glossary.md` | Vorhandene Begriffe und kurze Tabellenform. / Existing terms and concise table. | Fehlende englische Erklaerungen vervollstaendigen; Authority, Evidence, Receipt, Coverage und Stop-Gate fuer Erstlesende konsistent halten. / Complete missing English explanations and keep core first-reader terms consistent. |
| `authority-and-stop-gates.md` | G-00 bis G-08, fail-closed-Prinzip und globale G-05-Regel. / Existing gates, fail-closed principle, and global G-05 rule. | Tabelleninhalte vollstaendig DE/EN; G-01/G-05/G-06 mit erlaubter Aktion, Stop, Evidence und menschlicher Entscheidung praezisieren; G-06 nicht als Produktcode-Autoritaet lesen lassen; aktuellen META-LH-01-Start und spaetere `MergeAndSync`-Grenze erklaeren. / Complete bilingual table content and clarify the evidence/authority boundaries without granting product-code authority. |

## Umsetzungs- und Validierungsstrategie / Implementation and Validation Strategy

1. Vor jedem Edit Branch, Run-State und Checkpoint pruefen. `input-bindings` loest META-LH-01 deterministisch auf. Vor Implement fuehrt jede Oberflaeche generische Receipt-/Review-Frische aus; im exakt qualifizierten Implement-Zustand validiert sie stattdessen den vollstaendigen 14-Ziel-Snapshot und fuehrt ihre Run-State- und Review-Oberflaeche weiter. / Before each edit, validate branch, state, checkpoint, and the phase-qualified lifecycle-aware input bindings.
2. `global-ready` unmittelbar vor Tasks, jedem Analyze-Lauf und Implement sowie archivbewusst nach dem Rename ausfuehren. Vor Implement laufen beide installierten Receipt-/Review-Paare fuer alle 14; nur im exakten qualifizierten Implement-Zustand ersetzt der vollstaendige Snapshot die Receipt-Quellenfrische, nie die Review-Oberflaechen. / Run the fourteen-target gate at every named boundary; only the exact qualified Implement state substitutes the snapshot for receipt source freshness.
3. Die sechs Domain-Dateien in Leserpfad-Reihenfolge minimal bearbeiten und danach den `domain`-Modus sowie die isolierten Contract-Tests ausfuehren. / Minimally edit the six files and run domain validation and isolated tests.
4. Nach Preview den eingebetteten Skriptkatalog erzeugen und check-only pruefen; erst danach Homogeneity als Maschinen-Strukturcheck ausfuehren. Getrennte unabhaengige Rollen erfassen semantische und Accessibility-Evidence; `review-evidence --kind semantic` und `--kind accessibility` pruefen die jeweilige Vollstaendigkeit. / Keep machine structure, semantic review, and accessibility review as three separate proof classes.
5. Nach wesentlicher Umsetzung genau einen strukturierten AEPS-Receipt als Finding oder begruendetes NoChange erfassen; bei `Finding` muss der Validator den vollstaendigen gebundenen Ledger-Abschnitt pruefen, bei `NoChange` bleibt das Ledger unveraendert. / Capture exactly one bounded AEPS outcome and validate every mandatory ledger field for a Finding.
6. Statistik rendern und mit Bash/PowerShell check-only pruefen. / Render and check statistics.
7. `causal-closeout-evidence.json` bereits als `Pending`-Anker in den normalen Kandidaten aufnehmen. Erst nachdem alle anderen Lieferpfade existieren, die Public-Content- und Documentation-Impact-Evidence-Dateien erzeugen und dann die erste Sollmenge einfrieren. / Include the Pending causal-closeout anchor in the normal candidate before freezing candidate set one.
8. Secret-Scanner als Mustersuche ausfuehren. Gegen Sollmenge eins die Public-Content-Review und genau einen schema-1.1-Documentation-Impact-Eintrag vervollstaendigen. / Run secret-pattern scans and complete public-content and single Documentation Impact evidence against candidate set one.
9. Die Kandidatenmenge erneut ableiten, bytegleich mit Sollmenge eins vergleichen und `candidate-fixpoint` ausfuehren. Public-Content- und Documentation-Impact-Validatoren laufen erst nach diesem stabilen Fixpunkt; jede neue oder fehlende Datei beginnt den Fixpunkt neu. / Re-derive candidate set two, require byte equality with set one, and pass candidate-fixpoint before validating both evidence classes.
10. Nur die stabile normale Sollmenge stagen; `candidate` gleicht Porcelain, untracked, staged, unstaged und `git diff --cached --check` ab. Fremde Aenderungen bleiben ungestaged und unberuehrt. / Stage only the stable normal candidate and validate it exactly.
11. Aktuelle Autoritaet fail-closed pruefen und den normalen Kandidaten committen. Danach bei sauberer Feature-Schreibflaeche `scripts/rename-lastenheft.sh` ausfuehren; dies ist die letzte Polish-Aktion und erzeugt den letzten Feature-Branch-Commit. `terminal-rename` beweist genau einen byteidentischen R100-Rename, den exakten Trailer und keine Stage-Reste. / Commit the normal candidate first, then let the rename script create and verify the final branch commit.
12. Erst den danach unveraenderlichen terminalen Head pushen, PR erstellen/aktualisieren und `headRefOid` binden. Alle Checks, Review-Decision, Threads, Execution Record und providerneutrale Exact-Head-Evidence beziehen sich ausschliesslich auf diesen Head. / Push and review only the immutable terminal head.
13. Nach Feature-Merge und Fast-forward-Sync genau `codex/001-programmquellen-baseline-closeout` von synchronisiertem `main` erzeugen. Archivbewusst final validieren, exakt Tasks/State/Causal Evidence aktualisieren, `causal-closeout` und beide State-Validatoren ausfuehren und genau diese drei Pfade committen; dies ist der letzte lokale Akt von T066. / After feature merge and sync, create only the pre-named closeout branch, validate, update exactly three paths, and commit them as the last local act of T066.
14. Den unveraenderten Closeout-Head pushen, separat unabhaengig reviewen, alle Checks und null actionable Threads verlangen, normal oder nur beim Approval-only-Blocker administrativ mergen, Branch bereinigen, `main...origin/main = 0 0` und sauberen Worktree extern belegen. Keine neue Task-Checkbox und keine Selbstreferenz erzeugen. / Publish and merge the immutable closeout head through the bounded provider flow and report its PR/merge SHA externally.

## Aufloesbare Validierungsbefehle / Resolved Validation Commands

Die vollstaendigen, kopierbaren Befehle und erwarteten Ergebnisse stehen in [quickstart.md](quickstart.md). Die Gate-Bindung steht in `autonomous-run-gate-requirements.json`. Verwendet werden ausschliesslich im Repository vorhandene Validatoren oder lokal nachgewiesene Standardwerkzeuge: / Full copy-ready commands and expected results are in the quickstart; gate binding is in the feature-local requirements JSON. Only repository-provided validators or locally confirmed standard tools are used:

- `python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` mit den gebundenen expliziten Modi / with the bound explicit modes
- `python3 specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py`
- `python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . terminal-rename`
- `python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . causal-closeout`
- `validate-autonomous-gate-evidence.sh/.ps1` mit spaeterer exact-head Evidence / with later exact-head evidence
- `scripts/check-homogeneity.sh/.ps1`
- `scripts/render-script-reference.ps1` mit `-WhatIf`, Schreib- und `-CheckOnly`-Lauf / with preview, write, and check-only runs
- `scripts/scan-agent-secrets.sh/.ps1` und `gitleaks dir`
- `scripts/validate-documentation-impact.sh/.ps1`
- `scripts/render-project-statistics.sh/.ps1`
- `git status --porcelain=v1 -z`, `git diff --cached --name-only -z` und `git diff --cached --check` innerhalb des Kandidatenmodus / inside candidate mode
- spaeter fuer den autorisierten Closeout / later for authorised closeout: `gh pr checks`, `gh pr view`, paginiertes `gh api graphql` fuer Threads, `gh pr merge`, `git pull --ff-only`

## Projektstruktur / Project Structure

### Feature-Dokumentation / Feature documentation

```text
specs/001-programmquellen-baseline/
├── spec.md
├── checklists/
│   ├── requirements-quality.md
│   └── implementation-validation.md       # spaetere Umsetzung / later implementation
├── autonomous-run-state.json
├── autonomous-run-gate-requirements.json
├── intake-lifecycle.json                 # ein Pfaduebergang plus 14-Ziel-Snapshot / one transition plus fourteen-target snapshot
├── plan.md
├── plan-review.md                       # historisches R1 / historical R1
├── plan-review-r2.md                    # erneutes unabhaengiges Review / independent re-review
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── baseline-validation-contract.md
│   ├── validate_meta_lh01.py             # read-only Workflow-Evidence / workflow evidence
│   ├── test_validate_meta_lh01.py        # nur temporaere Fixtures / temporary fixtures only
│   └── candidate-paths.json              # maximale Pfadgrenze / maximum path boundary
├── documentation-impact-evidence.json    # spaetere Umsetzung / later implementation
├── semantic-review-evidence.json         # getrenntes Semantik-Review / separate semantic review
├── accessibility-review-evidence.json    # getrenntes A11Y-Review / separate A11Y review
├── public-content-review-evidence.json   # getrenntes Public-Content-Review / separate public-content review
├── causal-closeout-evidence.json         # normal Pending, im Closeout Completed / Pending then Completed
└── tasks.md                              # /speckit-tasks, nicht diese Phase / not this phase
```

### Fachliche Liefer- und Evidence-Pfade / Domain delivery and evidence paths

```text
requirements/baseline/
├── source-pack.md
├── constraint-register.md
├── review-findings-ledger.md
├── coverage-matrix.md
├── glossary.md
└── authority-and-stop-gates.md

docs/aeps/
├── findings-ledger.md                    # nur bei neuer Evidence / only for new evidence
└── receipts/meta-lh-01-programmquellen-implementation.md
                                           # Evidence oder No-change / evidence or no-change

docs/
├── scripts/embedded-scripts.md           # generiertes Inventar / generated inventory
├── project-statistics.config.json        # unveraenderte kanonische Konfiguration / unchanged canonical config
└── project-statistics.md                 # nach Implementierung gerendert / rendered after implementation
```

**Strukturentscheidung / Structure decision**: Dokumentations- und Workflow-Evidence-Struktur ohne `src/`, Produkt-`tests/`, Scaffold oder Produkt-Runtime. Markdown beschreibt die Proof-Grenze; der feature-lokale Standardbibliothek-Python-Vertrag fuehrt sie read-only aus. Beides ist keine Produkt-API. / Documentation and workflow-evidence structure without product source, tests, scaffold, or runtime. Markdown describes the proof boundary and the feature-local standard-library contract executes it read-only; neither is a product API.

## Post-Design-Verfassungspruefung / Post-Design Constitution Re-check

Bestanden: Research und Design fuegen keine Produkttechnologie, Architektur, Dependency, Produkt-Runtime, Preset-/Level-0-Aenderung oder Arbeit an einem anderen Intake hinzu. Die Constitution-konforme Archivierung bleibt terminaler Feature-Head. Der getrennte, exakt drei Pfade umfassende Closeout-Commit persistiert erst danach tatsaechliche Fakten und beansprucht seine eigenen Publikationsfakten nicht. Der Standardbibliothek-Python-Vertrag ist begrenzte Workflow-Evidence mit 43 temporaeren Fixtures. / Passed: archival remains the terminal feature head and the later exact three-path closeout persists only causal facts without self-reference.

## Installierte Preset-Versionsdelta-Pruefung / Installed Preset Version Delta Audit

Der in `autonomous-run-state.json` bereits gebundene Resume-Audit wurde erneut gelesen. Installiert sind `security-governance` 0.6.2, `architecture-governance` 0.5.2, `isaqb-architecture-governance` 0.2.2, `a11y-governance` 0.4.3, `cross-platform-governance` 0.2.2, `agent-parity-governance` 0.4.2, `model-routing-governance` 0.1.4, `intake-authoring-governance` 0.3.1, `intake-review-governance` 0.2.1, `intake-sequencing-governance` 0.2.3, `autonomous-run-governance` 0.3.6 und `parallel-autonomous-run-governance` 0.2.6. Gegenueber der Constitution-Matrix sind die dort genannten Governance-Presets jeweils auf einer neueren installierten Patch-Version; die vier operativen/optionalen Presets sind nur Laufkontext. Disposition: C-001 wird durch diese minimale Feature-Migration geloest; keine Preset-Version wird geaendert, installiert, herabgestuft oder in Feature-Anforderungen festgeschrieben. / The resume audit records the named installed versions. The matrix-bound presets are installed at newer patch versions; the operational/optional presets remain run context only. C-001 is resolved locally without changing or pinning any preset version.

## Komplexitaetsverfolgung / Complexity Tracking

Keine Verfassungsverletzung; Tabelle entfaellt. / No constitution violation; table omitted.
