# Specify-Qualitätsprüfung · RAW-01 / Specify quality review

**Datum / Date** 2026-11-27

**Feature** [Spezifikation / Specification](../spec.md)

**Prüfgrundlage / Review input** [Aktiver Intake / Active intake](../../../requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) · [RAW-Gate](../../../specs/intake-series/aoc-raw-features/review-gate.json)

## Inhalt / Content quality

- [x] Die Anforderungen beschreiben den fachlichen Nutzen und beobachtbare Ergebnisse für Lernende, Fachkräfte und nachgelagerte Verbraucher. / Requirements describe user value and observable outcomes for learners, practitioners and downstream consumers.
- [x] Die Spezifikation erklärt Git-, Snapshot- und Zugriffsbegriffe bei der ersten Verwendung. / The specification explains Git, snapshot and access concepts on first use.
- [x] Alle Pflichtabschnitte sind ausgefüllt. / All mandatory sections are complete.
- [x] Die fachlichen Anforderungen geben keine Implementierungsstruktur oder API vor. JSON mit JSON Schema ist der geforderte Austauschvertrag. `net11.0`, C# 15, xUnit.net v3 und Microsoft Testing Platform v2 stehen als ausdrücklich beauftragte Vertragsgrenzen bei den Randbedingungen. / Domain requirements prescribe no implementation structure or API. JSON with JSON Schema is the required exchange contract. The expressly required framework, language and test platform appear in the constraints.

## Anforderungen und Abnahme / Requirements and acceptance

- [x] Alle fachlichen Anforderungen sind prüfbar und durch mindestens ein Szenario abgedeckt. / All domain requirements are testable and covered by at least one scenario.
- [x] Die Erfolgskriterien sind messbar und beschreiben fachliches Verhalten unabhängig von der technischen Realisierung. / Success criteria are measurable and describe outcomes independently of implementation.
- [x] Positive Fälle, Fehlerfälle, unzulässige Wurzeln, veraltete Daten und unbekannte Schemaversionen sind abgedeckt. / Positive cases, failures, unauthorised roots, stale data and unknown schema versions are covered.
- [x] Umfang, Abhängigkeiten und Annahmen sind beschrieben. / Scope, dependencies and assumptions are documented.
- [x] Der fachliche Abgleich mit dem Intake enthält keine offenen Klärungsmarker. / Domain review against the intake found no unresolved clarification markers.

| Anforderungsgruppe / Requirement group | Prüffall / Scenario | Intake-Abnahme / Intake acceptance |
|---|---|---|
| FR-001 bis / through FR-003 | US-1, US-3 und der Grenzfall für Schreibversuche / and the write attempt edge case | AC-001, AC-002, AC-007 |
| FR-004 und / and FR-005 | US-2.2, US-3.1–3.2 | AC-002, AC-003 |
| FR-006 | US-2.1, US-3.2 | AC-005 |
| FR-007 | US-1.2, US-3.3 | AC-007 |
| FR-008 | US-2.1, US-3 und Plattformvergleich / and platform comparison | AC-008 |
| Bindende Randbedingungen / Binding constraints | Plattformneutralität, plattformübergreifender Testaufruf und stabile Paketübernahme / Platform neutrality, portable test invocation and stable package adoption | AC-004, AC-006, AC-009 |

## Governance und Nachweise / Governance and evidence

DE: Die folgende Prüfung erfasst den Stand von Specify. Die Prüfinstanz ist
Codex für die Spezifikationsprüfung. AOC-Maintainer und die jeweiligen
Fachverantwortlichen prüfen die benannten Nachweise, sobald ein späterer
Auftrag die jeweilige Fläche einführt.

EN: The following assessment records the Specify stage. Codex reviewed the
specification. AOC maintainers and the responsible reviewers verify the listed
evidence when a later task introduces the relevant surface.

