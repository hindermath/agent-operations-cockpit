# Repository-Validierungsvertrag: META-LH-01 / Repository Validation Contract: META-LH-01

## Zweck / Purpose

Dieser Vertrag definiert die pruefbare Oberflaeche der sechs Domain-Artefakte und der begrenzten Workflow-Evidence. [validate_meta_lh01.py](validate_meta_lh01.py) ist die einzige stabile ausfuehrbare Oberflaeche; sie nutzt nur die Python-Standardbibliothek und schreibt nicht in Repository, Index oder Worktree. Der temporaere Render-Modus lehnt Repository-Ziele ab. Das Werkzeug ist Workflow-Evidence, keine Produkt-API oder Produktfunktion. / This contract defines the verifiable surface of the six domain artefacts and bounded workflow evidence. The linked standard-library Python file is the sole stable executable surface. It is read-only against repository, index, and worktree; its temporary render mode rejects repository output paths. It is workflow evidence, not a product API or feature.

## Ausfuehrbare Modi / Executable Modes

Jeder erfolgreiche Modus schreibt genau eine `PASS:`-Zeile nach stdout. Fehler schreiben praezise `ERROR:`-Zeilen nach stderr und liefern einen von null verschiedenen Exitcode. / Every successful mode emits exactly one `PASS:` line to stdout. Failures emit precise `ERROR:` diagnostics to stderr and return non-zero.

| Modus / Mode | Deterministisch bewiesener Scope / Deterministically proven scope |
|---|---|
| `input-bindings --surface bash|powershell` | Genau drei logische akzeptierte Artefakte und schema-1.1-Lifecycle-Aufloesung. Vor Implement laufen generische Receipt-/Review-Pruefungen. Nur bei exakt `Implement`/`Active`/`GlobalReadyBeforeImplement`, aktuellem Branch und passenden Run-/Lifecycle-Bindungen darf der vollstaendige 14-Ziel-Snapshot die Receipt-Quellenfrische ersetzen; die gewaehlte Run-State- und Review-Oberflaeche laeuft weiter. Nach dem Rename validiert die unveraenderte Review-Oberflaeche eine automatisch entfernte externe Projektion der hashgeprueften Archivbytes am logischen Originalpfad. / After rename, the unchanged review surface validates a short-lived external projection of the proven archive bytes at the immutable logical path. |
| `global-ready` | Exakt 14 geordnete logische Ziele, META-LH-01 zuerst. Vor Implement laufen beide Receipt-/Review-Oberflaechen fuer alle 14. Im exakt qualifizierten Implement-Zustand bindet der vollstaendige Snapshot Zielpfad/Normalhash sowie eindeutigen Receipt-/Ready-Review-Pfad/Rohhash und ersetzt nur Receipt-Quellenfrische; beide Review-Oberflaechen laufen weiter. / Exactly fourteen ordered targets; generic receipt/review freshness applies before Implement and the qualified snapshot replaces only receipt source freshness. |
| `domain` | Alle sechs Pfade, exakte 23/21/10-Mengen, getrennte Pflichtfelder, Coverage, Glossar und G-01/G-05/G-06-Struktur. / All six paths, exact sets, fields, coverage, glossary, and gate structure. |
| `review-evidence --kind semantic|accessibility|public` | Vollstaendigkeit einer getrennten strukturierten unabhaengigen Review-Evidence; nicht die fachliche oder A11Y-Wahrheit selbst. / Completeness of separately structured independent evidence, not semantic or accessibility truth itself. |
| `documentation-impact` | Schema 1.1, genau ein Eintrag, logischer kanonischer Originalpfad, normale Kandidatenpfade plus Lifecycle-Datensatz und beide Rename-Pfade sowie beide installierten Validatoren. / Schema 1.1, one entry, logical original canonical source, normal candidate plus the lifecycle transition, and both installed validators. |
| `aeps` | Genau ein begrenzter Finding- oder No-change-Ausgang samt Hash-, Deduplizierungs-, Reife- und Nicht-Handoff-Grenze. / Exactly one bounded AEPS outcome. |
| `candidate` | Exakte staged Pfade gegen Maximum und eingefrorene Sollmenge, Porcelain einschliesslich untracked, keine unstaged Kandidatenreste und `git diff --cached --check`. / Exact staged inventory reconciliation including untracked state. |
| `candidate-list` | Schreibt die aktuelle erlaubte Worktree-Teilmenge ausschliesslich in eine benannte temporaere Datei ausserhalb des Repositorys. / Writes the current allowed worktree subset only to one named temporary file outside the repository. |
| `candidate-fixpoint` | Eingefrorene Sollmenge entspricht nach allen Evidence-Aktualisierungen weiterhin exakt dem Worktree und der Allowlist. / Frozen candidate paths remain exact after all evidence updates. |
| `terminal-rename` | Aktueller Head enthaelt exakt einen byteidentischen `R100`-Rename vom Original- zum branch-gestempelten Archivpfad, den exakten Co-Author-Trailer und keine Stage-Reste. / Current head contains exactly one byte-identical R100 transition, the exact trailer, and no staged residue. |
| `causal-closeout` | Exakt T001-T066 geprueft, `completed == total == 66`, realer Task-Hash, schema-1.1 `Completed` in `MergeAndSync`, terminale Closeout-Felder, `nextExactAction: N/A`, exakte Drei-Pfad-Stage, vollstaendige Documentation-/Public-Content-Re-Reviews und keine selbstreferenziellen Closeout-Publikationsfakten. / Exactly 66 checked tasks, matching terminal state and hash, exact three-path stage, complete re-reviews, and no self-reference. |
| `check-inventory` | Alle gemeldeten PR-Checks und die Required-Teilmenge sind nicht leer, konsistent und terminal `pass` oder `skipping`. / All reported and required PR checks are non-empty, consistent, and terminal-successful. |
| `render-gate-evidence` | Erzeugt aus einem exakten Head und vollstaendigem Execution Record genau eine temporaere providerneutrale Evidence ausserhalb des Repositorys. / Renders one temporary provider-neutral evidence file outside the repository. |

