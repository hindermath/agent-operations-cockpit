# Anforderungsqualitätscheckliste: Series Eligibility / Requirements Quality Checklist: Series Eligibility

**Zweck / Purpose**: Formale Prüfung vor der Planung mit der Tiefe eines Release-Qualitätsgates; bewertet wird die Anforderungsqualität. / Formal pre-plan review at release-gate depth; assesses requirements quality.
**Erstellt / Created**: 2026-09-13
**Feature / Feature**: [Akzeptierte Spezifikation / Accepted specification](../spec.md)
**Zielgruppe / Audience**: Peer-Reviewer / Peer reviewer
**Grundlage / Basis**: [Akzeptiertes Intake / Accepted intake](../../../requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md), [Kriterienvertrag / Criteria contract](../../../requirements/baseline/series-eligibility-contract.json)

Diese Checkliste wurde mit `speckit.checklist` erstellt und vollständig gegen die akzeptierte Spezifikation bewertet. `[x]` bedeutet, dass die schriftliche Anforderung den genannten Qualitätsaspekt erfüllt. Es bedeutet keine erfolgreiche Implementierungsprüfung oder Startfreigabe. Alle Fragen, Bewertungen und Gründe stehen Deutsch zuerst und Englisch danach. / *This checklist was created with speckit.checklist and fully assessed against the accepted specification. A checked box means the written requirement meets the named quality aspect. It does not mean implementation validation passed or execution is authorised. Questions, assessments, and reasons appear German first and English second.*

Eligibility bedeutet geprüfte Eignung; Authority bedeutet aktuelle ausdrückliche Autorität. Ein DAG ist ein gerichteter Graph ohne Zyklus. Root bezeichnet eine Wurzel ohne Vorgänger. Traceability bedeutet Rückverfolgbarkeit zum Quellenabschnitt; alle Angaben `Spec §` beziehen sich auf die verlinkte Spezifikation. / *Eligibility means assessed suitability; authority means current explicit permission. A DAG is a directed graph without cycles. A root has no predecessor. Traceability links an item to its source section; every Spec reference points to the linked specification.*

## Vollständigkeit der Kriterien / Criteria Completeness

- [x] CHK001 Sind genau neun eigenständige Kriterien mit eindeutigen Vertragsschlüsseln vorgeschrieben? / Are exactly nine separate criteria required with unique contract keys? [Completeness, Spec §FR-002]
  - Bestanden: Die Tabelle nennt `authority`, `sideEffects`, `reversibility`, `writeScope`, `decisions`, `integration`, `review`, `abort`, `recovery` einzeln. / Pass: The table names all nine keys separately.
- [x] CHK002 Gilt die exakte Kardinalität für jede Einstufung und jede Fixture, einschließlich fehlender, doppelter, zusammengelegter und zusätzlicher Kriterien? / Does exact cardinality apply to every classification and fixture, including missing, duplicate, merged, and extra criteria? [Coverage, Spec §FR-002, §US1.3, §SC-001]
  - Bestanden: Acht und zehn Kriterien sowie Duplikate und Zusammenlegung sind ausdrücklich unzulässig. / Pass: Eight or ten criteria, duplicates, and merging are explicitly disallowed.
- [x] CHK003 Sind Side Effects, Reversibilität und Write Scope inhaltlich unterscheidbar beschrieben? / Are side effects, reversibility, and write scope defined as distinct concepts? [Clarity, Spec §FR-002]
  - Bestanden: Zustandsänderung, kontrollierte Rücknahme und veränderbare Pfade/Ressourcen haben getrennte Aussagen. / Pass: State change, controlled reversal, and writable paths/resources have separate statements.
- [x] CHK004 Sind Integration und gemeinsames Review als getrennte Planungsanforderungen benannt? / Are integration and combined review named as separate planning requirements? [Completeness, Spec §FR-002, §FR-003, §US1.1]
  - Bestanden: Zusammenführungsweg und Consolidation Review, also gemeinsame Ergebnisprüfung, bleiben eigenständige Kriterien. / Pass: The path for combining results and consolidation review remain separate criteria.

