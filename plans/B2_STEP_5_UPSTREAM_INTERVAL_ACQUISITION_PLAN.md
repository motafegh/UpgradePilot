# B2 Step 5 — Authoritative Upstream Interval Acquisition Plan

**Status:** Selected implementation plan for parent-plan Step 5  
**Route:** B2 — Public PR vertical slice  
**Parent plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Prerequisites:** Steps 1–4 behavior-validated  
**Selected proof case:** S001 — `soupsieve` `2.6 → 2.8.4`

## Purpose

Implement the bounded network/evidence path that earns the exact upstream interval records already defined by Step 1.

The target flow is:

```text
DependencyReleaseInterval
+ trusted upstream repository identity
→ complete package release index
→ PEP 440 crossed-release selection
→ CrossedReleaseIndexEvidence

trusted upstream repository
+ accepted proposed-version tag
→ exact tag reference
→ resolved immutable commit
→ exact bounded changelog file
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
   or explicit problem
```

Step 5 acquires and reconciles evidence. It does not extract semantic support-drop claims, use an LLM, compare target Python ranges, reorder the CLI, or make compatibility/safety/recommendation decisions.

## Why Step 5 is split into bounded increments

This responsibility crosses several independent trust boundaries:

1. PyPI project release-index acquisition;
2. standards-based release selection and ordering;
3. Git tag reference resolution and annotated-tag peeling;
4. exact immutable repository-file acquisition;
5. construction of the existing Step 1 authority records.

Combining these in one vague client would make failures difficult to diagnose and would obscure which external source established each fact.

The implementation therefore proceeds in small increments while remaining one parent-plan Step 5 responsibility.

## Increment 5A — complete package release index

### Source

Use the public PyPI project JSON endpoint for the dependency package:

```text
/pypi/{normalized-package}/json
```

The project response is used only to establish package identity and the exact raw release keys published in the registry response.

### Source-specific evidence

Add:

```text
PackageReleaseIndexEvidence
├── requested_package
├── normalized_package
├── published_name
├── source_url
├── retrieved_at
├── last_serial
└── release_versions[]
```

`release_versions[]` preserves exact raw JSON object keys. Acquisition does not assign PEP 440 meaning or semantic order.

Add an explicit problem result for:

```text
package_not_found_or_inaccessible
identity_mismatch
malformed_response
acquisition_failed
```

### Crossed-release selection

A separate pure function consumes the acquired index plus `DependencyReleaseInterval`.

```text
PackageReleaseIndexEvidence
+ DependencyReleaseInterval
+ upstream repository identity
→ select_crossed_release_index(...)
→ SelectedCrossedReleaseIndex
   ├── evidence: CrossedReleaseIndexEvidence
   └── ignored_non_pep440_versions[]
   or CrossedReleaseIndexSelectionProblem
```

The selector must:

- reuse the accepted `packaging.version.Version` semantics;
- parse the dependency interval through the Step 3 method;
- admit release keys whose parsed meaning satisfies `old < release <= proposed`;
- preserve exact raw selected strings;
- require the exact raw proposed version to be present;
- reject PEP 440-equivalent duplicate selected identities through the existing crossed-release ordering method;
- preserve non-PEP-440 registry keys explicitly as ignored/out-of-scope rather than silently treating them as ordered releases;
- produce deterministic ordering;
- never hardcode S001 package names or versions.

The successful embedded `CrossedReleaseIndexEvidence` means the complete set of **admitted PEP 440 release identities** in the selected interval from that PyPI project response. It does not claim every arbitrary legacy/non-PEP-440 registry key has comparable version meaning.

## Increment 5B — exact proposed tag to commit

Add a dedicated GitHub tag-resolution responsibility rather than duplicating release-client logic.

Required result shape:

```text
repository
requested_tag
tag_ref
tag_object_type
tag_object_sha
resolved_commit_sha
```

Rules:

- accept only an explicitly supplied accepted version-tag form;
- exact returned ref must match `refs/tags/{requested_tag}`;
- lightweight tag: ref points directly to `commit`;
- annotated tag: peel tag object(s) deterministically to a commit;
- impose a small explicit maximum peel depth and detect cycles;
- unsupported object type, malformed identity, missing tag, or acquisition failure remains explicit.

Do not infer a tag from release title text.

## Increment 5C — exact immutable changelog file

Broaden the existing repository-file acquisition mechanism only enough to read a bounded UTF-8 file at an arbitrary **immutable commit SHA** while preserving the same strict evidence already used for exact PR base/head files:

```text
repository
requested path
returned path
revision/commit SHA
blob SHA
reported bytes
decoded bytes
UTF-8 content
```

