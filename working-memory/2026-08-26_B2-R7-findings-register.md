# Working Memory — B2 R7 Findings Register

**Date:** 2026-08-26  
**Status:** ACTIVE DURING R7; FINDINGS ACCUMULATE UNTIL FINAL REMOTE DISPOSITION  
**Execution branch:** `main`  
**Parent R7 record:** `2026-08-26_B2-R7-acceptance-cleanup-and-baseline-closure.md`

## 1. Purpose

This register collects bounded R7 edges, bugs, design pressure, proof risks, and cleanup candidates discovered while the remote R7 review progresses.

The purpose is to avoid two bad extremes:

```text
find one edge
→ patch immediately
→ churn architecture before the full R7 picture is visible
```

and:

```text
find one edge
→ mention it in chat
→ lose the reasoning/evidence before final closure
```

Normal rule:

```text
observe finding
→ establish exact current behavior from source/tests/real evidence
→ classify risk
→ record cause + consequence + possible repair shape + regression pressure
→ continue R7 when non-blocking
→ disposition all queued findings together before the final remote candidate is frozen
```

A finding may interrupt the current R7 slice immediately only when evidence establishes a hard blocker such as false support, proof strengthening/uncertainty erasure, authority/provenance conflation, a broken normal production route, contradiction with an admitted current real case/specification, or corruption that makes later R7 evidence unreliable.

Before R7.8 freezes the final remote candidate, every queued finding must receive one explicit disposition:

```text
FIX IN R7
ACCEPT AS KNOWN BOUNDED LIMITATION
SCHEDULE FOLLOW-UP WITH OWNER/TRIGGER
REJECT / NOT REQUIRED BY CURRENT PRODUCT RESPONSIBILITY
```

If a queued finding is promoted to `FIX IN R7`, implement it remotely in the owning R7 cleanup slice, add the smallest discriminating regression pressure, and include the resulting source/test revision in the final R7.9 local validation bundle.

---

## F-001 — Mixed safe + unresolved shell segments collapse to one unresolved R3 step

**Discovered:** R7.1 remote focused source/test audit  
**Current disposition:** QUEUED — NO IMPLEMENTATION YET  
**Current blocker:** NO  
**Risk class:** conservative under-reporting / granularity loss  
**Owning area if later fixed:** R3 project-environment selection contract, then R6 consumption of that contract

### Exact current cause

R3 parses one GitHub Actions `run:` block into bounded shell segments and separately gathers parsed declarations and unresolved details. But `ProjectEnvironmentSelectionObservation` exposes one step-level `state` for the whole `RunStepDefinition`.

Current shape:

```text
for each shell segment:
    parse segment
    append safe declaration(s)
    append unresolved detail(s)

if ANY unresolved detail exists:
    overall observation.state = unresolved
    retain declarations, but the whole run step is unresolved
```

R6 then consumes that aggregate state:

```text
R3 not_observed
→ no contribution

R3 unresolved
→ preserve one unresolved CI-consumption item
→ do not evaluate retained declarations through R4/R5

R3 observed
→ evaluate each declaration through R4/project-source membership → R5
```

Example:

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

Conceptually R3 can identify:

```text
segment 0 → readable literal docs declaration
segment 1 → dynamic selector → unresolved
```

but the final observation is `unresolved`, so R6 does not evaluate the safe docs declaration. Reversing segment order does not change the limitation. Separate GitHub Actions `run:` steps remain independent and are not affected.

### Consequence and proof classification

The current system can under-report a positive static fact:

```text
independently safe selected-root witness
→ could become supported consumption

another unresolved segment in same run step
→ whole observation unresolved
→ positive fact not derived
```

This is currently conservative under-reporting, not proof strengthening: possible support becomes unresolved rather than uncertainty becoming supported or `not_established`.

### Unsafe shortcut rejected

R6 must not simply evaluate every retained declaration from an unresolved observation. Example:

```bash
uv sync --all-extras --no-extra mlx
```

The positive `--all-extras` declaration can be retained while the same segment is unresolved because of the negative selector. Processing retained declarations blindly could manufacture false support.

### Suggested repair direction if selected later

Preserve the granularity R3 already parses:

```text
ProjectEnvironmentSelectionObservation
└── segment observations
    ├── segment_index
    ├── state = observed | not_observed | unresolved
    ├── reason/detail
    └── declarations owned by that segment
```

Then R6 consumes each segment independently. Semantic ownership remains in R3; R6 must not guess which declarations inside an unresolved step are safe.

### Suggested regression fixtures

1. Safe before unresolved:

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

Expected: independently evaluated docs result + unresolved dynamic result, both preserved.

2. Unresolved before safe: same evidence meaning as fixture 1; order must not affect preservation.

3. One tainted segment:

```yaml
- run: uv sync --all-extras --no-extra mlx
```

Expected: unresolved only; no support manufactured from retained `--all-extras`.

4. Separate `run:` steps: unresolved first step does not suppress an independently readable later docs step.

### End-of-R7 decision questions

- Does R7.3 real evidence expose this shape in an admitted workflow?
- Does another finding turn this into a stronger proof/authority issue?
- Can a segment-result contract remain bounded without becoming a shell interpreter?
- Is the current product need sufficient to justify fixing now, or should the limitation remain trigger-based?

Until final disposition, do not implement F-001 merely because the repair direction is understood.

---

## F-002 — Unavailable project-root evidence can disappear before CI consumption classification

**Discovered:** R7.2 remote normal investigation/CI orchestration trace  
**Current disposition:** QUEUED — HIGH-PRIORITY FINAL DISPOSITION; NO IMPLEMENTATION YET  
**Current blocker:** NOT YET — continue R7 evidence gathering, but R7.8 MUST NOT freeze without explicit disposition  
**Risk class:** proof calibration / uncertainty erasure into negative-ish absence  
**Owning area if fixed:** R6 project-environment source composition/admission, with investigation source acquisition as producer

### Exact current route

For a `UvLockDependencyContext`, normal `investigation.py` acquires:

```text
exact sibling pyproject.toml
+
exact uv.lock
→ WorkflowProjectEnvironmentSource
```

The sibling project file supplies the exact project-root path needed by R3. R4 deliberately does not parse its content; exact `uv.lock` remains R4's semantic source.

`derive_project_environment_consumptions(...)` currently contains this admission behavior:

```text
for project source:
    if project_file is not RepositoryTextFile:
        continue
```

Therefore an `UnavailableRepositoryFile` for the required sibling `pyproject.toml` is silently omitted from project-environment derivation. No R3 observation is created and no unresolved CI-consumption item is emitted.

Later, `inspect_workflow_dependency_evidence(...)` may therefore receive:

```text
uv dependency source context
+ readable workflow
+ zero project-environment external consumptions
```

and `_classify_static_consumption(...)` can fall through to:

```text
state = not_established
reason = static_dependency_consumption_not_observed
```

### Why this is materially different from F-001

F-001 loses possible positive evidence into `unresolved`.

F-002 can lose **known source unavailability** entirely and later express a negative-ish absence:

```text
required project-root evidence unavailable
→ evidence disappears
→ static consumption may become not_established/not_observed
```

That is the same dangerous proof direction as the post-R6 unresolved-selection bug, but at an earlier source-admission boundary.

### What is and is not established

If exact sibling `pyproject.toml` is unavailable, the system cannot safely bind R3 to the required project root through the current contract. That does not establish that no relevant project selection exists.

Therefore:

```text
required exact project-root evidence unavailable
!= project selection not observed
!= static dependency consumption not established by exhaustive evidence
```

### Suggested smallest repair direction if selected later

At the R6 project-environment composition seam, preserve material required-source unavailability as unresolved evidence rather than `continue`.

Likely bounded shape:

```text
project_file unavailable
→ unresolved project-environment CI evidence/problem
→ preserve exact missing path + provider reason/detail
→ do not invoke R3
→ do not invoke R4/project-source membership/R5
→ coverage remains unresolved unless stronger independent supported consumption exists
```

Do not invent a project root from `uv.lock` merely to bypass the missing R3 source contract unless a later ownership review explicitly redesigns that contract.

### Suggested regression fixtures

Fixture A — uv context, readable workflow, available lock, unavailable sibling project file:

```text
workflow: uv sync --group docs
project_file: UnavailableRepositoryFile(pyproject.toml)
lock_file: exact readable uv.lock
```

