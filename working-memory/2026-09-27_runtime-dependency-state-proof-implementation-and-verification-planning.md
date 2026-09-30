# Runtime Dependency-State Proof — Implementation and Verification Planning — 2026-09-27

## **Smart Situational Override Rule**

The implementation/proof sequence and stop lines in this planning record are applied under the **Smart Situational Override Rule**. Current evidence may justify expanding, shrinking, reordering, combining, splitting, pausing, or overriding a planned increment/gate when that route is more faithful to the real product responsibility. A material override must be explicit and reconciled with the controlling plan/ADR/owner when their responsibility changes. It cannot invent authorization or proof.


**Status:** R4 PLANNING/DESIGN COMPLETE; retained as the broader implementation/proof-sequence record. R2 semantic boundary and R3 evidence/data-flow architecture are closed. Increments 1–4 have been implemented, verified, learned, and closed in their dedicated cycle records. Increment 5 application integration is now ACTIVE under `working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md`; A0/A1 are DONE and the live route is at the canonical STOP before A2. This record does not itself authorize Build; `MEMORY.md` alone selects the live continuation.

**Controlling plan:** plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md  
**Accepted architecture:** docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md  
**Closed semantic design:** working-memory/2026-09-24_effective-package-manager-semantics-system-design.md  
**Closed evidence design:** working-memory/2026-09-27_effective-package-manager-evidence-source-type-data-flow-design.md  
**Live position owner:** MEMORY.md

UP-SKILL:upgradepilot-planning-design

## 1. R4 responsibility

Turn the accepted runtime dependency-state architecture into a bounded implementation sequence with exact ownership, tests, integration proof, representative real-case verification, pass conditions, and stop lines.

The implementation target remains the first Route-A normal proof:

exact trusted proposed dependency pin
+ exact direct requirements command applicability
+ effective package-manager semantics
+ positively resolved manager environment/destination
+ exact successful command execution
→ proposed requirement satisfied at exact command completion.

Do not implement Route-B log/stdout/artifact acquisition in the first Cycle-1 slice.

## 2. Implementation principles

- preserve existing DependencyCICoverageResult meaning;
- reuse parser-backed StaticCommandLocation and StaticDependencyConsumptionEvidence;
- refactor current runtime-strengthening machinery rather than creating a parallel subsystem;
- parse one package-manager operation once;
- resolve only decision-critical semantic dimensions;
- retain unresolved higher-precedence evidence rather than inventing defaults;
- keep each build increment responsibility-complete and independently testable;
- if implementation exposes a new consequential ownership/contract decision, stop that slice and return to Planning/Design before continuing.

## 3. Ordered Build increments

### Increment 1 — reusable step and exact-command execution evidence — COMPLETED

**Why first:** every later package-manager, setup-python, environment-write, venv, and Route-B path depends on trustworthy execution identity.

Implemented source owners:
- src/upgradepilot/ci/workflow_runtime_correlation.py
- src/upgradepilot/ci/runtime_strengthening.py
- src/upgradepilot/ci/runtime_execution.py
- src/upgradepilot/ci/dependency_exercise.py
- src/upgradepilot/github/workflow_definition.py for provider-accurate unnamed-step identity

Implementation responsibility:
1. derive provider-accurate runtime display identity for admitted unnamed literal user steps without guessing;
2. expose reusable correlated user-step execution assessment for run and uses steps;
3. separate exact command-occurrence execution assessment from user-step success;
4. reuse existing eligibility/structure rules;
5. preserve later-command conservatism until bounded sequential reachability is positively established;
6. migrate dependency_exercise.py to consume the reusable execution evidence while preserving its existing public semantics.

Focused proof owners:
- tests/test_workflow_runtime_correlation.py
- tests/test_ci_runtime_strengthening.py
- tests/test_ci_runtime_correlated_dependency_coverage.py

