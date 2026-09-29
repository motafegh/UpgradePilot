# Increment 2 — Static Package-Manager Operation Declaration and Semantic-Fact Core — Learning-by-Doing Cycle

## Smart Situational Override Rule

This cycle began under the previous single-A/B+C cadence. During its pre-B orientation, the project refined the canonical Learning-by-Doing model to A0 → A1 → A2 → B → Verification → D → E with C continuous across the whole cycle. On resumption, this existing record is retained rather than creating a duplicate cycle record; the new governance is applied from a deliberate A0 re-entry. The Smart Situational Override Rule permits this transition because no Increment-2 Build began. The rule does not create Build authorization or weaken evidence truth.

**Date:** 2026-09-28  
**Cycle status:** CLOSED — A0/A1/A2/B/D/E complete; Verification/Evidence gate GREEN; C reconciled through closure  
**Primary operation:** Increment-2 cycle closed after verified Build, evidence-backed ownership learning, and E gap repair/handoff  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**R4 implementation sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Live position owner:** `MEMORY.md`

UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory

## Canonical cycle status

```text
A0 — DONE: current main/owners/source/tests reconciled; existing cycle record reused; living A map seeded
A1 — DONE: Ali confirmed the continuity model; no material continuity gap surfaced
A2 — DONE: Ali demonstrated the package-manager declaration boundary and dry-run mutation-mode blocker; pre-B gate cleared
B — DONE: bounded package-manager operation declaration + command-local semantic-fact core implemented and existing pip consumers migrated
Verification gate — GREEN: Product verification #10 succeeded on exact run head `e838fa656964a898c037cca6ef0d390983f106ad`; full deterministic regression ran 653 tests including the new semantic core and both migrated consumers
D — DONE: real source/flow/proof learning completed; only small precision gaps surfaced and were repaired
E — DONE: gaps repaired, proof/non-proof consolidated, next responsibility identified
C — DONE: meaningful progression reconciled through cycle closure
```

## Why no separate new plan

No additional plan is needed. The controlling runtime dependency-state plan already owns the program responsibility, ADR-0010 owns the accepted cross-layer architecture, and the R4 implementation record already defines Increment 2's implementation responsibility, proof cases, pass condition, and next increments.

A second plan would duplicate ownership rather than clarify it. This record therefore owns only the real Increment-2 cycle progression and learning/evidence history.

## Governance refinement interruption and resumption

While this cycle was stopped before Build, Ali and the assistant identified that the old single-A cadence did not model fresh-session reorientation, user continuity onboarding, whole-cycle C preservation, or E handoff cleanly enough. The canonical governance was refined and recorded in `working-memory/2026-09-28_lbd-cycle-governance-refinement.md`.

Resumption rule:

```text
reuse this existing cycle record
→ execute refined A0 current-state reconciliation and seed/update the living A map
→ execute A1 continuity/recent-work onboarding
→ STOP at A1 continuity gate
→ execute A2 upcoming-responsibility orientation using the historical material below as input
→ STOP at A2 pre-B gate
→ only then may B begin when authorized
```

No Increment-2 product source or tests were changed before this governance refinement.
## Refined A0 — current-state reconciliation + cycle initialization — DONE

### Current-state evidence checked

A0 re-read the current canonical/active surfaces needed for Increment 2:

