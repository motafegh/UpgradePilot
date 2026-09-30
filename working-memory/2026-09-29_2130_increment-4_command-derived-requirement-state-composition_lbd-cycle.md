# Increment 4 — Command-Derived Requirement-State Composition — Learning-by-Doing Cycle

**Date:** 2026-09-29  
**Cycle status:** CLOSED — A0/A1/A2/B/D/E DONE; Verification GREEN; C COMPLETE  
**Primary responsibility:** compose already-established dependency/source applicability, package-manager semantic facts, and exact successful command execution into one bounded per-command requirement-state witness without changing CI-coverage, later-use, compatibility, or maintainer-action meaning  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Broader R4 sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`

## Cycle status

```text
A0 — DONE: current main/live owners/source/test seams reconciled; no route contradiction
A1 — DONE: continuity model understood; visible command text alone does not establish effective semantics or successful execution
A2 — DONE: product purpose, real-case data flow, proof boundary, stop points, and identity-safety responsibility understood
B — DONE: bounded command-derived requirement-state composer and focused/integration proof implemented
Verification gate — GREEN: Product verification #15 on exact implementation head c9edc76e8c3f4e9bb9d58e27ddac3cfbc291a8be
D — DONE: evidence-backed implementation learning and ownership cleared with no repair required
E — DONE: final owner reconciliation, closure, and handoff completed
C — COMPLETE: meaningful engineering + learning progression preserved across A0→E
```

## A0 — current-state reconciliation + cycle initialization — DONE

### Exact repository state

A0 started from canonical `main` at:

```text
0148b057dfe09a6b1792062a0e38e7a19aefc397
reconcile completed R4 increment ownership
```

The last hosted Increment-3 implementation proof remains Product verification #14 on exact implementation head:

```text
29247346d1c1e3ea7074ffd7daf9c53d8c3beeda
focused investigation composition: 15/15
full deterministic product regression: 699/699
conclusion: GREEN
```

Comparison from that verified head to current `main` shows 15 later commits changing only:

- `MEMORY.md`;
- `README.md`;
- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`;
- the R4 implementation-sequence working memory;
- the closed Increment-3 cycle record.

No `src/` or `tests/` file changed after the verified Increment-3 implementation head. Therefore the current implementation surface remains the hosted-verified Increment-3 source/test state while the later commits reconcile documentation and ownership.

### Live-owner reconciliation

The relevant owners agree:

- At A0, `MEMORY.md` showed Increment 3 closed and Increment 4 selected next.
- runtime dependency-state plan: Increments 1–3 are implemented/verified/learned/closed; Increment 4 is command-derived requirement-state composition; application integration is later Increment 5.
- ADR-0010: runtime dependency-state proof must remain separate from existing CI coverage/exercise evidence and must preserve explicit unresolved/not-established problems.
- R4 sequence: execution evidence → package-manager declaration → effective semantic facts → requirement-state composer → later application integration.

No current evidence invalidates or changes the selected Increment-4 responsibility.

### Current source seams available to Increment 4

The required upstream evidence already exists as separate owners:

1. **Exact dependency transition/source provenance**
   - `dependency/change.py`
   - `DependencyVersionChange`
   - `DependencyChangeSourceEvidence`

2. **Supported exact static dependency consumption**
   - `ci/consumption.py`
   - `StaticDependencyConsumptionEvidence`
   - direct-requirements and project-environment mechanisms remain separately represented.

3. **Static package-manager operation identity**
   - `dependency/package_manager_operation.py`
   - `PackageManagerOperationDeclaration`
   - one parsed operation preserves exact `StaticCommandLocation`.

4. **Independent effective semantic facts**
   - `dependency/package_manager_semantics.py`
   - `ManagerEnvironmentSelectionFact`
   - `InstallationDestinationFact`
   - `PackageMutationModeFact`
   - `DirectRequirementHandlingFact`
   - each fact preserves the same exact command location plus bounded provenance.

5. **Exact successful command execution**
   - `ci/runtime_execution.py`
   - `ExactCommandExecutionAssessment`
   - exact command execution remains distinct from successful user-step execution.

