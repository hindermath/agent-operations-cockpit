# Autonomie-, Parallelitäts- und Evidence-Modell / Autonomy, Parallelism, and Evidence Model

## Modi / Modes

- `manual-assisted`: Mensch entscheidet Materialfragen oder riskante Side Effects.
- `single-autonomous`: Ein begrenzter, reversibler Intake ohne gemeinsame Writes.
- `serial-autonomous`: Mehrere freigegebene Intakes in bindender Reihenfolge.
- `parallel-autonomous`: Nur disjunkte Worktrees/Writes, keine gemeinsame offene
  Decision und geplante Konsolidierung.
- `research-only`: Nur lesen, messen und Vorschläge erzeugen.
- `blocked`: Stop bis Authority, Decision oder Evidence vorliegt.

*A mode is eligibility, not execution authority. Every run still needs an exact
scope and current approval.*

Für die AOC-Programmreihe reicht auch eine individuelle Modus- oder
Eligibility-Einstufung nicht aus: Alle 14 Meta- und Fachlastenhefte benötigen
zuerst gleichzeitig aktuelle, formal validierte `Ready`-Single-Reviews. Bis
dahin sind Specify, Autonomous, Parallel Autonomous und Implementierung global
gesperrt. Nach Öffnung des Gates bleibt `META-LH-01` das erste Ziel und benötigt
einen separaten aktuellen Startauftrag; Drift schließt das Gate erneut. /
*For the AOC programme, individual mode or eligibility is insufficient. All 14
intakes first need current, formally validated Ready Single reviews. The global
gate blocks downstream work until then; afterwards `META-LH-01` is first and
still needs separate current authority. Drift closes the gate again.*

## Prüfkriterien / Assessment criteria

Jede Einstufung bewertet: Authority, Side Effects, Reversibilität, Schreibscope,
gemeinsame Decisions, Integrationsrisiko, Reviewbedarf sowie Abbruch und
Recovery. `Unknown` in einem Kriterium führt zu `blocked` oder
`manual-assisted`.

| Intake/Reihe | Authority | Side Effects / Reversibilität | Schreibscope | Decision-/Integrationsrisiko | Review und Recovery | Empfohlener Modus |
|---|---|---|---|---|---|---|
| META-01 | Level-2-Dokumente | docs-only, Git-revert | baseline | Quellenkonflikte mittel | unabhängiges Quellenreview | single-autonomous nach Create-Freigabe |
| META-02 | Portfolio | docs-only | ownership/manifests | Mehrfachowner hoch | DAG-Review; revert | manual-assisted |
| META-03 | Templates/Receipts | governance writes | templates/specs | Prozessvertrag hoch | Bash+PS Validator; revert | serial-autonomous |
| META-04 | Series/Eligibility | manifests | series paths | Scheduling hoch | DAG+Authority Review | manual-assisted |
| META-05 | neue Intakes | viele neue Dateien, reversibel | active intakes/receipts | gemeinsame Quellen mittel | Einzelreview, atomare Wave | serial-autonomous; parallel nur disjunkte Ziele |
| RAW-01 | read-only product slice | später Code, reversibel | eigene Feature-Worktree | zentrale Schema-Decisions | Security/A11Y/Platform Review | manual-assisted bis Decisions, dann single |
| RAW-02 | Orchestration | hohe Prozess-Side-Effects | eigene Reihe | IPC/Authority hoch | Integration und Recovery Pflicht | blocked bis RAW-01/03 |
| RAW-03 | State contracts | zunächst schemas/tests | eigene Reihe | zentrale Semantik hoch | Contract Review | serial nach RAW-01 |
| RAW-04 | Presentation contracts | UI/TUI später | eigene Reihe | State-Abhängigkeit | A11Y Review | serial nach RAW-03 |
| RAW-05 | Node discovery | read-only zuerst | eigene Reihe | Host/Sandbox Authority | Security Review | research-only, dann single |
| RAW-06 | CLI capabilities | Prozesseffekte später | eigene Reihe | Timeout/Exit/Secrets | Cross-platform Review | research-only bis Decision |
| RAW-07 | Hardware | Geräte-I/O; teilweise reversibel | Adapter je Gerät | SDK/Hardware mittel | Lab Evidence, kill switch | parallel je Adapter erst nach Contract |
| RAW-08 | Workflow Engine | Governance writes | evidence/workflow | Signatur/Persistenz mittel | Receipt Review | serial nach RAW-06/05 |
| RAW-09 | Preset Evolution | außerhalb AOC nur Vorschlag | evidence/proposals | geringe Produktintegration | menschliche Promotion | research-only |

## Evidence-Mindestvertrag / Minimum evidence contract

Positive Evidence zeigt das erwartete Verhalten mit Input, Umgebung, SHA und
Ergebnis. Negative Evidence zeigt mindestens einen absichtlich fehlerhaften,
stalen, nicht verfügbaren oder nicht autorisierten Fall und bestätigt, dass
kein verbotener Side Effect entstand. ProviderFailure, ProductFailure,
TestFailure und EvidenceUnavailable werden getrennt klassifiziert.

Abbruch erfolgt vor dem nächsten Write, wenn Scope, SHA, Authority oder
Decision driftet. Recovery verwendet sauberen Worktree, Receipt und letzten
bestätigten Checkpoint; kein Lauf rät einen fehlenden Zustand.
