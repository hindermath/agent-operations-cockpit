# Unabhängiger Plan-Review: Nachweisbarer Intake-Authoring-Vertrag

## Ergebnis

**Blocked** — Die eine beauftragte unabhängige Review-Aufgabe für Lauf
`044b77ae-85fd-46ee-97f4-61ce7a2c9c66` wurde vollständig ausgeführt. Die
Plan-Artefakte sind bytegenau an den Plan-Report gebunden, bilden die fünf
kanonischen Fachartefakte ab und planen wesentliche Sicherheits-, Sprach-,
Plattform-, Review-, Delivery- und Closeout-Grenzen korrekt. Fünf materielle
Findings bleiben jedoch offen. Deshalb sind die PlanReview-Gates nicht erfüllt
und die Übergabe an Tasks ist gesperrt.

Fehlende spätere Implementierungs-, Test-, PR-, Merge-, Lifecycle- oder
Sync-Ergebnisse wurden nicht als Finding bewertet; sie sind in dieser Phase
erwartungsgemäß noch nicht vorhanden. Der Blocker betrifft ausschließlich
fehlende oder widersprüchliche **Planung** für ausführbare Verifikation,
vollständige Konsumenten, Update-Lineage und kausalen Abschluss.

## Review-Grenze und Integrität

- Ausgeführt wurde nur die unabhängige Review-Rolle für `speckit.plan`.
- `plan.md`, `research.md`, `data-model.md`, `quickstart.md`, beide deklarativen
  Verträge sowie alle akzeptierten Eingaben wurden nur gelesen.
- Die abgeschlossene Vier-Intake-Binding-Reparatur, ihr Checker, Series/002 und
  die übrigen 13 aktuellen Blätter wurden als unveränderliche Vorgänger
  behandelt.
- Es wurden keine Plan- oder Designartefakte neu erzeugt oder geändert, keine
  Tasks oder Implementierung ausgeführt, kein Laufzustand geändert und keine
  Git- oder Remote-Aktion vorgenommen.
- `MergeAndSync` bleibt die aktuelle Lieferart. Normale Reviews, Checks und eine
  tatsächlich verfügbare Genehmigung bleiben Pflicht; Admin-Bypass bleibt
  ausgeschlossen.

Die folgenden normalisierten SHA-256-Werte stimmen mit der Übergabe in
`specs/003-authoring-contract/phase-results/plan-report.md` überein:

| Artefakt | Normalisierter SHA-256 |
|---|---|
| `specs/003-authoring-contract/plan.md` | `a005b8a02a38b5fa7bd69763298d46ae1f4ff15da64560a65e8b8962c57babf7` |
| `specs/003-authoring-contract/research.md` | `3f5ded3340d3dcb0b8e65a98f403513691f9307d4d75c3d758edaf7c2c091534` |
| `specs/003-authoring-contract/data-model.md` | `3acaaa664b3657dd425821bb10a788a77c54db582fb770dc589612f019e755a4` |
| `specs/003-authoring-contract/quickstart.md` | `cf286f234bbf8c6f967f9ad12e47e96de6eedc7abe781ef0f0fae8a23007ec1b` |
| `specs/003-authoring-contract/contracts/authoring-contract-design.json` | `fc94547957e42a249aa1f3f3d99e3d2632e05cc33abb6f1dd7badd5402ffadd9` |
| `specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json` | `abdaa3e5de8f17a67251ef604cdc226637aadb74903d254d4ddff0f2ae9e522e` |

Der während Plan ergänzte Berichtsauftrag wurde als ausdrücklich akzeptierter,
begrenzter Review-Eingang mit den normalisierten Hashes
`b377b9a76dbedfaf7069feb54d276f68d5c4562fd58d81133640b7362cfcec30`
für `specs/003-authoring-contract/reporting-contract-addendum.md` und
`f7349f7e625269965ab5fdb26196a20422df3b77934df5d33eb115ab6f4a9266`
für `docs/governance/engineering-retrospective.md` geprüft. Er ist kein neues
Feature und ändert keine früheren Phase-Payloads.

## Bestätigte Planqualität

- Die fünf kanonischen Fachartefakte sind vollständig, eindeutig und in stabiler
  Reihenfolge enthalten. Receipt-Schema `2.0`, Quellenreihenfolge,
  normalisierte Hashes, stabile Intake-ID sowie neue Ereignis-IDs sind geplant.
- `NeedsClarification` ist mit stabilen Decision-IDs, `BLOCKED` und `DO NOT RUN`
  in beiden Promptblöcken fail-closed; `ReadyForReview` bindet beide Prompts an
  dasselbe Ziel, ohne Folgeautorität abzuleiten.