## Klarheit von Modus und Autorität / Mode and Authority Clarity

- [x] CHK005 Sind die sechs zulässigen Modi abschließend benannt und Modus `blocked` sowie Ergebnis `Blocked` getrennt? / Are the six permitted modes exhaustively named and mode blocked separated from outcome Blocked? [Clarity, Spec §FR-001]
  - Bestanden: Eine geschlossene Modusliste und getrennte Felder verhindern die Gleichsetzung. / Pass: A closed mode list and separate fields prevent conflation.
- [x] CHK006 Definiert die Spezifikation aktuelle ausdrückliche Authority mit passender Grenze statt einer aus Historie abgeleiteten Freigabe? / Does the specification require current explicit authority with matching bounds rather than permission inferred from history? [Clarity, Spec §FR-002, §FR-007, §US1.3]
  - Bestanden: Aktueller Auftrag ist erforderlich; historische Receipt-Autorität ist nur Herkunftsnachweis. / Pass: A current instruction is required; historical receipt authority is provenance only.
- [x] CHK007 Werden Eligibility, Review, Lifecycle, Delivery-Modus und konkrete Startautorität widerspruchsfrei getrennt? / Are eligibility, review, lifecycle, delivery mode, and actual start authority consistently separated? [Consistency, Spec §FR-007, §US3.1]
  - Bestanden: FR-007 nennt alle fünf Achsen; US3 verlangt ihre getrennte Erklärung. / Pass: FR-007 names all five axes; US3 requires separate explanations.
- [x] CHK008 Ist die fachliche Einstufung `manual-assisted` mit einer separat autorisierten automatisierten Phase vereinbar beschrieben? / Is the manual-assisted domain classification described consistently with a separately authorised automated phase? [Consistency, Spec §Annahmen, Abhängigkeiten und Ausschlüsse, §Autonomer Lauf und Abnahmegrenzen]
  - Bestanden: Automatisiertes Specify ändert die Intake-Einstufung nicht; gespeichertes `MergeAndSync` ist Kontext. Specify-Sätze beschreiben den früheren Phasenauftrag. / Pass: Automated Specify does not change intake classification; stored MergeAndSync is context. Specify statements describe the earlier phase instruction.

## Konsistenz der Parallelklassifikation / Parallel Classification Consistency

- [x] CHK009 Ist die Freigabebedingung für Parallelität als gemeinsame Erfüllung aller erforderlichen Aussagen formuliert? / Is parallel eligibility defined as requiring all necessary statements together? [Completeness, Spec §FR-003, §US1.1]
  - Bestanden: Aktuelle Authority, disjunkte Writes, keine gemeinsame offene Decision, Review, Abort/Recovery und neun vollständige konsistente Kriterien sind erforderlich. / Pass: Current authority, disjoint writes, no shared open decision, review, abort/recovery, and nine complete consistent criteria are required.
- [x] CHK010 Sind gemeinsame Writes und gemeinsame offene Decisions als eigenständige Blocker formuliert? / Are shared writes and shared open decisions defined as independent blockers? [Coverage, Spec §FR-003, §US1.2, §SC-001]
  - Bestanden: Zwei getrennte Negativ-Fixtures binden beide Risiken; disjunkte Dateien allein reichen nicht. / Pass: Two separate negative fixtures bind both risks; disjoint files alone are insufficient.
- [x] CHK011 Ist das Ergebnis einer fehlgeschlagenen Parallelprüfung eindeutig, ohne unbelegte automatische Ersatzfreigabe? / Is a failed parallel assessment's outcome clear without an unsupported automatic fallback approval? [Clarity, Spec §FR-001, §FR-003]
  - Bestanden: Das Ergebnis muss `Blocked` sein; der geprüfte Parallelmodus bleibt erkennbar. / Pass: The outcome must be Blocked and the assessed parallel mode remains identifiable.
