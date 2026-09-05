# Plan Review R4: META-LH-03 Authoring Contract

## Ergebnis

**BLOCKED.** O1 ist auf Planebene behoben. O2 bleibt wegen zweier
maschinenlesbarer Reihenfolgewidersprueche offen; Tasks koennen noch nicht
sicher neu erzeugt werden. Dieser unabhaengige Review hat nur die begrenzte
R4-Remediation geprueft und keine spaetere Ausfuehrungstatsache behauptet.

## Pruefgrenze

- Gepruefte Remediation: `plan.md`, `contracts/authoring-contract-design.json`
  und `contracts/postmerge-gate-requirements.json`.
- Vergleich: `spec.md`, `research.md`, `data-model.md`, `quickstart.md`, der
  akzeptierte R3-Bericht und `phase-results/analyze-report.md`.
- Beide JSON-Vertraege sind syntaktisch gueltig. `.specify/extensions.yml`
  fehlt; Plan-Hooks waren nicht anwendbar.
- Keine Implementierung, kein Testlauf, kein Edit eines geprueften Artefakts
  und keine Git-/Remote-Schreibaktion erfolgte. Dieser Bericht ist die einzige
  Repository-Aenderung.

## Aufloesungsstatus O1 und O2

| Finding | Status | Nachweis |
|---|---|---|
| O1 | **Resolved** | `plan.md:255-261` beendet alle Repository-Writer einschliesslich Statistik, pusht und friert den finalen Feature-HEAD ein, konvergiert danach PR, Checks, Threads, Review und Approval fuer genau diesen HEAD und erzeugt/validiert erst dann den externen PreMerge-Snapshot. Bis zum Merge folgt kein Repository-Writer. |
| O2 | **Not resolved** | Die beabsichtigte Strategie steht in `plan.md:271-277`, `authoring-contract-design.json:491-502` und PMG-004/PMG-007. Der verbindliche Designgraph ordnet jedoch weiterhin `lifecycle -> postmerge -> closeout` (`authoring-contract-design.json:118-120`), obwohl Plan, Datenmodell und Quickstart den Runner-PostMerge-Snapshot erst nach dem tatsaechlichen Closeout-Merge und Sync verlangen. Ausserdem verlangt der PostMerge-Vertrag fuer jedes anwendbare Gate bereits `Pass` im Snapshot (`postmerge-gate-requirements.json:8-10`), waehrend PMG-007 Nachweis aus dem erst nach dem gerouteten Implement-Ergebnis zulaessigen Persistence-Merge fordert (`:110-119`). Das Implement-Ergebnis haengt seinerseits vom erfolgreichen PostMerge-Snapshot ab (`plan.md:273-277`). |

## Verifikation der sieben R4-Bedingungen

| Nr. | Status | Bewertung |
|---|---|---|
| 1 | **Pass** | Finaler Repository-Feature-HEAD wird vor PR-/Check-/Review-/Approval-Konvergenz eingefroren und gepusht. |
| 2 | **Pass** | PreMerge entsteht und besteht erst nach den Exact-HEAD-Fakten; bis zum Merge ist kein weiterer Repository-Writer erlaubt. |
| 3 | **Pass** | Der Closeout ist genau ein normal gepruefter transaktionaler PR mit exakt fuenf Pfaden und behauptet seinen eigenen Merge nicht. |
| 4 | **Blocked** | Die Texte und die Persistence-Strategie verlangen den externen Snapshot nach Closeout-Merge/Sync, aber der maschinenlesbare Phasengraph ordnet PostMerge vor Closeout. |
| 5 | **Blocked** | Die Zwei-Pfad-Positivliste und der einzelne normale Persistence-PR sind korrekt begrenzt; PMG-007 macht dessen spaetere externe Evidence jedoch zu einer Voraussetzung des frueher zu bestehenden PostMerge-Snapshots. |
| 6 | **Blocked** | `PostMerge-Pass -> Implement-Ergebnis -> Persistence-Merge -> fuer PostMerge verlangter Endnachweis` ist zyklisch; die Sequenz ist damit nicht endlich ausfuehrbar. |
| 7 | **Pass** | Keine neue Scope-, Delivery-, Bypass-, Level-0-, Preset-, Produkt- oder Provider-Faehigkeit wurde hinzugefuegt. `MergeAndSync` bleibt auf normale Aktionen im genehmigten Scope begrenzt. |

## Neues Finding

