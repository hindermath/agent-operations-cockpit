# Planprüfungs-Checkliste / Plan Review Checklist

**Datum / Date:** 2026-09-13. **Reviewer:** unabhängige Runner-Phase `plan-review`; nicht der vorherige Planer. / Independent runner phase, separate from the preceding planner.

Diese Liste prüft die korrigierte Planung. Sie behauptet keine Implementierung. / *This checklist assesses corrected planning, not implementation.*

- [x] Binding Intake, Spec, beide Anforderungschecklisten und alle Designverträge vollständig verglichen; unveränderter Scope. / Compared binding intake, spec, both requirement checklists and every design contract; unchanged scope.
- [x] Genau neun Kriterien und sechs Modi; optionale Parallelflags schränken andere Modi nicht ein. / Exactly nine criteria and six modes; optional parallel flags do not constrain other modes.
- [x] Drei behauptete Defekte in Bash und PowerShell erneut reproduziert; 17 Eingangsgates/Baseline-Prüfungen bestanden. / Three defects reproduced through both shells; seventeen input/baseline checks passed.
- [x] Kleinste sichere additive Grenze erhält gebundene Quellen und Graphlogik; transitive Reads und Symlinks sind ausdrücklich erfasst. / Minimal additive boundary preserves bound sources and graph logic and explicitly covers nested reads/symlinks.
- [x] Status/Next bleiben read-only; Lifecycle, Review, Eligibility, Delivery und Authority sind getrennt; mehrere Blocker erhalten stabile Reihenfolge. / Queries remain read-only with separate axes and stable blocker order.
- [x] Ein fachliches Red nach vollständiger Oberfläche; gleicher Test und enge Reparatur; historisches Red bleibt getrennt vom späteren HEAD. / One semantic red after surface readiness, same test and narrow fix; historical red stays distinct from later head.
- [x] Native sechs Shell-/OS-Kombinationen, Bash-Major-Version, Kindprozess-PATH, Help/Manpage/Advanced Function sind geplant. / Six native combinations, version, child PATH and help surfaces are planned.
- [x] Alle Gate-Tokens sind dokumentiert; 54 eindeutige Gates, davon 41 Applicable; Schema-Positiv- und Token-Negativproben bestanden. / Every token is documented; 54 unique gates, 41 applicable; schema and missing-token probes passed.
- [x] Security/MSL/Supply Chain, Architektur, A11Y einschließlich didaktischer Kommentare und Agentenparität haben konkrete Nachweise oder begründetes N/A. / Cross-cutting duties have concrete evidence plans or justified N/A.
- [x] Eine Documentation-Impact-Entscheidung `UpdateRequired`; Statistik erst beim vorgesehenen Abschluss; AEPS-Handoff mit Owner und Trigger. / One documentation decision; statistics at closeout; owned AEPS handoff.
- [x] Keine selbstreferenziellen Hashes oder vorweggenommenen Merge-Fakten; spätere Feature-Gates sind keine bereits bestandenen Review-Gates. / No circular hashes or anticipated merge facts; later feature gates are not claimed as review passes.
- [x] Zweiter vollständiger Review-Durchgang: null offene Critical/High und null undispositioned Medium; Änderungen bleiben im autorisierten Bereich. / Full second pass: no open critical/high or undispositioned medium findings; changes stay in scope.

Die [Review-Evidence](../phase-results/plan-review-report.md) benennt Findings, Reparaturen, Tests und Grenzen. / *The review report names findings, repairs, checks and limits.*

## Aktueller Geltungsstand / Current applicability

Die oben abgehakten Positionen sind der historische Plan-Review-Snapshot vor Analyze. C001–C004, I001–I002, O001 und L001 aus `phase-results/analyze-report.md` haben spätere Korrekturen ausgelöst; aktuelle Disposition und Hashbindungen stehen in [analysis-remediation.md](analysis-remediation.md). Diese Liste ersetzt weder den erneuten Analyze-Pass noch Feature-Gates. / *The checked items above preserve the historical pre-Analyze review. The eight later findings triggered corrections recorded in the current remediation checklist and evidence; this historical list replaces neither renewed Analyze nor feature gates.*