## Gebundene Pfade / Bound Paths

1. `requirements/baseline/source-pack.md`
2. `requirements/baseline/constraint-register.md`
3. `requirements/baseline/review-findings-ledger.md`
4. `requirements/baseline/coverage-matrix.md`
5. `requirements/baseline/glossary.md`
6. `requirements/baseline/authority-and-stop-gates.md`

Weitere Domain-Pfade sind nicht Bestandteil von META-LH-01. / No other domain paths belong to META-LH-01.

## Lifecycle- und Accepted-Artifact-Vertrag / Lifecycle and Accepted-Artifact Contract

`specs/001-programmquellen-baseline/intake-lifecycle.json` verwendet Schema 1.1. Der bestehende exakte `recordVersion: 1.0`-Datensatz fuer `META-LH-01` bleibt unveraendert. Zusaetzlich existiert genau ein `programmeEvidenceSnapshot` mit `snapshotVersion: 1.0`, Run-ID, Branch und exakt 14 geordneten `orderedLogicalTargets`. Jeder Eintrag enthaelt ausschliesslich logische ID, Zielpfad/Normalhash, Authoring-Receipt-Pfad/Rohhash und Ready-Single-Review-Pfad/Rohhash. Weder Datensatz noch Snapshot enthalten den SHA eines enthaltenden Commits oder mutable Zukunftsfakten. / The schema-1.1 lifecycle file preserves the exact META-LH-01 record and adds one ordered fourteen-target immutable evidence snapshot without containing-commit or future facts.

Vor dem Rename muss nur der Originalpfad existieren, danach nur der exakte Archivpfad. Die Archivdatei bleibt byteidentisch und normalisiert hashidentisch. Snapshot-Validierung verlangt die exakte geordnete Zielmenge ohne Duplikate; lowercase Hashes; aktuelle unveraenderte Receipt-/Review-Bytes; passende Zielpfade/-hashes; Receipt `ReadyForReview`; Review `Single`/`Primary`/`Ready`; leere Findings, Fragen und akzeptierte Risiken; eindeutige aktuelle Leaves; passende Run-ID, Branch und Lifecycle-Aufloesung. Jede Abweichung blockiert. / Snapshot validation exhaustively covers ordered identity, hashes, immutable bytes, Ready semantics, unique leaves, run, branch, and lifecycle resolution; every mismatch fails.

