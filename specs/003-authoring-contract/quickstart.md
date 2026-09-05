# Schnellstart: Umsetzung und Nachweis

## Geltungsbereich / Scope

Diese Befehlsfolge ist für die spätere Umsetzung bestimmt. Sie wurde in der Planphase nicht als bestandene Evidence ausgeführt. Jeder Befehl läuft an dem HEAD, der im jeweiligen Nachweis genannt wird. Die einzige Dokumentationsauswirkungsentscheidung bleibt `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

This command sequence is for later implementation. It was not executed as passing evidence during Plan. Every command runs at the HEAD named by its evidence record. The sole Documentation Impact decision remains `UpdateRequired` in `specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.

## 0. Lokaler Reparatur-Checkpoint vor Tasks / Local repair checkpoint before Tasks

Vor Tasks wird genau die 48-Pfade-Menge aus `authoring-contract-design.json.preTasksRepairCheckpoint.candidatePaths` read-only auf Existenz, Änderung/Untracked-Status, Symlinkfreiheit und Text-Whitespace geprüft. Der installierte Delivery-Validator erhält jeden Pfad als eigenes `--intended`-Argument. Danach wird ausschließlich die folgende literal benannte Menge ohne Glob gestaged:

Before Tasks, exactly the 48-path set in the design contract is checked read-only for existence, changed/untracked state, symlink safety, and text whitespace. The installed delivery validator receives every path as its own `--intended` argument. Only this literal no-glob set is then staged:

```bash
git add -- \
  requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md \
  specs/intake-authoring-receipts/META-LH-02-Portfolio-Ownership.json \
  specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json \
  specs/intake-authoring-receipts/META-LH-05-Erste-Welle.json \
  specs/intake-authoring-receipts/RAW-03-State-Truthfulness.json \
  specs/intake-authoring-archive/d0a6ef89-8a1f-4957-aa6f-be82d3cdbf3b/53564be1-65eb-47e8-9786-6c1fb19fd844/Lastenheft_META-LH-02-Portfolio-Ownership.md \
  specs/intake-authoring-archive/d0a6ef89-8a1f-4957-aa6f-be82d3cdbf3b/53564be1-65eb-47e8-9786-6c1fb19fd844/META-LH-02-Portfolio-Ownership.json \
  specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/4a0e33c5-6348-4778-823a-e4a093b75456/Lastenheft_META-LH-03-Authoring-Contract.md \
  specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/4a0e33c5-6348-4778-823a-e4a093b75456/META-LH-03-Authoring-Contract.json \
  specs/intake-authoring-archive/d672cfa4-13f0-43cb-84ba-27d191710342/238e0c7e-a300-4573-b91d-38385c155fed/Lastenheft_META-LH-05-Erste-Welle.md \
  specs/intake-authoring-archive/d672cfa4-13f0-43cb-84ba-27d191710342/238e0c7e-a300-4573-b91d-38385c155fed/META-LH-05-Erste-Welle.json \
  specs/intake-authoring-archive/af8d8b59-d146-44b0-8bf5-a63966865d4a/89293949-6174-4549-a33d-6cd6eeb71df3/Lastenheft_RAW-03-State-Truthfulness.md \
  specs/intake-authoring-archive/af8d8b59-d146-44b0-8bf5-a63966865d4a/89293949-6174-4549-a33d-6cd6eeb71df3/RAW-03-State-Truthfulness.json \
  specs/intake-authoring-operations/959e832f-be87-4f77-a0a9-478220708a6d/operation.json \
  specs/intake-authoring-operations/959e832f-be87-4f77-a0a9-478220708a6d/staging/META-LH-02-Portfolio-Ownership.json \
  specs/intake-authoring-operations/959e832f-be87-4f77-a0a9-478220708a6d/staging/META-LH-03-Authoring-Contract.json \
  specs/intake-authoring-operations/959e832f-be87-4f77-a0a9-478220708a6d/staging/META-LH-05-Erste-Welle.json \
  specs/intake-authoring-operations/959e832f-be87-4f77-a0a9-478220708a6d/staging/RAW-03-State-Truthfulness.json \
  specs/intake-review-requests/meta-lh-02-portfolio-ownership-2026-09-05-r1.json \
  specs/intake-review-results/meta-lh-02-portfolio-ownership-2026-09-05-r1.json \
  docs/reviews/meta-lh-02-portfolio-ownership-intake-review-2026-09-05-r1.md \
  specs/intake-review-requests/meta-lh-03-authoring-contract-2026-09-05-r1.json \
  specs/intake-review-results/meta-lh-03-authoring-contract-2026-09-05-r1.json \
  docs/reviews/meta-lh-03-authoring-contract-intake-review-2026-09-05-r1.md \
  specs/intake-review-requests/meta-lh-05-erste-welle-2026-09-05-r1.json \
  specs/intake-review-results/meta-lh-05-erste-welle-2026-09-05-r1.json \
  docs/reviews/meta-lh-05-erste-welle-intake-review-2026-09-05-r1.md \
  specs/intake-review-requests/raw-03-state-truthfulness-2026-09-05-r1.json \
  specs/intake-review-results/raw-03-state-truthfulness-2026-09-05-r1.json \
  docs/reviews/raw-03-state-truthfulness-intake-review-2026-09-05-r1.md \
  docs/aeps/findings-ledger.md \
  docs/aeps/receipts/2026-09-05-meta-lh03-binding-renewal.md \
  docs/aeps/receipts/2026-09-05-meta-lh03-binding-bridge.md \
  specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py \
  docs/man/validate-current-evidence-binding.1 \
  specs/003-authoring-contract/binding-approval.md \
  specs/003-authoring-contract/blocking-scope-decision.md \
  specs/003-authoring-contract/binding-repair-validation.json \
  specs/003-authoring-contract/current-evidence-binding.json \
  specs/003-authoring-contract/contracts/validate_current_evidence_binding.py \
  specs/003-authoring-contract/contracts/test_validate_current_evidence_binding.py \
  specs/003-authoring-contract/contracts/validate-current-evidence-binding.sh \
  specs/003-authoring-contract/contracts/validate-current-evidence-binding.ps1 \
  specs/003-authoring-contract/phase-results/specify-original.json \
  specs/003-authoring-contract/phase-results/specify-spec.md \
  specs/003-authoring-contract/phase-results/pre-binding-run-state.json \
  specs/003-authoring-contract/phase-results/specify.json
git diff --cached --name-only
git diff --cached --check
git status --porcelain=v1 -uall
git write-tree
```