The intended Increment-4 module `src/upgradepilot/ci/dependency_state.py` does not exist yet. That is expected and confirms the selected composer responsibility has not been implemented prematurely.

### Existing proof seams

Current tests already protect the ingredients independently:

- `tests/test_package_manager_semantics.py` — package-manager operation identity and semantic facts;
- `tests/test_package_manager_route_a_semantic_fixture.py` — one controlled Route-A fixture closes all four semantic facts while an ordinary-looking command remains unresolved;
- `tests/test_ci_runtime_execution.py` — exact command execution versus step execution and structural/continue-on-error/non-success boundaries;
- existing direct-install/CI-consumption tests protect static source-consumption meaning.

The plan's mention of `tests/test_runtime_dependency_contract.py` is only appropriate if an Increment-4 assertion genuinely belongs to that file's current dependency-version-bound responsibility. A dedicated focused dependency-state composer test module is likely the cleaner default; A2/B must decide from responsibility rather than filename convenience.

### A0 architectural observation

Increment 4 should begin as **composition of already-owned evidence**, not as another parser/environment/config subsystem.

The important join identity is distributed across the current inputs:
- CI consumption/execution carry workflow/revision/job/step identity plus command location;
- package-manager semantic facts currently carry command location but not standalone workflow identity.

Therefore `StaticCommandLocation` must not be treated as globally unique by itself. A2/B must preserve scoped identity when binding semantic facts to the exact CI command rather than joining unrelated facts merely because their source spans/source order happen to match.

The first design question is therefore not “what more environment state should we reconstruct?” but:

```text
when do these already-established propositions refer to the same exact dependency/source/command/runtime scope,
and when is their combined evidence sufficient to emit the bounded command-completion witness?
```

No new Increment-3-style environment producer is justified by A0 evidence.

### A0 non-goals preserved

Increment 4 must not silently establish:

- fresh-install causality;
- wheel/sdist or artifact identity;
- state persistence after command completion;
- later behavior/package exercise;
- compatibility;
- maintainer-action permission;
- generic job-log/stdout/artifact acquisition;
- application-level investigation integration (later Increment 5).

### A-phase orientation / learning map

#### A1 continuity topics
- what Increment 1 established: reusable exact-command execution evidence;
- what Increment 2 established: shared package-manager declaration + independent semantic dimensions;
- what Increment 3 added: enough bounded environment/config/executable evidence to close those semantic facts for one Route-A family;
- why none of those facts alone yet means the proposed dependency requirement is satisfied;
- why Increment 4 is the missing proof-composition edge rather than another evidence-producer increment.

#### A2 upcoming-responsibility topics
- exact proposition represented by `RequirementSatisfiedAtCommandCompletion`;
- distinction between **supported witness**, **not established**, and **unresolved**;
- identity alignment across dependency source, static consumption, semantic facts, and runtime execution;
- required positive premises for the first requirements-file/pip family;
- close-defeaters: dry-run, retargeting/exclusion, unresolved semantic source, non-success, command identity mismatch, multiple command candidates;
- witness provenance and limitations;
- likely focused source/test ownership;
- acceptance boundary and explicit non-goals.

#### Ownership depth
A2 should emphasize two engineering ownership points:
1. deciding when heterogeneous evidence may be joined as one proposition;
2. preserving the difference between absence/not-established and unresolved evidence when a join premise fails.

### A0 conclusion

A0 is complete.

No contradiction, stale live owner, implementation drift, or proof result requires replanning Increment 4.

## A1 — continuity / recent-work onboarding — DONE

Ali's A1 reasoning correctly identified the central continuity point:

> seeing only `pip install -r requirements.txt` is insufficient because effective conditions such as dry-run and PATH/environment-related state may change what the command actually means, so additional evidence is required.

Refinement recorded at the gate:

- dry-run/PATH/environment are concrete examples of the larger rule;
- visible static command text does not by itself establish effective package-manager semantics;
- visible static command text also does not establish that the exact command actually executed successfully;
- the stronger command-completion state claim therefore requires composition of source applicability + supported consumption + resolved semantic facts + exact successful execution.

