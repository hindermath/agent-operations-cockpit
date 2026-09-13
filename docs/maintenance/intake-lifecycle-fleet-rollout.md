# Intake-Lifecycle-Flottenrollout / Intake lifecycle fleet rollout

Datum: 2026-09-13. Owner: Repository Maintainer (Thorsten Hindermann).

DE: Die vorhandenen Intake-Presets werden auf Authoring 0.3.2, Review 0.2.2
und Sequencing 0.2.4 aktualisiert. Die optionalen Profilbindungen verwenden
dieselben Releases. Die Standard-Achtermatrix und andere Presets bleiben erhalten.
Die Installation fuehrt keine Intakes aus und verschiebt keine fachlichen Dateien.
Completed-Ziele gehoeren ins konfigurierte Archiv; ausfuehrbare Ziele in die
aktive Collection. Physischer Aktivbestand und aktive Serienziele werden getrennt
gezaehlt. Historische Receipts brauchen eine eindeutige Archiv-/Hashbindung.

EN: Existing intake presets are updated to Authoring 0.3.2, Review 0.2.2 and
Sequencing 0.2.4. Optional profiles bind the same releases; the standard eight
and other presets remain unchanged. Installation neither executes intakes nor
moves requirements. Completed members belong in the configured archive and
executable members in the active collection. Physical active inventory and active
series membership are separate counts. Historical receipts require unique
archive/hash evidence.

## Evidence und Dokumentationsauswirkung / Evidence and documentation impact

[intake-lifecycle-fleet-rollout.json](intake-lifecycle-fleet-rollout.json) erfasst
Paketbasis, lokale Erweiterungen und Pruefergebnisse. Technische Gates, Review-
Befunde und der exakte PR-Head werden vor Merge geprueft. Der ausdrueckliche
Auftrag umfasst MergeAndSync mit Admin-Bypass nach technischen Gates; er
behauptet keine unabhaengige menschliche Freigabe und keine Produktkonformitaet.

Entscheidung: UpdateRequired. Zielgruppen: Maintainer und Agenten; Leserpfad:
aktuelle Preset-/Agent-Guidance, dieses Dokument, JSON, PR-Gates. Kanonische
Quellen: veroeffentlichte Preset-Tags und bestehende optionale Profile. DE/EN
stehen gemeinsam hier; Darstellung ist textorientiert und ohne Farbabhaengigkeit.
Distribution: repository-lokale Presets und Evidence, verwaltete Profilkopien.
Die Level-0-Profilkonfiguration wird separat ueber den geprueften Home-Runtime-
Sync verteilt; Preset-Verzeichnisse werden nicht nach Home kopiert. Statistik
folgt der vorhandenen Repository-Konfiguration. Re-Evaluation bei Versions-,
Profil-, Lifecycle- oder lokaler Erweiterungsdrift.

The linked JSON records released package provenance, local extensions and
validation results. Technical gates, review findings and the exact PR head are
checked before the authorized MergeAndSync/admin-bypass delivery. This does not
claim independent human approval or product conformity. Documentation impact is
UpdateRequired, owned by the maintainer, with colocated German/English text.
Reassess after version, profile, lifecycle or local-extension changes.

## Lokale Cockpit-Erweiterungen / Local Cockpit extensions

Die Drei-Wege-Zusammenfuehrung erhaelt die eindeutige Lifecycle-Aufloesung
logischer Pfade, Profil-/Hashbindung, Duplicate-Key-Abweisung und die bestehende
aktuelle Evidence-Bindung. Die neue Collection-Pruefung verwendet den aufgeloesten
physischen Pfad. Zusaetzliche Cross-Shell-Fixtures pruefen einen abgeschlossenen
logischen Archivverweis, doppelte Lifecycle-Eintraege, Hashabweichung und fehlenden
Archivnachfolger. Das Authoring-Profil bleibt ausdruecklich de-DE; die allgemeinen
englischen Fixtures bestehen weiterhin in Review und Sequencing. Der bestehende
Authoring-Contract besteht ueber beide Shell-Wrapper. Die fachliche Konfiguration
meldet separat einen noch aktiv gespeicherten Completed-Intake.

The three-way merge preserves logical lifecycle resolution, profile/hash binding,
duplicate-key rejection and the existing current-evidence binding. Collection
checks use the resolved physical path. Added Bash/PowerShell fixtures cover an
archived logical target, ambiguous lifecycle records, hash drift and a missing
archive successor. The local authoring profile remains de-DE; generic English
fixtures continue to pass in review and sequencing. Both authoring-contract
wrappers pass. Project configuration separately reports a Completed intake still
stored in the active collection.

Die lokal erweiterte Receipt-Vorlage bleibt bytegleich als hashgebundene Quelle
von META-LH-03 erhalten, einschliesslich ihres historischen generator.version
0.3.1. Das ist eine explizite lokale Ausnahme; die installierte Preset-Version
ist 0.3.2. Neue Receipts muessen die tatsaechliche Generator-Version aus preset.yml
verwenden. Die historische Vorlage ersetzt keinen Nachweis der aktuellen Version.
Der laufende META-LH-03-Receipt wird ueber beide Wrapper erneut geprueft.

The locally extended receipt template is preserved byte-for-byte as a hash-bound
META-LH-03 source, including historical generator.version 0.3.1. This explicit
local exception does not change installed preset version 0.3.2. New receipts must
use the actual generator version from preset.yml. The historical template is not
proof of the current version. Both wrappers revalidate the META-LH-03 receipt.
