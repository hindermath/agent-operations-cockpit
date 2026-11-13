# Projektstatistik / Project Statistics — AgentOperationsCockpit

> **Lebendiges Dokument / Living document** — nach jedem abgeschlossenen Feature,
> jeder Spec-Kit-Phase und auf explizite Anfrage aktualisieren.
>
> *Update after every completed feature, Spec-Kit phase, or on explicit request.*

---

## Fortschreibungsprotokoll / Update Log

Ältester Eintrag oben, neuester Eintrag unten.
*Oldest entry at top, newest entry at bottom.*

| Datum / Date | Phase / Branch | Aktivtage ges. | Zeilen ges. | Commits ges. | Hauptarbeitspakete / Main Work Packages |
|---|---|---:|---:|---:|---|
| 2026-07-31 | 0 — Bootstrap | 1 | — | 1 | Initialer Projekt-Bootstrap via bootstrap-project |
| 2026-08-02 | 1 — CI-Runnerprofil | — | — | — | Documentation Impact `GeneratedUpdate`: Die generischen Maintenance-TUI- und PowerShell-Analyse-Workflows verwenden die Fleet-Policy; AOC bleibt als öffentliches Referenz-Repository vollständiger Linux-/macOS-/Windows-Canary. Produktcode, API und Bedienung bleiben unverändert. |

| 2026-09-09 | Assurance v0.1.3 Governance-Feldtest / Governance field test | — | — | — | Optionales 13-Preset-Profil, eigener training-Kontext, vier Gates und Runbooks, Rohhash-/Paritaets-/Kompositionsnachweise. Paket- und AOC-Governance-Tests bestanden; keine Produktlaeufe oder menschlichen Freigaben. Ausbildungszweck ab Lehrjahr 1 fuer vier IT-Ausbildungsberufe; AEPS NoChange. / Installed optional profile, scoped evidence and passing technical tests; no product run or human approval. |
| 2026-09-11 | Feature 032 AOC-Vertikalscheibe / Feature 032 AOC vertical slice | — | — | — | Documentation Impact `GeneratedUpdate`: Das unveränderte Phase-2-Manifest erzeugt zwei verlinkte Fünf-Felder-Ansichten. Drei historische logische META-LH-Pfade werden nur über jeweils eine featuregestempelte Datei und ihren hashgebundenen terminalen Abschlussnachweis aufgelöst; Manifest und Lifecycle bleiben unverändert. Gepaarte Bash-/PowerShell-Verträge validieren zusätzlich Zielhashes, Graphsemantik einschließlich sichtbarer Kantenrichtung, exakte Root-Mengen, fehlende logische Ausgabepfade und echte Cross-Implementation-Parität. `global-ready`, Secret-, PSScriptAnalyzer-, Skriptkatalog-, A11Y-, Security- und Architekturprüfungen sind lokal grün. Constitution und fünf Agentenflächen tragen die installierte Autonomous-Version 0.4.1; Assurance-Kontext, Produktcode, Dependencies und Home-Sync bleiben unverändert. Das fachliche Delta vor Statistikpflege umfasst 4.395 Nettozeilen. / The unchanged phase-2 manifest now generates two linked five-field views with hash-bound terminal stamped-path resolution. Paired Bash/PowerShell contracts additionally validate target hashes, graph semantics including visible edge direction, exact roots, missing logical output paths, and real cross-implementation parity. Local programme, security, documentation, and architecture gates pass; product and assurance contexts remain unchanged. |

---

| 2026-09-13 | Intake-Lifecycle-Preset-Rollout / Intake lifecycle preset rollout | N/A | N/A | N/A | Vorhandene Authoring-/Review-/Sequencing-Presets auf 0.3.2/0.2.2/0.2.4 aktualisiert; optionale Profile und Dokumentation nachgefuehrt. Pruefnachweise in docs/maintenance/intake-lifecycle-fleet-rollout.json. / Update existing presets and profile references; preserve other presets and project extensions. |
| 2026-09-13 | META-LH-04 Series Eligibility | — | — | — | Documentation Impact `UpdateRequired`: Neun typisierte Eligibility-Kriterien, sechs Auswertungsmodi, Bash-/PowerShell-Paritaet, positive und negative Fixtures sowie kausale Feature-, Lifecycle- und Closeout-Evidence geliefert. T001–T057 sind abgeschlossen; PR #49, #52 und #53 wurden an geprueften Heads gemergt und `main` auf `0 0` synchronisiert. / Nine typed eligibility criteria, six assessment modes, Bash/PowerShell parity, positive and negative fixtures, and causal feature, lifecycle and closeout evidence delivered. T001-T057 are complete; PRs #49, #52 and #53 merged at reviewed heads and main synchronized at zero divergence. |
| 2026-09-13 | Mermaid und Abschlussberichte | N/A | N/A | N/A | Neue textbasierte Diagrammregel, Berichtsvorlage, Agent-Paritaet und versionierte Governance; kein Produktcode. / Text-first diagram and completion-report governance; no product code. |