- root `AGENTS.md`, `OPERATING_GUIDE.md`, and the Learning-by-Doing / working-memory Skills after the 2026-09-28 governance refinement and root-context compaction;
- current `MEMORY.md`; 
- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`; 
- `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`; 
- accepted `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`; 
- this existing Increment-2 cycle record and the recent governance-refinement/compaction records;
- current source seam: `src/upgradepilot/dependency/pip_command.py`, `direct_install.py`, and `environment_selection.py`; 
- current focused tests: `tests/test_direct_install_declaration.py` and `tests/test_project_environment_selection.py`; 
- recent `main` commit history.

### Freshness / implementation reconciliation

The verified Increment-1 implementation head remains `a47923ee778b0984966bc09b8d01169205d0f7f9`. A compare from that commit to current `main` found **no changes under `src/`, `tests/`, `experiments/`, or `tools/`**. All later changes are governance/planning/working-memory reconciliation rather than product implementation.

Therefore:

```text
Increment 1 implementation truth remains intact
+ Increment 2 still has no product Build
+ current source seam is unchanged
+ no fresh implementation evidence invalidates the selected Increment-2 route
```

### Reconciliation discovered during A0

The controlling runtime-state plan and the active R4 implementation-sequence record still contained several references to the superseded `A → B → C → D → E` / `B+C` cadence. Their **technical responsibilities and proof obligations were still correct**, but their process language conflicted with current governance.

A0 reconciled only that process vocabulary:

- `a512ec1` — aligned `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md` with A0/A1/A2/B/Verification/D/E + continuous C;
- `84edbe0` — aligned the R4 continuation rhythm while preserving Increment-1 historical cadence as history.

No semantic/architecture/build scope was changed by this reconciliation.

### A0 conclusion

No contradiction requires replanning or redirecting Increment 2. The selected responsibility remains:

> parse one package-manager operation occurrence once and expose independent typed semantic resolution for manager environment selection, installation destination, package mutation mode, and direct requirement handling, without runtime claims or universal config reconstruction.

The existing cycle record is reused rather than creating a duplicate record, as already decided during the governance transition.

## Living A-phase orientation / learning map

This map is a living cycle aid, not a second plan. A1 may add/remove items when Ali's continuity gaps become visible.

### A1 — continuity / recent-work onboarding topics

- [x] Reconnect Increment 1's closed result: exact-command successful execution evidence exists, but it does not establish package-manager meaning or resulting package state.
- [x] Reconnect the governance interruption: Increment 2 started orientation but **no Build began**; governance was refined before product work continued.
- [x] Explain what changed since that point: LbD A0/A1/A2 model + continuous C, root governance compaction, and plan/R4 cadence reconciliation only.
- [x] Re-establish current live position: Increment 2 remains selected; technical scope/ADR/plan did not change.
- [x] Reconnect the current source seam: `pip_command.py` recognizes bounded pip prefixes; `direct_install.py` and `environment_selection.py` consume/reinterpret pieces independently.
- [x] Surface any continuity gaps/questions from Ali and record them before A2 — none surfaced at the A1 gate.

### A2 — upcoming responsibility orientation topics (do not execute before A1 gate)

- [x] Why one dependency-owned package-manager operation declaration should replace repeated prefix interpretation.
- [x] Invocation identity/forms that matter: bare pip, `python -m pip`, explicit interpreter relation, and pip global `--python` placement.
- [x] The four independent semantic facts and why they must not collapse into one `valid install` boolean.
- [x] Shared bounded semantic provenance/problem representation and fail-closed unresolved material values.
- [x] Command-local decisive semantics first: especially `--dry-run`, target/destination distinctions, and `--no-deps` direct-requirement meaning.
- [x] Exact Increment-2 pass condition, proof cases, non-goals, and ownership depth.

### A-phase understanding gaps

None are assumed at A0. A1 must discover them from Ali's actual questions/reasoning rather than infer them from prior approval.
## Refined A1 — continuity / recent-work onboarding — DONE

Ali confirmed both continuity propositions:

1. Increment 1 proves successful execution of the exact command occurrence, not resulting package state.
2. Increment 2 has not entered Build; subsequent work before this point was governance/reconciliation while the technical responsibility remained unchanged.

No material A1 understanding gap was identified. The cycle therefore advances to A2 only.
## Refined A2 — upcoming responsibility orientation — DONE

Ali's pre-B reasoning:

1. A shared package-manager operation core avoids repeated/duplicate parsing across downstream layers, lets different consumers reuse one result, and makes ownership/boundaries clearer.
2. For a successful command containing `--dry-run`, the decisive semantic blocker is **package mutation mode**: the operation can be structurally valid and successfully executed while still being explicitly non-mutating, so later package-presence inference must be blocked.

Clarification recorded: `--dry-run` is not itself a malformed/structural command problem. It is valid package-manager semantics whose mutation-mode fact resolves to a non-mutating state.

No material A2 ownership gap remains for entering the bounded Build responsibility. B has not started and still requires normal Build authorization/continuation.
## Cycle responsibility

Move UpgradePilot from repeated narrow package-manager prefix interpretation toward one reusable static package-manager operation declaration that can feed independent package-manager semantic facts.

The intended progression is conceptually:

```text
parser-neutral StaticCommandOccurrence
→ one dependency-owned package-manager operation declaration
→ independent semantic facts
   ├─ manager environment selection
   ├─ installation destination
   ├─ package mutation mode
   └─ direct requirement handling
