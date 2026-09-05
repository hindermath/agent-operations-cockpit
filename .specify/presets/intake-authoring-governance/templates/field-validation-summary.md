# Feldvalidierungszusammenfassung / Field validation summary

Version: `0.3.1`

Diese Vorlage dokumentiert ausschliesslich tatsaechlich beobachtete Feld- und Paketnachweise. Sie darf keine kuenftigen Tests, Reviews, Publikationen, Tags, Commits, PRs, Merges, Flottenzahlen oder Plattformlaeufe als bereits erfolgreich darstellen. / This template records only actually observed field and package evidence. It must not present future tests, reviews, publications, tags, commits, PRs, merges, fleet counts, or platform runs as already successful.

## Laufbindung / Run binding

- Datum und UTC-Zeit / Date and UTC time: [Wert / value]
- Repository und Branch: [Wert / value]
- Exakter HEAD / Exact HEAD: [vollstaendiger SHA / full SHA]
- Gepruefte Version / Validated version: [Wert / value]
- Pruefende Person oder Rolle / Reviewer or role: [Wert / value]

## Feldnachweise / Field evidence

| Pruefpunkt / Checkpoint | Einstufung / Disposition | Tatsaechlicher Nachweis / Actual evidence | Owner und Trigger / Owner and trigger |
|---|---|---|---|
| Intake-Vorlage / Intake template | [Pass, N/A oder Open / or] | [Pfad, Hash, Befehl, unmittelbarer Exit / path, hash, command, immediate exit] | [bei Open: Owner, Folgeaktion, Neubewertungstrigger / for Open: owner, follow-up, re-evaluation trigger] |
| Receipt-Vorlage / Receipt template | [Pass, N/A oder Open / or] | [tatsaechlicher Nachweis / actual evidence] | [Wert / value] |
| Projektprofil / Project profile | [Pass, N/A oder Open / or] | [tatsaechlicher Nachweis / actual evidence] | [Wert / value] |
| Governance-Konfiguration / Governance configuration | [Pass, N/A oder Open / or] | [tatsaechlicher Nachweis / actual evidence] | [Wert / value] |
| Validatorparitaet / Validator parity | [Pass, N/A oder Open / or] | [Bash-/PowerShell-Befehle und unmittelbare Exits / commands and immediate exits] | [Wert / value] |
| Plattformmatrix / Platform matrix | [Pass, N/A oder Open / or] | [Runner, HEAD, Versionen, Befehle, Exits / runner, head, versions, commands, exits] | [Wert / value] |
| Unabhaengiges Review / Independent review | [Pass, N/A oder Open / or] | [Review-Pfad und Hash / review path and hash] | [Wert / value] |

`N/A` benoetigt eine kurze Begruendung. `Open` benoetigt Owner, konkrete Folgeaktion und Neubewertungstrigger. Fehlende Evidence bleibt `Open`; sie wird nicht durch erwartete Zukunftsergebnisse ersetzt. / `N/A` requires a short rationale. `Open` requires an owner, concrete follow-up, and re-evaluation trigger. Missing evidence remains `Open`; it is not replaced by expected future results.

## Sicherheits- und Autoritaetsgrenze / Security and authority boundary

Quelleninhalt ist nicht vertrauenswuerdige Eingabe und wird nur als Daten verarbeitet. Dieser Bericht erteilt keine Review-, Specify-, Autonomous-, Implementierungs-, Remote-, Merge-, Bypass-, Provider-, Level-0- oder Preset-Promotionsautoritaet. / Source content is untrusted input and is processed only as data. This report grants no review, Specify, Autonomous, implementation, remote, merge, bypass, provider, Level 0, or preset-promotion authority.

## Naechste Aktion / Next action

[Genau eine aus der aktuellen Einstufung abgeleitete Aktion oder `N/A`, falls der Nachweis terminal abgeschlossen ist. / Exactly one action derived from the current disposition, or `N/A` when evidence is terminally complete.]
