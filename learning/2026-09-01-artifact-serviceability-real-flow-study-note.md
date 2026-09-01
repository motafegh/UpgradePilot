# Artifact Serviceability — Real-Flow Study Note

**Snapshot date:** 2026-09-01  
**Product source/test evidence horizon:** `958b4b73d5c8fc011f1150258b9e9a73b1f51151`  
**Primary responsibility:** `src/upgradepilot/impact/artifact_serviceability.py`  
**Learning depth:** implementation-adjacent study/relearning note; not mastery certification  
**Authority:** educational snapshot only; current source/tests and accepted owners remain authoritative for their responsibilities.

## 1. The big idea

Artifact serviceability asks a different question from Python-version support:

```text
"does the package still claim to support this Python?"
!=
"does the new release still publish a prebuilt wheel that this exact target can use?"
```

The module deliberately separates two stages:

```text
STAGE 1 — package-side transition
exact old PyPI release inventory
+ exact proposed PyPI release inventory
→ did any published wheel compatibility capability disappear?
→ ArtifactServiceabilityImpactCandidate OR evidence problem OR None

STAGE 2 — target applicability
candidate
+ exact target-supported wheel tags
→ did this exact target have an old compatible wheel?
→ does the proposed release still have some compatible wheel?
→ applicable / not applicable / unresolved
```

The most important boundary is:

```text
removed wheel tag
!=
target lost its prebuilt-wheel installation path
```

A different proposed-release wheel tag may still serve the same target.

## 2. Real case: S008 CARLA / OpenCV

The best real case is product-simulation **S008**:

```text
repository: carla-simulator/scenario_runner
PR: 1111
opencv-python: 4.2.0.32 → 4.8.1.78
bounded target concern: CPython 3.6 on Linux
```

The simulation established:

```text
old release
→ published CPython-3.6 manylinux wheels

new release
→ published CPython-3.7+ abi3 wheels
→ no CPython-3.6-compatible binary wheel in the inspected release inventory
→ still published a source distribution
```

So the installation **path** can change from prebuilt wheel to source-distribution fallback for the bounded CPython-3.6 target context.

That does **not** establish:

```text
source build succeeds
or
source build fails
or
OpenCV runtime behavior is broken
```

Those are different propositions.

S008 is therefore useful because it demonstrates why artifact availability deserves its own mechanism rather than being collapsed into interpreter support or runtime compatibility.

## 3. Stage 1 — build the target-agnostic candidate

Public entry point:

```python
build_artifact_serviceability_impact_candidate(...)
```

Inputs are already-structured trusted UpgradePilot records:

```text
PullRequestIdentity
DependencyVersionChange
old PackageReleaseEvidence
proposed PackageReleaseEvidence
```

### Step 1 — exact identity checks

`_validate_release_identity(...)` verifies that each release record matches:

- the normalized dependency package;
- the exact old/proposed dependency version.

This protects against comparing the right mechanism with the wrong release evidence.

A mismatch is treated as a caller/contract error and raises `ValueError`; it is not converted into "no impact".

### Step 2 — interpret published wheel filenames

`_interpret_wheels(...)` walks `distribution_files` and processes only `bdist_wheel` entries.

It uses:

```python
packaging.utils.parse_wheel_filename(...)
```

rather than manually parsing wheel naming rules.

For each wheel it obtains a set of `packaging.tags.Tag` values. A wheel tag represents the compatibility triple:

```text
interpreter + ABI + platform
```

Example shape:

```text
cp36-cp36m-manylinux1_x86_64
```

The parsed wheel package/version identity must also match the exact release evidence. A malformed or contradictory external record becomes an explicit `ArtifactServiceabilityEvidenceProblem` rather than a negative compatibility conclusion.

### Step 3 — compare capability sets

The module flattens all wheel tags for each release:

```text
old_tags
proposed_tags
```

and computes:

```text
removed_tags = old_tags - proposed_tags
added_tags   = proposed_tags - old_tags
```

If `removed_tags` is empty, this bounded mechanism returns `None`.

Important non-claim:

```text
None
!=
"the dependency update has no impact"
```

It means only that this specific mechanism did not observe a loss of published wheel-tag capability.

### Step 4 — preserve source-distribution context without overclaiming

The candidate records whether old/proposed releases publish an `sdist` (source distribution).

If the new release still has an sdist, the possible consequence is phrased as:

```text
prebuilt wheel may disappear
→ source-distribution fallback may remain
```

not:

```text
source build will work
```

This is a good example of UpgradePilot preserving **possible consequence** without promoting it into an established fact.

## 4. A real implementation mistake that the working history reveals

The current source contains this important comment around `parse_wheel_filename(...)`:

> interpret published evidence rather than linting compressed-tag ordering.

The reason is not guesswork; it is recorded in the Increment-1 working memory.

The first implementation used:

```text
parse_wheel_filename(..., validate_order=True)
```

Fresh local execution then produced:

```text
4 focused tests
3 passed
1 failed
```

The real-world-style compressed platform tag was parseable compatibility evidence but did not satisfy optional canonical ordering validation.

That exposed a responsibility mismatch:

```text
UpgradePilot responsibility here
→ interpret compatibility evidence

NOT
→ act as a wheel-filename style/lint validator
```

The implementation was corrected by leaving `validate_order` at its normal `False` default while retaining actual filename/identity interpretation checks.

This history is valuable because simply reading the final line of code does not reveal why enabling stricter validation would actually make this responsibility **worse**, not safer.

## 5. Stage 2 — exact target applicability

Public entry point:

```python
evaluate_artifact_serviceability_impact(candidate, target_evidence)
```

The target contract is deliberately narrow:

```python
TargetWheelCompatibilityEvidence(
    repository,
    revision,
    source,
    supported_tags,
)
```

The module does **not** acquire these tags itself.

It explicitly forbids treating UpgradePilot's own local `packaging.tags.sys_tags()` as evidence for a remote repository target, and it does not guess exact tags merely from broad labels such as "Python 3.6 + Linux".

### Exact target identity matters

Before using target evidence, the evaluator checks:

```text
target evidence repository == candidate target repository
target evidence revision   == candidate target revision
```

Otherwise it raises `ValueError`.

This prevents valid evidence for one repository revision from being silently applied to another.

### Applicability is a conjunction of propositions

The evaluator builds one bounded applicability path:

```text
1. published wheel transition established
2. exact target wheel compatibility established
3. target had at least one compatible old published wheel
4. target has no compatible proposed published wheel
```

The shared `impact.applicability` layer composes those proposition results.

The critical calculations are:

```text
old published tags ∩ target supported tags
```

and independently:

```text
proposed published tags ∩ target supported tags
```

That is better than checking only `candidate.removed_wheel_tags`.

Why?

Imagine:

```text
old target-compatible tag A disappears
but
new target-compatible tag B is added
```

Then one exact old tag disappeared, but the target still has a prebuilt-wheel path. The serviceability-loss candidate is therefore **not applicable** to that target.

## 6. Failure / unresolved paths worth understanding

### Published wheel cannot be interpreted

```text
external PyPI evidence
→ wheel filename malformed/uninterpretable
→ ArtifactServiceabilityEvidenceProblem
```

Do not convert evidence failure into "no compatibility problem".

### Target compatibility evidence unavailable or insufficient

```text
candidate exists
+ no exact supported target tags
→ applicability stays unresolved
```

Do not guess.

### Target never used an old compatible wheel

```text
old published tags ∩ target tags = ∅
→ serviceability-loss path refuted
```

Even if package-side wheel capabilities changed, that exact target did not lose the old path being claimed.

### Proposed release still has another compatible wheel

```text
proposed published tags ∩ target tags != ∅
→ serviceability-loss path refuted
```

This is the key regression against naive "removed tag = impact" reasoning.

## 7. What the focused tests actually protect

`tests/test_artifact_serviceability.py` protects two groups of behavior.

### Candidate construction

The tests establish that:

- disappearing published wheel tags create a target-agnostic candidate;
- unchanged tag capability does not manufacture a candidate;
- malformed wheel filenames become typed evidence problems;
- exact release/dependency identity mismatches are rejected.

### Target applicability

The tests establish that:

- missing target evidence remains unresolved;
- old-compatible + proposed-incompatible can establish applicability;
- a different proposed compatible wheel refutes serviceability loss;
- a target with no old compatible wheel refutes the path;
- insufficient target evidence remains unresolved;
- repository/revision mismatch is rejected.

Historical Increment-2 evidence records a user-run focused result of **11 tests PASS** and a full active suite of **397 tests PASS** at that 2026-08-13 checkpoint.

Those historical counts prove that checkpoint's tested behavior; they do not prove the current whole product integrates this mechanism end to end.

## 8. Current integration status — important audit finding

The current source search at this snapshot finds the two artifact-serviceability public functions used by:

```text
tests/test_artifact_serviceability.py
tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py
```

but not by the normal application orchestration.

Likewise, `TargetWheelCompatibilityEvidence(...)` is constructed in tests/verification, with no current product producer found by the bounded source search.

This should **not** be rationalized as though the full mechanism were already a live end-to-end product path.

The historical architecture record explicitly described:

```text
integrated today: Python-support path
not yet integrated: artifact-serviceability + target-artifact-environment path
```