This is sufficient continuity ownership for A1. No material misunderstanding remains that should block the next orientation.

A1 is **DONE**. A2 subsequently completed after the product-purpose and real-case grounding below.

## A2 — upcoming responsibility orientation — DONE

### Exact proposition

The first positive result should mean approximately:

```text
The exact proposed direct requirement is satisfied
in the resolved package-state scope
at the completion boundary of this exact successful command.
```

A shorter internal name such as `RequirementSatisfiedAtCommandCompletion` is an evidence proposition, not an installation-history claim.

### Required positive premises for the first Route-A family

A positive witness should require all of the following to align:

1. one trusted `DependencyVersionChange` establishes exact package + proposed version;
2. one source-applicable supported `StaticDependencyConsumptionEvidence` establishes that the exact command consumes the affected dependency source;
3. the semantic facts for that same command establish manager environment, admitted destination, mutation mode = `apply_changes`, and direct requirement handling = `handled`;
4. exact command execution is `supported`;
5. workflow/revision/job/step/command identity is mutually compatible rather than merely similar.

For the first requirements-file/pip family, the destination should remain inside the resolved manager-environment package-state scope. A materially retargeted destination must not be silently interpreted as satisfying that manager environment.

### Result-state model

A2 preserves at least three meanings:

- **supported witness** — every required edge is positively established and aligned;
- **not established** — factual evidence closes negatively, e.g. runtime command did not succeed, mutation mode is dry-run, direct requirement handling excludes the direct requirement, or destination is outside the admitted first-family scope;
- **unresolved** — a material premise cannot be known safely, e.g. semantic source precedence is unresolved, exact command reachability/correlation is unresolved, or evidence identity cannot be safely joined.

`not_established` is not the same as package absence. It means this evidence path does not prove the positive command-completion proposition.

### Identity discipline

The composer must prevent accidental cross-command/cross-workflow evidence joins.

Current evidence shape matters:

```text
StaticDependencyConsumptionEvidence
  → workflow_path / workflow_revision / job_key / step_source_index / command_location

ExactCommandExecutionAssessment
  → workflow_path / workflow_revision / job_key / step_source_index / command_location

semantic facts
  → command_location
```

Because semantic facts currently preserve only `command_location`, the Build must deliberately keep them bound to the scoped command from which they were resolved. Matching source span/order alone is not enough to assert global identity.

### Close-defeaters that must remain visible

At minimum:

- effective dry-run → no positive witness;
- direct-requirement exclusion → no positive witness;
- destination retargeting outside first admitted scope → no positive witness;
- unresolved environment/config semantic source → unresolved;
- exact command runtime non-success → not established;
- runtime execution/correlation uncertainty → unresolved;
- command/workflow identity mismatch → fail safely;
- several candidate commands → keep separate per-command results rather than collapsing environments.

### Witness content

A positive witness should preserve enough evidence to explain itself:

- package and proposed version;
- dependency source evidence;
- workflow/revision/job/step/command provenance;
- resolved manager environment;
- resolved destination scope;
- semantic fact provenance;
- exact execution evidence;
- observation boundary = exact successful command completion;
- explicit limitations.

### Likely implementation ownership

The clean default remains a new focused module such as `src/upgradepilot/ci/dependency_state.py`. It should compose existing facts rather than reparse commands or re-resolve environment/config semantics.

Focused tests should probably live in a dedicated file such as `tests/test_ci_dependency_state.py` rather than overloading `test_runtime_dependency_contract.py`, whose present responsibility is installed project dependency bounds.

Final names remain implementation decisions; ADR-0010 deliberately does not fix them.

### Acceptance boundary

Increment 4 passes when one exact Route-A command can yield the bounded witness and the important close-defeaters produce truthful not-established/unresolved outcomes without changing existing CI coverage semantics.

It does **not** need application-level exposure yet; that is Increment 5.

### A2 learning gap discovered — product purpose before implementation detail

Ali reported that the current A2 explanation jumped too quickly into identity mechanics before the purpose of Increment 4 itself was clear.

