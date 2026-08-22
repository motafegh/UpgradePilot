# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Revised:** 2026-08-22 — Plan-02 Chunk-1 evidence model corrected; live post-learning continuation reconciled  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 02 / Chunk 1  
**Exact pause:** first `pyproject.toml` + `uv.lock` evidence/background section, before the current-source provenance-validation walkthrough

## 1. Purpose and authority boundary

This file preserves continuity of the interactive learning journey: current position, demonstrated understanding, material corrections, open `[~]` questions, engineering-audit findings, and exact continuation.

It is intentionally a **working memory**, not:

- live project-state authority;
- product implementation authorization;
- an architecture/specification owner;
- source/test truth;
- a second learning contract;
- a polished learning note.

If this file conflicts with the learning contract, the contract wins. If it conflicts with current source/tests, source/tests win for implementation truth. If it conflicts with `../../MEMORY.md` about live project position/continuation, root `MEMORY.md` wins.

Status markers:

```text
[ ] not started / not demonstrated
[~] partial or non-blocking gap
[x] sufficiently demonstrated for current route
[!] blocking misconception/question; repair before proceeding
```

Record an item as Ali-owned only when Ali has exposed understanding through explanation, prediction, comparison, trace, overclaim diagnosis, premise/design challenge, or legitimate later change/diagnosis. Immediate recognition after an AI explanation is not enough by itself.

## 2. Live project context relevant to this learning package

The root `../../MEMORY.md` currently owns these continuation facts:

```text
execution branch: main
Clusters 0–5: COMPLETE / GREEN
validated Cluster-5 point: bfdfd4257574f85cc3a2d094bf46a37ad6373dea — 508 tests / OK
Cluster 6 ordinary integration: NOT STARTED
Tranche 2 static↔runtime correlation: NOT SELECTED / NOT AUTHORIZED
current responsibility: continue this approved learning route
selected post-learning checkpoint: bounded agentic investigation/orchestration evaluation
source-clarity / ordinary Cluster-6 continuation: deferred unless live authority changes
```

This local memory does not duplicate the full root state. Re-read root `MEMORY.md` before any return-to-building decision.

## 3. Learning route and progress

```text
Plan 01 — S001 real case → first UpgradePilot evidence models
Plan 02 — S001 membership → CI consumption → coverage
Plan 03 — S011 + S005 generalization pressure
Plan 04 — application boundary → return to live building decision
```

### Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Status:** `[~] CONTENT ROUTE COMPLETE — formal ownership/test gates intentionally deferred`  
**Opened:** 2026-08-17  
**Content route completed:** 2026-08-21

- [x] Chunk 1 — S001 orientation + Soup Sieve first contact — GREEN
- [x] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence — GREEN
- [x] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI — GREEN
- [~] Chunk 4 — exact dependency transition/source-context content covered; independent source/test ownership gate deferred
- [~] Chunk 5 — static project-environment selection content covered; independent prediction/test-ownership gate deferred

Durable Plan-01 notes:

```text
notes/01_PLAN01_END_TO_END_LEARNING_NOTE.md
notes/02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md
notes/03_PLAN01_EVIDENCE_AND_PROOF_BOUNDARIES.md
notes/04_PLAN01_MASTERY_AND_REVIEW_MAP.md
```

Those notes preserve the fuller historical study content; this working memory keeps only continuation-relevant facts.

### Plan 02 — S001 Membership → CI Consumption → Coverage

**Status:** `[~] ACTIVE`  
**Opened:** 2026-08-21

- [~] Chunk 1 — exact project + lock evidence boundary before membership semantics — ACTIVE / PAUSED DURING BACKGROUND-EVIDENCE SECTION
- [ ] Chunk 2 — S001 graph reachability + membership witness
- [ ] Chunk 3 — membership → exact static CI consumption
- [ ] Chunk 4 — whole-workflow evidence + bounded CI coverage

### Plan 03 — Generalization Pressure: S011 + S005

**Status:** `[ ] NOT STARTED`

### Plan 04 — Application Boundary + Return to Building

**Status:** `[ ] NOT STARTED`

Plan 04 is a learning handoff plan only. When reached, root `MEMORY.md` decides the actual post-learning product checkpoint.

## 4. Durable Plan-01 understanding carried into Plan 02

### S001 real dependency relationship

