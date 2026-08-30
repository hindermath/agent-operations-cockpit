# Schnellstart: Portfolio-Ownership-Validierung / Quickstart: Portfolio Ownership Validation

## Zweck und Proof-Grenze / Purpose and proof boundary

Dieser Leitfaden beschreibt die spaetere Ausfuehrung des dokumentarischen Deltas. Er implementiert nichts waehrend der Planungsphase. Automatische Checks beweisen Struktur, Hashes, Pfade, Ownership-/DAG-Regeln und Evidence-Vollstaendigkeit. Fachliche Decision-Aktualitaet, Verstaendlichkeit, Accessibility und Publikationseignung benoetigen die benannten unabhaengigen Reviews. / *This guide describes later execution of the documentary delta. It implements nothing during planning. Machine checks prove structure, hashes, paths, ownership/DAG rules, and evidence completeness. Decision currency, comprehension, accessibility, and publication suitability require the named independent reviews.*

## Voraussetzungen / Prerequisites

- Repository-Wurzel und Branch: `AgentOperationsCockpit`, `002-portfolio-ownership`. / Repository root and branch as named.
- Werkzeuge lokal: `git`, `python3`, `rg`, `bash`, `pwsh` 7+, `gitleaks`; `gh` erst im Remote-Closeout. / Local tools as named; `gh` only for remote closeout.
- Vertraege: [Planungs- und Validierungsvertrag](contracts/planning-validation-contract.md), [Delivery-Allowlist](contracts/delivery-allowlist.json), [Gate-Requirements](autonomous-run-gate-requirements.json). / Contracts are linked above.
- Schreibgrenze: Kein Produktcode, kein RAW-Start, kein Level 0, keine Preset-Promotion und keine Remote-Aktion vor ihren spaeter autorisierten Gates. / No product code, RAW start, Level 0, preset promotion, or premature remote action.

## 0. Finale Windows-Ziel-/Exitcode-Grenze fuer PR #29 / Final Windows target and exit-code boundary for PR #29

Die publizierten R-022-Heads `68a1af27eba8e1984a97e85325ee01c6c28f490a` und `7eb747056898c26b0cbcfbe9081bd568a7fd7116` bleiben unveraenderliche historische Evidence. Auf `7eb7470` melden 18/18 Checks Erfolg; das exakte `windows-2022`-Log beweist dennoch 8 Failures und 1 Error der Python-Suite. Ihr `LASTEXITCODE` wurde vor den spaeteren Peers nicht geprueft und dadurch ueberschrieben. Der gemeinsame Fehler `META-LH-02 exact Git target blob raw SHA-256 drift` ist zugleich kein zulaessiges aktuelles Zielgate: Das physische Ziel wird normalisiert ueber UTF-8 und LF/CRLF gebunden, waehrend rohe Byte-Unveraenderlichkeit nur fuer Authoring Receipt und Ready Review gilt. `implement-resume-9` ist deshalb trotz Provider-Scheingruen `Blocked`. Kein Befehl dieses Abschnitts wird in der Planphase ausgefuehrt. / *The published R-022 heads are immutable. Exact Windows command evidence proves a masked Python-suite failure and an over-strong raw physical-target gate despite 18/18 green conclusions. Planning executes none of the later commands.*

Der spaetere Follow-up-Vertrag ist bewusst klein: / *The later follow-up contract is intentionally small:*

