# B2 Shared External-Source Foundation Investigation

**Date:** 2026-07-27  
**Operation:** Audit and remove proven external-source validation duplication before adding another source  
**Starting revision:** `4520f981d7c7e0ab9f716daab0773643405e1338`  
**Investigation record created:** `2c55c107a8e2a831f5f0b65747e4ba83910adc2e`  
**Implemented revision:** `98a4914ce70b1cfe8d5ddd612185cb527d52a02c`  
**Status:** Implemented; behavior validation pending

## Objective

Determine whether UpgradePilot has enough repeated external-source behavior to justify a small shared foundation before implementing the project-controlled upstream-source resolver.

The goal is not to generalize every client. The goal is to remove proven repetition while preserving source-specific authority, identity, failure, and evidence semantics.

## Why the investigation was justified

UpgradePilot had:

- a shared GitHub REST/JSON foundation used by multiple GitHub clients;
- a separate PyPI exact-release client with its own JSON value checks;
- an upcoming upstream-source resolver that may introduce another acquisition boundary.

One GitHub implementation alone did not justify a source-neutral abstraction. Two implemented boundaries plus a credible third created a concrete duplication risk.

## Inventory findings

### Proven repeated mechanics

GitHub and PyPI both required runtime checks for:

- JSON objects and arrays;
- non-empty strings;
- integers while rejecting booleans;
- positive and non-negative integer ranges;
- actual boolean values;
- optional non-empty strings.

These checks have identical meaning before any source-specific error or evidence classification is applied.

### Similar-looking behavior that remains source-specific

The HTTP and evidence layers are not equivalent:

- GitHub uses authentication and API-version headers; PyPI does not;
- GitHub raises `GitHubAcquisitionError` and `GitHubResponseError`; PyPI returns `PackageReleaseProblem` values;
- GitHub and PyPI assign different meanings to HTTP status codes;
- PyPI performs a second package lookup after a release `404`;
- PyPI streams and caps response bodies while GitHub retains its existing JSON boundary;
- the future upstream source may be HTML, Markdown, raw text, repository content, or structured API data.

A universal HTTP client was therefore rejected as premature and likely to erase useful semantics.

## Compared options

### Keep every source completely separate

Rejected as the default path because JSON value-contract duplication was already proven and a third copy was likely.

### Extract only source-neutral JSON value contracts

Accepted. This removes exact duplication while focused clients preserve field policy, errors, evidence states, identity, and authority.

### Introduce a general external-source acquisition client

Rejected for now. It would require configuration or callbacks for materially different transport and evidence contracts before the next source format is selected.

## Approved boundary

Ali approved this exact design:

```text
source-neutral JSON value contracts
├── GitHub adapters preserve GitHub exceptions and messages
├── PyPI adapters preserve malformed-response classification
└── future structured sources may reuse identical value rules
```

The shared layer must not own:

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
- all existing HTTP, authentication, status, and JSON-decoding behavior.

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

- `tests/test_json_contract.py` — direct success and rejection tests for the neutral contracts;
- `tests/test_external_contract_adapters.py` — GitHub message-layer preservation and PyPI malformed-response translation.

Existing GitHub and PyPI tests remain the broader regression proof.

## Implementation commits

```text
14793050bec6f0fd14e6503acca9b0360daf064c  Add source-neutral JSON value contracts
d629e964e5d388b8bb16df83ce9afeaa76c2c7fd  Test source-neutral JSON value contracts
0f856040b3a121663e7f7ae9eb37697b42da460a  Delegate GitHub JSON checks to shared contracts
7112343d8d375aefa6310fb6112cef809b396eca  Delegate PyPI JSON checks to shared contracts
9031021611d439fad449c259f51c91e965f85255  Preserve layered GitHub integer errors
98a4914ce70b1cfe8d5ddd612185cb527d52a02c  Protect source-specific contract translations
```

## Validation required

The implementation must still be validated in Ali's WSL2 Python 3.12 environment:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

Expected discovery count if no other tests have changed: **41 tests**.

Because both source adapters changed internally, validation should also include:

```bash
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

and one unmocked `PyPIReleaseClient().get_release("pytest", "9.0.3")` smoke check.

The runtime used for this implementation could not clone the repository and the commits exposed no automated status checks, so no local or hosted test result is claimed here.

## Deferred possible extraction

Bounded response-body reading may become the next shared primitive only after the upstream source format is selected. It should be extracted only when a second consumer needs semantics genuinely identical to PyPI's streamed limit and closing behavior.

## Stable instruction pending validation

After the full regression and live smoke checks pass, add this concise repository-wide rule:

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

## Learning result

```text
same syntax or library call
≠
same responsibility
```

`isinstance(value, Mapping)` has source-neutral meaning. A PyPI release `404` followed by a package lookup has PyPI-specific evidence meaning. Only the first belongs in the shared foundation.

## Current classification

**Implemented, not yet behavior-validated.**

The approved architectural boundary is now represented in source and controlled tests. Closure requires Ali's complete Python 3.12 suite and the two safe live smoke checks. After validation, the stable instruction can be activated and B2 can resume at upstream-source resolution.
