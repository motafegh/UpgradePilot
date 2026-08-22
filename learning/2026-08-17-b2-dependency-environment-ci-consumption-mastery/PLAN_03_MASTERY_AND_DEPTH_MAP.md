# Plan 03 — Mastery and Depth Map

**Companion to:** `PLAN_03_GENERALIZATION_PRESSURE_S011_AND_S005.md`  
**Purpose:** define what Plan 03 must prove about transfer/generalization without creating unnecessary new source or technology mastery  
**Authority:** subordinate to the learning contract, live `MEMORY.md`, active source/tests, and Plan 03  
**Important rule:** Plan 03 is **not primarily a new-code mastery plan**. Its main target is transfer of the already learned model into materially different real cases.  
**Revised:** 2026-08-22 — explicit transfer-depth rationale and parallel architecture/correctness audit added

## 1. Depth labels

### OWN / MASTER
Ali can predict and explain the proposition, evidence state, relevant source branch, proof boundary, and material engineering judgment with reduced assistance.

### STRONG WORKING UNDERSTANDING
Ali can follow the relevant source slice and explain why the changed case produces a different result without assuming the current design is automatically correct.

### NAVIGATE / RECOGNIZE
Ali knows which previously learned source responsibility applies and can reopen it when needed.

### OPERATIONAL BACKGROUND
Ali understands the external technology only enough to understand and audit the real case.

### DEFER
No implementation/internal mastery unless a later authorized responsibility explicitly selects it.

## 2. Plan-03 end-state and why this depth matters

By the end of Plan 03, Ali should demonstrate that the S001 model is **transferable rather than memorized** by predicting and explaining why S011 becomes environment non-selection and why S005 is architecture/support pressure that current code must not pretend to solve.

Why this plan emphasizes reasoning over new-code mastery:

```text
S001 can be memorized as one happy path.
S011 and S005 change the environment mechanism enough to reveal whether Ali actually understands
the proposition boundaries and whether the architecture generalizes for the right reasons.
```

This plan does not require ownership of new large modules because the learning value comes from applying/auditing already learned mechanisms under changed evidence, not from maximizing source breadth.

## 3. Chunk 1 — S011 optional-extra non-selection

### MASTER — evidence reasoning

Ali should be able to explain and predict:

```text
affected dependency source environment = mlx
selected static environment = dev
→ affected environment is not established as selected
→ downstream changed-environment CI coverage cannot be promoted from green standard CI
```

He should distinguish:

- `not_established` from runtime absence;
- `not_established` from `unresolved` analysis failure;
- macOS CI from actual Apple-Silicon/MLX environment coverage;
- source environment identity from selected environment identity.

**Why this depth:** this is the first materially different transfer case for the environment model. Ali must be able to predict the evidence state from the proposition rather than copying the S001 outcome; the distinction will recur whenever affected and selected environments differ.

### `src/upgradepilot/dependency/environment_selection.py`

**NAVIGATE / REUSE:** revisit only `OptionalExtraSelector`, the relevant selector-recognition branch, and the exact static command interpretation required by S011.

**Why not deeper:** Plan 01 already selected the environment-selection responsibility for ownership. Plan 03 only needs the decisive branch to test transfer; rereading the entire source would measure repetition rather than generalization.

### `src/upgradepilot/dependency/environment_membership.py`

**STRONG WORKING UNDERSTANDING / TRANSFER TARGET:** understand the exact comparison branch that yields `not_established` for affected `mlx` versus selected `dev`, including normalization/project-root guards only where they affect the outcome.

**Why this depth:** this branch carries the changed-case decision we are testing, but the file's central comparison mechanism was already learned in Plan 02. We need enough source control to verify/audit the prediction without creating redundant whole-file mastery.

Ali should be able to verify his prediction against executable source rather than rely on the remembered S001 result.

### CI coverage source

**NAVIGATE / REUSE FROM PLAN 02:** follow only the downstream consequence needed to show that green CI does not manufacture coverage for the mismatched environment.

### Representative tests

- `tests/test_project_source_environment_membership.py`;
- `tests/test_ci_dependency_coverage.py` for the S011-shaped consequence.

At least one test should be used to explain why mismatch is different from unresolved analysis.

### OPERATIONAL BACKGROUND ONLY

- Python optional extras;
- editable install `pip install -e ".[dev]"`;
- MLX as Dictare's Apple-Silicon-related optional stack.

**Why operational only:** these concepts are needed to interpret the real Dictare evidence and understand why `dev` and `mlx` are different activation paths. UpgradePilot is not implementing MLX, pip editable-install internals, or Apple runtime behavior here.

### Parallel audit focus

- Does the current comparison model correctly represent an affected-extra vs selected-extra mismatch?
- Is `not_established` the narrowest accurate state, or does any current branch accidentally imply runtime absence?
- Do platform/job labels risk being treated as environment activation evidence without actual selection proof?
- Are normalization/project-root guards proportionate and correctly owned?

### DEFER

- MLX implementation;
- Apple hardware/runtime internals;
- generic optional-dependency packaging theory;
- every branch in environment selection/membership source.

## 4. Chunk 2 — S005 tox-mediated uv-lock pressure

### MASTER — architecture-transfer reasoning

Ali should be able to explain:

```text
historical target mechanism:
tox environment
→ uv-venv-lock-runner
→ locked environment / pytest path

current UpgradePilot admitted static syntax:
directly recognized project-environment selection mechanisms
```

and therefore reason:

> A semantic concept such as “uv-lock-backed environment consumption” must not be equated with one literal GitHub Actions syntax such as direct `uv sync`.

The correct current result may be **outside current admitted support / abstain / defer**, depending on current source. The important skill is recognizing this boundary rather than inventing support.