| 2026-09-19 | Statistik-Preset-Rollout v0.1.0 / Statistics preset rollout | — | — | — | Optionales 14er-Profil, getrennter UTC-Kontext ohne Referenzmodelle; Profil 2 bleibt kanonisch. Native Proof-CI und Paketbindung; keine Produktlaeufe oder Freigaben. / Optional profile, separate UTC context and native evidence; preserve legacy statistics and human approval boundaries. |

## Gesamtstand des Repositories / Repository Snapshot

Stand / As of: 2026-09-13. Die kanonischen aktuellen Werte stehen im
generierten Statistikprofil 2 unter `Gesamtstatistik / Overall Statistics`.
Der frühere, noch nicht befüllte Profil-1-Platzhalter wurde entfernt, damit
keine veraltete Momentaufnahme mit der lebenden Statistik konkurriert.

*As of 2026-09-13. The generated Profile 2 under `Gesamtstatistik / Overall
Statistics` is the canonical current snapshot. The former unpopulated Profile
1 placeholder was removed so that no stale snapshot competes with the living
statistics.*

### 2026-09-19 - OpenCode-Pfadmigration / OpenCode path migration

41 Befehlsdateien unter `.opencode/command/` vereinheitlicht; Inhalte
hashgeprüft, Manifestpfade und Ignore-Regeln angepasst. Drei Paritätstests
bestanden. Documentation Impact: UpdateRequired.
[Nachweis / Evidence](maintenance/opencode-path-migration-20260919.md).

*Migrated 41 commands to the singular path with hash verification,
manifest and ignore alignment. Three parity tests passed.*

### 2026-10-29 - Storage-Check-only-Make-Härtung / Storage check-only Make hardening

DE: Der gemeinsame cc65-Storage-Adapter startet in Check-only, Dry-run sowie
Dirty-/Busy-Updates kein projektgesteuertes Make mehr. Sechzehn gezielte
Vertragstests bestanden. Documentation Impact: UpdateRequired; die Manpage
beschreibt die sichere Modusgrenze. Statistik ist Git-basierte Transparenz,
keine gemessene KI-Produktivität.

EN: The shared cc65 storage adapter no longer starts project-controlled Make
in check-only, dry-run, or dirty/busy updates. Sixteen focused contract tests
passed. Documentation Impact: UpdateRequired; the man page documents the safe
mode boundary. Statistics provide Git-based transparency, not measured AI
productivity.

### 2026-10-31 - Security-Remediation / Security remediation

DE: Lokale Sicherheitsgrenzen fuer Wartung, Lernpakete und parallele
Kampagnen gehaertet. Der Paket-Freigabepfad hat einen verpflichtenden
Secret-Scan; produktive Parallel-Kampagnen bleiben bis zur isolierten
Worker-Laufzeit gesperrt. Documentation Impact: UpdateRequired. Das
generierte Profil 2 wurde nach dem lokalen Code-Commit aktualisiert;
Security-Diff-Scans und gezielte Tests liefern die technische Evidence.

EN: Local security boundaries for maintenance, learning packages and
parallel campaigns were hardened. Package release now requires a secret
scan; production parallel campaigns remain suspended until workers have an
isolated runtime. Documentation Impact: UpdateRequired. Profile 2 was
rendered after the local code commit; security diff scans and focused tests
provide technical evidence.

### 2026-11-03 - Dependabot-Wartung / Dependabot maintenance

DE: Branch `codex/dependabot-maintenance-20261103`, Arbeitsfenster 2026-11-03.
Repository-spezifische Versions-/Sicherheitsgruppen und zweisprachige
Wartungshinweise ergaenzt. Kein Produktions- oder Testcode geaendert;
Konfigurations-/Dokumentationsumfang ist im PR-Diff belegt. Profil 2 wird
aus der committed Inhaltsrevision gerendert; bestehende Referenzen bleiben.
YAML/Schema, Manifestabdeckung, Policy, Dokumentation, Liefermenge und
Secret-Scan bestanden. Hosted-Checks werden am PR verfolgt. Keine Pakete
aktualisiert; Git-basierte Statistik misst keine KI-Zeitersparnis.

