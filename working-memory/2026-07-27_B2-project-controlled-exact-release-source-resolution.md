# B2 Project-Controlled Exact-Release Source Resolution

**Date:** 2026-07-27  
**Operation:** Select, implement, and validate the smallest credible generalizable rule for resolving a project-controlled source that applies to an exact proposed Python package release  
**Starting revision:** `9c01c02f21828e2727e5ae53f5f7eb17fadefb37`  
**Investigation created:** `361ffcfd7a3b31b689cc93080e606a96b9eb5662`  
**Design accepted by Ali:** stronger but narrower provenance-backed GitHub Release/tag chain  
**Latest source/test implementation:** `bf4ede1d6e902b22fda384d6d43339efe46bab8f`  
**Status:** Completed and behavior-validated

## Objective

Move from validated PyPI package/version identity and publisher-supplied project-link candidates to a separately validated source that:

- is associated with the package through independent evidence rather than one link alone;
- is controlled through the reported upstream publisher identity;
- applies to the exact proposed version;
- is acquired through bounded public read-only operations;
- preserves locators, file digests, publisher identity, release identity, tag-ref identity, and retrieval context;
- does not interpret release prose or make compatibility, safety, or merge recommendations.

## Terms kept separate

### Discovery metadata

A PyPI `Project-URL` identifies a candidate. It does not independently prove authority.

### Project association

The accepted rule requires agreement between a well-known PyPI Source candidate and PyPI-reported exact-file provenance.

### Project control

The implementation records the publisher repository identity reported by PyPI. It does not claim independent cryptographic verification of the attestation envelope.

### Exact-release binding

The implementation requires one accepted version tag form, a published GitHub Release selected by that tag, and the exact Git tag-reference object SHA.

### Semantic interpretation

Release prose remains uninterpreted. Successful source acquisition returns `claim_state="unresolved_claim"`.

## Compared strategies

### Direct PyPI Source or Changelog URL

Rejected as the sole authority rule because it provides only publisher-supplied association, variable redirects and document structures, and weak exact-version binding.

### PyPI Source candidate plus GitHub Release

Credible but insufficiently independent because the repository relationship still rests on one metadata URL.

### PyPI Source candidate plus PyPI provenance plus exact GitHub Release/tag

Accepted as the strongest bounded first format. It is narrower because it requires usable PyPI provenance, a GitHub publisher, and a GitHub Release, but it keeps package file, publisher repository, release tag, and source content linked.

### Exact-tag repository release-document discovery

Deferred. It can expose project material omitted from a GitHub Release body but requires repository-tree acquisition, document-path discovery, and larger ambiguity and security rules.

### Source-distribution inspection

Rejected for this slice because archive download, decompression, path-traversal defense, file-count and size limits, and release-document discovery materially enlarge the surface.

## Accepted authority chain

```text
exact PyPI package/version
→ immutable distribution-file records
→ per-file PyPI Integrity provenance
→ one unambiguous PyPI-reported GitHub publisher repository
→ one unambiguous well-known PyPI Source candidate
→ Source candidate and provenance repository agree
→ exactly one accepted tag form resolves
→ published GitHub Release
→ exact Git tag reference and object SHA
→ bounded release body
→ semantic claim remains unresolved
```

Accepted initial tag forms:

```text
<exact-version>
v<exact-version>
```

The resolver accepts exactly one success. It does not search arbitrary tags or add package-name prefixes.

## Permitted claim

A successful result permits this bounded claim:

> PyPI reports usable provenance for at least one exact distribution file identifying a GitHub publisher repository; that repository agrees with the package's well-known GitHub Source candidate; and one accepted exact-version tag resolves to a published GitHub Release and exact tag-reference object.

It does not permit claims that:

- UpgradePilot independently verified attestation cryptography;
- every distribution file necessarily has provenance;
- the release is compatible or safe for the target repository;
- the release body contains every material upstream statement;
- the dependency update should be merged, deferred, or blocked.

## Partial provenance rule

The resolver:

- queries provenance for every exact distribution file;
- permits explicit `provenance_unavailable` files when at least one usable exact-file record exists;
- requires all usable GitHub publisher identities to agree;
- rejects multiple GitHub repositories as ambiguous;
- rejects mixed GitHub and non-GitHub publisher kinds as ambiguous;
- returns unsupported when available provenance contains no supported GitHub publisher.

This avoids selecting a favored wheel or source distribution through filename heuristics.

## Implemented responsibilities

### `src/upgradepilot/pypi_api.py`

Shared only the PyPI mechanics proven identical across release and provenance clients:

- timeout handling;
- streamed response-size limits;
- response closing;
- JSON decoding and top-level object validation;
- PyPI-specific request and response exceptions.

It does not own endpoint status meaning or evidence types.

### `src/upgradepilot/pypi_client.py`

Extended exact-release evidence with immutable `DistributionFile` records containing filename, URL, package type, and SHA-256 digest. The previous `distribution_file_count` remains as a computed property.

### `src/upgradepilot/pypi_provenance.py`

Added exact-file PyPI Integrity acquisition with explicit available, unavailable, unsupported, malformed, and acquisition-failed results. Valid non-GitHub publisher records remain valid evidence and are classified as unsupported by the GitHub-only resolver.

### `src/upgradepilot/github_release.py`

