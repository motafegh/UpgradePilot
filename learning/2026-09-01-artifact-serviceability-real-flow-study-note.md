# Artifact Serviceability — Real-Flow Study Note

**Snapshot date:** 2026-09-01  
**Product source/test evidence horizon:** `958b4b73d5c8fc011f1150258b9e9a73b1f51151`  
**Primary responsibility:** `src/upgradepilot/impact/artifact_serviceability.py`  
**Learning depth:** implementation-adjacent; not mastery certification  
**Authority:** educational snapshot only. Current owners/source/tests remain authoritative.

## 1. Core mental model

Artifact serviceability separates package artifact availability from interpreter support and from target applicability:

```text
package still supports Python X
!=
new release still publishes a wheel usable by this exact target
```

The module has two bounded stages:

```text
STAGE 1 — package-side transition
old PyPI release inventory
+ proposed PyPI release inventory
→ ArtifactServiceabilityImpactCandidate / evidence problem / None

STAGE 2 — exact target applicability
candidate
+ exact target-supported wheel tags
→ applicable / not applicable / unresolved
```

Central rule:

```text
removed published wheel tag
!=
target lost its prebuilt-wheel path
```

A different proposed wheel tag may still serve the same target.

## 2. Real case — S008 CARLA / OpenCV

Use product-simulation **S008** as the representative case:

```text
carla-simulator/scenario_runner PR 1111
opencv-python 4.2.0.32 → 4.8.1.78
bounded concern: CPython 3.6 on Linux
```

The inspected evidence established:

```text
old release
→ CPython-3.6 manylinux wheels

new release
→ CPython-3.7+ abi3 wheels
→ no CPython-3.6-compatible published binary wheel in the bounded inventory
→ source distribution still published
```

Therefore the bounded installation path can change:

```text
prebuilt wheel
→ source-distribution fallback
```

But this does **not** establish source-build success/failure or OpenCV runtime breakage. Those are separate propositions.

## 3. Stage 1 — candidate construction

Entry point:

```python
build_artifact_serviceability_impact_candidate(...)
```

Inputs:

```text
PullRequestIdentity
DependencyVersionChange
old PackageReleaseEvidence
proposed PackageReleaseEvidence
```

### Exact identity first

`_validate_release_identity(...)` checks that release evidence matches the normalized dependency package and exact old/proposed versions. Wrong evidence is a caller/contract error, not "no impact".

### Interpret real wheel evidence

`_interpret_wheels(...)` processes published `bdist_wheel` files with:

```python
packaging.utils.parse_wheel_filename(...)
```

A wheel compatibility `Tag` represents:

```text
interpreter + ABI + platform
```

The parser-derived package/version must match the exact release record. Malformed or contradictory external evidence becomes `ArtifactServiceabilityEvidenceProblem` rather than a negative compatibility conclusion.

### Compare capability sets

The module forms the complete old/proposed published tag sets and computes:

```text
removed_tags = old_tags - proposed_tags
added_tags   = proposed_tags - old_tags
```

If nothing was removed, the bounded mechanism returns `None`.

```text
None
!=
"the dependency update is safe / impact-free"
```

It means only that this mechanism did not observe published wheel-tag loss.

The candidate also records source-distribution availability. A proposed sdist means fallback **exists as an artifact**, not that a source build will succeed.

## 4. Why the working-memory history matters

The final source alone hides an important implementation lesson.

Increment 1 originally called:

```text
parse_wheel_filename(..., validate_order=True)
```

Fresh execution produced:

```text
4 focused tests
3 passed
1 failed
```

The real-world-style compressed wheel tag was valid compatibility evidence but failed optional canonical ordering validation.

The actual responsibility was:

```text
interpret published compatibility evidence
```

not:

```text
lint wheel-filename component ordering
```

So the implementation was corrected to use normal wheel parsing while preserving real filename/identity validation.

This is exactly why relevant working memories improve a learning artifact: they reveal **why a tempting "stricter" implementation was actually wrong for the responsibility**.

## 5. Stage 2 — exact target applicability

Entry point:

```python
evaluate_artifact_serviceability_impact(candidate, target_evidence)
```

The target contract is intentionally downstream of acquisition:

```python
TargetWheelCompatibilityEvidence(
    repository,
    revision,
    source,
    supported_tags,
)
```

This module does **not** acquire or guess those tags. In particular:

```text
UpgradePilot local sys_tags()
!=
remote target evidence

"Python 3.6 + Linux"
!=
exact target-supported wheel-tag set
```

Repository and revision must also match the candidate before target evidence can be used.

### The real applicability test

One bounded path requires:

```text
1. published wheel transition established
2. exact target compatibility established
3. target had an old compatible published wheel
4. target lacks any compatible proposed published wheel
```

The important calculations are separate intersections:

```text
old published tags      ∩ target supported tags
proposed published tags ∩ target supported tags
```

Why not just inspect `removed_wheel_tags`?

