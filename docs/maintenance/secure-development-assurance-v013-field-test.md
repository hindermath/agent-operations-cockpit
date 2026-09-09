# AOC-Feldtest: Assurance v0.1.3 / AOC field test

Stand / Date: 2026-09-09. Technische Empfehlung / Technical recommendation:
`ReleaseAccepted` für die unveränderte Preset-Funktion im begrenzten
Governance-Scope / for unchanged preset behavior in the scoped governance test.
Verbindlicher Remote-Lieferstatus: Tracker #43 und zugeordneter PR /
authoritative remote delivery status: tracker #43 and its linked PR.

## Umfang und Paketbindung / Scope and package binding

AOC erhält das optionale 13-Preset-Profil: Secure Development Assurance
Governance v0.1.3 auf Priorität 15, Security Governance v0.6.2 unverändert auf
Priorität 10. Keine anderen Preset-Versionen werden geändert.
@hindermath ist Test-Owner und benannter menschlicher technischer Reviewer;
Codex führt Tests und technische Befundprüfung aus. Keine menschliche
Sichtung wird durch automatisierte Prüfergebnisse behauptet.

*The optional profile adds Assurance at priority 15 without changing the other
twelve preset versions. @hindermath owns the test and designated human technical
review; Codex executes checks without claiming human sign-off.*

