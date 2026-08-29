# Retrospektive des autonomen Laufs / Autonomous Run Retrospective

## Laufidentitaet / Run Identity

| Feld / Field | Wert / Value |
|---|---|
| Feature und Quellrevision / Feature and source revision | `001-programmquellen-baseline`; terminaler Feature-Head `2ff8e4a9fa185a2836ee91c0edc9d0ff907a8b58` |
| Lauf / Run | `b3694a58-208b-4d6b-a4d4-1b01f3816dcc`; `Completed`; 66 von 66 Aufgaben |
| Delivery Evidence | `c773548c6cca752f61e73de4d77e1077347924d7:specs/001-programmquellen-baseline/causal-closeout-evidence.json` |
| Delivery-Modus / Delivery mode | `MergeAndSync` |
| Remote-Ergebnis / Remote result | Feature-PR #19, Merge `031c335360afd75f04a8837dc2fe6723a3c9ea91`; Closeout-PR #20, Merge `fc5c8e991d7a7ba23ca6beb53e284f7ad0bb93d9`; lokales und entferntes `main` synchron |
| Unterbrechung und Fortsetzung / Interruption and resume | Ein Resume-Audit ist im terminalen State gebunden; keine offene oder unsichere Operation |

Die Retrospektive bewertet den abgeschlossenen Lauf. Sie veraendert keine
akzeptierten Feature-Artefakte und erteilt keine Preset-, Level-0-, GitHub-,
Merge- oder Bypass-Berechtigung. / *This retrospective assesses the completed
run. It changes no accepted feature artifact and grants no preset, level-0,
GitHub, merge, or bypass authority.*

## Entscheidungen im Ueberblick / Decision Overview

| ID | Entscheidung / Decision | Artefaktart / Artifact kind | Auftreten und Vertrauen / Occurrences and confidence |
|---|---|---|---|
| `AR-001` | `Promote` | Script requirement und Evidence Structure | ein deterministischer Fehler, hoch / one deterministic defect, high |
| `AR-002` | `Promote` | Evidence Structure und Runbook | neun Referenzen in einem Lauf, hoch / nine references in one run, high |
| `AR-003` | `Promote` | Script requirement und Lifecycle Evidence | zwei Oberflaechen nach einer Transition, hoch / two surfaces after one transition, high |
| `AR-004` | `ObserveAgain` | Runbook und Template | ein Lauf, mittel / one run, medium |
| `AR-005` | `NoPromotion` | projektspezifische Implementierung / project-specific implementation | ein erwarteter Phasengrenzfall, hoch / one expected phase-bound case, high |

## AR-001 - N/A-Gates duerfen keine Ausfuehrungstokens behalten / N/A Gates Must Not Retain Execution Tokens

- **Unveraenderliche Quelle / Immutable source:** Vorher- und Nachherzustand in
  Commit `3ff1a80795a791fa7a9e1ea81bc41162be9e0fb9` fuer
  `autonomous-run-gate-requirements.json`; aktueller generischer Validator in
  `703494f0ec7edb603653c61834e32fd2de2e8415:.specify/presets/autonomous-run-governance/scripts/autonomous-evidence-core.py`.
- **Beobachtung und Grenze / Observation and boundary:** Das Feature-Gate
  `META01-G14-causal-closeout` war `N/A`, enthielt aber weiterhin erforderliche
  Command- und Runner-Tokens. Der Feature-Fix leerte beide Listen. Der aktuelle
  generische Schema-2.0-Validator akzeptiert dieselbe widerspruechliche Form
  weiterhin, weil er die Tokens bei `N/A` ignoriert. Das ist ein
  Evidence-Integritaetsfehler, keine Effizienzpraeferenz. / *The feature fixed
  an N/A gate that still required commands and runners. The current generic
  validator still accepts that contradictory shape.*
- **Projektausschluss / Project exclusion:** Gate-ID, Branchname und
  META-LH-01-Befehle sind AOC-spezifisch.
