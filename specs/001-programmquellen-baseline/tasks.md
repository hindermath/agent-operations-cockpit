# Aufgaben: Programmquellen-Baseline / Tasks: Program Sources Baseline

**Eingabe / Input**: Akzeptierte Design-Artefakte unter `specs/001-programmquellen-baseline/` sowie die gebundene Constitution unter `.specify/memory/constitution.md`. / Accepted design artefacts under `specs/001-programmquellen-baseline/` and the bound constitution under `.specify/memory/constitution.md`.

**Scope**: Ausschliesslich Dokumentation und Governance fuer `META-LH-01`: sechs gebundene Baseline-Dokumente, feature-lokale Workflow-Evidence, genau ein Lifecycle-Datensatz, genau eine Documentation-Impact-Entscheidung, AEPS-Ausgang, generiertes Skriptinventar, gerenderte Projektstatistik, normaler Kandidaten-Commit, terminaler byteidentischer Original-zu-Archiv-Rename-Commit und der autorisierte spaetere `MergeAndSync`-Closeout. Produktimplementierung, Scaffold, Produkt-Runtime, Dependencies, Preset-/Level-0-Aenderungen, Home-Sync und andere Intakes bleiben ausgeschlossen. / Documentation and governance only for META-LH-01, including one lifecycle record and the constitutional terminal rename; all named non-goals remain excluded.

**Tests / Pruefprinzip**: Die 66 isolierten Vertragsfaelle bewahren alle vorhandenen 43 Faelle und ergaenzen genau 23 Snapshot-Faelle: drei positive Post-Implement-Oberflaechen sowie negative pre-Implement-Drift-, Stage-/Status-/Gate-, Zielmengen-/Reihenfolge-, Pfad-/Hash-/Byte-, Ready-/Leaf- und Run-/Branch-/Lifecycle-Grenzen. / The 66 isolated cases preserve all existing 43 and add exactly 23 snapshot cases.

## Format: `[ID] [P?] [Story] Beschreibung mit Pfad / Description with path`

- **[P]**: Kann nach Erfuellung der genannten Abhaengigkeiten parallel laufen, weil die Aufgabe nur liest oder einen disjunkten Pfad schreibt. / May run in parallel after its dependencies because it is read-only or writes a disjoint path.
- **[Story]**: Ordnet eine Aufgabe der User Story aus `spec.md` zu. / Maps a task to the user story from `spec.md`.
- Jede schreibende Aufgabe beginnt erst nach einer unmittelbar frischen Branch-, Run-State-, Authority-, Scope- und Input-Binding-Pruefung gemaess `quickstart.md`; Drift fuehrt zu `Stop`. / Every writing task starts only after a fresh branch, run-state, authority, scope, and input-binding check under `quickstart.md`; drift results in `Stop`.
- `N/A` bleibt `Not Assessed` und benoetigt Begruendung, Evidence-Pfad, Owner, Reviewer, Restluecke, Follow-up und Neubewertungs-Trigger; `Open` benoetigt zusaetzlich Owner, Follow-up und Trigger und darf hier nicht stillschweigend entstehen. / `N/A` remains `Not Assessed` and needs complete audit evidence; any `Open` result needs an owner, follow-up, and trigger.

## Phase 1: Setup und Laufbindung / Setup and Run Binding

**Zweck / Purpose**: Die akzeptierten Eingaben, die 20 Gate-Anforderungen und die Tasks-zu-Analyze-Grenze fail-closed binden. / Bind accepted inputs, all twenty gates, and the Tasks-to-Analyze boundary fail closed.

- [ ] T001 Pruefe Branch `001-programmquellen-baseline`, Run-State `specs/001-programmquellen-baseline/autonomous-run-state.json`, Checkpoint-Ancestry, `acceptedArtifactLifecycle` und die drei akzeptierten logischen Artefakte gemaess Abschnitt 1 in `specs/001-programmquellen-baseline/quickstart.md`; stoppe bei jeder Pfad-, Hash-, Receipt-, Review-, Run-ID-, Branch- oder Evidence-Drift. / Verify branch, run state, lifecycle binding, checkpoint ancestry, and all three logical accepted artefacts; stop on drift.
- [ ] T002 [P] Fuehre `input-bindings --surface bash` mit `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` aus und bewahre die einzelne `PASS`-Zeile bis T004 in `/tmp/001-programmquellen-baseline-input-binding-bash.txt` auf. / Run the Bash input binding and retain its result outside the repository.
- [ ] T003 [P] Fuehre `input-bindings --surface powershell` mit `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` aus und bewahre die einzelne `PASS`-Zeile bis T004 in `/tmp/001-programmquellen-baseline-input-binding-powershell.txt` auf. / Run the PowerShell input binding and retain its result outside the repository.
- [ ] T004 Erzeuge `specs/001-programmquellen-baseline/checklists/implementation-validation.md` als DE-first/EN-second Evidence-Matrix fuer alle 20 eindeutigen Gate-IDs aus `specs/001-programmquellen-baseline/autonomous-run-gate-requirements.json`, uebernimm T002/T003 und erfasse getrennt Applicability, Umsetzung, Begruendung, Command/Runner, Evidence, Owner, Reviewer, Restrisiko, Follow-up und Neubewertungs-Trigger. / Create the audit-ready implementation matrix for all twenty unique gates and bind both input results.
- [ ] T005 Dokumentiere in `specs/001-programmquellen-baseline/checklists/implementation-validation.md` die vier Gate-Nachweise `META01-N01-product-tests-runtime`, `META01-N02-supply-chain`, `META01-N03-script-platform-parity` und `META01-N04-agent-parity-presets-level0` als `N/A`/`Not Assessed` mit Begruendung und Trigger; erfasse ASVS, Supply Chain, Architektur/Cloud/Regulierung weiterhin begruendet `N/A`, NIST SSDF/CWE anwendbar und Lastenheft-Archivierung ausdruecklich `Applicable`/`Partly Fulfilled`. Uebernimm den installierten Preset-Versionsdelta-Audit aus `autonomous-run-state.json`, ohne eine Version zu aendern. / Record all N/A gates, keep SSDF/CWE applicable, mark archival applicable, and carry forward the read-only installed-version delta audit without changing presets.
- [ ] T006 Validiere `specs/001-programmquellen-baseline/intake-lifecycle.json` als Schema 1.1 mit dem unveraenderten einzigen `recordVersion: 1.0`-META-LH-01-Datensatz und genau einem nicht selbstreferenziellen 14-Ziel-Programmevidence-Snapshot; pruefe exakte Reihenfolge, eindeutige Pfade/Leaves, Ziel-/Receipt-/Review-Hashes, Run-ID, Branch und aktuelle Originalpfad-Aufloesung. / Validate schema 1.1, the preserved unique lifecycle record, and the exact ordered fourteen-target immutable snapshot.

