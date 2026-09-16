# Cycle 2 Phase D Integrated Learning / Ownership Plan — Working Memory

**Date:** 2026-09-16  
**Session status:** ACTIVE  
**Primary responsibility:** Cycle 2 Phase D — integrated post-implementation learning and engineering-ownership check  
**Primary execution mode for D:** Learning-Only — product/source/test mutation paused unless Ali explicitly changes the action boundary later  
**Previous closure:** [`2026-09-16_cycle2-phase-b-hosted-proof-closure.md`](2026-09-16_cycle2-phase-b-hosted-proof-closure.md)  
**Phase A design record:** [`2026-09-14_static-command-consumer-migration-and-identity.md`](2026-09-14_static-command-consumer-migration-and-identity.md)  
**Phase B engineering record:** [`2026-09-15_cycle2-static-consumer-build.md`](2026-09-15_cycle2-static-consumer-build.md)  
**Hosted proof repairs:** [`2026-09-16_phase-b-hosted-proof-repair.md`](2026-09-16_phase-b-hosted-proof-repair.md), [`2026-09-16_phase-b-hosted-proof-repair-3.md`](2026-09-16_phase-b-hosted-proof-repair-3.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

## 1. Phase-D anchor

Cycle 2 exists to migrate static CI/dependency consumers onto the trusted parser-backed command-analysis producer while correcting command identity and bounded static ordering.

Current cycle position:

```text
A — COMPLETE
    substantial design/orientation: A1–A6 accepted migration contract

B — COMPLETE / CLOSED
    B1–B5 implementation + hosted executable proof green

C — COMPLETE through progressive preservation
    Phase-A decisions, B1–B5 engineering progression, hosted failures/repairs,
    final proof, and live continuation are all preserved in their normal owners

D — ACTIVE / THIS RECORD
    integrated learning + engineering-ownership check over stable final source

E — PENDING
    repair only demonstrated learning/ownership gaps, then orient Cycle 3

Cycle 3 — NOT STARTED
```

Phase D is deliberately separated from the long Phase-B implementation so we learn the **stable final architecture**, not a sequence of transitional snapshots.

This working memory is the Phase-D control/checklist and progression record. It is not a second specification, ADR, or permanent learning artifact. Stable semantics remain with their accepted owners; source/tests remain implementation truth.

## 2. What Phase D must accomplish

Phase D should make Ali able to **own the engineering responsibility**, not reproduce every line or library API from memory.

The central ownership target is:

```text
exact GitHub Actions workflow run step
→ effective shell / parser-neutral command analysis
→ real static command occurrence + canonical source identity
→ dependency / project-environment / package-invocation interpretation
→ one-pass CI composition
→ bounded static ordering
→ explicit proof and non-proof boundary
```

By D closure, Ali should be able to:

1. explain why Cycle 2 was needed and reconstruct the A1–A6 design responsibilities;
2. trace the final producer → consumers → CI composition flow through the important source owners;
3. distinguish workflow/job/step identity, inner command occurrence identity, source order, static ordering, runtime correlation, execution, and success;
4. explain why parser-neutral IR belongs above dependency/CI domain semantics;
5. reason about direct requirements, project-environment selection, and direct package invocation without treating them as equivalent propositions;
6. explain why unresolved step-level evidence may legitimately have no exact inner-command identity;
7. explain why B4's one-analysis/single-traversal shape is a correctness boundary, not merely an optimization;
8. use representative tests to state what is proven and what remains unproven;
9. trace one requirements-shaped case and one project-environment case end to end;
10. classify the important hosted-proof failures and defend why the repairs preserved rather than weakened the architecture;
11. identify exactly what Cycle 2 still does **not** prove and therefore belongs to Cycle 3 or later responsibilities;
12. reason through at least one nearby changed case without replaying the exact taught example.

## 3. Depth calibration

### Must own at high practical depth

These are central Cycle-2 responsibilities and should be explainable, traceable, testable, and challengeable:

- A1–A6 and the engineering reason for each;
- provider / dependency / CI ownership boundaries;
- `StaticCommandAnalysis`, `StaticCommandOccurrence`, and `StaticCommandLocation` at the level needed to trace consumers;
- outer workflow/job/step identity versus inner command source identity;
- why `segment_index` was overloaded and why identity/order/placeholder concerns were separated;
- literal versus dynamic/unsupported material command atoms at the consumer boundary;
- direct requirements versus project-environment versus package-invocation propositions;
- one-analysis / one-production-traversal handoff;
- canonical identity preservation through composition;
- `ordered_after | not_after | unresolved` and why source order is not execution-path proof;
- static occurrence versus execution versus success;
- unresolved evidence and non-fabrication of identity;
- representative proof tests and their non-claims;
- the proof-gate failures that exposed real/stale architectural clients.

### Understand operationally

Know what these do and where they matter; exact internals may be looked up:

- effective-shell resolution details already proven in Cycle 1;
- Tree-sitter CST/node layouts and individual grammar adapter internals;
- exact helper loops for every pip/uv option;
- every selector/enum/dataclass field in `environment_selection.py`;
- every reachability/membership branch below the project-environment composition seam;
- checkout-provenance helper details beyond the central fact that evidence must refer to the changed repository context;
- exact reason-string spelling except where a reason change demonstrates ownership/uncertainty movement;
- individual commit hashes and workflow run IDs;
- GitHub Git-object plumbing used during the B5 atomic-commit recovery.

### Recognize / lookup level

- incidental Python syntax or dataclass mechanics;
- exact Tree-sitter Python binding calls;
- complete uv/pip CLI option catalogs;
- all 587 tests individually;
- every test fixture constructor or helper.

### Deliberately deferred

Do not let Phase D expand into responsibilities Cycle 2 did not own:

- Cycle-3 runtime-strengthening eligibility design/implementation beyond understanding its boundary;
- arbitrary GitHub expression evaluation;
- matrix expansion / reusable-workflow execution;
- general control-flow simulation;
- Python/custom-interpreter command analysis;
- runtime log/artifact parsing as command proof;
- exact installed dependency version / selected wheel / compatibility evidence;
- Target redesign unrelated to the demonstrated downstream migration residue;
- maintainer-action enablement beyond the current synthesis baseline.

## 4. Stable source/test map for Phase D

Use only the source/tests needed by the active block rather than loading the whole repository.

### Provider / identity seam

```text
src/upgradepilot/github/workflow_command_analysis.py
src/upgradepilot/github/workflow_command_location.py
```

Cycle 1 parser internals are supporting context; Cycle 2 learning starts at the parser-neutral outputs and their identity meaning.

### Dependency semantics

```text
src/upgradepilot/dependency/pip_command.py
src/upgradepilot/dependency/direct_install.py
src/upgradepilot/dependency/environment_selection.py
```

Use reachability/membership owners only when the real project-environment case reaches them:

```text
src/upgradepilot/dependency/uv_reachability.py
src/upgradepilot/dependency/environment_membership.py
```

### CI ownership and composition

```text
src/upgradepilot/ci/consumption.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/static_command_order.py
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/investigation.py
```

### Representative tests

Core proofs to understand, not memorize:

```text
tests/test_parser_backed_ci_command_evidence.py
tests/test_static_command_order.py
tests/test_single_pass_workflow_static_evidence.py
tests/test_direct_install_declaration.py
tests/test_project_environment_selection.py
tests/test_ci_static_direct_exercise_order.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_coverage.py
tests/test_r6_project_environment_workflow_integration.py
tests/test_r6_project_source_workflow_integration.py
```

Use narrower tests from adjacent modules only when a question requires them.

## 5. Phase-D learning route and checklist

Statuses are updated as learning progresses:

```text
PENDING → IN PROGRESS → DONE
```

A block is DONE only after both explanation/tracing and a proportionate Ali ownership check. Agreement or immediate repetition alone is not completion evidence.

### D1 — Reconstruct the Cycle-2 problem and Phase-A design

**Status:** PENDING

Cover:

- what the old consumers did before Cycle 2;
- why duplicate textual splitting / regex / `shlex` command meaning was unsafe;
- why `segment_index` had become three responsibilities hidden in one integer;
- why one trusted provider-owned command analysis should feed several domain consumers;
- reconstruct A1–A6 and map each design decision to the final responsibility it created.

Primary evidence:

- Phase-A working memory;
- Phase-B final architecture summary;
- relevant final source signatures, not transitional source snapshots.

Depth:

- **must own** the problem statement, A1–A6, and owner/layer placement;
- transitional implementation details are historical context only.

Completion check:

Ali can explain the before → design correction → expected final architecture without relying on file-by-file narration.

---

### D2 — Canonical command identity and bounded static ordering

**Status:** PENDING

Trace:

```text
StaticCommandOccurrence
→ StaticCommandLocation(source_span, source_order)
→ StaticDependencyConsumptionEvidence / DirectPackageInvocationEvidence
→ relate_invocation_after_consumption(...)
```

Cover:

- outer workflow/revision/job/step identity versus inner command identity;
- why `source_order` is part of source identity/order reasoning but is not runtime identity;
- why missing same-step inner identity becomes `unresolved`;
- later different step versus later same-step occurrence;
- path-dependent structures and why later source position can still be unresolved;
- why same/earlier occurrence is `not_after`.

Primary proof:

- `tests/test_static_command_order.py`;
- relevant direct-exercise order regression.

Depth:

- **must own** identity/order/proof distinctions;
- exact byte-span arithmetic is operational detail.

Completion check:

Given a few changed command placements/structures, Ali can classify what identity exists and whether ordering is `ordered_after`, `not_after`, or `unresolved`, with the correct non-proof statement.

---

### D3 — Parser-neutral command facts versus dependency/CI semantics

**Status:** PENDING

Follow one requirements command and one project-environment command:

```text
RunStepDefinition
→ StaticCommandAnalysis / typed atoms
→ dependency-owned interpretation
→ domain observation/evidence
```

Cover:

- why GitHub/provider owns shell syntax and parser-neutral occurrences;
- why dependency code owns pip requirements/local-project/uv selector meaning;
- why CI owns changed-package direct invocation meaning;
- role of `parsed_pip_install_arguments(...)` as a narrow shared dependency-domain prefix recognizer rather than generic utility;
- literal versus dynamic/unsupported material atoms;
- why unrelated uncertainty may coexist with an already sound positive static fact;
- why no consumer reparses raw shell text as a positive fallback.

Primary source:

- `pip_command.py`;
- `direct_install.py`;
- the bounded relevant portions of `environment_selection.py` and `workflow_commands.py`.

Primary proof:

- direct-install tests;
- project-environment selection tests;
- parser-backed CI command-evidence tests.

Depth:

- **must own** the domain-boundary model and representative command interpretations;
- do not memorize the full pip/uv option machinery.

Completion check:

Ali can trace and classify representative literal/dynamic commands and explain which layer is allowed to decide each proposition.

---

### D4 — One-analysis production handoff and project-environment composition

**Status:** PENDING

Trace the final normal path:

```text
investigation.py
→ WorkflowDependencyCoverageInput(project_environment_sources=...)
→ inspect_workflow_dependency_evidence(...)
→ parse one WorkflowDefinition
→ one job/step traversal
→ analyze_run_step_commands(...) once per RunStepDefinition
→ same analysis to direct requirements + project environment + package invocation
```

Then follow project-environment evidence far enough to distinguish:

```text
visible project selection
→ project membership / uv reachability
→ CI dependency consumption evidence
```

Cover:

- why B4 was needed even after every consumer individually used the correct parser;
- why `derive_project_environment_consumptions(...)` may remain as a standalone test/compatibility entry without becoming a second semantic implementation;
- why normal production passes **sources** rather than detached precomposed consumptions;
- why canonical identity can be lost if evidence is derived separately and reattached later;
- checkout provenance as part of source binding, without deep-diving every helper.

Primary proof:

- `tests/test_single_pass_workflow_static_evidence.py`;
- `tests/test_workflow_dependency_evidence.py`;
- relevant R6 integration tests.

Depth:

- **must own** the single-traversal correctness rationale and cross-layer handoff;
- lower reachability algorithms are operational unless needed for the selected real case.

Completion check:

Ali can explain why “same parser in two traversals” was still insufficient and why the final source-in/single-traversal route preserves a stronger identity/composition invariant.

---

### D5 — Real cases: S001-style uv and S011-style pyproject

**Status:** PENDING

Use two representative cases to integrate the architecture.

#### Case A — S001-style uv project environment

Trace a real-shaped path such as:

```text
uv sync --all-packages --group docs
→ visible selection + package scope
→ uv-lock selected-root reachability
→ transitive witness to changed package
→ static project-environment consumption
```

Use the real regression facts in `test_r6_project_environment_workflow_integration.py`, including the docs-group witness to `soupsieve` and the dynamic-group unresolved case when useful.

#### Case B — S011-style pyproject optional extra

Trace:

```text
pip install -e ".[dev]"
+ changed dependency belongs to [project.optional-dependencies].mlx
→ visible dev selection
→ selected environment membership NOT established for mlx
→ changed dependency consumption NOT established
```

Use `test_r6_project_source_workflow_integration.py`.

Cover:

- selection is not membership/reachability;
- membership/reachability is not execution;
- positive and negative/not-established evidence both depend on exact source/context identity;
- unresolved remains distinct from not established.

Depth:

- **must own** the evidence transformation and proof boundary;
- exact lock parser details and all possible selectors remain operational/deferred.

Completion check:

Ali can trace both cases from workflow command to final static consumption result and explain exactly which proposition changes between the two cases.

---

### D6 — Static presence, direct exercise, runtime boundary, and proof discipline

**Status:** PENDING

Connect Cycle-2 static evidence to the existing CI coverage layer without entering Cycle-3 implementation.

Cover:

```text
static command exists
!= static direct exercise established
!= command executed
!= command succeeded
```

Use:

- clean linear same-step example;
- later separate-step example;
- short-circuit/conditional example;
- missing canonical inner identity example;
- representative `dependency_exercise.py` classification flow.

Clarify:

- Cycle 2 may establish supported static consumption/direct exercise;
- existing step-level runtime correlation is a separate proposition;
- Cycle 3 will decide when whole-step success may legitimately strengthen specific command occurrences under the new structural model;
- Phase D should understand this boundary but not pre-design Cycle 3.

Primary proof:

- static-order tests;
- CI static direct-exercise tests;
- relevant runtime-correlated coverage test only as a boundary example.

Completion check:

Ali can reject an overclaim such as “the workflow succeeded, so every parsed command ran” and state the minimum additional proposition that would be needed.

---

### D7 — Proof failures, migration cleanup, and final ownership synthesis

**Status:** PENDING

Use the Phase-B hosted proof history as a compact engineering/debugging lesson, not a chronology quiz.

Must understand these incidents:

1. **missed Target consumer** — strict `command_analysis` API was correct; a secondary downstream caller had not migrated;
2. **stale B5 test fixture** — removed `segment_index` survived in a lower-domain constructor;
3. **dynamic GitHub-expression case** — final uncertainty moved to the earlier provider-owned command-analysis boundary without changing the conservative final proposition;
4. **detached precomposed unresolved evidence** — step-level unresolved evidence had no earned inner command identity, so the compatibility seam correctly rejected rebinding; the real production source-in/single-traversal path was the right fix;
5. **B5 atomic Git-object failure** — operational lesson only: atomic publication prevented partial product state;
6. **final hosted proof** — fresh install, `pip check`, focused investigation 15/15, full deterministic suite 587/587.

Do not memorize run IDs, commit hashes, or raw logs. Learn how to classify:

```text
real source regression
stale fixture/client
changed trustworthy uncertainty owner
stale architectural test path
execution/tooling failure
```

Final synthesis must explicitly cover:

```text
what existed before Cycle 2
→ what was wrong/overloaded
→ what A decided
→ what B actually built
→ what proof failures taught us
→ what final implementation guarantees
→ what final implementation deliberately does not guarantee
```

Ownership checks:

- one end-to-end verbal/source trace chosen by Ali;
- one representative test explained as setup → action → assertion → proof → non-proof;
- one changed-context classification problem;
- one design judgment: defend an ownership/layer decision or identify a credible alternative/trade-off;
- identify any remaining must-own gap honestly.

Completion condition for D7:

Ali demonstrates proportionate ownership of the Cycle-2 responsibility without needing to reproduce incidental syntax or every helper implementation.

## 6. Newly discovered learning items

If a meaningful gap appears that this plan did not anticipate, add it here rather than silently expanding another block.

Use:

| ID | Item discovered | Why it matters to Cycle 2 ownership | Depth | Status / destination |
|---|---|---|---|---|
| — | none yet | — | — | — |

Rules:

- add only items that materially affect current Cycle-2 understanding, proof, modification, diagnosis, or Cycle-3 readiness;
- classify each as **must own**, **operational**, **recognize/lookup**, or **deferred**;
- a question does not automatically become a new lesson block;
- if the item exposes an implementation/design defect, record it but do **not** mutate product source while Learning-Only is active; explicitly transition to Audit/Planning/Build later if Ali authorizes it.

## 7. Phase-D progress record

Update this compact table after meaningful learning checkpoints.

| Block | Status | What was established | Open gap / next |
|---|---|---|---|
| D1 problem + A1–A6 design | PENDING | — | start here |
| D2 identity + static ordering | PENDING | — | — |
| D3 parser-neutral facts → domain semantics | PENDING | — | — |
| D4 one-analysis composition | PENDING | — | — |
| D5 S001 + S011 real cases | PENDING | — | — |
| D6 static/runtime/proof boundary | PENDING | — | — |
| D7 proof failures + synthesis | PENDING | — | — |

Do not mark a block DONE merely because the explanation was delivered. Preserve the ownership evidence or remaining gap in concise form.

## 8. Phase-D completion gate

Phase D closes only when:

- D1–D7 are DONE or an item is explicitly reclassified as safely operational/deferred;
- all **must-own** newly discovered items are resolved;
- Ali can reconstruct the important normal flow and the material unresolved/failure boundaries;
- Ali can explain the main ownership split across GitHub/provider, dependency, and CI;
- Ali can distinguish command identity, static ordering, execution, runtime correlation, and success;
- Ali can interpret representative tests and their non-claims;
- Ali can trace the two selected real cases;
- Ali can reason about at least one nearby changed case;
- no unexamined gap remains that would make Cycle-3 reasoning depend on black-box Cycle-2 behavior.

D closure does **not** require:

- memorizing all source;
- recreating code unaided;
- mastering Tree-sitter internals;
- memorizing pip/uv option tables;
- reviewing every test;
- learning Cycle-3 implementation before its A phase.

## 9. Phase E handoff after D

After D closes:

1. collect only demonstrated remaining gaps;
2. repair learning/prerequisite gaps at the minimum useful depth;
3. if a real product/design defect was discovered, separately select the appropriate Audit/Planning/Build route before mutation;
4. reconcile `MEMORY.md` and this working memory;
5. orient Cycle 3 A only after Ali has sufficient Cycle-2 ownership.

Do not start Cycle 3 merely because all explanations were presented.

## 10. Immediate next action

Start **D1 — Reconstruct the Cycle-2 problem and Phase-A A1–A6 design** in Learning-Only mode.

Use the Phase-A decision memory as rationale/provenance and the final source as implementation truth. Do not teach B1–B5 commit chronology as the primary structure; use chronology only when it explains an important engineering pressure or correction.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
