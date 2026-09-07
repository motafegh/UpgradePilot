# Artifact Serviceability Candidate Composition — Working Memory

**Date/time:** 2026-09-07 17:48 +03:30  
**Session status:** ACTIVE — candidate-composition source/test work completed; executable validation intentionally deferred until local system access returns  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)  
**Previous:** [`2026-09-06_artifact-serviceability-public-investigation-integration-session.md`](2026-09-06_artifact-serviceability-public-investigation-integration-session.md)

## Session anchor

The previous integration record established the additive `PublicPullRequestInvestigation` contract but left focused executable proof pending before artifact candidate composition.

Ali currently does not have access to the normal WSL control plane and explicitly authorized postponing all local execution/test work until system access returns. This does **not** convert unexecuted tests into passing evidence. It changes only the temporary route:

```text
local executable proof unavailable by user constraint
→ preserve proof debt explicitly
→ continue the next bounded source/test slice
→ do not claim executable validation
→ return to all deferred local proof before final plan closure
```

The selected bounded responsibility for this continuation is plan Slice 2: artifact-serviceability candidate composition. Target artifact-environment composition and CLI rendering remain out of this slice.

## Pre-action model and ownership decision

The key application relationship was established with Ali before mutation:

```text
established proposed PackageReleaseEvidence
├── artifact-serviceability branch
│   └── acquire exact old release
│       └── build candidate only when both releases are evidence
│
└── upstream semantic branch
    └── repository / release interval / changelog / Python-support reasoning
```

Ali selected the evidence-preserving behavior for an old-release provider problem:

```text
proposed release evidence established
+
old release provider problem
→ preserve old provider problem
→ do not manufacture artifact candidate/assessment
→ continue independent upstream/Python-support work
```

Reason: UpgradePilot should preserve all independently earned evidence so later investigation has the strongest truthful view rather than collapsing unrelated branches into one global stop.

This is consistent with the existing integration-plan invariant that independent evidence branches remain independently preserved.

## Bounded source implementation

Commit `0d7838db963b228c3ce5d9ac9e13455a694fd3a6` (`feat: compose artifact serviceability candidate`) changed only `src/upgradepilot/investigation.py`.

The application now:

1. acquires the proposed exact `PackageReleaseResult` as before;
2. only after proposed `PackageReleaseEvidence` is established, acquires the exact old-version `PackageReleaseResult` through the existing PyPI provider owner;
3. preserves an old-release provider problem directly in `old_package_result` without invoking candidate construction;
4. when old and proposed releases are both `PackageReleaseEvidence`, delegates candidate formation to `build_artifact_serviceability_impact_candidate(...)`;
5. preserves all three candidate-builder outcomes distinctly:
   - `ArtifactServiceabilityEvidenceProblem`;
   - `None` after valid comparison, meaning no bounded wheel-loss candidate;
   - `ArtifactServiceabilityImpactCandidate`;
6. only for a real candidate, creates the initial `ArtifactServiceabilityImpactAssessment` through `evaluate_artifact_serviceability_impact(...)` with no target evidence, therefore preserving unresolved applicability;
7. continues upstream repository resolution from the established proposed release regardless of old-release provider failure;
8. explicitly returns `old_package_result`, `artifact_serviceability_candidate_result`, and `artifact_serviceability_impact_result` rather than relying on inactive dataclass defaults.

The source includes one decision-boundary comment explaining why the artifact and upstream branches are siblings and why old-release acquisition failure does not stop upstream analysis.

No target artifact-environment acquisition, target wheel-compatibility inference, CLI rendering, framework work, or unrelated refactor was added.

## Focused test implementation

Commit `255474d6f2bc4f4e31a1c3e37148259c8cbd3509` (`test: protect artifact candidate composition`) changed only `tests/test_investigation.py`.

The harness was corrected from the old one-call assumption:

```text
old behavior
package_client.get_release(...) → always proposed 1.1 evidence

new behavior
get_release("demo", "1.1") → proposed release result
get_release("demo", "1.0") → old release result
```

This matters because returning proposed evidence for the old-version request would make the test double semantically dishonest after the application begins making two exact-version provider calls.

The focused integration family now contains discriminating cases for:

- exact old/proposed release evidence producing a real artifact-serviceability candidate and initial unresolved assessment;
- established old/proposed evidence with unchanged wheel capability producing `candidate_result is None`, distinct from an inactive/provider-blocked branch;
- uninterpretable published wheel evidence preserving `ArtifactServiceabilityEvidenceProblem` without creating an assessment;
- old-release provider failure preserving the explicit provider problem while the independent upstream branch still proceeds;
- an already-earned artifact candidate/assessment surviving a later unrelated upstream changelog-source stop;
- the pre-existing dependency-problem branch continuing to keep both dependency-specific branches inactive;
- existing Python-support tests adapting their provider-call assertion to the legitimate proposed-then-old exact-release sequence.

The integration tests consume the existing domain owner and do not duplicate wheel parsing or compatibility semantics inside `investigation.py`.

## Diff / repository evidence

A compare from the immediate pre-source parent `d7d8616a2ced244df12b48b172a0191331636eb6` to `255474d6f2bc4f4e31a1c3e37148259c8cbd3509` shows exactly two files changed by this slice:

```text
src/upgradepilot/investigation.py
+38 / -3

tests/test_investigation.py
+190 / -17
```

A broader compare from the earlier memory-index commit also exposed a concurrent independent commit:

`d7d8616a2ced244df12b48b172a0191331636eb6` — `Index dependency environment and uv reachability learning package`

which changed `learning/README.md`. That work was not part of this slice and was preserved untouched. The artifact-composition source commit was correctly based on that newer head rather than overwriting it.

Direct post-change inspection confirms the intended source ordering:

```text
proposed package acquisition
→ if proposed evidence:
   old exact release acquisition
   → if old evidence: candidate builder
      → if real candidate: unresolved assessment

   independent upstream repository resolution
```

## Evidence and proof limit

Available evidence now establishes:

```text
selected owner/plan inspected
+
active source and domain owner inspected
+
source change committed
+
focused tests written/updated
+
changed-file diff inspected
+
independent concurrent commit preserved
```

It does **not** establish:

```text
Python syntax/import execution
focused unittest PASS
artifact-serviceability focused domain regression PASS
nearest integration regression PASS
full deterministic suite PASS
```

Those executable claims are intentionally deferred because Ali currently lacks access to the normal WSL control plane. They remain required proof debt; no part of this record should be read as a test-pass claim.

## Learning-by-Doing closure for this slice

The central engineering lesson is **failure containment across independent evidence branches**:

```text
one provider/problem state
should stop only the proposition that depends on it
unless a controlling invariant makes the evidence globally unusable
```

Here, old package evidence is required for artifact transition comparison but is not required to resolve the proposed release's upstream repository. Therefore an old-release problem narrows artifact reasoning without erasing unrelated evidence.

A second important state-model lesson is that `None` is interpretable only together with its prerequisite state:

```text
package_result = proposed evidence
old_package_result = old evidence
candidate_result = None
→ bounded artifact comparison completed and observed no candidate

old_package_result = provider problem
candidate_result = None
→ candidate formation was not completed
```

The explicit provider fields are what keep these meanings distinguishable.

## Current route / handoff

Slice 2 source/test composition is complete but not executable-proven.

Ali explicitly authorized continuing while local execution is postponed. Therefore the next bounded product responsibility is plan Slice 3:

```text
real artifact-serviceability candidate
→ inspect/reuse exact workflow-definition + dependency-source evidence
→ compose target artifact-environment results only where proposition-relevant
→ preserve static evidence as static
→ do not manufacture TargetWheelCompatibilityEvidence
→ keep artifact applicability unresolved unless an admitted exact compatibility owner exists
```

Before implementing Slice 3, re-orient on:

- `src/upgradepilot/target/artifact_environment.py`;
- exact workflow-definition acquisition already performed in `investigation.py` for CI;
- `DependencyChangeAnalysis.source_contexts` cardinality;
- `tests/test_target_artifact_environment.py`;
- the selected plan's Slice-3 proof/stop boundary.

Deferred local validation must be accumulated explicitly and run when WSL access returns, beginning with the focused investigation family and then broadening according to the selected plan.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`