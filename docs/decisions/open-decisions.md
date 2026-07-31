# Offene menschliche Decisions / Open Human Decisions

| ID | Reihe | Entscheidung / Decision | Blockiert / Blocks | Frühester Entscheidungszeitpunkt / Earliest point |
|---|---|---|---|---|
| IAD201 | RAW-02 | IPC-/Prozessvertrag | Orchestrator Specify/Autonomy | nach RAW-01/03 Review |
| IAD202 | RAW-02 | Persistenz des Session Context | Orchestrator Plan | nach State Contract |
| IAD203 | RAW-02 | Command Queue und Idempotenz | mutierende Commands | nach read-only Slice |
| IAD601 | RAW-06 | sichere Process API | CLI Capability | nach RAW-05 Research |
| IAD602 | RAW-06 | Exit-, Signal-, Timeout- und Cancellation-Modell | CLI Execution | nach Plattformmatrix |
| IAD603 | RAW-06 | Environment Allowlist und Secret Injection | CLI Execution | vor erstem Prozessstart |
| IAD604 | RAW-06 | Remote Transport | Remote Nodes | nach lokalem Slice |
| IAD701 | RAW-07 | MIDI-Bibliothek | MIDI Adapter | nach Reference-Lab-Evidence |
| IAD702 | RAW-07 | Elgato Transport/SDK Bridge | Stream Deck Adapter | nach Thin-Adapter-Review |
| IAD703 | RAW-07 | erste freigegebene Gerätemenge | Hardware-Welle | nach Lab Inventory |
| IAD704 | RAW-07 | physische Lab- und Safety-Freigabe | Geräte-I/O | unmittelbar vor Feldtest |
| IAD901 | RAW-09 | Promotion Threshold | Preset Proposal Completion | nach zwei Evidence-Paketen |
| IAD902 | RAW-09 | Zielrepository je Proposal | Preset Write | nach Proposal Review |
| DEC-T01 | RAW-01 | konkrete .NET-/C#-Version und TFM | Produkt-Scaffold | vor erstem Scaffold |
| DEC-T02 | RAW-01 | Solution-/Projektzuschnitt und Testframework | Build/Test | vor erstem Scaffold |
| DEC-T03 | RAW-03 | Zeitquelle und Freshness-Schwellen | State Implementation | vor State Plan |
| DEC-T04 | RAW-04 | TUI/UI-Framework | Presentation Plan | nach Console/JSON Contract |
| DEC-T05 | RAW-08 | Persistenz, Signatur und Retention für Evidence | Workflow Plan | vor Workflow Implementation |

Eine offene Decision ist kein Fehler. Sie blockiert nur die ausdrücklich
genannte Arbeit. Antworten benötigen eigenes Decision Receipt und dürfen nicht
aus Bootstrap, Bibliotheksdefaults oder Agentenpräferenz abgeleitet werden.

*An open decision is not an error. It blocks only the named work. Answers need
their own decision receipt and must not be inferred from bootstrap defaults,
library defaults, or agent preference.*
