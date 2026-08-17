The best way to master what we built today is **not** to memorize Cluster 1, 2, 3, 4, 5 separately. We should reconstruct one real dependency update as if we were UpgradePilot and watch the evidence become stronger one proposition at a time.

One important boundary first: **Clusters 0–4 are validated green. Cluster 5 is implemented but still awaiting your validation.** Also, the new Cluster-5 path is not yet wired into the ordinary `investigate_public_pull_request()` application path; that migration belongs to Cluster 6. So what we review below is the real implemented domain/CI machinery, not yet the final ordinary CLI flow.

# 1. The whole thing we built today, in one picture

Forget individual files for a moment.

Our system now tries to answer this chain:

```text
PUBLIC DEPENDENCY UPDATE
        │
        ▼
What dependency changed?
        │
        ▼
Where does that changed dependency belong?
        │
        ▼
What project environment does CI statically select?
        │
        ▼
Does that selected environment contain the changed dependency?
        │
        ▼
Does this static CI workflow therefore consume the changed dependency?
        │
        ├──────────────► Is changed package directly exercised?
        │
        ▼
Do we separately have successful exact-head CI?
        │
        ▼
What CI coverage claim is actually justified?
```

And the most important design principle is:

```text
each arrow
=
a new proposition that needs its own evidence
```

Not:

```text
we saw something related
→ assume everything downstream
```

This is the core skill I want you to retain from today's work.

---

# 2. Our strongest real teaching case: S001

Real case:

```text
Repository:
pydantic/pydantic

PR:
#13432

Dependency:
soupsieve

2.6
→
2.8.4

Changed source:
uv.lock
```

The original simulation established that this was a transitive documentation dependency and that exact-head documentation CI covered the relevant dependency path.

Now let's send that real case through **our current code**.

---

# 3. Stage A — "What changed?"

Before today's environment work can do anything, we need a canonical fact:

```python
DependencyVersionChange(
    package="soupsieve",
    normalized_package="soupsieve",
    old_version="2.6",
    proposed_version="2.8.4",
    ...
)
```

But today we learned that this alone is too weak.

Imagine we only know:

```text
soupsieve changed
```

We still don't know:

```text
why it exists
where it belongs
which CI environment contains it
whether CI installed it
whether it executed
```

That is why Cluster 1 introduced **source contexts**.

Conceptually:

```text
DependencyVersionChange
+
DependencySourceContext
```

For S001:

```text
Soup Sieve 2.6 → 2.8.4
+
UvLockDependencyContext
```

This means:

> The change was established from this exact uv-lock source context.

It does **not** mean Soup Sieve belongs to every environment represented by the universal lock.

That's the first important mental model.

---

# 4. Stage B — "Where does the dependency belong?"

S001 is actually the harder case because `uv.lock` is a **universal lock**.

Think of the lock as containing many possible package relationships:

```text
uv.lock
│
├── packages for one group
├── packages for another group
├── optional extras
├── platform branches
├── Python-version branches
└── transitive packages
```

Therefore:

```text
Soup Sieve appears in uv.lock
```

does **not** imply:

```text
Soup Sieve is installed by docs CI
```

That logical mistake is precisely what Cluster 4 prevents.

---

# 5. Stage C — first understand what the workflow selects

Before asking whether `docs` contains Soup Sieve, we need to establish that the workflow actually selects `docs`.

Suppose the real workflow contains:

```bash
uv sync --all-packages --group docs
```

The relevant function is:

```python
observe_project_environment_selection(...)
```

in:

```text
dependency/environment_selection.py
```

Its inputs are conceptually:

```text
RunStepDefinition
+
exact project_file_path
+
workflow/job working-directory defaults
```

and its output is:

```python
ProjectEnvironmentSelectionObservation
```

with a declaration such as:

```python
ProjectEnvironmentSelectionDeclaration(
    manager="uv",
    operation="sync",
    project_root=None,
    selectors=(
        DependencyGroupSelector("docs"),
    ),
)
```

The module deliberately says that visible selectors are only **static declaration evidence**. They don't prove execution, environment formation, membership, or exercise.

So at this point:

```text
FACT:

workflow statically selects docs
```