## Phase 2: Foundational und Analyze-Grenze / Foundational and Analyze Boundary

**Zweck / Purpose**: Den vorhandenen Vertrag rot bestaetigen, Tasks unabhaengig analysieren lassen und unmittelbar vor Implement erneut das globale Gate pruefen. / Confirm the existing contract red, independently analyze the tasks, and recheck the global gate immediately before Implement.

**Kritischer Blocker / Critical blocker**: Keine Story-Umsetzung beginnt, bevor T007 bis T011 bestanden sind. / No story work begins before T007 through T011 pass.

- [ ] T007 Fuehre `python3 -B specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py` aus, verlange exakt `PASS: contract-tests: 66 isolated positive/negative cases` und protokolliere die bewahrten 43 sowie die 23 neuen Snapshot-/Drift-Proof-Grenzen in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`. / Run exactly 66 isolated cases and record the preserved 43 plus 23 snapshot boundaries.
- [ ] T008 Fuehre vor der Domain-Bearbeitung `python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . domain` aus und dokumentiere in `specs/001-programmquellen-baseline/checklists/implementation-validation.md` den erwarteten Exit 1 mit leerem stdout und genau einer stderr-Diagnose ausschliesslich fuer `SRC-163` bis `SRC-167`; jede andere Abweichung blockiert. / Capture the expected initial domain failure and reject every broader or different failure.
- [ ] T009 Fuehre unmittelbar vor jedem `/speckit-analyze`-Aufruf einschliesslich aller Wiederholungen `global-ready` aus und protokolliere jeden frischen Pass fuer vierzehn logische Ziele unter `META01-G03-global-ready-14`; bei Pfad-, Lifecycle- oder Evidence-Drift kein Analyze starten. / Run and record a fresh fourteen-logical-target gate immediately before every Analyze invocation.
- [ ] T010 Fuehre `/speckit-analyze` fuer `specs/001-programmquellen-baseline/spec.md`, `plan.md` und `tasks.md` aus, behebe ausschliesslich innerhalb der erneut autorisierten Feature-Artefakte materielle Inkonsistenzen und wiederhole T009 vor jedem erneuten Analyze, bis keine blockierende Inkonsistenz verbleibt. / Analyze the feature artefacts and rerun the fresh global gate before every analysis retry.
- [ ] T011 Fuehre unmittelbar vor `/speckit-implement` erneut `global-ready` aus `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` aus, bestaetige META-LH-01 als erstes Ziel und binde den Pass in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`; ohne frischen Pass keine Umsetzung. / Run the global gate again immediately before Implement and stop without a fresh pass.

**Checkpoint**: Die akzeptierten Eingaben und alle Vorphasen-Gates sind aktuell; die dokumentarische Umsetzung darf beginnen. / Accepted inputs and all pre-implementation gates are current; documentation delivery may begin.

---

## Phase 3: User Story 1 - Eigenstaendige Programmgrundlage verstehen / Understand the Self-contained Programme Baseline (Prioritaet / Priority: P1) MVP

**Ziel / Goal**: Zweck, Grenzen, Quellenrang, G-01/G-05/G-06 und genau eine sichere naechste Aktion werden allein aus Level 2 verstaendlich. / Purpose, boundaries, precedence, G-01/G-05/G-06, and exactly one safe next action are understandable from level 2 alone.

**Unabhaengige Pruefung / Independent Test**: Eine unabhaengige Person ohne Level-0-Lektuere liest den gebundenen Leserpfad und erklaert Scope, Nicht-Ziele, Quellenrang, die drei Gates und die naechste erlaubte Aktion korrekt; Produkt-, Preset- oder Folgeautoritaet wird nicht abgeleitet. / An independent reader without level-0 context correctly explains scope, non-goals, precedence, the three gates, and the next permitted action without deriving extra authority.