- Deutsch zuerst, Englisch danach, CEFR B2, Erstbegriffserklärungen,
  text-first-Ausgabe und anwendbare WCAG-2.2-AA-Kriterien sind als semantischer
  Review-Gate geplant.
- Die historischen vier Renewals und Reviews werden proportional
  wiederverwendet. Eine spätere fachliche Erneuerung ist auf META-LH-03 begrenzt;
  die anderen 13 Blätter sowie die Series-Brücke sollen unverändert bleiben.
- Die drei Betriebssysteme, reale Bash-/PowerShell-/Python-Oberflächen,
  unmittelbare Exitcodes, exakter HEAD, vollständiger Gitleaks-Scan,
  PSScriptAnalyzer `1.25.0` und vier unabhängige Fachreviews sind grundsätzlich
  benannt.
- Statistik, PreMerge-Evidence, normaler Merge, nachgelagerter Lifecycle und
  PostMerge-Evidence sind kausal getrennt. Es gibt kein Stash, Reset, Force,
  Amend oder spekulatives Zurückprojizieren von Historie.
- Die einzige Documentation-Impact-Entscheidung bleibt `UpdateRequired` im
  Laufnachweis; dieser Review erklärt keine zweite Entscheidung.

## Findings

### PR301 — High — Ergänzte Berichtslieferung widerspricht Positivliste und Closeout

**Fundstelle:**
`specs/003-authoring-contract/reporting-contract-addendum.md:19` bis `:58`,
`specs/003-authoring-contract/contracts/authoring-contract-design.json:122` bis
`:147`, `:189` bis `:193` und `:229` bis `:237`, sowie
`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json:570`
bis `:581`.

**Befund:** Das akzeptierte Addendum nimmt genau fünf gemeinsame
Agenten-Guidance-Dateien, die Governance-Richtlinie, den Feature-Bericht, das
Addendum und bestehenden Laufnachweis in die begrenzte Lieferung auf. Das
deklarative Design führt die fünf Agentenflächen dagegen weiterhin als
unveränderlich außerhalb des Scopes. ACG-026 ist weiterhin `N/A` und verlangt
als Beweis sogar, dass keine gemeinsame Agenten-Guidance geändert wurde. Die
neuen Berichtsdateien fehlen in `requiredConsumers` und in der auf nur drei
Pfade begrenzten Evidence-only-Closeout-Menge. Damit kann die Liefermenge die
ausdrückliche aktuelle Autorität nicht abbilden und der laufende
Retrospektivenbericht kann nach realem Merge/Sync nicht innerhalb der geplanten
Closeout-Positivliste wahrheitsgemäß finalisiert werden.

**Erforderliche Reparatur:** Ohne alte Phase-Payloads oder den fachlichen
Fünfervertrag neu zu erzeugen, muss vor Tasks ein eindeutiger ergänzender
Liefer- und Gate-Overlay festlegen: exakte zusätzliche Pfade, identischer Block
auf allen fünf Agentenflächen, ACG-026 als anwendbar für genau diese Ausnahme,
Review-/Hashnachweis und eine kausal zulässige Aktualisierung des
Feature-Berichts. Level 0, Preset-Versionen, Promotion, Series und andere
Intakes bleiben ausgeschlossen.

**Blockwirkung:** Tasks können aktuell keine widerspruchsfreie Positivliste und
keinen erfüllbaren finalen Berichts-Gate ableiten.

### PR302 — Critical — Global-Ready-Dispatcher erreicht den neuen Bridge-Validator nicht

**Fundstelle:**
`specs/001-programmquellen-baseline/contracts/validate_meta_lh01.py:113` bis
`:120`, `:302` bis `:323` und `:705` bis `:708`;
`specs/003-authoring-contract/contracts/validate_current_evidence_binding.py:625`
bis `:639`; `specs/003-authoring-contract/contracts/authoring-contract-design.json:122`
bis `:147`.

**Befund:** Der produktive Global-Ready-Einstieg ruft bei vorhandener
META03-Bindung ausschließlich den eingefrorenen Reparatur-Checker
`validate_current_evidence_binding.py` auf. Dieser Checker beweist absichtlich
den abgeschlossenen Reparaturzustand und erlaubt beim META-LH-03-Ziel nur die
historische exakte Ersetzung `0.3.0` nach `0.3.1`. Der Plan fügt einen neuen
additiven Feature-Validator hinzu, führt aber weder den Dispatcher noch dessen
Tests als betroffene Konsumenten auf. Nach der geplanten Änderung des
META-LH-03-Blatts würde Global Ready daher weiterhin den alten Checker
ausführen und den neuen Zustand ablehnen; der additive Validator wäre für den
kanonischen Einstieg wirkungslos.

