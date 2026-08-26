# Working Memory — B2 R7 Findings Register

**Date:** 2026-08-26  
**Status:** ACTIVE DURING R7; FINDINGS ACCUMULATE UNTIL FINAL DISPOSITION
**Execution branch:** `main`  
**Parent R7 record:** `2026-08-26_B2-R7-acceptance-cleanup-and-baseline-closure.md`

## 1. Purpose

This register collects bounded R7 edges, bugs, design pressure, proof risks, and cleanup candidates discovered while R7 review and cleanup progress. R7.0–R7.4 were remote-depth review; Ali changed the execution mode before R7.5 so remaining implementation and validation proceed locally.

The purpose is to avoid two bad extremes:

```text
find one edge
→ patch immediately
→ churn architecture before the full R7 picture is visible
```

and:

```text
find one edge
→ mention it in chat
→ lose the reasoning/evidence before final closure
```

Normal rule:

```text
observe finding
→ establish exact current behavior from source/tests/real evidence
→ classify risk
→ record cause + consequence + possible repair shape + regression pressure
→ continue R7 when non-blocking
→ disposition all queued findings together before the final executable candidate is frozen
```

A finding may interrupt the current R7 slice immediately only when evidence establishes a hard blocker such as false support, proof strengthening/uncertainty erasure, authority/provenance conflation, a broken normal production route, contradiction with an admitted current real case/specification, or corruption that makes later R7 evidence unreliable.

Before R7.8 freezes the final executable candidate, every queued finding must receive one explicit disposition:

```text
FIX IN R7
ACCEPT AS KNOWN BOUNDED LIMITATION
SCHEDULE FOLLOW-UP WITH OWNER/TRIGGER
REJECT / NOT REQUIRED BY CURRENT PRODUCT RESPONSIBILITY
```

If a queued finding is promoted to `FIX IN R7`, implement it in the owning R7 cleanup slice, add the smallest discriminating regression pressure, and include the resulting source/test revision in the final R7.9 local validation bundle.

---

## F-001 — Mixed safe + unresolved shell segments collapse to one unresolved R3 step

**Discovered:** R7.1 remote focused source/test audit  

**Current disposition:** ACCEPT AS KNOWN BOUNDED LIMITATION — TRIGGER-BASED REOPEN ONLY

**Current blocker:** NO  
**Risk class:** conservative under-reporting / granularity loss  
**Owning area if later fixed:** R3 project-environment selection contract, then R6 consumption of that contract

### Exact current cause

R3 parses one GitHub Actions `run:` block into bounded shell segments and separately gathers parsed declarations and unresolved details. But `ProjectEnvironmentSelectionObservation` exposes one step-level `state` for the whole `RunStepDefinition`.

Current shape:

```text
for each shell segment:
    parse segment
    append safe declaration(s)
    append unresolved detail(s)

if ANY unresolved detail exists:
    overall observation.state = unresolved
    retain declarations, but the whole run step is unresolved
```

R6 then consumes that aggregate state:

```text
R3 not_observed
→ no contribution

R3 unresolved
→ preserve one unresolved CI-consumption item
→ do not evaluate retained declarations through R4/R5

R3 observed
→ evaluate each declaration through R4/project-source membership → R5
```

Example:

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

Conceptually R3 can identify:

```text
segment 0 → readable literal docs declaration
segment 1 → dynamic selector → unresolved
```

but the final observation is `unresolved`, so R6 does not evaluate the safe docs declaration. Reversing segment order does not change the limitation. Separate GitHub Actions `run:` steps remain independent and are not affected.

### Consequence and proof classification

The current system can under-report a positive static fact:

```text
independently safe selected-root witness
→ could become supported consumption

another unresolved segment in same run step
→ whole observation unresolved
→ positive fact not derived
```

This is currently conservative under-reporting, not proof strengthening: possible support becomes unresolved rather than uncertainty becoming supported or `not_established`.

### Unsafe shortcut rejected

R6 must not simply evaluate every retained declaration from an unresolved observation. Example:

