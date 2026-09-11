# prepare-secure-development-hardening(1)

## Name

`prepare-secure-development-hardening` — bereitet MSL-Level-2-Repositories fuer spaetere Secure-Development-Haertung vor

*prepares MSL level-2 repositories for later secure-development hardening*

## Synopsis

```bash
bash scripts/prepare-secure-development-hardening.sh [--repo PATH] [--dry-run] [--commit] [--push] [--allow-dirty]
bash scripts/prepare-secure-development-hardening.sh --repo PATH --order-only --manifest PATH [--order-output PATH ...] [--dry-run]
```

```powershell
pwsh scripts/prepare-secure-development-hardening.ps1 -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Help
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo PATH -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo PATH -OrderOnly -Manifest PATH [-OrderOutput PATH] -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Commit -Push
```

## Beschreibung / Description

`prepare-secure-development-hardening` findet Level-2-Repositories unter dem
Home-Verzeichnis, prueft die Primaersprache gegen die MSL-Allowlist aus der
Workspace-Constitution und bereitet passende Repositories fuer spaetere
Spec-Kit-Haertungslaeufe vor.

*`prepare-secure-development-hardening` discovers level-2 repositories below the
home directory, checks the primary language against the MSL allow-list from the
workspace constitution, and prepares matching repositories for later Spec Kit
hardening runs.*

Bei MSL-Repositories werden:

- `docs/secure-development/` aus der zentralen Baseline synchronisiert,
- `Lastenheft_Secure-Development-Hardening.md` erzeugt, wenn es fehlt,
- `Lastenheft_Abarbeitungsreihenfolge.md` anhand eines eindeutigen kanonischen
  Series-Manifests oder, ohne ein solches Manifest, anhand von
  `Lastenheft*.md` gepflegt.

*For MSL repositories, the script synchronizes `docs/secure-development/`, creates
`Lastenheft_Secure-Development-Hardening.md` when missing, and maintains
`Lastenheft_Abarbeitungsreihenfolge.md` from one unambiguous canonical series
manifest or, when none exists, from `Lastenheft*.md`.*

## Erzeugte Ansicht / Generated View

Die manifestgestuetzte Tabelle besitzt genau diese Spaltenfolge:

1. `Position` aus ausdruecklicher Intake-Metadatenposition, sonst Manifestplatz,
2. `Status` unveraendert aus dem Manifest,
3. `Lastenheft/Intake` mit vollstaendigem Dateinamen und sicherem relativem Link,
4. `Abhängigkeiten / Dependencies` nur fuer direkte eingehende Manifestkanten,
5. `Spec-Kit-Feature` nur bei genau einer ausdruecklichen gueltigen Bindung.

*The manifest-backed table has exactly this column order: `Position` from
explicit intake metadata or otherwise the manifest slot, unchanged `Status`,
`Lastenheft/Intake` with the complete filename and a safe relative link,
`Abhängigkeiten / Dependencies` for direct incoming manifest edges only, and
`Spec-Kit-Feature` only for exactly one explicit valid binding.*

Ohne eingehende Kante erscheint exakt
`— (Root / keine direkte Abhängigkeit)`. Ohne eindeutigen gueltigen
Feature-Nachweis erscheint exakt
`— (kein Spec-Kit-Feature / no Spec Kit feature)`. Mehrdeutige oder unsichere
Nachweise stoppen den Lauf, statt einen Link zu raten.

*A row without an incoming edge uses exactly the root fallback above. A row
without unique valid feature evidence uses exactly the no-feature fallback
above. Ambiguous or unsafe evidence stops the run instead of guessing a link.*

Das Skript startet keinen Spec-Kit-Lauf, erzeugt keinen Feature-Branch und
befuellt keine projektspezifischen `docs/security/`-Nachweise. Diese Schritte
bleiben separate, explizit gestartete Haertungslaeufe.

*The script does not start a Spec Kit run, does not create a feature branch, and
does not populate project-specific `docs/security/` evidence. Those steps remain
separate hardening runs started explicitly.*

## Repo-Erkennung / Repository Discovery

Standard-Erkennung:

- Level 1: direkte Unterverzeichnisse von `~/` mit `.git`
- Level 2: direkte Unterverzeichnisse erkannter Level-1-Repos mit `.git` und
  `.specify/` oder Agenten-Dateien

*Default discovery: level 1 is each direct child of `~/` with `.git`; level 2 is
each direct child of those repositories with `.git` plus `.specify/` or agent
guidance files.*

## Optionen / Options

| Bash | PowerShell | Bedeutung / Meaning |
|---|---|---|
| `--dry-run` | `-WhatIf` | Nur anzeigen, keine Schreiboperationen |
| `--home-dir PATH` | `-HomeDir PATH` | Alternatives Home-Verzeichnis |
| `--repo PATH` | `-Repo PATH` | Explizites Level-2-Repo vorbereiten; wiederholbar |
| `--primary-language LANG` | `-PrimaryLanguage LANG` | Primaersprache explizit setzen |
| `--order-only` | `-OrderOnly` | Nur die Intake-Projektion; genau ein explizites Repo/Manifest |
| `--manifest PATH` | `-Manifest PATH` | Kanonisches Manifest relativ zum expliziten Repo |
| `--order-output PATH` | `-OrderOutput PATH` | Owned Ausgabe; wiederholbar/als Array fuer atomare Multi-Output-Publikation |
| `--commit` | `-Commit` | Pro geaendertem Repo committen |
| `--push` | `-Push` | Pro Repo pushen; aktiviert Commit |
| `--allow-dirty` | `-AllowDirty` | Bestehende lokale Aenderungen erlauben |
| `--help` | `-Help` | Vollstaendige zweisprachige Hilfe; keine Writes |

