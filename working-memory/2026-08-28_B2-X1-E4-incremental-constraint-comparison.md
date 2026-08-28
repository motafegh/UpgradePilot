# B2/X1 E4 — Incremental Constraint Comparison

**Date:** 2026-08-28  
**Status:** E4.1 / E4.2 / E4.3 COMPLETE — CONTROL RESPONSIBILITIES SEPARATED; NEXT COMPARE AGAINST STRICT PLANNER CONTRACT  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

E4 tests candidate planner controls one at a time, starting from the successful E3 minimally constrained S001 planner behavior.

The comparison discipline is:

```text
freeze the successful planner state
→ change one control
→ observe what changed
→ do not reacquire unrelated live evidence unless that is the variable being tested
```

## E3 control result

The successful E3 run showed that `gemma-4-e4b-it-ud`, given the real typed pre-investigation S001 propositions and bounded planning question, naturally proposed acquiring the exact target Python declaration.

The model correctly followed:

```text
upstream support drop established
→ exact target declaration unresolved / insufficient
→ range intersection depends on that missing declaration
→ acquire target declaration next
```

It did not receive a closed action catalog, JSON Schema, deterministic admission, or raw upstream changelog prose.

Persisted local E3 evidence:

```text
/tmp/upgradepilot-b2-x1-e3-minimal-s001-planner.json
```

## E4.1 design correction before valid execution

The first E4.1 implementation reacquired the entire real S001 normal product path. That was methodologically wrong for an incremental-control comparison because it added GitHub REST state, provider acquisition, the support-drop semantic-model pass, and grounding as uncontrolled variables.

Observed failed attempts before the correction were therefore **not planner results**:

1. one run did not retain the expected pre-investigation assessment;
2. a diagnostic revision was prepared to preserve that upstream prerequisite state;
3. the next run stopped at public GitHub acquisition with the client's `forbidden_or_rate_limited` category.

The experiment was then corrected to replay the exact successful E3 planner input instead of reacquiring S001.

Correct E4.1 flow:

```text
persisted successful E3 JSON
→ validate exact S001 identity / baseline / boundary facts
→ fingerprint replay source
→ retain exact E3 question + propositions
→ add one trusted action descriptor from build_target_python_declaration_action(...)
→ call LM Studio
→ record proposal only
→ execute nothing
```

## E4.1 live controlled result — PASS

User-executed result:

```text
case: pydantic/pydantic#13432
comparison_basis: exact persisted E3 planner input + one trusted action
e3_replay_sha256: d2a1cf7455571402b8b82633b2e951473159b857194a76f853ed808adf25a179
github_acquisition_performed: False
support_drop_model_reexecuted: False
model: gemma-4-e4b-it-ud
elapsed_seconds: 6.425
expected_action_id_mentioned: True
capability_executed: False
```

Model proposal:

```text
The most useful next investigation step is to acquire the exact target Python declaration...

action_id: "acquire_exact_target_python_declaration"
```

Its explanation correctly connected:

```text
exact_target_python_declaration_established
→ unresolved
→ action directly acquires that missing evidence
→ required before declared_python_range_intersects_dropped_line can be resolved
```

No raw upstream changelog text was supplied to the planner.

## E4.1 finding — closed action context improves binding precision

The strongest evidence-backed interpretation is:

```text
E3 typed state only
→ correct conceptual next step

same exact E3 state
+ one trusted closed action descriptor
→ same reasoning direction
+ exact action_id binding
```

Therefore the closed action descriptor earned a concrete role:

```text
trusted action context
→ maps good planning reasoning onto a known executable capability identity
```

Do **not** over-credit it. E3 had already demonstrated the core S001 reasoning before the action catalog existed.

The action descriptor also supplied repository/revision/path and action metadata. If the model repeats those values later, that is consumption of trusted context, not independent discovery.

## E4.2 controlled JSON-Schema comparison — PASS

E4.2 replayed the exact persisted E4.1 `planner_input` and changed only the provider output contract by adding strict JSON Schema structured output.

No GitHub acquisition or support-drop-model rerun occurred.

User-executed result:

```text
case: pydantic/pydantic#13432
comparison_basis: exact persisted E4.1 planner input + JSON Schema only
e4_1_replay_sha256: 4f9c0fd9950b824b5c1ca8dd8e0959ffc9b024af1ae874fac4d60e3f80b7fdae
github_acquisition_performed: False
support_drop_model_reexecuted: False
model: gemma-4-e4b-it-ud
elapsed_seconds: 5.607
expected_action_id_selected: True
capability_executed: False
```

Exact structured model result:

```json
{
  "action_id": "acquire_exact_target_python_declaration",
  "explanation": "The planning question requires determining if the upstream Python 3.8 support drop affects the target project's exact declared Python range. The current state shows that 'exact_target_python_declaration_established' is unresolved due to insufficient evidence. Acquiring this declaration is the necessary next step to resolve this proposition and subsequently evaluate whether the dependency update impacts the target project's supported Python versions."
}
```

