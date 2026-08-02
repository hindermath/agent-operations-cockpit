# AEPS Preset Engineering – ruhender Programmauftrag / Dormant Program Charter

## Zweck und aktueller Zustand / Purpose and current state

Dieser Charter registriert den Folgeauftrag **AEPS – Agentic Engineering
Preset Engineering Program** im Level-0-System-of-Record. Der Auftrag ist
`Dormant` und darf erst nach einem ausdruecklichen menschlichen Start sowie
einem vollstaendig bestandenen RAW-Aktivierungsaudit beginnen. Die heutige
[Baseline](activation-baselines/2026-08-01.json) ist keine Aktivierung. / *This
charter registers the AEPS Preset Engineering follow-up in the level-0 system
of record. The program is dormant and may start only after an explicit human
invocation and a completely successful RAW activation audit. Today's baseline
is not an activation.*

Strategischer Anker ist
[`hindermath/home-baseline#196`](https://github.com/hindermath/home-baseline/issues/196).
Das AOC bleibt primaere Evidence-Quelle. TuiVision, TinyCalc und TinyPl0
liefern qualifizierte Vergleichsevidence. Level 0 fuehrt Analyse, Landkarte,
Entwuerfe und Abschlussnachweis. / *Issue 196 is the strategic anchor. AOC
remains the primary evidence source, while TuiVision, TinyCalc, and TinyPl0
provide qualified comparison evidence. Level 0 owns the analysis, maps,
drafts, and completion evidence.*

## Aktivierungsgrenze / Activation boundary

Ein spaeterer Aktivierungslauf MUSS fuer jedes Lastenheft RAW-01 bis RAW-09
alle folgenden Bedingungen nachweisen: / *A later activation run MUST prove
all following conditions for every intake from RAW-01 through RAW-09:*

- aktuelles, hashgebundenes und mit Bash sowie PowerShell validiertes
  Authoring Receipt;
- aktuelles, hashgebundenes Single Review mit Status `Ready`, ebenfalls ueber
  beide Validatoroberflaechen geprueft;
- Series-Lifecycle `Completed`;
- eigenes gueltiges Completion Receipt;
- vollstaendig dokumentierte Review Findings;
- dokumentierter Coverage-Status fuer jedes Finding;
- keine offenen blocking Findings.

Zusaetzlich MUSS ein aktuelles RAW-Serien-Completion-Receipt Manifest,
Reihenfolge, Reviews, Findings, Coverage und Einzel-Receipts hashgebunden
zusammenfuehren. `Ready` und `Completed` bleiben getrennte Achsen. Keine der
beiden Angaben ersetzt die andere. / *A current RAW series completion receipt
must additionally bind the manifest, order, reviews, findings, coverage, and
individual receipts. Ready and Completed remain separate axes and do not
replace each other.*

Der [maschinenlesbare Aktivierungsvertrag](activation-contract.json) ist fuer
Gate-Namen, Zustaende, Quellen, Deliverables und Verbote verbindlich. Scheitert
eine Bedingung, schreibt der Lauf ein Audit mit dem betroffenen Lastenheft, dem
fehlenden Nachweis und der gezielt benoetigten menschlichen Entscheidung. Der
Zustand wird `BlockedPreconditions`; Phase 1 startet nicht. / *The machine-
readable activation contract controls gate names, states, sources,
deliverables, and prohibitions. A failed condition produces an audit naming
the intake, missing evidence, and required human decision. The state becomes
BlockedPreconditions and Phase 1 does not start.*

## Phase 1 – Analyse / Analysis

Nach erfolgreicher Aktivierung werden alle Eingangsartefakte commit-, hash-
oder URL-gebunden eingefroren. Die Quellen umfassen mindestens alle AOC-,
META- und RAW-Lastenhefte, Reviews, Findings, Decision Intakes,
Coverage-Matrizen, Evidence, Receipts, Engineering Sessions, Retrospektiven,
vorhandenen GitHub-, Spec-Kit- und AEPS-Presets sowie Issue #196. / *After
successful activation, every input is frozen by commit, hash, or URL. Sources
include all AOC, META, and RAW intakes and their reviews, findings, decisions,
coverage, evidence, receipts, sessions, retrospectives, existing presets, and
Issue 196.*

Phase 1 erzeugt ausschliesslich: / *Phase 1 produces only:*

1. Preset Inventory
2. Existing Preset Map
3. Finding-to-Preset Matrix
4. Preset Gap Analysis
5. Candidate Preset Register
6. Existing Preset Extension Plan
7. New Preset Candidate Register
8. AEPS Domain Map
9. Promotion Readiness Matrix

Jeder Kandidat wird als `observation`, `pilot-pattern`, `candidate`, `stable`
oder `canonical` klassifiziert. `stable` und `canonical` duerfen nur einen
bereits belegten Zustand beschreiben. Dieser Arbeitsstrang promotet nichts.
Positive und negative Evidence, Grenzen, Gegenbeispiele und
Cross-Project-Potenzial muessen getrennt sichtbar bleiben. / *Stable and
canonical may only describe an already proven state. This workstream promotes
nothing. Positive and negative evidence, limits, counterexamples, and
cross-project potential remain explicit.*

## Phase 2 – entscheidungskompletter Reihenentwurf / Decision-complete series draft

Phase 2 erzeugt ausserhalb aktiver Intake-Verzeichnisse selbststaendig
reviewbare Entwuerfe fuer mindestens: Preset Inventory, Preset Registry,
Preset Lifecycle, Preset Candidate Intake, Preset Coverage, Preset Promotion,
Preset Versionierung, Preset Compatibility, Preset Migration, Preset
Deprecation, Cross-Project Validation, Preset Quality Assurance, Preset
Documentation, Preset Review, Preset Evidence und Preset Completion. / *Phase
2 creates independently reviewable drafts outside active intake directories
for all sixteen named preset-engineering topics.*

Die Entwuerfe sind Spec-Kit-kompatibel, receipt-faehig, evidenzbasiert,
projektuebergreifend nutzbar, DE-first, EN-second, CEFR B2 und WCAG 2.2 AA.
Die Reihe besitzt eindeutige Roots, genau einen Owner je Lastenheft und einen
azyklischen Abhaengigkeitsgraphen. / *Drafts are Spec-Kit compatible,
receipt-capable, evidence-based, cross-project usable, German first, English
second, CEFR B2, and WCAG 2.2 AA. The series has explicit roots, one owner per
intake, and an acyclic dependency graph.*

Phase 2 liefert zusaetzlich: / *Phase 2 additionally delivers:*

- `10` AEPS Lastenheft-Landkarte
- `11` AEPS Series Map
- `12` AEPS Ownership Matrix
- `13` AEPS Decision Map
- `14` AEPS Roadmap
- `15` Completion Receipt

## Architektur- und Stop-Regeln / Architecture and stop rules

Ein Preset darf nie aus einer einzelnen Idee oder nur einem erfolgreichen
Projekt abgeleitet werden. Erforderlich sind wiederholte Findings, Review,
positive und negative Evidence, Retrospektiven und eine projektuebergreifende
Bewertung. / *A preset must never be derived from one idea or one successful
project. Repeated findings, review, positive and negative evidence,
retrospectives, and cross-project assessment are required.*

Der Lauf endet mit `AwaitingAuthoringApproval`. Bis zu einer neuen
menschlichen Freigabe sind folgende Aktionen verboten: / *The run ends in
AwaitingAuthoringApproval. Until a new human approval, the following actions
are prohibited:*

- Presets erstellen, aendern, versionieren oder promoten;
- aktive Lastenhefte mit Intake-Authoring-Kommandos erzeugen;
- Specify-, Plan-, Tasks- oder Implementierungslaeufe starten;
- AOC-Produktcode oder Referenzprojekte veraendern;
- GitHub-Issues schreiben, pushen, mergen oder einen Bypass verwenden.

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle sind der menschlich bestaetigte
Folgeauftrag und Issue #196. Owner ist der Level-0-AEPS-Maintainer. Betroffen
sind dieser Charter, der Aktivierungsvertrag und die Baseline; Evidence ist
[documentation-impact-evidence.json](documentation-impact-evidence.json). /
*Decision: UpdateRequired. The approved follow-up and Issue 196 are the
sources. The level-0 AEPS maintainer owns this charter, activation contract,
and baseline.*
