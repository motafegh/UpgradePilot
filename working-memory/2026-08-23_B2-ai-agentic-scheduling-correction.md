# Working Memory — B2 AI / Agentic Scheduling Correction

**Date:** 2026-08-23  
**Status:** RECORDED — supersedes the earlier indefinite-defer lifecycle conclusion; does not activate product-agent implementation before R7  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Related review:** `2026-08-23_B2-reconciliation-agentic-compatibility-pressure-review.md`

## Trigger

After reviewing the earlier AI/LLM and agentic work, the initial compatibility review concluded that the agentic evaluation should remain deferred while R1–R7 reconciles deterministic contracts.

Ali challenged the **deferred** lifecycle framing. The important observation is historical/project-process pressure:

```text
important AI / LLM responsibility
→ deferred behind deterministic prerequisites
→ project continues implementing new deterministic work
→ original AI checkpoint can repeatedly slip
```

The technical reason not to implement the agent during moving R1–R7 contracts remains sound. What was insufficient was leaving the responsibility without a guaranteed re-entry point.

## Corrected lifecycle distinction

The project now distinguishes:

```text
DEFERRED
→ valid question/opportunity
→ no committed near-term activation point

SCHEDULED
→ explicitly selected responsibility
→ concrete prerequisite / trigger
→ named owning plan
→ non-skippable route handoff when trigger is met
```

AUDIT-005 is therefore **SCHEDULED**, not deferred.

## Exact route placement

```text
CURRENT
R1 → R2 → R3 → R4 → R5 → R6 → R7

R7 acceptance requires:
- reconciled deterministic contracts
- focused + nearest integration + full deterministic validation
- exact accepted baseline revision/result
- current orchestration behavior frozen for comparison

THEN — mandatory next B2/X1 checkpoint
B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md

Phase 0
→ refreshed AI/LLM engineering + route/baseline reassessment
→ re-check ADR-0006 and current AI roles
→ explicit PROCEED / REJECT / DEFER-RESCHEDULE

if proceed:
Phase 1 capability/orchestration inventory
→ Phase 2 planner state/action/result contracts
→ Phase 3 deterministic baseline/replay harness
→ Phase 4 bounded model-planning pilot
→ Phase 5 failure diagnosis + baseline comparison
→ Phase 6 ADOPT / RETAIN AS PILOT / REJECT / DEFER
→ Phase 7 only if adopted: bounded normal-path integration

ONLY AFTER CHECKPOINT DISPOSITION
→ MEMORY.md selects Cluster 6 or another ordinary B2 continuation
```

## Why after R7, not now

Starting the agentic implementation before R7 would measure/build against contracts that are intentionally changing and could force immediate rework.

Waiting until an unspecified later date recreates the historical skip risk.

Therefore the smallest defensible sequencing is:

```text
finish the currently necessary deterministic reconciliation
→ freeze its accepted baseline
→ immediately run the already-admitted AI/agentic method checkpoint
```

## Freshness requirement

The agentic plan's Phase 0 now requires a fresh AI/LLM engineering reassessment at activation time. It must not assume that the model/provider/tool-calling/structured-output/agent-evaluation landscape from 2026-08-21 is still current.

Review current authoritative/recent evidence only where material to the bounded planner responsibility:

- structured output / tool calling;
- planner/agent evaluation methods and known failure modes;
- prompt-injection and tool-authority controls;
- plausible local/remote planning models under privacy/cost constraints;
- whether an orchestration framework solves an observed problem versus an ordinary Python loop;
- ADR-0006 reassessment triggers and existing local semantic-extractor deployment assumptions.

This freshness pass is evaluation input, not permission to adopt fashionable infrastructure.

## Durable repository changes

The correction is now represented through:

```text
plans/UPGRADEPILOT_90_DAY_PLAN.md
→ scheduled X1 checkpoints cannot be silently bypassed

plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md
→ R7 is the explicit prerequisite and mandatory AI handoff

plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
→ APPROVED + SCHEDULED; Phase 0 refreshed AI-engineering gate

audits/scheduled/README.md + audit lifecycle docs
→ AUDIT-005 classified as scheduled

MEMORY.md
→ records mandatory post-R7 checkpoint before ordinary B2 continuation
```

## Effect on current R1 work

No Step-2B technical conclusion is reversed.

Current execution remains:

```text
R1 Step 2B responsibility trace COMPLETE
→ Step 2B code migration NEXT
→ Step 2C
→ R2 ... R7
→ scheduled AI/agentic X1 checkpoint
```

Current R1 decisions should continue to receive agentic-compatibility pressure, but speculative agent abstractions remain prohibited before the scheduled checkpoint.
