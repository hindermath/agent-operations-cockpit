# Planungs- und Validierungsvertrag / Planning and Validation Contract

## Vertragszweck / Contract purpose

Dieser Vertrag verbindet die geklaerte Spezifikation mit der spaeteren Task- und Implementierungsphase. Er fuehrt keine fachliche Aenderung aus und erteilt keine Git-, Remote-, Merge- oder Bypass-Authority. Maschinenpruefbare Gate-Anforderungen stehen in [autonomous-run-gate-requirements.json](../autonomous-run-gate-requirements.json); Transaktionspfade stehen in [delivery-allowlist.json](delivery-allowlist.json). / *This contract connects the clarified specification to later tasks and implementation. It performs no domain change and grants no delivery authority. Machine-checkable gates and transaction paths are linked above.*

## Gebundener fachlicher Delta / Bound domain delta

1. Aendere zuerst ausschliesslich die Decision-Zelle `C-05` in `requirements/baseline/portfolio-ownership.md`. / First change only the `C-05` decision cell.
2. Binde den roten Ausgangszustand und den gruenen Zustand mit getrenntem `Answered: IAD604` und `Open: DEC-T06`. / Bind red baseline and green state with separately named statuses.
3. Rolle erst danach dieselbe Statusregel auf `C-06` bis `C-09` aus. / Only then roll the rule out to `C-06` through `C-09`.
4. Bewahre alle anderen Spalten, Zeilen, Owner, Handoffs, Textalternativen und Commands bytegenau, soweit der fokussierte Markdown-Edit dies erlaubt. / Preserve all other rows, columns, owners, handoffs, text alternatives, and commands.
5. Aendere JSON-Vertrag, Decision Map oder Validatoren nur nach einem neuen reproduzierbaren Driftbefund und fail-closed Re-Planung. / Change validation-only files only after new reproducible drift and fail-closed replanning.

## Sechs verbindliche Portfolio-Checks / Six binding portfolio checks

```text
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --contract requirements/baseline/portfolio-ownership.json --markdown requirements/baseline/portfolio-ownership.md
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
bash specs/intake-review-fixtures/meta-lh-02/validate-portfolio.sh --fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Contract requirements/baseline/portfolio-ownership.json -Markdown requirements/baseline/portfolio-ownership.md
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/duplicate-owner.json
pwsh -NoProfile -File specs/intake-review-fixtures/meta-lh-02/validate-portfolio.ps1 -Fixture specs/intake-review-fixtures/meta-lh-02/cycle.json
```

Alle sechs Befehle muessen mit Exitcode `0` enden. Die positiven Laeufe melden exakt `9 series, 9 concerns, 10 handoffs, acyclic`; die Fixture-Laeufe bestaetigen `PO002` beziehungsweise `PO007`. / *All six commands must exit zero with the exact expected positive counts or fixture error codes.*

## Zeitlich geteilte Eingangsgates / Temporally split input gates

Bis unmittelbar vor dem ersten C-05-Edit waren beide Review-, beide Authoring-Receipt-, der generische `global-ready`- und beide Run-State-Validatoren bindend. Ihre bestandenen Ausgaben bleiben historische Eingangsevidence. Nach dem beabsichtigten C-05-bis-C-09-Delta darf weder generische Receipt-Source-Freshness noch der generische `global-ready`-Befehl als aktueller Pass verlangt werden. / *Both review, both receipt, generic global-ready, and both state surfaces were binding through the last pre-edit boundary and remain historical entry evidence. Generic source freshness and generic global-ready are not current pass requirements after the intended delta.*