1. In `.github/workflows/powershell-analysis.yml` muss jeder serielle Feature-002-Prozess seinen Exitcode unmittelbar nach dem Command erfassen und pruefen: zuerst Python, dann Bash, dann PowerShell. Kein spaeterer Command darf einen frueheren Fehler maskieren.
2. Im Feature-002-Python-Core entfaellt ausschliesslich der Vergleich des physischen META-LH-02-Ziel-Git-Blobs mit `originalRawSha256`. Feldform, lowercase Digest, `acceptedArtifacts`-Bindung, Original-/Archiv-Exklusivitaet und normalisierter Zielhash bleiben bindend; rohe Receipt-/Review-Pruefungen bleiben bytegenau.
3. Der vorhandene fokussierte Test muss auf der vollstaendigen Validatoroberflaeche unmittelbare Exitpropagation, LF-/CRLF-Aequivalenz, substantive Ziel-Driftablehnung und unveraenderte Receipt-/Review-Rohhashfehler beweisen. PowerShell-Help, Man-Page, Quickstart und vorhandene Evidence werden nur fuer diese Semantik angepasst.
4. Genau ein normaler Follow-up-Commit auf `7eb7470` ist erlaubt. Kein Amend, Force-Push oder History-Rewrite. Nur wenn der unveraenderte Methodik-v2-Renderer danach tatsaechlichen Drift meldet, darf hoechstens ein weiterer Commit ausschliesslich `docs/project-statistics.md` synchronisieren.
5. PR #29 wird erst an den neuen unveraenderlichen finalen Head gebunden. Alle 18 Checks, exakte Ubuntu-/macOS-/`windows-2022`-Evidence und aktuelle Review-Konvergenz laufen neu. Auf jeder Plattform muessen Python, Bash und PowerShell selbst erfolgreich enden; eine gruene Job-Schlussfolgerung allein genuegt nicht.

Nach Gruenkonvergenz werden nur die bereits akzeptierten T080 bis T093 fortgesetzt. Der Lauf endet nach META-LH-02 mit ausdruecklicher No-next-run-Disposition; META-LH-03 und jeder andere Spec-Kit-Lauf bleiben ungestartet. / *After green convergence, only the accepted closeout continues and the run stops without starting another feature.*

## 1. Gate-Requirements vor Implementierung pruefen / Check gate requirements before implementation

Die installierte Requirements-Vorlage und der installierte Core verwenden Schema `1.0`; Schema `2.0` ist die getrennte Evidence-Vorlage. Vor dem ersten Domain-Edit: / *The installed requirements template/core use schema `1.0`; schema `2.0` is the separate evidence template. Before the first domain edit:*

```bash
python3 -m json.tool \
  specs/002-portfolio-ownership/autonomous-run-gate-requirements.json >/dev/null
PYTHONDONTWRITEBYTECODE=1 python3 -c 'import importlib.util,pathlib; p=pathlib.Path(".specify/presets/autonomous-run-governance/scripts/autonomous-evidence-core.py"); s=importlib.util.spec_from_file_location("aoc_evidence_core", p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); gates,digest=m.validate_requirements(pathlib.Path("specs/002-portfolio-ownership/autonomous-run-gate-requirements.json")); print(f"PASS: {len(gates)} gate requirements, normalized SHA-256 {digest}")'
```

Danach prueft eine unabhaengige Plan-Review-Rolle jede Gate-ID, Anwendbarkeit, Command-/Runner-Token, Owner-/Reviewer-Rolle, den exakten Evidence-Pfad und jeden `N/A`-Trigger. Ohne reviewte [Delivery-Allowlist](contracts/delivery-allowlist.json) und diese Evidence kein Implement. / *An independent plan reviewer then checks every listed field. Implementation remains blocked without that review and the reviewed allowlist.*

## 2. Aktuelle Eingaben vor dem Domain-Delta / Current inputs before the domain delta

```bash
bash .specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh --result specs/intake-review-results/meta-lh-02-portfolio-ownership-2026-08-29-r6.json --repo .
pwsh -NoProfile -File .specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1 -Result specs/intake-review-results/meta-lh-02-portfolio-ownership-2026-08-29-r6.json -Repo .
bash .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh --receipt specs/intake-authoring-receipts/META-LH-02-Portfolio-Ownership.json --repo .
pwsh -NoProfile -File .specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1 -Receipt specs/intake-authoring-receipts/META-LH-02-Portfolio-Ownership.json -Repo .
PYTHONDONTWRITEBYTECODE=1 python3 -B specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py --repo . global-ready
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh --state specs/002-portfolio-ownership/autonomous-run-state.json
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.ps1 -State specs/002-portfolio-ownership/autonomous-run-state.json
```