```bash
uv sync --all-extras --no-extra mlx
```

The positive `--all-extras` declaration can be retained while the same segment is unresolved because of the negative selector. Processing retained declarations blindly could manufacture false support.

### Suggested repair direction if selected later

Preserve the granularity R3 already parses:

```text
ProjectEnvironmentSelectionObservation
└── segment observations
    ├── segment_index
    ├── state = observed | not_observed | unresolved
    ├── reason/detail
    └── declarations owned by that segment
```

Then R6 consumes each segment independently. Semantic ownership remains in R3; R6 must not guess which declarations inside an unresolved step are safe.

### Suggested regression fixtures

1. Safe before unresolved:

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

Expected: independently evaluated docs result + unresolved dynamic result, both preserved.

2. Unresolved before safe: same evidence meaning as fixture 1; order must not affect preservation.

3. One tainted segment:

```yaml
- run: uv sync --all-extras --no-extra mlx
```

Expected: unresolved only; no support manufactured from retained `--all-extras`.

4. Separate `run:` steps: unresolved first step does not suppress an independently readable later docs step.

### R7.3 S001 pressure

Exact Pydantic S001 CI evidence does **not** trigger this edge. The real positive docs selector is a standalone literal step:

```text
uv sync --all-packages --group docs
```

No admitted S001 workflow inspected so far establishes a need to preserve one safe and one unresolved uv selector from the same `run:` block. F-001 therefore remains non-blocking and trigger-based after S001 pressure.

### R7.5 final disposition

R7.5 accepts this as a known bounded limitation and makes no source/test change. The observed
failure mode is conservative under-reporting, not proof strengthening; S001 does not contain the
mixed safe+unresolved shape; and no other admitted current workflow established a product need
for a new segment-result contract. Implementing the understood repair direction without that
trigger would add durable R3/R6 structure for a hypothetical responsibility.

Reopen F-001 only when admitted real workflow evidence contains one safe literal selector and
one materially unresolved selector in the same `run:` block and preserving both independently is
needed for a supported UpgradePilot decision. At that point, keep segment semantics in R3 and do
not let R6 infer that declarations retained by an unresolved segment are safe.

---

## F-002 — Unavailable project-root evidence can disappear before CI consumption classification

**Discovered:** R7.2 remote normal investigation/CI orchestration trace  
**Current disposition:** FIX IN R7 — IMPLEMENTED LOCALLY TO FOCUSED/NEAREST-INTEGRATION DEPTH
**Current blocker:** PROOF-CALIBRATION PATH CLOSED LOCALLY; FINAL BROAD R7 ACCEPTANCE PENDING
**Risk class:** proof calibration / uncertainty erasure into negative-ish absence  
**Owning area if fixed:** R6 project-environment source composition/admission, with investigation source acquisition as producer

### Exact current route

For a `UvLockDependencyContext`, normal `investigation.py` acquires:

```text
exact sibling pyproject.toml
+
exact uv.lock
→ WorkflowProjectEnvironmentSource
```

The sibling project file supplies the exact project-root path needed by R3. R4 deliberately does not parse its content; exact `uv.lock` remains R4's semantic source.

`derive_project_environment_consumptions(...)` currently contains this admission behavior:

```text
for project source:
    if project_file is not RepositoryTextFile:
        continue
```

Therefore an `UnavailableRepositoryFile` for the required sibling `pyproject.toml` is silently omitted from project-environment derivation. No R3 observation is created and no unresolved CI-consumption item is emitted.

Later, `inspect_workflow_dependency_evidence(...)` may therefore receive:

```text
uv dependency source context
+ readable workflow
+ zero project-environment external consumptions
```

and `_classify_static_consumption(...)` can fall through to:

```text
state = not_established
reason = static_dependency_consumption_not_observed
```

### Why this is materially different from F-001

F-001 loses possible positive evidence into `unresolved`.

F-002 can lose **known source unavailability** entirely and later express a negative-ish absence:

```text
required project-root evidence unavailable
→ evidence disappears
→ static consumption may become not_established/not_observed
```

