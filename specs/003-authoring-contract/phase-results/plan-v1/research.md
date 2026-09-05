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

**Entscheidung**: Der vorhandene Checker `specs/003-authoring-contract/contracts/validate_current_evidence_binding.py` und seine Adapter/Tests werden nicht geändert. Ein neuer additiver Feature-Validator belegt eine zweistufige Kette: abgeschlossene Reparatur als unveränderlicher Vorgänger und genau eine spätere META-LH-03-Erneuerung. Er verlangt Identität der übrigen 13 Zielblätter und der Series-Brücke.

**Begründung**: Der alte Checker beweist einen konkreten historischen Zustand. Würde er an den neuen Zustand angepasst, verlöre der Vorgängerbeweis seine Unveränderlichkeit.

**Verworfen**: Den alten Checker überschreiben oder `current-evidence-binding.json` ohne explizite Vorgängerbindung austauschen.

**Decision**: The existing checker `specs/003-authoring-contract/contracts/validate_current_evidence_binding.py` and its adapters/tests remain unchanged. A new additive feature validator proves a two-stage chain: completed repair as immutable predecessor and exactly one later META-LH-03 renewal. It requires identity of the other 13 target leaves and the Series bridge.

**Rationale**: The old checker proves a concrete historical state. Adapting it to the new state would remove the immutability of the predecessor proof.

**Rejected**: Overwriting the old checker or replacing `current-evidence-binding.json` without an explicit predecessor binding.

## Entscheidung 5: Proportionale Wiederverwendung / Decision 5: Proportional evidence reuse

**Entscheidung**: Vier vollständige Reparatur-Reviews, Global-14-Review-Coverage und 23 fokussierte Tests werden in Plan und späterer Umsetzung nicht pauschal wiederholt. Ihre unveränderten, hashgebundenen Artefakte sind ergänzende Vorgängerevidenz. Neu ausgeführt werden nur die fachlich betroffenen drei Fixture-Suiten, der additive Feature-Validator, direkte META-LH-03- und 14-Receipt-Prüfungen auf beiden Oberflächen, vollständiger Gitleaks-Scan, vier fokussierte semantische Reviews und die reale Plattformmatrix. META-LH-03 erhält nach den finalen Fachbytes einen neuen vollständigen Single-Review.

**Begründung**: Unveränderte Beweise werden proportional wiederverwendet; jede tatsächlich geänderte Grenze wird neu geprüft.

**Verworfen**: Alle vier historischen Reviews oder die gesamte Global-14-Reviewkampagne erneut ausführen. Das wäre nicht proportional und wurde ausdrücklich ausgeschlossen.

**Decision**: The four complete repair reviews, Global 14 review coverage, and 23 focused tests are not rerun wholesale during planning or later implementation. Their unchanged, hash-bound artefacts are Supplemental predecessor evidence. Newly executed evidence is limited to the three affected fixture suites, additive feature validator, direct META-LH-03 and 14-receipt checks on both surfaces, full Gitleaks scan, four focused semantic reviews, and the real platform matrix. META-LH-03 receives a new complete Single review after final domain bytes.

**Rationale**: Unchanged proof is reused proportionally; every changed boundary is tested anew.

**Rejected**: Rerunning all four historical reviews or the complete Global 14 review campaign. That is disproportionate and explicitly excluded.

## Entscheidung 6: Reale Plattformbefehle als Primärnachweis / Decision 6: Real platform commands as Primary proof

**Entscheidung**: Die bestehende Matrix in `.github/workflows/powershell-analysis.yml` wird nur dann um einen fokussierten Feature-Schritt ergänzt, wenn die exakten Befehle sonst nicht auf `ubuntu-22.04`, `macos-14` und `windows-2022` laufen. Der Primärnachweis enthält Runnerbezeichnung, geprüften HEAD, exakte Befehlszeile und unmittelbaren Exitcode. Der Workflow-/Jobstatus ist nur Supplemental. Auf Windows wird ausschließlich die vom Workflow validierte Git-for-Windows-Bash verwendet und ihr Verzeichnis für Kindprozesse in `PATH` aufgenommen.

**Begründung**: Plattformparität betrifft reale Interpreter und Pfadauflösung. Ein Jobname beweist diese Details nicht.

**Verworfen**: Neue Workflowdatei, Provider-Änderung, Admin-Konfiguration oder WSL-Annahme.

**Decision**: The existing matrix in `.github/workflows/powershell-analysis.yml` gains one focused feature step only if the exact commands otherwise do not run on `ubuntu-22.04`, `macos-14`, and `windows-2022`. Primary proof contains runner label, verified HEAD, exact command line, and immediate exit code. Workflow/job status is Supplemental only. Windows uses only the Git-for-Windows Bash validated by the workflow and adds its directory to `PATH` for child processes.

