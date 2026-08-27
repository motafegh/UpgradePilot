# Working Memory — B2/X1 Phase 2 Planner Contract and Admission Implementation

**Date:** 2026-08-27  
**Status:** PHASE 2 IMPLEMENTED — LOCAL DETERMINISTIC VALIDATION PENDING  
**Current plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Phase-1 record:** `2026-08-27_B2-X1-PHASE1-capability-and-orchestration-seam-inventory.md`  
**Pre-Phase-2 live-state revision:** `7fff121ab4c67d3d951a17827edb454945e00313`

## 1. Responsibility implemented

Phase 2 freezes the first experiment-owned planner state/action/result contract and the deterministic admission boundary that any later model output must pass.

This is **not** product-agent adoption and not normal-product-path integration.

The implementation lives under the existing experiment boundary:

```text
experiments/b2_x1_planner_contract.py
experiments/tests/test_b2_x1_planner_contract.py
```

No `src/upgradepilot` file was changed.

## 2. Why experiment ownership is correct

The checkpoint has not yet produced comparative evidence for adopting a planner architecture. Therefore placing these contracts in product runtime would pre-adopt the method under evaluation.

Current ownership is intentionally reversible:

```text
accepted product/domain types
→ may be imported by experiment code

experiment planner contract
→ must not be imported by product src/
```

If later Phase 6 rejects or defers agentic planning, the experiment boundary can remain historical evidence or be removed without product migration.

## 3. Contract shape

Trusted planner-facing snapshot:

```text
InvestigationSnapshot
├── case_key
├── repository
├── pull_number
├── exact revision
├── typed PropositionAssessment[]
├── attempted action outcomes
├── deterministically built allowed action catalog
├── remaining step budget
├── hard constraints
└── bounded untrusted evidence notes
```

Raw arbitrary repository/upstream content is deliberately absent from the core snapshot contract. Untrusted notes exist only to pressure security/replay cases and have no catalog/policy authority.

First real action:

```text
acquire_exact_target_python_declaration
```

The deterministic action catalog pre-binds:

```text
action ID
purpose / target proposition
repository
exact immutable revision
path = pyproject.toml
required proposition state = unresolved
required evidence coverage = insufficient
mutation class = read_only
result families = TargetPythonDeclaration | TargetPythonDeclarationProblem
cost class = low_network
```

## 4. Important narrowing during implementation

The first implementation initially let model-shaped output repeat repository/revision/path arguments and then validated exact equality.

Post-write responsibility review found a smaller and safer mechanism:

```text
model chooses action_id only

NOT

model chooses action_id
+ repeats exact repository
+ repeats exact revision
+ repeats exact path
```

Commit:

```text
55f70ef4178b26690b29943eb35ebfebdf8c0d41
Narrow B2 X1 planner contract to prebound actions
```

This is the stronger design because repository/revision/path are already trusted deterministic state. Asking the model to restate them creates no useful planning capability and adds an unnecessary source-selection/identity failure surface.

The action catalog itself is checked against the exact snapshot repository/revision, and the target-Python action ID cannot be repurposed to another path or proposition.

## 5. Structured output versus semantic admission

The experiment freezes a JSON Schema-shaped planner output surface:

```text
state = choose_action | stop | defer | unresolved
selected_action_id?
target_proposition
reason
expected_result_categories[]
limitations[]
```

`agent_plan_result_from_mapping(...)` owns strict field/type parsing.

Passing structured output is still not authorization:

```text
schema-valid model output
→ AgentPlanResult
→ admit_agent_plan(...)
→ AdmittedInvestigationAction
   OR AdmittedNoToolDisposition
   OR PlanAdmissionProblem
```

Deterministic admission separately owns the current semantic/action checks.

## 6. Admission guards implemented

The focused contract protects:

```text
unknown action ID
→ rejected

catalog action not read-only
→ rejected

already-attempted action
→ rejected

remaining step budget == 0
→ rejected

planner target proposition differs from action proposition
→ rejected

trusted proposition is no longer unresolved/insufficient
→ rejected

planner expected result categories differ from deterministic action result families
→ rejected

unsupported planner state
→ construction rejected

stop/defer/unresolved with selected action
→ construction rejected

stop/defer/unresolved with tool-result categories
→ construction rejected

prompt-injection-shaped untrusted evidence text
→ cannot add an action to the deterministic catalog
```

