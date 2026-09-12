# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

## Responsibility

UpgradePilot has three deliberately separate CI evidence responsibilities:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion

STATIC + RUNTIME
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

The bridge maps existing static job/step coordinates to factual runtime job/step records. It does not rediscover dependency semantics and does not turn provider observations into dependency claims by itself.

## A — design/investigation — DONE

A selected the smallest sound first correlation class from current source, GitHub documentation, and real historical UpgradePilot workflow/run evidence.

### Job correlation

Positive correlation is admitted only when:

```text
exact workflow revision == run head
+ valid WorkflowDefinition
+ all jobs are ordinary StepsJobDefinition
+ no strategy/matrix, reusable job, or JobProblem
+ every static job has an explicit literal non-expression non-empty name
+ static job names unique
+ runtime job names unique
+ static-name set == runtime-name set
→ static job key ↔ runtime job ID
```

Matrix/strategy, reusable, malformed, unnamed, dynamic, duplicate-name, and job-set mismatch shapes remain unresolved at the correlation layer.

Historical UpgradePilot evidence directly demonstrated the matrix pressure: one static job named `Python ${{ matrix.python-version }}` produced three runtime jobs (`Python 3.12`, `Python 3.13`, `Python 3.14`).

### Step correlation

Inside an already-correlated job:

```text
no StepProblem
+ every user-defined step has explicit literal non-expression non-empty name
+ static step names unique
+ runtime steps present
+ runtime step numbers unique and strictly ordered
+ each static step name appears exactly once at runtime
+ static step-name sequence is an ordered runtime subsequence
→ static source_index ↔ runtime step number
```

Runtime-only setup/post/completion steps are allowed as extras. Static source index is never equated directly with runtime step number.

### Correlation vs runtime-success interpretation

Identity and result interpretation remain separate. A positive successful-step interpretation requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

`continue-on-error: true` or dynamic semantics prevent treating conclusion `success` as an unmasked successful outcome.

### Claim boundary

The bridge may establish only:

```text
for this exact PR head/run attempt,
this statically identified user-defined run step
corresponds to this runtime step,
and GitHub reports this status/conclusion
```

It does **not** establish exact resolved dependency version, every shell segment succeeding, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or any maintainer action.

No job-log acquisition was needed for this bridge.

## B — Build/Implement — DONE

Implemented:

- `src/upgradepilot/ci/workflow_runtime_correlation.py`
- runtime-correlation integration in `src/upgradepilot/ci/dependency_exercise.py`
- compatibility handling in `src/upgradepilot/maintainer_action.py`
- focused correlation and dependency-CI proof tests
- maintainer-action regression protection

The correlation module returns either:

```text
correlated
→ WorkflowRuntimeJobCorrelation
   → WorkflowRuntimeStepCorrelation

unresolved
→ reason + detail
```

`dependency_exercise.py` now admits:

```text
supported_runtime_correlated
```

when an already-supported static dependency-consuming run step is safely correlated to an exact-attempt runtime step with `completed/success` and no visible `continue-on-error` masking.

The previous:

```text
supported_not_correlated
```

remains the conservative fallback when supported static consumption and successful exact-head CI exist but the bounded bridge cannot safely correlate the workflow.

If correlation succeeds but the relevant consuming step is skipped/failed/cancelled/non-completed, dependency-CI coverage becomes unresolved instead of hiding observed non-success. Static direct exercise remains a separate axis and now also has its own runtime-correlated execution axis.

### Relevant implementation commits

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
```

### Executable validation — GREEN

Ali ran the required narrow-to-broad validation in the real WSL UpgradePilot environment:

```text
focused correlation tests
→ PASS / GREEN

nearest CI / investigation / provider / parser / synthesis regression set
→ PASS / GREEN

full deterministic repository suite
→ Ran 549 tests in 0.144s
→ OK
```

The proof does **not** establish exact dependency/version installation, selected wheel, wheel compatibility, behavioral compatibility, complete external CI coverage, proposal safety, or a maintainer-action permission.

## C — state preservation — DONE

Final implementation, proof results, scope boundaries, and stronger-claim exclusions are preserved here and in `MEMORY.md`.

## D — post-implementation learning / ownership — DONE

The ownership check covered the implemented system as one flow rather than isolated syntax.

Ali demonstrated the following mental model:

1. the static layer tells UpgradePilot what workflow/job/step and command are declared;
2. the runtime layer tells UpgradePilot what GitHub reports for the exact run/attempt/job/step;
3. the bridge does not create a new runtime fact — it establishes which static declaration the runtime observation belongs to;
4. the first bridge uses display `name` as the matching anchor only under surrounding safety conditions such as exact workflow/run identity, literal names, uniqueness, whole-set consistency, ordering, and exclusion of unsupported ambiguous shapes;
5. those safety conditions are also current capability limitations: unsupported shapes are not guessed into positive correlation;
6. `supported_runtime_correlated` is stronger than `supported_not_correlated` because the exact supported static consuming step is tied to a completed-successful runtime step, while exact installed version/wheel and compatibility remain unproven;
7. stronger technical CI evidence does not create a maintainer-action permission.

### Final D state-label correction

```text
matrix/unsupported shape
→ correlation layer: unresolved
```

but when the workflow still has successful exact-head CI plus supported static dependency consumption:

```text
correlation unresolved
+ static consumption supported
+ successful CI
→ dependency-CI coverage: supported_not_correlated
```

This preserves evidence already earned rather than collapsing the whole CI result merely because the stronger bridge cannot be established.

## E — CURRENT — full limitations, bottlenecks, and improvement inventory

E now has a repository-audited inventory. The categories are intentionally different because they imply different priority and response:

```text
correctness / provenance defect
→ can create wrong or misattributed evidence

