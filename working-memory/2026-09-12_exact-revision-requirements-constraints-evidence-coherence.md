# Exact-Revision Requirements/Constraints Evidence Coherence — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-12_ci-static-runtime-correlation-bridge.md`](2026-09-12_ci-static-runtime-correlation-bridge.md)

## Why this responsibility is selected

The preceding E inventory separated confirmed correctness/provenance defects from evidence bottlenecks, deliberate conservative limits, and future product gaps.

The first selected repair is the requirements/constraints patch-to-frozen-revision coherence defect because it can create **misattributed source evidence before all later exact-head reasoning**:

```text
PR identity freezes head A
+
changed-file patch is later acquired from the mutable PR files endpoint
+
PR advances to head B while changed-file count remains the same
→ B patch content can be interpreted while the dependency source context is attributed to A
```

This is more foundational than broadening correlation/Target/runtime evidence because stronger downstream evidence cannot repair a dependency transition whose snapshot identity is wrong.

The second confirmed correctness responsibility remains the static shell/direct-install false-positive defect. It is intentionally retained as the next correctness reinforcement candidate after this cycle closes; no implementation for it begins inside this record.

## Current source path to understand in A

The current normal path is:

```text
GitHubPullRequestClient.get_pull_request(...)
→ PullRequestIdentity(base_sha, head_sha, changed_files, ...)

GitHubPullRequestClient.get_changed_files(identity)
→ GET /repos/{repository}/pulls/{number}/files
→ ChangedFile(..., patch=...)

analyze_dependency_change(identity, changed_files, repository_client)
→ requirements/constraints path consumes ChangedFile.patch directly
→ extract_exact_requirement_changes(...)
→ dependency/source context later receives identity.head_sha
```

By contrast, admitted `uv.lock` and pyproject optional-extra paths acquire exact base/head repository files through `GitHubRepositoryClient` before extracting the dependency transition.

Therefore the defect is **not** that UpgradePilot fails to acquire base/head SHAs or never uses immutable revisions. The defect is narrower: the requirements/constraints patch evidence itself is not proven to correspond to those frozen SHAs.

## A — pre-implementation investigation/design — CURRENT

A must select the smallest sound producer-level invariant:

> Every admitted requirements/constraints dependency transition used downstream is demonstrably derived from the investigation's frozen base/head snapshot.

### Questions to resolve before Build

1. What exact GitHub evidence source can prove the requirements/constraints transition at the frozen base/head revisions?
2. Should the existing changed-file patch remain only discovery/completeness metadata, or can it be retained in the trusted extraction path with an enforceable correspondence proof?
3. Is exact base/head repository-file acquisition and comparison the simplest adequate mechanism, or would an exact commit-comparison source preserve the existing patch-oriented extractor more cleanly?
4. Which owner should establish snapshot correspondence earliest so downstream dependency analysis never needs to reconstruct provenance?
5. What minimum type/provenance changes, if any, are actually necessary? Do not add fields merely because they are convenient for tests.
6. How do we preserve the current bounded requirements/constraints syntax and incomplete-patch protections without conflating them with snapshot coherence?

### Candidate mechanisms — not yet selected

A should compare at least the credible smallest approaches:

```text
A. exact frozen base/head file reads
   → derive the dependency transition from immutable file contents

B. exact base→head commit comparison / exact diff evidence
   → retain a patch/diff-oriented extraction contract while binding it to frozen SHAs

C. mutable PR-files request + revalidation
   → only acceptable if the normal provider can actually prove the returned patch still belongs to the frozen identity
```

Do not choose by implementation convenience alone. Evaluate correctness/proof fit, ownership, complexity, migration pressure, generality, and failure behavior.

## Expected owners/evidence

Primary source owners:

- `src/upgradepilot/github/pull_request.py`
- `src/upgradepilot/github/repository.py`
- `src/upgradepilot/dependency/analysis.py`
- `src/upgradepilot/dependency/requirements.py`

Focused proof likely spans:

- PR/provider acquisition tests;
- exact requirement/constraint extraction tests;
- dependency-analysis integration tests;
- application/investigation tests proving the normal path cannot mix head B evidence into head A identity.

Consult the Core trust/provenance invariants and the separate system-limitations/correctness record where the earlier controlled race was preserved. Do not infer the repair mechanism from that historical reproducer.

## Required Build proof once A selects the mechanism

The future B slice must discriminate at least:

```text
STABLE SNAPSHOT
base/head remain unchanged
→ supported exact requirements transition is still established

HEAD ADVANCES
identity captures head A
PR later advances to head B
→ B dependency content cannot be accepted as evidence for A

SAME FILE COUNT RACE
A and B expose the same number of changed files
→ count equality cannot bypass the protection

STRUCTURED EXACT-FILE PATHS
uv.lock / admitted pyproject exact base/head acquisition
→ remain correct and unregressed

UNSUPPORTED / AMBIGUOUS REQUIREMENTS INPUT
→ remains explicit problem/unresolved behavior rather than guessing
```

Focused proof must establish normal producer behavior, not only manually constructed trusted objects.

## Stop line

This cycle owns only requirements/constraints snapshot/provenance coherence.

Do not in this cycle:

- repair shell/direct-install parsing;
- add matrix/reusable workflow correlation;
- parse job logs or artifacts;
- prove exact installed dependency version/wheel;
- redesign Target artifact-environment composition;
- enable targeted checks or another non-abstention maintainer action;
- redesign CLI/reporting;
- introduce generic repository snapshot infrastructure unless the smallest sound repair actually requires a shared provider primitive.

## Current Learning-by-Doing state

```text
Slice: exact-revision requirements/constraints evidence coherence

A — CURRENT
    investigate/compare the smallest sound snapshot-binding mechanism
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

No product source/test mutation has been authorized or performed by opening this record.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
