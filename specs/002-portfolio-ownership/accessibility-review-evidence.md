# Barrierefreiheits- und Sprachreview / <span lang="en">Accessibility and Language Review</span>

## Rolle, Prüfgrenze und Begriffe / <span lang="en">Role, review boundary, and terms</span>

Die prüfende Rolle ist von Umsetzung und First-reader-Review unabhängig. Die
erste Prüfung fand vier blockierende Lücken in der damals noch nicht
vorhandenen vollständigen Textalternative. Diese Datei behebt ausschließlich
diese Evidence-Lücke; sie ändert keine Portfoliozelle und erteilt keine
Produkt-, RAW-, Level-0-, Preset-, Remote- oder Delivery-Autorität. Die
endgültige Disposition folgt aus der erneuten unabhängigen Prüfung.

<p lang="en"><em>The review role is independent from implementation and the
first-reader review. The first review found four blocking gaps in the
then-missing complete text alternative. This file remediates only that
evidence gap; it changes no portfolio cell and grants no product, RAW, Level-0,
preset, remote, or delivery authority. The final disposition comes from the
independent re-review.</em></p>

`Spec Kit` ist der repository-lokale, spezifikationsgetriebene Arbeitsablauf.
Ein `Concern` ist ein klar abgegrenztes fachliches Thema; sein `Owner` besitzt
Änderungsautorität nur für den benannten Vertrag. Ein `Producer` stellt einen
Handoff-Vertrag bereit, ein `Consumer` verwendet ihn. `Fail-closed` bedeutet:
Bei fehlender, veralteter oder unpassender Evidence stoppt die abhängige
Aktion. `BindingContract` ist eine zwingende Vertragskante;
`PreferredSerialOrder` ordnet Arbeit nur zeitlich. `Attestation` ist ein
prüfbarer Herkunfts- und Vertrauensnachweis. `Authority` bedeutet ausdrücklich
erteilte Handlungsbefugnis. Eine `Fixture` ist ein kontrollierter Testfall. Eine
topologische Reihenfolge ordnet alle Knoten so, dass jede gerichtete Kante nach
vorn zeigt. Weitere Definitionen stehen im
[zweisprachigen Glossar](../../requirements/baseline/glossary.md).

<p lang="en"><em>Spec Kit is the repository-local specification-driven
workflow. A concern is one bounded domain topic; its owner has change authority
only for the named contract. A producer provides a handoff contract and a
consumer uses it. Fail-closed means that dependent action stops when evidence
is missing, stale, or incompatible. BindingContract is mandatory;
PreferredSerialOrder only coordinates timing. Attestation is verifiable
provenance and trust evidence. Authority is explicitly granted permission to
act. A fixture is a controlled test case. A topological order lists every node
after its prerequisites.</em></p>

Der gelieferte Leserpfad verbindet die
[lesbare Portfolio-Übersicht](../../requirements/baseline/portfolio-ownership.md),
den [maschinenprüfbaren Portfoliovertrag](../../requirements/baseline/portfolio-ownership.json),
die [Decision Map mit offenen und bestätigten Entscheidungen](../../docs/decisions/open-decisions.md),
die [Feature-Spezifikation](spec.md) und das
[zweisprachige Glossar](../../requirements/baseline/glossary.md).

<p lang="en"><em>The delivered reader path connects the readable portfolio,
machine-checkable contract, decision map, feature specification, and bilingual
glossary.</em></p>

## Lineare Textalternative der Matrix / <span lang="en">Linear text alternative for the matrix</span>

### Deutsch

1. `C-01`, Referenz-Workspace, Discovery und Snapshot: Owner ist RAW-01.
   Quellen sind SRC-161 und SRC-177; abhängig sind RAW-02, RAW-03, RAW-05 und
   RAW-06. Der Handoff ist der Workspace Snapshot Contract. RAW-01 besitzt
   weder UI noch Commands. DEC-T02 bleibt für den Solution-/Projektzuschnitt
   offen; IAD101 bis IAD103 sind bestätigt. Das Parallelitätsrisiko ist am
   gemeinsamen Snapshot-Schema hoch.
