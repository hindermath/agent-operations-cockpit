# Unabhaengiges Plan-Review: Programmquellen-Baseline / Independent Plan Review: Program Sources Baseline

**Review-Datum / Review date**: 2026-08-09
**Review-Scope**: `specs/001-programmquellen-baseline`
**Endurteil / Final verdict**: **NeedsRemediation**

## Kurzurteil / Executive Assessment

Die fachliche Scope-Grenze ist grundsaetzlich treu: Die geplante Lieferung bleibt bei sechs Level-2-Governance-Dokumenten sowie begrenzter Workflow-, Documentation-Impact-, AEPS- und Statistik-Evidence. Produktcode, Produktarchitektur, Scaffold, Preset-Promotion und Level-0-Mutation bleiben ausgeschlossen. Die deklarierte Sollmenge von 23 Quellen, `RF-01` bis `RF-21` und die direkte zehnteilige META-LH-01-Menge sind zwischen Spezifikation, Vertrag und Datenmodell konsistent.

The domain scope is fundamentally faithful: delivery remains limited to six level-2 governance documents and bounded workflow, Documentation Impact, AEPS, and statistics evidence. Product code, product architecture, scaffolding, preset promotion, and level-0 mutation remain excluded. The declared 23-source set, `RF-01` through `RF-21`, and the direct ten-item META-LH-01 set are consistent across the specification, contract, and data model.

Der Plan ist dennoch nicht ausfuehrungsbereit. Drei Critical- und vier High-Befunde betreffen fail-closed Gates, deren vorhandene Befehle den jeweils behaupteten `requiredScope` nicht beweisen. Ein Markdown-Vertrag ist keine ausfuehrbare Pruefung; eine Token-Uebereinstimmung im Exact-Head-Validator beweist nicht, dass der protokollierte Befehl den fachlichen Scope tatsaechlich geprueft hat.

The plan is not execution-ready. Three Critical and four High findings affect fail-closed gates whose existing commands do not prove their declared `requiredScope`. A Markdown contract is not an executable check, and token matching in the exact-head validator does not prove that the recorded command actually tested the required domain scope.

## Verifizierte Ausgangslage / Verified Starting Point

- Die SHA-256-Werte des Intake, des Ready-Single-Reviews und des Authoring Receipt stimmen mit `spec.md:10-12` und `autonomous-run-state.json:11-23` ueberein. / The three accepted SHA-256 values match the spec and run state.
- `validate-autonomous-run-state.sh/.ps1`, `validate-intake-authoring-receipt.sh/.ps1` und `validate-intake-review-result.sh/.ps1` bestehen aktuell. / The Bash and PowerShell state, receipt, and review validators currently pass.
- Der Checkpoint `b8eb0735b2a7c46a65712d2e280242c85f8c1d64` ist Vorfahr des aktuellen `HEAD`. / The checkpoint is an ancestor of the current head.
- Alle in `plan.md:104-113` genannten lokalen Werkzeuge und Skriptdateien existieren in diesem Clone. Ihre Existenz allein reicht jedoch nicht als Scope-Nachweis. / All locally named tools and script files exist in this clone, but existence alone is not scope proof.

## Findings

### C-01 — Critical — Der zentrale Domain-Gate-Nachweis ist unvollstaendig und nicht stabil an einen ausfuehrbaren Vertrag gebunden

**Orte / Locations**: `autonomous-run-gate-requirements.json:44-60`; `quickstart.md:65-135`; `contracts/baseline-validation-contract.md:18-83`; `plan.md:87-92`; `research.md:29-38`.

**Befund / Finding**: `META01-G03-domain-contract` nennt `python3` und das Markdown-Vertragsdokument als Tokens, aber keinen stabil benannten ausfuehrbaren Validator. Der Inline-Python-Block in `quickstart.md` ist zwar ausfuehrbar, er beweist den deklarierten Scope nicht vollstaendig:

- `requiredScope` behauptet die Pruefung aller sechs Domain-Pfade, aber Gate-Tokens und Python-Code lesen weder `constraint-register.md` noch `glossary.md`;
- die sieben Pflichtfelder jeder Quelle werden nicht geprueft;
- positive und negative Evidence sowie Status und Restluecke werden nur als zusammengefasste Tabellenzellen beziehungsweise durch ein beliebiges `" / "` behandelt, nicht als getrennte Pflichtwerte;
- `Uncovered` fuer blocking Findings und die vollstaendige Coverage-Semantik werden nicht deterministisch ausgeschlossen;
- die Authority-Pruefung sucht nur einzelne Texttokens und prueft keine Gate-Zeile mit erlaubter Aktion, Stop-Bedingung, Evidence, menschlicher Entscheidung und genau einer sicheren naechsten Aktion;
- negative Vertragsfaelle und erwarteter sauberer Fehlerkanal fehlen.

