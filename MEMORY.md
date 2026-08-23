# UpgradePilot Current Memory

**Last updated:** 2026-08-23  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable implementation-retention rule

Existing implementation is evidence to inspect, not authority to preserve.

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ keep the smallest adequate owner
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, trace the admitted producer → integration/orchestration → consumer flow before deciding local ownership. A later repeat needs its own current reason: an independently supported boundary, independently combinable evidence branches, a distinct cross-object/domain proposition, or a material risk not already controlled upstream. Direct internal callability and fabricated fixtures are not retention authority unless that alternate route is explicitly supported.

Canonical owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Plan position:** **R0 COMPLETE; R1 IN PROGRESS**.
- **R1 Step 1:** implemented on migration branch; not execution-validated.
- **R1 Step 2A:** superseded intermediate provenance shape; its remaining revision fields were removed in Step 2B.
- **R1 Step 2B responsibility trace:** **COMPLETE**.
- **R1 Step 2B code migration:** **IMPLEMENTED + STATICALLY REVIEWED; NOT EXECUTION-VALIDATED**.
- **R1 Step 2C:** **NEXT — uv membership exact-source/composition reconciliation**.
- **R2:** not started.
- **Current progressive implementation record:** `working-memory/2026-08-23_B2-R1-step-2b-implementation.md` on the migration branch.
- Parent R1 reasoning record: `working-memory/2026-08-23_B2-R1-exact-file-contract-migration-continuation.md`.
- Dedicated B2 mastery learning package remains paused while source contracts are reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is SCHEDULED.** Successful R7 acceptance/validation activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as the mandatory next B2/X1 checkpoint before ordinary B2 continuation.

The migration branch and `main` have diverged in Git history because durable governance was promoted to `main` while product-source work remains isolated. Reconcile history before eventual integration; do not treat divergence itself as product failure and do not use destructive ref operations.

## Validation state

Assistant-side local WSL execution is unavailable for the current migration work.

```text
bounded implementation
→ static/source review
→ explicit NOT EXECUTION-VALIDATED marker
→ progressive working-memory record
→ later focused + integration + full local execution
```

**Latest accepted product-runtime validation remains:**

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

## R1 exact-file direction

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

Provider/acquisition metadata that did not earn durable exact-file retention:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

GitHub acquisition owns external response validation. Strong exact-file types own structural locator/content invariants. Downstream layers own only their actual semantics or independently necessary composition relationships.

## R1 Step 1 — implemented / unvalidated

Migration-branch commits:

```text
709aba4cdab1fd666579f90cbe6a5e974cad8626
→ strong exact repository-file contract/provider boundary

e88b1e21e3b1efd09c226b5ca1512230f6477057
74fd3aaede37b15cb2eedbfda41128bc4d81f46c
→ nearest provider/construction tests migrated
```

Resource protection remains based on bounded encoded input plus bounded actual decoded bytes.

## R1 Step 2B — implemented / statically reviewed / unvalidated

The completed end-to-end trace established this normal ownership chain:

```text
PullRequestIdentity + ChangedFile
→ dependency/analysis.py admits source path/status
→ GitHubRepositoryClient acquires base/head from the same PR identity + requested path
→ RepositoryFileEvidence
→ uv_lock.py / pyproject.py semantic extraction
→ minimal DependencyChangeSourceEvidence
```

Final source provenance contract:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

PR repository/base/head identity stays with `PullRequestIdentity`; exact file path/revision/content stays with `RepositoryTextFile`; exact-head repository/revision needed by later composition stays with `DependencySourceContext` constructed from PR identity.

### Extractor boundary after Step 2B

Final exact-file semantic entry shapes are:

```python
extract_uv_lock_changes(base_file, head_file)
extract_pyproject_optional_extra_change(base_file, head_file)
```

The extractors retain:

- typed exact-file unavailability;
- actual uv / PEP 621 / PEP 508 parsing and conservative comparison semantics;
- minimal source provenance.

They no longer repeat:

- changed-file path/status admission;
- base/head repository equality;
- ChangedFile↔exact-file path rebinding;
- returned-path checks;
- revision/blob/byte provider/invariant checks.

`dependency/analysis.py` remains the owner of source admission and PR-bound base/head acquisition. Its integration tests continue to protect those relationships at that owner.

`cli.py` was also migrated because it directly rendered the removed dependency-source revision/blob/byte fields. Dependency evidence presentation now prints path, format, and extraction method; PR base/head identity is already rendered from `PullRequestIdentity`.

Static diff review found no intended changes to uv schema/package-record/versionless/repeated-record comparison semantics or pyproject optional-extra/PEP-508 comparison semantics.

Detailed implementation record: `working-memory/2026-08-23_B2-R1-step-2b-implementation.md`.

## Exact next bounded step — R1 Step 2C

Inspect and migrate `src/upgradepilot/dependency/uv_membership.py` as a genuine **independent evidence-composition boundary**.

Current stale exact-file/provenance pressure there includes:

```text
ExactRepositoryFileEvidence alias
returned_path checks
blob SHA checks
reported/decoded byte checks
source_evidence.head_revision / head_blob_sha / head_byte_count rebinding
```

These should be pressured for removal under the Step-2B contract.

But do **not** mechanically remove every relationship check. Membership composes independently produced:

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml
+ exact uv.lock
```

Therefore context repository/revision ↔ exact project/lock files, dependency source path ↔ lock path, and declaration project-root ↔ project-file location may remain real composition propositions if the end-to-end trace shows this layer must establish them.

Do not redesign uv traversal/reachability semantics in Step 2C. R2/R4 own the later shared lock-model and reachability proposition reconciliation.

## Scheduled post-R7 AI/LLM engineering checkpoint

```text
R1 → R2 → R3 → R4 → R5 → R6 → R7
→ freeze accepted deterministic baseline
→ scheduled B2/X1 AI/agentic checkpoint Phase 0
→ refreshed current AI/LLM engineering reassessment
→ proceed / reject / defer-reschedule
→ bounded planner comparison if still justified
→ explicit disposition
→ only then ordinary B2 continuation
```

The checkpoint is mandatory; adoption is not. Phase 0 must refresh current model/tool-calling/structured-output/agent-evaluation/security evidence, re-check ADR-0006 triggers, and classify current/planned AI roles rather than blindly executing an old plan.

## Deferred validation ledger

When local WSL execution is available:

```text
Step 1 provider/type focused tests
→ Step 2B dependency contract/extractor/integration tests
→ Step 2C membership/composition tests
→ later Target/upstream migrations
→ nearest integration/end-to-end tests
→ full deterministic suite
```

Step-2B focused slice includes at least:

```text
tests.test_dependency_change_contracts
tests.test_uv_lock_change
tests.test_uv_lock_versionless_records
tests.test_pyproject_optional_extra_change
tests.test_dependency_analysis
tests.test_pyproject_dependency_analysis
tests.test_dependency_environment
```

Diagnose failures against the earliest relevant bounded step rather than patching only to make the final suite green.

## Learning state

Current R1 mental models:

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship
legitimate relationship != re-check at every layer
real proposition != local ownership
normal controlled composition != independent evidence-branch composition
removing a duplicate check != removing the invariant
scheduled responsibility != indefinite deferral
```

Engineering authority comes from admitted responsibilities, full producer/consumer flow, proof boundaries, material risk, and the simplest adequate mechanism—not from historical code or test convenience.
