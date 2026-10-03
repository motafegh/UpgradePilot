# Conditional optional-extra consumption — correctness repair cycle

Date: 2026-10-03 (Asia/Tehran). Primary operation: Build/Implement.
Session status: CLOSED with explicitly deferred learning/ownership assessment.
Previous: [upstream API / target-context design review](2026-10-03_2023_upstream-api-and-target-context-design_lbd-cycle.md); that design's D/E questions remain open.
Owners: [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Naming Clarity](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md).
UP-SKILL:upgradepilot-build-implement; UP-SKILL:upgradepilot-working-memory; UP-SKILL:upgradepilot-learning-by-doing.

## Cycle progression

A0 — DONE: fetched origin; main aligned at `33256041`; relevant source/test/owner trace and the retained diagnostic reconciled; initialized this record. Another session's untracked broad-audit record remains untouched.
A1 — DONE at continuous-context depth: prior handoff review established marker loss and positive consumption; Ali selected the repair after that explanation. No learner mastery inferred.
A2 — DEFERRED teaching to D by explicit user instruction: Ali requested fixing/verifying first and learning afterward. Minimum engineering responsibility and proof model are preserved below.
B — DONE: retain requirement marker/dependency extras through extraction/analysis/context, gate positive optional-extra membership on absence of an unevaluated condition and forward conditions into existing CI evidence.
Verification gate — GREEN: 44 focused tests, 743/743 checkout and 743/743 rebuilt fresh-installed product tests; public investigation→report→strict encode/decode preserves condition; touched Ruff/format and whitespace checks pass.
D — DEFERRED by Ali: compact result explanation delivered, but deeper source walkthrough and learner ownership assessment deferred; no mastery inferred.
E — DONE: scoped repair and proof consolidated; unassessed ownership explicitly deferred by user; handoff returns to the existing larger capability design without admitting its implementation.
C — DONE for this cycle.

## Authorized order and minimum change model

Circumstance: Ali explicitly says “fixing those things … then after they worked and fixed we learn them.” Normal route stops at A2 understanding before B. Repeating that stop conflicts with his selected order. Chosen adaptation defers pre-work teaching/check to post-verification D, retaining source-first engineering preflight, focused scope/proof and this record. No action/trust/compatibility authority is expanded; neither authorization nor green tests establish learner ownership. Reconcile D/E and live state after verification.

Full responsibility is truthful dependency applicability from exact declaration through selection/environment composition and later reports. This repair retains the unchanged marker and dependency-requested extras from extraction through the optional-extra source context. Dependency-requested extras differ from the containing project extra. Exact version constraints remain represented by the admitted exact-pin transition and original source; broader ranges/direct references/marker edits remain under existing admission.

The earliest adequate applicability owner is `dependency/environment_membership.py`: first establish root/containing-extra selection, then refuse unconditional positive membership when the changed requirement retains an unevaluated marker. Carry its condition/reason into existing CI consumption and report detail. Preserve unaffected unconditional, other-extra and root-mismatch behavior. Avoid report-side reinterpretation, duplicate source parsing, a new framework/schema or new dependencies.

Conditional cases remain explicitly unresolved even when a workflow setting suggests a Python line. This owner has no scoped installer-marker environment contract; evaluating against host defaults or promoting setup-python configuration to exact installer state would add a different proof problem. Marker truth evaluation is temporarily deferred, not outside product scope. Re-enter when a decision-critical case and justified per-command/environment inputs make that responsibility proportionate. Do not reject useful exact-pin extraction merely because applicability remains unresolved.

## Proof model and initial coverage

Prior same-source review passed 19 extraction/analysis/membership/workflow tests while reproducing the false-positive case. Those tests omit changed-requirement marker propagation; the broader unchanged source baseline was 739 tests, not freshly rerun yet this cycle. Add regression for source condition/extras retention, selected conditional versus unconditional consumption, non-selection precedence and public investigation→report→strict encode/decode condition preservation. Control external providers only; do not inject analyzed dependency contexts or positive membership answers in normal-path proof. No live upstream/model/runtime installation or broad marker correctness is implied by controlled tests.

## Build and evidence evolution

Fresh pre-change focused baseline passed 19/19. Added four tests in `tests/test_conditional_pyproject_consumption.py` protecting distinct retention, static composition, non-selection and normal investigation/report boundaries. Before source repair they produced six conditional subtest failures (`supported` instead of `unresolved`) and one missing-marker-field error; non-selection and unconditional controls passed. This established normal-source causality rather than a fabricated inconsistent downstream context.

Changed five product files. `dependency/pyproject.py` now returns parsed marker and dependency extras with the exact pin/containing extra; `dependency/analysis.py` carries the existing extraction result through source-context creation instead of reducing it to an extra name; `dependency/environment.py` preserves qualifiers explicitly. `dependency/environment_membership.py` checks root/selector first, then returns an explained unresolved condition for selected marked requirements. `ci/consumption.py` copies that condition into its existing `unresolved_conditions` field. Existing report projection carries state/reason/detail through the unchanged v1 report schema; no report-side semantic patch was required.

Regression includes markers that would be false/true under supplied Python settings, compound platform/Python conditions, an unbound matrix value, all-extra selection, another-extra non-selection and an unconditional public-investigation control. This confirms that no host marker evaluation or workflow-setting promotion is occurring. Dependency-requested extras and containing extra remain distinct.

One test assertion initially treated encoded report bytes as text; corrected the assertion to bytes. A grouped test command initially lacked `tests` on its import path for existing report fixtures; corrected invocation to `PYTHONPATH=src:tests` without modifying those fixtures. Touched-file lint exposed pre-existing import ordering; fixed locally. These were test-runner/assertion/format issues, not marker-evaluation failures.

Installed proof: initial no-build-isolation attempt failed because this venv lacks setuptools; retried the declared isolated backend rather than modifying the product environment or dependency contract. Built a wheel and installed it into a new `/tmp/upgradepilot-marker-proof.1Gktr0/venv`. `pip check` passed; module import resolves inside that fresh installation while cwd is outside the checkout; full product suite passes 743/743 and console/module help outputs match. No hosted workflow, live GitHub/LM Studio, target install/execution or experiment suite was run for this deterministic producer repair.

[Retained before/after outcome summary](evidence/2026-10-03-marker-propagation-repair/result.json) records baseline, exact working source/test and wheel hashes, four post-repair states and proof classes. Marked selected requirements now return `unresolved`; the unconditional control remains `supported`; another-extra selection remains `not_established`. Prior raw diagnostic/result remain unchanged for comparison. Public investigation and strict report serialization test confirms the marker/reason survive into human-readable output.

## Post-work learning and handoff

Explain the actual path: raw exact requirement → parsed marker/extras → source context → dependency-owned selection/applicability relation → CI evidence → report. `speed` selection establishes an extra choice, not the truth of `python_version < "3.12"` for the installer. The marker is now preserved and its unproven premise is visible; resolving that premise needs a separately justified environment contract. Compare expectation with verified output, then assess understanding. D/E remain open; fixing the implementation does not establish learner ownership or admit the broader API/source-policy trial.

Closure follow-up: repair published as `aa67a1f5` with local/fetched main aligned. Ali subsequently explicitly requested deferring learning and returning to the larger capability overview/plans. The earlier pending D/E handoff above is superseded by that instruction: D/ownership assessment is deferred rather than passed; E closes with verified engineering result, unevaluated-marker limitation and learning debt preserved. Do not reopen a learning prerequisite or quiz without a relevant user request. Broader capability design remains a separate non-controlling proposal and its accepted source/semantic decisions are not supplied by this repair.
