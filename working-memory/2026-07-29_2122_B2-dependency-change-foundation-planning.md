# B2 Dependency Change Foundation — Planning Record

**Local timestamp:** 2026-07-29 21:22 +03:30  
**Route:** B2 — Public PR vertical slice  
**Operation:** Audit the dependency-change foundation after S001 exposed a representation gap; create the bounded prerequisite plan and align every affected stable plan  
**Result:** Planning and authority updates completed; no product source or tests changed

## Trigger

After target Python declaration Step 1 was validated on S004, S001 was selected as the first full Python-support relevance case:

```text
pydantic/pydantic PR 13432
Soup Sieve 2.6 → 2.8.4
upstream: Drop support for Python 3.8.
target: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

The active dependency interpreter supports only complete same-file exact requirement transitions:

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

The product would therefore stop at `no_supported_pinned_change` before target Python, CI, package, upstream, or relevance work could run.

## Main conclusion

This is not merely an S001 syntax exception. Dependency identity is foundational input to:

- CI authority;
- package acquisition;
- upstream repository and release identity;
- crossed-version intervals;
- target relevance;
- later decision support.

Adding a Pydantic-, Soup Sieve-, or S001-specific patch rule would replace one narrow representation with accumulating fixture logic.

The required correction is:

```text
source-specific deterministic interpreters
→ representation-aware candidates
→ deterministic reconciliation
→ one canonical DependencyVersionChange
   or explicit unsupported/ambiguous/multiple/conflicting result