2. `C-02`, Orchestration, Fokus und Routing: Owner ist RAW-02. Quellen sind
   SRC-162 und SRC-177; abhängig sind RAW-03 bis RAW-06. Der Handoff ist der
   Orchestration Context Contract. RAW-02 besitzt weder Zustandssemantik noch
   Geräteprotokolle. IAD201 bis IAD203 sind bestätigt; es gibt keine offene
   Decision. Das Risiko ist am Command-Bus hoch.
3. `C-03`, State, Authority und Freshness: Owner ist RAW-03. Quellen sind
   SRC-172, SRC-180 und SRC-181; abhängig sind RAW-02, RAW-04 und RAW-05. Der
   Handoff ist der State Envelope Contract. RAW-03 besitzt weder Darstellung
   noch Discovery. IAD301 bis IAD303 ersetzen DEC-T03 vollständig und
   bestätigen duale Zeit, relative Freshness-Profile und deterministische
   Confidence-Klassen. Das Risiko ist wegen der zentralen Semantik hoch.
4. `C-04`, Surfaces und Presentation Manager: Owner ist RAW-04. Quellen sind
   SRC-169 und SRC-172; abhängig ist RAW-07. Der Handoff ist der Presentation
   Contract. RAW-04 besitzt keine Workspace-Domainlogik. DEC-T04 zu TUI/UI,
   Responsiveness und Lokalisierung bleibt offen. Das Risiko bei
   Vertragsänderungen ist mittel.
5. `C-05`, Host, Sandbox, Container und Remote Node: Owner ist RAW-05. Quellen
   sind SRC-177 und SRC-181; abhängig sind RAW-02, RAW-06 und RAW-08. Der
   Handoff ist der Node Capability and Authority Contract. RAW-05 besitzt
   weder die Produkt-Working-Copy noch CLI-Semantik. IAD604 zum Remote
   Transport ist beantwortet; DEC-T06 zu Node Attestation und Timeout bleibt
   offen. Das Risiko an Trust- und Mount-Grenzen ist mittel.
6. `C-06`, CLI- und Environment-Capabilities: Owner ist RAW-06. Quelle ist
   SRC-162; abhängig sind RAW-02, RAW-05 und RAW-08. Der Handoff ist der CLI
   Capability Contract. RAW-06 besitzt weder UI noch Hardware. IAD601 bis
   IAD604 sind beantwortet. Das Risiko bei Prozess- und Environment-Verträgen
   ist mittel.
7. `C-07`, Gerätefähigkeiten und Adapter: Owner ist RAW-07. Quellen sind
   SRC-169, SRC-171, SRC-173 und SRC-175; abhängig ist RAW-04. Der Handoff ist
   der Hardware Capability Contract. RAW-07 besitzt weder Domänenlogik noch
   State. IAD701 bis IAD704 sind beantwortet. Das Risiko ist je Adapter niedrig
   und am gemeinsamen Vertrag hoch.
8. `C-08`, Program-to-Knowledge Workflow: Owner ist RAW-08. Quellen sind
   SRC-168 und SRC-174; abhängig ist RAW-09. Der Handoff ist der Evidence and
   Retrospective Contract. RAW-08 besitzt keine Produktzustandslogik. IAD801
   bis IAD803 sind beantwortet; DEC-T05 ist ersetzt. Das Risiko am
   Evidence-Schema ist mittel.
9. `C-09`, Preset-Gap und Promotion: Owner ist RAW-09. Quellen sind SRC-170 und
   SRC-174; es hängt keine Produktreihe ab. Der Handoff ist der Proposal
   Evidence Contract. RAW-09 besitzt keine Produkt- oder Delivery-Autorität.
   IAD901, IAD902 und AUTH-RAW09-PROMOTION sind beantwortet; jede Promotion
   benötigt eine neue menschliche Freigabe, und dieses Feature erteilt keine
   Preset-Promotion. Das Risiko der read-only Analyse ist niedrig.

### <span lang="en">English</span>

