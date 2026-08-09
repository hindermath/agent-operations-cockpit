# Schnellstart: META-LH-01-Validierung / Quickstart: META-LH-01 Validation

## Zweck und Proof-Grenze / Purpose and Proof Boundary

Dieser Leitfaden prueft die spaetere Dokumentationsumsetzung und den deterministischen META-LH-01-Lifecycle. Der einzige feature-lokale ausfuehrbare Vertrag ist `contracts/validate_meta_lh01.py`; er nutzt nur die Python-Standardbibliothek und schreibt nicht in Repository, Index oder Worktree. `candidate-list` und `render-gate-evidence` schreiben je eine ausdruecklich benannte temporaere Datei ausserhalb des Repositorys. Nach dem terminalen Rename erzeugt die Review-Pruefung ausserhalb des Repositorys zusaetzlich eine automatisch entfernte Projektion: Sie stellt exakt die bereits hashgeprueften Archivbytes am unveraenderlichen logischen Originalpfad bereit und bindet die vorhandene Review-Evidence nur lesend ein. Maschinenchecks beweisen Struktur, Hashes, Pfadtransition und Evidence-Vollstaendigkeit. Fachliche Wahrheit, Sprache, Zugaenglichkeit und Publikationseignung benoetigen getrennte unabhaengige Review-Evidence. / The standard-library contract remains repository-read-only; post-rename review validation uses a short-lived external projection of the proven archive bytes at the immutable logical path.

Die aktuelle Benutzeranweisung autorisiert den vollstaendigen META-LH-01-Lauf, Commit, Push, PR, `MergeAndSync` und Admin-Bypass nur als letzten Approval-Fallback. Der gespeicherte Modus allein ist keine Autoritaet. Vor jeder irreversiblen Aktion und bei Drift werden Scope, Hashes, Evidence und diese aktuelle Autoritaet fail-closed neu geprueft. Solange sie aktuell bleibt, wird keine neue Autorisierung angefordert. / The current user instruction authorises the complete run and bounded closeout. Stored mode alone is not authority. Revalidate fail closed before every irreversible action and on drift; do not request renewed authority while it remains current.

## Voraussetzungen / Prerequisites

- Repository-Wurzel und Branch: `AgentOperationsCockpit`, `001-programmquellen-baseline`. / Repository root and branch as named.
- Werkzeuge: `python3`, `git`, `bash`, `pwsh` 7+, `gitleaks`; `gh` und `jq` erst im Remote-Closeout. / Tools as named; remote tools only during closeout.
- Exakte Regeln: [Validierungsvertrag](contracts/baseline-validation-contract.md), [Kandidaten-Allowlist](contracts/candidate-paths.json), `intake-lifecycle.json` und `autonomous-run-gate-requirements.json`. / Exact rules are in the linked contracts and lifecycle record.

### Verbindliche Fixpunkt-Reihenfolge / Binding Fixed-point Order

Die nummerierten Abschnitte liefern die Befehle; ausgefuehrt werden sie in dieser fail-closed Reihenfolge: Lifecycle-Datensatz, Domain und alle Feature-Artefakte; eingebetteter Skriptkatalog; getrennte semantische und Accessibility-Reviews; AEPS-Receipt und gegebenenfalls vollstaendiger Ledger-Abschnitt; Statistik; vorbenannte Public-Content- und Documentation-Impact-Dateien als vorhandene Pfadanker; Kandidatenmenge eins; Secret-Scans und Vervollstaendigung beider Evidence-Dateien gegen die normale Kandidatenmenge plus Original-/Archivtransition; Kandidatenmenge zwei; bytegleicher Vergleich und `candidate-fixpoint`; Public-Content-/Documentation-Impact-Validierung; Stage und normaler Commit; erst danach terminaler Rename-Commit. / Execute the fixed point for the normal candidate first, with public/documentation inventories expanded by the lifecycle transition; commit it before the terminal rename commit.

## 1. Akzeptierte Eingaben vor jedem Edit / Accepted Inputs Before Every Edit

```bash
test "$(git branch --show-current)" = "001-programmquellen-baseline"
git merge-base --is-ancestor b8eb0735b2a7c46a65712d2e280242c85f8c1d64 HEAD
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . input-bindings --surface bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . input-bindings --surface powershell
```

