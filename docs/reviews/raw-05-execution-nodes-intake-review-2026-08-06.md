# Einzelreview RAW-05 – Execution Nodes / Single Review RAW-05 – Execution Nodes

## Identität und Ergebnis / Identity and outcome

- Review-ID: `79d43997-ada1-4b19-b9bd-31d368b5b1eb`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `NeedsClarification`
- Review-Zeitpunkt / Review time: `2026-08-06T19:22:44Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `51b844e44e226ee1b00e1b74e23d86ee59d207a9873d7ed343b27e4ff2429f03`
- Git-Blob: `48845d019bd63a04b56a0ccb9e8a61123419630a`
- Request:
  `specs/intake-review-requests/raw-05-execution-nodes-2026-08-06.json`
- Request-SHA-256:
  `0062bd6c95a986344988bfbfc807c71ab44fbd9fac51e34421ef37986219b00d`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `6`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `3`
- Supersediertes Einzelreview / Superseded Single review: keines / *none*

Dieses unabhängige Einzelreview bewertet ausschließlich RAW-05. Es ändert
weder das Lastenheft noch Authoring Receipt, Series-Lifecycle oder Delivery
Authority und startet keine Folgephase. / *This independent Single review
assesses only RAW-05. It changes neither the intake, Authoring Receipt, Series
lifecycle, nor delivery authority and starts no downstream phase.*

## Ergebnis / Outcome

RAW-05 beschreibt einen sinnvollen Boundary-Zweck: Hosts, WSL, Container,
ABS-DD-Sandbox und spätere Remote Nodes sollen als explizit autorisierte
Ausführungsziele erscheinen, ohne automatisch Working Copy, Home Baseline oder
Produktentscheidungen zu besitzen. / *RAW-05 has a valid boundary purpose:
hosts, WSL, containers, the ABS-DD sandbox, and later remote nodes should be
explicitly authorised execution targets without automatically owning a working
copy, Home Baseline, or product decisions.*

`Ready` ist jedoch nicht zulässig. Drei materielle Fragen zu Remote Transport,
Node Attestation sowie Timeout/Health/Freshness/Recovery sind offen, während
das Receipt gleichzeitig `decisions=[]`, `openDecisionIds=[]` und
`questionCount=0` behauptet. Sechs High Findings betreffen außerdem
reproduzierbare Evidence, Sprache, Querschnittsanwendbarkeit, typisierte
Handoffs und Delivery Authority. Das Ergebnis lautet daher
`NeedsClarification`. / *Ready is not allowed. Three material questions about
remote transport, node attestation, and timeout/health/freshness/recovery are
open while the Receipt records no decisions or questions. Six High findings
also cover reproducible evidence, language, cross-cutting applicability, typed
handoffs, and delivery authority. The outcome is therefore NeedsClarification.*

## Findings / Findings

| ID | Severity | Kategorie / Category | Disposition | Nachweis / Evidence |
|---|---|---|---|---|
| IR501 | High | Offene Entscheidung und Provenienz / Open decision and provenance | NeedsClarification | Drei materielle Entscheidungen fehlen im Target und im Receipt. / Three material decisions are absent from target and Receipt. |
| IR502 | High | Anforderungen und Evidence / Requirements and evidence | NeedsRemediation | Kein versionierter Node Descriptor, keine Fixtures, Validatoren, Sollausgaben, Exitcodes oder Plattformmatrix. / No versioned descriptor, fixtures, validators, expected outputs, exit codes, or platform matrix. |
| IR503 | High | Sprache und Terminologie / Language and terminology | NeedsRemediation | DE/EN-Paare, Erstgebrauchserklärungen sowie text-first Lifecycle, Decisions und Next Action sind unvollständig. / Bilingual pairs, first-use explanations, and text-first lifecycle are incomplete. |
| IR504 | High | Querschnittsanwendbarkeit / Cross-cutting applicability | NeedsRemediation | Security, Privacy, Public Content, WCAG 2.2 AA, Plattform-, Container-/WSL- und Supply-Chain-Grenzen fehlen. / Cross-cutting boundaries are missing. |
| IR505 | High | Handoff und Abhängigkeit / Handoff and dependency contract | NeedsRemediation | Outputs an RAW-02/06/08 haben keine typisierten Producer-/Consumer-, Versions-, Authority- oder Failure-Bindungen. / Outputs to RAW-02/06/08 lack typed handoff bindings. |
| IR506 | High | Prompt und Delivery Authority / Prompt and delivery authority | NeedsRemediation | Historisches MergeAndSync/Admin-Bypass im Receipt und ein nicht fail-closed Autonomous-Prompt überschreiten nicht formal die Zielgrenze, sind aber nicht ausreichend getrennt. / Historic delivery data and the enabled prompt are not explicitly fail-closed. |

## Offene Fragen und Entscheidungen / Open questions and decisions

1. **IRQ501 – Remote Transport:** Welche Transportgrenze gilt für spätere
   Remote Nodes, und wie bleibt sie von read-only Research, Trust Zone und
   Delivery Authority getrennt? / *Which transport boundary applies to later
   remote nodes, and how is it separated from research, trust, and authority?*
2. **IRQ502 – Node Attestation:** Welche Attestation und fail-closed
   Vertrauensentscheidung gelten für Host, WSL, Container, ABS-DD-Sandbox und
   spätere Remote Nodes? / *Which attestation and fail-closed trust decision
   apply across the node types?*
3. **IRQ503 – Timeout und Recovery:** Welche Timeout-, Freshness-, Health- und
   Recovery-Schwellen gelten, und welche Aktionen bleiben bei Timeout oder
   Mount-Drift verboten? / *Which timeout, freshness, health, and recovery
   thresholds apply, and which actions remain forbidden on timeout or mount
   drift?*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass mit IR503 | Boundary und Non-Goals sind erkennbar; Sprach- und Terminologievertrag bleibt unvollständig. / Boundary and non-goals are visible; language and terminology remain incomplete. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Fail | Host-/Container-Grundlagen reichen nicht für Trust Zone, Attestation, Freshness, Health, ABS-DD und Authority ohne Erstgebrauchserklärung. / Stated prior knowledge does not cover key terms. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Fail | `ReadyForReview` im Target und leere Decision-Felder im Receipt widersprechen den offenen Fragen; Lifecycle, RAW-05-Eligibility und Review-only Next Action fehlen als geordneter Text. / Target and Receipt contradict the open decisions and ordered state is incomplete. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Fail | Identitäten und Mounts sind knapp benannt, aber Attestation, Timeout, Freshness, Health, Trust und Recovery nicht deterministisch. / Core node properties are named but not deterministic. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Fail | AC-001/002 besitzen keine versionierten Verträge, Fixtures, Validatoren oder Sollausgaben. / Acceptance has no versioned contracts or reproducible evidence. |
| Handoff, Risiken und Authority / Handoff, risks, and authority | Fail | RAW-02/06/08-Handoffs und historische Prompt-/Delivery-Grenzen sind nicht ausreichend typisiert oder fail-closed. / Handoffs and authority boundaries are incomplete. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Fail | Die wenigen Secret-/Hostpfad-Hinweise ersetzen keine vollständige Anwendbarkeits- und Re-Evaluation-Evidence. / Brief secret/path statements do not establish applicability evidence. |
| Prompt- und Projektionsparität / Prompt and projection parity | Fail | Der Autonomous-Prompt fordert MergeAndSync; aktuelle Scope-, Start-, Implementierungs-, Remote-, Merge-, Bypass- und Provider-Autorität wird nicht ausdrücklich vorausgesetzt. / The prompt lacks a complete current-authority precondition. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass mit IR504 | Das Target ist strict UTF-8 und nennt Secret-/Hostpfad-Grenzen; die normative Datenminimierung und negative Evidence bleiben offen. / Encoding is clean and some limits are named, but normative minimisation is incomplete. |

## Positive Nachweise / Positive evidence

- Authoring Receipt RAW-05: Bash und PowerShell `PASS`; Target- und
  Source-Pack-Hash sind aktuell. / *Both authoring validators pass.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`; RAW-05 ist als
  einziger deklarierter `Eligible`-Kandidat gebunden. / *Both Series validators
  pass and RAW-05 is the sole declared Eligible target.*