- [ ] T012 [P] [US1] Vervollstaendige in `requirements/baseline/source-pack.md` die 23 einzeln inventarisierten Programmquellen mit ID, Rolle, Inhaltsbeschreibung, Authority, Aktualitaet, Supersession-Status und Zielverwendung, DE zuerst/EN danach, ohne die fuenf numerischen Luecken oder eine notwendige Level-0-Abhaengigkeit. / Complete the exact self-contained source inventory.
- [ ] T013 [P] [US1] Vervollstaendige in `requirements/baseline/glossary.md` die gleichwertigen DE/EN-Erklaerungen fuer Authority, Evidence, Receipt, Coverage, Decision, Supersession und Stop-Gate auf CEFR-B2-Niveau fuer Erstlesende ohne Spec-Kit-Vorkenntnis. / Complete the bilingual first-reader glossary.
- [ ] T014 [P] [US1] Praezisiere in `requirements/baseline/authority-and-stop-gates.md` G-01, G-05 und G-06 jeweils mit erlaubter Aktion, fail-closed Stop-Bedingung, konkreter Evidence, getrennter menschlicher Entscheidung und genau einer sicheren naechsten Aktion; schliesse Produktcode-, Produktarchitektur-, Preset- und implizite Remote-Autoritaet aus. / Complete the three authority rows without granting downstream authority.
- [ ] T015 [US1] Schliesse den Leserpfad Source Pack -> Constraint Register -> Findings Ledger -> Coverage Matrix -> Glossar -> Authority/Stop Gates durch beschreibende Querverweise in `requirements/baseline/source-pack.md`, `requirements/baseline/glossary.md` und `requirements/baseline/authority-and-stop-gates.md`, ohne einen neuen Repository-Einstieg oder Home-Sync zu erzeugen. / Complete the descriptive reader-path links without adding a new entry point or distribution target.
- [ ] T016 [US1] Fuehre den unabhaengigen US1-Lesetest aus und protokolliere Pass/Fail, Rolle, Unabhaengigkeit, Begruendung und null blockierende Findings in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`; ein Fail blockiert US2/US3-Integration. / Record the independent US1 reader test with no blocking findings.

**Checkpoint**: US1 ist als eigenstaendiger Level-2-Leserpfad demonstrierbar und bildet den MVP. / US1 is demonstrable as a self-contained level-2 reader path and forms the MVP.

---

## Phase 4: User Story 2 - Quellen und Findings lueckenlos nachverfolgen / Trace Sources and Findings Completely (Prioritaet / Priority: P2)

**Ziel / Goal**: Alle 23 Quellen, `CON-01` bis `CON-25`, `RF-01` bis `RF-21`, ausdrueckliche Supersession und die exakte direkte META-LH-01-Menge sind ohne Erfindung oder Doppelzaehlung pruefbar. / All exact source, constraint, finding, supersession, and direct-ownership sets are traceable without invention or double counting.

**Unabhaengige Pruefung / Independent Test**: Eine unabhaengige Review-Rolle gleicht Source Pack, Ledger und Coverage Matrix ab; jede Source- und Finding-ID steht genau einmal in ihrer Einzelzeile, alle Pflichtfelder sind vorhanden, kein blocking Finding ist `Uncovered`, und `directMetaLh01=Yes` gilt exakt fuer die zehn gebundenen IDs. / An independent reviewer reconciles the exact sets and fields, with zero uncovered blocking findings and exactly ten direct META-LH-01 findings.

- [ ] T017 [P] [US2] Vervollstaendige `CON-01` bis `CON-25` in `requirements/baseline/constraint-register.md` mit gleichwertiger DE/EN-Bindung, Applicability/Evidence und Neubewertung fuer phasenbezogene N/A-Werte, ohne neue Produktconstraints. / Complete all twenty-five bilingual constraints without adding product scope.
- [ ] T018 [P] [US2] Vervollstaendige fuer jede Einzelzeile `RF-01` bis `RF-21` in `requirements/baseline/review-findings-ledger.md` Severity, Aussage und Quelle, Owner, Ziel, Akzeptanzkriterium, positive Evidence, negative Evidence, Status und Restluecke DE/EN; bewahre `Covered` als Requirements-Abdeckung ohne Implementierungs- oder Wirksamkeitsbehauptung. / Complete every finding row and preserve the proof boundary of Covered.
- [ ] T019 [P] [US2] Vervollstaendige in `requirements/baseline/coverage-matrix.md` je eine Einzelzeile fuer alle 23 Source-IDs und `RF-01` bis `RF-21`, einschliesslich `SRC-ES-01` und `SRC-163` bis `SRC-167`, und setze direkte META-LH-01-Verantwortung exakt fuer `RF-01`, `RF-04`, `RF-11` bis `RF-17` und `RF-21`. / Complete exact per-ID source and finding coverage with exactly ten direct findings.
- [ ] T020 [US2] Gleiche `requirements/baseline/source-pack.md`, `requirements/baseline/review-findings-ledger.md` und `requirements/baseline/coverage-matrix.md` zeilenweise gegen die Mengen und Felder in `specs/001-programmquellen-baseline/contracts/baseline-validation-contract.md` ab; entferne keine bestaetigte Decision und aendere Authority/Supersession nur mit ausdruecklichem Revisionsgrund. / Reconcile the three artefacts against the exact contract without implicit supersession.
- [ ] T021 [US2] Fuehre den unabhaengigen US2-Traceability-Test aus und protokolliere exakte 23/25/21/10-Mengen, null Doppelzaehlungen, null erfundene Luecken und null blocking `Uncovered` in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`. / Record the independent exact-set traceability test.

**Checkpoint**: US2 ist gegen Source Pack, Ledger und Coverage Matrix unabhaengig pruefbar. / US2 is independently testable across the source pack, ledger, and coverage matrix.

---

## Phase 5: User Story 3 - Zugaengliche Governance sicher anwenden / Apply Accessible Governance Safely (Prioritaet / Priority: P3)

**Ziel / Goal**: Die sechs Domain-Dokumente sind DE-first/EN-second, CEFR B2, text-first und WCAG-2.2-AA-orientiert nutzbar; Semantik und Accessibility bleiben zwei getrennte unabhaengige Proof-Klassen. / The six domain documents are bilingual, CEFR B2, text-first, and WCAG 2.2 AA-oriented, with separate semantic and accessibility proof classes.

**Unabhaengige Pruefung / Independent Test**: Zwei voneinander und von der Umsetzung unabhaengige Rollen pruefen alle sechs Domain-Pfade sowie den nutzerlesbaren Pending-Closeout-Anker getrennt fuer Semantik und Accessibility; beide liefern null blocking Findings. / Two separate roles review the six domain paths and readable Pending closeout anchor with zero blocking findings.

- [ ] T022 [US3] Fuehre nach T012 bis T021 `python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . domain` aus, verlange genau eine `PASS`-Zeile fuer `META01-G04-domain-contract` und protokolliere damit den Rot-Gruen-Uebergang in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`. / Require the domain contract to turn from the expected failure to one PASS.
- [ ] T023 [P] [US3] Lasse eine unabhaengige semantische Review-Rolle in `specs/001-programmquellen-baseline/semantic-review-evidence.json` genau eine begruendete Pass/Fail-Zeile je Domain-Pfad plus `causal-closeout-evidence.json` fuer DE-first, EN-Gleichwertigkeit, CEFR B2, Erstnutzungsbegriffe, fachliche Wahrheit und Authority-Auslegung erfassen; null blocking Findings sind Pflicht. / Create semantic evidence for the six domain paths plus the readable closeout anchor.
- [ ] T024 [P] [US3] Lasse eine von T023 getrennte unabhaengige A11Y-Review-Rolle in `specs/001-programmquellen-baseline/accessibility-review-evidence.json` genau eine begruendete Pass/Fail-Zeile je Domain-Pfad plus `causal-closeout-evidence.json` fuer strukturierte Lesereihenfolge, beschreibende Felder/Links, Text-first, Status ohne Nur-Farbe und WCAG-2.2-AA-Anwendbarkeit erfassen; null blocking Findings sind Pflicht. / Create accessibility evidence for the six domain paths plus the readable closeout anchor.
- [ ] T025 [US3] Lasse die semantische Review-Rolle Ergebnis, Begruendungen, Unabhaengigkeit und null blockierende Findings in `specs/001-programmquellen-baseline/semantic-review-evidence.json` final abnehmen; die Maschinenvalidierung folgt nach der von ihrem CLI-Vertrag verlangten Kandidatenliste in T038. / Finalise the independent semantic assessment; machine validation follows after candidate set one exists.
- [ ] T026 [US3] Lasse die getrennte A11Y-Review-Rolle Ergebnis, Begruendungen, Unabhaengigkeit und null blockierende Findings in `specs/001-programmquellen-baseline/accessibility-review-evidence.json` final abnehmen; die Maschinenvalidierung folgt nach der von ihrem CLI-Vertrag verlangten Kandidatenliste in T039. / Finalise the independent accessibility assessment; machine validation follows after candidate set one exists.
- [ ] T027 [US3] Fuehre den unabhaengigen US3-Lernendenpfad-Test fuer Voraussetzungen, Grenzen, Begriffe, Status und genau eine sichere naechste Aktion ohne Farbe, Grafik, Plattform- oder Spec-Kit-Vorwissen aus und protokolliere null blocking Abweichungen in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`. / Record the independent first-year learner-path test.