**Why this depth:** S005 tests whether the learned architecture is semantic or merely syntax-shaped. This is a high-value engineering judgment because future repositories can express the same environment responsibility through mediation rather than direct commands.

### `src/upgradepilot/dependency/environment_selection.py`

**NAVIGATE / REUSE:** inspect only enough current selector-admission logic to answer whether tox-mediated formation is represented.

### `src/upgradepilot/dependency/uv_membership.py`

**NAVIGATE / REUSE:** inspect only if needed to distinguish membership capability from the missing upstream selection/mediation interpretation.

### CI composition/evaluation source

**NAVIGATE / REUSE:** only as needed to show why downstream evidence cannot repair a missing/unrepresented earlier selection mechanism.

**Why source stays navigation-only:** the central learning question is whether the existing abstraction admits the real mechanism, not how every downstream helper works. Deep source study would not improve the architectural transfer judgment unless a real branch proves decisive.

### OPERATIONAL BACKGROUND ONLY

- tox as a Python environment/test orchestration tool;
- tox environment at practical depth;
- `uv-venv-lock-runner` as the mediation mechanism in S005.

**Why operational only:** Ali needs enough external-mechanism knowledge to recognize mediated lock/environment use and challenge syntax overfitting; plugin internals are not required unless UpgradePilot later implements tox support.

### Parallel audit focus

- Does the current architecture model a semantic environment responsibility or overfit to direct CLI syntax?
- Is current abstention a safe bounded limitation, or does it expose coupling that would make generalization expensive?
- Are we distinguishing “unsupported interpretation” from an ordinary negative evidence state?
- Do not invent a tox rationale or support path that current source/case evidence does not establish.

### DEFER

- tox configuration engine internals;
- plugin implementation;
- generic runner abstraction;
- implementing tox support;
- universal environment-consumption architecture.

## 5. Chunk 3 — Three-case transfer model

### MASTER — changed-case classification

Ali should be able to compare, before receiving a final summary:

```text
S001
explicit selected docs environment
+ reachable changed dependency
→ positive selected-environment membership / static consumption path

S011
explicit affected mlx environment
+ selected dev environment
→ not_established for affected-environment selection/membership

S005
indirect tox-mediated environment path
→ architecture/support pressure; do not invent unsupported interpretation
```

Ali should be able to say:

- what proposition is being tested in each case;
- what evidence state is justified;
- which source responsibility owns the decisive step;
- what transferred from S001;
- what did not transfer;
- whether the difference is a normal negative/non-establishment state, unresolved evidence, or an admitted-support limitation;
- whether any current architectural assumption looks correct, bounded-but-fragile, or still uncertain.

**Why this depth:** this comparison is the actual proof that the mental model generalizes. It also trains the ability to distinguish a product evidence state from a capability-support limitation—an important future investigation/design skill.

## 6. Source mastery rule for Plan 03

Plan 03 should generally **not add a new Career-grade whole responsibility merely because another file is opened**.

The expected pattern is:

```text
previously owned mechanism
→ materially changed real case
→ Ali predicts outcome
→ inspect only decisive source branch/test
→ compare prediction with evidence
→ audit correctness/generalization
→ explain transfer / non-transfer
```

A source branch becomes a new deeper ownership target only if:

- it introduces a genuinely new responsibility required by the case; or
- a later authorized modification/failure enters that branch materially.

Otherwise, this plan should strengthen transfer, not expand source breadth.

## 7. Concepts to MASTER

- optional-extra / dependency-group identity at the level needed to compare affected vs selected environment;
- `not_established` versus `unresolved` versus positive support;
- green CI is non-discriminating when the affected environment was not established as selected;
- semantic architecture must not overfit to literal syntax;
- historical case evidence != current implementation support;
- current abstention/support limit can be correct without proving the architecture is optimal forever;
- implementation fact versus engineering judgment;
- changed-case prediction before answer.

**Why these concepts deserve mastery:** they determine whether Ali can correctly classify new repositories/cases without forcing them into the S001 pattern and can challenge current support boundaries without confusing critique with implementation authorization.

## 8. What Plan 03 must NOT become

Do not turn this plan into:

- an MLX course;
- a tox course;
- a third deep pass through `uv_membership.py`;
- rereading `workflow_commands.py` or `dependency_exercise.py` end to end;
- implementing S005 support;
- collecting more technologies for résumé breadth;
- memorizing S001/S011/S005 outputs without understanding the proposition difference;
- assuming current abstention or current architecture is automatically correct because it is conservative.

## 9. Plan-03 completion evidence

Plan 03 is strong enough to hand to Plan 04 when Ali can, with reduced assistance:

1. predict S011 `mlx` vs `dev` as `not_established` and explain why;
2. distinguish non-selection from unresolved analysis and runtime absence;
3. verify the decisive S011 branch/test in current source;
4. explain why green CI cannot become changed-`mlx` coverage;
5. explain tox-mediated S005 at the minimum operational depth and why deeper tox knowledge is unnecessary now;
6. predict that literal direct-`uv sync` assumptions do not safely generalize to S005;
7. identify where current support should abstain/defer rather than overclaim;
8. compare S001/S011/S005 using propositions/evidence states rather than memorized outcomes;
9. explain why transfer reasoning—not new whole-file mastery—is the required depth in this plan;
10. critically evaluate at least one current support/generalization assumption without presuming current design quality;
11. name what source knowledge transferred and what did not;
12. preserve one concise changed-case transfer record in `LEARNING_MEMORY.md` when demonstrated;
13. preserve any material durable architecture/correctness finding through the contract's audit route when warranted.

Plan 03's strongest Career value is **transfer evidence**, not another giant source-ownership claim.
