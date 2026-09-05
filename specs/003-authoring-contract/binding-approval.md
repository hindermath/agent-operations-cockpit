# Begrenzte Bindungsreparatur / Bounded binding repair

## Aktuelle Freigabe / Current approval

Thorsten hat im bestehenden Thread ausdrücklich „Ja, genehmigt!“ zur
[begrenzten Bindungsreparatur](blocking-scope-decision.md) bestätigt.
Diese Freigabe gilt für den bestehenden Lauf
`044b77ae-85fd-46ee-97f4-61ce7a2c9c66` auf Basis
`ada16a88833aae246f2db396a565bc941109617b`.
Erfasst am 2026-09-05T13:58:06.012Z. / *Thorsten explicitly approved the linked bounded
repair in this thread for the stated existing run and base; this is the
recording timestamp.*

## Genehmigter Umfang / Approved scope

- Nur die Versionsreferenz in META-LH-03 von `0.3.0` auf die bereits
  installierte `0.3.1` ändern. / *Only align META-LH-03's version reference
  with the already installed 0.3.1.*
- Receipts für META-LH-02, META-LH-03, META-LH-05 und RAW-03 erneuern;
  Vorgänger bytegleich archivieren, Intake-Identitäten erhalten und neue
  Receipt-/Operations-IDs verwenden. META-LH-03 darf nach genehmigten eigenen
  Template-Änderungen erneut gebunden werden. / *Renew these four receipts,
  preserve byte-identical predecessors and stable intake identities, and mint
  new receipt/operation IDs; rebind META-LH-03 after its authorised template edits.*
- Jedes der vier Lastenhefte vollständig neu einzeln reviewen. Alte Ergebnisse
  bleiben als Vorgänger erhalten; Ready wird nicht vorausgesetzt.
  / *Fully re-review each of the four intakes; retain predecessor reviews and
  do not assume a Ready result.*
- Eine neue hashgebundene Auflösung der aktuellen Evidence ergänzen.
  Terminaler META-LH-02-Zustand, Lifecycle-Snapshot, abgeschlossene
  Seriennachweise und historische Evidence bleiben unverändert.
  / *Add a hash-bound current-evidence resolution while preserving the terminal
  META-LH-02 state, lifecycle snapshot, completed series evidence and history.*
- Danach nur denselben META-LH-03-Lauf nach aktuellem Resume-Preflight fortsetzen.
  Der separat beauftragte DeliveryMode bleibt MergeAndSync.
  / *Then resume only this META-LH-03 run after current preflight; its separately
  authorised delivery mode remains MergeAndSync.*

## Grenzen / Boundaries

Keine neuen fachlichen Entscheidungen, keine Änderung von Zweck, Scope,
Non-Goals, Abhängigkeiten, Reihenfolge oder Lifecycle-Status. Keine
Preset-Installation, Versionsänderung, Level-0- oder Promotion-Aktion,
kein neuer Autonomous-Lauf und kein Admin-Bypass. Diese Datei dokumentiert
die Freigabe; sie erteilt selbst keine Rechte. / *No new domain decisions,
scope, non-goal, dependency, order or lifecycle changes; no preset installation
or version change, level-0 action, promotion, new autonomous run or admin
bypass. This file records authority; it does not grant authority itself.*

Die einzige Dokumentationsentscheidung bleibt im
[Laufnachweis](autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact).
/ *The sole documentation-impact decision remains in the linked run evidence.*