**Checkpoint**: Alle drei User Stories sind fachlich getrennt pruefbar; die sechs Domain-Dokumente bestehen den Domain-, Semantik- und Accessibility-Pfad. / All three stories are independently testable and the six domain documents pass domain, semantic, and accessibility validation.

---

## Phase 6: Generierte Evidence und kausaler Kandidaten-Fixpunkt / Generated Evidence and Causal Candidate Fixed Point

**Zweck / Purpose**: Alle verbleibenden lokalen Evidence-Pfade erzeugen, danach die Kandidatenmenge zweimal bytegleich einfrieren und erst dann Public Content sowie Documentation Impact validieren. / Produce all remaining local evidence, freeze the candidate set twice byte-identically, and only then validate public content and documentation impact.

- [ ] T028 Fuehre die Vorschauen `bash scripts/render-script-reference.sh --repo . --dry-run` und `pwsh -NoProfile -File scripts/render-script-reference.ps1 -Repo . -WhatIf` fuer den Python-Vertrag samt `causal-closeout`-Modus, dessen Eingabe `causal-closeout-evidence.json` und den Test aus; bestaetige, dass nur `docs/scripts/embedded-scripts.md` und nicht `docs/scripts/reference.md` aktualisiert wird. / Preview the generated embedded-script inventory including the causal-closeout mode and evidence input.
- [ ] T029 Rendere `docs/scripts/embedded-scripts.md` mit `scripts/render-script-reference.ps1` und bestehe danach beide Check-only-Oberflaechen `bash scripts/render-script-reference.sh --repo . --check-only` und `pwsh -NoProfile -File scripts/render-script-reference.ps1 -Repo . -CheckOnly`; erfasse Vorschau, Rendererfolg und beide Checks unter `META01-G05-markdown-structure` in `specs/001-programmquellen-baseline/checklists/implementation-validation.md`. / Render the embedded-script inventory and pass both check-only surfaces.
- [ ] T030 Fuehre `scripts/check-homogeneity.sh --json --dry-run --no-patch .` und `scripts/check-homogeneity.ps1 -TargetDir . -Json -DryRun -NoPatch` aus und dokumentiere beide Ergebnisse in `specs/001-programmquellen-baseline/checklists/implementation-validation.md` ausschliesslich als deterministische Markdown-Struktur- und Repository-Konventionspruefung. / Run both homogeneity surfaces without claiming semantic or accessibility proof.
- [ ] T031 Pruefe den Trigger und den Deduplizierungsschluessel gegen `docs/aeps/findings-ledger.md` sowie `docs/aeps/README.md`, binde Quelle und normalisierten Hash und entscheide genau einen Ausgang `Finding` oder begruendetes `NoChange` fuer `docs/aeps/receipts/meta-lh-01-programmquellen-implementation.md`. / Deduplicate the AEPS trigger and select exactly one bounded outcome.
- [ ] T032 Erzeuge `docs/aeps/receipts/meta-lh-01-programmquellen-implementation.md` mit genau einem `aeps-outcome-json`-Block, maximalem Einzel-AOC-Reifegrad `candidate`, `presetPromotion: false` und `level0Handoff: false`; aktualisiere `docs/aeps/findings-ledger.md` nur bei `Finding` um genau einen vollstaendigen kanonischen Abschnitt, waehrend `NoChange` das Ledger bytegleich laesst. / Create one AEPS receipt and conditionally one complete ledger section, with promotion and handoff false.
- [ ] T033 Validiere `docs/aeps/receipts/meta-lh-01-programmquellen-implementation.md` mit dem `aeps`-Modus aus `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` und protokolliere Source-/Receipt-Pfade, Hash, Deduplizierung, Statusachsen, Reifegrad, reale Datumsbindung und Promotion-/Handoff-Grenzen unter `META01-G10-aeps-outcome`. / Validate the full AEPS ledger/receipt contract.
- [ ] T034 Rendere nach abgeschlossener Implementierung Profil 2 aus `docs/project-statistics.config.json` mit `bash scripts/render-project-statistics.sh --repo .` nach `docs/project-statistics.md`; bewahre ASCII-, 100-Zeichen-, Phasenslot-, Methodik-v2- und DE/EN-Textalternativ-Vertrag. / Render the project statistics from the canonical configuration.
- [ ] T035 Fuehre fuer `docs/project-statistics.md` beide Check-only-Oberflaechen `bash scripts/render-project-statistics.sh --repo . --check-only` und `pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly` aus und protokolliere beide Pass-Ergebnisse unter `META01-G11-statistics`. / Pass both statistics check-only surfaces.
- [ ] T036 Bestaetige den bereits im akzeptierten Feature-Kandidaten vorhandenen `Pending`-Anker `specs/001-programmquellen-baseline/causal-closeout-evidence.json`; lege erst nach T028 bis T035 die zwei weiteren Pfadanker `public-content-review-evidence.json` und `documentation-impact-evidence.json` an, ohne weitere Lieferpfade zu erzeugen. / Preserve the already-present Pending causal anchor and create only the two remaining anchors.
- [ ] T037 Erzeuge mit `candidate-list` und `specs/001-programmquellen-baseline/contracts/candidate-paths.json` die erste exakte, reviewte Sollmenge in `/tmp/001-programmquellen-baseline-expected-paths.txt`, pruefe jeden Pfad gegen Scope und tatsaechlichen Worktree und friere die Datei als Kandidatenmenge eins ein. / Render and review candidate set one outside the repository.
- [ ] T038 Validiere nach T037 `specs/001-programmquellen-baseline/semantic-review-evidence.json` mit `review-evidence --kind semantic --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` aus `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` und halte fest, dass der Modus Evidence-Vollstaendigkeit, nicht semantische Wahrheit beweist. / Validate semantic evidence after the CLI-required expected-paths file exists.
- [ ] T039 Validiere nach T037 `specs/001-programmquellen-baseline/accessibility-review-evidence.json` mit `review-evidence --kind accessibility --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` aus `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py` und halte die getrennte A11Y-Proof-Grenze in `specs/001-programmquellen-baseline/checklists/implementation-validation.md` fest. / Validate accessibility evidence after the CLI-required expected-paths file exists.
- [ ] T040 Fuehre `gitleaks dir --redact --no-banner --no-color` getrennt fuer `requirements/baseline` und `specs/001-programmquellen-baseline` sowie beide Oberflaechen `scripts/scan-agent-secrets.sh --fail-on-high .` und `scripts/scan-agent-secrets.ps1 -FailOnHigh -WorkspaceRoot .` aus; dokumentiere unter `META01-G07-secret-pattern-scans` nur Secret-Pattern-Ergebnisse, keine umfassende Publikationseignung oder Personendatenfreiheit. / Run the three secret-pattern surfaces without overstating their proof.
- [ ] T041 Lasse eine dritte, von Semantik und A11Y getrennte unabhaengige Rolle `public-content-review-evidence.json` fuer exakt jeden normalen Kandidatenpfad einschliesslich `causal-closeout-evidence.json` plus Lifecycle-Datensatz, Original- und Archivpfad mit begruendeten Pass/Fail-Kriterien vervollstaendigen. / Complete public-content evidence including the Pending causal anchor and lifecycle transition.
- [ ] T042 Vervollstaendige `documentation-impact-evidence.json` als Schema 1.1 mit exakt einem `UpdateRequired`-Eintrag und `documents` gleich Kandidatenmenge eins einschliesslich `causal-closeout-evidence.json` plus Lifecycle-Datensatz, Original- und Archivpfad; keine zweite Decision. / Complete one UpdateRequired record including the Pending causal anchor and lifecycle transition.
- [ ] T043 Erzeuge mit `candidate-list` die zweite Sollmenge `/tmp/001-programmquellen-baseline-expected-paths-r2.txt` und verlange mit `cmp` Bytegleichheit zu `/tmp/001-programmquellen-baseline-expected-paths.txt`; jede neue, fehlende oder entfernte Datei startet T036 bis T043 neu. / Render candidate set two and require byte equality.
- [ ] T044 Fuehre `candidate-fixpoint --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` aus und protokolliere den Pass unter `META01-G12A-candidate-fixed-point`, bevor Public-Content- oder Documentation-Impact-Validatoren laufen. / Prove the stable worktree fixed point before either dependent validator.
- [ ] T045 Validiere nach T044 `specs/001-programmquellen-baseline/public-content-review-evidence.json` mit `review-evidence --kind public --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` und dokumentiere unter `META01-G08-independent-public-content-review`, dass der Validator Evidence-Vollstaendigkeit und nicht Publikationseignung selbst beweist. / Validate public-content evidence only after the fixed point.
- [ ] T046 Validiere nach T044 `specs/001-programmquellen-baseline/documentation-impact-evidence.json` mit `documentation-impact --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` sowie explizit mit `scripts/validate-documentation-impact.sh` und `scripts/validate-documentation-impact.ps1`; verlange auf beiden installierten Validatoroberflaechen exakt eine `UpdateRequired`-Entscheidung und vollstaendige Pfadgleichheit. / Validate Documentation Impact with the feature contract and both installed surfaces.
- [ ] T047 Fuehre den kompletten lokalen Pre-Rename-Regressionssatz erneut aus: 66 Vertragsfaelle, beide snapshot-qualifizierten Input-Bindings, snapshot-qualifiziertes `global-ready`, beide State-Validatoren, `domain`, Kandidatenmengen/Fixpunkt, Skriptinventar/Homogeneity, AEPS, Statistik, Secret-Muster, drei Review-Evidence-Modi, Documentation Impact, JSON-/Python-Syntax und `git diff --check`; schliesse alle 16 `Applicable`- und vier `N/A`-Gate-Zeilen ohne unbegruendetes `Open`. / Rerun the complete affected regression with 66 cases and the qualified snapshot proof.