## Exakte Source-Menge / Exact Source Set

Die Inventur und die Source-Coverage enthalten je genau einmal: / The inventory and source coverage each contain exactly once:

```text
SRC-156 SRC-157 SRC-159 SRC-161 SRC-162 SRC-163 SRC-164 SRC-165 SRC-166
SRC-167 SRC-168 SRC-169 SRC-170 SRC-171 SRC-172 SRC-173 SRC-174 SRC-175
SRC-177 SRC-180 SRC-181 SRC-182 SRC-ES-01
```

`SRC-158`, `SRC-160`, `SRC-176`, `SRC-178` und `SRC-179` sind keine Quellen. Die sichtbare Bereichsnotation `SRC-163` bis `SRC-167` darf erklaerend verwendet werden, ersetzt aber keine Einzelzeilen. / The five named gaps are not sources. Visible range notation may be explanatory but never replaces individual rows.

## Exakte Finding-Menge / Exact Finding Set

Ledger und Finding-Coverage enthalten je genau einmal: / The ledger and finding coverage each contain exactly once:

```text
RF-01 RF-02 RF-03 RF-04 RF-05 RF-06 RF-07 RF-08 RF-09 RF-10 RF-11
RF-12 RF-13 RF-14 RF-15 RF-16 RF-17 RF-18 RF-19 RF-20 RF-21
```

Jede Ledger-Zeile besitzt: / Every ledger row has:

1. Schweregrad / Severity,
2. praezise Aussage und Quelle / precise statement and source,
3. Owner,
4. Ziel / target,
5. Akzeptanzkriterium / acceptance criterion,
6. positive Evidence,
7. negative Evidence,
8. Status,
9. Restluecke / residual gap.

Kein blocking Finding ist `Uncovered`. `Covered` bedeutet Requirements-Abdeckung, nicht Produktimplementierung oder Wirksamkeit. / No blocking finding is `Uncovered`. `Covered` means requirements coverage, not product implementation or effectiveness.

## Direkte META-LH-01-Verantwortung / Direct META-LH-01 Responsibility

Die direkte Menge ist exakt: / The direct set is exactly:

```text
RF-01 RF-04 RF-11 RF-12 RF-13 RF-14 RF-15 RF-16 RF-17 RF-21
```

Alle anderen Findings bleiben programmweit sichtbar, erhalten aber fuer die direkte META-LH-01-Spalte den Wert `No`. Sammelnotation darf diese zehn IDs nicht erweitern oder verkleinern. / All other findings remain programme-visible but use `No` in the direct META-LH-01 column. Aggregate notation must not expand or reduce these ten IDs.

## Source-Rang und Supersession / Source Precedence and Supersession

1. Bestaetigte Level-2-Decisions stehen vor dem Source Pack. / Confirmed level-2 decisions precede the source pack.
2. Das Source Pack steht vor aelteren Entwuerfen. / The source pack precedes older drafts.
3. Ein neueres Datum oder ein Kommentar ersetzt nichts ohne ausdrueckliche Decision und Revisionsgrund. / A newer date or comment supersedes nothing without an explicit decision and revision reason.
4. Level-0-Issues duerfen Provenienz sein, aber keine notwendige Lese- oder Laufzeitabhaengigkeit. / Level-0 issues may be provenance but not a required reading or runtime dependency.

## Authority-Gates / Authority Gates

`authority-and-stop-gates.md` beschreibt mindestens G-01, G-05 und G-06 in je einer strukturellen Zeile mit erlaubter Aktion, Stop-Bedingung, erforderlicher Evidence, menschlicher Entscheidung und genau einer sicheren naechsten Aktion. Jede fehlende oder veraltete Evidence wirkt fail-closed. G-05 bindet die 14er-Ready-Sperre und erteilt keine G-06-Implementierungsautoritaet. Fuer dieses Feature begrenzt G-06 die Umsetzung auf Dokumentation und Governance; Produktcode und Produktarchitektur bleiben ausgeschlossen. / The authority document uses one complete row per named gate. G-05 binds the fourteen-target gate and grants no implementation authority; G-06 remains documentation-only.

## Strukturierte Review-Evidence / Structured Review Evidence