Fuer die post-GlobalReady-Stages implementiert Feature 002 in T052/T053 ausschliesslich `contracts/validate_meta_lh02_snapshot.py` als Standardbibliotheks-Core, die Peers `contracts/validate-meta-lh02-snapshot.sh` und `contracts/validate-meta-lh02-snapshot.ps1`, `docs/man/validate-meta-lh02-snapshot.1`, `checklists/snapshot-tooling-parity.md`, `contracts/test_validate_meta_lh02_snapshot.py` und die sechs bereits benannten isolierten Fixtures. Der aktuelle Pflichtlauf ist nach deren Implementierung: / *For post-GlobalReady stages, T052/T053 implement only the local standard-library core, constitution-compliant paired surfaces, Unix manual, parity checklist, tests, and six named fixtures:*

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B specs/002-portfolio-ownership/contracts/test_validate_meta_lh02_snapshot.py
bash specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.sh --repo . post-global-ready
pwsh -NoProfile -File specs/002-portfolio-ownership/contracts/validate-meta-lh02-snapshot.ps1 -Repo . -Mode post-global-ready
```

Der Core qualifiziert nur Run `aa60069e-ded5-463f-a737-9b5aa96070c7`, Branch `002-portfolio-ownership`, den exakten Feature-002-Lifecycle, `status=Active` und die State-Stages `Plan`, `Implement`, `Validate`, `Publish`, `Review`, `MergeAndSync` oder `Retrospective`. `Plan` gilt nur fuer den runner-owned post-Delta Analyze-Retry dieses aktiven Vertrags und ist keine allgemeine Stage-Ausnahme. Der Core leitet Status/Stage aus dem State ab und verifiziert exakte Lifecycle-/Snapshot-Form, Original-/Archiv-Exklusivitaet, lowercase `originalRawSha256` samt historischer `acceptedArtifacts`-Bindung, den normalisierten physischen META-LH-02-Zielhash, alle 14 Snapshot-Zielnormalhashes, unveraenderte rohe Receipt-/Review-Bytes, eindeutige aktuelle `Single`/`Primary`/`Ready`-Leaves ohne Blocker und jede installierte Review-Oberflaeche. `originalRawSha256` bleibt Evidence, wird aber nicht gegen aktuelle physische Worktree- oder Git-Standardausgabebytes des META-LH-02-Ziels verglichen. Jede substantive Ziel-, Receipt-/Review-Rohbyte-, Leaf-, Series-, Lifecycle-, Branch-, Run-State- oder Authority-Drift und jeder Review-Peer-Ausfall stoppt die Folgephase. / *Qualification preserves the historical raw target field as evidence while current physical target identity is normalized; exact raw immutability remains for receipt and review.*

Der Bash-Peer verwendet `set -euo pipefail`, gequotete Variablen und `--`-Disziplin; `-h`/`--help` verweist auf die Man-Page oder gleichwertige interne Hilfe. Der PowerShell-Peer verwendet `#Requires -Version 7`, `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, validierte Parameter und vollstaendige bilinguale Comment Help und exportiert das genehmigte Advanced Function/Cmdlet `Test-AocMetaLh02Snapshot`; Evidence laeuft mit `pwsh -NoProfile`. Ausgabe und Exitcodes beider Peers muessen gleichwertig sein. Der Validator ist immer read-only, deshalb gibt es keinen getrennten mutierenden Dry-run. Die T053-Paritaetscheckliste dokumentiert die manuelle Ausfuehrung beider Varianten auf dem verfuegbaren macOS-Host, Help, Get-Help, Cmdlet, Man-Page, Strictness, Negativ-Fixtures, null Write, vollstaendige lokale Testsuite und Same-commit-Lieferung. Das ist keine Windows-Evidence. Reale Windows-Ausfuehrung bleibt bis zum exakten reviewten Head offen. / *T053 manually verifies both variants on macOS without claiming Windows; real Windows execution remains pending for the exact reviewed head.*

