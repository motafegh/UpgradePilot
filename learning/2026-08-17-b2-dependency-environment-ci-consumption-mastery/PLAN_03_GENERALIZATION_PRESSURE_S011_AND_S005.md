# Plan 03 — Generalization Pressure: S011 + S005

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Cases:** S011 — Dictare MLX optional extra; S005 — ModelArrayIO tox/uv-lock mediation  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plan 02 S001 proof path understood sufficiently to transfer  
**Live-state authority:** `../../MEMORY.md`  
**Depth companion:** `PLAN_03_MASTERY_AND_DEPTH_MAP.md`  
**Career ownership overlay:** `CAREER_DAY30_OWNERSHIP_HANDOFF.md` — transfer evidence/participation rules only; no technical sequencing authority  
**Status:** `[ ] NOT STARTED`  
**Refined:** 2026-08-22 — explicit transfer-depth rationale and evidence-driven audit alignment added

## Purpose and stop line

Pressure-test the S001 mental model against two different real repository shapes so we learn the architecture rather than one happy-path syntax.

This plan is intentionally short. It does not attempt to fully learn MLX, tox, or `uv-venv-lock-runner`, and it does not authorize new generic support for them.

## Pace and depth rule

Use each case only until it exposes the architectural distinction we need. Before deeper learning, use `PLAN_03_MASTERY_AND_DEPTH_MAP.md` to state why the selected reasoning/source/external-technology depth matters.

The default depth here is **transfer reasoning**, not new whole-file mastery. If a current implementation abstains on a mechanism, preserve that observed boundary rather than opening an implementation detour during this learning plan; do not assume the abstention is good architecture merely because it is conservative.

## Smart transfer, ownership, and parallel audit rule

This plan is less about reading every new source path and more about testing whether our existing model **generalizes for the right reasons**.

When source is revisited:

```text
real contrasting evidence first
→ state why this case/source slice deserves the planned depth
→ Ali predicts current state/branch/reason before the answer when enough context exists
→ inspect only the executable source branches needed to test that prediction
→ explain material syntax/control flow if it changes the result
→ compare the prediction with observed source/test evidence
→ audit correctness, evidence-state choice, support boundary, and syntax-specific assumptions
→ distinguish current support from future capability pressure
→ preserve material findings at the proper owner
```

This plan is the primary **changed-case transfer** surface for the Career ownership overlay. The useful evidence is not memorizing S001 and repeating it; it is making a prediction in S011/S005 before the assistant supplies the outcome and then explaining what transferred and what did not.

Do not treat a historical case as proof that current UpgradePilot supports it. Conversely, do not treat current abstention as automatically good design. Ask whether the observed boundary is correct for the current proposition, whether any intended boundedness is actually evidenced by plan/source/history, and whether the case reveals brittle coupling or a genuine future capability gap. If rationale is not established, say so.

Comments/docstrings may orient source inspection but do not substitute for the relevant executable branch when a source claim is being tested. Do not force code modifications or manufacture failures for Career evidence during transfer pressure.

Material durable audit findings follow `../../audits/README.md`; small transfer/audit observations may remain in `LEARNING_MEMORY.md`.

## Chunk map

### [ ] Chunk 1 — S011: optional-extra non-selection despite green CI

**Main subjects**
- Python optional dependencies / extras and why projects use them;
- Dictare's `mlx` extra as a real Apple-Silicon runtime family;
- practical meaning of editable install `pip install -e ".[dev]"`;
- affected environment `mlx` vs statically selected environment `dev`;
- `not_established` as a bounded evidence state.

**Why this depth matters**
- S011 is the first materially different environment-selection transfer case;
- Ali must be able to derive the result from affected-vs-selected environment semantics rather than memorize S001;
- MLX/pip internals beyond interpreting the real activation path do not own the UpgradePilot proposition.

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

**Transfer / code-audit focus**
- before showing the current outcome, Ali predicts the evidence state and gives the reason from `affected mlx` vs `selected dev`;
- inspect only the selector/environment-comparison executable branches needed to verify or correct that prediction;
- learn exact matching/normalization syntax if it carries environment identity;
- audit whether `not_established` accurately represents the evidence gap without silently implying runtime absence;
- audit whether platform/job labels are accidentally treated as activation evidence;
- when useful, explain one focused test that discriminates mismatch from unresolved analysis failure.

**Do not miss / assume**
- `.[dev]` != `.[mlx]`;
- macOS workflow != Apple-Silicon MLX dependency-environment coverage;
- `not_established` does not mean NumPy/MLX is absent at runtime everywhere;
- green standard CI must not be promoted into coverage for an affected environment it did not statically select;
- current comparison behavior is not presumed correct merely because tests encode it.

**Gate / proceed when**
- Ali can predict `affected mlx + selected dev → not_established` before the answer, verify it against the material executable source/test path, explain why this transfer reasoning deserves mastery depth, distinguish it from `unresolved`, explain why green CI remains non-discriminating for this affected extra, and critically evaluate at least one material comparison/proof choice.

### [ ] Chunk 2 — S005: tox-mediated uv-lock consumption pressure

**Main subjects**
- tox and tox environments at the minimum operational depth needed here;
- `uv-venv-lock-runner` only as the mediation mechanism preserved by the case;
- how CI can reach a uv-locked environment indirectly through tox instead of a direct `uv sync` workflow command;
- architectural overfitting risk.

