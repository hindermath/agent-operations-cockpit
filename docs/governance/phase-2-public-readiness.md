# Phase-2-Public-Readiness / Phase 2 Public Readiness

## Status und Zweck

Dieses Dokument ist das menschliche Stop-Gate vor der erstmaligen öffentlichen
Veröffentlichung des Agent Operations Cockpit. Es erlaubt weder die
Veröffentlichung selbst noch Specify-, Plan-, Tasks- oder Implementierungsläufe.
Freigegeben werden soll ausschließlich der nach allen lokalen Prüfungen benannte
Git-Commit.

*This document is the human stop gate before the initial public publication of
Agent Operations Cockpit. It authorises neither publication itself nor specify,
plan, task, or implementation runs. Only the exact Git commit named after all
local checks is proposed for approval.*

## Bestätigte Repository-Identität

| Feld | Verbindlicher Wert |
|---|---|
| ProductName | `Agent Operations Cockpit` |
| RepositoryName | `agent-operations-cockpit` |
| GitHubOwner | `hindermath` |
| Visibility | `Public` |
| lokaler Zielpfad | `~/RiderProjects/AgentOperationsCockpit` |
| Default Branch | `main` |
| Lizenz | `MIT` |
| Primärsprache | `C#/.NET`, speichersicher |
| Preset Profile | `intake-sequencing-eleven-governance-presets` |
| DeliveryMode | `MergeAndSync` mit Admin-Bypass nur für die ausdrücklich genehmigte Lieferung |

*These values resolve RF-04. Public visibility does not waive the separate
security and human approval gate.*

## Verbindlicher Veröffentlichungsumfang

Der erste öffentliche Commit darf enthalten:

- Bootstrap-, Constitution-, Agent-Guidance- und Spec-Kit-Artefakte,
- die elf freigegebenen Governance-Presets ohne lokalen Cache,
- Lastenheft-Intake- und Reihenfolgegrundlagen,
- sichere Entwicklungs- und Dokumentationsgrundlagen,
- README, MIT-Lizenz, Sicherheits- und Beitragsregeln,
- CI-, Dependency- und Public-Readiness-Konfiguration,
- reproduzierbar erzeugte Projektstatistik.

Er darf keinen Produktcode, keine Zugangsdaten, keine privaten Registry-Daten,
keine persönlichen absoluten Pfade, keine nicht redistribuierbaren Assets und
keinen `.specify/presets/.cache/` enthalten.

*The first public commit may contain the governance and requirements baseline
listed above. It must contain no product code, credentials, private registry
data, personal absolute paths, non-redistributable assets, or preset cache.*

## Findings-Coverage

| Finding | Auflösung in diesem Gate | Messbares Kriterium | Positive Evidence | Negative Evidence |
|---|---|---|---|---|
| RF-04 | Alle Repository-Identitätswerte sind menschlich bestätigt und oben festgehalten. | Kein Pflichtfeld ist leer oder mehrdeutig. | Tabelle und Freigabereceipt stimmen überein. | Abweichender Owner, Name, Pfad, Branch, Profil oder Lizenz. |
| RF-05 | Bootstrap legt C#/.NET als Primärsprache, aber keine Produkt-Runtime oder Bibliothek fest. | Kein Produkt-`.csproj`, keine Solution und keine Produktabhängigkeit im Commit. | CI meldet Restore/Build/Test zunächst `NotApplicable`. | Scaffold, TFM, Testframework, Logging, IPC oder Native AOT ohne Decision. |
| RF-11 | Formales Sicherheitsgate vor erstem Push. | Secret- und Pfadscan grün; Lizenz, `SECURITY.md`, `CONTRIBUTING.md`, CI, Dependency-Strategie und menschliche Freigabe vorhanden. | Prüfprotokoll und exakter Commit-SHA. | Cache, Geheimnis, persönlicher Pfad, fehlende Pflichtdatei oder unfreigegebener Push. |

## Security-, Trust- und Authority-Grenzen

- Das öffentliche Repository wird nach dem ersten genehmigten Push kanonische
  Produkt- und Lastenheftquelle.