Die sechs getrackten Fixtures decken falschen Run, Branch und Stage, Receipt-/Review-Byte-Drift sowie doppelten Review-Leaf ab. `test_validate_meta_lh02_snapshot.py` erzeugt weitere Faelle fuer falsche Lifecycle-Form, beide/keinen Original-/Archivpfad, akzeptierte Zielhash-Drift, inaktiven State und den Ausfall jeder installierten Review-Oberflaeche als temporaere Projektionen; vor/nach jedem Lauf wird null Repository-Write belegt. Security-Evidence prueft NIST SSDF, CWE Top 25, sichere Python-Grenzvalidierung ohne unsafe Deserialisierung, Shell oder dynamische Ausfuehrung, eingeschraenkte Pfade, dependency-freie Standardbibliothek, Public-/Secret-Grenzen und die Bash-/PowerShell-Disziplin. T052/T053 bleiben bis zur spaeteren Implementierungsphase unausgefuehrt. / *Tracked fixtures plus temporary projections cover every negative, prove no-write behaviour, and bind the complete SSDF/CWE/secure-code/public-content contract. Planning does not claim T052/T053 execution.*

## Archivbewusster Lifecycle-Vertrag / Archive-aware lifecycle contract

Der normale Feature-Kandidat enthaelt vor Freeze und Review genau `specs/002-portfolio-ownership/intake-lifecycle.json` mit Schema `1.1`, einem Record fuer `META-LH-02` und einem `programmeEvidenceSnapshot`. Der Record bindet Original-/Archivpfad, akzeptierten Intake-Normalhash, unveraenderte Receipt-/Review-Rohhashes, Run und Branch. Der Snapshot friert exakt 14 Ziele in kanonischer Reihenfolge mit den akzeptierten Vor-Implementierungs-Zielnormalhashes und den unveraenderlichen Receipt-/eindeutigen Ready-Single-Review-Rohhashes ein. Er enthaelt keine Git- oder Provider-Zukunftsfakten. Vor dem Rename muss genau der Originalpfad existieren, danach genau der Archivpfad; beide oder keiner blockieren. / *The schema-`1.1` lifecycle contains one META-LH-02 record and one immutable fourteen-target pre-implementation programme snapshot with no future facts.*

Erst nach Merge und Fast-forward-Sync des normalen Feature-PR wird von `main` ein dedizierter Rename-Branch erzeugt. Als letzte Aufgabe der Polish-Phase fuehrt der Operator genau eine der vorhandenen Oberflaechen aus: / *Only after normal delivery is merged and synchronized does the final Polish task run one existing script surface on a dedicated branch:*

```text
bash scripts/rename-lastenheft.sh requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md 002-portfolio-ownership
pwsh -NoProfile -File scripts/rename-lastenheft.ps1 -File requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md -BranchName 002-portfolio-ownership
```

Die Befehle sind Alternativen, nicht zwei aufeinanderfolgende Ausfuehrungen. Der Skript-Commit muss exakt ein byteidentisches `R100` vom Original- zum Archivpfad mit vorgeschriebenem Trailer enthalten. `intake-lifecycle.json`, Intake-Inhalt, Authoring Receipt, Ready Single Review, Series-Manifest/-Order, Domain, Tasks, Run-State und Evidence duerfen in diesem Commit nicht geaendert werden. Danach muessen der Feature-002-Snapshot-Vertrag, beide Review-Oberflaechen und der Series-Validator den Archivpfad read-only aufloesen; generische Receipt-Source-Freshness und generisches `global-ready` sind keine post-Delta-Erfolgsanforderung. / *After the exact rename, the local snapshot contract, both review peers, and series validator resolve the archive; generic post-delta freshness is not required.*

## Review-Evidence / Review evidence

