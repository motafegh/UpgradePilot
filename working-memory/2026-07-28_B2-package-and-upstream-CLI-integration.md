# B2 Package and Upstream Evidence CLI Integration

**Date:** 2026-07-28  
**Operation:** Expose the validated package and project-controlled exact-release evidence through the existing public command path  
**Starting revision:** `b6115ab6b96ff430f88fbe0e8beca73956c70384`  
**Status:** Active implementation

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

The CLI remains an orchestrator. It must not duplicate package parsing, provenance reconciliation, source-authority rules, tag selection, or semantic interpretation.

## Accepted input and output contracts

For a supported dependency change, the CLI will call:

1. `PyPIReleaseClient.get_release(package, proposed_version)`;
2. `UpstreamSourceResolver.resolve(package_evidence)` only when package evidence is available.

The terminal report will expose:

- package evidence state;
- exact published package/version identity;
- distribution-file count;
- upstream evidence state;
- canonical upstream repository;
- usable provenance coverage;
- unavailable-provenance filenames when present;
- accepted exact tag;
- release locator;
- exact tag-object SHA;
- semantic `claim_state`.

The full release body will not be printed by default.

## Problem-state behavior

`PackageReleaseProblem` and `UpstreamSourceProblem` are normal bounded evidence outcomes. The CLI will print their exact `state` and `detail`, stop dependent later stages, and preserve the existing shell-exit contract.

Therefore:

- package problem → upstream source is not evaluated;
- upstream problem → package evidence remains visible and upstream state/detail are printed;
- unsupported dependency → CI, package, and upstream stages remain not evaluated;
- no new recommendation or safety exit code is introduced.

## Test obligations

Controlled CLI tests must prove:

1. complete package and upstream success output;
2. package problem output and no upstream call;
3. upstream problem output after successful package evidence;
4. unsupported dependency does not trigger package or upstream acquisition;
5. full release prose is not printed;
6. existing PR, dependency, CI output, and exit behavior remain intact.

After implementation, run the complete active suite and one live public command.

## Non-goals

This integration does not:

- interpret release prose;
- independently verify attestation cryptography;
- make compatibility, safety, merge, defer, or block recommendations;
- search additional release documents or arbitrary tags;
- reorganize source modules;
- add a dependency, service, model, persistence layer, or target mutation.
