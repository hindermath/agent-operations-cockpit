# Statistik-Rollout v0.1.0 / Statistics rollout v0.1.0

## Auftrag und Umfang / Authority and scope

Vierter Kandidat von [Rollout #302](https://github.com/hindermath/home-baseline/issues/302).
Ausgangscommit: `e463963e048a4b0508dcba1a5c31fceed6b0f7f2`.
Installation und technische Pruefung sind beauftragt. Fachliche Abnahme und
Lieferfreigabe durch @hindermath bleiben vor Merge erforderlich; kein
uebertragener Admin-Bypass. Kein Produktlauf, kein Release, keine Promotion,
keine Intake-/Serienaenderung und kein Home-Sync. Die globale Review-Sperre
der AOC-Programmreihe bleibt unveraendert.

Fourth rollout target. Installation and technical validation are authorized;
human acceptance and delivery permission remain separate. No inherited bypass,
product run, release, promotion, intake mutation or home synchronization.
The programme-wide review gate is preserved.

## Paket und Profil / Package and profile

[Installationsbeleg](project-statistics-installation-v010.json): 26 Paketdateien
bytegleich mit dem v0.1.0-Tag-ZIP; bestehende 13 Registry-Eintraege und
vorherige Integrationsdateien nach Installation unveraendert.
ZIP SHA-256 `d8ad7d5eef920f50b629121b64ba8123c22ec4f6dadd14da5cd826d1c50f420a`;
Paketcommit `7e824ca8de11212aefdc5b05d7d05637f5343dab`.
Statistik Prioritaet 90, Assurance v0.1.3 bei 15, Security bei 10.
Die zentrale 14er-Matrix ist im Receipt hashgebunden. Globale Defaults bleiben
erhalten; operative Profilzuordnung erst nach Lieferung. Cache bleibt ignoriert.

The receipt binds package bytes and the central matrix. Existing preset entries
are preserved; no reinstall or global-default change. Update the operational
profile only after delivery. Exclude the local cache from Git.

## Messung und Nachweise / Measurement and evidence

[Kontext und Bedienung](../project-statistics/README.md): UTC, 52 Wochen,
keine Referenzmodelle oder manuell kopierten Phasen. Profil 2 bleibt kanonisch,
Europe/Berlin mit 80/125-Referenzen und dem bisherigen Phasenslot.
Beide Methoden schliessen den neuen Kontext aus. Inhalte zuerst committen;
Init/Update nur nach Vorschau und mit sauberem Arbeitsbaum. Beide Messungen
verwenden dieselbe Inhaltsrevision; Outputs separat committen und lesend pruefen.

The separate UTC context does not replace canonical Profile 2. Preserve its
references and authored phase. Preview before writing, commit content first,
and render both methods from the same revision without dirty-tree overrides.

`scripts/prove-project-statistics-context.ps1` mit
[Manpage](../man/prove-project-statistics-context.1.md) prueft Paketbindung,
exakte Matrix, list/info/resolve/check, Fixtures, Lifecycle, Idempotenz,
LF/CRLF/BOM und unveraenderte Quellhashes. Schreibtests nur in lokalen
Wegwerfkopien; keine vollstaendige I/O-Ueberwachung behauptet.
Native CI: Linux/Windows am exakten Head, macOS lokal; Nachweise im PR.
Bestehende Public-Readiness-, Maintenance-, PowerShell-, Homogeneity- und
Linked-Intake-Gates bleiben aktiv. AOC hat noch kein Produkt-Scaffold:
Produkt-Restore/Build/Test ist N/A, kein behaupteter .NET-Produktnachweis.
Governance- und Maintenancetests bleiben echte Pflichtpruefungen.

The reusable proof covers installation, commands, fixtures, composition,
encodings, idempotency and read-only source hashes. Writing tests use scratch
clones; no complete I/O trace is claimed. Retain existing CI. Product .NET
checks are not applicable without a product scaffold; governance tests remain
mandatory. Results and exact head are recorded in the PR, not predicted here.

## Dokumentation und Sicherheit / Documentation and security

Documentation Impact: `UpdateRequired`; Owner Thorsten Hindermann.
Zielgruppen: Lernende ab Jahr 1, Maintainer und Reviewer. Leserpfad:
README -> Kontextanleitung -> Bericht/Snapshot -> Installationsbeleg.
ActiveSemantic, DE-first/EN-second, CEFR B2, text-first; projektlokal, kein
Home-Sync. Quelle: Preset-Repository und lokale Konfiguration/Git-Historie.
Fuenf Agentenflaechen synchron; beide Constitutions und Registry-Zeile geprueft:
Runtime, 80/125-Basis und Produktgrenzen unveraendert. Neues Pruefskript im
lokalen Skriptkatalog unter Statistik; Referenz daraus generieren.
Re-Evaluation bei Paket-, Quellen-, Methodik-, Profil- oder Bedienungswechsel.

Apply the repository documentation contract with bilingual accessible reader
paths and local distribution. Preserve runtime and reference baselines; bind
the proof command to the script catalog. Reevaluate on source or contract drift.

Security: unveraendertes verifiziertes Paket, SHA-256, gepinnte CI-Actions,
minimale Leserechte und keine Secrets. Kein neues Netzwerk-/Auth-Produkt,
keine eigene Kryptografie oder Runtime-Abhaengigkeit. ASVS und AI-Runtime-SBOM
N/A fuer lokale Entwicklungsstatistik; vorhandene Produkt-Sicherheitsbewertungen
und menschliche Entscheidungen unveraendert. Kein C5-, Konformitaets-,
Zertifizierungs-, Qualitaets- oder KI-Produktivitaetsclaim. Das
[AEPS-Receipt](../aeps/receipts/2026-09-19-statistics-rollout.md) trennt
technische Wiederverwendung von neuer Evidence/Promotion.

Use verified package bytes, pinned actions and least privilege. No new product
trust boundary or runtime dependency. Existing assurance and human decisions
remain unchanged. Statistics provide no security, compliance, certification,
quality or measured AI-productivity claim. AEPS capture does not promote a preset.
