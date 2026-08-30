# UpgradePilot Current Memory

**Last updated:** 2026-08-30  
**Authority:** sole owner of the live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation and historical design are evidence to inspect, not authority to preserve unchanged.

```text
real responsibility / proof need / material risk / learning value
→ identify the earliest sufficient owner
→ keep or grow mechanisms that add real capability
→ refine redundant ownership/representation
→ avoid both over-engineering and under-engineering
```

Do **not** optimize UpgradePilot for minimum mechanism count. Complexity is welcome when it buys real product capability, stronger reasoning, useful failure handling, observability/replay, or meaningful engineering learning. Complexity is unwanted when it is redundant, ceremonial, speculative, or does not change a real responsibility.

Canonical governance owners remain `AGENTS.md`, `OPERATING_GUIDE.md`, the controlling specifications, and the active operation/Learning-by-Doing procedure.

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Mode:** Learning-by-Doing / Building.
- **Selected plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Current plan progress:** R0 re-anchor **PASS**; R1 responsibility vocabulary **COMPLETE**; R2 model-visible context contract **COMPLETE**.
- **Live next stage:** **R3 — EvidenceGapDecision structured output + deterministic admission/rebinding contract**.
- **Current implementation boundary:** EvidenceGapPlanner remains experiment-owned. Product `src/upgradepilot/` planner integration is not authorized.
- **Technical blocker:** none for R3 design/build work.
- **Validation limitation from R2:** the assistant environment could not obtain a full repository checkout and the repository exposes no GitHub Actions workflow for remote CI; R2 source was read back from the branch and passed local Python syntax/direct projection checks, but the actual repository focused test module still needs execution in a real checkout when available.
- **Product-simulation:** previous capability/value research is complete; do not launch another broad simulation job merely for more cases.

Current detailed execution evidence:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context-contract.md` — completed R2 field decisions, implementation, proof cases, and validation limits;
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R0-R1-responsibility-vocabulary.md` — completed R0/R1 decisions;
- `working-memory/2026-08-30_B2-X1-planner-responsibility-input-naming-and-next-route.md` — immediate post-research design context;
- `working-memory/2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md` — E1–E5 design reconciliation;
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md` — completed delegated capability/value research.

---

## Current responsibility vocabulary

### Component

**`EvidenceGapPlanner`**

Working responsibility:

> Given one bounded UpgradePilot planning question, trusted typed evidence state, trusted attempt history/budget, and a closed set of admitted investigation capabilities, decide which material evidence gap should be addressed next by selecting one useful admitted capability, or explicitly decide why no capability should execute now.

This name remains experiment/design vocabulary until product integration is separately authorized.

### Model result

**`EvidenceGapDecision`**

The model result is a proposal, not trusted authority.

### Working decision kind vocabulary

**`EvidenceGapDecisionKind`** with meanings:

```text
ACTION_SELECTED
→ one trusted admitted capability was selected

QUESTION_SETTLED
→ the bounded planning question is sufficiently settled; more investigation is not justified

KNOWN_INVESTIGATION_NOT_ADMITTED
→ a useful next investigation is known but no corresponding capability is currently admitted

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ the question remains non-final, but no justified resolving investigation is currently identified
```

Historical E5 vocabulary maps as:

```text
choose_action → ACTION_SELECTED
stop          → QUESTION_SETTLED
defer         → KNOWN_INVESTIGATION_NOT_ADMITTED
unresolved    → NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

R3 owns the final structured/wire representation.

---

## Evidence baseline that must not be re-proved without contradiction

### E1 — semantic interpretation vs grounding

A candidate can be exactly source-grounded without deterministic code independently proving the English semantic direction. The adopted local support-drop model handled the selected negation/future/instruction-shaped live pressures in the executed slice, but universal semantic robustness is not proven.

### E2 — context projection

Real S001 established:

```text
small typed proposition/action projection
→ raw external changelog prose absent

nested product assessment
→ raw source quote still exists internally
```

Raw-text carryover and semantic carryover are different channels. The planner does not need every internal evidence object merely because UpgradePilot stores it.

### E3 — minimally constrained reasoning

With typed propositions and a bounded question, `gemma-4-e4b-it-ud` correctly identified the missing exact target Python declaration before closed actions/schema/admission were added.

### E4 — mechanism responsibilities

```text
typed state
→ reasoning context

closed trusted action descriptor
→ exact capability binding

strict JSON Schema
→ machine-readable output shape

deterministic admission
→ fresh catalog/state/precondition revalidation
```

The model need not echo repository/revision/path/target/result-family metadata already owned by trusted action descriptors.

### E5 — no-tool semantics

The model distinguished the historical `stop | defer | unresolved` meanings on the selected development cases. Those semantics are retained through the R1 vocabulary rather than collapsed into one null-action state.

### Product-simulation capability research

```text
real additional/incomplete capabilities found
→ YES

second capability already justified for LLM-owned selection
→ NO

general adaptive-planner product value proven
→ NO
```

The strongest additional candidate was exact-head resolver/currentness/satisfiability evidence, but current research still supports compact deterministic selection better than manufacturing it as a second LLM action.