Diese Gruppe war bis unmittelbar vor dem ersten C-05-Edit bindend und ist als bestandene historische Eingangsevidence erhalten. Nach dem beabsichtigten C-05-bis-C-09-Delta werden die beiden generischen Receipt-Validatoren und der generische `global-ready`-Befehl nicht erneut als Pass verlangt, weil der unveraenderliche Receipt absichtlich den Vor-Implementierungs-Source-Hash bindet. / *This group was binding through the last pre-edit boundary. After the intended delta, generic receipt freshness and generic global-ready are historical entry evidence, not current pass requirements.*

### 2a. Feature-lokaler Vertrag nach dem Delta / Feature-local contract after the delta

Nach Umsetzung in T052/T053 pruefen genau diese Commands die Hilfe, den post-GlobalReady-Zustand ueber beide gleichwertigen Oberflaechen und die isolierten Positiv-/Negativfaelle: / *After T052/T053 implementation, these commands validate help, the qualified state through both equivalent surfaces, and isolated positive/negative cases:*

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  specs/002-portfolio-ownership/contracts/test_validate_meta_lh02_snapshot.py
bash specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.sh --help
bash specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.sh \
  --repo . post-global-ready
pwsh -NoProfile -File \
  specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1 \
  -Help
pwsh -NoProfile -File \
  specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1 \
  -Repo . -Mode post-global-ready
pwsh -NoProfile -Command \
  '. specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1; Get-Help Test-AocMetaLh02Snapshot -Full'