`META01-G03-domain-contract` names `python3` and the Markdown contract as tokens but no stable executable validator. The inline Python block is executable, yet it omits two of the six bound files and does not fully validate source fields, separated finding fields, blocking coverage, gate-row structure, or negative cases.

**Erforderliche Remediation / Required remediation**: G03 muss an genau einen kopierbaren, read-only ausfuehrbaren Vertrag gebunden werden: entweder den vollstaendigen Inline-Python-Block mit stabilen eindeutigen Command-Tokens und Hash-Bindung oder einen ausdruecklich als Workflow-Evidence autorisierten feature-lokalen Validator. Er muss alle sechs Pfade, exakt 23/21/10 IDs, alle Pflichtfelder, `Covered`-/blocking-Semantik, G-01/G-05/G-06-Struktur, erwartete Exitcodes, genau eine PASS-Ausgabe und einen sauberen Fehlerkanal pruefen. Mindestens je ein negativer Fall fuer fehlende/duplizierte Source, fehlendes RF-Feld, falsche direkte Ownership und unvollstaendiges Gate ist vorzusehen. Das fuegt keine Produktfunktion, kein Preset und keine Level-0-Aenderung hinzu.

### C-02 — Critical — Die Exact-Head-Evidence kann mit der beschriebenen Reihenfolge nicht erzeugt oder gueltig gehalten werden

**Orte / Locations**: `autonomous-run-gate-requirements.json:175-193`; `quickstart.md:241-275`; `plan.md:97-98`; `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh:60-65,175-236`; `.specify/presets/autonomous-run-governance/commands/speckit.autonomous.md:94-99,106-137`.

**Befund / Finding**:

1. `quickstart.md` behauptet, die temporaere Evidence-Datei werde erzeugt, ruft aber nur den read-only Validator auf; dieser verlangt eine bereits vorhandene Datei und erzeugt sie nicht.
2. `reviewed_head=$(git rev-parse HEAD)` wird vor dem in Abschnitt 10 beschriebenen Commit ermittelt. Der folgende Commit erzeugt einen neuen Head und macht die Evidence fuer den Lieferkandidaten ungueltig.
3. G10 vermischt Vor-Merge-Tatsachen mit `gh pr merge`, Default-Branch-Synchronisierung und finaler Validierung. Post-Merge-Fakten koennen nicht in einer vor dem Merge validierten Primary-Zeile fuer den aktuellen PR-Head bewiesen werden.
4. `gh pr view` fragt keinen handlungsrelevanten Review-Thread ab; keine dargestellte Bedingung vergleicht `headRefOid` fail-closed mit dem erwarteten Head.
5. Der Gate-Evidence-Validator prueft lediglich Hash, Head, Vollstaendigkeit und Token-Teilstrings. Er erzeugt keine Provider-Evidence und verifiziert nicht, ob das protokollierte Kommando den behaupteten Scope ausgefuehrt hat.

The quickstart validates but never creates the evidence file, derives the reviewed head before a later commit changes it, mixes pre-merge and post-merge facts in one gate, and does not prove actionable-thread convergence or a fail-closed PR-head comparison.

**Erforderliche Remediation / Required remediation**: Die Reihenfolge muss kausal neu gefasst werden: exakten Kandidaten stagen und pruefen; autorisiert committen und pushen; PR-Head, Checks und Reviews einschliesslich handlungsrelevanter Threads konvergieren; Commands und Runner aus Workflow-Definitionen oder Logs ableiten; die temporaere Gate-Evidence fuer genau diesen PR-Head tatsaechlich erzeugen; Bash- und/oder PowerShell-Validator aufrufen; erst dann mergen. Merge, Branch-Cleanup, Default-Branch-Sync, Post-Merge-Aktionen und finale Validierung gehoeren in die getrennten schema-1.1-Closeout-Felder beziehungsweise den vorbenannten kausalen Closeout, nicht in die Pre-Merge-Primary-Zeile.

### C-03 — Critical — Die globale G-05-Sperre besitzt vor nachgelagerten Phasen keinen aktuellen ausfuehrbaren 14er-Nachweis

**Orte / Locations**: `AGENTS.md:189-213`; `requirements/baseline/authority-and-stop-gates.md:18-44`; `spec.md:178-184`; `plan.md:89`; `autonomous-run-gate-requirements.json:4-42`.

