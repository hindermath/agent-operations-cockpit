# Einzelreview RAW-08 – Workflow Engine / Single Review RAW-08 – Workflow Engine

## Identität und Ergebnis / Identity and outcome

- Review-ID: `b904684a-1e7c-4e59-a0a9-e29e32c9836d`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `NeedsClarification`
- Review-Zeitpunkt / Review time: `2026-08-07T21:34:19Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `54cdd411d01d6a94a932b67cb2d71f8bd6931b19b86521bf47fa4614d678daa2`
- Git-Blob: `b65b950fbfc9979a31b7a95d68d692fd814003ec`
- Request:
  `specs/intake-review-requests/raw-08-workflow-engine-2026-08-07.json`
- Request-SHA-256:
  `602c416705d2734dc1a69975139e5d262ffe3fbc07741562e7e5dddcd56d519b`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `6`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `3`
- Supersediertes Einzelreview / Superseded Single review: keines / *none*

Dieses unabhängige Einzelreview bewertet ausschließlich RAW-08. Es ändert
weder das Lastenheft noch Authoring Receipt, Series-Lifecycle oder Delivery
Authority und startet keine Folgephase. / *This independent Single review
assesses only RAW-08. It changes neither the intake, Authoring Receipt, Series
lifecycle, nor delivery authority and starts no downstream phase.*

## Ergebnis / Outcome

RAW-08 beschreibt den richtigen fachlichen Owner für den Program-to-Knowledge-
Workflow: Artefakte sollen von Quellen und Decisions bis zu Evidence und
Retrospektiven nachvollziehbar bleiben, ohne AOC-Produktzustand oder Preset-
Promotion zu besitzen. Die bindenden Vorgänger RAW-05 und RAW-06 sind im
Serienmanifest abgeschlossen; RAW-08 ist der einzige `Eligible`-Kandidat. /
*RAW-08 identifies the correct owner for the program-to-knowledge workflow.
Its binding predecessors are complete and it is the sole Eligible candidate.*

`Ready` ist dennoch nicht zulässig. Persistenz, Signatur oder Attestation und
Retention sind im Target und als `DEC-T05` offen, während das Authoring Receipt
keine Decision oder offene Frage ausweist. Reproduzierbare Verträge, Fixtures,
vollständige DE/EN-Texte, Querschnittsanwendbarkeit, typisierte Handoffs und
fail-closed Authority-Grenzen fehlen ebenfalls. Das Ergebnis lautet daher
`NeedsClarification`. / *Ready is not permitted. Persistence, signature or
attestation, and retention remain open while the Receipt records no decisions
or questions. Reproducible contracts, bilingual content, cross-cutting
applicability, typed handoffs, and fail-closed authority are also incomplete.*

## Findings / Findings

| ID | Severity | Kategorie / Category | Disposition | Nachweis / Evidence |
|---|---|---|---|---|
| IR801 | High | Offene Entscheidung und Provenienz / Open decision and provenance | NeedsClarification | Target und Decision Register führen `DEC-T05`; das Receipt behauptet null Decisions und Fragen. / Target and register contain DEC-T05 while the Receipt claims no decisions or questions. |
| IR802 | High | Anforderungen und Evidence / Requirements and evidence | NeedsRemediation | Kein versionierter Workflow-/Knowledge-Package-Vertrag, keine Zustandsmatrix, Fixtures, Validatoren, Sollausgaben oder Exitcodes. / No versioned contract, state matrix, fixtures, validators, expected outputs, or exit codes. |
| IR803 | High | Sprache und Terminologie / Language and terminology | NeedsRemediation | Normative DE/EN-Paare, Erstgebrauchserklärungen sowie text-first Lifecycle, Decision und Next Action sind unvollständig. / Bilingual pairs, first-use explanations, and ordered lifecycle text are incomplete. |
| IR804 | High | Querschnittsanwendbarkeit / Cross-cutting applicability | NeedsRemediation | Security, Privacy, Public Content, WCAG 2.2 AA, Plattform-, Node- und Supply-Chain-Grenzen fehlen. / Cross-cutting boundaries are missing. |
| IR805 | High | Handoff und Abhängigkeit / Handoff and dependency contract | NeedsRemediation | RAW-05/06-Eingaben, RAW-09-Ausgabe und Child-Intakes besitzen keine vollständigen typisierten Verträge. / Inputs, output, and child-intakes lack complete typed contracts. |
| IR806 | High | Prompt und Delivery Authority / Prompt and delivery authority | NeedsRemediation | MergeAndSync und historischer Admin-Bypass sind nicht vollständig von aktueller Scope-, Start-, Write-, Merge- und Provider-Authority getrennt. / Historical delivery data and enabled prompts are not fully separated from current authority. |

## Offene Fragen und Entscheidungen / Open questions and decisions

1. **IRQ801 – Persistenz:** Welches versionierte Format, welcher Speicherort und
   welche atomare Schreib- und Wiederherstellungsgrenze gelten? / *Which
   versioned format, storage location, and atomic write and recovery boundary
   apply?*
2. **IRQ802 – Signatur oder Attestation:** Welche Methode, Trust-Root-Grenze und
   fail-closed Validierung gelten für Receipts und Knowledge Packages? / *Which
   method, trust-root boundary, and fail-closed validation apply?*
3. **IRQ803 – Retention:** Welche Aufbewahrungs-, Archivierungs-, Lösch- und
   Legal-Hold-Regeln gelten je Evidence-Klasse? / *Which retention, archival,
   deletion, and legal-hold rules apply per evidence class?*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass mit IR803 | Owner-Grenze und Ausschluss der Produktzustandslogik sind erkennbar; vollständige bilinguale Scope-/Non-Goal-Texte fehlen. / Ownership is visible; complete bilingual boundaries are absent. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Fail | Git-/Review-Grundlagen decken Workflow-, Evidence-, Receipt-, Attestation- und Authority-Begriffe nicht ab. / Stated prior knowledge does not cover the key terms. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Fail | `DEC-T05` und Receipt widersprechen sich; `Eligible` ist nicht ausdrücklich von Startautorität getrennt. / Decision state and Receipt conflict; Eligibility is not fully separated from start authority. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Fail | Artefakt- und Übergangsanforderungen sind knapp, aber Persistenz, Signatur, Retention und Recovery nicht deterministisch. / Persistence, signature, retention, and recovery are not deterministic. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Fail | AC-001/002 besitzen keine versionierten Verträge, Fixtures, Validatoren oder Sollausgaben. / Acceptance has no versioned contracts or reproducible evidence. |
| Handoff, Risiken und Authority / Handoff, risks, and authority | Fail | RAW-05/06/09-Handoffs, Child-Intakes und aktuelle Authority sind nicht ausreichend typisiert oder fail-closed. / Handoffs and current authority are incomplete. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Fail | `secret-free` allein begründet keine vollständige Anwendbarkeits- und Negativ-Evidence. / Secret-free alone does not establish applicability evidence. |
| Prompt- und Projektionsparität / Prompt and projection parity | Fail | Der Autonomous-Prompt fordert MergeAndSync ohne vollständige aktuelle Authority-Voraussetzungen. / The Autonomous prompt lacks complete current-authority prerequisites. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass mit IR804 | Target und Receipt sind UTF-8 und enthalten keine erkannten Secrets oder privaten Pfade; normative Datenminimierung bleibt offen. / Encoding and scans pass; normative minimisation remains open. |

## Positive Nachweise / Positive evidence

- Target-Hash und Git-Blob stimmen mit dem unveränderten RAW-08 überein. /
  *Target hash and Git blob match the unchanged RAW-08 intake.*
- Das Authoring Receipt bindet den aktuellen Target-Hash und besteht nach
  korrekter Invocation die Strukturvalidatoren; die semantische Decision-
  Diskrepanz bleibt davon unberührt. / *The Receipt binds the current target
  hash and structural validation does not resolve the semantic decision gap.*
- Series Manifest und Receipt bestehen unter Bash und PowerShell; RAW-08 ist
  der einzige deklarierte und strukturell eligible Kandidat. / *Both Series
  validators pass and RAW-08 is the sole eligible candidate.*
- Es wurden keine Binärdaten, Secrets, privaten Hostpfade oder Schreiboperationen
  im Target festgestellt. / *No binary data, secrets, private host paths, or
  target writes were found.*

## Serien- und Authority-Auswirkung / Series and authority impact

Dieses Single Review ändert weder den Series-Lifecycle noch RAW-08s Status
`Eligible`. Das Ergebnis `NeedsClarification` blockiert jede nachgelagerte
Ausführung. Eligibility, historisches MergeAndSync und ein späteres `Ready`
erteilen keine Specify-, Implementierungs-, Governance-Write-, Remote-, Merge-,
Bypass-, Provider-, Preset- oder Level-0-Autorität. RAW-09 bleibt außerdem durch
RAW-08 und seine eigenen Decisions blockiert. / *This review changes no Series
lifecycle. NeedsClarification blocks downstream work, and no stored state grants
delivery authority. RAW-09 remains blocked by RAW-08 and its own decisions.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich angeforderte
unabhängige RAW-08-Single-Review; Owner ist `RAW-08 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Das Lastenheft,
Authoring Receipt und Series-Artefakte bleiben unverändert. / *Decision:
UpdateRequired. The requested Single review is the source and RAW-08 intake
review is the owner. The request, result, and report are new; target, Authoring
Receipt, and Series artifacts remain unchanged.*

## Risiken, Ausnahmen und Nicht-Autorität / Risks, exceptions, and non-authority

Es wurden keine Risiken akzeptiert und keine Operator-Ausnahmen erteilt.
Zusammenfassung: Critical `0`, High `6`, Medium `0`, Low `0`. Dieses Review
genehmigt keine fachliche Antwort, Reparatur, Specify-, Implementierungs-,
Remote-, Merge-, Bypass-, Preset- oder Promotion-Aktion. / *No risks or
operator exceptions were accepted. This review authorises no decisions, repair,
delivery, preset change, or promotion.*

## Exakte nächste Aktion / Exact next action

Thorsten beantwortet ausdrücklich `IRQ801`, `IRQ802` und `IRQ803`. Danach kann
ein begrenztes Intake-Update `DEC-T05` und `IR801` bis `IR806` einarbeiten,
Authoring Receipt und Serien-Hashbindung erneuern und ein vollständiges RAW-08-
Re-Review durchführen. / *Thorsten explicitly answers IRQ801 through IRQ803.
Only then may a bounded intake update record DEC-T05, remediate IR801 through
IR806, renew hashes, and perform a complete RAW-08 re-review.*

```text
$speckit-intake-update requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md
```
