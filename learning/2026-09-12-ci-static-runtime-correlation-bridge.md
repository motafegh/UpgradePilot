# CI Static↔Runtime Correlation Bridge — Learning and Relearning Note

**Snapshot date:** 2026-09-12  
**Repository horizon:** `e8acb761b347a1bdc0dcc9ec4207221c4058b5e2`  
**Learning responsibility:** Understand why UpgradePilot needs a bounded static↔runtime CI correlation layer, how the first admitted bridge works, what `supported_runtime_correlated` actually means, and what the current proof still does not establish.  
**Status:** Frozen learning snapshot; not a live-state or continuation owner.

## 1. Why this responsibility exists

UpgradePilot already had two distinct evidence classes:

```text
STATIC WORKFLOW EVIDENCE
→ what the checked-in workflow declares

RUNTIME ACTIONS EVIDENCE
→ what GitHub reports actually ran for one exact run attempt
```

Those facts are useful, but they are not automatically the same fact.

The engineering problem was:

> How can UpgradePilot safely establish that one user-declared static workflow job/step corresponds to one exact runtime job/step observation without guessing across ambiguous workflow shapes?

The central mental model is:

```text
static declaration
+ runtime observation
≠ automatically correlated

static declaration
+ runtime observation
+ bounded deterministic identity conditions
→ correlation evidence
```

The correlation layer establishes **relationship/identity**. It does not independently establish dependency semantics, dependency installation, compatibility, or maintainer-action permission.

## 2. Where the bridge sits

```text
exact PR-head workflow file
        ↓
static workflow parser
        ↓
static jobs / steps / commands

exact workflow run + run attempt
        ↓
runtime jobs / runtime step summaries

STATIC + RUNTIME
        ↓
correlate_workflow_runtime(...)
        ↓
job/step correlation result
        ↓
dependency-CI interpretation
        ↓
supported_runtime_correlated
or conservative weaker/unresolved state
```

Responsibility boundary:

- GitHub/provider modules own factual static/runtime records;
- `workflow_runtime_correlation.py` owns only the bounded cross-source relationship;
- `dependency_exercise.py` interprets that relationship for dependency-CI evidence;
- maintainer-action synthesis remains a separate later responsibility.

## 3. The first admitted job-correlation class

Positive job correlation currently requires:

```text
static workflow revision == runtime run head SHA
+ workflow parses successfully
+ jobs are ordinary steps jobs
+ no strategy/matrix expansion
+ no reusable-workflow job
+ each static job has an explicit literal non-expression name
+ static job names are unique
+ runtime job names are unique
+ static-name set == runtime-name set
→ static job ↔ runtime job
```

A display name alone is not a trustworthy identifier. It becomes useful only inside the stronger safety envelope of exact workflow/run identity, literal names, uniqueness, and exact whole-set agreement.

If those conditions do not hold, UpgradePilot keeps the correlation result unresolved instead of inventing a relationship.

### Matrix pressure

A static job such as:

```yaml
name: Python ${{ matrix.python-version }}
```

can expand to runtime jobs such as:

```text
Python 3.12
Python 3.13
Python 3.14
```

The first bridge deliberately refuses to guess that mapping. This is a conservative capability boundary, not automatically a defect.

## 4. Step correlation inside an already-correlated job

Positive step correlation requires:

```text
no unresolved static StepProblem
+ explicit literal static step names
+ static step names unique
+ runtime step summaries present
+ runtime step numbers unique and strictly increasing
+ each static step name appears exactly once at runtime
+ static step-name order preserved as a runtime subsequence
→ static step ↔ runtime step
```

GitHub may insert runtime-only setup/post/completion steps, so UpgradePilot does **not** assume:

```text
static source index == runtime step number
```

### Representative example

Static:

```text
Build project
  0. Check out repository
  1. Install dependencies
```

Runtime:

```text
1. Set up job
2. Check out repository
4. Install dependencies
9. Post Check out repository
10. Complete job
```

The bridge can establish:

```text
static step 0 "Check out repository" ↔ runtime step 2
static step 1 "Install dependencies" ↔ runtime step 4
```

because names are literal/unique and their order is preserved despite runtime-only steps.

## 5. Correlation is not execution meaning

Correlation answers:

> Which static declaration does this runtime observation belong to?

A stronger successful-execution interpretation additionally requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

Visible `continue-on-error` matters because tolerated failure must not be silently interpreted as unmasked successful execution.

## 6. The two important dependency-CI states

### `supported_not_correlated`

Approximately:

```text
static dependency consumption supported
+ exact-head CI succeeded
+ no safe consuming-step ↔ runtime-step relationship established
```

### `supported_runtime_correlated`

Approximately:

```text
static dependency consumption supported
+ exact consuming step safely correlated to exact-attempt runtime step
+ runtime step completed/successful
+ no visible continue-on-error masking
```

The second state is stronger because UpgradePilot knows which runtime step corresponds to the static dependency-consuming step and has bounded successful runtime evidence for that step.

## 7. Important state-preservation distinction

If matrix/unsupported shape makes the correlation layer unresolved, UpgradePilot does not automatically discard weaker evidence already earned.

If it still has:

```text
supported static dependency consumption
+ successful exact-head CI
```

then dependency-CI coverage may remain:

```text
supported_not_correlated
```

Unresolved stronger evidence should not erase legitimate weaker evidence.

## 8. What the tests prove

Representative tests in `tests/test_workflow_runtime_correlation.py` cover:

