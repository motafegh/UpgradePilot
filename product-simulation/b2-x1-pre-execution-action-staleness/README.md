# B2/X1 Pre-Execution Action-Staleness Transfer Evaluation

**Date:** 2026-08-28  
**Status:** PRODUCT-SIMULATION CROSS-CASE EVALUATION — non-controlling discovery/transfer evidence  
**Evaluated main revision:** `a30c18bf067af82d2f016ce8d6e9ce495bf5772c`  
**Primary preserved evidence:** S007 plus current B2/X1 planner/admission source  
**Related prior transfer asset:** `../b2-x1-no-tool-disposition-transfer/README.md`

## 1. Evaluation question

This evaluation asks one bounded lifecycle question:

> What should happen when an investigation action looked useful when selected, but trusted evidence changes before execution so that the action no longer has discriminating value or no longer satisfies its action precondition?

The question is intentionally narrower than general agent-loop architecture.

It does **not** ask for:

- a new numbered scenario;
- a second B2/X1 executable action;
- a generic workflow/state-machine framework;
- a new product runtime schema;
- product/experiment implementation during the current Learning-Only pause;
- autonomous concurrent workers;
- final production orchestration semantics.

This is analysis/transfer work only. Current `MEMORY.md` permits read/inspect/trace/explain/compare/diagnose during the Learning-Only pause while product/experiment implementation remains paused.

---

## 2. Why this has its own folder

The responsibility is distinct from the previous no-tool-disposition evaluation.

That prior evaluation asked:

```text
Given the current trusted state,
why should the planner choose stop vs defer vs unresolved?
```

This evaluation asks:

```text
A plan was selected from trusted state at T1.
Trusted state changes before execution at T2.
Is the selected action still authorized/useful at T2?
```

That is a lifecycle/temporal correctness pressure rather than merely a one-turn classification pressure.

A dedicated folder is therefore proportionate, but the folder starts with only this one record. No empty bundle or new scenario machinery is created.

---

## 3. Evidence method

The evaluation used the smallest evidence route that can answer the question:

1. re-check current `main` live-state boundary and selected Learning-Only plan;
2. synchronize the product-simulation branch without dropping prior simulation assets;
3. inspect S007 admission-time investigation candidates;
4. inspect S007 final proposition/evidence state and stopping rationale;
5. inspect the earlier cross-case Conversation-C pressure test;
6. inspect current `AllowedInvestigationAction`, `InvestigationSnapshot`, and `admit_agent_plan(...)` semantics;
7. inspect the current Phase-4A runner to see which snapshot is actually used for admission;
8. derive one controlled current-contract transfer using the existing A1 action rather than fabricating an S007 resolver action;
9. separate current capability, future pressure, and speculative implementation options.

No external target was mutated. No model was called. No local test/runtime PASS is claimed.

---

## 4. S007 establishes the real temporal pressure

### 4.1 T1 — execution is a plausible candidate

At S007 admission, the owned question was whether BiomedParse PR #96's exact Torch/TorchVision/TorchAudio requirements could form one coherent package family in the documented Python-3.10.14 / CUDA-12.4 context.

Reasonable candidate observations included:

```text
1. inspect exact target-relevant TorchVision wheel metadata
2. run an isolated resolver dry-run
```

The resolver was therefore not nonsense or an obviously invalid idea. At that evidence state it could plausibly have produced discriminating corroboration.

### 4.2 T2 — stronger evidence arrives before execution

Further authoritative source inspection established the TorchVision 0.21 release/build contract strongly enough to show that its retained family pins Torch to the 2.6 release family, while the proposal independently requires `torch==2.8.0`.

The exact equality constraints therefore have no common Torch version.

The owned proposition changed from needing further discrimination to being deterministically closed/refuted at the package-family layer.

### 4.3 The previously plausible check loses value

Once the stronger evidence was admitted:

```text
owned package-family proposition resolved/refuted
→ resolver dry-run becomes corroborative
→ additional TorchAudio metadata becomes redundant
→ runtime/GPU/API work remains downstream/inactive
→ no further check required for the owned question
```

