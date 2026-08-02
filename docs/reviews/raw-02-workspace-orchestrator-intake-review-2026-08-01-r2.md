# Erneutes Einzelreview RAW-02 – Workspace Orchestrator / Re-review RAW-02 – Workspace Orchestrator

## Identität und Ergebnis / Identity and outcome

- Review-ID: `b1ffb007-f963-4f0f-b787-492f1b4b6717`
- Modus: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `Ready`
- Review-Zeitpunkt: `2026-08-01T12:48:45Z`
- Repository-HEAD: `ddba7482163c7e61161ad0b90f4e019844335898`
- Ziel: `requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md`
- Normalisierter SHA-256: `7b2f4241e92c9dba5eb6b420d98d587b34ffe6a6ee5e607762125687a334c4e6`
- Request: `specs/intake-review-requests/raw-02-workspace-orchestrator-2026-08-01-r2.json`
- Request-SHA-256: `d313e1a6d763860d83892f1d7b3454df5ac52e61628d10ae534e1f099570cf62`
- Supersediertes Ergebnis: `specs/intake-review-results/raw-02-workspace-orchestrator-2026-08-01.json`
- Ziele: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken: `0`; offene Fragen: `0`

*This is the complete single-intake re-review after the explicitly authorised
IR201 and IR202 repair. It starts no Specify, implementation, remote, merge, or
bypass action.*

## Ergebnis / Outcome

RAW-02 erfüllt nach der begrenzten Reparatur alle zehn
Single-Intake-Prüffelder. Die früheren Findings IR201 und IR202 sind behoben.
Es bestehen keine Findings, offenen Fragen, akzeptierten Risiken oder
Operator-Ausnahmen; das Ergebnis ist `Ready`.

*After the bounded repair, RAW-02 satisfies all ten single-intake review areas.
Prior findings IR201 and IR202 are resolved. There are no findings, open
questions, accepted risks, or operator exceptions; the outcome is `Ready`.*

## Reparatur- und Autorisierungsnachweis / Repair and authority evidence

Thorsten autorisierte am 2026-08-01 ausschließlich die Behebung von IR201 und
IR202 sowie dieses vollständige Re-Review. IAD201 bis IAD203, Scope,
Abhängigkeiten und Delivery Authority wurden nicht geändert. Specify,
Implementierung, Remote Writes, Merge und Bypass blieben ausgeschlossen.

*Thorsten authorised only the repair of IR201 and IR202 plus this complete
re-review on 2026-08-01. IAD201 through IAD203, scope, dependencies, and
delivery authority were unchanged. Specify, implementation, remote writes,
merge, and bypass remained excluded.*

| Vorgänger-Finding / Prior finding | Begrenzte Reparatur / Bounded repair | Ergebnis / Result |
|---|---|---|
| IR201 High | Vollständige DE/EN-Paare, lokale Erstbegriffserklärungen, CEFR-B2-Erklärung und präziser Glossarverweis ergänzt. / Added complete German/English pairs, local first-use explanations, a CEFR B2 explanation, and a precise glossary reference. | Resolved |
| IR202 High | Security, Privacy, WCAG 2.2 AA, Plattformparität und Software-Lieferkette ausdrücklich eingestuft; AC-006 und positive/negative Evidence machen die Prüfung messbar. / Explicitly classified security, privacy, WCAG 2.2 AA, platform parity, and software supply chain; AC-006 plus positive/negative evidence make validation measurable. | Resolved |

## Erhalt der drei Entscheidungen / Preservation of the three decisions