| Regel oder Preset / Rule or preset | Anwendbarkeit und Nachweis / Applicability and evidence |
|---|---|
| Security Governance · NIST SSDF, CWE Top 25, speichersichere Sprache / memory-safe language | **Applicable.** C# ist in der Konstitution zugelassen. Wurzelgrenzen und sichere Fehlerausgaben sind prüfbar festgelegt, insbesondere Pfadbegrenzung (CWE-22) und Daten in Fehlermeldungen (CWE-209). Der Security Owner bestätigt das C#-Secure-Coding-Profil, Bedrohungsmodell und Negativnachweise vor späterer Abnahme in `docs/security/`. / C# is constitution-approved. Root confinement and safe errors have explicit requirements. The security owner reviews secure C# guidance, threat modelling and negative evidence before later acceptance in the default security evidence location. |
| OWASP ASVS, AI-SBOM, SBOM/VEX, SLSA, OpenSSF Scorecard | **N/A für Specify / for Specify.** Kein Web-, HTTP- oder Authentifizierungsdienst, keine KI im Produkt und keine Paketübernahme, Build-Lieferkette oder Veröffentlichung in diesem Schritt. KI dient der Entwicklung. Bei neuen Diensten, KI-Komponenten, Abhängigkeiten oder Release-Absicht neu bewerten. Vor erster Paketübernahme gilt AC-009. Bei späterer Lieferkette sind SBOM/VEX, SLSA und Abhängigkeitsprüfung in `docs/security/supply-chain-evidence.md` zu bewerten. / This step adds no web, HTTP or authentication service, product AI, dependency, build supply chain or release. AI is used for development. Reassess at those triggers and record supply-chain evidence before later adoption or release. |
| Architecture Governance und iSAQB / and iSAQB | **Applicable.** Die lokale Leseberechtigung und die Grenze zur Konsolenausgabe sind in FR-001, FR-003 und FR-007 erfasst. Vor Realisierung dominanter Risiken führt der Architecture Owner eine strukturierte Bedrohungsanalyse (STRIDE und Vertraulichkeit, Integrität, Verfügbarkeit) durch und bewertet CAPEC, Sicherheits-ADR und Querschnittskonzepte in `docs/architecture/` und `docs/security/`. Die Akzeptanzfälle liefern die prüfbaren Qualitätsszenarien. / The specification identifies the local read boundary and output boundary. Before implementing high-risk paths, architecture reviews threats, attack-pattern relevance, security decisions and cross-cutting concepts using the named evidence locations. Acceptance cases define the quality scenarios. |
| Zero Trust, OWASP SAMM, BSI C3A und C5 | **N/A für Specify / for Specify.** Kein verteilter Zugriff, Cloud-Dienst, Providerbetrieb oder Programmreifegrad-Assessment. Neu bewerten bei einem solchen Auftrag. / Specify introduces no distributed access, cloud service, provider operation or maturity assessment. Reassess if one enters scope. |
| Accessibility Governance | **Applicable.** Textprüfung für Deutsch/Englisch, Einstieg ab dem ersten Ausbildungsjahr und verständliche Zustände ohne visuelle Hinweise findet in dieser Checkliste statt. Der A11Y-Owner weist später die anwendbaren WCAG-2.2-AA-Kriterien für die tatsächliche Konsolenausgabe unter `docs/accessibility/` nach. / This checklist records the German/English, learner and text-first review. The accessibility owner verifies applicable AA criteria against the actual console output later. |
| Cross-Platform Governance | **Applicable** für gleiche fachliche Bedeutung auf macOS, Linux und Windows. **N/A für Skriptparität / for script parity.** Specify und der Snapshot-Vertrag führen kein Skriptwerkzeug ein. Bei einem späteren Skriptauftrag sind Bash und PowerShell, Hilfe und Vorschau-Parität zu bewerten. / Platform meanings must match. No script-shaped tool is introduced. Review paired scripts, help and preview parity if a later task adds one. |
| Agent Parity Governance, Autonomous Run und Parallel Autonomous Run | **N/A für Änderungen in Specify / for changes in Specify.** Die fünf gepflegten Agentenflächen, gemeinsame Vorlagen und die Konstitution behalten ihre bestehenden Inhalte. Ein eigenständiger Specify-Lauf verwendet keinen autonomen oder parallelen Modus. Neu bewerten bei Änderung gemeinsamer Regeln oder eigener Laufautorität. / The five maintained agent surfaces, shared templates and constitution retain their current content. This standalone Specify step uses no autonomous or parallel workflow. Reassess if shared rules or run authority change. |
| Intake Authoring, Review und Sequencing | **Applicable.** Der aktuelle Intake-Hash, die Receipts, das Ready-Einzelreview und der Serienstatus sind im RAW-Gate gebunden. Änderungen an ihnen erfordern eine neue Gate-Prüfung. / The RAW gate binds the current hashes, receipts, Single review and lifecycle status. Re-run it after changes. |
| Regulatorische Anwendbarkeit / Regulatory applicability | **Applicable** als Prüfung der Entwurfsgrenzen. Einzelne Organisationsfragen bleiben **Open** bis zu einer konkreten Betriebs- oder Veröffentlichungsentscheidung. / Applicable as a design-scope review. Organisation-specific questions remain open until concrete operating or distribution decisions. [Security-Nachweis / Security record](../../../docs/security/raw-01-regulatory-applicability.md) |
| Projektstatistik / Project statistics | **N/A für diesen Schritt / for this step.** Specify allein schließt kein Feature und keine Implementierungsphase ab. Nach einem späteren Abschluss anhand der Repository-Regel neu bewerten. / Specify completes neither a feature nor an implementation phase. Reassess after later completion per repository policy. |

## Dokumentationsauswirkung / Documentation impact

**Entscheidung / Decision** `UpdateRequired`

DE: RAW-01 ändert die verbindliche Vertragsdokumentation. Kanonische Quelle ist
der aktuelle Intake mit seinem Einzelreview. Der AOC-Maintainer pflegt Intake,
Serienreihenfolge und Spezifikation als Level-2-Quelldokumentation ohne
Home-Sync. Lernende beginnen beim Glossar und den Szenarien, Fachkräfte und
Maintainer können von dort zu Akzeptanzkriterien und Nachweisen wechseln.
Beide Sprachen stehen im selben Dokument. Die Dokumentprüfung belegt die
Beispielabdeckung und Sprachparität. Die praktischen Plattformbeispiele
werden bei Realisierung auf den Zielplattformen geprüft. Neu bewerten, wenn
eine Wurzel-, Snapshot-, Datenschutz- oder Plattformgrenze geändert wird.

EN: RAW-01 changes the binding contract documentation. The current intake
and its Single review are the authoritative source. The AOC maintainer owns
the intake, series order and specification as level-2 source documentation
with no Home sync. Learners start at the glossary and scenarios. Practitioners
and maintainers can follow through to acceptance and evidence. Both languages
appear in one document. Document review verifies scenario coverage and
language parity. Practical examples are checked on the target platforms
during implementation. Reassess if a root, snapshot, privacy or platform
boundary changes.
