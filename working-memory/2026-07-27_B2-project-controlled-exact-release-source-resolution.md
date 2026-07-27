# B2 Project-Controlled Exact-Release Source Resolution

**Date:** 2026-07-27  
**Operation:** Select the smallest credible generalizable rule for resolving a project-controlled source that applies to an exact proposed Python package release  
**Starting revision:** `9c01c02f21828e2727e5ae53f5f7eb17fadefb37`  
**Investigation created:** `361ffcfd7a3b31b689cc93080e606a96b9eb5662`  
**Status:** Active; initial authority comparison recorded

## Objective

Design the upstream-source boundary required by the selected B2 package and upstream evidence plan.

The investigation must determine how UpgradePilot can move from validated PyPI package/version evidence and publisher-supplied project-link candidates to a separately validated source that:

- is associated with and controlled by the package's upstream project;
- applies to the exact proposed version;
- can be acquired through a bounded public read-only operation;
- preserves locator, retrieval or revision context, and explicit uncertainty;
- does not interpret release prose or make a compatibility, safety, or merge recommendation.

## Starting product boundary

Already behavior-validated:

```text
public PR identity
→ exact pinned dependency change
→ exact-head CI authority
→ exact PyPI package/version identity
→ publisher-supplied project-link candidates
```

Not yet established:

```text
project-controlled source
+ exact-release binding
+ bounded upstream content acquisition
```

## Exact design question

> What is the smallest credible and generalizable authority chain that lets UpgradePilot establish that an acquired public source is controlled by the project associated with a PyPI package and applies to the exact proposed version?

## Preliminary claim boundary

The resolver should establish only an acquisition and provenance claim of this form:

> A supported project-link candidate was bound to a project-controlled source, and the acquired source exposes a release record or version marker applying to the exact proposed version.

It must not establish:

- that the release is compatible with the target repository;
- that the release is safe;
- that release prose has a particular semantic meaning;
- that the dependency update should be merged, deferred, or blocked.

## Terms that must remain separate

### Discovery metadata

A `Project-URL` tells a consumer where the package publisher says a related resource is located. It is useful for discovering candidates.

### Project association

Project association answers whether the candidate repository or site is connected to the PyPI package. A publisher-supplied URL is an assertion of association, but stronger evidence may be available.

### Project control

Project control answers whether the source is operated through an identity belonging to the upstream project. It does not imply that the code or prose is safe or correct.

### Exact-release binding

Exact-release binding answers whether the acquired source applies to the proposed version rather than merely to the project generally.

### Semantic interpretation

Semantic interpretation transforms source prose into a structured meaning such as `drop_in_bug_fix_release`. This remains outside the current acquisition decision.

## Official-source findings

### PyPI JSON and Core Metadata

- The exact-release JSON route establishes one package/version record and returns metadata supplied at upload time.
- `Project-URL` labels are producer-supplied free text, but PEP 753 defines consumer-side normalization and well-known meanings.
- Well-known source labels include `source` with aliases `repository`, `sourcecode`, and `github`.
- Well-known release-material labels include `changelog`, `releasenotes`, `changes`, `whatsnew`, and `history`.
- Duplicate normalized labels are possible and must not be silently collapsed into one winner.

Therefore label normalization can identify candidate intent, but it cannot establish authority by itself.

### PyPI verified project URLs

PyPI can display project URLs as verified, including GitHub repository URLs associated with Trusted Publishing.

Important limitation from PyPI's own documentation:

- verification attests only that the URL was controlled by the PyPI package owner at upload time;
- verification is not repeated later;
- it does not establish safety or any broader relationship;
- current release JSON exposes project URLs but does not provide a stable per-entry verification contract suitable for this resolver.

Therefore the web page's verified presentation is useful evidence during investigation, but should not become the initial machine authority rule.

### PyPI provenance and attestations

PyPI's Integrity API can expose provenance for an exact distribution file. A PyPI Publish Attestation can identify the Trusted Publisher repository and workflow used to publish that file.

This creates a stronger possible binding:

```text
exact PyPI package/version/file
→ PyPI provenance identity
→ GitHub repository/workflow that published the file
```

The permitted claim must remain precise unless UpgradePilot performs independent cryptographic verification:

> PyPI reports that this exact distribution file was published through the stated Trusted Publisher repository identity.

It must not become:

> UpgradePilot independently proved the repository or package is trustworthy.

Absence of provenance must remain explicit because many valid public packages and older releases do not provide attestations.

### GitHub Releases and tags

GitHub provides structured public endpoints for:

- a published release selected by tag name;
- an exact Git tag reference;
- the commit or tag object identified by that reference.

A GitHub Release gives structured fields such as release ID, tag name, body, publication time, draft/prerelease state, and locator. A separate tag lookup can preserve the exact object SHA observed during acquisition.

