# Deferred Phase D — D1 supporting note: agenticity, capability, and authority

**Date:** 2026-10-05  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Status:** D1 ownership checkpoint COMPLETE; supporting learning/design evidence.  
**Cycle-status owner:** `working-memory/2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md` remains the sole deferred-D checklist/status record and will be reconciled with this evidence during the next durable cycle-record update.  
**Mutation boundary:** no product/experiment source, tests, active implementation-cycle record, `MEMORY.md`, specification or ADR change.

## D1 question that surfaced

While learning the architecture/responsibility map, Ali challenged the deliberate limitation of LLM capability and authority:

> Why keep the model so bounded if a more versatile or agentic system might investigate the repository/source more effectively? Why not experiment with stronger agent capability and potentially greater authority rather than assuming the deterministic-heavy route is permanently best?

This is a valid architectural challenge, not a contradiction of the current bounded interpreter design.

## Clarified design distinction

The important distinction is:

```text
CAPABILITY
what a model/agent can inspect, retrieve, choose, execute, compare and iterate over

!=

AUTHORITY
what UpgradePilot is justified in accepting as established fact/effect/action from that system
```

The current source-only interpreter is deliberately narrow primarily because it creates a clean, measurable semantic baseline and clear responsibility ownership. That should not be interpreted as a permanent claim that mature UpgradePilot must keep model capability equally narrow.

A low-authority role may later be highly capable. A highly capable agent still does not automatically earn stronger evidence or action authority.

## Relationship to existing project research

The branch already contains a completed AI/agent architecture research program:

- `plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`;
- `proposals/2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md`;
- earlier EvidenceGapPlanner/LangGraph experimental evidence.

That research already preserved the relevant unresolved competitions:

- narrow model projections vs controlled raw-source access;
- fixed investigation vs bounded adaptive planner;
- bounded planner vs generalist agent for long-tail cases;
- binary model authority vs calibrated/selective authority.

The D1 discussion therefore refines an existing architecture competition rather than creating a new unrelated direction.

## Durable refinement recorded from D1

A new branch-local supporting plan now preserves a concrete future experiment:

- `plans/AI_AGENTIC_CAPABILITY_AUTHORITY_LADDER_EXPERIMENT_PLAN.md`

It proposes a comparative ladder:

```text
Level A
bounded source-only interpreter / fixed evidence control

Level B
evidence-constrained read-only investigative agent

Level C
broader agentic impact investigator across upstream/target/adapter evidence

Level D
possible verifier-backed selective authority only if earlier levels earn it
```

The experiment keeps the current API interpretation route intact as a control and compares broader agentic capability on correctness, coverage, unsupported relationships/claims, unresolved handling, provenance/replay, cost/latency, long-tail generalization, robustness/security and maintainer usefulness.

## Key architectural idea

The mature direction worth testing is not:

```text
unrestricted agent
→ trust final answer
```

and not necessarily:

```text
permanently tiny model role
→ deterministic logic for everything else
```

A stronger candidate is:

```text
agentic reasoning / evidence selection
        ↓
provenance-preserving evidence substrate
        ↓
independent grounding / verification / admission
        ↓
conditional proposal and explicit missing premises
```

The agent may become responsible for more discovery/reasoning while exact authority remains proposition-specific and evidence-earned.

## Why the current bounded interpreter should remain unchanged

The bounded interpreter is valuable as a control condition. If tools, target context, iterative search, retries and broader authority are gradually added to the same role, later comparison cannot determine whether improvement came from semantic interpretation, evidence retrieval, agent planning, retries, or evaluation leakage.

Therefore the future agentic experiment should be separate and comparative rather than silently broadening `source-only-api-change-v1` in place.

## D1 ownership evidence

Ali correctly reconstructed the responsibility boundaries across the checkpoint questions:

- deterministic producers establish the HTTPX/source/release evidence and exact source material; the LLM's legitimate role is to propose the semantic interpretation, such as an `app` argument removal, from that supplied evidence;
- a correct upstream interpretation does not establish target impact because target exposure is a separate proposition requiring independent target-side provenance/evidence rather than being inferred from nearby upstream facts;
- the broader API interpreter should be evaluated separately instead of silently broadening the already admitted support-drop role; shared transport/infrastructure does not imply shared semantic authority or that the two responsibilities must later become one component.

Changed-case transfer was also demonstrated. Given a hypothetical agent that correctly discovers HTTPX `app` removal and a target Starlette `TestClient` relationship but lacks evidence for the target's actually resolved Starlette version, Ali rejected the target-impact conclusion. He identified the missing version/exposure evidence and correctly reduced the result to a candidate/conditional relationship pending evidence that connects the target to an affected Starlette version.

One refinement remains part of the recorded understanding: runtime evidence is **not automatically required** for that proposition. The necessary standard is sufficient independent evidence for the exact target/exposure claim. If exact resolved-version and source relationship evidence is enough, runtime proof may be unnecessary; if static/version evidence cannot establish a decision-critical runtime proposition, runtime evidence can become the next needed evidence family.

## D1 assessment

**D1 — COMPLETE at the intended architecture/responsibility ownership depth.**

Established learning evidence:

- whole path understood: acquisition/source evidence → source-only semantic proposal → validation/evaluation → later target-exposure composition;
- experiment-local placement understood as a technology/semantic-admission boundary, not merely a directory choice;
- support-drop infrastructure reuse versus semantic-role separation understood;
- producer/model/evaluator/downstream claim ownership understood;
- reasoning transferred to a changed agentic/Starlette case rather than only repeating the prepared HTTPX example;
- capability and authority are understood as independent axes for future AI/agent experiments.

This closes D1 only. It does **not** establish D2 contract-level ownership, D3 evaluation/coverage/failure ownership, D4 broader changed-case ownership, interpreter implementation, model accuracy, target exposure in the real case, product usefulness or adoption.

**Next deferred-D responsibility: D2 — actual interpretation contract and one real evidence trace.**