This was a material learning gap, not a gate failure. At that point A2 remained open until the model was rebuilt from:

```text
product question
→ missing evidence proposition
→ what Increments 1–3 already prove
→ what they still cannot prove
→ why Increment 4 exists
→ only then implementation/identity mechanics
```

Do not ask detailed identity-joining ownership questions again until the broader Increment-4 goal and problem are understood.


### A2 real-case grounding — S002 / S011 / S008

A2 is now grounded in existing product-simulation cases rather than abstract-only examples.

#### S002 — HTTPX 0.27.2 → 0.28.1

Real case:
- repository: `Aidan-Wallace/kubernetes-dashboard-token-api`;
- PR #20;
- changed source: `requirements.txt`;
- Python workflow contains `python -m pip install --no-cache-dir --upgrade pip -r requirements.txt`, then Ruff and pytest;
- that Python workflow did not trigger for the historical PR because its path filters excluded `requirements.txt`;
- a separate Docker workflow was green, but historical Docker logs/resolved dependency state are no longer recoverable.

Increment-4 relevance:

```text
DependencyVersionChange(httpx 0.27.2 → 0.28.1)
+ direct requirements consumption in the Python workflow
+ command semantic facts
+ exact successful execution of THAT SAME Python command
→ possible RequirementSatisfiedAtCommandCompletion
```

But the historical Python command did not obtain positive runtime execution evidence. Therefore no positive command-completion witness may be inferred from the separate green Docker workflow.

This is also the clearest real identity-safety example: semantic/static evidence from the skipped Python workflow must never be joined with success from the different Docker workflow merely because both belong to the same PR/repository.

#### S011 — NumPy 1.26.4 → 2.4.6 inside optional `mlx`

Real case:
- repository: `dragfly/dictare`;
- PR #34;
- changed dependency is inside `[project.optional-dependencies].mlx`;
- inspected Ubuntu and macOS test workflows both install `.[dev]`, not `.[mlx]`.

Increment-4 relevance:

```text
DependencyVersionChange(numpy in mlx)
+
inspected CI selects dev, not mlx
→ affected dependency source/environment is not consumed
→ stop before package-manager semantics/runtime composition
→ no RequirementSatisfiedAtCommandCompletion witness for the changed mlx family
```

This demonstrates that Increment 4 is not a mechanism for forcing every case through semantic/runtime evidence. If the affected dependency environment is not formed, the proof fails at an earlier edge.

#### S008 — OpenCV 4.2.0.32 → 4.8.1.78

Real case:
- repository: `carla-simulator/scenario_runner`;
- PR #1111;
- changed source: `requirements.txt`;
- inspected CI installs requirements on Ubuntu;
- the owned concern is specifically the CPython-3.6 Linux wheel → source-distribution fallback transition;
- inspected workflows do not pin/matrix Python 3.6.

Increment-4 relevance:

Even if a future exact CI command earned:

```text
RequirementSatisfiedAtCommandCompletion(
  opencv-python==4.8.1.78,
  environment=<that exact CI Python environment>
)
```

that witness would prove only package-state satisfaction in that exact environment at command completion.

It would still not prove:
- that the environment is CPython 3.6 unless interpreter identity establishes that;
- that the Python-3.6 source-fallback branch was exercised;
- that source build succeeded;
- behavioral compatibility.

S008 therefore demonstrates the Increment-4 claim boundary: a correct package-state witness may still be non-discriminating for a more specific artifact-selection proposition.

#### Cross-case data-flow lesson

```text
S011
source/environment applicability fails first
→ do not continue pretending semantic/runtime proof matters

S002
source/command may be relevant
but exact relevant runtime execution is missing
→ no positive witness
→ never borrow success from another workflow

S008
a package-state witness could be valid for one environment
but still not answer the case-specific Python-3.6 artifact question
→ preserve proposition-specific proof limits
```

These cases are the preferred A2 anchors before returning to implementation-level identity mechanics.


### A2 gate closure

After resetting A2 from product purpose downward and grounding it in S002/S011/S008, Ali confirmed the broader Increment-4 model and explicitly asked to begin B.