This is not ordinary action completion.

The resolver did **not** execute and produce the new evidence. The action became stale because **other admitted evidence changed the state before that action executed**.

---

## 5. Core transfer invariant

S007 supports this bounded invariant:

> **Action selection is a proposal justified by a particular trusted evidence state. Selection is not permanent execution authorization. Before execution, the action must still be useful and satisfy its trusted preconditions under the current admitted state.**

In compact form:

```text
T1 snapshot S1
→ action A has discriminating value
→ select A

new trusted evidence
→ snapshot becomes S2

before execution:
validate A against S2

if A is still useful/actionable
→ execution may remain admitted

if A is no longer useful/actionable
→ prune/reject stale A
→ continue from S2 rather than executing because A was selected earlier
```

This is an evaluation-derived reasoning invariant. It is not yet a product architecture mandate.

---

## 6. Standard engineering concept: TOCTOU / stale-plan control

The closest general engineering name is a **time-of-check to time-of-use (TOCTOU)** or stale-state problem.

Here the relevant times are:

```text
CHECK / DECISION TIME
→ planner sees snapshot S1
→ planner selects A

USE / EXECUTION TIME
→ system is about to execute A
```

If trusted state can change between those points, correctness cannot rely only on what was true at selection time.

In agent/orchestration terms this can also be described as:

- stale plan / stale action;
- pre-execution revalidation;
- optimistic concurrency-style validation;
- state-version or snapshot-fingerprint checking when concurrency eventually justifies it.

These names are useful because the underlying problem is not specific to LLMs. The LLM merely makes the planning decision; the temporal correctness problem exists whenever a plan and its execution are separated by changing state.

### Learning/adoption boundary

Understanding TOCTOU and optimistic-concurrency patterns is relevant now.

Adopting a general state machine, middleware layer, pre-tool hook framework, checkpoint system, or distributed concurrency mechanism is **not** justified by this evidence alone.

---

## 7. Current contract already contains useful revalidation ingredients

`AllowedInvestigationAction` is not only an action name. It carries trusted preconditions including:

```text
required_proposition_state
required_evidence_coverage
exact repository
exact revision
exact path
action target proposition
mutation class
result families
```

For the current A1 action:

```text
required proposition state    = unresolved
required evidence coverage    = insufficient
```

`admit_agent_plan(snapshot, plan)` then checks, for a `choose_action` proposal:

- the target proposition exists;
- the action is in the current trusted catalog;
- it is read-only;
- it has not already been attempted;
- step budget remains;
- the action and target proposition match;
- result categories match the trusted action contract;
- the **current proposition state/coverage supplied to admission still matches the action precondition**.

Therefore the deterministic admission function is already capable of rejecting a plan whose action precondition is stale **if admission is performed against the updated trusted snapshot**.

This is an important positive transfer finding: S007 does not automatically require a new low-level action-precondition concept.

---

## 8. Controlled current-contract transfer without inventing a second action

The current X1 catalog contains only one independently justified executable action:

```text
A1 = acquire_exact_target_python_declaration
```

S007's resolver dry-run is not an admitted B2/X1 action. Fabricating a resolver action merely to test staleness would violate the accepted one-action claim boundary.

Instead, the same temporal pattern can be transferred to the existing real A1 semantics.

### 8.1 T1 — A1 is legitimately selectable

Use the accepted S001-style state:

```text
exact_target_python_declaration_established
→ unresolved / insufficient

A1 available
→ requires unresolved / insufficient
```

A model plan can legitimately be:

```text
choose_action(A1)
```

### 8.2 T2 — equivalent trusted evidence arrives before A1 executes

Suppose another deterministic acquisition path or already-running evidence operation admits the exact target declaration before A1 executes:

```text
requires-python = ">=3.10"
grounded dropped line = Python 3.8

→ exact_target_python_declaration_established = established / sufficient
→ declared_python_range_intersects_dropped_line = refuted / sufficient
```

The repository/revision may remain exactly the same. What changed is the **epistemic/evidence state**.

