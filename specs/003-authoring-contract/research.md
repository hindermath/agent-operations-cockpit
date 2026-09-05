# Forschung und Entscheidungen: Nachweisbarer Intake-Authoring-Vertrag

## Ergebnis / Result

Es bleibt keine umsetzungsrelevante technische Unbekannte. Die akzeptierte Spezifikation, beide Checklisten, die aktuelle Binding-Genehmigung, das gebundene Evidence-Inventar, die fünf Fachartefakte, ihre Validatoren und Fixtures sowie die bestehende Drei-Plattform-Pipeline liefern hinreichende Entscheidungsgrundlagen. Deshalb wurde kein unabhängiger Forschungsauftrag ausgelöst.

No implementation-relevant technical unknown remains. The accepted specification, both checklists, current binding approval, bound evidence inventory, five domain artefacts, their validators and fixtures, and the existing three-platform pipeline provide sufficient decision input. Therefore no independent research assignment was dispatched.

Die einzige Dokumentationsauswirkungsentscheidung ist `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`. Dieses Dokument trifft keine zweite Entscheidung.

The sole Documentation Impact decision is `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`. This document does not make a second decision.

## Entscheidung 1: Exakter Fachumfang / Decision 1: Exact domain scope

**Entscheidung**: Genau die folgenden fünf Fachartefakte werden in der vorgegebenen Reihenfolge geändert:

1. `.specify/presets/intake-authoring-governance/templates/intake-template.md`
2. `.specify/presets/intake-authoring-governance/templates/intake-authoring-receipt-template.json`
3. `.specify/presets/intake-authoring-governance/templates/project-profile-template.md`
4. `requirements/intake-governance.json`
5. `.specify/presets/intake-authoring-governance/templates/field-validation-summary.md`

**Begründung**: Nur diese Dateien bilden den in META-LH-03 benannten kanonischen Fachvertrag. Alle anderen Änderungen müssen nachweisbar notwendige Konsumenten oder Evidence sein.

**Verworfen**: Generische neue Features, ein neuer Intake, Änderungen am Produktcode, Preset-Versionen oder Level 0. Sie überschreiten Genehmigung und Spezifikation.

**Decision**: Exactly the five listed domain artefacts change in the prescribed order.

**Rationale**: Only these files form the canonical domain contract named by META-LH-03. Every other change must be a demonstrably necessary consumer or evidence artefact.

**Rejected**: Generic new features, a new intake, product-code changes, preset-version changes, or Level 0 work. They exceed the approval and specification.

## Entscheidung 2: Gesperrtes Receipt ist nicht ausführbar / Decision 2: A blocked receipt is not executable

**Entscheidung**: `NeedsClarification` zusammen mit gesperrtem Promptzustand enthält stabile Decision-IDs, in beiden Promptblöcken `BLOCKED` und `DO NOT RUN`, aber keine ausführbare `/speckit`- oder `$speckit`-Invocation. Platzhalter sind syntaktisch nicht ausführbar. Der vorhandene Receipt-Validator weist gesperrte Receipts mit ausführbar wirkenden Folgeaufrufen zurück. Bei `ReadyForReview` sind Specify- und Autonomous-Prompt kopierbar und auf exakt dasselbe Lastenheft gebunden, werden aber nicht ausgeführt und leiten keine aktuelle Authority aus historischen Werten ab. Die Validator-Fixture-Suite belegt beide positiven Zustände und die zugehörigen Negativfälle.

**Begründung**: Ein gesperrter Default darf weder menschlich noch maschinell als Folgeautorität fehlinterpretiert werden. Die Prüfung am Receipt ist näher an der Vertrauensgrenze als eine nachgelagerte reine Zieltextprüfung.

**Verworfen**: Nur erläuternder Prosa-Hinweis oder nur Prüfung, ob der Ziel-Intake die genaue Receipt-Zeile enthält. Beides lässt ausführbare Befehle im Receipt bestehen.

**Decision**: `NeedsClarification` with a blocked prompt state contains stable decision IDs and `BLOCKED` plus `DO NOT RUN` in both prompt blocks, but no executable `/speckit` or `$speckit` invocation. Placeholders are syntactically non-executable. The existing receipt validator rejects blocked receipts with executable-looking follow-up calls. At `ReadyForReview`, Specify and Autonomous prompts are copyable and bind the exact same intake, but are not executed and derive no current authority from historical values. The validator fixture suite proves both positive states and their corresponding negative cases.