- Der Target-Hash und Git-Blob stimmen mit dem unveränderten Lastenheft überein.
  / *Target hash and Git blob match the unchanged intake.*
- Es wurden keine Secrets, Binärdaten oder Schreiboperationen im Target
  festgestellt. / *No secrets, binary data, or target writes were found.*

Die bestandenen Strukturvalidatoren widerlegen IR501 nicht: Sie bestätigen
Hash- und Schemaaktualität, prüfen aber nicht, ob die leeren Receipt-Decision-
Felder dem fachlichen Inhalt entsprechen. / *Passing structural validators do
not negate IR501: they prove hash and schema currency but do not compare empty
Receipt decision fields with the target's domain meaning.*

## Serien- und Authority-Auswirkung / Series and authority impact

Dieses Single Review ändert weder den Series-Lifecycle noch RAW-05s Status
`Eligible`. `Eligible` und ein späteres Review-`Ready` sind keine Start-,
Specify-, Implementierungs-, Remote-, Merge-, Bypass-, Provider-, Preset- oder
Level-0-Autorität. RAW-05 bleibt durch die offene Review-Coverage und die drei
Entscheidungen blockiert. / *This Single review changes neither Series lifecycle
nor RAW-05's Eligible status. Eligible and a later Ready review grant no
downstream authority. RAW-05 remains blocked by incomplete review coverage and
the three decisions.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich angeforderte
unabhängige RAW-05-Single-Review; Owner ist `RAW-05 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Das Lastenheft
und das Authoring Receipt bleiben unverändert. / *Decision: UpdateRequired. The
requested independent RAW-05 Single review is the source and RAW-05 intake
review is the owner. The request, machine-readable result, and this report are
new; the intake and Authoring Receipt remain unchanged.*

## Risiken, Ausnahmen und Nicht-Autorität / Risks, exceptions, and non-authority

Es wurden keine Risiken akzeptiert und keine Operator-Ausnahmen erteilt.
Zusammenfassung: Critical `0`, High `6`, Medium `0`, Low `0`. Dieses Review
genehmigt weder die drei fachlichen Antworten noch eine Reparatur, Specify,
Implementierung, Remote Write, Merge, Bypass, Preset-Änderung oder Promotion.
/ *No risks or operator exceptions were accepted. Summary: Critical 0, High 6,
Medium 0, Low 0. This review authorises no decision, repair, delivery, preset
change, or promotion.*

## Exakte nächste Aktion / Exact next action

Thorsten beantwortet ausdrücklich `IRQ501`, `IRQ502` und `IRQ503`. Erst danach
kann ein begrenzter Intake-Update die bestätigten Antworten und `IR501` bis
`IR506` einarbeiten, Receipt-/Serien-Hashbindungen erneuern und ein vollständiges
RAW-05-Re-Review vorbereiten. / *Thorsten explicitly answers IRQ501 through
IRQ503. Only then may a bounded intake update record the answers and remediate
IR501 through IR506, renew Receipt and Series hashes, and prepare a complete
RAW-05 re-review.*

```text
$speckit-intake-update requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md
```