<ol lang="en">
<li><code>C-01</code>, reference workspace, discovery, and snapshot: RAW-01 owns the concern. Sources are SRC-161 and SRC-177; RAW-02, RAW-03, RAW-05, and RAW-06 depend on it. The handoff is Workspace Snapshot Contract. RAW-01 owns no UI or commands. DEC-T02 remains open for solution/project layout; IAD101 to IAD103 are confirmed. Concurrency risk is high at the shared schema.</li>
<li><code>C-02</code>, orchestration, focus, and routing: RAW-02 owns the concern. Sources are SRC-162 and SRC-177; RAW-03 through RAW-06 depend on it. The handoff is Orchestration Context Contract. RAW-02 owns neither state semantics nor device protocols. IAD201 to IAD203 are confirmed and no decision is open. Risk is high at the command bus.</li>
<li><code>C-03</code>, state, authority, and freshness: RAW-03 owns the concern. Sources are SRC-172, SRC-180, and SRC-181; RAW-02, RAW-04, and RAW-05 depend on it. The handoff is State Envelope Contract. RAW-03 owns neither presentation nor discovery. IAD301 to IAD303 fully replace DEC-T03 and confirm dual time, relative freshness profiles, and deterministic confidence classes. Risk is high because the semantics are central.</li>
<li><code>C-04</code>, surfaces and presentation manager: RAW-04 owns the concern. Sources are SRC-169 and SRC-172; RAW-07 depends on it. The handoff is Presentation Contract. RAW-04 owns no workspace domain logic. DEC-T04 remains open for TUI/UI, responsiveness, and localisation. Contract-change risk is medium.</li>
<li><code>C-05</code>, host, sandbox, container, and remote node: RAW-05 owns the concern. Sources are SRC-177 and SRC-181; RAW-02, RAW-06, and RAW-08 depend on it. The handoff is Node Capability and Authority Contract. RAW-05 owns neither the product working copy nor CLI semantics. IAD604 for remote transport is answered; DEC-T06 for node attestation and timeout remains open. Risk is medium at trust and mount boundaries.</li>
<li><code>C-06</code>, CLI and environment capabilities: RAW-06 owns the concern. Source is SRC-162; RAW-02, RAW-05, and RAW-08 depend on it. The handoff is CLI Capability Contract. RAW-06 owns neither UI nor hardware. IAD601 to IAD604 are answered. Process and environment contract risk is medium.</li>
<li><code>C-07</code>, hardware capabilities and adapters: RAW-07 owns the concern. Sources are SRC-169, SRC-171, SRC-173, and SRC-175; RAW-04 depends on it. The handoff is Hardware Capability Contract. RAW-07 owns neither domain logic nor state. IAD701 to IAD704 are answered. Risk is low per adapter and high at the shared contract.</li>
<li><code>C-08</code>, program-to-knowledge workflow: RAW-08 owns the concern. Sources are SRC-168 and SRC-174; RAW-09 depends on it. The handoff is Evidence and Retrospective Contract. RAW-08 owns no product-state logic. IAD801 to IAD803 are answered and DEC-T05 is superseded. Evidence-schema risk is medium.</li>
<li><code>C-09</code>, preset gaps and promotion: RAW-09 owns the concern. Sources are SRC-170 and SRC-174; no product series depends on it. The handoff is Proposal Evidence Contract. RAW-09 owns no product or delivery authority. IAD901, IAD902, and AUTH-RAW09-PROMOTION are answered; every promotion requires new human approval, and this feature grants no preset promotion. Read-only analysis risk is low.</li>
</ol>

## Lineare Textalternative des Handoff-Graphen / <span lang="en">Linear text alternative for the handoff graph</span>

### Deutsch

1. `H-01`: RAW-01 produziert für RAW-03 den Workspace Snapshot Contract in
   Version `requirements-v1`. Die Kante ist bindend. Ein fehlender oder
   unpassender Snapshot hält State auf Unknown und stoppt Folgeprojektionen.
2. `H-02`: RAW-01 produziert für RAW-02 denselben bindenden Vertrag und dieselbe
   Version. Fehlt er oder passt er nicht, stoppt Orchestration ohne geratenen
   Workspace-State.