**Rationale**: Platform parity concerns real interpreters and path resolution. A job name does not prove those details.

**Rejected**: A new workflow file, provider mutation, admin configuration, or WSL assumption.

## Entscheidung 7: Evidence-Rollen und HEAD-Genauigkeit / Decision 7: Evidence roles and HEAD exactness

**Entscheidung**: Jedes Gate besitzt genau einen Primary-Nachweis. Supplemental-Nachweise verweisen auf ihn. `premerge-gate-evidence.json` ist ein temporäres Runner-Artefakt, kein Repository-Pfad, und bindet den exakten finalen Feature-HEAD. `specs/003-authoring-contract/causal-closeout-evidence.json` entsteht erst nach realem Merge und Sync. Review, aktueller Checkstatus und verfügbare Approval sind eigenständige Pflichtbeweise.

**Begründung**: Dies verhindert doppeldeutige Beweisquellen und vorweggenommene Erfolgsaussagen.

**Verworfen**: Geplante Ergebnisse als Evidence, grüne Namen ohne Logs oder Approval aus Nichtverfügbarkeit ableiten.

**Decision**: Each gate has exactly one Primary proof. Supplemental proof refers to it. `premerge-gate-evidence.json` is a temporary runner artefact, not a repository path, and binds the exact final feature HEAD. `specs/003-authoring-contract/causal-closeout-evidence.json` is created only after real merge and sync. Review, current check status, and available approval are separate mandatory proof.

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

**Entscheidung**: Die Lastenheft-Umbenennung folgt nach dem Feature-Merge in einem eigenen normal geprüften PR über die vorhandenen Bash-/PowerShell-Skripte. Ein feature-lokales Lifecycle-Artefakt hält logischen und physischen Pfad auseinander. Der abgeschlossene Series-Manifestpfad und `specs/002-portfolio-ownership/intake-lifecycle.json` bleiben unverändert. Ein nötiger kausaler Abschluss verwendet höchstens den vorbenannten Branch `003-authoring-contract-closeout` und genau drei Evidence-Pfade.

**Begründung**: Der logische Series-Schlüssel darf nicht nachträglich umgeschrieben werden, während der physische Abschluss dennoch verfassungsgemäß nachgewiesen werden muss.

**Verworfen**: Series-Lifecycle reaktivieren, META-LH-02 ändern, vor dem Merge umbenennen oder Run-State vor dem realen Ereignis terminal setzen.

**Decision**: Lastenheft renaming follows after feature merge in its own normally reviewed PR through the existing Bash/PowerShell scripts. A feature-local lifecycle artefact separates logical and physical paths. The completed Series manifest path and `specs/002-portfolio-ownership/intake-lifecycle.json` remain unchanged. Any necessary causal closeout uses at most the pre-named branch `003-authoring-contract-closeout` and exactly three evidence paths.

**Rationale**: The logical Series key must not be rewritten retrospectively, while physical completion still requires constitutional evidence.

**Rejected**: Reactivating Series lifecycle, changing META-LH-02, renaming before merge, or marking run state terminal before the real event.

## Entscheidung 10: Nur META-LH-03 benötigt eine zweite Erneuerung / Decision 10: Only META-LH-03 needs a second renewal

**Entscheidung**: Das aktuelle Receipt-Inventar wurde gegen die fünf kanonischen Pfade geprüft. Genau ein Receipt, `specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json`, führt alle fünf als Quellen; die übrigen 13 Receipts tun dies nicht. Deshalb ist nach den Fachänderungen genau eine zweite Erneuerung von META-LH-03 fachlich notwendig und ausdrücklich genehmigt. Die übrigen 13 Leaf-Bindungen werden auf byte- und hashgenaue Gleichheit geprüft, nicht erneuert.

**Begründung**: Die Freshness-Grenze folgt der tatsächlichen Quellenabhängigkeit und nicht einer pauschalen Kampagnenannahme.

**Verworfen**: Alle 14 Intakes oder die vier zuvor reparierten Intakes erneut authoren/reviewen. Dies hätte keine Quellenabhängigkeit und würde die genehmigte Grenze überschreiten.

**Decision**: The current receipt inventory was checked against the five canonical paths. Exactly one receipt, `specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json`, lists all five as sources; the other 13 do not. Therefore exactly one second META-LH-03 renewal is materially necessary and explicitly approved after the domain changes. The other 13 leaf bindings are checked for byte- and hash-exact equality, not renewed.

**Rationale**: The freshness boundary follows the actual source dependency rather than a blanket campaign assumption.

**Rejected**: Re-authoring/reviewing all 14 intakes or all four previously repaired intakes. They have no such source dependency and this would exceed the approved boundary.