- **Providerneutrale Zielregel / Provider-neutral target rule:** Bei
  `applicability == "N/A"` MUESSEN Command-Tokens, Runner-Tokens und geplante
  Ausfuehrungsevidence leer sein; Begruendung und Re-Evaluation-Trigger MUESSEN
  nichtleer sein. `Applicable` verwendet die umgekehrte Form. / *N/A requires
  empty execution tokens and planned execution evidence plus a substantive
  rationale and re-evaluation trigger.*
- **Berechtigungs- und Evidenzrisiko / Permission and evidence risk:** Sonst
  kann eine nicht anwendbare Zeile spaeter als versteckte Ausfuehrungsanweisung
  oder als scheinbar fehlende Evidence gelesen werden.
- **Reproduzierbarer Test / Reproducible test:** Eine In-Memory-Fixture mit
  `N/A`, nichtleeren Command- und Runner-Tokens und gueltiger N/A-Evidence muss
  mit einem stabilen Fehlercode scheitern; der kanonische leere N/A-Fall muss
  bestehen. Der Lauf vom 2026-08-29 ergab vor einer Preset-Aenderung
  `UNEXPECTED_PASS`.

## AR-002 - Dauerhafte Closeout-Evidence darf nicht nur auf Temp-Dateien zeigen / Durable Closeout Evidence Must Not Depend Only on Temporary Files

- **Unveraenderliche Quelle / Immutable source:** Commit
  `c773548c6cca752f61e73de4d77e1077347924d7`, Pfad
  `specs/001-programmquellen-baseline/causal-closeout-evidence.json`, SHA-256
  `0f93b1beb51d69c1b89e05e4bb512cd22265eef6e85c974f3cbeaf67304a5588`;
  PR #20 und Merge `fc5c8e991d7a7ba23ca6beb53e284f7ad0bb93d9`.
- **Beobachtung und Grenze / Observation and boundary:** Neun bestandene
  Command-Zeilen verweisen ausschliesslich auf `/tmp/*.txt`. Am
  Retrospektivtag existiert keine dieser Dateien mehr. PR-, Commit-, Aufgaben-
  und State-Evidence bleiben erhalten, aber die konkrete Ausgabe dieser neun
  lokalen Pruefungen ist nicht mehr direkt lesbar. / *Nine passing command rows
  point only to temporary files that no longer exist. Other immutable evidence
  remains, but those outputs are no longer directly inspectable.*
- **Projektausschluss / Project exclusion:** Die konkreten Temp-Pfade,
  META-LH-01-Kommandos und GitHub-PR-Nummern bleiben AOC-spezifisch.
- **Providerneutrale Zielregel / Provider-neutral target rule:** Vor
  `Completed` muss jede dauerhafte Pass-/Fail-Zeile auf einen Commit-Blob, ein
  hashgebundenes Repository-Artefakt oder ein dauerhaftes Provider-Artefakt
  zeigen. Temp-Pfade duerfen nur waehrend des aktiven Laufs oder als
  zusaetzliche lokale Referenz verwendet werden. / *Every durable result must
  bind a commit blob, hash-bound repository artifact, or durable provider
  artifact before completion.*
- **Berechtigungs- und Evidenzrisiko:** Ein spaeteres Audit darf fehlende
  Temp-Dateien nicht als bestanden rekonstruieren. Das Materialisieren von
  Logs muss Secrets, private Pfade und Aufbewahrungsfristen beachten.
- **Reproduzierbarer Test:** Eine temporaere Closeout-Fixture mit einer
  ausschliesslichen Temp-Referenz besteht waehrend die Datei existiert. Nach
  ihrer Loeschung muss die Durable-Reference-Pruefung scheitern. Dieselbe Zeile
  mit Commit-Blob plus SHA-256 muss bestehen.

## AR-003 - Logische Intake-Identitaet muss alle Validatoren erreichen / Logical Intake Identity Must Reach Every Validator

- **Unveraenderliche Quelle / Immutable source:** Lifecycle-Datensatz
  `703494f0ec7edb603653c61834e32fd2de2e8415:specs/001-programmquellen-baseline/intake-lifecycle.json`,
  Serienmanifest `703494f0ec7edb603653c61834e32fd2de2e8415:specs/intake-series/aoc-phase-2/manifest.json` und
  Governance-Konfiguration `703494f0ec7edb603653c61834e32fd2de2e8415:requirements/intake-governance.json`.