- [x] CHK012 Ist ausdrücklich festgelegt, dass eine gültige Fixture und eine positive Empfehlung keinen realen Start autorisieren? / Is it explicit that a valid fixture and a positive recommendation do not authorise a real start? [Consistency, Spec §FR-003, §FR-006, §FR-007]
  - Bestanden: Fixture-Freigabe, Abfrage und Startautorität sind getrennt begrenzt. / Pass: Fixture approval, queries, and start authority have separate bounds.

## Graph-, Reihenfolge- und Hashintegrität / Graph, Order, and Hash Integrity

- [x] CHK013 Sind DAG, explizite Roots, typisierte Kanten, exakte stabile Reihenfolge und Lifecycle als Manifestanforderungen vollständig benannt? / Are the DAG, explicit roots, typed edges, exact stable order, and lifecycle fully named as manifest requirements? [Completeness, Spec §FR-004, §US2.1]
  - Bestanden: FR-004 nennt alle Bindungen und verlangt einen gerichteten zyklusfreien Graphen. / Pass: FR-004 names all bindings and requires a directed acyclic graph.
- [x] CHK014 Ist die Hashbindung auf den bestehenden Normalisierungsvertrag zurückgeführt und Drift als Blocker definiert? / Is hash binding tied to the existing normalization contract and drift defined as a blocker? [Traceability, Spec §FR-004, §FR-005, §Annahmen, Abhängigkeiten und Ausschlüsse]
  - Bestanden: Normalisierter SHA-256 mit UTF-8-/Zeilenendenvertrag und verlinkten kanonischen Quellen; kein neuer Hashvertrag. / Pass: Normalized SHA-256 follows the UTF-8/line-ending contract and linked canonical sources; no new hash contract.
- [x] CHK015 Sind Zyklus, fehlende Root, Hash-Drift und mehrfach deklarierte Eligibility mit eindeutiger Disposition beschrieben? / Are cycles, missing roots, hash drift, and multiple declared eligibility given clear dispositions? [Coverage, Spec §US2.2, §FR-005, §SC-002]
  - Bestanden: Alle vier Fälle blockieren vor einer Empfehlung; automatische Reparatur ist ausgeschlossen. / Pass: All four cases block before a recommendation; automatic repair is excluded.
- [x] CHK016 Sind verpflichtende Vorgänger und historische Dateinamen ohne Gleichsetzung von Snapshot und aktuellem Zustand geregelt? / Are mandatory predecessors and historical filenames governed without treating a snapshot as current state? [Dependencies, Spec §US2.3, §Annahmen, Abhängigkeiten und Ausschlüsse]
  - Bestanden: META-LH-01/02/03 sind Pflichtvorgänger; historische Namen benötigen belegte Lifecycle-Bindung, Manifest und Reihenfolge sind aktuelle Quellen. / Pass: META-LH-01/02/03 are mandatory predecessors; historical names need proven lifecycle bindings, while manifest and order are current sources.

## Lesende Abfragen und messbare Abnahme / Read-only Queries and Measurable Acceptance

- [x] CHK017 Sind die verbotenen Mutationen und Folgeaktionen für `status` und `next` vollständig abgegrenzt? / Are prohibited mutations and downstream actions fully bounded for status and next? [Completeness, Spec §FR-006, §US3.2]
  - Bestanden: Dateien, Receipts, Lifecycle, Laufzustand sowie Worker, Worktrees, Specify, Implementierung und Remote-Aktionen sind ausdrücklich erfasst. / Pass: Files, receipts, lifecycle, run state, workers, worktrees, Specify, implementation, and remote actions are explicitly covered.
- [x] CHK018 Sind die erlaubten Ausgaben von `status` und `next` sowie Fälle ohne Kandidaten klar beschrieben? / Are permitted status/next outputs and cases without a candidate clearly described? [Scenario Coverage, Spec §US3.1, §US3.2, §FR-005]
  - Bestanden: Getrennte Statusachsen, Kandidat oder konkrete Blocker und genau eine sichere nächste Aktion; kein erfundener Nachfolger. / Pass: Separate status axes, a candidate or specific blockers, and one safe next action; no invented successor.
