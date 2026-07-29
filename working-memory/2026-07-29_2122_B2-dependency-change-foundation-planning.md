# B2 Dependency Change Foundation — Planning Record

**Local timestamp:** 2026-07-29 21:22 +03:30  
**Route:** B2 — Public PR vertical slice  
**Operation:** Audit the dependency-change foundation after S001 exposed a representation gap; create the bounded prerequisite plan and align dependent plans  
**Result:** Planning and authority updates completed; no product source or tests changed

## Why this record exists

After target Python declaration Step 1 was validated on S004, S001 was selected as the first full Python-support relevance case:

```text
pydantic/pydantic PR 13432
Soup Sieve 2.6 → 2.8.4
upstream: Drop support for Python 3.8.
target: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

Before running S001 through the product, the active dependency interpreter was inspected. It supports only complete same-file exact requirement transitions:

```text
package==old_version
→ package==new_version
```

The exact S001 patch instead changes a structured `uv.lock` package record:

```toml
[[package]]
name = "soupsieve"
-version = "2.6"
+version = "2.8.4"
```

The product would therefore stop at:

```text
no_supported_pinned_change
```

before target Python, CI, package, upstream, or relevance work could run.

## Main conclusion

This is not merely an S001 syntax exception. Dependency identity is a foundational input to:

- CI authority;
- package acquisition;
- upstream repository and release identity;
- crossed-version intervals;
- target relevance;
- later decision support.

Adding a Pydantic-, Soup Sieve-, or `uv.lock` patch heuristic directly to the existing function would replace one narrow representation with accumulating case logic.

The required correction is:

```text
source-specific deterministic interpreters
→ representation-aware candidates
→ deterministic reconciliation
→ one canonical DependencyVersionChange
   or explicit unsupported/ambiguous/multiple/conflicting result
