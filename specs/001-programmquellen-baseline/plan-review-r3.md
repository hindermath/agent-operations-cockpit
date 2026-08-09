# Unabhaengiges Plan-Review R3: Programmquellen-Baseline / Independent Plan Review R3: Program Sources Baseline

**Review-Datum / Review date**: 2026-08-09
**Review-Scope**: `specs/001-programmquellen-baseline`
**Review-Rolle / Review role**: neue unabhaengige R3-Plan-Review-Rolle ohne Beteiligung an R1, R2 oder den Remediations / new independent R3 plan reviewer without participation in R1, R2, or their remediations

## Kurzurteil / Executive Assessment

R2-H01, R2-H03 und R2-M01 sind vollstaendig geschlossen. Der zweipassige Kandidaten-Fixpunkt besitzt jetzt die richtige Reihenfolge, alle gemeldeten PR-Checks einschliesslich nicht-required muessen bestehen oder `skipping` sein, die Required-Teilmenge ist nicht leer, und semantische sowie Accessibility-Evidence sind als getrennte Dateien, Kriterienklassen, Rollen und Gates modelliert. Die zuvor geschlossenen R1-/R2-Punkte zeigen keine Regression. / *R2-H01, R2-H03, and R2-M01 are fully closed. The two-pass candidate fixed point is correctly ordered, every reported PR check including non-required checks must pass or be skipping, the required subset is non-empty, and semantic and accessibility evidence are modelled as separate files, criteria classes, roles, and gates. Previously closed R1/R2 findings have not regressed.*

R2-H02 bleibt jedoch offen. Der AEPS-Validator prueft bei `Finding` zwar den kanonischen Abschnitt, Source-/Receipt-Pfade sowie erlaubte Capture- und Upstream-Statuswerte. Er prueft fuer die uebrigen Pflichtfelder aber nur, ob ihr Feldname irgendwo im Abschnitt vorkommt. Ein Abschnitt mit allen Feldnamen, aber leeren Pflichtwerten, besteht deshalb. Die isolierte R3-Negativpruefung hat diesen unzulaessigen Pass reproduziert. Damit verbleibt ein High-Befund und ein materieller Stop-Grund vor Tasks. / *R2-H02 remains open. For a Finding, the AEPS validator checks the canonical section, source and receipt paths, and allowed capture and upstream status values. For the other mandatory fields it only checks whether a field label occurs somewhere in the section. A section containing every label but empty mandatory values therefore passes. The isolated R3 negative check reproduced this invalid pass. One High finding and a material stop reason before Tasks remain.*

## Pruefgrundlage und Schreibgrenze / Review Basis and Write Boundary

Vollstaendig gelesen wurden `AGENTS.md`, die einschlaegigen Constitution-Regeln, die installierte Autonomous-Run-Governance zu Authority, Evidence, Kandidat und Closeout, `docs/documentation-governance.md`, `docs/aeps/README.md`, `requirements/baseline/autonomy-and-evidence-model.md`, `requirements/baseline/authority-and-stop-gates.md`, das vollstaendige META-LH-01-Intake und alle textuellen Artefakte unter `specs/001-programmquellen-baseline`, besonders `plan-review.md` und `plan-review-r2.md`. Abgeleitete `__pycache__`-Binaerdateien wurden nicht als normative Quelle behandelt. / *The review fully read the named governance, intake, historical reviews, and every textual feature artefact. Derived bytecode files were not treated as normative sources.*

Ausser dieser Datei wurde nichts erzeugt oder geaendert. Intake, Spec, Plan, Contracts, Tests, Run-State, Domain-Dateien, Git-Index und Remotes blieben unveraendert. Dieses R3-Review gehoert zum bereits geplanten einzigen Feature-weiten `UpdateRequired`-Eintrag und erzeugt keine zweite Documentation-Impact-Entscheidung. / *No artefact other than this file was created or changed. The intake, feature artefacts, run state, domain files, Git index, and remotes remained unchanged. This R3 review belongs to the already planned single feature-wide `UpdateRequired` record and creates no second Documentation Impact decision.*

## Nur-lesende Ausfuehrungsevidence / Read-only Execution Evidence