**Erforderliche Reparatur:** Der alte Checker und seine historische Evidence
bleiben unverändert. Der Plan muss den Dispatcher und seine Tests als zwingende
Konsumenten aufnehmen und eine fail-closed Auswahl des alten Reparaturzustands
oder des neuen additiven Nachfolgezustands definieren. Positive und negative
Fixtures müssen beide Ketten, exakte Erfolgs- und Fehlerausgabe, unbekannte oder
mehrdeutige Bridge-Zustände, die unveränderten 13 Blätter und die unveränderte
Series-Brücke prüfen.

**Blockwirkung:** Der geplante aktuelle Evidence-Bridge-Zustand kann den realen
Global-Ready-Verbraucher nicht passieren und damit keinen späteren Abschluss
tragen.

### PR303 — High — Update-Lineage bindet nicht den vollständigen installierten Update-Vertrag

**Fundstelle:**
`.specify/presets/intake-authoring-governance/commands/speckit.intake-update.md:13`
bis `:27` und `:36` bis `:52`;
`specs/003-authoring-contract/plan.md:180` bis `:188`;
`specs/003-authoring-contract/data-model.md:71` bis `:81`;
`specs/003-authoring-contract/contracts/authoring-contract-design.json:154` bis
`:179`; ACG-019 in
`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json:415`
bis `:436`.

**Befund:** Der installierte Update-Vertrag verlangt aktuelle ausdrückliche
Update-Autorität, Prüfung von Ziel, Receipt, Quellen, Review, Git-Zustand und
unvollständigen Operationen, den Vorgänger-Intake als erste Quelle,
transaktionale Veröffentlichung sowie bytegleiche Archive von **Ziel und
Receipt** mit beiden Pfaden und Hashes in `supersedes`. Plan, Datenmodell und
ACG-019 nennen nur einen bytegleichen „Vorgänger“ beziehungsweise eine
Archivkopie im Singular. Zwar listet `renewalPaths` beide Archivpfade, es fehlt
aber eine ausführbare Gleichheits- und Supersession-Anforderung für das alte
Receipt sowie der Nachweis des Operation-Journals und seines terminalen
Transaktionszustands.

**Erforderliche Reparatur:** Die Renewal-Aufgabe und der additive Validator
müssen den installierten Update-Vertrag vollständig binden: Operationstyp
`Update`, aktuelle Autorität, Preflight/Git-Zustand, Vorgänger als erste Quelle,
bytegleiche aktive-zu-archivierte Ziel- **und** Receipt-Bytes samt Hashes und
Pfaden in `supersedes`, Staging, atomare Publikation/Rollback und terminaler
Operationstatus. Negative Fixtures müssen getrennt Zielarchivdrift,
Receipt-Archivdrift, falsche Quellenreihenfolge und unvollständige Operationen
ablehnen.

**Blockwirkung:** Die derzeitige Planung könnte eine scheinbar gültige neue
Leaf-Bindung erzeugen, obwohl Receipt-Lineage oder Authoring-Operation den
installierten Vertrag verletzt.

### PR304 — High — Zwei veröffentlichte Prüfkommandos sind nicht fail-closed

**Fundstelle:** `specs/003-authoring-contract/quickstart.md:61` bis `:75` und
`:108` bis `:127`; ACG-008 und ACG-013 in
`specs/003-authoring-contract/contracts/autonomous-run-gate-requirements.json:156`
bis `:174` und `:282` bis `:301`;
`scripts/invoke-psscriptanalyzer.ps1:103` bis `:124`.

**Befund:**

1. Die Bash-Schleife für 14 Receipts besitzt weder `errexit`/`pipefail` noch
   einen Fehler-Akkumulator. Scheitert ein früher Validator und besteht ein
   späterer, kann der Pipeline-Exitcode trotzdem `0` sein.
2. Der direkte PSScriptAnalyzer-Befehl prüft `$Error.Count`. Analyzer-Findings
   werden jedoch als Ausgabeobjekte geliefert; das vorhandene kanonische Skript
   sammelt sie deshalb ausdrücklich in `$findings` und beendet bei jedem Fund
   mit `1`. Der Quickstart-Befehl kann Warning-/Error-Findings als Erfolg melden.
3. Die beschriebene Plattformsequenz führt nur Quickstart-Abschnitte 2 bis 7
   aus, während der PSScriptAnalyzer-Befehl in Abschnitt 8 steht. Das bestehende
   Workflow-Skript analysiert zwar separat, doch diese Beziehung ist im
   acceptance-spezifischen Ablauf nicht eindeutig gebunden.