**Why this depth matters**
- S005 tests whether UpgradePilot's concept of environment/lock consumption is semantic or accidentally tied to one literal workflow syntax;
- tox/plugin internals are only needed far enough to establish the mediated real mechanism, not as independent mastery targets.

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

**Transfer / engineering-audit focus**
- before the assistant states the architecture conclusion, Ali predicts whether current support should establish, abstain, or remain outside the admitted mechanism and explains why;
- identify any assumption that equates a semantic concept such as lock/environment consumption with one literal workflow syntax such as direct `uv sync`;
- distinguish a safely bounded current capability from brittle architectural coupling based on evidence, not presumed implementation intent;
- if plan/history documents an intentional bounded first implementation, verify that rationale rather than invent it;
- record a future capability pressure only when the real case demonstrates it; do not turn the observation into unauthorized implementation work;
- explicitly state what did **not** transfer from S001 and why.

**Do not miss / assume**
- architecture must not equate `uv.lock` consumption with the literal presence of direct `uv sync` in GitHub Actions if the intended semantic responsibility is broader;
- the historical case's successful tox jobs do not automatically mean current UpgradePilot can statically interpret that mediation;
- transfer pressure can reveal a future capability need without becoming immediate implementation scope;
- conservative behavior is not automatically well-designed behavior.

**Gate / proceed when**
- Ali can predict the expected current-support boundary, explain why S005 challenges syntax-specific overfitting, explain why architecture-transfer reasoning deserves mastery while tox internals remain operational, identify where current support should abstain/defer rather than overclaim, and distinguish an evidenced bounded limitation from a possible architectural generalization problem.

### [ ] Chunk 3 — Compare the three cases and preserve the reusable model

**Main subjects**
- S001: supported transitive selected-environment membership/consumption;
- S011: explicit affected-extra vs selected-extra mismatch;
- S005: indirect environment formation/consumption pressure not reducible to direct workflow syntax.

**Why this depth matters**
- this comparison is the actual transfer check: it shows whether Ali can classify a new case by proposition/evidence state and distinguish a negative result from a support limitation.

**Ali transfer reconstruction**
Ali should compare the cases before receiving a final summary:

```text
S001 → what proposition is positively established?
S011 → which relation fails to be established and why?
S005 → which mechanism is outside/pressure against the current admitted interpretation?
```

Then identify:
- which concepts/control-flow patterns transferred;
- which case requires a different evidence state;
- which case exposes an architecture/support limitation rather than an ordinary negative result;
- which current design assumptions remain justified, questionable, or uncertain after comparison.

**Do not miss / assume**
- the three cases test different propositions; do not force them into one Boolean model;
- a real case can be important even when it is only pressure against architectural assumptions;
- current implementation support and future generalization pressure must remain distinguishable;
- do not equate “current code is conservative” with “current architecture is automatically optimal.”

**Gate / proceed when**
- Ali can use the cases to predict whether evidence should be supported, not established, unresolved, or outside current admitted support—and explain the evidence reason, why this transfer depth matters, what transferred from prior source understanding, and any material architectural limitation revealed by the comparison.

## Career transfer evidence target

Plan 03 should produce a concise candidate transfer record in `LEARNING_MEMORY.md` when demonstrated:

```text
prior mechanism/case
→ new materially different case
→ Ali prediction before answer
→ inspected evidence/source branch
→ what transferred
→ what did not transfer
→ assistance level
```

This is supporting evidence, not a fifth mandatory Career capability category and not a project-state owner.

## Plan-level TODO / gate

- [ ] Optional-extra activation/non-selection is understood through S011.
- [ ] `not_established` is not confused with runtime absence or analysis failure.
- [ ] S005 tox mediation is understood at the minimum useful depth and deeper tox/plugin study is explicitly unjustified for now.
- [ ] Current support is not overstated merely because a historical case has stronger manual evidence.
- [ ] S001/S011/S005 can be compared using the proposition ladder rather than memorized outcomes.
- [ ] At least one changed-case outcome is predicted before the assistant reveals it and then checked against real source/evidence.
- [ ] Ali can explain why transfer/classification deserves mastery depth while most revisited source remains navigation/working depth.
- [ ] Material architecture/syntax-specific assumptions can be challenged without turning critique into unauthorized implementation.
- [ ] Material durable findings are preserved through the audit route when warranted.

## Depth / deliberate deferral

**Must master across the route:** environment identity/selection mismatch, evidence-state distinctions, changed-case prediction/transfer, architectural abstention, avoiding syntax-specific overfitting, and the ability to separate implementation fact from engineering judgment.  
**Why:** these determine whether the S001 mental model generalizes to materially different repositories and whether Ali can recognize support limitations without overclaiming.  
**Operational only:** MLX internals, tox internals, runner-plugin implementation, incidental source syntax.  
**Why not deeper:** they explain the external mechanism but do not own the selected UpgradePilot evidence proposition.  
**Deferred:** implementing generic tox/runner mediation, platform execution, compatibility experiments, universal environment modeling.

## Handoff

Proceed to Plan 04 once the S001 model survives these contrasts through Ali-first prediction plus evidence verification, and any remaining architecture/audit questions are clearly classified rather than silently resolved by assumption. The next task is to locate the actual ordinary-application integration seam and decide—using live project authority—when learning has become sufficient to return to building.