Required cases:
- explicit named run step still correlates;
- ordinary unnamed run/uses provider display identity correlates;
- setup-python uses step can obtain unmasked successful step evidence;
- continue-on-error true/dynamic prevents positive step interpretation;
- sole/first admitted command can be strengthened under existing shell profiles;
- later command is not automatically strengthened;
- unsupported conditional/loop/background structure remains unresolved/not established;
- existing CI coverage result meanings/regressions stay unchanged.

**Increment pass condition:** reusable step and command execution facts exist, existing coverage behavior remains compatible, and no package-manager-specific logic is introduced into CI execution evidence.

### Increment 2 — static package-manager operation declaration and semantic fact core — COMPLETED

Implemented source owners:
- src/upgradepilot/dependency/package_manager_operation.py
- src/upgradepilot/dependency/package_manager_semantics.py
- src/upgradepilot/dependency/direct_install.py and src/upgradepilot/dependency/environment_selection.py as migrated consumers
- existing parser-neutral command-analysis types remain inputs rather than package-manager owners

Implementation responsibility:
1. replace repeated pip-prefix interpretation with one reusable static package-manager operation declaration;
2. preserve command location and invocation form;
3. admit current pip forms plus the explicit interpreter/global-option forms selected by R2 as needed by the first implementation;
4. introduce shared semantic-resolution provenance/problem representation;
5. introduce the four accepted independent facts:
   - manager environment selection;
   - installation destination;
   - package mutation mode;
   - direct requirement handling;
6. implement command-local decisive semantics first, without fabricating ambient defaults.

Focused proof:
- extend existing pip/direct-install tests where responsibility fits;
- add a focused package-manager runtime-semantics test module when one responsibility no longer fits current files.

Required cases:
- bare pip, python -m pip, explicit interpreter -m pip parsed distinctly;
- pip global --python placement is represented correctly;
- --dry-run produces dry-run mutation mode decisively;
- explicit target/destination is distinct from manager environment;
- no-deps does not exclude direct requirement;
- dynamic/unsupported material values remain semantic problems;
- command atoms are parsed once rather than independently by each resolver.

**Increment pass condition:** one exact package-manager occurrence can feed independent typed semantic resolution without runtime claims or universal config reconstruction.

### Increment 3 — bounded executable/environment/config evidence required by Route A — COMPLETED

Implemented source owners:
- src/upgradepilot/github/workflow_definition.py
- src/upgradepilot/github/workflow_environment.py
- src/upgradepilot/github/process_environment.py
- src/upgradepilot/github/executable_selection.py
- src/upgradepilot/ci/executable_selection.py
- src/upgradepilot/dependency/package_manager_config.py
- src/upgradepilot/dependency/package_manager_semantics.py

Implementation remained demand-driven. The verified pass condition was reached without general venv activation, arbitrary GITHUB_ENV/GITHUB_PATH propagation, universal workflow-env promotion, arbitrary persistent-config acquisition, or general bare-pip provenance; those remain explicit later expansion points rather than incomplete Increment-3 work.

#### 3A. Declarative environment representation

Add workflow/job/step environment mappings only to the bounded GitHub workflow IR surface needed by admitted exact-process variable queries.

Preserve absent/literal/dynamic distinctions and precedence scope. Do not build an expression evaluator or complete Actions environment model.

#### 3B. Executable/interpreter identity

Implement the easiest strongest relations first:
1. supported explicit interpreter path;
2. literal python -m pip interpreter relationship when positive executable provenance is available;
3. setup-python action/PATH relation;
4. bounded venv activation/executable relation;
5. bare pip provenance only where the selected evidence chain closes.

Do not require absolute filesystem paths when the proof has a trustworthy relational environment identity.

#### 3C. Exact-process environment values

Provide a bounded query for one requested variable at one exact command occurrence. Add source adapters only as required by proof cases:
- workflow/job/step env;
- positively executed same-job GITHUB_ENV writes/propagation;
- shell-local assignment/export when admitted;
- provider-established values.

Never use a generic ambient-safe boolean.