EN: Branch `codex/dependabot-maintenance-20261103`, work window 2026-11-03.
Adds repository-specific version/security groups and bilingual maintenance
guidance. No production or test code changed; the PR diff records the exact
configuration/documentation scope. Profile 2 is rendered from the committed
content revision with existing references. YAML/schema, manifest coverage,
policy, documentation, delivery scope and secret scan passed. Hosted checks
are tracked on the PR. No packages updated; Git statistics do not measure
AI time savings.

### 2026-11-09 - Dependabot PR #73 / Dependabot maintenance

DE: Branch codex/dependabot-repair-20261109-agent-operations-cockpit--73; sichtbares Wartungsfenster 09.11.2026, keine
Stoppuhrmessung. chore(deps): bump astral-sh/setup-uv from 6.8.0 to 10.3.3. Dokumentationsentscheidung: NoUpdateRequired
fuer die technische Aenderung; GeneratedUpdate fuer beide vorhandenen
Statistikprofile. Bestehende Referenzwerte bleiben erhalten. Die beobachtete
Liefermenge ist keine Messung von Lernleistung oder KI-Zeitersparnis.
Aktuelle Head-/Plattform-Pruefungen sind vor dem Merge erforderlich.
Owner: Repository-Maintainer; Source-only, kein Home-Sync.

EN: Branch codex/dependabot-repair-20261109-agent-operations-cockpit--73; observable maintenance window 9 November 2026,
not stopwatch time. chore(deps): bump astral-sh/setup-uv from 6.8.0 to 10.3.3. Documentation impact: NoUpdateRequired for
the technical change; GeneratedUpdate for the existing statistics profiles.
Existing references remain unchanged. Delivery volume is not a measurement
of learning outcomes or AI time savings. Current head/platform checks are
required before merge. Owner: repository maintainer; source-only, no Home sync.
### 2026-11-12 — Sicherheitsrichtlinie / Security policy

DE: Genehmigte Sicherheitsrichtlinie DE zuerst/EN danach auf CEFR-B2-Niveau
harmonisiert, projektspezifische Grenzen und bestehende Reaktionsziele erhalten.
Private Advisory-Links und Sprach-/Überschriftenstruktur geprüft.
Documentation Impact: UpdateRequired; Nachweis unter
`docs/documentation-impact/security-policy-2026-11-12.json`.
Keine Produktlogik geändert; CodeQL unter Tools wird nach Lieferung separat
eingerichtet. Keine AI-Scan-Aktivierung oder neue praktische A11Y-Abnahme.

EN: Harmonised the approved German-first/English-second security policy at
CEFR B2, preserving project boundaries and existing response targets. Checked
private advisory links, language boundaries and heading structure.
Documentation Impact: UpdateRequired; see the evidence path above.
No product logic changed; CodeQL under Tools is configured separately after
delivery. No AI Scan activation or new practical accessibility acceptance.

### 2026-11-13 — Gemeinsame Preset-Sicherheitswartung / Shared preset security maintenance

Vierzehn veroeffentlichte Patch-Releases sind ueber echte Quellen- und Installationsbindungen uebernommen. Gemeinsame Workflow-Rechte sind explizit begrenzt; Produktlogik und Lifecycle bleiben unveraendert. Offene CodeQL-Belegluecken bleiben offen, ohne automatische Alert-Verwerfung.

Fourteen published patches are recorded through real source and installed bindings. Shared workflow permissions are explicitly restricted; product logic and lifecycle remain unchanged. Open CodeQL evidence gaps remain open without automatic alert dismissal.

