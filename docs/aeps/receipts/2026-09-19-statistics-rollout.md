# AEPS-Receipt: Statistik-Rollout / Statistics rollout

Datum / Date: 2026-09-19. Owner: AOC Repository Owner.
Status: `PendingPublication`; Base-HEAD `e463963e048a4b0508dcba1a5c31fceed6b0f7f2`.
Quelle: [Rollout-Vertrag](../../maintenance/project-statistics-rollout-v010.md),
SHA-256 `0ee69bbca156685598370fffe7ffd1a6d31f8254b0405e5a160e20ee22fb3739`.
Deduplizierung: Quellpfad + Hash + Datum. Trigger: technische Integrationspruefung.

**Keine neue AEPS-Evidence / No new AEPS evidence.** Der genehmigte Rollout
verwendet das bereits stabile Statistik-Preset und die vorhandene gestufte
Lieferung. Die Trennung von Inhaltscommit und Messung bestaetigt den bereits
erfassten Quellschutz (AEPS-FIND-AOC-007) und die Statistik-Reihenfolge; keine
neue generalisierbare Regel. Der erste Init-Schreibversuch blockierte korrekt
bei zwischenzeitlich hinzugefuegten Integrationsdateien (Exit 2, kein Config-Write).
Fortsetzung erst nach Inhaltscommit; keine Lockerung der Clean-Tree-Grenze.
Die Installation bewahrt 13 Presets. Vollstaendige native Ergebnisse folgen
im PR; hier wird keine vorweggenommene Abnahme behauptet.

The rollout reuses a stable preset and the established source-before-measurement
sequence. An init attempt correctly rejected a dirty tree (exit 2, no config
write); continue only after committing content. No clean-tree bypass. Installation
preserves existing presets. Native results are separate PR evidence, not predicted
acceptance. No new transferable rule, finding ID or maturity increase.

Historische Findings und Negativevidence bleiben erhalten. Matrix, Gap-Analyse
und Handoff haben keine neue Disposition. Kein Upstream-Handoff oder Promotion;
naechste Validierung: exakte native CI und menschliche Sichtung dieses Rollouts.
Documentation Impact bleibt `UpdateRequired` des Rollout-Vertrags.

Preserve historical evidence and derived dispositions. No promotion or upstream
action; next validate exact-head CI and human review. Retain the rollout's sole
documentation decision.