| Evidence | Exakter Pfad / Exact path | Mindestabschluss / Minimum completion |
|---|---|---|
| Implementierungsprotokoll / implementation record | `specs/002-portfolio-ownership/checklists/implementation-validation.md` | Alle Applicable Gates mit echter Evidence; N/A mit Begruendung und Trigger. / Every applicable gate with real evidence; every N/A justified. |
| Script-Paritaet / script parity | `specs/002-portfolio-ownership/checklists/snapshot-tooling-parity.md` | Bash-/PowerShell-Ausgabe und Exitcodes gleichwertig; Help, Man-Page, Cmdlet, strikte Regeln, Negativ-Fixtures, vollstaendige lokale Testsuite, null Write, manuelle Ausfuehrung beider Varianten auf macOS und Same-commit belegt; keine Windows-Behauptung. / Equivalent peers manually verified on macOS without a Windows claim. |
| Exakter Plattform-Head / exact-head platform proof | `.github/workflows/powershell-analysis.yml` und temporaerer Execution Record / and temporary execution record | Linux-, macOS- und zwingend Windows-Job fuer denselben reviewten Head; Workflow, Job, Runner, Log-URL sowie je ein erfolgreicher Python-, Bash- und PowerShell-Command-Exit belegt. Ein Jobstatus allein genuegt nicht; fehlende oder rote Windows-Command-Evidence blockiert ohne Bypass. / Linux, macOS, and mandatory Windows command-level evidence bind every serial process to the same head. |
| First-reader | `specs/002-portfolio-ownership/first-reader-review-evidence.md` | `6/6` korrekte Antworten, null Blocker. / `6/6`, zero blockers. |
| A11Y/B2 | `specs/002-portfolio-ownership/accessibility-review-evidence.md` | Alle benannten Kriterien Pass, null Blocker. / All named criteria pass, zero blockers. |
| Security/Privacy | `specs/002-portfolio-ownership/security-privacy-review-evidence.md` | Exakte Kandidatenabdeckung, null Blocker. / Exact candidate coverage, zero blockers. |
| Documentation Impact | `specs/002-portfolio-ownership/documentation-impact-evidence.md` | Genau eine vollstaendige `UpdateRequired`-Entscheidung einschliesslich `intake-lifecycle.json` und byteidentischem Original-/Archivpfadwechsel. / Exactly one complete decision including the lifecycle record and path transition. |
| AEPS | `docs/aeps/receipts/2026-08-30-meta-lh-02-portfolio-ownership.md`, finale Trigger-Evidence aus T092/T093 / final trigger evidence from T092/T093 | Implementierungsassessment T054 bleibt als unabhaengig validiertes `NoChange` erhalten. Nach der materiellen Retrospektive T092 und vor terminaler Completion in T093 ist die getrennte Allowlist-Transaktion `final-aeps-reassessment` unter `docs/aeps/README.md` Pflicht: Finding oder begruendet NoChange, unabhaengige Validierung und stabiler Delta-Abschluss vor dem kausalen Closeout, ohne dessen exakte drei Pfade zu verbreitern; keine Promotion-, Level-0-, Upstream- oder Folgelauf-Authority. / Preserve the implementation assessment and require the separate independently validated final AEPS transaction after T092 and before completion without broadening causal closeout. |
| Statistik / statistics | `docs/project-statistics.md`, historische T055-/T079-/R-022-Evidence und temporaere neue Final-Head-Bindung ausserhalb des Repositorys / historical evidence and temporary final-head binding | `68a1af2` und `7eb7470` bleiben verbrauchte unveraenderliche Historie. Nach genau einem normalen `windows-target-exit-followup` auf `7eb7470` wird der unveraenderte Renderer geprueft. Nur bei tatsaechlichem Drift entsteht hoechstens ein neuer `statistics-head-sync`-Commit ausschliesslich aus dem Ledger; Methodik v2 schliesst ihn aus. Beide realen Peers muessen auf dem finalen Head `CURRENT`/`0` melden, und jede betroffene Head-/Command-Evidence wird dorthin neu gebunden. / The published R-022 heads remain immutable; one follow-up and at most one actual-drift ledger-only sync lead to the final bound head. |

## Shared-Writer-Reihenfolge / Shared-writer order

