# Unabhaengiges Plan-Review R2: Programmquellen-Baseline / Independent Plan Review R2: Program Sources Baseline

**Review-Datum / Review date**: 2026-08-09
**Review-Scope**: `specs/001-programmquellen-baseline`
**Review-Rolle / Review role**: unabhaengige Plan-Review-Rolle ohne Beteiligung an R1 oder der Plan-Remediation / independent plan reviewer without participation in R1 or its remediation

## Kurzurteil / Executive Assessment

Die Remediation hat den Plan deutlich gehaertet. Der feature-lokale Python-Vertrag ist stabil benannt, read-only gegen Repository, Index und Worktree und besitzt isolierte Positiv- und Negativfixtures. Die drei akzeptierten Roh-Hashes sind wirklich an die Dateien gebunden. Das aktuelle globale 14er-Gate besteht auf Bash und PowerShell. Maschinenstruktur, Secret-Mustersuche, semantischer Review und Public-Content-Review behaupten nicht mehr dieselbe Proof-Grenze. Der Renderer erkennt kausal genau die zwei neuen Python-Dateien als eingebettete Skripte. / *The remediation substantially hardened the plan. The feature-local Python contract is stable, repository-read-only, and covered by isolated positive and negative fixtures. All three accepted raw hashes are bound to actual files. The current fourteen-target gate passes on Bash and PowerShell. Machine structure, secret-pattern scanning, semantic review, and public-content review no longer claim the same proof boundary. The renderer causally discovers exactly the two new Python files as embedded scripts.*

Der Plan ist dennoch noch nicht ausfuehrungsreif. Drei offene High-Befunde betreffen eine zirkulaere Kandidaten-/Evidence-Reihenfolge, eine zu schwache AEPS-Finding-Ledger-Pruefung und einen Exact-Head-Vertrag, der nur Required Checks ausfuehrt und dessen Check-Token nicht zum tatsaechlichen Befehl passt. Ein Medium-Befund betrifft die noch nicht eigenstaendig ausgewiesene Accessibility-Evidence. / *The plan is still not execution-ready. Three open High findings concern circular candidate/evidence sequencing, insufficient AEPS finding-ledger validation, and an exact-head contract that executes only required checks and whose check token does not match the actual command. One Medium finding concerns accessibility evidence that is not yet represented independently.*

## Pruefgrundlage und Schreibgrenze / Review Basis and Write Boundary

Geprueft wurden `AGENTS.md`, die einschlaegigen Verfassungsregeln zu Security, Cross-Platform-Paritaet, Accessibility, DE-first/EN-second, Secure-Development-Anwendbarkeit, Documentation Impact und Governance, `docs/documentation-governance.md`, `docs/aeps/README.md`, `requirements/baseline/authority-and-stop-gates.md`, der installierte Autonomous-Run-Vertrag sowie alle vom Benutzer benannten META-LH-01-Artefakte vollstaendig. / *The review covered AGENTS.md, the relevant constitution rules, Documentation Impact and AEPS governance, the authority gates, the installed autonomous-run contract, and every user-named META-LH-01 artefact in full.*

Ausser dieser Datei wurde nichts erzeugt oder geaendert. Intake, R1, Spec, Plan, Contracts, Run-State, Domain-Dateien, Git-Index, Commits und Remotes blieben unveraendert. Dieses Review ist vom bereits geplanten einzigen Feature-weiten `UpdateRequired`-Eintrag abzudecken und erzeugt keinen zweiten Documentation-Impact-Eintrag. / *No artefact other than this file was created or changed. The intake, R1, spec, plan, contracts, run state, domain files, Git index, commits, and remotes remained unchanged. This review belongs to the already planned single feature-wide `UpdateRequired` record and creates no second Documentation Impact entry.*

## Nur-lesende Ausfuehrungsevidence / Read-only Execution Evidence