---

## R2 model-visible context contract — frozen candidate

R2 introduced `experiments/b2_x1_evidence_gap_model_context.py` as the post-research projection owner rather than mutating the consumed Phase-3/v2 harness.

The candidate model-visible context is:

```text
planning_question
case_identity
  repository
  pull_number
  revision

dependency_transition
  package
  old_version
  proposed_version

ordered propositions
  key
  state
  evidence_coverage
  bounded detail

attempted_actions
  action_id
  outcome

remaining_budget
  remaining_steps

allowed_actions
  action_id
  purpose
  target_proposition
  required proposition/evidence precondition
  cost_class
  mutation_class
  result-family names
```

Explicitly excluded from the first-seam model context:

- dependency normalized identity/source provenance/limitations;
- proposition `evidence_owner`, origin, or raw-text flags;
- action repository/revision/path locator duplication;
- free-form action-history prose;
- historical `hard_constraints` string lists;
- `untrusted_evidence_notes` / synthetic raw-note pressure channels;
- evaluator case labels, oracle, expected answers, protected/grading metadata;
- wholesale CI logs/payloads, diffs, source files, lockfiles/graphs, raw upstream release/changelog text, or whole product object graphs.

Underlying evidence and authority remain with deterministic product/domain owners. Visibility does not transfer authority to the model.

R2 proof covered the real S001 action state, real S004 no-tool state, and an attempted-action replay state. The actual repository focused tests are added but not yet runtime-executed in a real checkout from this assistant environment.

---

## R3 — immediate design/build question

R3 now owns the smallest `EvidenceGapDecision` representation that preserves R1 semantics while removing redundant model-echoed authority fields.

Conceptually the candidate should decide:

```text
decision_kind
action_id | null
no_tool_disposition | null
explanation
```

Trusted code must continue to own/rebind:

- repository/revision/path/command/source locator;
- target proposition;
- action preconditions;
- mutation class;
- result/problem families;
- execution authorization;
- trusted state changes.

Deterministic admission must re-check at least current action existence, mutation boundary, attempted-action history, remaining budget, and current proposition precondition where applicable.

Do not retain the historical six-field `AgentPlanResult` merely for compatibility if R3 can preserve the required semantics more clearly with a smaller contract.

---

## Current learning ladder

Near-term:

```text
R3 output/admission contract
→ structured outputs, tagged decisions, tool/action authority, stale-plan revalidation

R4 cohesive experiment build
→ ordinary-Python agent state/action loop mechanics

R5 bounded development/replay proof
→ tracing, replay, model/system/transport failure separation
```

Later, only when earned:

- fresh v3 repeated/holdout evaluation for a selected narrow claim;
- multiple real actions and information-value prioritization;
- real multi-turn plan → execute → update → re-plan loop;
- failure-aware replanning and retry ownership;
- broader upstream semantic mechanism discovery as a separate LLM responsibility;
- LangGraph/LangChain comparison when state/node/edge/checkpoint concepts are understood from the actual UpgradePilot loop; no framework adoption without an independent need.

---

## Proof limits / prohibited claims

Current evidence does **not** prove:

- production reliability;
- general planner superiority over deterministic orchestration;
- correct selection across several real actions;
- product adoption value;
- compatibility/safety/merge authority;
- that raw evidence should never enter any future planner;
- that every omitted historical strict mechanism is permanently unnecessary.

Do not:

- fabricate a second planner action;
- freeze v3 before an exact claim is selected and fresh holdouts are screened/reserved;
- reuse historical v2 protected material as an uncontaminated final scorecard;
- begin product `src/upgradepilot` planner integration merely because the experiment seam works;
- add LangGraph/LangChain/another agent framework merely for learning exposure;
- continue product-simulation research merely to increase case count.

---

## Environment facts relevant to the current route

- WSL remains the control plane.
- LM Studio is locally available at `127.0.0.1:12345` for the current checkpoint.
- Model used in E1–E5: `gemma-4-e4b-it-ud`.
- Local LM Studio requests disable ambient proxy inheritance.
- Public GitHub acquisition can be disrupted by stale `GITHUB_TOKEN` or proxy variables; reusable environment handling remains owned by `ENVIRONMENT.md`.
- No cloud/paid fallback is part of the current X1 checkpoint.

---

## Immediate continuation

```text
R3 — EvidenceGapDecision structured representation + deterministic admission/rebinding ownership
→ R4 — cohesive experiment-owned implementation
→ R5 — bounded development/replay proof
→ R6 — explicit X1 disposition
```

Before treating R2 runtime proof as fully closed, run the new focused repository test module in a real checkout when that execution surface is available. This pending check does not reopen R2 field design unless it reveals a real contradiction.

Richer multi-action/multi-turn planner work reopens only when multiple independently justified capabilities naturally coexist and real state/history/budget-dependent selection becomes materially non-trivial for a small deterministic policy.

Historical detail remains in the dated working-memory records and Git history; do not turn root `MEMORY.md` back into a duplicate archive.
