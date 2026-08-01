# UpgradePilot B2 Evidence-Pipeline Mastery — Session 1 Continuation

**Date:** 2026-08-02  
**Learning branch:** `agent/learning-current-implementation`  
**Package:** `learning/2026-07-31-b2-evidence-pipeline-mastery/`  
**Purpose:** Preserve the learning completed after the first Session 1 note and before the next synchronization with `main`.

## Snapshot boundary

This note is a learning snapshot, not live project authority.

At the moment immediately before this note was written, the learning branch was still based on main revision:

```text
52d56773342f5dfe31c41fb0e39e58cc745ef5bf
```

and current `main` had advanced beyond it. The newer implementation is intentionally analyzed only after this learning checkpoint is preserved.

Implementation truth remains source, tests, commands, outputs, and environment. Live project position remains owned by root `MEMORY.md` on the actively developed main branch.

---

# 1. Learning focus of this continuation

The continuation stayed on the Step 7 CI dependency-exercise contract rather than jumping ahead to newer implementation.

The learning target was:

```text
successful CI execution
vs
proof that the changed dependency was actually consumed and exercised
```

and then:

```text
per-workflow decision precedence
+
overall existential aggregation
+
important Python function-signature contracts
```

The source under study was:

```text
src/upgradepilot/ci_dependency_exercise.py
```

with controlled behavior protected by:

```text
tests/test_ci_dependency_exercise.py
```

---

# 2. State distinction demonstrated by Ali

The three Step 7 states remain:

```text
proven
no_successful_ci
unresolved
```

Their meanings are intentionally narrow.

## `proven`

At least one successful exact-head CI path satisfies the currently admitted rule for:

```text
explicit requirements installation
+
direct changed-package invocation
```

This does not establish compatibility, complete coverage, safety, or a merge recommendation.

## `no_successful_ci`

No completed successful exact-head job is available.

This is an execution-evidence state.

## `unresolved`

Successful exact-head CI exists, but the currently admitted evidence cannot prove dependency consumption plus package exercise.

This is a proof/interpretation insufficiency state.

---

# 3. Prediction 1 — successful CI but installation not proved

Scenario:

```text
exact-head CI exists
workflow is successful
changed package is invoked
but installation of the explicit requirements path is not proved
```

Ali predicted:

```text
unresolved
```

Reason given in substance:

> We have a successful CI workflow, but no installation evidence. We cannot label it `proven` because there is no evidence showing the requirements file was installed.

This prediction was correct.

The central distinction established was:

```text
successful CI execution
!=
proven dependency consumption
```

A green workflow alone does not prove the narrower product claim.

Important semantic refinement:

```text
unresolved
!=
proved that installation did not happen
```

Instead:

```text
unresolved
=
UpgradePilot cannot establish the required fact under its admitted evidence rule
```

This is an example of a broader evidence principle that appears repeatedly in UpgradePilot:

```text
not proved
!=
proved false
```

---

# 4. Prediction 2 — CI exists but no successful job exists

Scenario:

```text
exact-head workflow exists
workflow jobs exist
all relevant jobs failed or were cancelled
no completed successful job exists
```

Ali predicted:

```text
no_successful_ci
```

Reason given in substance:

> We have evidence that CI exists, but it was not successful, so it should be `no_successful_ci`.

This prediction was correct, with one precision refinement:

The exact current contract asks whether there is a job satisfying both:

```python
job.status == "completed"
and
job.conclusion == "success"
```

So the precise fact is:

```text
no completed successful exact-head job exists
```

not merely the broader phrase "CI was unsuccessful."

---

# 5. Execution availability versus proof sufficiency

The two predictions establish the conceptual center of Step 7:

```text
successful execution absent
→ no_successful_ci

successful execution present
+ proof blocked or insufficient
→ unresolved
```

This is not a simple three-value good/bad/unknown state machine.

It separates two different questions:

```text
1. Is successful execution evidence available?
2. If yes, can the admitted evidence prove dependency exercise?
```

That separation determines the source-code decision order.

---

# 6. Per-workflow decision order

The current per-workflow evaluator follows this conceptual funnel:

```text
Do we have a completed successful job?
        |
        +-- no  → no_successful_ci
        |
        +-- yes
             |
             v
Is the workflow run completed-successful?
        |
        +-- no  → unresolved
        |
        +-- yes
             |
             v
Is the exact workflow definition available?
        |
        +-- no  → unresolved
        |
        +-- yes
             |
             v
Does definition revision match run head SHA?
        |
        +-- no  → unresolved
        |
        +-- yes
             |
             v
Is an independently established direct-requirements path available?
        |
        +-- no  → unresolved
        |
        +-- yes
             |
             v
Do admitted visible commands prove install + direct invocation?
        |
        +-- no  → unresolved
        |
        +-- yes → proven
```

