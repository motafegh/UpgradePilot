# UpgradePilot Current Memory

**Last updated:** 2026-08-23  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable engineering rule

Existing implementation is evidence to inspect, not authority to preserve.

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ locate earliest sufficient owner
→ keep the smallest adequate mechanism
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, trace producer → integration/orchestration → consumer before deciding local ownership. A downstream repeat needs its own current reason: an independently supported boundary, independently combinable evidence branches, a distinct domain/cross-object proposition, or a material risk not already controlled upstream. Direct internal callability and fabricated fixtures are not retention authority unless that alternate route is explicitly supported.

Canonical owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Plan position:** **R0 COMPLETE; R1 IN PROGRESS**.
- **R1 Step 1:** strong exact-file owner implemented and focused-runtime green.
- **R1 Step 2B:** dependency exact-file semantic extractors migrated + statically reviewed + focused-runtime green.
- **R1 Step 2C:** uv-membership composition migrated + statically reviewed + focused-runtime green.
- **R1 Target artifact-environment migration:** complete + statically reviewed + focused-runtime green.
- **R1 tagged-changelog/upstream exact-source migration:** complete + statically reviewed + focused-runtime green.
- **R1 Target-Python migration:** complete + statically reviewed; post-change runtime validation pending.
- **R1 CI/workflow fixture fan-out migration:** complete + statically reviewed; no production CI redesign was required; post-change runtime validation pending.
- **R1 integration / Step-7F / live-tool fan-out migration:** complete + statically reviewed; no production orchestration or model-boundary change was required; post-change runtime validation pending.
- **R1 pull-request provider-test reconciliation:** complete + statically reviewed; obsolete provider-size/blob representation tests removed while actual encoded/decoded bounds remain protected by the shared provider suite; post-change runtime validation pending.
- **R1 current continuation:** larger branch-specific residual-contract closure audit across remaining standard-test/tool consumers; production change only if a surviving product proposition actually requires it.
- **R2:** not started.
- **Current progressive implementation record:** `working-memory/2026-08-23_B2-R1-integration-provider-tool-fanout-implementation.md`.
- **Current runtime checkpoint:** `working-memory/2026-08-23_B2-R1-local-runtime-validation-checkpoint.md`.
- Dedicated B2 mastery learning package remains paused while source contracts are reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is SCHEDULED.** Successful R7 acceptance/validation activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as the mandatory next B2/X1 checkpoint before ordinary B2 continuation.

The migration branch and `main` remain divergent in Git history because durable governance and product-source migration were promoted separately. Reconcile history only after the current migration branch is internally runtime-green; do not use destructive ref operations and do not create another migration branch.

## Validation state

Local WSL execution became available on 2026-08-23 and the deferred validation ladder was started before any `main` reconciliation.

Focused runtime evidence recorded before the latest Target-Python and residual-fan-out edits:

```text
Gate 1 — exact-file provider/type
  → 13 tests / OK

Gate 2 — dependency exact-file extraction
  → PASS

Gate 3 — uv composition + Target artifact environment
  → 34 tests / OK

Gate 4 — tagged changelog / upstream authority / bounded semantic pipeline
  → 88 tests / OK

source topology
  → 3 tests / OK

experiments/tests
  → 27 tests / OK

compileall src + tests + Step-6C smoke
  → exit 0
```

The pre-change Target-Python focused run produced:

```text
tests.test_target_python
→ 8 tests / 8 errors
→ stale RepositoryTextFile(blob_sha=...) fixtures
→ stale UnavailableRepositoryFile fixture missing repository
→ production target/python.py still propagated evidence.blob_sha
```

That blocker has been migrated and statically reviewed, but has not yet been rerun locally after the edit.

Subsequent residual fan-out work migrated:

```text
5 CI/workflow test files
2 application integration/end-to-end test files
2 S001 developer live-proof tools
1 PR-specific provider test suite
```

These later edits also await runtime rerun.

Full standard-suite inventory before these fixes:

```text
507 tests
FAILED (failures=5, errors=51)
```