| Pruefung / Check | Ergebnis / Result | Einordnung / Assessment |
|---|---|---|
| `test_validate_meta_lh01.py` | Pass: 15 isolierte Positiv-/Negativfaelle / 15 isolated positive/negative cases | Einschliesslich Kandidaten-Fixpunktdrift, unvollstaendiger Accessibility-Evidence, unvollstaendigem AEPS-Abschnitt und fehlgeschlagenem nicht-required Check. / Includes fixed-point drift, incomplete accessibility evidence, incomplete AEPS section, and a failed non-required check. |
| `input-bindings --surface bash` | Pass | Alle drei realen Roh-SHA-256-Werte und die Bash-Schemaoberflaechen bestehen. / All three actual raw hashes and Bash schema surfaces pass. |
| `input-bindings --surface powershell` | Pass | Alle drei realen Roh-SHA-256-Werte und die PowerShell-Schemaoberflaechen bestehen. / All three actual raw hashes and PowerShell schema surfaces pass. |
| `global-ready` | Pass | Alle 14 aktiven Ziele, aktuelle Hashes, Receipts, nicht supersedierten `Ready`-Single-Leafs und beide Validatoroberflaechen bestehen; META-LH-01 bleibt zuerst. / All fourteen targets and both validator surfaces pass; META-LH-01 remains first. |
| Alle Feature-JSON-Dateien | Pass | `jq` kann jede JSON-Datei fehlerfrei lesen. / Every feature JSON file parses successfully. |
| Python-AST-Pruefung | Pass | Vertrag und Tests sind syntaktisch gueltig; Bytecode-Erzeugung war deaktiviert. / Contract and tests are syntactically valid with bytecode generation disabled. |
| Gate-JSON-Struktur | Pass | 19 eindeutige Gate-IDs, getrennte Semantic-/A11Y-Gates und atomare G13-Command-Tokens. / Nineteen unique gate IDs, separate semantic/A11Y gates, and atomic G13 command tokens. |
| `domain` vor Implementierung / before implementation | Erwarteter Fail / expected failure | Genau eine Fehlerzeile nennt ausschliesslich die fehlenden Einzelzeilen `SRC-163` bis `SRC-167`; stdout bleibt leer. / Exactly one error line names only the five planned missing source rows and stdout remains empty. |
| Isolierte All-Checks-Pruefung | Pass | `pass` und `skipping` fuer All-Checks werden akzeptiert; eine leere Required-Teilmenge wird abgewiesen. / Pass and skipping are accepted, while an empty required subset is rejected. |
| Isolierter AEPS-Leerwertfall | **Unzulaessiger Pass / invalid pass** | Ein Ledger-Abschnitt mit allen Pflichtfeldnamen, gueltigen Status-Tokens und gebundenen Pfaden, aber leeren Werten fuer Datum/Commit, Problem, Kontext, positive/negative Evidence, Grenzen, Einordnung, Domaene, Reifegrad, Preset-Bezug, naechste Validierung und Promotion-Blocker wird akzeptiert. / A ledger section with every label but empty mandatory values is accepted. |

Der reale `candidate-fixpoint` wurde vertragsgemaess nicht gegen den aktuellen Vorimplementierungs-Worktree verlangt: Die beiden Evidence-Pfadanker und weitere Lieferartefakte entstehen erst in der Implementierungsphase. Seine Reihenfolge und seine isolierte Drift-Erkennung wurden dennoch geprueft. / *The real candidate fixed point was not required against the pre-implementation worktree because its evidence anchors and other delivery artefacts are created during implementation. Its ordering and isolated drift detection were still reviewed.*

## R2-Befunde / R2 Findings

### R2-H01 — Closed

**Orte / Locations**: `plan.md:96-99`; `quickstart.md:15-17,124-158`; `contracts/baseline-validation-contract.md:101-105`; `contracts/validate_meta_lh01.py:580-652`; `autonomous-run-gate-requirements.json`, Gate `META01-G12A-candidate-fixed-point`.

Alle sonstigen Domain-, Feature-, Review-, AEPS-, Renderer- und Statistikpfade entstehen vor der ersten Menge. Die Public-Content- und Documentation-Impact-Dateien existieren vorher als vorbenannte Pfadanker. Danach wird Menge eins erzeugt, nur der Inhalt dieser beiden vorhandenen Dateien vervollstaendigt, Menge zwei erneut abgeleitet und mit `cmp` bytegleich gebunden. `candidate-fixpoint` prueft anschliessend dieselbe Allowlist-/Worktree-Menge. Public-Content- und Documentation-Impact-Validierung sowie Stage folgen erst danach; jede Pfadabweichung startet beide Ableitungen neu. / *All other delivery paths and the two named evidence anchors exist before set one. Evidence completion changes no path, set two must be byte-identical, candidate-fixpoint binds the same worktree set, and only then may the evidence validators and staging run. Any path drift restarts both derivations.*