Das staged Inventar muss nach einem order-unabhängigen Vergleich exakt der 48-Pfade-Liste entsprechen; alle anderen Änderungen bleiben unstaged. Dann entsteht genau ein lokaler Reparatur-Commit, kein Push. `repair-checkpoint-manifest.json` wird erst im späteren Feature-Commit erzeugt und bindet Commit, Tree und Rohhash je Pfad; es darf nicht behaupten, im Reparatur-Commit vorhanden gewesen zu sein.

The staged inventory must equal the 48-path list exactly after an order-independent comparison; every other change remains unstaged. One local repair commit follows, with no push. The repair manifest is created only in the later feature commit and must not claim it existed in the repair commit.

## 1. Read-only Ausgangsprüfung / Read-only baseline check

```bash
git branch --show-current
git rev-parse HEAD
git status --short
jq -e '.schemaVersion == "1.0" and (.orderedLogicalTargets | length) == 14 and ([.orderedLogicalTargets[].logicalTargetId] | unique | length) == 14' specs/003-authoring-contract/current-evidence-binding.json
python3 -B specs/003-authoring-contract/contracts/test_validate_current_evidence_binding.py
bash specs/003-authoring-contract/contracts/validate-current-evidence-binding.sh --repo . current-evidence
pwsh -NoProfile -File specs/003-authoring-contract/contracts/validate-current-evidence-binding.ps1 -Repo . -Mode current-evidence
python3 -B specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py
python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-validator.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-lifecycle.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-governance-config.ps1
pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1 -RepositoryRoot .
gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100
bash scripts/check-homogeneity.sh --dry-run --no-patch .
```