This order is part of the product semantics, not merely coding style.

---

# 7. Decision precedence

A new term introduced in this continuation was **precedence**.

Practical meaning here:

> If several weaknesses or problems exist at the same time, which condition determines the classification first?

Example:

```text
job conclusion = failure
+
workflow definition unavailable
```

There are two observable problems:

```text
1. no successful job
2. definition unavailable
```

Ali predicted that the evaluator should stop at the earlier condition:

```text
state  = no_successful_ci
reason = no_successful_jobs
```

Reason given in substance:

> One of the first conditions is already not met (`conclusion = failure`), so we do not enter the later checks; at the beginning we classify it as no successful job.

This prediction was correct.

Why this precedence is semantically appropriate:

```text
Before interpreting what a successful execution means,
we first need successful execution evidence to exist.
```

If no successful job exists, an unavailable workflow definition cannot change that fundamental fact.

Therefore:

```text
no successful job
precedes
workflow-definition availability
```

The controlled test protects this explicitly with a case equivalent to:

```text
no successful job + unavailable definition
→ no_successful_ci / no_successful_jobs
```

---

# 8. Workflow job versus workflow run

A workflow run and its jobs are separate evidence objects.

Conceptually:

```text
WorkflowRun
└── WorkflowJob(s)
```

A specific job may complete successfully while the overall workflow run is not successful, for example because another job failed.

Therefore:

```text
successful job
!=
successful workflow run
```

The evaluator first requires at least one completed successful job and then checks the workflow run itself.

Current behavior:

```text
successful job exists
+
workflow run not completed-successful
→ unresolved
  reason = workflow_not_successful
```

This is another example of preserving evidence distinctions rather than collapsing related facts into one boolean.

---

# 9. Execution evidence versus interpretation/authority evidence

A useful layered mental model established in this session is:

```text
EXECUTION EVIDENCE
------------------
successful job
successful workflow run

        ↓

INTERPRETATION / AUTHORITY EVIDENCE
-----------------------------------
workflow definition available
workflow definition revision matches run head SHA
explicit requirements path has appropriate authority
commands are statically interpretable under the admitted rule

        ↓

NARROW PROOF
------------
dependency exercise proven
```

This means a workflow YAML file alone does not prove successful execution.

Likewise, a successful execution record alone does not prove the dependency-consumption path.

Different evidence objects establish different facts.

---

# 10. Overall aggregation and the existential rule

After every workflow is evaluated separately, the outer evaluator asks whether **any** workflow has:

```text
state == proven
```

Conceptually:

```text
Does there exist at least one workflow that proves the Step 7 claim?
```

The term introduced was **existential**.

Symbolically:

```text
∃ workflow such that workflow.state == proven
```

`∃` means "there exists."

For the current Step 7 contract:

```text
Workflow A → proven
Workflow B → unresolved
Workflow C → no_successful_ci

Overall → proven
```

The individual weaker results are preserved; they are not erased.

---

# 11. Ali challenged the existential rule

Ali asked whether:

```text
one proven workflow
→ overall proven
```

might be too simplified.

This was an important architectural challenge.

The answer depends on the exact product claim.

If `proven` meant:

```text
all CI is healthy
all relevant workflows exercised the dependency
complete compatibility is established
PR is safe
PR should be merged
```

then one successful workflow would be far too weak.

But Step 7 owns the narrower question:

```text
Does at least one successful exact-head CI path prove
that the changed dependency was consumed and exercised
under the admitted deterministic rule?
```

Because the claim itself is existential, one valid witness is logically sufficient.

This is different from a **universal** claim:

```text
∀ relevant workflows satisfy the condition
```

`∀` means "for all."

If the product question were universal, one proven workflow would not be enough.

---

# 12. Why the existential result is not lossy

Suppose:

```text
Regression Tests
→ proven dependency exercise

Tox Tests
→ unresolved because current command reader cannot trace tox configuration

Lint
→ failed
```

The overall Step 7 claim is still:

```text
proven
```

because one admitted successful CI path establishes the narrow existence claim.

However, the aggregate result preserves every `WorkflowDependencyExerciseResult`.

Therefore the system may simultaneously retain:

```text
overall dependency exercise = proven

AND

one workflow unresolved
one workflow without successful CI
```

The overall state does not rewrite history or claim that every workflow was successful.

---

# 13. Claim-boundary ownership demonstrated by Ali

A mixed-workflow prediction was presented:

```text
Workflow A:
  successful
  requirements-dev.txt installed
  pytest directly invoked
  → proven

Workflow B:
  successful
  uses tox in an unsupported/untraced way
  → unresolved

Workflow C:
  failed
  → no_successful_ci
```

Ali correctly predicted:

```text
overall = proven
```

because of the current "at least one" rule.

Ali also correctly stated that the result supports a claim about the changed dependency being installed/exercised, but does not establish source-code compatibility.

The precise allowed claim is:

```text
At least one successful exact-head CI path
provably installed the explicitly established requirements source
and directly exercised the changed package.
```

Not established by Step 7:

```text
all workflows succeeded
all platforms/configurations were covered
complete source-code compatibility
safety
absence of regressions everywhere
merge readiness
maintainer recommendation
```

This reinforces a central UpgradePilot architecture principle:

```text
establish evidence
→ make exactly the claim that evidence supports
→ do not silently promote it into a stronger claim
```

---

# 14. Unit 2 entry — the public evaluator signature

The next learning layer began from:

```python
def evaluate_dependency_ci_exercise(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyExerciseInput],
    *,
    direct_requirements_install_path: str | None,
) -> DependencyCIExerciseResult:
```

Conceptually:

```text
DependencyVersionChange
+
workflow evidence bundles
+
explicit direct-requirements operational path (or expected absence)

        ↓

evaluate_dependency_ci_exercise(...)

        ↓

DependencyCIExerciseResult
```

---

# 15. Input responsibility — `DependencyVersionChange`

```python
dependency: DependencyVersionChange
```

This tells Step 7 which canonical dependency transition is being evaluated.

Controlled example:

```text
package = pytest
normalized package = pytest
old version = 9.0.2
proposed version = 9.0.3
```

Step 7 does not rediscover the dependency change.

Its boundary is approximately:

```text
Upstream responsibility:
"Establish exactly what dependency changed."

Step 7 responsibility:
"Determine what exact-head CI proves about exercising that established change."
```

---

# 16. Input responsibility — workflow evidence bundle

Each sequence element is:

```python
@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseInput:
    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence
```

Conceptually:

```text
WorkflowDependencyExerciseInput
├── run
│   └── workflow execution-level evidence
├── jobs
│   └── individual job execution records
└── definition
    └── exact workflow-file evidence used for interpretation
```

These pieces must be interpreted together.

---

# 17. Input responsibility — `str | None`

The parameter is:

```python
direct_requirements_install_path: str | None
```

Ali predicted that `None` is intentional because the system expects absence and later reports that condition as unresolved.

This was correct.

Practical meaning:

```text
str
→ an explicit qualifying path was independently established
  e.g. "requirements-dev.txt"

None
→ no qualifying direct-requirements operational path was established
```

Important API-design point:

```text
None does not necessarily mean
"the programmer forgot an argument."
```

Here it can represent a valid product/evidence state:

```text
upstream evidence legitimately cannot establish this fact
```

The evaluator handles it explicitly as:

```text
unresolved
reason = direct_requirements_install_path_unavailable
```

If the annotation were only:

```python
direct_requirements_install_path: str
```

then the function contract would incorrectly imply that every valid caller must possess such a path.

---

# 18. Keyword-only `*`

The standalone `*` in:

```python
def evaluate_dependency_ci_exercise(
    dependency,
    workflow_inputs,
    *,
    direct_requirements_install_path,
):
```

makes arguments after `*` keyword-only.

Valid:

```python
evaluate_dependency_ci_exercise(
    dependency,
    workflows,
    direct_requirements_install_path="requirements-dev.txt",
)
```

Invalid positional form:

```python
evaluate_dependency_ci_exercise(
    dependency,
    workflows,
    "requirements-dev.txt",
)
```

Why this is useful here:

```text
"requirements-dev.txt"
```

is not just an arbitrary string. It carries a specific evidence responsibility.

The keyword exposes that semantic role at the call site:

```text
direct_requirements_install_path="requirements-dev.txt"
```

This makes the API harder to misuse or misread.

Current depth: introduced with implementation-adjacent meaning. Deep Python call-signature mechanics are not required yet.

---

# 19. `Sequence[WorkflowDependencyExerciseInput]`

A prediction was asked about why the evaluator uses:

```python
Sequence[WorkflowDependencyExerciseInput]
```

rather than:

```python
list[WorkflowDependencyExerciseInput]
```

Ali initially connected `Sequence` with ordering and the exact sequence exercised.

The useful part of that intuition was ordering, but the semantic correction is:

```text
Sequence does not mean CI execution chronology.
```

It is a Python collection contract.

Practical meaning:

> The evaluator needs an ordered readable collection of `WorkflowDependencyExerciseInput` objects, not specifically a mutable list.