```text
Pydantic documentation/tooling
→ docs dependency group
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Separate path:

```text
docs-upload
→ beautifulsoup4
→ soupsieve
```

Important boundary:

```text
repository/tooling dependency
!= normal core Pydantic runtime dependency
```

### `uv` / lockfile understanding

Ali demonstrated the important boundary:

```text
soupsieve appears in universal uv.lock
!= a particular project/CI environment selected or installed soupsieve
```

Residual `[~]`: independent restatement of lock-record/edge mechanics can be reinforced naturally during Plan-02 parsing/traversal; no need to reopen a separate uv course.

### CI / GitHub Actions understanding

Ali demonstrated:

```text
static workflow YAML
!= runtime execution evidence
```

For historical S001 `docs-build`, the important static structure includes:

```text
uv sync --all-packages --group docs
→ later docs-related commands / MkDocs build
```

Preferred wording:

> configured to synchronize the docs group and invoke an MkDocs build

Do not call static YAML direct package `exercise` without the later stronger evidence proposition.

### Plan-01 provenance/design audit carried forward

Ali previously challenged whether every provenance field/check is genuinely necessary rather than assuming `more provenance = automatically better`.

Carry this question into Plan-02 provenance validation using the refined classification:

```text
PROPOSITION-ESSENTIAL
CURRENT-IMPLEMENTATION REQUIREMENT
DEFENSIVE / BOUNDARY HARDENING
UNCERTAIN / AUDIT NEEDED
```

Do not answer `because the code uses it`.

## 5. ACTIVE RECORD — Plan 02 / Chunk 1

### Real question

> Given the already established static `DependencyGroupSelector("docs")` and S001 changed-package/source context, what exact project/lock evidence and provenance does the current evaluator require before it may safely interpret selected-environment membership?

### Exact real S001 anchors

```text
repository: pydantic/pydantic
base: 652a61ce4f9d7d76eaada31535807a485ece0e21
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
changed package: soupsieve
old: 2.6
proposed: 2.8.4
selected static group: docs
```

Relevant real artifacts:

```text
pyproject.toml
[project] name = pydantic
[dependency-groups].docs includes mkdocs-llmstxt

uv.lock
mkdocs-llmstxt → beautifulsoup4
beautifulsoup4 → soupsieve
soupsieve = 2.8.4
```

### Material covered before pause

The first teaching pass introduced `pyproject.toml`, TOML at minimum depth, the real docs-group fragment, the real lock path, and the idea that current membership evaluation uses exact project + exact lock evidence before traversal.

Ali then paused and challenged two premises before completing the section.

## 6. Important corrections/discoveries from Ali's challenges

### [x] Correction 1 — `pyproject.toml` and `uv.lock` are not cleanly disjoint evidence owners

The earlier explanation was too clean:

```text
pyproject.toml tells selection/group
uv.lock tells graph
```

Corrected model:

```text
STATIC ENVIRONMENT-SELECTION DECLARATION
→ establishes that the inspected static command selected `docs`

EXACT pyproject.toml
→ primary project declaration/configuration evidence
→ current evaluator uses relevant project identity/root/group semantics

EXACT uv.lock
→ resolved lock/dependency graph evidence
→ can ALSO preserve overlapping project/group information
```

Therefore:

```text
information overlap is real
and must be taught explicitly
```

Do not force an artificial `A tells only X / B tells only Y` division.

### [x] Correction 2 — file contents do not themselves establish the static selection proposition

Even if `uv.lock` contains docs-group information, that does not itself establish that the inspected CI command selected the docs environment.

The static selection proposition comes from the already established selection declaration, for S001 conceptually:

```text
uv sync ... --group docs
→ DependencyGroupSelector("docs")
```

Project/lock evidence then contributes to the separate membership question.

### [x] Correction 3 — current evaluator requiring both artifacts != universal logical necessity

The current implementation consumes exact `pyproject.toml` + exact `uv.lock`.

Learning must now distinguish:

```text
what each artifact contributes in CURRENT source
vs
what the membership proposition logically requires in any valid design
vs
what is defensive or implementation-specific
```

Do not ask Ali to memorize `both are required` as an unexplained universal invariant.

Lock freshness / resolver currentness remains outside the current proof boundary.

### [x] Correction 4 — mixed-revision evidence is a defensive failure scenario, not normal operation

Ali correctly challenged an example shaped like:

```text
pyproject.toml from HEAD-A
uv.lock from HEAD-B
```

because UpgradePilot normally freezes the case to immutable exact revisions before this responsibility.

Correct framing:

```text
NORMAL / EXPECTED PATH
context + project evidence + lock evidence should already agree on the frozen exact case/revision/root