#### 3D. Persistent config/defaults

Implement config resolution only when the selected positive proof cannot stop at a higher source.

Prefer explicit, repository-visible, or deliberately disabled/replaced config cases first. Unknown user/system ambient config remains unresolved.

Manager defaults may be used only after higher relevant sources are positively non-overriding/disabled.

Proof owners:
- tests/test_github_workflow_definition.py
- tests/test_github_workflow_command_analysis.py
- new focused process-environment/executable-selection tests when necessary
- package-manager semantics tests from Increment 2

Required close-defeaters:
- step/job/workflow env dynamic;
- effective dry-run environment value;
- unresolved ambient/config source blocks default;
- setup-python update-environment false does not establish PATH relation;
- closer PATH/executable selector supersedes earlier relation;
- arbitrary third-party action effects are not guessed;
- mismatched/dynamic venv paths remain unresolved.

**Increment pass condition:** the first selected Route-A fixture can obtain all required semantic facts from bounded evidence, while ordinary-looking cases with materially unknown ambient sources remain explicitly unresolved.

### Increment 4 — command-derived dependency-state composer — COMPLETED

Expected source owners:
- new focused CI/runtime dependency-state composition module, plausibly src/upgradepilot/ci/dependency_state.py
- existing dependency/source evidence types
- execution and semantic facts from prior increments

Implementation responsibility:
1. create per-command RequirementSatisfiedAtCommandCompletion witness;
2. create explicit not-established/unresolved problem result;
3. enforce exact identity alignment across dependency/source/command/semantic/execution evidence;
4. preserve supporting typed facts and claim limitations;
5. keep existing CI coverage result unchanged;
6. preserve multiple candidate command witnesses separately.

Proof:
- new focused tests for runtime dependency-state composition;
- tests/test_runtime_dependency_contract.py where existing product contract assertions belong.

Required cases:
- exact positive requirements-file pip family produces witness;
- effective dry-run does not produce witness;
- unsupported first-family retargeting does not produce witness;
- unresolved env/config produces unresolved problem, not absence;
- runtime non-success produces not-established;
- identity mismatch fails safely;
- multiple candidate commands do not collapse their environments.

**Increment pass condition:** one exact command-derived package-state witness can be produced with the R2 claim limit and no change to later-use/action semantics.

**Completion evidence:** implemented in `src/upgradepilot/ci/dependency_state.py` with focused proof in `tests/test_ci_dependency_state.py`. Product verification #15 (`36717618416`) is GREEN on exact implementation head `c9edc76e8c3f4e9bb9d58e27ddac3cfbc291a8be`: focused investigation composition 15/15 and deterministic product regression 708/708. The Increment-4 Learning-by-Doing cycle closed with D ownership cleared and no repair required.

### Increment 5 — application integration — ACTIVE; A0/A1/A2 DONE; STOP before Build

Expected owner:
- src/upgradepilot/investigation.py
- presentation/JSON only if a current external contract genuinely requires exposing the new evidence
- no maintainer-action expansion in this cycle

Implementation responsibility:
1. compute runtime dependency-state result from already-acquired workflow/source/runtime evidence;
2. add it as a separate typed investigation field alongside ci_coverage_result;
3. preserve existing consumers unless a new field must be surfaced;
4. do not reinterpret it as compatibility or action permission.

Proof owners:
- tests/test_investigation.py
- tests/test_r6_investigation_ci_integration.py
- relevant end-to-end tests only when their admitted contract reaches this new result.

**Increment pass condition:** the normal investigation path carries the new state proof without changing existing evidence/action meanings.

**Active cycle:** `working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md`. A0 confirmed no `src/`/`tests/` drift after the verified Increment-4 implementation head and no need to reopen prior work. A1 established the continuity/application seam. A2 selected a separate typed runtime dependency-state application result with per-command assessments, CI-owned evaluation in `ci/dependency_state.py`, application orchestration in `investigation.py`, reuse of existing coverage consumptions/runtime correlation, and no aggregate package-state collapse. Build has not started.

