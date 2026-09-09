# baseline: AOC-Feldtest / AOC field test

Owner: @hindermath. Mode: training. Context: aoc-assurance-v013.

Voraussetzung: unverändertes v0.1.3-ZIP, aktive Security Governance und
genehmigter Governance-Scope ohne Produktlauf. Nur baseline prüfen.
Baseline bindet Quellen, Delta die Installation und Autorität, Closure trennt
menschliche Entscheidungen, Image Impact dokumentiert unveränderte Images.
Vorher/nachher rohe SHA-256 aller Kontextdateien (inklusive versteckter Dateien)
ordinal nach relativem Pfad vergleichen. Bei Drift, fehlender Evidence oder
unerwartetem Ergebnis stoppen; keine Quellen oder Entscheidungen ändern.

*Require the immutable package, active dependency and authorized governance-only
scope. Review only baseline; compare ordinal relative paths and raw SHA-256 of all
context files before/after, including hidden files. Stop on drift or unexpected
results. No source mutation or inferred human decisions.*

Auf macOS Bash zuerst, danach PowerShell / *On macOS run Bash first, then PowerShell:*

```bash
bash .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.sh review baseline aoc-assurance-v013 training
```

```powershell
pwsh -NoProfile -File .specify/presets/secure-development-assurance-governance/scripts/validate-secure-development-assurance.ps1 -Action Review -Gate baseline -ContextId aoc-assurance-v013 -Mode training
```

Erwarteter Exitcode / Expected exit: 0. Negativfälle nur in isolierten
Fixtures, erwarteter Exit 2 / *Negative cases use isolated fixtures, exit 2.*