DEFENSIVE / INVALID-INPUT PATH
membership boundary revalidates identity and fails closed if a caller/provider/cache/test fixture violates that invariant
```

Immutability of each SHA does not by itself guarantee correct composition of arbitrary evidence objects, but inconsistent composition should not be taught as normal expected pipeline behavior.

### [x] Ownership evidence from the challenges

Ali's questions are positive engineering-audit evidence because they challenged:

- whether `uv.lock` already contains some information attributed to `pyproject.toml`;
- whether both artifacts are logically necessary or merely required by the current design;
- whether a HEAD-A/HEAD-B example represented a realistic normal flow;
- whether repeated downstream provenance validation may be defensive redundancy rather than proposition-essential logic.

These challenges improved both the learning contract and Plan-02 framing. They are not blocking misconceptions.

## 7. Current source target — not yet fully walked in this chunk

Primary source:

```text
src/upgradepilot/dependency/uv_membership.py
```

Current evaluator path to inspect next:

```text
evaluate_uv_selected_environment_membership(...)
→ _validate_exact_source_identity(...)
→ unresolved early return on source/provenance problem
→ _parse_project(...)
→ _parse_lock(...)
→ later workspace/root selection and traversal
```

Chunk 1 owns only the **evidence boundary + semantic preparation** needed before graph reachability.

Chunk 2 owns:

```text
_bind_workspace_package(...)
_selected_roots(...)
_traverse_selected_roots(...)
BFS / deque / visited / witness path
```

Do not jump into BFS before Chunk-1 gate is sufficiently met.

## 8. Current Chunk-1 open `[~]` items

These are non-blocking questions to resolve through current source/tests before Chunk 1 closes:

- [~] exactly which `pyproject.toml` facts the current evaluator actually consumes before/while binding the project;
- [~] exactly which `uv.lock` facts the current evaluator consumes before traversal;
- [~] where project/lock information overlaps in the current admitted representation;
- [~] which `_validate_exact_source_identity(...)` checks appear proposition-essential versus defensive/current-design-specific;
- [~] whether repeated provenance validation is proportionate at this semantic trust boundary or could be simplified by stronger upstream invariants;
- [~] one representative identity/provenance test still needs to be inspected and explained at setup/action/assertion/protected-boundary/non-proof depth.

No `[!]` blocking misconception is currently recorded.

## 9. Exact continuation — resume here

Do **not** restart Plan 02 and do **not** advance to graph traversal.

Resume from the corrected Chunk-1 mental model:

```text
1. briefly restate selection declaration vs project evidence vs lock evidence
2. inspect evaluate_uv_selected_environment_membership(...) entry
3. inspect _validate_exact_source_identity(...)
4. group material checks by protected invariant rather than reading validation strings mechanically
5. label each discussed mismatch as NORMAL vs DEFENSIVE/TEST FIXTURE appropriately
6. where material, classify checks as essential/current-design/defensive/uncertain
7. inspect only the parsing stages needed to see what project/lock evidence the current evaluator actually consumes
8. inspect one focused identity/provenance test
9. Ali reconstructs the boundary and test meaning
10. close Chunk 1 only if gate is sufficiently met
11. then proceed to Chunk 2 BFS/reachability
```

Before asking a learner checkpoint, ensure the answer depends only on material already taught or inspected. A checkpoint may be recall, reasoning/prediction, source reconstruction, or open engineering critique; do not test untaught implementation details.

## 10. Do-not-forget proof boundaries

Throughout Plan 02 preserve:

```text
lock presence
!= selected-environment membership

static selection declaration
!= runtime execution

selected-environment membership
!= CI static consumption until exact CI binding

static consumption
!= static direct exercise
!= runtime authority

successful exact-head CI + static consumption
→ supported_not_correlated
!= correlated consuming-step success
!= exact changed runtime version witness
!= resolver currentness
!= behavioral compatibility/safety/action
```

## 11. Recording rule going forward

Keep future entries concise and continuity-oriented:

```text
current chunk/state
material new understanding
Ali-owned evidence
important correction/audit finding
open [~] / [!] items
exact next continuation
```

Do not duplicate full plan/contract rules here. Durable polished teaching content belongs in notes only when explicitly needed.