| Pruefung / Check | Ergebnis / Result | Einordnung / Assessment |
|---|---|---|
| `test_validate_meta_lh01.py` | Pass: 11 isolierte Faelle / 11 isolated cases | Positivfixture sowie die von R1 geforderten Negativfaelle fuer fehlende und doppelte Source, fehlendes RF-Feld, falsche direkte Ownership und unvollstaendiges Gate bestehen. / The positive fixture and the R1-required negative cases pass. |
| `input-bindings --surface bash` | Pass | Alle drei tatsaechlichen Roh-SHA-256-Werte und die Bash-Schemaoberflaechen bestehen. / All three actual raw hashes and Bash schema surfaces pass. |
| `input-bindings --surface powershell` | Pass | Alle drei tatsaechlichen Roh-SHA-256-Werte und die PowerShell-Schemaoberflaechen bestehen. / All three actual raw hashes and PowerShell schema surfaces pass. |
| `global-ready` | Pass | Alle 14 aktuellen Ziele, normalisierten Hashes, Receipts, nicht supersedierten `Ready`-Single-Leafs und beide Validatoroberflaechen bestehen; META-LH-01 ist zuerst. / All fourteen current targets and both validator surfaces pass; META-LH-01 is first. |
| `domain` vor Implementierung / before implementation | Erwarteter Fail / expected failure | Es fehlen noch die Einzelzeilen `SRC-163` bis `SRC-167`. Das ist gemaess Review-Auftrag kein Planfehler. / The individual source rows are not implemented yet; this is not a plan defect under the review instruction. |
| Script-Renderer `-WhatIf` | Pass | Der Preview enthaelt genau `test_validate_meta_lh01.py` und `validate_meta_lh01.py` als neue eingebettete Skripte. / The preview contains exactly the two new Python files as embedded scripts. |
| Script-Renderer `-CheckOnly` vor Implementierung / before implementation | Erwarteter Fail / expected failure | Drift wird ausschliesslich fuer `docs/scripts/embedded-scripts.md` gemeldet; `docs/scripts/reference.md` bleibt aktuell. / Drift is reported only for the generated embedded-script inventory. |
| Gate-Requirements und Kandidaten-Allowlist | Pass | Beide JSON-Dateien sind syntaktisch gueltig. / Both JSON files are syntactically valid. |

## Findings nach Severity / Findings by Severity

### Kritisch / Critical

Keine offenen Critical-Befunde. / *No open Critical findings.*

### Hoch / High

#### R2-H01 — Die eingefrorene Kandidatenmenge wird zu spaet erzeugt

**Orte / Locations**: `plan.md:93-98`; `quickstart.md:63-96,130-170`; `contracts/validate_meta_lh01.py:386-430`; `candidate-paths.json`.

**Befund / Finding**: Plan-Schritte 5 und 6 verlangen bereits die exakte Kandidatenmenge fuer Public-Content- und Documentation-Impact-Evidence. Schritt 9 erzeugt diese Menge aber erst spaeter. Im Quickstart validiert Abschnitt 5 Public Content vor der Erzeugung der Datei in Abschnitt 6. Danach entstehen oder aendern sich in den Abschnitten 7 und 8 noch Documentation-Impact-Evidence, AEPS-Receipt beziehungsweise Ledger und Projektstatistik. Die als "nach allen Implementierungsedits" bezeichnete Menge ist deshalb weder zu diesem Zeitpunkt vollstaendig noch stabil. / *Plan steps 5 and 6 already require the exact candidate set, but step 9 creates it later. The quickstart validates public content before generating the file and then creates or changes Documentation Impact, AEPS, and statistics artefacts afterward. The set described as final is therefore neither complete nor stable at that point.*

**Auswirkung / Impact**: `publicContentReviews` und der einzige schema-1.1-Documentation-Impact-Eintrag koennen Pfade auslassen, die erst nach dem Freeze entstehen. Ein spaeteres Stage kann dann entweder die Evidence verletzen oder eine unvollstaendige Lieferung erzeugen. Das schliesst R1-H02 und R1-H03 noch nicht vollstaendig. / *Public-content evidence and the single schema-1.1 record can omit paths created after the freeze. Later staging must then violate the evidence or omit delivery paths. R1-H02 and R1-H03 are not fully closed.*

**Erforderliche Remediation / Required remediation**: Eine eindeutige Fixpunkt-Reihenfolge festlegen: alle Domain-, Feature-, Review-, AEPS-, Renderer- und Statistikartefakte erzeugen; danach die tatsaechliche Kandidatenmenge bilden; Public-Content- und Documentation-Impact-Evidence gegen genau diese Menge erzeugen oder aktualisieren; die Menge erneut ableiten und exakte Stabilitaet beweisen; erst dann stagen. Alternativ ist ein ausdruecklicher zweipassiger, fail-closed Fixpunktvertrag zu definieren. / *Define an explicit fixed-point sequence: create all delivery artefacts, derive the actual candidate, create or update public-content and Documentation Impact evidence against it, re-derive and prove exact stability, and only then stage. An explicit two-pass fail-closed fixed-point contract is also acceptable.*

