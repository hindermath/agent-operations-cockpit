# Constraint Register / Constraint Register

| ID | Verbindliche Anforderung / Binding constraint | Geltung und Nachweis / Applicability and evidence |
|---|---|---|
| CON-01 | Zielgruppe sind IHK-IT-Auszubildende ab Ausbildungsjahr 1 und erfahrene Fachkräfte. / Audience includes first-year IHK IT apprentices and experienced professionals. | Jedes Lastenheft nennt Zielgruppe und Vorwissen. |
| CON-02 | CEFR B2; Fachbegriffe beim ersten Auftreten erklären oder im Glossar verankern. / CEFR B2; explain terms at first use or in the glossary. | Sprachreview und Glossarlinks. |
| CON-03 | Deutsch zuerst und autoritativ, Englisch danach konsistent. / German first and authoritative, English second and consistent. | Bilinguales Review; Abweichung ist Finding. |
| CON-04 | WCAG 2.2 AA soweit anwendbar. / WCAG 2.2 AA where applicable. | A11Y-Checklist und positive/negative Evidence. |
| CON-05 | Semantik, Tastatur, sichtbarer Fokus, Kontrast, Textalternativen; keine Nur-Farbe-Bedeutung. / Semantics, keyboard, visible focus, contrast, alternatives; no colour-only meaning. | UI-/Dokumentationsreview. |
| CON-06 | Keine Kenntnis der internen Entstehungsgeschichte voraussetzen. / Do not assume internal project history. | Eigenständigkeitsreview. |
| CON-07 | C#/.NET ist primär und speichersicher; konkrete Version bleibt Decision. / C#/.NET is primary and memory safe; exact version is a decision. | Kein implizites TFM im Intake. |
| CON-08 | macOS-first; Windows verbindlich; Linux/WSL/Container als Nodes nach Applicability. / macOS first; Windows mandatory; Linux/WSL/containers as applicable nodes. | Plattformmatrix. |
| CON-09 | CLI-first; GUI/TUI/Hardware verwenden dieselben strukturierten Verträge. / CLI first; GUI/TUI/hardware use the same structured contracts. | Contract- und Paritätstests. |
| CON-10 | Erster Slice ist read-only: Discovery, Snapshot, Authority, Freshness, Projektion. / First slice is read-only. | Keine Command-Seiteneffekte. |
| CON-11 | Zustände `Unknown`, `Stale`, `Unavailable` und Degraded Mode sind explizit. / States are explicit. | Negative Fixtures. |
| CON-12 | Host- und Sandbox-Authority dürfen nicht verwechselt werden. / Host and sandbox authority must not be confused. | Authority-Provenienz. |
| CON-13 | ABS-DD-Sandbox ist Execution Node, nicht Product- oder Home-Owner. / Sandbox is an execution node, not product or home owner. | Mount-/Write-Scope-Evidence. |
| CON-14 | Hardware wird als Capability modelliert; Raw MIDI und Herstellerprotokolle bleiben in dünnen Adaptern. / Hardware is capability-modelled; raw protocols stay in thin adapters. | Boundary-Tests. |
| CON-15 | Presentation Manager enthält keine Produktdomänenlogik. / Presentation manager contains no product domain logic. | Architekturreview. |
| CON-16 | Jeder Concern hat genau eine Owner-Reihe. / Each concern has exactly one owner series. | Ownership-Matrix ohne Duplikat. |
| CON-17 | Abhängigkeitsgraph ist azyklisch; bindende und bevorzugte Kanten sind unterscheidbar. / Dependency graph is acyclic and edge semantics are explicit. | DAG-Validator. |
| CON-18 | Parallelität nur bei disjunkten Schreibflächen und ohne gemeinsame offene Decision. / Parallelism only with disjoint write scopes and no shared open decision. | Eligibility-Receipt. |
| CON-19 | Positive und negative Evidence sind für jedes Lastenheft vorab definiert. / Positive and negative evidence is predefined. | Evidence-Plan. |
| CON-20 | Blocking Findings müssen vor Freigabe der betroffenen Reihe behandelt sein. / Blocking findings must be covered before series approval. | Coverage Matrix. |
| CON-21 | Secrets, persönliche Pfade, Registry-Daten und nicht redistribuierbare Assets bleiben unveröffentlicht. / Exclude secrets, personal paths, registry data, and non-redistributable assets. | Full-history and directory scans. |
| CON-22 | Schreib- und Remote-Autorität ist explizit, minimal und widerrufbar. / Write and remote authority is explicit, minimal, and revocable. | Authority Receipt. |
| CON-23 | Meta-Lastenhefte erzeugen keine Produktimplementierung. / Meta requirements do not create product implementation. | Prompt- und Scope-Gate. |
| CON-24 | Evidence und Retrospektiven dürfen Preset-Evolution informieren, aber Presets besitzen keine Produktentscheidungen. / Evidence may inform presets; presets do not own product decisions. | Handoff-Review. |
| CON-25 | Sichere Architektur und sichere Codeerzeugung gelten zusätzlich zum MSL-Status. / Secure architecture and code generation apply in addition to MSL status. | Security-Governance-Evidence. |