Damit sind die Kandidaten-, Public-Content- und Documentation-Impact-Anteile der frueheren R1-H02-/R1-H03-Befunde geschlossen. / *This closes the candidate, public-content, and Documentation Impact portions of the earlier R1 findings.*

### R2-H02 — Open (High)

**Orte / Locations**: `docs/aeps/README.md:112-153`; `contracts/validate_meta_lh01.py:451-492`; `contracts/test_validate_meta_lh01.py:171-193`; `autonomous-run-gate-requirements.json`, Gate `META01-G10-aeps-outcome`.

Der Finding-Zweig bindet jetzt genau eine kanonische `## AEPS-FIND-AOC-NNN`-Ueberschrift, Source- und Receipt-Pfad, erlaubte Capture-/Upstream-Statuswerte sowie die im Receipt gepruefte Reifegrenze. `NoChange` bleibt ledgerfrei und verlangt weiterhin eine Receipt-Begruendung. Das ist eine deutliche Verbesserung. / *The Finding branch now binds one canonical heading, source and receipt paths, allowed capture/upstream status values, and the receipt maturity boundary. NoChange remains ledger-free with a receipt rationale.*

Die Funktion `validate_aeps_ledger_section` sucht fuer fast alle Pflichtfelder jedoch nur Regex-Tokens im gesamten Abschnitt. Sie parst weder die jeweilige Feldzeile noch fordert sie einen nichtleeren Wert nach dem Label. Auch der vorhandene Negativtest entfernt fast den gesamten Abschnitt und deckt deshalb den Leerwertfall nicht ab. Die zusaetzliche R3-Fixture mit vollstaendigen Labels und leeren Werten wurde unzulaessig akzeptiert. Ein Finding kann somit weiterhin ohne vollstaendigen Ledger-Datensatz bestehen. / *The validator only searches for labels and does not require a non-empty value for each field. The existing negative test removes most of the section and misses the empty-value case. The additional R3 fixture was incorrectly accepted, so a Finding can still pass without a complete ledger record.*

**Erforderliche Remediation / Required remediation**: Den exakt abgegrenzten Finding-Abschnitt feldweise parsen und fuer jedes Pflichtfeld einen nichtleeren, zugeordneten Wert verlangen. Datum/Commit muss den AEPS-Vertrag erfuellen, Reifegrad und Preset-Bezug muessen gueltig beziehungsweise begruendet sein, und Capture- sowie Upstream-Status muessen an ihre eigenen Felder gebunden bleiben. Ein isolierter Negativtest muss mindestens einen Abschnitt mit allen Labels, aber einem oder mehreren leeren Pflichtwerten fail-closed abweisen. / *Parse the exact Finding section field by field and require a non-empty assigned value for every mandatory field. Bind date/commit, maturity, preset relation, capture status, and upstream status to their own fields, and add an isolated negative case for present labels with empty values.*

### R2-H03 — Closed

**Orte / Locations**: `plan.md:100-102`; `quickstart.md:196-221,223-280`; `contracts/validate_meta_lh01.py:655-676`; `contracts/test_validate_meta_lh01.py:210-223`; `autonomous-run-gate-requirements.json`, Gate `META01-G13-pr-head-convergence`.

Der Quickstart wartet zuerst auf alle gemeldeten Checks, erfasst danach eine nichtleere All-Checks-Menge und getrennt eine nichtleere Required-Teilmenge. `check-inventory` erlaubt fuer jede Zeile nur terminal `pass` oder `skipping`, verlangt die Required-Menge als Teilmenge und blockiert damit auch fehlgeschlagene nicht-required Checks. Die zusaetzliche R3-Pruefung bestaetigt den positiven `pass`/`skipping`-Fall und den negativen Leer-Required-Fall. / *The quickstart captures all reported checks and a separate non-empty required subset. The validator permits only terminal pass or skipping, requires subset consistency, and therefore blocks failed non-required checks. R3 also confirmed the positive and empty-required negative cases.*

Die G13-Tokens sind atomar und passen zu den ehrlich beschriebenen Befehlen, insbesondere `gh pr checks`, `--watch`, `--fail-fast`, `--json bucket,name,state,link`, `--required` und `check-inventory`. Commands und Runner muessen weiterhin aus Definitionen oder Logs stammen. Admin-Bypass bleibt auf den Fall begrenzt, dass unabhaengige Approval der einzige verbleibende Blocker ist; Checks, Exact-Head, Change Request, Threads und aktuelle Authority muessen zuvor bestehen. / *G13 tokens are atomic and match the documented executed commands. Commands and runners remain definition/log-derived. Admin bypass remains approval-only after every technical and review gate passes.*