```

Der Core liest Run, Branch, Status und Stage aus `autonomous-run-state.json`; ein CLI-Argument darf diese Qualifikation nicht ueberschreiben. Er verlangt die exakte Schema-`1.1`-Lifecycle-/Snapshot-Form, Original-/Archiv-Exklusivitaet, historische `originalRawSha256`-Feld-/lowercase-/Evidence-Bindung, den exakten normalisierten physischen Zielhash, unveraenderte Receipt-/Review-Rohbytes, `status=Active`, eindeutige aktuelle `Single`/`Primary`/`Ready`-Leaves ohne Blocker und den Erfolg jeder Bash-/PowerShell-Review-Oberflaeche. Der historische Ziel-Rohhash wird nicht gegen aktuelle physische Worktree- oder Git-Standardausgabebytes geprueft. Der Vertrag ist nur in `Plan`, `Implement`, `Validate`, `Publish`, `Review`, `MergeAndSync` oder `Retrospective` gueltig; `Plan` deckt nur den runner-owned post-Delta Analyze-Retry ab. / *The core preserves the historical raw field as shaped evidence, accepts the physical target through normalized identity, and keeps receipt/review raw bytes immutable.*

Die sechs getrackten Negativ-Fixtures pruefen falschen Run, Branch und weiterhin unzulaessige Stage `Specify`, Receipt-/Review-Byte-Drift und doppelten Review-Leaf. Der fokussierte Test belegt zusaetzlich den exakt gebundenen positiven `Plan`-Retry, falsche Lifecycle-Form, beide/keinen Original-/Archivpfad, normalisierte LF-/CRLF-Aequivalenz, substantive Ziel-Driftablehnung, die unveraenderten Receipt-/Review-Rohbytefehler, inaktiven State und den getrennten Ausfall jeder installierten Review-Oberflaeche. Er bindet ausserdem die unmittelbare Exitcode-Pruefung der Python-Suite vor Bash sowie die unmittelbaren Bash-/PowerShell-Postconditions im Workflow. Vorher-/Nachher-Status beweist null Repository-Write. [snapshot-tooling-parity.md](checklists/snapshot-tooling-parity.md) bindet gleiche Ausgabe/Exitcodes, Strictness, bilinguale Hilfe, Cmdlet, Man-Page, Same-commit und spaetere exakte Dreiplattform-Commands. / *The focused suite proves normalized target semantics, unchanged raw receipt/review failures, no-write behaviour, and immediate fail-closed serial command propagation.*

## 3. `C-05` als Red/Green-Slice / `C-05` as the red/green slice

Vor dem Edit wird die aktuelle Zeile in `checklists/implementation-validation.md` als roter Ausgangszustand erfasst: Sie nennt `IAD604` und `DEC-T06`, trennt aber deren Status nicht. Dann wird nur die Decision-Zelle `C-05` geaendert. / *Before editing, capture the current row as red because it names both IDs without separating their status. Then change only the `C-05` decision cell.*

```bash
rg -n '^\| C-05 \|' requirements/baseline/portfolio-ownership.md
rg -n '^\| C-05 \|.*Answered.*IAD604.*Open.*DEC-T06' requirements/baseline/portfolio-ownership.md
git diff -- requirements/baseline/portfolio-ownership.md
```

Der zweite Befehl muss vor dem Edit fehlschlagen und danach genau die gruen korrigierte Zeile finden. Der Diff darf zu diesem Zeitpunkt keine Zeile `C-06` bis `C-09` aendern. / *The second command must fail before the edit and find the corrected row afterwards. At this point the diff must not change rows `C-06` through `C-09`.*

## 4. Rollout `C-06` bis `C-09` / Roll out `C-06` through `C-09`

Erst nach gruenem `C-05` werden die vier restlichen Decision-Zellen an [data-model.md](data-model.md) angeglichen. / *Only after green `C-05`, reconcile the remaining decision cells with the data model.*

```bash
rg -n '^\| C-0[6-9] \|' requirements/baseline/portfolio-ownership.md
rg -n '^\| C-06 \|.*Answered.*IAD601.*IAD602.*IAD603.*IAD604' requirements/baseline/portfolio-ownership.md
rg -n '^\| C-07 \|.*Answered.*IAD701.*IAD702.*IAD703.*IAD704' requirements/baseline/portfolio-ownership.md
rg -n '^\| C-08 \|.*Answered.*IAD801.*IAD802.*IAD803.*Superseded.*DEC-T05' requirements/baseline/portfolio-ownership.md
rg -n '^\| C-09 \|.*Answered.*IAD901.*IAD902.*AUTH-RAW09-PROMOTION' requirements/baseline/portfolio-ownership.md
git diff -- requirements/baseline/portfolio-ownership.md
```

Wenn Decision Map, Maschinenvertrag oder Validatoren waehrenddessen einen neuen Widerspruch zeigen, stoppt der Lauf vor weiteren Edits und geht in fail-closed Re-Planung. / *Any newly proven contradiction stops further edits and triggers fail-closed replanning.*

## 5. Sechs Portfolio-Laeufe / Six portfolio runs

```bash
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --contract requirements/baseline/portfolio-ownership.json --markdown requirements/baseline/portfolio-ownership.md
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Contract requirements/baseline/portfolio-ownership.json -Markdown requirements/baseline/portfolio-ownership.md
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
```

Erwartet werden zwei positive `PASS`-Zeilen und pro Shell je `PO002` sowie `PO007`, alle mit Exitcode `0`. / *Expect two positive passes plus `PO002` and `PO007` per shell, all exiting zero.*

## 6. Reviews, Documentation Impact und Security / Reviews, Documentation Impact, and security

Erzeuge und pruefe seriell: / *Create and review serially:*

1. `specs/002-portfolio-ownership/first-reader-review-evidence.md` mit `6/6` und null Blockern;
2. `specs/002-portfolio-ownership/accessibility-review-evidence.md` mit null blockierenden DE/EN-, B2-, A11Y- oder Text-first-Befunden;
3. `specs/002-portfolio-ownership/security-privacy-review-evidence.md` gegen die spaeter eingefrorene exakte Kandidatenmenge;
4. `specs/002-portfolio-ownership/documentation-impact-evidence.md` mit genau einer `UpdateRequired`-Entscheidung.

Maschinelle Secret-Musterchecks: / *Machine secret-pattern checks:*

```bash
gitleaks dir --redact --no-banner --no-color requirements/baseline
gitleaks dir --redact --no-banner --no-color specs/002-portfolio-ownership
bash scripts/scan-agent-secrets.sh --fail-on-high .
pwsh -NoProfile -File scripts/scan-agent-secrets.ps1 -FailOnHigh -WorkspaceRoot .
```

Diese Befehle beweisen keine semantische Publikationseignung und ersetzen nicht das unabhaengige Review. / *These commands do not prove semantic publication suitability and do not replace independent review.*

## 7. AEPS und Statistik als Shared Writer / AEPS and statistics as shared writers

T055 bis T058 bleiben als abgeschlossene historische Projektions-Evidence erhalten. Der spaetere reale provisorische 35-Pfad-Kandidat `7b99227045deb8cc34e0062db09eb4f6dd134501` machte beide realen Peers erwartbar erneut `DRIFT`/`1`: Das committed Ledger bindet Quelle `3e1d9d5ccd98`, die reale Methodik-v2-Quelle ist `7b99227045de` mit 222411 getrackten Textzeilen. Das ist kein Rendererfehler und darf nicht als `CURRENT` umgedeutet werden. / *T055-T058 remain truthful historical projection evidence. The later provisional 35-path real commit necessarily made both real peers report DRIFT because the committed ledger binds the disposable source rather than the real methodology-v2 source.*

`7b992270`, sein reviewtes Amend, `a78a785`, die T079-Heads `8f395f8`/`0b0808c` und die R-022-Heads `68a1af2`/`7eb7470` bleiben ausschliesslich historische Evidence und erteilen keine Wiederverwendungsautoritaet. Der finale Follow-up-Commit baut normal auf `7eb7470` auf. Die 72 abgeschlossenen Marker bleiben unveraendert. / *All published predecessors remain immutable history; the final normal follow-up builds on `7eb7470` without changing the 72 durable markers.*

Nach dem neuen normalen Follow-up-Commit laeuft der unveraenderte Renderer auf genau diesem sauberen Head oder einer bytegenauen sauberen Projektion. Erst dort sind die folgenden drei Befehle zulaessig: / *After the normal follow-up commit, run the unchanged renderer only on that exact clean head or a byte-identical clean projection:*

```bash
bash scripts/render-project-statistics.sh --repo "$projection_worktree"
bash scripts/render-project-statistics.sh --repo "$projection_worktree" --check-only
pwsh -NoProfile -File scripts/render-project-statistics.ps1 -Repo "$projection_worktree" -CheckOnly
```

Nur die erzeugten `docs/project-statistics.md`-Bytes duerfen in den realen Branch uebernommen werden. Meldet der unveraenderte Renderer danach weiterhin Drift, darf hoechstens ein neuer lokaler `statistics-head-sync`-Commit entstehen, der nur diesen Pfad und den vorgeschriebenen Trailer enthaelt; ohne Ledger-Delta entsteht kein solcher Commit. Methodik v2 muss weiterhin Git-getrackten Text und Nicht-Merge-Bruttoaenderungen verwenden und Ledger, `STATS.md` sowie Binaerdaten ausschliessen. Beide realen Check-only-Peers muessen auf dem daraus resultierenden neuen finalen Head `CURRENT`/`0` melden. / *Copy back only the ledger and create at most one new ledger-only synchronization commit only if drift remains; both real peers must be CURRENT on the resulting new final head.*

Der normale Follow-up-Head bleibt final, wenn der Renderer keinen Drift meldet. Meldet er Drift, wird ausschliesslich der daraus kausal erzeugte Ledger-only-Head als `/tmp/002-portfolio-ownership-feature-head.txt` und im PR-Body gebunden. Danach werden alle betroffenen Pfad-, Diff-, State-, Review-, Snapshot-, Documentation-, Secret/Security-, Authority-, Stage- und Exact-head-Gates wiederholt. / *Use the normal follow-up head unless the unchanged renderer proves a ledger-only synchronization is required; bind and revalidate only the resulting immutable final head.*

## 8. Exakte Liefermenge read-only pruefen / Validate the exact delivery set read-only

Nach allen Artefakten und Reviews wird die passende Transaktion aus `contracts/delivery-allowlist.json` in eine temporaere exakte Liste aufgeloest. Jede Bedingung wird einzeln begruendet; nicht ausgeloeste optionale Pfade fehlen in der Liste. / *After all artefacts and reviews, resolve the matching allowlist transaction to a temporary exact list. Each condition is justified; non-triggered paths are absent.*

```bash
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.sh --repo . --intended specs/002-portfolio-ownership/plan.md
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-delivery-set.ps1 -Repo . -Intended specs/002-portfolio-ownership/plan.md
git status --porcelain=v1 --untracked-files=all
```

Die gezeigten `--intended`-Argumente sind nur ein Syntaxbeispiel. Der echte Aufruf nennt jeden tatsaechlich untracked Lieferpfad aus der reviewten eingefrorenen Liste einzeln. Fremde untracked Pfade bleiben sichtbar und unberuehrt. / *The shown intended argument demonstrates syntax only. The real call names every actual untracked delivery path individually. Unrelated paths remain visible and untouched.*

## 9. Stage-Pruefung erst nach spaeterer Authority / Stage check only after later authority

Kein Befehl dieses Abschnitts ist durch die Planungsphase autorisiert. Nach Tasks, Analyze, Implement, allen Gates und frischer Authority werden nur die einzeln eingefrorenen Pfade gestaged. Danach: / *Planning authorises none of these commands. Only after downstream gates and fresh authority, stage individually frozen paths and then run:*

```bash
git status --porcelain=v1 --untracked-files=all
git diff --cached --name-only
git diff --cached --check
```

Fuer `windows-target-exit-followup` muessen die staged Namen exakt der neu eingefrorenen Follow-up-Liste entsprechen; implementierende Bytes duerfen nur in `.github/workflows/powershell-analysis.yml` und `specs/002-portfolio-ownership/contracts/validate_meta_lh02_snapshot.py` liegen. Hinzu kommen ausschliesslich vorhandene direkt betroffene Test-/Help-/Man-/Quickstart-/Planungs-/Gate-/Evidence-Pfade. Fuer einen durch tatsaechlichen Rendererdrift erforderlichen `statistics-head-sync` darf Stage und Commit ausschliesslich `docs/project-statistics.md` enthalten. Unstaged Kandidatenreste, fremde Stage-Pfade oder Pfaddrift stoppen. / *The follow-up uses its exact bounded two-defect list and retains a strictly one-path ledger-only synchronization only on actual drift.*

## 10. Normalen Feature-Head reviewen und mergen / Review and merge the normal feature head

Fuer den exakten spaeter reviewten finalen Statistik-PR-Head: / *For the exact later reviewed final statistics PR head:*

```bash
gh pr view --json number,headRefOid,reviewDecision,url
gh pr checks --watch --fail-fast --json bucket,name,state,link
gh pr checks --required --json bucket,name,state,link
gh api graphql -f query='query($owner:String!,$name:String!,$number:Int!){repository(owner:$owner,name:$name){pullRequest(number:$number){reviewThreads(first:100){nodes{isResolved isOutdated}}}}}' -F owner=OWNER -F name=REPO -F number=PR
```

Workflow-Definitionen und `gh run view`-Logs muessen Command-/Runner-Token fuer denselben finalen Head belegen. Insbesondere muss `.github/workflows/powershell-analysis.yml` auf Linux, macOS und `windows-2022` Python-Suite, Bash-Peer und PowerShell-Peer fuer den exakt reviewten Head ausfuehren und jeden Exit unmittelbar erfolgreich pruefen. T077/T080/T084 erfassen Workflow, Job, Runner, Head-SHA, Log-URL, jeden Command und seinen Exit; eine gruene Job-Schlussfolgerung ohne diese Einzelbelege ist unzureichend. Fehlende oder rote Windows-Command-Evidence stoppt fail-closed und darf nicht durch Admin-Bypass ersetzt werden. Fuer diesen Feature-Head wird nur ein vorlaeufiger Execution Record erzeugt: `PO-G32` ist noch nicht ausgefuehrt, deshalb waere ein vollstaendig erfolgreicher Schema-`2.0`-`PreMerge`-Snapshot hier erfundene Zukunftsevidence. / *Workflow definitions and logs must prove every serial command on all three platforms; green job conclusions alone are insufficient.*

Ein Bypass bleibt verboten, bis exakt ein konkretes Approval-/Ruleset-Gate letzter Blocker ist und alle Bedingungen aus `PO-N01` nach neuer Review zutreffen. Der unveraenderte finale Statistik-Feature-Head wird zuerst gemergt und `main` per Fast-forward synchronisiert. Fuer diesen Head wird noch kein terminales PostMerge behauptet, weil der von der Constitution verlangte Rename als getrennte Transaktion folgt. / *Bypass remains forbidden until its exact trigger is met. Merge and synchronize the immutable final statistics feature head first; terminal PostMerge does not yet apply because the required rename follows separately.*

## 11. Lifecycle binden und Lastenheft terminal umbenennen / Bind lifecycle and perform the terminal intake rename

`specs/002-portfolio-ownership/intake-lifecycle.json` muss bereits mit Record und `programmeEvidenceSnapshot` Bestandteil des gemergten normalen Kandidaten sein. Vor dem Rename werden der Feature-002-Snapshot-Vertrag, beide Review-Oberflaechen, Series-Bindung, Original-vorhanden/Archiv-fehlt, ein sauberer Worktree und aktuelle Authority geprueft. Danach wird von synchronisiertem `main` ein dedizierter Rename-Branch erzeugt. / *The merged normal candidate must contain both lifecycle record and programme snapshot. Validate the local snapshot contract, both review peers, series, path exclusivity, worktree, and authority before creating the rename branch.*

Als letzte Aufgabe der Polish-Phase genau eine der folgenden Alternativen ausfuehren: / *As the final Polish task, run exactly one alternative:*

```bash
bash scripts/rename-lastenheft.sh \
  requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md \
  002-portfolio-ownership