Nothing stronger.

---

# 6. Why `ProjectEnvironmentSelectionDeclaration` is useful

Notice we didn't return:

```python
"docs"
```

We returned a typed structure containing:

```text
manager
operation
project root
segment index
selectors
```

Why?

Because later this distinction matters:

```text
pip install -e ".[dev]"

vs

uv sync --group docs

vs

uv run --extra mlx ...
```

They're all "environment selections," but their semantics are not identical.

This is a general software-engineering principle:

> **Preserve semantic structure early instead of flattening everything into strings.**

Strings are convenient at first and expensive later.

---

# 7. Working-directory context is also evidence

Consider:

```yaml
defaults:
  run:
    working-directory: services/api
```

and:

```bash
pip install -e ".[dev]"
```

That does not necessarily refer to repository-root `pyproject.toml`.

Therefore Cluster 3 shares:

```text
dependency/workflow_context.py
```

to establish:

```text
step working-directory
>
job defaults.run
>
workflow defaults.run
>
repository root
```

That shared helper is used by both direct-requirements observation and project-environment observation.

The architectural lesson:

```text
working-directory resolution
```

is not really:

```text
pip semantics
```

or:

```text
uv semantics
```

It's shared workflow path context needed by both.

So we extracted the common responsibility rather than copy/pasting it.

---

# 8. Now comes the hard S001 question

We know:

```text
selected group = docs
```

Now:

> Does `docs` contain Soup Sieve?

This goes to:

```python
evaluate_uv_selected_environment_membership(...)
```

in:

```text
dependency/uv_membership.py
```

Its inputs are very important:

```text
UvLockDependencyContext
+
ProjectEnvironmentSelectionDeclaration
+
exact-head pyproject.toml
+
exact-head uv.lock
```

Notice that it needs **both** project metadata and lock metadata.

---

# 9. Why both `pyproject.toml` and `uv.lock`?

They answer different questions.

```text
pyproject.toml
```

answers:

> Does this selected environment identity actually exist in the exact project?

For example:

```toml
[dependency-groups]
docs = [...]
```

While:

```text
uv.lock
```

answers:

> What exact resolved package relationships correspond to it?

So:

```text
pyproject.toml
→ environment identity

uv.lock
→ resolved package graph
```

This is excellent evidence design.

We're not asking one file to prove something it doesn't own.

---

# 10. Exact source identity happens before semantic reasoning

Look at what `evaluate_uv_selected_environment_membership()` does first:

```python
source_problem = _validate_exact_source_identity(...)
```

Only after that succeeds does it parse the project and lock.

And `_validate_exact_source_identity()` checks things such as:

```text
same repository
same exact revision
correct pyproject path
correct uv.lock path
matching lock source evidence
matching blob SHA
matching byte count
matching project root
```

This is a major concept:

> **Provenance before interpretation.**

Bad:

```text
here is some uv.lock
let's reason about it
```

Good:

```text
prove this is THE uv.lock
for THIS repository
at THIS revision
that established THIS dependency change

then reason about it
```

That is evidence engineering rather than plain parsing.

---

# 11. Next we parse the project

The private function:

```python
_parse_project(...)
```

uses:

```python
tomllib.loads(...)
```

and only extracts what Cluster 4 needs:

```text
[project].name

[project.optional-dependencies]
    environment names

[dependency-groups]
    group names
```

Notice what it does **not** do:

```text
interpret the whole pyproject ecosystem
evaluate every PEP
execute configuration
become a generic packaging framework
```

This is another strong architecture lesson:

> Parse only enough structure to prove the proposition you own.

---

# 12. Then we parse `uv.lock`

`_parse_lock()` creates a bounded internal graph representation:

```python
_ParsedLock(
    packages=...,
    by_name=...
)
```

Each package becomes roughly:

```python
_LockPackage(
    package=...,
    normalized_package=...,
    version=...,
    source=...,
    resolution_markers=...,
    dependencies=...,
    optional_dependencies=...,
    dev_dependencies=...,
)
```

And each edge:

```python
_DependencyEdge(
    package=...,
    normalized_package=...,
    version=...,
    source=...,
    marker=...,
    extras=...,
)
```