That is the same dangerous proof direction as the post-R6 unresolved-selection bug, but at an earlier source-admission boundary.

### What is and is not established

If exact sibling `pyproject.toml` is unavailable, the system cannot safely bind R3 to the required project root through the current contract. That does not establish that no relevant project selection exists.

Therefore:

```text
required exact project-root evidence unavailable
!= project selection not observed
!= static dependency consumption not established by exhaustive evidence
```

### Suggested smallest repair direction if selected later

At the R6 project-environment composition seam, preserve material required-source unavailability as unresolved evidence rather than `continue`.

Likely bounded shape:

```text
project_file unavailable
→ unresolved project-environment CI evidence/problem
→ preserve exact missing path + provider reason/detail
→ do not invoke R3
→ do not invoke R4/project-source membership/R5
→ coverage remains unresolved unless stronger independent supported consumption exists
```

Do not invent a project root from `uv.lock` merely to bypass the missing R3 source contract unless a later ownership review explicitly redesigns that contract.

### Suggested regression fixtures

Fixture A — uv context, readable workflow, available lock, unavailable sibling project file:

```text
workflow: uv sync --group docs
project_file: UnavailableRepositoryFile(pyproject.toml)
lock_file: exact readable uv.lock
```

Current expected pressure: no external consumption; coverage can fall to `static_dependency_consumption_not_observed`.

Safe target if fixed: explicit unresolved project-environment evidence preserving `pyproject.toml` unavailability; coverage consumption state unresolved.

Fixture B — project file available, lock unavailable: retain the already intended R4 unresolved lock-source behavior; do not conflate with project-file unavailability.

Fixture C — another independent supported consumption exists: aggregate support may remain existentially supported, but the unavailable project-environment evidence must still remain in the underlying evidence collection rather than disappear.

### R7.3 S001 pressure

S001 does not exercise this missing-source branch: exact PR-head `pyproject.toml` and `uv.lock` are both readable. Therefore the real case neither disproves nor resolves F-002. Its proof direction remains high-priority and still requires explicit disposition before R7.8.

### End-of-R7 decision questions

- Does later R7.3 evidence expose this source-unavailability shape in another real admitted case?
- Is the smallest correct owner R6 composition, or should project-source acquisition expose a typed composition problem earlier?
- Can the correction preserve uncertainty without inventing new project/lock currentness semantics?
- Which exact reason/diagnostic type best preserves source identity without creating a generic evidence framework?

R7.8 must explicitly disposition F-002 before candidate freeze because its current direction can erase uncertainty.

### Implemented local disposition

The selected R7.5 correction keeps ownership at the R6 composition seam:

```text
typed unavailable required project-root source
+ relevant static selector located from its exact path
+ changed-repository root checkout provenance
→ unresolved project-environment CI consumption
→ reason = required_project_root_source_unavailable
→ preserve missing path + provider reason/detail
→ stop before R4 reachability/project-source membership
```

Using the typed unavailable evidence's exact path to locate the static selector does not admit
the missing project file or strengthen its authority. It avoids duplicating R3 command parsing in
R6, while the unavailable state still blocks dependency-domain composition.

The discriminating regression first failed with zero consumptions (`0 != 1`), then passed after
the repair. Progressive local validation executed 39 focused/nearest-integration tests across
the F-002 route, normal investigation, coverage, S001, S011, S005, workflow parsing, and nearest
F-004 checkout-provenance behavior; all passed. Targeted `compileall` and `git diff --check`
passed. Ruff was not run because `.venv/bin/ruff` is absent. No full deterministic suite or live
GitHub verifier was run, so final executable acceptance remains pending.

---

## F-003 — Legacy CI compatibility surfaces are absent from the normal product route but remain protected by tests/topology

**Discovered:** R7.2 remote normal investigation/CI orchestration trace  
**Current disposition:** R7.4 REMOVE/NARROW DECISIONS IMPLEMENTED LOCALLY IN R7.5
**Current blocker:** CLOSED FOR F-003; LATER R7 EXECUTABLE ACCEPTANCE STILL PENDING
**Risk class:** architectural retention / naming / migration residue  
**Owning area:** CI/investigation compatibility surfaces