Jeder Python-Aufruf bindet genau drei logische akzeptierte META-LH-01-Artefakte und den schema-1.1-Lifecycle-Vertrag. Vor Implement laufen generische Receipt-/Review-Pruefungen. Nur bei exakt `stage: Implement`, `status: Active`, `lastPassingGate: GlobalReadyBeforeImplement`, aktuellem Git-Branch und passenden Run-/Lifecycle-Bindungen validiert die Oberflaeche zusaetzlich den vollstaendigen 14-Ziel-Snapshot und ersetzt ausschliesslich die Receipt-Quellenfrische; ihre installierte Run-State- und Review-Oberflaeche laeuft weiter. Nach dem Rename erhaelt die unveraenderte Review-Oberflaeche eine kurzlebige externe Projektion der geprueften Archivbytes am urspruenglichen logischen Pfad. Vor dem Rename existiert nur der Originalpfad, danach nur der exakte Archivpfad. Erwartet ist je genau eine `PASS:`-Zeile. / After rename, the unchanged installed review surface validates an external projection of the proven archive bytes at the original logical path.

## 2. Globales 14er-Gate / Global Fourteen-target Gate

Unmittelbar vor Tasks, jedem Analyze-Lauf und Implement: / Run immediately before Tasks, every Analyze run, and Implement:

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . global-ready
```

Der Modus zaehlt exakt vierzehn logische Ziele und laesst META-LH-01 logisch zuerst. Im aktuellen qualifizierten Zustand muss die Ausgabe `qualified immutable programme snapshot` nennen. Der Snapshot bindet je Ziel den normalisierten Zielhash sowie Pfad/Rohhash des eindeutig aktuellen Receipts und Ready-Single-Review-Leaves. Beide installierten Review-Validatoren laufen fuer alle 14 Ziele. Fehlende, duplizierte oder umsortierte Ziele; falsche Pfade, Hashes oder Bytes; non-Ready oder mehrdeutige Leaves; falsche Stage, Status, Last-Gate, Run-ID, Branch oder Lifecycle-Bindung blockieren. / The qualified output names the immutable programme snapshot. All fourteen ordered target/receipt/review bindings and both review surfaces remain mandatory; every listed drift fails closed.

## 3. Contract-Tests und Domain-Vertrag / Contract Tests and Domain Contract

Die Tests verwenden nur temporaere Fixtures. Sie veraendern weder reales Repository noch Index oder Worktree. / Tests use temporary fixtures only and do not touch real repository state.

```bash
python3 specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . domain
```

Erwartet ist `PASS: contract-tests: 66 isolated positive/negative cases` und genau eine Domain-`PASS:`-Zeile. Die vorhandenen 43 Faelle bleiben erhalten; 23 neue Faelle pruefen die drei positiven Post-Implement-Oberflaechen und jede geforderte Snapshot-/Drift-Grenze. / Expect 66 isolated cases: the preserved 43 plus 23 snapshot and drift cases.

## 4. Maschinenstruktur und unabhaengige Semantik / Machine Structure and Independent Semantics

Der neue getrackte Python-Vertrag und sein Test erweitern das generierte Inventar eingebetteter Skripte. Vor dem schreibenden Renderer erfolgt eine Vorschau; danach werden Inventar und Homogeneity check-only geprueft. `docs/scripts/reference.md` darf dabei ohne Aenderung unter `scripts/` nicht driften. Homogeneity beweist nur Struktur und Repository-Konventionen. / The new tracked Python contract and test extend the generated embedded-script inventory. Preview precedes the write, followed by check-only and homogeneity validation. The canonical script reference must not drift without a change under `scripts/`; homogeneity proves only structure and repository conventions.

```bash
pwsh -NoProfile -File scripts/render-script-reference.ps1 -Repo . -WhatIf
pwsh -NoProfile -File scripts/render-script-reference.ps1 -Repo .
pwsh -NoProfile -File scripts/render-script-reference.ps1 -Repo . -CheckOnly
bash scripts/check-homogeneity.sh --json --dry-run --no-patch .
pwsh -NoProfile -File scripts/check-homogeneity.ps1 -TargetDir . -Json -DryRun -NoPatch
```

Eine unabhaengige semantische Rolle erfasst Schema 1.0 fuer DE zuerst, gleichwertiges EN, CEFR B2, Erstnutzungsbegriffe, fachliche Wahrheit und Authority-Auslegung. Eine davon getrennte unabhaengige A11Y-Rolle erfasst Heading-Hierarchie beziehungsweise strukturierte Lesereihenfolge, beschreibende Felder/Links, Text-first, Status ohne Nur-Farbe und WCAG-2.2-AA-Anwendbarkeit. Beide Dateien decken die sechs Domain-Pfade plus den nutzerlesbaren Pending-Anker `causal-closeout-evidence.json` exakt ab und besitzen jeweils `blockingFindings: []`. / Independent semantic and accessibility roles cover the six domain paths plus the readable Pending causal-closeout anchor.

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . review-evidence --kind semantic \
  --evidence specs/001-programmquellen-baseline/semantic-review-evidence.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . review-evidence --kind accessibility \
  --evidence specs/001-programmquellen-baseline/accessibility-review-evidence.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
```