```

The Increment-2 pass condition remains:

> one exact package-manager occurrence can feed independent typed semantic resolution without runtime claims or universal config reconstruction.

## B — real bounded Build / implementation — DONE, verification pending

### Implementation result

Build moved the package-manager responsibility from a narrow pip-prefix helper to two explicit dependency-owned source owners:

```text
StaticCommandOccurrence
→ package_manager_operation.py
   → PackageManagerOperationDeclaration | PackageManagerOperationProblem
→ package_manager_semantics.py
   → independent semantic facts/problems
```

#### 1. Static operation declaration

`src/upgradepilot/dependency/package_manager_operation.py` now owns bounded static pip-install operation identity.

It preserves:

- manager and operation;
- invocation form (`pip`/`pip3` executable versus Python `-m pip`);
- launcher and explicit Python interpreter token when applicable;
- pip global arguments required by the admitted first surface, including `--python` and `--isolated`;
- install-operation arguments;
- canonical `StaticCommandLocation`.

Supported explicit interpreter-path forms such as `/opt/venv/bin/python3.12 -m pip install ...` are admitted. Unsupported/dynamic recognizable prefixes produce explicit operation problems rather than textual fallback.

#### 2. Independent command-local semantic facts

`src/upgradepilot/dependency/package_manager_semantics.py` now owns the shared bounded semantic result/provenance model and four independent fact families:

- `ManagerEnvironmentSelectionFact`;
- `InstallationDestinationFact`;
- `PackageMutationModeFact`;
- `DirectRequirementHandlingFact`;
- plus `PackageManagerSemanticProblem` when the dimension cannot be established safely.

Command-line decisive cases implemented in this increment include:

- pip global `--python` → explicit manager-environment selection;
- `--target`, `--user`, `--prefix`, `--root` → typed non-default installation destinations;
- `--dry-run` → `PackageMutationModeFact(mode="dry_run")`; 
- `--only-deps` → direct requirement excluded;
- `--no-deps` → explicitly recorded as **not** excluding the direct requirement, while effective handling remains unresolved until lower semantic sources are closed.

When no decisive command-line fact exists, the resolver preserves the next required source (normally exact process environment) instead of fabricating manager defaults.

Dynamic/unsupported command-line material fails closed. A later Build review tightened this further so unclassified dynamic CLI material blocks an otherwise visible same-dimension winner when it could still alter that semantic dimension.

#### 3. Existing consumers migrated

`direct_install.py` and the pip branch of `environment_selection.py` now consume `PackageManagerOperationDeclaration.operation_arguments` instead of owning/repeating pip-prefix parsing.

The superseded `src/upgradepilot/dependency/pip_command.py` helper was removed after migration. A dependency-package scan checked all 16 active dependency Python files and found no remaining `pip_command` / `parsed_pip_install_arguments` references.

The existing uv project-selection interpretation in `environment_selection.py` remains unchanged. Increment 2's admitted first implementation responsibility is the repeated pip-prefix seam and first pip semantic family; this Build does not silently widen into a full uv effective-semantics rewrite.

### Focused test surface added/extended

- added `tests/test_package_manager_semantics.py` for operation parsing and the four command-local semantic dimensions;
- extended `tests/test_direct_install_declaration.py` for pip global `--python` migration;
- extended `tests/test_project_environment_selection.py` for explicit interpreter-path `python -m pip` migration.

Important cases represented in tests include:

- bare pip versus Python-module invocation;
- explicit interpreter path;
- pip global `--python` and dynamic target;
- explicit `--dry-run`; 
- no fabricated `apply_changes` default when lower sources remain unknown;
- target/user/prefix/root destination facts;
- `--no-deps` versus `--only-deps`; 
- dynamic/unsupported material values;
- one declaration feeding all four semantic resolvers;
- dynamic CLI material blocking otherwise visible semantic winners;
- empty inline destination values such as `--target=`;
- non-install pip global commands such as `pip --version` not being misclassified as unresolved installs.

### Build review / repairs

Two source-review issues were found and repaired before B closure:

1. otherwise-visible destination/mutation/direct-handling facts could have won despite unrelated dynamic CLI material that might alter the same dimension; resolvers now fail closed first;
2. unsupported-looking pip global flags on non-install commands and empty inline destination values had imprecise classification; both boundaries now classify more accurately.

### Build scope and head

Build-ready base: `909b739c00ffa1a7a9404fa7b3efb17af1e1593f`  
Final B implementation head: `a5595370b29a88caa4bdd3f7a875fae819a57c25`

The 13-commit Build diff is limited to eight intended files:

```text
modified  src/upgradepilot/dependency/direct_install.py
modified  src/upgradepilot/dependency/environment_selection.py
added     src/upgradepilot/dependency/package_manager_operation.py
added     src/upgradepilot/dependency/package_manager_semantics.py
removed   src/upgradepilot/dependency/pip_command.py
modified  tests/test_direct_install_declaration.py
added     tests/test_package_manager_semantics.py
modified  tests/test_project_environment_selection.py
```

No unrelated product responsibility was intentionally changed.

### Proof boundary at B handoff

B establishes **implementation state only**. No focused or broader test command has yet been executed in the Verification/Evidence gate, so this result is not yet accepted as green.

Even after verification, Increment 2 is intended to establish only:

> one exact supported package-manager occurrence can feed independent typed command-local semantic resolution with explicit provenance/problems.

It still does not establish effective ambient/config semantics, command execution, resulting package state, later use, compatibility, or maintainer-action permission.

UP-SKILL:upgradepilot-build-implement
## Verification / Evidence gate — GREEN

Ali manually dispatched **Product verification #10** (`run 36463198913`). GitHub reports:

- event: `workflow_dispatch`;
- status: `completed`;
- conclusion: `success`;
- run head: `e838fa656964a898c037cca6ef0d390983f106ad`;
- one product job, `Installed package and deterministic product tests`, completed successfully;
- checkout/setup/install/CLI/focused-investigation/full-regression steps all concluded `success`.

### Exact implementation identity

The run head is two commits ahead of final B implementation head `a5595370b29a88caa4bdd3f7a875fae819a57c25`. The only intervening files are:

```text
MEMORY.md
working-memory/2026-09-28_increment-2_package-manager-operation-semantic-facts_lbd-cycle.md
```

Therefore the Product verification run tested the exact Increment-2 product source/test implementation with only state-record updates on top; no product source/test changed between B head and the verified run head.

### Test evidence

The workflow installed UpgradePilot in a fresh Python 3.12 virtual environment and verified installed CLI entry points.

The focused investigation composition step passed **15 tests**.

The full deterministic product regression passed:

```text
Ran 653 tests
OK
```

The full regression log explicitly shows successful execution of the new/migrated Increment-2 cases, including:

- package-manager operation parsing for bare pip, `python -m pip`, explicit interpreter path, pip global `--python`, unsupported/global/non-install classification;
- semantic tests for explicit dry-run, no fabricated `apply_changes` default, manager-environment/destination independence, target/user/prefix/root destinations, `--no-deps`, `--only-deps`, dynamic CLI fail-closed behavior, empty inline destination, and one declaration feeding all four dimensions;
- direct-install migration through pip global `--python`;
- project-selection migration through explicit interpreter-path `python -m pip`;
- existing uv project-selection regression cases.

### Focused-first procedural note

The live handoff had described running the three focused Increment-2 families first and then the broader regression. Product verification #10 did not invoke those three files as a separate command before the full suite. However, the full deterministic discovery executed those exact test cases individually and they all passed, followed by the complete 653-test green result.

Under the Smart Situational Override Rule, a separate duplicate focused rerun is not required here: it would add diagnostic convenience if failures existed, but it would not materially strengthen the already observed success evidence. The intended proof responsibilities—new semantic behavior, migrated-consumer regression, fresh installed-package execution, and broad deterministic regression—are all covered by the successful workflow.

### Verification conclusion

Increment 2 satisfies its verification gate for the current bounded claim:

> one exact supported package-manager occurrence can feed independent typed command-local semantic resolution with explicit provenance/problems, while existing migrated consumers continue to pass the deterministic product suite.

This verification does **not** establish ambient process-env/config semantics, final effective defaults, command-derived package-state satisfaction, later persistence/use, compatibility, or maintainer-action permission.
## D learning extension — real product-simulation anchors

During D, Ali requested that ownership learning use preserved real product-simulation cases and exact data-flow tracing rather than only synthetic commands.

Selected anchors:

- **S011 — Dictare MLX optional-extra CI coverage:** real inspected workflows use `pip install -e .[dev]` while the affected runtime family requires the `mlx` optional extra. This is the strongest current real example for shared operation parsing feeding project-environment selection while effective package-manager semantics remain independently unresolved.
- **S002 — Kubernetes Dashboard Token API / httpx:** preserved workflow uses `python -m pip install --no-cache-dir --upgrade pip -r requirements.txt`, giving a real Python-module pip invocation plus direct requirements-file consumption.
- **S008 — CARLA OpenCV Python-3.6 artifact fallback:** retained as an evidence-source boundary example. Its documented pip3 installation path is real repository evidence, but it is not automatically a GitHub Actions run-step occurrence, so the workflow command parser must not be assumed to own it.

D should explicitly distinguish:

```text
workflow run-step acquisition/parsing
→ StaticCommandOccurrence
→ shared PackageManagerOperationDeclaration
→ existing consumers (direct requirements / project selection)
AND/OR
→ Increment-2 semantic fact resolvers
```

The semantic-fact core is currently a reusable dependency-layer substrate; final effective ambient/config resolution and package-state composition remain later increments.
## D governance refinement — real-case teaching priority

During D, Ali established a reusable teaching preference that is now canonical governance:

```text
existing real project / product-simulation case
→ suitable external real-world case when practical and reliably inspectable
→ synthetic / constructed example only as fallback
```

This priority applies to teaching/examples, not to product-proof authority: a realistic teaching case does not automatically expand the current cycle's admitted proof boundary.

Canonical owners updated:

- root `AGENTS.md` D cadence;
- `OPERATING_GUIDE.md` §2.6;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` D procedure.
## D ownership-check findings

