# UpgradePilot Current Memory

**Last updated:** 2026-08-24  
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
- **Execution branch:** `agent/r2-uv-lock-structural-model`.
- **Plan position:** **R0 COMPLETE; R1 COMPLETE; R2 IN PROGRESS**.
- **R1 static closure record:** `working-memory/2026-08-23_B2-R1-static-closure-audit.md`.
- **R1 Gate-A/reconciliation record:** `working-memory/2026-08-23_B2-R1-gate-a-runtime-and-main-reconciliation.md`.
- **R1 completion record:** `working-memory/2026-08-24_B2-R1-completion-and-main-acceptance.md`.
- **R2 initial structural-owner record:** `working-memory/2026-08-24_B2-R2-uv-lock-structural-model-initial-slice.md`.
- **Current bounded continuation:** validate the implemented R2 shared structural owner narrow → broader; diagnose/fix any regression before broadening. Do not start R3/R4/R5 while R2 runtime and final ownership acceptance remain unresolved.
- Dedicated B2 mastery learning package remains paused while this reconciliation plan is active.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration remains SCHEDULED.** Successful R7 acceptance activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` before ordinary B2 continuation.

## R1 accepted runtime authority

Accepted executable commit:

```text
9fb19dd483f568a459a0680527a8b00683334359
```

Local environment:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Gate A before main reconciliation:

```text
structural contract assertions               PASS
focused R1 regression suite                  272 tests / OK
experiment suite                              27 tests / OK
compileall src/tests/tools/experiments       PASS
complete standard suite                      502 tests / OK
```

Gate B after current `main` was merged into the same R1 branch:

```text
complete standard suite                      502 tests / OK
experiment suite                              27 tests / OK
```

`main` was then fast-forwarded non-destructively to the exact Gate-B-tested commit `9fb19dd483f568a459a0680527a8b00683334359`. At promotion time GitHub reported `main` and `agent/r1-exact-file-contract-migration` identical.

Any later commits that only record R1 completion/live state are documentation-only and do not supersede the executable acceptance SHA.

The old pre-fix result:

```text
507 tests
FAILED (failures=5, errors=51)
```

is historical migration-pressure evidence only and is fully superseded by the accepted R1 runtime results above.

## R1 accepted exact-file ownership

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

The GitHub provider still validates returned-path equality, regular-file type, supported/strict base64, actual encoded/decoded bounds, UTF-8, and exact repository/path/revision identity before constructing successful evidence.

## Current ownership map retained for later work

```text
GitHubRepositoryClient
→ external acquisition truth + provider admission

RepositoryTextFile / UnavailableRepositoryFile
→ intrinsic exact locator/content state

dependency/analysis.py
→ PR source admission + exact base/head orchestration + source-context rebinding

uv_lock_structure.py
→ shared bounded uv.lock schema/core package-record structural admission

uv_lock.py / pyproject.py
→ source-format transition semantics after admitted source structure

uv_membership.py
→ reachability-specific lock projection + genuine independent dependency/workflow/project/lock composition joins

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-object application sequencing and exact PR/target identity binding

CLI / tests / tools
→ consume current product contracts; they do not enlarge evidence contracts for convenience
```

Final reduced dependency source provenance:

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

## R2 exact continuation

R2 goal from the active plan:

> Introduce one bounded uv-specific structural lock model so external `uv.lock` structural truth is established once and separate semantic consumers use that admitted structure.

Starting pressure was:

```text
uv_lock.py transition parser
+
uv_membership.py reachability parser
→ overlapping structural truth
→ demonstrated versionless-record drift
```

The initial R2 Audit/Design + Build slice has now selected and implemented the smallest shared owner:

```text
exact uv.lock text
→ uv_lock_structure.py
   - TOML admission
   - schema/revision admission
   - core package-record name/version/source admission
   - versionless editable/virtual boundary
   - repeated normalized-name preservation
→ admitted UvLockStructure
   ├── uv_lock.py transition semantics
   └── uv_membership.py reachability-specific projection/traversal
```

Important design boundary:

```text
SHARED STRUCTURAL FACT
schema/revision/core package record/version/source/repeated-record structure

!=

TRANSITION SEMANTICS
base/head pairing, artifact-only canonical comparison, exact version transition

!=

REACHABILITY SEMANTICS
project binding, selected roots, edge markers/extras, deterministic edge resolution, traversal
```

Reachability-only edge/root interpretation intentionally remains in `uv_membership.py` because moving it would enlarge the shared owner without eliminating duplicated responsibility. R3 workspace/`--all-packages` semantics and R4 reachability proposition/naming remain deliberately deferred.

The known versionless-record disagreement is removed structurally: a package with no textual version now enters either consumer only when the shared parser admits an exact one-key editable/virtual local source. The shared parser also closes the former membership-only `version = true` schema-admission bug by requiring exact integer type.

Current R2 executable candidate before documentation-only state commits:

```text
77575e3558c6425066047b5e3201e61f8665d0d9
```

Focused regression added:

```text
tests/test_uv_lock_structure.py
```

Current verification status:

```text
connector/static ownership + diff review       PASS to current depth
runtime focused R2 tests                       PENDING
standard suite                                 PENDING
compileall                                     PENDING
```

Required continuation:

```text
run shared-structure + existing uv transition/versionless + reachability/universal-lock tests
→ diagnose/fix any focused regression inside R2
→ broaden to standard suite
→ compileall / other plan-required proof
→ final R2 ownership/diff review
→ R2 acceptance record
```

R2 is not complete until that runtime evidence is green. R3 (`--all-packages` / command scope), R4 (reachability proposition/naming), R5 (CI rebinding), R6 (real-case pressure), and R7 (final reconciliation acceptance) remain later steps.

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
Git history divergence != content conflict
same commit SHA under two refs = same executable tree
closure documentation != new executable authority
shared structural parsing != shared semantic interpretation
one external format != permission to build a generic package-manager abstraction
```