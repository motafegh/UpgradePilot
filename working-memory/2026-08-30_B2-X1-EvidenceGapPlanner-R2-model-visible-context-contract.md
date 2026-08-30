# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context Contract

**Date:** 2026-08-30  
**Branch:** `agent/b2-x1-r2-model-visible-context-contract-2026-08-30`  
**Base main:** `ac470e73c52ea0037bb5a88328b6de76dc4c02a0`  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** freeze and prove the candidate field-level context that the experiment-owned `EvidenceGapPlanner` may receive before R3 designs the output/admission contract

## 1. Entry state

R0 re-anchor and R1 responsibility vocabulary were already complete. `MEMORY.md` selected R2 as the live next stage.

The active historical implementation evidence still exposed a wider Phase-3/v2 snapshot to the model, including fields that the post-research design had not independently justified:

- proposition `evidence_owner`;
- action repository/revision/path locator metadata;
- `hard_constraints` strings;
- `untrusted_evidence_notes`.

At the same time, the historical request did **not** carry the dependency transition as first-class structured context.

R2 therefore did not mutate the consumed Phase-3/v2 harness. Instead it created a new post-research projection owner under `experiments/` so historical evaluation code remains evidence rather than silently becoming the new contract.

---

## 2. Implemented owner

New experiment module:

`../experiments/b2_x1_evidence_gap_model_context.py`

Primary function:

```text
trusted PlannerEvaluationCase
+ trusted DependencyVersionChange
→ build_evidence_gap_model_context(...)
→ exact compact model-visible context
```

Stable JSON rendering is supplied separately for direct inspection, hashing, and later replay.

R2 deliberately does **not** freeze the historical `AgentPlanResult` output schema. R3 owns the candidate structured decision and deterministic admission contract.

---

## 3. Field decision table

| Candidate field | Model-visible? | Trusted owner / source | Why visible or excluded |
|---|---|---|---|
| `planning_question` | yes | evaluator/project-owned bounded question | Defines which uncertainty/responsibility the planner is advancing; prevents every unresolved proposition becoming automatic work. |
| `case_identity.repository` | yes | trusted snapshot / PR identity | Compact trace/context for the exact target case; visibility does not transfer repository authority. |
| `case_identity.pull_number` | yes | trusted snapshot / PR identity | Identifies the PR-based case without relying on evaluator labels. |
| `case_identity.revision` | yes | trusted snapshot / exact immutable revision | Makes the planning turn explicitly revision-scoped; model cannot redefine it. |
| `dependency_transition.package` | yes | `DependencyVersionChange` | Central upgrade context that should not be reconstructed from proposition prose. |
| `dependency_transition.old_version` | yes | `DependencyVersionChange` | Exact trusted source version is directly relevant to upgrade reasoning. |
| `dependency_transition.proposed_version` | yes | `DependencyVersionChange` | Exact trusted target version is directly relevant to upgrade reasoning. |
| dependency `normalized_package` | no | product dependency owner | Needed for deterministic identity/consensus, not for this planner decision. |
| dependency source provenance / limitations | no | product dependency/evidence owners | Underlying proof remains available outside the model; R2 needs the trusted transition result, not the whole product object. |
| proposition `key` | yes | trusted proposition state | Stable handle for reasoning/action targeting. |
| proposition `state` | yes | trusted proposition state | Establishes whether the fact is established/refuted/unresolved/conflicted. |
| proposition `evidence_coverage` | yes | trusted proposition state | Distinguishes adequate from inadequate evidence for planning. |
| proposition `detail` | yes | bounded project-authored projection | Supplies the semantic content needed to reason about the proposition without raw object serialization. |
| proposition `evidence_owner` | no | domain/evidence owner | Current E3/E4 reasoning did not require source-owner labels; planner does not decide evidence authority from this field. |
| proposition `origin` | no | not part of current required planner projection | No evidence that source-origin metadata changes the first-seam planning responsibility. |
| raw-external-text flag | no | evidence/domain owner | Raw-text carryover is already prevented by projection; adding a flag would describe an excluded channel rather than enable required reasoning. |
| attempted `action_id` | yes | trusted system action history | Lets later turns avoid blind repetition and reason over bounded prior attempts. |
| attempted `outcome` | yes | trusted system action history | `completed | problem | rejected` is enough for the current replay/repetition responsibility. |
| free-form action-history prose | no | none needed | Findings that matter belong in updated propositions/evidence state; history is not free-form LLM memory. |
| `remaining_budget.remaining_steps` | yes | trusted bounded-loop state | Makes the remaining action budget explicit without giving the model authority to change it. |
| allowed `action_id` | yes | trusted action catalog | Closed capability binding handle selected by the model. |
| allowed `purpose` | yes | trusted action catalog | Explains what discriminating evidence the capability can obtain. |
| allowed `target_proposition` | yes | trusted action catalog | Connects the capability to the evidence gap it can address. |
| allowed required proposition/evidence precondition | yes | trusted action catalog | Helps the model understand when the capability is applicable; deterministic admission still re-checks it. |
| allowed `cost_class` | yes | trusted action catalog | Supports future prioritization/budget reasoning without making the model the cost authority. |
| allowed `mutation_class` | yes | trusted action catalog | Makes the capability boundary visible; deterministic code still enforces the allowed mutation class. |
| allowed result-family names | yes | trusted action catalog | Explains what evidence/result family the capability can produce without requiring the model to redefine it. |
| allowed repository/revision/path locator | no | trusted action object | Duplicates exact case/action binding and is not needed to choose the capability; R3 admission/rebinding keeps this deterministic. |
| `hard_constraints` string list | no | deterministic/system control plane | Current invariants are better enforced structurally/system-side; repeating them as planner-visible state adds context without new responsibility. |
| `untrusted_evidence_notes` | no | historical adversarial evaluation channel | E2/post-research first seam does not need synthetic raw-note exposure; excluding it removes unnecessary prompt-injection surface. |
| evaluator case key / partition / oracle / expected answer | no | evaluator only | Would leak grading/protected information and has no planning role. |