Der Modus beweist nur Vollstaendigkeit und Pass-Ergebnisse der jeweiligen unabhaengigen Evidence, nicht die Semantik oder Accessibility selbst. / The mode proves evidence completeness and pass results, not semantic or accessibility truth itself.

## 5. Secret-Muster und Public Content / Secret Patterns and Public Content

Die Maschinenbefehle beweisen nur Secret-Muster: / Machine commands prove only secret-pattern results:

```bash
gitleaks dir --redact --no-banner --no-color requirements/baseline
gitleaks dir --redact --no-banner --no-color specs/001-programmquellen-baseline
bash scripts/scan-agent-secrets.sh --fail-on-high .
pwsh -NoProfile -File scripts/scan-agent-secrets.ps1 -FailOnHigh -WorkspaceRoot .
```

Eine getrennte unabhaengige Public-Content-Review erfasst fuer exakt jeden Pfad der Kandidatenmenge eins einschliesslich Pending-Closeout-Anker plus `intake-lifecycle.json`, Originalpfad und Archivpfad `Pass`/`Fail` samt Begruendung. Der folgende Validator erweitert die temporaere Kandidatenliste deterministisch um diese Transition und laeuft erst nach dem bytegleichen Fixpunkt in Abschnitt 8. / A separate independent review covers the normal candidate including the Pending closeout anchor plus the lifecycle transition.

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . review-evidence --kind public \
  --evidence specs/001-programmquellen-baseline/public-content-review-evidence.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
```

## 6. AEPS und Documentation Impact / AEPS and Documentation Impact

Der AEPS-Receipt und bei `Finding` sein vollstaendiger Ledger-Abschnitt entstehen vor Kandidatenmenge eins. Der Validator prueft alle Pflichtfelder, Source-/Receipt-Bindung, Capture- und Upstream-Status. `NoChange` veraendert das Ledger nicht. / The AEPS receipt and any complete Finding ledger section exist before candidate set one; NoChange leaves the ledger unchanged.

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . aeps \
  --receipt docs/aeps/receipts/meta-lh-01-programmquellen-implementation.md
```

`documentation-impact-evidence.json` wird als vorbenannter Pfadanker vor Kandidatenmenge eins angelegt. Es verwendet Schema 1.1, genau einen `UpdateRequired`-Eintrag und den Ready-geprueften Originalpfad als logische `canonicalSource`; `documents` umfasst die normale Kandidatenmenge einschliesslich des bereits vorhandenen Pending-Closeout-Ankers plus Lifecycle-Datensatz, Original- und Archivpfad. Sein Validator laeuft erst nach Abschnitt 8. / Documentation Impact covers the normal candidate including the Pending closeout anchor plus the full lifecycle transition.

## 7. Statistik / Statistics

Erst nach abgeschlossener Implementierung: / Only after completed implementation:

```bash
bash scripts/render-project-statistics.sh --repo .
bash scripts/render-project-statistics.sh --repo . --check-only
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo . -CheckOnly
```

## 8. Kandidaten-Fixpunkt und Evidence-Abschluss / Candidate Fixed Point and Evidence Closure