**Erforderliche Reparatur:** Die Receipt-Iteration muss alle 14 Ergebnisse
protokollieren und am Ende bei mindestens einem Fehler ungleich `0` liefern;
`jq`-Fehler müssen ebenfalls propagieren. Für PowerShell ist das vorhandene
kanonische `scripts/invoke-psscriptanalyzer.ps1` mit expliziter Repository-Wurzel
zu verwenden und als tatsächlicher Matrixbefehl einschließlich Version `1.25.0`
zu binden. Negative Harness-Fixtures müssen zeigen, dass ein früher
Receipt-Fehler und ein Analyzer-Finding den Gesamtgate wirklich sperren.

**Blockwirkung:** ACG-008 oder ACG-013 könnten trotz realer Fehler fälschlich
als bestanden dokumentiert werden.

### PR305 — High — Verbindlicher tests-first Vertikalschnitt fehlt

**Fundstelle:**
`.specify/presets/autonomous-run-governance/templates/plan-addendum.md:8` bis
`:20`; `specs/003-authoring-contract/plan.md:168` bis `:178` und
`specs/003-authoring-contract/quickstart.md:23` bis `:35` sowie `:89` bis `:106`.

**Befund:** Das installierte autonome Plan-Addendum verlangt einen
repräsentativen Vertikalschnitt mit Tests-first-Nachweis, die vollständige
Compile-/Ausführungsoberfläche vor dem ersten erwarteten Rotlauf und den exakten
Evidence-Pfad vor Implementierungsänderungen. Der Plan ändert dagegen zuerst
alle fünf Fachartefakte und danach ihre Konsumenten; die Fixtures werden erst
anschließend ausgeführt. Es gibt weder einen benannten ersten fehlschlagenden
Test noch die kleinste Artefakt-Validator-Fixture-Scheibe und keine Regel, die
erwartetes Rot von unerwartetem Gateversagen trennt.

**Erforderliche Reparatur:** Vor Tasks ist eine konkrete Reihenfolge zu
ergänzen: vollständige bestehende Ausführungsoberfläche prüfen, Evidence-Pfad
anlegen, einen kleinen positiven und negativen Fixture-Fall zuerst hinzufügen
und den erwarteten Fehler mit lokaler Ownership erfassen, die kleinste
Fachartefakt-/Validatoränderung umsetzen, beide Fälle grün machen und erst dann
auf den restlichen Vertrag erweitern. Die Reparaturen aus PR302 bis PR304 müssen
in diese vertikale Abfolge und ihre exakten Fixtures aufgenommen werden.

**Blockwirkung:** Tasks könnten die bindende Tests-first-Governance nicht
reproduzierbar und ohne vorweggenommenen Erfolg ausführen.

## Gate-Entscheidung und nächste sichere Aktion

Die Review-Aufgabe selbst ist `1/1` abgeschlossen. Wegen PR301 bis PR305 ist
`gatesSatisfied=false`; PlanReview ist `Blocked`. Es wurde kein Finding als
akzeptiertes Risiko herabgestuft.

Die nächste sichere Aktion ist eine begrenzte Plan-Remediation mit anschließendem
neuen unabhängigen PlanReview. Sie darf die alten Phase-Payloads, die
abgeschlossene Vier-Intake-Reparatur, Series/002 oder die anderen 13 Blätter
nicht umschreiben. Tasks oder Implementierung dürfen erst nach einem aktuellen
Review ohne offene Critical-/High-Findings beginnen.