Die JSON-Evidence verwendet Schema 1.0, eine Rolle mit `independent: true`, eine nichtleere Unabhaengigkeitserklaerung und `blockingFindings: []`. Semantik und Accessibility enthalten genau die sechs Domain-Pfade plus den nutzerlesbaren Pending-Anker `causal-closeout-evidence.json`. Public Content enthaelt exakt alle Pfade der stabil eingefrorenen normalen Kandidatenliste einschliesslich dieses Ankers plus Lifecycle-Datensatz, Original- und Archivpfad. Jedes Kriterium ist `Pass` oder blockiert; jede Zeile besitzt eine Begruendung. / Semantic and accessibility evidence also cover the readable Pending closeout anchor; public-content evidence covers the full normal candidate and lifecycle transition.

## Documentation Impact und AEPS / Documentation Impact and AEPS

- Documentation Impact ist Schema 1.1 mit genau einem `UpdateRequired`-Eintrag. `canonicalSource` bleibt der originale logische Pfad; `documents` entspricht exakt der eingefrorenen normalen Kandidatenliste einschliesslich Pending-Closeout-Anker plus Lifecycle-Datensatz, Original- und Archivpfad der Rename-Transition. Der spaetere Closeout-Delta wird erneut reviewt, erzeugt aber keine zweite Decision. / Documentation Impact includes the Pending closeout anchor; the later exact delta is re-reviewed without a second decision.
- Der AEPS-Receipt besitzt genau einen eingezaeunten Block `aeps-outcome-json`. `outcome` ist `Finding` oder `NoChange`; ein einzelner AOC-Lauf bleibt hoechstens `candidate`. Bei `ReadyReview` ist der Deduplizierungsschluessel exakt `Review-ID + Zielpfad + normalisierter Zielhash`; bei anderen Triggern exakt `Quellpfad + normalisierter Artefakthash + Erfassungsdatum`. Ein bereits in einem anderen Receipt vorhandener Schluessel blockiert. Finding bindet genau einen Ledger-Abschnitt mit allen Pflichtfeldern, gueltigem Capture-/Upstream-Status sowie Source- und Receipt-Pfad; NoChange veraendert das Ledger nicht. Beide setzen Preset-Promotion und Level-0-Handoff auf `false`. / A Finding binds one complete canonical ledger section; NoChange remains ledger-free.

## Kandidaten- und Exact-Head-Vertrag / Candidate and Exact-head Contract

`candidate-paths.json` ist nur die maximale Feature-Grenze und nennt Lifecycle-Datensatz, beide Rename-Pfade und `causal-closeout-evidence.json` bereits als Pending-Anker. Die normale Kandidatenmenge wird zweipassig eingefroren und exakt gestaged. Nach dem normalen Kandidaten-Commit darf ausschliesslich `scripts/rename-lastenheft.sh` den Originalpfad als byteidentischen Archivpfad committen. / The maximum allowlist includes the lifecycle transition and the Pending causal-closeout anchor before the script-created terminal rename commit.

