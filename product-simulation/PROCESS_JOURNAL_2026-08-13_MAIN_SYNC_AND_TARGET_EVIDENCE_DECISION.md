# Process Journal — Main Sync and Target-Evidence Decision

**Date:** 2026-08-13  
**Role:** non-authoritative execution/process journal  
**Related Cycle-02 journal:** [`REAL_WORLD_SCREENING_PROCESS_JOURNAL_CYCLE_02.md`](REAL_WORLD_SCREENING_PROCESS_JOURNAL_CYCLE_02.md)  
**Result handoff:** [`TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md`](TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md)

> This entry records how the branch synchronization and evidence-design conclusion were reached. It is not project-state authority, a source-design specification, or a replacement for `MEMORY.md`.

## 1. Why this process started

The current product-simulation work had reached a point where continuing broad screening risked becoming momentum-driven rather than decision-driven.

At the same time, `main` had advanced. The immediate task therefore changed from:

```text
continue screening
```

to:

```text
synchronize product context
→ inspect what main now needs
→ ask whether existing simulation evidence already answers it
→ only then choose any new simulation work
```

This was important because simulation should pressure real product decisions, not develop in isolation from them.

## 2. First branch comparison — histories had diverged

The original product-simulation branch was:

```text
agent/product-simulation-case-screening-02
```

Its head at the start of this pass was:

```text
d159d09aa41da4816df4622a2e4c6ce23aabc880
```

The first current-main snapshot inspected was:

```text
1785d670f1dc88ee5c76fd1456143f0f5ca57951
```

with merge base:

```text
2af5236c1d3291d44325676a714140545ad62c37
```

The histories had diverged rather than simply becoming one-sided stale.

The file-level comparison was reassuring:

- main had changed `MEMORY.md`, production source/tests/tools, and working-memory;
- the simulation side had changed `product-simulation/`;
- there was no material path overlap in the divergent work.

That made a normal history-preserving synchronization the right conceptual operation.

## 3. What changed on main — the simulation corpus had become directly relevant

The material main change was not another generic planning rewrite.

Main had opened and implemented a second mechanism:

```text
artifact_serviceability
```

Increment 1 compared old/proposed PyPI wheel inventories.

Increment 2 introduced the downstream target contract:

```text
TargetWheelCompatibilityEvidence
```

and an evaluator that asks whether one already-established target environment loses a compatible prebuilt-wheel path.

The strict boundary in source was important:

```text
package artifact evidence
!= target environment evidence
```

and UpgradePilot's own runtime tags cannot stand in for another repository.

This immediately connected main's open question to S008 and the environment-oriented challenge cases.

## 4. Main's exact unresolved question

The dated target-evidence checkpoint made the continuation explicit:

```text
owned wheel-serviceability claim
→ required target facts
→ admissible exact repository evidence
```

The evaluator existed, but UpgradePilot still could not acquire/derive real target-environment evidence automatically.

Main specifically asked to inspect `product-simulation/` before selecting the first acquisition method.

At this point broad screening was no longer the highest-value activity. Existing cases had become requested design input.

## 5. Synchronization complication — main advanced again during the pass

While synchronization was being prepared, main advanced by another six commits.

The additional file-level changes were only:

- `MEMORY.md`;
- `working-memory/2026-08-13_B2-product-simulation-review-summary.md`.

The new review summary showed that main had independently reviewed S001–S009 and the Buildtest environment challenge for the same decision.

Its conclusion was highly aligned with the simulation evidence:

- environment evidence is proposition-specific;
- real evidence is often partial and scoped;
- multiple legitimate environments must retain identity;
- apparent disagreement can reflect scope rather than conflict;
- static evidence can be sufficient;
- no new case was justified merely to discover more broad evidence shapes.

This was an important process pivot.

The task was no longer:

```text
convince main that evidence may be partial
```

because main had already reached that conclusion.

The useful remaining question became:

```text
Do branch-only S010–S012 materially sharpen the decision?
And can the corpus justify one smallest first acquisition slice?
```

## 6. Synchronization transport limitation and chosen response

The connector allowed creation of exact Git merge objects but refused the final direct branch-ref move and also refused the PR route used to move the original branch pointer.

An authenticated `gh` CLI fallback was not available in the execution environment.

The important choice was **not** to force, rewrite, rebase, or destructively replace anything.