### Evidence from the normal route

Repository-wide caller tracing established:

```text
investigation.py
→ evaluate_dependency_ci_coverage(...)
→ ci_coverage_result

CLI
→ reads ci_coverage_result directly
```

The ordinary product route does **not** call `evaluate_dependency_ci_exercise(...)` or `inspect_workflow_commands(...)` after the R6 migration.

Current retained compatibility surfaces include at least:

```text
evaluate_dependency_ci_exercise(...)
inspect_workflow_commands(...)
PublicPullRequestInvestigation.ci_exercise_result read alias
direct_requirements_install_path compatibility projection/field
```

The legacy evaluator and helper remain protected by old tests and `tests/test_source_topology.py`; the alias and direct-requirements projection also remain referenced by older tests/history.

### Why this is a finding, not an automatic delete decision

Project governance says:

```text
current use / tests / historical design
!= retention justification
```

But the converse is also true:

```text
not on normal route
!= automatically safe to remove
```

R7.4 must establish whether any real supported alternate API, compatibility obligation, verifier/tool, or external/public contract still needs each surface.

### Required R7.4 disposition trace

For each candidate:

```text
exact responsibility
→ current callers
→ normal producer/integration/consumer route
→ supported alternate route or compatibility obligation, if any
→ concrete failure if removed
→ KEEP / MOVE / NARROW / REMOVE
```

Also review the now-misaligned migration comments/names, including `WorkflowDependencyExerciseInput` and `external_consumptions`, after the product route has become coverage-oriented.

### Suggested regression pressure if removal/narrowing is selected

- normal `investigate_public_pull_request(...)` still reaches `ci_coverage_result` with no legacy evaluator call;
- CLI continues to render coverage-oriented evidence;
- R6 normal investigation regression remains the primary integration guard;
- source-topology tests are updated to protect current owners rather than preserve legacy surfaces by inertia;
- any intentionally retained compatibility alias has a focused test naming the real compatibility obligation.

### End-of-R7 decision questions

- Is any legacy API intentionally public/supported outside the normal application path?
- Are old tests the only remaining callers?
- Does removing a surface simplify proof language and naming without losing a real responsibility?
- Should compatibility removal occur in R7.5 or be explicitly scheduled after the agentic evaluation?

### Implemented local disposition

F-003 was completed at exact executable/test revision:

```text
0ff7b5d8613d521950e2b45006800f269b8597b3
```

The obsolete evaluator/result types, combined workflow-command helper/evidence, investigation
alias, and direct-requirements compatibility projection/result field were removed. The retained
coverage input and composition path now use `WorkflowDependencyCoverageInput` and
`project_environment_consumptions`; related diagnostics use the same concrete responsibility.

Before deleting the two legacy-only test modules, five current cases were migrated to the
coverage owner: no inputs, unavailable-definition precedence with/without successful jobs,
unsuccessful workflow runs with successful jobs, and invocation-before-consumption ordering.
Other admitted requirements/constraints/multi-job/aggregation behavior was already protected by
current coverage and static-evidence suites.

Validation executed 68 focused/nearest tests and the complete standard suite at 529 tests; all
passed. `compileall src tests` and `git diff --check` passed. F-004 checkout-provenance guards were
unchanged and their nearest regressions passed again. Ruff remained unavailable and was not
claimed. Later R7 changes will create a newer executable candidate, so final acceptance remains
pending.

---

## F-004 — Workflow checkout provenance could rebind external-repository commands to changed-repository dependency evidence

**Discovered:** R7.3 S001 real-case GitHub evidence pressure  
**Initial disposition:** HARD BLOCKER — INTERRUPTED R7.3 EVIDENCE SAMPLING  

**Current disposition:** FIXED LOCALLY TO R7.5 FOCUSED/FULL-STANDARD DEPTH; FINAL ACCEPTANCE PENDING R7.9

