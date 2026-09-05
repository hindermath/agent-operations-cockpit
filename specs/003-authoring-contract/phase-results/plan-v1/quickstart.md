# Schnellstart: Umsetzung und Nachweis

## Geltungsbereich / Scope

Diese Befehlsfolge ist für die spätere Umsetzung bestimmt. Sie wurde in der Planphase nicht als bestandene Evidence ausgeführt. Jeder Befehl läuft an dem HEAD, der im jeweiligen Nachweis genannt wird. Die einzige Dokumentationsauswirkungsentscheidung bleibt `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

This command sequence is for later implementation. It was not executed as passing evidence during Plan. Every command runs at the HEAD named by its evidence record. The sole Documentation Impact decision remains `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

## 1. Read-only Ausgangsprüfung / Read-only baseline check

```bash
git branch --show-current
git rev-parse HEAD
git status --short
jq -e '.schemaVersion == "1.0" and (.orderedLogicalTargets | length) == 14 and ([.orderedLogicalTargets[].logicalTargetId] | unique | length) == 14' specs/003-authoring-contract/current-evidence-binding.json
python3 -m unittest specs/003-authoring-contract/contracts/test_validate_current_evidence_binding.py
bash specs/003-authoring-contract/contracts/validate-current-evidence-binding.sh --repo .
pwsh -NoProfile -File specs/003-authoring-contract/contracts/validate-current-evidence-binding.ps1 -Repo .
```

Die letzten drei Befehle bestätigen nur, dass der abgeschlossene Reparaturbeweis vor der Fachänderung noch unverändert ist. Sie ersetzen weder die vier historischen Reviews noch einen neuen META-LH-03-Review. Die dokumentierten 23 Reparaturtests und Global-14-Abdeckung werden nicht pauschal erneut ausgeführt.

The final three commands only confirm that the completed repair proof is unchanged before the domain update. They replace neither the four historical reviews nor a new META-LH-03 review. The documented 23 repair tests and Global 14 coverage are not rerun wholesale.

## 2. Drei kanonische Fixture-Suiten / Three canonical fixture suites

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-validator.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-lifecycle.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-governance-config.ps1
```

Jede Suite muss den unmittelbaren Exitcode festhalten. Die Validator-Suite enthält positive und negative Fälle für einen gesperrten, nicht ausführbaren Receipt-Platzhalter sowie verbotene ausführbare Specify- und Autonomous-Aufrufe. Die Lifecycle-Suite prüft unveränderliche Vorgänger und getrennte logische/physische Pfade. Die Konfigurations-Suite prüft Profilpfad, Profil-ID, `de-DE`, Pfadgrenze sowie fehlende oder widersprüchliche Profile.

Each suite records the immediate exit code. The validator suite contains positive and negative cases for a blocked, non-executable receipt placeholder and forbidden executable Specify and Autonomous calls. The lifecycle suite checks immutable predecessors and separate logical/physical paths. The configuration suite checks profile path, profile ID, `de-DE`, path boundary, and missing or contradictory profiles.

## 3. Governance-Konfiguration direkt / Direct governance configuration

```bash
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-governance-config.sh --config requirements/intake-governance.json --repo . --json
```

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-governance-config.ps1 -Config requirements/intake-governance.json -Repo . -Json
```

## 4. META-LH-03 direkt / Direct META-LH-03

Nach der genehmigten Erneuerung müssen beide Oberflächen dasselbe neue Receipt und seinen aktuellen Zielhash prüfen.

After the approved renewal, both surfaces must validate the same new receipt and its current target hash.

```bash
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json --repo .
```

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json -Repo .
```

## 5. Exakt 14 Receipts über Bash / Exactly 14 receipts through Bash

```bash
jq -e '(.orderedLogicalTargets | length) == 14' specs/003-authoring-contract/current-evidence-binding.json
jq -e '([.orderedLogicalTargets[].authoringReceipt.path] | unique | length) == 14' specs/003-authoring-contract/current-evidence-binding.json
jq -r '.orderedLogicalTargets[].authoringReceipt.path' specs/003-authoring-contract/current-evidence-binding.json |
while IFS= read -r receipt_path; do
  bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt "$receipt_path" --repo .
  test "$?" -eq 0