Dieser Report referenziert ausschließlich die Entscheidung `UpdateRequired` in
`specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.
Er trifft keine zweite Documentation-Impact-Entscheidung.

# Independent Plan Review: Verifiable Intake Authoring Contract

## Result

**Blocked** — The single requested independent review task for run
`044b77ae-85fd-46ee-97f4-61ce7a2c9c66` is complete. The Plan artefacts match
the byte-bound Plan report, cover the five canonical domain artefacts, and
correctly plan essential security, language, platform, review, delivery, and
closeout boundaries. Five material findings remain open. The PlanReview gates
therefore do not pass, and handoff to Tasks is blocked.

Missing future implementation, test, PR, merge, lifecycle, or synchronization
results are not findings; they are expected to be absent now. The blockers are
missing or contradictory **design** for executable verification, complete
consumers, Update lineage, and causal closeout.

## Review boundary and integrity

- Only the independent review role for `speckit.plan` was performed.
- The Plan artefacts and accepted inputs were read without modification.
- The completed four-intake binding repair, its checker, Series/002, and the
  other 13 current leaves were treated as immutable predecessors.
- No Plan or design artefact was regenerated, no Tasks or implementation ran,
  no run state changed, and no Git or remote action occurred.
- `MergeAndSync` remains current. Normal reviews, checks, and an actually
  available approval remain mandatory; admin bypass remains forbidden.

The SHA-256 table in the German section records the normalized hashes verified
against `specs/003-authoring-contract/phase-results/plan-report.md`. The reporting
addendum and governance retrospective were reviewed as bounded supplemental
inputs, not as a new feature or a reason to regenerate completed phase payloads.

## Confirmed Plan quality

- Exactly five ordered canonical artefacts, receipt schema `2.0`, source order,
  normalized hashes, stable intake identity, and new event identities are
  represented.
- Blocked prompts are mechanically non-executable, while both ReadyForReview
  prompts bind the same target without implying follow-up authority.
- German first, English second, CEFR B2, first-use explanations, text-first
  output, and applicable WCAG 2.2 AA criteria have a semantic review gate.
- The completed repair is reused proportionately, while the planned domain
  renewal is limited to META-LH-03 and preserves the other 13 leaves and the
  Series bridge.
- Real operating systems and interpreter surfaces, exact HEAD and exit-code
  evidence, Gitleaks, PSScriptAnalyzer, and four independent reviews are named.
- Statistics, PreMerge, normal merge, lifecycle, and PostMerge evidence are
  causally separated without stash, reset, force, amend, or speculative history.
- The sole Documentation Impact decision remains the `UpdateRequired` decision
  in run evidence.

## Findings

### PR301 — High — Supplemental reporting delivery conflicts with the allowlist and closeout

The accepted addendum authorizes the five shared guidance files, governance
policy, feature report, addendum, and existing run evidence. The design still
marks the five guidance files immutable/out of scope, ACG-026 remains `N/A`, and
the reporting files are absent from required consumers and the three-path
evidence-only closeout. Add a bounded delivery/gate overlay that preserves old
phase payloads and domain scope while making this exact exception and causal
report finalization executable. Until then, Tasks cannot derive one coherent
allowlist or a satisfiable final reporting gate.

### PR302 — Critical — Global Ready cannot dispatch to the new bridge validator

The canonical Global-Ready entry point always invokes the frozen repair checker
when the META03 binding exists. That checker intentionally accepts only the old
repair projection, including the exact `0.3.0` to `0.3.1` target change. The new
additive validator is not wired into the dispatcher, and neither dispatcher nor
its tests are listed as consumers. Preserve the historical checker, but plan a
fail-closed dispatch contract and positive/negative tests for old and new bridge
states. Otherwise the planned current leaf cannot pass the real consumer.

### PR303 — High — Update lineage does not bind the complete installed Update contract

The installed Update operation requires current update authority, complete
target/receipt/source/review/Git preflight, the predecessor as the first source,
byte-identical archives of both target and receipt with paths and hashes in
`supersedes`, transactional publication, and terminal operation evidence. The
Plan and ACG-019 describe only a singular byte-identical predecessor. Bind every
Update invariant and add separate negative fixtures for target archive drift,
receipt archive drift, source-order drift, and an incomplete operation.

### PR304 — High — Two published verification commands are not fail closed

The Bash 14-receipt loop can return zero after an earlier failed validator, and
the direct PSScriptAnalyzer command checks `$Error.Count` instead of analyzer
result objects. The repository already provides a canonical analyzer script
that correctly fails on findings. Use a receipt accumulator with propagated
`jq` failures, bind the canonical analyzer script and version on all runners,
and prove both fail-closed paths with negative harness fixtures.

### PR305 — High — Required test-first vertical slice is absent

The installed autonomous Plan addendum requires a representative test-first
vertical slice, full execution-surface check before the first expected red
command, and creation of the evidence path before implementation edits. The
current sequence changes all five artefacts before running fixtures. Define one
small positive/negative fixture first, capture its expected failure, implement
the smallest artefact/validator slice, make it pass, and then expand. Include
the PR302–PR304 repairs in this exact sequence.

## Gate decision and next safe action

The review task itself is complete (`1/1`), but PR301 through PR305 make
`gatesSatisfied=false`; PlanReview is `Blocked`. No finding was downgraded to an
accepted risk.

The next safe action is bounded Plan remediation followed by a fresh independent
PlanReview. It must not rewrite completed phase payloads, the completed
four-intake repair, Series/002, or the other 13 leaves. Tasks and implementation
must not start until a current review has no open Critical or High finding.

This report only references the `UpdateRequired` decision in
`specs/003-authoring-contract/autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact`.
It makes no second Documentation Impact decision.