```text
requirements/baseline/portfolio-ownership.md
  -> feature-lokale Review- und Gate-Evidence
  -> specs/002-portfolio-ownership/intake-lifecycle.json im normalen Kandidaten
  -> docs/aeps/* als eine serielle Assessment-Transaktion
  -> temporaere saubere Ein-Commit-Projektion ohne Ledger-Input
  -> docs/project-statistics.md ausschliesslich durch Renderer und Ledger-only-Copy
  -> provisorischer 35-Pfad-Kandidat, verbrauchtes Amend und Ledger-only-Sync bis a78a785 nur als Historie
  -> publizierte T079-Reparatur 8f395f8 und verbrauchter Ledger-only-Head 0b0808c als Historie
  -> publizierter R-022-Normalhead 68a1af2 und verbrauchter Ledger-only-Head 7eb7470 als Historie
  -> genau ein normaler windows-target-exit-followup auf 7eb7470
  -> finaler Render vom gefrorenen neuen Follow-up-Head
  -> nur bei weiterem Drift hoechstens ein neuer lokaler Ledger-only-Statistikcommit
  -> exakte Kandidatenmenge, Stage und alle betroffenen Gates auf dem Statistik-Head
  -> vorlaeufiger Execution Record ohne erfundenen PO-G32-Pass
  -> normaler Merge und Fast-forward-Sync
  -> dedizierter terminaler R100-Rename-Head als letzte Polish-Aufgabe
  -> eigene temporaere PreMerge-Evidence, Rename-Merge und Fast-forward-Sync
  -> kausales PostMerge und optionale Drei-Pfad-Closeout-Transaktion
  -> materielle Retrospektive und getrennte abschliessende unabhaengig validierte AEPS-Transaktion
  -> persistierter oder No-Persistence-Closeout mit ausdruecklichem No-next-run-Stop
```

Kein paralleler Worker darf einen dieser Pfade gleichzeitig schreiben. `8f395f8`, `0b0808c`, `68a1af2` und `7eb7470` bleiben verbrauchte Evidence ohne Wiederverwendungsautoritaet. Die optionale neue Synchronisation konsumiert ausschliesslich den gefrorenen normalen Follow-up-Head; Runtime-Artefakte, Caches, fremde Pfade und das Ledger selbst sind kein Methodikinput. Ein neuer Statistikcommit ist nur bei tatsaechlichem Drift zulaessig, enthaelt nur das Ledger und wird von Methodik v2 ausgeschlossen. Jede spaetere Head-Mutation invalidiert die Bindung und verlangt eine neue explizite Transaktionsreview. AEPS-Derivationen werden nur bei echtem Finding atomar aktualisiert; es bleibt genau eine bestehende `UpdateRequired`-Dokumentationsentscheidung. / *The final follow-up head alone drives any actual-drift synchronization; consumed history grants no reuse.*

## Finale Windows-Ziel-/Exitcode-Reparatur / Final Windows target and exit-code remediation

`implement-resume-9` ist auf PR #29 und exaktem Head `7eb747056898c26b0cbcfbe9081bd568a7fd7116` trotz 18/18 gruener Provider-Schlussfolgerungen wahrheitsgemaess `Blocked`. Das Windows-Log beweist 8 Failures und 1 Error der Python-Suite, deren Exitcode vor spaeteren Peers nicht geprueft wurde. Der kausale Fehler ist das physische Ziel-Rohblob-Gate, obwohl R-019 aktuelle Zielannahme normalisiert und rohe Unveraenderlichkeit nur fuer Receipt/Review verlangt. `68a1af2` und `7eb7470` bleiben unveraenderliche historische Evidence. Die spaetere Implementierung besitzt genau eine neue Follow-up-Transaktion mit diesen Mindestregeln: / *Implement-resume-9 is blocked by exact Windows command evidence despite green conclusions. One final bounded two-defect follow-up is permitted.*

