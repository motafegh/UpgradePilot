# Live Learning and Review Notes

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Branch:** `agent/learning-current-implementation`  
**Started:** 2026-08-03  
**Status:** live learning/review capture; non-controlling

## Purpose

This file is the lightweight intermediate capture layer for things discovered while learning the current UpgradePilot implementation.

The active learning process is intentionally broader than passive code reading:

```text
inspect implementation
→ build the mental model
→ predict behavior
→ challenge the design
→ discover limitations or questions
→ inspect evidence
→ correct the model
→ preserve useful observations
```

Use this file when an observation is worth keeping but is not yet mature enough to become a formal audit, stable learning note, implementation plan, ADR, or project-state update.

Typical contents include:

- learning mechanisms worth remembering;
- source-code relationships that became clear during discussion;
- design questions exposed by learning;
- possible limitations or defects that still need inspection;
- audit candidates that are not yet justified as formal audits;
- questions to revisit after another source/test boundary is understood;
- observations later promoted into durable learning notes or `audits/` records.

## Authority boundary

This file is **not** project-control authority.

It does not own or replace:

- `MEMORY.md` for live project state and continuation;
- plans or specifications for selected work;
- ADRs for accepted architecture;
- source/tests for implemented behavior;
- `audits/` for mature durable technical audits;
- dated session notes for distilled learning evidence.

A statement here may be provisional, incomplete, or later shown to be a misunderstanding. Preserve that uncertainty explicitly.

A useful lifecycle is:

```text
conversation / source-code learning
→ LIVE_LEARNING_AND_REVIEW_NOTES.md
   ├── learning point
   ├── open review observation
   └── question to revisit
→ later evidence review
   ├── promote mature concern → audits/AUDIT-NNN on main
   ├── promote durable understanding → session/learning notes
   ├── mark resolved / misunderstanding
   └── discard or supersede low-value scratch detail
```

Do not create a formal audit merely because a line of code is interesting or debatable. First establish the actual implemented behavior, consequence, and proof boundary.

## Update discipline

Keep this file useful rather than exhaustive.

When adding an item:

1. state what was actually observed;
2. distinguish code fact from interpretation;
3. identify the relevant source/test boundary when known;
4. avoid calling something a defect before the consequence is established;
5. record what evidence would be needed before promotion;
6. move mature concerns to `audits/` instead of duplicating a full audit here;
7. preserve durable learning separately when a session checkpoint is written.

Suggested review classifications:

```text
observation
question
possible limitation
possible defect
audit candidate
resolved / no issue
promoted to audit
```

Suggested learning classifications:

```text
mental model
Python mechanism
architecture/design insight
boundary/nonclaim
question to revisit
```

---

# Current learning position

The active source-learning path remains in **Unit 2 — one complete CI `proven` path** from `LEARNING_SESSION_PLAN.md`.

The current code under study is the aggregate portion of:

```text
src/upgradepilot/ci_dependency_exercise.py
```

Current conceptual path:

```text
workflow_inputs
→ evaluate every workflow independently
→ materialize all WorkflowDependencyExerciseResult records
→ select one `proven` witness if any exists
→ map per-workflow evidence to the aggregate DependencyCIExerciseResult
```

The branch has been synchronized with current `main`; later Step 5 acquisition work is recorded for future intake but does not change the present lesson order.

---

# Open review observations

## LR-001 — Aggregate CI detail names only the first proof witness

**Classification:** question / possible diagnostic-presentation limitation  
**Seen while learning:** Unit 2 aggregate CI evaluation  
**Primary source:** `src/upgradepilot/ci_dependency_exercise.py`  
**Current disposition:** preserve for later inspection; not yet a formal audit finding

### Observed behavior

The aggregate evaluator first materializes every per-workflow result:

```python
results = tuple(
    _evaluate_workflow_dependency_exercise(...)
    for workflow_input in workflow_inputs
)
```

It then selects the first result whose state is `proven`:

```python
proven = next(
    (result for result in results if result.state == "proven"),
    None,
)
```

When a witness exists, the aggregate detail uses:

```python
proven.workflow_name
```

while the aggregate object still preserves:

```python
workflows=results
```

Therefore, for:

```text
Workflow A → unresolved
Workflow B → proven
Workflow C → proven
```

current semantics are approximately:

```text
aggregate state = proven
selected witness for detail = Workflow B
preserved workflow evidence = A + B + C
```

### What is currently correct

The aggregate product question is existential:

```text
Does at least one admitted successful exact-head workflow path satisfy the current dependency-exercise rule?
```

For that decision, one witness is sufficient. Selecting the first `proven` result does not make the aggregate-state logic incorrect.

