# Constraint Register / Constraint Register

Die Evidence-Spalte nennt den Nachweis oder bei phasenbezogenen Punkten den
Neubewertungs-Trigger. / *The evidence column names the proof or, for
phase-dependent items, the re-evaluation trigger.*

CEFR, WCAG, A11Y, Target Framework, WSL, CLI, GUI, TUI, Discovery, Raw MIDI,
DAG, Fixtures, NIST SSDF, CWE und MSL sind beim ersten Auftreten über das
[Glossar](glossary.md) erklärt. / *CEFR, WCAG, accessibility, target framework,
WSL, CLI, GUI, TUI, discovery, raw MIDI, DAG, fixtures, NIST SSDF, CWE, and MSL
are explained at first use through the [glossary](glossary.md).*

| ID | Verbindliche Anforderung / Binding constraint | Geltung und Nachweis / Applicability and evidence |
|---|---|---|
| CON-01 | Zielgruppe sind IHK-IT-Auszubildende ab Ausbildungsjahr 1 und erfahrene Fachkräfte. / The audience includes first-year IHK IT apprentices and experienced professionals. | Jedes Lastenheft nennt Zielgruppe und Vorwissen. / Every intake names its audience and prior knowledge. |
| CON-02 | CEFR B2; Fachbegriffe werden beim ersten Auftreten erklärt oder im Glossar verankert. / Use CEFR B2 and explain first-use terms or link them to the glossary. | Unabhängiges Sprachreview und Glossarlinks. / Independent language review and glossary links. |
| CON-03 | Deutsch steht zuerst und ist autoritativ; gleichwertiges Englisch folgt. / German comes first and is authoritative; equivalent English follows. | Bilinguales Review; eine Abweichung ist ein Finding. / Bilingual review; a deviation is a finding. |
| CON-04 | WCAG 2.2 AA gilt, soweit Kriterien anwendbar sind. / WCAG 2.2 AA applies wherever criteria are applicable. | Unabhängiges A11Y-Review mit positiver und negativer Evidence. / Independent accessibility review with positive and negative evidence. |
| CON-05 | Semantik, Tastatur, sichtbarer Fokus, Kontrast und Textalternativen gelten; Bedeutung hängt nie nur von Farbe ab. / Semantics, keyboard use, visible focus, contrast, and text alternatives apply; meaning never depends on colour alone. | Dokumentations- oder UI-Review; UI-Teile werden erst bei UI-Scope neu bewertet. / Documentation or UI review; UI aspects are re-evaluated when UI enters scope. |
| CON-06 | Interne Entstehungsgeschichte ist kein vorausgesetztes Wissen. / Internal project history is not assumed knowledge. | Eigenständiger Leserpfad-Test ohne Level-0-Lektüre. / Self-contained reader-path test without level-0 reading. |
| CON-07 | C#/.NET ist primär und speichersicher; die konkrete Version bleibt eine Decision. / C#/.NET is primary and memory-safe; the exact version remains a decision. | Kein implizites Target Framework im Intake; neu bei Runtime-Decision. / No implicit target framework in the intake; re-evaluate at a runtime decision. |
| CON-08 | macOS-first; Windows verbindlich; Linux, WSL und Container sind Nodes nach Applicability. / macOS first; Windows is mandatory; Linux, WSL, and containers are nodes as applicable. | Spätere Plattformmatrix; für diese Dokumentphase nicht bewertet. / Later platform matrix; not assessed for this documentation phase. |
| CON-09 | CLI-first; GUI, TUI und Hardware verwenden dieselben strukturierten Verträge. / CLI first; GUI, TUI, and hardware use the same structured contracts. | Spätere Vertrags- und Paritätstests; neu bei Produktoberfläche. / Later contract and parity tests; re-evaluate for a product interface. |
| CON-10 | Der erste Slice ist read-only: Discovery, Snapshot, Authority, Freshness und Projektion. / The first slice is read-only: discovery, snapshot, authority, freshness, and projection. | Spätere Tests verlangen null Command-Seiteneffekte. / Later tests require zero command side effects. |
| CON-11 | `Unknown`, `Stale`, `Unavailable` und Degraded Mode sind explizite Zustände. / `Unknown`, `Stale`, `Unavailable`, and degraded mode are explicit states. | Spätere negative Fixtures; neu bei Zustandsvertrag. / Later negative fixtures; re-evaluate with the state contract. |
| CON-12 | Host- und Sandbox-Authority dürfen nicht verwechselt werden. / Host and sandbox authority must not be confused. | Authority-Provenienz nennt Quelle und Grenze. / Authority provenance names its source and boundary. |
| CON-13 | Die ABS-DD-Sandbox ist Execution Node, nicht Product- oder Home-Owner. / The ABS-DD sandbox is an execution node, not a product or home owner. | Mount- und Write-Scope-Evidence; neu bei Sandbox-Integration. / Mount and write-scope evidence; re-evaluate for sandbox integration. |
| CON-14 | Hardware wird als Capability modelliert; Raw MIDI und Herstellerprotokolle bleiben in dünnen Adaptern. / Hardware is modelled as capabilities; raw MIDI and vendor protocols remain in thin adapters. | Spätere Boundary-Tests; neu bei Hardware-Scope. / Later boundary tests; re-evaluate when hardware enters scope. |
| CON-15 | Der Presentation Manager enthält keine Produktdomänenlogik. / The presentation manager contains no product-domain logic. | Späteres Architekturreview; neu bei Presentation-Implementierung. / Later architecture review; re-evaluate for presentation implementation. |
| CON-16 | Jeder Concern besitzt genau eine Owner-Reihe. / Every concern has exactly one owner series. | Ownership-Matrix ohne Mehrfachowner. / Ownership matrix without duplicate owners. |
| CON-17 | Der Abhängigkeitsgraph ist azyklisch; bindende und bevorzugte Kanten sind unterscheidbar. / The dependency graph is acyclic and distinguishes binding from preferred edges. | DAG-Validator und explizite Edge-Typen. / DAG validator and explicit edge types. |
| CON-18 | Parallelität ist nur bei disjunkten Schreibflächen und ohne gemeinsame offene Decision erlaubt. / Parallelism is allowed only for disjoint write surfaces and no shared open decision. | Eligibility-Receipt; neu bei Kampagnenauftrag. / Eligibility receipt; re-evaluate for a campaign instruction. |
| CON-19 | Positive und negative Evidence werden für jedes Lastenheft vorab definiert. / Positive and negative evidence is defined in advance for every intake. | Evidence-Plan vor Umsetzung. / Evidence plan before implementation. |
| CON-20 | Blocking Findings werden vor Freigabe der betroffenen Reihe behandelt. / Blocking findings are covered before the affected series is approved. | Coverage Matrix mit null blocking `Uncovered`. / Coverage matrix with zero blocking `Uncovered`. |
| CON-21 | Secrets, persönliche Pfade, Registry-Daten und nicht redistribuierbare Assets bleiben unveröffentlicht. / Secrets, personal paths, registry data, and non-redistributable assets remain unpublished. | Secret-Pattern-Scans und unabhängiges Public-Content-Review. / Secret-pattern scans and independent public-content review. |
| CON-22 | Schreib- und Remote-Autorität ist explizit, minimal und widerrufbar. / Write and remote authority is explicit, minimal, and revocable. | Aktuelle Benutzerautorität und Run-State werden getrennt geprüft. / Current user authority and run state are checked separately. |
| CON-23 | Meta-Lastenhefte erzeugen keine Produktimplementierung. / Meta requirements do not create product implementation. | Scope-Gate schließt Produktcode und Scaffold aus. / The scope gate excludes product code and scaffolding. |
| CON-24 | Evidence und Retrospektiven dürfen Preset-Evolution informieren; Presets besitzen keine Produktentscheidungen. / Evidence and retrospectives may inform preset evolution; presets own no product decisions. | Getrenntes AEPS-Receipt; neu bei autorisiertem Upstream-Handoff. / Separate AEPS receipt; re-evaluate for an authorised upstream handoff. |
| CON-25 | Sichere Architektur und sichere Codeerzeugung gelten zusätzlich zum MSL-Status. / Secure architecture and secure code generation apply in addition to MSL status. | NIST SSDF und CWE bleiben anwendbar; Produktdetails werden erst bei Produktcode bewertet. / NIST SSDF and CWE remain applicable; product details are assessed only when product code enters scope. |

Weiter im Leserpfad: [Findings Ledger](review-findings-ledger.md). / *Continue
with the findings ledger.*