Interpretation: this is not 56 independent product defects. Focused gates establish large migrated surfaces as runtime-green. The full-suite result is a remaining-contract fan-out inventory; diagnose by earliest stale responsibility instead of patching terminal failures individually. It must not be reused as a current post-fix result after later fixture/tool migrations.

Latest historical full accepted product-runtime validation remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

The newer focused runtime gates materially strengthen current evidence, but the historical full-suite proof is not superseded until the migration branch itself returns to a green full suite.

## Stable proof guards

```text
dependency transition
!= explicit-root/environment membership evidence
!= static environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime execution/success
!= exact-version witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

remain controlling.

## R1 strong exact-file contract

Successful exact repository text:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Provider/acquisition metadata not retained durably:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

GitHub acquisition owns external response validation. Strong exact-file types own structural locator/content invariants. Downstream layers own only their actual semantics or independently necessary composition relationships.

## Completed R1 migration lessons

### Controlled-route dependency extractors

```text
PullRequestIdentity + ChangedFile
→ dependency/analysis.py admission
→ exact base/head acquisition
→ uv_lock.py / pyproject.py semantic extraction
```

Final dependency source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

`ChangedFile` was removed from source-specific semantic extractor APIs after upstream admission made it non-semantic orchestration context.

### Independent uv-membership composition

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml
+ exact lock source
→ bounded membership result
```

Provider/circular checks were removed, but real cross-branch repository/revision/source-path/project-root joins remain because independently valid evidence can still be incoherent when combined.

### Target artifact-environment consumer

Admitted flow:

```text
one RepositoryFileEvidence workflow source
+ independent dependency_source_file
→ provider-owned workflow IR
→ partial Target facts
```

Removed provider-metadata revalidation and `workflow_blob_sha`; retained `repository + revision + workflow_path` as minimal derived-domain source provenance and retained independent `dependency_source_file` semantic validation.

### Tagged upstream changelog exact source

Final durable evidence:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

The successful type owns intrinsic locator/content validity. Later authority/window composition retains only the genuine independent repository/interval joins. Blob/byte/returned-path/retrieval metadata and tag-object/ref details are not propagated.

### Target Python exact source

Normal flow:

```text
grounded support-drop claim
→ impact candidate(target_repository, target_revision)
→ exact target-declaration investigation selection
→ selection repository/revision checked against PR identity
→ exact-head pyproject.toml acquisition
→ interpret_target_python_declaration(...)
→ TargetPythonEvidence
→ target relevance
→ impact composition
```

Final successful evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

Final problem evidence:

```text
TargetPythonDeclarationProblem
├── state
├── path
├── revision
└── detail
```

Removed `blob_sha` from domain evidence and CLI presentation. Did not add repository because the current normal route already binds target repository through PR/impact identity and no later independent Target-Python repository proposition requires a duplicate field.

Retained the semantic source-role check `evidence.path == "pyproject.toml"` and the real later composition invariant `target_evidence.revision == candidate.target_revision`.

### CI/workflow fixture fan-out

Production trace:

```text
RepositoryTextFile
→ github/workflow_definition.py
→ WorkflowDefinition
→ ci/workflow_commands.py
→ static dependency evidence
→ ci/dependency_exercise.py
```

The production modules already use the current strong contract correctly and retain genuine cross-object checks such as workflow revision ↔ runtime head and external-consumption workflow path/revision ↔ current workflow.

Therefore the residual problem was fixture construction, not production architecture.

Migrated tests:

```text
tests/test_github_workflow_definition.py
tests/test_workflow_commands.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_exercise.py
tests/test_ci_dependency_coverage.py
```

Fixture changes:

```text
RepositoryTextFile: add repository, remove blob_sha
UnavailableRepositoryFile: add repository
DependencyChangeSourceEvidence: remove copied head_revision
```

All existing semantic assertions were retained, including S001/S011 behavior and CI static/runtime proof separation.

### Integration / Step-7F / live-tool fan-out

Application integration path remains:

```text
dependency transition
→ upstream interval authority
→ exact tagged changelog
→ bounded source window
→ semantic candidate extraction
→ deterministic grounding
→ conditional target acquisition
→ target relevance
→ impact applicability
```

`tests/test_investigation.py` and `tests/test_step7f_end_to_end.py` now construct only the strong exact-file contract. Their orchestration, activation, and model-trust assertions are unchanged.

Developer S001 tools were migrated to display durable exact source locators:

```text
repository@resolved_commit_sha:path
```

instead of deleted blob/count fields. Diagnostic convenience is not a reason to enlarge durable product evidence.

### PR provider-test reconciliation

`tests/test_pull_request_repository_files.py` now owns only PR-specific wrapper responsibilities:

```text
base wrapper → PR base SHA
head wrapper → PR head SHA
minimum durable RepositoryTextFile
404 exact locator
shared provider path/UTF-8 admission on the PR route
```

Generic base64/bounds/type invariants remain owned by `tests/test_exact_commit_repository_files.py`.

Provider size protection now rests on actual data processed:

```text
bound compact encoded base64 before decode
→ strict base64 decode
→ bound actual decoded bytes
→ UTF-8 decode
```

rather than trusting a separate GitHub-reported `size` field.

Detailed latest records on the migration branch:

```text
working-memory/2026-08-23_B2-R1-integration-live-tool-fanout-trace.md
working-memory/2026-08-23_B2-R1-pull-request-provider-test-reconciliation.md
working-memory/2026-08-23_B2-R1-integration-provider-tool-fanout-implementation.md
```

## Exact next bounded R1 continuation

Do **not** jump to R2 and do **not** merge current `main` yet.

Next step is a larger branch-specific residual-contract closure audit across remaining standard-test and tool consumers.

Rules:

```text
default-branch code-search hit
!= current migration-branch fact

branch-specific stale fixture/tool
→ migrate to current contract

branch-specific production consumer
→ trace producer → orchestration → consumer before editing

no surviving proposition
→ do not restore retired metadata
```

High-probability neighboring suites already spot-checked as current on the migration branch:

```text
tests/test_dependency_change_contracts.py
tests/test_target_artifact_environment.py
tests/test_uv_lock_change.py
tests/test_upstream_interval_acquisition_integration.py
```

After the residual static closure audit, the highest-value next proof is accumulated local execution:

```text
Target-Python family
+ CI/workflow family
+ investigation / Step-7F integration
+ PR provider suite
→ full standard suite
```

If the migration branch is fully green, then merge current `origin/main` INTO THE SAME branch, resolve non-destructively, and rerun affected + full validation before considering R1 complete.

## Deferred validation / integration order

```text
finish remaining R1 exact-file residual audit
→ accumulated focused tests
→ current migration branch full suite green
→ merge current origin/main INTO SAME branch
→ resolve non-destructively
→ rerun affected focused/integration tests
→ full deterministic suite
→ only then consider R1 closure / R2 entry
```

No second migration branch is justified.

## Scheduled post-R7 AI/LLM checkpoint

```text
R1 → R2 → R3 → R4 → R5 → R6 → R7
→ freeze accepted deterministic baseline
→ scheduled B2/X1 AI/agentic checkpoint Phase 0
→ refreshed current AI/LLM engineering reassessment
→ proceed / reject / defer-reschedule
→ bounded planner comparison if justified
→ explicit disposition
→ only then ordinary B2 continuation
```

The checkpoint is mandatory; adoption is not.

## Learning state

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship
real proposition != local ownership
normal controlled composition != independent evidence-branch composition
orchestration context != semantic input
same-looking relation + different composition boundary → different ownership decision
derived-domain provenance != copying every provider field
successful evidence type should own intrinsic validity
full-suite failures after contract migration are pressure inventory, not automatic independent bugs
test fixture mismatch != reason to restore deleted production fields
diagnostic convenience != evidence-retention requirement
test suite responsibility != duplicate every lower-layer mechanism
resource protection should bind actual processed data, not merely provider-reported metadata
working memory = execution consistency check, not only history
scheduled responsibility != indefinite deferral
```