## 4. Verification matrix

### Controlled positive fixtures

Use deterministic repository/workflow fixtures where every material premise is explicitly closed. A first positive fixture should make environment/config assumptions deliberate rather than relying on developer-machine ambient state.

Prove:
- exact dependency pin/source;
- exact command/source relation;
- environment identity;
- non-dry-run/apply-changes;
- normal destination;
- direct-requirement handling;
- exact runtime success;
- positive command-completion witness.

### Controlled close-defeaters

At minimum:
- CLI dry-run;
- dry-run from a higher-precedence process source;
- explicit target/retargeting outside the first normal family;
- continue-on-error masking;
- unsuccessful runtime step;
- dynamic/unresolved environment value;
- unresolved config source blocking a default;
- unsupported shell/control flow;
- identity mismatch;
- later command without supported reachability;
- setup-python update-environment false;
- venv --without-pip / mismatched activation where that family is implemented.

Expected result is explicit not-established/unresolved evidence, never fabricated package absence.

### Existing regression suite

Run focused tests after each increment and full deterministic suite before cycle acceptance:

python3 -m unittest discover -s tests -v

Use the repository's current Python/test environment and existing validation rules. Record actual outputs/pass counts only after Build executes them; this planning record does not claim test results.

### Representative public evidence

Use public workflows as pressure/verification, not as fixtures whose result must be positive.

Useful known shapes include:
- explicit clean venv + explicit interpreter + pip --isolated install;
- explicit PIP_CONFIG_FILE=/dev/null package installs;
- setup-python followed by package-manager operations;
- normal-looking commands whose ambient semantics remain unresolved.

A real public case passes verification when UpgradePilot returns the strongest truthful result its evidence supports. An unresolved result is correct when a material source cannot be established.

Do not weaken the proof to force a positive public result.

## 5. First Build slice — completed

The selected first Build slice was **Increment 1 — reusable step and exact-command execution evidence**.

Why it was first:
- it is shared by setup-python, GITHUB_ENV, venv sequences, package-manager commands, and Route B;
- it removed generic execution interpretation from dependency-specific ownership;
- it could be verified without prematurely committing to package-manager source adapters;
- later increments can now consume a stable execution contract rather than duplicating step-success interpretation.

Increment 1 is complete and closed in:
`working-memory/2026-09-27_increment-1_reusable-step-exact-command-execution_lbd-cycle.md`.

The original sequencing warning remains valid for later work: do not jump directly to ambient pip config reconstruction before the package-manager operation/semantic core and demand-driven source needs justify it.

## 6. Build slicing and learning-by-doing rhythm

Each substantive increment follows the current canonical cycle from root `AGENTS.md`:

```text
A0 — reconcile current truth, initialize/reuse the coherent cycle record, seed the living A map
A1 — continuity/recent-work onboarding, then STOP
A2 — upcoming increment responsibility/proof orientation, then STOP before Build
B — implement one coherent bounded increment
Verification — run/inspect the focused and broader proof justified by the increment
D — after sufficient evidence, learn from the actual result and check ownership
E — repair/defer important gaps, close the cycle, identify the next responsibility briefly
C — continuously preserve meaningful progression across A0→E
```

Failed/unavailable verification keeps the responsibility in B/diagnosis/repair or explicit proof debt while C preserves the actual state; do not advance to D on an unproven result.

Do not batch all five implementation increments into one unreviewable change.
## 7. Pass condition for this R4 planning responsibility

**R4 planning responsibility is complete.** Its original Build-readiness conditions were:
- accepted architecture is promoted to ADR-0010;
- controlling runtime-state plan is reconciled;
- ordered implementation increments and owner boundaries are explicit;
- focused/integration/real-case proof obligations are explicit;
- first Build slice is selected;
- no unresolved architectural decision blocks Increment 1;
- prohibited scope and Build stop line are explicit.

