# B2 Project-Controlled Exact-Release Source Resolution

**Date:** 2026-07-27  
**Operation:** Select and implement the smallest credible generalizable rule for resolving a project-controlled source that applies to an exact proposed Python package release  
**Starting revision:** `9c01c02f21828e2727e5ae53f5f7eb17fadefb37`  
**Investigation created:** `361ffcfd7a3b31b689cc93080e606a96b9eb5662`  
**Design accepted by Ali:** stronger but narrower provenance-backed GitHub Release/tag chain  
**Latest source/test implementation:** `bf4ede1d6e902b22fda384d6d43339efe46bab8f`  
**Status:** Implemented; complete repository and live validation pending

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

A PyPI `Project-URL` tells a consumer where the package publisher says a related resource is located. It identifies a candidate; it does not independently prove authority.

### Project association

Project association asks whether a repository is connected to the package. The accepted rule requires agreement between a PyPI Source candidate and PyPI-reported exact-file provenance.

### Project control

Project control asks whether the source is operated through the reported upstream publisher identity. The current implementation records what PyPI reports; it does not claim independent cryptographic verification of the attestation envelope.

### Exact-release binding

Exact-release binding requires one accepted version tag form, a published GitHub Release selected by that tag, and the exact Git tag-reference object SHA.

### Semantic interpretation

Semantic interpretation would transform release prose into a structured meaning such as `drop_in_bug_fix_release`. It remains outside this implementation.

## Compared strategies

### Direct PyPI Source or Changelog URL

Rejected as the sole authority rule. It has broad coverage but relies on publisher-supplied association, variable redirects and document structures, and weak exact-version binding.

### PyPI Source candidate plus GitHub Release

Credible but insufficiently independent because the repository relationship still rests on one metadata URL.

### PyPI Source candidate plus PyPI provenance plus exact GitHub Release/tag

Accepted as the strongest bounded first format. It is narrower because it requires usable PyPI provenance, a GitHub publisher, and a GitHub Release, but it keeps package file, publisher repository, release tag, and source content linked.

### Exact-tag repository release-document discovery

Deferred. It can expose project material omitted from the GitHub Release body but requires tree acquisition, document-path discovery, ambiguity rules, and more heuristic pressure.

### Source-distribution inspection

Rejected for the first slice because archive download, decompression, traversal defense, file-count and size limits, and document discovery materially enlarge the security and implementation surface.

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

It does not permit:

- UpgradePilot independently verified the attestation cryptography;
- every distribution file has provenance;
- the release is compatible or safe for the target repository;
- the release body contains every material upstream statement;
- the dependency update should be merged, deferred, or blocked.

## Partial provenance rule

A Python release may contain several distribution files. The implementation:

- queries provenance for every exact file;
- permits files with explicit `provenance_unavailable` when at least one usable exact-file record exists;
- requires all usable GitHub publisher identities to agree;
- rejects multiple GitHub repositories as ambiguous;
- rejects mixed GitHub and non-GitHub publisher kinds as ambiguous;
- returns unsupported when available provenance contains no supported GitHub publisher.

This avoids selecting one favored wheel or source distribution by filename convention.

## Source and responsibility changes

### `src/upgradepilot/pypi_api.py`

Added a small shared PyPI JSON acquisition boundary for behavior now proven identical across two consumers:

- timeout handling;
- streamed response-size limits;
- response closing;
- JSON decoding;
- top-level object validation;
- source-specific request and response exceptions.

It does not own endpoint status meaning or evidence types.

### `src/upgradepilot/pypi_client.py`

Extended exact-release evidence to preserve immutable `DistributionFile` records:

- filename;
- download URL;
- package type;
- SHA-256 digest.

The previous `distribution_file_count` interface remains as a computed property.

### `src/upgradepilot/pypi_provenance.py`

Added exact-file PyPI Integrity API acquisition with:

- version-one media type;
- exact package/version/filename locator;
- PyPI-reported publisher kind;
- GitHub repository and workflow identity when applicable;
- attestation count;
- explicit unavailable, unsupported, malformed, and acquisition-failed states.

Valid non-GitHub publisher records are preserved as valid provenance instead of being mislabeled malformed. The upstream resolver decides that they are outside the first supported source format.

