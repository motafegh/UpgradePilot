# S016 Post-Case Synthesis — Lock Membership Is Not Selected-Environment State

**Date:** 2026-09-22
**Status:** Completed bounded synthesis; non-controlling Product Simulation evidence
**Scenario:** `scenarios/S016-thumbor-uv-selector-scope-coverage/README.md`

## 1. Result

S016 empirically validates the current UpgradePilot separation between uv lock transition, selected environment, and changed-package reachability.

The same Dependabot proposal and same `uv.lock` participate in two successful direct workflow operations:

- `uv sync --locked --extra tests` → selected tests environment includes `coverage==7.15.4`;
- `uv run --locked --only-group release --only-group build ...` → selected release/build environment succeeds without selecting coverage.

Therefore raw lock membership plus uv command success is not a valid changed-package state proposition.

## 2. B5 consequence

B5 P2 is necessary and substantive:

`exact source/environment relation` must establish that the proposed package is reachable from the exact roots selected by this command.

Only then can B4/B5 operation semantics and runtime success contribute to:

`proposed version satisfied/present at command completion`.

A successful sibling uv command with a different selector scope is not transferable evidence.

## 3. Existing architecture validated

Current source already models the important ownership split:

- `uv_lock.py`: one exact textual lock transition;
- `environment.py`: lock context is not universal environment membership;
- `environment_selection.py`: uv extras/groups/package selectors;
- `uv_reachability.py`: selected-root reachability.

S016 is valuable precisely because it does **not** demand more architecture. It shows why the existing decomposition exists and gives it a real regression/evaluation anchor.

## 4. Negative control precision

The release/build command creates a fresh `.venv` and installs its selected package set without coverage.

For the bounded command/environment proposition, this is strong evidence that coverage is not part of the selected release/build environment.

Do not broaden that into:

- global runner absence;
- absence from caches or another environment;
- absence before environment creation;
- package absence as a repository-wide fact.

The useful negative conclusion is selector-relative:

`this operation is not a positive coverage-state witness`.

## 5. Direct runtime output versus product proof

The uv runtime output directly reports the positive test-scope package state (`+ coverage==7.15.4`) and the release scope's installed package set.

This is excellent evaluation evidence.

It does not mean UpgradePilot must ingest uv logs. Current selected-root reachability plus admitted uv operation semantics may provide an inferential proof route; a future direct runtime witness would be a separate route, as already exposed by S014.

## 6. Relationship to S015

S015:

`same requirements file + different Python marker applicability`.

S016:

`same uv.lock + different explicit extras/groups`.

Both establish the same higher-level invariant:

> source identity alone does not define the dependency proposition; applicability/selection must compose with the exact environment.

## 7. Engineering-priority reality check

Scoped uv sync/run is an observed real CI pattern in an untouched Dependabot update, and current UpgradePilot already has bounded machinery for it.

Therefore the right response is not a new generalized environment system. The right response is to preserve and test the existing selector/reachability ownership when B5 is implemented.

## 8. Main-thread handoff

Useful B5/B6 handoff:

1. P2 should consume the existing selected-root reachability result rather than raw lock membership.
2. A `not_established` result for one selected scope must not become package absence.
3. Runtime success from another selector scope must not be borrowed.
4. Keep the current separation between lock extraction and environment selection/reachability.
5. Use S016 as an implementation/regression case when the B5 proof slice is selected.

No source implementation is authorized by this scenario.

## 9. Stop

S016 is complete at the admitted depth. Reopen only for B5/B6 transfer, selector-parser changes, or reachability implementation changes.