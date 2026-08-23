# UpgradePilot Current Memory

**Last updated:** 2026-08-23  
**Authority:** sole owner of the live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable implementation-retention rule

**Existing code is evidence to inspect, not authority to preserve.** Current use, passing tests, comments, historical intent, prior effort, or another under-review consumer does not by itself justify keeping a field, check, type, helper, abstraction, metadata value, alias, dependency, or compatibility surface.

For every material mechanism under review:

```text
What current admitted responsibility / proof need / material risk / real compatibility obligation requires it?
→ independently justified: keep the smallest adequate mechanism
→ not independently justified: remove or narrow it
```

Do not use circular retention arguments such as `X must stay because Y uses X` when Y's dependence on X is itself under review.

For validation checks specifically, **classifying a check as relational is not enough to retain it at every consumer**. Before keeping a downstream relationship/rebinding check, trace the normal producer/caller chain and identify the earliest boundary that already establishes the proposition. Repeat it downstream only when that function has a real independent trust/public-boundary responsibility or another material risk requires the repetition. Direct-call/test convenience is not retention authority.

Canonical durable rules: `AGENTS.md`, `OPERATING_GUIDE.md`, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-003`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Current mode:** normal learning by doing/building under `OPERATING_GUIDE.md`.
- **Plan position:** **R0 COMPLETE; R1 IN PROGRESS**.
- **Current R1 position:** Step 1 implemented; Step 2A implemented; **Step 2B responsibility boundary reopened before editing**.
- **Current progressive record:** `working-memory/2026-08-23_B2-R1-exact-file-contract-migration-continuation.md`, continuing `working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`.
- **Dedicated learning package:** `learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/` remains paused while its source is actively reconciled.
- **Previous dependency-environment/CI plan:** deferred at completed Cluster 5; Cluster 6 must not start during reconciliation.
- **Agentic orchestration evaluation:** deferred until reconciliation closes and continuations are re-reviewed.
- **R2:** NOT STARTED.

## Validation state

Ali temporarily has no access to the WSL/laptop checkout, so local execution is unavailable now.

This changes validation cadence, not proof standards:

```text
bounded implementation
→ static/source review
→ explicit NOT EXECUTION-VALIDATED marker
→ progressive working-memory record
→ next bounded implementation
→ later accumulated focused + integration + full local execution
```

No migration-branch commit is runtime-proven merely because it was written or statically inspected.

**Latest accepted product-runtime validation remains:**

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
HEAD == origin/main and clean at that historical validation point
```

Later governance, memory, design, and unvalidated migration commits do not supersede it.

## Stable proof ladder

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

## R0 disposition

R0 is complete and does not need to be rerun. Its taxonomy is an ownership map, not a retention list:

```text
external trust-boundary validation
semantic/domain validation
relational/rebinding validation
repeated internal invariants
impossible-state defense
```

Durable R0 findings:

- external GitHub response validation needs one provider owner;
- independently meaningful cross-object relations can be legitimate after stronger types, but a legitimate relation still must be owned at the correct boundary rather than repeated automatically;
- `uv_lock.py` and `uv_membership.py` duplicate material `uv.lock` structure and already drift on versionless records;
- S001 `--all-packages` scope is currently lost from the typed uv selection declaration;
- the smallest justified uv proposition is explicit selected-root reachability;
- S001 positive witness remains `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- static dependency consumption, static direct exercise, and exact-head runtime authority remain separate proof classes.

## R1 frozen exact-file direction

Successful exact repository text should carry only:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability carries:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Fields that did not earn durable exact-file retention:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

The provider may validate external response details and discard them. Downstream code should validate domain meaning and independently necessary relationships, not revalidate provider transport facts or relationships already guaranteed by an upstream integration path without a separate boundary reason.

## R1 Step 1 — implemented / unvalidated

Branch commits:

```text
709aba4cdab1fd666579f90cbe6a5e974cad8626
→ strong RepositoryTextFile / UnavailableRepositoryFile + necessary-only GitHub acquisition boundary

e88b1e21e3b1efd09c226b5ca1512230f6477057
74fd3aaede37b15cb2eedbfda41128bc4d81f46c
→ nearest provider/construction tests migrated
```

Construction invariants now belong to the exact-file types; GitHub acquisition truth remains provider-owned. Resource protection uses bounded encoded input plus bounded actual decoded bytes rather than provider `size` propagation.

## R1 Step 2 — dependency source provenance

### Step 2A — implemented / unvalidated

Commit:

```text
4ccf14aef0b473870e63eb482ba3409fe239926f
```

`DependencyChangeSourceEvidence` is narrowed to:

```text
path
file_format
extraction_method
base_revision
head_revision
```

Removed:

```text
base_blob_sha
head_blob_sha
base_byte_count
head_byte_count
```

The revision fields remain implemented but are still subject to the same necessity pressure if later analysis shows the downstream rebinding proposition can be established more simply.

### Step 2B — responsibility boundary reopened before implementation

A review correction changed the next task.

The normal product route is:

```text
investigate_public_pull_request
→ PullRequestIdentity
→ changed files from that PR identity
→ analyze_dependency_change(identity, changed_files, repository_client)
→ base/head repository acquisition using the same identity and changed_file.filename
→ semantic extractor
```

This means repository/path/base-head relations may already be established by the integration/acquisition path before `uv_lock.py` or `pyproject.py` receives the files.

Therefore do **not** automatically preserve these checks inside the semantic extractors:

```text
base repository == head repository
base path == changed_file path
head path == changed_file path
```

First answer for each candidate check/fact:

```text
1. what exact proposition does it establish?
2. where is that proposition first guaranteed on the normal product path?
3. is the downstream function a real independent trust/public boundary?
4. what material failure remains possible if the repeat check is removed?
```

Only then edit:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
```

Do not change uv-lock parsing/comparison semantics or pyproject optional-dependency semantics in this substep. Treat remaining `uv_membership.py` rebinding pressure separately as Step 2C.

## Deferred validation ledger

When laptop/WSL access returns, run validation in causal order:

```text
Step 1 provider/type focused tests
→ Step 2 dependency extraction/provenance focused tests
→ later Target/upstream focused tests
→ nearest integration/end-to-end tests
→ full deterministic suite
```

Diagnose failures against the earliest relevant bounded step; do not patch blindly until only the final suite is green.

## Learning state

Ali requires the implementation itself to remain educational and incremental.

Current R1 mental models established:

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship between objects
legitimate relationship != justification to re-check it at every layer
```

Ali's predictions/questions are learning inputs. Engineering decisions come from admitted responsibilities, full producer/consumer flow, proof boundaries, material risk, and the simplest adequate technical mechanism.

## Continuation-critical guards

- `MEMORY.md` alone owns live continuation.
- Do not start R2 before R1 is coherent and execution-validated.
- Do not resume old Cluster 6, agentic evaluation, or Tranche 2 in parallel.
- Do not introduce production compatibility shims merely for old fixtures.
- Before retaining downstream validation, trace the upstream construction/integration guarantees.
- Preserve necessary trust-boundary validation and real relational joins only at boundaries that independently own them.
- Do not preserve provider metadata for completeness or because current consumers reference it.
- Do not introduce generic trust/provenance wrappers, generic dependency graphs, package-manager abstractions, or a complete uv interpreter without new admitted need.