evidence / architecture bottleneck
→ stays conservative but blocks a stronger useful claim

deliberate safety / coverage limit
→ intentionally refuses unsupported or ambiguous cases

future product / observability gap
→ desired capability is not yet implemented
```

The previous mixed-rerun-attempt defect is **not** a current defect: it was repaired and proven in the preceding A→E cycle.

### Category 1 — confirmed current correctness / provenance defects

#### 1. Static shell/direct-install recognition can produce false-positive dependency consumption

Current static direct-install recognition still relies on bounded command-text splitting rather than real shell grammar/semantics. The earlier controlled investigation reproduced false positives such as:

```text
pip install -r requirements-dev.txt                 → observed
pip install wheel                                   → not_observed
pip install wheel # -r requirements-dev.txt         → observed — false positive
echo "pip install -r requirements-dev.txt"          → not_observed
echo "note; pip install -r requirements-dev.txt"    → observed — false positive
```

Relevant current owners include `src/upgradepilot/dependency/direct_install.py` and `src/upgradepilot/dependency/workflow_context.py`; command segmentation still uses bounded textual separators rather than shell syntax ownership.

This defect becomes more important after the correlation bridge:

```text
wrong static semantic interpretation
+ correct static↔runtime identity correlation
+ runtime step completed/success
→ potentially stronger but still semantically wrong CI evidence
```

The bridge proves **which step ran**. It cannot repair an incorrect interpretation of **what the step meant**.

#### 2. Requirements/constraints changed-file patch evidence is not bound to the frozen PR head

The pull-request identity freezes one `head_sha`, but the requirements/constraints route later acquires changed-file patches from the live pull-request files endpoint and only checks the changed-file count. The earlier controlled investigation proved that when the PR advances from head A to head B without changing the file count, B's patch may be interpreted while the dependency context is stamped with A's revision.

Current source still has this shape across `src/upgradepilot/github/pull_request.py` and `src/upgradepilot/dependency/analysis.py`.

The failure mode is:

```text
frozen identity at head A
+ live changed-file patch from head B
+ same changed-file count
→ B content attributed to revision A
```

This is a snapshot/provenance defect. Later exact-head CI evidence cannot retroactively repair an earlier mixed-snapshot dependency change.

### Category 2 — major evidence / architecture bottlenecks

#### 3. No normal producer for exact target wheel-compatibility evidence

`src/upgradepilot/impact/artifact_serviceability.py` has an exact target-wheel compatibility evidence concept/evaluator, but the normal investigation path does not currently produce the exact target wheel-tag witness needed to populate it. `src/upgradepilot/target/artifact_environment.py` therefore keeps exact wheel compatibility unresolved.

This is an evidence-production gap, not a false-positive defect.

#### 4. Target composition discards an already-known CI `job_key`

Supported static CI consumption evidence already carries the exact consuming `job_key` and step location. In `src/upgradepilot/investigation.py`, `_compose_target_artifact_environments()` uses that supported relationship to select a workflow/source pair, but then calls the target interpreter on the whole workflow without carrying the exact consuming job into Target.

`src/upgradepilot/target/artifact_environment.py` therefore re-solves job selection under its conservative one-job boundary and can return `ambiguous_target_job_selection` even though CI already knows which job consumed the dependency.

Potential improvement direction:

```text
CI-supported exact consuming job
→ preserve job identity into Target composition
→ interpret target facts for that exact job
```

This should be evaluated under earliest-sufficient-owner reasoning before implementation; it is currently an architecture/evidence-composition bottleneck, not a proven false-evidence bug.

#### 5. No exact runtime dependency-version / artifact witness

The new bridge establishes:

```text
static consuming step
↔ exact runtime step
+ GitHub status/conclusion
```

It still does not reveal:

- exact dependency version resolved/installed;
- wheel versus sdist selection;
- exact artifact filename/tags;
- resolver/install output;
- exact runtime target tags.

A later log/artifact/runtime-evidence responsibility may address a precisely selected proposition, but logs are not justified merely because they are available.

#### 6. CI acquisition failure containment is source-traced but needs fresh proof

The current investigation orchestration acquires CI evidence before several independent package/upstream branches. There is no obvious local typed degradation boundary around every provider exception, so a CI/network/provider exception may still abort otherwise independent evidence acquisition.

This was identified by the earlier system-limitations work, but this E pass did not execute a fresh current-main discriminating reproduction. Therefore retain it as:

```text
resilience / architecture risk
→ source-traced
→ needs fresh proof before calling it a confirmed current defect
```

### Category 3 — deliberate conservative safety / coverage limits

These are not defects merely because they return unresolved or do not support every real GitHub/Python shape.

#### 7. Correlation bridge supports only the first bounded ordinary named-workflow class

Current unsupported/unresolved correlation shapes include:

- matrix/strategy jobs;
- reusable workflows;
- missing/dynamic/duplicate job names;
- static/runtime job-name-set mismatch;
- missing/dynamic/duplicate step names;
- missing runtime step summaries;
- ambiguous runtime step-name matches;
- runtime step-number/order defects.

Expand only when real cases or a selected product claim require it.

#### 8. Target artifact-environment interpretation is intentionally narrow

Current Target rules remain conservative around multi-job selection, matrix/strategy, reusable workflows, containers, dynamic runners/setup-python values, and exact wheel compatibility. This is a supported-domain boundary, not automatically technical debt.

#### 9. Target composition currently promotes only direct-requirements consumption

`_compose_target_artifact_environments()` currently uses supported `direct_requirements` relationships for Target composition. Supported project-environment/uv/pyproject consumption does not yet receive equivalent Target composition.

This is a coverage limitation to revisit only when the product decision needs it.

#### 10. Dependency-analysis source domain remains intentionally bounded

UpgradePilot still deliberately rejects/keeps explicit problems for unsupported dependency-file forms, conflicting source evidence, and multiple incompatible dependency transitions. This remains consistent with Minimum Useful Generality unless real-case pressure justifies expansion.

#### 11. Provider changed-file count has an explicit finite operational bound

The GitHub pull-request provider intentionally caps changed-file acquisition. This is an operational bound and low priority absent real evidence that supported target PRs exceed it.

### Category 4 — future product / observability / engineering gaps

#### 12. Maintainer-action synthesis is still abstain-only

Current `src/upgradepilot/maintainer_action.py` admits only:

```text
abstain
```

The Charter's wider public action space — merge after normal review, run targeted checks, investigate/block, defer, abstain — is not yet implemented. This is an intentional major product-completion gap, not a bug in the current evaluator.

#### 13. CLI/reporting does not expose the full new runtime-correlation diagnostic surface

The technical result now carries runtime consumption/direct-exercise states and detailed correlation reasons, but the current CLI/presentation surface does not expose all of that detail. This is a lower-priority observability improvement unless current user-facing debugging requires it.

#### 14. Full investigation persistence/replay/corpus evaluation is not yet a normal product path

The repository has bootstrap JSON contracts and simulation/learning evidence, but no mature normal path was found that persists and replays the complete current investigation/evidence graph for corpus-scale regression and explanation. This is a future engineering/product capability rather than an immediate correctness defect.

## E priority discipline — no selection yet

The inventory is recorded, but **no next A→E cycle is selected yet**.

When we rank it together, use this order of questions rather than raw feature count:

```text
1. Can this issue currently create wrong or misattributed evidence?
2. If not, does it block the next decision-critical proposition?
3. Is the limitation deliberately conservative and currently acceptable?
4. Is it only presentation/product-completion work that can wait?
```

Initial risk signal, not yet a selected route:

- the shell false-positive defect can now be amplified by the new runtime correlation into stronger wrong semantic evidence;
- the patch/head mismatch can corrupt source-revision identity before all later exact-head reasoning;
- exact wheel/runtime-artifact production and exact-job Target composition are major evidence bottlenecks after correctness is trustworthy;
- matrix/reusable/dynamic-name expansion should not be prioritized merely for completeness.

The next E responsibility is **learning and priority review of this inventory with Ali**. A new implementation cycle starts only after that discussion selects and bounds one distinct responsibility.

## Current Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — DONE
B — DONE
    full suite: 549 tests OK
C — DONE
D — DONE
E — CURRENT
    full limitation/bottleneck/improvement inventory recorded
    learning + priority selection still pending
```

## Scope exclusions retained until E selects otherwise

Do not yet:

- implement any inventory item merely because it is listed;
- download/parse job logs;
- add exact wheel/version installation semantics;
- enable `run targeted checks`;
- add merge/investigate/block/defer permissions;
- redesign CLI/reporting;
- expand matrix/reusable/dynamic-name support merely for completeness.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`