A2 is therefore **DONE**.

Build authorization is bounded to Increment 4:
- compose existing exact dependency/source applicability, semantic facts, and exact command execution;
- preserve identity and explicit not-established/unresolved results;
- prove the first direct-requirements/pip Route-A family;
- do not start Increment-5 application integration or broaden earlier semantic/environment producers without a newly exposed blocker.

## B — implementation progression — DONE

### B1 selected responsibility — command-derived requirement-state composition contract

Pre-change model:

```text
DependencyVersionChange
+ exact requirements source context
+ one exact supported direct-requirements CI consumption
+ semantic evidence bound to that same command
+ exact execution evidence for that same scoped command
→ RequirementSatisfiedAtCommandCompletion
   OR explicit not-established / unresolved problem
```

B1 must encode identity checks rather than rely on caller convention. Existing package-manager semantic facts remain dependency-owned and CI-independent; the new CI composition owner may bind them to workflow/revision/job/step scope without moving GitHub-specific identity into those semantic types.

Focused proof must cover at least:
- positive direct-requirements Route-A witness;
- dry-run → not established;
- unsupported/retargeted destination → not established;
- semantic unresolved → unresolved;
- runtime non-success → not established;
- scoped command identity mismatch → unresolved/fail-safe;
- multiple candidates remain separately composable rather than collapsing environments.


### B1/B2 implementation state — source complete, execution proof pending

Implemented on `main`:

- `src/upgradepilot/ci/dependency_state.py`
  - `ExactCICommandIdentity` for workflow/revision/job/step/command identity;
  - `ScopedPackageManagerSemanticEvidence` for CI-owned binding of dependency-owned semantic facts;
  - `RequirementSatisfiedAtCommandCompletion` as the bounded positive witness;
  - `RequirementStateProblem` with `not_established | unresolved`;
  - typed blocker provenance for semantic failures;
  - source/package/revision/command identity checks;
  - admitted first-family checks for manager-environment destination, apply-changes mutation, direct-requirement handling, and exact successful execution.

- `tests/test_ci_dependency_state.py`
  - positive direct-requirements witness;
  - effective dry-run → not established;
  - retargeted destination → not established;
  - unresolved semantic source → unresolved with typed blocker provenance;
  - runtime non-success → not established;
  - same local command location from a different workflow → rejected through full scoped identity;
  - multiple command candidates remain separate witnesses;
  - dependency-source mismatch fails closed;
  - real Route-A integration path using actual workflow parsing, direct-requirements consumption, process-environment/config semantic resolution, workflow/runtime correlation, exact-command execution, and final composition.

Important correction during B:
- the first semantic-scope binder copied full scope from the consumption being proved;
- review showed that this could conceptually launder semantic facts from another workflow when local command locations collide;
- the binder was corrected so semantic scope is supplied independently from its semantic-producing workflow/job/step/occurrence context, then compared against consumption/execution scope by the composer.

Additional source check:
- the current exact-requirement extractor admits only bare `package==version` changed lines; environment-marker conditional pins are not silently admitted into this first family.

Execution validation state:
- no runtime PASS is claimed yet;
- the available connector cannot dispatch the intentionally manual `product-verification.yml`;
- the fallback execution container cannot resolve GitHub, so it cannot obtain the repository snapshot;
- at that point B remained open until the focused composer test and broader deterministic regression were executed; Product verification #15 later cleared this condition.

No Increment-5 application integration has started.


## Verification gate — GREEN

Product verification #15:

```text
run: 36717618416
event: workflow_dispatch
status: completed
conclusion: success
exact run head: c9edc76e8c3f4e9bb9d58e27ddac3cfbc291a8be
```

The hosted run verified the exact Increment-4 implementation head before later documentation-only reconciliation.

Observed proof:

- fresh package build/install completed;
- `pip check`: `No broken requirements found.`;
- installed CLI entry point and `python -m upgradepilot` both executed successfully;
- focused investigation composition: **15/15**;
- deterministic product regression: **708/708**;
- all Increment-4 composer tests ran inside that regression, including:
  - positive bounded witness;
  - dry-run not-established;
  - retargeted destination not-established;
  - unresolved semantic provenance;
  - runtime non-success;
  - cross-workflow same-local-location rejection;
  - separate multiple command candidates;
  - dependency-source mismatch;
  - real producer-to-composer Route-A integration.