These conditions were satisfied before Increment 1 Build authorization. Subsequent implementation progress is evidence recorded in the relevant cycle records and `MEMORY.md`, not a reopening of R4 planning.

## 7A. Increment 1 cycle execution record

Increment 1 execution/learning status is now owned by the dedicated coherent cycle record:

`working-memory/2026-09-27_increment-1_reusable-step-exact-command-execution_lbd-cycle.md`

That record preserves Increment 1 under the then-canonical cadence used when it executed. It remains historical evidence; later increments follow the refined A0/A1/A2 model above.

Recorded Increment-1 outcome:

- A — done;
- B — done;
- C — done/progressively preserved;
- verification gate — green (35 focused + 632 full + exact-head Product verification);
- D — done;
- E — done;
- cycle — closed.

The live continuation after that closure is owned only by `MEMORY.md`; this R4 record keeps the broader sequence and dated implementation evidence.

This R4 record remains the broader implementation/proof-sequence owner and must not compete with the cycle record as the phase-status owner.

## 7B. Increment 2 cycle execution record

Increment 2 execution/learning is closed in:
`working-memory/2026-09-28_increment-2_package-manager-operation-semantic-facts_lbd-cycle.md`.

Recorded outcome:

- A0/A1/A2 — done;
- B — done;
- Verification gate — green via Product verification #10 (15 focused investigation tests + 653 deterministic product tests);
- D — done with real-case ownership learning and small precision-gap repair;
- E — done;
- C — reconciled through closure;
- cycle — closed.

The implementation now provides a shared static pip operation declaration and independent command-local semantic facts/problems without claiming ambient/config closure or resulting package state. Increment 3 remains the next planned technical responsibility, but Build authorization/selection remains owned by `MEMORY.md` and the next cycle.

## 7C. Increment 3 cycle execution record

Increment 3 execution/learning is closed in:
`working-memory/2026-09-29_1556_increment-3_executable-environment-config-evidence_lbd-cycle.md`.

Recorded outcome:

- A0/A1/A2 — done;
- B — done through B1-B5;
- Verification gate — green via Product verification #14 on exact head `29247346d1c1e3ea7074ffd7daf9c53d8c3beeda` (15 focused investigation tests + 699 deterministic product tests);
- D — done with integrated B1-B5 learning using S002/S008/S011 and targeted ownership repair;
- E — done;
- C — reconciled through closure;
- cycle — closed.

The implementation now provides bounded declarative environment observations, exact-process command-local environment evidence, pip persistent-config/default closure for the admitted settings, explicit/setup-python executable-selection evidence, and a verified controlled Route-A fixture that yields all four independent semantic facts while ordinary ambient cases remain unresolved.

Intentionally deferred surfaces such as arbitrary GITHUB_ENV/GITHUB_PATH propagation, general venv activation, arbitrary persistent-config content, and universal PATH/runtime reconstruction remain non-blocking scope boundaries rather than unfinished Increment-3 work.

The next planned technical responsibility is **Increment 4 — command-derived requirement-state composition**: combine exact dependency/source applicability, the independent semantic facts, and exact successful command execution into a separate command-completion state witness. Application integration remains a later increment. Build authorization and the next cycle's A0/A1/A2 remain owned by `MEMORY.md`.

## 8. Stop line / prohibited scope

For any increment that has not been explicitly authorized for Build:
- do not modify product source or tests merely because it appears next in this sequence.

During the selected Cycle-1 Build responsibilities:
- no generic job-log/stdout/artifact ingestion;
- no Conditional Cycle 2 selection;
- no universal environment/config reconstruction;
- no generic shell/runner simulator;
- no maintainer-action semantic expansion;
- no later-use/compatibility claim;
- no broad pip/uv option catalog merely for completeness;
- no weakening of fail-closed behavior to increase real-case positivity.

If a Build increment uncovers a new consequential contract/owner decision, pause that increment, record the evidence, return to Planning/Design, then resume Build only after reconciliation.