### `src/upgradepilot/github_release.py`

Added bounded acquisition of:

- a published GitHub Release selected by exact tag;
- release ID, locator, name, body, publication time, and prerelease state;
- exact `refs/tags/<tag>` identity;
- referenced object type and SHA.

The release body has a configurable character limit. Missing required release or tag fields become `malformed_response`, not uncaught `KeyError`.

### `src/upgradepilot/upstream_source.py`

Added deterministic reconciliation of:

- PEP 753-style project URL label normalization;
- canonical public `https://github.com/<owner>/<repository>` Source candidates;
- all exact-file provenance outcomes;
- publisher kind and repository consistency;
- candidate/provenance repository agreement;
- exact and `v`-prefixed tag forms;
- published release and exact tag-ref evidence.

A successful result carries `claim_state="unresolved_claim"` because release prose has not been interpreted.

### `src/upgradepilot/__init__.py`

Exported the new evidence, problem, client, and resolver contracts without introducing network work at import time.

## Evidence states

The implemented resolver returns:

- `available` with `unresolved_claim` — authority and exact-release source resolved, meaning not interpreted;
- `source_unavailable` — no usable provenance or no accepted published release;
- `unsupported_source` — candidate host, publisher kind, provenance version, or source format is outside the first boundary;
- `identity_mismatch` — independently acquired identities contradict each other;
- `ambiguous_source` — several repositories, publisher kinds, or accepted tag forms remain plausible;
- `malformed_response` — successful external data violates the required contract;
- `acquisition_failed` — transport or unusable HTTP failure.

## Security and trust boundaries

- All network operations are read-only.
- Canonical Source URLs require HTTPS, `github.com`, exactly owner/repository path components, and no credentials, port, query, or fragment.
- Distribution SHA-256 values are validated and preserved, but package files are not downloaded in this slice.
- Attestation envelopes are not independently cryptographically verified.
- Release bodies are bounded before later consumers receive them.
- Redirect-based repository identity is not inferred.
- No target repository is mutated.

## Tests added or changed

### Existing PyPI release tests

Now verify exact file identity, SHA-256 validation, and backward-compatible file counts.

### `tests/test_pypi_provenance.py`

Covers:

- exact-file provenance success;
- correct Integrity media type;
- `404` provenance absence;
- unsupported API version;
- malformed empty bundle;
- valid non-GitHub publisher shape;
- malformed GitHub publisher missing repository identity.

### `tests/test_github_release.py`

Covers:

- published release plus exact tag-ref success;
- release absence;
- returned tag mismatch;
- release-body limit;
- missing release fields;
- missing tag-object fields.

### `tests/test_upstream_source.py`

Covers:

- matching end-to-end authority chain;
- partial provenance availability;
- candidate/provenance mismatch;
- multiple Source repositories;
- unsupported non-GitHub Source host;
- both accepted tag forms resolving;
- PEP 753 label normalization.

## Implementation commits

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

## Validation evidence available now

A reconstructed focused source environment was used to compile the changed modules and run 20 controlled tests. They passed.

This is implementation-adjacent evidence only. It is not the complete active repository suite and is not live-network proof.

## Validation still required in Ali's environment

```bash
source .venv/bin/activate
git pull origin main
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

Expected count if no unrelated tests change: **60 tests**.

Then run one live read-only control case through the new public Python contracts. A successful result is expected to establish upstream source evidence or return an accurately classified unsupported/unavailable state; the live outcome must be observed rather than assumed.

## Deferred work

- CLI integration;
- independent cryptographic attestation verification;
- exact-tag release-document discovery;
- semantic release-note interpretation;
- compatibility or safety analysis;
- final maintainer recommendation;
- wider B3 source robustness.

## Official references consulted

- PyPI JSON API documentation;
- PyPI Integrity API documentation;
- PyPI attestation and security-model documentation;
- Core Metadata and PEP 753 well-known project URL rules;
- GitHub REST release-by-tag and Git-reference documentation.

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

## Current classification

**Implemented, not yet behavior-validated in Ali's complete repository and live environment.**

The next action is validation only. Do not integrate the resolver into the CLI or begin semantic interpretation until the complete suite and live source-resolution smoke check have been reviewed.
