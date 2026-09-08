# Target Artifact-Environment Composition — Working Memory

**Date/time:** 2026-09-07 21:49 +03:30  
**Session status:** ACTIVE — Slice-3 A–E complete at source/test structural-evidence boundary; executable validation deferred; next cycle begins with Slice-4 A-stage orientation  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)  
**Previous:** [`2026-09-07_1748_artifact-serviceability-candidate-composition.md`](2026-09-07_1748_artifact-serviceability-candidate-composition.md)

## Slice 3 A–E status

```text
A — DONE
    Pre-implementation orientation traced the current Target interpreter, CI consumption
    evidence, exact workflow-definition reuse path, target proof boundary, and workflow/job
    ambiguity. Ali selected option B: evidence-gated composition using only already-earned
    supported direct-requirements workflow/source relationships for the first integration.

B — DONE WITH DEFERRED EXECUTABLE PROOF
    The selected route was added to the plan, implemented in investigation.py, and protected
    by focused investigation tests. Source/test diffs were inspected. Local WSL execution is
    unavailable by user constraint and the latest commit has no remote commit status, so no
    executable PASS claim exists.

C — DONE
    This working memory preserves the slice decisions, source/test evidence, proof debt, and
    concurrent-work observation. MEMORY.md points here as the active working record.

D — DONE
    The post-implementation learning pass covered the real application join, CI evidence gate,
    exact identity checks, evidence reuse, deduplication, Target-domain abstention, focused
    integration tests, CI runtime/static separation, and the exact compatibility proof gap.
    Ali's questions and answers demonstrated the main evidence-preservation model; one gap was
    repaired around the exact target wheel-compatibility proposition.

E — DONE
    The exposed capability limits were classified as deferred re-entry candidates rather than
    current blockers. Multi-job Target selection, uv/project-environment Target formation,
    runtime static-step correlation, and exact target wheel compatibility must be revisited only
    when concrete product evidence makes the corresponding proposition necessary. Slice 3 is
    closed for learning/ownership; Slice 4 human-facing explanation is the next bounded cycle.
```

## A — adopted selection decision

The existing plan was directionally correct but did not yet state the exact first-integration gate. It was refined in commit `d0d094ee4faa818cd35999f6f63635cdb9517ea7` (`docs: record slice three target selection gate`).

The selected route is:

```text
real ArtifactServiceabilityImpactCandidate
+
already-earned StaticDependencyConsumptionEvidence
  state == "supported"
  mechanism == "direct_requirements"
  exact source_path
+
matching exact DependencySourceContext
+
already-acquired exact workflow definition
→ interpret_target_artifact_environment(...)
→ DependencySourceArtifactEnvironmentResult
```

Explicit exclusions for this first integration:

- no workflow × source cross-product;
- no unresolved/plausible CI relationship promotion;
- no project-environment / uv-selection consumption promotion into the current Target direct-install interpreter;
- no ad-hoc use of CI `job_key` to extend or bypass the Target API;
- no synthetic `TargetWheelCompatibilityEvidence` from runner/Python/install declarations;
- no CLI work in this slice.

Reasoning:

1. CI already owns and preserves the proposition that one exact static declaration consumes the changed dependency.
2. Supported direct-requirements evidence carries exact workflow path/revision, source path, job/step identity, package identity, and a direct requirements mechanism understood by the current Target interpreter.
3. Unresolved CI evidence should remain uncertainty in `ci_coverage_result`; selecting it as a Target association would strengthen a relationship that is not established.
4. Supported project-environment consumption is real CI evidence, but the current Target interpreter does not own general uv/project-environment formation. Feeding such relations into it would risk misleading `not_observed` Target installation state.
5. Multi-job/reusable/unsupported Target shapes remain explicit Target problems under the current owner instead of being silently solved by application orchestration.

## B — source implementation

Commit `ec45deb77450011470ff12c35419289e431d1c64` (`feat: compose target artifact environments`) changed only `src/upgradepilot/investigation.py`.

The application now initializes and returns:

```text
target_artifact_environment_results
```

and activates Target composition only after a real `ArtifactServiceabilityImpactCandidate` exists.

The new `_compose_target_artifact_environments(...)` application join:

1. consumes the already-produced `DependencyCICoverageResult` and the exact `WorkflowDependencyCoverageInput` values used to create it;
2. requires workflow-result/input cardinality and workflow-path identity to remain aligned;
3. selects only consumptions where:
   - `state == "supported"`;
   - `mechanism == "direct_requirements"`;
   - `source_path` is exact/present;
4. verifies each selected consumption matches the exact workflow path/revision;
5. maps it to exactly one `RequirementsFileDependencyContext` using source path + revision + normalized package;
6. treats a failed/ambiguous exact join as an application invariant error rather than silently weakening identity;
7. deduplicates identical `(workflow revision, workflow path, dependency source path)` relationships;
8. reuses the same exact workflow definition already acquired for CI;
9. delegates interpretation to `interpret_target_artifact_environment(...)`;
10. preserves either Target evidence or Target problem inside `DependencySourceArtifactEnvironmentResult`.

The code includes decision-boundary comments explaining that Target composition is CI-evidence-gated, workflow evidence is reused rather than reacquired, and static Target facts are not exact wheel-compatibility evidence.

Importantly, the existing `ArtifactServiceabilityImpactAssessment` is **not** re-evaluated from `TargetArtifactEnvironmentResult`. Current static Target evidence still does not satisfy the separate `TargetWheelCompatibilityEvidence` contract, so applicability remains unresolved.

## B — focused integration tests

Commit `20fc2b964643eb56d2f3c2f44e32adac33fdc099` (`test: protect target artifact composition`) changed only `tests/test_investigation.py`.

The focused family now adds:

1. **Supported direct requirements → Target evidence**
   - real cp39→cp310 artifact candidate;
   - successful exact-head workflow with root checkout + setup-python 3.9 + `pip install -r requirements.txt`;
   - one dependency-source ↔ Target association;
   - exact repository/revision/workflow/source identity preserved;
   - runner/Python/install declaration extracted;
   - `exact_wheel_compatibility_state == "unresolved"`;
   - artifact applicability remains unresolved and `target_evidence is None`;
   - the workflow definition provider method is called only once, demonstrating reuse rather than a Target re-fetch.

2. **No real artifact candidate → Target branch inactive**
   - supported CI consumption exists;
   - unchanged universal-wheel capability produces no artifact candidate;
   - `target_artifact_environment_results == ()`.

3. **Unresolved direct-requirements CI relationship → not selected**
   - a visible requirements install without established current-repository checkout provenance remains unresolved in CI;
   - no Target association is created;
   - artifact assessment remains unresolved.

4. **Multi-job Target ambiguity is preserved**
   - CI identifies supported consumption in a multi-job workflow;
   - application does not use CI job relevance to bypass Target semantics;
   - Target returns `ambiguous_target_job_selection`;
   - artifact applicability remains unresolved.

The harness now has explicit exact-head workflow run/job/definition setup for these orchestration cases and continues to stop unrelated upstream semantics when a test is focused on Target composition.

## Structural evidence / proof boundary

Direct re-read after mutation confirms:

```text
candidate exists
→ initial unresolved artifact assessment
→ CI-gated target composition
→ Target evidence/problem collection

NO TargetArtifactEnvironmentResult
→ TargetWheelCompatibilityEvidence conversion

NO Target result
→ artifact applicability strengthening
```

Commit diff inspection shows:

```text
ec45deb... → only src/upgradepilot/investigation.py
20fc2b9... → only tests/test_investigation.py
```

An isolated compare from the plan-decision commit `d0d094e...` to `20fc2b9...` shows exactly those two source/test files changed by Slice-3 B.

A broader compare exposed independent concurrent work in `README.md`, `experiments/`, and separate working memories. Those changes were not part of this slice and were preserved untouched.

Available evidence establishes:

```text
plan decision recorded
+
source implementation committed
+
focused tests committed
+
source/test diffs inspected
+
exact target proof boundary re-read
+
concurrent independent work preserved
```

It does **not** establish:

```text
Python syntax/import execution
focused tests PASS
target-artifact-environment regression PASS
artifact-serviceability regression PASS
nearest integration PASS
full deterministic suite PASS
```

The latest source/test commit has no remote commit statuses. Local WSL execution remains intentionally deferred by user constraint. This is proof debt, not passing evidence.

## C — state preservation result

