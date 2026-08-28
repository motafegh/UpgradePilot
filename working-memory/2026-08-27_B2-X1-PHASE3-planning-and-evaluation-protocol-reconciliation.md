# B2/X1 Phase 3 Planning and Evaluation-Protocol Reconciliation

**Date:** 2026-08-27
**Status:** PLANNING CORRECTION COMPLETE — PHASE 3A NEXT; NO HARNESS, MODEL, OR PRODUCT IMPLEMENTATION AUTHORIZED
**Selected plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
**Live-state owner:** `../MEMORY.md`

## 1. Question and authorization

Ali authorized a pre-build review and any planning/documentation correction needed to make
the next UpgradePilot building slice follow the strongest available plan. The authorized
mutation boundary was planning, live-state, lifecycle, and dated evidence artifacts. It did
not authorize product source, experiment harness, provider/model, or target-repository work.

The bounded question was:

```text
Is the selected B2/X1 Phase-3 plan specific enough to produce a fair,
reproducible, security-aware, and claim-bounded planner comparison before coding begins?
```

## 2. Evidence inspected

The review reconciled:

- the selected B2/X1 plan and the 90-day route;
- `PROJECT_CHARTER.md`, `SECURITY.md`, and the Minimum Useful Generality specification;
- current `MEMORY.md` continuation;
- the completed R7 plan and active-audit lifecycle index;
- Phase-0, Phase-1, and Phase-2 dated records;
- current planner contract/admission experiment source and focused tests;
- current deterministic investigation/orchestration source;
- official OpenAI evaluation, agent-evaluation, function-calling, and agent-safety guidance.

Official guidance used for method calibration:

- <https://developers.openai.com/api/docs/guides/evaluation-best-practices>
- <https://developers.openai.com/api/docs/guides/agent-evals>
- <https://developers.openai.com/api/docs/guides/function-calling>
- <https://developers.openai.com/api/docs/guides/agent-builder-safety>

These sources informed evaluation procedure and risk controls; they do not grant UpgradePilot
product authority or prove this experiment's behavior.

## 3. Findings

### 3.1 Scored-set contamination was not prevented strongly enough

The prior wording froze a case set but still allowed model tuning on that scored set. That
would make the same outcomes both development feedback and final evidence. The plan now
requires distinct development/calibration and protected scored instances, and consumes a
protected instance if its outcome drives a planner, prompt, schema, policy, case, or grading
change.

### 3.2 The disposition rules were under-specified

The prior metrics did not freeze repeat count, aggregation/denominator rules, thresholds,
cost ceiling, critical zero-tolerance failures, or their mapping to `ADOPT`, `RETAIN AS PILOT`,
`REJECT`, or `DEFER`. Those fields now belong to a versioned precommitted protocol that must
be accepted before protected scoring.

### 3.3 Required security pressure had drifted

Phase 0 required a prompt-injection-shaped untrusted-evidence case, but the selected plan
listed that pressure as optional and live memory omitted it. It is now one of six required
case families. Structured output and a closed catalog remain blast-radius controls, not a
claim that prompt injection is solved.

### 3.4 Baseline absence was vulnerable to an inflated win claim

Each instance must now be classified as `comparable`, `coverage_extension`, or
`non_comparable`. A missing deterministic policy may show possible added coverage, but it is
not an automatic planner win.

### 3.5 One action cannot establish general adaptive selection value

The current catalog has one real executable read-only action plus no-tool dispositions. That
is sufficient to evaluate evidence-gap diagnosis and action-vs-stop/defer behavior, but not
general multi-action planning value. General adaptive-planner `ADOPT` therefore requires at
least two independently justified executable actions and protected alternative-selection
evidence. A second action must not be fabricated to satisfy the gate.

### 3.6 Phase 3 mixed design acceptance with implementation

The next slice is now split:

```text
Phase 3A
→ freeze exact instances, oracle, replay identities, baseline classes,
  thresholds, contamination rules, cost ceiling, claim branch, and disposition mapping

Phase 3B
→ only after Phase 3A acceptance, implement the deterministic baseline/replay harness
```

No new experiment code or model/provider call belongs in Phase 3A.

### 3.7 Lifecycle wording needed reconciliation

The accepted R7 plan still labelled itself active, even though `MEMORY.md` and the selected
B2/X1 plan showed the completed handoff. Its status is now explicitly completed/historical.
The eventual post-X1 continuation must be reassessed against current source and plans rather
than mechanically resuming the old Cluster-6 sequence.

## 4. Decisions preserved

The correction does not change these accepted boundaries:

- deterministic code owns evidence acquisition, validation, state transition, and final
  product decisions;
- model output remains untrusted proposed planning data;
- exact repository/revision/path identity is trusted and pre-bound;
- the action catalog remains closed and read-only;
- `stop | defer | unresolved` remain explicit no-tool dispositions;
- no framework, MCP, multi-agent architecture, ADR-0006 change, product integration, or target
  mutation is admitted by this planning slice;
- provider/model selection remains deferred until the evaluation protocol makes comparison
  requirements concrete.

## 5. Proof and limitation

This record proves that the governing plan and live continuation now contain explicit
pre-build evaluation and claim gates. It does not prove that:

- exact case instances or oracle values have been selected correctly;
- thresholds, repeats, aggregation, or cost ceilings have been frozen;
- a second action exists;
- the replay/baseline harness works;
- any model/provider is suitable;
- the planner improves UpgradePilot;
- product adoption is justified.

Those questions remain future evidence responsibilities.

## 6. Exact continuation

Execute Phase 3A as a planning/design and evidence-freeze slice:

1. freeze exact development/calibration and protected instances for all six required families;
2. freeze trusted snapshots, replay identities, expected transitions, acceptable outcomes, and
   forbidden outputs;
3. run the deterministic baseline at equivalent decision points and classify each relationship;
4. select and freeze repeats, aggregation, thresholds, critical gates, cost ceiling, scored-set
   replacement, and disposition mapping;
5. accept either the two-action selection branch or the narrow one-action claim branch;
6. review and accept the complete versioned manifest/oracle design.

Only after that acceptance may Phase 3B implementation begin.