- [Release v0.1.3](https://github.com/hindermath/spec-kit-preset-secure-development-assurance-governance/releases/tag/v0.1.3), Pre-Release.
- Tag: `0d03aa9ebe8f74a26e331815bca5609fb48d7a14`.
- Tag-ZIP SHA-256: `9023b442b4d82e25bee5a7fe9b73efb7f591a4f265f54061ae6e4a56b9b5c75f`.
- Plattform / Platform: macOS Darwin arm64; Bash 3.2.57; PowerShell 7.6.5; Spec Kit 0.12.8.
- Base-HEAD: `17df5332f4d4b6923b1596e11ebfb56d2629a5cc`.
- [AOC-Tracker #43](https://github.com/hindermath/agent-operations-cockpit/issues/43).
- [Zentrale Erweiterung #276](https://github.com/hindermath/home-baseline/issues/276).

Die Installation ist bytegleich zum vorher hashgeprüften Archiv. Die zentrale
13-Preset-Matrix ist die Installationsquelle, nicht eine neue lokale
Preset-Variante.

*Installation matches the hash-verified archive; the central thirteen-preset
matrix defines installation, with no local preset fork.*

## Kontext und Prüfungen / Context and checks

Der [eigene training-Kontext](../security/secure-development/2026-09-09-aoc-assurance-v013/evidence-matrix.md)
prüft Dokumentintegrität, Installation, Autoritätsgrenzen und Gate-Semantik.
30 Dokumentbindungen sind keine Abnahme aller 157 Sicherheitsmaßnahmen.
AOC besitzt keinen freigegebenen Produkt-Scaffold; Produkt-Restore, Release-Build,
Tests und TUI-Smoke sind deshalb nicht anwendbar. Vorhandene Wartungswerkzeuge
werden durch ihre eigenen CI-Prüfungen abgedeckt.

*This context tests document integrity and governance semantics, not full
implementation of 157 security controls. No approved product scaffold exists;
product restore/build/tests/TUI smoke are not applicable. Maintenance tooling
keeps its separate CI gates.*

| Prüfung / Check | Ergebnis / Result | Exit |
|---|---|---|
| 13-Preset-CheckOnly Bash/PowerShell | Exakte Matrix / exact matrix | 0 / 0 |
| preset list/info/resolve; specify check | v0.1.3 aufgelöst / resolved | jeweils / each 0 |
| Status und vier Reviews in beiden Shells | Ready, gleiche Ausgabe / matching output | 10 x 0 |
| Rohe Kontext-Hashes / raw context hashes | Vorher = nachher / unchanged | 0 |
| Acht generierte Oberflächen aus Tag-ZIP | Kanonische, ausführbare Befehle / executable canonical commands | Suite 0; negative 2 |
| Installierte Negativ-/Paritätssuite | Alle Assertions bestanden / all assertions passed | 0 |
| Isolierte Disable/Enable/Remove/12-Profil/Wiederinstallation | Matrix stimmt; CLI-Grenze unten / exact matrix; limit below | jeweils / each 0 |
| Authoring-Contract-Tests | 12 bestanden / passed | 0 |
| Gate-Evidence-Invariantentests | 6 bestanden / passed | 0 |
| Authoring-Vertrag und global-ready | Gültige 14-Intake-Kette / valid chain | 0 / 0 |
| Secure-Development-Sammelband | Aktuell, unverändert / current and unchanged | 0 |
| Secret-Scan | Keine hohen Findings / no high findings | 0 |

Die Negativsuite umfasst alle Runbook-Fälle: Manifest-/Dokument-/Sammelbanddrift,
fehlende/doppelte Checklisten, Versionsfehler, offene Pflichtpunkte bei Ready,
N/A ohne Grund, Reviewablauf, unvollständige Risiken, fehlende Security Governance,
verbotene Zertifizierungsbehauptungen, fehlende Runbooks/Image-Felder sowie
v0.1.3-Kontext-/Mode-/Risikotyp-Grenzen. LF/CRLF/BOM und Rohhash-Schutz werden
separat geprüft. Ein erwarteter Negativfall liefert 2, die erfolgreiche Suite 0.

*The suite covers every runbook failure category plus v0.1.3 context/mode/risk
type boundaries, line-ending parity and raw-byte protection. Negative fixtures
must exit 2; the successful runner exits 0. Fixtures are not product evidence.*

Nachweise / Records:
[Kontext und Rohhashes](assurance-v013-context-verification.json),
[isolierte Komposition](assurance-v013-composition-verification.json).
Native Linux-/Windows-Prüfungen werden nur mit konkreter PR-CI-Evidence
behauptet; lokale PowerShell-Ausführung ist kein nativer Windows-Nachweis.

*Records bind actual commands, exits and context hashes. Native platform
evidence requires the actual PR job, not just another shell on macOS.*

## Findings, Lernzweck und Grenzen / Findings, education and boundaries

- Spec Kit 0.12.8 lässt beim Entfernen in der temporären Kopie zwei Claude-Skills
  zurück. Daher kein vollständiger Deinstallationsnachweis. Wiederinstallation
  stellt die Oberflächen wieder her. Kein CLI-Patch, keine echte Deinstallation.
- Die erste CI-Prüfung erkannte eine veraltete generierte Skriptübersicht nach
  Installation. Der bestehende Renderer aktualisiert ausschließlich die
  eingebettete Skriptreferenz; der Katalog bleibt unverändert.
- Der globale 14-Intake-Vertrag, Lastenhefte, Receipts und Quellbaseline bleiben
  unverändert. Ein bestandener global-ready-Preflight startet keinen Produktlauf.
- AOC, home-baseline, TinyCalc, TinyPl0, InventarWorkerService,
  absdd-image-sandbox und TuiVision sind nichtproduktive, nichtkommerzielle
  Ausbildungs-/Referenzprojekte für die vier IHK-IT-Ausbildungsberufe, mit allen
  vier FI-Fachrichtungen. Sicherheit ab Lehrjahr 1: Eingaben prüfen, Secrets
  schützen, Agentenrechte begrenzen, KI-Änderungen verstehen, testen und
  menschliche Entscheidungen begründen. Didaktische Tiefe wächst mit.
- C5-Test ist N/A im genehmigten Scope; keine neue rechtliche Freistellung.
  Scope-Wiedervorlage 2026-12-31, technische Wiedervorlage 2027-09-09,
  früher bei relevanter Scope-/Quellen-/Paketänderung.
- Pilot-, Projekt- und allgemeine Freigaben bleiben Open; keine Risiko-,
  Produkt-, Image-, Konformitäts- oder Zertifizierungsentscheidung folgt daraus.
  Zentrale Preset-Abnahme bleibt separat nach sieben belegten Ergebnissen und
  dem Upstream-Ergebnis von [github/spec-kit#4455](https://github.com/github/spec-kit/issues/4455).

*The CLI leaves two orphan Claude skills after temporary removal; reinstall
works, but complete removal is not claimed. The global gate and intake
provenance stay intact. All seven projects are non-production educational
references for the four IT training occupations, with secure AI-assisted work
from year one. C5 testing is outside scope; scope review is due 2026-12-31,
technical review 2027-09-09. Human approvals, legal conclusions and central
preset acceptance are not inferred.*

*Initial CI also detected the stale embedded-script inventory after installation.
The existing renderer updates that reference without changing the catalog.*

## Dokumentation und AEPS / Documentation and AEPS

Documentation Impact: `UpdateRequired`. Owner @hindermath; Zielgruppen
Lernende, Maintainer und Reviewer. Leserpfad: README -> Feldbericht -> Matrix,
Runbooks, Rohhash- und Kompositionsnachweise. DE zuerst, EN danach, textorientiert.
Repository-lokale Preset-Installation; kein Home-Sync aus AOC.
Statistikpflege über den bestehenden Renderer.

*The report and context are canonical repository-local evidence, reached from
README. Documentation is German-first/English-second and text-oriented;
statistics use the existing renderer. AOC does not synchronize Home.*

AEPS-Prüfung / AEPS assessment:
[No-change-Receipt](../aeps/receipts/2026-09-09-assurance-v013-field-test.md).
Die Beobachtungen bestätigen bestehende Evidence-/Autoritätsgrenzen und die
bereits dokumentierte CLI-Deinstallationsgrenze; keine neue Preset-Promotion.

*The receipt records no new deduplicable AEPS candidate. Existing integrity
and authority patterns are confirmed; no preset promotion is granted.*