Der normale Kandidat wird zuerst committed. Der Rename ist die letzte Polish-Aktion und der letzte Feature-Branch-Commit; `terminal-rename` prueft dessen exakten `R100`-Inhalt. Erst dieser unveraenderliche Head wird gepusht, reviewt, exact-head validiert und gemergt. Nach Fast-forward-Sync entsteht genau `codex/001-programmquellen-baseline-closeout` von `main`. Dessen Write-Allowlist ist exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`. Vor seinem einzigen Commit werden archivbewusste Finalvalidierung und beide Re-Reviews abgeschlossen; `causal-closeout` prueft Stage, 66/66, Hash, terminalen State und die Nicht-Selbstreferenz. / The immutable terminal feature head is merged first; a separate pre-named exact three-path closeout branch then persists completion.

Der Closeout-Commit ist der letzte lokale Akt von T066. Fuer seine checkboxfreie Publikation wird ein Body in `/tmp/001-programmquellen-baseline-closeout-pr-body.md` geschrieben. Unter den jeweils exakt einmal validierten Ueberschriften `Betroffene Skripte und Dokumente / Affected scripts and documents`, `Manuelle Pruefung / Manual verification`, `Beispielausgabe / Sample output` und `Security-Risiko / Security risk` nennt er als betroffene Pfade exakt `tasks.md`, `autonomous-run-state.json` und `causal-closeout-evidence.json`, die tatsaechliche manuelle Verifikation, Beispielausgabe oder ein begruendetes `N/A` und eine ausdrueckliche Security-Risikoaussage. Erst danach darf `gh pr create --body-file` oder `gh pr edit --body-file` publizieren. Push, exakte Head-Pruefung, unabhaengiger Review, alle Checks samt nichtleerer Required-Teilmenge, null actionable Threads, normaler Merge oder der bereits begrenzte Approval-only-Admin-Fallback, Cleanup, finaler `main...origin/main = 0 0`-Vergleich und sauberer Worktree publizieren den Commit unveraendert. Closeout-PR- und Merge-SHA werden extern berichtet und nicht in den eigenen Commit geschrieben. / The closeout commit completes T066 locally. Its checkbox-free publication writes and validates a four-heading body file naming exactly the three closeout paths and required verification, sample-output-or-N/A, and security-risk content before `gh pr create --body-file` or `gh pr edit --body-file`; all exact-head, independent-review, check, bounded-merge, cleanup, and external-reporting controls remain unchanged without self-claim or mutation.

## Negative Vertragsfaelle / Negative Contract Cases

[test_validate_meta_lh01.py](test_validate_meta_lh01.py) prueft exakt 66 isolierte temporaere Faelle. Alle vorhandenen 43 bleiben erhalten. Genau 23 neue Faelle pruefen positive Post-Implement-Shared-Source-Evolution fuer Bash, PowerShell und `global-ready` sowie negative pre-Implement-Drift-, Stage-/Status-/Last-Gate-, fehlende/duplizierte/umsortierte Ziel-, falsche Ziel-/Receipt-/Review-Pfad-/Hash-, geaenderte Receipt-/Review-Byte-, non-Ready-, non-unique-Leaf- und falsche Branch-/Run-/Lifecycle-Grenzen. / The suite preserves all 43 cases and adds exactly 23 snapshot cases, for 66 total.

## Sprach-, A11Y- und Inhaltsvertrag / Language, Accessibility, and Content Contract

- Deutsch steht zuerst und ist autoritativ; gleichwertiges Englisch folgt. / German comes first and is authoritative; equivalent English follows.
- Sprache zielt auf CEFR B2 und erklaert Fachbegriffe bei Erstnutzung oder verlinkt das Glossar. / Language targets CEFR B2 and explains first-use terms or links the glossary.
- Heading-Hierarchie, Tabellen, Links, Status und Reihenfolge bleiben mit Screenreader und Textbrowser verstaendlich. / Heading hierarchy, tables, links, status, and order remain understandable with screen readers and text browsers.
- Bedeutung haengt nicht von Farbe, Grafik, Position oder Raumbezug ab. / Meaning does not depend on colour, diagrams, position, or spatial relations.
- Nur oeffentlich geeignete Inhalte ohne Secrets, private Pfade oder unnoetige personenbezogene Daten sind erlaubt. / Only public-suitable content without secrets, private paths, or unnecessary personal data is allowed.

## Pruefgrenze / Proof Boundary

Deterministische Mengen- und Strukturpruefungen beweisen IDs, Pflichtfelder und Marker. Der unabhaengige semantische Review beweist DE/EN-Gleichwertigkeit, CEFR-B2-Naehe, fachliche Wahrheit und Authority-Auslegung. Der getrennte unabhaengige Accessibility-Review bewertet WCAG-2.2-AA-Anwendbarkeit und Text-first-Qualitaet. Keine dieser Pruefungen beweist Produktimplementierung. / Deterministic checks, semantic review, and accessibility review have separate proof boundaries; none proves product implementation.

## Aenderungsregel / Change Rule

Eine Aenderung dieses Vertrags ist nur bei Drift der geklaerten Spezifikation, einer neuen bestaetigten Quelle, Decision, Supersession oder einem neuen Finding zulaessig. Dann muessen Spec, Plan, Tasks, Gate-Anforderungen und alle betroffenen Bindungen erneut geprueft werden. / This contract changes only when the clarified specification drifts or a newly confirmed source, decision, supersession, or finding appears. The spec, plan, tasks, gate requirements, and all affected bindings must then be revalidated.
