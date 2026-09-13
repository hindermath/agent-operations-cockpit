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

## Korrigierter Patchstand / Corrected patch releases

Die Flottenreviews deckten physische Collection-Aliase und Receipt-Pfadfluchten
auf. Die zentral korrigierten Releases sind Authoring 0.3.4, Review 0.2.3 und
Sequencing 0.2.6. Negative Tests reproduzierten die Befunde vor der Korrektur;
anschliessend bestehen die nativen Release-Suiten auf macOS, Linux und Windows.
Die aktuellen Profile, Source-Locks und vorhandenen Bootstrap-/Agent-Vorlagen
verwenden diese Versionen. Die mitgelieferten verschachtelten Workflows sind
Quellmetadaten der Presets und aktivieren keine Verbraucher-Jobs; die technischen
PR-Gates stammen aus den Root-Workflows des jeweiligen Verbraucher-Repositories.

Fleet review found physical collection aliases and receipt path escapes. The
centrally corrected releases are Authoring 0.3.4, Review 0.2.3 and Sequencing 0.2.6.
Shipped JSON templates are parsed and their generator versions checked in native CI. Negative tests reproduced the findings before correction; native release suites
then pass on macOS, Linux and Windows. Existing profiles, source locks and
bootstrap/agent templates bind these versions. Packaged nested workflows are
preset-source metadata, not consumer jobs; consumer PR gates use root workflows.

Documentation Impact remains UpdateRequired. Re-evaluation includes portability,
physical path aliases, source/hash bindings and local overlays. Project lifecycle
inventory findings remain separate from successful package/regression checks.

Lokale Quellbindung / Local source binding: Auch templates/field-validation-summary.md
bleibt wegen eines aktuellen historischen Authoring-Receipts byteidentisch auf
seiner Quellversion 0.3.1. Zusammen mit der Receipt-JSON-Vorlage ist dies eine
absichtliche lokale Ausnahme; aktuelle Release-Identitaet ist preset.yml (0.3.4).
Both the field-validation summary and receipt JSON template remain exact historical
receipt-bound sources. Their 0.3.1 source labels are intentional local exceptions;
new evidence records the installed release from preset.yml (0.3.4).

Checkpoint-Vertrag / Checkpoint contract: Der alte validate_current_evidence_binding.py
ist selbst als historischer Pfad im 48-Dateien-Reparaturcheckpoint gebunden und
prueft dessen 0.3.0-auf-0.3.1-Transaktion. Er wird nicht zur allgemeinen
Paketversionspruefung umgeschrieben. Der aktuelle CI-Einstieg
validate-authoring-contract.sh/.ps1 prueft den Checkpoint und die erneuerte
META-LH-03-Transaktion erfolgreich; die heutige 0.3.4-Installation hat getrennte
Registry-, Paket- und Receipt-Evidence. Die historische Freigabe erteilt keine
heutige Rollout-Autoritaet; diese stammt aus dem aktuellen Benutzerauftrag.
The old bridge validator is checkpoint-bound historical evidence. Current CI
uses validate-authoring-contract in both shells, while release/package checks
prove the current authorized installation. No historical approval is expanded.
