# Erneutes Einzelreview RAW-01 – Reference Agentic Workspace / Re-review RAW-01 – Reference Agentic Workspace

## Identität und Ergebnis / Identity and outcome

- Review-ID: `f9f08f54-95eb-4abd-8ce1-bac180a6f742`
- Modus: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `Ready`
- Review-Zeitpunkt: `2026-08-01T14:10:05Z`
- Repository-HEAD: `ddba7482163c7e61161ad0b90f4e019844335898`
- Ziel: `requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md`
- Normalisierter SHA-256: `c61d9786b27ea09e0e954363a1b4335d3255ea55b0f8a5167ee52c25c583f9b6`
- Git-Blob: `N/A`; der reparierte Inhalt ist noch nicht committet. / *The repaired content is not committed yet.*
- Request: `specs/intake-review-requests/raw-01-reference-agentic-workspace-2026-08-01-r2.json`
- Request-SHA-256: `041f9e791f31810aae5d883bf9c3406cccc5f07a6dd96efad206a533fe9dcb83`
- Supersediertes Ergebnis: `specs/intake-review-results/raw-01-reference-agentic-workspace-2026-08-01.json`
- Ziele: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken: `0`; offene Fragen: `0`

*This is the complete Single re-review after the explicitly authorised repair
of IR101 through IR103. It starts no Specify, implementation, remote write,
merge, or bypass action.*

## Ergebnis / Outcome

RAW-01 erfüllt nach der begrenzten Reparatur alle zehn
Single-Intake-Prüffelder. Die früheren Findings IR101, IR102 und IR103 sind
behoben. Es bestehen keine Findings, offenen Fragen, akzeptierten Risiken oder
Operator-Ausnahmen; das Ergebnis ist `Ready`. / *After the bounded repair,
RAW-01 satisfies all ten Single-intake review areas. Prior findings IR101,
IR102, and IR103 are resolved. There are no findings, open questions, accepted
risks, or operator exceptions; the outcome is `Ready`.*

## Reparatur- und Autorisierungsnachweis / Repair and authority evidence

Thorsten autorisierte am 2026-08-01 ausschließlich die Behebung von IR101,
IR102 und IR103 sowie dieses vollständige Re-Review. IAD101 bis IAD103, Scope,
Non-Goals, Abhängigkeiten und Delivery Authority wurden nicht geändert.
Specify, Implementierung, Remote Writes, Merge und Bypass blieben
ausgeschlossen. / *Thorsten authorised only the repair of IR101, IR102, and
IR103 plus this complete re-review. IAD101 through IAD103, scope, non-goals,
dependencies, and delivery authority were unchanged. Specify, implementation,
remote writes, merge, and bypass remained excluded.*

| Vorgänger-Finding / Prior finding | Begrenzte Reparatur / Bounded repair | Ergebnis / Result |
|---|---|---|
| IR101 High | Vollständige DE/EN-Paare, Einstiegserklärungen für technische und Spec-Kit-Begriffe sowie präziser Glossarverweis ergänzt. / Added complete German/English pairs, first-use explanations for technical and Spec Kit terms, and a precise glossary reference. | Resolved |
| IR102 High | Security, Privacy, WCAG 2.2 AA, Plattformparität und Software-Lieferkette ausdrücklich eingestuft; AC-007 bis AC-009 und positive/negative Evidence machen sie messbar. / Explicitly classified security, privacy, WCAG 2.2 AA, platform parity, and software supply chain; AC-007 through AC-009 plus positive and negative evidence make them measurable. | Resolved |
| IR103 High | Der unveränderte `MergeAndSync`-Prompt besitzt jetzt eine fail-closed Vorbedingung für separate aktuelle Scope-, Implementierungs-, Remote-, Merge- und Bypass-Autorität. / The unchanged `MergeAndSync` prompt now has a fail-closed precondition for separate current scope, implementation, remote, merge, and bypass authority. | Resolved |

## Erhalt von Paket A / Preservation of Package A

