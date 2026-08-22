# AUDIT-004 — `uv.lock` Resolution-Satisfiability Evidence Boundary

**Audit date:** 2026-08-16  
**Audit type:** compact evidence-quality / future-reassessment audit  
**Inspected product source baseline:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3` (accepted Phase-E / Tranche-1 source-test revision)  
**Publication context:** learning-only commits may exist after the inspected product baseline; this audit does not change product behavior or live continuation.  
**Authority:** non-controlling audit evidence only.

## 1. Question and trigger

During S001 learning (`pydantic/pydantic#13432`, `soupsieve 2.6 -> 2.8.4` via `uv.lock`), a useful evidence question surfaced:

> If an exact-head project has a successfully resolved and current `uv.lock`, can UpgradePilot use that as evidence that the declared dependency graph is mutually satisfiable under uv's resolver, even though it does not prove source/API/runtime compatibility?

This is distinct from the current `uv.lock` extraction responsibility, which establishes the exact package-version transition from complete base/head lockfiles but does not execute uv or claim resolver success.

## 2. Prior related work — not a duplicate

### AUDIT-002

[`2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`](2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) examined CI dependency-exercise proof strength and explicitly left `uv.lock` CI-consumption semantics outside scope. It did not define positive resolver-satisfiability evidence.

### S007 package-family resolution

[`../product-simulation/scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md`](../product-simulation/scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md) and its `INVESTIGATION_SELECTION_AND_STOPPING.json` already explored the same broader proposition class from the opposite direction:

```text
Can the proposed package family form one coherent dependency set?
```

