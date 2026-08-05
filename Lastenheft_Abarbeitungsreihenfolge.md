# Lastenheft-Abarbeitungsreihenfolge / Requirements Processing Order

Diese Datei haelt die sichtbare Abarbeitungsreihenfolge der vorhandenen Lastenhefte fest. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf.

*This file records the visible processing order of existing requirements documents. It prepares later Spec Kit runs and does not start a run by itself.*

## AOC-Programmreihe / AOC programme series

Für das eigenständige AOC-Lastenheftprogramm ist die kanonische,
SHA-gebundene Reihenfolge unter
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md)
festgelegt. Der Einstieg und Status aller Meta- und Fachreihen steht in
[`Pflichtenheft.md`](Pflichtenheft.md). Die unten automatisch ermittelte
Root-Tabelle betrifft ausschließlich ältere Root-Intakes und besitzt keine
Authority über die AOC-Series.

*The canonical, hash-bound AOC programme order is defined in
[`requirements/intakes/series/order.md`](requirements/intakes/series/order.md).
[`Pflichtenheft.md`](Pflichtenheft.md) is the programme index. The automatically
generated root table below covers legacy root intakes only and has no authority
over the AOC series.*

Für diese AOC-Programmreihe gilt eine globale Review-Sperre: Alle 14 Meta- und
Fachlastenhefte müssen aktuelle, formal validierte `Ready`-Single-Reviews
besitzen, bevor ein `speckit specify`-, Autonomous-, Parallel-Autonomous- oder
Implementierungslauf starten darf. Danach bleibt `META-LH-01` das erste Ziel und
benötigt einen neuen ausdrücklichen Startauftrag. Drift schließt die Sperre
erneut. Die zwei älteren Root-Intakes in der generierten Tabelle sind nicht Teil
dieser 14er-Gesamtmenge.

*The AOC programme has a global review gate: all 14 META and RAW intakes require
current formally validated Ready Single reviews before downstream Spec Kit work
may start. `META-LH-01` remains the first target and needs a new explicit start
instruction. Drift closes the gate again. The two generated legacy root intakes
are outside this fourteen-intake set.*

<!-- secure-development-hardening-order:start -->
## Automatisch ermittelte Lastenheft-Reihenfolge / Automatically Detected Requirements Order

Diese Tabelle wird aus `Lastenheft*.md` im Repository-Root erzeugt. Sie ist eine Vorbereitung fuer spaetere Spec-Kit-Laeufe und startet selbst keinen Lauf. Manuelle Projektentscheidungen ausserhalb dieses markierten Abschnitts bleiben erhalten.

*This table is generated from `Lastenheft*.md` in the repository root. It prepares later Spec Kit runs and does not start a run. Manual project decisions outside this marked section remain preserved.*

| Rang | Lastenheft | Gruppe | Status |
|---:|---|---|---|
| 1 | `Lastenheft_RL-SE-Checklist-Selbstpruefung.md` | RL-SE-/Checklist-Selbstpruefung | aktiv / active |
| 2 | `Lastenheft_Secure-Development-Hardening.md` | Secure-Development-Hardening | aktiv / active |
<!-- secure-development-hardening-order:end -->