# Windows-Alternative, nicht zusaetzlich ausfuehren / Windows alternative; do not run in addition
pwsh -NoProfile -File scripts/rename-lastenheft.ps1 \
  -File requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md \
  -BranchName 002-portfolio-ownership
```

Der Skript-Commit muss ausschliesslich diesen byteidentischen Pfadwechsel enthalten: / *The script commit must contain only this byte-identical path transition:*

```bash
git diff-tree --summary -M100% HEAD^ HEAD
git diff-tree --no-commit-id --name-status -r -M100% HEAD
git diff --cached --name-only
```

Erwartet wird exakt `R100` von `Lastenheft_META-LH-02-Portfolio-Ownership.md` nach `Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md`, null Stage-Rest und der vorgeschriebene Co-Author-Trailer. Danach laufen beide Feature-002-Snapshot-Oberflaechen, beide installierten Review-Validatoren und der Series-Validator. Generische Receipt-Source-Freshness und der generische `global-ready`-Befehl werden nach dem beabsichtigten Delta nicht verlangt. Receipt, Review, Series, Lifecycle, Tasks, State und Evidence bleiben im Rename-Commit unveraendert. / *Require the exact R100 plus both feature-local snapshot peers, both installed review peers, and series validation; do not require impossible generic post-delta freshness.*

```bash
bash .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.sh \
  --file specs/intake-series/aoc-phase-2/manifest.json --repo .
