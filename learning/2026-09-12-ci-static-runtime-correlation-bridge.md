# CI Static↔Runtime Correlation Bridge — Learning and Relearning Note

**Snapshot date:** 2026-09-12  
**Repository horizon:** `e8acb761b347a1bdc0dcc9ec4207221c4058b5e2`  
**Learning responsibility:** Understand why UpgradePilot needs a bounded static↔runtime CI correlation layer, how the first admitted bridge works, what `supported_runtime_correlated` actually means, and what the current proof still does not establish.  
**Status:** Frozen learning snapshot; not a live-state or continuation owner.

## 1. Why this responsibility exists

UpgradePilot already had two different kinds of CI evidence:

```text
STATIC WORKFLOW EVIDENCE
→ what the checked-in workflow declares

RUNTIME ACTIONS EVIDENCE
→ what GitHub reports actually ran for one exact run attempt
```

Those facts are useful, but they are not automatically the same fact.

The key engineering problem was:

> How can UpgradePilot safely establish that one user-declared static workflow job/step corresponds to one exact runtime job/step observation without guessing across ambiguous workflow shapes?

That is the job of the correlation bridge.

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

The correlation layer establishes **relationship/identity**. It does not independently establish dependency semantics, dependency installation, compatibility, or maintainer action permission.

## 2. Where the bridge sits in the real flow

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

Important ownership boundary:

- GitHub/provider modules own factual static/runtime records;
- `workflow_runtime_correlation.py` owns only the bounded cross-source relationship;
- `dependency_exercise.py` interprets that relationship for dependency-CI evidence;
- maintainer-action synthesis remains a separate later responsibility.

## 3. The current admitted job-correlation class

The first positive bridge intentionally supports only a narrow ordinary-workflow class.

Positive job correlation requires:

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

Why so strict?

Because a display name by itself is not a trustworthy identifier. It becomes usable only inside a stronger safety envelope: exact workflow/run identity, literal names, uniqueness, and exact whole-set agreement.

If any of those conditions fail, UpgradePilot does not invent a relationship. The result stays `unresolved` at the correlation layer.

### Real pressure: matrix jobs

A static job such as:

```yaml
name: Python ${{ matrix.python-version }}
```

can expand into several runtime jobs such as:

```text
Python 3.12
Python 3.13
Python 3.14
```

There is no simple literal one-to-one display-name identity anymore. The first bridge therefore refuses to guess matrix correlation.

That is a deliberate conservative boundary, not automatically a defect.

## 4. Step correlation inside an already-correlated job

Once a job is safely correlated, the bridge applies another bounded identity contract to user-declared steps.

Positive step correlation requires:

```text
no unresolved static StepProblem
+ every relevant static step has an explicit literal name
+ static step names are unique
+ runtime step summaries exist
+ runtime step numbers are unique
+ runtime step numbers are strictly increasing
+ each static step name appears exactly once at runtime
+ static step-name order is preserved as a runtime subsequence
→ static step ↔ runtime step
```

The runtime sequence may contain extra GitHub-generated steps such as:

- setup;
- post-action cleanup;
- job completion.

So UpgradePilot does **not** assume:

```text
static source index == runtime step number
```

It matches the declared user-step identity under the bounded name/order contract instead.

## 5. One representative example

Static workflow:

```text
Build project
  0. Check out repository
  1. Install dependencies
```

Runtime job:

```text
1. Set up job
2. Check out repository
4. Install dependencies
9. Post Check out repository
10. Complete job
```

The bridge can establish:

```text
static step 0 "Check out repository"
↔ runtime step 2

static step 1 "Install dependencies"
↔ runtime step 4
```

because the names are literal/unique and their order is preserved even though GitHub inserted extra runtime-only steps.

This is why ordered-subsequence matching matters.

## 6. Correlation is not execution meaning

A matched runtime step carries status/conclusion, but correlation itself answers only:

> Which static declaration does this runtime observation belong to?

A stronger successful-execution interpretation additionally requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

Why check `continue-on-error`?

Because GitHub can report an overall successful-looking result even when a user step's failure is intentionally tolerated. UpgradePilot should not silently interpret such a step as unmasked successful execution.

## 7. The two important dependency-CI states

### `supported_not_correlated`

Means, approximately:

```text
static dependency consumption is supported
+ exact-head CI succeeded
+ no safe consuming-step ↔ runtime-step relationship was established
```

### `supported_runtime_correlated`

Means:

```text
static dependency consumption is supported
+ the exact supported consuming step is safely correlated
  to an exact-attempt runtime step
+ that runtime step is completed/successful
+ visible continue-on-error masking is absent
```

So the second state is stronger because UpgradePilot knows **which exact runtime step corresponds to the static dependency-consuming step** and has a bounded successful runtime observation for it.

## 8. A subtle but important state distinction

Suppose the workflow uses a matrix, so the correlation layer says:

```text
correlation = unresolved
```

That does **not** mean UpgradePilot must discard every weaker fact already established.

If it still has:

```text
supported static dependency consumption
+ successful exact-head CI
```

then dependency-CI coverage may remain:

```text
supported_not_correlated
```

This preserves evidence already earned instead of collapsing the whole result merely because the stronger bridge is unavailable.

That distinction was important during the post-build ownership check.

## 9. What the tests actually prove

Representative tests in `tests/test_workflow_runtime_correlation.py` cover:

- successful named job/step correlation with runtime-only extra steps;
- matrix/strategy rejection;
- reusable-workflow rejection;
- missing/dynamic job-name rejection;
- duplicate job-name rejection;
- exact static/runtime job-name-set requirement;
- missing/dynamic/duplicate step-name rejection;
- duplicate/unordered runtime step-number rejection;
- missing/ambiguous runtime step match rejection;
- static/runtime step-order mismatch rejection.

The current real-environment validation recorded for the slice reached:

```text
focused correlation tests                         PASS
nearest CI/investigation/provider/parser/synthesis PASS
full deterministic repository suite              549 tests OK
```

That establishes the implemented bounded bridge and regression protection at this snapshot.

## 10. What this proof does NOT establish

Do not strengthen the claim beyond the evidence.

The bridge does **not** prove:

- exact installed dependency version;
- which wheel or sdist was selected/downloaded;
- target wheel compatibility;
- behavioral compatibility;
- complete CI coverage;
- proposal safety;
- merge permission;
- targeted-check permission;
- investigate/block/defer permission.

A successful correlated `pip install ...`-like step is still much weaker than an exact runtime artifact/version witness.

## 11. Current limitations worth recognizing, not automatically fixing

The first bridge deliberately does not positively correlate:

- matrix/strategy jobs;
- reusable workflows;
- dynamic job names;
- missing job names;
- ambiguous/duplicate names;
- unsupported/malformed static structures.

Those are capability limits. They become implementation priorities only if a real decision/evidence requirement shows they matter.

Current E-phase reasoning is therefore not:

> broaden correlation because broader support is always better.

It is:

> identify the next decision-relevant missing proposition, then ask what smallest evidence improvement can establish it.

## 12. Important surrounding risks after this bridge

The current E inventory highlights that stronger correlation can make upstream evidence-quality defects more important, not less.

Examples include:

- false-positive static shell/direct-install recognition;
- changed-file patch evidence not fully bound to the frozen PR head;
- no normal exact target wheel-compatibility producer;
- target composition potentially losing an already-known CI `job_key`;
- no exact runtime dependency-version/artifact witness.

This is a useful engineering lesson:

> Strengthening a later evidence layer does not repair a weak earlier proposition. It can make a wrong earlier proposition look more convincing.

## 13. Depth calibration

### Must own

- static evidence and runtime evidence are separate;
- correlation establishes identity/relationship, not dependency truth by itself;
- positive correlation is intentionally conditional and fail-closed;
- `supported_runtime_correlated` is stronger than `supported_not_correlated` but still bounded;
- unresolved stronger evidence should not erase weaker evidence already legitimately established;
- tests/proof must not be read as exact version/wheel/compatibility proof.

### Understand operationally

- why literal unique names + whole-set agreement + order constraints make bounded matching safer;
- why runtime-only setup/post steps require subsequence matching;
- how `continue-on-error` affects successful-execution interpretation;
- how unresolved correlation flows into downstream dependency-CI interpretation.

### Lookup-level

- exact dataclass field layouts;
- every individual `reason` string;
- Python helper implementation details such as `_first_duplicate`;
- exact fixture construction syntax in every unit test.

### Deferred deliberately

- matrix/reusable workflow correlation algorithms;
- full GitHub Actions expression evaluation;
- job-log parsing;
- exact package-manager artifact reconstruction;
- broader maintainer-action permissions.

## 14. Fast relearning route

When returning weeks later, use this order:

1. Recall the sentence: **static declaration + runtime observation ≠ automatically correlated**.
2. Open `src/upgradepilot/ci/workflow_runtime_correlation.py` and read `correlate_workflow_runtime()` plus `_correlate_job_steps()`.
3. Open `tests/test_workflow_runtime_correlation.py` and inspect:
   - the successful subsequence case;
   - the matrix rejection case;
   - the order-mismatch case.
4. Re-state the difference between `supported_not_correlated` and `supported_runtime_correlated`.
5. Name at least three things the bridge still does not prove.
6. Only then inspect current `MEMORY.md` to see whether the project has moved beyond this snapshot.

## 15. Notebook/Gemini Notebook source-grounding suggestion

For an audio/video/quiz transform, prefer a small grounded source set rather than the whole repository:

1. this learning note;
2. `src/upgradepilot/ci/workflow_runtime_correlation.py`;
3. `tests/test_workflow_runtime_correlation.py`;
4. optional: `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md` if the engineering progression matters.

Do not use `MEMORY.md` as the primary frozen teaching source because it is the live-state owner and can continue changing.

## 16. Retrieval and transfer questions

1. Why is matching a static step name to a runtime step name unsafe unless uniqueness, exact workflow identity, and ordering constraints also hold?
2. If matrix correlation is unresolved but static dependency consumption and successful exact-head CI are still supported, why can `supported_not_correlated` remain valid?
3. What additional evidence would you need before claiming an exact dependency version or exact wheel actually executed in CI?
4. Suppose runtime correlation is perfect but static command recognition falsely says a dependency was consumed. Why can the final evidence still be wrong?
5. If a future real case requires matrix support, what proposition should the new implementation prove rather than simply "support matrices" in general?

## 17. Evidence anchors

Current snapshot anchors:

- `src/upgradepilot/ci/workflow_runtime_correlation.py`
- `src/upgradepilot/ci/dependency_exercise.py`
- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`
- `tests/test_maintainer_action.py`
- `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`
- repository snapshot `e8acb761b347a1bdc0dcc9ec4207221c4058b5e2`

This note is a learning snapshot. Current project continuation always comes from `MEMORY.md`.

`UP-SKILL:upgradepilot-learning-artifact`