```

This broadens the foundation while keeping B2 bounded.

## Authority and specification audit

The root operating rules and accepted minimum-useful-generality specification require:

- bound the supported domain, not a known PR;
- use source-specific evidence semantics where meanings differ;
- preserve unsupported, ambiguous, incomplete, and conflicting states;
- avoid a handcrafted implementation per fixture;
- create an ADR only for a durable cross-cutting choice after Ali understands and approves it;
- update each truth owner only when its own responsibility changes.

The controlling 90-day route already defines B2 as one supported Python dependency-version change without repository-specific hardcoding. It assigns broad declarations, locks, role/path, graphs, and wider context reasoning to B4.

The selected boundary is therefore:

- generalize the dependency-transition contract and extension architecture now;
- preserve exact-pin requirements and admit one structured lock representation;
- keep exactly one transition and explicit abstention;
- defer broad package-manager, graph, role, and multi-update behavior to B4.

## Active-source findings

### Dependency interpretation

`src/upgradepilot/dependency_change.py`:

- consumes complete `ChangedFile` records;
- scans visible patch lines;
- accepts only full `package==version` syntax;
- reconciles patch counts with GitHub metadata;
- requires one removed and one added pin;
- normalizes package names;
- preserves ambiguity and unsupported syntax;
- returns `PinnedDependencyChange` or `UnsupportedDependencyChange`.

The implementation is deterministic and not S004-hardcoded, but its contract and name are tied to one representation.

### Tests

`tests/test_dependency_change.py` proves:

- supported exact-pin extraction;
- missing patch evidence;
- range syntax unsupported;
- package mismatch;
- multiple exact-pin changes ambiguous;
- incomplete patch evidence.

These protections must survive extraction into a source-specific adapter.

### Exact repository files

`src/upgradepilot/github_repository.py` provides exact-head UTF-8 acquisition with:

- path validation;
- exact immutable head SHA;
- returned-path reconciliation;
- blob SHA;
- base64 and UTF-8 validation;
- a 1,000,000 decoded-byte limit;
- unavailable file evidence.

Structured `uv.lock` comparison requires equivalent exact-base acquisition and a justified lockfile-size decision.

S001's exact-head `uv.lock` blob is:

```text
def33fe05d78ab851ce91a33db5bc55a439873a1
```

It contains thousands of lines and extensive wheel metadata. Exact base/head byte sizes must be measured before selecting or changing acquisition bounds.

### CLI and CI coupling

The CLI invokes later evidence stages only after `PinnedDependencyChange` is established.

The existing CI-authority path treats `source_file` as a requirements file that a workflow explicitly installs. That is valid for an admitted `pip -r requirements-dev.txt` rule but cannot be generalized to:

```text
uv.lock contains the change
→ CI consumed uv.lock
```

The canonical contract must distinguish:

```text
where the change was proven
≠
how CI consumed the representation
```

A first `uv.lock` transition may reach package/upstream/target evidence while CI authority remains unresolved until a separate bounded `uv` consumption rule is admitted.

## New bounded plan

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

Commit:

```text
d8f983426fca77f0d918369429269fe6b77837c1
```

## Stable plan corrections

### B2 public vertical-slice gate

Updated:

```text
plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md
```

The gate now requires one supported exact-version dependency transition through an admitted representation rather than one exact-pin syntax. It separates dependency-change evidence from CI consumption and preserves malformed, multiple, and conflicting states.

Commit:

```text
99addcfba51910f8c9843ad0ebfcb367a47ad044
```

### Target Python support relevance

Updated:

```text
plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md
```

The plan now:

- names the dependency foundation as a prerequisite;
- consumes one trusted canonical dependency change;
- prohibits S001 end-to-end relevance work before `uv.lock` dependency identity is established;
- preserves upstream interval, trusted claim, `packaging`, conditional activation, and relevance responsibilities as downstream work;
- permits CI authority to remain unresolved where lock consumption is not separately proven.

Commit:

```text
468a6709db20329d098da92d037e02c631700af8
```

### Transparent decision method

Updated:

```text
plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md
```

The decision plan now consumes a trusted canonical exact-version dependency transition rather than an exact-pin type. It explicitly separates representation provenance from role, usage, CI consumption, sufficiency, and action meaning. Its contrast proof now requires equivalent downstream behavior across admitted representations.

Commit:

```text
3dc7129a86cefe3fb1e911a6979e3d6ac62d73c5
```

### Minimum package and upstream evidence

Updated:

```text
plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md
```

The package plan now consumes a representation-neutral package/old-version/proposed-version contract and no longer requires a requirements-file-specific `source_file`. Dependency evidence paths remain provenance only and cannot create CI or package authority.

Commit:

```text
bdfa6677ed9f32ebac8953d28cae1e13fc064f9f
```

### Documents intentionally unchanged

No change was made to:

- `PROJECT_CHARTER.md` — mission and frozen product boundary did not change;
- `plans/UPGRADEPILOT_90_DAY_PLAN.md` — it already requires one supported dependency-version change and assigns broader dependency breadth to B4;
- `plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md` — it is a completed historical gate record and already describes a selected supported dependency form rather than a permanent exact-pin method;
- minimum-useful-generality specification — its project-wide rule already controls this correction;
- historical learning and working-memory records — they accurately preserve what was true at their dates;
- architecture register — no ADR was accepted yet.

## Recommended durable decisions awaiting Ali review

No source implementation or ADR was created because these choices require review first.

1. **Canonical contract** — use one representation-neutral `DependencyVersionChange` downstream.
2. **Architecture** — source-specific interpreters produce candidates; a deterministic reconciler produces the trusted result.
3. **First representations** — exact-pin requirements/constraints plus modified same-path `uv.lock`.
4. **Exact-pin eligibility** — use a bounded requirements/constraints path family rather than arbitrary changed files.
5. **Exactly-one boundary** — return `multiple_dependency_changes`; do not select one package heuristically.
6. **Equivalent/conflicting candidates** — combine provenance for identical transitions; return conflict for different transitions.
7. **Duplicate lock identities** — abstain when normalized `uv.lock` names are not uniquely comparable.
8. **File status** — support only modified same-path `uv.lock` first.
9. **Version meaning** — preserve raw exact version strings here; defer PEP 440 ordering to later release-interval work.
10. **CI authority** — preserve the exact-pin install rule; keep `uv.lock` consumption unresolved until separately proven.
11. **File size** — measure exact S001 base/head sizes and select a bounded acquisition method; do not remove limits merely to pass the case.
12. **ADR** — after decisions 1–11 are approved or revised, create a durable representation-policy ADR before source implementation.

## No implementation performed

No active source, tests, runtime dependency, CLI behavior, or target repository was changed.

No claim is made that:

- `uv.lock` support exists;
- S001 passes through the product;
- CI authority understands `uv`;
- target Python relevance exists;
- UpgradePilot is production-ready.

## Exact continuation proposed by this record

1. Ali reviews the foundation plan and twelve recommendations.
2. Revise any rejected boundary before code.
3. Create the architecture ADR only after approval.
4. Freeze canonical contracts and diagnostics.
5. Extract the exact-pin implementation with S004 regression proof.
6. Add deterministic reconciliation before `uv.lock`.
7. Add exact base/head acquisition and measure S001 lock sizes.
8. Implement bounded `uv.lock` interpretation.
9. Validate controlled tests, full suite, S004, and S001.
10. Return to the target Python support relevance plan.
