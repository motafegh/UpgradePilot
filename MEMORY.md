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
- **R1 current blocker / next bounded responsibility:** `src/upgradepilot/target/python.py` still consumes the retired `blob_sha` exact-file contract; `tests.test_target_python` fails 8/8 before semantic coverage can run.
- **R2:** not started.
- **Current progressive runtime record:** `working-memory/2026-08-23_B2-R1-local-runtime-validation-checkpoint.md`.
- Dedicated B2 mastery learning package remains paused while source contracts are reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is SCHEDULED.** Successful R7 acceptance/validation activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as the mandatory next B2/X1 checkpoint before ordinary B2 continuation.

The migration branch and `main` remain divergent in Git history because durable governance and product-source migration were promoted separately. Reconcile history only after the current migration branch is internally runtime-green; do not use destructive ref operations and do not create another migration branch.

## Validation state

Local WSL execution became available on 2026-08-23 and the deferred validation ladder was started before any `main` reconciliation.

Focused runtime evidence now recorded:

```text
Gate 1 — exact-file provider/type
  tests.test_github_repository
  tests.test_exact_commit_repository_files
  → 13 tests / OK

Gate 2 — dependency exact-file extraction
  focused dependency contract/uv-lock/pyproject tests
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

Confirmed blocker:

```text
tests.test_target_python
→ 8 tests / 8 errors
→ stale RepositoryTextFile(blob_sha=...) fixtures
→ stale UnavailableRepositoryFile fixture missing repository
→ production target/python.py still propagates evidence.blob_sha
```

Full standard-suite inventory:

```text
507 tests
FAILED (failures=5, errors=51)
```

Interpretation: this is not 56 independent product defects. The focused gates establish large migrated surfaces as runtime-green. The full-suite result is a remaining-contract fan-out inventory; diagnose by earliest stale responsibility instead of patching terminal failures individually.

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

Removed from Target:

```text
_validate_exact_file_provenance(...)
insufficient_file_provenance problem state
workflow_blob_sha
returned-path / byte-count / retrieved-at dependency
```

Retained durable Target provenance:

```text
repository + immutable revision + workflow_path
```

Reason: the derived Target evidence may outlive its source object and needs the smallest exact source locator. This is domain provenance, not provider transport metadata.

Retained independent semantic validation:

```text
repository_relative_parts(dependency_source_file)
```

because `dependency_source_file` is a separate plain/domain input, not an invariant already owned by `RepositoryTextFile`.

Target semantic behavior was intentionally unchanged: runner/setup-python interpretation, job/reusable/matrix/container boundaries, direct-install observation, and `exact_wheel_compatibility_state="unresolved"` remain intact.

Detailed records:

```text
working-memory/2026-08-23_B2-R1-target-artifact-environment-responsibility-trace.md
working-memory/2026-08-23_B2-R1-target-artifact-environment-implementation.md
```

### Tagged upstream changelog exact source

Normal flow:

```text
DependencyReleaseInterval
+ selected upstream repository
→ resolve proposed tag
→ discover changelog at resolved commit
→ acquire RepositoryTextFile at same repository/commit/path
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence
```

The composer is a controlled packaging stage, not an independently supplied tag/file boundary. Repeated tag/file acquisition joins were therefore removed there.

Final durable domain evidence:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

The successful type owns its intrinsic repository/commit/path/content invariants. Later authority/window composition retains the real independent joins:

```text
CrossedReleaseIndexEvidence.repository/interval
↔ TaggedChangelogEvidence.repository/interval
```

Removed provider/acquisition propagation includes tag object/ref details, returned path, blob SHA, byte counts, and retrieval time. `CrossedReleaseSourceWindow` also no longer propagates blob SHA. Markdown selection, line/offset grounding, semantic extraction, and ADR-0006 local-model authority boundaries remain unchanged.

Detailed records:

```text
working-memory/2026-08-23_B2-R1-tagged-changelog-responsibility-trace.md
working-memory/2026-08-23_B2-R1-tagged-changelog-implementation.md
```

## Exact next bounded R1 continuation

Do **not** jump to R2 and do **not** merge current `main` yet.

Next consumer:

```text
src/upgradepilot/target/python.py
```

Confirmed stale contract:

```text
TargetPythonDeclaration.blob_sha
TargetPythonDeclarationProblem.blob_sha
RepositoryTextFile.blob_sha propagation
```

Normal application path already visible:

```text
grounded upstream support-drop claim
→ impact assessment selects exact target pyproject.toml path at PR head
→ repository_client.get_exact_head_text_file(...)
→ RepositoryFileEvidence
→ interpret_target_python_declaration(...)
→ TargetPythonEvidence
→ evaluate_target_python_relevance(...)
```

Before editing, trace:

1. exact Target-Python proposition: `[project].requires-python` from exact-head `pyproject.toml`;
2. which source locator facts the derived declaration/problem needs after the source object is gone;
3. whether `blob_sha` establishes any independent Target-Python proposition (current evidence strongly suggests no);
4. whether repository identity should be preserved alongside path + immutable revision for the same reason Target artifact-environment keeps a minimal exact source locator;
5. whether `_TARGET_PATH == "pyproject.toml"` is a semantic role check that remains justified;
6. immediate consumers (`target/relevance.py`, impact orchestration, CLI/tests) that rely on the result contract.

Do not patch all 51 errors/5 failures independently. Fix this earliest confirmed stale contract, migrate its direct consumers/tests, statically review, then rerun focused/downstream tests when local execution is next available.

## Deferred validation / integration order

```text
finish remaining R1 exact-file migrations
→ focused tests for each migrated family
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
working memory = execution consistency check, not only history
scheduled responsibility != indefinite deferral
```