Examples of common compatible sequence shapes:

```python
[workflow_a, workflow_b]

(workflow_a, workflow_b)
```

The evaluator needs operations conceptually like:

```text
check whether empty
iterate through items
preserve item order when constructing per-workflow results
```

It does not require list-specific mutation such as:

```text
append
remove
sort in place
```

So `Sequence[...]` expresses the narrower actual need more accurately than `list[...]`.

Important precision:

```text
input order is preserved in per-workflow results
```

but that order does not itself prove workflow execution chronology or determine product precedence.

Current depth: introduced and corrected; not yet independently demonstrated.

---

# 20. Output responsibility

The public return type is:

```python
DependencyCIExerciseResult
```

with conceptually:

```text
state
reason
detail
workflows[]
```

This preserves:

```text
overall product conclusion
+
machine-readable reason
+
human-readable explanation
+
all per-workflow evidence interpretations
```

That retained per-workflow structure is what lets the overall existential result remain transparent rather than hiding unresolved or failed workflows.

---

# 21. Current demonstrated learning depth

The following labels intentionally avoid claiming mastery beyond evidence.

## Step 7 product question

**Depth:** operationally understood.

Evidence:

- correctly distinguished green CI from dependency-exercise proof;
- correctly stated that missing installation evidence prevents `proven`;
- correctly avoided compatibility overclaim.

## `unresolved` versus `no_successful_ci`

**Depth:** operationally understood.

Evidence:

- correctly classified successful CI with missing install proof as `unresolved`;
- correctly classified absence of completed successful jobs as `no_successful_ci`.

## Per-workflow decision precedence

**Depth:** operationally understood at the current branch set.

Evidence:

- correctly predicted that no successful job takes precedence over unavailable workflow definition;
- correctly explained that later checks are not entered once the earlier execution condition determines the state.

## Existential aggregation

**Depth:** operationally understood with healthy design challenge.

Evidence:

- correctly predicted overall `proven` from one proving workflow among weaker workflow results;
- questioned whether the rule was overly simplified;
- understood that its correctness depends on the exact narrow "at least one" product claim;
- correctly separated dependency-exercise proof from compatibility conclusions.

## Claim-boundary discipline

**Depth:** operationally understood for the current example.

Evidence:

- correctly limited the conclusion to dependency installation/exercise evidence;
- explicitly withheld source-code compatibility conclusion.

## `str | None`

**Depth:** implementation-adjacent introduction with correct prediction.

Evidence:

- correctly identified `None` as an expected evidence state leading to explicit unresolved handling.

## Keyword-only `*`

**Depth:** introduced.

No independent prediction or implementation use has yet been demonstrated.

## `Sequence[...]`

**Depth:** introduced / partially understood.

Evidence:

- recognized ordering relevance;
- required correction that it is a collection-interface contract, not CI execution chronology.

No independent use has yet been demonstrated.

---

# 22. Not yet learned or demonstrated

Do not infer mastery of the following from this session:

```text
tuple(...) materialization
generator expressions
next(..., None)
why frozen dataclasses are selected here
why slots are selected here
full WorkflowRun / WorkflowJob acquisition path
full exact-head acquisition and alignment path
workflow_commands.py parsing mechanics
multi-job command-reader abstention details
shell segmentation behavior
package invocation normalization
full test-suite ownership
Ali-authored source/test modification
```

These remain future learning work.

---

# 23. Important design question preserved for later

Ali raised a legitimate higher-level product question:

> Is "one proven workflow means overall dependency exercise is proven" too narrow or simplified for the eventual product?

Current answer:

```text
For the existing Step 7 contract: no.
The implementation correctly matches its existential claim.
```

But a later product layer may separately need information about:

```text
overall CI health
important failing workflows
platform/configuration breadth
coverage breadth
compatibility evidence
safety/recommendation
```

Those should not be silently folded into Step 7's `proven` state. If needed, they belong to explicit later responsibilities or separate aggregate dimensions.

This question should be revisited only when the controlling product plan reaches those responsibilities.

---

# 24. Exact continuation point

The next planned teaching point before newer implementation intake interrupted the session was:

```text
tuple(...) construction around the per-workflow generator
```

Then:

```text
generator expression
→ immutable tuple of per-workflow results
→ next(..., None) existential witness selection
→ complete one-path proven trace
```

After synchronizing with current `main`, first classify the implementation delta as:

```text
unrelated
locally relevant
architecture-changing
```

Then update the learning plan only if the new implementation materially changes the required learning sequence, ownership proof, or prerequisite chain.

Do not restart already demonstrated Step 7 concepts merely because main advanced.