A valid `stop`, `defer`, or `unresolved` produces `AdmittedNoToolDisposition`; it contains no executable action.

## 7. Proof boundary

The Phase-2 contract can establish only:

```text
one model-shaped proposal is structurally and semantically admissible
for one exact trusted snapshot/action catalog
```

It cannot establish:

```text
model planning quality
provider/model reliability
actual GitHub capability execution
correct evidence-state reduction after execution
generalization across multiple action choices
agent superiority over deterministic orchestration
product adoption
compatibility/safety/maintainer action
```

## 8. One-action catalog decision

Disposition:

```text
ONE REAL ACTION + STOP/DEFER/UNRESOLVED
= SUFFICIENT FOR PHASE-2 CONTRACT/ADMISSION PROOF

ONE REAL ACTION ALONE
!= SUFFICIENT FOR FINAL PLANNER ACTION-SELECTION VALUE CLAIM
```

Why it is sufficient now:

- Phase 2 needs to prove authority, identity, action-catalog, budget, repeat, no-tool, and result-family guards;
- the existing target-Python action is a real admitted discriminating investigation, not a fabricated wrapper;
- stop/defer/unresolved behavior is itself a material first-pilot responsibility.

Why it is not enough for final comparison:

- with only one executable action, choosing among alternative useful actions is not meaningfully exercised;
- Phase 3 must therefore either identify at least one second real/replay-safe independent action for the scored planner decision points, or explicitly narrow the later evaluation claim to action-vs-stop/defer behavior and treat broader adaptive action selection as unproven.

Do not create a fake second tool merely to make the catalog look agentic.

## 9. Implementation revisions

Initial contract:

```text
f1e8b1b85e8483dfb6fb8d1ff90bc6b349a8c6d6
```

Initial focused tests:

```text
831bfeb26f4d030bc40d410baf8a4d66607e8bc1
```

Pre-bound action narrowing:

```text
55f70ef4178b26690b29943eb35ebfebdf8c0d41
```

Result-semantics tightening:

```text
c1f23af4b1b7e66a232e5db376d95be16c0b4c18
```

Focused guard tests update:

```text
4e9c0e01d9e62eb2ccc15f81e4eedc1de3e8f6de
```

At that point the Phase-2 diff from `7fff121...` contains only:

```text
experiments/b2_x1_planner_contract.py
experiments/tests/test_b2_x1_planner_contract.py
```

## 10. Validation state

Static/source/diff inspection:

```text
experiment-only placement                              PASS
no src/ product mutation                               PASS
pre-bound repository/revision/path authority           PASS
read-only admission guard                              PRESENT
repeat/budget/proposition guards                       PRESENT
result-family ownership guard                          PRESENT
no-tool stop/defer/unresolved contract                 PRESENT
prompt-injection-shaped catalog-expansion regression   PRESENT
```

Runtime:

```text
focused experiment unit tests                          PENDING
compileall for Phase-2 files                           PENDING
```

An attempted isolated runtime checkout from the assistant execution environment could not resolve `github.com`, so no runtime result was produced. That environment/network failure is not classified as a product or test failure.

## 11. Exact local validation needed

Run from the normal WSL project checkout after syncing `main`:

```bash
.venv/bin/python -m unittest -v \
  experiments.tests.test_b2_x1_planner_contract

.venv/bin/python -m compileall -q \
  experiments/b2_x1_planner_contract.py \
  experiments/tests/test_b2_x1_planner_contract.py
```

If focused validation fails, preserve the exact output and repair only the owning Phase-2 experiment contract/test boundary before Phase 3.

## 12. Current gate

```text
Phase-2 contract design                  COMPLETE TO SOURCE/DESIGN DEPTH
Phase-2 implementation                  COMPLETE
Phase-2 deterministic runtime proof      PENDING
Phase 3                                 BLOCKED ON PHASE-2 RUNTIME GATE
```
