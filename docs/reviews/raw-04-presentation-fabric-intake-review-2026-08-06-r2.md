# Einzelreview RAW-04 – Presentation Fabric / Single Review RAW-04 – Presentation Fabric

## Identität und Ergebnis / Identity and outcome

- Review-ID: `3fd458f6-7d86-4961-a03d-05ae4bb89662`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `Ready`
- Review-Zeitpunkt / Review time: `2026-08-06T18:50:33Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `d3b4240276767a2cd67e86292ccc3b00f7d1aae32b583e081c0fc02751dcbc10`
- Git-Blob: `N/A` – das autorisierte Update ist noch nicht committet. / *The
  authorised update is not committed yet.*
- Request:
  `specs/intake-review-requests/raw-04-presentation-fabric-2026-08-06-r2.json`
- Request-SHA-256:
  `fdef90d592b1cd213917425814a76a122b7035e44cd7269812afafcf8760a239`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review:
  `specs/intake-review-results/raw-04-presentation-fabric-2026-08-06.json`

Das vollständige Re-Review bewertet ausschließlich das erneuerte RAW-04 und
seine gebundene Evidence. Es erweitert weder den fachlichen Scope noch die
Serie und startet keine Folgephase. / *This complete re-review assesses only
the renewed RAW-04 intake and its bound evidence. It expands neither the domain
scope nor the Series and starts no downstream phase.*

## Ergebnis / Outcome

RAW-04 ist `Ready`. Der Presentation Contract ist frameworkneutral; Console
und JSON sind kanonische Projektionen, während Spectre.Console ausschließlich
als Referenz-TUI-Adapter vorgesehen ist. Frameworktypen dürfen die
Vertragsgrenze nicht überschreiten. / *RAW-04 is Ready. The Presentation
Contract is framework neutral; Console and JSON are canonical projections,
while Spectre.Console is only the intended reference TUI adapter. Framework
types may not cross the contract boundary.*

Die Layoutprofile sind deterministisch: `Linear` unter 40, `Compact` von 40
bis 99 und `Enhanced` ab 100 Spalten. Fehlende Terminal-Interaktivität oder
Capability erzwingt `Linear`. Der JSON-Nachrichtenkatalog verlangt Schema 1,
stabile Message IDs sowie vollständiges `de` und `en` in deutscher und danach
englischer Reihenfolge. / *Layout profiles are deterministic: Linear below
40, Compact from 40 through 99, and Enhanced from 100 columns. Missing terminal
interactivity or capability forces Linear. The JSON message catalog requires
schema 1, stable message IDs, and complete de and en content in German-first
and English-second order.*

`IAD401`, `IAD402` und `IAD403` beantworten `IRQ401` bis `IRQ403` und
supersedieren `DEC-T04` im owner-spezifischen Target, Authoring Receipt und
maschinenlesbaren Presentation Contract ohne offenen Rest. Die allgemeinen
Portfolio-Unterlagen bleiben unveränderte Eingangsquellen; der neuere
owner-spezifische Vertrag ist die präzisierende Evidence für RAW-04. /
*IAD401, IAD402, and IAD403 answer IRQ401 through IRQ403 and supersede DEC-T04
without an open remainder in the owner-specific target, Authoring Receipt, and
machine-readable Presentation Contract. General portfolio documents remain
unchanged input sources; the newer owner-specific contract is the refining
evidence for RAW-04.*

## Auflösung der früheren Findings / Resolution of prior findings

| Finding | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| IR401 | Erledigt / Resolved | `IAD401` bis `IAD403`, Target, Presentation Contract und erneuertes Authoring Receipt stimmen überein; null offene Fragen. / Decisions, target, contract, and receipt agree with zero open questions. |
| IR402 | Erledigt / Resolved | Versionierter Vertrag, typisierte Handoffs, Validatoren, positive und negative Fixtures, Befehle, Sollausgaben, Exitcodes und Plattformgrenze sind gebunden. / The versioned contract, typed handoffs, validators, fixtures, commands, expected outputs, exit codes, and platform boundary are bound. |
| IR403 | Erledigt / Resolved | Alle normativen Abschnitte sind DE-first/EN-second; zentrale Begriffe, Lifecycle, nächste Aktion und Authority-Trennung sind lokal erklärt. / Normative sections are bilingual and terminology, lifecycle, next action, and authority separation are explicit. |
| IR404 | Erledigt / Resolved | Security, Privacy, Public Content, WCAG 2.2 AA, Plattformparität und Supply Chain besitzen prüfbare Grenzen und Re-Evaluation-Trigger. / Cross-cutting concerns have testable boundaries and reassessment triggers. |
| IR405 | Erledigt / Resolved | Prompts und Receipt erklären fail-closed, dass Eligibility, Ready und historische Delivery-Daten keine aktuelle Start-, Implementierungs-, Remote-, Merge- oder Bypass-Autorität erteilen. / Prompts and receipt fail closed on current authority. |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass | Presentation Ownership ist klar von State, Orchestration, Discovery, Commands und Hardware getrennt. / Presentation ownership is separated from state, orchestration, discovery, commands, and hardware. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Pass | DE-first/EN-second, CEFR B2 und Erstgebrauchserklärungen sind vollständig. / German-first/English-second, CEFR B2, and first-use explanations are complete. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass | RAW-03 ist bindender Vorgänger, RAW-04 allein Eligible, DEC-T04 supersediert und die Authority-Trennung ausdrücklich. / Lifecycle, dependency, decision state, and authority separation are explicit. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Frameworkgrenze, Layout, Lokalisierung, Fallback, Status, Fokus und State-Grenze sind deterministisch. / Framework boundary, layout, localization, fallback, status, focus, and state boundary are deterministic. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | Acht Akzeptanzkriterien binden Vertrag, fünf Fixtures, stabile Fehlercodes und beide Shell-Oberflächen. / Eight acceptance criteria bind the contract, five fixtures, stable error codes, and both shell surfaces. |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Pass | Producer, Consumer, Version, Authority und Failure Behavior sind gebunden; Revision und Delivery bleiben fail-closed. / Typed handoffs, revision triggers, and delivery boundaries are explicit and fail closed. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Pass | Anwendbarkeit, messbare Grenzen und Re-Evaluation sind vollständig. / Applicability, measurable boundaries, and reassessment are complete. |
| Prompt- und Projektionsparität / Prompt and projection parity | Pass | Prompts überschreiten keine aktuelle Autorität; Console-/JSON-Parität und negative Abweichung `PR009` sind reproduzierbar. / Prompts do not exceed current authority; Console/JSON parity and negative mismatch PR009 are reproducible. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass | Datenminimierung ist normativ; strict UTF-8, JSON-Syntax und `git diff --check` bestehen. / Data minimisation is normative; strict UTF-8, JSON syntax, and diff checks pass. |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, `11`
  gebundene Quellen. / *Both authoring validators pass with 11 bound sources.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- RAW-04-Fixtures: Layout-, Status-, Übersetzungs-, Fokus- und
  Console-/JSON-Parität bestehen auf Bash und PowerShell. Die vier negativen
  Fixtures werden erwartungsgemäß mit `PR007`, `PR008`, `PR009` und `PR010`
  abgelehnt. / *Positive evidence and all four expected rejection cases pass
  through Bash and PowerShell.*
- Der Vertrag prüft die Referenzbreiten `39`, `79` und `120`, erzwungenes
  lineares Layout ohne interaktive Capability sowie sichtbares
  `SURFACE_UNAVAILABLE`. / *The contract tests widths 39, 79, and 120, forced
  linear layout without interactive capability, and visible surface failure.*
- JSON-Syntax, Python-Kompilierung, Bash-Syntax, strict UTF-8 und
  `git diff --check` bestehen. / *JSON, Python, Bash, encoding, and whitespace
  checks pass.*

## Serien- und Authority-Auswirkung / Series and authority impact

Das Review ändert den Series-Lifecycle nicht. RAW-04 bleibt der einzige
deklarierte `Eligible`-Kandidat. `Ready` bestätigt nur die Qualität des exakt
hashgebundenen Lastenhefts; es setzt RAW-04 nicht auf `Completed` und erteilt
keine Start-, Specify-, Implementierungs-, Remote-, Merge-, Bypass-, Provider-,
Preset- oder Level-0-Autorität. / *The review does not change Series lifecycle.
RAW-04 remains the sole declared Eligible candidate. Ready confirms only the
quality of the exact hash-bound intake and grants no downstream authority.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich autorisierte
vollständige RAW-04-Re-Review; Owner ist `RAW-04 intake review`. Neu sind der
Re-Review-Request, das maschinenlesbare Ergebnis und dieser Bericht. Evidence
sind die gebundenen Target-/Request-Hashes und die oben aufgeführten
Validierungen. / *Decision: UpdateRequired. The authorised full RAW-04
re-review is the source and RAW-04 intake review is the owner. The new request,
machine-readable result, and this report are backed by the bound hashes and
listed validation evidence.*

## Exakte nächste Aktion / Exact next action

Der nächste sichere Spec-Kit-Befehl ist read-only: / *The next safe Spec Kit
command is read-only:*

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

Er validiert den neuen Ready-Nachweis im Serienkontext und startet keine
Folgeaktion. / *It validates the new Ready evidence in Series context and
starts no downstream action.*