**Checkpoint**: Die lokale Kandidatenmenge ist stabil, alle Proof-Klassen sind getrennt und alle 20 Gate-Anforderungen besitzen konkrete Evidence oder einen begruendeten N/A-Nachweis. / The local candidate set is stable and all twenty gates have concrete evidence or justified N/A evidence.

---

## Phase 7: Polish, terminaler Rename und Remote-Konvergenz / Polish, Terminal Rename, and Remote Convergence

**Zweck / Purpose**: Den stabilen normalen Kandidaten zuerst committen, danach als letzte Polish-Aktion den terminalen Rename-Commit erzeugen und ausschliesslich diesen unveraenderten Head publizieren, reviewen und mergen. / Commit the normal candidate first, then create the terminal rename as the last Polish action and publish/review only that immutable head.

- [ ] T048 Revalidiere unmittelbar vor Staging aktuelle Benutzerautoritaet, Branch, Scope, Run-State, beide Input-Binding-Oberflaechen fuer alle drei akzeptierten Artefakte, den letzten `global-ready`-Pass und Kandidaten-Fixpunkt; protokolliere die Freigabegrenze in `specs/001-programmquellen-baseline/checklists/implementation-validation.md` und stoppe bei Drift. / Revalidate authority and every mutable binding immediately before staging.
- [ ] T049 Stage jeden Pfad aus `/tmp/001-programmquellen-baseline-expected-paths.txt` einzeln mit `git add -- <path>` ohne Verzeichnis-, Punkt- oder Glob-Staging und lasse alle fremden Aenderungen ungestaged sowie unberuehrt. / Stage each frozen path explicitly and preserve unrelated work.
- [ ] T050 Fuehre `candidate --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt` aus und verlange exakte Gleichheit von Allowlist-Teilmenge, Porcelain einschliesslich untracked, Stage-Namen und null unstaged Kandidatenresten sowie einen erfolgreichen `git diff --cached --check`; protokolliere den Pass unter `META01-G12-exact-candidate`. / Reconcile the exact staged candidate and pass the staged whitespace check.
- [ ] T051 Revalidiere unmittelbar vor dem Commit erneut Authority, Scope, Hashes, Evidence, exakten Stage und `git diff --cached --check`; erstelle danach genau einen Conventional-Commit fuer den eingefrorenen normalen Kandidaten mit dem exakten Trailer, pruefe die gespeicherte Commit-Message und erfasse die HEAD-ID in `/tmp/001-programmquellen-baseline-normal-head.txt`. / Commit the frozen normal candidate first and capture its head.
- [ ] T052 Pruefe eine saubere autorisierte Feature-Schreibflaeche, den existierenden Originalpfad, den fehlenden Archivpfad und die byte-/hashgebundene Lifecycle-Evidence; fuehre danach als letzte Polish-Aktion `bash scripts/rename-lastenheft.sh requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md 001-programmquellen-baseline` aus. Das Script erzeugt den letzten Feature-Branch-Commit; danach ist jede weitere Feature-Head-Mutation verboten. / Run the constitutional rename script as the last Polish action and final feature-branch commit.
- [ ] T053 Erfasse den terminalen Head in `/tmp/001-programmquellen-baseline-terminal-head.txt`, fuehre `terminal-rename` aus und verlange exakt einen byteidentischen `R100`-Rename vom Original- zum Archivpfad, den exakten Co-Author-Trailer, null Stage-Reste, bestandene beide archivbewusste Input-Bindings und `global-ready`; jede Abweichung stoppt vor Push. / Validate the exact terminal commit and archived state before push.
- [ ] T054 Erzeuge und validiere den Feature-PR-Body mit den vier verpflichtenden Inhaltsklassen; das Inventar nennt normale Pfadliste, Pending-Closeout-Anker, Lifecycle-Datensatz und Rename, ohne spaetere Closeout-Fakten zu behaupten. / Build the four-part feature PR body including the Pending anchor without future closeout claims.
- [ ] T055 Revalidiere unmittelbar vor Push und PR erneut Authority und den terminalen Head aus `/tmp/001-programmquellen-baseline-terminal-head.txt`, pushe ausschliesslich Branch `001-programmquellen-baseline`, erstelle oder aktualisiere den Pull Request mit `--body-file` und belege mit `gh pr view`, dass `headRefOid` exakt diesem terminalen Head entspricht. / Push only the terminal head and prove exact PR-head equality.
- [ ] T056 Lasse mit `gh pr checks --watch --fail-fast` alle Checks terminal werden, erfasse All-Checks und die nichtleere Required-Teilmenge unter `/tmp/001-programmquellen-baseline-all-checks.json` und `/tmp/001-programmquellen-baseline-required-checks.json` und validiere beide Inventare mit `check-inventory` aus `specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py`; auch jeder nicht-required Check muss `pass` oder `skipping` sein. / Require every reported check, including non-required checks, to be terminal-successful.
- [ ] T057 Erfasse fuer denselben PR-Head `reviewDecision`, blockiere `CHANGES_REQUESTED`, frage alle Review-Threads mit paginiertem `gh api graphql --paginate --slurp` ab, bewahre das Ergebnis in `/tmp/001-programmquellen-baseline-review-state.json` auf und verlange null handlungsrelevante nicht-veraltete offene Threads; pruefe danach `headRefOid` erneut. / Converge review decision and all paginated actionable threads on the exact head.
- [ ] T058 Erfasse fuer jeden Check des exakten Heads Workflow-Definition, `gh run view`-Logs und Jobmetadaten unter `/tmp/001-programmquellen-baseline-*`, ordne tatsaechlich ausgefuehrte Commands und Runner unabhaengig den 15 Applicable-Gates zu und erzeuge `/tmp/001-programmquellen-baseline-execution-record.json` ohne Check-Namen als alleinigen Ausfuehrungsbeweis. / Derive executed commands and runners from definitions or logs into the temporary execution record.
- [ ] T059 Rendere aus `specs/001-programmquellen-baseline/autonomous-run-gate-requirements.json`, dem Execution Record und dem exakten Head `/tmp/001-programmquellen-baseline-gate-evidence.json` mit `render-gate-evidence` und validiere sie fuer denselben Head mit beiden Oberflaechen `validate-autonomous-gate-evidence.sh` und `validate-autonomous-gate-evidence.ps1`. / Render and validate provider-neutral exact-head evidence with both surfaces.
- [ ] T060 Pruefe nach T059 PR-Head, alle Checks, Required-Teilmenge, Review-Decision und paginierte Threads erneut und aktualisiere `/tmp/001-programmquellen-baseline-review-state.json`; jede Drift verwirft Execution Record und Gate-Evidence und beginnt beim betroffenen Remote-Gate neu. / Re-converge every mutable remote token after exact-head evidence.
- [ ] T061 Pruefe den normalen Mergepfad: verlange fuer den unveraenderten Head eine aktuelle unabhaengige `APPROVED`-Entscheidung sowie alle Ergebnisse aus T056 bis T060 und dokumentiere in `/tmp/001-programmquellen-baseline-review-state.json` entweder die normale Merge-Freigabe oder exakt, dass fehlende Approval der einzige verbleibende Blocker ist. / Prefer and fully evaluate the normal independent-approval merge path.
- [ ] T062 Verwende den Admin-Fallback ausschliesslich dann, wenn T061 beweist, dass unabhaengige Approval der einzige verbleibende Blocker ist und Authority, Exact Head, alle Checks einschliesslich nicht-required, beide Gate-Evidence-Validatoren, keine Change Request und null actionable Threads weiterhin bestehen; andernfalls erfasse fuer diesen Fallback einen begruendeten N/A-Nachweis in `/tmp/001-programmquellen-baseline-review-state.json`. / Permit admin fallback only for the approval-only blocker, otherwise record justified N/A.
- [ ] T063 Fuehre nach erneuter unmittelbarer Authority- und Drift-Pruefung genau einen Mergepfad aus: normal `gh pr merge --merge --delete-branch` bei `APPROVED`, andernfalls nur unter T062 `gh pr merge --merge --delete-branch --admin`; mische beide Pfade nicht und erfasse Merge-Commit sowie Branch-Cleanup spaeter in `specs/001-programmquellen-baseline/autonomous-run-state.json` als Post-Merge-Fakten, nicht als Pre-Merge-Primary-Evidence. / Execute exactly one authorised merge path and keep merge facts out of pre-merge evidence.

