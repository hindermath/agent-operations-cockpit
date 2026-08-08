# Einzelreview RAW-06 – CLI und Environment / Single Review RAW-06 – CLI and Environment

## Identität und Ergebnis / Identity and outcome

- Review-ID: `bcf426d0-4b2b-4add-86e6-ff6bf3f1dfbe`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `Ready`
- Review-Zeitpunkt / Review time: `2026-08-07T19:27:23Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `957e8c5a6607f900d88d4e854eee3373410142735e4b8b8eb893c9e0a65bf3fb`
- Git-Blob: `N/A` – das autorisierte Update ist noch nicht committet. / *The
  authorised update is not committed yet.*
- Request:
  `specs/intake-review-requests/raw-06-cli-environment-orchestration-2026-08-07.json`
- Request-SHA-256:
  `92b848242de485465976fc26fa471eec2d2caa67ed32d45d53f32662214181e1`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review: `N/A`

Das vollständige Single Review bewertet ausschließlich das erneuerte RAW-06
und seine gebundene Requirements-Evidence. Es erweitert weder Scope noch
Serie und startet keine Folgephase. / *This complete Single review assesses
only the renewed RAW-06 intake and its bound requirements evidence. It expands
neither scope nor the Series and starts no downstream phase.*

## Ergebnis / Outcome

RAW-06 ist `Ready`. `IAD601` bis `IAD604` sind im Lastenheft, im
maschinenlesbaren CLI-Capability-Vertrag und im Authoring Receipt konsistent
als beantwortet gebunden. Die Process API ist typisiert und shell-frei;
Executable und Argumentarray bleiben getrennt. / *RAW-06 is Ready. IAD601
through IAD604 are consistently bound as answered in the intake, the
machine-readable CLI capability contract, and the Authoring Receipt. The
Process API is typed and shell-free, with separate executable and argument
array.*

Das normalisierte Ergebnis unterscheidet Erfolg, Nonzero Exit, Startfehler,
Timeout, Abbruch, Signal und fehlendes Werkzeug. Native Exit- und Signaldetails
sowie Teilausgabe bleiben erhalten. Automatischer Retry für unbekannte oder
nicht-idempotente Aktionen und implizite Prozessbaum-Terminierung sind
ausgeschlossen. / *The normalised outcome distinguishes success, non-zero
exit, start failure, timeout, cancellation, signal, and missing tool. Native
details and partial output are retained. Automatic retry for unknown or
non-idempotent actions and implicit process-tree termination are excluded.*

Die Environment-Policy ist je Capability und Node versioniert und fail-closed;
das Eltern-Environment wird nicht pauschal vererbt. Secrets sind nur als opake
Referenzen zulässig. Der Remote-Vertrag bleibt transportneutral; SSHv2 ist nur
ein optionaler, standardmäßig deaktivierter Referenzadapter. Seine spätere
Aktivierung benötigt ein separates Review und aktuelle Authority. / *The
environment policy is versioned per capability and node and fails closed; the
parent environment is not inherited by default. Secrets are opaque references
only. The remote contract stays transport neutral; SSHv2 is only an optional,
disabled-by-default reference adapter. Later activation requires a separate
review and current authority.*

## Auflösung des früheren Serien-Findings / Resolution of the earlier Series finding

| Finding | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| `IR002` aus dem Phase-2-Serienreview | Erledigt für RAW-06 / Resolved for RAW-06 | IAD601–IAD604, Target, CLI-Capability-Vertrag und Receipt stimmen überein; null offene Fragen. / Decisions, target, contract, and receipt agree with zero open questions. |

Das historische Series Review wird durch dieses Single Review nicht
überschrieben. Seine damalige Negativ-Evidence bleibt unverändert; wegen des
neuen RAW-06- und Manifest-Hashes ist es nicht aktuell und benötigt bei einem
später autorisierten Serienreview eine neue Bewertung. / *This Single review
does not overwrite the historic Series review. Its negative evidence remains
immutable; the new RAW-06 and manifest hashes make it non-current until a
separately authorised Series review reassesses it.*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass | Prozess-, Environment- und optionaler Adaptervertrag sind von UI, Hardware, Produktcommand-Policy, Credential-Speicherung, Implementierung, Presets und Level 0 getrennt. / Process, environment, and optional adapter contracts are separated from excluded concerns. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Pass | DE-first/EN-second, CEFR B2 und Erklärungen für Capability, Process API, Shell-Evaluation, Allowlist, native Details, Teilausgabe, Remote-Endpunkt und Authority sind vorhanden. / Language and terminology are complete. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass | RAW-05 ist Completed, RAW-06 bleibt Blocked, IAD601–IAD604 sind beantwortet und nur das Review ist als aktuelle Folgeaktion autorisiert. / Lifecycle, dependencies, decisions, and authority are explicit. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Descriptor, Anfrage, Ergebnis, Output, Cancellation, Retry, Environment, Secrets, Capability-Klassen, Remote- und SSH-Grenzen sind deterministisch. / The contracts are deterministic and testable. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | Acht Kriterien binden Vertrag, sechs Fixtures, stabile `CLI`-Codes, Sollausgaben, Exitcode und beide Shell-Oberflächen. / Eight criteria bind the contract, six fixtures, stable codes, expected output, exit code, and both shell surfaces. |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Pass | Drei typisierte Handoffs, Re-Evaluation-Trigger und fail-closed Authority-Grenzen sind vollständig. / Typed handoffs, reassessment triggers, and authority boundaries are complete. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Pass | Shell-/Environment-Injection, Secrets, De-Identifizierung, DE/EN-Textalternativen, macOS/Linux/Windows-Parität und spätere Dependency-Evidence sind prüfbar. / Cross-cutting concerns have testable boundaries. |
| Prompt-Ausrichtung / Prompt alignment | Pass | Kopierbare Prompts erteilen keine aktuelle Process-, SSH-, Remote-, Specify-, Implementierungs-, Merge-, Bypass-, Provider-, Preset- oder Level-0-Autorität. / Copy-ready prompts grant no current downstream authority. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass | Opake Secret-Referenzen und logische Pfade sind normativ; UTF-8, JSON und `git diff --check` bestehen. / Secret references, logical paths, UTF-8, JSON, and whitespace checks pass. |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, `16`
  gebundene Quellen. / *Both authoring validators pass with 16 bound sources.*
- Single Review: Bash und PowerShell `PASS`, Status `Ready`, ein aktuelles
  Ziel. / *Both review validators pass with one current target.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- RAW-06-Fixtures: eine positive Read-only-Capability sowie fünf erwartete
  Ablehnungen für Shell-Evaluation, Environment-Injection, Remote-Aktivierung,
  Secret-Material und nicht-idempotenten Retry bestehen auf Bash und
  PowerShell mit identischen Codes und Exitcode `0`. / *The positive fixture
  and five expected rejection fixtures pass identically on both surfaces.*
- JSON-, Python-, Bash- und PowerShell-Syntax sowie PSScriptAnalyzer bestehen;
  die archivierten Vorgängerhashes sind unverändert gebunden. / *Syntax,
  PowerShell analysis, and archived predecessor hashes pass.*
- Der begrenzte Secret-Musterscan und `git diff --check` melden keinen Treffer.
  / *The bounded secret-pattern and whitespace checks report no finding.*

## Serien- und Authority-Auswirkung / Series and authority impact

Das Review ändert den Series-Lifecycle nicht. RAW-06 bleibt `Blocked`; es gibt
weiterhin keinen `Eligible`-Kandidaten. `Ready` bestätigt nur die Qualität des
exakt hashgebundenen Lastenhefts und erteilt keine Start-, Process-, Hardware-,
SSH-, Remote-, Specify-, Implementierungs-, Merge-, Bypass-, Provider-,
Preset-, GitHub- oder Level-0-Autorität. / *The review does not change Series
lifecycle. RAW-06 remains Blocked and no target is Eligible. Ready confirms
only the quality of the exact hash-bound intake and grants no downstream
authority.*

Die AOC-weite Review-Sperre bleibt geschlossen: Elf der vierzehn aktiven
Lastenhefte besitzen nun aktuelle formal validierte Ready-Evidence; RAW-07,
RAW-08 und RAW-09 fehlen noch. / *The AOC-wide review gate remains closed:
eleven of fourteen active intakes now have current, formally validated Ready
evidence; RAW-07, RAW-08, and RAW-09 remain outstanding.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich autorisierte
vollständige RAW-06-Single-Review; Owner ist `RAW-06 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Evidence sind
die gebundenen Target-/Request-Hashes und die aufgeführten Validierungen. /
*Decision: UpdateRequired. The authorised full RAW-06 Single review is the
source and RAW-06 intake review is the owner. The request, machine-readable
result, and this report are backed by the listed hashes and validation.*

## Exakte nächste Aktion / Exact next action

Der nächste sichere Spec-Kit-Befehl ist read-only: / *The next safe Spec Kit
command is read-only:*

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

Er validiert den neuen Ready-Nachweis im Serienkontext und startet keine
Folgeaktion. / *It validates the new Ready evidence in Series context and
starts no downstream action.*
