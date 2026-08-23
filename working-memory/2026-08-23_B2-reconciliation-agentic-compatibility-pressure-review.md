# B2 Reconciliation — AI / Agentic Compatibility Pressure Review

**Date:** 2026-08-23  
**Status:** REVIEW COMPLETE — compatibility pressure admitted; agentic implementation remains deferred  
**Execution context:** `agent/r1-exact-file-contract-migration`  
**Current owner of live continuation:** `../MEMORY.md`  
**Current implementation plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Why this review exists

During R1 exact-file/dependency-source reconciliation, Ali asked to re-open the project's earlier LLM/AI-engineering and product-agentic work before more source redesign. The purpose is to avoid finishing R1–R7 in a shape that immediately requires another architectural rewrite when the already-approved agentic investigation evaluation is reconsidered.

This review does **not** activate agentic implementation. It uses existing accepted/deferred AI work as architectural pressure while the deterministic substrate is being reconciled.

## 2. AI / LLM artifacts re-read

### Accepted current product LLM architecture

- `docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`

Current accepted role:

```text
authoritative bounded upstream text
→ local LM Studio semantic candidate extraction
→ untrusted structured candidate
→ deterministic exact-source recovery / validation
→ grounded claim or explicit problem
```

The model owns bounded semantic candidate generation only. Deterministic code owns source authority, exact identity, grounding, admitted direction/category, downstream proof strength, security, and action policy.

### Historical/local-model evaluation plan

- `plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`

Important reusable lesson: structured output/schema compliance is not semantic truth. Model output remains untrusted and must degrade explicitly when malformed, ungrounded, ambiguous, or unsupported.

### Product-level AI / agentic reassessment

- `audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`
- `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`

AUDIT-005 concluded that broader product-level agentic behavior is feasible but should first target **investigation orchestration**, not deterministic evidence semantics.

The approved evaluation concept is:

```text
trusted typed InvestigationSnapshot
→ bounded model planner chooses ONE admitted action or STOP/DEFER
→ deterministic action admission
→ read-only capability execution
→ typed evidence/problem
→ deterministic validation / interpretation / reconciliation
→ updated snapshot
```

The model proposes/plans. Deterministic code remains evidence and authority owner.

### Current lifecycle state

AUDIT-005 is **deferred, not rejected**. The agentic evaluation plan is approved but not live while the source-evidence/uv reconciliation is active.

## 3. Compatibility conclusion

The deferred agentic work should influence **how we pressure current contracts**, but it should not cause speculative agent abstractions now.

Correct stance:

```text
ignore future agentic pressure
→ risk avoidable later redesign

build agent/controller/action framework now
→ premature architecture over moving contracts

preferred
→ reconcile deterministic contracts now
→ pressure them for clean later composition
→ introduce agent-specific contracts only when the agentic evaluation is activated
```

## 4. Reconciliation-wide agentic compatibility pressures

Apply these while reviewing R1–R7.

### ACP-1 — Canonical identity/provenance ownership must remain explicit

A future `InvestigationSnapshot` already has its own case identity / exact revision responsibility. Do not duplicate repository/base/head identity into every domain evidence record merely so a future model might need it.

Prefer:

```text
PullRequestIdentity owns PR repository/base/head identity
RepositoryTextFile owns exact-file locator/revision/content
DependencySourceContext owns exact-head source context when later composition needs it
semantic evidence owns only its semantic provenance/result
future InvestigationSnapshot references/composes these canonical owners
```

### ACP-2 — Deterministic domain semantics remain authoritative capabilities

Do not move uv parsing, dependency transition semantics, environment reachability, CI proof composition, exact grounding, or similar deterministic meaning into prompts/model output.

A later planner may choose **which admitted capability to invoke**. It does not become the owner of what that capability's result means.

### ACP-3 — Typed normal problem/uncertainty states are agent-enabling infrastructure

Preserve explicit states such as unavailable, malformed, unsupported, unresolved, conflicting, not-established, and bounded witness results where the responsibility genuinely produces them.

These states allow a later planner to choose another action or stop/defer without guessing from exceptions or prose.

Do not invent extra states only for an agent. Keep the smallest semantically true domain states.

### ACP-4 — Internal helpers do not become public/trust boundaries merely for hypothetical agent calls

The future action executor needs **supported capabilities**, not arbitrary direct access to every source-specific helper.

Therefore:

```text
future planner might need dependency evidence
!= preserve duplicate validation inside raw uv_lock.py / pyproject.py extractors
```

If a later agentic action requires a separately supported invocation boundary, admit a deterministic adapter/wrapper at that time and validate at that boundary.

This preserves `JUST-004` / `JUST-005`: future possibility is architectural pressure, not current retention authority.

### ACP-5 — Avoid fixed-orchestration-only domain design

