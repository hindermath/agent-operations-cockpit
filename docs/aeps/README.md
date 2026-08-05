# AEPS-Evidence-Vertrag / AEPS Evidence Contract

## Zweck und Systemgrenze / Purpose and system boundary

Das **Agentic Engineering Preset System (AEPS)** ist das projektübergreifende
System für wiederverwendbare Verträge, Presets und den zugehörigen
Wissenskreislauf. Das strategische Anchor-Issue ist
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196).
Das Agent Operations Cockpit (AOC) ist ein Level-2-Referenzprojekt und eine
Evidence-Quelle, aber nicht das kanonische AEPS-System-of-Record. / *The
Agentic Engineering Preset System is the cross-project system for reusable
contracts, presets, and the related learning loop. The AOC is a level-2
reference project and evidence source, not the canonical AEPS system of
record.*

Die Arbeitsformel lautet: **Level 2 entdeckt, testet und härtet; Level 0
konsolidiert, versioniert und promotet.** Ein AOC-Ergebnis darf daher keine
projektübergreifende Preset-Promotion allein auslösen. / *Level 2 discovers,
tests, and hardens; level 0 consolidates, versions, and promotes. An AOC result
cannot grant cross-project preset promotion by itself.*

## Kanonische AOC-Artefakte / Canonical AOC artifacts

- [AEPS Findings Ledger](findings-ledger.md)
- [Finding-to-Preset-Candidate-Matrix](finding-to-preset-candidate-matrix.md)
- [Preset-Lückenanalyse](preset-gap-analysis.md)
- [Upstream-Handoff-Empfehlungen](upstream-handoff.md)
- [Initiales Completion Receipt](receipts/2026-08-01-initial-inventory.md)

Diese Datei ist der AOC-Arbeitsvertrag. Das Ledger ist die kanonische
projektbezogene Finding-Sammlung; die übrigen Dateien leiten Zuordnung,
Lücken, Handoff und Abschlussnachweise daraus ab. / *This file is the AOC
working contract. The ledger is the canonical project finding collection; the
other files derive mapping, gaps, handoff, and completion evidence from it.*

## Erfassungszeitpunkte / Capture triggers

Eine AEPS-Prüfung ist mindestens erforderlich: / *An AEPS assessment is
required at least:*

1. einmalig für den vorhandenen AOC-Bestand; / *once for the existing AOC
   baseline;*
2. nach jedem Lastenheft mit formal bestätigtem `Ready`; / *after every intake
   with formally confirmed Ready status;*
3. nach wesentlichen Reviews, Retrospektiven oder Completion Receipts mit
   übertragbaren Erkenntnissen; / *after material reviews, retrospectives, or
   completion receipts with transferable learning;*
4. nach einem fehlgeschlagenen oder abgebrochenen Lauf, wenn daraus ein
   relevantes Anti-Pattern oder Governance-Finding folgt. / *after a failed or
   aborted run when it yields a relevant anti-pattern or governance finding.*

Eine Prüfung darf mit dem Ergebnis `Keine neue AEPS-Evidence / No new AEPS
evidence` enden. Dieses Ergebnis wird im zugehörigen Receipt begründet, damit
ein Trigger nicht stillschweigend übersprungen wird. / *An assessment may end
with no new AEPS evidence. The related receipt records the rationale so a
trigger cannot be skipped silently.*

## Formale Ready-Grenze / Formal Ready boundary

`Ready` bezeichnet ausschließlich ein aktuelles Single-Intake-Review, das die
gültige Repository-Policy erfüllt. Vor einer Erfassung MÜSSEN alle folgenden
Bedingungen erfüllt sein: / *Ready means only a current Single-intake review
that satisfies the active repository policy. All following conditions MUST be
met before capture:*

- Review-Status ist `Ready`;
- Zielpfad und normalisierter Zielhash stimmen mit dem aktuellen Lastenheft;
- das Ergebnis besteht Bash- und PowerShell-Review-Validation;
- das Authoring Receipt ist aktuell und besteht beide Validatoroberflächen;
- ein supersediertes Ergebnis wird nicht als aktueller Trigger verwendet.