Zu diesem Zeitpunkt existieren alle sonstigen Lieferartefakte einschliesslich `intake-lifecycle.json` und `causal-closeout-evidence.json` im Zustand `Pending`. `public-content-review-evidence.json` und `documentation-impact-evidence.json` sind ebenfalls vorbenannte Pfadanker. Die erste Ableitung ist die normale Kandidatenmenge; die beiden Evidence-Inventare enthalten den Closeout-Anker und ergaenzen deterministisch Original- und Archivpfad. / All normal delivery artefacts exist, including the Pending causal-closeout anchor; public and documentation inventories include it and both rename paths.

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . candidate-list \
  --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json \
  --output /tmp/001-programmquellen-baseline-expected-paths.txt
sed -n '1,240p' /tmp/001-programmquellen-baseline-expected-paths.txt

# Jetzt Public-Content- und Documentation-Impact-Dateien gegen Menge eins vervollstaendigen.
# Now complete the two evidence files against candidate set one.

python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . candidate-list \
  --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json \
  --output /tmp/001-programmquellen-baseline-expected-paths-r2.txt
cmp /tmp/001-programmquellen-baseline-expected-paths.txt \
  /tmp/001-programmquellen-baseline-expected-paths-r2.txt
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . candidate-fixpoint \
  --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . review-evidence --kind public \
  --evidence specs/001-programmquellen-baseline/public-content-review-evidence.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . documentation-impact \
  --evidence specs/001-programmquellen-baseline/documentation-impact-evidence.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
```

Jede Pfadabweichung, jedes spaeter neu erzeugte Artefakt oder eine fehlende Evidence-Datei verwirft beide Listen und beginnt Abschnitt 8 neu. / Any path drift or later-created artefact invalidates both lists and restarts section 8.

## 9. Exakten Kandidaten stagen und pruefen / Stage and Validate the Exact Candidate

Die eingefrorene Liste wird einzeln gestaged; keine Verzeichnis- oder Punkt-Wildcard ist erlaubt. Vor `git add` werden aktuelle Autoritaet, Scope und Evidence erneut bestaetigt. / Stage each frozen path explicitly; directory and dot wildcards are forbidden. Reconfirm current authority, scope, and evidence before staging.

```bash
while IFS= read -r candidate_path; do
  git add -- "$candidate_path"
done < /tmp/001-programmquellen-baseline-expected-paths.txt
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . candidate \
  --allowlist specs/001-programmquellen-baseline/contracts/candidate-paths.json \
  --expected-paths /tmp/001-programmquellen-baseline-expected-paths.txt
```

Der Modus verlangt exakte staged Gleichheit, liest `git status --porcelain=v1 -z` einschliesslich untracked, blockiert unstaged Kandidatenreste und fuehrt `git diff --cached --check` aus. Fremde unstaged oder untracked Pfade werden nicht veraendert. / The mode requires exact staged equality, reconciles porcelain including untracked paths, blocks unstaged candidate residue, and runs the staged whitespace check. Unrelated unstaged work is untouched.

## 10. Normaler Commit und terminaler Rename-Commit / Normal Commit and Terminal Rename Commit

Diese Befehle laufen erst nach Tasks, Analyze, Implement und allen lokalen Gates. Die aktuelle Autoritaet wird unmittelbar vor Commit, Push und PR erneut fail-closed geprueft; solange keine Drift vorliegt, ist keine neue Anfrage erforderlich. / Run only after downstream phases and all local gates. Revalidate current authority before every irreversible action; no renewed request is needed without drift.

```bash
set -euo pipefail
git commit -m "docs: establish self-contained programme baseline" \
  -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
committed_head=$(git rev-parse HEAD)
git show -s --format=%B "$committed_head" \
  | rg -Fx "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

# Letzte Polish-Aktion und letzter Feature-Branch-Commit; vorher keine Stage-/Kandidatenreste.
# Last Polish action and last feature-branch commit; no staged/candidate residue beforehand.
bash scripts/rename-lastenheft.sh \
  requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md \
  001-programmquellen-baseline
terminal_head=$(git rev-parse HEAD)
test "$terminal_head" != "$committed_head"
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . terminal-rename

cat >/tmp/001-programmquellen-baseline-pr-body.md <<'EOF'
## Betroffene Skripte und Dokumente / Affected scripts and documents

- Exakte Kandidatenliste aus `/tmp/001-programmquellen-baseline-expected-paths.txt`.

## Manuelle Pruefung / Manual verification