**Current blocker:** FALSE-SUPPORT PATH CLOSED AT CURRENT LOCAL CANDIDATE; FINAL EXECUTABLE ACCEPTANCE STILL PENDING

**Risk class:** authority/provenance conflation → false static consumption/direct exercise  
**Owning area:** CI workflow orchestration/composition in `ci/workflow_commands.py`; not R3/R4/R5 dependency semantics

### Exact real S001 evidence that exposed the defect

Pydantic S001 is PR `#13432` at exact head:

```text
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
```

The PR changes only `uv.lock`, including:

```text
soupsieve 2.6 → 2.8.4
```

Its admitted PR-head workflow set includes the normal CI workflow, codspeed, and `Third party tests`.

The exact Third-party workflow deliberately tests Pydantic inside other projects. Its own instructions say to check Pydantic out under a custom path such as `pydantic-latest`. The Pandera job concretely does:

```yaml
- name: Checkout Pandera
  uses: actions/checkout@...
  with:
    repository: unionai-oss/pandera

- name: Checkout Pydantic
  uses: actions/checkout@...
  with:
    path: pydantic-latest

- name: Install Pandera dependencies
  run: |
    pip install uv
    uv sync --no-progress --extra pandas --extra fastapi --extra pandas --group dev --group testing --group docs
    uv pip uninstall --system pydantic pydantic-core
    uv pip install --system -e ./pydantic-latest
```

At that `uv sync` step:

```text
GITHUB_WORKSPACE root = Pandera
Pydantic = ./pydantic-latest
```

Therefore the root `--group docs` selector belongs to Pandera, not Pydantic.

### Pre-fix false-support path

Before the repair, normal investigation acquired one exact Pydantic project/lock source bundle and passed it to every admitted workflow definition. R6 then iterated every `run:` step without tracking checkout provenance.

That allowed:

```text
Pandera root command
uv sync ... --group docs
→ R3 supplied Pydantic project_file_path = pyproject.toml
→ selector docs interpreted as Pydantic docs
→ R4 reads exact Pydantic uv.lock
→ real Pydantic path docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
→ R5 supported Pydantic static consumption
```

The dependency path itself is real, but the command→repository binding is false. This is authority/provenance conflation, not merely conservative under-reporting.

S001's Third-party run happened to be skipped at this exact PR head, but static evidence is not allowed to become false merely because runtime happened not to activate it. The same workflow can run under its admitted label condition, so the defect met the R7 hard-blocker rule.

### Ownership decision

The repair deliberately does **not** move GitHub checkout semantics into R3 or R4.

Existing ownership remains:

```text
workflow-definition provider IR
→ represents uses: actions/checkout + with:/if: structure

R3
→ interprets project-selection command semantics

R4 / project-source membership
→ interprets dependency reachability/membership

R6 CI compositor
→ owns whether a workflow command may be bound to the changed repository's source evidence
```

Therefore checkout provenance belongs in R6 orchestration/composition.

### Implemented bounded repair

`derive_project_environment_consumptions(...)` now tracks one bounded per-job workspace-root state while walking steps in source order:

```text
not_established
current_repository
other_repository
unresolved
```

Only explicit static `actions/checkout` declarations affect it.

Rules:

```text
checkout current repository at root
→ current_repository

checkout explicit different repository at root
→ other_repository

checkout literal subpath
→ does not displace current root owner

checkout with dynamic/unsafe path or dynamic repository
→ unresolved

conditional root checkout
→ unresolved
```

Project-environment semantics now require:

```text
R3 selector visible
+
root_checkout_state = current_repository
→ allowed to enter R4/project-source membership → R5
```

while:

```text
other_repository
→ no current-repository project consumption

not_established / unresolved
→ preserve unresolved checkout-provenance consumption
→ do not invoke R4/R5
```

Reason:

```text
project_environment_checkout_provenance_unresolved
```

This is intentionally **not** a checkout simulator. It answers only the minimum proposition R6 needs: whether the changed repository is statically established at workspace root for repository-relative dependency evidence.

### Root-cause extension to direct requirements/direct invocation