**Rationale**: A blocked default must not be mistaken for follow-up authority by either people or machines. Receipt-level validation is closer to the trust boundary than downstream target-text-only validation.

**Rejected**: A prose warning alone or checking only whether the target intake contains the exact receipt line. Both leave executable commands in the receipt.

## Entscheidung 3: Portables Profil, aufgelöste AOC-Bindung / Decision 3: Portable profile, resolved AOC binding

**Entscheidung**: Die Preset-Projektprofil-Vorlage beschreibt portable Schlüssel und Regeln. Die AOC-Konfiguration bindet repository-spezifisch `requirements/baseline/intake-authoring-profile.md`, Profilidentität und `de-DE`-Sprachvertrag. Schema `2.0` bleibt bestehen, sofern die additive Bindung mit ihm kompatibel ist. Der Konfigurationsvalidator prüft Pfadgrenze, Existenz, Profilidentität und Sprachkonsistenz fail-closed.

**Begründung**: So bleibt das Preset wiederverwendbar, während das AOC eine eindeutige aufgelöste Policy besitzt.

**Verworfen**: AOC-Pfade in die portable Vorlage einbauen oder eine unnötige Schema-/Preset-Versionserhöhung. Beides vergrößert den Scope ohne fachlichen Nutzen.

**Decision**: The preset project-profile template defines portable keys and rules. The AOC configuration binds `requirements/baseline/intake-authoring-profile.md`, profile identity, and the `de-DE` language contract at repository level. Schema `2.0` remains when the additive binding is compatible. The configuration validator checks path boundary, existence, profile identity, and language consistency fail-closed.

**Rationale**: This keeps the preset reusable while giving AOC one unambiguous resolved policy.

**Rejected**: Embedding AOC paths in the portable template or making an unnecessary schema/preset version bump. Both expand scope without domain value.

## Entscheidung 4: Historische Reparatur bleibt unveränderlich / Decision 4: Historical repair stays immutable

**Entscheidung**: Vor Tasks wird die abgeschlossene Reparatur als eigener lokaler 48-Pfade-Checkpoint committet. Die literal no-glob Menge steht ausschließlich in `authoring-contract-design.json.preTasksRepairCheckpoint.candidatePaths`, wird vor dem Staging read-only validiert, danach exakt gestaged und mit staged Diff plus Inventar geprüft. Plan-, Reporting- und Fachdateien bleiben außerhalb. Der spätere Feature-Commit erzeugt `repair-checkpoint-manifest.json` mit Reparatur-Commit, Tree und Rohhash je Pfad; das Manifest behauptet keine eigene Anwesenheit im früheren Commit. Der vorhandene Checker und seine Adapter/Tests werden nach diesem Checkpoint nicht geändert.

**Begründung**: Der aktuelle Ausgangs-HEAD enthält die erforderlichen Worktree-Artefakte noch nicht. Nur die exakte lokale Commit-Grenze schafft einen realen unveränderlichen Vorgänger, den der finale Primary-Validator per Ancestry sowie Manifestpfad/-hash gegen den Reparatur-Tree prüfen kann.

**Verworfen**: Den alten Checker überschreiben oder `current-evidence-binding.json` ohne explizite Vorgängerbindung austauschen.

**Decision**: Before Tasks, the completed repair becomes one local 48-path checkpoint. The literal no-glob set is read-only validated, staged exactly, and checked by staged diff and exact inventory. The later feature commit creates a non-self-referential manifest binding repair commit/tree and per-path hashes. The existing checker becomes immutable after that checkpoint.

**Rationale**: Current base HEAD does not contain the required worktree evidence. The exact local checkpoint creates the real immutable ancestor that final Primary proof can validate.

**Rejected**: Overwriting the old checker or replacing `current-evidence-binding.json` without an explicit predecessor binding.

## Entscheidung 5: Proportionale Wiederverwendung / Decision 5: Proportional evidence reuse

