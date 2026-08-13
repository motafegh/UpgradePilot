# Target Environment Evidence Design Handoff — 2026-08-13

**Status:** non-controlling simulation-to-design handoff  
**Main context reviewed:** `main@4ec8cf21e859c95ee606e00de4d8e2ac47b0dbf4`  
**Simulation context:** S001–S012 plus challenge cases  
**Owner boundary:** this file supplies transfer/adversarial evidence only; `MEMORY.md`, plans, architecture records, and production source remain authoritative for their own responsibilities.

## 1. Why this handoff exists now

Current main has already implemented the bounded downstream artifact-serviceability contract:

```text
artifact candidate
+ already-established exact target wheel tags for one environment
→ bounded target applicability
```

What remains open is the acquisition/interpretation step before those exact tags exist.

Main's current question is therefore not whether target environment matters. That is settled. The open question is:

> What is the smallest defensible way to acquire and preserve real target-environment evidence without guessing exact wheel compatibility from broad repository labels?

The existing cases now provide enough pressure to make one useful design decision and to reject several shortcuts. Another numbered case is not required for this decision.

## 2. Core recommendation

**Yes: the first target-evidence implementation should preserve partial, provenance-carrying, environment-specific facts before deriving exact `packaging.tags.Tag` compatibility.**

The current `TargetWheelCompatibilityEvidence` should remain a downstream contract for evidence that has already become exact enough. Real repository acquisition should not be forced to manufacture that object prematurely.

The conceptual flow supported by the cases is:

```text
exact repository + exact revision
→ one identified target environment / environment path
→ proposition-specific evidence items
→ partial environment facts with provenance
→ enough facts to derive exact wheel compatibility?
    ├── yes → exact TargetWheelCompatibilityEvidence
    └── no  → unresolved / insufficient for this proposition
```

This is an intermediate **responsibility**, not yet a request for a universal environment schema or generic reconstruction engine.

## 3. What must survive the intermediate boundary

The cases support preserving at least these semantics when they are material to the owned proposition:

1. **Exact repository and revision identity.** Evidence from another revision must not silently satisfy the current target proposition.
2. **Environment identity.** Multiple legitimate environments must remain distinct rather than being unioned into one repository-wide environment.
3. **Evidence provenance and scope.** A fact should retain where it came from and what that source actually establishes.
4. **Partiality.** Python version may be established while architecture, ABI, platform compatibility, or installation path remains unresolved.
5. **Dependency-environment formation.** Evidence that a platform exists is different from evidence that the changed dependency is actually installed in that environment.
6. **No broad-label-to-tag shortcut.** Labels such as `Python 3.6 on Linux`, `ubuntu-latest`, or `macOS tests` are not themselves exact wheel-tag sets.
7. **Bounded negative evidence.** An inspected workflow can establish that *that workflow* does not install an extra; it does not prove repository-global absence.
8. **Stop state.** If the currently owned proposition is already resolved by static evidence, deeper acquisition or execution should stop.

These are evidence semantics. They do not imply that every first implementation object needs one field for every item above.

## 4. Case evidence that directly supports the recommendation

### S008 — primary artifact-serviceability anchor

S008 shows that a useful target environment can be assembled from several exact repository artifacts with different scopes:

```text
Python-version context
+ installation path / requirements context
+ dependency/runtime relationship
+ CI coverage boundary
→ bounded target relevance for the artifact transition
```

It also demonstrates the key separation:

```text
package/interpreter admissibility
!= binary wheel availability
!= source fallback availability
!= source fallback success
```

The most reusable evidence shape is not a universal environment model. It is the case's provenance-carrying `TARGET_INSTALLATION_CONTEXT.json`: exact target/revision, source-specific environment facts, installation-path evidence, runtime relationship, and explicit claim limits.

### S011 — direct adversarial pressure on the acquisition layer

S011 adds a missing guard that the earlier main review did not yet have as a numbered case:

```text
optional dependency declared
!= optional dependency installed

platform-specific workflow exists
!= affected optional environment formed

workflow success
!= compatibility evidence for a dependency family the workflow never installs
```

For artifact serviceability this matters before wheel compatibility is even evaluated. A workflow or platform source is useful only for propositions that its exact commands/environment actually establish.

S011 also supports local closed-world reasoning: exact inspected workflow commands may establish that the workflow omits an extra, while repository-global absence remains unproven.

### Buildtest / C203 — unresolved is a legitimate result

The environment pathway can be established while an exact environment fact remains unavailable. Missing exact evidence must remain unresolved rather than becoming non-applicability or an invented compatibility answer.

### S006 — CI evidence is proposition-relative

Broad test or CI presence is not enough. Evidence is useful only if it forms/exercises the branch relevant to the proposition being evaluated.

### S007 — acquisition is sequential and may be pruned

A check or evidence source that looked useful at time T1 may become redundant after stronger authoritative evidence arrives at T2. `No further check needed` is a positive result when the proposition is already resolved.