---

## 4. Direct proof cases

### Real S001 action state

The new projection renders:

```text
planning_question
case_identity = pydantic/pydantic #13432 @ aa2dc0...
dependency_transition = soupsieve 2.6 → 2.8.4
ordered typed propositions
attempted_actions = []
remaining_steps = 1
one allowed action = acquire_exact_target_python_declaration
```

The allowed action includes its purpose, target proposition, precondition, cost/mutation class, and result families, but does not expose repository/revision/path locator duplication.

### Real S004 no-tool state

The projection renders the real S004 bounded state with:

```text
dependency_transition = pytest 9.0.2 → 9.0.3
allowed_actions = []
attempted_actions = []
remaining_steps = 1
```

Evaluator/oracle fields, historical case key, hard-constraint strings, untrusted notes, and proposition evidence-owner labels are absent.

### Attempt-history / stale-repeat state

A replay-style development state was constructed from the existing A1 case with:

```text
action_id = acquire_exact_target_python_declaration
outcome = problem
```

The next model context receives only this typed system history. No free-form reason/detail is used as model memory. The action may still be present in the trusted catalog; R3 deterministic admission remains responsible for rejecting a forbidden repeat.

---

## 5. Focused tests added

New test module:

`../experiments/tests/test_b2_x1_evidence_gap_model_context.py`

It protects:

1. exact top-level R2 fields and S001 structured transition;
2. proposition-field narrowing;
3. allowed-action field narrowing and locator exclusion;
4. real S004 no-tool projection and exclusion of evaluator/raw channels;
5. typed attempt-history projection without prose memory;
6. projection of `DependencyVersionChange` rather than wholesale object serialization;
7. stable JSON rendering.

---

## 6. Validation performed in this execution environment

The available execution environment could not clone GitHub because outbound DNS/network access from the local container was unavailable, and the repository has no GitHub Actions workflow directory to provide a remote CI run for this branch.

Validation therefore used the strongest available checks here:

```text
GitHub branch read-back of created source/test files
→ PASS

branch compare against base main
→ PASS: branch ahead only by the intended experiment source/test commits before records

Python 3.13 syntax compilation of the new projection module
→ PASS

direct behavioral assertions against representative typed object shapes
→ PASS
```

The behavioral assertions checked:

- exact R2 top-level keys;
- structured dependency transition;
- omission of proposition `evidence_owner`;
- omission of action repository/revision/path;
- omission of evaluator/raw/hard-constraint channels;
- typed attempted-action history;
- stable JSON parsing/rendering.

This is not a substitute for running the repository's actual focused unit test module in a real checkout. That remains a validation limitation, not a hidden PASS.

---

## 7. R2 result — COMPLETE

R2 pass condition is met at the design/implementation boundary:

> Every model-visible field has an explicit planning role and an authoritative non-model owner where appropriate; the request does not depend on serializing entire product objects.

The candidate model-visible context is now explicit and experiment-owned.

R2 does **not** prove model quality, product integration value, or the final output/admission shape.

---

## 8. Stop line and next stage

Stop this slice here.

The next justified stage is **R3 — freeze the candidate `EvidenceGapDecision` structured output and deterministic admission/rebinding contract**.

R3 should use the R1 decision vocabulary and this R2 context projection, and should remove redundant model-echoed authority fields rather than retaining the historical six-field `AgentPlanResult` shape by inertia.
