# Einzelreview RAW-08 – Workflow Engine / Single Review RAW-08 – Workflow Engine

## Identität und Ergebnis / Identity and outcome

- Review-ID: `fbcfda58-7c07-417b-9eb9-6167fbd78dc7`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `Ready`
- Review-Zeitpunkt / Review time: `2026-08-08T15:40:05Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `e9c39efd55e9ca5646eaf0c6e52b4bcf8d50b3ead10ea494b0499594251d1f55`
- Git-Blob: `8846e23fc8473c3e104a26a8880e8c3edc3582ca`
- Request:
  `specs/intake-review-requests/raw-08-workflow-engine-2026-08-08-r2.json`
- Request-SHA-256:
  `4750836f88361e039969d0dce940359ec0c50118e0caa5fcbfa828e5ee84cbb6`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review:
  `specs/intake-review-results/raw-08-workflow-engine-2026-08-08.json`

Das vollständige Ersatzreview bewertet ausschließlich das erneuerte RAW-08
und seine offline prüfbare Requirements-Evidence. Es verändert weder
IAD801–IAD803 noch Zweck, Scope, Non-Goals, Abhängigkeiten, Series-Lifecycle
oder Delivery Authority und startet keine Folgephase. / *This complete
replacement review assesses only the renewed RAW-08 intake and its offline
requirements evidence. It changes neither IAD801–IAD803 nor purpose, scope,
non-goals, dependencies, Series lifecycle, or delivery authority and starts no
downstream phase.*

## Ergebnis / Outcome

RAW-08 ist `Ready`. Der erneuerte, versionierte
`workflow-evidence-contract.json` bindet Artifact- und Evidence-Klassen,
deterministische Lifecycle-Übergänge, typisierte Handoffs, Authority-Gates,
Reason Codes und Cross-Cutting-Grenzen. Eine positive End-to-End-Fixture und
sieben negative Fixtures machen die Anforderungen auf Bash und PowerShell
reproduzierbar. / *RAW-08 is Ready. The renewed versioned workflow evidence
contract binds artifact and evidence classes, deterministic lifecycle
transitions, typed handoffs, authority gates, reason codes, and cross-cutting
boundaries. One positive end-to-end fixture and seven negative fixtures make
the requirements reproducible on Bash and PowerShell.*

IAD801 bleibt beim Receipt-last-JSON-Modell mit atomischem Replace und dem
letzten vollständig validierten, hashgebundenen Receipt als Recovery-Anker.
IAD802 bleibt beim versionierten detached Attestation Envelope und einer
separat versionierten Trust Policy. IAD803 bleibt bei Projektlebensdauer für
Governance-/Decision-/Completion-Receipts, 90 Tagen für operative Evidence und
zwölf Monaten für Security-/Failure-Evidence; Legal Hold setzt Löschung aus
und jede Löschung benötigt ein Receipt. / *IAD801–IAD803 retain exactly the
confirmed persistence, attestation, and retention decisions.*

## Auflösung der Findings / Finding resolution

| Finding | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| `IR802` | Erledigt / Resolved | Der Vertrag definiert Artifact- und Evidence-Klassen, Lifecycle-Zustände und -Übergänge, persistente Receipts, 14 stabile `WFE`-Codes sowie eine positive und sieben negative Fixtures mit Befehlen, Sollausgaben und Exitcodes. / *The contract and fixtures provide deterministic, runnable requirements evidence.* |
| `IR803` | Erledigt / Resolved | Alle normativen Abschnitte sind semantisch vollständig DE-first/EN-second; Begriffe für Artefakte, Evidence, Lifecycle, Attestation, Retention, Handoffs, Authority und Spec Kit werden lokal in CEFR-B2-Sprache erklärt. / *All normative sections are complete bilingual pairs with local first-use explanations.* |
| `IR804` | Erledigt / Resolved | Security, Datenminimierung, Public Content, WCAG 2.2 AA, Text-/Tastaturalternativen, macOS/Linux/Windows, Container-/Remote-Node-Provenienz und Supply Chain besitzen messbare Positiv-/Negativgrenzen sowie Re-Evaluation-Trigger. / *Cross-cutting applicability now has measurable boundaries and triggers.* |
| `IR805` | Erledigt / Resolved | RAW-05→RAW-08, RAW-06→RAW-08 und RAW-08→RAW-09 sowie vier Child-Boundaries binden Producer, Consumer, Version, Felder, Authority, Kompatibilität, Fehlerverhalten und Series-Relation. / *Every predecessor, successor, and child boundary is typed and versioned.* |
| `IR806` | Erledigt / Resolved | Beide kopierbaren Prompts und das erneuerte Receipt unterscheiden die historische `MergeAndSync`-Obergrenze von aktueller Authority und verlangen fail-closed alle acht aktuellen Authority-Gates. / *Prompts and receipt now fail closed on every current authority gate.* |

Das frühere `NeedsRemediation`-Ergebnis bleibt als unveränderliche historische
Negativ-Evidence erhalten und wird durch dieses Ergebnis ausdrücklich
supersediert. / *The earlier NeedsRemediation result remains immutable historic
negative evidence and is explicitly superseded by this result.*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass | Workflow-Governance und Knowledge-Package-Bildung bleiben von Produktzustand, Produktcommands, Implementierung, Presets und Promotion getrennt. / *Governance stays separated from excluded product work.* |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Pass | DE-first/EN-second, CEFR B2, lokale Begriffserklärungen und Text-first-Status sind vollständig. / *Language, readability, terminology, and text-first status are complete.* |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass | RAW-05/06 sind Completed, RAW-08 bleibt allein Eligible, RAW-09 bleibt Blocked, IAD801–IAD803 sind beantwortet und nur Statusprüfung ist die sichere Folgeaktion. / *Lifecycle, dependencies, decisions, and next action are explicit.* |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Elf funktionale und fünf nichtfunktionale Anforderungen binden deterministische Verträge, Übergänge, Handoffs, Failure-Verhalten und Authority. / *Requirements are deterministic and testable.* |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | Zehn Akzeptanzkriterien binden Vertrag, acht Fixtures, stabile Codes, Sollausgaben, Exitcodes und beide Shell-Oberflächen. / *Acceptance binds contract, fixtures, codes, output, exit codes, and both shells.* |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Pass | Drei typisierte Series-Handoffs, vier Child-Boundaries, Re-Evaluation-Trigger und acht fail-closed Authority-Gates sind vollständig. / *Handoffs, triggers, and authority gates are complete.* |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Pass | Datenschutz, Public Content, WCAG, Plattform-/Node-Parität und spätere Dependency-Evidence sind messbar und negativ geprüft. / *Cross-cutting concerns have measurable positive and negative evidence.* |
| Prompt-Ausrichtung / Prompt alignment | Pass | Kopierbare Prompts verlangen jede aktuelle Authority und erteilen durch `Ready`, `Eligible` oder historisches `MergeAndSync` keine Ausführungserlaubnis. / *Copy-ready prompts grant no authority from lifecycle or historical delivery state.* |
| Referenzen, Secrets, Personendaten, Encoding und Whitespace / References, secrets, personal data, encoding, and whitespace | Pass | Lokale Quellen sind auflösbar; Secrets und unnötige Personendaten sind verboten; JSON, UTF-8 und Whitespace-Prüfung bestehen. / *References and data boundaries pass.* |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, `18`
  gebundene Quellen. / *Both authoring validators pass with 18 bound sources.*
- Single Review: Bash und PowerShell `PASS`, Status `Ready`, ein aktuelles
  Ziel. / *Both review validators pass with one current target.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- RAW-08-Fixtures: die vollständige Source-to-Retrospective-Evidence und sieben
  erwartete Negativfälle bestehen auf Bash und PowerShell mit identischen
  Codes und Exitcode `0`. / *The end-to-end fixture and seven expected negative
  cases pass identically on both surfaces.*
- JSON-, Python- und Bash-Syntax sowie PSScriptAnalyzer bestehen. Die
  archivierten Vorgänger sind hashgebunden. / *Syntax, PowerShell analysis,
  and archived predecessor bindings pass.*
- Der begrenzte Secret-/Personendaten-Musterscan und `git diff --check` melden
  keinen Treffer. / *The bounded sensitive-data and whitespace checks report
  no finding.*

## Serien- und Authority-Auswirkung / Series and authority impact

Das Review ändert den Series-Lifecycle nicht. RAW-08 bleibt der einzige
deklarierte `Eligible`-Kandidat. `Ready` bestätigt ausschließlich die Qualität
des exakt hashgebundenen Lastenhefts und erteilt keine Scope-, Start-,
Implementierungs-, Governance-Write-, Remote-Write-, Merge-, Bypass-,
Provider-, Preset-, GitHub- oder Level-0-Autorität. / *The review does not
change Series lifecycle. RAW-08 remains the sole Eligible target. Ready grants
no downstream authority.*

Die AOC-weite Review-Sperre bleibt geschlossen: Dreizehn der vierzehn aktiven
Lastenhefte besitzen nun aktuelle formal validierte Ready-Evidence; RAW-09
fehlt noch. / *The AOC-wide review gate remains closed: thirteen of fourteen
active intakes now have current formally validated Ready evidence; RAW-09 is
still outstanding.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist die ausdrücklich autorisierte
Reparatur und das vollständige RAW-08-Ersatzreview; Owner ist `RAW-08 intake
repair and review`. Geändert oder neu sind Lastenheft, Requirements-Vertrag,
Fixtures, Authoring-/Series-Evidence, Review-Request, Review-Ergebnis und dieser
Bericht. Evidence sind die gebundenen Hashes und die aufgeführten
Validierungen. / *Decision: UpdateRequired. The authorised repair and complete
replacement review are the source; the listed artifacts and validations are
the evidence.*

## Exakte nächste Aktion / Exact next action

Der nächste sichere Spec-Kit-Befehl ist read-only: / *The next safe Spec Kit
command is read-only:*

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

Er validiert den neuen Ready-Nachweis im Serienkontext und startet keine
Folgeaktion. / *It validates the new Ready evidence in Series context and
starts no downstream action.*