**Entscheidung**: Vier vollständige Reparatur-Reviews, Global-14-Review-Coverage und 23 fokussierte Tests werden in Plan und späterer Umsetzung nicht pauschal wiederholt. Ihre unveränderten, hashgebundenen Artefakte sind ergänzende Vorgängerevidenz. Neu ausgeführt werden nur die fachlich betroffenen drei Fixture-Suiten, der additive Feature-Validator, direkte META-LH-03- und 14-Receipt-Prüfungen auf beiden Oberflächen, vollständiger Gitleaks-Scan, vier fokussierte semantische Reviews und die reale Plattformmatrix. META-LH-03 erhält nach den finalen Fachbytes einen neuen vollständigen Single-Review.

**Begründung**: Unveränderte Beweise werden proportional wiederverwendet; jede tatsächlich geänderte Grenze wird neu geprüft.

**Verworfen**: Alle vier historischen Reviews oder die gesamte Global-14-Reviewkampagne erneut ausführen. Das wäre nicht proportional und wurde ausdrücklich ausgeschlossen.

**Decision**: The four complete repair reviews, Global 14 review coverage, and 23 focused tests are not rerun wholesale during planning or later implementation. Their unchanged, hash-bound artefacts are Supplemental predecessor evidence. Newly executed evidence is limited to the three affected fixture suites, additive feature validator, direct META-LH-03 and 14-receipt checks on both surfaces, full Gitleaks scan, four focused semantic reviews, and the real platform matrix. META-LH-03 receives a new complete Single review after final domain bytes.

**Rationale**: Unchanged proof is reused proportionally; every changed boundary is tested anew.

**Rejected**: Rerunning all four historical reviews or the complete Global 14 review campaign. That is disproportionate and explicitly excluded.

## Entscheidung 6: Reale Plattformbefehle als Primärnachweis / Decision 6: Real platform commands as Primary proof

**Entscheidung**: Die bestehende Matrix in `.github/workflows/powershell-analysis.yml` wird als zwingender Konsument um den additiven Validator, den realen Global-Ready-Dispatcher und die positiven/negativen Harness-Fälle ergänzt, damit die exakten Befehle auf `ubuntu-22.04`, `macos-14` und `windows-2022` laufen. Der Primärnachweis enthält Runnerbezeichnung, geprüften HEAD, exakte Befehlszeile und unmittelbaren Exitcode. Der Workflow-/Jobstatus ist nur Supplemental. Auf Windows wird ausschließlich die vom Workflow validierte Git-for-Windows-Bash verwendet und ihr Verzeichnis für Kindprozesse in `PATH` aufgenommen.

**Begründung**: Plattformparität betrifft reale Interpreter und Pfadauflösung. Ein Jobname beweist diese Details nicht.

**Verworfen**: Neue Workflowdatei, Provider-Änderung, Admin-Konfiguration oder WSL-Annahme.

**Decision**: The existing matrix in `.github/workflows/powershell-analysis.yml` is a mandatory consumer and gains the additive validator, real Global-Ready dispatcher, and positive/negative harness cases so the exact commands run on `ubuntu-22.04`, `macos-14`, and `windows-2022`. Primary proof contains runner label, verified HEAD, exact command line, and immediate exit code. Workflow/job status is Supplemental only. Windows uses only the Git-for-Windows Bash validated by the workflow and adds its directory to `PATH` for child processes.

**Rationale**: Platform parity concerns real interpreters and path resolution. A job name does not prove those details.

**Rejected**: A new workflow file, provider mutation, admin configuration, or WSL assumption.

## Entscheidung 7: Evidence-Rollen und HEAD-Genauigkeit / Decision 7: Evidence roles and HEAD exactness

**Entscheidung**: Jedes Gate besitzt genau einen Primary-Nachweis. Jedes Supplemental-Element verweist auf das eindeutige Primary-Element desselben Gates. Der feature-lokale Pre-Validator `contracts/validate_gate_evidence_invariants.py` erzwingt diese Beziehung. In PostMerge erzwingt er außerdem, dass `acceptedPreMergePath` exakt dem in den Requirements konfigurierten Runner-Pfad entspricht und `acceptedPreMergeSha256` dessen Normalhash ist. Er läuft vor dem unveränderten installierten Evidence Core; diese zusätzlichen Regeln werden nicht dem Core zugeschrieben.

**Begründung**: Dies verhindert doppeldeutige Beweisquellen und vorweggenommene Erfolgsaussagen.