- successful named job/step correlation with runtime-only extra steps;
- matrix/strategy rejection;
- reusable-workflow rejection;
- missing/dynamic/duplicate job names;
- exact static/runtime job-name-set agreement;
- missing/dynamic/duplicate step names;
- duplicate/unordered runtime step numbers;
- missing/ambiguous runtime step matches;
- static/runtime step-order mismatch.

Recorded real-environment proof for the slice:

```text
focused correlation tests                          PASS
nearest CI/investigation/provider/parser/synthesis PASS
full deterministic repository suite               549 tests OK
```

## 9. What this proof does NOT establish

The bridge does not prove:

- exact installed dependency version;
- selected/downloaded wheel or sdist;
- target wheel compatibility;
- behavioral compatibility;
- complete CI coverage;
- proposal safety;
- merge permission;
- targeted-check permission;
- investigate/block/defer permission.

A successful correlated install-like step is still much weaker than an exact runtime version/artifact witness.

## 10. Current limitations worth recognizing, not automatically fixing

The first bridge does not positively correlate:

- matrix/strategy jobs;
- reusable workflows;
- dynamic or missing job names;
- duplicate/ambiguous names;
- unsupported/malformed static structures.

Those become implementation priorities only if a real decision/evidence responsibility shows they matter.

The E-phase question is therefore not:

> How do we support every GitHub Actions shape?

It is:

> Which next missing proposition actually matters, and what smallest trustworthy evidence improvement can establish it?

## 11. Surrounding risks after the bridge

Current E inventory includes issues such as:

- false-positive static shell/direct-install recognition;
- changed-file patch evidence not fully bound to the frozen PR head;
- no normal exact target wheel-compatibility producer;
- target composition potentially losing an already-known CI `job_key`;
- no exact runtime dependency-version/artifact witness.

Transferable lesson:

> Strengthening a later evidence layer does not repair a weak earlier proposition. It can make a wrong earlier proposition look more convincing.

## 12. Depth calibration

### Must own

- static evidence and runtime evidence are separate;
- correlation establishes identity/relationship, not dependency truth by itself;
- positive correlation is conditional and fail-closed;
- `supported_runtime_correlated` is stronger than `supported_not_correlated` but still bounded;
- unresolved stronger evidence should not erase weaker evidence legitimately established;
- tests/proof must not be read as exact version/wheel/compatibility proof.

### Understand operationally

- why literal unique names + whole-set agreement + order constraints make matching safer;
- why runtime-only steps require subsequence matching;
- how `continue-on-error` affects successful-execution interpretation;
- how unresolved correlation flows into downstream dependency-CI interpretation.

### Lookup-level

- exact dataclass field layouts;
- every `reason` string;
- helper details such as `_first_duplicate`;
- exact fixture-construction syntax.

### Deferred deliberately

- matrix/reusable workflow correlation algorithms;
- full Actions expression evaluation;
- job-log parsing;
- exact package-manager artifact reconstruction;
- broader maintainer-action permissions.

## 13. Fast relearning route

1. Recall: **static declaration + runtime observation ≠ automatically correlated**.
2. At snapshot `e8acb761...`, read `correlate_workflow_runtime()` and `_correlate_job_steps()` in `src/upgradepilot/ci/workflow_runtime_correlation.py`.
3. At the same snapshot, inspect the successful subsequence, matrix rejection, and order-mismatch tests in `tests/test_workflow_runtime_correlation.py`.
4. Re-state `supported_not_correlated` vs `supported_runtime_correlated`.
5. Name at least three things the bridge still does not prove.
6. Only then inspect current `MEMORY.md` if the goal is to return to present-day project work rather than relearn this frozen snapshot.

## 14. Source-grounded audio/video/quiz transform

For a transform intended to teach **this frozen snapshot**, use sources from repository horizon `e8acb761b347a1bdc0dcc9ec4207221c4058b5e2`:

1. this learning note;
2. snapshot-pinned `src/upgradepilot/ci/workflow_runtime_correlation.py`;
3. snapshot-pinned `tests/test_workflow_runtime_correlation.py`;
4. optional snapshot-pinned `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md` when the engineering progression is useful.

Do **not** silently combine this frozen note with later mutable `main` versions of those files.

If the goal is instead to learn the **current implementation**, first orient from current `MEMORY.md` and current owners/source/tests, then generate a current-source transform rather than treating this old snapshot as current truth.

## 15. Retrieval and transfer questions

1. Why is matching a static step name to a runtime step name unsafe unless exact workflow identity, uniqueness, and ordering constraints also hold?
2. If matrix correlation is unresolved but static consumption and successful exact-head CI remain supported, why can `supported_not_correlated` remain valid?
3. What additional evidence is needed before claiming an exact dependency version or exact wheel executed in CI?
4. If runtime correlation is perfect but static command recognition falsely says a dependency was consumed, why can the final evidence still be wrong?
5. If a future real case requires matrix support, what proposition should the new implementation prove rather than simply “support matrices” in general?

## 16. Evidence anchors

Snapshot `e8acb761b347a1bdc0dcc9ec4207221c4058b5e2`:

- `src/upgradepilot/ci/workflow_runtime_correlation.py`
- `src/upgradepilot/ci/dependency_exercise.py`
- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`
- `tests/test_maintainer_action.py`
- `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`

This note is a frozen learning snapshot. Current continuation always comes from current `MEMORY.md`.

`UP-SKILL:upgradepilot-learning-artifact`