and the approved cross-responsibility implementation plan deliberately says heterogeneous mechanism orchestration is a **separate later responsibility**:

```text
when artifact serviceability is actually integrated into investigation.py
→ design the smallest typed multi-mechanism boundary then
```

### Assessment

```text
module-level deterministic capability: PRESENT
focused permanent tests: PRESENT
retained verification procedure: PRESENT
real S008 discovery evidence: PRESENT
normal application orchestration integration: NOT PRESENT in this snapshot
automatic exact target wheel-tag acquisition/producer: NOT PRESENT in this snapshot
```

This is a **known bounded capability/integration limitation**, not evidence of a hidden bug by itself. The plan explicitly avoided inventing a universal orchestration layer before a real second-mechanism integration responsibility was selected.

If future project work claims artifact serviceability is live in the normal application path, this integration boundary must be re-checked rather than inferred from the existence of the module/tests.

## 9. Engineering judgment: why the current separation is useful

The module keeps three facts separate:

```text
package publishes artifact capability
!=
target supports that artifact capability
!=
source fallback succeeds
```

That separation is strong because each proposition needs different evidence.

The target-agnostic candidate is intentionally broad enough to notice a package-side capability loss. Applicability then asks whether the exact target actually lost serviceability.

Trade-off:

- benefit — package evidence can be interpreted without inventing remote target facts;
- cost — candidate generation can produce possibilities that later target evidence refutes;
- justification — that is preferable to collapsing package and target evidence into one guessed conclusion.

No stronger rationale should be inferred beyond the current source, tests, S008 evidence, and recorded design history.

## 10. Python / packaging mechanisms — depth calibration

### Must own

- set difference versus set intersection and why they answer different propositions;
- evidence problem versus negative conclusion;
- package-side candidate versus target applicability;
- repository/revision evidence binding;
- target evidence must come from the target, not UpgradePilot's local environment;
- `None` as "no candidate from this bounded mechanism", not universal safety;
- applicability proof/non-proof boundaries.

### Understand operationally

- `@dataclass(frozen=True, slots=True)` as immutable compact domain records;
- `Literal[...]` as constrained vocabulary for states;
- union result types such as `Evidence | Problem`;
- `frozenset[Tag]` for stable compatibility capability sets;
- `packaging.utils.parse_wheel_filename()` and `packaging.tags.Tag`;
- early-return flow for typed problems/unresolved states;
- helper functions that isolate proposition construction.

### Recognize / lookup-level

- internal implementation details of `packaging`'s wheel parser;
- exact PEP history behind every wheel tag combination;
- advanced Python typing internals behind the `type` statement;
- every possible platform/interpreter tag family.

Know how they serve this module; look up deeper details when a real change requires them.

### Deliberately deferred from this note

- how to acquire exact target wheel tags from arbitrary repositories/environments;
- source-build execution and native compiler dependency analysis;
- universal multi-mechanism orchestration;
- complete Python packaging compatibility theory.

## 11. Fast relearning route

When returning later:

```text
1. Recall:
   removed tag != target lost wheel path.

2. Open:
   build_artifact_serviceability_impact_candidate(...)
   evaluate_artifact_serviceability_impact(...)

3. Trace S008:
   OpenCV 4.2.0.32 → 4.8.1.78
   old CPython-3.6 wheel path → proposed sdist fallback possibility.

4. Reconstruct the two set questions:
   old_tags - proposed_tags
   old/proposed tags ∩ target_tags

5. Read these two tests:
   test_removed_published_wheel_tags_form_target_agnostic_candidate
   test_different_proposed_compatible_tag_refutes_serviceability_loss

6. Explain the current limitation:
   module is tested, but normal orchestration and exact target-tag production are not currently integrated here.
```

## 12. Ownership questions

Without rereading the whole note:

1. Why is a disappeared old wheel tag insufficient to prove target impact?
2. Why must old and proposed wheel inventories each be intersected with the target's supported tags?
3. Why is `sys_tags()` from UpgradePilot's own machine invalid evidence for a remote target?
4. What did the `validate_order=True` failure teach about evidence interpretation versus linting?
5. What does a proposed sdist establish, and what does it not establish?
6. Why can this module be a real tested capability while still not being a live end-to-end application path?

## 13. Evidence anchors

Current source/test snapshot:

```text
src/upgradepilot/impact/artifact_serviceability.py
tests/test_artifact_serviceability.py
tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py
```

Directly relevant implementation history:

```text
working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md
working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md
working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md
```

Real case:

```text
product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/README.md
```

Integration boundary owner:

```text
plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md
```

This note is a frozen learning artifact, not current project-state or implementation authority.