**R4-N1 — HIGH — widerspruechliche PostMerge-Orchestrierung.** Der
maschinenlesbare Phasengraph und PMG-007 widersprechen der gewaehlten endlichen
Strategie. Begrenzte Korrektur: den Graphen kausal auf
`lifecycle -> closeout -> postmerge` ausrichten und PMG-007 so trennen, dass
der PostMerge-Snapshot nur bereits bekannte Closeout-/Sync-Fakten prueft. Der
einmalige Zwei-Pfad-Persistence-PR und sein nachgelagerter externer
Fast-forward-/Clean-/`0/0`-Nachweis duerfen erst nach dem gerouteten
Implement-Ergebnis liegen und keine Voraussetzung dieses Ergebnisses sein.

## Gate-Entscheidung

**Blocked.** O1 ist geschlossen; O2 und R4-N1 bleiben High. Tasks duerfen erst
nach der begrenzten, widerspruchsfreien Plan-/Design-Gate-Korrektur neu erzeugt
werden.

## Result

**BLOCKED.** O1 is resolved at Plan level. O2 remains open because two
machine-readable ordering contradictions prevent safe Tasks regeneration. This
independent review assessed only the bounded R4 remediation and claims no later
execution fact.

## Review boundary

- Remediation reviewed: `plan.md`, `contracts/authoring-contract-design.json`,
  and `contracts/postmerge-gate-requirements.json`.
- Compared with `spec.md`, `research.md`, `data-model.md`, `quickstart.md`, the
  accepted R3 report, and `phase-results/analyze-report.md`.
- Both JSON contracts parse successfully. No `.specify/extensions.yml` exists,
  so no Plan hook applied.
- No implementation, test run, reviewed-artifact edit, or Git/remote write was
  performed. This report is the only repository change.

## O1 and O2 resolution status

| Finding | Status | Evidence |
|---|---|---|
| O1 | **Resolved** | `plan.md:255-261` completes all repository writers, including statistics, freezes and pushes the final feature head, converges PR/check/thread/review/approval facts for that exact head, and only then creates and validates the external PreMerge snapshot. No repository writer follows before merge. |
| O2 | **Not resolved** | The intended strategy appears in `plan.md:271-277`, `authoring-contract-design.json:491-502`, and PMG-004/PMG-007. However, the binding design graph still orders `lifecycle -> postmerge -> closeout` (`authoring-contract-design.json:118-120`) although Plan, data model, and quickstart require the runner PostMerge snapshot only after the actual closeout merge and synchronization. The PostMerge contract also requires every applicable gate to be `Pass` in that snapshot (`postmerge-gate-requirements.json:8-10`), while PMG-007 requires proof from the persistence merge allowed only after the routed Implement result (`:110-119`). That Implement result itself depends on the successful PostMerge snapshot (`plan.md:273-277`). |

## Verification of the seven R4 conditions

| No. | Status | Assessment |
|---|---|---|
| 1 | **Pass** | The final repository feature head is frozen and pushed before PR/check/review/approval convergence. |
| 2 | **Pass** | PreMerge is created and passes only after exact-head facts, with no repository writer before merge. |
| 3 | **Pass** | Closeout is one normally reviewed transactional PR limited to exactly five paths and does not claim its own merge. |
| 4 | **Blocked** | Text and strategy require the external snapshot after closeout merge/sync, but the machine-readable graph orders PostMerge before closeout. |
| 5 | **Blocked** | The two-path allowlist and single normal persistence PR are bounded correctly, but PMG-007 makes their later external evidence a prerequisite of the earlier PostMerge snapshot. |
| 6 | **Blocked** | `PostMerge pass -> Implement result -> persistence merge -> evidence required by PostMerge` is cyclic and therefore not finitely executable. |
| 7 | **Pass** | No scope, delivery, bypass, Level 0, preset, product, or provider capability was added. `MergeAndSync` remains limited to normal actions in approved scope. |

## New finding

**R4-N1 — HIGH — contradictory PostMerge orchestration.** The machine-readable
phase graph and PMG-007 contradict the selected finite strategy. Bounded
remediation: align the graph causally as `lifecycle -> closeout -> postmerge`
and split PMG-007 so the PostMerge snapshot checks only already-known
closeout/synchronization facts. The one-time two-path persistence PR and its
later external fast-forward/clean/`0/0` proof must occur after the routed
Implement result and must not be a prerequisite of that result.

## Gate decision

**Blocked.** O1 is closed; O2 and R4-N1 remain High. Tasks may be regenerated
only after the bounded Plan/design-gate correction is internally consistent.
