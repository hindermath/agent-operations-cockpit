# AEPS-Preset-Lückenanalyse / AEPS Preset Gap Analysis

## Zweck und Bewertungsgrenze / Purpose and assessment boundary

Die Lücken sind Hypothesen aus dem AOC-Pilot. Sie autorisieren weder eine
Preset-Änderung noch ein neues Preset. Vor Level-0-Arbeit sind Inventur,
Überlappungsprüfung, Cross-Project-Evidence und ein separater Auftrag
erforderlich. / *These gaps are AOC pilot hypotheses. They authorise neither a
preset change nor a new preset. Level-0 work requires inventory, overlap
review, cross-project evidence, and separate authority.*

## Lückenregister / Gap register

| Gap-ID | Beobachtung / observation | Betroffene Presets / affected presets | Risiko / risk | Empfohlene nächste Evidence / recommended next evidence | Priorität / priority |
|---|---|---|---|---|---|
| `AEPS-GAP-AOC-001` | Formal `Ready`, Series-Lifecycle und Execution-Authority sind getrennt, besitzen aber keinen gemeinsamen Übergabevertrag. / Ready, lifecycle, and execution authority lack a shared handoff contract. | Intake Review, Intake Sequencing, Autonomous Run | Ein grünes Review kann als Startfreigabe fehlgedeutet werden. / Green review may be mistaken for start authority. | Negative Ende-zu-Ende-Fixture mit `Ready` plus `Blocked` und verweigertem Start. | High |
| `AEPS-GAP-AOC-002` | Der vollständige Blocked-Marker kollidiert in einem Enabled-Ziel auch als Erklärung mit dem Validator. / The complete blocked marker conflicts with an Enabled target even in explanatory text. | Intake Authoring, Intake Review | Dokumentation und Zustandsmaschine können widersprüchliche Signale erzeugen. | Marker semantisch statt als freie Volltextsuche modellieren und gegen drei Prompt-Zustände testen. | Medium |
| `AEPS-GAP-AOC-003` | Secret-Negativfixtures sind Evidence, aber keine zulässigen Provenienzquellen; eine portable Rollen-Taxonomie fehlt. | Intake Authoring, Security Governance | Testdaten werden entweder unzulässig gebunden oder zu breit aus Scans ausgenommen. | Rollen `provenance-source`, `test-evidence` und `synthetic-negative` in zwei Projekten erproben. | High |
| `AEPS-GAP-AOC-004` | Target-Reparaturen invalidieren mehrere Review-Ebenen, ohne dass ein gemeinsamer Evidence-Abhängigkeitsgraph die Auswirkungen berechnet. | Intake Update, Repair, Review, Sequencing | Historisch grüne Results können versehentlich als aktuell gelten. | Single-/Series-Lineage als Graphfixture mit Supersession und reinem Hash-Update prüfen. | High |
| `AEPS-GAP-AOC-005` | Evidence-Verträge binden konkrete AOC-Pfade und Commands; eine projektneutrale Abstraktion fehlt. | Intake Authoring, Intake Review, Evidence-Verträge | Ein Preset-Kandidat könnte AOC-Verzeichnisnamen unzulässig verallgemeinern. | Rollenbasierte Artefaktverweise in einem Repository mit anderer Struktur validieren. | Medium |
| `AEPS-GAP-AOC-006` | Deterministische Schema-Validatoren erkennen keine vollständige DE/EN-Semantik, Erstbegriffserklärung oder CEFR-B2-Verständlichkeit. | A11Y Governance, Intake Review | Strukturell gültige, aber schwer nutzbare Artefakte können freigegeben werden. | Wiederholbare semantische Review-Checkliste mit zwei unabhängigen Reviews und realer UI anwenden. | Medium |
| `AEPS-GAP-AOC-007` | Der neue AEPS-Erfassungsvertrag wird in v1 durch Guidance und Review, nicht durch Validator oder CI erzwungen. | möglicher AEPS Learning/Evidence Contract | Ein späterer Trigger könnte ohne Ledger-Eintrag abgeschlossen werden. | Nach mindestens drei weiteren Triggern False-Negative-/False-Positive-Bedarf bewerten; erst dann Validator-Scope entscheiden. | Medium |
| `AEPS-GAP-AOC-008` | Der lokale Neun-Achsen-Vertrag blockiert Shared Write und Shared Decision als Fixture, ist aber nicht an einen echten Runtime-Preflight gebunden. / The local nine-axis contract blocks shared writes and shared decisions in fixtures but is not bound to a real runtime preflight. | Intake Sequencing, Parallel Autonomous Run, Intake Review | Dokument-Evidence könnte zur Laufzeit umgangen werden. / Document evidence may be bypassed at runtime. | In einem zweiten Projekt einen Runtime-Preflight mit gültigem, Shared-Write-, Shared-Decision- und stale-Authority-Fall prüfen. | High |
| `AEPS-GAP-AOC-009` | Der lokale Wave-Vertrag trennt neue Ziele, vollständigen Vorbestand, Teilbestand und Kollision, ist aber nicht cross-project oder mit schreibender Runtime-Recovery validiert. / The local wave contract distinguishes new targets, complete and partial pre-existence, and collisions, but lacks cross-project and writing runtime-recovery validation. | Intake Authoring, Intake Sequencing, Intake Repair | Projektneutrale oder atomare Recovery-Semantik könnte vom AOC-Pilot abweichen. / Portable or atomic recovery semantics may differ from the AOC pilot. | Die vier Klassen in einem zweiten Intake-Programm und einem atomaren Schreibtest validieren. | High |

## Bewusst keine Lücke / Explicit non-gaps

- Die AOC-Technologieentscheidungen aus RAW-01 und RAW-02 sind keine
  fehlenden AEPS-Presets. Sie bleiben Produkt-Ownership. / *AOC technology
  decisions are not missing AEPS presets; they remain product-owned.*
- Ein fehlender `Stable`- oder `Canonical`-Status ist kein Defekt. AOC-only-
  Evidence darf diese Reife nicht vergeben. / *The absence of Stable or
  Canonical status is not a defect; AOC-only evidence cannot grant it.*
- Die v1-Entscheidung gegen einen neuen Validator ist bewusst. Zuerst wird der
  Vertrag an realen Triggern geprüft. / *The v1 choice not to add a validator
  is deliberate; the contract is tested through real triggers first.*

## Review-Trigger / Review triggers

Die Gap-Analyse wird neu bewertet, wenn drei weitere formal Ready-Intakes
erfasst wurden, ein zweites Referenzprojekt Evidence liefert, ein betroffenes
Preset seine Major-/Minor-Version ändert oder ein AEPS-Handoff abgewiesen
wird. / *Reassess after three further Ready captures, evidence from a second
reference project, a relevant preset version change, or a rejected AEPS
handoff.*