- **Beobachtung und Grenze / Observation and boundary:** Der Feature-Vertrag
  loest META-LH-01 nach dem bytegleichen Rename ueber die logische ID am
  Archivpfad auf. Die generischen Bash- und PowerShell-Governance-Oberflaechen
  lesen dagegen weiterhin den alten aktiven Pfad aus dem abgeschlossenen
  Manifest und blockieren beide mit `RIG014`. / *The feature contract resolves
  the archived target through logical identity, while both generic governance
  surfaces still require the former active path and fail with RIG014.*
- **Projektausschluss / Project exclusion:** META-LH-01, die 14er-Serie und der
  konkrete Archivsuffix sind AOC-spezifisch.
- **Providerneutrale Zielregel / Provider-neutral target rule:** Eine
  autorisierte Lifecycle-Transition muss Referenzen atomar aktualisieren oder
  allen Konsumenten eine hash- und lineagegebundene logische Aufloesung
  bereitstellen. Ein Terminalzustand darf weder beliebige Archive akzeptieren
  noch einen nachgewiesen migrierten Zielpfad als fehlend behandeln. / *A
  lifecycle transition must update references atomically or provide every
  consumer with hash- and lineage-bound logical resolution.*
- **Berechtigungs- und Evidenzrisiko:** Eine zu breite Archivsuche koennte
  supersedierte oder manipulierte Intakes reaktivieren. Nur eindeutige ID,
  Originalhash, Archivhash und Transitionsevidence duerfen bestehen.
- **Reproduzierbarer Test:** Ein temporaeres Projekt verschiebt ein
  bytegleiches Target mit gueltigem Lifecycle-Datensatz aus `active` in ein
  Archiv. Alle Authoring-, Review- und Sequencing-Oberflaechen muessen den
  terminalen Zustand akzeptieren; fehlender Datensatz, Hashdrift oder zwei
  moegliche Archive muessen fail-closed scheitern.

## AR-004 - Generierte Ledger koennen einen Closeout-Folgecommit erzwingen / Generated Ledgers Can Force a Closeout Follow-up Commit

- **Unveraenderliche Quelle / Immutable source:** Closeout-Commit
  `c773548c6cca752f61e73de4d77e1077347924d7` aenderte exakt drei Pfade; der
  unmittelbar folgende Commit `f682be5660eeee5e5247592e467683868413e08d`
  aenderte nur `docs/project-statistics.md`. Beide liegen in PR #20.
- **Beobachtung und Grenze / Observation and boundary:** Der Plan bezeichnete
  den kausalen Closeout als single-commit-faehig. Weil die Statistik aus der
  Git-Historie erzeugt wird, entstand nach diesem Commit neue Renderer-Drift
  und ein zweiter Commit. Dies ist zunaechst eine einzelne
  Ablauf-/Effizienzbeobachtung, kein Beleg fuer eine allgemeine Regel. / *The
  Git-derived statistics ledger required a second commit after the planned
  single-commit closeout. This is one workflow observation, not yet a general
  rule.*
- **Projektausschluss / Project exclusion:** Profil 2, Methodik v2 und der
  konkrete Renderer gehoeren zum AOC.
- **Providerneutrale Zielregel als Hypothese / Candidate rule:** Vor der
  Behauptung `single-commit-capable` alle generierten Writer pruefen, deren
  Quelle den Closeout-Commit selbst einschliesst; einen notwendigen
  Folgecommit explizit vorplanen oder die Nichtanwendbarkeit begruenden.
- **Berechtigungs- und Evidenzrisiko:** Ein unerwarteter Folgecommit aendert den
  reviewten Head und darf keine bestehende Approval- oder Exact-Head-Evidence
  erben.
- **Reproduzierbarer Test:** In einem temporaeren Git-Repository einen
  history-basierten Ledger rendern, einen Evidence-Closeout committen und
  `--check-only` wiederholen. Die Hypothese wird erst nach einer zweiten
  unabhaengigen Feldbeobachtung promotet.

## AR-005 - Der Transaktionsvalidator ist absichtlich phasengebunden / The Transaction Validator Is Intentionally Phase-Bound