1. Implementierende Bytes sind auf `.github/workflows/powershell-analysis.yml` und `contracts/validate_meta_lh02_snapshot.py` begrenzt. Der Workflow prueft Python, Bash und PowerShell jeweils unmittelbar vor dem naechsten Command fail-closed. / Only the workflow and Python core contain implementation bytes.
2. Der Core entfernt nur den physischen META-LH-02-Ziel-Rohblobvergleich. `originalRawSha256` bleibt formal/lowercase/evidence-gebunden; Original-/Archiv-Exklusivitaet, normalisierter Zielhash und rohe Receipt-/Review-Bytes bleiben bindend. / Remove only the current physical target raw comparison.
3. Vorhandene fokussierte Tests, PowerShell-Help, Man-Page, Quickstart und Evidence beweisen unmittelbare Exitpropagation, LF-/CRLF-Aequivalenz, substantive Ziel-Driftablehnung und unveraenderte Receipt-/Review-Rohhashfehler. / Use only existing focused proof paths.
4. Genau ein normaler Follow-up-Commit auf `7eb7470` ist erlaubt. Kein Amend, Force-Push oder History-Rewrite. Nur wenn der unveraenderte Methodik-v2-Renderer tatsaechlichen Drift meldet, darf hoechstens ein weiterer Commit nur `docs/project-statistics.md` synchronisieren. / One normal commit and at most one actual-drift ledger-only sync.
5. PR #29 wird an den resultierenden unveraenderlichen finalen Head gebunden. Alle 18 Checks, exakte Ubuntu-/macOS-/`windows-2022`-Evidence und Review-Konvergenz laufen neu. Jeder Python-/Bash-/PowerShell-Einzelcommand muss erfolgreich sein; technischer Fehler ist nicht bypassbar. / Rebind and rerun all head- and command-bound gates.
6. Erst danach werden T080 bis T093 fortgesetzt; beide terminalen Pfade enden mit No-next-run nach META-LH-02. / Continue the accepted closeout only after green and start no next run.

## CI-Zuordnung / CI mapping

| Workflow / Job | Plattform / Platform | Proof-Grenze / Proof boundary |
|---|---|---|
| `Homogeneity Check / homogeneity` | Ubuntu | T079 rendert ausschliesslich den ausgeloesten Embedded-Inventarpfad nach beiden Previews und verlangt beide Check-only-Peers; `docs/scripts/reference.md` bleibt unveraendert. / T079 closes only the canonical generated embedded-inventory drift. |
| `Public Readiness / Repository baseline` | Ubuntu | Secret-Muster und persoenliche absolute Pfade. / Secret patterns and personal absolute paths. |
| `Public Readiness / .NET contract` | Ubuntu, Windows, macOS | Aktuell `NotApplicable`, solange kein Produkt-Scaffold existiert. / Currently not applicable absent product scaffold. |
| `PowerShell Static Analysis / PSScriptAnalyzer` | Ubuntu, Windows, macOS | R-022s skalare Bash-Auswahl bleibt unveraendert. Python-Suite, Bash-Peer und PowerShell-Peer muessen jeweils unmittelbar fail-closed geprueft werden. Das physische META-LH-02-Ziel verwendet normalisierte UTF-8-Identitaet; Receipt-/Review-Rohbytes bleiben exakt. Workflow-/Job-/Runner-/Head-/Log-/Einzelcommand-/Exit-Evidence fuer alle drei Plattformen ist Pflicht. / Preserve scalar Bash selection, require immediate serial-command failure propagation, and bind normalized target plus raw receipt/review semantics. |
| `Maintenance TUI` | Ubuntu, Windows, macOS | Unveraenderte Wartungsregression; kein Feature-Acceptance-Ersatz. / Unchanged maintenance regression. |

Vor Merge werden `headRefOid`, beide Statistik-Check-only-Peers, alle gemeldeten Checks, die nichtleere Required-Teilmenge, `reviewDecision`, Workflow-Definitionen/Logs und alle nicht veralteten Review-Threads fuer denselben exakten finalen Statistik-Head abgeglichen. / *Before merge, both statistics peers and every provider/review fact are reconciled on the same final statistics head.*