This is where you should recognize a standard **graph model**.

A package is a **node**.

A dependency is an **edge**.

```text
A depends on B

A ───────► B
```

---

# 13. But this is not a generic graph library

Important distinction.

We did not create:

```text
upgradepilot.graph
```

with a giant abstract graph framework.

Why?

Because current evidence only requires bounded uv dependency reachability.

So the graph representation remains private:

```python
_LockPackage
_DependencyEdge
_TraversalState
```

The leading `_` matters conceptually:

> implementation detail, not a public product contract.

This keeps us from prematurely architecting an abstraction before another real use case earns it.

---

# 14. Bind the actual workspace project

Next:

```python
_bind_workspace_package(...)
```

does something subtle.

Suppose the lock contains many packages called `pydantic`, or there's a workspace.

We don't want:

```text
name matches
→ probably this project
```

Instead it combines:

```text
normalized project distribution name
+
editable/virtual source path
```

to identify exactly one workspace package record.

This is an example of **identity disambiguation**.

Again:

```text
similar name
!= same entity
```

---

# 15. Turn the selector into graph roots

Then:

```python
_selected_roots(...)
```

takes:

```text
DependencyGroupSelector("docs")
```

and finds:

```text
project confirms docs exists
+
workspace lock package provides docs roots
```

For real S001 one root is:

```text
mkdocs-llmstxt
```

So now our graph search starts here:

```text
docs
 │
 ▼
mkdocs-llmstxt
```

---

# 16. The actual S001 traversal

Now comes:

```python
_traverse_selected_roots(...)
```

This uses:

```python
queue: deque[_TraversalState] = deque()
```

This is a classic **Breadth-First Search (BFS)** style traversal.

Breadth-First Search means:

> Explore graph nodes outward from the starting roots, level by level.

For S001:

```text
LEVEL 0
mkdocs-llmstxt

LEVEL 1
beautifulsoup4

LEVEL 2
soupsieve
```

So the proof path becomes:

```text
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

and returns:

```python
state="member"
membership_kind="transitive"
witness_root="mkdocs-llmstxt"
witness_path=(
    "mkdocs-llmstxt",
    "beautifulsoup4",
    "soupsieve",
)
```

This is probably the most important piece of code from Cluster 4 to understand.

---

# 17. Why preserve `witness_path`?

We could simply return:

```python
True
```

But `True` tells us almost nothing.

Instead:

```text
member
+
transitive
+
exact witness path
```

lets the later product explain:

> Soup Sieve is covered because the selected `docs` group contains `mkdocs-llmstxt`, which depends on `beautifulsoup4`, which depends on `soupsieve`.

That's human-auditable evidence.

So another strong lesson:

```text
decision state
+
proof witness
```

is much stronger than:

```text
boolean
```

---

# 18. Why `deque`, `visited`, and limits?

Real dependency graphs can contain cycles:

```text
A → B → C → A
```

Without protection:

```text
A
B
C
A
B
C
...
```

forever.

So we keep:

```python
visited
```

and bounds:

```text
MAX_VISITED_STATES = 10,000
MAX_PATH_DEPTH = 100
```

If those bounds are crossed:

```text
unresolved
```

not:

```text
not a member
```

Why?

Because exceeding our analysis capability is:

```text
we don't know
```

not:

```text
false
```

This is a critical general reasoning principle.

---

# 19. The three-state model

Across today's implementation you see this pattern repeatedly:

```text
member / supported
not_established
unresolved
```

You need to become very comfortable with the difference.

### `member` / `supported`

We have sufficient positive evidence.

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Therefore:

```text
member
```

### `not_established`

We successfully analyzed the bounded evidence, but it didn't prove the proposition.

Example:

```text
affected extra = mlx
selected extra = dev
```

Nothing ambiguous.

It simply doesn't establish `mlx`.

### `unresolved`

Something prevents safe evaluation:

```text
dynamic expression
marker-dependent branch
ambiguous lock record
wrong revision
unknown project binding
malformed structure
```

These states must never collapse into:

```python
True / False
```

because:

```text
False
```

would erase the difference between:

```text
we checked and didn't establish it
```

and:

```text
we could not safely check
```

---

# 20. Why markers cause `unresolved`

Imagine:

```text
beautifulsoup4
→ soupsieve ; python_version >= "3.12"
```

Without knowing the actual target runtime context, can we say Soup Sieve is definitely active?

No.

So Cluster 4 does:

```python
if edge.marker is not None:
    ambiguous_branch_seen = True
    continue