**Befund / Finding**: Die Spezifikation verlangt eine neue G-05-Pruefung vor jedem nachgelagerten Spec-Kit-Schritt. Die Gate-Requirements validieren bei G01/G02 jedoch nur Run-State, META-LH-01-Receipt und META-LH-01-Single-Review. Es gibt keinen benannten Befehl und keinen gebundenen Evidence-Pfad, der fuer alle 14 aktiven Intakes gleichzeitig Zielpfad, normalisierten Zielhash, aktuelles Authoring Receipt, nicht-supersediertes `Ready`-Single-Review sowie Bash- und PowerShell-Erfolg beweist. Eine fruehere Textzusammenfassung in einem Routing-Output ist kein aktueller fail-closed Nachweis.

The specification requires G-05 revalidation before every downstream phase, but the gate requirements validate only the current feature's three bindings. No executable, bound 14-intake proof is declared.

**Erforderliche Remediation / Required remediation**: Vor Tasks, Analyze und Implement muss ein eigener `Applicable`-Gate-Eintrag einen reproduzierbaren read-only Befehl und Evidence-Pfad fuer alle 14 Einzelreviews und Receipts binden. Der Nachweis muss exakte Zielmenge, aktuelle normalisierte Hashes, `Ready`/`Single`, Supersession, beide Validatoroberflaechen und META-LH-01 als erstes Ziel pruefen. Jede Drift muss die Fortsetzung blockieren.

### H-01 — High — G01/G02 pruefen nicht alle drei im Run-State akzeptierten Artefakthashes

**Orte / Locations**: `autonomous-run-gate-requirements.json:4-42`; `quickstart.md:15-63`; `.specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh:149-167`.

**Befund / Finding**: Der Run-State-Validator prueft fuer `acceptedArtifacts` nur relative Pfade, Duplikate und SHA-256-Format; er liest die Dateien nicht und vergleicht ihre Inhalte nicht. Receipt- und Review-Validator pruefen ihre eigenen Ziel-/Request-Bindungen, aber nicht die rohen SHA-256-Werte der Receipt- und Review-Datei gegen `autonomous-run-state.json`. Die separaten `shasum`-/`Get-FileHash`-Befehle in `quickstart.md:39-61` sind nicht in G01/G02 gebunden.

The run-state validator checks accepted-artifact shape, not file contents. The explicit hash commands exist in the quickstart but are absent from the gate requirements.

**Erforderliche Remediation / Required remediation**: Die Bash- und PowerShell-Gates muessen die drei konkreten Datei-Hashvergleiche als erforderliche Commands/Tokens aufnehmen und deren Exitcode sowie erwartete Ausgabe belegen. Der Run-State-Schema-Pass bleibt zusaetzlich erforderlich, darf aber nicht als Inhaltsbindung ausgegeben werden.

### H-02 — High — G04, G05 und G07 behaupten mehr als ihre Commands beweisen

**Orte / Locations**: `autonomous-run-gate-requirements.json:62-99,117-134`; `quickstart.md:137-175,193-204`; `scripts/scan-agent-secrets.sh:48-69,72-104,121-215`; `docs/aeps/README.md:92-133,175-190`.

**Befund / Finding**:

- G04: Homogeneity prueft Struktur, aber nicht DE/EN-Gleichwertigkeit, CEFR B2, fachliche Wahrheit oder semantische WCAG-Qualitaet. Der Pfad zur spaeteren Checkliste ist kein ausfuehrbarer Befehl.
- G05: `gitleaks` und der Repository-Scanner pruefen Secret-Muster; der Scanner fokussiert Agentenverzeichnisse und den aktuellen Git-Diff. Sie beweisen weder vollstaendige Public-Suitability noch unnoetige personenbezogene Daten auf allen behaupteten Pfaden. Das `rg`-Muster ist nur eine begrenzte Heuristik.
- G07: `rg` kann das Vorhandensein einzelner Tokens melden, prueft aber weder den AEPS-Deduplizierungsschluessel noch genau einen Finding-/No-change-Ausgang, Pflichtfelder, Maturity-Grenze oder den Ausschluss von Preset-/Level-0-Handoff.

G04, G05, and G07 overstate what homogeneity, secret-pattern scans, a checklist path, and `rg` can prove.