- **Unveraenderliche Quelle / Immutable source:** Commit
  `c773548c6cca752f61e73de4d77e1077347924d7`, Pfade
  `contracts/validate_meta_lh01.py` und `causal-closeout-evidence.json`.
- **Beobachtung und Grenze / Observation and boundary:** `causal-closeout`
  besteht nur fuer das exakt gestagte Drei-Pfad-Delta. Auf sauberem `main` nach
  Abschluss scheitert der Modus erwartungsgemaess, waehrend beide terminalen
  State-Validatoren und alle 66 isolierten Vertragstests bestehen. / *The
  transaction validator intentionally fails without the exact staged delta;
  terminal state validation and all 66 contract tests still pass.*
- **Projektausschluss, Risiko und Test / Exclusion, risk, and test:** Dieser
  Modus ist eine AOC-spezifische Transaktionspruefung. Ihn als allgemeinen
  Statusvalidator zu verwenden, waere ein Phasenfehler. Positivfixture mit
  exakt drei gestagten Pfaden und Negativfixture auf sauberem `main` bleiben
  ausreichend.
- **Entscheidung / Decision:** `NoPromotion`; kein Defekt und keine neue
  portable Regel.

## Ergebnis / Outcome

- **Promotierte Regeln / Promoted rules:** `AR-001`, `AR-002`, `AR-003` als
  providerneutrale Korrektheits- beziehungsweise Evidence-Regeln fuer einen
  spaeter separat autorisierten Level-0-Handoff.
- **Offene Beobachtung / Pending observation:** `AR-004` benoetigt eine zweite
  unabhaengige Feldbeobachtung.
- **Nicht promotiert / Not promoted:** `AR-005`; der Fehler auf sauberem
  Terminalzustand ist die erwartete Transaktionsgrenze.
- **Lokale nichtleere Korrektur / Local non-empty correction:** diese
  Retrospektive sowie die zugehoerige AEPS-Ledger-, Matrix-, Gap-, Handoff- und
  Receipt-Evidence und das daraus neu gerenderte Projektstatistik-Ledger; keine
  akzeptierten Feature- oder Preset-Artefakte.
- **Portabler Handoff / Portable handoff:** `docs/aeps/upstream-handoff.md`,
  bis zu stabiler Publikation und neuer Authority nur `PendingPublication`.
- **Resume-State-Qualitaet / Resume-state quality:** `Valid`; beide
  State-Validatoren melden `Completed`, 66/66, `CausalCloseoutValidated` und
  `nextExactAction: N/A`.
- **Naechstes Feldgate / Next field gate:** Die drei Promote-Regeln in einem
  temporaeren zweiten Projekt mit positiven und negativen Fixtures pruefen;
  `AR-004` erst nach einer zweiten unabhaengigen Closeout-/Ledger-Beobachtung
  neu bewerten.

## Dokumentationsauswirkung / Documentation Impact

- **Entscheidung:** `UpdateRequired`.
- **Quelle und Owner / Source and owner:** terminale Lauf-Evidence und
  Retrospektivvertrag; AOC Requirements Maintainer und AEPS Evidence Owner.
- **Dokumente / Documents:** diese Retrospektive, AEPS Findings Ledger,
  Candidate-Matrix, Gap-Analyse, Upstream-Handoff, Retrospektiv-Receipt und das
  generierte Projektstatistik-Ledger.
- **Leserpfad / Reader path:** Ergebnis und Grenzen hier beginnen, danach die
  Finding-IDs im Ledger lesen und nur bei stabiler Publikation und neuer
  Authority dem Handoff folgen.
- **Sprache, A11Y und Distribution / Language, accessibility, and
  distribution:** Deutsch zuerst, Englisch danach, text-first und
  repository-lokal `sourceOnly`; keine Level-0- oder Home-Synchronisation.
- **Evidence und Re-Evaluation:** Commit- und PR-IDs, beide State-Validatoren,
  66 Vertragstests, die drei gezielten Negativproben und die dokumentierten
  Hashes. Neu bewerten bei Preset-Validatorfix, zweitem Projekt oder weiterer
  Closeout-Evidence.
