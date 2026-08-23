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
- **R1 Step 2A:** intermediate implementation; blob/byte fields removed, but revision retention has now been superseded by the Step-2B trace.
- **R1 Step 2B responsibility trace:** **COMPLETE**.
- **R1 Step 2B code migration:** **NEXT; NOT STARTED**.
- **R1 Step 2C:** not started.
- **R2:** not started.
- **Progressive record:** `working-memory/2026-08-23_B2-R1-exact-file-contract-migration-continuation.md` on the migration branch, continuing the August 22 reconciliation record.
- Dedicated B2 mastery learning package remains paused while its source contracts are being reconciled.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration is now SCHEDULED, not deferred.** Its activation trigger is successful R7 acceptance/validation of the current reconciliation.
- **Mandatory post-R7 next checkpoint:** `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` as an early B2/X1 checkpoint. It must reach an explicit evidence-backed `ADOPT`, `RETAIN AS PILOT`, `REJECT`, or `DEFER/RESCHEDULE` disposition before old Cluster 6 or another ordinary B2 continuation can become live.

The migration branch and `main` have diverged in Git history because durable governance was promoted to `main` while product-source work remains isolated. Reconcile that history before eventual integration; do not treat divergence itself as product failure.

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

## R1 Step 2B responsibility-trace conclusions

Normal admitted flow:

```text
investigate_public_pull_request
→ PullRequestIdentity + changed files from that PR
→ analyze_dependency_change(identity, changed_files, repository_client)
→ same ChangedFile.filename passed to base/head acquisition
→ repository provider uses identity.repository + base/head SHA + requested path
→ strong RepositoryTextFile
→ uv/pyproject semantic extractor
```

`repository_relative_parts()` is strict and spelling-preserving, so path admission does not silently normalize a different path.

### Decisions

**Repository equality in `uv_lock.py` / `pyproject.py`**

```text
REMOVE local repeat
```

The same `PullRequestIdentity` already supplies both acquisitions from one repository. No second admitted product composition route for these extractors was found.

**Base/head path == ChangedFile path in those extractors**

```text
REMOVE local repeat
```

`analysis.py` admits the changed-file path, passes the same exact spelling to both acquisitions, and the repository provider validates GitHub's returned path against the request.

**Repeated path-role / modified-status admission inside the exact-file extractors**

```text
REMOVE or narrow during Step 2B
```

`analysis.py` already owns PR-wide source admission before exact-file acquisition. Direct unit-test calls are migration pressure, not an independent product boundary.

**`base_revision` / `head_revision` in `DependencyChangeSourceEvidence`**

```text
REMOVE in coherent Step-2B implementation
```

Reasons:

- PR base/head snapshot identity is already owned by `PullRequestIdentity`.
- exact file revisions exist on `RepositoryTextFile` while parsing occurs.
- exact-head downstream composition receives repository/revision from `DependencySourceContext`, constructed directly from the same PR identity.
- `uv_membership.py`'s `evidence.head_revision == context.revision` check therefore re-proves a copied value and should be removed in Step 2C.
- CLI already prints PR base/head once from `PullRequestIdentity`; per-source revision output is duplicate presentation.
- patch-derived requirements evidence has no base/head revision fields, confirming that `DependencyChangeSourceEvidence` is PR-scoped source provenance rather than a self-contained snapshot identity record.

### Resulting target dependency-source contract

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

`path` identifies the source inside the already-owned PR context; `file_format` identifies admitted source semantics; `extraction_method` identifies how the transition was established.

## Exact next bounded implementation

If Step 2B implementation is selected, touch only the coherent dependency-side migration surface first:

```text
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
nearest affected tests/fixtures
```

Goals:

1. finish `DependencyChangeSourceEvidence` as `path + file_format + extraction_method`;
2. migrate exact-file extractor types/imports to `RepositoryFileEvidence`;
3. remove provider metadata and upstream-owned PR-binding revalidation;
4. preserve exact-file availability handling and actual uv/pyproject semantic parsing/comparison;
5. make source comments/docstrings accurately state the new preconditions and ownership;
6. do not modify `uv_membership.py` until Step 2C.

After Step 2B code is coherent and statically reviewed, Step 2C should inspect `uv_membership.py`. Unlike the extractors, membership composes separate dependency/workflow/project/lock evidence branches, so genuine cross-branch repository/revision/path/project-root relations may remain even while provider metadata and circular rebinding checks are removed.

## Scheduled post-R7 AI/LLM engineering checkpoint

The current reconciliation remains the immediate engineering responsibility, but the AI/LLM work now has an explicit route position rather than an indefinite defer state.

```text
R1 → R2 → R3 → R4 → R5 → R6 → R7
→ freeze accepted deterministic baseline
→ B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN Phase 0
   refreshed AI/LLM engineering reassessment + route/baseline check
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
→ Step 2 dependency extraction/provenance focused tests
→ later Target/upstream focused tests
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
scheduled responsibility != indefinite deferral
```

Engineering authority comes from admitted responsibilities, full producer/consumer flow, proof boundaries, material risk, and the simplest adequate mechanism—not from historical code or test convenience.