All per-workflow results are already evaluated before witness selection, and `workflows=results` preserves them. Workflow C is therefore not lost merely because `next(...)` stops after finding B.

### Review question

Decision and presentation have different information needs:

```text
aggregate-state decision
→ one witness is sufficient

human-facing evidence summary
→ several proof witnesses may be relevant
```

The current detail names one workflow even when several workflows independently satisfy the rule.

That detail is not necessarily false; it describes one sufficient witness. But it may be incomplete or unnecessarily narrow if a caller treats the aggregate `detail` as the summary of all supporting CI evidence.

### Candidate alternatives to evaluate later

Do not implement from this note alone. Possible shapes include:

```text
A. Keep one witness and explicitly word the detail as "At least one workflow ..."

B. Collect proven_results and summarize the count/names of all proven workflows

C. Keep concise aggregate detail and rely on workflows=results for per-workflow evidence
```

### Evidence required before promotion

Before deciding whether this deserves a formal audit or source change, inspect:

- the intended contract of aggregate `detail`;
- CLI rendering and other consumers of `DependencyCIExerciseResult.detail`;
- tests that protect the exact current wording/semantics;
- whether multiple simultaneously proven workflows occur in supported public cases;
- whether naming only one witness can cause a materially misleading downstream conclusion rather than merely less-complete diagnostics.

### Current judgment

```text
not an aggregation correctness defect
likely a presentation/diagnostic design question
formal audit not yet justified
```

---

# Learning points worth preserving

## LP-001 — `tuple(generator_expression)` materializes all per-workflow results

**Classification:** Python mechanism + mental model

Code shape:

```python
results = tuple(
    _evaluate_workflow_dependency_exercise(...)
    for workflow_input in workflow_inputs
)
```

The inner generator expression yields one per-workflow result at a time, but `tuple(...)` immediately consumes it completely.

After the statement finishes:

```text
results
```

contains completed result objects, not deferred computations.

For inputs A, B, C:

```text
A → evaluate once → Result A
B → evaluate once → Result B
C → evaluate once → Result C

results = (Result A, Result B, Result C)
```

The tuple provides an ordered fixed snapshot of the evaluated workflow results and matches the aggregate result contract that stores a tuple of workflow results.

## LP-002 — `next(...)` implements existential witness selection, not full evidence collection

**Classification:** Python mechanism + architecture/design insight

Code:

```python
proven = next(
    (result for result in results if result.state == "proven"),
    None,
)
```

Its responsibility is:

```text
find the first complete result object satisfying state == "proven"
```

This implements the existential rule:

```text
∃ result in results such that result.state == "proven"
```

It differs from:

```python
any(result.state == "proven" for result in results)
```

because `any(...)` would preserve only a Boolean answer, while `next(...)` preserves one actual proof witness that can later supply evidence such as `workflow_name`.

Important distinction:

```text
results
→ complete already-evaluated workflow evidence

proven
→ one witness sufficient for existential aggregation
```

## LP-003 — `next(generator, None)` represents expected absence without `StopIteration`

**Classification:** Python mechanism

When no result has:

```python
state == "proven"
```

this form:

```python
next(generator, None)
```

returns:

```python
None
```

rather than allowing `StopIteration` to escape.

Here, absence of a proven workflow is an expected product situation, not a programming exception.

Therefore:

```python
if proven is not None:
```

means:

```text
Did witness selection return an actual WorkflowDependencyExerciseResult rather than the explicit absence marker?
```

## LP-004 — Stopping the witness search does not stop earlier workflow evaluation

**Classification:** mental model

This distinction was important during discussion.

Because `results = tuple(...)` runs before `next(...)`, every workflow has already been evaluated.

With:

```text
A → unresolved
B → proven
C → proven
```

`next(...)` stops its **search** after B, but C was already evaluated when `results` was materialized.

So distinguish:

```text
per-workflow evaluation
```

from:

```text
later aggregate witness search
```

Stopping the second operation does not undo or skip the first.

## LP-005 — One witness decides the existential state while all evidence remains preserved

**Classification:** architecture/design insight

Current aggregate behavior intentionally separates:

```text
proof sufficiency
```

from:

```text
evidence preservation
```

One `proven` workflow is enough for overall `state="proven"`, but the returned aggregate record uses:

```python
workflows=results
```

so weaker, unresolved, failed, or additional proven workflow results remain available.

This avoids incorrectly turning:

```text
"one path proved the narrow proposition"
```

into:

```text
"all workflows were healthy or proved the same thing"
```

## LP-006 — Aggregate and per-workflow evaluators have different responsibilities

**Classification:** architecture/design insight

Current responsibility split:

