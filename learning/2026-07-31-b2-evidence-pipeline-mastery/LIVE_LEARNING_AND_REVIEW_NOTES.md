# Live Learning and Review Notes

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Branch:** `agent/learning-current-implementation`  
**Status:** live learning/review capture; non-controlling  
**Current synchronized main baseline:** `7db6a6b6f0f6c261d98c6df66d51e14eb99359cd`

## Purpose

This file is the lightweight intermediate capture layer for material observations discovered while learning the current UpgradePilot implementation.

Use it for:

```text
learning mechanisms worth preserving
open design questions
possible limitations
possible defects that still need evidence
formal-audit candidates not yet mature
questions to revisit
```

Do not use it as:

```text
MEMORY.md
implementation plan
architecture authority
formal audit
proof that an observation is a defect
mastery tracker
```

Lifecycle:

```text
source learning / design debate
→ capture material observation here
→ inspect source/tests/consumers/consequence
→ later:
   ├── mature concern → audits/
   ├── durable understanding → dated learning note
   ├── misunderstanding → resolve
   └── low-value item → retire
```

---

# Current learning position

The active source-learning path is inside the bounded workflow-command reader:

```text
src/upgradepilot/workflow_commands.py
```

Exact continuation:

```python
_command_invokes_package(...)
```

Already covered immediately before this point:

```text
tuple(generator) materialization
next(..., None) existential witness selection
aggregate proven/no-success/unresolved hierarchy
per-workflow execution/definition/revision/path gates
workflow-command reader entry
exactly-one-job restriction
install + execution witness searches
_command_installs_source_file(...)
_shell_segments(...) introduction
_normalize_command_path(...)
```

The branch is synchronized with current `main`. The latest main delta closes Step 5, validates Step 6A, and activates Step 6B, but does not change the CI/workflow-reader source currently being learned.

Detailed progress/checkmarks now live in `LEARNING_SESSION_PLAN.md` rather than being duplicated here.

---

# Open review observations

## LR-001 — Aggregate CI detail names only the first proof witness

**Classification:** question / possible diagnostic-presentation limitation  
**Primary source:** `src/upgradepilot/ci_dependency_exercise.py`  
**Disposition:** preserve; not yet a formal audit finding

### Observed behavior

The outer evaluator materializes every per-workflow result, then selects:

```python
proven = next(
    (result for result in results if result.state == "proven"),
    None,
)
```

The aggregate human detail names `proven.workflow_name`, while `workflows=results` preserves all workflow results.

Example:

```text
A → unresolved
B → proven
C → proven

aggregate state = proven
selected detail witness = B
preserved evidence = A + B + C
```

### What is currently correct

The aggregate question is existential:

```text
Does at least one admitted workflow prove the narrow dependency-exercise proposition?
```

One witness is enough for state correctness.

### Review question

Decision and presentation have different information needs:

```text
state decision
→ one witness sufficient

human evidence summary
→ all proving witnesses may be relevant
```

Possible future alternatives, only after consumer/test inspection:

```text
A. explicitly say "at least one workflow"
B. summarize all proven workflows/count
C. keep concise aggregate detail and rely on workflows=results
```

### Evidence needed before promotion

Inspect:

- aggregate-detail contract;
- CLI/other consumers;
- tests protecting wording;
- whether first-witness ordering has product meaning;
- whether the current detail can materially mislead rather than merely omit useful diagnostics.

Current judgment:

```text
not an aggregation correctness defect
possible diagnostic/presentation limitation
```

---

## LR-002 — Exactly-one-job reader restriction is stricter than the same-job proof proposition

**Classification:** possible capability limitation / prototype boundary  
**Primary source:** `src/upgradepilot/workflow_commands.py`  
**Disposition:** preserve; not yet a formal defect

### Observed behavior

Current reader requires:

```python
len(jobs) == 1
```

otherwise it returns:

```text
unresolved / multiple_or_zero_workflow_jobs
```

Therefore:

```yaml
jobs:
  test:
    steps:
      - run: pip install -r requirements-dev.txt
      - run: pytest

  lint:
    steps:
      - run: ruff check .
```

is unresolved even though `test` independently contains both admitted evidence facts.

### Important distinction

This is not literal case-specific hardcoding such as:

```text
if package == pytest
if repo == glyphsLib
```

No such case constants were observed in the reader.

It is shape-specific/narrow grammar:

```text
exactly one workflow job
visible pip -r
visible direct package invocation
```

### Conservative alternative worth evaluating later

A broader rule could remain conservative:

```text
for each statically readable job independently:
    does this same job contain install + exercise?

if any one job does:
    one same-job witness exists
```

This would still reject unsafe cross-job composition:

```text
Job A installs
Job B exercises
→ not sufficient
```

### Why this matters

```text
conservative reasoning
≠
reject every richer input shape wholesale
```

A per-job existential rule may increase supported coverage without inferring shared environments/artifacts across jobs.

### Evidence needed before promotion

Inspect:

- current workflow-command tests;
- supported public workflow shapes;
- whether result contract needs a job witness/name;
- interaction with runtime job evidence;
- whether AUDIT-002 already owns any overlapping consequence;
- proof obligations for multi-job support.

