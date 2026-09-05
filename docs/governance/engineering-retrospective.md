# Engineering-Retrospektive pro Feature / Engineering retrospective per feature

## Geltung und Ablage / Scope and location

Auf Thorstens ausdrücklichen Auftrag vom 2026-09-05 gilt dieser Bericht ab
`003-authoring-contract` für jeden aktuellen und zukünftigen Feature-Lauf in
diesem Repository, autonom oder manuell mit Spec Kit. Er ergänzt technische
Receipts und AEPS-Evidence; er ersetzt sie nicht. Frühere abgeschlossene Läufe
werden ohne neuen Auftrag nicht rückwirkend neu bewertet.

*At Thorsten's explicit request of 2026-09-05, this report applies from
`003-authoring-contract` to every current and future feature run in this
repository, whether autonomous or manual with Spec Kit. It supplements, rather
than replaces, technical receipts and AEPS evidence. Previously completed runs
are not retrospectively reassessed without a new request.*

Speichere genau einen lesbaren Bericht je Feature unter
`specs/<feature>/engineering-retrospective.md`. Gib beim Abschluss eine kurze
Zusammenfassung mit Link aus. Bei einem sicheren Zwischenstopp dokumentiere
`Zwischenstand` statt eines angeblichen Abschlusses und aktualisiere denselben
Bericht nach Fortsetzung. Der Bericht nennt Feature, Run-ID falls vorhanden,
Standdatum, tatsächlichen Lauf-/Lieferstatus und Beweisgrenzen.

*Save one readable report per feature at
`specs/<feature>/engineering-retrospective.md`. Deliver a short summary and link
at closeout. At a safe intermediate stop, label it an interim report rather than
claiming completion, and update the same report after resuming. State the feature,
run ID where available, reporting date, actual run/delivery status, and evidence
limits.*

## Die sechs Perspektiven / The six perspectives

1. **Output – tatsächlich erzeugt oder verändert:** Benenne die wichtigsten
   Artefakte und ihr Ergebnis. Trenne lokale Entwürfe, validierte Ergebnisse und
   ausgelieferte Änderungen. Behaupte keine Implementierung allein aufgrund
   einer Spezifikation oder eines `Ready`-Reviews.
2. **Findings – neu entdeckt:** Nenne neue Probleme, Lücken, Patterns
   (wiederkehrende brauchbare Ansätze) und Anti-Patterns (wiederkehrende
   Fehlansätze). Verlinke stabile Finding-IDs, Status, Evidence und offene
   Folgeaktionen. Neue Evidence zu einem bekannten Finding ist kein neues
   Finding.
3. **Bestätigung – praktisch bewährt:** Erkläre, welche bestehenden Governance-,
   Spec-Kit- oder AEPS-Regeln im Lauf nachweisbar geholfen haben. Trenne einen
   einzelnen positiven Nachweis von projektübergreifender Gültigkeit.
4. **Intervention – Eingriffe und Entscheidungen:** Zeige, wo repariert, geklärt,
   interpretiert oder menschlich entschieden werden musste, warum dies nötig
   war, wer handelte und was danach möglich wurde. Ungeklärte Autorität bleibt
   ungeklärt.
5. **Effizienz – Aufwand und Einsparmöglichkeiten:** Beschreibe unnötige
   Schleifen, vermeidbare Agentenarbeit, redundante Reviews, wirksame
   Wiederverwendung und mögliche Preset-Verbesserungen. Unterscheide notwendige
   Pflichtgates von vermeidbarer Wiederholung. Quantifiziere nur mit belastbaren
   Daten; Schätzungen sind als solche zu kennzeichnen.
6. **AEPS-Relevanz – Einordnung statt Promotion:** Ordne neue und bestätigte
   Evidence bestehenden AEPS-Findings zu. Trenne AOC-spezifische Details,
   wiederholbare Beobachtungen und mögliche projektübergreifende Kandidaten.
   Verlinke Ledger und AEPS-Receipt einschließlich eines begründeten
   No-Change-Ergebnisses; nenne fehlende Evidence und den nächsten Feldnachweis.

*1. Output: Identify what was actually created or changed and its result.
Distinguish local drafts, validated results, and delivered changes. A specification
or Ready review alone does not prove implementation.*
*2. Findings: Identify newly discovered problems, gaps, patterns, and
anti-patterns, with stable finding IDs, status, evidence, and follow-up. New
evidence for an existing finding is not a new finding.*
*3. Confirmation: Explain which existing governance, Spec Kit, or AEPS rules
demonstrably helped. A single successful observation does not prove cross-project
validity.*
*4. Intervention: Explain repairs, clarifications, interpretations, and human
decisions, including why they were needed, who acted, and what became possible.
Unresolved authority remains unresolved.*
*5. Efficiency: Describe unnecessary loops, avoidable agent work, redundant
reviews, effective reuse, and possible preset improvements. Separate mandatory
gates from avoidable repetition. Quantify only with supporting data and label
estimates.*
*6. AEPS relevance: Map new and confirming evidence to existing AEPS findings.
Separate AOC-specific details, repeatable observations, and possible
cross-project candidates. Link the ledger and AEPS receipt, including a justified
no-change outcome, and name missing evidence and the next field test.*