- Dokumentierte Vorschau-, Schreib- und Check-only-Befehle einschliesslich `-WhatIf` und ihrer tatsaechlichen Ergebnisse.

## Beispielausgabe / Sample output

- Reale `PASS:`-Zeilen der lokalen Validatoren; keine neue nutzerseitige Konsolenoberflaeche.

## Security-Risiko / Security risk

- Keine Hook- oder Scannerlogik geaendert; Secret-Pattern-Scans wurden getrennt ausgefuehrt und ueberbehaupten keine Publikationseignung.
EOF

for required_heading in \
  "Betroffene Skripte und Dokumente / Affected scripts and documents" \
  "Manuelle Pruefung / Manual verification" \
  "Beispielausgabe / Sample output" \
  "Security-Risiko / Security risk"; do
  rg -Fx "## ${required_heading}" /tmp/001-programmquellen-baseline-pr-body.md
done

git push --set-upstream origin 001-programmquellen-baseline
if ! pr_number=$(gh pr view --json number --jq .number 2>/dev/null); then
  gh pr create \
    --title "docs: establish self-contained programme baseline" \
    --body-file /tmp/001-programmquellen-baseline-pr-body.md
  pr_number=$(gh pr view --json number --jq .number)
else
  gh pr edit "$pr_number" \
    --body-file /tmp/001-programmquellen-baseline-pr-body.md
fi
reviewed_head=$(git rev-parse HEAD)
test "$reviewed_head" = "$terminal_head"
test "$(gh pr view "$pr_number" --json headRefOid --jq .headRefOid)" = "$reviewed_head"
```

Der normale Kandidat ist `committed_head`; der ausschliessliche Folgecommit ist `terminal_head`. Kein weiterer Feature-Head-Commit darf zwischen `terminal_head`/`reviewed_head` und Merge entstehen. PR-Body, Push, Exact-Head-Evidence und Review folgen erst nach dem Rename. / The normal candidate head is followed only by the terminal rename head; no later feature-head commit is allowed.

## 11. Checks, Review-Entscheidung und Threads konvergieren / Converge Checks, Review Decision, and Threads

```bash
gh pr checks "$pr_number" --watch --fail-fast
gh pr checks "$pr_number" --json bucket,name,state,link \
  > /tmp/001-programmquellen-baseline-all-checks.json
gh pr checks "$pr_number" --required --json bucket,name,state,link \
  > /tmp/001-programmquellen-baseline-required-checks.json
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . check-inventory \
  --all-checks /tmp/001-programmquellen-baseline-all-checks.json \
  --required-checks /tmp/001-programmquellen-baseline-required-checks.json
review_decision=$(gh pr view "$pr_number" --json reviewDecision --jq .reviewDecision)
test "$review_decision" != "CHANGES_REQUESTED"

repo_name=$(gh repo view --json name --jq .name)
repo_owner=$(gh repo view --json owner --jq .owner.login)
open_threads=$(gh api graphql --paginate --slurp \
  -f owner="$repo_owner" -f name="$repo_name" -F number="$pr_number" \
  -f query='query($owner:String!,$name:String!,$number:Int!,$endCursor:String){repository(owner:$owner,name:$name){pullRequest(number:$number){reviewThreads(first:100,after:$endCursor){nodes{isResolved isOutdated}pageInfo{hasNextPage endCursor}}}}}' \
  --jq '[.. | objects | select(has("isResolved")) | select(.isResolved == false and .isOutdated == false)] | length')
test "$open_threads" = "0"
test "$(gh pr view "$pr_number" --json headRefOid --jq .headRefOid)" = "$reviewed_head"
```

`check-inventory` verlangt eine nichtleere All-Checks-Menge und eine nichtleere Required-Teilmenge; jeder Check ist terminal `pass` oder `skipping`. Damit blockiert auch ein fehlgeschlagener nicht-required Check. Die Exact-Head-Evidence verlangt ausserdem eine Review-Entscheidung ohne `CHANGES_REQUESTED`, aber noch nicht `APPROVED`. Normaler Merge verlangt spaeter eine aktuelle unabhaengige `APPROVED`-Entscheidung. Fehlt nur diese, kann ausschliesslich der eng begrenzte Admin-Fallback ausloesen. / Every reported check, including non-required checks, must be terminal-successful. Approval remains the only permitted admin-fallback blocker.

## 12. Commands und Runner aus Definitionen oder Logs / Derive Commands and Runners from Definitions or Logs

Fuer jeden Check des exakten Heads werden Workflow-Definition, Jobmetadaten und Logs temporaer erfasst. Der unabhaengige Reviewer ordnet jeden Gate-Scope nur einem tatsaechlich ausgefuehrten Command und Runner zu; Check-/Jobnamen allein genuegen nicht. / Capture workflow definitions, job metadata, and logs temporarily for the exact head. An independent reviewer maps each gate only to commands and runners actually executed; names alone are insufficient.

```bash
gh run list --commit "$reviewed_head" --json databaseId,headSha,conclusion,workflowName \
  > /tmp/001-programmquellen-baseline-runs.json