---

## Phase 8: Post-Merge-Fast-forward und finaler Closeout / Post-Merge Fast-forward and Final Closeout

**Zweck / Purpose**: Feature-Merge und `main` kausal synchronisieren, danach genau eine separate Drei-Pfad-Closeout-Transaktion als dauerhaftes Completion-Artefakt erzeugen. / Synchronize the feature merge and then create exactly one durable three-path closeout transaction.

- [ ] T064 Wechsle nach bestaetigtem Feature-Merge auf `main`, fuehre `git pull --ff-only` aus, belege Feature-Merge-SHA und `main...origin/main = 0 0`, verlange einen sauberen Worktree und erzeuge danach ausschliesslich Branch `codex/001-programmquellen-baseline-closeout` von diesem synchronisierten `main`. / Fast-forward main, prove convergence, and create only the pre-named closeout branch.
- [ ] T065 Fuehre vor jeder terminalen Behauptung die vollstaendige archivbewusste Finalvalidierung aus: beide Input-Bindings, `global-ready`, 66 Vertragsfaelle, beide State-Validatoren, `domain`, Skriptinventar/Homogeneity, AEPS, Statistik, Secret-Pattern-Scans und `git diff --check`. Der Snapshot-Ersatz bleibt nur zulaessig, solange der Run-State weiterhin exakt `Implement`/`Active`/`GlobalReadyBeforeImplement` ist; andernfalls muss die strengere generische Receipt-Pruefung bestehen. Erfasse danach nur tatsaechliche Closeout-Fakten. / Validate first with 66 cases; the snapshot substitution remains limited to the exact qualified state.
- [ ] T066 Setze erst nach T065 jede T001-T066-Checkbox auf komplett, `tasks.completed == tasks.total == 66`, den realen Roh-SHA-256 der vollstaendig geprueften `tasks.md`, State Schema 1.1 `Completed` mit `stage: MergeAndSync`, terminalen Closeout-Feldern und `nextExactAction: N/A`. Stage exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`, fuehre `causal-closeout`, beide Run-State-Validatoren und `git diff --cached --check` aus und committe genau diese drei Pfade. Dieser Commit ist der letzte lokale Akt von T066. / Complete and commit exactly the validated three-path transaction as T066's last local act.

**Provider-Publikation nach T066 / Provider publication after T066**: Fuer den unveraenderten Drei-Pfad-Head einen Closeout-PR-Body in eine temporaere Datei schreiben. Unter den vier exakt einmal zu validierenden Ueberschriften `Betroffene Skripte und Dokumente / Affected scripts and documents`, `Manuelle Pruefung / Manual verification`, `Beispielausgabe / Sample output` und `Security-Risiko / Security risk` muss er als betroffene Pfade exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`, die tatsaechliche manuelle Verifikation, Beispielausgabe oder ein begruendetes `N/A` sowie eine ausdrueckliche Security-Risikoaussage nennen. Erst nach erfolgreicher Heading-Validierung den unveraenderten Head pushen und den separaten Closeout-PR mit `gh pr create --body-file` erstellen oder mit `gh pr edit --body-file` aktualisieren; dann exakten Head, unabhaengigen Review, alle Checks, nichtleere Required-Teilmenge und null actionable Threads verlangen; normal mergen oder nur den vorhandenen Approval-only-Admin-Fallback nutzen; Branch bereinigen; `main` fast-forward synchronisieren; `main...origin/main = 0 0` und sauberen Worktree extern belegen; Closeout-PR und Merge-SHA extern berichten. Keine neue Checkbox und keine Mutation des Closeout-Commits. / Write the immutable three-path closeout PR body to a temporary file, validate exactly once each of the four mandatory headings and their required content, and publish it only through `gh pr create --body-file` or `gh pr edit --body-file`; preserve exact-head, review, check, thread, bounded-merge, cleanup, and external-reporting requirements without another task or commit mutation.

