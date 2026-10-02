# S013 — LangChain anyio: prior sync state under later uv no-sync execution

**Date:** 2026-09-22
**Status:** Complete at admitted simulation depth
**Form:** untouched real public Dependabot proposal + exact workflow/runtime evidence

## Case identity

Target: `langchain-ai/langchain#40646`

Dependency transition: `anyio 4.14.2 → 4.15.1` in `libs/standard-tests/uv.lock`.

Frozen proposal revisions:

- base: `39535dc58e029c28b562f531cfbad810c23e1f5a`
- head: `3908f2baf0db73c0f3242107df0428a510f4be47`
- observed PR CI merge checkout: `63e06a2ba490c0bcdc7de672d38e5210f7cc0650`

The runtime checkout is a GitHub synthetic PR merge commit combining the proposal head with the then-base. It is not the bare head and is not interchangeable with the PR API's later post-merge commit metadata.

## Owned question

> Can a real dependency-update CI establish the proposed dependency state through an earlier explicit `uv sync`, then legitimately exercise that already-formed environment with a later `uv run` while `UV_NO_SYNC=true`, without attributing synchronization to the later command?

## Why this case exists

The exact workflow/reusable workflow globally declares `UV_NO_SYNC=true`, but the unit-test job explicitly executes `uv sync --group test --dev` before testing.

Observed runtime then reports the proposed version installed, followed by a later `uv run --group test pytest ...` under the same visible no-sync baseline.

This separates three propositions:

`ambient no-sync semantics` != `earlier environment formation` != `later exercise`.

## Exact sequence

At the observed PR merge revision:

1. setup uv;
2. `uv sync --group test --dev`;
3. runtime result reports `anyio==4.15.1` installed;
4. next workflow step executes `make test`;
5. the selected Makefile target expands to `uv run --group test pytest ...`;
6. pytest starts from the project `.venv` and reports plugin `anyio-4.15.1`.

No package-mutating workflow step exists between the selected sync step and the selected test step.

## Core distinction

An over-broad rule would say:

`UV_NO_SYNC=true → no usable dependency-state evidence`.

S013 shows that is false for this real sequence. No-sync constrains what the later `uv run` does; it does not erase state established by an earlier explicit sync.

The opposite overclaim is also invalid:

`later successful uv run → later uv run synchronized/installed the proposed version`.

The state-forming evidence belongs to the earlier sync operation and its runtime result.

## Runtime evidence

Head-associated CI run `35378301060` succeeded.

Selected job `105708268180` (`libs/standard-tests`, Python 3.14) logs:

- `UV_NO_SYNC: true`;
- `uv sync --group test --dev`;
- `Installed 48 packages`;
- `+ anyio==4.15.1`;
- later `uv run --group test pytest -q tests/unit_tests/`;
- pytest plugin list containing `anyio-4.15.1`.

Selected Python 3.10 job `105708268228` independently shows the same semantic sequence and proposed version.

## What S013 establishes

- a real Dependabot uv-lock update can run under visible ambient `UV_NO_SYNC=true`;
- an explicit earlier `uv sync` may still form the relevant environment;
- runtime installer/sync output may establish the proposed version at that state-forming boundary;
- later no-sync execution can exercise the already-formed environment;
- package-manager semantic interpretation must be operation- and sequence-relative;
- state formation and later exercise may need explicit temporal/evidence composition.

## What S013 does not establish

Do not infer:

- that every `UV_NO_SYNC` workflow is safe or sufficiently evidenced;
- that every prior sync state survives arbitrary later operations;
- that pytest plugin reporting alone proves all package-state properties;
- that runtime merge-ref evidence equals bare-head execution;
- ecosystem prevalence;
- a required implementation architecture or generic environment resolver.

## Evidence bundle

Read:

1. `artifacts/CASE_IDENTITY_AND_TRANSITION.json`
2. `artifacts/ENVIRONMENT_AND_COMMAND_SEQUENCE.json`
3. `artifacts/RUNTIME_STATE_AND_EXERCISE.json`
4. `artifacts/DISCOVERY_AND_STOPPING.json`

Supporting analysis:

- `../../S013_CANDIDATE_SCREENING.md`
- `../../S013_POST_CASE_SYNTHESIS.md`
- `../../2026-09-22_G3_REALITY_CHECK_AMBIENT_SEMANTICS.md`

## Stop

S013 stops at the bounded sequence:

`exact changed lock → explicit successful sync → proposed version observed → later no-sync test execution`.

Reopen only for a concrete question about intervening mutation, cross-job continuity, richer state witnesses, or implementation transfer.