R7.3 review found the same pre-fix provenance defect on the direct-requirements branch:

```text
other repository at root
+ pip install -r requirements-dev.txt
→ could be rebound to changed repository RequirementsFileDependencyContext
```

and a later direct invocation could then be correlated in the same job.

The repair therefore reuses the same root checkout state in `inspect_workflow_dependency_evidence(...)`:

```text
current_repository
→ direct requirements consumption/invocation may be admitted

other_repository
→ do not bind root-relative requirements or invocation to changed repository

not_established / unresolved
→ requirements declaration becomes explicit unresolved provenance evidence
→ direct invocation is not promoted
```

Reason for ambiguous requirements provenance:

```text
direct_requirements_checkout_provenance_unresolved
```

This closes the root cause instead of patching only the S001 uv manifestation.

### Real S001 post-repair source-level pressure

The exact normal CI docs job checks Pydantic out at workspace root before:

```text
uv sync --all-packages --group docs
```

and exact Pydantic `uv.lock` preserves:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve 2.8.4
```

so the intended positive witness remains admissible.

Codspeed likewise performs the normal current-repository root checkout before its uv selector. Its selector remains expected non-positive for SoupSieve.

The Third-party workflow is the opposite topology: external projects at root, Pydantic in `pydantic-latest`. Repository-wide inspection of the main CI workflow found no explicit alternate `repository:` checkout competing with its normal root owner.

### Regression pressure added

Deterministic regressions now cover:

1. exact S001/Pandera-shaped external root checkout + Pydantic subpath + external `--group docs` → **no Pydantic consumption**;
2. dynamic checkout path + plausible Pydantic docs selector → explicit checkout-provenance `unresolved`;
3. current Pydantic root + another repository in a literal subpath → Pydantic docs support remains valid;
4. existing S001/S011/investigation happy-path fixtures now explicitly declare current-repository checkout;
5. direct-requirements external-root checkout → no current-repository requirements consumption or invocation;
6. dynamic checkout path + direct requirements declaration → unresolved requirements provenance and no direct invocation promotion;
7. direct-requirements coverage fixtures explicitly establish the current repository checkout premise.

The real S001 verifier now also rejects any `supported` project-environment consumption originating from:

```text
.github/workflows/third-party.yml
```

while preserving the existing docs-witness and codspeed-negative checks.

### Remote repair revisions

Primary production correction:

```text
d14bb6d70c9bc34d0116d7c3abd56ea7bab9d6f5
R7 guard project selection with checkout provenance
```

Follow-up source correction closing the same root cause on direct requirements/invocation:

```text
e320ad64403360ff8b5c9c5a5e55e3c096bfee5a
R7 extend checkout provenance to direct CI evidence
```

Supporting regression/verifier commits include:

```text
30656ae3c56fae496877571b4b7ec23ab74c25df
fc13dfb44cf97863d7165f8e0e7d03ea39d5749d
9b3f0797059f30d447714e08b8076b94c04306f8
b852812035f1bf5009ef48ca591fa77070cc9473
85db9107f821dc23f0a1773051e3731e8b8c0fc5
ed1eb87f71c4f0b4c0aacb8d7b54e698c3fd4e24
127593f7e20b4e0b1e6d5722ec891e1d39a4738f
```

The R7.5 post-cleanup re-audit inspected the complete cleanup diff from
`0ce34f153925a45fdb2ad50385faf69e751ce6de` through
`b50e4b1a656625c3215dd3fbf08c28012c6d18aa`. F-002 added an earlier unavailable-source stop;
F-003 removed legacy CI surfaces and narrowed current names; F-005 did not touch workflow or
coverage code. None bypassed the per-job root-checkout gate before R4/project-source or direct
requirements composition.

The five discriminating project-environment/direct-requirements provenance regressions were
then executed explicitly at the F-005 candidate and passed (**5 tests / OK**). The full standard
suite at that candidate also passed (**515 tests / OK**). This is local regression evidence for
the repaired path, but the final R7 executable acceptance claim remains reserved for R7.9.

### Retained bounded limitation

This repair establishes only **workspace-root ownership**. If the changed repository itself is intentionally checked out into a non-root subpath and a workflow later uses `working-directory` to operate inside that subpath, current R3 project-root contracts are not rebased to the checkout location. Such a case is currently expected to under-report or remain unresolved rather than manufacture support.

Do not broaden this repair into a general checkout/filesystem simulator without a real product trigger.

### R7 disposition questions remaining

Before final acceptance:

- R7.6 must re-audit the post-cleanup source/diff for proof strengthening and checkout-state bypasses.
- R7.9 must execute focused provenance regressions, nearest CI integration, the full deterministic suite, and the real S001 verifier when the final candidate is frozen.
- If executable evidence exposes a missed checkout shape, reopen the smallest owning R7 slice rather than weakening the provenance guard.

---

## F-005 — Legacy uv membership API hosted current R4 reachability mechanics

**Discovered:** R7.4 architecture/naming/retention review

**Current disposition:** FIXED LOCALLY IN R7.5 BY OWNER MOVE + LEGACY SURFACE REMOVAL

**Current blocker:** NO

**Risk class:** responsibility/naming drift and accidental legacy retention

**Owning area:** `dependency/uv_reachability.py`

### Exact cause and ownership result

The public `evaluate_uv_selected_environment_membership(...)` proposition had no current
production caller after R5 moved CI composition to the narrower selected-root reachability
contract. However, `uv_reachability.py` still imported its private graph projection and edge
resolution mechanics from `uv_membership.py`. Retaining the whole old module would preserve an
obsolete and over-broad public contract; deleting it directly would break current R4.

R7.5 traced the actual dependency closure and kept the responsibilities separated:

```text
uv_lock_structure.py
→ shared external lock structural admission

