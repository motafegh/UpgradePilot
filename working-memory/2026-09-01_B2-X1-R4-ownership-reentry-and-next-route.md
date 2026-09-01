# B2/X1 R4 — Ownership Re-entry, Architecture Learning, and Refined Continuation

**Date:** 2026-09-01  
**Mode:** Learning-by-Doing / Building  
**Scope:** R4 ordinary-Python `EvidenceGapPlanner` seam, ownership re-entry, real-flow continuation, and newly surfaced proposition/persistence architecture questions  
**Live-state owner:** `../MEMORY.md`  
**Primary plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Prior checkpoint:** `2026-08-31_B2-X1-R4A3-mocked-proof-and-ownership-reentry.md`

## 1. Starting goal and route

We resumed from the recorded R4 ownership/learning re-entry after the focused A1+A2+A3 mocked proof was green (36/36) but before live LM Studio inference.

Starting route:

```text
A1 planner/context boundary
→ A3 local provider/model boundary
→ A2 deterministic admission boundary
→ ownership closure
→ real-product-output composition into EvidenceGapPlannerContext
→ focused composition proof
→ live A3 LM Studio smoke
→ A3 closure
→ decide/continue into A4
```

The live smoke remains intentionally blocked until the ordinary-Python responsibility is understood and the live request is composed from real UpgradePilot product outputs rather than hand-reconstructed S001 facts.

## 2. What we reviewed and learned

### A1 / A3 / A2 responsibility split

Current source separation is deliberate:

```text
experiments/b2_x1_evidence_gap_planner.py
→ A1: model-visible context, projection, decision contract/parser

experiments/b2_x1_evidence_gap_model.py
→ A3: LM Studio/OpenAI-compatible request-response boundary

experiments/b2_x1_evidence_gap_admission.py
→ A2: trusted action rebinding and fresh deterministic admission
```

Core trust flow:

```text
trusted UpgradePilot state
→ A1 bounded observation
→ A3 untrusted model decision
→ A2 current trusted admission
```

A3 invocation validity, A2 authorization freshness, and model semantic quality are separate responsibilities.

### Bounded planner context

`EvidenceGapPlannerContext` is the bounded model observation. It contains only the approved planning state needed for one turn:

```text
planning_question
dependency_transition
propositions
planning_evidence
consumed_actions
planning_budget
allowed_actions
```

The model should not receive raw repository/source authority, exact revision/path bindings, full raw evidence, mutation policy, result-family authority, or evaluator/oracle metadata by default.

Real cases S001, S003, S004, and S005 were used to understand how the same context shape can represent different planning situations without making every case use the same proposition set.

### Proposition ownership

Important corrected mental model:

```text
raw/acquired evidence
→ owning UpgradePilot domain interpretation
→ PropositionAssessment state
→ A1 selects/projects relevant proposition state
→ planner reasons over it
```

The planner does not establish proposition truth. A1 does not establish proposition truth either.

Current S001 product flow already produces typed proposition state through the Python-support impact path. Some proposition semantics may originate from model-assisted extraction, but later planner use receives already-grounded/accepted product semantic state rather than raw upstream prose.

Different cases may instantiate different propositions, but the future goal should not be handcrafting an unrelated proposition vocabulary per case.

## 3. Architecture questions surfaced during learning

### Current S001 specialization versus general seam

The overall A1/A3 architecture is generic, and A2 admission mechanics are generic, but the first concrete real action is intentionally S001-shaped (`acquire_exact_target_python_declaration`, `pyproject.toml`, target-Python proposition/result contract).

Therefore the current seam is best understood as:

```text
generic planner/admission architecture
+ first narrow real S001 vertical slice
```

not a fully generalized multi-case proposition/action system yet.

### Generalized proposition-generation direction

A promising future shape is capability/domain-owned proposition production rather than one giant universal generator:

```text
product evidence/results
→ specialized domain owners/producers
→ PropositionAssessment records
→ current investigation state
→ question-specific proposition/evidence selection
→ EvidenceGapPlannerContext
```

Possible domains include Python support, CI consumption/coverage, failure attribution, upstream behavior/activation conditions, dependency/lock semantics, and later responsibilities only when actually implemented.

The composition layer should select relevant propositions for the current planning question; it should not become a second owner of proposition truth.

### Persistence / database tension

Current product runtime mainly builds and returns typed in-memory state (`PublicPullRequestInvestigation`). Product runtime does not yet have a durable investigation-state database.

The repository does persist experiment/evaluation evidence in JSON and historical product-simulation artifacts, so the absence is specifically a product-runtime persistence decision/state, not a total absence of persisted evidence.

Durable state may become materially useful for:

```text
resume/restart
consumed-action history
budget/state transitions
proposition evolution
audit/replay
model-decision trace
avoiding unnecessary reacquisition
multi-turn investigation
```

This becomes especially relevant around A4, which introduces transition/update/trace/replay responsibility.

### Dataset/table mental model

A wide CSV-style case table is a useful analysis/export mental model, but likely not the best sole operational schema as proposition/evidence types grow.

A more scalable relational shape could separate:

```text
cases / investigations
propositions
evidence records
proposition-evidence relationships
actions / consumed actions
planner decisions
admission results
```

Wide CSV/DataFrame exports can still be generated for analysis/evaluation/ML-style comparison.

Important context-selection rule:

```text
stored/non-null
!= automatically model-visible
```

Storage answers what state exists. Proposition generation answers what that state establishes/refutes/leaves unresolved. Context selection answers which propositions/evidence matter for this exact planning question.

## 4. Refined continuation for this session

### Step 1 — close A1 → A3 → A2 ownership re-entry

Confirm the minimum-complete end-to-end model is clear enough to proceed:

```text
real trusted state
→ bounded context
→ local structured-output model call
→ untrusted EvidenceGapDecision
→ fresh trusted rebinding/admission
```

Do not require memorization of incidental syntax or every constructor invariant.

### Step 2 — real-flow composition seam

Build the smallest experiment-owned adapter from actual `investigate_public_pull_request(...)` outputs into `EvidenceGapPlannerContext`.

Requirements:

```text
reuse product-owned dependency transition
reuse product-owned proposition state
reuse product-owned CI/reachability semantics where supplied
project only approved planner-visible semantics
preserve hidden exact action/source authority
avoid re-parsing/re-normalizing/re-establishing product truth in experiments
```

### Step 3 — focused proof

Prove that the adapter:

```text
real product outputs
→ correct bounded planner values
→ no product semantic duplication
→ hidden authority remains hidden
```

### Step 4 — live A3 LM Studio smoke

Only after Steps 1–3:

```text
real product flow
→ composition seam
→ A1 context
→ A3 live local model call
→ inspect actual provider/model evidence
```

Then close the A3 Learning-by-Doing slice based on actual evidence.

### Step 5 — A4 design/implementation entry

Before or at the start of A4, explicitly revisit two newly surfaced architecture responsibilities:

1. reusable/domain-owned proposition production across different investigation responsibilities;
2. what investigation state should become durable/persistent and why.

Do not implement a database, generic rule engine, knowledge graph, or generalized persistence framework merely because it is attractive. Design/adopt only the minimum structure justified by the A4 state-transition/replay responsibility and real evidence.

Then continue A4:

```text
no-tool OR admitted action
→ execution/result
→ domain interpretation/state update
→ consumed-action/budget update
→ deterministic trace/replay
→ optional next planner turn when justified
```

Later framework comparison remains:

```text
ordinary Python coherent baseline
→ LangGraph comparison/LbD
→ bounded LangChain slice
→ evidence-backed comparison/disposition
```

## 5. Step 1 ownership closure — COMPLETE

Ali reconstructed the core responsibility correctly:

```text
A1
→ receives already-established trusted product/domain state
→ validates planner-boundary coherence and projects the bounded model-visible context
→ does not establish evidence/proposition truth

A3
→ receives the A1 context
→ constructs the bounded LM Studio request, performs the provider/model call, validates/parses the returned structured decision
→ does not authorize execution or judge current action freshness

A2
→ receives a valid selected-action decision plus fresh trusted admission state
→ rebinds the action ID and re-checks current consumed/budget/identity/policy/proposition preconditions
→ does not validate the model JSON/wire shape and does not let the model redefine executable authority
```

The initial explanation correctly identified the A1 → A3 → A2 flow; the two ownership corrections above were made explicitly. This is sufficient ownership for the next material step without requiring source memorization.

## 6. Step 2 real-product composition seam — IMPLEMENTED / INSPECTED; RUNTIME PROOF PENDING

Added:

```text
experiments/b2_x1_evidence_gap_composition.py
experiments/tests/test_b2_x1_evidence_gap_composition.py
```

Implemented responsibility:

```text
PublicPullRequestInvestigation
→ require the current pre-target Python-support product state
→ reuse DependencyVersionChange
→ reuse the product-owned Python-support PropositionAssessment records
→ mechanically project supported product-owned CI consumption records
→ reuse the current deterministic Python-support investigation selection
→ rebind/project only the smaller A1 action descriptor
→ combine caller-owned planning question / consumed history / budget
→ EvidenceGapPlannerContext
```

Important decisions/evidence:

- the adapter is responsibility-specific (`pre_target_python_support`), not hardcoded to S001 repository/PR identity;
- current product truth is reused rather than re-parsed or re-derived;
- the actual current pre-acquisition proposition set is the three product-owned keys from `python_support.py`, not the larger historical R2 representative list;
- existing S001 verification explicitly preserves every supported real CI consumption rather than discarding additional matches through an arbitrary first-match policy, so the adapter projects every supported product-owned consumption;
- unresolved/non-supported consumption records are not promoted to supported planner evidence;
- exact repository/revision/action path, workflow/source paths, commands, lockfile paths, and raw evidence remain excluded from the A1 request projection;
- pre-call action projection removes the current action when it is already consumed or the semantic investigation budget is zero; A2 still retains fresh defense-in-depth checks after model reasoning;
- a cross-layer coherence guard rejects a product investigation selection if its kind/path/target proposition no longer matches the existing exact A2 action contract.

Focused test intent:

```text
actual UpgradePilot domain/result types
→ product transition/proposition reuse
→ preserve all supported CI consumptions
→ hidden source/action authority absent from rendered request
→ consumed/zero-budget action not offered
→ selector/action contract drift rejected
```

Proof limit: source and test inspection is complete, but the tests have not yet been executed in the normal local UpgradePilot environment. They also do not by themselves prove the live `investigate_public_pull_request(...)` S001 path reaches the adapter correctly; that is the stronger Step-3 real-flow proof.

Commits:

```text
500a9c0f4632168cb57f9ae4a89be0b0c06056d9 — composition source
33af5e3d43812ab7d121ecceacba1c96a43c1a4c — focused composition tests
```

## 7. Session checkpoint policy

This file is the dated session record. Add only material completed steps, evidence, design corrections, and continuation-relevant learning from this session. `MEMORY.md` should be updated only when the live continuation/blocker/selected route materially changes.

**Current checkpoint:** Step 1 complete; Step 2 implemented and inspected with local runtime proof pending. Next is Step 3 — run/prove the focused composition tests and add the smallest real S001 normal-product-flow composition probe before any live LM Studio call.

**Procedure provenance:** `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-build-implement`