pwsh -NoProfile -File .specify/presets/intake-sequencing-governance/scripts/validate-intake-series-manifest.ps1 \
  -File specs/intake-series/aoc-phase-2/manifest.json -Repo .
bash specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.sh \
  --repo . post-global-ready
pwsh -NoProfile -File \
  specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1 \
  -Repo . -Mode post-global-ready
```

## 12. Rename-Head reviewen, mergen und kausal abschliessen / Review, merge, and causally close the rename head

Der Rename-Head besitzt eigene temporaere Schema-`2.0`-`PreMerge`-Evidence, einen eigenen unveraenderten `headRefOid`, alle gemeldeten Checks, eine nichtleere Required-Teilmenge, unabhaengige Review und null handlungsrelevante Threads. T090 verlangt fuer diesen Head erneut die Linux-/macOS-/Windows-Matrixevidence mit Workflow-, Job-, Runner-, Log- und Command-Bindung; insbesondere bleibt reale Windows-Ausfuehrung fuer genau diesen Head zwingend. Erst nach Merge und erneutem Fast-forward-Sync entsteht ein `PostMerge`-Snapshot, der den akzeptierten Rename-PreMerge-Hash, denselben reviewten Rename-Head, den tatsaechlichen Rename-Merge-Commit und leere `changedPaths` bindet. / *The rename head receives its own exact-head Linux/macOS/Windows matrix proof, including mandatory real Windows execution, before causal merge evidence.*

```bash
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/002-portfolio-ownership/autonomous-run-gate-requirements.json \
  --evidence /tmp/002-portfolio-ownership-rename-premerge.json --head RENAME_REVIEWED_HEAD
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.ps1 \
  -Requirements specs/002-portfolio-ownership/autonomous-run-gate-requirements.json \
  -Evidence /tmp/002-portfolio-ownership-rename-premerge.json -Head RENAME_REVIEWED_HEAD