---

## Abhaengigkeiten und Ausfuehrungsreihenfolge / Dependencies and Execution Order

### Phasenabhaengigkeiten / Phase Dependencies

- **Phase 1** startet nach dem bereits frisch bestandenen globalen 14er-Gate fuer Tasks und schliesst die Lifecycle-Bindung mit T006 ab. / Phase 1 starts after the fresh pre-Tasks global gate and closes lifecycle binding through T006.
- **Phase 2** haengt von Phase 1 ab und blockiert alle Stories; T009 muss unmittelbar vor T010 und jeder Analyze-Wiederholung laufen, T011 unmittelbar vor Implement. / Phase 2 blocks all stories and binds the fresh Analyze and Implement gates.
- **US1 und US2** haengen von Phase 2 ab und koennen bei disjunkten Dateien teilweise parallel bearbeitet werden; T015/T016 folgen T012 bis T014, T020/T021 folgen T017 bis T019. / US1 and US2 may partially proceed in parallel after Phase 2.
- **US3** haengt von abgeschlossener US1 und US2 ab; T022 muss vor den unabhaengigen Reviews bestehen, T025 folgt T023 und T026 folgt T024. / US3 depends on completed US1 and US2.
- **Phase 6** haengt von allen Stories ab und ist strikt kausal: T028 -> T029 -> T030; T031 -> T032 -> T033; T034 -> T035; danach T036 -> T037 -> T038/T039/T040/T041/T042 -> T043 -> T044 -> T045/T046 -> T047. / Phase 6 follows the binding fixed-point order.
- **Phase 7** haengt von T047 ab und ist strikt sequenziell: Authority -> normaler Stage/Kandidat -> normaler Commit T051 -> terminaler Rename T052 -> terminaler Nachweis T053 -> PR/Exact-Head/Review -> genau ein Mergepfad. Nach T052 ist jede Feature-Head-Mutation verboten. / Phase 7 strictly commits the normal candidate before the terminal rename and permits no later feature-head mutation.
- **Phase 8** beginnt erst nach bestaetigtem Feature-Merge; T064 -> T065 -> T066. Die Provider-Publikation folgt kausal ohne neue Task und ohne Mutation. / Phase 8 ends with the one closeout commit; publication follows without a new task or mutation.

