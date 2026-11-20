# GitHub Copilot Instructions — AgentOperationsCockpit

## Einstieg und Detailregeln / Entry point and detailed rules

DE: Lies die Projektkonstitution und die für deine Aufgabe einschlägigen
[Detailregeln](../../docs/agent-guidance.md), bevor du arbeitest. Die Referenz
enthält die hierher ausgelagerten Regeln zu sicheren Arbeitsabläufen,
Werkzeugen, Presets und projektspezifischen Prüfungen. Projektgrenzen und
Freigaben gelten auch für Arbeiten nach der Detailreferenz.

EN: Read the project constitution and the task-specific
[detailed rules](../../docs/agent-guidance.md) before working. The reference
contains relocated guidance on secure workflows, tools, presets and project
checks. Project boundaries and approval gates apply to work using the reference.

**Workspace**: ~/RiderProjects
**Projekt / Project**: AgentOperationsCockpit

---

## Überblick / Overview

Dieses Dokument konfiguriert GitHub Copilot für das Projekt **AgentOperationsCockpit**.

This document configures GitHub Copilot for the **AgentOperationsCockpit** project.

---

## Projektkontext / Project Context

- **Projektname**: AgentOperationsCockpit
- **Workspace**: ~/RiderProjects
- **Primärsprache / Primary Language**: C# / .NET Framework
- **Standard / Standard**: Workspace Homogeneity Guardian

### Level-0- und Home-Sync-Grenze / Level-0 and Home Sync Boundary

- Der persönliche Fork `~/home-baseline-source` bleibt die versionierte
  Level-0-Quelle und wird nach dem ersten Sync nicht gelöscht.
- `~/` ist nur die manifestgesteuerte lokale Betriebskopie. Vor einem echten
  Home-Sync `--check-only` / `-CheckOnly` verwenden und Konflikte nicht ohne
  Prüfung mit `--force` / `-Force` überschreiben.
- In Containern und insbesondere der ABS-DD-Sandbox die eingebundene
  Level-0-Referenz direkt verwenden; schreibende Home-Sync-Laeufe gehoeren auf
  den Host.

*Keep the personal fork `~/home-baseline-source` as the versioned level-0 source.
`~/` is only the manifest-managed local runtime copy. Check before syncing and
use force only after reviewing conflicts. In containers, especially the
ABS-DD sandbox, use the mounted level-0 reference directly and run writing Home
sync operations on the host.*

---

## Verwendung / Usage

### Coding-Konventionen / Coding Conventions

Dieses Projekt verwendet folgende Konventionen:

- C# mit .NET Framework (kein .NET Core, es sei denn explizit anders vermerkt)
- Deutsch als primäre Kommentarsprache, Englisch als sekundär
- XML-Dokumentationskommentare für öffentliche API-Mitglieder
- Keine bezahlten NuGet-Pakete (DevExpress, Telerik, Syncfusion etc.)

This project uses the following conventions:

- C# with .NET Framework (no .NET Core unless explicitly noted otherwise)
- German as primary comment language, English as secondary
- XML documentation comments for public API members
- No paid NuGet packages (DevExpress, Telerik, Syncfusion etc.)

---

## Einrichtung / Setup

### Voraussetzungen / Prerequisites

- Visual Studio / JetBrains Rider
- .NET Framework SDK
- GitHub Copilot Extension

---

## Statistik-Pflege / Statistics Maintenance