**Verworfen**: Geplante Ergebnisse als Evidence, grüne Namen ohne Logs oder Approval aus Nichtverfügbarkeit ableiten.

**Decision**: Each Supplemental item references the unique Primary item for its gate. A feature-local pre-validator enforces this and exact PostMerge equality to the configured PreMerge runner path plus matching normalized hash before the unchanged installed Evidence Core. The Core is not credited with these extra rules.

**Rationale**: This prevents ambiguous proof sources and premature success claims.

**Rejected**: Treating planned results as evidence, accepting green names without logs, or inferring approval from unavailability.

## Entscheidung 8: Statistik ohne Zeitreise / Decision 8: Statistics without time travel

**Entscheidung**: Erst wird die exakt geprüfte Feature-Liefermenge ohne Ledger normal committet. Auf diesem sauberen echten Branch läuft der kanonische Writer. Das allein geänderte Ledger wird separat committet; anschließend laufen beide Check-only-Oberflächen erneut am sauberen finalen HEAD. Es gibt keine temporäre Historienprojektion, kein Restore und kein Amend. Spätere Lifecycle-/Closeout-Textcommits werden beim nächsten regulären Statistik-Trigger erfasst.

**Begründung**: Der Writer verlangt einen sauberen Worktree; Methodik v2 schließt Ledger und Ledger-Commit aus. Die Reihenfolge ist damit reproduzierbar und endlich.

**Verworfen**: Spekulative Rückprojektion, temporärer Commit, Restore/Amend oder ein Regenerationszyklus nach jedem Ledger-Commit.

**Decision**: The exactly validated feature delivery set without the ledger is committed normally first. The canonical writer runs on that clean, real branch. The ledger-only change is committed separately; both check-only surfaces then rerun on the clean final HEAD. There is no temporary history projection, restore, or amend. Later lifecycle/closeout text commits are captured by the next regular statistics trigger.

**Rationale**: The writer requires a clean worktree; Methodology v2 excludes the ledger and ledger commit. This makes the sequence reproducible and finite.

**Rejected**: Speculative back-projection, temporary commits, restore/amend, or a regeneration loop after every ledger commit.

## Entscheidung 9: Verfassungsgemäßer Lifecycle / Decision 9: Constitution-compliant lifecycle

**Entscheidung**: Die Lastenheft-Umbenennung folgt nach dem Feature-Merge in einem eigenen normal geprüften PR über die vorhandenen Bash-/PowerShell-Skripte. Ein feature-lokales Lifecycle-Artefakt hält logischen und physischen Pfad auseinander. Der abgeschlossene Series-Manifestpfad und `specs/002-portfolio-ownership/intake-lifecycle.json` bleiben unverändert. Danach folgt der kausale Closeout auf dem vorbenannten Branch `003-authoring-contract-closeout` mit genau fünf Evidence-Pfaden: Tasks, Run-State, kausale Closeout-Evidence, Engineering-Retrospektive und Laufnachweis. Erst nach dessen realem Merge und finalem Sync entsteht der externe PostMerge-Snapshot.

**Begründung**: Der logische Series-Schlüssel darf nicht nachträglich umgeschrieben werden, während der physische Abschluss dennoch verfassungsgemäß nachgewiesen werden muss.

**Verworfen**: Series-Lifecycle reaktivieren, META-LH-02 ändern, vor dem Merge umbenennen oder Run-State vor dem realen Ereignis terminal setzen.

**Decision**: Lastenheft renaming follows after feature merge in its own normally reviewed PR through the existing Bash/PowerShell scripts. A feature-local lifecycle artefact separates logical and physical paths. The completed Series manifest path and `specs/002-portfolio-ownership/intake-lifecycle.json` remain unchanged. Causal closeout then uses the pre-named branch `003-authoring-contract-closeout` and exactly five evidence paths: Tasks, run state, causal closeout evidence, engineering retrospective, and run evidence. The external PostMerge snapshot is created only after that real merge and final synchronization.

**Rationale**: The logical Series key must not be rewritten retrospectively, while physical completion still requires constitutional evidence.

**Rejected**: Reactivating Series lifecycle, changing META-LH-02, renaming before merge, or marking run state terminal before the real event.

## Entscheidung 10: Nur META-LH-03 benötigt eine zweite Erneuerung / Decision 10: Only META-LH-03 needs a second renewal

