---
name: speckit-parallel-autonomous-consolidate
description: Inspect parallel results; production consolidation is suspended.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: preset:parallel-autonomous-run-governance
---

# Speckit Parallel Autonomous Consolidate Skill

*DE: Produktive Parallel-Kampagnen sind bis zu einer isolierten Worker-Laufzeit
gesperrt. `Start`, `Resume` und `Consolidate` duerfen weder ueber den
Koordinator noch direkt durch Agenten ausgefuehrt werden. Erlaubt bleiben
`Validate`, `Status` und `Stop` ueber den Koordinator. Die folgenden Schritte
sind derzeit inaktiv.*

*EN: Production parallel campaigns are suspended until workers have an
isolated runtime. Agents must not run `Start`, `Resume` or `Consolidate`,
including by scheduling workers or merging directly. Only coordinator
`Validate`, `Status` and `Stop` remain available. The steps below are dormant.*

For `AlternativeSolutions`, require a named human-selected worker and reject
automatic scoring or merging of several candidates.

For `MergeAndSync`, require every eligible worker to be `ReadyForMerge` with an
exact reviewed head, passing required checks, no actionable review thread, and
current explicit merge authority. Cross the all-ready barrier before the first
merge. Use a provider-bound preflight contract for open/not-draft state, exact
head, mergeability, current change requests and threads, and check policy.
Revalidate all remaining direct or stacked PR bases after every merge.

Checkpoint every verified merge. On resume, skip verified merged workers and
adopt an externally merged exact head. Drift becomes `NeedsRevalidation`.
Honor cooperative stop between operations. Execute only manifest-declared,
idempotent post-merge actions. Set `Completed` only after merge,
synchronization, post-merge work, and final validation all succeed. Never
claim cross-repository atomicity.

*DE: Teilmerges sind fortsetzbar. Worker-Handoffs duerfen keine
Post-Merge-Kommandos definieren.*