- Führe `docs/project-statistics.md` als lebendes Statistik-Ledger dieses Projekts.
- Aktualisiere die Datei nach jeder abgeschlossenen Spec-Kit-Implementierungsphase, nach jedem abgeschlossenen Feature oder wenn explizit angefordert.
- Im `## Fortschreibungsprotokoll`-Abschnitt gilt: ältester Eintrag oben, neuester Eintrag unten.
- Halte `## Gesamtstatistik` immer als letzten Top-Level-Abschnitt der Datei.
- `docs/project-statistics.config.json` und der markierte Profil-2-Block sind der verbindliche Vertrag; mit `render-project-statistics.*` aktualisieren.
- Profil 2 zeigt KPI, Artefaktmix, 52-Wochen-Tagesaktivität, Wochen- und kumulatives Volumen, Phasen- oder Monatsvolumen, Speedup-Gauges und den manuellen Vergleich.
- Nur ASCII verwenden: Heatmap `0..4`, `-` für noch nicht abgelaufene Tage und Gauges `#`/`.`; keine Unicode-Blöcke, Farbcodierung oder `\ | /` als Intensitätsskala.
- Phasenslots stabil halten, in 16er-Blöcke teilen und ohne belastbare Phasenwerte Monatsvolumen zeigen.
- Diagramme bleiben höchstens 100 Zeichen breit und erhalten genaue Werte sowie eine CEFR-B2-Textalternative in DE zuerst, EN danach.
- Methodik v2 nutzt Git-getrackten Text und Bruttoänderungen aus Nicht-Merge-Commits; Ledger, `STATS.md` und Binärdaten bleiben ausgeschlossen.
- Manuelle Referenz-Basiswerte: `80` Zeilen/Arbeitstag (konservativ) + projektspezifischer Thorsten-Solo-Wert, konsistent dokumentiert in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` und `.github/copilot-instructions.md`.
- Gemeinsame Default-Basis für C#/.NET-Projekte: `125` Zeilen/Arbeitstag, sofern das Repo keinen abweichenden, begründeten Wert dokumentiert.
- Umrechnung in Stunden: `7.8 h` (`7h 48m`) pro Arbeitstag (TVöD). Monate: `21.5` AT/Monat; 30 Urlaubstage bis Ende 2026, ab 2027 dann 31.
- Beschleunigungsfaktoren = blended repository speedup — Lieferdichte gegen manuelle Referenz, keine Stoppuhrzeit.
- Wenn Statistikmethodik oder gemeinsame Guidance geändert wird: alle fünf Agentenflächen einschließlich `.github/agents/copilot-instructions.md` zusammen aktualisieren.

*Maintain the living statistics ledger and render Profile 2 from its JSON configuration. Use ASCII `0..4`, `-`, and `#`/`.` gauges, exact values, bilingual text alternatives, stable phase slots in blocks of 16, and a 100-character chart limit. Methodology v2 excludes the ledger, `STATS.md`, and binaries. Acceleration remains delivery density, not stopwatch time.*

## Hinweise / Notes

