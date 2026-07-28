# B2 Package and Upstream Evidence CLI Integration

**Date:** 2026-07-28  
**Operation:** Expose the validated package and project-controlled exact-release evidence through the existing public command path  
**Starting revision:** `b6115ab6b96ff430f88fbe0e8beca73956c70384`  
**Implementation revision:** `2303f453a71948579ab2c48555314ed14fea25a3`  
**Status:** Implemented; complete-suite and live-command validation pending

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
```

## Validation required

Run in Ali's WSL2 Python 3.12 environment:

```bash
git pull origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

Expected count if no unrelated tests changed: **64 tests**.

Then run the integrated live path:

```bash
unset GITHUB_TOKEN
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

The live report should retain the validated PR/dependency/CI output and continue into package and upstream evidence. The observed outcome must be recorded rather than assumed.

## Non-goals and stop line

This integration does not:

- interpret release prose;
- independently verify attestation cryptography;
- make compatibility, safety, merge, defer, or block recommendations;
- search additional release documents or arbitrary tags;
- reorganize source modules;
- add a dependency, service, model, persistence layer, or target mutation.

Stop after the complete suite and one integrated live command are reviewed. Only then close this record and decide the next bounded product action.
