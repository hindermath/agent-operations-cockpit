# Architektur verlinkter Intake-Evidence / Linked Intake Evidence Architecture

## Kontext und Datenfluss / Context and data flow

```text
Kanonisches AOC-Phase-2-Manifest
  + vorhandene Intake-Dateien oder eindeutig belegte featuregestempelte Ziele
  + vorhandene Feature-Spezifikationen und Abschlusszustände
  -> UTF-8-, Schema-, Pfad-, Typ-, Kanten- und Proof-Validierung
  -> typisierte Fünf-Felder-Projektion
  -> zwei Markdown-Kandidaten
  -> Check oder atomare lokale Publication mit Recheck/Rollback
```

Die Manifestpfade bleiben die logischen Identitäten für Reihenfolge und
Kanten. Nur Dateizugriff und Linkziel verwenden bei META-LH-01/02/03 den in
T079 eindeutig belegten aktuellen Pfad. Dadurch bleiben Series- und
Lifecycle-Semantik unverändert, während Links auf tatsächlich vorhandene
vollständige Dateinamen zeigen.

*Manifest paths remain the logical identities for ordering and edges. Only
file access and link targets use the uniquely proven current path for
META-LH-01/02/03. This preserves series and lifecycle semantics while links
target complete filenames that actually exist.*

## Qualitätsziele / Quality goals

| Ziel | Szenario | Messbares Ergebnis |
|---|---|---|
| Integrität | Pfad, Kante, Status oder Proof ist ungültig. | Stabiler `LIE001`–`LIE012`-Blocker; kein Write. |
| Eindeutigkeit | Kein oder mehr als ein gestempelter Kandidat ist vorhanden. | Fail-closed; keine Dateinamenheuristik ohne Abschlussnachweis. |
| Determinismus | Unveränderte Eingaben werden erneut verarbeitet. | Beide Ansichten bleiben bytegleich; `writes=0`. |
| Wiederherstellbarkeit | Publication scheitert nach dem ersten Replace. | Beide Altstände werden wiederhergestellt; keine Tempdatei bleibt. |
| Plattformparität | Bash und PowerShell erhalten dieselben Fixtures. | Gleiche fünf Felder, Fehlerklassen, Links, Kanten und Proofs. |
| Produktisolation | Governance-Renderer wird geändert. | Kein AOC-Produkt-, API-, Runtime- oder Dependency-Diff. |

## Architekturentscheidung und Kommentare

Die Erweiterung bleibt in den vorhandenen Bash-/PowerShell-Bibliotheken und
ihren öffentlichen Prepare-Wrappern. Es entsteht kein neuer Produktbaustein,
keine externe Schnittstelle und keine Deploymentänderung. ADR/S-ADR und
Produktbuild sind daher `N/A / Not Assessed`; neu zu bewerten bei neuer
Komponente, Produktdatei, Runtime, externem Interface oder Trust Boundary.

Didaktische Kommentare erklären nur nicht offensichtliche Grenzen: warum
unsichere Werte nicht reflektiert werden, warum gestempelte Pfade einen
Feature-Abschlussnachweis benötigen und warum Publication vor dem Replace den
gesamten Input erneut bindet. Offensichtliche Ablaufschritte bleiben
unkommentiert.

*The change stays within the existing paired libraries and public prepare
wrappers. Comments explain proof and safety boundaries rather than obvious
operations. No new product component, external interface, or deployment is
introduced.*

Owner: AOC Repository Owner. Reviewer: Feature-032 Architecture Reviewer.
Re-Evaluation bei Quellen-, Komponenten-, Schnittstellen-, Deployment-,
Trust-Boundary-, Lifecycle- oder Transaktionsänderung.