GitHub Releases do not include ordinary tags that have no associated release. Therefore:

```text
Git tag exists
≠
GitHub Release exists
```

A release body is project-controlled release material, but it may be mutable and may omit claims published elsewhere. Retrieval time and tag/object identity must therefore be preserved.

## Control-case observations

The control case is `pytest==9.0.3`.

Observed without encoding these values as runtime behavior:

1. PyPI presents the pytest Source and Tracker links as verified, while Changelog and Homepage are unverified.
2. The Source candidate points to `pytest-dev/pytest`.
3. The GitHub repository exposes a published release tagged `9.0.3`.
4. The GitHub release body contains release-specific bug-fix entries.
5. At the exact `9.0.3` repository tag, `doc/en/announce/release-9.0.3.rst` exists and states that the release is a bug-fix release and a drop-in replacement.
6. The published GitHub release body does not expose that exact drop-in statement.

This establishes an important product lesson:

```text
authoritative exact-release source
≠
source containing every material upstream claim
```

A GitHub Release source can be valid and exact while the later structured claim still remains unresolved because the project published additional release material elsewhere.

## Strategy comparison

### Strategy A — Use a PyPI source/changelog URL directly

**Strengths**

- smallest number of requests;
- broad potential coverage;
- well-known labels provide deterministic candidate-intent normalization.

**Weaknesses**

- publisher-supplied association is not independent authority proof;
- URL verification is not available through the existing stable JSON contract;
- redirects and domain control can change;
- changelog HTML structure and exact-version sections vary;
- the pytest changelog section does not contain the material drop-in statement.

**Disposition:** reject as the sole initial authority rule.

### Strategy B — PyPI source candidate plus exact GitHub Release

**Strengths**

- structured and deterministic;
- exact tag selection;
- public read-only GitHub API;
- small implementation and test surface;
- strong project control once repository association is validated.

**Weaknesses**

- the source candidate remains only publisher asserted unless independently checked;
- many projects use tags without GitHub Releases;
- release bodies may omit separate announcements;
- exact tag naming varies.

**Disposition:** credible baseline only if repository association is strengthened and tag forms are tightly bounded.

### Strategy C — PyPI source candidate plus PyPI provenance agreement plus exact GitHub Release/tag

Proposed chain:

```text
exact PyPI package/version
→ well-known source candidate identifies one GitHub repository
→ exact PyPI distribution-file provenance reports a GitHub publisher repository
→ candidate repository and provenance repository agree
→ one accepted exact-version tag form resolves
→ a published GitHub Release and tag/ref are acquired
```

**Strengths**

- strongest package-to-repository binding among the compared bounded methods;
- exact package file, repository identity, release tag, and source content remain linked;
- structured JSON at each stage;
- deterministic mismatch and ambiguity handling;
- no need to trust an arbitrary documentation domain as the first format.

**Weaknesses**

- narrower coverage: requires usable PyPI provenance and a GitHub-hosted publisher;
- GitHub Releases are not used by every project;
- current `PackageReleaseEvidence` preserves only file count, not file records;
- the release body may not contain the control case's drop-in statement;
- claiming cryptographic verification would require a separately justified verification method or dependency.

**Disposition:** provisional recommendation for the first supported authority format, with an honest `unresolved_claim` when the release body lacks the later semantic evidence.

### Strategy D — Exact-tag repository release-document discovery

Example control-case source:

```text
doc/en/announce/release-9.0.3.rst @ tag 9.0.3
```

**Strengths**

- content is acquired at an exact repository revision;
- exposes the material pytest drop-in statement;
- avoids a mutable documentation `stable` URL.

**Weaknesses**

- projects organize release documents differently;
- discovering the file requires repository-tree search and path conventions;
- fixed path/token rules risk becoming heuristic or package-specific;
- recursive tree acquisition and ambiguity handling add scope.

**Disposition:** defer as a second supported source format unless the first format proves insufficient to satisfy the B2 stop line.

### Strategy E — Download and inspect the source distribution

**Strengths**

- exact PyPI artifact and hash binding;
- release documentation may be included in the sdist.

**Weaknesses**

- archive download, decompression, path traversal defense, file-count and size bounds;
- release-document discovery remains variable;
- significantly larger security and implementation surface.

**Disposition:** reject for the first source-resolution slice.

## Provisional recommended authority rule

The smallest strong initial source format is:

```text
attested GitHub-published PyPI release
+ matching well-known GitHub source candidate
+ exact GitHub Release/tag
```

Proposed supported domain:

- exact public Python package release exists on PyPI;
- metadata contains one unambiguous well-known source candidate identifying a public GitHub repository;
- one selected exact release distribution file has usable PyPI provenance identifying a GitHub Trusted Publisher repository;
- the candidate repository and provenance repository match exactly after URL canonicalization;
- exactly one accepted tag form has a published GitHub Release;
- the release tag/ref resolves and its object SHA is preserved.

