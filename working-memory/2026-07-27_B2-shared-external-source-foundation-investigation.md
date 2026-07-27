# B2 Shared External-Source Foundation Investigation

**Date:** 2026-07-27  
**Operation:** Audit and remove proven external-source validation duplication before adding another source  
**Starting revision:** `4520f981d7c7e0ab9f716daab0773643405e1338`  
**Implemented revision:** `98a4914ce70b1cfe8d5ddd612185cb527d52a02c`  
**Behavior-validated repository revision:** `64b08fa93c16baa6f9557ba0f6b44ea97dff3098`  
**Status:** Completed and behavior-validated

## Objective

Determine whether UpgradePilot had enough repeated external-source behavior to justify a small shared foundation before implementing the project-controlled upstream-source resolver.

The goal was not to generalize every client. It was to remove proven repetition while preserving source-specific authority, identity, failure, and evidence semantics.

## Why the investigation was justified

UpgradePilot had:

- a shared GitHub REST/JSON foundation used by multiple GitHub clients;
- a separate PyPI exact-release client with its own JSON value checks;
- an upcoming upstream-source resolver likely to introduce another acquisition boundary.

One GitHub implementation alone did not justify a source-neutral abstraction. Two implemented boundaries plus a credible third created a concrete duplication risk.

## Findings

### Proven repeated mechanics

GitHub and PyPI both required runtime checks for:

- JSON objects and arrays;
- non-empty strings;
- optional non-empty strings;
- integers while rejecting booleans;
- positive and non-negative integer ranges;
- actual boolean values.

These checks have identical meaning before any source-specific error or evidence classification is applied.

### Similar-looking behavior that remains source-specific

The HTTP and evidence layers are not equivalent:

- GitHub uses authentication and API-version headers; PyPI does not;
- GitHub raises `GitHubAcquisitionError` and `GitHubResponseError`; PyPI returns `PackageReleaseProblem` values;
- GitHub and PyPI assign different meanings to HTTP status codes;
- PyPI performs a second package lookup after a release `404`;
- PyPI streams and caps response bodies while GitHub retains its existing JSON boundary;
- a future upstream source may be HTML, Markdown, raw text, repository content, or structured API data.

A universal external-source HTTP client was therefore rejected as premature and likely to erase useful semantics.

## Compared options

### Keep every source completely separate

Rejected as the default path because JSON value-contract duplication was already proven and a third copy was likely.

### Extract only source-neutral JSON value contracts

Accepted. This removes exact duplication while focused clients preserve field policy, errors, evidence states, identity, and authority.

### Introduce a general external-source acquisition client

Rejected for now. It would require configuration or callbacks for materially different transport and evidence contracts before the next source format is selected.

## Approved boundary

Ali approved this design:

```text
source-neutral JSON value contracts
├── GitHub adapters preserve GitHub exceptions and messages
├── PyPI adapters preserve malformed-response classification
└── future structured sources may reuse identical value rules
```

The shared layer does not own:

- HTTP requests, headers, authentication, or status-code meaning;
- required-field presence policy;
- package, repository, PR, workflow, release, or upstream identity;
- provenance records;
- source authority;
- public evidence, problem, or exception types.

## Implementation

### Shared source-neutral module

Added `src/upgradepilot/json_contract.py` with:

- `JsonContractViolation`;
- `expect_mapping`;
- `expect_list`;
- `expect_nonempty_text`;
- `expect_optional_nonempty_text`;
- `expect_integer`;
- `expect_positive_integer`;
- `expect_nonnegative_integer`;
- `expect_boolean`.

The functions validate values only. They do not fetch fields or name any external source.

### GitHub compatibility adapter

Updated `src/upgradepilot/github_api.py` so existing `required_*` helpers delegate to the neutral contracts while preserving:

- existing helper names and imports used by focused GitHub clients;
- `KeyError` behavior for missing required fields;
- GitHub-specific exception types and messages;
- layered integer behavior, where a wrong type remains distinct from a wrong numeric range;
- existing HTTP, authentication, status, and JSON-decoding behavior.

### PyPI compatibility adapter

