# Process Journal — Main Refresh 02

**Date:** 2026-08-13  
**Role:** non-authoritative execution/process journal  
**Active simulation branch:** `agent/product-simulation-case-screening-02`  
**Related handoff:** [`TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md`](TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md)

> This journal records how the current synchronization/review decision was reached. It is not live project-state authority and does not replace `MEMORY.md`.

## 1. Why the work changed direction

Broad screening had been continuing on Cycle 02 when `main` advanced materially again. The correct next action therefore changed from finding another case to:

```text
refresh main
→ identify the exact new implementation/design boundary
→ test whether existing simulation evidence already answers it
→ synchronize branch context
→ only then choose more simulation work
```

This avoided continuing research against a stale product model.

## 2. What changed on main

The important main-side advance is the second technical mechanism:

```text
artifact serviceability
```

The current product now has:

- exact old/proposed PyPI artifact inventory interpretation;
- wheel-tag parsing using `packaging`;
- preservation of source-distribution availability;
- a target-agnostic artifact-serviceability candidate;
- `TargetWheelCompatibilityEvidence` / problem state;
- bounded target applicability using exact old/proposed wheel inventories and an already-established target-supported tag set;
- permanent focused regression coverage.

Fresh main memory records Increment 2 as verified complete at its bounded scope:

```text
retained Increment-2 smoke: PASS
focused artifact-serviceability suite: 11 tests, OK
full active suite: 397 tests, OK
```

The remaining problem is **not** artifact applicability itself. It is how exact repository-owned evidence may legitimately become target-environment facts before `TargetWheelCompatibilityEvidence` exists.

## 3. Main independently reviewed the simulation corpus

Current main now contains a product-simulation review summary covering S001–S009 plus the Buildtest environment case.

Main independently reached several conclusions already supported by our branch work:

- environment evidence is proposition-specific;
- repository evidence is often partial/scoped rather than one complete environment description;
- multiple legitimate environments must retain identity;
- apparent disagreement may be scope difference rather than conflict;
- broad CI/package exercise is not proof of the exact artifact-selection path;
- static evidence can sometimes close the proposition and deeper work should stop;
- no universal environment reconstructor is justified.

This changed the role of our branch evidence. We no longer need to argue that partial/environment-specific evidence exists. The useful question is what **additional discriminating pressure** branch-only cases add.

## 4. Case transfer review

### S008 — primary direct anchor

S008 remains the closest real artifact-serviceability case.

It shows that different repository artifacts establish different facts:

- exact dependency declaration;
- documented installation path;
- direct runtime relationship;
- Python-3.6 repository context;
- bounded CI coverage.

The Dockerfile establishes Python-3.6 relevance but does not itself prove that OpenCV is installed through that exact environment. This is a concrete reason to preserve source/provenance/scope per fact rather than flattening several observations into one canonical target environment.

### S011 — most important branch-only addition for the current decision

S011 sharpens the current acquisition boundary:

```text
optional dependency declared
!= optional dependency installed

macOS workflow exists
!= affected MLX environment formed
```

The exact inspected workflows install only `.[dev]`, not `.[mlx]`.

Therefore a workflow/platform label can be relevant context while still being non-discriminating for whether the changed dependency environment exists.

This is directly useful for a first workflow-based target-evidence implementation.

### Buildtest / C203

A target environment path can be real while one exact compatibility-critical fact remains unavailable. The correct result remains unresolved rather than guessed.

### S007

Environment formation can depend on package index/build family/coordinated package versions and documented environment intent. This prevents reducing target environment to only Python version + operating system.

### S010

A declaration can carry compatibility semantics (for example an intentional version guard), but broad candidate discovery remains outside the current artifact-evidence slice.

### S012

Historical producer state can matter for persisted-artifact mechanisms. This is a real mature-system boundary but should remain out of the current wheel-serviceability increment unless the mechanism itself demands history.

## 5. Current simulation recommendation

The existing handoff remains valid and is now better interpreted as a **specific next-step recommendation**, not a general argument.

Recommended first acquisition family:

```text
one statically readable GitHub Actions job
+ exact workflow/job identity
+ literal runner/platform fact when present
+ literal setup-python version when present
+ visible install evidence showing whether the changed dependency environment is formed
→ partial provenance-carrying target-environment evidence
```

Important boundary:

```text
partial workflow/environment facts
!= exact packaging.tags.Tag set
```

If the facts are insufficient for exact wheel compatibility, the downstream state must remain unresolved/insufficient.

The useful reuse from existing CI code is the **bounded deterministic parsing discipline**, not blindly reusing an unrelated final predicate such as requiring direct package invocation.

## 6. Synchronization process

The branch had diverged from current main. Direct two-parent merge creation and the temporary PR route were blocked by the connector safety layer during this refresh.

The response was deliberately non-destructive:

1. identify the exact main-only delta affecting the active branch;
2. copy the exact current main versions of the missing main-owned files onto Cycle 02;
3. verify blob identity rather than relying on prose comparison;
4. do not force-update or rewrite branch history.

Verified current blob equality between Cycle 02 and main for the active artifact-serviceability state includes:

- `MEMORY.md`;
- `working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`;
- `src/upgradepilot/impact/artifact_serviceability.py`;
- `tests/test_artifact_serviceability.py`.

Git ancestry remains formally divergent because the connector refused creation of the final merge object. The working branch content used for the current decision is nevertheless aligned with main for the relevant main-owned state.

No force push, rebase, history rewrite, or target repository mutation was performed.

## 7. What not to do next

Do not admit S013 merely because broad screening can continue.

Do not expand the current artifact-serviceability question into:

- universal environment reconstruction;
- historical-state reconstruction from S012;
- generic cross-source conflict resolution;
- every CI/workflow syntax form;
- exact wheel-tag invention from broad runner labels;
- a generic planner/registry/plugin architecture.

## 8. Next branch duty

For this responsibility, broad screening should pause.

The next useful trigger is a concrete main-side decision or implementation of the first target-environment evidence slice.

Then use the existing corpus as transfer/adversarial evaluation:

```text
S008 → composed static evidence without overclaiming exact tags
S011 → platform/CI evidence without forming affected optional environment
C203 → unresolved exact environment detail
S006 → broad CI versus discriminating evidence
S007 → static sufficiency / pruning
S001 → authoritative bounded declarative evidence
```

Only search for a new case if the implemented slice exposes a behavior the existing anchors cannot discriminate.

## 9. Stop

The immediate synchronization/review question is answered.

Cycle 02 should now act as a transfer-test lab for the target-environment evidence boundary rather than continue broad screening for momentum.