### R2-M01 — Closed

**Orte / Locations**: `plan.md:20,93,143`; `research.md:40-49`; `data-model.md:95-101`; `quickstart.md:55-80`; `contracts/baseline-validation-contract.md:16,92-94,119-121`; `contracts/validate_meta_lh01.py:60-71,364-400`; Gates `META01-G06-independent-semantic-review` und `META01-G06A-independent-accessibility-review`.

Semantik und Accessibility besitzen getrennte JSON-Dateien, unterschiedliche exakte Kriterienmengen (`semanticReviews` und `accessibilityReviews`), getrennt benannte unabhaengige Rollen/Runner-Tokens, eigene Gate-IDs und jeweils eine eigene Null-Blocking-Grenze. Der Validator waehlt die Kriterienklasse ueber `--kind`, bindet fuer beide Klassen exakt die sechs Domain-Pfade und lehnt fehlende Accessibility-Kriterien isoliert ab. Maschinenstruktur bleibt eine dritte, engere Proof-Klasse. / *Semantics and accessibility now have separate JSON files, exact criteria sets, separately named independent roles, distinct gate IDs, and independent zero-blocking outcomes. The validator binds each kind to the six domain paths and rejects incomplete accessibility criteria. Machine structure remains a third, narrower proof class.*

## Keine Regression geschlossener R1-/R2-Punkte / No Regression of Closed R1/R2 Findings

| Historischer Befund / Historical finding | R3-Status | Begruendung / Rationale |
|---|---|---|
| R1-C01 | Closed | Stabiler read-only Domain-Vertrag, sechs Pfade, exakte 23/21/10-Mengen und 15 bestehende Fixtures. / Stable executable domain contract and fixtures. |
| R1-C02 | Closed | Kausale Commit-/PR-Head-Reihenfolge, temporaerer Evidence-Render, All-Checks-Inventar, Threads und getrennter schema-1.1-Closeout. / Causal head evidence, all checks, threads, and separate closeout. |
| R1-C03 | Closed | `global-ready` besteht aktuell und bleibt vor Tasks, jedem Analyze und Implement gebunden. / Current global gate passes and remains bound to every required boundary. |
| R1-H01 | Closed | Beide Input-Modi vergleichen alle drei realen Roh-Hashes vor den Schemaoberflaechen. / Both input modes bind all three raw hashes. |
| R1-H02 | Open nur wegen R2-H02 / open only because of R2-H02 | Maschinen-, Secret-, Public-, Semantic- und A11Y-Proof-Grenzen sind getrennt; nur die AEPS-Leerwertluecke bleibt. / Proof boundaries are separated; only the AEPS empty-value gap remains. |
| R1-H03 | Closed | Schema 1.1, genau ein Eintrag, kanonisches Intake und stabiler Kandidaten-Fixpunkt. / Schema, cardinality, canonical intake, and stable fixed point. |
| R1-H04 | Closed | Aktuelle Benutzerautoritaet und gespeicherter Modus bleiben getrennt; Revalidierung vor irreversiblen Aktionen ist gebunden. / Current authority remains separate from stored mode. |
| R1-M01 | Closed | Staged, unstaged und untracked Inventare sowie `git diff --cached --check` bleiben fail-closed gebunden. / Candidate inventories and staged whitespace remain fail closed. |

## Erneute Bewertung aller Gate-Anforderungen / Reassessment of All Gate Requirements

`Closed` bedeutet hier: Der Plan besitzt einen scope-treuen, ausfuehrbaren oder klar phasengebundenen Nachweis. Spaetere Implementierungs- und Remote-Gates behaupten noch keinen realen Ausfuehrungspass. / *Closed means that the plan has a scope-faithful executable or clearly phase-bound proof; later implementation and remote gates do not yet claim an execution pass.*