Proposed initial tag forms:

```text
<exact-version>
v<exact-version>
```

The resolver must try both bounded forms and:

- accept exactly one successful match;
- return ambiguity if both resolve to different releases;
- avoid broader guessing, package-name prefixes, or arbitrary tag pattern search.

## Proposed evidence result

A successful result should preserve at least:

- requested package and exact version;
- selected distribution filename and SHA256;
- PyPI provenance locator and retrieval time;
- reported Trusted Publisher repository and workflow identity;
- matched PyPI source candidate label and URL;
- canonical GitHub repository identity;
- accepted tag form and exact tag/ref object SHA;
- GitHub Release ID, URL, publication time, draft/prerelease state, body, and retrieval time;
- explicit statement that release-body meaning has not been interpreted.

## Proposed failure and abstention states

- `source_candidate_missing` — no well-known source candidate exists;
- `source_candidate_ambiguous` — multiple distinct supported repository candidates remain;
- `provenance_unavailable` — the selected exact distribution file has no accessible provenance;
- `provenance_unsupported` — provenance exists but the publisher identity is outside the initial GitHub format;
- `project_identity_mismatch` — source candidate and provenance repository disagree;
- `release_source_unavailable` — repository identity is established but no accepted exact-version release/tag source is acquired;
- `release_source_ambiguous` — more than one accepted tag form resolves inconsistently;
- `source_redirected` — a redirect occurred and canonical identity has not been independently reconciled;
- `malformed_response` — a successful response violates the expected contract;
- `acquisition_failed` — transport or unusable HTTP failure;
- `unresolved_claim` — trustworthy exact-release content exists, but the later required meaning is not established.

Names may be refined to align with the controlling plan before implementation.

## Architecture implications

Likely focused responsibilities, subject to approval:

```text
pypi_client.py          preserve exact distribution-file records
PyPI provenance client acquire bounded Integrity API evidence
GitHub release client  acquire exact release and tag/ref identity
upstream resolver      reconcile candidate, provenance, repository, and version
```

No universal source framework is justified.

The PyPI Integrity API would create a second PyPI JSON consumer with the same bounded-body and response-closing mechanics as the existing release client. During implementation design, determine whether to extract only those identical PyPI mechanics rather than duplicating them or creating a universal HTTP client.

## Proposed proof

Controlled tests should cover:

1. one well-known GitHub source candidate plus matching provenance and exact-version release success;
2. `v`-prefixed tag success;
3. duplicate normalized source labels resolving to the same repository;
4. distinct repository candidates remaining ambiguous;
5. missing provenance;
6. unsupported non-GitHub provenance identity;
7. candidate/provenance repository mismatch;
8. tag exists but no GitHub Release;
9. neither accepted tag form exists;
10. both accepted tag forms resolving inconsistently;
11. redirected repository or release endpoint remains explicit;
12. malformed provenance or release response;
13. no package-specific name, version, path, wording, or answer;
14. successful acquisition does not produce a compatibility, safety, or merge recommendation.

One live read-only proof should use the control case only after the runtime rule is demonstrably package-independent.

## Official references consulted

- https://docs.pypi.org/api/json/
- https://docs.pypi.org/project_metadata/
- https://docs.pypi.org/api/integrity/
- https://docs.pypi.org/attestations/
- https://docs.pypi.org/attestations/consuming-attestations/
- https://docs.pypi.org/attestations/security-model/
- https://packaging.python.org/en/latest/specifications/core-metadata/
- https://packaging.python.org/en/latest/specifications/well-known-project-urls/
- https://peps.python.org/pep-0753/
- https://docs.github.com/en/rest/releases/releases
- https://docs.github.com/en/rest/git/refs
- https://docs.github.com/en/rest/git/tags

## Learning-by-building contract

During this investigation:

- explain the difference between discovery metadata, project association, source control, exact-version binding, and semantic interpretation;
- connect each proposed rule to concrete current source objects and future code responsibilities;
- expose assumptions and rejected alternatives rather than presenting only the final choice;
- keep the investigation bounded so architectural learning does not stall B2 momentum;
- do not create code until the authority rule is understood and approved.

## Non-goals

This investigation does not yet:

- implement the upstream resolver;
- integrate PyPI into the CLI;
- interpret release-note prose;
- produce a final maintainer recommendation;
- create a universal source framework, adapter registry, plugin system, or new runtime dependency;
- reorganize the package into subpackages.

## Current classification

**Active; provisional recommendation available.** The attested GitHub Release/tag chain is the strongest bounded first format found so far, but it requires Ali's review before the design is accepted or implemented.