```

This broadens the foundation while keeping the first admitted domain bounded.

## Authority and specification audit

The root operating rules require:

- bound the supported domain, not a known PR;
- use source-specific evidence semantics where meaning differs;
- preserve unsupported, ambiguous, incomplete, and conflicting meaning;
- create an ADR only for durable cross-cutting architecture after Ali understands and approves the choice;
- update the owner whose responsibility changes.

The accepted minimum-useful-generality specification confirms that one fixture cannot define the product method and that representative variation is required inside the admitted boundary.

The controlling 90-day route already defines B2 as one supported Python dependency-version change without repository-specific hardcoding. It assigns broad dependency declarations, locks, role/path, and graph behavior to B4.

The correct B2 boundary is therefore:

- generalize the dependency-transition contract and extension architecture now;
- support exact-pin requirements and one structured lock representation;
- keep exactly-one-transition and explicit abstention;
- defer broad package-manager, graph, role, and multi-update behavior to B4.

## Active source findings

### Dependency interpreter

`src/upgradepilot/dependency_change.py`:

- consumes complete `ChangedFile` records;
- scans visible patch lines;
- accepts only full `package==version` syntax;
- reconciles patch line counts with GitHub metadata;
- requires one removed and one added pin;
- preserves package-name normalization and ambiguity;
- returns `PinnedDependencyChange` or `UnsupportedDependencyChange`.

The implementation is deterministic and not S004-hardcoded, but its semantic contract and name are tied to one representation.

### Tests

`tests/test_dependency_change.py` proves:

- supported exact-pin extraction;
- missing patch evidence;
- range syntax unsupported;
- package mismatch;
- multiple exact-pin changes ambiguous;
- incomplete patch evidence.

These tests are valuable and must be retained through extraction into a source-specific adapter.

### Repository file acquisition

`src/upgradepilot/github_repository.py` provides exact-head UTF-8 text acquisition with:

- path validation;
- exact immutable head SHA;
- returned path reconciliation;
- blob SHA;
- base64 and UTF-8 validation;
- a 1,000,000 decoded-byte limit;
- unavailable file evidence.

Structured `uv.lock` comparison requires equivalent exact-base acquisition and an explicit lockfile-size decision. S001's exact head `uv.lock` blob is:

```text
def33fe05d78ab851ce91a33db5bc55a439873a1
```

The file contains thousands of lines and substantial wheel metadata. The plan therefore requires measuring exact base/head byte sizes before selecting or changing acquisition bounds.

### CLI and CI coupling

The CLI invokes target, CI, package, and upstream work only after `PinnedDependencyChange` is established.

The existing CI-authority path uses `source_file` as a requirements file that a workflow explicitly installs. That is valid for an admitted `pip -r requirements-dev.txt` rule, but it must not be generalized to:

```text
uv.lock exists
→ CI installed uv.lock
```

The new canonical dependency contract must distinguish:

```text
where the change was proven
≠
how CI consumed the dependency representation
```

A first `uv.lock` transition may legitimately reach package/upstream/target stages while CI authority remains unresolved until a separate bounded `uv` consumption rule is admitted.

## Plan created

Created:

```text
plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md
```

The plan defines:

- one representation-neutral dependency-version-change contract;
- candidate versus trusted change separation;
- source-specific exact-pin and `uv.lock` interpreters;
- deterministic reconciliation;
- exact base/head structured-file acquisition;
- lockfile size, duplicate identity, multiple transition, and conflict behavior;
- evidence-path versus CI-consumption separation;
- contract, adapter, reconciliation, acquisition, CLI, test, and live-proof sequence;
- S004 preservation and S001 admission;
- B4 deferrals and stop lines.

Creation commit:

```text
d8f983426fca77f0d918369429269fe6b77837c1
```

## Stable plan corrections

### B2 gate

Updated:

```text
plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md
```

The gate now requires one supported exact-version dependency transition through an admitted representation rather than one exact-pin syntax. It also separates dependency-change evidence from CI consumption and preserves malformed, multiple, and conflicting states.

Commit:

```text
99addcfba51910f8c9843ad0ebfcb367a47ad044
```

### Target Python support relevance

Updated:

```text
plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md
```

The target plan now:

- names the dependency foundation as a prerequisite;
- consumes one trusted canonical dependency change;
- prohibits S001 end-to-end relevance work before `uv.lock` dependency identity is established;
- preserves upstream interval, trusted claim, `packaging`, conditional activation, and relevance responsibilities as downstream work;
- permits CI authority to remain unresolved where lock consumption is not separately proven.

Commit:

```text
468a6709db20329d098da92d037e02c631700af8
```

## Recommended decisions awaiting Ali review

No source implementation or ADR was created because these durable choices should be reviewed first.

### 1. Canonical contract

Recommendation:

```text
DependencyVersionChange
```

as the downstream representation-neutral type, replacing `PinnedDependencyChange` as the product-facing meaning.

Reason:

- package/upstream/target work needs package and version identity, not source grammar;
- representation provenance remains attached separately;
- later adapters can extend without downstream rewrites.

### 2. Adapter and reconciliation architecture

Recommendation:

```text
source-specific interpreters
→ candidates
→ deterministic reconciler
→ canonical change or problem
```

Reject a giant multi-format parser and case-by-case CLI branching.

### 3. First admitted representations

Recommendation:

- exact-pin requirements/constraints files;
- modified same-path `uv.lock` base/head files.

Defer all other dependency managers and lock formats.

### 4. Exact-pin file eligibility

Recommendation:

Use a bounded requirements/constraints path family rather than scanning arbitrary changed files for example text.

The exact path grammar still requires approval and tests.

### 5. Multiple dependency changes

Recommendation:

Return explicit `multiple_dependency_changes` in B2. Do not use PR title, ordering, or heuristics to choose one package.

### 6. Equivalent and conflicting candidates

Recommendation:

- semantically identical candidates combine provenance;
- different package/version transitions produce `conflicting_dependency_evidence`;
- no source-priority guess.

### 7. Duplicate `uv.lock` package names

Recommendation:

For the first boundary, require one unambiguous normalized package record per compared transition. Duplicate names across sources/markers/resolutions return `ambiguous_lock_package_identity`.

Do not design a universal uv resolution identity model inside B2.

### 8. File status

Recommendation:

Support only modified same-path `uv.lock` files first. Added, deleted, and renamed lockfiles remain unsupported because they change the comparison and identity problem.

### 9. Version meaning

Recommendation:

Preserve exact raw version strings during dependency-transition recognition. Do not use PEP 440 ordering here. `packaging` belongs to later release-interval and specifier work.

### 10. CI authority

Recommendation:

Keep the existing exact-pin install rule. For `uv.lock`, return an explicit unresolved representation/consumption reason until a separate `uv` command rule is selected.

### 11. File size

Recommendation:

Measure S001 exact base/head lock sizes and compare bounded contents versus blob acquisition. Do not remove limits merely to pass S001.

### 12. ADR

Recommendation:

After Ali accepts or revises decisions 1–11, create a durable ADR for:

```text
source-specific dependency interpreters
→ canonical contract
→ deterministic reconciliation
```

Do not create an accepted ADR before that review.

## No implementation performed

No active source, tests, runtime dependency, CLI behavior, or target repository was changed during this operation.

No claim is made that:

- `uv.lock` support exists;
- S001 passes through the product;
- CI authority understands `uv`;
- target Python relevance exists;
- UpgradePilot is production-ready.

## Exact continuation proposed by this record

1. Ali reviews the new foundation plan and the twelve recommendations above.
2. Revise any rejected boundary before code.
3. Create the architecture ADR only after approval.
4. Freeze canonical contracts and diagnostics.
5. Begin the exact-pin extraction/refactor with S004 regression proof.
6. Add reconciliation before adding `uv.lock`.
7. Add exact base/head acquisition and measure S001 lock size.
8. Implement bounded `uv.lock` interpretation.
9. Validate S004 and S001.
10. Return to the target Python support relevance plan.
