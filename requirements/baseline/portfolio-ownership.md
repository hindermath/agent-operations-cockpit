# Lastenheft-Portfolio und Ownership / Requirements Portfolio and Ownership

| Concern | Kanonische Owner-Reihe / Canonical owner | Quellen / Sources | Abhängige Reihen / Dependents | Handoff | Explizite Non-Ownership | Offene Decisions | Parallelitätsrisiko |
|---|---|---|---|---|---|---|---|
| Referenz-Workspace, Discovery, Snapshot | RAW-01 Reference Agentic Workspace | 161, 177 | RAW-02,03,05,06 | versionierter Workspace Snapshot | Keine UI, keine Commands | TFM, Workspace-Manifestformat | Hoch bei gemeinsamem Snapshot-Schema |
| Orchestration, Fokus, Routing | RAW-02 Workspace Orchestrator | 162,177 | RAW-03,04,05,06 | Orchestration Context | Keine Zustandssemantik, keine Geräteprotokolle | Prozess-/IPC-Vertrag | Hoch bei Command-Bus |
| State, Authority, Freshness | RAW-03 State Truthfulness | 172,180,181 | RAW-02,04,05 | canonical State Envelope | Keine Darstellung, keine Discovery | Zeitquelle, Confidence-Modell | Hoch; zentrale Semantik |
| Surfaces und Presentation Manager | RAW-04 Presentation Fabric | 169,172 | RAW-07 | Presentation Contract | Keine Workspace-Domainlogik | TUI/UI-Framework | Mittel bei Contract-Änderung |
| Host, Sandbox, Container, Remote Node | RAW-05 Execution Nodes | 177,181 | RAW-02,06 | Node Capability/Authority Descriptor | Kein Produkt-Working-Copy-Owner | Remote Transport | Mittel |
| CLI und Environment Capabilities | RAW-06 CLI Capability and Environment Orchestration | 162 | RAW-02,05,08 | typed CLI Capability Descriptor | Keine UI und keine Hardware | Prozessausführung, Exit-/Timeoutmodell | Mittel |
| Gerätefähigkeiten und Adapter | RAW-07 Hardware Capability Layer | 169,171,173,175 | RAW-04 | normalized Input/Output Capability | Keine Domänenlogik, kein State Owner | MIDI-/Elgato-Bibliothek, Gerätefreigabe | Niedrig je Adapter, hoch am gemeinsamen Contract |
| Program-to-Knowledge Workflow | RAW-08 Workflow Engine | 168,174 | RAW-09 | Evidence/Receipt/Retrospective Package | Keine Produktzustandslogik | Persistenz- und Signaturformat | Mittel |
| Preset-Gap und Promotion | RAW-09 Preset Evolution | 170,174 | keine Produktreihe | generalisierte Proposal Evidence | Keine Produkt- oder Delivery-Autorität | Promotion-Kriterien | Niedrig bei read-only Analyse |

## Abhängigkeitsgraph / Dependency graph

```text
RAW-01 -> RAW-03 -> RAW-04 -> RAW-07
RAW-01 -> RAW-02 -> RAW-05 -> RAW-06
RAW-03 -> RAW-02
RAW-06 -> RAW-08 -> RAW-09
RAW-05 -> RAW-08
```

Die Kanten sind Anforderungen-/Vertragshandoffs. Topologische Prüfung ergibt
keinen Zyklus. RAW-05 und RAW-06 dürfen in einer detaillierten Planung ihre
Reihenfolge nur ändern, wenn Node- und CLI-Verträge zuvor getrennt stabilisiert
sind. / *Edges are requirement or contract handoffs. The graph is acyclic.*