Ali demonstrated the core Increment-2 architecture and uncertainty model with only two material refinements needed before E:

- For `pip --python /venv/python install --target vendor --no-deps -r requirements.txt`, manager environment and installation destination are command-line decisive; mutation mode remains unresolved without lower-source evidence, and `--no-deps` is known not to exclude the direct requirement but effective direct-requirement handling remains unresolved until lower semantic sources are closed.
- Dynamic material such as `${{ matrix.extra_flags }}` must preserve uncertainty because its exact value could introduce same-dimension semantics; later matrix/static-value support would help only when the exact command occurrence's effective value can actually be established.
- The shared `StaticCommandOccurrence → PackageManagerOperationDeclaration → independent facts/problems` architecture was correctly understood as avoiding duplicate parsing/ownership and preserving proposition-level provenance instead of collapsing evidence into one boolean.
- In S011, the decisive CI-coverage gap is `.[dev]` versus the affected `.[mlx]` environment. Unresolved manager-environment semantics are a separate proposition and are not the reason the workflow fails to establish MLX coverage.
- In S002, successful `python -m pip ... -r requirements.txt` execution plus direct requirements consumption still lacks effective executable/environment, destination, mutation-mode/default, and direct-handling closure before package-state satisfaction can be composed.

Ali also identified that the compact real-case D trace intentionally omitted environment/config traversal. This is correct: Increment 2 produces semantic facts/problems and blocking-source information; Increment 3 owns bounded executable/process-environment/config evidence and default closure, and Increment 4 owns the command-derived requirement-state composer.
## D — evidence-backed learning / ownership — DONE

