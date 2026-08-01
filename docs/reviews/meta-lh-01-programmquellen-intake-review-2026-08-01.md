# Einzelreview META-LH-01 – Programmquellen / Single Review META-LH-01 – Programme Sources

## Identität / Identity

- Review-ID: `3484ab5e-f374-4a57-be11-6ff510277f22`
- Modus: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis: `NeedsRemediation`
- Review-Zeitpunkt: `2026-07-31T22:49:47Z`
- Repository-HEAD: `d81ca316f6a01599008363461dbf0060b497de29`
- Ziel: `requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md`
- Normalisierter SHA-256: `4429ca8c4c132fac83a840f5c29f8361a01c3c233e5805d4a0c4055931eb9fe7`
- Git-Blob: `e21e94530c36a9cc5347ed1ab89e24bffcadf7b6`
- Request: `specs/intake-review-requests/meta-lh-01-programmquellen-2026-08-01.json`
- Request-SHA-256: `7545da0398031e826179cb5552950adb0204c462a2beb0bd13e2dc2de362060c`

*This is an independent single-intake review of one target. It does not broaden
the scope to the series and starts no Specify or autonomous run.*

## Ergebnis / Outcome

META-LH-01 ist fachlich klar abgegrenzt und besitzt eine aktuelle,
hashgebundene Authoring Receipt. Drei High Findings und ein Medium Finding
verhindern jedoch den Status `Ready`. Die Abweichungen sind eindeutig
reparierbar und benötigen keine zusätzliche fachliche Entscheidung; deshalb
lautet das Ergebnis `NeedsRemediation` statt `NeedsClarification`.

*META-LH-01 has a clear boundary and a current, hash-bound authoring receipt.
Three High findings and one Medium finding prevent a `Ready` outcome. They are
remediable without another material decision, so the outcome is
`NeedsRemediation`, not `NeedsClarification`.*

## Findings / Findings

| ID | Severity | Kategorie / Category | Disposition | Nachweis / Evidence |
|---|---|---|---|---|
| IR101 | High | Sprache und Terminologie / Language and terminology | NeedsRemediation | Das Profil verlangt vollständiges DE-first/EN-second und Erklärungen oder Glossarverweise beim ersten Gebrauch. FR-002 bis NFR-002, Risiken und Akzeptanzkriterien sind nicht durchgängig zweisprachig; Spec-Kit- und Programmbegriffe bleiben trotz Zielgruppe ohne Projektgeschichte unerklärt. / The profile requires complete paired language and first-use explanations or glossary links; several normative sections and terms do not comply. |
| IR102 | High | Prompt-Ausrichtung / Prompt alignment | NeedsRemediation | Scope und Nicht-Autorität schließen Specify, Plan, Tasks, Code, Remote Writes und nachgelagerte Spec-Kit-Autorität aus. Der aktivierte Autonomous-Prompt fordert dennoch einen vollständigen `MergeAndSync`-Lauf ohne gleichwertige Grenzen. / The enabled autonomous prompt exceeds the normative scope and authority boundary. |
| IR103 | High | Anforderungsnachweis / Requirements evidence | NeedsRemediation | FR-002 verlangt auch für neue Findings Owner, Ziel, Akzeptanz, positive/negative Evidence, Status und Restlücke. Die Tabelle RF-19 bis RF-21 weist Ziel, positive/negative Evidence und Restlücke nicht ausdrücklich aus. / The RF-19 through RF-21 table does not expose every field required by FR-002. |
| IR104 | Medium | Anwendbarkeit / Applicability | NeedsRemediation | Plattform- und Supply-Chain-Anwendbarkeit sind für dieses dokumentationsbezogene Intake weder als anwendbar noch begründet als `N/A` festgelegt. / Platform and supply-chain applicability are not explicitly decided or marked `N/A` with a rationale. |

## Fragen und Entscheidungen / Questions and decisions

Es bestehen keine offenen Reviewfragen und keine akzeptierten Risiken. Die
Findings dürfen nicht durch Annahmen oder Admin-Bypass umgangen werden.

*There are no open review questions and no accepted risks. Assumptions or an
admin bypass cannot waive the findings.*

## Coverage / Coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass | Explizit und widerspruchsfrei, abgesehen vom separat bewerteten Prompt. / Explicit and internally clear apart from the separately assessed prompt. |
| Vorwissen / Prior knowledge | Pass | Keine Spec-Kit- oder Level-0-Geschichte wird vorausgesetzt. / No Spec Kit or level-0 history is assumed. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Fail | Siehe IR101. / See IR101. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first status, dependencies, decisions, and next action | Pass | Status, Root-Rolle, Entscheidungsstand und Review-Nächster-Schritt sind über Target und aktuelle Receipt gebunden. / Status, root role, decision state, and review next action are bound by the target and current receipt. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Fail | FR-002 ist prüfbar, aber die gebundene Evidence erfüllt den vollständigen Feldvertrag nicht; siehe IR103. / FR-002 is testable, but its evidence does not satisfy the complete field contract; see IR103. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Fail | Siehe IR103. / See IR103. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependency, authority, delivery, risks, and follow-up | Fail | Der Autonomous-Prompt überschreitet die normative Authority; siehe IR102. / The autonomous prompt exceeds normative authority; see IR102. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Security, privacy, A11Y, platform, and supply chain | Fail | Secret Scan und öffentliche Inhaltsgrenze bestehen; Plattform und Supply Chain bleiben offen, siehe IR104. / Secret scanning and public-content boundaries pass; platform and supply-chain applicability remain open, see IR104. |
| Referenzen und Prompt-Parität / References and prompt parity | Fail | Quellenbindung ist aktuell; der Autonomous-Prompt ist nicht scopegleich, siehe IR102. / Source binding is current; the autonomous prompt is not scope-equivalent, see IR102. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass | Strict UTF-8, kein NUL und Gitleaks ohne Fund. / Strict UTF-8, no NUL, and no Gitleaks finding. |

## Validierungsnachweise / Validation evidence

- Die Governance-Konfiguration Schema 2.0 ist `Aligned`. / *The schema-2.0 governance configuration is aligned.*
- Die Authoring Receipt ist aktuell und bindet Ziel und Source Pack. / *The authoring receipt is current and binds the target and source pack.*
- Ziel- und Source-Pack-Hashes stimmen mit den Receipts überein. / *Target and source-pack hashes match their receipts.*
- Gitleaks meldet keinen Fund im Reviewziel. / *Gitleaks reports no finding in the review target.*
- Der maschinenlesbare Review-Validator meldet `PASS`. / *The machine-readable review validator reports `PASS`.*

## Restrisiko / Residual risk

Keine Risiken wurden akzeptiert. Zusammenfassung: `Critical 0`, `High 3`,
`Medium 1`, `Low 0`. Zielanzahl: `1`; Workeranzahl: `0`.

*No risks were accepted. Summary: `Critical 0`, `High 3`, `Medium 1`, `Low 0`.
Target count: `1`; worker count: `0`.*

## Exakte nächste Aktion / Exact next action

Zulässig ist eine ausdrücklich autorisierte, eng begrenzte Reparatur von
META-LH-01 und der betroffenen RF-19-bis-RF-21-Evidence. Danach müssen Target
und Authoring Receipt neu hashgebunden und dieses Single Review erneut
ausgeführt werden. Dieses Review startet weder Specify noch einen autonomen
Lauf.

*The exact next action is an explicitly authorised, narrowly scoped repair of
META-LH-01 and the affected RF-19-through-RF-21 evidence. Rebind the target and
authoring receipt, then rerun this single review. This review starts neither
Specify nor an autonomous run.*
