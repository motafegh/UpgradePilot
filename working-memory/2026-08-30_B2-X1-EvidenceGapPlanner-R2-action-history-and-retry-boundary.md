# B2/X1 EvidenceGapPlanner R2 — Consumed-Action History and Retry Boundary

**Date:** 2026-08-30  
**Status:** R2 SLICE COMPLETE — planner-visible action-history boundary decided  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`  
**Previous R2 slice:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`

## 1. Product / experiment truth inspected

The historical experiment contract currently defines:

```text
AttemptedInvestigationAction
    action_id
    outcome = completed | problem | rejected
```

and `admit_agent_plan(...)` blocks blind repetition when the selected `action_id` already appears in `attempted_actions`.

The current focused repeat test uses:

```text
A1 already represented as outcome = problem
+ planner selects A1 again
→ action_already_attempted
```

The existing contract is therefore a valid simple pilot guard, but its terminology and outcome model are broader/coarser than the evidence-refined R2 responsibility now requires.

The completed product-simulation action-failure/retry transfer evaluation additionally established:

```text
valid typed action result / typed domain problem
!= transient provider/acquisition failure
```

and:

```text
planner-level semantic repetition
!= deterministic transport retry
```

## 2. Main R2 correction — history should represent consumed investigations, not every proposal

The first-seam planner does not need every model proposal, admission failure, provider HTTP attempt, or executor-internal retry as model-visible investigation history.

The planning-relevant fact is narrower:

> Which already-admitted bounded investigation has produced a trusted typed result/problem for this exact state such that blindly selecting the same investigation again would add no justified information?

Use **`consumed_actions`** as the R2 working concept instead of generic `attempted_actions`.

Conceptually:

```text
consumed_actions:
  - action_id
```

Do not freeze a concrete dataclass merely from this design record. R4 should implement the smallest representation that preserves this meaning.

## 3. What counts as a consumed action

An investigation action enters planner-visible `consumed_actions` only after this lifecycle:

```text
EvidenceGapPlanner proposes action_id
→ deterministic admission accepts the current trusted action
→ deterministic executor/provider performs the bounded execution responsibility
→ domain owner receives enough trustworthy material to emit a typed action result or typed domain/evidence problem
→ trusted propositions / EvidenceGapPlanningEvidence are updated as appropriate
→ action is recorded as consumed for the current bounded state
```

Examples for current A1:

```text
TargetPythonDeclaration
→ trusted typed result
→ A1 consumed

TargetPythonDeclarationProblem
  file_unavailable
  malformed_toml
  project_table_absent
  requires_python_absent
  invalid_requires_python
→ trusted typed domain/evidence problem
→ A1 consumed for the same exact state
```

The exact finding is not stored only in action history. Its planning meaning must be represented in the updated proposition/evidence state.

## 4. What does NOT count as a consumed investigation

### 4.1 Model proposal rejected by deterministic admission

Examples:

```text
unknown_action
action_not_read_only
budget_exhausted
target_proposition_mismatch
target_proposition_not_actionable
```

No investigation action executed.

Therefore:

```text
model proposal rejected
→ not consumed_actions
```

The event may remain in evaluator/diagnostic/system trace if useful, but it is not a completed/consumed investigation fact.

This is why historical `outcome = rejected` is a poor semantic fit inside `AttemptedInvestigationAction` for the evidence-refined contract.

### 4.2 Pre-execution stale action

If an action was valid at T1 but fresh trusted state at T2 makes its precondition false before execution:

```text
selected earlier
→ revalidation rejects/prunes before execution
→ not consumed
```

The new trusted state/catalog explains why the action is no longer useful. Do not pretend the investigation ran.

### 4.3 Transient provider / acquisition failure

Examples:

```text
timeout
transport_error
forbidden_or_rate_limited
other transient HTTP acquisition failure
```

These do not by themselves establish a domain/evidence result.

Therefore:

```text
transient acquisition failure
→ no false proposition update
→ no automatic consumed-action record
→ deterministic provider/executor may own bounded retry/backoff/defer behavior if separately authorized
```

The planner should not spend another model turn merely to say "retry the same HTTP GET".

### 4.4 Untrusted/malformed successful provider response

A response whose shape/encoding/path cannot be trusted is a provider/source-boundary failure, not target-domain evidence.

Fail closed. Any retry handling remains deterministic/evidence-bounded. Do not flatten it into a stable planner-visible domain problem automatically.

## 5. Planner-visible history shape — first-seam decision

For the current first seam, prefer the minimal model-visible shape:

```text
consumed_actions:
  - action_id
```

Do **not** include a coarse planner-facing outcome enum such as:

```text
completed | problem | rejected
```

in the base first-seam context.

Why:

1. `rejected` is not an executed investigation outcome.
2. `problem` collapses stable domain/evidence problems and transient operational failures that have different owners/retry semantics.
3. Findings that matter to future reasoning already belong in updated `PropositionAssessment` and/or `EvidenceGapPlanningEvidence`.
4. The planner's history responsibility is mainly to know that the exact investigation has already been meaningfully consumed, not to reconstruct the provider/domain result from one coarse label.

The full system may retain richer execution/audit records outside the model projection.

## 6. Findings and history remain separate

Correct multi-turn state shape:

```text
A1 executes
→ target declaration found / domain problem established
→ domain logic interprets result
→ propositions update
→ selected structured planning evidence updates when useful
→ A1 enters consumed_actions
→ next planner turn sees updated state + consumed action ID
```

Do not use:

```text
history.prose = "A1 found X ..."
```

as the only carrier of the result.

This keeps trusted investigation knowledge in its proper evidence/proposition owners and prevents free-form conversational memory from becoming product truth.

## 7. Idempotency does not imply semantic retry value

The current A1 exact-file read is read-only and logically idempotent for one immutable repository/revision/path.

That means repetition is comparatively safe from mutation side effects.

It does **not** mean repetition is useful:

```text
idempotent
!= informative to repeat indefinitely
```

Once a trusted typed result/problem has been produced for the same immutable state, blindly selecting the same action again has no justified new information value unless some separately trusted condition changes.

## 8. Transport retry vs semantic retry

Keep these owners separate:

```text
TRANSPORT / EXECUTION RETRY
same admitted bounded request
+ operational delivery/acquisition failure
→ deterministic provider/executor responsibility

SEMANTIC REPLANNING
trusted investigation state changed or a meaningful result/problem was produced
→ EvidenceGapPlanner may choose the next useful capability / no-tool disposition
```

This is a standard agent/tool-engineering separation even though UpgradePilot currently uses ordinary Python rather than an agent framework.

## 9. Relationship to action identity

`consumed_actions` suppresses blind repetition of the same **trusted bounded action instance** in the current seam.

Future richer action catalogs must not assume that one generic capability name is globally consumed forever. If the same capability can legitimately run against a different target/input/state, trusted catalog/action identity must represent that distinction explicitly.

Do not solve that hypothetical generalization inside current R2.

## 10. Relationship to remaining budget — deliberately deferred to next slice

Consumed-action history and budget are related but not identical.

For example, transient provider retries may cost time/network while remaining inside one deterministic execution responsibility; they should not automatically appear as several planner actions.

R2 has **not yet frozen** exactly when `remaining_budget` decreases relative to:

```text
model selection
admission
execution start
trusted typed result/problem
exhausted transient acquisition failure
```

That is the next budget slice.

## 11. Current evidence-backed owner split

```text
MODEL / EvidenceGapPlanner
→ choose among current admitted investigation capabilities
→ see consumed action IDs to avoid blind semantic repetition

DETERMINISTIC ADMISSION
→ revalidate current catalog / preconditions / budget / policy before execution

PROVIDER / EXECUTOR
→ acquisition and transport failure taxonomy
→ optional bounded operational retry policy when justified

DOMAIN EVIDENCE OWNER
→ interpret valid result/problem
→ update propositions / planning evidence

SYSTEM TRACE / EVALUATOR
→ may preserve proposal rejection, provider attempts, retry counts, latency, detailed execution diagnostics
```

Do not collapse these owners into one planner history list.

## 12. R4 implementation pressure

When the coherent experiment is built, the historical contract should be reconsidered rather than copied verbatim:

```text
historical:
attempted_actions: [{action_id, outcome}]

current R2 candidate:
consumed_actions: [action_id]
```

R4 tests should prove at least:

- consumed action blocks blind reselection;
- admission rejection does not masquerade as executed investigation history;
- updated findings live in propositions/planning evidence;
- transient provider failure is not flattened into trusted domain evidence;
- exact transport retry policy remains outside EvidenceGapPlanner unless later evidence changes the ownership decision.

No product runtime implementation is authorized by this record.

## 13. LbD concepts earned in this slice

- action lifecycle: proposal → admission → execution → interpretation → state update;
- planner history vs full execution/audit trace;
- consumed semantic investigation vs operational attempt;
- idempotency;
- transient vs stable/domain failure;
- transport retry vs semantic retry;
- pre-execution staleness / TOCTOU;
- model memory vs trusted system state;
- why expressive naming can reveal an ownership bug.

## 14. Next R2 slice

Continue with `remaining_budget`.

Questions to answer:

```text
What exactly is being budgeted?

Does one planner-selected investigation spend one unit at selection, admission, execution start, or trusted result?

Do deterministic transport retries spend planner budget or a different provider/execution budget?

Should budget be only remaining_steps, or does future multi-action planning need cost-aware structured budget?

What is justified now versus merely useful later?
```