**Entscheidung**: Das aktuelle Receipt-Inventar wurde gegen die fünf kanonischen Pfade geprüft. Genau ein Receipt, `specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json`, führt alle fünf als Quellen; die übrigen 13 Receipts tun dies nicht. Deshalb ist nach den Fachänderungen genau eine zweite Erneuerung von META-LH-03 fachlich notwendig und ausdrücklich genehmigt. Die übrigen 13 Leaf-Bindungen werden auf byte- und hashgenaue Gleichheit geprüft, nicht erneuert.

**Begründung**: Die Freshness-Grenze folgt der tatsächlichen Quellenabhängigkeit und nicht einer pauschalen Kampagnenannahme.

**Verworfen**: Alle 14 Intakes oder die vier zuvor reparierten Intakes erneut authoren/reviewen. Dies hätte keine Quellenabhängigkeit und würde die genehmigte Grenze überschreiten.

**Decision**: The current receipt inventory was checked against the five canonical paths. Exactly one receipt, `specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json`, lists all five as sources; the other 13 do not. Therefore exactly one second META-LH-03 renewal is materially necessary and explicitly approved after the domain changes. The other 13 leaf bindings are checked for byte- and hash-exact equality, not renewed.

**Rationale**: The freshness boundary follows the actual source dependency rather than a blanket campaign assumption.

**Rejected**: Re-authoring/reviewing all 14 intakes or all four previously repaired intakes. They have no such source dependency and this would exceed the approved boundary.

## Entscheidung 11: Zeitlich getrennte Gate-Requirements / Decision 11: Temporally split gate requirements

**Entscheidung**: `contracts/autonomous-run-gate-requirements.json` enthält nur PreMerge-Fakten. `contracts/postmerge-gate-requirements.json` enthält nur tatsächlichen normalen Merge, PR-/Merge-Commit, Lifecycle, kausalen Closeout, finalen Bericht, Retrospektive, Trend und Synchronisierung. Der Schema-2.0-PostMerge-Snapshot bindet den akzeptierten PreMerge-Snapshot über dessen exakten `acceptedPreMergePath` und normalisierten `acceptedPreMergeSha256`; beide Snapshots behalten denselben geprüften Feature-HEAD. PreMerge verlangt normale Merge-Bereitschaft, aber weder einen ausgeführten `gh pr merge`-Befehl noch einen Merge-Commit.

**Begründung**: Der installierte Evidence Core verlangt für jede `Applicable`-Anforderung im aktuellen Snapshot `Pass`. Eine gemeinsame Liste mit zukünftigen Merge-Fakten wäre vor dem Merge unerfüllbar.

**Verworfen**: PostMerge-Fakten in PreMerge als geplant, pending oder vorweggenommen erfolgreich zu führen. Das wäre fail-open und würde reale Kausalität vortäuschen.

**Decision**: The existing requirements file contains only PreMerge facts; the new PostMerge requirements file contains only actual normal merge, PR/merge commit, lifecycle, causal closeout, final report, retrospective, trend, and synchronization facts. The schema-2.0 PostMerge snapshot binds the accepted PreMerge snapshot through its exact path and normalized hash. PreMerge requires normal-policy merge readiness but neither an executed merge command nor a merge commit.

**Rationale**: The installed evidence core requires every Applicable item in a snapshot to be Pass. One mixed temporal list would be impossible to satisfy before merge.

**Rejected**: Marking future facts planned, pending, or prematurely successful in PreMerge.

## Entscheidung 12: Historische und aktuelle Bridge-Beweise / Decision 12: Historical and current bridge proof

**Entscheidung**: Die eingefrorene Vier-Receipt-Reparatur, ihr Checker und ihre 23 Tests bleiben Supplemental Evidence am exakten 48-Pfade-Reparatur-Checkpoint. Der neue additive Validator ist Primary am finalen Feature-HEAD und validiert das spätere Manifest vollständig gegen den Reparatur-Tree, beweist Ancestry, die unmittelbare META-LH-03-R1-zu-R2-Ziel-, Receipt- und Review-Supersession, 13 unveränderte Blätter und die unveränderte Series-Brücke. Der produktive Global-Ready-Dispatcher und sein Test bleiben zwingende Konsumenten.