- [x] CHK019 Ist die Erstellung eines Planungs-Receipts von lesenden Abfragen und deren Autorität getrennt? / Is planning-receipt creation separated from read-only queries and their authority? [Consistency, Spec §FR-008]
  - Bestanden: Eingaben und Ergebnis werden gebunden; Erstellung ist ausschließlich separat autorisiertes Authoring. / Pass: Inputs and outcome are bound; creation belongs only to separately authorised authoring.
- [x] CHK020 Sind No-write, No-start und Wiederholbarkeit objektiv messbar formuliert? / Are no-write, no-start, and repeatability requirements objectively measurable? [Measurability, Spec §SC-003, §US3]
  - Bestanden: Null Dateiänderungen, null Folgeaktionen und semantisch gleiche Aussagen bei unveränderten Eingaben sind konkrete Maßstäbe. / Pass: Zero file changes, zero downstream actions, and equivalent statements for unchanged inputs are concrete measures.
- [x] CHK021 Sind erwartete Fixture-Ergebnisse und erfolgreicher Prüfprozess-Exitcode eindeutig voneinander getrennt? / Are expected fixture outcomes clearly separated from a successful validation-process exit code? [Acceptance Criteria, Spec §SC-001, §Autonomer Lauf und Abnahmegrenzen]
  - Bestanden: Einmal `Eligible`, zweimal `Blocked`, insgesamt 100 Prozent; korrekt erwartete Negativfälle haben Exitcode 0. / Pass: One Eligible and two Blocked outcomes, covering 100 percent; correctly expected negative cases exit zero.

## Negativfälle, Abbruch und Wiederaufnahme / Negative Cases, Abort, and Recovery

- [x] CHK022 Sind leere, unbekannte oder widersprüchliche Werte und ein unbekannter Modus fail-closed abgedeckt? / Are empty, unknown, or conflicting values and an unknown mode covered fail-closed? [Edge Case Coverage, Spec §Grenzfälle, §FR-005]
  - Bestanden: Ohne ausreichenden Nachweis gilt `Blocked`; fehlende Kriterien und Authority werden ausdrücklich abgewiesen. / Pass: Insufficient evidence means Blocked; missing criteria and authority are explicitly rejected.
- [x] CHK023 Sind unsichere Evidence, sensible Daten und unzulässige Remote-Befehle mit Stop und Schutz der Ausgabe geregelt? / Are unsafe evidence, sensitive data, and forbidden remote commands covered by stopping and output protection requirements? [Security Coverage, Spec §Grenzfälle, §Sicherheit]
  - Bestanden: Verarbeitung stoppen, sensible Werte nicht wiedergeben, Re-Evaluation verlangen. / Pass: Stop processing, do not repeat sensitive values, and require reassessment.
- [x] CHK024 Sind ProviderFailure und ProductFailure klar definiert und von Eligibility sowie Erfolg getrennt? / Are ProviderFailure and ProductFailure clearly defined and separated from eligibility and success? [Clarity, Spec §US3.3, §FR-008]
  - Bestanden: Dienst-/Runnerausfall und Artefaktfehler sind verschiedene Ursachen; Ausfall ist kein Pass. / Pass: Service/runner failure and artifact defects are distinct causes; failure is not a pass.
- [x] CHK025 Sind Abort und Recovery als eigenständige Anforderungen mit Haltepunkt, Teilmerge-Verbot und erneuter Prüfung formuliert? / Are abort and recovery separate requirements with a stopping boundary, no partial merge, and reassessment? [Recovery Coverage, Spec §FR-002, §FR-009]
  - Bestanden: Stop-Bedingung, sicherer Haltepunkt und Wiederherstellung bleiben getrennt; Manifest und Eligibility müssen erneut geprüft werden. / Pass: Stop condition, safe boundary, and recovery remain distinct; manifest and eligibility require reassessment.