python3 - <<'PY'
import json, subprocess
runs = json.load(open('/tmp/001-programmquellen-baseline-runs.json', encoding='utf-8'))
for run in runs:
    run_id = str(run['databaseId'])
    with open(f'/tmp/001-programmquellen-baseline-run-{run_id}.log', 'w', encoding='utf-8') as target:
        subprocess.run(['gh', 'run', 'view', run_id, '--log'], check=True, text=True, stdout=target)
    with open(f'/tmp/001-programmquellen-baseline-jobs-{run_id}.json', 'w', encoding='utf-8') as target:
        subprocess.run(['gh', 'api', f'repos/{{owner}}/{{repo}}/actions/runs/{run_id}/jobs'], check=True, text=True, stdout=target)
PY
```

Aus diesen Nachweisen und den lokalen Gate-Ausgaben entsteht `/tmp/001-programmquellen-baseline-execution-record.json`. Er verwendet Schema 1.0, denselben `reviewedHead` und genau eine `Pass`-Zeile je `Applicable` Gate mit `provider`, `runId`, `workflow`, `job`, `runnerOrPlatform`, `executedCommand` und `evidenceReference`. / These sources and local gate logs form one schema-1.0 execution record with exact executed commands and runners.

## 13. Temporaere Exact-Head-Evidence tatsaechlich erzeugen / Actually Create Temporary Exact-head Evidence

Der erste Befehl erzeugt die temporaere Evidence; die folgenden beiden validieren sie. Keiner schreibt in das Repository. / The first command creates temporary evidence; the next two validate it. None writes to the repository.

```bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . render-gate-evidence \
  --requirements specs/001-programmquellen-baseline/autonomous-run-gate-requirements.json \
  --execution-record /tmp/001-programmquellen-baseline-execution-record.json \
  --head "$reviewed_head" \
  --output /tmp/001-programmquellen-baseline-gate-evidence.json

bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/001-programmquellen-baseline/autonomous-run-gate-requirements.json \
  --evidence /tmp/001-programmquellen-baseline-gate-evidence.json \
  --head "$reviewed_head"
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.ps1 \
  -Requirements specs/001-programmquellen-baseline/autonomous-run-gate-requirements.json \
  -Evidence /tmp/001-programmquellen-baseline-gate-evidence.json \
  -Head "$reviewed_head"
```

Danach PR-Head, Checks, Review und Threads erneut pruefen. Jede Drift verwirft die temporaere Evidence und beginnt ab dem betroffenen Gate neu. / Recheck PR head, checks, review, and threads afterward. Any drift invalidates temporary evidence.

## 14. Feature-Merge und synchronisiertes Main / Feature Merge and Synchronized Main

Normalfall mit unabhaengiger Approval: / Normal path with independent Approval:

```bash
test "$(gh pr view "$pr_number" --json reviewDecision --jq .reviewDecision)" = "APPROVED"
test "$(gh pr view "$pr_number" --json headRefOid --jq .headRefOid)" = "$reviewed_head"
gh pr merge "$pr_number" --merge --delete-branch
git switch main
git pull --ff-only
```

Admin-Bypass ist nur erlaubt, wenn die unabhaengige Approval der einzige verbleibende Blocker ist: alle Checks erfolgreich, Exact-Head-Evidence auf beiden Oberflaechen gueltig, keine Change Request, null actionable Threads, unveraenderter PR-Head und aktuelle Authority. Dann und nur dann darf statt des normalen Merge-Befehls `gh pr merge "$pr_number" --merge --delete-branch --admin` laufen. / Admin bypass is permitted only when independent Approval is the sole remaining blocker after checks, exact-head evidence, no change request, zero actionable threads, exact PR head, and current authority all pass.

Der Feature-Branch bleibt nach `terminal_head` unveraendert. Merge, Branch-Cleanup und dieser Fast-forward-Sync stehen nicht in der Pre-Merge-Primary-Evidence. Die folgenden Schritte beginnen ausschliesslich auf sauberem, synchronisiertem `main`. / The feature branch remains immutable after the terminal head. The next steps begin only from clean synchronized main.

## 15. Exakte Drei-Pfad-Closeout-Transaktion / Exact Three-Path Closeout Transaction

```bash
closeout_branch=codex/001-programmquellen-baseline-closeout
git status --short
test "$(git rev-list --left-right --count main...origin/main)" = $'0\t0'
git switch -c "$closeout_branch" main