`MEMORY.md` was reconciled in commit `a59d06b4d268def2080439516bb86346b14734e5` so the live project state records the Slice-3 implementation/proof boundary and points to this working memory.

## D — post-implementation learning / ownership result

The completed teaching pass established these responsibility boundaries from the real source/tests:

```text
artifact candidate formation
≠ CI relevance
≠ Target artifact-environment interpretation
≠ exact target wheel compatibility
≠ artifact applicability conclusion
```

CI currently combines two separate evidence axes:

```text
successful exact-head workflow/job runtime status
+
static changed-dependency consumption in the exact workflow definition
→ supported_not_correlated
```

The result intentionally does not claim that the exact static install/exercise step was correlated to runtime execution or success.

The Slice-3 application path does not globally couple artifact-serviceability candidate formation to CI. CI is used only as the current evidence gate for selecting proposition-relevant Target workflow/source relationships. When that gate cannot establish relevance, the candidate survives and applicability remains unresolved.

Ownership-check answers demonstrated:

- Target ambiguity must be preserved rather than hidden or guessed; it does not invalidate the artifact candidate;
- unsupported Target mechanisms such as current uv/project-environment formation should not be forced through a narrower interpreter, because `not_observed` could falsely look like negative evidence;
- the remaining proposition needed to strengthen applicability is exact target wheel compatibility: evidence of the target runtime's supported wheel tags and their relationship to the wheel capability lost by the candidate.

Gap repair for the final point:

```text
runner = Ubuntu
+
Python = 3.9
+
static install declaration observed
```

does not establish the runtime's exact interpreter/ABI/platform tag set. Therefore it cannot by itself prove that a removed wheel tag was required, accepted, or irrelevant to the target.

## E — deferred capability observations and re-entry triggers

The learning pass exposed four legitimate limitations. None is a blocker for closing this bounded Slice-3 integration because the current typed model preserves their uncertainty honestly.

### 1. Multi-job Target selection

Current effect:

```text
CI may establish the consuming job
+
Target sees a multi-job workflow
→ ambiguous_target_job_selection
```

Re-entry trigger: revisit the Target API/job-selection responsibility only when real candidate cases are materially blocked by recurring multi-job ambiguity. Do not use CI `job_key` ad hoc in application code to bypass Target ownership.

### 2. uv/project-environment Target formation

Current effect:

```text
CI/dependency owners may establish supported uv/project-environment consumption
+
current Target artifact interpreter does not own that formation mechanism
→ first integration does not create a Target association from it
```

Re-entry trigger: add Target-side project-environment/uv semantics only when real relevant repositories make the direct-requirements-only Target coverage materially insufficient. Existing uv CI/dependency evidence remains valid and should be reused rather than reimplemented.

### 3. Static declaration ↔ runtime execution correlation

Current effect:

```text
successful exact-head workflow/job evidence
+
supported static consumption
→ supported_not_correlated
```

Re-entry trigger: strengthen runtime correlation only when a product proposition specifically requires proof that the relevant declared install/exercise step itself executed successfully. Do not build this merely to make CI evidence appear stronger.

### 4. Exact target wheel compatibility

Current effect:

```text
partial Target environment facts
→ exact wheel compatibility unresolved
→ artifact applicability unresolved
```

Re-entry trigger: investigate/admit an exact compatibility owner when the product needs to strengthen artifact applicability to established applicable/not-applicable. This is a conclusion-strength gap and is potentially more consequential than broadening workflow-shape coverage, but it is not silently folded into the current static Target interpreter.

These are preserved as re-entry candidates rather than automatically scheduled implementation work. Real product cases should determine which one earns priority.

## Immediate continuation

Slice 3 is closed through A–E for implementation and learner ownership, with executable proof still deferred.

The next bounded cycle is plan **Slice 4 — human-facing explanation**:

```text
A — NEXT: inspect current CLI presentation + tests and orient the proof-strength vocabulary
B — pending
C — pending
D — pending
E — pending
```

The immediate goal is not to deepen Target or CI. It is to make the already-earned artifact candidate, Target evidence/problem, unresolved applicability, and proof limitations understandable to the human user without manufacturing an overall maintainer recommendation.

Deferred local validation remains accumulated proof debt and must be resumed when normal WSL access returns.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`