- [x] CHK026 Begrenzen die Anforderungen Stop und Wiederanlauf fremder Prozesse auf passende separate Autorität? / Do requirements restrict stopping and restarting other processes to matching separate authority? [Consistency, Spec §FR-009]
  - Bestanden: Eine Empfehlung verleiht keine Abbruch-/Wiederanlaufrechte; ohne gesonderten Auftrag werden Worker nicht gestartet. / Pass: A recommendation grants no cancellation/restart rights; workers do not start without a separate instruction.
- [x] CHK027 Sind bewusster Stop und unerwartete Unterbrechung mit verschiedenen Fortsetzungsbedingungen beschrieben? / Are deliberate stop and unexpected interruption described with distinct continuation conditions? [Recovery Coverage, Spec §Autonomer Lauf und Abnahmegrenzen]
  - Bestanden: `PausedByUser` benötigt ausdrückliches Resume; Unterbrechung verlangt Hash-, Authority-, Operations- und Gate-Neuprüfung. / Pass: PausedByUser needs explicit resume; interruption requires rechecking hashes, authority, operations, and gates.
- [x] CHK028 Sind die Re-Evaluation-Trigger über reine Dateihash-Drift hinaus vollständig benannt? / Are reassessment triggers fully named beyond file-hash drift? [Coverage, Spec §Grenzfälle, §Governance-Anwendbarkeit und Nachweise]
  - Bestanden: Roots, Kanten, Decisions, Governance, Fixtures, Plattform und Supply Chain sind zusätzlich genannt. / Pass: Roots, edges, decisions, governance, fixtures, platform, and supply chain are also named.

## Sprache, Barrierefreiheit und Plattformen / Language, Accessibility, and Platforms

- [x] CHK029 Sind DE-first/EN-second, CEFR B2 und Begriffserklärungen verbindlich und für normative Inhalte konsistent gefordert? / Are German-first/English-second, CEFR B2, and term explanations mandatory and consistent for normative content? [Clarity, Spec §NFR-002, §CR-003, §US3.4]
  - Bestanden: Paarigkeit umfasst Überschriften, Fehlergründe und Beispiele; Fachbegriffe werden beim ersten Auftreten erklärt. / Pass: Pairing includes headings, error reasons, and examples; technical terms are explained at first use.
- [x] CHK030 Sind Status, Gründe, Abhängigkeiten und nächste Aktion auch ohne Farbe oder Diagramm vollständig gefordert? / Are statuses, reasons, dependencies, and next action fully required without colour or diagrams? [Accessibility Completeness, Spec §NFR-001, §CR-002, §SC-005]
  - Bestanden: Alle vier Informationstypen bleiben verständlicher Text; visuelle Darstellung ersetzt keinen Text. / Pass: All four information types remain understandable text; visuals do not replace it.
- [x] CHK031 Sind anwendbare WCAG-Prüfpunkte, Leserpfad und Grenzen des A11Y-Nachweises konkret beschrieben? / Are applicable WCAG checkpoints, the reader path, and accessibility-evidence limits described concretely? [Measurability, Spec §Barrierefreiheit]
  - Bestanden: WCAG 2.2 AA benennt Struktur, Reihenfolge, Farbe, Links, Überschriften und Sprache; tatsächliche Umgebung und Grenzen sind zu dokumentieren. / Pass: WCAG 2.2 AA names structure, sequence, colour, links, headings, and language; the actual environment and limits must be recorded.
- [x] CHK032 Sind Shell-Parität und native Plattformabnahme getrennt und fehlende Nachweise sichtbar geregelt? / Are shell parity and native-platform acceptance separated with missing evidence kept visible? [Measurability, Spec §NFR-003, §SC-004, §Plattformen, §Grenzfälle]
  - Bestanden: Bash/PowerShell müssen gleiche Ergebnisse, Gründe und nächste Aktionen liefern; macOS belegt nicht Linux/Windows, fehlende Parität blockiert spätere Abnahme. / Pass: Both shells must provide equivalent outcomes, reasons, and next actions; macOS does not prove Linux/Windows, and missing parity blocks later acceptance.