Dies ist die vollständige bestehende Ausführungsoberfläche vor dem ersten erwarteten Rotlauf. Jeder unmittelbare Exitcode und der Checkpoint-HEAD werden erfasst. Die ersten drei Bridge-Befehle bestätigen nur den historischen Reparaturzustand; sie ersetzen weder die vier historischen Reviews noch einen neuen META-LH-03-Review. Die dokumentierte 23-Test-Evidence bleibt Supplemental am Checkpoint und wird später nicht gegen das geänderte r2-Blatt ausgeführt.

This is the repaired existing execution surface before the first expected red run. Every immediate exit and the checkpoint head are recorded. The first three bridge commands confirm only the historical repair state; they replace neither the four historical reviews nor a new META-LH-03 review. The two direct governance-config entrypoints are deliberately deferred to the green US1 gate because T016 through T025 add their current-evidence and profile resolution. At this pre-implementation boundary, only the statistics drift scheduled for T065 may remain; every other homogeneity finding blocks. The documented 23-test evidence remains Supplemental at the checkpoint and is not run later against the changed r2 leaf.

### Tests-first-Grenze / Test-first boundary

Nach grünem Baseline-Lauf wird `specs/003-authoring-contract/tests-first-evidence.md` als erster neuer Implementierungspfad angelegt. Erst danach erhält `specs/003-authoring-contract/contracts/test_validate_authoring_contract.py` eine kleinste gültige r1-zu-r2-Fixture und eine negative Fixture mit einem zweiten geänderten Blatt. Der erste Lauf muss aus genau einem lokal verantworteten Grund rot sein: der additive Validator fehlt oder weist die noch nicht implementierte kleinste Regel zurück. Andere Fehler blockieren. Danach wird nur `validate_authoring_contract.py` so weit ergänzt, dass beide Fälle grün sind; alle weiteren Fälle werden nach demselben Test-vor-Implementierung-Muster verbreitert.

After a green baseline, `specs/003-authoring-contract/tests-first-evidence.md` is created as the first new implementation path. Only then does the additive-validator test gain the smallest valid r1-to-r2 fixture and a negative second-changed-leaf fixture. The first run must be red for exactly one locally owned reason: the additive validator is missing or rejects the not-yet-implemented smallest rule. Any other failure blocks. Only the validator is then implemented far enough to make both cases green; every later case follows the same test-before-implementation pattern.

## 2. Drei kanonische Fixture-Suiten / Three canonical fixture suites

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-validator.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-authoring-lifecycle.ps1
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/tests/test-intake-governance-config.ps1
```

Jede Suite muss den unmittelbaren Exitcode festhalten. Die Validator-Suite enthält positive und negative Fälle für einen gesperrten, nicht ausführbaren Receipt-Platzhalter sowie verbotene ausführbare Specify- und Autonomous-Aufrufe. Die Lifecycle-Suite prüft unveränderliche Vorgänger, getrennte logische/physische Pfade, ausschließlich `Proposed`/`Approved`/`Applying`/`Completed`/`Failed`, `Completed` als Erfolg, `Failed` mit Reparaturdetails und identische Zielmengen. Die Konfigurations-Suite prüft Profilpfad, Profil-ID, `de-DE`, Pfadgrenze sowie fehlende oder widersprüchliche Profile.

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

Vor der Erneuerung prüft der additive Validator aktuelle ausdrückliche Update-Autorität, das R1-Ziel, das R1-Receipt, dessen Review-Link, Quellen und Git-Zustand sowie null unvollständige Operationen. Proposal und Operation liegen exakt unter `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/proposal.json` und `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/operation.json`; `proposalNormalizedSha256` bindet die strikte UTF-8-Normalisierung. Die beiden R1-Artefakte werden byte-identisch nach `specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/Lastenheft_META-LH-03-Authoring-Contract.md` und `specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/META-LH-03-Authoring-Contract.json` kopiert. Ziel- und Receipt-Kandidat liegen exakt unter `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/staging/Lastenheft_META-LH-03-Authoring-Contract.md` und `specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/staging/META-LH-03-Authoring-Contract.json`. `intendedTargets`, `validatedTargets` und `publishedTargets` sind exakt gleich.

Nur `Proposed`, `Approved`, `Applying`, `Completed` und `Failed` sind zulässige Operation-Statuswerte. Erfolg ist ausschließlich `Completed`; Fehler ist `Failed`, mit Details in `failure`, `nextAction` und `rollbackBoundary`. Beide folgenden installierten Artefaktvalidatoren müssen vor `Completed` bestehen. Danach supersediert das neue R2-Review-Tripel ausdrücklich die drei hashgebundenen R1-Review-Artefakte.

Before renewal, proposal hash, approval, operation, both isolated staged candidates, both predecessor archives, complete supersedes fields, and equal intended/validated/published sets are checked. Only the five validator-accepted statuses are used: `Completed` succeeds and `Failed` records repair details. Both installed artefact validators must pass before completion, and the exact R2 review triple explicitly supersedes the hash-bound R1 triple.

```bash
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-artifact.sh --artifact specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/operation.json --repo .
```

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-artifact.ps1 -Artifact specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/operation.json -Repo .
```