Der Review-Status ist von der Series-Lifecycle-Angabe getrennt. Ein Intake kann
formal `Ready` und in der Series weiterhin `Pending`, `Eligible`, `Blocked`
oder `Completed` sein. `Ready` erteilt weder Start-, Specify-,
Implementierungs-, Remote-, Merge-, Bypass- noch Promotion-Authority. / *The
review status is separate from the Series lifecycle. Ready grants no start,
delivery, or promotion authority.*

Zusätzlich gilt für das AOC eine projektlokale globale Review-Sperre: Erst wenn
alle 14 aktiven Lastenhefte der kanonischen Programmreihe gleichzeitig die oben
definierte aktuelle `Ready`-Grenze erfüllen, darf ein nachgelagerter Spec-Kit-
Lauf überhaupt separat autorisiert werden. `META-LH-01` ist danach zwingend das
erste Ziel; Drift schließt die Sperre erneut. Diese konservative
Portfolioentscheidung ist AOC-spezifische Evidence und darf ohne
Cross-Project-Validierung nicht als allgemeine AEPS- oder Preset-Regel
promotet werden. / *A project-local global review gate additionally requires
all 14 active AOC programme intakes to meet the current Ready boundary before
any downstream run can be authorised separately. `META-LH-01` is then the
mandatory first target, and drift closes the gate again. This conservative
portfolio decision is AOC-specific evidence, not a general AEPS or preset rule.*

## Identität und Deduplizierung / Identity and deduplication

- Jedes projektbezogene Finding erhält eine stabile ID im Format
  `AEPS-FIND-AOC-NNN`.
- Eine vorhandene Upstream-ID wie `CAND-AEPS-01` bleibt unverändert und wird
  referenziert, nicht dupliziert.
- Ein neuer Preset-Kandidat darf erst nach der Übertragbarkeitsprüfung eine ID
  im Format `AEPS-CAND-AOC-NNN` erhalten.
- Für Ready-Evidence ist der Deduplizierungsschlüssel
  `Review-ID + Zielpfad + normalisierter Zielhash`.
- Für Reviews, Receipts oder Fehl-/Abbruchläufe ohne Ready-Status gilt
  `Quellartefakt + normalisierter Artefakthash + Datum`.
- Supersession ergänzt Lineage; sie löscht oder überschreibt historische
  Evidence nicht.

*Every AOC finding receives a stable finding ID. Existing upstream candidate
IDs are referenced rather than duplicated. Review identity, target, and hash
form the Ready deduplication key; other evidence uses artifact, hash, and date.
Supersession preserves history.*

## Pflichtfelder / Required fields

Jeder Ledger-Eintrag MUSS enthalten: / *Every ledger entry MUST contain:*

| Feld / Field | Vertrag / Contract |
|---|---|
| Finding-ID | stabile `AEPS-FIND-AOC-NNN`-ID / stable ID |
| Quelle und Lastenheft / source and intake | repository-relativer Pfad, Review-/Receipt-ID oder GitHub-Link / repository-relative path, review or receipt ID, or GitHub link |
| Datum und Repository-Commit | Evidence-Commit; bis zur Veröffentlichung `PendingPublication` plus Base-HEAD und Artefakthash / evidence commit, or PendingPublication with base HEAD and artifact hash |
| Problem oder Beobachtung / problem or observation | konkrete, reproduzierbare Aussage / concrete reproducible statement |
| Kontext und Randbedingungen / context and constraints | Plattform, Phase, Authority und relevante Voraussetzungen / platform, phase, authority, and prerequisites |
| Positive Evidence | bestandener Nachweis und erwartetes Ergebnis / passing evidence and expected result |
| Negative Evidence | Gegenbeispiel, Failure oder ausdrücklich begründete offene Negativ-Evidence / counterexample, failure, or justified open negative evidence |
| Grenzen / limits | Nicht-Ziele, bekannte Proof-Grenzen und Restlücke / non-goals, proof limits, and residual gap |
| AOC-spezifisch versus generisch / AOC-specific versus generic | getrennte Aussagen, keine ungeprüfte Generalisierung / separate statements without unchecked generalisation |
| AEPS-Domäne / domain | vorgeschlagene Domäne aus #196 / proposed domain from #196 |
| Reifegrad / maturity | `observation`, `pilot-pattern`, `candidate` oder `cross-project-validated` |
| Preset-Bezug / related presets | bestehende oder mögliche Presets; `N/A` ist zu begründen / existing or possible presets; N/A requires rationale |
| Nächste Validierung / next validation | konkrete Evidence-Aktion / concrete evidence action |
| Promotion-Blocker / promotion blockers | offene Evidence, Kompatibilität, Review oder Authority / open evidence, compatibility, review, or authority |
| Erfassungsstatus / capture status | einer der unten definierten Zustände / one of the states below |
| Upstream-Status / upstream status | `NotApplicable`, `PendingPublication`, `PendingAuthority`, `Recommended`, `Posted` oder `Superseded` |