```

Likewise package-level `resolution-markers` cause ambiguity.

At the end:

```text
no unconditional path found
+
ambiguous/conditional branch existed

→ unresolved
```

Not:

```text
not_established
```

That's conservative reasoning done correctly.

---

# 21. Now contrast S011

S011 is our best **negative** teaching case.

Real proposal:

```text
dragfly/dictare
PR #34

pyproject.toml

[project.optional-dependencies]
mlx = [
    ...
    "numpy==1.26.4"
]
```

becomes:

```text
numpy==2.4.6
```

The real repository instructs MLX users to install:

```bash
uv sync --python 3.11 --extra mlx
```

but both the ordinary Linux workflow and the macOS test workflow install:

```bash
pip install -e ".[dev]"
```

not `mlx`.

This is why S011 is perfect alongside S001:

```text
S001
positive membership/consumption

S011
visible environment mismatch/non-establishment
```

---

# 22. Cluster 2's S011 extraction

The source owner is:

```text
dependency/pyproject.py
```

Its job is deliberately narrow:

> Compare exact base/head `pyproject.toml` and establish at most one exact pin change inside one optional extra.

The key object is:

```python
_RequirementRecord(
    package,
    normalized_package,
    extras,
    specifier,
    marker,
    url,
)
```

Notice what we preserve:

```text
package identity
dependency extras
version specifier
marker
URL/direct reference
```

because if any of these other semantics change, we shouldn't pretend we saw a pure version transition.

---

# 23. Why use `packaging.Requirement`?

Example strings:

```text
numpy==2.4.6

soundfile>=0.12

mlx-metal==0.30.4; sys_platform == "darwin"
```

Parsing these ourselves with regex would be fragile.

So:

```python
Requirement(raw_requirement)
```

comes from Python's `packaging` library.

Mental model:

```text
tomllib
→ understands TOML syntax

packaging.Requirement
→ understands PEP 508 requirement syntax

UpgradePilot
→ understands our evidence policy
```

Different layers, different responsibilities.

---

# 24. How the S011 comparison works

The code compares base/head requirement collections.

It demands:

```text
exactly one removed record
+
exactly one added record
```

Then verifies:

```text
same extra
same normalized package
same dependency extras
same marker
same direct-reference identity
```

Only the exact version may change.

For S011:

```text
mlx:

numpy==1.26.4
→
numpy==2.4.6
```

passes.

Therefore we get conceptually:

```text
DependencyVersionChange(
    numpy,
    1.26.4,
    2.4.6
)

+

PyprojectOptionalExtraDependencyContext(
    extra="mlx"
)
```

Notice again:

```text
extra = mlx
```

came from **source evidence**.

Not from CI.

---

# 25. Why unrelated `pyproject.toml` changes are neutral

This was one of the useful implementation discoveries.

Suppose:

```toml
description = "new description"
```

changes but dependency lists don't.

We should not say:

```text
dependency analysis failed
```

because `pyproject.toml` is not exclusively a dependency file.

So we created:

```python
PyprojectOptionalExtraNoChange
```

This means:

> The optional dependency surface relevant to this rule did not change.

Not:

```text
the entire pyproject did not change
```

That's a good example of **precise result naming**.

---

# 26. Cluster 3 sees `.[dev]`

Now Dictare's workflow:

```bash
pip install -e ".[dev]"
```

is processed by:

```python
observe_project_environment_selection(...)
```

The parser recognizes `.[dev]` as a local project requirement and returns:

```python
OptionalExtraSelector("dev")
```

So now we have two independent facts:

```text
SOURCE FACT
affected extra = mlx

