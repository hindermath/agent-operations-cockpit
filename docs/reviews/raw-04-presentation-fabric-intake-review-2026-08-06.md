# Einzelreview RAW-04 – Presentation Fabric / Single Review RAW-04 – Presentation Fabric

## Ergebnis / Outcome

- Review-ID: `8715f818-7fd0-4387-92e5-fdb4ae6f832e`
- Modus: `Single`; Ergebnis: `NeedsClarification`
- Ziel- und Worker-Anzahl: `1` / `0`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel: `requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md`
- Normalisierter Zielhash: `b796736d154deb4ff244cf301f3d07fe462f135d888a30906b2cdbf33da2035b`
- Request: `specs/intake-review-requests/raw-04-presentation-fabric-2026-08-06.json`
- Request-Hash: `0df596478414f4872cbbc229bbea2734973147995bbf7c7176723e069a882129`
- Findings: Critical `0`, High `5`, Medium `0`, Low `0`
- Offene Fragen: `3`; akzeptierte Risiken: `0`; Operator-Ausnahmen: `0`

*This read-only review found unresolved material decisions and five blocking
high findings. It starts no Specify, implementation, remote write, merge, or
bypass action.*

## Findings / Befunde

| ID | Severity | Kategorie / Category | Kurzbefund / Summary |
|---|---|---|---|
| IR401 | High | OpenDecisionAndProvenance | TUI/UI-Framework, Responsiveness und Lokalisierungsformat sind offen, obwohl der Receipt keine offenen Decisions ausweist. / Material decisions remain open while the Receipt records none. |
| IR402 | High | RequirementsEvidence | Presentation Contract, Fixtures, Validatoren, erwartete Ausgaben, Exitcodes und vollständige Handoffs sind nicht reproduzierbar gebunden. / Contract, fixtures, validators, expected outputs, exit codes, and handoffs are not reproducibly bound. |
| IR403 | High | LanguageAndTerminology | DE-first/EN-second, CEFR B2 und Erstbegriffserklärungen sind für Anforderungen, Decisions, Acceptance und Evidence unvollständig. / Bilingual readability and first-use terminology are incomplete. |
| IR404 | High | CrossCuttingApplicability | Security, Privacy, Supply Chain, Plattformparität und konkrete A11Y-Evidence sind nicht entschieden und nicht messbar gebunden. / Cross-cutting applicability and evidence are not explicit or measurable. |
| IR405 | High | PromptAndDeliveryAuthority | Der aktivierte Autonomous-Prompt fordert MergeAndSync; historische Receipt-Autorität und Eligibility ersetzen keine aktuelle Delivery Authority. / The enabled prompt requests MergeAndSync; historic authority and Eligibility are not current delivery authority. |

## Offene Klärungen / Open questions

1. Welches TUI/UI-Framework und welche frameworkneutrale Boundary gelten?
2. Welche Responsiveness- und Layout-Schwellen gelten für alle Surfaces?
3. Welches versionierte Lokalisierungsformat und welcher DE-first/EN-second-
   Fallback gelten?

*The three questions concern the framework boundary, responsiveness thresholds,
and the versioned localization/fallback contract.*

## Review-Coverage / Review coverage

Identität, Zielgruppe, Zweck, Scope und Non-Goals sind erkennbar. FR-001 bis
FR-004 und NFR-001/002 sind grundsätzlich atomar. Der Review blockiert dennoch,
weil Entscheidungen, messbare Evidence, Cross-Cutting-Anwendbarkeit,
Terminologie und Prompt-/Authority-Grenzen nicht vollständig geschlossen sind.

*Identity, audience, purpose, scope, non-goals, and basic requirement
atomicity are visible. The review blocks because decisions, measurable
evidence, cross-cutting applicability, terminology, and authority boundaries
are incomplete.*

Die Zuständigkeit bleibt bei RAW-04: Presentation Contract und Surface-
Projektion; keine Workspace-, State-, Command- oder Hardwareprotokollautorität.
RAW-03 liefert den State Envelope, RAW-07 konsumiert den Presentation Contract.
Die Serien-Lifecycle-Werte und der Zielhash wurden nicht verändert.

*RAW-04 owns the presentation contract and surface projection only; it does not
own workspace, state, command, or hardware protocol logic. RAW-03 provides the
State Envelope and RAW-07 consumes the Presentation Contract.*

## Validierung / Validation

- UTF-8-Zielprüfung, normalisierter Zielhash und Git-Blob: gebunden.
- Review-Ergebnis wird mit Bash und PowerShell validiert.
- Keine Review-, Specify-, Implementierungs-, Remote-, Merge- oder
  Bypass-Aktion wurde gestartet.

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle und Owner sind der RAW-04-Intake, das
Source Pack und der Findings Ledger. Die Evidence wird separat als Review-
Request, maschinenlesbares Ergebnis und lesbarer Bericht geführt.

*Decision: `UpdateRequired`. The review package is separate evidence and does
not modify the intake or product files.*

## Exakte nächste Aktion / Exact next action

```text
$speckit-intake-repair specs/intake-review-results/raw-04-presentation-fabric-2026-08-06.json
```

*Repair requires a separately scoped human authorization for the findings; the
review itself grants no mutation or delivery authority.*
