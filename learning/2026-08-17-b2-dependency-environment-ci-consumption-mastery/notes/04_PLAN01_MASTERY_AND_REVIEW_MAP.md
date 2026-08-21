# Plan 01 — Mastery and Review Map

**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Learning package:** `2026-08-17-b2-dependency-environment-ci-consumption-mastery`  
**Role:** smart mastery guide — what must be learned, what should be recognized, and what is intentionally deferred  
**Companion notes:** [`01_PLAN01_END_TO_END_LEARNING_NOTE.md`](01_PLAN01_END_TO_END_LEARNING_NOTE.md), [`02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md`](02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md), [`03_PLAN01_EVIDENCE_AND_PROOF_BOUNDARIES.md`](03_PLAN01_EVIDENCE_AND_PROOF_BOUNDARIES.md)  
**Status:** Plan-01 content route complete; independent reconstruction/test-ownership gates remain `[~]` until demonstrated later

---

## 1. How to use this file

This is not another full lesson and it is not a checklist of every line of code encountered.

Its purpose is to answer:

> **What do I actually need to master from Plan 01 so I can understand, explain, review, and later modify this part of UpgradePilot without relying on vague memory?**

The rule is:

```text
MASTER the causal mechanisms and proof boundaries.
RECOGNIZE supporting syntax and structures.
DO NOT memorize incidental helper details.
DEFER stronger membership/runtime questions to their proper plans.
```

A topic belongs in **MUST MASTER** only if misunderstanding it would make later UpgradePilot reasoning materially unreliable.

---

# 2. The one end-to-end route you MUST be able to reconstruct

You should eventually be able to explain this path in your own words without needing a line-by-line script:

```text
S001 dependency update
Soup Sieve 2.6 → 2.8.4
        ↓
exact base/head uv.lock evidence
        ↓
repository.py
exact immutable RepositoryTextFile evidence
        ↓
uv_lock.py
validate + interpret one file-level transition
        ↓
ExtractedDependencyVersionChange
        ↓
change.py
reconcile admitted source interpretations
        ↓
DependencyVersionChange
        ↓
analysis.py
coordinate extraction/reconciliation and translate provenance
        ↓
environment.py
UvLockDependencyContext
        ↓
exact static GitHub Actions workflow
        ↓
workflow_definition.py
WorkflowDefinition → StepsJobDefinition → RunStepDefinition
        ↓
workflow_context.py
effective working-directory/project binding
        ↓
environment_selection.py
recognize uv sync + parse --group docs
        ↓
DependencyGroupSelector("docs")
        ↓
ProjectEnvironmentSelectionObservation(state="observed")
```

And then you must stop at the correct boundary:

```text
DependencyGroupSelector("docs")
!=
docs reaches Soup Sieve
```

That missing membership bridge belongs to Plan 02.

If you can reconstruct this route accurately, most of Plan 01 is structurally understood.

---

# 3. MUST MASTER — the core concepts

## 3.1 Repository dependency vs core runtime dependency

You must understand why this statement is too broad:

```text
"Pydantic uses Soup Sieve"
```

The precise S001 relationship is:

```text
Pydantic repository docs/tooling
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

You must be comfortable with:

```text
direct dependency
transitive dependency
repository/tooling dependency
core runtime dependency
```

### Required understanding

You should be able to explain:

- why a transitive docs dependency can still matter to an upgrade investigation;
- why that does not make it a normal Pydantic runtime dependency;
- why relevance depends on the environment/path actually under investigation.

### Do not over-study

You do **not** need Soup Sieve internals, CSS-selector implementation details, or Beautiful Soup internals for this route.

---

## 3.2 Lockfile presence vs selected-environment membership

This is one of the highest-value Plan-01 lessons.

You must retain:

```text
soupsieve appears in uv.lock
!=
soupsieve belongs to every project environment
```

`uv.lock` can preserve packages from different groups/extras/workspace paths and other resolution conditions.

### Required understanding

You should be able to explain the difference between:

```text
resolved dependency evidence
selected environment
installed environment
runtime-exercised package
```

and why each requires stronger evidence than the previous one.

### Source anchor

`src/upgradepilot/dependency/uv_lock.py`

### Later bridge

Plan 02 must establish:

```text
DependencyGroupSelector("docs")
+ exact project metadata
+ exact lock graph
→ docs reaches soupsieve
```

---

## 3.3 Static workflow definition vs runtime execution

You must understand GitHub Actions at this practical depth:

```text
workflow
→ job
→ step
```

and distinguish:

```yaml
- uses: owner/action@revision
```

from:

```yaml
- run: shell command
```

For S001, the important static command is:

```bash
uv sync --all-packages --group docs
```

### Required understanding

You must be able to say:

```text
"The workflow is statically configured to synchronize the docs group"
```

without silently upgrading that to:

```text
"the command executed"
"the sync succeeded"
"Soup Sieve was installed"
"Soup Sieve was exercised"
```

### Source anchors

- `src/upgradepilot/github/workflow_definition.py`
- later runtime evidence is a separate responsibility; Plan 01 does not merge them.

---

## 3.4 Exact evidence identity and provenance

You do not need to memorize every field, but you must understand **why exact evidence is exact**.

Core identity:

```text
repository + path + immutable revision
```

Supporting provenance/defensive evidence includes:

```text
blob SHA
returned path
reported byte count
decoded byte count
retrieval metadata
```

### Required understanding

You should be able to explain:

- why revision + path identify a specific immutable Git file lookup;
- why blob SHA is an additional Git object/content provenance handle rather than merely another version number;
- why byte counts are defensive acquisition/boundedness checks, not dependency semantics;
- why current downstream code may revalidate strong fields because `RepositoryTextFile` still admits older/manual fixtures.

### Source anchor

`src/upgradepilot/github/repository.py`

### Important precision

Do not claim that UpgradePilot independently recomputes the Git blob hash from decoded bytes unless the source actually does so.

---

## 3.5 File-level interpretation vs PR-wide reconciliation

This distinction is central to the architecture.

### File-level interpretation

`uv_lock.py` answers:

> What exact dependency transition does this admitted `uv.lock` evidence establish?

Output:

```text
ExtractedDependencyVersionChange
```

S001:

```text
soupsieve 2.6 → 2.8.4
```

### PR-wide reconciliation

`change.py` answers:

> Do all admitted dependency-change interpretations safely agree on one canonical PR-wide change?

Output:

```text
DependencyVersionChange
```

### Required understanding

You must retain:

```text
INTERPRETED file-level result
!=
RECONCILED PR-wide result
```

and understand why a material `DependencyChangeProblem` cannot simply be ignored because another source succeeded.

### Source anchors

- `src/upgradepilot/dependency/uv_lock.py`
- `src/upgradepilot/dependency/change.py`

---

## 3.6 Source context vs selected environment

After reconciliation, `analysis.py` translates trusted provenance into typed dependency-source context.

For S001:

```text
DependencyVersionChange
+ uv.lock provenance
→ UvLockDependencyContext
```

### Required understanding

You must be able to explain:

```text
UvLockDependencyContext
= the trusted change came from exact uv.lock evidence
```

but not:

```text
UvLockDependencyContext
= docs contains Soup Sieve
```

The best compact rule is:

```text
SOURCE CONTEXT
!=
SELECTED ENVIRONMENT CONTEXT
```

### Source anchors

- `src/upgradepilot/dependency/analysis.py`
- `src/upgradepilot/dependency/environment.py`

---

## 3.7 Provider-owned workflow IR vs dependency-owned semantics

This is an important design/ownership lesson.

GitHub owns:

```text
workflow YAML structure
jobs
steps
run/uses
working-directory/defaults
static source locations
```

Dependency owns:

```text
what a Python project-selection command means
```

Therefore:

```text
github/workflow_definition.py
→ RunStepDefinition(
     command="uv sync --all-packages --group docs"
   )
```

then:

```text
dependency/environment_selection.py
→ DependencyGroupSelector("docs")
```

### Required understanding

You should be able to explain why `environment_selection.py` does **not** parse YAML directly and why `workflow_definition.py` does **not** become dependency-aware merely because a `run:` string contains `uv` or `pip`.

This separation is one of the strongest architectural ideas in Plan 01.

---

## 3.8 `observed` vs `not_observed` vs `unresolved`

Do not reduce this to True/False.

You must understand:

```text
observed
= supported static declaration safely interpreted

