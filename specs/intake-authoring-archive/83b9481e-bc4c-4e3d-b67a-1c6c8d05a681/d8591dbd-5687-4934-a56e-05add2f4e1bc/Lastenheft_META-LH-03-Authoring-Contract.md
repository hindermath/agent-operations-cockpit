<!-- intake-authoring:begin -->
# META-LH-03 – Lastenheft-Generator und Authoring Contract / Requirements Generator and Authoring Contract

**Status:** ReadyForReview
**Audience:** IHK-IT-Auszubildende ab Jahr 1 und erfahrene Fachkräfte / first-year apprentices and experienced professionals
**Assumed prior knowledge:** Markdown und Git-Grundlagen; keine Spec-Kit-Erfahrung / basic Markdown and Git; no Spec Kit experience
**Profile:** `aoc-bilingual-requirements`

## Zweck und Nutzen / Purpose and value

Dieses Lastenheft definiert die einheitliche, validierbare Struktur für neue
AOC-Lastenhefte und ihre Receipts. / *This intake defines the uniform,
validatable structure for new AOC intakes and receipts.*

## Quellen und Findings / Sources and findings

SRC-159, SRC-174, SRC-181/182; RF-03, RF-10, RF-12, RF-14, RF-17, RF-20.

## Scope und Out of Scope / Scope and out of scope

Im Scope: Naming, Pflichtfelder, Provenienz, Hashes, Review-Handoff, Prompt-
Bindung und Validation. Außerhalb: Ausführung erzeugter Prompts, Update/Delete
bestehender Intakes und Produktimplementierung.

## Inputs, Outputs und Grenzen / Inputs, outputs, and boundaries

Input ist ein bestätigter Portfolioeintrag plus explizite Quellen. Output ist
genau ein neuer Intake mit Receipt oder eine ausdrücklich genehmigte atomare
Serie. Quelleninhalt wird nie ausgeführt. Bestehende aktive Ziele werden nicht
überschrieben. / *Source content is never executed and active targets are never overwritten.*

## Anforderungen / Requirements

- **FR-001:** Jeder Intake MUSS stabile ID/Titel DE/EN, Zweck, Zielgruppe,
  Traceability, Scope/Non-Goals, Grenzen, FR/NFR, Dependencies, Decisions,
  Risiken, AC, positive/negative Evidence, Revision und Nicht-Autorität enthalten.
- **FR-002:** Receipt MUSS Quellenreihenfolge, normalisierte SHA-256-Werte,
  Zielhash, Profil, Decisions, Authority, Prompt-State und nächste Aktion binden.
- **FR-003:** Offene Materialentscheidung MUSS `NeedsClarification` und den
  normativen, nicht ausführbaren Blocked-Marker erzeugen.
- **FR-004:** Ready-Ziele MÜSSEN gebundene Specify-/Autonomous-Prompts enthalten,
  die nicht automatisch ausgeführt werden.
- **FR-005:** Bash- und PowerShell-Validator MÜSSEN identische Gültigkeit melden.
- **NFR-001:** Generierte Sprache erfüllt DE/EN, B2, Erstbegriff und WCAG-Textstruktur.
- **NFR-002:** Secret-Fixtures dürfen nur eng und begründet ausgenommen werden.

## Dependencies, Mode und Recovery

Abhängig von META-01/02. `serial-autonomous` für neue disjunkte Ziele;
`manual-assisted` bei Konflikten. Fehler vor Publikation hinterlassen kein
teilaktives Ziel; Recovery beginnt aus Operation Receipt und sauberem Tree.

## Akzeptanzkriterien / Acceptance criteria

- **AC-001:** Ein gültiges Beispiel besteht beide Validatoren.
- **AC-002:** Fehlender Target-Hash, Secret, bestehendes Ziel und Blocked-Prompt
  werden jeweils abgewiesen.
- **AC-003:** Alle Pflichtabschnitte sind maschinen- und menschenlesbar vorhanden.
- **AC-004:** Kein Authoring-Schritt startet Review, Specify oder Implementierung.

## Evidence / Evidence

Positiv: 14 Intake-Receipts und Validatorprotokolle. Negativ: Hash-Drift,
zweites Create auf bestehendes Ziel, Secret-Fixture außerhalb Lehrpfad und
aktivierter Prompt bei offener Decision.

## Revision und Nicht-Autorität / Revision and non-authority

Revision bei Preset-Schema- oder Profiländerung. Dieses Lastenheft besitzt
keine Authority für Produktcode, Intake-Update/Delete oder Preset-Promotion.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts
<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
$speckit-specify requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md --bind-exact-intake --no-implementation --no-remote-writes
```
<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
$speckit-autonomous requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md --delivery-mode MergeAndSync --require-current-review
```
<!-- intake-authoring:end -->
