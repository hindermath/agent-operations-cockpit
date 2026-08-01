# Erneutes AOC-Phase-2-Serienreview / AOC Phase 2 Series Re-review

## Identität und Ergebnis / Identity and outcome

- Review-ID: `8d193d13-f8ca-4c5e-a3f9-e3f3da89cdcb`
- Modus: `Series`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `NeedsClarification`
- Review-Zeitpunkt: `2026-07-31T23:31:44Z`
- Repository-HEAD: `d81ca316f6a01599008363461dbf0060b497de29`
- Ziele: `14`; Worker: `0`
- Critical: `0`; High: `4`; Medium: `0`; Low: `0`
- Akzeptierte Risiken: `0`; offene Fragen: `3`
- Request: `specs/intake-review-requests/aoc-phase-2-series-2026-08-01-r2.json`
- Request-SHA-256: `07d90dc471b8b921f82f38cc771abf82e04c9fa296624e2226999361d2a93d95`
- Supersediertes Ergebnis: `specs/intake-review-results/aoc-phase-2-series.json`

*The complete 14-target Series was reviewed again after the authorised
META-LH-01 repair. The result is current but not accepted: one target needs a
repository-bound remediation and three targets still need human decisions.*

## Ergebnisänderung / Outcome change

Das frühere Serienreview war wegen des geänderten META-LH-01-Hashes veraltet.
Dieses Review bindet alle 14 aktuellen Ziel-Hashes und einen neuen
Schema-1.1-Request. Die vier High Findings bleiben stabil als `IR001` bis
`IR004`; nur `IR001` ändert seine Disposition:

- IAD201 bis IAD203 wurden von Thorsten im aktuellen Task jeweils mit Option A
  entschieden.
- Diese Entscheidungen sind noch nicht im RAW-02-Intake, dessen Authoring
  Receipt oder der Serien-Hashbindung festgehalten.
- RAW-02 benötigt deshalb keine weitere inhaltliche Klärung dieser drei Punkte,
  sondern ein ausdrücklich autorisiertes Intake-Update mit vollständigem
  Re-Review.

*The previous result was stale after the META-LH-01 hash change. This result
binds every current target and a new schema-1.1 request. IR001 now records
`NeedsRemediation`: the three choices are known in the task context but are not
yet durable repository evidence.*

## Für RAW-02 bestätigte Entscheidungen / Confirmed RAW-02 decisions

Die folgenden Entscheidungen sind Review-Kontext, noch kein aktualisierter
normativer Intake:

1. **IAD201 – IPC-/Prozessvertrag:** RAW-02 besitzt den logischen Vertrag für
   Aufruf, Antwort, Ereignisse, Abbruch und Lebenszyklus. Konkrete Process API
   und Transportwahl bleiben bei RAW-06. RAW-01 und RAW-03 müssen vor der
   nachgelagerten RAW-02-Ausführung aktuell reviewt sein.
2. **IAD202 – Session Context:** Flüchtige und persistente Daten werden
   getrennt; Versionierung, Wiederherstellung und Invalidierung sind
   ausdrücklich zu behandeln. Die State-Semantik bleibt bei RAW-03.
3. **IAD203 – Command Queue:** Reihenfolge, Deduplizierung, Wiederholung,
   Abbruch und der Umgang mit nicht-idempotenten Aktionen werden vertraglich
   festgelegt. Mutierende Commands bleiben bis nach dem Read-only-Slice
   gesperrt.

*These three choices are review context, not yet the updated normative intake.
An authorised update must preserve the ownership boundaries and fail-closed
command sequencing stated above.*

## Individuelle Coverage / Individual coverage

| Intake | Identität, Scope und Anforderungen | Security, A11Y und Plattform | Evidence, Authority und Prompts | Ergebnis |
|---|---|---|---|---|
| META-01 | erfüllt | erfüllt | aktuelles Einzelreview `Ready` | ReadyForReview |
| META-02 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| META-03 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| META-04 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| META-05 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| RAW-01 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| RAW-03 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| RAW-02 | erfüllt | erfüllt | IAD201–203 beschlossen, aber nicht repositorygebunden | NeedsRemediation |
| RAW-04 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| RAW-05 | erfüllt | erfüllt | `research-only` bleibt bindend | ReadyForReview |
| RAW-06 | erfüllt | erfüllt | blockiert durch IAD601–604 | NeedsClarification |
| RAW-07 | erfüllt | erfüllt | blockiert durch IAD701–704 | NeedsClarification |
| RAW-08 | erfüllt | erfüllt | erfüllt | ReadyForReview |
| RAW-09 | erfüllt | erfüllt | blockiert durch IAD901–902 und Promotion Authority | NeedsClarification |