```bash
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json --repo .
```

```powershell
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json -Repo .
```

## 5. Exakt 14 Receipts über Bash / Exactly 14 receipts through Bash

```bash
set -uo pipefail
receipt_list="$(mktemp)" || exit 1
if ! jq -er '
  if (.orderedLogicalTargets | length) == 14 and
     ([.orderedLogicalTargets[].logicalTargetId] | unique | length) == 14 and
     ([.orderedLogicalTargets[].authoringReceipt.path] | unique | length) == 14
  then .orderedLogicalTargets[].authoringReceipt.path
  else error("Expected exactly 14 unique logical targets and receipt paths")
  end
' specs/003-authoring-contract/current-evidence-binding.json >"$receipt_list"; then
  rm -f -- "$receipt_list"
  exit 1
fi
receipt_count=0
receipt_failures=0
while IFS= read -r receipt_path; do
  receipt_count=$((receipt_count + 1))
  if bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt "$receipt_path" --repo .; then
    receipt_exit=0
  else
    receipt_exit=$?
    receipt_failures=$((receipt_failures + 1))
  fi
  printf '%s\t%s\n' "$receipt_exit" "$receipt_path"
done <"$receipt_list"
rm -f -- "$receipt_list"
if [ "$receipt_count" -ne 14 ] || [ "$receipt_failures" -ne 0 ]; then
  exit 1
fi
```

Die Iteration vermeidet `mapfile`, propagiert jeden `jq`-Fehler, protokolliert alle 14 unmittelbaren Exitcodes und gibt nach vollständiger Inventarprüfung bei mindestens einem Fehler ungleich null zurück. Die negative Harness-Fixture lässt den ersten Receipt-Aufruf scheitern und spätere Aufrufe bestehen; der Gesamtbefehl muss trotzdem scheitern.