Instead, a clean two-parent merge was constructed from:

```text
simulation head d159d09...
+
latest main 4ec8cf2...
```

with a merged tree equal to:

```text
latest main tree
+
current product-simulation subtree
```

The resulting merge commit was:

```text
14cbbd7c9019c5e468374cf10bdaba540b66dace
```

and a successor synchronized branch was created:

```text
agent/product-simulation-case-screening-02-synced-2026-08-13
```

Verification against current main showed:

```text
behind_by = 0
merge base = current main
all remaining file differences = product-simulation/
```

So the synchronized successor has the intended semantic state without rewriting either history.

The original branch remains untouched because the environment would not safely move its ref.

## 7. Re-reading the branch-only cases against the live main question

### S010

S010 mainly pressures broad candidate discovery and shows that a dependency constraint can encode a deliberate compatibility guard.

This is useful evidence-source semantics, but it does not justify expanding current wheel-serviceability acquisition into broad candidate discovery.

### S011

S011 became immediately relevant.

Its exact lesson is:

```text
optional dependency declared
!= optional dependency installed

macOS workflow exists
!= MLX optional environment formed
```

This prevents a likely acquisition error: treating workflow/platform labels as if they already establish the affected dependency environment.

S011 therefore strengthens the case for preserving:

- exact workflow/job identity;
- literal environment facts;
- exact install commands / dependency-environment formation;
- bounded negative evidence;
- unresolved when exact conditions are missing.

### S012

S012 shows that some mechanisms require historical producer-state provenance and that current repository/environment identity is not universally complete technical context.

For the current wheel-serviceability decision, this is mostly a **scope guard**.

It warns against claiming the future intermediate environment representation is universal. It does not justify importing historical state into the first wheel-evidence increment.

## 8. Source-boundary check changed the recommendation from abstract to concrete

The existing source was then inspected to avoid recommending a new subsystem disconnected from current implementation.

Two facts mattered:

1. `artifact_serviceability.py` explicitly places `TargetWheelCompatibilityEvidence` **after** acquisition/interpretation and forbids guessing tags from broad labels.
2. `ci/workflow_commands.py` already demonstrates a bounded deterministic style:
   - shallow supported workflow shape;
   - visible commands only;
   - ambiguity becomes `unresolved`;
   - no generic YAML/shell/reusable-workflow interpretation.

This suggested a first source family that reuses an existing product seam rather than creating a universal environment reconstructor.

## 9. Final design recommendation produced by the pass

The handoff records the following recommendation:

```text
partial + provenance-carrying + environment-specific facts
→ preserve before exact wheel tags
```

and proposes the first bounded acquisition family as:

```text
one statically readable GitHub Actions job
+
literal runner/platform fact, when available
+
literal setup-python version, when available
+
visible installation evidence proving the affected dependency environment is formed
→ partial target-environment evidence
```

Crucially:

```text
partial workflow facts
!= exact packaging.tags.Tag set
```

If the evidence is not enough to derive exact wheel compatibility, the result should remain insufficient/unresolved.

The existing CI command parser's *discipline* is reusable, but its current final predicate (`install + direct package invocation`) should not be copied blindly because artifact serviceability needs environment formation, not necessarily runtime invocation.

## 10. Why no S013 was admitted

The current corpus already discriminates the immediate design risks:

```text
S008  composed artifact/environment evidence
S011  optional environment and CI overclaim
C203  unresolved exact environment detail
S006  broad CI != discriminating evidence
S007  static sufficiency / investigation pruning
S001  authoritative bounded declarative refutation
```

A new case now would mostly collect another example before a new implementation hypothesis exists.

Therefore the selected simulation posture is:

```text
pause broad-world screening for this responsibility
→ let main choose/implement the first acquisition slice
→ transfer-test that concrete slice against existing cases
→ admit a new case only if a real unanswered failure mode appears
```

## 11. Result artifacts

This process produced:

- [`TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md`](TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md)
- this process journal entry

No production source, plan, architecture record, or `MEMORY.md` was changed from the simulation workspace.

## 12. Stop

Stop here for simulation-side design work on this responsibility.

The next useful trigger is a concrete main-branch choice or implementation of the target-environment acquisition slice. At that point the existing cases should be used as transfer/adversarial evaluation before searching for more cases.