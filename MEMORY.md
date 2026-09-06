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
- **Mode:** Learning-by-Doing + Build/Implement, with the real S001 LangGraph smoke now complete.
- **Selected implementation/comparison plan:** `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`.
- **Selected LangGraph plan:** `plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`.
- **Selected learning-depth companion:** `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Naming migration plan:** `plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md`.
- **Naming rule:** semantic/responsibility identity is primary; `B2/X1`, `R4`, `R4-A`, `R4-B`, and similar execution coordinates are secondary route/history metadata rather than durable active source/plan identities.

## Current evidence horizon

### Ordinary-Python control

The bounded ordinary-Python evidence-gap planner remains the real comparison control.

Established evidence includes:

```text
model boundary + deterministic admission + local model seam + product composition + transition
→ focused ordinary-Python family 47/47 PASS before semantic rename

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

Graph API / `StateGraph` remains the selected first LangGraph implementation paradigm for this experiment. Product adoption is not implied.

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

- native graph + ordinary-Python control-adapter focused family: **7/7 PASS** before semantic rename;
- post-rename focused semantic family including the graph/adapters: **58/58 PASS**.

### Controlled ordinary-Python vs LangGraph comparison

Framework-neutral semantic comparison established **4/4 PASS** for:

1. no-action with no external effect;
2. fresh T2 consumed-action rejection;
3. authorized semantic success;
4. expected repository operational failure.

The post-rename **58/58 PASS** also re-executed the renamed comparison path successfully.

This establishes bounded behavior-equivalence evidence for the exercised cases. It does **not** establish broad planner quality, product reliability, or LangGraph superiority/adoption.

### Real S001 LangGraph executable proof

On 2026-09-06 Ali ran the real S001 LangGraph smoke in the normal WSL `.venv` using process-local public-proof isolation for ambient GitHub credentials/proxies.

Observed result:

```text
case: pydantic/pydantic#13432
model: gemma-4-e4b-it-ud
outcome: semantic_result
graph_elapsed_seconds: 6.726
observed_node_path: ['plan', 'authorize', 'investigate', 'conclude']
planner_action_id: acquire_exact_target_python_declaration
authority_status: authorized
authority_repository: pydantic/pydantic
authority_revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
authority_path: pyproject.toml
investigation_state: available
requires_python: >=3.10
target_relevance_state: outside_declared_python_range
applicability_state: established_not_applicable
remaining_investigations: 0
consumed_actions: ('acquire_exact_target_python_declaration',)
product_target_result_match: True
product_final_assessment_match: True
expected_node_path_match: True
basic_expectation_match: True
```

This directly establishes for one real S001 run that:

```text
real PublicPullRequestInvestigation
→ real local planner/model proposal
→ separate deterministic authority
→ exact immutable GitHub target read
→ target declaration interpretation
→ deterministic graph conclusion
→ graph target/final semantic result matches normal product path
```

The graph `updates` stream also exposed the expected runtime path `plan → authorize → investigate → conclude` without adding persistence/checkpoint/HITL machinery.

Evidence owner:
`working-memory/2026-09-06_1752_real-s001-langgraph-executable-proof.md`.

Proof limit: one real green S001 does not establish general planner quality, multi-action/multi-agent generality, concurrent durable T2 freshness, persistence/recovery value, product readiness, or framework superiority.

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

Active semantic adapter identities:

```text
OrdinaryPythonEvidenceGapPlanner
OrdinaryPythonEvidenceGapPlannerAdapter
OrdinaryPythonEvidenceGapAuthorityAdapter
```

### Framework-neutral comparison projection

```text
experiments/evidence_gap_implementation_semantic_comparison.py
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

### Real S001 LangGraph smoke

```text
experiments/s001_langgraph_evidence_gap_real_flow_smoke.py
```

### Focused active tests

```text
experiments/tests/test_evidence_gap_planner_model_boundary.py
experiments/tests/test_evidence_gap_action_admission.py
experiments/tests/test_evidence_gap_product_planner_composition.py
experiments/tests/test_local_evidence_gap_planner.py
experiments/tests/test_evidence_gap_investigation_transition.py
experiments/tests/test_langgraph_evidence_gap_ordinary_python_control_adapters.py
experiments/tests/test_langgraph_evidence_gap_workflow.py
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

