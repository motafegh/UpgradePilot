# S014 — production-ready-cicd pip: already satisfied versus installed by command

**Date:** 2026-09-22
**Status:** Complete at admitted simulation depth
**Form:** untouched real Dependabot proposal + natural base/head CI control

## Case identity

Target: `HaitamELF/production-ready-cicd#11`

Dependency transition:

`pip 26.1.2 → 26.2.1` in `requirements-tooling.txt`.

Frozen revisions:

- base: `b9ea298798d7d1d7d74ec6769d5164bf4ac8bd04`
- head: `9ee04438e99b8cb87818f830009b276b892d5d38`
- observed PR runtime merge checkout: `65bbb07fd28cdbdc224d3ed655af96f3480ec429`

The CI workflow blob is identical at base and head: `519bd96f32a06140dbcdf5927813c06f9901faba`.

## Owned question

> Can successful execution of the exact pip requirements command be described generically as `installed the proposed version`, or must the product use the weaker and more accurate proposition `the exact requirement was satisfied/present at command completion`?

## Exact command

The unchanged `Python Dependency Audit` job executes one dependency-consuming command:

`python -m pip install -r requirements-tooling.txt`

The changed file directly pins pip on line 1.

## Natural before/after pair

### Base run

Base CI run `35755384469`, job `106839725526`, success.

With `pip==26.1.2`, the runtime reports:

- `Collecting pip==26.1.2`;
- `Found existing installation: pip 26.2.1`;
- `Successfully uninstalled pip-26.2.1`;
- `Successfully installed ... pip-26.1.2 ...`.

This command actively changed pip state.

### PR run

Head-associated CI run `35756041967`, job `106841940374`, success.

The PR runtime checks out synthetic merge commit `65bbb07...` combining head `9ee04438...` with base `b9ea298...`.

With `pip==26.2.1`, the same command reports:

`Requirement already satisfied: pip==26.2.1 ... (26.2.1)`

and the final `Successfully installed ...` list contains the other tooling dependencies but not pip.

This command succeeds without freshly installing pip.

Both runs use setup-python CPython 3.12.14 and the same workflow definition.

## Core distinction

These two successful executions have different state-transition mechanisms:

`base: preexisting 26.2.1 → uninstall → install 26.1.2`

versus:

`PR: preexisting 26.2.1 → requirement already satisfied → retain 26.2.1`.

Therefore:

`successful exact pip install command`

does not imply:

`proposed version was newly installed by this command`.

The bounded proposition that survives both observations is:

`at successful command completion, the exact requested pip version was satisfied/present in the selected environment`.

## Additional proof-path distinction

The PR runtime log is stronger than generic step success because it directly observes pip's exact-version state as `Requirement already satisfied`.

This suggests two conceptually distinct future evidence routes:

1. operation-guarantee inference: exact requirement + admitted semantics + exact success → satisfied/present at completion;
2. direct state observation: trusted runtime evidence directly reports the exact requirement/version as already satisfied.

S014 does not decide whether UpgradePilot should ingest pip logs or how those routes should be represented.

## What S014 establishes

- B5's `satisfied/present at completion` wording matches a real dependency-update case;
- `installed by this command` would overclaim in the PR execution;
- the same exact workflow/command can either mutate package state or leave an already-satisfying version untouched depending on the requested version and incoming environment;
- provenance of how the state became true is separate from the state proposition itself;
- direct runtime state evidence may be stronger than generic command-success inference.

## What S014 does not establish

Do not infer:

- that all successful pip commands preserve state;
- that ambient semantics can always be ignored;
- that the package remains present after later commands;
- exact artifact/wheel identity;
- behavioral compatibility or update safety;
- that log parsing must be implemented;
- that the observed PR ran the bare head rather than the synthetic merge revision.

## Evidence bundle

1. `artifacts/CASE_IDENTITY_AND_CONTROL.json`
2. `artifacts/BASE_STATE_CHANGE.json`
3. `artifacts/PR_ALREADY_SATISFIED_STATE.json`
4. `artifacts/PROOF_BOUNDARY_AND_STOP.json`

Supporting analysis:

- `../../S014_CANDIDATE_SCREENING.md`
- `../../S014_POST_CASE_SYNTHESIS.md`

## Stop

S014 stops at the command-completion state proposition and provenance distinction. Reopen only for a concrete implementation/evaluation question about direct runtime state witnesses, later state continuity, or artifact identity.