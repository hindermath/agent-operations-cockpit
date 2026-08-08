# Einzelreview RAW-08 – Workflow Engine / Single Review RAW-08 – Workflow Engine

## Identität und Ergebnis / Identity and outcome

- Review-ID: `5d0b7069-0a37-4339-88ba-a512409fd8f6`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `NeedsRemediation`
- Review-Zeitpunkt / Review time: `2026-08-08T15:09:10Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `69228e27f596683ae7e1c502d27b230e736577d73610e1781f47fe01d4bdaae6`
- Git-Blob: `8efb6dd30120d34fa80a768a15adbbd762faf6de`
- Request:
  `specs/intake-review-requests/raw-08-workflow-engine-2026-08-08.json`
- Request-SHA-256:
  `39bf131cb3d917a027f413402379d0c9a03cd3351a8cdbe9eda3af8ca54ee3f5`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `5`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review:
  `specs/intake-review-results/raw-08-workflow-engine-2026-08-07.json`

Dieses vollständige Einzelreview bewertet ausschließlich das aktualisierte
RAW-08. Es ändert weder Lastenheft, Authoring Receipt, Series-Lifecycle noch
Delivery Authority und startet keine Folgephase. / *This complete Single
review assesses only the updated RAW-08. It changes neither the intake,
Authoring Receipt, Series lifecycle, nor delivery authority and starts no
downstream phase.*

## Ergebnis / Outcome

Die drei früher offenen Decisions sind nun vollständig beantwortet. IAD801
bindet kanonische versionierte JSON-Persistenz, atomare Veröffentlichung und
Recovery am letzten gültigen Receipt. IAD802 bindet Attestation Envelope,
Trust Policy und fail-closed Prüfung. IAD803 bindet Projekt-Receipts,
90-tägige operative Evidence, zwölfmonatige Sicherheits- und
Fehlschlagevidence, Legal Hold und Lösch-Receipts. Target, Decision Register,
Authoring Receipt und Series-Hash stimmen überein. / *The three former open
decisions are now fully answered and consistently bound across target,
Decision Register, Authoring Receipt, and Series hash.*

`IR801` und alle drei Reviewfragen sind damit erledigt. `Ready` ist dennoch
nicht zulässig: `IR802` bis `IR806` bestehen in aktualisierter Form fort. Es
fehlen reproduzierbare Verträge und Fixtures, vollständige DE/EN-Texte und
Begriffserklärungen, Querschnittsanwendbarkeit, typisierte Handoffs sowie eine
fail-closed Prompt-/Authority-Ausrichtung. Das Ergebnis lautet deshalb
`NeedsRemediation`. / *IR801 and all three questions are resolved. Ready is
still blocked by five High findings covering reproducible evidence, language
and terminology, cross-cutting applicability, typed handoffs, and prompt or
authority alignment.*

## Auflösung der früheren Klärung / Resolution of the former clarification

| Finding oder Frage / Finding or question | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| `IR801` | Erledigt / Resolved | IAD801–IAD803 sind im Target, Decision Register und Receipt beantwortet; null offene Decision-IDs. / Decisions are bound with zero open IDs. |
| `IRQ801` | Beantwortet / Answered | Versioniertes kanonisches JSON unter `evidence/workflow/<workflow-id>/`, atomare Veröffentlichung, Receipt-Recovery. / Versioned canonical JSON, atomic publication, and receipt recovery. |
| `IRQ802` | Beantwortet / Answered | Versioniertes Attestation Envelope, Trust Policy und fail-closed Prüfung. / Versioned attestation envelope, trust policy, and fail-closed verification. |
| `IRQ803` | Beantwortet / Answered | Projektlebensdauer für Governance-Receipts, 90 Tage operativ, zwölf Monate Security/Failure, Legal Hold und Lösch-Receipt. / Project receipts, 90-day operational and twelve-month security or failure retention, legal hold, and deletion receipt. |

## Findings / Findings

| ID | Severity | Kategorie / Category | Disposition | Nachweis / Evidence |
|---|---|---|---|---|
| IR802 | High | Anforderungen und Evidence / Requirements and evidence | NeedsRemediation | Kein versionierter Workflow-/Knowledge-Package-Vertrag, keine Zustandsmatrix, Schemas, Fixtures, Validatoren, Reason Codes, Sollausgaben oder Exitcodes. / No complete reproducible contract or validation evidence. |
| IR803 | High | Sprache und Terminologie / Language and terminology | NeedsRemediation | Wesentliche normative Abschnitte sind keine vollständigen DE/EN-Paare; technische und Spec-Kit-Begriffe bleiben unerklärt. / Normative bilingual pairs and first-use explanations remain incomplete. |
| IR804 | High | Querschnittsanwendbarkeit / Cross-cutting applicability | NeedsRemediation | Public Content, WCAG 2.2 AA, Plattform-, Node- und Supply-Chain-Grenzen sowie messbare Evidence fehlen. / Cross-cutting boundaries and measurable evidence remain incomplete. |
| IR805 | High | Handoff und Abhängigkeit / Handoff and dependency contract | NeedsRemediation | RAW-05/06-Eingaben, RAW-09-Ausgabe und Child-Intakes besitzen keine vollständigen typisierten Verträge. / Inputs, output, and child-intakes lack complete typed contracts. |
| IR806 | High | Prompt und Delivery Authority / Prompt and delivery authority | NeedsRemediation | Der Autonomous-Prompt fordert MergeAndSync ohne alle separaten aktuellen Authority-Gates fail-closed zu verlangen. / The Autonomous prompt does not fail closed on every required current authority. |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass mit IR803 | Workflow-Ownership und Ausschluss der Produktzustandslogik sind erkennbar; vollständige bilinguale Grenzen fehlen. / Ownership is visible; complete bilingual boundaries are absent. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Fail | Das angegebene Vorwissen deckt die zahlreichen Governance-, Evidence- und Spec-Kit-Begriffe nicht ab. / Stated prior knowledge does not cover the unexplained terms. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass mit IR803/IR806 | Decisions und `Eligible` sind korrekt getrennt; geordnete bilinguale Next Action und vollständige Prompt-Gates fehlen. / Decisions are coherent; ordered next action and prompt gates remain incomplete. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Fail | Persistenz, Attestation und Retention sind deterministisch, der übrige Workflow-Vertrag besitzt aber keine Zustands- und Schemagrenzen. / Decisions are deterministic, but the workflow contract is not. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Fail | AC-001/002 binden keine ausführbaren Fixtures, Validatoren, Reason Codes, Sollausgaben oder Exitcodes. / Acceptance lacks executable evidence. |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Fail | RAW-05/06/09 und Child-Intakes sind nicht vollständig typisiert; Prompt-Authority bleibt unvollständig. / Handoffs and prompt authority are incomplete. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Fail | Signatur, Secrets, Retention und Legal Hold sind geregelt; A11Y, Plattform, Node, Public Content und Supply Chain fehlen. / Several cross-cutting areas remain absent. |
| Prompt-Ausrichtung / Prompt alignment | Fail | MergeAndSync wird ohne alle separaten aktuellen Authority-Gates angefordert. / MergeAndSync lacks complete current-authority gates. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass | Datenminimierung ist normativ gebunden; UTF-8, Target-Hash und begrenzter Musterscan bestehen. / Data minimisation, encoding, hash, and bounded scan pass. |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, sechs
  gebundene Quellen. / *Both authoring validators pass with six bound sources.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, 14 Ziele, ein Root,
  14 Abhängigkeiten und RAW-08 als einziger `Eligible`-Kandidat. / *Both Series
  validators pass and RAW-08 is the sole eligible candidate.*
- Das neue Review-Ergebnis besteht den Bash- und PowerShell-Validator mit
  einem aktuellen Ziel und fünf High-Findings. / *Both review validators pass
  with one current target and five High findings.*
- Target und Receipt sind UTF-8; normalisierter Target-Hash, Request-Hash und
  Git-Blob sind reproduzierbar. / *Encoding and content bindings are
  reproducible.*
- Der begrenzte Secret-/Personendaten-Musterscan und `git diff --check` melden
  keinen neuen Treffer. / *The bounded sensitive-data and whitespace checks
  report no new finding.*
- Für RAW-08 existieren gerade keine ausführbaren Vertragsfixtures; diese
  Abwesenheit ist die Negativ-Evidence für `IR802`. / *The current absence of
  executable RAW-08 contract fixtures is the negative evidence for IR802.*

## Serien- und Authority-Auswirkung / Series and authority impact

Dieses Single Review ändert den Series-Lifecycle nicht. RAW-08 bleibt
`Eligible`, ist mit `NeedsRemediation` aber nicht startfähig. Das Ergebnis
erteilt keine Reparatur-, Specify-, Implementierungs-, Governance-Write-,
Remote-, Merge-, Bypass-, Provider-, Preset-, Promotion-, GitHub- oder Level-0-
Autorität. RAW-09 bleibt durch RAW-08 und seine eigenen Decisions blockiert. /
*The review changes no Series lifecycle. RAW-08 remains Eligible but cannot
start with NeedsRemediation, and no downstream authority is granted.*

Die AOC-weite Review-Sperre bleibt geschlossen: Zwölf der vierzehn aktiven
Lastenhefte besitzen aktuelle formal validierte Ready-Evidence; RAW-08 und
RAW-09 fehlen weiterhin. / *The AOC-wide review gate remains closed at twelve
of fourteen Ready Single reviews.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich angeforderte
vollständige RAW-08-Single-Review; Owner ist `RAW-08 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Das Lastenheft,
Authoring Receipt und Series-Artefakte bleiben unverändert. / *Decision:
UpdateRequired. The requested Single review is the source and RAW-08 intake
review is the owner. The request, machine-readable result, and this report are
new; target, Authoring Receipt, and Series artifacts remain unchanged.*

## Risiken, Fragen und Nicht-Autorität / Risks, questions, and non-authority

Es wurden keine Risiken akzeptiert, keine Operator-Ausnahmen erteilt und keine
materiellen Fragen offengelassen. Zusammenfassung: Critical `0`, High `5`,
Medium `0`, Low `0`. Dieses Review genehmigt keine Reparatur oder Folgephase. /
*No risks, exceptions, or material questions remain. The review authorises no
repair or downstream phase.*

## Exakte nächste Aktion / Exact next action

Der nächste schreibende Schritt benötigt einen ausdrücklich begrenzten
Repair-Auftrag für `IR802` bis `IR806`; IAD801 bis IAD803, Scope,
Abhängigkeiten und Delivery Authority bleiben unverändert. / *The next writing
step requires explicit bounded repair authority for IR802 through IR806 while
preserving the confirmed decisions and boundaries.*

```text
$speckit-intake-repair specs/intake-review-results/raw-08-workflow-engine-2026-08-08.json
```