## Schema-2.0-Evidence und Bypass / Schema-2.0 evidence and bypass

- `PreMerge`: Vollstaendig erst fuer den terminalen Rename-Head, weil erst dort alle 33 anwendbaren Gates tatsaechlich erfuellt sein koennen; temporaer ausserhalb des Repositorys, normalisierter Requirements-Hash, exakter reviewter Rename-Head und Pass beider installierter Gate-Evidence-Oberflaechen. Der normale Feature-Head besitzt vorher nur einen wahrheitsgemaessen vorlaeufigen Execution Record. / Full PreMerge exists only for the terminal rename head; the normal feature head has a truthful preliminary execution record.
- Enger Bypass: auf PR #29 wegen der exakten roten Windows-Command-Evidence trotz 18/18 gruener Provider-Schlussfolgerungen ausdruecklich unzulaessig. Erst nach neuem Head, allen 18 erfolgreichen/regelkonform uebersprungenen Checks, erfolgreichen Python-/Bash-/PowerShell-Einzelcommands auf allen drei Plattformen, vollstaendiger Security-/Plattform-/Review-Evidence, null handlungsrelevanten Threads und genau einer verbleibenden Approval-/Ruleset-Policy darf `PO-N01` neu bewertet werden. / Exact Windows command failure prohibits bypass until complete command-level green reconvergence leaves only one policy blocker.
- `PostMerge`: erst kausal nach echtem Merge und Fast-forward-Sync des terminalen Rename-Heads; bindet dessen akzeptierten PreMerge-Hash, reviewten Rename-Head, echten Rename-Merge-Commit und leere `changedPaths`. / Created causally only after the merged terminal rename.
- AEPS-Abschluss: Die materielle Retrospektive T092 loest vor T093 die getrennte Allowlist-Transaktion `final-aeps-reassessment` aus. Sie bindet den verpflichtenden Receipt und nur bei echtem Finding die vier bestehenden konditionalen AEPS-Pfade, wird unabhaengig validiert und stabil abgeschlossen, bevor der exakte Drei-Pfad-Closeout oder der No-Persistence-Pfad endet; kein Level-0-, Preset-, Upstream- oder Folgelauf-Schritt. / The material retrospective triggers the separate independently validated final AEPS transaction before either closeout path, without expanded authority.
- Closeout: Nur wenn Providerfakten repository-lokal gespeichert werden muessen und ein echter Delta besteht, exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`; sonst keine leere PR. Beide Pfade enden mit der ausdruecklichen No-next-run-Disposition nach META-LH-02. / Exact three-path closeout only for a real eligible delta; otherwise no empty PR, and both paths end with no next run after META-LH-02.

## Abschlussregel / Completion rule

`Completed` ist erst zulaessig, wenn alle fuer die jeweilige Phase erwarteten Artefakte existieren, jede aktuelle Gate-Evidence bestanden ist und der Payload-Normalhash stimmt. Terminale Feature-Completion verlangt zusaetzlich normalen Merge, Fast-forward-Sync, den separat reviewten und gemergten `R100`-Rename, erneuten Sync, kausale PostMerge-Disposition, die nach T092 unabhaengig validierte abschliessende AEPS-Finding-oder-NoChange-Neubewertung und auf dem persistierten wie dem No-Persistence-Pfad die ausdrueckliche No-next-run-Disposition. Danach stoppt der Run; META-LH-03 und jeder andere Spec-Kit-Lauf bleiben ohne neuen ausdruecklichen Auftrag ungestartet. Planungs-`Completed` behauptet keine dieser spaeteren Ausfuehrungen. / *Terminal completion requires causal delivery, the final independently validated AEPS reassessment, and an explicit no-next-run stop on either closeout path; planning completion claims none of those future facts.*