PR-specific helper methods must keep their current guards and behavior.

The tagged-changelog composition then combines:

```text
DependencyReleaseInterval
+ resolved exact tag commit
+ one explicit normalized changelog path
+ exact repository file evidence
→ TaggedChangelogEvidence
   or UpstreamAuthoritySourceProblem
```

The acquisition API accepts a path; it does not hardcode an S001 path. Changelog-path discovery is not silently mixed into file retrieval. If automated path discovery becomes necessary, it requires its own bounded rule before activation.

## Increment 5D — Step 1 authority composition

Use the existing pure Step 1 assembler rather than creating a second authority implementation:

```text
assemble_upstream_interval_authority(...)
```

For the first S001 proof, the minimum successful authority path is:

```text
complete PyPI-derived crossed-release index
+ exact proposed-tag changelog
→ authority_basis = tagged_changelog
```

A complete GitHub Release-body series is a valid alternative authority path but is not required merely to prove S001 if the tagged changelog path succeeds.

## Naming rules

Names in this step must expose their source or responsibility. Prefer concrete names such as:

```text
PackageReleaseIndexEvidence
select_crossed_release_index
SelectedCrossedReleaseIndex
GitHubTagCommitEvidence
resolve_tag_to_commit
acquire_exact_repository_text_file
```

Avoid generic names such as `manager`, `processor`, `context`, `resolver` where the exact action can be named.

## Educational code requirements

New source should include:

- a module docstring showing where the file sits in the data flow;
- concise class/function docstrings that state both responsibility and non-responsibility;
- comments only where an invariant, trust boundary, or non-obvious failure rule needs explanation;
- short ASCII data-flow representations when they materially improve later study;
- no line-by-line narration of obvious Python syntax.

## Controlled proof obligations

### Increment 5A

Tests must prove:

1. PyPI project lookup normalizes the requested package but preserves requested/published identity;
2. exact raw release keys are retained deterministically;
3. malformed `releases` structure is not trusted;
4. package 404 remains explicit;
5. successful response with a conflicting published package name is identity mismatch;
6. transport/HTTP/size/JSON failures remain acquisition or malformed problems as appropriate;
7. `2.6 → 2.8.4` over raw releases including `2.7`, `2.8`, `2.8.1`, `2.8.2`, `2.8.3`, `2.8.4` selects only the old-exclusive/proposed-inclusive set;
8. releases above the proposed version and the old version are excluded;
9. selected PEP 440-equivalent duplicates stop rather than being silently collapsed;
10. exact proposed raw identity must exist;
11. non-PEP-440 registry keys are preserved as ignored/out-of-scope;
12. source URL/retrieval time/repository/interval provenance survives into `CrossedReleaseIndexEvidence`;
13. no fixture-specific package/version logic enters production source.

### Later Step 5 increments

Before Step 5 closes, tests must additionally prove:

- lightweight and annotated tag resolution;
- bounded nested tag peeling and cycle/depth failure;
- exact immutable changelog file identity and byte agreement;
- unavailable/malformed/tag/path/blob problems remain explicit;
- successful tagged changelog constructs the exact Step 1 record;
- the existing Step 1 assembler accepts the resulting S001-shaped authority bundle;
- the complete repository test suite remains green.

## Initial modification surface

Increment 5A may modify:

```text
src/upgradepilot/pypi_client.py
src/upgradepilot/upstream_interval_acquisition.py
src/upgradepilot/__init__.py
tests/test_pypi_client.py
tests/test_upstream_interval_acquisition.py
tests/test_package_interface.py
```

Later increments may deliberately touch GitHub tag/repository acquisition modules and their tests.

Do not modify during Increment 5A:

```text
src/upgradepilot/cli.py
src/upgradepilot/upstream_claim.py
src/upgradepilot/target_python.py
src/upgradepilot/target_python_relevance.py
```

## Validation cadence

Each Step 5 increment stops at a local validation gate:

```text
focused tests
→ complete deterministic suite
→ only then activate the next Step 5 increment
```

A later increment must not treat unvalidated earlier Step 5 code as proven merely because it exists in the repository.

## Step 5 stop line

Step 5 closes only when the repository can behavior-validly acquire enough exact public upstream evidence for the S001 path to produce `AuthoritativeUpstreamIntervalEvidence` from live source identities.

Do not proceed during Step 5 into:

- semantic claim extraction/model integration;
- target Python comparison changes;
- CLI conditional orchestration;
- S001 full end-to-end product output;
- compatibility, safety, recommendation, or maintainer action.
