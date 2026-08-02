<!-- intake-authoring:begin -->
# RAW-03 – Zustandswahrheit / State Truthfulness

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** grundlegende Zustandsmodelle / basic state models
**Profile:** `aoc-bilingual-requirements`

## Zweck und Systemgrenze / Purpose and boundary

Alle Oberflächen benötigen dieselbe belegbare Wahrheit zu Wert, Quelle,
Authority, Freshness und Unsicherheit. Die Reihe besitzt diese Semantik, aber
nicht Discovery, UI oder Orchestration. / *All surfaces need the same provable
truth about value, source, authority, freshness, and uncertainty. This series
owns that semantics, not discovery, UI, or orchestration.*

## Quellen, Findings, Inputs und Outputs / Sources, findings, inputs, and outputs

SRC-172, 180, 181; RF-06, RF-10. Input: RAW-01 Snapshot und Node Evidence.
Output: `StateEnvelope` an RAW-02/04 mit Status `Known`, `Unknown`, `Stale`,
`Unavailable` oder `Degraded`.

## Anforderungen / Requirements

- **FR-001:** Jeder Zustand MUSS Wert/Abwesenheit, Quelle, observed-at,
  freshness-as-of, Authority und Reason Code enthalten.
- **FR-002:** `Unknown` DARF nicht als leerer Normalwert projiziert werden.
- **FR-003:** Konfliktquellen MÜSSEN sichtbar bleiben; kein stilles Last-Writer-Wins.
- **FR-004:** Text, JSON und spätere TUI MÜSSEN semantisch äquivalent sein.
- **NFR-001:** Zeit-, Locale- und Zeitzonenbehandlung ist deterministisch.
- **NFR-002:** Status bleibt für Screenreader und ohne Farbe verständlich.

## Decisions, Dependencies und Mode / Decisions, dependencies, and mode

Offen: Zeitquelle, Freshness-Schwellen und Confidence-Modell. Abhängig von
RAW-01; Handoff vor RAW-02/04. Modus `serial-autonomous` nach Decisions; keine
parallele Änderung des State-Schemas.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

State Envelope; Freshness Policy; Authority Projection; Projection Parity.
**AC-001:** Fixtures für alle fünf Status liefern erwartete Reason Codes.
**AC-002:** JSON/Text-Parität ist feldweise prüfbar.
**AC-003:** Zukunftszeit, fehlende Quelle und widersprüchliche Authority blockieren `Known`.

Positive Evidence: stabile Snapshot-Fixtures. Negative Evidence: Clock Skew,
Quelle fehlt, stale und unavailable. Revision bei State-/Zeitvertrag. Keine
Discovery-, UI- oder Command-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