The iteration avoids `mapfile`, propagates every `jq` failure, logs all 14 immediate exits, and returns nonzero after the complete inventory if any invocation failed. The negative harness fixture makes the first receipt invocation fail and later ones pass; the aggregate command must still fail.

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
python3 -B specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py
python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready
```

```powershell
pwsh -NoProfile -File specs/003-authoring-contract/contracts/validate-authoring-contract.ps1 -Repo . -Json
```

Der Validator muss am finalen Feature-HEAD den Reparatur-Commit als Ancestor und jeden der 48 Manifestpfade samt Rohhash gegen dessen Tree prüfen. Das erst im Feature-Commit vorhandene `repair-checkpoint-manifest.json` darf nicht als Datei des früheren Reparatur-Commits erwartet werden. Zusätzlich prüft er die finalen fünf Artefakthashes, vollständige `Completed`-Update-Operation, R1-zu-R2-Ziel-, Receipt- und Review-Supersession, beide byte-identischen Archive, genau ein geändertes META-LH-03-Blatt, 13 unveränderte Blätter und die unveränderte Series-Brücke.

At final feature head, the validator proves checkpoint ancestry and validates every manifest path/hash against the repair tree without expecting the later manifest in that earlier commit. It also checks the complete `Completed` Update, all R1-to-R2 supersession links, one changed leaf, 13 unchanged leaves, and the unchanged Series bridge.

### Feature-lokaler Gate-Evidence-Pre-Validator / Feature-local Gate Evidence pre-validator

Tests entstehen zuerst unter `specs/003-authoring-contract/contracts/test_validate_gate_evidence_invariants.py`. Die positiven Fixtures heißen `valid-supplemental-primary-reference.json` und `valid-postmerge-premerge-binding.json`. Die vier separaten Negativ-Fixtures heißen `missing-primary-reference.json`, `wrong-primary-reference.json`, `wrong-premerge-path.json` und `wrong-premerge-hash.json`; alle liegen unter `contracts/fixtures/gate-evidence/`.

Tests are added first at the exact test path. The two positive and four separate negative fixture paths are fixed in the design contract.

```bash
python3 -B specs/003-authoring-contract/contracts/test_validate_gate_evidence_invariants.py
python3 -B specs/003-authoring-contract/contracts/validate_gate_evidence_invariants.py --repo . --requirements specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json --evidence .specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json
```

Der erste Befehl muss die positiven Fälle annehmen und jeden Negativfall einzeln ablehnen. Der zweite Befehl läuft vor dem unveränderten installierten Evidence Core. Für PostMerge wird derselbe Pre-Validator mit `postmerge-gate-requirements.json` und dem exakten PostMerge-Runner-Pfad aufgerufen. Der Pre-Validator erzwingt Supplemental-zu-eindeutigem-Primary-Referenzen sowie den exakt konfigurierten PreMerge-Pfad und seinen Normalhash; der Evidence Core wird nicht als Durchsetzer dieser Regeln dargestellt.

The test accepts both positive fixtures and rejects each negative fixture separately. The pre-validator runs before the unchanged installed Evidence Core for both snapshots. It owns the extra reference and exact path/hash invariants; the Core does not.

## 8. PSScriptAnalyzer und vollständiger Secret-Scan / PSScriptAnalyzer and full secret scan

```powershell
pwsh -NoProfile -File scripts/invoke-psscriptanalyzer.ps1 -RepositoryRoot .
```

```bash
gitleaks dir . --config .gitleaks.toml --no-banner --no-color --redact=100
rg -n 'intake-authoring-governance/tests|authoring.*tests' .gitleaks.toml
```

Das kanonische Analyzer-Skript bindet die Registry-Version `1.25.0`, sammelt Outputobjekte und beendet bei jedem Warning-/Error-Finding mit `1`. Die negative Harness-Fixture erzeugt in einem isolierten temporären Git-Repository eine getrackte PowerShell-Datei mit einem sicheren Analyzer-Finding, ruft dasselbe Skript mit explizitem `-RepositoryRoot`, `-Registry` und `-Settings` auf und verlangt einen von null verschiedenen Gesamtstatus. Der `rg`-Befehl ist eine Inspektion: Sein Treffer darf keine aktive Ausnahme der Authoring-Testpfade zeigen. Falls er keinen Treffer liefert, wird Exitcode `1` als erwartetes „kein Muster gefunden“ protokolliert und nicht als Gitleaks-Erfolg umgedeutet. Nur der unmittelbare Exitcode `0` des vollständigen `gitleaks dir` erfüllt den Secret-Gate.

The canonical analyzer script binds registry version `1.25.0`, collects result objects, and exits `1` for every Warning/Error finding. The negative harness creates a tracked PowerShell file with a safe analyzer finding in an isolated temporary Git repository, invokes the same script with explicit repository root, registry, and settings, and requires a nonzero aggregate status. The `rg` command is an inspection: any match must not show an active exclusion for Authoring test paths. If it has no match, exit code `1` is recorded as expected “pattern not found” and is not reinterpreted as Gitleaks success. Only immediate exit code `0` from the full `gitleaks dir` satisfies the secret gate.

## 9. Reale Drei-Plattform-Matrix / Real three-platform matrix

Die vorhandene Matrix verwendet exakt `ubuntu-22.04`, `macos-14` und `windows-2022`. Der fokussierte Schritt führt Abschnitte 2 bis 8 einschließlich beider negativer Harness-Fälle sowie den realen Global-Ready-Einstieg aus, protokolliert vorab `git rev-parse HEAD`, `bash --version`, `pwsh --version` und `python3 --version` und erfasst nach jedem Fachbefehl den unmittelbaren Exitcode. Auf Windows muss der bereits geprüfte `AOC_GIT_BASH_EXE` verwendet und dessen Verzeichnis vor den PowerShell-Fixtures in `PATH` aufgenommen werden. WSL gilt nicht als Ersatz.

The existing matrix uses exactly `ubuntu-22.04`, `macos-14`, and `windows-2022`. The focused step executes sections 2 through 8, including both negative harnesses and the real Global-Ready entry point, first logs `git rev-parse HEAD`, `bash --version`, `pwsh --version`, and `python3 --version`, and captures the immediate exit after every domain command. On Windows, the validated `AOC_GIT_BASH_EXE` is used and its directory added to `PATH` before PowerShell fixtures. WSL is not a substitute.

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

## 13. PreMerge-Bereitschaft / PreMerge readiness

`.specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json` ist der erhaltene Schema-2.0-Runner-Snapshot für `contracts/autonomous-run-gate-requirements.json`. Er bindet den normalisierten Requirements-Hash und exakten finalen Feature-HEAD. Vor Merge müssen alle PreMerge-Primary-Gates, die vier Reviewberichte, aktuelle verpflichtende Checks, null offene actionable Threads, eine tatsächlich verfügbare erforderliche Approval und normale Merge-Bereitschaft vorliegen. `acceptedPreMergePath`, `acceptedPreMergeSha256` und `mergeCommit` sind leer. Ein ausgeführtes `gh pr merge` oder ein tatsächlicher Merge-Commit darf nicht als PreMerge-Beweis verlangt oder behauptet werden.

The named runtime path is the retained schema-2.0 PreMerge snapshot for the PreMerge requirements. It binds their normalized hash and the exact final feature head. All PreMerge Primary gates, four reviews, current required checks, zero actionable threads, an actually available required approval, and normal-policy merge readiness must exist. The accepted-PreMerge fields and merge commit remain empty. An executed merge command or actual merge commit is neither required nor claimed in PreMerge.

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

Die JSON-Antwort muss den exakten HEAD, aktuelle Required Checks, eine ausreichende tatsächliche Approval, null offene actionable Threads und `mergeStateStatus` als normale Policy-Bereitschaft belegen. Nicht verfügbare oder unvollständige Antworten blockieren. Diese Befehle validieren nur Bereitschaft.

The JSON response must prove exact head, current required checks, sufficient actual approval, zero actionable threads, and normal-policy merge readiness. Unavailable or incomplete responses block. These commands validate readiness only.

Der PreMerge-Snapshot wird zuerst mit dem feature-lokalen Pre-Validator und danach mit dem unveränderten installierten Evidence Core gegen den exakten HEAD validiert:

```bash
reviewed_head="$(git rev-parse HEAD)"
python3 -B specs/003-authoring-contract/contracts/validate_gate_evidence_invariants.py --repo . --requirements specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json --evidence .specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json
python3 -B .specify/presets/autonomous-run-governance/scripts/autonomous-evidence-core.py gate --requirements specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json --evidence .specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json --head "$reviewed_head"
```

Das Core-Ergebnis muss `snapshotType=PreMerge`, `result=Pass` und `mergeAuthorized=false` melden.

The feature-local pre-validator runs first; only then does the unchanged installed Evidence Core validate the same PreMerge snapshot at the exact head. The Core result must report `snapshotType=PreMerge`, `result=Pass`, and `mergeAuthorized=false`.

## 14. Normaler Feature-Merge / Normal feature merge

Erst nach akzeptiertem PreMerge-Snapshot ist der normale Merge ohne `--admin` zulässig. Diese tatsächlichen Befehle gehören ausschließlich zur PostMerge-Evidence:

Only after an accepted PreMerge snapshot is a normal merge without `--admin` allowed. These actual commands belong exclusively to PostMerge evidence:

```bash
gh pr merge "$PR_NUMBER" --merge
git switch main
git pull --ff-only
git rev-list --left-right --count main...origin/main
test -z "$(git status --porcelain)"
```

Der PostMerge-Snapshot muss tatsächliche PR-Nummer/-URL, akzeptierten Feature-HEAD und tatsächlichen Merge-Commit aus `gh pr view` und Git binden. Ein erfolgreicher PreMerge-Snapshot allein behauptet keinen Merge.

The PostMerge snapshot binds actual PR number/URL, accepted feature head, and actual merge commit from GitHub CLI and Git. Passing PreMerge alone does not claim a merge.

## 15. Lifecycle und kausaler Abschluss / Lifecycle and causal closeout

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

PostMerge-Fakten werden erst danach geschrieben. Der Schema-2.0-Snapshot `.specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/postmerge-gate-evidence.json` wird erst nach tatsächlichem Closeout-Merge und finalem Sync erzeugt. Er verwendet `contracts/postmerge-gate-requirements.json`, denselben `reviewedHead` wie PreMerge, den tatsächlichen Feature-`mergeCommit`, `changedPaths: []` und exakt `acceptedPreMergePath=.specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/premerge-gate-evidence.json` plus dessen normalisierten `acceptedPreMergeSha256`. Der feature-lokale Pre-Validator prüft Pfad und Hash zuerst; erst danach läuft der unveränderte Evidence Core.

PostMerge facts are written only afterwards. The snapshot must use the configured literal accepted PreMerge runner path and its normalized hash. The feature-local pre-validator checks both before the unchanged Evidence Core runs.

```bash
reviewed_head="<accepted-full-feature-head>"
merge_commit="<actual-full-feature-merge-commit>"
python3 -B specs/003-authoring-contract/contracts/validate_gate_evidence_invariants.py --repo . --requirements specs/003-authoring-contract/contracts/postmerge-gate-requirements.json --evidence .specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/postmerge-gate-evidence.json
python3 -B .specify/presets/autonomous-run-governance/scripts/autonomous-evidence-core.py gate --requirements specs/003-authoring-contract/contracts/postmerge-gate-requirements.json --evidence .specify/runtime/autonomous-routing/044b77ae-85fd-46ee-97f4-61ce7a2c9c66/postmerge-gate-evidence.json --head "$reviewed_head" --merge-commit "$merge_commit"
```

Der Branch `003-authoring-contract-closeout` besitzt die exakt im Design festgelegte PostMerge-Positivliste:

The `003-authoring-contract-closeout` branch has the exact PostMerge allowlist defined by the design:

```text
specs/003-authoring-contract/tasks.md
specs/003-authoring-contract/autonomous-run-state.json
specs/003-authoring-contract/causal-closeout-evidence.json
specs/003-authoring-contract/engineering-retrospective.md
specs/003-authoring-contract/autonomous-run-evidence.md
```

Der PostMerge-Runner-Snapshot gehört nicht zum Repository-Closeout-Kandidaten; er wird in der separaten exakten Runner-Positivliste geführt. So kann er den tatsächlichen Closeout-Merge und den danach erreichten End-Sync belegen, ohne einen weiteren selbstbezüglichen Evidence-PR auszulösen. Fehlende oder gedriftete PreMerge-Evidence blockiert weiterhin.

The PostMerge runner snapshot is not part of the repository closeout candidate; it is listed in the separate exact runner allowlist. It can therefore prove the actual closeout merge and subsequent final sync without another self-referential evidence PR. Missing or drifted PreMerge evidence still blocks.

Der Feature-Bericht enthält in dieser Reihenfolge `Output`, `Findings`, `confirmed rules`, `interventions/repairs`, `efficiency observations`, `AEPS relevance` und danach `Completion/Retrospective Evidence`. Der Trend `META-LH-01 -> META-LH-02 -> META-LH-03` nennt pro Wert Quellpfad, Quellhash und identische Metrikdefinition; fehlende Vergleichsdaten werden als `Nicht vergleichbar / Not comparable` benannt. Auch der Closeout-PR verwendet normale Checks, Review und Approval ohne Bypass. Der Abschlussnachweis endet mit sauberem Worktree, `main` auf Remote-HEAD und Ahead/Behind `0/0`.

The feature report contains the six named perspectives in order followed by Completion/Retrospective Evidence. The META-LH-01-through-03 trend names source path, source hash, and one identical metric definition for every value; missing comparable data is marked explicitly. The closeout PR also uses normal checks, review, and approval without bypass. Closeout evidence ends with a clean worktree, `main` at remote head, and ahead/behind `0/0`.
