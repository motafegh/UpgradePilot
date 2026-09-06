# UpgradePilot Current Memory

**Last updated:** 2026-09-06  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation and historical design are evidence to inspect, not authority to preserve unchanged.

```text
real responsibility / proof need / material risk / learning value
→ identify the earliest sufficient owner
→ keep or grow mechanisms that add capability or learning value
→ refine redundant ownership/representation
→ avoid both over-engineering and under-engineering
```

Framework learning/comparison is allowed when attached to a real UpgradePilot responsibility. Product adoption remains a separate evidence-backed decision.

---

## Live position

- **Route coordinate:** B2 / X1 — Bounded Product Agentic Investigation Planner and Orchestration Evaluation.
- **Mode:** Learning-by-Doing; LangGraph bounded implementation/evidence/findings are complete enough for handoff.
- **Selected implementation/comparison plan:** `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`.
- **Selected LangGraph plan:** `plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`.
- **Selected learning-depth companion:** `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Naming rule:** semantic/responsibility identity is primary; `B2/X1`, `R4`, `R4-A`, `R4-B`, and similar execution coordinates are secondary route/history metadata rather than durable active source/plan identities.

## Current evidence horizon

### Ordinary-Python control

The bounded ordinary-Python evidence-gap planner remains the real comparison control.

Established evidence:

```text
focused ordinary-Python family
→ 47/47 PASS before semantic rename

real S001
→ ACTION_SELECTED
→ acquire_exact_target_python_declaration
→ deterministic current admission
→ exact pyproject.toml read
→ target requires-python >=3.10
→ applicability unresolved → established_not_applicable
→ budget 1 → 0
→ selected action consumed
→ deterministic replay equivalent
```

The old A1/A2/A3/A4 labels are historical execution coordinates, not current source identity.

### Native LangGraph implementation

Graph API / `StateGraph` remains the tested LangGraph candidate for this experiment. Product adoption is not implied.

Accepted bounded topology:

```text
START → PLAN
PLAN --Command(action)--> AUTHORIZE
PLAN --Command(no-action/problem)--> CONCLUDE
AUTHORIZE --Command(authorized)--> INVESTIGATE
AUTHORIZE --Command(rejected)--> CONCLUDE
INVESTIGATE → CONCLUDE → END
```

Executable evidence:

```text
native graph + ordinary-Python control-adapter focused family
→ 7/7 PASS before semantic rename

post-rename focused semantic family
→ 58/58 PASS

controlled ordinary-Python vs LangGraph semantic comparison
→ 4/4 PASS
```

The controlled comparison covers no-action, fresh-T2 rejection, semantic success, and expected repository operational failure through a framework-neutral semantic projection.

### Real S001 LangGraph proof

Real WSL smoke on `pydantic/pydantic#13432` passed:

```text
model: gemma-4-e4b-it-ud
outcome: semantic_result
observed node path: plan → authorize → investigate → conclude
planner action: acquire_exact_target_python_declaration
authority: authorized
exact target: pydantic/pydantic@aa2dc024d33f61cdef50bf1973ab5adf0a974f5a:pyproject.toml
requires-python: >=3.10
target relevance: outside_declared_python_range
applicability: established_not_applicable
remaining investigations: 0
action consumed: yes
product target result match: True
product final assessment match: True
basic expectation match: True
```

Evidence owner:
`working-memory/2026-09-06_1752_real-s001-langgraph-executable-proof.md`.

Proof limit: one real green S001 does not establish general planner quality, multi-action/multi-agent generality, concurrent durable T2 freshness, persistence/recovery value, product readiness, or framework superiority.

### LangGraph framework value/cost findings

Current evidence supports LangGraph as a **viable serious candidate**, not an adopted winner.

**Currently exercised value:**

```text
explicit executable orchestration topology
runtime node-path observability via updates stream
clear Graph State vs Runtime Context separation
clean routing/effect-stage isolation
useful dependency injection for focused orchestration tests
```

**Current cost:**

```text
substantial graph-owned state/result/port/schema plumbing for one action
LangGraph dependency/API learning + maintenance surface
comparison adapters needed to hold ordinary-Python planner/admission semantics constant
ordinary Python remains locally cheaper for the current small workflow
LangGraph has not replaced the hard product/domain/authority semantics
```

**Important retained conclusion:**

```text
LangGraph should orchestrate established product/domain owners
!=
move product/domain truth into framework-specific nodes/tools
```

