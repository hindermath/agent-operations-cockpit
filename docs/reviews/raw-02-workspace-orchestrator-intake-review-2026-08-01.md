# Einzelreview RAW-02 – Workspace Orchestrator / Single Review RAW-02 – Workspace Orchestrator

## Identität und Ergebnis / Identity and outcome

- Review-ID: `1207c518-c097-44b9-92e8-33786181be2b`
- Modus: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `NeedsRemediation`
- Review-Zeitpunkt: `2026-07-31T23:53:59Z`
- Repository-HEAD: `d81ca316f6a01599008363461dbf0060b497de29`
- Ziel: `requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md`
- Normalisierter SHA-256: `75d6dd94d4e5b97de0ef43c62a0dd2ad7f68826665feca71e48610ae1eef523c`
- Request: `specs/intake-review-requests/raw-02-workspace-orchestrator-2026-08-01.json`
- Request-SHA-256: `dbe4067361c3ebc47efa02282d88d00ab835ec30f21014a19e6759ce7c659377`
- Ziele: `1`; Worker: `0`
- Critical: `0`; High: `2`; Medium: `0`; Low: `0`
- Akzeptierte Risiken: `0`; offene Fragen: `0`

*The complete RAW-02 intake was reviewed after the explicitly authorised
IAD201-IAD203 update. The three decisions are correctly bound, but two existing
quality gaps require a separately authorised remediation.*

## Entscheidungsergebnis / Decision outcome

Das frühere Serien-Finding `IR001` zur fehlenden Persistierung der drei
Entscheidungen ist inhaltlich behoben:

- **IAD201:** transportneutraler IPC-/Prozessvertrag bei RAW-02; konkrete
  Process API und Transportwahl bei RAW-06.
- **IAD202:** explizite Trennung flüchtiger und persistenter Context-Daten;
  versionierte, fail-closed Wiederherstellung und Invalidierung; State-Semantik
  bleibt bei RAW-03.
- **IAD203:** geordnete Command Queue mit Correlation/Idempotency, begrenzter
  Deduplizierung und Wiederholung, sichtbarem Abbruch und keinem automatischen
  Replay nicht-idempotenter Aktionen; Mutationen erst nach dem Read-only-Slice.

Authoring-Status und Receipt sind `ReadyForReview`. Der Serien-Lifecycle bleibt
korrekt `Blocked`, bis RAW-01 und RAW-03 in der bindenden Reihenfolge
abgeschlossen sind und aktuelle Reviews besitzen.

*The decision-persistence gap is resolved. Authoring readiness does not bypass
the binding RAW-01 and RAW-03 predecessors or grant downstream authority.*

## Findings / Findings

| ID | Severity | Aussage / Statement | Disposition und Re-Evaluation |
|---|---|---|---|
| IR201 | High | Mehrere normative Abschnitte besitzen keine vollständige englische Entsprechung; zentrale Begriffe werden für die erklärte Zielgruppe nicht beim ersten Gebrauch erklärt. / Several normative sections lack complete English counterparts, and central terms are not explained for the declared learner audience. | `NeedsRemediation`; vollständige DE/EN-Paare und Erstbegriffserklärungen oder präziser Glossarverweis, danach vollständiges Re-Review. |
| IR202 | High | Privacy, WCAG 2.2 AA, Plattform-/Cross-Platform- und Supply-Chain-Anwendbarkeit sowie messbare Evidence sind nicht ausdrücklich entschieden. / Privacy, WCAG 2.2 AA, platform/cross-platform and supply-chain applicability plus measurable evidence are not explicitly decided. | `NeedsRemediation`; begrenzte Querschnittsreparatur ohne Änderung von IAD201–203 oder Delivery Authority, danach vollständiges Re-Review. |

## Review-Coverage / Review coverage

| Prüffeld / Review area | Status | Nachweis / Evidence |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass mit IR201 | Grenzen sind klar; englische Parität ist unvollständig. / Boundaries are clear; English parity is incomplete. |
| Vorwissen / Prior knowledge | Pass | Prozesse und CLI sind als Vorwissen benannt. / Process and CLI basics are explicit. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Fail | IR201. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first status, dependencies, decisions, and next action | Pass | Authoring- und Serienstatus sowie RAW-01/03-Gates sind getrennt erklärt. / Authoring and Series status plus RAW-01/03 gates are distinct. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | FR/NFR, drei Decisions und AC-001 bis AC-005 besitzen prüfbare Grenzen. / FR/NFR, three decisions, and AC-001 through AC-005 are testable. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass mit IR202 | Decision-Evidence ist messbar; Querschnittsevidence fehlt. / Decision evidence is measurable; cross-cutting evidence is missing. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependency, authority, delivery, risks, and follow-up | Pass | Prompts verlangen aktuelle Reviews und separate Startautorität; Remote, Merge und Bypass sind ausgeschlossen. / Prompts require current reviews and separate start authority; remote, merge, and bypass are excluded. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Security, privacy, A11Y, platform, and supply chain | Fail | IR202. |
| Referenzen und Prompt-Parität / References and prompt parity | Pass | Source-/RF-Handoffs, exakter Target-Pfad und `LocalImplementation` stimmen überein. / Sources, handoffs, target path, and `LocalImplementation` agree. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass | Strict UTF-8, kein NUL und Secret Scan ohne High-Fund. / Strict UTF-8, no NUL, and no high secret finding. |

## Lineage und Review-Drift / Lineage and review drift

- Intake-ID `10c3fbdc-38f8-4e6c-b6ce-bd762f6cb2ee` bleibt erhalten.
- Vorgänger-Target und -Receipt sind bytegleich unter der Update-Operation
  `37887e13-cb91-4ade-954a-d9eb5fb33455` archiviert.
- Das Serienmanifest behält 14 Ziele, einen Root und 14 Kanten; nur der
  RAW-02-Hash wurde inhaltlich erneuert.
- Das frühere Serienreview
  `specs/intake-review-results/aoc-phase-2-series-2026-08-01-r2.json` ist durch
  RAW-02-Hash-Drift ausdrücklich invalidiert. Dieses Single Review ersetzt
  nicht dessen übrige 13 Zielprüfungen; ein späteres aktuelles Serienreview
  muss es gesondert supersedieren.

*Identity and graph cardinalities are preserved. The prior Series result is
explicitly stale; this Single result does not claim to replace its other
thirteen target reviews.*

## Exakte nächste Aktion / Exact next action

Die beiden neuen Findings benötigen eine separate, begrenzte
Reparaturautorität:

```text
$speckit-intake-repair specs/intake-review-results/raw-02-workspace-orchestrator-2026-08-01.json
Scope: ausschließlich IR201 und IR202 beheben; IAD201–IAD203, Scope, Abhängigkeiten und Delivery Authority nicht ändern; danach RAW-02 vollständig neu reviewen. Keine Specify-, Implementierungs-, Remote-, Merge- oder Bypass-Aktionen.
```

*This review records the repair boundary but does not authorise or start it.*