- [x] CHK033 Sind reine Leseoperationen und separat autorisierte Schreibvorschauen bei Bash/PowerShell klar unterschieden? / Are read-only operations clearly distinguished from separately authorised write previews across Bash/PowerShell? [Consistency, Spec §Plattformen, §FR-006]
  - Bestanden: Lesen braucht keinen schreibenden Dry-run; für autorisierte Manifest-Writes werden gleichwertige Vorschau und WhatIf verlangt. / Pass: Reading needs no writing dry-run; authorised manifest writes require equivalent preview and WhatIf.

## Abhängigkeiten, Ausschlüsse und Restfragen / Dependencies, Exclusions, and Remaining Questions

- [x] CHK034 Sind bestehende Quellen und Laufzeiten benannt und neue Abhängigkeiten an Re-Evaluation gebunden? / Are existing sources and runtimes named and new dependencies tied to reassessment? [Dependencies, Spec §Annahmen, Abhängigkeiten und Ausschlüsse, §NFR-003, §CR-005]
  - Bestanden: Intake, Kriterienvertrag, Manifest und Reihenfolge sind Quellen; bestehende Laufzeiten und sichere Adaptergrenzen werden wiederverwendet. / Pass: Intake, criteria contract, manifest, and order are sources; existing runtimes and safe adapter bounds are reused.
- [x] CHK035 Sind Produkt-/Scaffold-Arbeit, reale Parallelität, Worktrees, Level 0, Home-Sync, Remote/Provider-Aktionen, Merge, Bypass und Promotion ausdrücklich ausgeschlossen? / Are product/scaffold work, real parallelism, worktrees, level 0, Home sync, remote/provider operations, merge, bypass, and promotion explicitly excluded? [Scope Clarity, Spec §Annahmen, Abhängigkeiten und Ausschlüsse, §Autonomer Lauf und Abnahmegrenzen]
  - Bestanden: Die Ausschlussliste erfasst alle genannten Bereiche; Eligibility startet weder Specify noch Implementierung. / Pass: The exclusion list covers all named areas; eligibility starts neither Specify nor implementation.
- [x] CHK036 Sind Anforderungen, spätere Ausführungsevidence und verbleibende Planungsarbeit getrennt, ohne materielle offene Frage zu verdecken? / Are requirements, later execution evidence, and remaining planning work separated without hiding a material open question? [Ambiguities and Conflicts, Spec §SC-001–005, §Governance-Anwendbarkeit und Nachweise, §Autonomer Lauf und Abnahmegrenzen]
  - Bestanden: Anwendbarkeit ist entschieden, Umsetzung bleibt `Not Assessed`; EL-01–03 sind spätere Gates. Keine materielle Anforderungsfrage erkannt. / Pass: Applicability is decided, implementation remains Not Assessed, and EL-01–03 are later gates. No material requirements question was found.

## Bewertung und nächste Aktion / Assessment and Next Action

**36 von 36 bestanden; 0 offen; 0 nicht bestanden; 36 von 36 mit Spec-Bezug (100 Prozent).** Jede Position wurde inhaltlich gegen den genannten Abschnitt bewertet. Nicht vorhandene Plan-/Tasks-Dateien sind bei dieser ausdrücklich vorgezogenen Prüfung kein Mangel. / **36 of 36 passed; 0 open; 0 failed; 36 of 36 with specification references (100 percent).** *Each item was assessed against its named section. Missing plan/tasks files are not a defect in this explicitly pre-plan review.*

Der [Phasenbericht / Phase report](../phase-results/checklist-report.md) bindet Quellen, Gates und Prüfgrenzen. Nächste sichere Aktion: Den Bericht an den koordinierenden Runner zurückgeben. / *The phase report binds sources, gates, and validation limits. Next safe action: return the report to the coordinating runner.*