- Secrets niemals in Code einfügen — immer Keychain/Umgebungsvariablen verwenden
- Pre-Push-Hook prüft auf Secret-Muster — Commits mit Credentials werden abgelehnt
- `Programmierung #include<everyone>` gilt für alle nutzerseitigen Artefakte: CLI-Ausgaben, Doku, HTML, UI und generierte Templates.
- WCAG 2.2 Level AA ist die Standard-Basis, sobald die Kriterien auf das Artefakt anwendbar sind.
- Shared guidance wird immer gemeinsam in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` und `.github/agents/copilot-instructions.md` gepflegt.

- Never embed secrets in code — always use Keychain/environment variables
- Pre-push hook checks for secret patterns — commits with credentials are rejected
- `Programmierung #include<everyone>` applies to all user-facing artefacts: CLI output, docs, HTML, UI, and generated templates.
- WCAG 2.2 Level AA is the default baseline wherever the criteria apply.
- Keep shared guidance synchronized across `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, and `.github/agents/copilot-instructions.md`.

## GitHub/GitLab CLI First / GitHub/GitLab CLI zuerst

Für GitHub-Repositories zuerst die authentifizierte `gh` CLI für mögliche Schreibaktionen und Live-Repository-Operationen verwenden, einschließlich PR-/Issue-Kommentaren, PR-Statusprüfungen, Review-Follow-up, Workflow-Prüfung und Merge-/Statusabfragen. GitHub-Connector-Tools hauptsächlich für strukturierte Read-only-Inspektion oder Fälle nutzen, in denen die CLI nicht geeignet ist.

Für GitLab-Repositories die authentifizierte `glab` CLI zuerst für gleichwertige Aktionen verwenden. Bekanntermaßen fehlschlagende Connector-Schreibwege nicht wiederholt versuchen, wenn `gh`/`glab` die Aufgabe direkt erledigen kann.

For GitHub repositories, use the authenticated `gh` CLI first for feasible write actions and live repository operations, including PR/issue comments, PR status checks, review follow-up, workflow inspection, and merge/status queries. Use GitHub connector tools mainly for structured read-only inspection or when the CLI is not suitable.

For GitLab repositories, use the authenticated `glab` CLI first for equivalent actions. Do not repeatedly try connector write paths that are known to fail when `gh`/`glab` can perform the task directly.

## Skriptreferenz und Quellpfad / Script Reference and Source Path

Die Skriptinventur steht unter `docs/scripts/`. Vor schreibenden Laeufen Hilfe
und Preview verwenden. Die Level-0-Quelle ueber den gemeinsamen Resolver
ermitteln und nicht als absoluten Pfad fest eincodieren.

*The script inventory lives under `docs/scripts/`. Read help and preview before
writing. Resolve Level 0 through the shared contract; do not hard-code it.*

## Dokumentationsauswirkung / Documentation Impact

Jede Änderung erhält genau eine Entscheidung: `UpdateRequired`,
`NoUpdateRequired`, `GeneratedUpdate` oder `FollowUp`. Quelle, Owner,
Dokumente und Evidence richten sich nach `docs/documentation-governance.md`.
`FollowUp` benötigt Owner, Risiko, Frist, Trigger, Evidence und Scope-Grund.

*Every change records exactly one Documentation Impact decision. Follow the
source, ownership, generated-output, and evidence contract in
`docs/documentation-governance.md`.*

## AEPS-Evidence-Rückführung / AEPS Evidence Feedback

Das AOC ist Level-2-Referenzprojekt und Evidence-Quelle für das Agentic
Engineering Preset System (AEPS). Der verbindliche Erfassungs-, Reifegrad-,
Deduplizierungs- und Upstream-Handoff-Vertrag steht in
`docs/aeps/README.md`; das aktuelle Ledger steht in
`docs/aeps/findings-ledger.md`.

Nach jedem formal validierten `Ready`-Single-Review, nach wesentlichen Reviews,
Retrospektiven oder Completion Receipts sowie nach relevanten Fehl- oder
Abbruchläufen MUSS geprüft werden, ob neue Findings, Learnings, Patterns,
Anti-Patterns oder Evidence vorliegen. Das Ergebnis wird im Ledger und in einem
AEPS-Receipt festgehalten; auch `Keine neue AEPS-Evidence` benötigt eine kurze
Begründung. Review-`Ready`, Series-Lifecycle und Ausführungsautorität bleiben
getrennte Achsen.

Level 2 entdeckt, testet und härtet. Level 0 konsolidiert, versioniert und
promotet. AOC-spezifische Details dürfen nicht ungeprüft generalisiert werden;
ein einzelner Lauf erreicht höchstens `pilot-pattern` oder `candidate`.
Upstream-Handoff benötigt stabile veröffentlichte Evidence und aktuelle
GitHub-Schreibautorität. Dieser Vertrag erteilt weder Preset-Promotion noch
Level-0-, Remote-, Merge- oder Bypass-Autorität.

*The AOC is a level-2 AEPS reference and evidence source. Follow the canonical
capture and handoff contract in `docs/aeps/README.md` after every formally
validated Ready review and every material review, retrospective, completion,
failure, or abort trigger. Record either new evidence or a justified no-change
receipt. Ready, lifecycle, and execution authority remain separate. Level 2
discovers and hardens; level 0 consolidates and promotes. Upstream work requires
stable published evidence and current write authority.*

## AOC-weite globale Review-Sperre / AOC-Wide Global Review Gate

Für die kanonische AOC-Programmreihe sind alle nachgelagerten Spec-Kit-Läufe
global und fail-closed gesperrt, bis alle 14 aktiven Lastenhefte `META-LH-01`
bis `META-LH-05` und `RAW-01` bis `RAW-09` jeweils ein aktuelles, formal
validiertes `Ready`-Single-Review besitzen. Zielpfad, normalisierter Zielhash,
Authoring Receipt sowie Bash- und PowerShell-Validierung müssen aktuell sein;
`ReadyWithAcceptedRisks`, supersedierte Ergebnisse und Series-Lifecycle-Werte
genügen nicht. Bis dahin dürfen weder `speckit specify` noch Autonomous,
Parallel Autonomous oder Implementierung gestartet werden.

Nach vollständiger Review-Coverage ist `META-LH-01` zwingend das erste Ziel und
benötigt weiterhin einen neuen ausdrücklichen Startauftrag. Jede Ziel- oder
Evidence-Drift schließt die Sperre erneut. Die zwei älteren Root-Lastenhefte
gehören nicht zu dieser 14er-Programmmenge. Die kanonischen Details stehen in
`requirements/baseline/authority-and-stop-gates.md`.

*All downstream Spec Kit work for the canonical AOC programme is globally and
fail-closed blocked until all 14 active META and RAW intakes have current,
formally validated `Ready` Single reviews with matching target, hash, Authoring
Receipt, and Bash and PowerShell validation. Accepted-risk or superseded
results and lifecycle values do not pass. Once full coverage is current,
`META-LH-01` is the mandatory first target and still requires a new explicit
start instruction. Any drift closes the gate again. The two legacy root
intakes are outside this programme set.*

## Lernreihen-Governance / Learning Series Governance

Neue Lernreihen fuer Fachinformatiker*innen und weitere IT-Ausbildungsberufe werden zuerst in `docs/learning-units/` als Level-0-Quelle vorbereitet. Der `Lernreihen-Blueprint`, das `Lernreihen-Register`, das IT-Berufe-Mapping und die Vorlagen unter `docs/learning-units/templates/` sind verbindlich, bevor eine konkrete Level-1-/Level-2-Struktur gespiegelt wird. KI-Agenten duerfen Lernreihen, Lastenhefte, Berufsbild-Mappings, Reihenfolgen und ZIP-Paketierung vorbereiten, starten aber keine Spec-Kit-Laeufe fuer Lernende ohne ausdruecklichen Auftrag. Spec-Kit-Laeufe sind begleitende SDD-Aufgaben und ersetzen nicht Berufsschule, betriebliche Ausbildung, Rahmenlehrplan, Ausbilderentscheidung oder Pruefungsvorbereitung.

*New learning series for IT specialist apprentices and additional IT training occupations are prepared first in `docs/learning-units/` as the level-0 source. The Learning Series Blueprint, Learning Series Register, IT occupation mapping, and templates under `docs/learning-units/templates/` are binding before a concrete level-1/level-2 structure is mirrored. AI agents may prepare learning series, intake files, occupation mappings, ordering, and ZIP packaging, but must not start learner Spec Kit runs without an explicit instruction. Spec Kit runs are companion SDD tasks and do not replace vocational school, workplace training, the curriculum, instructor decisions, or exam preparation.*

## Spec-Kit-Modell-Routing / Spec Kit Model Routing

- Modellwahl ist operative Agenten-Routing-Guidance, keine Feature-Anforderung. Modellnamen nicht in `spec.md`, `plan.md`, `tasks.md` oder einzelne Feature-Specs schreiben; diese Artefakte muessen reproduzierbar bleiben, auch wenn Modellnamen wechseln oder ein anderer KI-Agent verwendet wird.
- Der jeweilige Agent soll diese Empfehlungen auf seine aktuell verfuegbaren Modelle abbilden; keine feste Anbieter- oder Modellbindung ableiten.
- Fuer Spec-Kit-Spezifikation, Klaerung, Planung, Tasks und Analyse (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; je nach Agent auch `/speckit.specify` usw.) das staerkste verfuegbare Frontier-Reasoning-/Coding-Modell bevorzugen.
- Fuer vollstaendige, lang laufende `/speckit-implement`-Laeufe das staerkste verfuegbare Long-Running-Agent-Modell bevorzugen; das Frontier-Modell nutzen, wenn maximale Urteilsguete wichtiger ist als Laufzeitstabilitaet.
- Fuer fokussierte Reviews oder CI-Fixes ein coding-optimiertes Modell bevorzugen.
- Fuer triviale Bereinigung, Formatierung oder risikoarme mechanische Edits ist ein schnelles kleines Coding-Modell akzeptabel.

*Model choice is operational agent-routing guidance, not a feature requirement. Do not pin model names in `spec.md`, `plan.md`, `tasks.md`, or individual feature specs; those artifacts must stay reproducible even when model names change or another AI agent is used. Each agent should map these recommendations to its currently available models; do not derive a fixed vendor or model requirement. For Spec-Kit specification, clarification, planning, task generation, and analysis (`/speckit-specify`, `/speckit-clarify`, `/speckit-plan`, `/speckit-tasks`, `/speckit-analyze`; or `/speckit.specify` etc. depending on the agent surface), prefer the strongest available frontier reasoning/coding model. For complete long-running `/speckit-implement` runs, prefer the strongest available long-running agent model; use the frontier model when maximum judgment quality is more important than runtime stability. For focused review or CI fixes, prefer a coding-optimized model. For trivial cleanup, formatting, or low-risk mechanical edits, a fast small coding model is acceptable.*

<!-- engineering-retrospective:start -->
## Engineering-Retrospektive je Feature / Engineering retrospective per feature

Ab `003-authoring-contract` erhält jeder aktuelle und zukünftige Feature-Lauf
einen gespeicherten, verständlichen Abschlussbericht nach
`docs/governance/engineering-retrospective.md`, unter
`specs/<feature>/engineering-retrospective.md`. Den Bericht nach jedem Lauf
zusätzlich direkt in der Abschlussantwort anzeigen; ein bloßer Dateilink genügt
nicht. Sechs Perspektiven getrennt behandeln: Output,
Findings, bestätigte Regeln, Interventionen/Reparaturen, Effizienzbeobachtungen
und AEPS-Relevanz. Completion-/Retrospective-Evidence verlinken; Zwischenstände
kennzeichnen und keine nicht erfolgte Lieferung behaupten. Bestehende Evidence
wiederverwenden, wenn ihre Bindung unverändert ist; zusammengehörige Änderungen
bündeln, Providergrenzen früh prüfen und vollständige Matrizen nur bei geänderter
Fläche oder verbindlicher Exact-Head-Regel wiederholen. Pflichtgates bleiben
unverändert. Keine Review-Schleife oder Preset-Promotion allein durch den Bericht
auslösen. Die Regel gilt auch für neu startende Agentensitzungen.

*From `003-authoring-contract` onwards, every current and future feature run
gets a readable, saved closeout report under
`specs/<feature>/engineering-retrospective.md`, following
`docs/governance/engineering-retrospective.md`. Show the report directly in the
final response after every run; a file link alone is insufficient. Keep six
perspectives separate: output, findings, confirmed
rules, interventions/repairs, efficiency observations, and AEPS relevance.
Link completion/retrospective evidence, label interim reports, and never claim
unperformed delivery. Reuse evidence when its binding is unchanged, bundle
related changes, check provider boundaries early, and repeat full matrices only
for a changed surface or a mandatory exact-head rule. Mandatory gates remain
unchanged. The report alone triggers no review loop or preset promotion. This
applies to new agent sessions as well.*
<!-- engineering-retrospective:end -->

<!-- learner-a11y-baseline:start -->
## Hinweise zur Lernenden- und A11Y-Basis / Notes on the Learner and A11Y Baseline

- Inhalte richten sich ab dem ersten Ausbildungsjahr an Fachinformatiker*innen,
  Kaufleute für IT-System-Management und Kaufleute für
  Digitalisierungsmanagement.
- Sie müssen Deutsch zuerst und Englisch danach, ohne Spec-Kit-Vorkenntnisse,
  auf CEFR-B2-Niveau und ohne ausschließlich visuelle
  Abhängigkeitsdarstellung verständlich sein. Fachbegriffe werden beim ersten
  Auftreten erklärt; WCAG 2.2 Level AA ist die anwendbare Prüfbasis.

*Content targets IT specialist apprentices and both IT management occupations
from their first training year. It is German-first/English-second at CEFR B2,
explains technical terms at first use, assumes no prior Spec Kit experience,
never relies on visual-only dependency information, and uses WCAG 2.2 Level AA
as the applicable review baseline.*
<!-- learner-a11y-baseline:end -->

<!-- EN: copilot-instructions.md contains bilingual Copilot guidance for this level-2 project. -->

<!-- BEGIN spec-kit-diagrams-completion -->
## Mermaid und Spec-Kit-Abschlussbericht / Mermaid and Spec Kit completion report

Neue Lastenhefte enthalten bei hilfreichen Abläufen, Zuständen oder Abhängigkeiten
lesbaren Mermaid-Quelltext im Markdown und eine gleichwertige Textalternative.
Bei einfachen Inhalten die Nichtanwendung kurz begründen. Diagramme bilden die
verbindlichen Text-/Manifestquellen ab; Farbe allein trägt keine Bedeutung.
Nach jedem vollständig abgeschlossenen Spec-Kit-Feature-Lauf den vollständigen
Ergebnisbericht im Chat anzeigen und im Feature-Verzeichnis als
`engineering-retrospective.md` versionieren. Einzelne Planungs-/Status-/Review-Kommandos
lösen keinen solchen Bericht aus; blockierte oder pausierte Läufe als
Zwischenbericht kennzeichnen. Vorlage: `.specify/templates/completion-report-template.md`;
Regel: `docs/spec-kit-diagrams-and-completion-reports.md`.
Ergebnis, Tests, Dokumentation, Git-gebundene Umfangszahlen, Verlauf und Restpunkte
belegen. Programmlogik von generierter Evidence, Git-Wandzeit von aktiver
Arbeitszeit und bestandene von ausgefallenen Prüfungen unterscheiden. Finale
Merge-/Sync-Evidence im Chat und bestehenden Closeout-Nachweis ergänzen; keine
zusätzlichen Commits allein für selbstreferenzielle Berichts-/Statistikwerte.
Diese Projektregel und lokale Vorlagen bei Spec-Kit-Updates erhalten.

*New intakes use readable Mermaid Markdown and equivalent text alternatives for
useful workflows, states or dependencies; justify omission for simple content.
Diagrams reflect authoritative text/manifests and never rely on color alone.
After each completed feature run, show the full outcome report in chat and
version engineering-retrospective.md in the feature directory using the shared template
and rule above. Individual planning/status/review commands do not trigger it;
paused/blocked runs receive interim reports. Evidence outcomes, tests, docs,
Git-bound counts, delivery history and remaining work. Distinguish code from
volume generated as evidence, elapsed from active time, and passed from failed
checks. Add final merge/sync proof in chat and existing closeout evidence, without
commits solely for self-referential counts or IDs. Preserve local rules/templates
across Spec Kit updates.*
<!-- END spec-kit-diagrams-completion -->

<!-- project-statistics-rollout:begin -->
## Statistik-Preset und Pflege / Statistics preset and maintenance

Das aktuelle Projektprofil ist `project-statistics-fourteen-governance-presets`:
bestehende 13er-Basis plus Statistik v0.1.0 bei Prioritaet 90. Globale Defaults
bleiben erhalten; die operative lokale Zuordnung folgt erst nach Lieferung.
`docs/project-statistics/config.json` steuert den getrennten UTC-/52-Wochen-Kontext.
Profil 2 bleibt kanonisch; Referenzmodelle im neuen Kontext bleiben aus.
Nach abgeschlossenem Feature/Implementierungsabschnitt Inhalte zuerst committen,
Update ausdruecklich beauftragen und vorab im Dry-Run pruefen. Beide Statistiken
aus derselben Inhaltsrevision pflegen, Ausgaben committen und lesend verifizieren.
Keine Personen-, Lernleistungs-, Qualitaets-, Sicherheits- oder KI-Produktivitaetsbewertung.
Bedienung: `docs/project-statistics/README.md`; Quellen und Abnahme:
`docs/maintenance/project-statistics-rollout-v010.md`. Kein automatischer
Spec-Kit-Lauf und keine Commit-/Push-/Merge- oder menschliche Freigabe durch das Preset.

The current profile adds statistics v0.1.0 at priority 90 to the unchanged
thirteen-preset base. Preserve global defaults and defer operational assignment
until delivery. Keep legacy Profile 2 authoritative; use the separate UTC context
with reference models disabled. After feature/implementation completion, commit
content first, preview an expressly authorized update, render both contexts,
commit outputs and verify read-only status. Statistics do not rate people,
learning, quality, security or AI productivity. See the repository-relative
usage and rollout records. Installation grants no feature or delivery authority.
<!-- project-statistics-rollout:end -->