#### R2-H02 — Ein AEPS-Finding kann ohne vollstaendigen Ledger-Datensatz bestehen

**Orte / Locations**: `docs/aeps/README.md` Pflichtfelder; `autonomous-run-gate-requirements.json:95-102`; `contracts/validate_meta_lh01.py:445-497`; `contracts/test_validate_meta_lh01.py:143-155`.

**Befund / Finding**: Der AEPS-Modus beweist den eindeutigen `Finding`-oder-`NoChange`-Ausgang, Source-Hash, Deduplizierung, Reifegrenze und Nicht-Handoff. Bei `Finding` prueft er im Ledger aber nur, ob die ID exakt einmal irgendwo vorkommt. Er prueft nicht den zu dieser ID gehoerenden Ledger-Abschnitt und dessen verpflichtende Felder wie Quelle, Datum/Commit, positive und negative Evidence, Grenzen, AOC-spezifisch versus generisch, Domäne, Preset-Bezug, naechste Validierung, Promotion-Blocker sowie Capture- und Upstream-Status. Die Negativtests decken nur einen ungueltigen Doppelausgang ab. / *The AEPS mode proves a unique Finding-or-NoChange outcome, source hash, deduplication, maturity, and non-handoff. For a Finding, however, it only checks that the ID occurs once somewhere in the ledger. It does not validate the ledger section or its mandatory fields. The negative suite covers only an invalid dual outcome.*

**Auswirkung / Impact**: Eine einzelne nackte ID im Ledger wuerde den ausfuehrbaren Vertrag bestehen, obwohl der kanonische AEPS-Vertrag verletzt ist. Damit bleibt der AEPS-Teil von R1-H02 offen. / *A bare ledger ID would pass the executable contract while violating the canonical AEPS contract. The AEPS part of R1-H02 remains open.*

**Erforderliche Remediation / Required remediation**: Fuer `Finding` den exakt zugeordneten Ledger-Abschnitt samt allen Pflichtfeldern, Source-/Receipt-Bindung und Statuswerten deterministisch pruefen und mindestens ein negatives Fixture fuer einen unvollstaendigen Ledger-Eintrag hinzufuegen. `NoChange` darf weiterhin ohne Ledger-Mutation bestehen, muss aber seine Begruendung im Receipt behalten. / *For a Finding, deterministically validate the corresponding ledger section, all mandatory fields, source/receipt binding, and status values, and add at least one negative fixture for an incomplete ledger entry. NoChange may remain ledger-free but must retain its receipt rationale.*

#### R2-H03 — Der Exact-Head- und Bypass-Nachweis deckt nicht alle fehlgeschlagenen Checks ab

**Orte / Locations**: `quickstart.md:195-212,259-273`; `autonomous-run-gate-requirements.json:125-132`; installierter Gate-Evidence-Validator.

**Befund / Finding**: Der Quickstart fuehrt nur `gh pr checks "$pr_number" --required --watch` aus. G13 behauptet entsprechend nur erfolgreiche Required Checks. Die aktuelle Benutzerautoritaet erlaubt einen Admin-Bypass jedoch nur dann, wenn keine fehlgeschlagenen Checks umgangen werden; ein fehlgeschlagener nicht-required Check bleibt durch den Plan unbelegt. Zusaetzlich verlangt G13 den zusammenhaengenden Token `gh pr checks --required --watch`. Dieser Token ist kein Teil des tatsaechlichen Befehls, weil die PR-Nummer zwischen `checks` und `--required` steht. Der installierte Validator arbeitet mit wortgetreuen Teilstrings; eine ehrliche `executedCommand`-Angabe wuerde daher scheitern. / *The quickstart runs only required checks, while current authority permits admin bypass only when no failed check is bypassed. A failed non-required check is therefore not covered. In addition, G13 requires the contiguous token `gh pr checks --required --watch`, which is not present in the actual command because the PR number appears between `checks` and `--required`. The installed validator uses literal substrings, so an honest executedCommand would fail.*

**Auswirkung / Impact**: Die weitgehend reparierte kausale Exact-Head-Sequenz kann ihre eigene Gate-Evidence nicht wahrheitsgetreu validieren und koennte einen fehlgeschlagenen nicht-required Check beim Admin-Fallback umgehen. R1-C02 bleibt deshalb offen. / *The largely repaired causal exact-head sequence cannot truthfully validate its own gate evidence and could bypass a failed non-required check during the admin fallback. R1-C02 therefore remains open.*