not_observed
= source safely inspected; no admitted declaration found

unresolved
= materially relevant syntax/context exists, but exact meaning cannot be established safely
```

Examples worth remembering:

```text
uv sync --group docs
→ observed

 echo "pip install -e .[dev]"
→ not_observed

uv sync --group "${{ matrix.group }}"
→ unresolved

uv sync
→ unresolved for exact group selection because defaults need separate evidence
```

### Required principle

```text
UNRESOLVED
!=
NEGATIVE FACT
```

Missing/ambiguous evidence must not be converted into proof of absence.

### Source anchor

`src/upgradepilot/dependency/environment_selection.py`

---

# 4. MUST MASTER — the source-code mechanisms

You do not need every helper memorized. You do need to understand the control-flow patterns that carry the actual responsibility.

## 4.1 Guard clauses / early returns

Pattern:

```python
if unsupported_or_invalid:
    return problem
```

Used heavily in source evidence and selector interpretation.

### Why it matters

The code makes proof admission explicit and stops before stronger interpretation when prerequisites fail.

You should be able to read a function and identify:

```text
admission checks
→ narrowing
→ interpretation
→ result construction
```

---

## 4.2 `isinstance(...)` narrowing + assertions after guards

Typical pattern:

```python
if isinstance(value, ProblemType):
    return value

assert isinstance(value, ExpectedType)
```

### Why it matters

The assertion is an internal invariant **after** earlier control flow has ruled out other states. It is not a substitute for validating untrusted evidence.

You should be able to distinguish:

```text
external/domain uncertainty
→ typed problem/abstention

impossible internal state after established guards
→ assertion/RuntimeError invariant
```

---

## 4.3 Typed unions and dataclasses as responsibility contracts

Examples:

```python
type StepEntry = RunStepDefinition | UsesStepDefinition | StepProblem
```

and frozen dataclasses such as:

```python
@dataclass(frozen=True, slots=True)
class DependencyGroupSelector:
    ...
```

### Why it matters

The type shape makes legal evidence states explicit and prevents downstream consumers from depending on generic dictionaries/parser nodes.

You should understand `frozen=True` and `slots=True` at operational depth:

```text
frozen=True
→ instances are intended to be immutable after construction

slots=True
→ fixed attribute layout; avoids ordinary per-instance __dict__
```

Do not turn this into a dataclass-internals course.

---

## 4.4 Collections used for reconciliation

You must be able to read these mechanisms when they carry proof logic:

```text
list accumulation + append/extend
set comprehensions
len(set) == 1 consensus checks
tuple conversion for immutable output
generator expressions
next(..., None)
enumerate(...)
```

Especially in `change.py`, sets are not incidental syntax; they implement consensus checks such as:

```text
exactly one normalized package identity
exactly one old→proposed version pair
```

---

## 4.5 `**common` / keyword unpacking

In `_source_contexts(...)`, shared fields can be collected once:

```python
common = {
    "repository": ...,
    "revision": ...,
    "normalized_package": ...,
    "source_evidence": ...,
}
```

then supplied to a typed context:

```python
UvLockDependencyContext(**common)
```

### Why it matters

You need to understand the data flow, not memorize the syntax trick. `**mapping` expands mapping keys/values into keyword arguments.

---

## 4.6 `shlex` + bounded selector parsing

For S001:

```python
shlex.split("uv sync --all-packages --group docs")
```

produces shell-like tokens approximately:

```python
["uv", "sync", "--all-packages", "--group", "docs"]
```

Then the bounded parser recognizes the explicit selector:

```text
--group docs
→ DependencyGroupSelector("docs", mode="include")
```

### Why it matters

You should understand why this is safer than naïve whitespace/string-substring matching and why the parser deliberately abstains on unsupported/dynamic ambiguity.

You do **not** need to master general shell parsing or regular-expression theory here.

---

## 4.7 Normalized identity vs source spelling

Examples:

```text
name="Docs.Build"
normalized_name="docs-build"
```

or normalized package names in dependency reconciliation.

### Why it matters

UpgradePilot often needs both:

```text
original spelling
→ provenance/diagnostics