**Erforderliche Remediation / Required remediation**: Automatische und semantische Gates sind zu trennen. Fuer den unabhaengigen Review muss ein ausfuehrbarer Evidence-Check pruefen, dass jede geforderte Datei und jedes Kriterium von einer benannten unabhaengigen Rolle mit `Pass`/`Fail` und Begruendung bewertet wurde; der `requiredScope` darf nur diesen aufgezeichneten Nachweis, nicht maschinell unbeweisbare Semantik behaupten. Public-Content-/PII-Review braucht eigene dokumentierte Scope-Coverage. AEPS braucht eine deterministische Receipt-/Ledger-Pruefung gegen den Vertrag oder einen engeren, ehrlich durch `rg` beweisbaren Scope. Das Receipt-Datum darf erst zum tatsaechlichen Erfassungsdatum festgelegt werden.

### H-03 — High — Der Documentation-Impact-Gate beweist weder genau einen Eintrag noch den vollstaendigen geplanten Dokumentumfang

**Orte / Locations**: `plan.md:64-74`; `autonomous-run-gate-requirements.json:100-115`; `quickstart.md:177-191`; `scripts/validate-documentation-impact.ps1:62-79,107-152,183-188`; `spec.md:119`.

**Befund / Finding**: G06 verlangt genau einen Eintrag. Der vorhandene Validator akzeptiert jedoch jede nichtleere `entries`-Liste und meldet sogar die beliebige Anzahl als PASS. Ausserdem nennt `plan.md:68` nur die sechs Domain-Dateien als betroffene aktuelle Dokumente, obwohl der Plan feature-lokale Workflow-/Evidence-Dokumente, ein AEPS-Receipt beziehungsweise Ledger und `docs/project-statistics.md` schreibt. Die kanonische Quelle driftet zwischen dem Ready-geprueften Intake in `spec.md:119` und `spec.md` selbst in `plan.md:67`.

G06 claims exactly one entry, while the validator permits any positive entry count. The planned document inventory and canonical source are also inconsistent.

**Erforderliche Remediation / Required remediation**: Die Evidence muss schema 1.1 verwenden; ein zusaetzlicher ausfuehrbarer Count-Check muss `.entries` exakt auf eins begrenzen. Der eine Eintrag muss alle tatsaechlich geplanten Dokumentpfade beziehungsweise bewusst getrennten generierten Evidence-Pfade abdecken. Kanonische fachliche Quelle und Workflow-Ableitung sind zwischen Spec, Plan und Evidence eindeutig und widerspruchsfrei festzulegen.

### H-04 — High — Gespeicherter Liefermodus und historische Authority werden als aktuelle Remote-Autoritaet behandelt

**Orte / Locations**: `spec.md:95,161-170`; `plan.md:61-62,98`; `autonomous-run-state.json:6-7`; `.specify/presets/autonomous-run-governance/commands/speckit.autonomous.md:113-137`.

**Befund / Finding**: Der Run-State speichert `MergeAndSync`, und historische Receipt-/Spec-Texte dokumentieren eine fruehere Freigabe. Ein gespeicherter Delivery-Modus ist nach dem Autonomous-Vertrag aber keine aktuelle Berechtigung. Der aktuelle Benutzerauftrag autorisiert ausschliesslich dieses Review und verbietet Implementierung, Commit und Remote-Aktionen. G10 erwaehnt zwar „current authority“, doch Plan und Spec bezeichnen den Gesamtablauf weiterhin als aktuell autorisiert und `authorityRevalidationRequired` steht auf `false`.

The stored `MergeAndSync` mode and historical authority evidence are not current remote authority. The current request authorizes this review only and explicitly prohibits implementation, commits, and remote actions.

**Erforderliche Remediation / Required remediation**: `MergeAndSync` ist im Plan als beabsichtigter, aber vor jeder irreversiblen Stufe neu zu autorisierender Modus zu behandeln. Vor Commit, Push, PR-Erstellung, Merge, optionalem Bypass und Default-Branch-Sync muss aktuelle ausdrueckliche Authority separat geprueft und gebunden werden. Bis dahin gilt fuer die aktuelle Arbeit nur die Review-Schreibflaeche; der Run-State darf keine Berechtigung ableiten.

### M-01 — Medium — Der Exact-Path-Diff kann untracked oder falsch gestagte Pfade nicht vollstaendig ausschliessen

**Orte / Locations**: `autonomous-run-gate-requirements.json:152-173`; `quickstart.md:221-239,263-275`; `plan.md:97-98`.

