# Einzelreview RAW-01 – Reference Agentic Workspace / Single Review RAW-01 – Reference Agentic Workspace

## Identität und Ergebnis / Identity and outcome

- Review-ID: `4ab724bc-61ce-4ed9-a602-225218870d29`
- Modus: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `NeedsRemediation`
- Review-Zeitpunkt: `2026-08-01T13:39:53Z`
- Repository-HEAD: `ddba7482163c7e61161ad0b90f4e019844335898`
- Ziel: `requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md`
- Normalisierter SHA-256: `b0d217e8c440bd2a01106e827564a5354a9bef040d28910633171cb092ff1453`
- Git-Blob: `b68008cad854963e583f9002c28915ec7f0003be`
- Request: `specs/intake-review-requests/raw-01-reference-agentic-workspace-2026-08-01.json`
- Request-SHA-256: `22e7114efb49cc2fef1a0153da92feb81bc3aad0e4356f58ecc5a0bbfe569b83`
- Ziele: `1`; Worker: `0`
- Critical: `0`; High: `3`; Medium: `0`; Low: `0`
- Akzeptierte Risiken: `0`; offene Fragen: `0`
- Supersediertes Einzelreview: keines / *none*

*This is an independent Single review of the hash-bound RAW-01 update. It
creates review evidence only and starts no repair, Specify, implementation,
remote write, merge, or bypass action.*

## Entscheidungsergebnis / Decision outcome

Paket A ist vollständig und widerspruchsfrei in Intake und Receipt gebunden:

- **IAD101:** `net10.0` ist der plattformneutrale Vertrags-TFM; Domain und Core
  bleiben frei von Windows-spezifischen Abhängigkeiten.
- **IAD102:** `WorkspaceSnapshot` ist kanonisches, versioniertes JSON mit
  expliziter Schemaversion und JSON Schema; die Konsole projiziert dasselbe Modell.
- **IAD103:** xUnit.net v3 und Microsoft Testing Platform v2 werden mit stabilen
  Paketen und `dotnet test` verwendet.

*Package A is completely and consistently bound in the intake and receipt.
IAD101 through IAD103 are answered and `openDecisionIds` is empty.*

Die drei Entscheidungen sind nicht selbst der Blocker. Drei bereits im
Gesamtdokument vorhandene Qualitäts- und Authority-Lücken erfordern eine
separat autorisierte Reparatur. / *The three decisions are not the blocker.
Three quality and authority gaps in the complete intake require separately
authorised remediation.*

## Findings / Findings

| ID | Severity | Aussage / Statement | Disposition und Re-Evaluation |
|---|---|---|---|
| IR101 | High | Mehrere normative Abschnitte besitzen keine vollständige englische Entsprechung; zentrale Begriffe werden für die erklärte Zielgruppe nicht beim ersten Gebrauch erklärt oder mit dem Glossar verbunden. / Several normative sections lack complete English counterparts; central terms are not explained on first use or linked to the glossary for the declared audience. | `NeedsRemediation`; vollständige DE/EN-Paare und Erstbegriffserklärungen oder präziser Glossarlink, danach vollständiges Re-Review. |
| IR102 | High | Privacy, Datenminimierung und Software-Lieferketten-Anwendbarkeit sind trotz Host-/Repositorydaten und externer Testpakete nicht entschieden; Security, WCAG und Plattformparität besitzen keine vollständige messbare positive und negative Evidence. / Privacy, data minimisation, and supply-chain applicability are undecided despite host and repository data plus external test packages; security, WCAG, and platform parity lack complete measurable positive and negative evidence. | `NeedsRemediation`; begrenzte Querschnittsreparatur ohne Änderung von IAD101–IAD103, danach vollständiges Re-Review. |
| IR103 | High | Der `MergeAndSync`-Prompt verlangt nur ein aktuelles Review, obwohl Intake und Receipt keine aktuelle Implementierungs-, Remote-, Merge- oder Bypass-Autorität erteilen. / The `MergeAndSync` prompt requires only a current review although the intake and receipt grant no current implementation, remote, merge, or bypass authority. | `NeedsRemediation`; fail-closed Vorbedingung für eine separate aktuelle Benutzerentscheidung ergänzen, gespeicherte Delivery Authority unverändert lassen, danach vollständiges Re-Review. |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Nachweis / Evidence |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass mit IR101 | Identität und Grenzen sind fachlich klar; die englische Parität der Grenze fehlt. / Identity and boundaries are clear, but the boundary lacks English parity. |
| Vorwissen / Prior knowledge | Pass | Git- und Terminal-Grundlagen sind benannt; AOC-Historie wird ausgeschlossen. / Git and terminal basics are named; AOC history is excluded. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Fail | IR101. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first status, dependencies, decisions, and next action | Pass mit IR101 | `ReadyForReview`, die drei IADs und der Handoff zu RAW-03 vor RAW-02 sind textuell vorhanden; Workflow-Begriffe benötigen Einstiegserklärungen. / Status, decisions, and handoff are textual; workflow terms need first-use explanations. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Drei FRs, zwei NFRs und die drei Paket-A-Verträge besitzen eindeutige fachliche Grenzen. / Three FRs, two NFRs, and the three Package A contracts have clear boundaries. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass mit IR102 | AC-001 bis AC-006 prüfen Discovery, Fehlerfälle, Host/Sandbox, TFM, Schema und Testlauf; Querschnittsevidence ist unvollständig. / AC-001 through AC-006 test discovery, failures, host/sandbox, TFM, schema, and test execution; cross-cutting evidence is incomplete. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependency, authority, delivery, risks, and follow-up | Fail | IR103; Handoff und Revisionsauslöser sind vorhanden, aber der autonome Prompt ist nicht fail-closed an neue Delivery-Autorität gebunden. / Handoff and revision triggers exist, but the autonomous prompt is not fail-closed against fresh delivery authority. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Security, privacy, A11Y, platform, and supply chain | Fail | IR102. |
| Referenzen und Prompt-Parität / References and prompt parity | Fail | Source- und RF-Referenzen sowie Hashbindungen sind aktuell; die autonome Prompt-Parität scheitert an IR103. / Source and finding references plus hashes are current; autonomous prompt parity fails through IR103. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass mit IR102 | Strict UTF-8, kein BOM/NUL und Secret Scan ohne Fund; die normative Privacy-Minimierung fehlt weiterhin. / Strict UTF-8, no BOM or NUL, and no secret finding; normative privacy minimisation is still missing. |