**Begründung**: Der eingefrorene Checker soll den historischen Zustand beweisen und kann die absichtlich geänderte finale Leaf nicht akzeptieren. Ancestry plus additiver Delta-Validator bewahrt Historie und ermöglicht aktuellen Abschluss.

**Verworfen**: Den eingefrorenen Checker zu ändern oder ihn am finalen r2-Blatt als Primary laufen zu lassen.

**Decision**: Frozen repair evidence stays Supplemental at the exact 48-path checkpoint. The final Primary validator checks the later manifest against the repair tree, ancestry, direct R1-to-R2 target/receipt/review supersession, 13 unchanged leaves, and unchanged Series bridge. Global Ready remains mandatory.

**Rationale**: The frozen checker proves history and cannot legitimately accept the intentionally changed final leaf. Ancestry plus additive delta validation preserves history and makes current completion feasible.

**Rejected**: Mutating the frozen checker or using it as Primary against r2.

## Entscheidung 13: Vollständige Update-Transaktion / Decision 13: Complete Update transaction

**Entscheidung**: META-LH-03 R2 folgt vollständig dem unveränderten installierten Operation-Template und beiden Artefaktvalidatoren. Proposal-Pfad und Normalhash, aktuelle Approval, Operation `986c1d6c-d485-460b-8d8d-7cf5816a2c36`, Receipt `f41328cd-b301-4533-89dc-02aab758ab1f`, Review `b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf`, beide isolierten Staging-Pfade, beide Archive unter dem R1-Receipt `7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71`, vollständige `supersedes`-Hashes/-Pfade, identische Zielmengen und explizite R1-zu-R2-Review-Supersession sind verbindlich. Nur `Proposed`, `Approved`, `Applying`, `Completed` und `Failed` sind zulässig; Erfolg ist `Completed`, Fehler `Failed`, mit Reparaturdetails in `failure`, `nextAction` und `rollbackBoundary`. Beide installierten Validatoren müssen vor Erfolg bestehen.

**Begründung**: Nur Zielarchivierung beweist keine Receipt-Lineage und kein atomisches Authoring-Ereignis.

**Verworfen**: Eine einzelne generische Vorgängerdatei oder ein nichtterminales Operation-Journal als ausreichenden Beweis zu behandeln.

**Decision**: META-LH-03 R2 binds the unchanged installed template and both artefact validators, exact proposal/hash/approval, preallocated identities and literal paths, equal target sets, full predecessor archives/supersedes, explicit R1-to-R2 review supersession, and only the five accepted statuses. `Completed` succeeds; `Failed` records repair detail. Both validators must pass before success.

**Rationale**: Target archival alone proves neither receipt lineage nor an atomic authoring event.

**Rejected**: Treating one generic predecessor or a non-terminal operation journal as sufficient.

## Entscheidung 14: Fail-closed Ausführungsoberflächen / Decision 14: Fail-closed execution surfaces

**Entscheidung**: Die Bash-14-Receipt-Prüfung validiert Inventar und Eindeutigkeit mit einem fehlerpropagierenden `jq`, protokolliert jeden der 14 unmittelbaren Validator-Exitcodes, akkumuliert Fehler und endet bei jedem Fehler ungleich null. PowerShell verwendet für statische Analyse ausschließlich `pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1 -RepositoryRoot .`; dessen Registry-Bindung muss Version `1.25.0` ausgeben. Negative Harness-Fälle beweisen, dass ein früher Receipt-Fehler trotz späterer Erfolge und ein tatsächliches Analyzer-Finding das Gesamtgate sperren.

**Begründung**: Ein letzter erfolgreicher Schleifendurchlauf und `$Error.Count` sind keine zuverlässigen Gesamtgate-Signale.

**Verworfen**: Fail-fast ohne vollständige 14er-Protokollierung oder direkter `Invoke-ScriptAnalyzer`-Aufruf mit `$Error.Count`.

**Decision**: The Bash inventory propagates `jq` failures, logs all 14 immediate exits, accumulates failures, and exits nonzero for any failure. Static analysis uses only the canonical repository script and proves pinned version 1.25.0. Negative harnesses prove early receipt and analyzer findings block the aggregate gate.

**Rationale**: A final successful loop iteration and `$Error.Count` are not reliable aggregate gate signals.