| Entscheidung / Decision | Bestätigter Inhalt / Confirmed content | Review |
|---|---|---|
| IAD101 | `net10.0` als plattformneutraler Vertrags-TFM; Domain und Core ohne Windows-spezifische Abhängigkeit. / `net10.0` as the platform-neutral contract TFM; domain and core without Windows-specific dependencies. | Pass; unverändert / unchanged |
| IAD102 | Versioniertes kanonisches JSON mit expliziter Schemaversion und JSON Schema; Konsole als Projektion desselben Modells. / Versioned canonical JSON with explicit schema version and JSON Schema; console as a projection of the same model. | Pass; unverändert / unchanged |
| IAD103 | xUnit.net v3, Microsoft Testing Platform v2, stabile Pakete und `dotnet test`. / xUnit.net v3, Microsoft Testing Platform v2, stable packages, and `dotnet test`. | Pass; unverändert / unchanged |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Nachweis / Evidence |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass | Ziel und Grenzen sind ausdrücklich und vollständig zweisprachig; die Reparatur erweitert den Scope nicht. / Goal and boundaries are explicit and fully bilingual; the repair does not broaden scope. |
| Vorwissen / Prior knowledge | Pass | Git- und Terminal-Grundlagen sind benannt; AOC- oder Spec-Kit-Geschichte wird nicht vorausgesetzt. / Git and terminal basics are named; AOC or Spec Kit history is not assumed. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Pass | Alle normativen Abschnitte besitzen DE/EN-Paare; zentrale Begriffe sind lokal erklärt oder präzise mit dem Glossar verbunden. / All normative sections have German/English pairs; central terms are explained locally or precisely linked to the glossary. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first status, dependencies, decisions, and next action | Pass | `ReadyForReview`, RAW-03 vor RAW-02, IAD101–IAD103 und die getrennten Prompt-Grenzen sind textuell; das Receipt benennt das vollständige Single Review. / Status, ordering, decisions, and prompt boundaries are textual; the receipt names the complete Single review. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Drei FRs, zwei NFRs, fünf Querschnittsregeln und drei IAD-Verträge besitzen klare Modalität und Owner-Grenzen. / Three FRs, two NFRs, five cross-cutting rules, and three IAD contracts have clear modality and ownership boundaries. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | AC-001 bis AC-009 sowie positive und negative Fixtures prüfen Discovery, Schema, TFM, Testlauf, Datenschutz, A11Y, Plattform und Lieferketten-Handoff. / AC-001 through AC-009 plus positive and negative fixtures test discovery, schema, TFM, test execution, privacy, accessibility, platform, and supply-chain handoff. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependency, authority, delivery, risks, and follow-up | Pass | RAW-03 bleibt unverändert vor RAW-02; `MergeAndSync` bleibt nur gespeicherte Obergrenze und benötigt zusätzlich eine separate aktuelle Benutzerentscheidung. Risiken und Revisionsauslöser sind ausdrücklich. / RAW-03 remains before RAW-02; `MergeAndSync` remains only a stored ceiling and additionally requires a separate current user decision. Risks and revision triggers are explicit. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Security, privacy, A11Y, platform, and supply chain | Pass | Read-only und Redaction, opake Hostidentität, WCAG 2.2 AA, identische macOS-/Linux-/Windows-Semantik sowie aktuelles `N/A` mit Dependency-Re-Evaluation sind ausdrücklich und messbar. / Read-only behaviour and redaction, opaque host identity, WCAG 2.2 AA, identical macOS/Linux/Windows semantics, and current `N/A` with dependency re-evaluation are explicit and measurable. |
| Referenzen und Prompt-Parität / References and prompt parity | Pass | Source-/RF-Zuordnung, Glossarlink, Target-Pfad, Receipt und beide Prompts stimmen mit den normativen Grenzen überein. / Source and finding mapping, glossary link, target path, receipt, and both prompts match the normative boundaries. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass | Strict UTF-8, kein BOM/NUL, ausdrückliche Datenminimierung und Secret Scan ohne Fund. / Strict UTF-8, no BOM or NUL, explicit data minimisation, and no secret finding. |

## Lineage und Serienauswirkung / Lineage and series impact

- Die Intake-ID `fbe82f90-1f0d-439b-bf2c-15b0dec8e605` und Delivery Authority
  `MergeAndSync` bleiben erhalten. / *The intake identity and stored delivery
  ceiling remain unchanged.*
- Vorgänger-Target und -Receipt sind unter Operation
  `1c8974d9-5ad1-46b8-b57e-9574a1f813e9` bytegleich archiviert. / *The
  predecessor target and receipt are archived byte-identically under the repair
  operation.*
- Die Serienoperation `5f59d351-54e2-4c01-90ef-2a5f104d0ee0` aktualisiert nur
  die RAW-01-Hashbindung. Vierzehn Ziele, ein Root, vierzehn Kanten,
  Reihenfolge und Lifecycle bleiben unverändert. / *The Series operation
  updates only the RAW-01 hash binding. Fourteen targets, one root, fourteen
  edges, order, and lifecycle remain unchanged.*
- Das frühere RAW-01-Single-Ergebnis wird ausdrücklich supersediert. Ältere
  Series Reviews bleiben wegen Target-Hash-Drift historisch und werden durch
  dieses Single Review nicht ersetzt. / *The prior RAW-01 Single result is
  explicitly superseded. Older Series reviews remain historical because of
  target hash drift and are not replaced by this Single review.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quellen sind das Vorgängerreview und das
Authoring-Profil; Owner ist RAW-01. Aktualisiert wurden Lastenheft,
Authoring-/Series-Receipts und dieses Re-Review-Paket. Evidence sind die
gebundenen normalisierten Hashes sowie die Bash-/PowerShell-Validatoren. /
*Decision: documentation must be updated. Sources are the predecessor review
and authoring profile; RAW-01 is the owner. The intake, authoring and Series
receipts, and this re-review package were updated. Bound normalised hashes plus
the Bash and PowerShell validators provide evidence.*

## Validierungsnachweise / Validation evidence

- Intake Authoring Receipt: Bash `PASS`, PowerShell `PASS`.
- Series Manifest und Receipt: Bash `PASS`, PowerShell `PASS`.
- Single-Review-Ergebnis: Bash `PASS`, PowerShell `PASS`.
- Requirements-Governance-Konfiguration: nicht im Repository vorhanden und für
  dieses einzelne Ziel nicht im Scope. / *No configuration exists in the
  repository; it is outside this Single-target scope.*
- UTF-8, BOM, NUL und lokaler Glossarlink: `PASS`.
- Secret Scan: keine Funde. / *No findings.*
- `git diff --check`: `PASS`.

## Restrisiko / Residual risk

Keine akzeptierten Risiken. Zusammenfassung: Critical `0`, High `0`, Medium
`0`, Low `0`. Zielanzahl: `1`; Workeranzahl: `0`. / *There are no accepted
risks. Summary: Critical `0`, High `0`, Medium `0`, Low `0`. Target count: `1`;
worker count: `0`.*

## Exakte nächste Aktion / Exact next action

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

*This read-only status check can confirm the current Series blockers. It starts
neither Specify nor an autonomous or delivery action.*