## Erfassungs- und Reifezustände / Capture and maturity states

Die Bestandsaufnahme verwendet genau diese Erfassungszustände: / *The baseline
uses exactly these capture states:*

- `AlreadyRecorded`: in #196 oder einem verlinkten Upstream-Issue vollständig
  vorhanden;
- `NotRecorded`: noch nicht upstream erfasst;
- `PartiallyRecorded`: Grundidee vorhanden, neue Evidence oder Grenze fehlt;
- `AocSpecific`: nützlich für AOC, aber derzeit nicht generalisierbar;
- `PotentialCandidate`: begründete projektübergreifende Hypothese;
- `MoreEvidenceRequired`: Einordnung bleibt bis weiterer Evidence offen.

Der Reifegrad ist eine andere Achse. Ein einzelnes AOC-Ergebnis erreicht
höchstens `pilot-pattern` oder `candidate`. `cross-project-validated` verlangt
bestätigende oder widersprechende Evidence aus mindestens einem weiteren
geeigneten Referenzprojekt. / *Capture state and maturity are separate axes. A
single AOC result reaches at most pilot-pattern or candidate. Cross-project
validation requires another suitable reference project.*

## Upstream-Handoff / Upstream handoff

- Kleine ergänzende Findings können als strukturierter Kommentar in #196
  eingetragen werden.
- Umfangreiche, zusammengehörige oder eigenständig bearbeitbare Findings
  erhalten ein neues Issue im geeigneten Repository.
- Jedes neue Issue referenziert #196. Wenn aktuelle Authority vorliegt, erhält
  #196 einen Rückverweis auf das neue Issue.
- Ein Handoff erfolgt erst mit stabiler Commit-, PR- oder gleichwertiger
  öffentlicher Evidence. Lokale Evidence bleibt `PendingPublication`.
- Ohne aktuelle GitHub-Schreibautorität bleibt der Datensatz
  `PendingAuthority`; ein gespeicherter historischer Delivery-Modus genügt
  nicht.
- Level-0-Promotion benötigt einen separaten Arbeitsauftrag und Completion
  Evidence.

*Small findings may be posted to #196; substantial work receives a linked
issue. Upstream handoff requires stable published evidence and current write
authority. Promotion remains a separate level-0 action.*

## Ablauf je Trigger / Procedure per trigger

1. Trigger und formale Gültigkeit prüfen.
2. Quellen, Hashes, Commit-/Publikationsstand und vorhandene Upstream-Einträge
   erfassen.
3. Bestehende Ledger-Datensätze über den Deduplizierungsschlüssel suchen.
4. Findings, Learnings, Patterns, Anti-Patterns und Gegenbeispiele fachlich
   bewerten.
5. Ledger, Candidate-Matrix, Gap-Analyse und Handoff-Empfehlung atomar
   aktualisieren.
6. Ein Receipt unter `docs/aeps/receipts/` erzeugen; bei fehlender neuer
   Evidence ein begründetes No-change-Receipt verwenden.
7. Dokumentationsauswirkung, Links, Sprache, A11Y, Secrets und Whitespace
   prüfen.
8. Erst nach stabiler Veröffentlichung und aktueller Authority upstream
   schreiben; URL und Status anschließend im Ledger binden.

## Nicht-Autorität / Non-authority

Dieser Vertrag autorisiert keine Änderung oder Promotion eines Presets, keine
Level-0-Mutation, keine Produktimplementierung, keinen Spec-Kit-Lauf und keine
GitHub-Schreibaktion ohne aktuelle Authority. Er ersetzt weder unabhängiges
Review noch Cross-Project-Validation. / *This contract authorises no preset or
level-0 mutation, implementation, Spec Kit run, or GitHub write without
current authority. It replaces neither independent review nor cross-project
validation.*