The ordinary-Python control still has the stronger currently exercised explicit trace/replay asset. LangGraph persistence/checkpoint/recovery is deferred and must not be implemented merely to improve the framework score.

**Credible but not yet exercised architectural value:** richer branching/composition, durable execution/recovery, HITL/interrupt boundaries, stronger multi-stage observability, subgraph/parallel composition when real product responsibilities later require them.

**Speculative value excluded from decision weight:** generic swarms, automatic parallelism, persistent memory, multi-turn loops, generic tool loops, or HITL without a real admitted responsibility.

Graph API ceremony is now an observed cost, but it has not dominated enough to justify a second Functional API implementation. Keep Graph API as the tested candidate; reopen Functional API only if later comparison cannot judge LangGraph fairly because Graph-API ceremony itself remains the material uncertainty.

Evidence owner:
`working-memory/2026-09-06_1810_langgraph-framework-value-cost-findings.md`.

---

## Current semantic executable owners

### Ordinary-Python evidence-gap control

```text
experiments/evidence_gap_planner_model_boundary.py
experiments/evidence_gap_action_admission.py
experiments/evidence_gap_product_planner_composition.py
experiments/local_evidence_gap_planner.py
experiments/evidence_gap_investigation_transition.py
```

### LangGraph implementation/comparison bridge

```text
experiments/langgraph/evidence_gap_workflow.py
experiments/langgraph/evidence_gap_ordinary_python_control_adapters.py
```

### Framework-neutral comparison

```text
experiments/evidence_gap_implementation_semantic_comparison.py
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

### Real S001 LangGraph smoke

```text
experiments/s001_langgraph_evidence_gap_real_flow_smoke.py
```

Compatibility-only old coordinate-heavy experiment paths remain provenance/re-export surfaces. Do not create new consumers of them.

---

## Live next slice

The LangGraph bounded implementation/comparison/findings route (historical R4-B) is complete enough for the parent-plan handoff.

The next selected responsibility is **R4-C — bounded LangChain learning/integration slice**.

Explore only LangChain abstractions that materially intersect this same bounded EvidenceGapPlanner responsibility after the lower-level LangGraph mechanics are now understood:

```text
model abstraction
create_agent / agent-loop abstraction
tool definitions / tool calling
middleware / lifecycle hooks
retry / fallback / guardrail concepts only where this responsibility makes them real
relationship to the LangGraph runtime
```

The objective is not to build a generic LangChain agent. Determine which, if any, higher-level abstractions reduce meaningful burden while preserving:

```text
bounded model observation
model proposal != execution authority
fresh deterministic pre-effect authority
exact external-effect isolation
semantic/domain result != expected operational/provider failure
existing product/domain ownership
framework-neutral comparison proof
```

Start with proportionate learning/research and responsibility classification before deciding whether a small executable LangChain slice is justified.

Do not force the EvidenceGapPlanner into a generic tool-calling loop merely to exercise LangChain.

---

## Boundaries that remain frozen

- Product/runtime integration of the planner, LangGraph, or LangChain is **not authorized**.
- LangGraph Graph API is experiment architecture, not product adoption.
- Established product/domain capabilities remain truth owners.
- Model output remains proposal/semantic output, never automatic execution authority.
- Sufficiently current deterministic authority is required after model proposal and before external effect.
- Semantic/domain result, expected external/provider failure, and unexpected programmer/framework defect remain distinct.
- The current LangGraph T2 supplier does not claim independent concurrent/durable state freshness.
- Do not implement persistence/HITL/subgraphs/parallelism/multi-turn machinery merely for framework exposure.
- Do not add a second LangGraph Functional API implementation unless the recorded reassessment trigger becomes real.
- Do not adopt/reject LangGraph or LangChain before the later common implementation comparison/disposition.

---

## Current detailed evidence / provenance

- `working-memory/2026-09-06_1810_langgraph-framework-value-cost-findings.md`
- `working-memory/2026-09-06_1752_real-s001-langgraph-executable-proof.md`
- `working-memory/2026-09-06_1652_real-s001-langgraph-smoke.md`
- `working-memory/2026-09-06_semantic-naming-main-reconciliation-and-merge.md`
- `working-memory/2026-09-06_B2-X1-R4B-first-wsl-executable-proof.md`
- `working-memory/2026-09-06_B2-X1-R4B6-controlled-semantic-comparison-build.md`
- `working-memory/2026-09-04_2017_B2-X1-R4B-r4a-representation-coupling-correction.md`
- `working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