**Rejected**: Fail-fast without full inventory evidence or direct analyzer invocation using `$Error.Count`.

## Entscheidung 15: Reporting und Tests-first als explizite Konsumenten / Decision 15: Reporting and test-first as explicit consumers

**Entscheidung**: Vor dem ersten Implementierungsedit wird die vollständige bestehende Ausführungsoberfläche geprüft und `specs/003-authoring-contract/tests-first-evidence.md` angelegt. Ein kleinstes positives/negatives Bridge-Paar erzeugt lokal verantwortetes erwartetes Rot, danach wird die kleinste Validator-Scheibe grün und erst dann verbreitert. Der Reporting-Vertrag umfasst exakt die 19 Pfade aus `reporting-contract-addendum.md`: fünf Agentenflächen, fünf Agenten-Templates, Constitution und Mirror, drei Spec-Kit-Templates sowie Policy, Addendum, Feature-Retrospektive und Laufnachweis. Die zehn Agentenflächen/-Templates tragen einen byte-identischen Block. Der Feature-Bericht nutzt sieben geordnete Teile: Output, Findings, bestätigte Regeln, Interventionen/Reparaturen, Effizienzbeobachtungen, AEPS-Relevanz und Completion/Retrospective Evidence. Der quellengebundene META-LH-01-bis-03-Trend entsteht erst nach Abschluss; fehlende Vergleichsdaten bleiben sichtbar statt geschätzt.

**Begründung**: Die Reihenfolge macht Regressionen und Verantwortlichkeit prüfbar und hält zukünftige Abschlussfakten kausal korrekt.

**Verworfen**: Erst alle Domain-Dateien ändern und anschließend Tests ergänzen, oder fehlende Trendwerte aus Prosa ableiten.

**Decision**: The complete existing execution surface and evidence path precede the first edit; one smallest positive/negative bridge pair goes red under local ownership, the smallest validator slice turns green, then coverage broadens. Reporting uses exactly the 19 addendum paths: five agent surfaces, five agent templates, the constitution and mirror, three Spec Kit templates, policy, addendum, feature retrospective, and run evidence. The block is byte-identical across all ten agent surfaces/templates. The feature report has seven ordered parts: Output, Findings, confirmed rules, interventions/repairs, efficiency observations, AEPS relevance, and Completion/Retrospective Evidence. Its source-bound META-LH-01 through META-LH-03 trend is created only after completion, with missing comparable evidence left explicit.

**Rationale**: This ordering makes regressions and ownership auditable while preserving causal truth for closeout facts.

**Rejected**: Editing all domain files before tests or inventing trend values from prose.

## Entscheidung 16: Feature-lokaler Gate-Evidence-Pre-Validator / Decision 16: Feature-local Gate Evidence pre-validator

**Entscheidung**: `specs/003-authoring-contract/contracts/test_validate_gate_evidence_invariants.py` entsteht vor `validate_gate_evidence_invariants.py`. Zwei positive Fixtures prüfen gültige Supplemental-zu-Primary-Referenzen und gültige PostMerge-zu-PreMerge-Bindung. Vier getrennte Negativ-Fixtures prüfen fehlende Primary-Referenz, falsche Primary-Referenz, falschen PreMerge-Pfad und falschen PreMerge-Normalhash. Der Pre-Validator läuft für PreMerge und PostMerge immer vor dem unveränderten installierten Evidence Core.

**Begründung**: Der installierte Core zählt Primary-Elemente und validiert einen angegebenen PreMerge-Hash, erzwingt aber weder die Supplemental-Referenz noch die Gleichheit mit dem konfigurierten Runner-Pfad. Ein enger lokaler Vorcheck schließt genau diese Lücke ohne Preset- oder Level-0-Änderung.

**Verworfen**: Dem unveränderten Core Regeln zuzuschreiben, die er nicht prüft, oder das Preset in diesem Feature zu ändern.

**Decision**: The exact test path precedes the feature-local validator. Two positive and four separate negative fixtures cover valid references/binding, missing or wrong Primary references, and wrong PreMerge path/hash. This pre-validator always runs before the unchanged installed Evidence Core.

**Rationale**: The installed Core does not enforce these two configured invariants. A narrow local pre-check closes only that gap without preset or Level 0 change.

**Rejected**: Crediting the unchanged Core with checks it does not perform or changing the preset here.