**Erforderliche Remediation / Required remediation**: Alle fuer den exakten Head gemeldeten Checks erfassen und auf einen terminal erfolgreichen Zustand pruefen; Required Checks duerfen zusaetzlich separat ausgewiesen werden. Die Command-Tokens atomar formulieren, zum Beispiel `gh pr checks`, `--required` und `--watch`, oder exakt den tatsaechlich ausgefuehrten Befehl binden. Erst danach darf fehlende unabhaengige Approval als einziger Admin-Fallback-Blocker gelten. / *Capture every check reported for the exact head and require a terminal successful state, with required checks optionally represented as an additional subset. Use atomic command tokens or bind the exact actual command. Only then may missing independent approval be the sole admin-fallback blocker.*

### Mittel / Medium

#### R2-M01 — Accessibility ist ein Kriteriensatz, aber keine getrennte Evidence-Klasse

**Orte / Locations**: `data-model.md:100-106`; `quickstart.md:63-72`; `autonomous-run-gate-requirements.json:55-62`; `contracts/validate_meta_lh01.py:57-61,352-385`.

**Befund / Finding**: Maschinenstruktur und Public Content sind getrennt. Die einzige `semanticReviews`-Liste mischt jedoch Sprachgleichwertigkeit, CEFR B2 und fachliche Wahrheit mit Accessibility-Kriterien wie Heading-Hierarchie, linearen Tabellen, beschreibenden Links und Text-first. Es gibt weder eine getrennte Accessibility-Evidence-Klasse noch einen eigenen Gate-Ausgang beziehungsweise eine ausdrücklich benannte Accessibility-Review-Rolle. / *Machine structure and public content are separate, but the single semanticReviews list combines language and domain truth with accessibility criteria. There is no separate accessibility evidence class, gate outcome, or explicitly named accessibility reviewer role.*

**Auswirkung / Impact**: Die Kriterien sind ehrlich benannt und maschinell nicht ueberbehauptet, aber die im R2-Auftrag verlangte Trennung von semantischer und Accessibility-Evidence ist nicht eindeutig nachweisbar. / *The criteria are honest and not overclaimed, but the R2-required separation between semantic and accessibility evidence is not explicit.*

**Erforderliche Remediation / Required remediation**: Accessibility als eigene strukturierte Review-Klasse oder mindestens als getrennten, eigenstaendig auswertbaren Gate-Block mit benannter Reviewer-Rolle und eigener Null-Blocking-Grenze modellieren. / *Model accessibility as its own structured review class or at least as a separately evaluable gate block with a named reviewer role and its own zero-blocking boundary.*

## Abbildung aller R1-Befunde / Mapping of All R1 Findings

| R1-ID | Status | R2-Begruendung / R2 rationale |
|---|---|---|
| C-01 | Closed | Stabiler read-only Python-Vertrag, sechs gebundene Domain-Pfade, exakte 23/21/10-Mengen, Pflichtfelder, Coverage und Gate-Struktur; 11 isolierte Positiv-/Negativtests bestehen. / Stable executable contract and passing isolated fixtures cover the required domain proof. |
| C-02 | Open | Commit-vor-Head, Threads, temporaerer Render und Post-Merge-Trennung sind repariert; All-Checks-Abdeckung und ein wahrheitsgetreuer G13-Command-Token fehlen noch. / Causal sequencing is repaired, but all-check coverage and a truthful G13 token remain missing. |
| C-03 | Closed | `global-ready` ist ein eigener reproduzierbarer Modus, wird vor Tasks, jedem Analyze und Implement verlangt und besteht aktuell fuer alle 14 Ziele auf beiden Oberflaechen. / The dedicated mode is required at every named boundary and currently passes for all fourteen targets. |
| H-01 | Closed | Beide Input-Gates vergleichen zuerst alle drei tatsaechlichen Roh-Hashes mit `acceptedArtifacts` und fuehren danach ihre jeweilige Schemaoberflaeche aus. / Both gates bind all three actual raw hashes before their schema surface. |
| H-02 | Open | Maschinen-, Secret-Pattern-, semantische und Public-Content-Grenzen sind ehrlicher; Public-Content-Reihenfolge, getrennte Accessibility und vollstaendige AEPS-Ledger-Pflichtfelder bleiben offen. / Proof boundaries are more honest, but candidate timing, separate accessibility, and complete AEPS ledger validation remain open. |
| H-03 | Open | Schema 1.1, genau ein Eintrag und die alleinige Intake-Quelle sind ausfuehrbar gebunden; die exakte Pfadmenge wird jedoch vor spaeteren Evidence-/Statistik-Aenderungen eingefroren. / Schema, cardinality, and canonical source are fixed, but exact path timing remains circular. |
| H-04 | Closed | Die aktuelle Benutzeranweisung autorisiert den vollstaendigen Lauf und `MergeAndSync`; der Plan trennt diese Authority vom gespeicherten Modus und verlangt Revalidierung vor irreversiblen Aktionen. Die R2-Schreibgrenze verbietet lediglich Aktionen in diesem Review. / Current authority is explicit and separate from stored mode; this review's narrow write boundary only limits the present step. |
| M-01 | Closed | Der Kandidatenmodus vergleicht eingefrorene Sollmenge, staged Namen, Porcelain einschliesslich untracked, unstaged Kandidatenreste und `git diff --cached --check`; fremde gestagte Pfade blockieren. / The candidate mode now reconciles staged, unstaged, and untracked state exactly. |