WORKFLOW FACT
selected extra = dev
```

The crucial thing is not to prematurely combine them inside the parser.

---

# 27. Cluster 5 added the tiny missing relation

The function:

```python
evaluate_project_source_environment_membership(...)
```

in:

```text
dependency/environment_membership.py
```

does exactly that comparison.

For an optional extra:

```python
affected = context.normalized_extra
```

then it checks selectors.

If:

```text
--all-extras
```

or:

```text
selected normalized extra == affected normalized extra
```

then:

```text
member
```

Otherwise:

```text
not_established
```

For S011:

```text
affected = mlx
selected = dev

→ not_established
```

Simple code.

Very important proposition.

---

# 28. Why normalization matters

Suppose source says:

```text
dev_test
```

but command says:

```text
dev-test
```

Python packaging name rules can treat variations such as `-`, `_`, `.` equivalently for comparison.

So our types preserve:

```text
original spelling
```

and expose:

```text
normalized_name
```

for comparison. `environment_selection.py` uses `canonicalize_name()` for extras/groups.

This is an important general idea:

```text
display identity
!= comparison identity
```

Preserve both when necessary.

---

# 29. Now Cluster 5: turn membership into CI consumption

This is today's newest conceptual jump.

We now know for S001:

```text
workflow selected docs
+
Soup Sieve is member of docs
```

But those are still dependency-domain facts.

CI owns the proposition:

> This static CI declaration consumes an environment containing the changed dependency.

So we introduced:

```text
ci/consumption.py
```

and:

```python
StaticDependencyConsumptionEvidence
```

---

# 30. Look at what that evidence preserves

It stores:

```python
state
mechanism
normalized_package

workflow_path
workflow_revision

job_key
step_source_index
segment_index
command

reason
detail

source_path
membership_kind
witness_path
```

This may look verbose, but every field answers an important question:

```text
WHAT?
which package?

WHERE?
which exact workflow?

WHEN/WHICH REVISION?
workflow_revision

WHICH JOB?
job_key

WHICH STEP?
step_source_index

WHICH COMMAND SEGMENT?
segment_index

WHY?
reason/detail

HOW IS IT A MEMBER?
direct/transitive + witness path
```

That is a **provenance-rich evidence object**.

---

# 31. `compose_project_environment_consumption()`

This function does not discover anything new about dependency semantics.

Instead it maps:

```text
selection observation
+
selection declaration
+
membership result
```

into:

```text
CI static consumption evidence
```

If membership says:

```text
member
```

CI gets:

```text
supported
```

If membership says:

```text
not_established
```

CI gets:

```text
not_established
```

If membership says:

```text
unresolved
```

CI keeps:

```text
unresolved
```

No evidence strength is upgraded.

---

# 32. Why the exact rebinding guard matters

This was one of today's best engineering discoveries.

Imagine we calculated valid evidence for:

```text
workflow A
job "docs"
Soup Sieve
```

and later another workflow also has:

```text
job "docs"
```

We cannot attach evidence merely because `"docs"` matches.

That would be evidence contamination.

So when the external consumption reaches:

```python
inspect_workflow_dependency_evidence(...)
```

we verify:

```text
same normalized package
same workflow path
same workflow revision
same job
same step source index
same command
valid segment index
```

This is called **rebinding** in our implementation discussion.

Meaning:

> Before consuming previously derived evidence, prove that it points back to the exact source object we're currently evaluating.

That's a very transferable engineering/evidence concept.

---

# 33. Cluster 5's new workflow inspector

The new function is:

```python
inspect_workflow_dependency_evidence(...)
```

It returns:

```python
WorkflowStaticDependencyEvidence(
    job_count,
    consumptions,
    invocations,
    problems,
)
```

Notice the architecture.

It does **not** return:

```text
pass / fail
```

It preserves the raw CI-level premises:

```text
consumptions
invocations
problems
```

Then a later function classifies them.

This is an important pattern:

```text
OBSERVE
then
EVALUATE
```

rather than:

```text
parse and make final conclusion simultaneously
```

---

# 34. Requirements files still work

Cluster 5 didn't discard our old requirements support.

If source context is:

```python
RequirementsFileDependencyContext(
    source_path="requirements-dev.txt",
    ...
)
```

then the inspector calls:

```python
observe_direct_installation_declaration(...)
```

and a command such as:

```bash
pip install -r requirements-dev.txt
```

becomes:

```python
StaticDependencyConsumptionEvidence(
    mechanism="direct_requirements",
    state="supported",
    ...
)
```

But importantly:

```text
ConstraintsFileDependencyContext
```

is not treated as:

```text
pip -r install source
```

merely because it has a path.

Typed contexts prevent this category error.

---

# 35. Then package invocation is collected separately

The workflow inspector also searches for direct package invocation:

```python
DirectPackageInvocationEvidence
```

Examples its bounded recognizer understands include prefixes such as:

```text
package
python -m package
python3 -m package
uv run package
coverage run -m package
...
```

But finding an invocation alone doesn't yet mean **exercise supported**.

Why?

Because ordering matters.

---

# 36. Static ordering is represented as coordinates

Every consumption and invocation has:

```text
(step_source_index, segment_index)
```

Example:

```yaml
- run: |
    pip install -r requirements-dev.txt
    pytest tests