normalized identity
→ reliable comparison
```

You must understand the distinction even when S001's simple name `docs` looks identical after normalization.

---

# 5. MUST RECOGNIZE — but do not over-study

These topics matter enough that they should not look unfamiliar, but they are not Plan-01 mastery targets.

## 5.1 PyYAML representation nodes

Recognize:

```text
MappingNode
SequenceNode
ScalarNode
```

and the architecture:

```text
raw YAML
→ PyYAML syntax nodes
→ UpgradePilot typed GitHub Actions IR
```

You do not need to memorize the ~650-line parser or PyYAML internals.

---

## 5.2 Source spans and `source_index`

Recognize that the workflow IR preserves static source location/order so evidence can point back to a specific job/step.

Do not confuse static source index with runtime step identity.

---

## 5.3 Working-directory precedence

Remember:

```text
step
>
job defaults
>
workflow defaults
>
repository root
```

You should understand why a dynamic higher-precedence value makes the result unresolved rather than falling through to a lower value.

You do not need to memorize path-normalization helpers line by line.

---

## 5.4 Parser hardening details

Recognize the current safety mechanisms:

```text
bounded node visits
bounded nesting depth
recursive-alias rejection
duplicate material-key detection
```

Also remember the audit finding:

```text
yaml.compose(...) occurs before UpgradePilot's post-compose graph guard
→ pathological nesting can raise composition-time RecursionError
→ bounded robustness gap worth a focused future fix/test
```

This is an engineering-audit finding, not a Plan-01 concept you need to rehearse daily.

---

# 6. Representative source responsibilities you should later reconstruct independently

These are the best ownership checkpoints. You do not need to memorize exact source text; you should be able to reconstruct the responsibility and important control flow.

## A. `extract_uv_lock_changes(...)`

You should eventually explain:

```text
input/preconditions
→ admitted uv.lock changed-file path/status
→ exact base/head availability
→ provenance construction
→ independent TOML parsing/validation
→ base/head package comparison
→ exactly-one-transition rule
→ ExtractedDependencyVersionChange or DependencyChangeProblem
```

Must state the non-proof:

```text
no environment membership
no CI consumption
no runtime exercise
```

---

## B. `compare_extracted_dependency_changes(...)`

You should eventually explain:

```text
admitted source results
→ preserve blocking problems
→ require at least one extraction
→ require exactly one normalized package
→ require exactly one exact version pair
→ DependencyVersionChange
```

Must state why reconciliation is stronger than one file-level extraction.

---

## C. `_source_contexts(...)`

You should eventually explain:

```text
trusted reconciled change + source provenance
→ choose typed source-context variant
→ for uv_lock: UvLockDependencyContext
```

Must state:

```text
source-context construction
!= environment membership inference
```

---

## D. `observe_project_environment_selection(...)`

You should eventually explain:

```text
RunStepDefinition
+ independently known pyproject path
+ effective working directory
→ bounded shell segments
→ recognize pip/uv project command
→ parse explicit selectors
→ ProjectEnvironmentSelectionObservation
```

For S001, predict:

```text
manager = uv
operation = sync
selector = DependencyGroupSelector("docs", mode="include")
state = observed
```

Must state:

```text
observed static selector
!= command execution
!= membership
```

---

# 7. Representative tests worth owning later

Formal test ownership was intentionally deferred during the learning route. When revisiting it, these are the highest-value tests/families rather than every test in the modules.

## 7.1 uv-lock extraction

Source family:

```text
tests/test_uv_lock_change.py
```

Own at least:

```text
one successful exact-transition/provenance case
one discriminating problem/abstention case
```

You should be able to explain:

```text
setup
→ function under test
→ expected output/problem
→ protected invariant
→ what the test does NOT prove
```

---

## 7.2 PR-wide change reconciliation

Source family:

```text
tests/test_dependency_change.py
```

Own one case demonstrating why agreeing sources promote and conflicting/problem evidence does not.

---

## 7.3 Workflow IR

Source:

```text
tests/test_github_workflow_definition.py
```

Understand one test that protects typed run/uses structure or local problem preservation.

Do not try to memorize every YAML edge case.

---

## 7.4 Project-environment selection

Source:

```text
tests/test_project_environment_selection.py
```

Highest-value cases:

```text
S001-style uv --group docs → observed selector
uv dynamic group → unresolved
uv with no explicit selector → unresolved, not negative
echoed pip text → not_observed
```

These four cases capture most of the proof semantics of the observer.

---

# 8. What you should be able to answer after mastering Plan 01

You should eventually be able to answer these without vague language.

### Dependency meaning

1. Why is Soup Sieve relevant to Pydantic S001 even though it is not a normal core runtime dependency?
2. What is the exact `docs → ... → soupsieve` conceptual path?
3. Why does Soup Sieve appearing in `uv.lock` not establish docs membership?

### Evidence pipeline

4. What is the difference between `RepositoryTextFile`, `ExtractedDependencyVersionChange`, `DependencyVersionChange`, and `UvLockDependencyContext`?
5. Why is file-level INTERPRETATION different from PR-wide RECONCILIATION?
6. Why does source provenance travel with the dependency change?

### Architecture

7. Why does `github/workflow_definition.py` own workflow structure rather than Dependency?
8. Why does `dependency/environment_selection.py` own `--group docs` interpretation rather than GitHub?
9. Why is `analysis.py` mostly orchestration/integration rather than another source parser?

### Static selection

10. Starting from `uv sync --all-packages --group docs`, how does the code reach `DependencyGroupSelector("docs")`?
11. Why does working-directory/project binding matter?
12. Why are `observed`, `not_observed`, and `unresolved` separate states?

### Proof boundary

13. At the exact end of Plan 01, what has been established?
14. What is still missing before we can say the docs environment reaches Soup Sieve?
15. Why can none of Plan 01's static evidence alone establish runtime execution or package exercise?

If these answers are accurate and source-grounded, the conceptual core of Plan 01 is mastered.

---

# 9. What NOT to memorize

Do not waste learning effort memorizing:

```text
all helper function names in workflow_definition.py
all regular expressions
all parser reason strings
all YAML node mechanics
all uv CLI options
all SourceSpan values
all exact provenance byte counts
all test fixture boilerplate
all line numbers
```

Instead, know where to find them and understand the responsibility they support.

The durable skill is:

```text
open source
→ identify owner/input/output
→ trace material control flow
→ understand evidence strength
→ recognize unsupported ambiguity
→ avoid overclaiming
```

---

# 10. Intentionally deferred — do not pull these backward into Plan 01

These are important, but they belong later.

## Plan 02

```text
pyproject.toml dependency-group semantics
uv.lock environment membership
selected-root graph traversal
BFS / reachability witness
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
membership states
static CI consumption
coverage aggregation
```

## Later runtime/evaluation work

```text
static↔runtime job/step correlation
actual command execution
resolver/install success
exact proposed-version runtime witness
direct package exercise
behavioral compatibility
safety/action recommendation
```

The discipline is:

```text
learn the current proof boundary deeply
without pretending later proof layers are already solved
```

---

# 11. Current mastery status

The Plan-01 **content route is complete**.

Current honest status:

```text
[x] conceptual route taught through Chunk 5
[x] current-source guided walkthroughs completed for the core mechanisms
[x] major design/proof boundaries discussed and audited
[x] Plan-01 study artifacts created

[~] independent closed-source/current-source reconstruction still deferred
[~] representative-test explanations still need independent user-owned demonstration
```

These `[~]` items do not invalidate the learning already completed and should not block Plan 02 while no RED misconception exists.

They remain visible so later review can distinguish:

```text
"I have studied and understood this with assistance"
from
"I can independently reconstruct and defend this mechanism"
```

---

# 12. Minimal high-value review loop

When returning to Plan 01 later, do not reread everything from scratch.

Use this order:

```text
1. Read the end-to-end diagram in this file.
2. Re-state the five highest-value inequalities:
   lock presence != membership
   interpreted != reconciled
   source context != selected environment
   static definition != runtime execution
   selector("docs") != docs reaches Soup Sieve
3. Open the four ownership functions:
   extract_uv_lock_changes(...)
   compare_extracted_dependency_changes(...)
   _source_contexts(...)
   observe_project_environment_selection(...)
4. Explain one representative test from each side:
   dependency-change evidence
   project-environment selection
5. Stop once the Plan-01 boundary is accurate; continue to the current active plan.
```

That review loop is intentionally small. It targets the knowledge that is expensive to lose and avoids turning maintenance learning into repeated full-course study.