Current judgment:

```text
intentional first-rule restriction
production-capability limitation worth reassessing
formal defect not yet established
```

---

# Learning points worth preserving

## LP-001 — `tuple(generator_expression)` materializes all per-workflow results

```text
generator is lazy by itself
tuple(...) immediately consumes it
→ all workflow evaluations complete before later witness search
```

## LP-002 — `next(..., None)` implements existence + witness

```text
any(...)
→ Boolean

next(generator, None)
→ first matching object or expected absence marker
```

In the aggregate evaluator this directly implements an existential proof rule while retaining one actual proof witness.

## LP-003 — `None` is an expected absence state here

No proven workflow is normal product evidence, not a Python iteration error. `next(..., None)` avoids escaping `StopIteration`.

## LP-004 — Witness-search short-circuit does not skip earlier workflow evaluation

`results` is already fully materialized. `next(...)` stops only its search through those completed results.

## LP-005 — Proof sufficiency and evidence preservation are separate

```text
one proven workflow
→ sufficient for existential aggregate state

workflows=results
→ preserves weaker/additional evidence
```

## LP-006 — Per-workflow and aggregate evaluators own different questions

```text
_evaluate_workflow_dependency_exercise(...)
→ interpret one workflow bundle

evaluate_dependency_ci_exercise(...)
→ aggregate classified workflow evidence
```

## LP-007 — `assert` represents an internal invariant

Expected incomplete evidence must become an explicit product state such as `unresolved`.

An impossible internal combination after those evidence gates is a programming-contract problem and may justify an assertion.

## LP-008 — `state`, `reason`, `detail`, and evidence payloads serve different roles

Do not treat a human-readable detail string as the complete evidence model.

## LP-009 — Conservative support can be existential at multiple levels

Current outer architecture already uses:

```text
∃ workflow that proves dependency exercise
```

A future multi-job reader could analogously use:

```text
∃ job within a workflow that independently proves install + exercise
```

without permitting cross-job evidence composition.

## LP-010 — Dependency identity evidence and CI installation evidence are different facts

```text
changed dependency found in uv.lock / constraints / requirements
≠
CI proved installation of that source
```

The explicit `direct_requirements_install_path` gate preserves this distinction.

## LP-011 — Exact revision alignment is an evidence-integrity property

```text
workflow definition revision
=
workflow run head SHA
```

must hold before visible YAML commands are admitted as evidence about that run.

## LP-012 — Path normalization is intentionally superficial

The install matcher normalizes extracted path identity:

```text
./requirements-dev.txt
→ requirements-dev.txt
```

but does not infer:

```text
..
variables
symlinks
working-directory state
```

because those facts are not established by the narrow reader.

---

# Promoted / already formalized review findings

## PR-001 — CI dependency-exercise proof boundary

**Formal record:** `audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`

Already-formalized concerns include:

```text
failure masking (`|| true`)
continue-on-error
conditional/skipped execution
install-before-exercise ordering
matched-command runtime-step success
exact proposed-version runtime observation
interpreter/environment continuity
```

Do not duplicate them here.

Learning connection:

```text
static command recognition
≠
per-command runtime proof
≠
exact-version observation
≠
exercised-version proof
```

---

# Questions to revisit

## Q-001 — Should aggregate state selection and human presentation use the same witness shape?

Revisit with CLI/result consumers.

## Q-002 — Is first-proven-workflow ordering intentionally meaningful?

If result order is only acquisition order, naming the first witness may accidentally imply importance.

## Q-003 — Which Unit 4 concerns are new versus already owned by AUDIT-002?

Understand mechanics first, then avoid duplicate audit findings.

## Q-004 — Can multiple workflow jobs be supported conservatively by evaluating each job independently?

Revisit after tests and result-contract inspection.

## Q-005 — If a per-job witness is added later, what runtime evidence must bind static YAML job identity to the successful Actions job record?

This question may connect LR-002 to AUDIT-002 but must not be answered by assumption.

---

# Promotion checklist

Before a new formal audit:

```text
[ ] exact current behavior confirmed from source
[ ] relevant tests/consumers inspected
[ ] consequence exceeds stylistic preference
[ ] owning product claim identified
[ ] defect/risk/limitation/simplification classification is precise
[ ] plausible alternatives/tradeoffs understood
[ ] existing audit/ADR does not already own the concern
[ ] future proof requirement can be stated
```

Before a learning point becomes a durable session conclusion:

```text
[ ] mental model can be explained without copying source prose
[ ] relevant terms are understood
[ ] product meaning separated from syntax
[ ] changed-case prediction attempted when useful
[ ] nonclaims preserved
```

---

# Session-use reminder

Use this file selectively:

```text
learn
→ challenge
→ capture material insight
→ continue
→ periodically distill
```

Do not turn each code line into documentation work.

The durable checkpoint for the current conversation is:

```text
2026-08-03-Session1-continuation-2.md
```

and the exact next learning mechanism is:

```python
_command_invokes_package(...)
```