Documentation Impact: UpdateRequired; [Wartungsnachweis / maintenance evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — Intake Authoring 0.3.14 / Intake-Authoring-Folgekorrektur

DE: Die geprüfte Patch-Version 0.3.14 ergänzt den Sicherheitsrollout; Quellen- und Installationsbindungen sowie kompatible Nachweise bleiben getrennt nachvollziehbar. Keine neue Produktfunktion oder menschliche Sicherheitsabnahme.

EN: Verified patch 0.3.14 supplements the security rollout; source, installation and compatible evidence remain separately traceable. No new product feature or human security acceptance.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

### 2026-11-13 — npm-Agent-Proben begrenzt / Bound npm agent probes

DE: Die verteilten Wartungsskripte begrenzen npm-Agent-Proben vor der Ausfuehrung. TinyPl0 behaelt seine ausdrueckliche Freigabe fuer alternative Registries. Es wird kein Spec-Kit-Lauf hinzugezaehlt.

EN: Distributed maintenance scripts bound npm agent probes before execution. TinyPl0 retains its explicit opt-in for alternate registries. No Spec Kit run is added.

Documentation Impact: UpdateRequired; [Nachweis / evidence](maintenance/shared-security-rollout-2026-11-13.md).

+### 2026-11-13 — npm-Cachepfad gebunden / Bound npm cache path

DE: Die verteilte Speicherwartung liest den tatsächlich konfigurierten
npm-Cachepfad, prüft ihn innerhalb des Home-Verzeichnisses und bindet genau
diesen Pfad an verify und clean. Eine abweichende Projekt-.npmrc kann die
spätere Bereinigung nicht mehr umleiten. Kein Spec-Kit-Lauf wird ergänzt.

EN: Distributed storage maintenance reads npm's effective cache path, checks
it inside home, and binds that exact path to verify and clean. A different
project .npmrc path can no longer redirect the later cleanup. No Spec Kit run
is added.

Documentation Impact: UpdateRequired; [Nachweis / evidence](documentation-impact/npm-cache-boundary-2026-11-13.json).
## Gesamtstatistik / Overall Statistics

<!-- project-statistics-v2:begin -->

Profil 2 verwendet Git-getrackte Textdateien und sichtbare Git-Aktivitaet. Die Werte beschreiben Lieferdichte, keine persoenliche Arbeitszeit.

*Profile 2 uses Git-tracked text files and visible Git activity. The values describe delivery density, not personal working time.*

| Kennzahl / Metric | Wert / Value |
|---|---:|
| Textbasis / Text base | 418030 lines |
| Textdateien / Text files | 2414 |
| Beobachtbarer Zeitraum / Observable period | 2025-11-16..2026-11-13 |
| Aktivtage / Active days | 29 |
| Relevante Commits / Relevant commits | 202 |
| Zeilen je Aktivtag / Lines per active day | 14414.8 |
| Peak-Tag im Fenster / Peak day in window | 2026-07-31 / 132656 |
| Peak-Woche im Fenster / Peak week in window | 2026-07-26 / 135472 |
| Laengste Serie / Longest streak | 4 days |
| Speedup vs. 80 lines/day | 180.2x |
| Speedup vs. 125 lines/day | 115.3x |
| Methodik / Methodology | v2; source `f64e6959f1a7` |

### Artefaktmix / Artifact Mix

```text
Produktiv / Production          [#...................]   2.5% | 10650
Tests                           [###.................]  12.7% | 53253
Dokumentation / Documentation   [##########..........]  47.8% | 199685
Skripte / Scripts               [###.................]  13.9% | 58261
Konfiguration / Configuration   [#####...............]  23.0% | 96038
Daten und Medien / Data and media [....................]   0.0% | 0
Sonstiger Text / Other text     [#...................]   0.0% | 143
```

Die Balken teilen die aktuelle getrackte Textbasis in stabile Kategorien. Prozent und Zeilenwert sind die genaue, textorientierte Aussage.

*The bars split the current tracked text base into stable categories. Percentages and line counts provide the exact text-first result.*

### Tagesaktivitaet / Daily Activity

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
So/Su  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Mo/Mo  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Di/Tu  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Mi/We  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Do/Th  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Fr/Fr  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Sa/Sa  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
So/Su  0 0 0 0 0 0 0 0 0 0 0 4 4 4 0 4 4 4 4 0 0 0 0 0 4 0
Mo/Mo  0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 2
Di/Tu  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0
Mi/We  0 0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 4 0 0 0 0 0 0 0 0 0
Do/Th  0 0 0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 2 0 2
Fr/Fr  0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 4 0 1 0 0 0 0 3 0 4
Sa/Sa  0 0 0 0 0 0 0 0 0 0 4 0 2 0 3 4 3 4 2 0 0 0 0 4 0 -
```

DE: 0 = keine Aenderung; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ geaenderte Textzeilen; - = noch nicht abgelaufen.

*EN: 0 = no change; 1 = 1..79; 2 = 80..399; 3 = 400..1599; 4 = 1600+ changed text lines; - = not elapsed.*

### Wochenvolumen / Weekly Volume

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
Keine Aktivitaet / No activity
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
  cap 200000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      166667 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      133333 | . . . . . . . . . . # . . . . . . . . . . . . . . .
      100000 | . . . . . . . . . . # . . . . . . # . . . . . . . .
       66667 | . . . . . . . . . . # . . . . . . # . . . . . . . .
       33333 | . . . . . . . . . . # . # . . . . # . . . . . . . #
           0 +-----------------------------------------------------
```

Das Wochenvolumen zeigt Additionen plus Loeschungen. Es ist Aenderungsaktivitaet, nicht die aktuelle Groesse des Repositories.

*Weekly volume shows additions plus deletions. It represents change activity, not the current repository size.*

### Kumulative Entwicklung / Cumulative Development

```text
Wochen / Weeks 01..26 | 2025-11-16..2026-05-16
Keine Aktivitaet / No activity
```

```text
Wochen / Weeks 27..52 | 2026-05-17..2026-11-14
  cap 500000 | . . . . . . . . . . . . . . . . . . . . . . . . . .
      416667 | . . . . . . . . . . . . . . . . . . . . . . . . . #
      333333 | . . . . . . . . . . . . . . . . . # # # # # # # # #
      250000 | . . . . . . . . . . . . . . . . # # # # # # # # # #
      166667 | . . . . . . . . . . . . # # # # # # # # # # # # # #
       83333 | . . . . . . . . . . # # # # # # # # # # # # # # # #
           0 +-----------------------------------------------------
```

Die kumulative Kurve summiert nur das Brutto-Aenderungsvolumen im Fenster. Sie darf nicht als aktuelle Codebasis gelesen werden.

*The cumulative curve sums gross change volume within the window only. It must not be read as the current code base.*

### Phasenvolumen / Phase Volume

```text
Slots 0..1
    cap 5000 | . .
        4167 | # .
        3333 | # .
        2500 | # .
        1667 | # .
         833 | # .
           0 +-----
             00 01
```

| Slot | Phase | Nettozeilen / Net lines |
|---:|---|---:|
| 0 | Feature 032 AOC-Vertikalscheibe / Feature 032 AOC vertical slice | 4395 |
| 1 | Storage-Check-only-Make-Härtung / Storage check-only Make hardening | 187 |

Die festen Slots halten den Phasenvergleich auch bei fehlenden oder spaeter ergaenzten Werten stabil.

*Stable slots keep the phase comparison consistent when values are missing or added later.*

### Beschleunigungsfaktoren / Acceleration Factors

```text
Scale: 0..200x
80 lines/day       [##################..] 180.2x
125 lines/day      [############........] 115.3x
```

Die Faktoren vergleichen sichtbare Lieferdichte mit den dokumentierten manuellen Referenzen. Sie messen keine Arbeitszeit.

*The factors compare visible delivery density with documented manual references. They do not measure working time.*

### Durchsatzvergleich / Throughput Comparison

```text
Scale: 0..20000 lines/day
Experienced manual [#...................] 80
Thorsten solo      [#...................] 125
Visible repository [##############......] 14414.8
```

Die gemeinsame Skala vergleicht Referenzen und sichtbare Lieferdichte. Sie schreibt die Git-Aktivitaet keiner Person oder KI pauschal zu.

*The common scale compares references with visible delivery density. It does not attribute Git activity to a person or AI by default.*

### Textalternative / Text Alternative

DE: Das Fenster beginnt am 2025-11-16 und endet am 2026-11-13. Es enthaelt 29 aktive und 334 inaktive vergangene Tage. Peak-Tag: 2026-07-31 / 132656. Peak-Woche: 2026-07-26 / 135472. Laengste Serie: 4 Tage (2026-10-29..2026-11-01).

*EN: The window starts on 2025-11-16 and ends on 2026-11-13. It contains 29 active and 334 inactive elapsed days. Peak day: 2026-07-31 / 132656. Peak week: 2026-07-26 / 135472. Longest streak: 4 days (2026-10-29..2026-11-01).*

| Monat / Month | Geaenderte Textzeilen / Changed text lines |
|---|---:|
| 2025-12 | 0 |
| 2026-01 | 0 |
| 2026-02 | 0 |
| 2026-03 | 0 |
| 2026-04 | 0 |
| 2026-05 | 0 |
| 2026-06 | 0 |
| 2026-07 | 132656 |
| 2026-08 | 100254 |
| 2026-09 | 145652 |
| 2026-10 | 7659 |
| 2026-11 | 62176 |

<!-- project-statistics-v2:end -->