## Gate-Anforderungen im Einzelurteil / Individual Gate Assessment

| Gate | Status | Beurteilung / Assessment |
|---|---|---|
| `META01-G01-input-binding-bash` | Closed | Aktuell ausgefuehrt und bestanden; echte Roh-Hash-Bindung plus Bash-Schema. / Executed and passed with real raw-hash binding. |
| `META01-G02-input-binding-powershell` | Closed | Aktuell ausgefuehrt und bestanden; echte Roh-Hash-Bindung plus PowerShell-Schema. / Executed and passed with real raw-hash binding. |
| `META01-G03-global-ready-14` | Closed | Aktuell ausgefuehrt und fuer alle 14 Ziele bestanden; erneute Ausfuehrung ist vor Tasks, jedem Analyze und Implement gebunden. / Executed and passed; rerun is bound to every required phase boundary. |
| `META01-G04-domain-contract` | Closed | Vertrag und Fixtures sind ausfuehrbar; der aktuelle Vorimplementierungs-Fail ist erwartbar und fail-closed. / Contract and fixtures are executable; the current pre-implementation failure is expected. |
| `META01-G05-markdown-structure` | Closed | Preview, kausaler Render, Check-only und anschliessende Homogeneity sind korrekt getrennt; Preview/Check belegen den erwarteten eingebetteten Skript-Drift. / Preview, render, check-only, and homogeneity are correctly ordered and causally bound. |
| `META01-G06-independent-semantic-review` | Open (Medium) | Semantische Proof-Grenze ist ehrlich, Accessibility aber nicht als getrennte Evidence-Klasse ausgewiesen. / Semantic proof is honest, but accessibility is not a separate evidence class. |
| `META01-G07-secret-pattern-scans` | Closed | Required Scope behauptet nur Mustersuche, nicht Publikationseignung. / Scope is correctly limited to pattern detection. |
| `META01-G08-independent-public-content-review` | Open (High) | Der Validator verlangt exakte Pfade, aber der Quickstart ruft ihn vor dem Kandidaten-Freeze und vor spaeteren Evidence-/Statistik-Aenderungen auf. / Validation precedes the final candidate freeze and later artefact changes. |
| `META01-G09-documentation-impact` | Open (High) | Schema, Kardinalitaet und kanonische Quelle sind korrekt; die exakte Pfadmenge besitzt noch keinen stabilen Fixpunkt. / Schema, cardinality, and source are correct, but path coverage has no stable fixed point. |
| `META01-G10-aeps-outcome` | Open (High) | Eindeutiger Ausgang und Deduplizierung bestehen konzeptionell; ein Finding-Ledger-Eintrag wird nicht gegen alle Pflichtfelder geprueft. / Outcome and deduplication are sound, but a finding ledger entry is not fully validated. |
| `META01-G11-statistics` | Closed | Render plus Bash- und PowerShell-Check-only nach Implementierung sind korrekt gebunden. / Render and both check-only surfaces are correctly bound. |
| `META01-G12-exact-candidate` | Closed | Der ausfuehrbare Kern schliesst untracked, staged und unstaged Kandidatendrift fail-closed aus. / The executable core fails closed on all candidate-state drift. |
| `META01-G13-pr-head-convergence` | Open (High) | Commit-/Head-Kausalitaet, Threads und Post-Merge-Trennung sind korrekt; All-Checks-Abdeckung und literal passender Command-Token fehlen. / Head causality, threads, and closeout separation are correct; all-check coverage and a matching token are missing. |
| `META01-N01-product-tests-runtime` | N/A accepted | Kein Produktcode oder Produkt-Runtime; Neubewertungs-Trigger ist vorhanden. / No product code or runtime; trigger is present. |
| `META01-N02-supply-chain` | N/A accepted | Keine externe Dependency, Binaer-, Build-, AI-Runtime- oder Release-Ausgabe; Trigger ist vorhanden. / No applicable supply-chain output; trigger is present. |
| `META01-N03-script-platform-parity` | N/A accepted | Kein neues Bash-/PowerShell-Produkttool; vorhandene Validatorpaare bleiben Pruefoberflaechen. / No new Bash/PowerShell product tool. |
| `META01-N04-agent-parity-presets-level0` | N/A accepted | Shared Guidance, Presets, Level 0 und Home Sync bleiben ausserhalb des Scopes. / Shared guidance, presets, level 0, and Home Sync remain out of scope. |