`--dry-run` und `-WhatIf` fuehren Manifest-, Link-, Kanten-, Positions- und
Feature-Pruefungen aus, veroeffentlichen aber keine Ausgabe. Relative Links
werden vom erzeugten View aus berechnet und muessen innerhalb des Repositorys
auf vorhandene Ziele zeigen.

*`--dry-run` and `-WhatIf` run manifest, link, edge, position, and feature
checks without publishing output. Relative links are calculated from the
generated view and must resolve to existing targets inside the repository.*

`--order-only` / `-OrderOnly` umgeht bewusst die Produktsprachenerkennung und
die Secure-Development-Templatevorbereitung. Dieser Modus erfordert genau ein
explizites Repository und ein repositoryrelatives Manifest. Commit und Push
sind dort verboten. Mehrere Ausgaben werden candidate-first vorbereitet,
gegen die vollstaendige verbrauchte Eingabemenge erneut validiert und atomar
ersetzt oder vollstaendig zurueckgerollt. Ausgaben duerfen keine kanonische
Eingabe ueberlappen.

*`--order-only` / `-OrderOnly` deliberately bypasses product-language detection
and secure-development template preparation. It requires exactly one explicit
repository and a repository-relative manifest. Commit and push are forbidden.
Multiple outputs are prepared candidate-first, revalidated against the complete
consumed input set, and then atomically replaced or fully rolled back. Outputs
must not overlap canonical inputs.*

## Diagnostik und Wiederherstellung / Diagnostics and Recovery

Fehler verwenden die stabile Familie `LIE001` bis `LIE012`. Fuer diesen
positiven Slice sind insbesondere ungueltige Manifestdaten (`LIE002`),
unsichere Pfade (`LIE003`), fehlende Ziele (`LIE004`), Repository-Escapes
(`LIE005`), ungueltige Kanten (`LIE007`) und mehrdeutige Feature-Evidence
(`LIE008`) relevant. Der Renderer schreibt erst nach erfolgreicher Pruefung.
Bei einem Fehler bleibt der vorherige Marker erhalten; Eingabe korrigieren,
Safe Mode erneut ausfuehren und erst danach den Write wiederholen.

*Errors use the stable `LIE001` through `LIE012` family. For this positive
slice, malformed manifests (`LIE002`), unsafe paths (`LIE003`), missing targets
(`LIE004`), repository escapes (`LIE005`), invalid edges (`LIE007`), and
ambiguous feature evidence (`LIE008`) are most relevant. The renderer writes
only after successful validation. On error, keep the previous marker, correct
the input, rerun safe mode, and only then retry the write.*

## Beispiele / Examples

```bash
# Nur pruefen, welche Repos vorbereitet wuerden
bash scripts/prepare-secure-development-hardening.sh --dry-run

# Sprache fuer neue/leere Repos explizit setzen
bash scripts/prepare-secure-development-hardening.sh --dry-run --primary-language C#

# Home-Projektion ohne falschen Produktsprachen-Override pruefen
bash scripts/prepare-secure-development-hardening.sh --repo . --order-only \
  --manifest requirements/intakes/series/home-baseline-delivery/manifest.json \
  --dry-run

# Vier bekannte C#-Level-2-Repos gezielt vorbereiten
bash scripts/prepare-secure-development-hardening.sh --dry-run \
  --repo ~/RiderProjects/TinyPl0 \
  --repo ~/RiderProjects/TinyCalc \
  --repo ~/RiderProjects/TuiVision \
  --repo ~/RiderProjects/InventarWorkerService

# Vorbereiten, committen und pushen
bash scripts/prepare-secure-development-hardening.sh --commit --push
```

```powershell
# Windows / PowerShell
pwsh scripts/prepare-secure-development-hardening.ps1 -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -PrimaryLanguage C# -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo . -OrderOnly -Manifest requirements/intakes/series/home-baseline-delivery/manifest.json -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Repo ~/RiderProjects/TuiVision -WhatIf
pwsh scripts/prepare-secure-development-hardening.ps1 -Commit -Push
```

## Sicherheit / Security

`docs/secure-development/` wird anhand von `baseline-manifest.json`
synchronisiert. Nur dort aufgeführte verwaltete Dateien werden aktualisiert oder
als veraltet entfernt. Projektspezifische Dateien unter `docs/security/` und
vorhandene Lastenhefte bleiben unberührt.

*`docs/secure-development/` is synchronized from `baseline-manifest.json`.
Only listed managed files are updated or removed as stale. Project-specific
files under `docs/security/` and existing Lastenhefte remain untouched.*

Nicht-MSL- oder unklare Repositories werden uebersprungen und melden eine
Begruendung. Eine explizite Sprache kann mit `--primary-language` /
`-PrimaryLanguage` gesetzt werden. `docs/security/` bleibt der projektspezifische
Evidenzpfad und wird nicht automatisch befuellt.

*Non-MSL or unclear repositories are skipped with a rationale. An explicit
language can be provided with `--primary-language` / `-PrimaryLanguage`.
`docs/security/` remains the project-specific evidence path and is not populated
automatically.*