3. `H-03`: RAW-03 produziert für RAW-02 den bindenden State Envelope Contract
   in Version `requirements-v1`. Unbekannter, veralteter oder unpassender State
   blockiert Seiteneffekte und abgeleiteten Kontext.
4. `H-04`: RAW-03 produziert denselben bindenden Vertrag für RAW-04. Ungültiger
   State erscheint als verschlechterter Text und wird nie zu Known aufgewertet.
5. `H-05`: RAW-04 produziert für RAW-07 den bindenden Presentation Contract in
   Version `requirements-v1`. Eine unpassende Version deaktiviert die
   Adapterfähigkeit sichtbar.
6. `H-06`: RAW-02 produziert für RAW-05 den Vertrag `Delivery ordering only`
   in Version `requirements-v1`. Die Kante `PreferredSerialOrder` ist
   ausdrücklich nicht bindend. RAW-05 darf read-only forschen, aber keine
   RAW-02-Implementierungsfakten ableiten.
7. `H-07`: RAW-05 produziert für RAW-06 den bindenden Node Capability and
   Authority Contract in Version `requirements-v1`. Fehlende Authority oder
   Node Capability verhindert Prozessausführung.
8. `H-08`: RAW-05 produziert denselben bindenden Vertrag für RAW-08. Unbekannte
   Node-Herkunft verhindert den Abschluss der Evidence.
9. `H-09`: RAW-06 produziert für RAW-08 den bindenden CLI Capability Contract
   in Version `requirements-v1`. Fehlende oder gescheiterte CLI-Evidence bleibt
   ein ausdrücklich unvollständiger Workflow-Status.
10. `H-10`: RAW-08 produziert für RAW-09 den bindenden Evidence and
    Retrospective Contract in Version `requirements-v1`. Unzureichende oder
    private Evidence blockiert Proposal-Abschluss und Promotion.

### <span lang="en">English</span>

<ol lang="en">
<li><code>H-01</code>: RAW-01 produces Workspace Snapshot Contract version <code>requirements-v1</code> for RAW-03. This edge is binding. A missing or incompatible snapshot keeps state Unknown and stops downstream projection.</li>
<li><code>H-02</code>: RAW-01 produces the same binding contract and version for RAW-02. A missing or incompatible snapshot stops orchestration without guessed state.</li>
<li><code>H-03</code>: RAW-03 produces binding State Envelope Contract version <code>requirements-v1</code> for RAW-02. Unknown, stale, or incompatible state blocks side effects and derived context.</li>
<li><code>H-04</code>: RAW-03 produces the same binding contract for RAW-04. Invalid state is shown as degraded text and is never promoted to Known.</li>
<li><code>H-05</code>: RAW-04 produces binding Presentation Contract version <code>requirements-v1</code> for RAW-07. An incompatible version visibly disables the adapter capability.</li>
<li><code>H-06</code>: RAW-02 produces contract <code>Delivery ordering only</code> version <code>requirements-v1</code> for RAW-05. This PreferredSerialOrder edge is explicitly non-binding. RAW-05 research may continue read-only but may infer no RAW-02 implementation fact.</li>
<li><code>H-07</code>: RAW-05 produces binding Node Capability and Authority Contract version <code>requirements-v1</code> for RAW-06. Missing authority or node capability prevents process execution.</li>
<li><code>H-08</code>: RAW-05 produces the same binding contract for RAW-08. Unknown node provenance prevents evidence completion.</li>
<li><code>H-09</code>: RAW-06 produces binding CLI Capability Contract version <code>requirements-v1</code> for RAW-08. Missing or failed CLI evidence remains an explicitly incomplete workflow state.</li>
<li><code>H-10</code>: RAW-08 produces binding Evidence and Retrospective Contract version <code>requirements-v1</code> for RAW-09. Insufficient or private evidence blocks proposal completion and promotion.</li>
</ol>