## Completion- und Retrospective-Evidence / Completion and retrospective evidence

Nach den sechs Perspektiven verlinke die vorhandenen technischen Receipts,
Lauf-/Reviewnachweise und gegebenenfalls PR, Merge-SHA und Sync-Nachweis. Diese
Links binden den lesbaren Bericht an tatsächliche Ereignisse; sie sind keine
neuen technischen Receipts. Offene oder noch nicht eingetretene Ereignisse
werden als solche benannt.

*After the six perspectives, link existing technical receipts, run/review
evidence, and where applicable the PR, merge SHA, and synchronization proof.
These links connect the readable report to real events without creating new
technical receipts. Identify pending or unperformed events honestly.*

## Erster Trendvergleich nach META-LH-03 / First trend comparison after META-LH-03

Erst wenn META-LH-03 abgeschlossen ist, ergänze in dessen Bericht einen kleinen
Vergleich von META-LH-01, META-LH-02 und META-LH-03 anhand vorhandener Evidence:
wiederkehrende Findings, Interventionen, bewährte Presets und neue Fehlerklassen.
Trenne Unterschiede im Scope von tatsächlichen Verbesserungen. Fehlende oder
nicht vergleichbare Daten bleiben sichtbar; definiere Zählregeln, bevor du
Zahlen vergleichst. Keine rückwirkenden Reviews, erfundenen Zeitmessungen oder
kanonische Promotion allein aufgrund von drei AOC-Läufen.

*Only after META-LH-03 is complete, add a small comparison of META-LH-01,
META-LH-02, and META-LH-03 to its report using existing evidence: recurring
findings, interventions, confirmed presets, and new error classes. Separate
scope differences from actual improvement. Show missing or non-comparable data
and define counting rules before comparing numbers. Do not start retrospective
reviews, invent timings, or promote a canonical rule from three AOC runs alone.*

## Qualitäts- und Authority-Grenzen / Quality and authority boundaries

- Verwende sechs klar getrennte Abschnitte in dieser Reihenfolge, Deutsch zuerst,
  Englisch danach, CEFR B2 und die anwendbaren WCAG-2.2-AA-Regeln. Erkläre
  Fachbegriffe beim ersten Auftreten. Halte den Bericht verständlich und knapp.
- Jede wesentliche Aussage verlinkt vorhandene Evidence. Wo nichts Neues
  vorliegt, sage dies mit kurzer Begründung; erfinde keine Findings oder Zahlen.
- Nenne am Ende offene Punkte und die nächste sichere Aktion. Ein nicht erfolgter
  Merge wird nicht als Lieferung dargestellt.
- Nutze vorhandene Review- und Laufnachweise proportional. Der Bericht allein
  löst keine erneute Reviewkampagne und keine neue technische Testmatrix aus.
  Tatsächliche Artefakt- oder Gate-Drift bleibt gesondert zu behandeln.
- Folge dem [AEPS-Vertrag](../aeps/README.md) für Erfassung und Deduplizierung.
  Vorschläge sind keine Preset-Änderungs- oder Promotion-Autorität. Reine
  Effizienzpräferenzen benötigen die dort und im Retrospektiven-Skill geforderte
  wiederholte Evidence; ein einzelner Lauf erzeugt keine kanonische Regel.
- Referenziere die einzige Documentation-Impact-Entscheidung des jeweiligen
  Changes. Dokumentiere keine zweite Entscheidung nur für den Bericht.
- Passe den normalen Closeout so an, dass der Bericht mit den bereits bekannten
  Fakten geliefert wird. Unvermeidbar spätere Merge-/Sync-Fakten dürfen im
  genehmigten kausalen Evidence-Closeout ergänzt werden. Keine zusätzlichen
  leeren PRs, Selbsthash-Schleifen oder neue Feature-Läufe nur für diesen Bericht.

*Use six separate sections in the stated order, German first and English
second, at CEFR B2 with applicable WCAG 2.2 AA rules. Explain first-use terms and
keep the report concise. Link material claims to existing evidence; state and
explain when there is nothing new. End with open items and the next safe action.
Do not claim an unperformed merge as delivery. Reuse evidence proportionately:
reporting alone triggers neither a new review campaign nor a new test matrix;
actual drift is handled separately. Follow the AEPS capture and deduplication
contract. Suggestions grant no preset-change or promotion authority, and a
single run creates no canonical efficiency rule. Reference the change's sole
Documentation Impact decision. Deliver the report within the normal closeout;
later causal facts may be added in its authorized evidence closeout, without
empty PRs, self-hash loops, or new feature runs.*

## Aktueller Einstieg / Current starting point

- [META-LH-03 – laufender Bericht](../../specs/003-authoring-contract/engineering-retrospective.md)

*The linked META-LH-03 report is the first report under this rule.*
