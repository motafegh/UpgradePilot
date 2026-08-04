# Live Learning and Review Notes

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Branch:** `agent/learning-current-implementation`  
**Status:** live learning/review capture; non-controlling  
**Current synchronized main baseline:** `523360e85fd7541bbf91fd013e9f48f2c68703c8`  
**Major architecture sync:** PR #20, merge commit `b0451f3cf797aa50d907f9b335f0c8fc31c6658a`  
**Latest documentation follow-up sync:** PR #21, merge commit `87067ccd912087f8d04b6f06f30ea7d9ad5e1127`

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

The active source-learning path remains the bounded workflow-command reader, now under its accepted responsibility owner:

```text
src/upgradepilot/ci/workflow_commands.py
```

Exact continuation:

```text
_extract_job_definitions(...)
→ continue after locating plain jobs: and recording jobs_index/jobs_indent
→ direct child-job discovery
→ sibling job-body slicing
→ _extract_run_commands(...)
```

Already covered before this point:

```text
tuple(generator) materialization
next(..., None) existential witness selection
aggregate proven/no-success/unresolved hierarchy
per-workflow execution/definition/revision/path gates
workflow-command reader entry
exactly-one-job restriction
install + execution witness searches
_command_installs_source_file(...)
_shell_segments(...)
_normalize_command_path(...)
_command_invokes_package(...)
package/normalized-package candidate set
supported invocation wrappers
leading environment-variable assignment stripping
segment-start and command-token boundary matching
current install/execution ordering is not enforced
first-stage _extract_job_definitions jobs: discovery
```

The 2026-08-04 main delta is architecture-changing globally but does not materially change the CI decision algorithm already learned. The active files moved from the old flat package to `upgradepilot.ci` and their imports now point to responsibility owners.

Detailed progress/checkmarks live in `LEARNING_SESSION_PLAN.md`.

---

# Architecture reconciliation intake

## AR-001 — Responsibility-based subpackages

**Classification:** durable architecture learning point; introduced depth  
**Reference:** `docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`

Current architectural reading:

```text
GitHub     → provider-specific acquisition and exact GitHub identity
PyPI       → provider-specific release/index/provenance acquisition
Dependency → dependency-change contracts/extraction/coordination/version ordering
CI         → workflow-command reading and dependency-exercise interpretation
Upstream   → repository identity, interval authority, evidence composition, claim grounding
Target     → target Python declaration, specifier semantics, relevance
Application→ PR investigation orchestration
Interface  → CLI arguments/rendering/exit policy
```

Learning principle:

```text
module location should communicate responsibility
```

The project deliberately avoids generic architecture buckets without demonstrated ownership.

## AR-002 — Precise imports preserve ownership

`upgradepilot.__init__` is intentionally minimal and does not re-export the internal object graph.

Learning principle:

```text
convenient package-root façade
can hide ownership
and accidentally imply a public API
```

Internal code now imports precise owners.

## AR-003 — Architecture can have executable tests

`tests/test_source_topology.py` protects:

```text
new owner imports work
+
package root remains minimal
+
obsolete flat module paths remain absent
```

Learning principle:

```text
architecture invariants can be executable contracts
```

not merely diagrams or documentation.

## AR-004 — Shared dependency does not imply shared responsibility

The old `packaging_method.py` was split into:

```text
dependency/versioning.py
target/python_specifier.py
```

Both use `packaging`, but they answer different product questions.

Learning principle:

```text
same library
≠
same domain responsibility
```

## AR-005 — Application orchestration versus interface

The current application flow is:

```text
CLI input
→ investigate_public_pull_request(...)
→ typed PublicPullRequestInvestigation
→ CLI rendering / exit policy
```

Learning principle:

```text
orchestration responsibility
≠
presentation/interface responsibility
```

This will materially affect the later request-to-output learning unit.

## AR-006 — Product runtime, experiments, and tools are different executable boundaries

The accepted repository boundary is:

```text
src/upgradepilot/
→ installable product runtime only

tests/
→ active deterministic product regression

experiments/
→ non-product research/evaluation/calibration

experiments/tests/
→ regression for experiment machinery, not product-runtime coverage

tools/
→ developer-operated diagnostics/live proofs/maintenance utilities
```

Normal dependency direction points **toward** the product source; `src/upgradepilot/` must not depend on experiments, tests, or tools.

Learning principle:

```text
executable Python
≠
automatically product runtime architecture
```

A successful experiment or developer proof must still be deliberately adopted into a product responsibility and product tests before it becomes normal runtime behavior.

---

# Open review observations

## LR-001 — Aggregate CI detail names only the first proof witness

**Classification:** question / possible diagnostic-presentation limitation  
**Current source:** `src/upgradepilot/ci/dependency_exercise.py`  
**Disposition:** preserve; not yet a formal audit finding

### Observed behavior

The outer evaluator materializes every per-workflow result, then selects one first proven witness:

```python
proven = next(
    (result for result in results if result.state == "proven"),
    None,
)
```

The aggregate human detail names that witness while `workflows=results` preserves all workflow results.

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
- investigation/CLI consumers;
- tests protecting wording;
- whether first-witness ordering has product meaning;
- whether current detail can materially mislead rather than merely omit diagnostics.

Current judgment:

```text
not an aggregation correctness defect
possible diagnostic/presentation limitation
```

---

## LR-002 — Exactly-one-job reader restriction is stricter than the same-job proof proposition

**Classification:** possible capability limitation / prototype boundary  
**Current source:** `src/upgradepilot/ci/workflow_commands.py`  
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

Therefore a workflow containing one self-contained test job plus an unrelated lint job remains unresolved even when the test job independently contains both admitted evidence facts.

### Important distinction

This is not literal package/repository case hardcoding.

It is shape-specific narrow grammar:

```text
exactly one workflow job
visible pip -r
visible direct package invocation
```

### Conservative alternative worth evaluating later

```text
for each statically readable job independently:
    does this same job contain install + exercise?

if any one job does:
    one same-job witness exists
```

This still rejects unsafe cross-job composition:

```text
Job A installs
Job B exercises
→ not sufficient
```

### Evidence needed before promotion

Inspect:

- current workflow-command tests;
- supported public workflow shapes;
- whether result contract needs a job witness/name;
- binding between static YAML job identity and runtime successful job evidence;
- overlap with AUDIT-002;
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

## LP-003 — `None` is an expected absence state here

No proven workflow is normal product evidence, not a Python iteration error.

## LP-004 — Witness-search short-circuit does not skip earlier workflow evaluation

`results` is already fully materialized. `next(...)` stops only its search through completed results.

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

Expected incomplete evidence becomes an explicit product state. Impossible internal combinations may indicate programming-contract defects.

## LP-008 — `state`, `reason`, `detail`, and evidence payloads serve different roles

Do not treat human-readable detail as the complete evidence model.

## LP-009 — Conservative support can be existential at multiple levels

```text
current outer rule:
∃ workflow that proves dependency exercise

possible future job rule:
∃ job within workflow that independently proves install + exercise
```

without permitting cross-job evidence composition.

## LP-010 — Dependency identity evidence and CI installation evidence are different facts

```text
changed dependency identified
≠
CI proved installation of that source
```

## LP-011 — Exact revision alignment is an evidence-integrity property

```text
workflow definition revision
=
workflow run head SHA
```

must hold before visible YAML is admitted as evidence about that run.

## LP-012 — Path normalization is intentionally superficial

The install matcher tolerates superficial spelling differences but does not infer `..`, variables, symlinks, or working-directory state.

## LP-013 — Direct invocation matching is allowlisted, not word-search based

The current reader recognizes explicit invocation shapes such as:

```text
pytest
python -m pytest
uv run pytest
poetry run pytest
pipenv run pytest
coverage run -m pytest
```

and requires the invocation at shell-segment start with a whitespace/end token boundary.

## LP-014 — Leading shell environment assignments are not the invoked command

```text
PYTHONWARNINGS=error python -m pytest
```

is reduced for matching purposes to the visible invocation:

```text
python -m pytest
```

without attempting general shell evaluation.

## LP-015 — Install/exercise existence does not establish chronology

Current command searches are independent:

```text
∃ install witness
AND
∃ execution witness
```

They do not establish:

```text
install occurs before execution
```

This ordering limitation is already owned by AUDIT-002.

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

---

# Questions to revisit

## Q-001 — Should aggregate state selection and human presentation use the same witness shape?

Revisit with investigation/CLI/result consumers.

## Q-002 — Is first-proven-workflow ordering intentionally meaningful?

If result order is only acquisition order, naming the first witness may accidentally imply importance.

## Q-003 — Which Unit 4 concerns are new versus already owned by AUDIT-002?

Understand mechanics first, then avoid duplicate audit findings.

## Q-004 — Can multiple workflow jobs be supported conservatively by evaluating each job independently?

Revisit after tests and result-contract inspection.

## Q-005 — If a per-job witness is added later, what runtime evidence must bind static YAML job identity to the successful Actions job record?

This may connect LR-002 to AUDIT-002 but must not be answered by assumption.

## Q-006 — Which architectural boundaries from ADR-0007 become independently explainable only after we visit their code owners?

Do not convert the 2026-08-04 architecture orientation into a mastery claim merely because the map is understandable.

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

Current durable intake/checkpoint chain:

```text
2026-08-03-Session1-continuation-2.md
→ detailed pre-reconciliation CI mechanics

2026-08-04-main-architecture-reconciliation-intake.md
→ current owner map + architecture-changing delta
```

Exact next learning mechanism:

```text
src/upgradepilot/ci/workflow_commands.py
→ _extract_job_definitions(...)
→ direct child-job discovery after the already-covered jobs: lookup stage
```
