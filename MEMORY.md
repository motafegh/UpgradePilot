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

For cross-layer mechanisms, trace producer → integration/orchestration → consumer before deciding local ownership. A downstream repeat needs its own reason: an independently supported boundary, independently combinable evidence branches, a distinct cross-object/domain proposition, or a material risk not already controlled upstream. Direct internal callability and fabricated fixtures are not retention authority unless that alternate route is explicitly supported.

Canonical owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Plan position:** **R0 COMPLETE; R1 IN PROGRESS**.
- **R1 Step 1:** implemented; not execution-validated.
- **R1 Step 2A:** superseded into the coherent Step-2B provenance contract.
- **R1 Step 2B trace + code migration:** **COMPLETE / STATICALLY REVIEWED / NOT EXECUTION-VALIDATED**.
- **R1 Step 2C trace + code migration:** **COMPLETE / STATICALLY REVIEWED / NOT EXECUTION-VALIDATED**.
- **R1:** still in progress; later Target/upstream exact-file consumers remain to be traced/migrated one bounded responsibility at a time.
- **R2:** not started.
- **Current progressive record:** `working-memory/2026-08-23_B2-R1-step-2c-implementation.md` on the migration branch.
- Step-2C reasoning record: `working-memory/2026-08-23_B2-R1-step-2c-responsibility-trace.md` on the migration branch.
- Step-2B implementation record: `working-memory/2026-08-23_B2-R1-step-2b-implementation.md` on the migration branch.
- Dedicated B2 mastery learning package remains paused while source contracts are reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is SCHEDULED.** Successful R7 acceptance/validation activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as the mandatory next B2/X1 checkpoint before ordinary B2 continuation.

The migration branch and `main` remain divergent in Git history because durable governance and product-source migration were promoted separately. Reconcile history before eventual integration; do not use destructive ref operations.

## Validation state

Assistant-side local WSL execution is unavailable for the current migration work.

```text
bounded implementation
→ static/source review
→ explicit NOT EXECUTION-VALIDATED marker
→ progressive working-memory record
→ later focused + integration + full local execution
```

Latest accepted product-runtime validation remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

No later governance, design, memory, static review, or migration-branch commit supersedes that runtime proof.

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

## R1 exact-file contract

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

## R1 Step 2B — controlled-route semantic extractors

Normal ownership chain:

```text
PullRequestIdentity + ChangedFile
→ dependency/analysis.py source role/status admission
→ exact base/head acquisition using same PR identity + requested path
→ RepositoryFileEvidence
→ uv_lock.py / pyproject.py semantic extraction
→ minimal DependencyChangeSourceEvidence
```

Final source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Exact-file semantic entry points are now:

```python
extract_uv_lock_changes(base_file, head_file)
extract_pyproject_optional_extra_change(base_file, head_file)
```

`ChangedFile` was removed from these semantic APIs because it supplied no independent semantic fact after upstream admission.

## R1 Step 2C — independent evidence composition

`evaluate_uv_selected_environment_membership(...)` is a materially different boundary. It combines independently produced:

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml
+ exact lock source
```

Final exact-source arguments:

```python
project_file: RepositoryFileEvidence
lock_file: RepositoryFileEvidence
```

### Removed

```text
ExactRepositoryFileEvidence alias
repeated structural path validation already owned by RepositoryTextFile
separate lock-basename recheck after retaining the stronger source-path join
returned_path checks
source_evidence.head_revision rebinding
source-evidence blob/byte rebinding
exact-file blob existence checks
reported-vs-decoded byte consistency checks
```

### Retained

```text
declaration.manager == uv
explicit positive selector requirement
typed project/lock unavailability
project file has pyproject.toml semantic role
project_file.repository/revision == context.repository/revision
lock_file.repository/revision == context.repository/revision
lock_file.path == context.source_evidence.path
declaration.project_root == exact project-file root
```

Why: these retained relations join independently valid evidence branches. Removing them could bind dependency evidence from one repository/revision/lock source/project root to another and manufacture membership.

The test suite was migrated accordingly: provider metadata fixtures were removed; the obsolete blob mismatch test was replaced with real repository/revision/source-path/project-root/unavailability composition cases. Existing S001 witness, ambiguity, marker, cycle, repeated-record, selected-root, and nested-workspace behavior was preserved by static inspection.

No uv parser/traversal semantic redesign belongs to Step 2C. AUDIT-007/R2–R4 still own shared lock structure, `--all-packages`, project-content necessity, `not_established` completeness, and reachability naming.

Detailed implementation record: `working-memory/2026-08-23_B2-R1-step-2c-implementation.md` on the migration branch.

## Exact next bounded R1 continuation

Do **not** jump directly to R2 yet.

Remaining exact-file pressure still exists in other consumers, especially Target/upstream paths. Search results or old field names are only migration pressure, not deletion authority.

Next step:

```text
choose one remaining materially different exact-file consumer
→ trace its admitted proposition and producer/consumer ownership
→ classify each old metadata/revalidation mechanism
→ migrate only the justified bounded surface
→ static review + working-memory record
```

Likely pressure includes upstream interval/changelog evidence and target artifact-environment evidence, but the next consumer must be selected by current responsibility/proof relevance rather than bulk search-and-replace.

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

## Deferred validation ledger

When local WSL execution is available:

```text
Step 1 provider/type focused tests
→ Step 2B dependency contract/extractor/integration tests
→ Step 2C membership/composition tests
→ later R1 Target/upstream migrations
→ nearest integration/end-to-end tests
→ full deterministic suite
```

Step-2C focused tests include at least:

```text
tests.test_uv_selected_environment_membership
tests.test_uv_membership_universal_lock_boundary
```

Diagnose failures against the earliest relevant bounded responsibility rather than patching only to make the final suite green.

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
working memory = execution consistency check, not only history
scheduled responsibility != indefinite deferral
```