The JSON Schema deliberately did **not** enumerate the accepted action ID. It allowed `action_id` to be any non-empty string or `null`, so the correct action selection still came from the model consuming the trusted action catalog rather than being forced by the output schema.

## E4.2 finding — JSON Schema improves integration shape, not observed reasoning quality

The controlled comparison is:

```text
E4.1
same typed state + same trusted action descriptor
→ correct action in free-form text

E4.2
same exact planner input
+ strict JSON Schema only
→ same correct action
→ directly parseable {action_id, explanation}
```

Therefore E4.2 supports this bounded responsibility:

```text
JSON Schema
→ machine-readable field/type shape
→ deterministic parsing boundary
→ less output-format ambiguity for integration
```

E4.2 does **not** show that JSON Schema made the planner reason better. The reasoning direction and action selection were already correct in E4.1.

## E4.3 deterministic-admission replay — PASS

E4.3 did not call GitHub or LM Studio. It replayed the exact successful E4.2 parsed model result against reconstructed trusted S001 state and the existing `admit_agent_plan(...)` owner.

The minimal E4.2 model output contained only:

```text
action_id
explanation
```

Trusted action metadata was rebound deterministically before admission:

```text
target_proposition
result_families
repository
revision
path
mutation class
preconditions
```

User-executed result:

```text
case: pydantic/pydantic#13432
comparison_basis: exact persisted E4.2 result + deterministic admission
e4_2_replay_sha256: 4d2f6b5bb3335fc6bfaa157ad72b71300152231ca93e036961dff2163b9a75cf
model_called: False
observed_admission: admitted_action
unknown_action_counterfactual: admission_problem | unknown_action
stale_state_counterfactual: admission_problem | target_proposition_not_actionable
capability_executed: False
```

### Happy path

The observed correct E4.2 action was admitted as the exact trusted read-only capability:

```text
acquire_exact_target_python_declaration
→ pydantic/pydantic
→ aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
→ pyproject.toml
```

The model did not supply or redefine those locator/action semantics during E4.3.

### Unknown-action counterfactual

The same trusted state with an untrusted invented action ID:

```text
invented_untrusted_action
```

was rejected as:

```text
admission_problem | unknown_action
```

This proves the planner cannot expand executable authority merely by naming a new capability.

### Stale-state counterfactual

The exact originally correct model proposal was replayed after the trusted target proposition was changed to:

```text
state = established
evidence_coverage = sufficient
```

Admission rejected the formerly useful action as:

```text
admission_problem | target_proposition_not_actionable
```

This demonstrates fresh-state revalidation: a plan that was correct when proposed need not remain executable after trusted state changes.

## E4.3 finding — deterministic admission earns execution-time containment responsibility

E4.3 supports:

```text
model proposal
!=
execution authority
```

and specifically:

```text
trusted catalog membership
+ current proposition state/coverage
+ trusted action preconditions
→ rechecked at admission time
```

This role is distinct from planner reasoning and JSON formatting.

The bounded evidence-backed consequence is:

```text
wrong/forged action ID
→ cannot become executable solely because the model emitted it

stale previously-correct action
→ cannot remain executable solely because it was once valid
```

## E4 simplification finding — model echo of trusted action metadata is not yet justified

The old planner contract asks the model to emit more than E4.2 required, including trusted action-related fields such as target proposition and expected result categories.

E4.3 showed that for this first S001 seam those values can be rebound from the trusted action descriptor after the model selects only:

```text
action_id
explanation
```

Therefore current evidence does **not** justify requiring the model to redundantly echo trusted action metadata merely so admission can compare the echo with the owner.

This is not yet a durable contract change. It is a design finding to compare against the accepted strict X1 contract and no-tool cases before reconciliation.

## E4 complete responsibility separation

The controlled E3→E4 sequence now supports:

```text
typed proposition projection
→ planner reasoning context

closed trusted action descriptor
→ exact capability/action binding

minimal JSON Schema
→ machine-readable output shape / deterministic parsing

deterministic admission
→ trusted catalog/state/precondition revalidation before execution
```

The mechanisms are useful for different reasons. Treating all of them as one generic "guardrail stack" would obscure those responsibilities.

## What E4 still does not prove

E4 does not establish that:

- the model will choose correctly across several allowed actions;
- one successful S001 call proves planner repeatability;
- the minimal `{action_id, explanation}` result can represent every required no-tool disposition;
- `stop`, `defer`, and `unresolved` all need to remain distinct planner outputs;
- the existing hard-constraint list must or need not be planner-visible;
- `untrusted_evidence_notes` belongs in the first product planner seam;
- every current `AgentPlanResult` field is redundant;
- the planner is useful enough across varied real cases to justify product integration.

## Next discriminating question

Before modifying the accepted planner contract or durable X1 plans, compare the now-observed minimal action path against the strict contract and test the largest remaining semantic difference: **no-tool disposition representation**.

The current minimal E4.2 shape can express:

```text
action_id = <trusted id>
action_id = null
```

but the older contract distinguishes:

```text
stop
defer
unresolved
```

The next experiment should determine whether that distinction is actually useful/necessary on a real no-tool case (start with S004) rather than preserving or removing it by intuition.