### 8.3 Re-admitting the T1 plan against T2 state

If the old A1 plan is passed to `admit_agent_plan(...)` with the updated T2 snapshot while A1 remains listed, the action no longer satisfies:

```text
required state = unresolved
required coverage = insufficient
```

The existing code path therefore returns the admission problem:

```text
target_proposition_not_actionable
```

Alternatively, if a future snapshot builder removes no-longer-actionable actions from `allowed_actions`, the same stale plan would fail earlier as an action no longer in the current catalog.

Either behavior can safely block execution.

### 8.4 Proof limit

This is a **static code-path transfer derivation**, not a newly executed test.

The current Learning-Only environment has no local WSL/runtime validation in this session, so this record does not claim an observed runtime PASS for the controlled variant.

---

## 9. The actual missing future responsibility is orchestration freshness

The current contract can reject stale preconditions when given fresh state.

The unresolved lifecycle question is:

> **Which trusted snapshot does the execution boundary use immediately before capability execution?**

The current Phase-4A development runner does:

```text
case
→ render request from case.snapshot
→ model response
→ parse
→ admit_agent_plan(case.snapshot, plan)
```

It reuses the same immutable development-case snapshot for request generation and admission.

That is appropriate for the current smoke because:

- the cases are frozen development fixtures;
- no real capability executes;
- no independent evidence acquisition occurs during the request;
- the purpose is transport/schema/basic planner capability probing.

Therefore this is **not a current Phase-4A defect**.

But a future execution-capable loop cannot assume that the planning snapshot is necessarily still current at execution time.

---

## 10. Four distinct kinds of staleness

S007 helps avoid collapsing several different freshness problems.

### 10.1 Source-identity staleness

```text
repository / PR / revision changes
```

Current exact repository/revision binding already addresses much of this class.

### 10.2 Evidence-state / epistemic staleness

```text
same repository/revision
+
new trusted evidence changes proposition state/coverage
```

S007 is primarily this class.

A revision hash alone cannot detect it because the target source may be unchanged while UpgradePilot's admitted knowledge improves.

### 10.3 Action-history staleness

```text
same action was completed/problem/rejected elsewhere or earlier
```

Current `attempted_actions` plus `action_already_attempted` admission already gives a first bounded guard.

### 10.4 Policy/budget/catalog staleness

```text
remaining budget changes
or action becomes disallowed/removed
or action policy changes before execution
```

The current admission function can evaluate these values when the supplied snapshot/catalog reflects the latest trusted state.

The common requirement is therefore not "add one stale flag." It is to ensure execution authority is evaluated against the right current state.

---

## 11. S007 is not the same as S001 post-action replay

These transitions must remain distinct.

### S001 post-action replay

```text
A selected
→ A executes
→ A result admitted
→ state changes because A completed
→ construct next planning turn
→ stop
```

### S007 pre-execution staleness

```text
A selected
→ A has NOT executed
→ different/new trusted evidence changes state
→ A loses discriminating value before use
→ cancel/prune A
```

Both require state re-evaluation, but at different lifecycle points.

A system that only re-plans **after** tool completion can still execute unnecessary stale actions.

---

## 12. Failure heuristics this pressure exposes

### H-ST-01 — selected once means authorized forever

```text
planner selected A at T1
→ execute A later without rechecking state
```

Fails S007.

### H-ST-02 — exact revision means knowledge state is fresh

```text
repository/revision unchanged
→ snapshot still semantically current
```

Fails when new evidence about the same revision arrives.

### H-ST-03 — prior admission means permanent permission

```text
A passed admission at T1
→ no need to validate again at T2
```

Confuses historical validity with current validity.

### H-ST-04 — repeat prevention solves all stale actions

```text
action not in attempted_actions
→ action is still worth executing
```

False. S007's resolver had never been attempted; it still became redundant.

### H-ST-05 — no external mutation means no TOCTOU risk

Read-only evidence acquisition can still change the trusted epistemic state and invalidate a planned read-only investigation.

### H-ST-06 — stronger evidence only matters after the selected action finishes

