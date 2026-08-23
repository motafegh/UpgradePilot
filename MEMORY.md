# UpgradePilot Current Memory

**Last updated:** 2026-08-23  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable implementation-retention rule

Existing code is evidence to inspect, not authority to preserve.

For any material field/check/type/helper/abstraction/metadata propagation/compatibility or defensive mechanism:

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ keep the smallest adequate owner
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, do not decide ownership from the local file alone. Trace the admitted producer → integration/orchestration → consumer path and identify the earliest sufficient owner. A later repeat requires its own reason: an independently supported boundary, independently combinable evidence branches, a distinct domain/cross-object proposition, or a material risk not already controlled upstream. Direct internal callability and fabricated fixtures are not retention authority unless that alternate route is explicitly supported.

Canonical owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Plan position:** **R0 COMPLETE; R1 IN PROGRESS**.
- **R1 Step 1:** implemented on migration branch; not execution-validated.
- **R1 Step 2A:** superseded into the coherent Step-2B source-provenance contract.
- **R1 Step 2B responsibility trace:** complete.
- **R1 Step 2B code migration:** **IMPLEMENTED + STATICALLY REVIEWED; NOT EXECUTION-VALIDATED**.
- **R1 Step 2C:** **NEXT — inspect/migrate `dependency/uv_membership.py` composition ownership**.
- **R2:** not started.
- **Latest progressive record:** `working-memory/2026-08-23_B2-R1-step2b-implementation-and-step2c-handoff.md`.
- Dedicated B2 mastery learning package remains paused while its source contracts are being reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is SCHEDULED.** Its activation trigger is successful R7 acceptance/validation of the current reconciliation.
- **Mandatory post-R7 next checkpoint:** `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as an early B2/X1 checkpoint. It must reach an explicit evidence-backed `ADOPT`, `RETAIN AS PILOT`, `REJECT`, or `DEFER/RESCHEDULE` disposition before old Cluster 6 or another ordinary B2 continuation can become live.

The migration branch and `main` remain divergent in Git history because durable governance was promoted separately while product-source work remains isolated. Reconcile that history before eventual integration; do not treat divergence itself as product failure.

## Validation state

Local WSL execution is temporarily unavailable.

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

No later governance, memory, design, or migration-branch commit supersedes that runtime proof.

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

Removed durable exact-file metadata:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

GitHub acquisition owns external response validation. Strong exact-file types own structural locator/content invariants. Downstream layers own only their actual semantic or independently necessary composition relationships.

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

End-to-end trace established the admitted flow:

```text
investigate_public_pull_request
→ PullRequestIdentity + changed files
→ analyze_dependency_change
→ source role/status admission
→ exact base/head acquisition using one identity + one changed-file path
→ strong RepositoryTextFile evidence
→ uv/pyproject semantic extractor
```

The resulting source-provenance contract is:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Removed from this record:

```text
base_revision
head_revision
blob identifiers
byte counts
```

Canonical ownership now remains:

```text
PullRequestIdentity
→ PR repository/base/head identity

RepositoryTextFile
→ exact repository/path/revision/content

DependencyChangeSourceEvidence
→ dependency source path/format/extraction method

DependencySourceContext
→ exact-head repository/revision when later composition needs it
```

### Additional implementation finding

After duplicate path/status/repository checks were removed, `ChangedFile` no longer supplied an independent semantic fact to the exact-file extractors. It existed only to copy the already-admitted filename into source provenance.

Therefore:

```text
orchestration context != semantic input
```

and the exact-file semantic APIs were narrowed to:

```python
extract_uv_lock_changes(base_file, head_file)
extract_pyproject_optional_extra_change(base_file, head_file)
```

Their source-evidence path comes from the already-admitted exact HEAD file. `analysis.py` remains the owner of changed-file role/status admission and exact acquisition.

### Step-2B implementation commits recorded

```text
34b577b54a855f50eacc3eca3d6b0d8426f542a3
→ analysis caller narrowed to exact-file semantic inputs

c19012359be6986fdc19f0c105b76bf5bb40a2bd
→ uv-lock extractor narrowed to source semantics

267bd2d96ff0bd27608b6070fb582d2f0075ad8c
→ pyproject extractor narrowed to source semantics

f3e9c01aa4d4f2ff7e98a02f44dd0ea4df6aec35
→ shared source-contract tests

0def155a62a327a015820d2a502d82cc8d6ceab8
→ pyproject semantic tests

11bcef2fd40efca30c63f61e9fc11e3133f0a754
→ uv versionless semantic tests

01a8499eda33ed09f6343ce51733835e6f9e3415
→ main uv semantic tests
```

Current `change.py`, dependency-analysis integration tests, pyproject integration tests, and CLI presentation are also aligned with the minimal source-provenance contract. The CLI already presents PR base/head from `PullRequestIdentity` and each dependency source only as path/format/extraction method.

No intentional uv parser/comparison or PEP-508/optional-extra semantic rule was changed.

## Exact next bounded step — R1 Step 2C

Inspect and reconcile `src/upgradepilot/dependency/uv_membership.py` before editing it.

Unlike the Step-2B exact-file extractors, uv membership composes separate evidence branches:

```text
UvLockDependencyContext
+ workflow-derived ProjectEnvironmentSelectionDeclaration
+ exact pyproject.toml
+ exact uv.lock
```

Current known old-contract pressure includes:

```text
ExactRepositoryFileEvidence alias
returned_path checks
blob/count checks
source_evidence.head_revision rebinding
```

Step 2C must apply the same end-to-end responsibility trace but **must not mechanically delete every relationship check**. Keep only cross-branch repository/revision/path/project-root relations that genuinely establish the composition proposition; remove provider-internal or circular copied-field checks.

Key contrast:

```text
same controlled producer path
→ repeated relation often redundant

independently assembled evidence branches
→ relation may be the actual proof of coherent composition
```

Do not redesign traversal or uv membership semantics yet; R2/R4 own the later structural-model/reachability redesign.

## Scheduled post-R7 AI/LLM engineering checkpoint

The current reconciliation remains the immediate engineering responsibility, but the AI/LLM work has an explicit route position rather than indefinite deferral.

```text
R1 → R2 → R3 → R4 → R5 → R6 → R7
→ freeze accepted deterministic baseline
→ B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN Phase 0
→ fresh AI/LLM engineering reassessment + route/baseline check
→ Phases 1–6 if still justified
→ explicit disposition
→ Phase 7 only if adopted
→ then choose ordinary B2 continuation
```

Phase 0 must refresh current model/tool-calling/structured-output/agent-evaluation/security evidence, re-check ADR-0006 triggers, and explicitly classify current/planned AI roles before model experimentation. The checkpoint may reject or reschedule itself on evidence, but it may not be silently skipped.

## Deferred validation ledger

When WSL/laptop access returns:

```text
Step 1 provider/type focused tests
→ Step 2B dependency source/analysis focused tests
→ Step 2C membership focused tests once implemented
→ later R1 Target/upstream migrations
→ nearest integration/end-to-end tests
→ full deterministic suite
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
orchestration context != semantic input
scheduled responsibility != indefinite deferral
```

Engineering authority comes from admitted responsibilities, full producer/consumer flow, proof boundaries, material risk, and the simplest adequate mechanism—not from historical code or test convenience.