### User-Story-Abhaengigkeiten / User Story Dependencies

- **US1 (P1)**: Keine Story-Abhaengigkeit nach Phase 2; allein demonstrierbarer MVP. / No story dependency after Phase 2; independently demonstrable MVP.
- **US2 (P2)**: Keine inhaltliche Abhaengigkeit von US1 fuer die drei disjunkten Kernartefakte; die integrierte Leserpfad- und Contract-Pruefung erfolgt erst nach beiden Stories. / Core files are independent of US1; integration follows both.
- **US3 (P3)**: Abhaengig von US1 und US2, weil beide unabhaengigen Reviews exakt alle sechs finalen Domain-Pfade bewerten. / Depends on US1 and US2 because both reviews cover all six final paths.

### Gate-Abdeckung / Gate Coverage

- `META01-G01-input-binding-bash`: T001, T002, T006 und Wiederholungen in T047/T048/T051/T053/T065.
- `META01-G02-input-binding-powershell`: T001, T003, T006 und Wiederholungen in T047/T048/T051/T053/T065.
- `META01-G03-global-ready-14`: T009 unmittelbar vor jedem Analyze, T011 unmittelbar vor Implement sowie T047/T048/T053/T065.
- `META01-G04-domain-contract`: T008 erwarteter Fail, T022 erwarteter Pass, T047/T065 Regression.
- `META01-G05-markdown-structure`: T028 bis T030 sowie T047/T065.
- `META01-G06-independent-semantic-review`: T023, T025 und T038.
- `META01-G06A-independent-accessibility-review`: T024, T026 und T039.
- `META01-G07-secret-pattern-scans`: T040 und T047/T065.
- `META01-G08-independent-public-content-review`: T041 und T045.
- `META01-G09-documentation-impact`: T042, T044 und T046.
- `META01-G10-aeps-outcome`: T031 bis T033.
- `META01-G11-statistics`: T034 und T035.
- `META01-G12-exact-candidate`: T048 bis T053 fuer normalen Kandidaten, terminalen Rename und dessen Nachweis.
- `META01-G12A-candidate-fixed-point`: T036, T037, T043 und T044.
- `META01-G13-pr-head-convergence`: T053 bis T063 fuer den unveraenderten terminalen Head.
- `META01-G14-causal-closeout`: T064 bis T066 sowie die checkboxfreie externe Provider-Publikation des unveraenderten Closeout-Heads.
- `META01-N01-product-tests-runtime`: T005 und Abschlussabgleich T047.
- `META01-N02-supply-chain`: T005 und Abschlussabgleich T047.
- `META01-N03-script-platform-parity`: T005 und Abschlussabgleich T047.
- `META01-N04-agent-parity-presets-level0`: T005 und Abschlussabgleich T047.

## Parallele Ausfuehrungsbeispiele / Parallel Execution Examples

### Setup

```text
Nach T001 parallel: T002 (Bash-Inputbindung) || T003 (PowerShell-Inputbindung)
```

### User Story 1

```text
Nach T011 parallel auf disjunkten Pfaden: T012 (source-pack.md) || T013 (glossary.md) || T014 (authority-and-stop-gates.md)
Danach sequenziell: T015 -> T016
```

### User Story 2

```text
Nach T011 parallel auf disjunkten Pfaden: T017 (constraint-register.md) || T018 (review-findings-ledger.md) || T019 (coverage-matrix.md)
Danach sequenziell: T020 -> T021
```

### User Story 3

```text
Nach T022 parallel mit getrennten Rollen und Dateien: T023 (semantic-review-evidence.json) || T024 (accessibility-review-evidence.json)
Danach: T025 folgt T023; T026 folgt T024; abschliessend T027
```

## Umsetzungsstrategie / Implementation Strategy

### MVP zuerst / MVP First

1. Phase 1 und Phase 2 vollstaendig abschliessen. / Complete Phases 1 and 2.
2. US1 mit T012 bis T016 liefern. / Deliver US1 through T012 to T016.
3. Stoppen und den unabhaengigen US1-Lesetest wiederholen; der MVP ist die eigenstaendige Level-2-Erklaerung von Zweck, Scope, Quellenrang und Stop-Gates. / Stop and repeat the independent US1 reader test; this self-contained explanation is the MVP.

### Inkrementelle Lieferung / Incremental Delivery

1. US1 liefert Orientierung und Authority-Grenzen. / US1 delivers orientation and authority boundaries.
2. US2 ergaenzt exakte Quellen-, Constraint-, Finding- und Coverage-Nachverfolgbarkeit. / US2 adds exact traceability.
3. US3 belegt getrennt Semantik und Accessibility fuer alle sechs Domain-Pfade. / US3 separately evidences semantics and accessibility.
4. Phase 6 schliesst generierte Evidence, AEPS, Statistik, Secret-Muster, das um die Lifecycle-Transition erweiterte Public-Content-/Documentation-Impact-Inventar und den normalen Kandidaten-Fixpunkt. / Phase 6 closes evidence and the normal fixed point with expanded lifecycle inventory.
5. Phase 7 committed zuerst den normalen Kandidaten, fuehrt den terminalen Rename als letzte Feature-Polish-Aktion aus und publiziert nur diesen Head. Phase 8 validiert archivbewusst und persistiert den Abschluss in genau einem separat reviewbaren Drei-Pfad-Commit; dessen Provider-Publikation folgt ohne weitere Task oder Mutation. / Phase 7 preserves the immutable feature head; Phase 8 persists completion in one separately publishable three-path closeout commit.
