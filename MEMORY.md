# UpgradePilot Current Memory

**Last updated:** 2026-08-23  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation is evidence to inspect, not authority to preserve.

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ locate earliest sufficient owner
→ keep the smallest adequate mechanism
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, trace normal producer → integration/orchestration → consumer before deciding local ownership. Direct callability, historical fixtures, or diagnostic convenience are not retention authority unless the alternate route is an explicitly supported product boundary.

Canonical governance owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Implementation branch:** `agent/r1-exact-file-contract-migration`.
- **Base branch:** `main`.
- **Plan position:** **R0 COMPLETE; R1 STATIC CLOSURE CANDIDATE; R2 NOT STARTED**.
- **R1 static closure record:** `working-memory/2026-08-23_B2-R1-static-closure-audit.md`.
- **R1 current continuation:** local structural/focused/full validation on the migration branch. Do not merge `main` until this branch is internally green.
- Dedicated B2 mastery learning package remains paused while reconciliation is active.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration remains SCHEDULED.** Successful R7 acceptance activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` before ordinary B2 continuation.

The migration branch and `main` remain intentionally divergent. Do not create another migration branch, rebase/reset/force-push to hide divergence, or merge the migration into `main` before the validation/reconciliation sequence below is green.

## R1 status

Completed/migrated on `agent/r1-exact-file-contract-migration`:

```text
R1 Step 1 — strong exact-file owner
R1 Step 2B — dependency exact-file semantic extractors
R1 Step 2C — uv membership exact-source composition
Target artifact-environment exact-file consumer
Tagged changelog / upstream exact-source chain
Target-Python exact-source consumer
CI/workflow fixture fan-out
Application investigation / Step-7F fixture fan-out
S001 developer live-proof tooling
PR-specific provider-test reconciliation
Residual branch-specific exact-file contract closure audit
```

Branch-specific static review found **no remaining R1 production blocker**. Remaining exact-file relations in production are either:

1. provider-local external-response admission checks; or
2. independently justified semantic/composition relations.

R1 is **not complete yet** because the post-edit runtime/full-suite and `main` reconciliation gates remain.

## Strong exact-file contract

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

Not retained as durable exact-file evidence:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Important distinction:

```text
retired as durable evidence field
!= forbidden as provider-local validation state
```

The GitHub provider still validates returned-path equality, regular-file type, supported base64 encoding, strict base64, bounded encoded/decoded actual data, UTF-8, and exact repository/path/revision identity before constructing successful evidence.

## Current ownership map

```text
GitHubRepositoryClient
→ external acquisition truth + provider admission

RepositoryTextFile / UnavailableRepositoryFile
→ intrinsic exact locator/content state

dependency/analysis.py
→ PR source admission + exact base/head orchestration + source-context rebinding

uv_lock.py / pyproject.py
→ source-format semantics

uv_membership.py
→ genuine independent dependency/workflow/project/lock composition joins

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-branch application sequencing and exact PR/target identity binding

CLI / tests / tools
→ consume current product contracts; they do not enlarge evidence contracts for convenience
```

Final dependency source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Final Target Python evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

Final tagged changelog evidence:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

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

The bounded local-model path remains:

```text
authoritative deterministic source
→ bounded model semantic candidate
→ deterministic source reconstruction / admission
→ grounded claim
```

The model does not own source authority, target relevance, compatibility, safety, or action.

## Validation state

Earlier focused runtime evidence, collected before the latest Target-Python/fan-out fixes:

```text
Gate 1 exact-file provider/type                13 tests / OK
Gate 2 dependency extraction                   PASS
Gate 3 uv composition + Target artifact env    34 tests / OK
Gate 4 upstream/tagged/semantic pipeline       88 tests / OK
source topology                                3 tests / OK
experiments/tests                              27 tests / OK
compileall                                     exit 0
```

The old pre-fix full-suite result:

```text
507 tests
FAILED (failures=5, errors=51)
```

is **stale evidence**. It preceded the Target-Python and later fixture/tool/provider-test migrations and must not be presented as the current branch result.

Latest historical fully accepted runtime proof remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

It is not superseded until the current migration branch and reconciled-main tree pass the required full suite.

## Exact continuation / R1 acceptance sequence

### Gate A — migration branch internal acceptance

```text
sync exact migration branch
→ active-surface retired-contract grep
→ accumulated focused R1 tests
→ experiments tests
→ compileall
→ full standard suite
```

Any failure blocks `main` reconciliation and must be diagnosed at the earliest failing responsibility.

### Gate B — absorb current main into the SAME branch

Only after Gate A is green:

```text
fetch current origin/main
→ merge origin/main INTO agent/r1-exact-file-contract-migration
→ resolve non-destructively if needed
→ rerun focused/affected tests
→ compileall
→ full standard suite
```

### Gate C — integrate the validated tree into main

Only after Gate B is green:

```text
push validated migration branch
→ switch/update main
→ fast-forward main to the validated migration branch if main has not advanced
→ final deterministic validation on main
→ push main
```

If `main` advances before Gate C, do not force integration; repeat Gate B with the new `origin/main`.

## R1 completion definition

R1 becomes **COMPLETE** only when all are true:

1. `working-memory/2026-08-23_B2-R1-static-closure-audit.md` remains valid;
2. migration-branch focused tests are green;
3. migration-branch full suite is green;
4. current `origin/main` has been merged into the same migration branch;
5. reconciled branch focused/full validation is green;
6. the exact validated tree is integrated into `main`;
7. final main-tree deterministic validation is green;
8. this file records `R1 COMPLETE; R2 NOT STARTED` with exact commit/test evidence.

## R2 guard

Do not pull these known later concerns into R1:

```text
duplicate uv.lock structural parsers
versionless-record drift between transition/reachability models
--all-packages workspace scope loss
membership naming/proposition breadth
bounded selected-root reachability redesign
later CI rebinding
```

Those are R2–R5 responsibilities.

## Learning state to retain

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship
real proposition != local ownership
orchestration context != semantic input
controlled composition != independent evidence-branch composition
test fixture mismatch != reason to restore deleted production fields
diagnostic convenience != evidence-retention requirement
test suite responsibility != duplicate every lower-layer mechanism
resource protection should bind actual processed data, not merely provider-reported metadata
retired durable field != forbidden provider-local variable
runtime green != proof of every later compatibility/safety proposition
```