### Compatibility-only paths

Old `experiments/b2_x1_evidence_gap_*` modules and `experiments/langgraph/r4a_control_adapters.py` are compatibility/provenance surfaces only. Do not create new consumers of them.

---

## Naming migration status

The semantic naming migration is merged and executable proof is closed:

```text
8 migrated focused semantic test modules
→ 58/58 PASS
```

No additional naming cleanup is required before continuing the experiment route. Historical working-memory/proposal/probe filenames remain unchanged as provenance.

Detailed merge/proof evidence:
`working-memory/2026-09-06_semantic-naming-main-reconciliation-and-merge.md`.

---

## Live next slice

The bounded real S001 LangGraph smoke (historical R4-B7) is complete and green.

The next selected responsibility is **LangGraph framework value/cost findings for the later implementation comparison/disposition** (historical R4-B8 → R4-D handoff).

Evaluate the strongest current LangGraph implementation against the ordinary-Python control under dimensions already owned by the selected LangGraph plan, including:

```text
responsibility / topology clarity
workflow-state and routing clarity
authority/trust clarity
failure-model clarity
external-effect isolation
testability and semantic proof ergonomics
runtime observability/debuggability
boilerplate/state plumbing
dependency/framework cost
learning/maintenance burden
change locality
credible future orchestration fit
```

Distinguish explicitly:

```text
CURRENTLY EXERCISED VALUE
→ demonstrated by source/tests/real S001 runtime

CREDIBLE ARCHITECTURAL VALUE
→ relevant to UpgradePilot's intended trajectory but not yet exercised

SPECULATIVE VALUE
→ imagined framework benefits without a concrete responsibility/evidence path
```

Do not treat framework capability lists as adoption proof. Do not implement additional persistence/HITL/subgraph/parallel/multi-turn machinery merely to improve the score.

---

## Boundaries that remain frozen

- Product/runtime integration of the planner or LangGraph is **not authorized**.
- Graph API selection is experiment architecture, not product adoption.
- Established product/domain capabilities remain truth owners; experiment isolation does not authorize duplicate product semantics.
- Model output remains proposal/semantic output, never automatic execution authority.
- Sufficiently current deterministic authority is required after a model proposal and before external effect.
- Semantic/domain result, expected external/provider failure, and unexpected programmer/framework defect remain distinct.
- The current T2 supplier does not claim independent concurrent/durable state freshness.
- Do not implement persistence/HITL/subgraphs/parallelism/multi-turn machinery merely for framework exposure.
- Functional API remains a reassessment fallback only if actual Graph API evidence makes ceremony/state plumbing a material confounder.

---

## Current governance addition retained from main

The accepted workstream-supervision Skill and its supporting governance/evaluation surfaces remain separate from the B2/X1 experiment route:

```text
.agents/skills/upgradepilot-workstream-supervision/SKILL.md
plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md
tools/agent-governance/workstream_supervision_cases.json
```

---

## Current detailed evidence / provenance

- `working-memory/2026-09-06_1752_real-s001-langgraph-executable-proof.md`
- `working-memory/2026-09-06_1652_real-s001-langgraph-smoke.md`
- `working-memory/2026-09-06_semantic-naming-main-reconciliation-and-merge.md`
- `working-memory/2026-09-06_1609_semantic-executable-naming-migration.md`
- `working-memory/2026-09-05_1801_semantic-naming_coordinate-decoupling.md`
- `working-memory/2026-09-06_B2-X1-R4B-first-wsl-executable-proof.md`
- `working-memory/2026-09-06_B2-X1-R4B6-controlled-semantic-comparison-build.md`
- `working-memory/2026-09-04_2017_B2-X1-R4B-r4a-representation-coupling-correction.md`
- `working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`

Older R4-A/R4-B, E1-E5, proposal, and learning records remain historical provenance rather than live naming authority.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
