# ADR-0004 — Dependency Version Change Evidence

**Status:** Accepted  
**Date:** 2026-07-30  
**Owner:** Ali Rajabi  
**Scope:** Deterministic source-specific dependency-version extraction and one representation-neutral trusted dependency transition  
**Controlling plan:** [`../../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Naming standard:** [`../specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)

## Context

At this decision boundary, UpgradePilot could establish an exact dependency transition from conventional `package==version` patch evidence but could not handle materially different structured dependency representations such as `uv.lock` without leaking file-format semantics into downstream CI/package/upstream/target logic.

Dependency identity is a high-authority upstream responsibility. The selected design therefore needed to preserve exact evidence, handle multiple formats conservatively, and expose ambiguity rather than choosing a convenient package/change.

## Decision

### 1. Source-specific extraction, representation-neutral comparison

Use:

```text
supported dependency source
→ source-specific deterministic extraction
→ ExtractedDependencyVersionChange | explicit source problem

all admitted extracted changes/problems
→ compare_extracted_dependency_changes(...)
→ DependencyVersionChange | explicit comparison problem
```

`DependencyVersionChange` means only that admitted dependency-file evidence establishes one package transition from one exact old version string to one exact proposed version string. It does not establish dependency role, CI consumption, compatibility, safety, or maintainer action.

### 2. Exactly one trusted transition in the admitted B2 responsibility

Equivalent extracted changes require the same normalized package identity and exact raw old/proposed version strings. Equivalent evidence may be combined.

Several distinct package transitions remain `multiple_dependency_version_changes`; incompatible representations of the same update remain `conflicting_dependency_version_changes`.

PR title, patch order, alphabetical order, known-case identity, or convenience must not select one transition.

A recognized admitted dependency file that is malformed, unavailable, incomplete, or beyond the supported bound prevents a trusted result rather than being ignored because another file produced a convenient answer.

### 3. First admitted source families

The first source families are:

1. conventional exact requirements/constraints representations using `package==version` evidence;
2. modified same-path files whose basename is exactly `uv.lock`.

Path/source eligibility establishes only that a file may supply package/version evidence.

### 4. Preserve exact version evidence; parse semantics downstream

Extraction preserves exact raw old/proposed version strings and validates only the narrow source contract needed to establish a textual change.

PEP 440 parsing, equivalence, ordering, and crossed-release semantics belong to the later version-method responsibility. A later version-semantics failure does not erase the observed dependency-file transition.

### 5. Exact structured-file acquisition

When complete base/head file content is required, acquire it only at the exact immutable pull-request base/head revisions and preserve repository, path, requested revision, returned path, blob identity, reported size, decoded size, and UTF-8 text.

The admitted content bound is **1,000,000 decoded bytes**. Enforce the reported-size bound before decoding, then verify decoded size and the bound again. Do not add blob/raw/large-file fallback merely to make an oversized or unavailable file succeed.

### 6. First `uv.lock` boundary

Use Python's standard-library TOML parser (`tomllib`) for the first bounded rule; add no TOML dependency for this responsibility.

Admit the initial lock schema:

```text
version = 1
revision = non-negative integer
```

The first file-status boundary supports only a modified `uv.lock` at the same complete path on base and head with both exact files available. Added/deleted/renamed lockfiles remain unsupported until separately admitted.

### 7. `uv.lock` record comparison

Group package records by normalized package identity.

For unambiguous single-record groups, preserve source/resolution-context identity and establish only exact version transitions. Do not silently pair records whose source/resolution context changed.

Repeated package-name groups are handled conservatively:

- remove only top-level `sdist` and `wheels` artifact fields from the equality comparison;
- retain all other fields and internal list ordering;
- compare repeated records as unordered multisets so file order does not matter but duplicate counts do;
- unchanged duplicate groups do not block another unambiguous transition;
- changed duplicate groups remain ambiguous.

Do not infer uv resolver semantics, pair repeated records by position, or select the first convenient record.

### 8. CI dependency exercise remains a separate responsibility

Dependency-file evidence and CI-consumption proof are different facts.

The first CI result vocabulary distinguishes:

```text
proven
no_successful_ci
unresolved
```

Only an explicitly admitted rule may establish that exact-head successful CI consumed and exercised the changed dependency. `uv.lock` or constraints evidence does not inherit requirements-file installation semantics automatically.

Unresolved CI does not erase trusted dependency identity and must not be presented as green dependency-exercise evidence.

## Alternatives considered

### Keep only exact requirements parsing

Rejected as the destination because downstream logic would depend permanently on one incidental dependency-file grammar and selected real evidence could not be represented honestly.

### One giant multi-format parser

Rejected because patch-based requirements evidence and complete structured base/head files have materially different source/failure semantics.

### Per-format branching throughout downstream code

Rejected because representation details would leak into CI, package, upstream, target, and decision responsibilities.

### Infer structured lock changes from patch proximity

Rejected because structured/artifact metadata can make patch locality misleading. Exact complete base/head files are the trust boundary.

### Fully interpret repeated uv resolution branches

Rejected for this bounded decision because correct pairing can require resolver/marker/source semantics outside the admitted responsibility.

### Change acquisition mechanism or size bound for the known case

Rejected because the selected case fit the existing bounded Contents-path approach. A new transport mechanism requires evidence of an actual unsupported need.

## Consequences

### Benefits

- downstream code consumes one clear dependency-transition meaning independent of source format;
- adding a source representation stays localized to extraction/comparison boundaries;
- exact raw evidence is preserved;
- malformed, ambiguous, multiple, conflicting, and oversized evidence remains explicit;
- source evidence remains separate from CI-consumption proof;
- the design remains deterministic and testable without semantic-model trust.

### Costs

- more explicit domain/problem states than the former one-function path;
- exact base/head acquisition for structured sources;
- conservative abstention for changed duplicate-resolution groups;
- first `uv.lock` support is intentionally narrow;
- CI exercise may remain unresolved for otherwise valid source representations.

These costs are accepted because explicit non-proof and bounded abstention are preferable to guessed dependency identity.

## Reversibility

The decision remains reversible because source extractors are independent, comparison is representation-neutral, raw/source evidence is retained, and no dynamic plugin framework, persistence schema, service boundary, or target mutation is introduced.

A source representation may return to explicit unsupported status if it cannot remain bounded and trustworthy without changing downstream semantics.

## Reassessment triggers

Reassess when evidence shows that:

- admitted files commonly exceed the existing size/acquisition boundary;
- GitHub changes the relied-on exact-file behavior;
- uv changes the admitted schema incompatibly;
- common lockfiles frequently produce unsupported structural ambiguity that a bounded identity rule can resolve;
- downstream consumers genuinely require source-specific meaning absent from `DependencyVersionChange`;
- conventional source eligibility creates material false positives;
- a selected responsibility requires broader CI-consumption semantics.

Convenience, a known case title, or the existence of a larger parsing framework is not by itself a trigger.

## Proof boundary

The controlling plan and product tests own the detailed proof matrix. At minimum, implementation evidence must discriminate:

- supported versus arbitrary dependency files;
- equivalent versus multiple/conflicting transitions;
- complete versus malformed/unavailable/oversized structured evidence;
- exact source/revision identity;
- supported versus ambiguous `uv.lock` groups;
- dependency identity versus CI-consumption proof;
- known-case success from generic rules rather than hardcoding.

Acceptance of this ADR authorizes the method; it does not itself prove implementation or learner ownership.