## Lineage und Serienauswirkung / Lineage and series impact

- Intake-ID `fbe82f90-1f0d-439b-bf2c-15b0dec8e605` und Delivery Authority
  `MergeAndSync` bleiben unverändert. / *The intake identity and stored delivery
  ceiling are unchanged.*
- Vorgänger-Target und -Receipt sind bytegleich unter Operation
  `c7023703-0500-4c2c-9131-8f0597e24599` archiviert. / *The predecessor target
  and receipt are archived byte-identically under the update operation.*
- Serienoperation `851b053d-2ff3-4045-a539-2f1b65de8fca` änderte ausschließlich
  die RAW-01-Hashbindung; 14 Ziele, ein Root, 14 Kanten, Reihenfolge und
  Lifecycle blieben unverändert. / *The Series operation changed only the
  RAW-01 hash binding; target, root, edge, order, and lifecycle cardinalities
  remain unchanged.*
- Es existierte kein früheres RAW-01-Single-Ergebnis. Die älteren
  Serienreviews bleiben wegen RAW-01- und RAW-02-Hash-Drift historisch und
  werden durch dieses Einzelreview nicht ersetzt. / *No prior RAW-01 Single
  result existed. Older Series reviews remain historical because of RAW-01 and
  RAW-02 target drift and are not replaced by this Single review.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das unabhängige RAW-01-Single-Review;
Owner ist RAW-01. Neu sind Request, maschinenlesbares Ergebnis und dieser
zweisprachige Bericht. Evidence sind die gebundenen normalisierten Hashes,
Validatoren und der Secret Scan. / *Decision: documentation must be updated.
The independent RAW-01 Single review is the source and RAW-01 is the owner.
The request, machine-readable result, and this bilingual report are new. Bound
normalised hashes, validators, and the secret scan provide evidence.*

## Validierungsnachweise / Validation evidence

- Intake Authoring Receipt: Bash `PASS`, PowerShell `PASS`.
- Series Manifest und Receipt: Bash `PASS`, PowerShell `PASS`.
- Single-Review-Ergebnis: Bash `PASS`, PowerShell `PASS`.
- Requirements-Governance-Konfiguration: nicht im Repository vorhanden und für
  dieses einzelne Ziel nicht im Scope. / *No configuration exists in the
  repository; it is outside this Single-target scope.*
- UTF-8, BOM und NUL: `PASS`.
- Secret Scan: keine Funde. / *No findings.*
- `git diff --check`: `PASS`.

## Fragen, Risiken und Ausnahmen / Questions, risks, and exceptions

- Offene Fragen: `0` / *Open questions: `0`*
- Akzeptierte Risiken: `0` / *Accepted risks: `0`*
- Operator-Ausnahmen: `0` / *Operator exceptions: `0`*

Das Ergebnis ist wegen drei High-Findings `NeedsRemediation`; ein autonomer
Agent akzeptiert diese Risiken nicht. / *The result is `NeedsRemediation`
because of three High findings; an autonomous agent does not accept them.*

## Exakte nächste Aktion / Exact next action

```text
$speckit-intake-repair specs/intake-review-results/raw-01-reference-agentic-workspace-2026-08-01.json
Scope: ausschließlich IR101, IR102 und IR103 beheben; IAD101–IAD103, Scope, Non-Goals, Abhängigkeiten und Delivery Authority nicht ändern; danach RAW-01 vollständig neu reviewen. Keine Specify-, Implementierungs-, Remote-, Merge- oder Bypass-Aktionen.
```

*This review records the bounded remediation handoff but does not authorise or
start it.*
