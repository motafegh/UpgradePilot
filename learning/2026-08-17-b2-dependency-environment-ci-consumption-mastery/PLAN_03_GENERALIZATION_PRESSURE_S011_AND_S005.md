# Plan 03 — Generalization Pressure: S011 + S005

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Cases:** S011 — Dictare MLX optional extra; S005 — ModelArrayIO tox/uv-lock mediation  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plan 02 S001 proof path understood sufficiently to transfer  
**Live-state authority:** `../../MEMORY.md`  
**Status:** `[ ] NOT STARTED`

## Purpose and stop line

Pressure-test the S001 mental model against two different real repository shapes so we learn the architecture rather than one happy-path syntax.

This plan is intentionally short. It does not attempt to fully learn MLX, tox, or `uv-venv-lock-runner`, and it does not authorize new generic support for them.

## Pace rule

Use each case only until it exposes the architectural distinction we need. If the current implementation abstains on a mechanism, preserve that boundary rather than opening an implementation detour during this learning plan.

## Chunk map

### [ ] Chunk 1 — S011: optional-extra non-selection despite green CI

**Main subjects**
- Python optional dependencies / extras and why projects use them;
- Dictare's `mlx` extra as a real Apple-Silicon runtime family;
- practical meaning of editable install `pip install -e ".[dev]"`;
- affected environment `mlx` vs statically selected environment `dev`;
- `not_established` as a bounded evidence state.

**Real material**
- `product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md`;
- frozen NumPy `1.26.4 → 2.4.6` change inside `[project.optional-dependencies].mlx`;
- relevant Ubuntu/macOS workflow install commands;
- exact target activation context only as needed to establish that `mlx` is a real path.

**First-contact flags**
- optional extra;
- editable install;
- MLX at the operational depth needed for Dictare's Apple-Silicon path.

**UpgradePilot source / functions / tests**
- `src/upgradepilot/dependency/environment_selection.py`
  - `OptionalExtraSelector`;
  - `observe_project_environment_selection(...)`;
- `src/upgradepilot/dependency/environment_membership.py`
  - affected source environment vs selected environment comparison;
- downstream CI consumption/coverage source from Plan 02 only as needed to follow the consequence;
- `tests/test_project_environment_selection.py`;
- `tests/test_project_source_environment_membership.py`;
- `tests/test_ci_dependency_coverage.py` where the S011-shaped consequence is protected.

**Do not miss / assume**
- `.[dev]` != `.[mlx]`;
- macOS workflow != Apple-Silicon MLX dependency-environment coverage;
- `not_established` does not mean NumPy/MLX is absent at runtime everywhere;
- green standard CI must not be promoted into coverage for an affected environment it did not statically select.

**Gate / proceed when**
- Ali can predict `affected mlx + selected dev → not_established`, distinguish it from `unresolved`, and explain why green CI remains non-discriminating for this affected extra.

### [ ] Chunk 2 — S005: tox-mediated uv-lock consumption pressure

**Main subjects**
- tox and tox environments at the minimum operational depth needed here;
- `uv-venv-lock-runner` only as the mediation mechanism preserved by the case;
- how CI can reach a uv-locked environment indirectly through tox instead of a direct `uv sync` workflow command;
- architectural overfitting risk.

**Real material**
- `product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/CASE.md`;
- pytest `9.0.3 → 9.1.1`, changed `uv.lock`;
- tox `latest` environments → `uv-venv-lock-runner` → pytest;
- exact-head latest CI evidence as historical case evidence.

**First-contact flags**
- tox;
- tox environment;
- `uv-venv-lock-runner`.

**Source/code relation**
- revisit `src/upgradepilot/dependency/environment_selection.py`, `uv_membership.py`, and CI composition only to ask what the current admitted syntax/mechanisms actually cover;
- do **not** manufacture a tox interpretation if current code does not implement one.

**Do not miss / assume**
- architecture must not equate `uv.lock` consumption with the literal presence of direct `uv sync` in GitHub Actions;
- the historical case's successful tox jobs do not automatically mean current UpgradePilot can statically interpret that mediation;
- transfer pressure can reveal a future capability need without becoming immediate implementation scope.

**Gate / proceed when**
- Ali can explain why S005 challenges syntax-specific overfitting and identify where current support should abstain/defer rather than overclaim.

### [ ] Chunk 3 — Compare the three cases and preserve the reusable model

**Main subjects**
- S001: supported transitive selected-environment membership/consumption;
- S011: explicit affected-extra vs selected-extra mismatch;
- S005: indirect environment formation/consumption pressure not reducible to direct workflow syntax.

**Do not miss / assume**
- the three cases test different propositions; do not force them into one Boolean model;
- a real case can be important even when it is only pressure against architectural assumptions;
- current implementation support and future generalization pressure must remain distinguishable.

**Gate / proceed when**
- Ali can use the cases to predict whether evidence should be supported, not established, unresolved, or outside current admitted support—and explain why.

## Plan-level TODO / gate

- [ ] Optional-extra activation/non-selection is understood through S011.
- [ ] `not_established` is not confused with runtime absence or analysis failure.
- [ ] S005 tox mediation is understood at the minimum useful depth.
- [ ] Current support is not overstated merely because a historical case has stronger manual evidence.
- [ ] S001/S011/S005 can be compared using the proposition ladder rather than memorized outcomes.

## Depth / deliberate deferral

**Must master across the route:** environment identity/selection mismatch, evidence-state distinctions, architectural abstention, avoiding syntax-specific overfitting.  
**Operational only:** MLX internals, tox internals, runner-plugin implementation.  
**Deferred:** implementing generic tox/runner mediation, platform execution, compatibility experiments, universal environment modeling.

## Handoff

Proceed to Plan 04 once the S001 model survives these contrasts. The next task is to locate the actual ordinary-application integration seam and decide—using live project authority—when learning has become sufficient to return to building.
