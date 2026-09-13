# Datenmodell / Data Model

## Quellen und Lebensdauer / Sources and lifetime

Der [bestehende Kriterienvertrag](../../requirements/baseline/series-eligibility-contract.json) und das [Series-Manifest](../intake-series/aoc-phase-2/manifest.json) bleiben kanonisch. Die folgenden Ergebnisobjekte leben nur im Speicher und auf stdout. Status/Next speichern weder Manifest noch Receipt oder Laufzustand. / *The existing criteria contract and series manifest remain canonical. The following result objects live only in memory and on stdout. Status/next store no manifest, receipt, or run state.*

## Bestehende Entitäten / Existing entities

| Entität / Entity | Felder und Regeln / Fields and rules |
|---|---|
| `SeriesEligibilityContract` | Schema `1.0`; exakt neun eindeutige `criteria`, sechs `modes`, vorhandene `parallelEligibility` und `failureTaxonomy`. Keine Schemaänderung. / Exact existing criteria, modes, parallel rules and failure taxonomy; no schema change. |
| `IntakeSeriesManifest` | Schema `1.0`; `seriesId`, `title`, `policy`, `status`, `orderedTargets`, `roots`, `dependencies`, `evidencePaths`. Pfade repository-relativ und innerhalb der Wurzel; bestehende Lifecycle-Auflösung. / Repository-relative contained paths; existing lifecycle resolution. |
| `orderedTargets[]` | `path`, `role`, `normalizedSha256`, `status`; eindeutige stabile Reihenfolge. `Pending`, `Blocked`, `Eligible`, `Active`, `Completed`, `Withdrawn` bleiben deklarierte Werte. / Unique stable order; target states remain declared values. |
| `dependencies[]` | `from`, `to`, `kind`, `binding`; bestehende Kind-/Binding-Zuordnung. DAG bedeutet gerichteter Graph ohne Zyklus. Roots entsprechen exakt den Knoten ohne eingehende Kante. / Reuse edge kinds and binding rules; roots exactly match zero-indegree nodes. |
| Authority-/Review-Evidence | Benutzerauftrag, dessen Scope, aktuelle Ziel-/Reviewhashes; historische Receipt-Autorität ist Herkunft. Kein boolesches Fixture-Feld beweist reale Benutzerautorität. / Instruction, scope and current target/review hashes; historical receipt authority is provenance. A fixture boolean does not prove real authority. |
| `IntakeSeriesReceipt` | Bestehende Operation, Manifesthash, Vorgänger-/Archiv-/Tombstonebindung. Nur lesen; keine neue Receipt-Art. / Read existing operation and lineage bindings; no new receipt type. |

Hashes verwenden UTF-8 ohne BOM, CRLF/CR werden LF, sonst bleibt Text unverändert. Die bestehende Normalisierung wird wiederverwendet. / *Hashes use UTF-8 without BOM, normalize CRLF/CR to LF, and preserve other text. Reuse existing normalization.*

## Kriterienwerte / Criterion values

Der neue Prüfer akzeptiert die vorhandenen positiven Werte und die beiden belegten negativen Varianten. Fehlende, leere, unbekannte oder widersprüchliche Werte werden blockiert. Zusätzliche Wertdialekte werden nicht erfunden; bei einem späteren legitimen Bedarf ist der Vertrag neu zu prüfen. / *The new checker accepts existing positive values and the two proven negative variants. Missing, empty, unknown, or contradictory values block. Do not invent additional value dialects; reassess the contract if a legitimate need arises.*

| Schlüssel / Key | Positiver Wert / Positive value | Belegte Konsistenzregel / Proven consistency rule |
|---|---|---|
| `authority` | `current-and-explicit` | `currentAuthority` muss Boolean true sein. / Must be boolean true. |
| `sideEffects` | `bounded` | Alle Änderungen begrenzt; Abfrage erzeugt keine. / Bounded changes; query causes none. |
| `reversibility` | `recoverable` | Recovery nicht durch einen früheren Pass ersetzen. / Earlier pass cannot replace recovery. |
| `writeScope` | `disjoint` | `shared` mit `disjointWrites=false` blockiert Parallelität; Widerspruch blockiert. / Shared writes block parallelism; contradiction blocks. |
| `decisions` | `no-shared-open-decisions` | `shared-open-decision` mit `sharedOpenDecisions=true` blockiert Parallelität. / Shared open decisions block parallelism. |
| `integration` | `planned` | Leer oder unbekannt blockiert. / Empty or unknown blocks. |
| `review` | `consolidation-review-planned` | Muss zu Boolean `consolidationReview` passen. / Must agree with the boolean. |
| `abort` | `defined` | Muss zu Boolean `abortRule` passen. / Must agree with the boolean. |
| `recovery` | `defined` | Muss zu Boolean `recoveryRule` passen. / Must agree with the boolean. |

Für `parallel-autonomous` müssen alle sechs Parallelflags vorhanden und echte Booleans sein. Für die anderen fünf Modi ist `currentAuthority` Pflicht; die fünf übrigen Parallelflags sind optional und dürfen keine zusätzliche Parallelfreigabepflicht erzeugen. Vorhandene Flags müssen echte Booleans sein; Strings, Zahlen und null gelten nicht als Ersatz. JSON wird mit Duplicate-Key-Erkennung gelesen, bevor ein Dictionary Schlüssel verlieren kann. Gleiches gilt für doppelte Top-Level-Felder. / *All six parallel flags are mandatory for parallel-autonomous. Other modes require currentAuthority; the remaining five parallel flags are optional and must not impose parallel approval requirements. Present flags must be actual booleans; strings, numbers, and null are not substitutes. Detect duplicate JSON keys before a dictionary can discard them, including duplicate top-level fields.*