## Beurteilung der zehn R2-Schwerpunkte / Assessment of the Ten R2 Focus Areas

1. **Domain-Vertrag / Domain contract**: bestanden auf Planebene; Positiv- und Negativfixtures bestehen. / *Passed at plan level with passing positive and negative fixtures.*
2. **Roh-Hash-Bindung / Raw-hash binding**: bestanden und aktuell auf beiden Oberflaechen ausgefuehrt. / *Passed and currently executed on both surfaces.*
3. **14er-Ready-Gate / Fourteen-target Ready gate**: bestanden und an alle drei geforderten Phasengrenzen gebunden. / *Passed and bound to every required downstream boundary.*
4. **Getrennte Evidence / Separated evidence**: teilweise offen; Accessibility ist noch mit der semantischen Evidence vermischt. / *Partly open because accessibility remains combined with semantic evidence.*
5. **Documentation Impact**: in Schema, Kardinalitaet und Quelle bestanden, aber wegen der instabilen Kandidatenreihenfolge offen. / *Schema, cardinality, and source pass, but candidate sequencing remains open.*
6. **AEPS-Ausgang / AEPS outcome**: der eindeutige Ausgang ist bewiesen; der Finding-Ledger-Zweig ist noch unvollstaendig validiert. / *The unique outcome is proven, but the Finding ledger branch is incompletely validated.*
7. **Kandidatenabstimmung / Candidate reconciliation**: der Validator-Kern ist bestanden; staged, unstaged und untracked werden exakt abgeglichen. / *The validator core passes and reconciles all three states exactly.*
8. **Generated Update**: bestanden; Preview findet genau die zwei Python-Dateien, und vor Render driftet nur `docs/scripts/embedded-scripts.md`. / *Passed; preview discovers exactly the two Python files and only the embedded inventory drifts before rendering.*
9. **Exact Head und Closeout / Exact head and closeout**: kausale Sequenz weitgehend bestanden, aber All-Checks- und Token-Luecke bleibt offen. / *Causal sequencing largely passes, but all-check and token gaps remain.*
10. **Aktuelle Autoritaet / Current authority**: bestanden. Vollstaendiger Lauf und `MergeAndSync` sind aktuell genehmigt; Admin-Bypass bleibt Approval-only. Die technische Check-Luecke unter Punkt 9 muss diese Grenze noch vollstaendig erzwingen. / *Passed. The complete run and MergeAndSync are currently authorised, with admin bypass limited to approval-only; the technical check gap in item 9 must still enforce that boundary fully.*

## Abschlussbedingung vor Tasks / Closure Required Before Tasks

Vor Tasks muessen R2-H01 bis R2-H03 geschlossen und die betroffenen Plan-, Quickstart-, Contract-/Test- und Gate-Requirements-Stellen erneut unabhaengig geprueft werden. R2-M01 ist entsprechend der ausdruecklichen R2-Evidence-Anforderung ebenfalls vor der Freigabe zu schliessen. Danach ist `global-ready` unmittelbar neu auszufuehren; jede zwischenzeitliche Target-, Review-, Receipt-, Authority- oder Evidence-Drift stoppt fail-closed. / *Before Tasks, R2-H01 through R2-H03 must be closed and the affected planning and contract surfaces independently re-reviewed. R2-M01 must also be closed because it is an explicit R2 evidence requirement. Then global-ready must be rerun immediately; any intervening drift fails closed.*

## Endurteil / Final Verdict

**NeedsRemediation**