D used the verified implementation plus real product-simulation anchors S011 and S002, with S008 as an evidence-source boundary example.

Ownership result:

- Ali correctly understood the shared declaration / independent-fact architecture, proposition-level provenance, and fail-closed treatment of dynamic material;
- the only material precision gaps were distinguishing command-line-known dimensions from lower-source unresolved dimensions, and separating S011's `.[dev]` versus `.[mlx]` coverage failure from manager-environment uncertainty;
- those gaps were corrected during D and recorded in this cycle;
- no remaining ownership gap blocks closure.

## E — gap repair + cycle closure / handoff — DONE

### Repaired / consolidated understanding

For the representative command:

```text
pip --python /venv/python install --target vendor --no-deps -r requirements.txt
```

Increment 2 can decide manager environment (`--python`) and installation destination (`--target`) from command-line evidence. It cannot infer `apply_changes` merely from the absence of `--dry-run`, and `--no-deps` proves only that transitive dependencies are suppressed—not that all effective direct-requirement semantics are closed. Lower-precedence sources remain an Increment-3 responsibility.

For S011, the bounded CI-coverage conclusion is independently:

```text
workflow installs .[dev]
!= affected .[mlx] optional environment formed
```

Manager-environment uncertainty is a separate proposition, not the cause of that coverage failure.