done
```

Die Iteration vermeidet `mapfile` und ist dadurch auch bei abweichender Plattformvorbelegung stabil. Die erforderliche Matrix weist dennoch Bash 5+ explizit nach.

The iteration avoids `mapfile` and is therefore stable across different platform defaults. The required matrix still proves Bash 5+ explicitly.

## 6. Exakt 14 Receipts über PowerShell / Exactly 14 receipts through PowerShell

```powershell
$Binding = Get-Content -LiteralPath 'specs/003-authoring-contract/current-evidence-binding.json' -Raw | ConvertFrom-Json
$ReceiptPaths = @($Binding.orderedLogicalTargets | ForEach-Object { $_.authoringReceipt.path })
if ($ReceiptPaths.Count -ne 14 -or @($ReceiptPaths | Sort-Object -Unique).Count -ne 14) { throw 'Expected exactly 14 unique receipt paths.' }
foreach ($ReceiptPath in $ReceiptPaths) {
    & pwsh -NoProfile -File '.specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1' -Receipt $ReceiptPath -Repo '.'
    if ($LASTEXITCODE -ne 0) { throw "Receipt validation failed: $ReceiptPath" }
}
```

## 7. Additiver Feature-Validator / Additive feature validator

Die spätere Umsetzung stellt folgende neue, feature-lokale Oberflächen bereit. Der historische Reparatur-Checker bleibt unverändert.

Later implementation provides the following new feature-local surfaces. The historical repair checker remains unchanged.

```bash
python3 -m unittest specs/003-authoring-contract/contracts/test_validate_authoring_contract.py
bash specs/003-authoring-contract/contracts/validate-authoring-contract.sh --repo . --json
```

```powershell
pwsh -NoProfile -File specs/003-authoring-contract/contracts/validate-authoring-contract.ps1 -Repo . -Json
```

Der Validator muss die alte Reparatur als Vorgänger, die finalen fünf Artefakthashes, neue Operation/Receipt/Review, byte-identisches Archiv, genau ein geändertes META-LH-03-Blatt, 13 unveränderte Blätter und die unveränderte Series-Brücke prüfen. Er muss negative Fixtures für Hashdrift, zweite Blattänderung, wiederverwendete ID, ausführbaren Blocked-Prompt und fehlende Approval enthalten.

The validator must check the old repair as predecessor, final hashes of the five artefacts, new operation/receipt/review, byte-identical archive, exactly one changed META-LH-03 leaf, 13 unchanged leaves, and the unchanged Series bridge. It must contain negative fixtures for hash drift, a second leaf change, reused ID, executable blocked prompt, and missing approval.

## 8. PSScriptAnalyzer und vollständiger Secret-Scan / PSScriptAnalyzer and full secret scan

```powershell
pwsh -NoProfile -Command "Invoke-ScriptAnalyzer -Path '.specify/presets/intake-authoring-governance','specs/003-authoring-contract/contracts' -Recurse -Severity Warning,Error; if (`$Error.Count -gt 0) { exit 1 }"
```

```bash
gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100
rg -n 'intake-authoring-governance/tests|authoring.*tests' .gitleaks.toml
```

Der `rg`-Befehl ist eine Inspektion: Sein Treffer darf keine aktive Ausnahme der Authoring-Testpfade zeigen. Falls er keinen Treffer liefert, wird Exitcode `1` als erwartetes „kein Muster gefunden“ protokolliert und nicht als Gitleaks-Erfolg umgedeutet. Nur der unmittelbare Exitcode `0` des vollständigen `gitleaks dir` erfüllt den Secret-Gate.

The `rg` command is an inspection: any match must not show an active exclusion for Authoring test paths. If it has no match, exit code `1` is recorded as expected “pattern not found” and is not reinterpreted as Gitleaks success. Only immediate exit code `0` from the full `gitleaks dir` satisfies the secret gate.

## 9. Reale Drei-Plattform-Matrix / Real three-platform matrix

Die vorhandene Matrix verwendet exakt `ubuntu-22.04`, `macos-14` und `windows-2022`. Der fokussierte Schritt führt Abschnitte 2 bis 7 aus, protokolliert vorab `git rev-parse HEAD`, `bash --version`, `pwsh --version` und `python3 --version` und erfasst nach jedem Fachbefehl den unmittelbaren Exitcode. Auf Windows muss der bereits geprüfte `AOC_GIT_BASH_EXE` verwendet und dessen Verzeichnis vor den PowerShell-Fixtures in `PATH` aufgenommen werden. WSL gilt nicht als Ersatz.

The existing matrix uses exactly `ubuntu-22.04`, `macos-14`, and `windows-2022`. The focused step executes sections 2 through 7, first logs `git rev-parse HEAD`, `bash --version`, `pwsh --version`, and `python3 --version`, and captures the immediate exit code after every domain command. On Windows, the already validated `AOC_GIT_BASH_EXE` must be used and its directory added to `PATH` before PowerShell fixtures. WSL is not a substitute.

## 10. Semantische Reviews / Semantic reviews

Die späteren Reviewer schreiben reale Ergebnisse in genau diese Pfade:

Later reviewers write real results to exactly these paths:

```text
specs/003-authoring-contract/security-review-evidence.md
specs/003-authoring-contract/architecture-review-evidence.md
specs/003-authoring-contract/accessibility-review-evidence.md
specs/003-authoring-contract/cross-platform-parity-evidence.md
```

Jeder Bericht bindet Reviewer, HEAD, geprüfte Pfade, Findings mit Status/Owner/Trigger sowie seine konkreten Befehle. Sicherheit deckt Quellenautorität, Pfadgrenzen, Prompt-Injection, Secrets, Datenschutz, NIST SSDF, CWE Top 25 und den Nachweis von null automatisch gestarteten Review-, Specify-, Autonomous-, Implementierungs- oder Delivery-Aktionen ab. Architektur deckt Vertrauensgrenzen, Schichten, Fail-safe Defaults und den additiven Vorgängerbeweis ab. A11Y deckt Deutsch zuerst, Englisch danach, CEFR B2, Erstbegriff-Erklärungen, semantische Überschriften, Textalternativen und WCAG 2.2 AA ab. Eine Person der Zielgruppe muss ohne Spec-Kit-Vorwissen Zweck, Voraussetzungen, Status, offene Entscheidungen, Nicht-Autorität und genau eine nächste sichere Aktion zu 100 Prozent korrekt benennen. Parität deckt reale Befehle und Ergebnisse aller drei Runner ab. Nicht anwendbare Produktstandards erhalten Begründung und Re-Evaluation-Trigger.

Each report binds reviewer, HEAD, reviewed paths, findings with status/owner/trigger, and its concrete commands. Security covers source authority, path boundaries, prompt injection, secrets, privacy, NIST SSDF, CWE Top 25, and proof that zero review, Specify, Autonomous, implementation, or delivery action starts automatically. Architecture covers trust boundaries, layers, fail-safe defaults, and the additive predecessor proof. A11Y covers German first, English second, CEFR B2, first-use explanations, semantic headings, text alternatives, and WCAG 2.2 AA. A target-audience participant without prior Spec Kit knowledge must identify purpose, prerequisites, status, open decisions, non-authority, and exactly one next safe action with 100 percent accuracy. Parity covers real commands and results from all three runners. Non-applicable product standards receive a rationale and re-evaluation trigger.

## 11. Exakte Liefermenge und Implementierungs-Checkpoint / Exact delivery set and implementation checkpoint

Vor dem Staging werden die Pfade aus `specs/003-authoring-contract/contracts/authoring-contract-design.json` aufgelöst und mit `git status --short`, `git diff --name-only` und `git diff --cached --name-only` abgeglichen. Der Reparatur-Checkpoint wird getrennt vom späteren Feature-Checkpoint behandelt. Nur einzeln benannte, für den jeweiligen Commit bestimmte Pfade werden gestaged.

Before staging, paths from `specs/003-authoring-contract/contracts/authoring-contract-design.json` are resolved and reconciled with `git status --short`, `git diff --name-only`, and `git diff --cached --name-only`. The repair checkpoint is handled separately from the later feature checkpoint. Only individually named paths intended for the respective commit are staged.

```bash
git diff --cached --name-only
git diff --cached --check
git status --short
```

`changed - planned`, `staged - intended` und unerklärte fehlende Pfade müssen leer sein. Der normale Implementierungs-Checkpoint enthält nicht `docs/project-statistics.md`. Es gibt kein `git add -A`, keinen Stash, Reset, Force oder Amend.

`changed - planned`, `staged - intended`, and unexplained missing paths must be empty. The normal implementation checkpoint does not contain `docs/project-statistics.md`. There is no `git add -A`, stash, reset, force, or amend.

## 12. Statistik auf sauberem echten Branch / Statistics on a clean real branch

Nach dem normalen Implementierungs-Checkpoint muss `git status --porcelain` leer sein.

After the normal implementation checkpoint, `git status --porcelain` must be empty.

```bash
bash scripts/render-project-statistics.sh --repo .
bash scripts/render-project-statistics.sh --repo . --check-only --json
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly -Json
git diff --name-only
```

Nur `docs/project-statistics.md` darf geändert sein und wird separat committet. Danach:

Only `docs/project-statistics.md` may be changed and is committed separately. Afterwards:

```bash
test -z "$(git status --porcelain)"
bash scripts/render-project-statistics.sh --repo . --check-only --json
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly -Json
```

Ein unverändertes Ledger führt nicht zu einem leeren Commit. Methodik v2 schließt Ledger und Ledger-Commit aus; es folgt kein zusätzlicher Writer-Zyklus.

An unchanged ledger does not produce an empty commit. Methodology v2 excludes the ledger and ledger commit; no additional writer cycle follows.

## 13. PreMerge, Merge und Sync / PreMerge, merge, and sync

`premerge-gate-evidence.json` ist ein temporäres Runner-Artefakt, kein Repository-Pfad. Es bindet den finalen Requirements-Hash und exakten finalen Feature-HEAD. Vor Merge müssen alle Primary Gates, die vier Reviewberichte, aktuelle verpflichtende Checks, keine offenen actionable Threads und eine tatsächlich verfügbare erforderliche Approval vorliegen. Ein fehlender oder nicht abrufbarer Approval-Nachweis blockiert. Merge erfolgt nach normaler Policy ohne Admin-Bypass. Danach wird `main` ausschließlich fast-forward synchronisiert; Ahead/Behind muss `0/0` ergeben.

`premerge-gate-evidence.json` is a temporary runner artefact, not a repository path. It binds the final requirements hash and exact final feature HEAD. Before merge, all Primary gates, four review reports, current required checks, no unresolved actionable threads, and an actually available required approval must exist. Missing or unavailable approval proof blocks. Merge follows normal policy without admin bypass. Afterwards `main` is synchronized by fast-forward only; ahead/behind must be `0/0`.

Die Live-Prüfung verwendet die authentifizierte GitHub CLI. `PR_NUMBER` und `GH_REPOSITORY` werden aus dem aktuellen PR beziehungsweise Remote aufgelöst und vor Nutzung angezeigt; sie sind keine vorab behaupteten Werte.

The live check uses the authenticated GitHub CLI. `PR_NUMBER` and `GH_REPOSITORY` are resolved from the current PR and remote and displayed before use; they are not pre-claimed values.

```bash
gh auth status
gh pr view "$PR_NUMBER" --json number,url,baseRefName,headRefName,headRefOid,mergeStateStatus,reviewDecision,statusCheckRollup,reviews
test "$(gh pr view "$PR_NUMBER" --json headRefOid --jq '.headRefOid')" = "$(git rev-parse HEAD)"
gh pr checks "$PR_NUMBER" --required
gh api --paginate "repos/$GH_REPOSITORY/pulls/$PR_NUMBER/comments"
gh api graphql -f owner="$GH_OWNER" -f name="$GH_NAME" -F number="$PR_NUMBER" -f query='query($owner:String!,$name:String!,$number:Int!){repository(owner:$owner,name:$name){pullRequest(number:$number){reviewThreads(first:100){nodes{isResolved comments(first:20){nodes{url body author{login}}}}}}}}'
```

Die JSON-Antwort muss den exakten HEAD, aktuelle Required Checks, eine ausreichende tatsächliche Approval und null offene actionable Threads belegen. Nicht verfügbare oder unvollständige Antworten blockieren. Erst dann ist der normale Merge ohne `--admin` zulässig:

The JSON response must prove the exact HEAD, current required checks, a sufficient actual approval, and zero unresolved actionable threads. Unavailable or incomplete responses block. Only then is a normal merge without `--admin` allowed:

```bash
gh pr merge "$PR_NUMBER" --merge
git switch main
git pull --ff-only
git rev-list --left-right --count main...origin/main
test -z "$(git status --porcelain)"
```

## 14. Lifecycle und kausaler Abschluss / Lifecycle and causal closeout

Nach dem Feature-Merge wird die Umbenennung in einem eigenen normal geprüften PR vorbereitet und mit beiden Oberflächen gleichwertig nachgewiesen:

After feature merge, renaming is prepared in its own normally reviewed PR and equivalently proven through both surfaces:

```bash
bash scripts/rename-lastenheft.sh requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md 003-authoring-contract
```

```powershell
pwsh -NoProfile -File scripts/rename-lastenheft.ps1 -File requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md -BranchName 003-authoring-contract
```

Die tatsächlich schreibende Oberfläche wird einmal verwendet; die zweite Oberfläche wird über Fixture/Preview oder einen isolierten, read-only Äquivalenznachweis geprüft, damit kein zweites Rename erfolgt. `specs/003-authoring-contract/intake-lifecycle.json` hält logischen und physischen Pfad fest. Series und META-LH-02 bleiben unverändert.

The actually writing surface is used once; the second surface is verified through a fixture/preview or isolated read-only equivalence proof so no second rename occurs. `specs/003-authoring-contract/intake-lifecycle.json` records logical and physical paths. Series and META-LH-02 remain unchanged.

PostMerge-Fakten werden erst danach in `specs/003-authoring-contract/causal-closeout-evidence.json` geschrieben. Falls ein Evidence-only-PR nötig ist, lautet der Branch `003-authoring-contract-closeout` und die Positivliste besteht genau aus:

PostMerge facts are written to `specs/003-authoring-contract/causal-closeout-evidence.json` only afterwards. If an evidence-only PR is required, its branch is `003-authoring-contract-closeout` and its allowlist contains exactly:

```text
specs/003-authoring-contract/tasks.md
specs/003-authoring-contract/autonomous-run-state.json
specs/003-authoring-contract/causal-closeout-evidence.json
```

Auch dieser PR verwendet normale Checks, Review und Approval ohne Bypass. Der Abschlussnachweis endet mit sauberem Worktree, `main` auf dem Remote-HEAD und Ahead/Behind `0/0`.

This PR also uses normal checks, review, and approval without bypass. Closeout evidence ends with a clean worktree, `main` at remote HEAD, and ahead/behind `0/0`.