```text
old compatible tag A disappears
+
new compatible tag B exists
→ target still has a prebuilt-wheel path
→ serviceability-loss path is refuted
```

## 6. Important problem/unresolved paths

```text
published wheel cannot be interpreted
→ typed evidence problem
→ not a negative compatibility conclusion

no exact target tags
→ unresolved
→ do not guess

target had no old compatible wheel
→ serviceability-loss path refuted

proposed release still has another compatible wheel
→ serviceability-loss path refuted
```

These distinctions are central to UpgradePilot's evidence discipline.

## 7. What the focused tests prove

`tests/test_artifact_serviceability.py` protects:

**Candidate construction**
- removed tags form a target-agnostic candidate;
- unchanged tags do not manufacture one;
- malformed wheel evidence becomes a typed problem;
- exact release/dependency identity mismatch is rejected.

**Target applicability**
- missing/insufficient target evidence stays unresolved;
- old-compatible + proposed-incompatible can establish applicability;
- another proposed compatible wheel refutes serviceability loss;
- no old compatible wheel refutes the path;
- repository/revision mismatch is rejected.

Historical Increment-2 working memory records **11 focused tests PASS** and **397 full active tests PASS** on 2026-08-13. Those are historical proof for that checkpoint, not proof that this mechanism is currently integrated throughout the application.

## 8. Current integration boundary — audit finding

A bounded current-source search at this snapshot found the artifact-serviceability public functions used by:

```text
tests/test_artifact_serviceability.py
tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py
```

but not by normal application orchestration. `TargetWheelCompatibilityEvidence(...)` likewise appears in tests/verification, with no current product producer found by that bounded search.

Do **not** invent a story that the mechanism is therefore already live end to end.

The historical architecture record explicitly said:

```text
integrated: Python-support path
not yet integrated: artifact-serviceability + target-artifact-environment path
```

and the approved implementation plan keeps heterogeneous mechanism orchestration as a separate later responsibility.

Current classification for this snapshot:

```text
module-level deterministic capability         PRESENT
focused permanent tests                       PRESENT
retained verification                         PRESENT
real S008 discovery evidence                  PRESENT
normal application orchestration integration  NOT PRESENT
exact target wheel-tag producer/acquisition   NOT PRESENT
```

This is a **known bounded capability/integration limitation**, not automatically a defect. If later work claims artifact serviceability is live in the normal application path, re-check this boundary rather than inferring integration from module/test existence.

## 9. Engineering judgment

The strongest design property is separation of evidence responsibilities:

```text
package publishes artifact capability
!=
target supports that capability
!=
source fallback succeeds
```

That allows package evidence to surface a candidate without manufacturing target facts. The cost is that some candidates will later be refuted by exact target evidence. That is preferable to collapsing package and target evidence into one guessed conclusion.

No stronger rationale should be inferred beyond current source/tests, S008 evidence, and the recorded design history.

## 10. Depth map

### Must own

- set difference vs set intersection and why they answer different questions;
- candidate vs target applicability;
- evidence problem vs negative conclusion;
- repository/revision binding;
- remote-target evidence cannot come from UpgradePilot's own environment;
- `None` is bounded no-candidate, not universal safety;
- what the focused tests prove and do not prove.

### Understand operationally

- `@dataclass(frozen=True, slots=True)` domain records;
- `Literal[...]` state vocabularies;
- union result types (`Evidence | Problem`);
- `frozenset[Tag]` capability sets;
- `parse_wheel_filename()` / `Tag`;
- early-return typed problem/unresolved flow.

### Recognize / lookup-level

- `packaging` parser internals;
- complete PEP/tag-family history;
- advanced typing internals behind Python's `type` statement.

### Deferred

- generic exact target-tag acquisition;
- native/source-build analysis;
- universal multi-mechanism orchestration;
- complete packaging compatibility theory.

## 11. Fast relearning route

```text
1. Recall: removed tag != target lost wheel path.
2. Open the two public functions in artifact_serviceability.py.
3. Trace S008 OpenCV 4.2.0.32 → 4.8.1.78.
4. Reconstruct:
      old_tags - proposed_tags
      old/proposed_tags ∩ target_tags
5. Read:
      test_removed_published_wheel_tags_form_target_agnostic_candidate
      test_different_proposed_compatible_tag_refutes_serviceability_loss
6. Explain why validate_order=True was the wrong responsibility.
7. Explain the current non-integration boundary.
```

Ownership questions:

1. Why is a removed old tag insufficient to prove target impact?
2. Why are old and proposed inventories intersected with target tags separately?
3. Why is local `sys_tags()` invalid remote-target evidence?
4. What does a proposed sdist establish and not establish?
5. Why can this be a tested module capability without being a live end-to-end product path?

## Evidence anchors

```text
src/upgradepilot/impact/artifact_serviceability.py
tests/test_artifact_serviceability.py
tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py

working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md
working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md
working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md

product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/README.md
plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md
```

This is a frozen learning artifact, not live project-state or implementation authority.
