# Offene und bestätigte menschliche Decisions / Open and Confirmed Human Decisions

## Offene Decisions / Open decisions

| ID | Reihe / Series | Entscheidung / Decision | Blockiert / Blocks | Frühester Entscheidungszeitpunkt / Earliest point |
|---|---|---|---|---|
| DEC-T02 | RAW-01 | Solution- und Projektzuschnitt; das Testframework ist bereits durch IAD103 bestätigt. / Solution and project layout; the test framework is already confirmed by IAD103. | Produkt-Scaffold / product scaffold | vor erstem Scaffold / before the first scaffold |
| DEC-T04 | RAW-04 | TUI/UI-Framework, Responsiveness und Lokalisierungsformat / TUI/UI framework, responsiveness, and localisation format | Presentation Plan | nach Console/JSON Contract / after the console/JSON contract |
| DEC-T06 | RAW-05 | Node Attestation und Timeout Policy / node attestation and timeout policy | Node Implementation | nach RAW-05 Research / after RAW-05 research |
| IAD601 | RAW-06 | sichere Process API / safe process API | CLI Capability | nach RAW-05 Research / after RAW-05 research |
| IAD602 | RAW-06 | Exit-, Signal-, Timeout- und Cancellation-Modell / exit, signal, timeout, and cancellation model | CLI Execution | nach Plattformmatrix / after the platform matrix |
| IAD603 | RAW-06 | Environment Allowlist und Secret Injection / environment allowlist and secret injection | CLI Execution | vor erstem Prozessstart / before the first process start |
| IAD604 | RAW-06/RAW-05 | Remote Transport | Remote Nodes | nach lokalem Slice / after the local slice |
| IAD701 | RAW-07 | MIDI-Bibliothek / MIDI library | MIDI Adapter | nach Reference-Lab-Evidence / after reference-lab evidence |
| IAD702 | RAW-07 | Elgato Transport/SDK Bridge | Stream Deck Adapter | nach Thin-Adapter-Review / after thin-adapter review |
| IAD703 | RAW-07 | erste freigegebene Gerätemenge / first approved device set | Hardware-Welle / hardware wave | nach Lab Inventory / after lab inventory |
| IAD704 | RAW-07 | physische Lab- und Safety-Freigabe / physical lab and safety approval | Geräte-I/O / device I/O | unmittelbar vor Feldtest / immediately before field testing |
| DEC-T05 | RAW-08 | Persistenz, Signatur und Retention für Evidence / persistence, signature, and retention for evidence | Workflow Plan | vor Workflow Implementation / before workflow implementation |
| IAD901 | RAW-09 | Promotion Threshold | Preset Proposal Completion | nach zwei Evidence-Paketen / after two evidence packages |
| IAD902 | RAW-09 | Zielrepository je Proposal / target repository per proposal | Preset Write | nach Proposal Review / after proposal review |

## Bestätigte und supersedierte Decisions / Confirmed and superseded decisions

| ID | Reihe / Series | Status | Nachweis und Supersession / Evidence and supersession |
|---|---|---|---|
| IAD101 | RAW-01 | Answered | `net10.0` ist als plattformneutraler TFM bestätigt und ersetzt den TFM-Anteil von DEC-T01. / `net10.0` is confirmed as the platform-neutral TFM and supersedes the TFM part of DEC-T01. |
| IAD102 | RAW-01 | Answered | `WorkspaceSnapshot` ist als versioniertes JSON plus JSON Schema bestätigt. / `WorkspaceSnapshot` is confirmed as versioned JSON plus JSON Schema. |
| IAD103 | RAW-01 | Answered | xUnit.net v3 mit Microsoft Testing Platform v2 ist bestätigt; DEC-T02 bleibt nur für Solution-/Projektzuschnitt offen. / xUnit.net v3 with Microsoft Testing Platform v2 is confirmed; DEC-T02 remains open only for solution/project layout. |
| IAD201 | RAW-02 | Answered | RAW-02 besitzt den transportneutralen IPC-/Prozessvertrag; konkrete Process API und Transport bleiben bei RAW-06. / RAW-02 owns the transport-neutral IPC/process contract; concrete process API and transport remain with RAW-06. |
| IAD202 | RAW-02 | Answered | Nur bestätigte Fokus-/Routingauswahl mit Schemaversion darf persistieren; Laufzeitkontext bleibt flüchtig. / Only confirmed focus/routing choices with schema version may persist; runtime context remains volatile. |
| IAD203 | RAW-02 | Answered | Queue-Reihenfolge, Idempotenz, Deduplizierung, Retry und Abbruch sind bestätigt; nicht-idempotente Aktionen werden nicht automatisch wiederholt. / Queue order, idempotency, deduplication, retry, and cancellation are confirmed; non-idempotent actions are not replayed automatically. |
| IAD301 | RAW-03 | Answered | `observed-at` nutzt die UTC-/RFC-3339-Uhr des beobachtenden Execution Nodes, `freshness-as-of` die UTC-/RFC-3339-Uhr des bewertenden AOC-Prozesses und laufende Dauer eine monotone Uhr. / Observed-at and freshness-as-of use their named UTC clocks; elapsed runtime uses a monotonic clock. |
| IAD302 | RAW-03 | Answered | Versionierte Source-/Capability-Profile verwenden das relative Modell `0,5T / T / 2T` und die Klassen `Fresh`, `Aging`, `Stale`, `Expired`, `Unknown`. / Versioned source/capability profiles use the relative model and five freshness classes. |
| IAD303 | RAW-03 | Answered | Confidence ist deterministisch `High`, `Medium`, `Low` oder `Unknown` mit Reason Code, niemals ein Prozentwert. / Confidence is a deterministic reasoned class, never a percentage. |
| DEC-T01 | RAW-01 | Superseded | Der frühere TFM-Anteil ist durch IAD101 ersetzt; kein offener Rest verbleibt. / The former TFM part is superseded by IAD101; no open remainder remains. |
| DEC-T03 | RAW-03 | Superseded | IAD301–IAD303 ersetzen Zeit-, Freshness- und Confidence-Anteil vollständig; kein offener Rest verbleibt. / IAD301-IAD303 fully supersede the time, freshness, and confidence parts; no open remainder remains. |

Eine offene Decision ist kein Fehler. Sie blockiert nur die ausdrücklich
genannte Arbeit. Antworten benötigen ein eigenes Decision Receipt und dürfen
nicht aus Bootstrap, Bibliotheksdefaults oder Agentenpräferenz abgeleitet
werden. Eine bestätigte Decision bleibt offenheitsfrei, bis eine ausdrücklich
dokumentierte Supersession sie ersetzt. / *An open decision is not an error. It
blocks only the named work. Answers require their own decision receipt and must
not be inferred from bootstrap defaults, library defaults, or agent preference.
A confirmed decision remains closed until an explicitly documented
supersession replaces it.*