## Abgeleitete Ergebnisse / Derived results

Die konkrete Schnittstelle steht im [CLI-Vertrag](contracts/series-eligibility-interface.md). / *The interface contract defines the concrete representation.*

- `EligibilityAssessment`: Schema `1.0`, `mode`, `criteria`, `outcome`, `reasons`, `nextAction`, `failureClass`, `authorityGranted=false`. Modus und Ergebnis sind getrennt; negatives Parallelassessment behält `mode=parallel-autonomous`. / *Mode and outcome stay separate; a negative parallel assessment retains its mode.*
- `SeriesProjection`: getrennte Felder `declaredLifecycle`, `reviewState`, `eligibleCandidates`, `preferredCandidate`, `blockers`, `deliveryMode`, `currentStartAuthority`, `historicalReceiptProvenance`, `nextAction`, `failureClass`, `authorityGranted=false`. Review nur aus aktueller validierter Evidence übernehmen; sonst `NotAssessed`, niemals aus Lifecycle. / *Use current validated review evidence or NotAssessed; never derive review state from lifecycle.*
- `reasons[]`: stabiler Code, betroffene Kriterium-/Zielreferenz und DE/EN-Erklärung. Nicht vertrauenswürdige Rohwerte werden nicht ausgegeben. `nextAction` hat genau ein DE/EN-Paar. / *Stable code, affected criterion/target reference, and bilingual explanation; never echo untrusted raw values. Exactly one bilingual next action.*
- `failureClass`: `null` bei normaler erfolgreicher Prüfung, sonst `ProductFailure` bei ungültigem Artefakt oder `ProviderFailure` bei nachweislichem Laufzeit-/Dienstfehler. Ein korrektes `Blocked` wegen gemeinsamer Writes ist eine fachliche Einstufung mit `failureClass=null`. / *Null for an ordinary completed assessment; product failure for invalid artifacts; provider failure for proven runtime/service faults. Shared-write blocking is a domain result with null failure class.*

`deliveryMode` ist nur gelesener Kontext oder `NotAssessed`; `currentStartAuthority=NotGrantedByQuery` und historische Receipt-Herkunft bleiben eigene Felder. / *Delivery mode is read context or NotAssessed; current authority is NotGrantedByQuery, with receipt provenance in a separate field.*

Ein ungültiger Modus bleibt im sicheren Diagnostikpfad und wird nicht als gültige Einstufung ausgegeben. Eine nicht lesbare Datei bzw. ungültiges JSON ergibt nur eine Diagnose mit `Blocked`; kein künstliches vollständiges Kriterienobjekt. / *An invalid mode produces a safe diagnostic, not a valid classification. An unreadable file or invalid JSON yields a Blocked diagnostic; never fabricate complete criteria.*

## Übergänge und Nicht-Übergänge / Transitions and non-transitions

Lesen → Schema/Kriterien/Hashes prüfen → bestehende Graphprüfung → Ergebnis anzeigen. Bei Fehler: blockierte Diagnose mit einer sicheren nächsten Aktion. Keine Abfrage führt zu `Pending → Eligible`, `Eligible → Active` oder Receipt-Erzeugung. Diese Zustandsänderungen bleiben ausdrücklich autorisierten Schreiboperationen vorbehalten. / *Read → validate schema/criteria/hashes → existing graph check → display result. On failure, display a blocked diagnostic with one safe next action. Queries never change lifecycle or create receipts; those remain explicitly authorized write operations.*

## Modusregeln und stabile Reihenfolge / Mode rules and stable order

Die neun Kriterien bleiben in **jedem** Modus Pflicht. `blocked` ergibt immer `Blocked`. Für die vier anderen nichtparallelen Modi ergibt eine vollständige konsistente Fixture mit aktueller Authority `Eligible`; fehlende oder falsche Authority blockiert. Konsistente gemeinsame Writes oder Decisions blockieren ausschließlich den Parallelmodus. Widersprüche zwischen vorhandenen Flags und Kriterien bleiben in jedem Modus ungültig. Die Tabelle definiert nur den belegten Fixture-Wortschatz, kein allgemeines Schema für reale Projektentscheidungen. / *All modes require nine criteria. Mode blocked always yields Blocked. The four remaining nonparallel modes yield Eligible for complete consistent fixtures with current authority; absent or false authority blocks. Consistent shared writes or decisions block only parallel mode. Contradictory supplied flags remain invalid in every mode. The table defines the evidenced fixture vocabulary, not a general schema for real project decisions.*

Die bestehende Engine berechnet Blocker über eine Python-Menge; deren Aufzählungsreihenfolge ist nicht stabil. Der Adapter erhält ihre Bedeutung, sortiert aber jede Ziel-/Blockerliste nach `orderedTargets` und Kriteriengründe nach der kanonischen Neunerfolge. `preferredCandidate` filtert niemals `eligibleCandidates`. Tests verwenden mindestens zwei unvollständige Vorgänger und mehrere Prozessstarts mit unterschiedlichen `PYTHONHASHSEED`-Werten; JSON und Text müssen dieselbe Reihenfolge haben. / *The engine derives blockers from a Python set whose enumeration order is unstable. Preserve its meaning but order every target/blocker list by orderedTargets and criterion reasons by the canonical nine-key order. Preferred candidate never filters the candidate list. Test at least two incomplete predecessors across processes with different hash seeds; JSON and text must retain the same order.*
