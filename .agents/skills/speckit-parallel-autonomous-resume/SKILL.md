---
name: speckit-parallel-autonomous-resume
description: Inspect a paused parallel campaign; production resume is suspended.
compatibility: Requires spec-kit project structure with .specify/ directory
metadata:
  author: github-spec-kit
  source: preset:parallel-autonomous-run-governance
---

# Speckit Parallel Autonomous Resume Skill

*DE: Produktive Parallel-Kampagnen sind bis zu einer isolierten Worker-Laufzeit
gesperrt. `Start`, `Resume` und `Consolidate` duerfen weder ueber den
Koordinator noch direkt durch Agenten ausgefuehrt werden. Erlaubt bleiben
`Validate`, `Status` und `Stop` ueber den Koordinator. Die folgenden Schritte
sind derzeit inaktiv.*

*EN: Production parallel campaigns are suspended until workers have an
isolated runtime. Agents must not run `Start`, `Resume` or `Consolidate`,
including by scheduling workers or merging directly. Only coordinator
`Validate`, `Status` and `Stop` remain available. The steps below are dormant.*

Revalidate campaign manifest hash, repositories, worktrees, branches, current
authority, runner profile, worker result contracts, autonomous states,
completed handoffs, and the last trustworthy operation. Reuse verified
completed work. Retry only an unproven or incomplete operation. Reconcile
current mandatory governance deltas before scheduling.

For fail-closed routing, revalidate the campaign or worker role, exact profile
match, declared model, reasoning effort, executable, and read-only preflight.
Profile drift or preflight failure blocks new scheduling without fallback.

For schema `1.2` with required intake review, revalidate the stored result
hash, every worker input hash and applicability row, series relations, and
non-expired operator exceptions. Drift blocks new scheduling.

For consolidation, revalidate every PR against the exact expected head. Skip a
verified `Merged` worker, adopt an externally merged exact head, and classify
any drift as `NeedsRevalidation`. Retry only failed idempotent post-merge
actions from the reviewed manifest.

*DE: Bereits verifizierte Merges nicht wiederholen. Extern gemergte exakte
Heads duerfen uebernommen werden; Drift bleibt blockierend.*