Evidence may arrive through another source/operation before execution. The selected action must not block or outrank that stronger state.

---

## 13. Minimal future implementation shapes worth understanding

This evaluation does **not** select an architecture, but it narrows the credible implementation family if/when an execution-capable loop becomes active.

### Option A — reconstruct and re-admit immediately before execution

```text
planner returns plan bound to S1
→ deterministic orchestration refreshes/reconstructs trusted current snapshot S2
→ admit old plan against S2
→ execute only if still admitted
```

This is the smallest conceptual shape and reuses current action preconditions.

### Option B — bind plan to a snapshot identity/fingerprint

```text
plan created from snapshot version/fingerprint V1
→ execution boundary sees current V2
→ stale mismatch
→ reconstruct/revalidate/replan
```

Potentially useful if real concurrency, asynchronous evidence acquisition, or longer-lived plans eventually exist.

No evidence currently justifies adding this mechanism to the Phase-4A smoke.

### Option C — pre-tool hook / middleware / lifecycle guard

Some agent frameworks expose `before_tool`, middleware, interceptor, or callback surfaces where a current-state validation could run.

That is a recognizable implementation pattern, not a requirement to adopt a framework or hook layer. UpgradePilot's current direct deterministic function boundary may be simpler if/when the responsibility is implemented.

### Option D — explicit state-machine transition guard

A future planner loop could model states such as planned → validated → executing, with validation guarding the transition.

Again, this should be earned by actual lifecycle complexity rather than added for conceptual neatness.

---

## 14. Transfer finding — action preconditions should be treated as current-state predicates

### F-ST-01 — CONFIRMED

The strongest reusable interpretation of the existing action contract is:

```text
required_proposition_state
required_evidence_coverage
...
```

are not only conditions for *generating/selecting* an action.

They are naturally usable as **current-state execution predicates**.

That gives deterministic code a clean way to say:

```text
this action was legitimate earlier
but no longer matches the current trusted proposition state
→ do not execute
```

This interpretation is supported by the existing `admit_agent_plan(...)` state/coverage recheck.

---

## 15. Transfer finding — the missing boundary is freshness ownership, not another planner action

### F-ST-02 — CONFIRMED

S007 does not justify adding a resolver action to the first X1 catalog.

The current claim can remain one-action.

The actual future question is orchestration ownership:

```text
who reconstructs/owns the latest trusted snapshot before execution?
who decides that the selected plan is still based on current state?
```

That belongs to deterministic orchestration/integration if product work reaches real action execution.

---

## 16. Transfer finding — identity freshness and evidence freshness are different

### F-ST-03 — CONFIRMED

Exact Git revision identity is necessary but not sufficient for planner-state freshness.

S007 shows:

```text
same target revision
+
more authoritative evidence
→ different justified investigation state
```

A future freshness model must not infer epistemic freshness merely from repository identity equality.

---

## 17. Transfer finding — no current implementation blocker

### F-ST-04 — CONFIRMED

The present Phase-4A development smoke executes no capability and uses frozen development fixtures.

Therefore pre-execution state drift is outside its immediate responsibility.

Do not delay the first smoke to add:

- snapshot versioning;
- concurrent state coordination;
- pre-tool hooks;
- generic checkpoints;
- a state-machine framework;
- a second action;
- background evidence workers.

Revisit the finding before real action execution or a longer-lived planner loop is integrated.

---

## 18. Proposed future pressure test when implementation reaches execution

When real execution becomes active, the smallest useful regression/evaluation shape is not a new public scenario.

Use an existing admitted action with two trusted snapshots:

```text
S1
→ target proposition unresolved/insufficient
→ action selected

S2
→ before action execution, proposition established/refuted or otherwise no longer actionable

old plan + S2
→ deterministic execution admission must reject/prune the stale action
```

The existing S001/A1 semantics are enough to express that controlled variant without contaminating the one-action claim.

A later executable test could verify the exact rejection path once implementation authorization resumes.

---

## 19. Relationship to no-tool disposition transfer

The two evaluation assets together expose both sides of bounded orchestration correctness.

### No-tool transfer