# Archivbewusste Finalvalidierung vor jeder terminalen Behauptung.
# Archive-aware final validation before any terminal claim.
python3 -B specs/001-programmquellen-baseline/contracts/test_validate_meta_lh01.py
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . input-bindings --surface bash
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . input-bindings --surface powershell
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . domain
```

Danach werden nur tatsaechliche Feature-PR-Merge-, Main-Sync-, Post-Merge- und Validierungsfakten in `causal-closeout-evidence.json` geschrieben. Jede Task-Zeile T001-T066 wird geprueft, `tasks.completed == tasks.total == 66` gesetzt und der rohe SHA-256 der vollstaendig geprueften `tasks.md` in den State uebernommen. Der State wird Schema 1.1 `Completed`, `stage: MergeAndSync`, alle anwendbaren Closeout-Felder terminal und `nextExactAction: N/A`. Documentation Impact und Public Content werden unabhaengig fuer exakt die drei folgenden Pfade neu geprueft: / Then record only actual prior facts, check T001-T066, bind the raw tasks hash, complete the schema-1.1 state, and independently re-review exactly these paths:

```text
specs/001-programmquellen-baseline/tasks.md
specs/001-programmquellen-baseline/autonomous-run-state.json
specs/001-programmquellen-baseline/causal-closeout-evidence.json
```

Das Command-/Result-Inventar besitzt genau diese `checkId`-Werte: `feature-pr-merge`, `main-fast-forward-sync`, `post-merge-actions`, `archive-input-bindings-bash`, `archive-input-bindings-powershell`, `global-ready-14`, `contract-tests-66`, `domain`, `run-state-bash`, `run-state-powershell`, `task-hash` und `git-diff-check`. Jede Zeile nennt den tatsaechlichen Befehl, `Pass` oder begruendetes `N/A` sowie eine Evidence-Referenz. / The command/result inventory contains exactly the named check IDs, actual command, Pass or justified N/A, and an evidence reference.

`nonSelfReferentialBoundary.containingCommitSha`, `closeoutPullRequest` und `closeoutMergeSha` bleiben `N/A`. Anschliessend werden exakt diese drei Pfade einzeln gestaged und validiert: / The three self-publication fields remain N/A. Stage and validate exactly the three paths:

```bash
git add -- specs/001-programmquellen-baseline/tasks.md
git add -- specs/001-programmquellen-baseline/autonomous-run-state.json
git add -- specs/001-programmquellen-baseline/causal-closeout-evidence.json
python3 specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py \
  --repo . causal-closeout
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh \
  --state specs/001-programmquellen-baseline/autonomous-run-state.json
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.ps1 \
  -State specs/001-programmquellen-baseline/autonomous-run-state.json
git diff --cached --check
git commit -m "docs: persist META-LH-01 causal closeout" \
  -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
closeout_head=$(git rev-parse HEAD)
```

Dieser Commit ist der letzte lokale Akt von T066. Er beansprucht weder seine eigene Commit-ID noch seinen spaeteren PR oder Merge. / This commit is the last local act of T066 and claims none of its own publication facts.

## 16. Closeout-PR unveraendert publizieren / Publish the Immutable Closeout PR

Vor jeder Publikation wird der Closeout-PR-Body in eine temporaere Datei geschrieben. Sein Pfadinventar nennt exakt die drei Closeout-Pfade; alle vier Constitution-Pflichtueberschriften muessen vor Push und PR-Publikation jeweils genau einmal bestehen. / Before publication, write the closeout PR body to a temporary file. Its affected-path inventory names exactly the three closeout paths, and each of the four mandatory Constitution headings must validate exactly once before push and PR publication.

```bash
closeout_pr_body=/tmp/001-programmquellen-baseline-closeout-pr-body.md
cat >"$closeout_pr_body" <<'EOF'
## Betroffene Skripte und Dokumente / Affected scripts and documents