Current expected pressure: no external consumption; coverage can fall to `static_dependency_consumption_not_observed`.

Safe target if fixed: explicit unresolved project-environment evidence preserving `pyproject.toml` unavailability; coverage consumption state unresolved.

Fixture B — project file available, lock unavailable: retain the already intended R4 unresolved lock-source behavior; do not conflate with project-file unavailability.

Fixture C — another independent supported consumption exists: aggregate support may remain existentially supported, but the unavailable project-environment evidence must still remain in the underlying evidence collection rather than disappear.

### End-of-R7 decision questions

- Does R7.3 expose this source-unavailability shape in real admitted cases?
- Is the smallest correct owner R6 composition, or should project-source acquisition expose a typed composition problem earlier?
- Can the correction preserve uncertainty without inventing new project/lock currentness semantics?
- Which exact reason/diagnostic type best preserves source identity without creating a generic evidence framework?

R7.8 must explicitly disposition F-002 before candidate freeze because its current direction can erase uncertainty.

---

## F-003 — Legacy CI compatibility surfaces are absent from the normal product route but remain protected by tests/topology

**Discovered:** R7.2 remote normal investigation/CI orchestration trace  
**Current disposition:** QUEUED FOR R7.4 RETENTION REVIEW — NO IMPLEMENTATION YET  
**Current blocker:** NO  
**Risk class:** architectural retention / naming / migration residue  
**Owning area:** CI/investigation compatibility surfaces

### Evidence from the normal route

Repository-wide caller tracing established:

```text
investigation.py
→ evaluate_dependency_ci_coverage(...)
→ ci_coverage_result

CLI
→ reads ci_coverage_result directly
```

The ordinary product route does **not** call `evaluate_dependency_ci_exercise(...)` or `inspect_workflow_commands(...)` after the R6 migration.

Current retained compatibility surfaces include at least:

```text
evaluate_dependency_ci_exercise(...)
inspect_workflow_commands(...)
PublicPullRequestInvestigation.ci_exercise_result read alias
direct_requirements_install_path compatibility projection/field
```

The legacy evaluator and helper remain protected by old tests and `tests/test_source_topology.py`; the alias and direct-requirements projection also remain referenced by older tests/history.

### Why this is a finding, not an automatic delete decision

Project governance says:

```text
current use / tests / historical design
!= retention justification
```

But the converse is also true:

```text
not on normal route
!= automatically safe to remove
```

R7.4 must establish whether any real supported alternate API, compatibility obligation, verifier/tool, or external/public contract still needs each surface.

### Required R7.4 disposition trace

For each candidate:

```text
exact responsibility
→ current callers
→ normal producer/integration/consumer route
→ supported alternate route or compatibility obligation, if any
→ concrete failure if removed
→ KEEP / MOVE / NARROW / REMOVE
```

Also review the now-misaligned migration comments/names, including `WorkflowDependencyExerciseInput` and `external_consumptions`, after the product route has become coverage-oriented.

### Suggested regression pressure if removal/narrowing is selected

- normal `investigate_public_pull_request(...)` still reaches `ci_coverage_result` with no legacy evaluator call;
- CLI continues to render coverage-oriented evidence;
- R6 normal investigation regression remains the primary integration guard;
- source-topology tests are updated to protect current owners rather than preserve legacy surfaces by inertia;
- any intentionally retained compatibility alias has a focused test naming the real compatibility obligation.

### End-of-R7 decision questions

- Is any legacy API intentionally public/supported outside the normal application path?
- Are old tests the only remaining callers?
- Does removing a surface simplify proof language and naming without losing a real responsibility?
- Should compatibility removal occur in R7.5 or be explicitly scheduled after the agentic evaluation?

---

## Future finding template

Use the next stable ID (`F-004`, `F-005`, ...).

```text
Finding ID / title
Discovered at R7 slice
Current disposition
Blocker? yes/no
Risk class
Owning area

Exact evidence/current behavior
Root cause
User/product/proof consequence
Why it is or is not a blocker
Possible repair direction (not authorization)
Suggested discriminating regression/real-case fixtures
Dependencies/interaction with earlier findings
Questions for final R7 disposition
```

Do not duplicate one root cause into multiple findings merely because it appears through different callers; extend the existing finding when later evidence belongs to the same underlying issue.