| Entscheidung / Decision | Bestätigter Inhalt / Confirmed content | Review |
|---|---|---|
| IAD201 | RAW-02 besitzt den transportneutralen logischen Vertrag; konkrete Process API und Transportwahl bleiben bei RAW-06. / RAW-02 owns the transport-neutral logical contract; the concrete process API and transport remain with RAW-06. | Pass; unverändert / unchanged |
| IAD202 | Nur bestätigte Fokus- und Routingauswahlen mit Schemaversion dürfen persistieren; Laufzeitkontext bleibt flüchtig und ungültiger Kontext wird fail-closed verworfen. RAW-03 behält State-Semantik. / Only confirmed focus and routing choices with schema version may persist; runtime context remains volatile and invalid context is discarded fail-closed. RAW-03 retains state semantics. | Pass; unverändert / unchanged |
| IAD203 | Reihenfolge gilt pro Session; Deduplizierung und Retry nur für ausdrücklich idempotente Aktionen; Abbruch ist sichtbar und terminal; nicht-idempotente Aktionen werden nie automatisch wiederholt. / Ordering applies per session; deduplication and retry apply only to explicitly idempotent actions; cancellation is visible and terminal; non-idempotent actions are never replayed automatically. | Pass; unverändert / unchanged |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Nachweis / Evidence |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass | Ziel und Grenzen sind ausdrücklich und vollständig zweisprachig; die Reparatur erweitert den Scope nicht. / Goal and boundaries are explicit and fully bilingual; the repair does not broaden scope. |
| Vorwissen / Prior knowledge | Pass | Prozesse und CLI-Grundlagen sind benannt; Spec-Kit- oder interne Projekthistorie wird nicht vorausgesetzt. / Process and CLI basics are named; Spec Kit or internal project history is not assumed. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Pass | IPC, Session Context, Correlation ID, Idempotency Key, fail-closed, Cancellation Handle, Routing, Read-only-Slice, Spec Kit, CEFR B2, WCAG, UI und SBOM sind erklärt oder präzise verlinkt. / Central technical and workflow terms are explained or precisely linked. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first status, dependencies, decisions, and next action | Pass | `ReadyForReview`, `Blocked`, RAW-01/03, alle drei IADs, Recovery und Nicht-Autorität stehen als geordneter Text. / Status, dependencies, all three decisions, recovery, and non-authority are ordered text. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Drei FRs, zwei NFRs und die drei IAD-Verträge besitzen eindeutige Modalität und Owner-Grenzen. / Three FRs, two NFRs, and the three IAD contracts have clear modality and ownership boundaries. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | AC-001 bis AC-006 prüfen Handoffs, Authority, Transportneutralität, Persistenz, Queue-Verhalten und Querschnittsanwendbarkeit positiv und negativ. / AC-001 through AC-006 test handoffs, authority, transport neutrality, persistence, queue behaviour, and cross-cutting applicability with positive and negative evidence. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependency, authority, delivery, risks, and follow-up | Pass | RAW-01/03 bleiben bindende Vorgänger; `LocalImplementation` bleibt nur die nicht-remote Obergrenze ohne aktuelle Startautorität. Revisionsauslöser sind ausdrücklich. / RAW-01/03 remain binding predecessors; `LocalImplementation` remains only the non-remote ceiling without current start authority. Revision triggers are explicit. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Security, privacy, A11Y, platform, and supply chain | Pass | Authority und Datenminimierung sind fail-closed; WCAG 2.2 AA gilt für Dokument und Textstatus; der logische Vertrag ist plattformneutral; die aktuelle Lieferketten-Einstufung `N/A` besitzt einen Re-Evaluation-Trigger. / Authority and data minimisation are fail-closed; WCAG 2.2 AA applies to the document and textual status; the logical contract is platform-neutral; the current supply-chain `N/A` has a re-evaluation trigger. |
| Referenzen und Prompt-Parität / References and prompt parity | Pass | Glossarlink, Source-/RF-Zuordnung, Target-Pfad, Receipt und beide Prompts stimmen mit den normativen Grenzen überein. / Glossary link, sources and findings, target path, receipt, and both prompts match the normative boundaries. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass | Strict UTF-8, kein BOM/NUL, ausdrückliches Personendatenverbot und Secret Scan ohne High-Fund. / Strict UTF-8, no BOM or NUL, explicit prohibition of unnecessary personal data, and secret scan without a high finding. |

## Lineage und Serienauswirkung / Lineage and series impact

- Die Intake-ID `10c3fbdc-38f8-4e6c-b6ce-bd762f6cb2ee` bleibt erhalten. /
  *The intake retains its identity.*
- Vorgänger-Target und -Receipt sind unter Operation
  `b9f65ae1-0992-4224-a318-0564c3d0fd3c` bytegleich archiviert. / *The
  predecessor target and receipt are archived byte-identically under the repair
  operation.*
- Die Series-Operation `17ec1159-b856-4e2f-918e-10a48f0e3368` aktualisiert nur
  die RAW-02-Hashbindung. Vierzehn Ziele, ein Root, vierzehn Kanten, Reihenfolge
  und Lifecycle bleiben unverändert. / *The Series operation updates only the
  RAW-02 hash binding. Fourteen targets, one root, fourteen edges, order, and
  lifecycle remain unchanged.*
- Das frühere RAW-02-Single-Ergebnis wird ausdrücklich supersediert. Die
  älteren Series Reviews bleiben wegen Target-Hash-Drift historisch und werden
  durch dieses Single Review nicht ersetzt. / *The prior RAW-02 Single result
  is explicitly superseded. Older Series reviews remain historical because of
  target hash drift and are not replaced by this Single review.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle sind das Vorgängerreview und das
Authoring-Profil; Owner ist RAW-02. Aktualisiert wurden Lastenheft,
Authoring-/Series-Receipts und dieses Review-Paket. Evidence sind die gebundenen
normalisierten Hashes sowie die Bash-/PowerShell-Validatoren. / *Decision:
documentation must be updated. Sources are the predecessor review and authoring
profile; RAW-02 is the owner. The intake, authoring and Series receipts, and
this review package were updated. Bound normalised hashes plus the Bash and
PowerShell validators provide evidence.*

## Validierungsnachweise / Validation evidence

- Intake Authoring Receipt: Bash `PASS`, PowerShell `PASS`.
- Series Manifest und Receipt: Bash `PASS`, PowerShell `PASS`.
- Single-Review-Ergebnis: Bash `PASS`, PowerShell `PASS`.
- Governance-Konfiguration: `Aligned`.
- UTF-8, BOM, NUL und lokale Links: `PASS`.
- Secret Scan: High `0`. / *No high finding.*
- `git diff --check`: `PASS`.

## Restrisiko / Residual risk

Keine akzeptierten Risiken. RAW-02 bleibt im Serien-Lifecycle wegen der
bindenden Vorgänger RAW-01 und RAW-03 `Blocked`; dieser bekannte
Sequencing-Status ist kein Review-Finding und keine Delivery-Freigabe. /
*There are no accepted risks. RAW-02 remains `Blocked` in the Series lifecycle
because RAW-01 and RAW-03 are binding predecessors; this known sequencing state
is neither a review finding nor delivery authority.*

## Exakte nächste Aktion / Exact next action

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

*This read-only status check can confirm the current Series blockers. It starts
neither Specify nor an autonomous or delivery action.*
