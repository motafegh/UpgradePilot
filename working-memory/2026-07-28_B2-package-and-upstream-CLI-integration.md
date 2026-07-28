# B2 Package and Upstream Evidence CLI Integration

**Date:** 2026-07-28  
**Operation:** Expose the validated package and project-controlled exact-release evidence through the existing public command path  
**Starting revision:** `b6115ab6b96ff430f88fbe0e8beca73956c70384`  
**Implementation revision:** `2303f453a71948579ab2c48555314ed14fea25a3`  
**Behavior-validated repository revision:** `bc5aafece111802f1e777dd2b8151ccad1fd822e`  
**Status:** Completed and behavior-validated

## Objective

Extend the current public CLI pipeline from validated PR, dependency, and CI evidence into the already behavior-validated package and upstream-source boundaries:

```text
public repository + PR number
→ PR and changed-file evidence
→ exact pinned dependency change
→ exact-head CI authority
→ exact PyPI package/version evidence
→ project-controlled exact-release source evidence
→ concise terminal presentation
```

The CLI remains an orchestrator. It does not duplicate package parsing, provenance reconciliation, source-authority rules, tag selection, or semantic interpretation.

## Implemented orchestration

For a supported `PinnedDependencyChange`, `cli.py` now:

1. preserves the existing exact-head CI acquisition and authority evaluation;
2. calls `PyPIReleaseClient.get_release(package, proposed_version)`;
3. calls `UpstreamSourceResolver.resolve(package_evidence)` only after successful package evidence;
4. prints the typed package and upstream result without reinterpreting it;
5. returns the existing completed-analysis exit status for normal problem or unresolved states.

The GitHub token is passed to the new `GitHubReleaseClient` used inside the resolver so every GitHub stage uses one environment credential identity.

## Terminal output

Successful package evidence exposes:

- `Package evidence: available`;
- exact published package/version;
- distribution-file count.

Successful upstream evidence exposes:

- `Upstream source: available`;
- canonical repository;
- usable provenance coverage;
- explicitly unavailable-provenance filenames or `none`;
- accepted exact tag;
- release URL;
- exact tag-object SHA;
- `Claim state: unresolved_claim`.

The release body is intentionally not printed.

## Problem-state behavior

`PackageReleaseProblem` and `UpstreamSourceProblem` remain normal bounded evidence outcomes:

- package problem → state/detail are printed and upstream is `not evaluated`;
- upstream problem → successful package evidence remains visible and upstream state/detail are printed;
- unsupported dependency → CI, package, and upstream stages remain explicitly not evaluated;
- the command returns `0` for these completed evidence outcomes;
- existing input and exceptional GitHub PR/CI exit codes remain unchanged.

This preserves an important distinction:

```text
analysis reached an explicit unsupported/unavailable result
≠
program crashed or could not execute its owning boundary
```

## Controlled tests added

Added `tests/test_cli.py` with four tests covering:

1. full package/upstream success presentation;
2. package problem stopping upstream resolution;
3. upstream problem preserving successful package evidence;
4. unsupported dependency skipping every dependent stage.

The tests also protect:

- package and resolver call arguments;
- existing CI output presence;
- provenance coverage output;
- exact tag and tag-object output;
- the semantic `unresolved_claim` boundary;
- non-disclosure of the full release body;
- unchanged completed-analysis exit status.

## Implementation commits

```text
fdc4cd2300634c25995badeb2db474f0f99ed085  Start B2 package and upstream CLI integration
c1a9c3d4c15437c03f04feabee521f720a7a6f05  Integrate package and upstream evidence into CLI
2303f453a71948579ab2c48555314ed14fea25a3  Test package and upstream CLI orchestration
78b4b70263b76e9b45e36f1a6784aafa914ee63c  Record CLI evidence integration implementation
bc5aafece111802f1e777dd2b8151ccad1fd822e  Set CLI integration validation gate
```

## Complete-suite validation

Observed in Ali's WSL2 Python 3.12 environment after pulling revision `bc5aafece111802f1e777dd2b8151ccad1fd822e`:

```text
Ran 64 tests in 0.021s
OK
```

This establishes that:

- the four new CLI orchestration tests passed;
- the previous 60 source, acquisition, parsing, reconciliation, and CI-authority tests still passed;
- the integrated source tree imports and executes under the active project environment;
- no deterministic regression was observed in the complete active suite.

## Integrated live-command validation

Command:

```bash
unset GITHUB_TOKEN
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

Observed result:

```text
existing PR identity and changed-file evidence preserved
existing pytest 9.0.2 → 9.0.3 dependency evidence preserved
existing exact-head workflow/job evidence preserved
CI authority: sufficient
Package evidence: available
Published package: pytest==9.0.3
Distribution files: 2
Upstream source: available
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Provenance unavailable files: none
Accepted tag: 9.0.3
Release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

The full release body and any compatibility, safety, or maintainer recommendation were not printed.

## Permitted integrated claim

> The public UpgradePilot command now behavior-validly connects exact PR and dependency identity, bounded exact-head CI authority, exact PyPI package/file identity, PyPI-reported publisher provenance, matching upstream repository identity, and an exact GitHub Release/tag reference into one concise evidence report.

The result does not establish:

- independent cryptographic verification of PyPI attestations;
- semantic meaning of the release body;
- target-repository compatibility or upgrade safety;
- a merge, defer, or block recommendation.

## Learning result

```text
modules existing in one package
≠ end-to-end product integration

controlled orchestration tests passing
+ complete repository suite passing
+ one live public command traversing every stage
= behavior-validated integrated command path

upstream source available
≠ upstream claim interpreted
```

## Stop line reached

The selected minimum package and upstream evidence increment is complete:

- trusted package and exact-release upstream evidence are exposed through the public product path;
- explicit problem states remain visible;
- semantic interpretation and recommendation remain outside this completed increment.

The next legitimate B2 boundary is Increment E — Transparent decision. Begin it only with a bounded decision-method design that states the exact recommendation or abstention claim, decisive evidence, unresolved conditions, and proof obligations before implementation.