**Befund / Finding**: `git diff --check` und `git diff -- <paths>` zeigen untracked Dateien nicht. `git status --short` listet sie, beweist aber ohne maschinenlesbaren Allowlist-Vergleich nicht, dass der spaetere Kandidat exakt und vollstaendig ist. Die nur textlich erwaehnte Staging-Pruefung besitzt keinen kopierbaren exakten Pfadinventar-Befehl.

`git diff` omits untracked files, and status output alone does not prove an exact candidate inventory.

**Erforderliche Remediation / Required remediation**: Vor jedem autorisierten Commit ist ein expliziter Allowlist-Vergleich fuer `git diff --cached --name-only`, `git status --porcelain=v1` und die erwarteten untracked/unstaged Pfade vorzusehen. Danach muessen `git diff --cached --check` und der staged Inhalt geprueft werden. Fremde Index- und Worktree-Aenderungen bleiben unangetastet.

## Gate-fuer-Gate-Ausfuehrbarkeitsurteil / Gate-by-Gate Executability Verdict

| Gate | Urteil / Verdict | Begruendung / Reason |
|---|---|---|
| `META01-G01-input-binding-bash` | NeedsRemediation | Commands exist, but the three accepted file hashes are not all compared to run-state values. |
| `META01-G02-input-binding-powershell` | NeedsRemediation | Same proof gap as G01; schema validity is not content binding. |
| `META01-G03-domain-contract` | NeedsRemediation | The Markdown contract is non-executable and the inline Python proof omits required files and invariants. |
| `META01-G04-bilingual-a11y` | NeedsRemediation | Homogeneity cannot prove semantic language/A11Y quality; a checklist path is not a command. |
| `META01-G05-public-content-secrets` | NeedsRemediation | Secret scans and regex heuristics do not prove the full public-content/PII scope. |
| `META01-G06-documentation-impact` | NeedsRemediation | Validators exist but do not enforce exactly one entry or complete planned path coverage. |
| `META01-G07-aeps-feedback` | NeedsRemediation | `rg` token presence does not prove AEPS deduplication, required fields, or exactly one bounded outcome. |
| `META01-G08-statistics` | Ready | Bash and PowerShell commands exist; the renderer consumes the canonical config and check-only detects drift. |
| `META01-G09-exact-path-diff` | NeedsRemediation | Current commands do not deterministically reconcile untracked and staged inventories. |
| `META01-G10-exact-head-closeout` | NeedsRemediation | Evidence creation is absent, sequencing self-invalidates the head, and pre-/post-merge facts are conflated. |

## Bestandene Aspekte / Passed Aspects

- **Scope fidelity**: Keine Produkt-, Runtime-, Architektur-, Preset- oder Level-0-Erweiterung ist geplant. / No product, runtime, architecture, preset, or level-0 expansion is planned.
- **Kardinalitaetsdefinition**: Die Sollmengen 23 Sources, 21 Findings und 10 direkte META-LH-01-Findings sind korrekt und konsistent definiert. / The declared 23/21/10 cardinalities are correct and consistent.
- **Security/A11Y/language intent**: Public-content, DE-first/EN-second, CEFR-B2- und WCAG-2.2-AA-Grenzen sind inhaltlich benannt; nur ihre Ausfuehrungsevidence ist unzureichend. / The intended gates are defined, but their execution evidence is insufficient.
- **Statistics**: Profil 2, `80`/`125` Referenzen sowie Schreib- und Check-only-Reihenfolge sind korrekt geplant. / Profile 2, the `80`/`125` references, and render/check-only order are correctly planned.
- **N/A boundaries**: Produkt-, Supply-Chain-, Script-Parity- und Agent-/Preset-/Level-0-Gates besitzen nachvollziehbare Begruendungen und Neubewertungs-Trigger. / The N/A boundaries have reasonable rationales and re-evaluation triggers.

## Erforderlicher Abschluss vor Tasks / Required Closure Before Tasks

Alle Critical- und High-Befunde muessen in Plan, Quickstart, Gate-Requirements und gegebenenfalls Spec/Vertrag minimal behoben werden. Danach ist dieses unabhaengige Plan-Review gegen die geaenderten Zeilen und Commands erneut auszufuehren. Tasks, Analyze, Implementierung, Commit und Remote-Closeout bleiben bis zu einem neuen Urteil **Ready** fail-closed gesperrt.

All Critical and High findings must be remediated minimally in the plan, quickstart, gate requirements, and where necessary the spec or contract. This independent plan review must then be repeated against the revised lines and commands. Tasks, Analyze, implementation, commit, and remote closeout remain fail-closed until a new **Ready** verdict.

## Endurteil / Final Verdict

**NeedsRemediation**
