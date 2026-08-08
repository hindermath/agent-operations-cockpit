<!-- intake-authoring:begin -->
# RAW-09 – Preset Evolution / Preset Evolution

**Status:** NeedsClarification
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Governance- und Testgrundlagen / governance and testing basics
**Profile:** `aoc-bilingual-requirements`

## Zweck und Grenze / Purpose and boundary

Wiederholbare, generalisierbare AOC-Evidence kann als Preset-Verbesserung
vorgeschlagen werden. Diese Reihe besitzt Analyse und Proposal Evidence, aber
keine Authority zur Änderung oder Promotion eines Presets. / *Repeatable,
generalisable AOC evidence may become a preset improvement proposal. This
series owns analysis and proposal evidence, not preset modification or promotion.*

## Quellen, Findings und Handoffs / Sources, findings, and handoffs

SRC-168, 170, 174; RF-16, RF-19 bis RF-21. Input: RAW-08 Knowledge Packages,
Field Evidence und Retrospektiven. Output: de-identifiziertes Preset Proposal
mit Applicability, Nutzen, Risiken, Tests und Rückwärtskompatibilität.

## Anforderungen / Requirements

- **FR-001:** Proposal MUSS mindestens zwei unabhängige oder eine begründete
  systemische Evidence-Quelle besitzen.
- **FR-002:** Projektspezifische Produktentscheidung DARF nicht als Preset-Regel verallgemeinert werden.
- **FR-003:** Proposal MUSS Versionierung, Migration, Tests, A11Y, Security und Rollback behandeln.
- **FR-004:** ProviderFailure und Tooling-Gap werden getrennt von Produktfehlern bewertet.
- **NFR-001:** Evidence wird de-identifiziert und enthält keine privaten Pfade/Registry-Daten.

## Decisions, Mode und Recovery / Decisions, mode, and recovery

Offen: **IAD901** Promotion Threshold und **IAD902** Zielrepository je Proposal. Modus
`research-only`; separate menschliche Authority ist für jede Promotion nötig.
Recovery verwirft keine Evidence, sondern markiert Proposal `Deferred` oder
`RejectedWithRationale`.

## Child-Intakes, Akzeptanz und Evidence / Child intakes, acceptance, and evidence

Gap Detection; Generalisation Review; Proposal Package; Field Validation.
**AC-001:** projektspezifische und generalisierbare Befunde sind trennbar.
**AC-002:** Proposal ohne ausreichende Evidence oder mit privatem Datum wird blockiert.

Revision bei Preset-Flotte oder Evidence-Vertrag. Keine Produkt-, Preset-Write-
oder Promotion-Autorität.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
BLOCKED - DO NOT RUN: IAD901 and IAD902 require human decisions.
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
BLOCKED - DO NOT RUN: IAD901, IAD902, and separate preset-promotion authority are required.
```
<!-- intake-authoring:end -->