### S001 — exact declarative evidence can sometimes refute a necessary proposition

An exact target declaration can be sufficient negative evidence when the declaration is authoritative for the bounded proposition. This supports using partial facts to close some branches without first manufacturing a complete environment.

### S010 — declarations can carry compatibility semantics

A version constraint can be an explicit compatibility guard rather than arbitrary package syntax. Target evidence acquisition should preserve source meaning when exact evidence supports that interpretation instead of flattening every declaration into generic version metadata.

### S012 — important scope guard, but not a reason to expand this increment

S012 shows that some mechanisms depend on durable state produced under an earlier environment:

```text
current repository/revision/environment
!= always the complete technical context
```

That is a real mature-system responsibility. It should **not** be imported into the current wheel-serviceability acquisition slice unless a wheel candidate itself makes historical producer context necessary. S012 is therefore a guard against claiming a universal environment model, not a requirement for this increment.

## 5. Recommended first implementation slice

The smallest useful first acquisition family is a **single statically readable GitHub Actions job**, reusing the product's existing exact-workflow acquisition and shallow workflow-reading posture rather than opening a parallel repository scanner.

The slice should be narrower than generic YAML/environment reconstruction.

For one exact workflow job, admit only literal/static facts that can be read deterministically, for example:

```text
workflow file + job identity
+ literal runner/platform declaration, if present
+ literal setup-python version, if present
+ visible install command proving the changed dependency source/environment is formed
→ partial target-environment evidence
```

Important boundary:

> The output of this first slice should normally be **partial environment evidence**, not automatically `TargetWheelCompatibilityEvidence`.

A literal `ubuntu-latest` plus Python version is still not permission to invent exact supported wheel tags. If architecture/platform/ABI facts required for exact wheel compatibility are not defensibly established, the downstream result remains insufficient/unresolved.

Why start here:

- exact GitHub workflow acquisition already exists in the product;
- `ci/workflow_commands.py` already demonstrates the desired bounded style: shallow supported syntax, deterministic extraction, and `unresolved` rather than guessing;
- S011 gives a strong adversarial case for checking whether the affected dependency environment is actually formed;
- this slice can produce useful evidence even when it cannot yet finish exact wheel compatibility;
- it avoids opening container registries, deployment systems, arbitrary shell interpretation, generic YAML evaluation, or universal platform reconstruction at once.

This recommendation does **not** require reusing the existing `source installed AND package invoked` CI conclusion as-is. Artifact serviceability needs an environment-formation proposition, not necessarily direct runtime invocation. Reuse the acquisition/parsing discipline, not an unrelated final predicate.

## 6. What the first slice should deliberately not do

Do not make the first increment responsible for:

- every workflow/job/matrix/reusable-workflow shape;
- arbitrary expression evaluation;
- every container/deployment/configuration source;
- mapping broad runner labels directly to exact `packaging.tags.Tag` sets;
- repository-wide environment unioning;
- selecting one canonical environment for the repository;
- generic cross-source conflict resolution;
- historical persisted-state reconstruction from S012;
- source-build success;
- maintainer merge/block/defer recommendation.

Unsupported or incomplete cases should remain partial/unresolved and become evidence for the next bounded increment.

## 7. Product-simulation job selection from here

For the simulation branch, broad-world screening should pause for this responsibility.

The next useful simulation job is **transfer evaluation after main implements the first acquisition slice**, not S013 for momentum.

Use existing anchors first:

```text
S008     → can composed static environment evidence be preserved without overclaiming exact tags?
S011     → does CI/platform evidence prove the affected optional environment is formed, or does the method overclaim?
C203     → can exact environment detail remain unresolved?
S006     → does broad CI get mistaken for discriminating evidence?
S007     → can stronger static evidence prune deeper work?
S001     → can authoritative bounded declarations close a necessary proposition when appropriate?
```

Only admit a new case if that implementation exposes a concrete unanswered behavior that the existing corpus cannot discriminate.

S010 and S012 should remain future transfer anchors for broader candidate-discovery and historical-state responsibilities; they should not expand the current artifact-serviceability increment merely because they exist.

## 8. Decision summary

```text
CURRENT DOWNSTREAM CONTRACT
exact target wheel tags for one established environment
→ keep

NEW ACQUISITION RESPONSIBILITY
partial + provenance-carrying + environment-specific target facts
→ yes, justified

FIRST EVIDENCE FAMILY
one statically readable GitHub Actions job
→ recommended bounded entry

BROAD LABEL → EXACT TAGS
→ forbidden

MULTIPLE ENVIRONMENTS
→ preserve identity; do not union

MISSING EXACT FACT
→ unresolved, not negative evidence

NEW NUMBERED CASE NOW
→ no

NEXT SIMULATION WORK
→ evaluate the implemented acquisition slice against existing anchors
```

This is the strongest conclusion the current corpus supports without over-designing the mature system.