### What Increment 2 established

- one dependency-owned static pip-install operation declaration replaces repeated pip-prefix interpretation;
- command location, invocation form, launcher/interpreter relation, admitted pip-global arguments and operation arguments are preserved;
- manager environment selection, installation destination, mutation mode and direct-requirement handling are independent typed semantic dimensions;
- command-line decisive facts carry provenance;
- materially unresolved/unsupported semantics become explicit problems rather than guessed defaults;
- existing direct-requirements and project-selection consumers now reuse the shared operation declaration;
- the superseded `pip_command.py` owner is removed;
- Product verification #10 is GREEN with fresh installation/CLI checks, 15 focused investigation tests and 653 deterministic product tests.

### What Increment 2 did not establish

- workflow/job/step process-environment precedence;
- executed `GITHUB_ENV` propagation or shell-local environment effects;
- setup-python/PATH, virtual-environment or bare-pip executable provenance beyond command-local declaration;
- persistent pip/uv configuration and final manager-default closure;
- universal pip/uv option semantics;
- resulting package state / `RequirementSatisfiedAtCommandCompletion`;
- later package persistence/use, compatibility or maintainer-action permission.

### Residual debt / limitations

No Increment-2 blocker remains. Ordinary-looking package-manager commands may correctly stay unresolved until Increment 3 closes the exact executable/environment/config evidence required by the selected Route-A proof. The uv effective-semantics family remains outside this first pip-focused Increment-2 implementation.

### Next responsibility

**Increment 3 — bounded executable/environment/config evidence required by Route A.**

Why next, briefly:

```text
Increment 2 now tells us which semantic source is still blocking
→ Increment 3 acquires/resolves only the bounded executable/process-env/config evidence needed
→ defaults become usable only after higher-precedence sources are closed
→ Increment 4 can then compose command-derived requirement state
```

Do not perform Increment-3 orientation or Build inside this closed cycle. Its next substantive work begins with a fresh A0/A1/A2 cycle.

**Cycle closure date:** 2026-09-29
## Historical pre-refinement A orientation — input to refined A1/A2

### 1. Starting implementation truth

Increment 1 already established the reusable execution boundary:

```text
static/runtime step identity
→ correlated successful user-step execution
→ exact-command structural eligibility
→ exact-command execution evidence
```

That proves a bounded proposition that an exact command occurrence executed successfully. It deliberately does not prove what pip/uv effectively did or what package state resulted.

### 2. Current source seam

#### `src/upgradepilot/dependency/pip_command.py`

The current helper `parsed_pip_install_arguments(...)` recognizes bounded pip install prefixes and returns the remaining typed command atoms.

Current admitted shapes include:

```text
pip install ...
pip3 install ...
python -m pip install ...
python3 -m pip install ...
```

Its current result is essentially:

```text
install arguments | not this shape | materially unresolved prefix
```

It does not preserve a reusable typed operation identity such as invocation form, explicit interpreter relation, pip global-option placement, or semantic facts.

#### `src/upgradepilot/dependency/direct_install.py`

This consumer uses the pip helper and then independently interprets `-r/--requirement` arguments against an already-established repository dependency-source path.

Its proof stops at visible static declaration. It does not establish execution, mutation, installed version, or package state.

#### `src/upgradepilot/dependency/environment_selection.py`

This consumer also uses the pip helper for local-project pip installs while separately interpreting uv command identity and uv-specific selectors/options.

This exposes the architectural pressure directly: package-manager operation identity is partly reconstructed inside different consumers instead of being parsed once into one dependency-owned declaration.

### 3. What Increment 2 is fixing

The problem is not merely “support `--dry-run`.”

If each downstream consumer independently asks:

```text
is this pip?
is it python -m pip?
where is install?
are there pip global options?
which arguments belong to the operation?
```

then package-manager identity and invocation semantics can drift across consumers.

ADR-0010 therefore requires:

> Parse one package-manager operation once.

The package-manager declaration should preserve enough static identity for later semantic resolvers without becoming a universal shell parser or universal pip/uv configuration model.

### 4. The four independent semantic facts

These are deliberately separate because proving one must not accidentally prove the others.

#### Manager environment selection

Question:

> Which Python/package-manager environment does this invocation select or relate to?

Examples of relevant static evidence can include an explicit interpreter form or pip's global `--python` relation.

This is not automatically the same proposition as the final installation destination.

#### Installation destination

Question:

> Where is the package state being written or targeted?

Examples later include explicit destination-changing mechanisms such as target/user/root/prefix-style behavior where admitted.

A command can select one manager/interpreter environment while directing installation somewhere else, so this fact must remain independent.

#### Package mutation mode

Question:

> Does the effective operation actually mutate/synchronize package state, or is it non-mutating?

The decisive first example is explicit `--dry-run`.

```text
exact command executed successfully
+
effective dry-run
≠ package state changed
```

This is why Increment 1 execution evidence alone cannot support the later requirement-state proposition.

#### Direct requirement handling

Question:

> Does the operation still include the exact direct requirement that UpgradePilot is reasoning about?

This must distinguish direct-package treatment from transitive-dependency treatment. For example, pip `--no-deps` suppresses dependency installation; it does not by itself exclude the explicitly requested direct requirement.

### 5. What “independent facts” buys us

Avoid one giant boolean such as:

```text
safe_install = true
```

Instead later composition can reason from explicit propositions:

```text
operation identity known
AND mutation mode supports state change
AND direct requirement is included
AND manager environment is sufficiently established
AND destination is sufficiently established
AND exact command execution is supported
→ candidate command-completion requirement-state witness
```

That final composition belongs to a later increment, not this one.

### 6. Expected Increment-2 Build responsibility after the gate

If the A gate is cleared and Build is explicitly entered, the already-admitted plan expects us to:

1. replace repeated pip-prefix interpretation with one reusable static package-manager operation declaration;
2. preserve command location and invocation form;
3. support the bounded invocation forms required by the accepted first family, including explicit-interpreter/global-option forms as justified;
4. introduce shared semantic-resolution provenance/problem representation;
5. introduce the four independent facts;
6. implement command-local decisive semantics first;
7. preserve dynamic/unsupported material inputs as semantic problems instead of guessing.

Required proof cases already exist in the R4 plan, including bare pip, `python -m pip`, explicit interpreter forms, pip global `--python`, `--dry-run`, destination distinction, `--no-deps`, unresolved material values, and parse-once behavior.

### 7. Explicit non-goals for Increment 2

Increment 2 does **not** yet solve:

- workflow/job/step environment precedence;
- `GITHUB_ENV` propagation;
- setup-python/PATH executable provenance;
- virtual-environment activation provenance;
- ambient `PIP_*` / `UV_*` process variables;
- user/system/project persistent config reconstruction;
- universal pip/uv option coverage;
- resulting package-state proof;
- later package exercise/compatibility;
- maintainer-action permission;
- generic job-log/stdout/artifact acquisition.

Those remain later responsibilities, principally Increment 3 and Increment 4.

### 8. Professional engineering ownership target

**Primary:** code/system understanding — own the boundary between parser-neutral command evidence, one package-manager operation declaration, and downstream semantic facts.

**Secondary:** design/system judgment — understand why operation identity is parsed once while semantic propositions remain independent rather than collapsing into one “effective install” object.

**Required depth:** must own the responsibility/proof boundaries and normal data flow; exact class/function names and full pip/uv option catalogs remain recognize/lookup-level.

## Historical pre-refinement understanding gate — superseded by refined A1/A2 gates

Before B begins, Ali should be able to reason about these two points:

1. Why is a successful exact command from Increment 1 still insufficient to say the proposed dependency became present?
2. Why should “manager environment”, “installation destination”, “mutation mode”, and “direct requirement handling” remain separate facts instead of one combined “pip install is valid” result?

No product source/test Build should begin until this gate is cleared or a justified Smart Situational Override is explicitly recorded.