Do not hide domain truth inside `investigation.py` branches or ambient mutable orchestration state when a clear typed domain result/capability naturally owns it.

Current fixed orchestration may call the capability today; a later deterministic action executor may call the same capability tomorrow.

This does **not** require generic plugins, registries, MCP, or action catalogs during reconciliation.

### ACP-6 — Keep proof boundaries machine-readable enough for deterministic admission

The future planner must not infer that:

```text
static evidence == runtime execution
missing == negative
lock reachability == lock currentness/resolver success
model claim == source truth
green CI == changed behavior proven
```

R1–R5 proof distinctions therefore serve both today's deterministic product and later agentic action/stop safety.

### ACP-7 — Do not optimize current contracts for model context size prematurely

Smaller, non-duplicated evidence contracts are desirable because they improve ownership and reduce ambiguity, not because they save LLM tokens.

A future `InvestigationSnapshot` should project only the facts needed for planning. Domain contracts must remain truthful independently of any prompt representation.

## 5. Step-2B decisions pressure-tested against the agentic plan

### `DependencyChangeSourceEvidence` target remains minimal

Current Step-2B trace target:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

**Agentic compatibility result: KEEP THIS DIRECTION.**

The agentic plan's conceptual `InvestigationSnapshot` explicitly owns case identity/exact revision separately from established findings. Therefore `base_revision` / `head_revision` do not need to remain duplicated in every dependency-source record for future planning.

### Removing extractor-level repository/path rebinding remains correct

The normal supported dependency capability is assembled through `analyze_dependency_change(...)` + `GitHubRepositoryClient`. A future planner can invoke an admitted analysis/action wrapper rather than treating `extract_uv_lock_changes(...)` or `extract_pyproject_optional_extra_change(...)` as independent untrusted composition boundaries.

Do not retain repeated guards solely to make those helpers safe against hypothetical agent misuse.

### Source-specific semantic functions should remain deterministic and explicit

Removing upstream-owned PR-binding checks must not turn the extractors into prompt logic. They still own actual uv/pyproject parsing and transition semantics under their admitted preconditions.

Their source documentation should state those preconditions clearly.

## 6. Pressure on later reconciliation steps

### R2 — shared uv structural model

Agentic pressure strengthens the existing R2 direction:

```text
exact uv.lock
→ one deterministic bounded structural interpretation
→ separate deterministic semantic consumers
```

A later planner should not need to understand uv's lock schema itself. It should receive typed results/problems from deterministic capabilities.

Do not create a generic package-manager graph merely because an agent could use one.

### R3 / R4 — scope and selected-root reachability

Preserving real workspace/project scope, explicit selectors, witnesses, and `unresolved` behavior is especially important for future next-action / stop-defer planning.

A planner can safely reason from:

```text
member with witness
not_established within a stated complete modeled scope
unresolved because scope/markers/ambiguity exceed current support
```

It cannot safely reason from an over-broad boolean `member = false` whose proof domain is unclear.

### R5 — CI consumption

Keep static consumption, static direct exercise, and runtime authority distinct. A future agent must not choose to stop merely because one weaker proof class looks superficially positive.

### R6 — changed-case pressure

S001, S011, S005, and workspace transfer remain useful not only as deterministic regressions but also as materially different future planner states. Do not reshape implementation around their literal strings or expected actions.

### R7 — mandatory agentic-plan re-review remains correct

After reconciliation closes, re-read AUDIT-005 and `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` against the **new actual contracts** before activation.

Concrete type names and substrate assumptions in the old agentic plan are not frozen architecture. Its durable conceptual boundary is what matters:

```text
model planning
!= deterministic evidence authority
```

## 7. No active-plan rewrite required now

The current reconciliation plan already:

- lists AUDIT-005 as a deferred but important proof guard;
- explicitly defers the agentic evaluation while contracts are reconciled;
- prohibits introducing an agentic controller during R1–R7;
- requires deferred-plan re-review at R7 rather than blindly resuming stale work.

Therefore a second agentic mini-plan inside the active reconciliation plan would duplicate responsibility and add ceremony without a new requirement.

The new operational refinement is this review's compatibility pressure: **when making a consequential R1–R7 contract/ownership decision, check that it preserves a clean deterministic capability/evidence boundary suitable for either today's fixed orchestration or a later explicitly admitted action adapter.**

## 8. Current continuation consequence

No source decision is reversed by this review.

Current continuation remains:

```text
R1 Step 2B trace        COMPLETE
→ R1 Step 2B code       NEXT
→ R1 Step 2C
→ R2 ...
```

Before each consequential later structural decision, apply both:

```text
end-to-end responsibility trace (JUST-004 / JUST-005)
+
agentic compatibility pressure (this review)
```

Neither permits speculative future-proofing. A mechanism still requires a current product/proof/risk/compatibility justification to exist now.