Die sichtbare topologische Reihenfolge ist RAW-01, RAW-03, RAW-02, RAW-04,
RAW-05, RAW-06, RAW-07, RAW-08 und RAW-09. Neun Kanten sind bindend; nur H-06
ist nicht bindend. Es gibt keinen Rückweg und keine implizite gegenseitige
Authority.

<p lang="en"><em>The visible topological order is RAW-01, RAW-03, RAW-02,
RAW-04, RAW-05, RAW-06, RAW-07, RAW-08, and RAW-09. Nine edges are binding;
only H-06 is non-binding. There is no return path or implicit mutual
authority.</em></p>

## Kriterien und bestätigte Evidence / <span lang="en">Criteria and confirmed evidence</span>

| Kriterium / <span lang="en">Criterion</span> | Status / <span lang="en">Status</span> | Begründung / <span lang="en">Rationale</span> |
|---|---|---|
| DE-first/EN-second | Pass | Jeder Abschnitt beginnt deutsch und liefert danach die englische Entsprechung. / <span lang="en">Every section starts in German and then provides its English equivalent.</span> |
| CEFR B2 | Pass | Kurze Sätze, aktive Verben und erklärte Fachwörter bilden den primären Leserpfad. / <span lang="en">Short sentences, active verbs, and defined terms form the primary path.</span> |
| Erstgebrauchserklärungen / <span lang="en">first-use explanations</span> | Pass | Alle für Matrix und Graph notwendigen Fachbegriffe stehen im ersten Abschnitt und verlinken das Glossar. / <span lang="en">Required terms are defined in the first section with a glossary link.</span> |
| Heading-Hierarchie / <span lang="en">heading hierarchy</span> | Pass | Genau eine H1; H2-Abschnitte und H3-Sprachpartner ohne Sprung. / <span lang="en">One H1 with H2 sections and H3 language partners without skipped levels.</span> |
| Beschreibende Links / <span lang="en">descriptive links</span> | Pass | Fünf repository-relative Links nennen Zweck und Ziel statt eines nackten Pfads. / <span lang="en">Five repository-relative links name purpose and target.</span> |
| Lineare Lesereihenfolge / <span lang="en">linear reading order</span> | Pass | Matrix und Graph sind jeweils vollständig als nummerierte DE- und EN-Listen verfügbar. / <span lang="en">Matrix and graph each have complete numbered German and English lists.</span> |
| Status nicht nur durch Farbe oder Position / <span lang="en">status beyond colour or position</span> | Pass | Answered, Open, Superseded, bindend und nicht bindend sind im Text benannt. / <span lang="en">Decision and binding states are explicitly named in text.</span> |
| WCAG 2.2 AA | Pass | Anwendbar sind Textalternativen, Struktur, Linkzweck, Sprache, Reflow und Nicht-Farb-Abhängigkeit. Der vollständige englische Alternativpfad besitzt maschinenlesbare HTML-`lang="en"`-Attribute; Markdown enthält keine zeit- oder zeigerabhängige Interaktion. / <span lang="en">Applicable evidence covers text alternatives, structure, link purpose, language, reflow, and independence from colour. The complete English alternative path carries machine-readable HTML `lang="en"` attributes; no timed or pointer interaction exists.</span> |

## Re-Review-Ergebnis / <span lang="en">Re-review result</span>

- Disposition: <span lang="en">`Pass`</span>
- `blocking findings: 0`
- Unabhängige Rolle / <span lang="en">independent role</span>: strikt read-only,
  getrennt von Umsetzung und First-reader-Review. / <span lang="en">Strictly
  read-only and separate from implementation and first-reader review.</span>
- Drei anfängliche und drei erste Re-Review-Blocker wurden behoben; die finale
  Re-Review bestätigte alle Kriterien. / <span lang="en">Three initial and
  three first re-review blockers were remediated; the final re-review confirmed
  every criterion.</span>
- Re-Review-Trigger: Änderung an Matrix, Handoff, Decision-Status, Glossar,
  Linkziel, Übersetzungsparität oder Heading-Struktur. /
  <span lang="en"><em>Re-review on any matrix, handoff, decision, glossary,
  link, translation, or heading drift.</em></span>