```

might conceptually become:

```text
install:
(step=0, segment=0)

pytest:
(step=0, segment=1)
```

Or separate steps:

```text
install:
(step=0, segment=0)

invoke:
(step=1, segment=0)
```

Then comparison is normal tuple ordering:

```python
install_location < invocation_location
```

The code in `_classify_direct_exercise()` requires:

```text
same job
+
invocation after supported consumption
```

Simple representation, strong payoff.

---

# 37. Finally: `evaluate_dependency_ci_coverage()`

This is Cluster 5's main CI evaluator.

Inputs:

```python
dependency

workflow_inputs:
    WorkflowRun
    WorkflowJobs
    exact workflow definition
    optional external consumptions

source_contexts
```

Output:

```python
DependencyCICoverageResult
```

Its workflow-level result has **three different dimensions**:

```text
overall CI coverage state

static consumption state

static direct-exercise state
```

This is the major improvement over the old model.

---

# 38. Real S001 final result under Cluster 5

Let's run our mental machine.

Input evidence:

```text
Soup Sieve 2.6 → 2.8.4

workflow:
uv sync --group docs

selection:
docs

membership:
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve

runtime:
successful exact-head CI
```

Static consumption:

```text
SUPPORTED
```

Direct Soup Sieve invocation:

```text
not observed
```

Therefore:

```text
consumption_state = supported

direct_exercise_state = not_established

overall coverage =
supported_not_correlated
```

Why `not_correlated`?

Because we have:

```text
STATIC:
workflow definition declares consumption

RUNTIME:
workflow/run succeeded
```

but we haven't proven:

```text
THIS exact static docs step
↔
THIS exact successful runtime job/step
```

That static↔runtime join is Tranche 2.

---

# 39. Real S011 final result

Input:

```text
NumPy 1.26.4 → 2.4.6
affected extra = mlx

workflow:
pip install -e ".[dev]"

selected extra = dev
```

Dependency membership:

```text
not_established
```

Therefore static consumption:

```text
not_established
```

Even if runtime CI is green:

```text
successful exact-head CI
+
no supported mlx consumption

→ overall coverage unresolved/not established
```

This matches S011's real case conclusion: standard Ubuntu and macOS test workflows both install only `.[dev]`; neither establishes the MLX dependency environment.

This is why:

```text
green CI
!= affected dependency environment covered
```

---

# 40. One subtle Cluster-5 aggregation rule

`evaluate_dependency_ci_coverage()` first looks for any workflow result with:

```text
supported_not_correlated
```

If one exists, aggregate coverage can be supported while **all workflow results are still preserved**.

Example:

```text
Workflow A
consumption supported

Workflow B
unresolved

Workflow C
not established
```

Aggregate:

```text
supported_not_correlated
```

but results B and C do not disappear.

That's **heterogeneous evidence preservation**.

The strongest witness answers the positive proposition, while weaker evidence still remains visible.

---

# 41. Today's architecture in ownership terms

This is another thing you should be able to explain without looking at code:

```text
GitHub domain
    owns workflow structure

dependency domain
    owns:
        dependency source meaning
        extras/groups
        selection semantics
        lock membership

CI domain
    owns:
        does static CI consume changed dependency?
        is package directly invoked after consumption?
        combine static evidence with runtime CI authority