```text
no capability executes
but wrong stop/defer/unresolved can change control flow incorrectly
```

### Pre-execution staleness transfer

```text
an action may have been correct when selected
but later execution can become incorrect/redundant after state changes
```

Together:

> **Safe agentic orchestration requires more than restricting tools. It also requires temporally correct control-flow decisions against current trusted state.**

This remains an evaluation/design pressure, not a product architecture conclusion.

---

## 20. Methods and barriers encountered in this evaluation

These are operational/evaluation-history facts, not product evidence.

### M/B-01 — moving `main` during simulation work

`main` advanced from the previous synchronized point to:

```text
a30c18bf067af82d2f016ce8d6e9ce495bf5772c
```

with the compact B2/X1 Learning-Only mastery plan and its `MEMORY.md` selection.

The branch was re-synchronized before the S007 evaluation so the analysis did not silently rely on stale live-state governance.

### M/B-02 — simulation work remains analysis-only under current live boundary

The selected Learning-Only plan explicitly keeps implementation paused while inspection/comparison/diagnosis remain active.

Therefore this evaluation records a future execution pressure but does not modify planner/product code or tests.

### M/B-03 — current X1 catalog cannot faithfully encode S007 resolver execution

Only `acquire_exact_target_python_declaration` is admitted as an executable planner action.

Creating a fake resolver action would contaminate the current X1 claim. The evaluation therefore used:

```text
real S007
→ establishes the lifecycle principle

existing S001/A1 contract
→ tests whether the current action-precondition model can carry that principle
```

This split is deliberate evidence discipline, not a missing-case workaround.

### M/B-04 — no runtime validation available in this session

The A1 stale-plan rejection is derived statically from current source behavior. No local WSL test was executed, so no runtime PASS is claimed.

### M/B-05 — connector branch-sync mistake was corrected before analysis continued

During GitHub connector synchronization, a temporary probe file was accidentally committed to the simulation branch.

It was immediately removed by resetting the branch to the prior verified branch head before the final merge-tree construction. Candidate merge commits created while checking tree composition were never pointed to by the branch.

The final synchronization was rebuilt explicitly as:

```text
latest main tree
+ retained simulation inventory blob
+ retained no-tool evaluation blob
→ merge commit with both histories
```

A final branch comparison confirmed the branch was `0` commits behind current `main` before substantive S007 analysis continued.

This incident changes no product/simulation evidence conclusion, but it is retained here because repository-operation barriers and their resolution are part of the requested work history.

---

## 21. Claim limits

This evaluation establishes only:

- S007 is a real example of a useful investigation becoming redundant before execution;
- this is distinct from post-action replay;
- current action-precondition/admission semantics are compatible with rejecting a stale action if supplied fresh trusted state;
- current Phase-4A does not own a real pre-execution freshness window because it executes no capability;
- future execution-capable orchestration should explicitly revisit freshness/revalidation ownership.

It does **not** establish:

- production concurrency requirements;
- that snapshot hashing/versioning is mandatory;
- a universal TOCTOU solution;
- that current source has a runtime bug;
- that a framework/hook/state-machine layer is needed;
- a second action catalog entry;
- protected evaluation outcomes;
- planner reliability;
- update compatibility/safety;
- maintainer action.

---

## 22. Stopping decision

This evaluation has reached its bounded stop condition.

We have enough evidence to distinguish:

```text
selection-time validity
!=
execution-time validity
```

and enough current-source evidence to show that the existing action contract can participate in future revalidation without inventing new action semantics.

More work now—such as implementing a snapshot version, adding an S007 resolver tool, or building a generic lifecycle framework—would cross from simulation analysis into premature product design/implementation during the current Learning-Only pause.

### Bounded disposition

```text
S007 pre-execution action-staleness pressure
→ CONFIRMED as a future execution-loop responsibility
→ NOT a blocker for current Phase-4A development smoke
→ NO second action required
→ NO new numbered scenario required
→ preserve as future transfer/regression evidence
→ revisit when product work reaches real capability execution / multi-turn planner lifecycle
```
