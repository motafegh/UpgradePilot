# B2 Step 5B — Git Tag to Commit Implementation

**Date:** 2026-08-02  
**Parent plan:** [`../plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`](../plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md)  
**Live-state owner:** [`../MEMORY.md`](../MEMORY.md)

## Purpose

Implement only Step 5B:

```text
trusted GitHub repository
+ explicitly supplied accepted version tag
→ exact refs/tags/<tag> identity
→ bounded annotated-tag peeling when required
→ immutable commit SHA
```

This increment does not acquire a changelog file, assemble Step 1 interval authority, extract semantic claims, change target relevance, or modify CLI orchestration.

## Product/test boundary

The Step 5B source/test implementation boundary is:

```text
783a22c790b0c45487acf3b4d3a4698ba7484a82
```

Later working-memory and live-state commits do not alter this executable boundary.

## Source added

```text
src/upgradepilot/github_tag.py
```

Public contracts:

```text
GitHubTagCommitClient
GitHubTagCommitEvidence
GitHubTagCommitProblem
GitHubTagCommitResult
```

Primary operation:

```text
GitHubTagCommitClient.resolve_tag_to_commit(repository, requested_tag)
```

## Git model represented

```text
Git tag reference
refs/tags/vX.Y.Z
        │
        ├── points to commit
        │   → lightweight tag
        │   → resolved immediately
        │
        └── points to tag object
            → annotated tag
            → fetch exact tag object by SHA
            → follow object target
            → repeat only while target type == tag
            → stop at commit
```

The result preserves:

```text
repository
requested_tag
tag_ref
tag_object_type
tag_object_sha
resolved_commit_sha
peeled_tag_object_shas[]
retrieved_at
```

`tag_object_type` and `tag_object_sha` describe the object directly named by the tag reference. `resolved_commit_sha` is the immutable commit reached after any required peeling. `peeled_tag_object_shas` preserves the annotated tag-object chain rather than hiding the traversal.

## Bounded failure rules

Explicit problem states are:

```text
source_unavailable
identity_mismatch
malformed_response
unsupported_object_type
peel_cycle
peel_depth_exceeded
acquisition_failed
```

The default maximum annotated-tag peel depth is eight tag objects. The client detects repeated object SHAs before another request, so a cyclic object graph cannot loop indefinitely.

The caller supplies the tag exactly. The component does not search release titles or invent `v` prefixes.

## Shared tag-reference rule

`GitHubReleaseClient` previously contained its own exact tag-reference parser. Step 5B moved that pure parsing rule into `github_tag.py` as the shared internal `parse_exact_tag_reference` function, and `GitHubReleaseClient` now reuses it.

This preserves the narrower release-client behavior—it still binds a release to the direct Git object named by the tag reference and does not perform commit peeling—while preventing two implementations of exact ref/object identity.

## Controlled tests

Added:

```text
tests/test_github_tag.py
```

Coverage includes:

- lightweight tag → commit;
- one annotated tag object → commit;
- nested annotated tags → commit;
- exact returned ref mismatch;
- missing tag reference;
- unsupported direct Git object type;
- annotated tag object SHA mismatch;
- object cycle;
- maximum peel-depth enforcement;
- malformed annotated tag response;
- timeout/acquisition failure;
- strict public input and configured-bound validation.

The package-interface test also exposes only the intended Step 5B contracts.

## Validation status

Implementation and controlled tests are complete, but no local test pass is claimed in this record.

Validation must occur from the real checkout before Step 5C changelog-file acquisition begins.
