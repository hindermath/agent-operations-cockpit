# Authority- und Stop-Gates / Authority and Stop Gates

| Gate | Erlaubt / Allows | Stoppt bei / Stops when | Menschliche Entscheidung / Human decision |
|---|---|---|---|
| G-00 Public Readiness | Exakten geprüften Basis-SHA veröffentlichen. | Scan-, Lizenz-, Pfad-, Ruleset- oder Freigabelücke. | Bereits für Basis-SHA erteilt. |
| G-01 Source Baseline | Quellen und Findings lokal authorieren/reviewen. | Uncovered blocking Finding oder versteckte Level-0-Abhängigkeit. | Baseline akzeptieren oder korrigieren. |
| G-02 Portfolio | Owner, Handoffs und DAG festlegen. | Mehrfachowner, Zyklus oder unklare Decision. | Portfolio bestätigen. |
| G-03 Authoring | Neue Intakes mit Receipts erzeugen. | Bestehendes Ziel, Secret, offene Materialentscheidung oder Validatorfehler. | Create-/Update-Autorität getrennt. |
| G-04 Series Eligibility | Reihenfolge und Autonomiemodus empfehlen. | Gemeinsame Writes, Decision-Abhängigkeit, fehlendes Review/Recovery. | Parallelität ausdrücklich freigeben. |
| G-05 Specify | Genau ein reviewtes Lastenheft in eine Spezifikation überführen. | Intake nicht `Approved`, SHA driftet oder Authority fehlt. | Separater Startauftrag. |
| G-06 Implementation | Plan/Tasks/Code aus freigegebener Spezifikation. | Sicherheits-, Architektur-, Test- oder Scope-Gate offen. | Separater Implementierungsauftrag. |
| G-07 Command/Hardware | Reversible Commands oder Geräteadapter entwickeln. | Read-only Slice nicht stabil, Trust/Recovery offen. | Eigene Decision und Lastenheftfreigabe. |
| G-08 Preset Evolution | Generalisierbare Evidence in Preset-Vorschlag übergeben. | Nur projektspezifische Beobachtung oder Produktentscheidung. | Separate Preset-Promotion. |

*Every gate is fail-closed: missing or stale evidence is not approval. Admin
bypass changes delivery mechanics only and never satisfies a quality gate.*