uv_reachability.py
→ R4-specific package/edge/root projection
→ deterministic edge resolution
→ bounded selected-root traversal

uv_membership.py
→ removed obsolete public proposition and result types
```

No generic graph abstraction was introduced because no second present consumer justified one.

### Unique proof migration

Before deleting the legacy tests, current R4 retained explicit coverage for:

1. optional-extra and all-extra root selection;
2. traversal through an activated dependency extra;
3. ambiguous repeated records versus version-discriminated resolution;
4. cycle-safe traversal without false reachability;
5. a sound positive witness under all-workspace package scope.

The legacy universal-lock marker case was already covered more precisely by current R4
conditional-candidate and resolution-marker tests. The shared lock-structure integration test
was rebound from the obsolete membership consumer to the current reachability consumer.

### Executable revision and validation

```text
b50e4b1a656625c3215dd3fbf08c28012c6d18aa
Retire legacy uv membership API

.venv/bin/python -m unittest \
  tests.test_uv_selected_root_reachability \
  tests.test_uv_lock_structure
→ 21 tests / OK

.venv/bin/python -m unittest discover -s tests -p "test_uv*.py"
→ 43 tests / OK

nearest CI/integration/topology modules
→ 27 tests / OK

.venv/bin/python -m unittest discover -s tests
→ 515 tests / OK

.venv/bin/python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

The executable/test diff was **425 insertions / 1650 deletions across 8 files**. The deletion is
the authorized retirement of one obsolete production module and two legacy-only test modules,
not a loss of the current R4 proof owner. Ruff remained unavailable in `.venv` and was not
claimed. Final R7 executable acceptance remains pending R7.9.

---

## Future finding template

Use the next stable ID (`F-006`, `F-007`, ...).

```text
Finding ID / title
Discovered at R7 slice
Current disposition
Blocker? yes/no
Risk class
Owning area

Exact evidence/current behavior
Root cause
User/product/proof consequence
Why it is or is not a blocker
Possible repair direction (not authorization)
Suggested discriminating regression/real-case fixtures
Dependencies/interaction with earlier findings
Questions for final R7 disposition
```

Do not duplicate one root cause into multiple findings merely because it appears through different callers; extend the existing finding when later evidence belongs to the same underlying issue.