- Home Baseline bleibt Bootstrap-, Tooling- und Governance-Provenienz, ist aber
  keine Produktlaufzeitabhängigkeit und keine fachliche Geheimquelle.
- Der lokale Checkout ist vor Veröffentlichung die einzige Schreibquelle.
- Die ABS-DD-Sandbox ist später Execution Node: Sie darf freigegebene Quellen
  mounten, bauen, testen und analysieren, besitzt aber keine Repository- oder
  Home-Autorität.
- Remote-Schreiben ist auf das bestätigte Repository und den exakten Commit
  begrenzt. Andere Issues, Repositories und Branches sind nicht umfasst.
- Admin-Bypass ändert keine Qualitäts-, Security- oder Human-Review-Gates.

*The public repository becomes the canonical product and requirements source
after the approved first push. Home Baseline remains tooling and governance
provenance, not a runtime or hidden domain dependency. Sandbox execution has no
repository authority. Admin bypass does not waive quality, security, or human
review gates.*

## Bewusst vertagte Decisions

Folgende Entscheidungen bleiben offen und dürfen nicht durch Bootstrap oder CI
vorweggenommen werden:

- konkrete .NET-/C#-Version und Target Framework Moniker (TFM),
- Solution- und Projektzuschnitt,
- Testframework, Coverage-Grenzen und Testdatenstrategie,
- Logging, Konfiguration, Persistenz und Telemetrie,
- IPC-, Plugin-, Geräte- und Hardwareadapter-Verträge,
- Terminal-/TUI-Framework und alternative Darstellungen,
- Native AOT und Plattformpaketierung,
- Dependency- und Vulnerability-Automation für künftige NuGet-Pakete,
- endgültiges Branch-Ruleset nach Anlage des öffentlichen Repositories.

*These decisions remain open and require their own decision intakes. Bootstrap
and CI must not settle them implicitly.*

## Lokale Readiness-Checkliste

- [ ] Exakter Commit-SHA und vollständige Dateiliste sind dokumentiert.
- [ ] Working Tree ist sauber.
- [ ] Elf Presets sind in den freigegebenen Versionen installiert.
- [ ] Preset-Cache ist ignoriert und nicht getrackt.
- [ ] Homogenitätscheck ist erfolgreich.
- [ ] Secret-Scan ist erfolgreich.
- [ ] Prüfung auf persönliche absolute Pfade und private Registry-Daten ist erfolgreich.
- [ ] Alle veröffentlichbaren Assets besitzen eine zulässige Herkunft oder Lizenz.
- [ ] README, `LICENSE`, `SECURITY.md` und `CONTRIBUTING.md` sind vorhanden.
- [ ] CI und Dependency-Strategie sind vorhanden.
- [ ] Documentation Impact ist dokumentiert.
- [ ] Mensch hat den exakten öffentlichen Payload freigegeben.

*Every checkbox requires evidence. A failed or unknown check stops publication.*

## Documentation Impact

- Bootstrap- und Preset-Artefakte: `GeneratedUpdate`; Quelle ist der genehmigte
  Level-0-Bootstrap mit dem Elf-Preset-Profil.
- README, Lizenz, Sicherheits-, Beitrags-, CI- und Readiness-Unterlagen:
  `UpdateRequired`; Owner ist die Phase-2-Repository-Baseline.
- Projektstatistik nach finaler Erzeugung: `GeneratedUpdate`; Quelle ist die
  versionierte Statistik-Konfiguration und der Renderer.

*The generated bootstrap/preset artifacts and rendered statistics use
`GeneratedUpdate`. The manually authored public-readiness documents use
`UpdateRequired`.*

## Freigaberegel

Die Freigabe muss Repository, Sichtbarkeit und exakten Commit-SHA nennen. Jede
inhaltliche Änderung danach macht die Freigabe ungültig und erfordert eine neue
Prüfung. Erst nach dieser Freigabe darf `hindermath/agent-operations-cockpit`
öffentlich erzeugt und `main` erstmals gepusht werden.

*Approval must name the repository, visibility, and exact commit SHA. Any
content change invalidates approval and requires a new review. Only then may
the public repository be created and `main` pushed for the first time.*
