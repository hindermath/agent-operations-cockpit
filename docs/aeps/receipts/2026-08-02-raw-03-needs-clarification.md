# AEPS-Erfassungsreceipt RAW-03 NeedsClarification / AEPS Capture Receipt RAW-03 NeedsClarification

## Identität und Ergebnis / Identity and outcome

- Receipt-ID: `AEPS-RECEIPT-AOC-2026-08-02-006`
- Datum / Date: `2026-08-02`
- Trigger: materielles RAW-03-Single-Review / *material RAW-03 Single review*
- Review-ID: `1159da03-43fd-41ae-9876-f3df2633af12`
- Review-Status: `NeedsClarification`
- Repository-Base-HEAD: `60706c5dc6d96996fd7b4b4780c0b736a643dbb0`
- Ergebnis / Outcome: `NewLocalNegativeEvidence`
- Upstream-Status: `PendingPublication`

Das Review enthält drei offene Fachfragen und sechs High Findings. IR302 bis
IR306 bestätigen vorhandene AOC-Muster. IR301 liefert neue reproduzierbare
Negativ-Evidence für den Authoring-Receipt-Vertrag: Ein hash- und schemagültiges
Receipt kann offene Target-Decisions fälschlich als leer ausweisen. Diese
Beobachtung wird als `AEPS-FIND-AOC-015` erfasst. / *The review contains three
open domain questions and six High findings. IR302 through IR306 confirm
existing AOC patterns. IR301 adds reproducible negative evidence for the
authoring Receipt contract: a hash-current and schema-valid Receipt can
incorrectly represent open target decisions as empty. AEPS-FIND-AOC-015
records the observation.*

## Deduplizierung und Coverage / Deduplication and coverage

| RAW-03-Evidence | Bereits abgedeckt durch / Already covered by |
|---|---|
| IR301 – offene `DEC-T03` und widersprüchliche Receipt-Felder | neue lokale Negativ-Evidence: `AEPS-FIND-AOC-015`; Bezug zu `CAND-AEPS-06` und `CAND-AEPS-08` |
| IR302 – nicht gebundener Node-Evidence-Handoff | `AEPS-FIND-AOC-008` und der vorhandene Single-Ownership-/DAG-Vertrag |
| IR303 – unvollständige DE/EN- und Erstbegriffserklärung | `CAND-AEPS-11`, `AEPS-FIND-AOC-010` |
| IR304 – nicht reproduzierbare Vertrags- und Fixture-Evidence | `CAND-AEPS-02`, `CAND-AEPS-08`, `AEPS-FIND-AOC-009` |
| IR305 – unvollständige Querschnittsanwendbarkeit | `CAND-AEPS-10`, `CAND-AEPS-11`, `AEPS-FIND-AOC-006` |
| IR306 – historische Delivery-Daten als scheinbare aktuelle Authority | `CAND-AEPS-07`, `AEPS-FIND-AOC-003`, `AEPS-FIND-AOC-011` |

`AEPS-FIND-AOC-010` beschreibt bereits die allgemeine Grenze von Schema- und
semantischem Sprach-/A11Y-Review. IR301 präzisiert jedoch eine andere
maschinenrelevante Parität: Receipt-Decision-Metadaten müssen der Semantik des
hashgebundenen Targets entsprechen. Diese engere Lücke erhält deshalb eine
eigene Finding-ID und `AEPS-GAP-AOC-010`. / *AEPS-FIND-AOC-010 already covers
the general boundary between schema validation and semantic language or
accessibility review. IR301 identifies a distinct machine-relevant parity:
Receipt decision metadata must match the semantics of its hash-bound target.
The narrower gap therefore receives its own finding and gap IDs.*

## Gebundene Quellen / Bound sources