Updated `src/upgradepilot/pypi_client.py` so PyPI structural checks delegate to the neutral contracts while preserving:

- `_MalformedResponse` translation;
- `PackageReleaseProblem(state="malformed_response")` behavior;
- release-versus-package `404` classification;
- exact package/version identity checks;
- streamed body limits and response closing;
- publisher-supplied project-link candidate behavior.

### Tests added

Added:

- `tests/test_json_contract.py` — direct success and rejection tests for neutral contracts;
- `tests/test_external_contract_adapters.py` — GitHub message-layer preservation and PyPI malformed-response translation.

Existing GitHub and PyPI tests supplied the broader regression proof.

## Implementation commits

```text
14793050bec6f0fd14e6503acca9b0360daf064c  Add source-neutral JSON value contracts
d629e964e5d388b8bb16df83ce9afeaa76c2c7fd  Test source-neutral JSON value contracts
0f856040b3a121663e7f7ae9eb37697b42da460a  Delegate GitHub JSON checks to shared contracts
7112343d8d375aefa6310fb6112cef809b396eca  Delegate PyPI JSON checks to shared contracts
9031021611d439fad449c259f51c91e965f85255  Preserve layered GitHub integer errors
98a4914ce70b1cfe8d5ddd612185cb527d52a02c  Protect source-specific contract translations
```

## Validation evidence

Observed in Ali's WSL2 Python 3.12 virtual environment after pulling repository revision `64b08fa93c16baa6f9557ba0f6b44ea97dff3098`.

### Installation and deterministic suite

```text
editable installation succeeded
41 active repository tests ran
41 tests passed
runtime: 0.008 seconds
```

This covered the new neutral contracts, both source-specific adapters, and all existing GitHub, dependency, CI-authority, workflow-command, and PyPI behavior.

### Live PyPI regression proof

An unmocked request for `pytest==9.0.3` returned:

```text
result type: PackageReleaseEvidence
state: available
requested: pytest==9.0.3
published: pytest==9.0.3
distribution files: 2
```

This established that the refactored PyPI adapter still converts the real PyPI response into the expected exact-release evidence.

### Live GitHub regression proof and credential diagnosis

The first live CLI attempt returned HTTP `401` while `GITHUB_TOKEN` was set. Network connectivity to GitHub was independently available. After removing the environment variable, the same command succeeded anonymously against the public repository.

Successful rerun:

```text
python3 -m upgradepilot googlefonts/glyphsLib 1145
→ exact PR and head identity acquired
→ pytest 9.0.2 → 9.0.3 extracted
→ 2 exact-head workflow runs acquired
→ Regression Tests classified sufficient
→ Test + Deploy classified unresolved
→ overall CI authority classified sufficient
```

The evidence therefore indicates an invalid, expired, or otherwise unusable token in the local environment—not a regression in the shared-contract refactor. No token value was exposed or recorded.

## What the validation establishes

- neutral JSON value contracts operate correctly;
- GitHub adapters preserve their established public classifications and messages;
- PyPI adapters preserve their evidence/problem classifications;
- existing GitHub and PyPI live acquisition paths still work;
- no CLI endpoint, authority rule, or product claim changed;
- no new dependency or universal HTTP framework was introduced.

It does not establish compatibility, upgrade safety, complete CI coverage, upstream release authority, or a maintainer recommendation.

## Stable repository rule activated

The validated architectural lesson is:

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

## Deferred possible extraction

Bounded response-body reading may become the next shared primitive only after the upstream source format is selected. It should be extracted only when a second consumer needs semantics genuinely identical to PyPI's streamed limit and response-closing behavior.

## Learning result

```text
same syntax or library call
≠
same responsibility
```

`isinstance(value, Mapping)` has source-neutral meaning. A PyPI release `404` followed by a package lookup has PyPI-specific evidence meaning. Only the first belongs in the shared foundation.

## Final classification and continuation

**Completed and behavior-validated.**

The proven duplication was removed without widening the product or creating a generic source framework. B2 can now resume at the bounded design comparison for binding PyPI project-link candidates to a project-controlled source that applies to the exact proposed release.