application
    owns sequencing
```

The modules now line up with that:

```text
dependency/
    pyproject.py
    environment.py
    environment_selection.py
    environment_membership.py
    uv_membership.py
    workflow_context.py
    direct_install.py

ci/
    consumption.py
    workflow_commands.py
    dependency_exercise.py
```

That separation is more important to master than remembering every helper function.

---

# 42. The migration pattern we used is also worth learning

We did **not** rip out the old CI API immediately.

Current `dependency_exercise.py` contains both:

```python
evaluate_dependency_ci_coverage(...)
```

and legacy:

```python
evaluate_dependency_ci_exercise(...)
```

Why?

Because `investigation.py` still uses the old:

```text
direct_requirements_install_path
→ evaluate_dependency_ci_exercise(...)
```

Cluster 6 will migrate that.

This is a recognized software migration strategy:

```text
introduce new path
→ validate it independently
→ preserve old caller compatibility
→ migrate callers
→ later remove legacy path
```

You can think of it as a **strangler-style incremental migration** at a small code scale.

Much safer than changing contract + callers + CLI + real cases simultaneously.

---

# 43. What you should actually master from today

If tomorrow you forgot every exact class name but retained these ideas, today's learning succeeded:

```text
1. Provenance before semantics.

2. One proposition per evidence boundary.

3. Selection != membership.

4. Membership != consumption.

5. Consumption != exercise.

6. Static declaration != runtime execution.

7. Green CI != relevant dependency coverage.

8. not_established != unresolved.

9. Universal lock presence != selected-environment membership.

10. Positive conclusions should carry witnesses.

11. Preserve typed semantic structure instead of flattening into strings/booleans.

12. Provider parsing, dependency semantics, CI composition, and application sequencing
    belong to different owners.

13. Migrate incrementally instead of rewriting every layer together.
```

Those are much more valuable than memorizing `deque` syntax.

---

# 44. Your current code-reading map

When reading today's implementation, follow this exact order rather than jumping randomly:

```text
S011 dependency source
dependency/pyproject.py
        ↓
dependency/environment.py

S001/S011 workflow selector
dependency/environment_selection.py
        ↓

S011 simple environment relation
dependency/environment_membership.py

S001 lock-backed relation
dependency/uv_membership.py
        ↓

CI meaning
ci/consumption.py
        ↓

static workflow collection
ci/workflow_commands.py
        ↓

runtime/static CI classification
ci/dependency_exercise.py
```

That order follows **data dependency**, not alphabetical file order.

---

# 45. Quick mastery check

Try answering these mentally before reading the answers:

> **Q1.** `soupsieve` exists in `uv.lock`. Can we say docs CI consumes it?

No. We need selected environment + membership proof.

> **Q2.** `uv sync --group docs` is visible. Can we say `docs` successfully formed?

No. Static selection only.

> **Q3.** `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`. What did we establish?

Static lock-backed transitive membership.

> **Q4.** `mlx` contains NumPy but CI installs `.[dev]`. Is NumPy's changed environment covered?

Not established by that workflow.

> **Q5.** Static consumption supported + exact-head CI green. Did the consuming command definitely execute successfully?

No. `supported_not_correlated`; static↔runtime correlation is absent.

> **Q6.** Why isn't `unresolved` the same as `not_established`?

`not_established` means our admitted analysis completed without proving the proposition. `unresolved` means ambiguity/missing evidence prevented safe determination.

If those six answers are clear, your mental model of today's work is already in good shape.

---

## Where I would go next in the learning session

The two pieces worth **deep code mastery**, rather than another broad overview, are:

```text
A. evaluate_uv_selected_environment_membership()
   especially:
   _validate_exact_source_identity
   _selected_roots
   _traverse_selected_roots
   _resolve_edge

B. evaluate_dependency_ci_coverage()
   especially:
   inspect_workflow_dependency_evidence
   _classify_static_consumption
   _classify_direct_exercise
```

Those two areas contain most of today's important engineering logic: **graph traversal + evidence-state composition**.

And we should do them with the actual S001 values flowing variable-by-variable through the functions, rather than explaining Python syntax abstractly.