| Quelle / Source | Normalisierter SHA-256 / Normalised SHA-256 |
|---|---|
| `specs/intake-authoring-archive/af8d8b59-d146-44b0-8bf5-a63966865d4a/78672bee-803e-4f4d-848d-6448946d3c48/Lastenheft_RAW-03-State-Truthfulness.md` | `6886c5cc5243f033620e82895c601d78d4309108c8f364b81900598a2f563eae` |
| `specs/intake-review-results/raw-03-state-truthfulness-2026-08-02.json` | `10c1b13052d919f6d3d612135dbba359e0296f85a0985636df41d7c65aaf4931` |
| `docs/reviews/raw-03-state-truthfulness-intake-review-2026-08-02.md` | `9578d0c2439602357184eebcba498748fce2dcc0016092284575b3e7df8bc590` |
| `docs/aeps/findings-ledger.md` | `ea013c5b452e99a4b97727104385d9a59a17bba727d656bda1b04db3de896ffe` |
| `docs/aeps/finding-to-preset-candidate-matrix.md` | `4755e1731a4e9baf8b83c93325d1617b146746b951c027b11e359adb07fd5dbf` |
| `docs/aeps/preset-gap-analysis.md` | `acf3c5a87e0bfcfe60fb5ff7fdacf3cad29a6f35928ae9216f03c9d2194356c6` |
| `docs/aeps/upstream-handoff.md` | `de459342122f3d41be4cf5a5d6d5ce02ba26dbaa63fcfb3cdaebc7cfccf0bb9b` |

Der archivierte Target-Pfad ist die unveränderliche Vorgänger-Evidence. Die
vier AEPS-Analysepfade sind lebende Ledgers; ihre hier genannten Hashes binden
den Stand dieses Receipts, spätere Receipts binden ihre Fortschreibung. /
*The archived target is immutable predecessor evidence. The four AEPS analysis
paths are living ledgers; these hashes bind this Receipt's point-in-time state,
and later Receipts bind subsequent revisions.*

Für das nicht erfolgreiche Review gilt als Deduplizierungsschlüssel der
Ergebnis-Pfad, sein normalisierter Hash und das Datum. Die neuen Review- und
Receipt-Artefakte bleiben bis zu einer späteren autorisierten Veröffentlichung
`PendingPublication`; dieses Receipt startet keine Veröffentlichung. / *For
the non-Ready review, the result path, normalised result hash, and date form
the deduplication key. The new review and Receipt artifacts remain pending
publication until separately authorised publication; this Receipt starts no
publication.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist die durch das materielle
RAW-03-Review ausgelöste AEPS-Pflichtprüfung; Owner ist der
AOC-AEPS-Evidence-Workstream. Aktualisiert wurden Ledger, Candidate-Matrix,
Gap-Analyse, Handoff-Empfehlung und dieses Receipt. Evidence sind die
gebundenen Review-Artefakte, die bestandenen Validatoren und der semantische
Abgleich von Target und Receipt. / *Decision: UpdateRequired. The mandatory
assessment triggered by the material RAW-03 review is the source and the AOC
AEPS evidence workstream is the owner. The ledger, candidate matrix, gap
analysis, handoff recommendation, and this Receipt are updated.*

## Grenzen und Nicht-Autorität / Boundaries and non-authority

- Kein formal validiertes `Ready`; deshalb keine Ready-Capture oder
  Reifegradänderung. / *No formally validated Ready outcome; no Ready capture
  or maturity change.*
- Keine positive State-Runtime- oder Cross-Project-Evidence. / *No positive
  State runtime or cross-project evidence.*
- Keine Validatoränderung; `AEPS-FIND-AOC-015` bleibt `observation` und
  `PotentialCandidate`. / *No validator change; AEPS-FIND-AOC-015 remains an
  observation and PotentialCandidate.*
- Keine Änderung oder Promotion von Presets und keine Level-0-, GitHub-,
  Produkt-, Specify-, Implementierungs-, Remote-, Merge- oder Bypass-Aktion. /
  *No preset, Level-0, GitHub, product, delivery, merge, or bypass action.*

Die nächste AEPS-Prüfung erfolgt nach einem späteren vollständigen
RAW-03-Re-Review oder nach anderer materieller Evidence. / *The next AEPS
assessment follows a later complete RAW-03 re-review or other material
evidence.*
