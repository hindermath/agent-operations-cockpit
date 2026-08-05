# Authority- und Stop-Gates / Authority and Stop Gates

| Gate | Erlaubt / Allows | Stoppt bei / Stops when | Menschliche Entscheidung / Human decision |
|---|---|---|---|
| G-00 Public Readiness | Exakten geprüften Basis-SHA veröffentlichen. | Scan-, Lizenz-, Pfad-, Ruleset- oder Freigabelücke. | Bereits für Basis-SHA erteilt. |
| G-01 Source Baseline | Quellen und Findings lokal authorieren/reviewen. | Uncovered blocking Finding oder versteckte Level-0-Abhängigkeit. | Baseline akzeptieren oder korrigieren. |
| G-02 Portfolio | Owner, Handoffs und DAG festlegen. | Mehrfachowner, Zyklus oder unklare Decision. | Portfolio bestätigen. |
| G-03 Authoring | Neue Intakes mit Receipts erzeugen. | Bestehendes Ziel, Secret, offene Materialentscheidung oder Validatorfehler. | Create-/Update-Autorität getrennt. |
| G-04 Series Eligibility | Reihenfolge und Autonomiemodus empfehlen. | Gemeinsame Writes, Decision-Abhängigkeit, fehlendes Review/Recovery. | Parallelität ausdrücklich freigeben. |
| G-05 Global Review / Specify | Erst nach aktueller formaler `Ready`-Coverage aller 14 AOC-Lastenhefte genau `META-LH-01` in die erste Spezifikation überführen. | Mindestens ein Ziel ist nicht `Ready`, Target/Hash/Receipt/Validator-Evidence driftet, das Ergebnis ist supersediert oder Authority fehlt. | Nach vollständiger Coverage separater Startauftrag für `META-LH-01`. |
| G-06 Implementation | Plan/Tasks/Code aus freigegebener Spezifikation. | Sicherheits-, Architektur-, Test- oder Scope-Gate offen. | Separater Implementierungsauftrag. |
| G-07 Command/Hardware | Reversible Commands oder Geräteadapter entwickeln. | Read-only Slice nicht stabil, Trust/Recovery offen. | Eigene Decision und Lastenheftfreigabe. |
| G-08 Preset Evolution | Generalisierbare Evidence in Preset-Vorschlag übergeben. | Nur projektspezifische Beobachtung oder Produktentscheidung. | Separate Preset-Promotion. |

*Every gate is fail-closed: missing or stale evidence is not approval. Admin
bypass changes delivery mechanics only and never satisfies a quality gate.*

## AOC-weite Review-Sperre / AOC-wide review gate

G-05 ist für die kanonische AOC-Programmreihe ein globales, fail-closed Gate.
Alle 14 Lastenhefte `META-LH-01` bis `META-LH-05` und `RAW-01` bis `RAW-09`
müssen gleichzeitig ein aktuelles, formal validiertes `Ready`-Single-Review
besitzen. Zielpfad und normalisierter Zielhash müssen dem aktiven Lastenheft
entsprechen; das Authoring Receipt und die Bash- sowie PowerShell-Validierung
müssen aktuell sein. `ReadyWithAcceptedRisks`, supersedierte Ergebnisse und
Series-Lifecycle-Werte erteilen keine Ausnahme.

Vor vollständiger Coverage sind `speckit specify`, Autonomous, Parallel
Autonomous und Implementierung für jedes Ziel gesperrt. Danach ist
`META-LH-01` zwingend das erste Ziel und benötigt einen neuen, ausdrücklichen
Startauftrag. Änderungen an einem Ziel oder seiner Review-Evidence schließen
das Gate erneut. Die älteren Root-Lastenhefte sind nicht Teil dieser
14er-Programmmenge. Review, Series-Lifecycle, Global-Gate-Status und konkrete
Ausführungsautorität bleiben getrennte Wahrheiten.

*G-05 is a global fail-closed gate for the canonical AOC programme. All 14 META
and RAW intakes must simultaneously have current, formally validated `Ready`
Single reviews with matching target path, normalised hash, current Authoring
Receipt, and passing Bash and PowerShell validation. Accepted-risk or
superseded results and lifecycle values grant no exception. Before full
coverage, Specify, autonomous, parallel-autonomous, and implementation work is
blocked for every target. Afterwards `META-LH-01` is mandatory as the first
target and still requires a new explicit start instruction. Any drift closes
the gate again. Legacy root intakes are outside this fourteen-intake set.*