Added bounded acquisition of a published GitHub Release selected by exact tag plus exact `refs/tags/<tag>` object type and SHA. Missing required fields become `malformed_response`; release body length is bounded.

### `src/upgradepilot/upstream_source.py`

Added deterministic reconciliation of Source-label normalization, canonical public GitHub repository URLs, all exact-file provenance outcomes, publisher consistency, Source/provenance agreement, accepted tag forms, and exact release/tag-ref evidence.

### `src/upgradepilot/__init__.py`

Exported the new public evidence, problem, client, and resolver contracts without performing network work at import time.

## Evidence states

The resolver returns:

- `available` with `unresolved_claim` — exact upstream authority resolved, meaning not interpreted;
- `source_unavailable` — no usable provenance or no accepted published release;
- `unsupported_source` — source host, publisher kind, provenance version, or source format is outside the initial boundary;
- `identity_mismatch` — independently acquired identities contradict each other;
- `ambiguous_source` — several repositories, publisher kinds, or accepted tag forms remain plausible;
- `malformed_response` — successful external data violates the required contract;
- `acquisition_failed` — transport or unusable HTTP failure.

## Security and trust boundaries

- All network operations are read-only.
- Canonical Source URLs require HTTPS, `github.com`, exactly owner/repository path components, and no credentials, port, query, or fragment.
- Distribution SHA-256 values are validated and preserved, but package files are not downloaded.
- Attestation envelopes are not independently cryptographically verified.
- Release bodies are bounded before later consumers receive them.
- Redirect-based repository identity is not inferred.
- No target repository is mutated.

## Tests

The complete active test suite covers package-file identity, PyPI provenance states and publisher shapes, GitHub release/tag-ref acquisition, missing and malformed fields, Source-label normalization, repository mismatch, partial provenance, unsupported hosts and publishers, and ambiguous tag forms.

Implementation commits:

```text
870acdaf2b2e37ea154181f2fd2ac78abf46661b  Add shared bounded PyPI JSON acquisition
242e9a3c00040e5587bb522e8ee858a0a4bb5b65  Preserve exact PyPI distribution file identities
e3004569cf36b7c7b3a30ff5304ddc4c1cfa9df7  Add exact-file PyPI provenance acquisition
04f1e311c0395a344fd9b18c7797766763b420dc  Add exact GitHub release and tag acquisition
975213d91b6517b626cd50548f60d4a2b310b464  Resolve project-controlled exact GitHub releases
128e099a9966ee944d0cba18b689068e8653d7e7  Test exact PyPI distribution file records
3a3d1b2c7dcabecc22e3bcde36ea7d87e10bd1e2  Test exact-file PyPI provenance states
b8f6a623e967d58a4b2870455fa8f82b3733e8af  Test exact GitHub release and tag evidence
537d3fb0936f62a8e28868800bfd176f6d53202c  Test upstream source authority reconciliation
da2ee44fd5aa11bab33123f0f9862a3554cf1277  Export upstream source evidence contracts
7f20cfb77d5219278fe1efd0fdb00f175c1cb6f8  Classify missing GitHub release fields
c37c2c7a42512c1db9462af356544f4597f903c2  Preserve non-GitHub PyPI publisher identities
5eda5886d272fe129825b9e282829a7a9df97e37  Guard optional provenance repository identities
b1dc799991dce7a9c3f79a4cac5a2aab930aabee  Test malformed GitHub release field handling
bf4ede1d6e902b22fda384d6d43339efe46bab8f  Test valid unsupported PyPI publisher shapes
```

## Validation evidence

Observed in Ali's WSL2 Python 3.12 environment:

```text
editable installation succeeded
60 active repository tests passed in 0.012 seconds
live package result: PackageReleaseEvidence / available
requested and published identity: pytest==9.0.3
distribution files: wheel and sdist with exact SHA-256 values
live upstream result: UpstreamReleaseEvidence / available
repository: pytest-dev/pytest
claim state: unresolved_claim
both exact files: one GitHub attestation each
both publishers: pytest-dev/pytest via deploy.yml
provenance unavailable files: none
accepted tag: 9.0.3
release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
tag ref: refs/tags/9.0.3
tag object type: tag
tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
published at: 2026-04-07T17:16:45Z
prerelease: false
bounded release body acquired: 2136 characters
```

## What the live proof establishes

The control case validated the complete accepted authority chain:

```text
pytest==9.0.3 exact PyPI release
→ two exact distribution files
→ provenance for both files
→ one matching GitHub publisher repository
→ one matching Source candidate
→ exactly one accepted tag form
→ published GitHub Release
→ exact annotated tag object SHA
```

It does not establish the semantic meaning of the release body. `unresolved_claim` is the correct successful boundary, not a validation failure.

## Deferred work

- CLI integration;
- independent cryptographic attestation verification;
- exact-tag release-document discovery;
- semantic release-note interpretation;
- compatibility or safety analysis;
- final maintainer recommendation;
- wider B3 source robustness.

## Learning result

```text
same project name
≠ independent project association

valid provenance
≠ supported publisher kind

exact tag identity
≠ semantic release meaning

PyPI-reported attestation identity
≠ independent cryptographic verification
```

## Final classification

**Completed and behavior-validated.**

The next product action is bounded CLI integration of the already validated package and upstream evidence. That integration must expose evidence and explicit problem states only; it must not interpret release prose or produce compatibility, safety, or merge recommendations.