„Erfüllt“ bestätigt die Qualität des Lastenhefts, nicht Produktimplementierung
oder Startautorität. / *“Satisfied” confirms intake quality, not product
implementation or start authority.*

## Findings / Findings

| ID | Severity | Owner | Aussage / Statement | Disposition und Re-Evaluation |
|---|---|---|---|---|
| IR001 | High | RAW-02 | IAD201–203 sind im Task entschieden, RAW-02 bezeichnet sie aber weiterhin als offen. | `NeedsRemediation`; nach autorisiertem Update, erneuertem Receipt und vollständigem Re-Review neu bewerten. |
| IR002 | High | RAW-06 | Process API, Exit-/Signalmodell, Environment Allowlist und Remote Transport sind offen. | `NeedsClarification` bis IAD601–604 repositorygebunden sind. |
| IR003 | High | RAW-07 | MIDI-Bibliothek, Elgato Transport, Geräteauswahl und Lab-Freigaben sind offen. | `NeedsClarification` bis IAD701–704 repositorygebunden sind. |
| IR004 | High | RAW-09 | Promotion Threshold, Zielrepository und separate Promotion Authority sind offen. | `NeedsClarification` bis IAD901–902 und der Authority-Vertrag vorliegen. |

## Serien- und Graphprüfung / Series and graph review

- Schema-2.0-Governance ist in Bash und PowerShell `Aligned`.
- Alle 14 aktiven Intakes kommen genau einmal in Request und Manifest vor.
- Alle Ziel-Hashes sind aktuell; `META-LH-01` ist der einzige deklarierte
  `Eligible`-Kandidat.
- Der Graph besitzt einen Root, 14 geordnete typisierte Kanten und keinen
  Zyklus.
- Die lesbare Reihenfolge und das Manifest stimmen pfad- und statusgenau
  überein.
- RAW-05 ist wegen der nicht bindenden `PreferredSerialOrder`-Kante zusätzlich
  strukturell startfähig, bleibt aber ausdrücklich `Pending` und
  `research-only`.
- Owner, Handoffs, Non-Ownership, DE/EN, CEFR B2, WCAG-Textstruktur,
  Security-/Privacy-Grenzen und Nicht-Autorität bleiben konsistent.
- Kein Prompt, Specify-, Implementierungs- oder autonomer Lauf wurde gestartet.

*Governance, order, hashes, roots, edges, ownership, handoffs, accessibility,
security, and authority boundaries are internally consistent. Structural
eligibility grants no execution or delivery authority.*

## Fragen, Risiken und Ausnahmen / Questions, risks, and exceptions

- Offene Fragen: `3` – IAD601–604, IAD701–704 sowie IAD901–902 einschließlich
  Promotion Authority.
- Akzeptierte Risiken: `0`.
- Operator-Ausnahmen: `0`.
- RAW-02 besitzt keine offene inhaltliche Frage zu IAD201–203 mehr; offen ist
  ausschließlich die autorisierte, nachvollziehbare Persistierung.

*Three decision groups remain open. No risk or operator exception was accepted.
RAW-02 needs persistence and re-review, not another decision round.*

## Exakte nächste Aktion / Exact next action

Die drei RAW-02-Entscheidungen werden dauerhaft durch ein ausdrücklich
autorisiertes, auf IAD201–203 begrenztes Update eingearbeitet:

```text
$speckit-intake-update requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md
Scope: ausschließlich die bestätigten Optionen A für IAD201, IAD202 und IAD203 einarbeiten; Vorgänger archivieren, Authoring Receipt und Serien-Hashbindung erneuern und anschließend RAW-02 vollständig neu reviewen. Keine Ausführung von Specify-, Implementierungs-, Remote-, Merge- oder Bypass-Aktionen.
```

*The exact next action is a separately authorised, bounded RAW-02 intake
update. This review does not itself authorise that mutation.*