```text
_evaluate_workflow_dependency_exercise(...)
→ interpret ONE workflow bundle


evaluate_dependency_ci_exercise(...)
→ aggregate the already-classified workflow results
```

The outer evaluator should not need to reproduce the complete command/definition decision path used to classify each workflow. It asks aggregate questions over those results instead.

This is why witness selection can operate only on:

```python
result.state
```

rather than re-reading workflow commands.

## LP-007 — `assert` expresses an internal invariant, not an ordinary evidence state

**Classification:** Python mechanism + boundary/nonclaim

After a proven witness is found, current code asserts:

```python
assert direct_requirements_install_path is not None
```

The per-workflow decision order should already make this true:

```text
no direct requirements path
→ unresolved
→ cannot legitimately produce a proven workflow result
```

Therefore the assertion represents an internal invariant:

```text
proven workflow witness
→ direct requirements path must exist
```

This differs from an ordinary product state.

```text
expected incomplete/unsupported evidence
→ explicit product result such as unresolved

impossible internal contract combination
→ assertion/programming defect
```

## LP-008 — Aggregate `state`, `reason`, `detail`, and `workflows` serve different roles

**Classification:** architecture/design insight

For the successful aggregate path:

```text
state
→ broad outcome category: proven

reason
→ machine-readable rule explaining why the state was reached

detail
→ human-readable explanation using the selected witness/path/package

workflows
→ complete preserved per-workflow result evidence
```

Do not assume the human-readable `detail` is the complete evidence model. That distinction is directly relevant to LR-001.

---

# Promoted / already formalized review findings

## PR-001 — CI dependency-exercise proof boundary

**Status:** promoted to formal audit on `main`  
**Formal record:** `audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`

During learning we identified that the current CI `proven` rule combines successful exact-head run/job evidence with static recognized install/exercise commands, but does not independently establish all relevant execution semantics.

Important formalized concerns include:

```text
failure masking such as `|| true`
continue-on-error
conditional/skipped execution
install-before-exercise ordering
matched-command runtime-step success
exact proposed-version runtime observation
interpreter/environment continuity
```

The formal audit owns the complete technical reasoning, source references, strengthening options, reassessment triggers, and proof obligations.

Do not recreate AUDIT-002 here. This live file should only preserve the learning connection:

```text
current bounded static proof rule
≠
independent per-command runtime proof
```

and remind future learning sessions to use AUDIT-002 as the design-review companion when Unit 4 reaches the workflow-command reader and its proof boundary.

---

# Questions to revisit

## Q-001 — Should witness selection and aggregate presentation use the same data shape?

Current decision logic needs only one witness. Human-facing explanation may benefit from knowing all proven witnesses.

Revisit after inspecting the aggregate result consumers and CLI rendering.

## Q-002 — Is first-witness ordering intentionally meaningful anywhere?

`next(...)` selects the first proven result according to the order of `results`.

Questions:

- Is that order guaranteed to have meaningful product semantics or merely acquisition order?
- If the selected workflow name appears in public detail, could order changes alter diagnostics without changing evidence strength?
- Would generic "at least one workflow" wording better avoid accidental importance being assigned to the first witness?

Do not infer a problem until caller/output behavior is inspected.

## Q-003 — When Unit 4 reaches the workflow reader, which findings remain learning questions versus audit concerns?

Use AUDIT-002 to avoid rediscovering already formalized issues, but independently understand the source mechanism first.

The learning goal is not simply to accept the audit conclusions. It is to be able to explain how the current implementation produces the relevant behavior and why the stronger proof alternatives change the evidence boundary.

---

# Promotion checklist

Before promoting an open review observation into a new formal audit, establish as many of these as relevant:

```text
[ ] exact implemented behavior confirmed from current source
[ ] relevant tests/consumers inspected
[ ] consequence is more than stylistic preference
[ ] current product/architecture claim identified
[ ] concern classified accurately: defect, risk, limitation, simplification, or reassessment
[ ] plausible alternatives and tradeoffs understood
[ ] existing audit/ADR does not already own the issue
[ ] proof required for a future change can be stated
```

Before promoting a learning point into a durable session note, establish:

```text
[ ] mental model can be explained without copying source prose
[ ] relevant Python/technical terminology is understood
[ ] product meaning is separated from implementation syntax
[ ] at least one changed-case prediction has been attempted when useful
[ ] nonclaims and boundaries are preserved
```

---

# Session-use reminder

During active learning, update this file selectively when a point would otherwise be lost across sessions.

Do not interrupt every small code explanation to write notes. Capture material observations at natural checkpoints, then continue the learning path.

The intended balance is:

```text
learn first
challenge when useful
capture material insight
continue
periodically distill
```

rather than turning learning into documentation ceremony.
