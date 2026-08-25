# UpgradePilot Current Memory

**Last updated:** 2026-08-25  
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
- **Plan position:** **R0 COMPLETE; R1 COMPLETE; R2 COMPLETE; R3 IN PROGRESS**.
- **R1 static closure record:** `working-memory/2026-08-23_B2-R1-static-closure-audit.md`.
- **R1 Gate-A/reconciliation record:** `working-memory/2026-08-23_B2-R1-gate-a-runtime-and-main-reconciliation.md`.
- **R1 completion record:** `working-memory/2026-08-24_B2-R1-completion-and-main-acceptance.md`.
- **R2 initial structural-owner record:** `working-memory/2026-08-24_B2-R2-uv-lock-structural-model-initial-slice.md`.
- **R2 acceptance/promotion record:** `working-memory/2026-08-25_B2-R2-runtime-acceptance-and-main-promotion.md`.
- **R3 implementation record:** `working-memory/2026-08-25_B2-R3-uv-package-scope-implementation.md`.
- **Learning-by-Building loop reinforcement record:** `working-memory/2026-08-24_LEARNING_BY_BUILDING_LOOP_REINFORCEMENT.md`.
- **Current bounded continuation:** validate the implemented R3 package-scope candidate in the established local `.venv`, diagnose/fix any regression inside R3, then complete final diff/ownership review. Do not start R4/R5/R6/R7 until R3 runtime acceptance is resolved.
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

environment_selection.py
→ static project selector observation + bounded command package-scope preservation

uv_lock_structure.py
→ shared bounded uv.lock schema/core package-record structural admission

uv_lock.py / pyproject.py
→ source-format transition semantics after admitted source structure

uv_membership.py
→ reachability-specific lock projection + scope-calibrated explicit-root proof + genuine independent dependency/workflow/project/lock composition joins

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

## R2 accepted uv.lock structural ownership

R2 goal from the active plan was:

> Introduce one bounded uv-specific structural lock model so external `uv.lock` structural truth is established once and separate semantic consumers use that admitted structure.

Starting pressure was:

```text
uv_lock.py transition parser
+
uv_membership.py reachability parser
→ overlapping structural truth
→ demonstrated versionless-record drift
```

R2 selected and implemented the smallest shared owner:

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

Reachability-only edge/root interpretation intentionally remains in `uv_membership.py` because moving it would enlarge the shared owner without eliminating duplicated responsibility. R3 workspace/`--all-packages` semantics and R4 reachability proposition/naming remain deliberately separate responsibilities.

The known versionless-record disagreement is removed structurally: a package with no textual version now enters either consumer only when the shared parser admits an exact one-key editable/virtual local source. The shared parser also closes the former membership-only `version = true` schema-admission bug by requiring exact integer type.

Product-code implementation/test milestone:

```text
77575e3558c6425066047b5e3201e61f8665d0d9
```

Accepted locally tested R2 branch head before closure-only documentation:

```text
9da2ebe6d4073bfde3f58aee7111004e71ad9cc2
```

No product code changed between those two SHAs; the later commits reinforced governance/learning/live-state documentation.

Focused regression:

```text
tests/test_uv_lock_structure.py
```

Accepted R2 runtime evidence:

```text
shared structural regression                  5 tests / OK
existing uv-focused regression discovery      user reported green
complete standard suite                       507 tests / OK
compileall src/tests                          PASS
local worktree after validation               clean
final connector ownership/diff review         PASS
```

Final review found no unexplained structural drift and no accidental R3 workspace-scope implementation, R4 proposition/naming redesign, generic dependency graph abstraction, or resolver/runtime proof.

Real S001 learning/ownership trace used during closure:

```text
base/head uv.lock
→ UvLockStructure
→ uv_lock.py
→ soupsieve 2.6 → 2.8.4

head uv.lock + selected docs roots
→ uv_membership.py
→ docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
→ transitive selected-root witness
```

**R2 disposition: COMPLETE / ACCEPTED.** Closure details are in `working-memory/2026-08-25_B2-R2-runtime-acceptance-and-main-promotion.md`.

## R3 current package-scope reconciliation

R3 goal from the active plan is:

> Preserve the minimum real uv command scope required by current evidence, beginning with S001 `--all-packages`, so positive and negative-ish reachability semantics remain sound.

Pre-R3 loss:

```text
real command
uv sync --all-packages --group docs

old declaration
manager=uv
operation=sync
selectors=(docs,)
project_root=...

--all-packages
→ discarded
```

The current R3 implementation candidate adds one bounded producer-owned fact:

```text
ProjectEnvironmentSelectionDeclaration
└── package_scope
    ├── bound_project
    └── all_workspace_packages
```

`environment_selection.py` now preserves literal `--all-packages` as `all_workspace_packages`. Ordinary pip/uv declarations remain `bound_project`. Unsupported package-targeting scope such as `--package`, `--directory`, and `--no-project` remains unresolved and does not emit a misleading bound-project declaration.

The consumer applies the proof asymmetry explicitly:

```text
all_workspace_packages
+ one unconditional bound-project selected-root witness
→ member

all_workspace_packages
+ no bound-project witness
+ complete workspace roots not modeled/exhausted
→ unresolved
  uv_membership_workspace_scope_not_exhausted

NOT
→ not_established
```

This deliberately does not enumerate guessed workspace members from editable/virtual lock records. Complete workspace discovery/member/config semantics, defaults, exclusions, conflicts, package targeting, and complete `--only-group` environment formation are not introduced in R3.

Focused R3 tests now cover:

```text
S001-shaped --all-packages scope preservation
ordinary bound-project scope
uv run option-prefix scope preservation
unsupported --package targeting → unresolved/no false declaration
S001 positive witness under all-workspace scope
no-witness all-workspace → unresolved
explicit [tool.uv.workspace] multi-member producer→consumer regression
```

Current R3 source/test candidate before memory-only state recording:

```text
4b6714aef29c57682c96e3c0b243bb1b93268181
```

Current verification status:

```text
static producer→consumer responsibility review    PASS to current depth
focused R3 runtime tests                          PENDING
uv-focused regression discovery                  PENDING
complete standard suite                          PENDING
compileall src/tests                              PENDING
```

R3 remains **IN PROGRESS**. Next action is local narrow-to-broad validation in the established project `.venv`; any regression stays inside R3 until resolved. R4 must not start before R3 runtime acceptance and final ownership/diff closure.

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
pre-action orientation != post-action learning closure
pending local validation != reason to defer learning closure for already-established work
file-level dependency transition != PR-wide trusted dependency transition
lock structural truth != dependency-transition truth != selected-root reachability truth
positive reachability witness requires one sound path != not_established requires complete claimed scope exhaustion
preserved command scope != complete command/environment interpretation
```