No `FAILED` or `ERROR` outcome appears in the hosted job log.

### Verification interpretation

The gate establishes that the admitted Increment-4 composer behavior works in the hosted installed-package product environment and does not regress the deterministic product suite.

It does not establish:
- universal package-manager semantics;
- optional-extra/project-environment requirement-state composition;
- arbitrary runtime-state observation;
- later dependency exercise;
- behavioral compatibility;
- maintainer-action permission.

B is **DONE** and the formal Verification gate is **GREEN**.

## D — evidence-backed learning / ownership — DONE

D should now inspect the actual implemented proof ladder and verify ownership of:
- why the composer belongs in CI composition rather than dependency semantic producers;
- why scoped semantic identity must be independently supplied and then compared;
- the practical difference between `not_established` and `unresolved`;
- why a positive command-completion witness still stops before later-use/compatibility/action claims;
- how S002/S011/S008 map onto the implemented stop points.

No new product mutation is authorized by entering D; repair becomes justified only if D exposes a material implementation/understanding gap.


### D1 — verified positive Route-A implementation walkthrough — DONE

D begins from the exact producer-to-composer integration case that passed inside Product verification #15.

Verified fixture flow:

```text
DependencyVersionChange
  requests 2.32.4 -> 2.33.0
  source: requirements.txt / exact_requirement

RequirementsFileDependencyContext
  repository: example/project
  revision: exact fixture revision
  normalized package: requests

workflow static evidence
  checkout current repository
  install step consumes requirements.txt
  -> StaticDependencyConsumptionEvidence(state=supported, mechanism=direct_requirements)

package-manager declaration + semantic producers
  /opt/bootstrap/bin/python -m pip
  --python /opt/target/bin/python
  install --no-user --no-deps -r requirements.txt
  PIP_DRY_RUN=0
  PIP_CONFIG_FILE=/dev/null
  PIP_TARGET/PIP_PREFIX/PIP_ROOT empty
  PIP_ONLY_DEPS/PIP_ONLY_DEPENDENCIES=0

  -> manager environment: /opt/target/bin/python
  -> destination: manager_environment_scheme
  -> mutation mode: apply_changes
  -> direct requirement handling: handled

CI semantic binding
  workflow path + revision + job + step + command location
  -> ScopedPackageManagerSemanticEvidence

runtime
  exact workflow revision
  job "Tests"
  runtime step "Install" completed-successfully
  exact command eligible/correlated
  -> ExactCommandExecutionAssessment(state=supported)

composer
  validates dependency/source identity
  validates direct-requirements mechanism
  validates semantic scope == consumption scope
  validates runtime scope == consumption scope
  rejects semantic problems
  requires one manager identity
  requires manager-environment destination
  requires apply_changes
  requires direct requirement handled
  requires exact execution supported

  -> RequirementSatisfiedAtCommandCompletion
```

D ownership emphasis:
- `--no-deps` does not exclude the direct requirement itself; it excludes dependency expansion, so direct-requirement handling can still be `handled`.
- full CI command identity is a composition safety invariant, not merely metadata.
- `not_established` means a known negative edge prevents this proof; `unresolved` means a material edge cannot be safely determined.
- the positive witness stops at successful command completion and deliberately does not imply later package exercise, compatibility, or maintainer-action permission.

D1 ownership check cleared.

Ali correctly classified:
- known effective dry-run as not_established because the required mutation is positively known not to occur;
- unknown effective dry-run as unresolved because a material semantic premise is unknown;
- semantics from one workflow plus success from another as unresolved because the evidence cannot safely be joined.

### D2 — command-completion witness versus later proof — DONE

Next ownership focus: why RequirementSatisfiedAtCommandCompletion does not itself establish later dependency exercise, behavioral compatibility, or maintainer-action permission.