For S007, authoritative static metadata already produced a deterministic contradiction (`torch==2.8.0` versus the retained TorchVision-0.21 release family's exact Torch-2.6 requirement). An isolated pip/uv resolver dry run was considered but correctly pruned because expected resolver failure would only corroborate an already-refuted proposition.

Therefore the current audit is not introducing “resolver reasoning” from scratch. It records the missing positive-side evidence boundary for projects where an exact-head uv resolution may itself materially reduce uncertainty.

## 3. Observed current mechanism

Current source:

- [`../src/upgradepilot/dependency/analysis.py`](../src/upgradepilot/dependency/analysis.py)
- [`../src/upgradepilot/dependency/uv_lock.py`](../src/upgradepilot/dependency/uv_lock.py)

The active `uv.lock` path currently does:

```text
exact changed-file identity
+ exact base RepositoryTextFile
+ exact head RepositoryTextFile
-> parse complete TOML lockfiles
-> conservatively compare package records
-> ExtractedDependencyVersionChange
-> PR-wide DependencyVersionChange
```

That establishes dependency-transition identity and provenance. It does **not** establish that:

- uv generated the exact head lockfile;
- the lockfile is current against exact-head project metadata;
- a fresh resolver run succeeds now;
- the lock can be installed in a target environment;
- installed libraries behave correctly together.

This is the correct current boundary; no implementation defect is asserted.

## 4. External resolver semantics relevant to the question

Current official uv documentation states that:

- resolution converts requirements into package versions that fulfill the requested requirements and recursively checks compatibility of package requirements;
- `uv.lock` is created through uv's universal resolution;
- project dependencies, optional dependencies, and dependency groups are resolved together, except where conflicts are explicitly modeled;
- incompatible declared requirements cause resolution failure;
- `uv lock --check` checks that the lockfile is up to date and asserts that `uv.lock` would remain unchanged after resolution, failing if the lockfile is missing or requires an update.

Primary references:

- https://docs.astral.sh/uv/concepts/resolution/
- https://docs.astral.sh/uv/concepts/projects/dependencies/
- https://docs.astral.sh/uv/reference/cli/#uv-lock

These semantics support a distinct evidence class: **declared dependency-resolution satisfiability**.

## 5. Findings

### AUDIT-004-F1 — Successful exact-head uv resolution can reduce one specific compatibility uncertainty

**Classification:** evidence opportunity  
**Disposition:** preserve for later design/implementation selection; do not add it to current product semantics automatically.

A successful exact-head resolver observation can support a proposition of the form:

```text
exact-head project dependency declarations
+ admitted uv resolver configuration/index/source context
+ successful uv resolution
-> the declared dependency constraint graph is satisfiable under that resolver context
```

This can eliminate or reduce concern about one class of failure:

```text
mutually unsatisfiable declared package/version constraints
```

It can therefore be useful early evidence before more expensive API/runtime investigation.

### AUDIT-004-F2 — Repository presence of a valid-looking `uv.lock` is weaker than an observed current resolver check

**Classification:** proof-strength guard  
**Disposition:** if this evidence class is implemented later, keep these levels distinct.

Suggested proof ladder:

```text
L1  exact-head uv.lock exists and parses
    -> repository contains a structurally admitted lockfile

L2  exact-head lockfile is shown current against project metadata
    -> stronger relationship between declarations and lock

L3  exact-head `uv lock --check` succeeds
    -> uv reports that a resolution would leave uv.lock unchanged

L4  target-relevant `uv sync --locked` / equivalent succeeds
    -> installation/environment-formation evidence

L5  relevant import/test/runtime path succeeds
    -> behavioral evidence
```

The current S001 `uv_lock.py` responsibility is at L1 plus exact base/head comparison for transition identity. It should not silently be interpreted as L3.

A committed lockfile could theoretically be stale, manually modified, generated under materially different resolver/index assumptions, or otherwise not independently observed as current. Therefore:

```text
uv.lock exists
!=
we observed successful current resolution
```

### AUDIT-004-F3 — Resolution satisfiability is not behavioral compatibility

**Classification:** claim-boundary guard  
**Disposition:** durable reassessment guard if resolver evidence is later admitted.

Even strong resolver evidence establishes only declared metadata/constraint compatibility under the admitted resolver context. It does not establish that libraries' APIs or behavior work together.

Keep the proof classes distinct:

```text
resolver-satisfiable
!= artifact available/installable everywhere
!= installation succeeded in the target environment
!= imports succeeded
!= relevant behavior/tests succeeded
!= target compatibility/safety
!= maintainer action
```

A package can satisfy a declared version range while still breaking a consumer because of an undeclared behavioral/API incompatibility.

### AUDIT-004-F4 — Universal resolution needs proposition-specific interpretation

**Classification:** scope/semantics guard  
**Disposition:** account for this before any generic “all packages compatible” wording.

`uv.lock` is a universal lockfile. A successful universal resolution may legitimately contain marker/platform/Python-specific forks and multiple versions of a package. Therefore the strongest safe generic claim is not:

```text
one concrete package set works everywhere
```

but closer to:

```text
uv found a satisfiable universal resolution across the project's declared resolution model,
including the marker/fork/conflict semantics admitted by that project and uv configuration.
```

If UpgradePilot needs a target-specific proposition, the resolver evidence may still need to be projected onto the relevant Python/platform/extra/group context.

## 6. Why this could help UpgradePilot

For a dependency-update candidate, resolver evidence can become an early discriminator:

```text
exact dependency change
-> ask whether declared dependency graph remains satisfiable

resolution fails
-> strong early package-constraint problem; deeper runtime work may be pruned

resolution succeeds
-> remove/reduce declared-constraint-conflict uncertainty
-> continue only with remaining artifact/API/runtime/target questions
```

This complements rather than replaces existing evidence branches.

The S007 case already demonstrated the negative/pruning side: authoritative constraint evidence refuted family formation before a resolver execution was worth running. S001 exposed the corresponding positive-side opportunity: when a fresh/current uv resolution exists, it may reduce dependency-constraint uncertainty without pretending to prove behavioral compatibility.

## 7. Disposition and reassessment trigger

**Disposition:** record and defer. No source, test, plan, ADR, specification, or `MEMORY.md` change is authorized by this audit.

Reassess when one of these becomes true:

1. UpgradePilot next designs a resolver/package-family applicability investigation;
2. `uv.lock` cases need a stronger evidence tier than transition extraction alone;
3. a real case presents unresolved declared-package compatibility where an exact-head `uv lock --check` would materially discriminate the proposition;
4. later synthesis needs to distinguish resolver satisfiability from installation/runtime compatibility explicitly.

At reassessment time, the smallest useful implementation should define:

- exact input/revision/config/index authority;
- whether the check is observational or executes untrusted package metadata/build steps;
- result states such as established / refuted / unresolved rather than broad “compatible” wording;
- target-specific versus universal-resolution semantics;
- proof and stopping conditions;
- regression cases for stale lockfile, explicit conflicts, marker forks, unavailable indexes/metadata, and resolver failure.

## 8. Compact conclusion

Keep this rule available for future work:

```text
successful exact-head uv resolution
=
useful evidence of declared dependency-constraint satisfiability

but

successful exact-head uv resolution
!=
proof of library behavioral compatibility
```

Current UpgradePilot does not yet make this claim, and this audit intentionally does not activate it.