# Erst nach Rename-Merge und Fast-forward-Sync / Only after rename merge and sync
bash .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.sh \
  --requirements specs/002-portfolio-ownership/autonomous-run-gate-requirements.json \
  --evidence /tmp/002-portfolio-ownership-postmerge.json --head RENAME_REVIEWED_HEAD
pwsh -NoProfile -File .specify/presets/autonomous-run-governance/scripts/validate-autonomous-gate-evidence.ps1 \
  -Requirements specs/002-portfolio-ownership/autonomous-run-gate-requirements.json \
  -Evidence /tmp/002-portfolio-ownership-postmerge.json -Head RENAME_REVIEWED_HEAD
```

Nach der materiellen Retrospektive T092 wird vor terminaler Completion unter `docs/aeps/README.md` abschliessend Finding oder begruendet NoChange als getrennte Allowlist-Transaktion `final-aeps-reassessment` neu bewertet und durch die bestehende unabhaengige AEPS-Rolle validiert. Der Receipt-Pfad ist verpflichtend; nur bei echtem Finding duerfen die vier bestehenden konditionalen AEPS-Pfade atomar folgen, bei NoChange bleiben sie bytegleich. Ein echter Delta wird vor dem kausalen Closeout stabil geliefert und `main` synchronisiert, ohne die exakte Drei-Pfad-Transaktion zu verbreitern. Daraus folgen weder Level-0-Handoff, Preset-Promotion, Upstream-Posting noch neue Authority. / *After the material retrospective and before terminal completion, complete the separate independently validated repository-contract AEPS transaction without broadening causal closeout or granting upstream authority.*

Wenn keine repository-lokale Persistenz notwendig ist, gibt es keine leere Closeout-PR. Andernfalls gilt nur die exakte Drei-Pfad-Transaktion `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json` aus der Allowlist. Sie darf vergangene Rename-/PostMerge-/Retrospektiv-/AEPS-Fakten binden, aber weder ihren eigenen zukuenftigen PR-Head noch ihren eigenen Merge behaupten. Nach Finalvalidierung enden beide Pfade mit derselben ausdruecklichen Disposition: Run `aa60069e-ded5-463f-a737-9b5aa96070c7` stoppt nach META-LH-02-Completion; META-LH-03 und jeder andere Spec-Kit-Lauf werden nicht gestartet und benoetigen einen neuen ausdruecklichen Auftrag. / *No eligible local delta means no empty closeout PR. Both the exact three-path and no-persistence paths end with the explicit stop after META-LH-02 and no next Spec Kit run.*