#### D2 ownership check — CLEARED

Ali correctly separated the downstream propositions:

1. **Established:** NumPy 2.4.6 may be claimed satisfied at command completion when the Increment-4 witness exists, with the witness's exact provenance explaining why.
2. **Not established by Increment 4:** later tests exercised NumPy-dependent behavior; that requires an explicit later-use/exercise proposition.
3. **Not established by Increment 4:** compatibility or maintainer action; those belong to later evidence synthesis/decision responsibilities.

Key ownership statement from the check: the system should say only what its recorded evidence proves and must not invent or guess missing proof edges.

### D3 — ownership of composition layer and scoped identity — DONE

Final core D focus:
- package-manager semantic producers answer command-local questions such as manager environment, destination, mutation mode, and direct-requirement handling;
- CI composition owns workflow/revision/job/step/runtime identity and the decision to join heterogeneous evidence into the stronger command-completion proposition;
- therefore GitHub workflow identity should not be pushed into dependency semantic fact types merely to make composition convenient;
- semantic scope must be established independently and compared against consumption/runtime scope so evidence cannot be laundered across commands.

D3 remains open for one concise ownership check.


#### D3 ownership check — CLEARED

Ali identified the core architectural principle correctly: keep responsibility boundaries explicit, let each layer/provider own the facts it can actually establish, and reuse those shared facts rather than repeating provider-specific context or logic everywhere.

Refinement:
- package-manager semantic facts stay dependency-owned because they describe command meaning independently of GitHub Actions;
- provider/CI layers own workflow/runtime identity and execution evidence;
- the CI dependency-state composer owns the cross-layer join that turns those independently established facts into the stronger command-completion proposition;
- this preserves reuse, avoids duplicated semantics, and prevents provider-specific identity from leaking into lower dependency abstractions.

## D — COMPLETE

D ownership now covers:
- known-negative versus unresolved proof failure;
- command-completion witness versus later-use/compatibility/action claims;
- why scoped identity is an evidence-safety invariant;
- why cross-layer composition belongs in CI rather than package-manager semantic producers;
- how the verified Route-A path and S002/S008/S011 stop points map onto the architecture.

No material implementation or understanding gap was exposed by D. No repair is required.

## E — closure / handoff — DONE

### Final verified implementation

Increment 4 is closed against Product verification #15:

```text
run: 36717618416
event: workflow_dispatch
conclusion: success
verified implementation head: c9edc76e8c3f4e9bb9d58e27ddac3cfbc291a8be
focused investigation composition: 15/15
deterministic product regression: 708/708
```

The hosted job also passed fresh package build/install, `pip check`, installed CLI, and `python -m upgradepilot` checks.

A final comparison from the verified implementation head to the closure state found no later `src/` or `tests/` changes. Post-verification commits changed only live planning/memory/working-memory owners, so no new execution proof is required for closure.

### Final Increment-4 capability

The first admitted direct-requirements/pip Route-A family can now produce:

```text
RequirementSatisfiedAtCommandCompletion
```

when exact dependency/source applicability, package-manager semantic facts, scoped command identity, and exact successful command execution all align.

The implementation also preserves explicit `not_established` and `unresolved` outcomes for known-negative and insufficient/unsafe proof edges.

### Preserved proof boundary / deferred scope

Increment 4 does not establish or add:
- fresh-install causality;
- wheel/sdist or artifact identity;
- persistence after command completion;
- later dependency use or affected-behavior exercise;
- behavioral compatibility;
- maintainer-action permission;
- generic job-log/stdout/artifact acquisition;
- universal pip/uv semantics;
- application-level investigation integration.

These remain separate responsibilities and must not be inferred from the command-completion witness.

### Handoff

Increment 4 is **CLOSED**.

The accepted next technical responsibility is **Increment 5 — application integration**: carry the new runtime dependency-state result through the normal investigation path while preserving existing CI-coverage and action semantics.

Increment 5 is **SELECTED NEXT BUT NOT STARTED**. Its A0 must begin in a new cycle only after the current STOP boundary is deliberately left.

No blocking gap remains from Increment 4.