- `specs/001-programmquellen-baseline/tasks.md`
- `specs/001-programmquellen-baseline/autonomous-run-state.json`
- `specs/001-programmquellen-baseline/causal-closeout-evidence.json`

## Manuelle Pruefung / Manual verification

- `causal-closeout`, beide Run-State-Validatoroberflaechen und `git diff --cached --check` bestanden fuer das exakte Drei-Pfad-Delta. / `causal-closeout`, both run-state validator surfaces, and `git diff --cached --check` passed for the exact three-path delta.

## Beispielausgabe / Sample output

- `N/A`: Der reine Dokumentations-, Status- und Evidence-Closeout aendert keine nutzerseitige Konsolenausgabe; die tatsaechlichen Validatorergebnisse werden als externe Laufnachweise aufbewahrt. / `N/A`: This documentation, state, and evidence closeout changes no user-visible console output; actual validator results are retained as external run evidence.

## Security-Risiko / Security risk

- Keine Hook- oder Scannerlogik geaendert; das exakt drei Pfade umfassende Delta wurde auf Secrets, private Pfade und unnoetige personenbezogene Daten geprueft. / No hook or scanner logic changed; the exact three-path delta was reviewed for secrets, private paths, and unnecessary personal data.
EOF

for required_heading in \
  "Betroffene Skripte und Dokumente / Affected scripts and documents" \
  "Manuelle Pruefung / Manual verification" \
  "Beispielausgabe / Sample output" \
  "Security-Risiko / Security risk"; do
  test "$(rg -Fxc "## ${required_heading}" "$closeout_pr_body")" = "1"
done
test "$(rg -c '^## ' "$closeout_pr_body")" = "4"

test "$(git rev-parse HEAD)" = "$closeout_head"
git push --set-upstream origin "$closeout_branch"
if ! closeout_pr_number=$(gh pr view "$closeout_branch" --json number --jq .number 2>/dev/null); then
  gh pr create \
    --base main \
    --head "$closeout_branch" \
    --title "docs: persist META-LH-01 causal closeout" \
    --body-file "$closeout_pr_body"
  closeout_pr_number=$(gh pr view "$closeout_branch" --json number --jq .number)
else
  gh pr edit "$closeout_pr_number" --body-file "$closeout_pr_body"
fi
test "$(git rev-parse HEAD)" = "$closeout_head"
test "$(gh pr view "$closeout_pr_number" --json headRefOid --jq .headRefOid)" = "$closeout_head"
gh pr checks "$closeout_pr_number" --watch --fail-fast
# All-/Required-Checks mit check-inventory, Review-Decision und paginierte Threads wie Abschnitt 11 pruefen.
# Validate all/required checks, review decision, and paginated threads as in section 11.
gh pr merge "$closeout_pr_number" --merge --delete-branch
git switch main
git pull --ff-only
test "$(git rev-list --left-right --count main...origin/main)" = $'0\t0'
test -z "$(git status --porcelain)"
```

Nach der Body- und Exact-Head-Pruefung gelten dieselben Provider-Grenzen wie fuer den Feature-PR: unabhaengiger Review, alle Checks terminal erfolgreich, nichtleere Required-Teilmenge, keine `CHANGES_REQUESTED`, null handlungsrelevante nicht-veraltete Threads und normaler Merge. Der vorhandene Admin-Fallback ist nur zulaessig, wenn Approval der einzige verbleibende Blocker ist. Closeout-PR-Nummer und Merge-SHA werden danach extern berichtet. Es gibt keine neue Task-Checkbox und keine Mutation des Closeout-Commits. / After body and exact-head validation, require the same independent review, all-check and non-empty required-check convergence, no change request, zero actionable threads, and normal merge as for the feature PR. The existing admin fallback remains limited to approval as the sole blocker. Report the closeout PR number and merge SHA externally without another task or closeout-commit mutation.