| Gate | R3-Status | Beurteilung / Assessment |
|---|---|---|
| `META01-G01-input-binding-bash` | Closed | Aktuell ausgefuehrt: drei Roh-Hashes plus Bash-Schema bestehen. / Executed and passed. |
| `META01-G02-input-binding-powershell` | Closed | Aktuell ausgefuehrt: drei Roh-Hashes plus PowerShell-Schema bestehen. / Executed and passed. |
| `META01-G03-global-ready-14` | Closed | Aktuell fuer alle 14 Ziele und beide Oberflaechen bestanden; erneute Ausfuehrung bleibt phasengebunden. / Passed and phase-bound for rerun. |
| `META01-G04-domain-contract` | Closed | Vertrag und Fixtures bestehen; der aktuelle Fail nennt erwartungsgemaess nur `SRC-163` bis `SRC-167`. / Contract is sound; only planned rows are missing. |
| `META01-G05-markdown-structure` | Closed | Rendererfolge und Homogeneity-Proof-Grenze bleiben kausal und ehrlich getrennt. / Renderer order and structure-only proof remain sound. |
| `META01-G06-independent-semantic-review` | Closed | Eigene Datei, Kriterienklasse, unabhaengige Rolle und Gate-Ausgang. / Separate evidence class, role, and outcome. |
| `META01-G06A-independent-accessibility-review` | Closed | Eigene Datei, A11Y-Kriterien, unabhaengige A11Y-Rolle und Gate-Ausgang. / Separate accessibility evidence, role, and outcome. |
| `META01-G07-secret-pattern-scans` | Closed | Scope behauptet nur Secret-Mustersuche. / Scope claims only pattern detection. |
| `META01-G08-independent-public-content-review` | Closed | Exakte Kandidatenabdeckung und Validierung erst nach bytegleichem Fixpunkt. / Exact coverage is validated only after the fixed point. |
| `META01-G09-documentation-impact` | Closed | Schema 1.1, genau ein Eintrag, einziges kanonisches Intake und exakte stabile Pfadmenge. / Correct schema, cardinality, source, and stable path set. |
| `META01-G10-aeps-outcome` | **Open (High)** | Finding-Pflichtfeldnamen werden erkannt, leere Pflichtwerte aber nicht fail-closed abgewiesen. / Labels are detected, but empty mandatory values are accepted. |
| `META01-G11-statistics` | Closed | Schreiben nach Implementierung und beide check-only-Oberflaechen bleiben gebunden. / Post-implementation render and both checks remain bound. |
| `META01-G12-exact-candidate` | Closed | Exakte Stage-, Porcelain-, Restdiff- und Whitespace-Abstimmung. / Exact staged/status/whitespace reconciliation. |
| `META01-G12A-candidate-fixed-point` | Closed | Zwei Ableitungen, bytegleiches `cmp`, Fixpunkt vor Evidence-Validierung und Stage. / Two derivations and fixed point precede validation and staging. |
| `META01-G13-pr-head-convergence` | Closed | All-Checks plus Required-Teilmenge, atomare Tokens, exakter Head, Threads und Approval-only-Bypass. / All checks, required subset, exact head, threads, and approval-only bypass. |
| `META01-N01-product-tests-runtime` | N/A accepted | Kein Produktcode oder Produkt-Runtime; Trigger vorhanden. / No product code or runtime; trigger present. |
| `META01-N02-supply-chain` | N/A accepted | Keine Dependency-, Build-, Paket-, AI-Runtime- oder Release-Ausgabe; Trigger vorhanden. / No applicable supply-chain output; trigger present. |
| `META01-N03-script-platform-parity` | N/A accepted | Kein neues Bash-/PowerShell-Produkttool; vorhandene Paare bleiben Pruefoberflaechen. / No new product script pair. |
| `META01-N04-agent-parity-presets-level0` | N/A accepted | Shared Guidance, Presets, Level 0 und Home Sync bleiben ausserhalb des Scopes. / Shared guidance, presets, level 0, and Home Sync remain out of scope. |

## Abschlussbedingung vor Tasks / Closure Required Before Tasks

Vor Tasks muss R2-H02 minimal repariert und mit einem neuen isolierten Leerwert-Negativfall erneut ausgefuehrt werden. Danach sind beide Input-Bindungen und `global-ready` unmittelbar neu auszufuehren. Jede zwischenzeitliche Target-, Review-, Receipt-, Authority- oder Evidence-Drift stoppt fail-closed. R2-H01, R2-H03 und R2-M01 benoetigen keine weitere Remediation, solange ihre geprueften Artefakte nicht driften. / *Before Tasks, R2-H02 must be minimally repaired and rerun with an isolated empty-value negative case. Both input bindings and global-ready must then be rerun immediately. Any intervening drift fails closed. The other three R2 findings require no further remediation unless their reviewed artefacts drift.*

## Endurteil / Final Verdict

**NeedsRemediation**
