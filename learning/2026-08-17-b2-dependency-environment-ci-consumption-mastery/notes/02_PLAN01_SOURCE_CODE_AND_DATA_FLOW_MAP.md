# Plan 01 — Source Code and Data-Flow Map

**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Learning package:** `2026-08-17-b2-dependency-environment-ci-consumption-mastery`  
**Role:** source-oriented study map for Plan 01  
**Companion note:** [`01_PLAN01_END_TO_END_LEARNING_NOTE.md`](01_PLAN01_END_TO_END_LEARNING_NOTE.md)  
**Status:** Plan-01 content route mapped; deferred ownership/reconstruction gates remain deferred

---

## 1. Purpose of this file

This artifact is not another narrative explanation of Plan 01. Its job is to answer the source-code questions that matter when reopening UpgradePilot later:

```text
Which module owns this responsibility?
What exact kind of input enters it?
Which functions/types carry the responsibility?
What output leaves it?
Which module consumes that output next?
Which Python control-flow mechanisms carry the behavior?
What proposition has actually been established at that boundary?
What has NOT been established yet?
```

The central Plan-01 source path is split into two related evidence tracks:

```text
TRACK A — dependency-change meaning

repository.py
→ uv_lock.py
→ change.py
→ analysis.py
→ environment.py

TRACK B — static workflow/project-selection meaning

repository.py / exact workflow source
→ github/workflow_definition.py
→ dependency/workflow_context.py
→ dependency/environment_selection.py
```

Those tracks become conceptually related in Plan 01 because they describe the same real S001 investigation, but this diagram must **not** be misread as one literal Python call stack from the first file to the last file.

A module-to-module arrow in this artifact can mean one of three things:

```text
DIRECT CALL
module A actually invokes module B

TYPED DATA HANDOFF
A produces a typed value later consumed by B or by an orchestrator

EVIDENCE COMPOSITION RELATION
two independently established facts are later intended to be composed
```

Where that distinction matters, this file states it explicitly.

---

# 2. Plan-01 source topology at a glance

```text
UPSTREAM / REPOSITORY EVIDENCE

ChangedFile metadata
Exact base/head repository files
Exact head workflow definition
        │
        ▼
┌─────────────────────────────────────────────┐
│ upgradepilot.github.repository             │
│                                             │
│ RepositoryTextFile                         │
│ exact immutable repository text evidence   │
└─────────────────────────────────────────────┘
        │
        ├───────────────────────────────────────────────┐
        │                                               │
        ▼                                               ▼
DEPENDENCY-CHANGE TRACK                           WORKFLOW TRACK

┌─────────────────────────────┐             ┌──────────────────────────────┐
│ dependency/uv_lock.py       │             │ github/workflow_definition.py│
│                             │             │                              │
│ exact uv.lock evidence      │             │ raw workflow YAML            │
│ → file-level transition     │             │ → typed GitHub Actions IR    │
└─────────────────────────────┘             └──────────────────────────────┘
        │                                               │
        ▼                                               ▼
ExtractedDependencyVersionChange                RunStepDefinition
        │                                               │
        ▼                                               ├──────────────┐
┌─────────────────────────────┐                         │              │
│ dependency/change.py        │                         ▼              ▼
│                             │               workflow_context.py  environment_selection.py
│ admitted interpretations   │               static path/default  selector semantics
│ → PR-wide reconciliation   │               resolution          
└─────────────────────────────┘                         │              │
        │                                               └──────┬───────┘
        ▼                                                      ▼
DependencyVersionChange                          ProjectEnvironmentSelectionObservation
        │                                        └─ DependencyGroupSelector("docs")
        ▼
┌─────────────────────────────┐
│ dependency/analysis.py      │
│                             │
│ orchestration + context     │
│ construction                │
└─────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│ dependency/environment.py   │
│                             │
│ UvLockDependencyContext     │
└─────────────────────────────┘

PLAN-01 STOP LINE

UvLockDependencyContext
+
DependencyGroupSelector("docs")

DO NOT YET COMPOSE INTO:
"docs contains/reaches Soup Sieve"

That missing relation belongs to Plan 02 membership analysis.
```

---

# 3. Concrete S001 values carried through the map

Keep these values nearby when reading the source. They prevent abstract types from losing contact with the real investigation.

```text
repository:
pydantic/pydantic

changed package:
soupsieve

old version:
2.6

proposed version:
2.8.4

base revision:
652a61ce4f9d7d76eaada31535807a485ece0e21

head revision:
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a

changed dependency source:
uv.lock

relevant project file:
pyproject.toml

relevant workflow job:
docs-build

relevant static command:
uv sync --all-packages --group docs

static project selector:
DependencyGroupSelector(name="docs", mode="include")
```

The later dependency path known from preserved real-case evidence is:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Plan 01 does not yet execute the source logic that proves that graph-membership relation.

---

# 4. `github/repository.py` — exact repository-file evidence provider

Source:
[`src/upgradepilot/github/repository.py`](../../../src/upgradepilot/github/repository.py)

## Responsibility

`repository.py` owns **GitHub-specific acquisition and provenance of repository text at immutable revisions**.

It answers:

> Give the investigation the exact repository text requested at this exact commit, with enough acquisition/provenance information for stricter downstream boundaries to decide whether they can trust it.

It does **not** interpret dependency semantics, TOML meaning, workflow meaning, environment selection, or package membership.

## Central type

```python
@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    path: str
    revision: str
    blob_sha: str
    content: str
    repository: str | None = None
    returned_path: str | None = None
    reported_byte_count: int | None = None
    decoded_byte_count: int | None = None
    retrieved_at: datetime | None = None
```

### Practical meaning

```text
path
→ requested repository-relative source location

revision
→ immutable commit identity used for acquisition

blob_sha
→ Git object/content-provenance handle returned by GitHub

content
→ decoded UTF-8 source text

repository / returned_path
→ stronger provider/source identity

reported_byte_count / decoded_byte_count
→ acquisition-consistency and bounded-resource evidence

retrieved_at
→ acquisition time provenance
```

Important design nuance:

```text
repository + path + immutable revision
```

are the core coordinates for locating an exact repository file.

`blob_sha` strengthens provenance/content identity but is not currently presented as a locally recomputed cryptographic verification of the downloaded bytes.

The byte counts are defensive acquisition/resource metadata, not dependency semantics.

## Material provider methods for Plan 01

```python
get_pull_request_base_file(...)
get_pull_request_head_file(...)
get_exact_commit_text_file(...)
get_exact_head_workflow_file(...)
```

The dependency-change path needs exact base/head file evidence. The workflow path needs exact workflow text at a revision.

## Input → output

```text
INPUT
repository identity
+ immutable commit SHA
+ repository-relative path

PROVIDER WORK
validate request identity/path
→ GitHub acquisition
→ response/path/content/provenance checks
→ size/UTF-8 boundary

OUTPUT
RepositoryTextFile
or
UnavailableRepositoryFile
```

## Important Python mechanisms

At Plan-01 depth:

```text
frozen dataclass
→ evidence object is value-like and not intended for mutation after construction

union result types
→ successful exact text and unavailable evidence are different states

early failure / explicit provider errors
→ malformed acquisition does not become fabricated content

optional strong fields
→ historical/manual fixtures are admitted by the type, so downstream strict boundaries may need to revalidate them
```

## Downstream relationships

### To `dependency/uv_lock.py`

Typed data handoff:

```text
RepositoryTextFile(base uv.lock)
RepositoryTextFile(head uv.lock)
→ extract_uv_lock_changes(...)
```

### To `github/workflow_definition.py`

Typed data handoff:

```text
RepositoryTextFile(.github/workflows/...yml)
→ parse_workflow_definition(...)
```

## Evidence state

```text
external repository source
→ ACQUIRED
→ provider-level VALIDATED evidence
```

## Does not establish

```text
the file's dependency semantics
that a dependency changed
that a workflow command executed
that any package belongs to any environment
```

---

# 5. `dependency/uv_lock.py` — source-specific exact transition interpretation

Source:
[`src/upgradepilot/dependency/uv_lock.py`](../../../src/upgradepilot/dependency/uv_lock.py)

## Responsibility

`uv_lock.py` answers:

> Given admitted exact base/head `uv.lock` evidence, what exact dependency version transition can this source establish?

This is **source-specific interpretation**.

It does not decide whether multiple dependency source formats agree across the whole PR. That belongs to `change.py`.

## Main entry point

```python
extract_uv_lock_changes(...)
```

## Conceptual input

```text
ChangedFile for uv.lock
+
exact base RepositoryTextFile
+
exact head RepositoryTextFile
```

For S001:

```text
base uv.lock
contains Soup Sieve 2.6

head uv.lock
contains Soup Sieve 2.8.4
```

## Material control flow

```text
extract_uv_lock_changes(...)
        ↓
repository-relative path / basename admission
        ↓
modified-status admission
        ↓
exact base/head availability
        ↓
post-guard type narrowing
        ↓
_build_source_evidence(...)
        ↓
parse base TOML independently
parse head TOML independently
        ↓
_validate_package_record(...)
        ↓
group normalized package records
        ↓
_compare_uv_lock_packages(...)
        ↓
_compare_single_record(...)
        ↓
require exactly one transition
        ↓
ExtractedDependencyVersionChange
```

## Central output type

```text
ExtractedDependencyVersionChange
```

Conceptually for S001:

```text
package = "soupsieve"
normalized_package = "soupsieve"
old_version = "2.6"
proposed_version = "2.8.4"
source_evidence.file_format = "uv_lock"
source_evidence.extraction_method = "exact_base_head_files"
```

This is a **file-level interpreted transition**, not yet a canonical PR-wide transition.

## Material helper responsibilities

### `_build_source_evidence(...)`

Translates strict exact-file provenance into dependency-owned source provenance.

### `_parse_uv_lock(...)`

Parses TOML syntax/structure for the bounded lockfile responsibility.

### `_validate_package_record(...)`

Rejects package records that cannot safely participate in the bounded comparison.

### `_compare_uv_lock_packages(...)`

Coordinates package-level comparison between validated base/head record groups.

### `_compare_single_record(...)`

Compares one candidate base record and one candidate head record while preserving the exact-change rule.

### `_freeze_toml_value(...)`

Produces stable/comparable representations of nested TOML values where comparison requires them.

## Important Python mechanisms learned

```python
parts[-1]
```

Negative index: final repository-relative path component. This permits locations such as `backend/uv.lock`; it does not mean only root-level `uv.lock`.

```python
if ...:
    return _problem(...)
```

Guard clauses / early returns keep unsupported evidence from falling deeper into trusted interpretation.

```python
isinstance(...)
assert isinstance(...)
```

External uncertain evidence is checked first; assertions after guards express internal invariants/narrowed states.

Other material mechanisms:

```text
_MISSING sentinel + `is`
defaultdict
enumerate
append
set union
tuple return/unpacking
Counter
canonicalization
```

These are worth knowing because they carry the actual comparison, grouping, and ambiguity logic.

## Direct downstream relationship

`uv_lock.py` returns an admitted result later consumed by the PR-wide reconciliation boundary:

```text
ExtractedDependencyVersionChange
or DependencyChangeProblem
        ↓
dependency/change.py
```

## Evidence state

```text
VALIDATED exact uv.lock evidence
→ INTERPRETED file-level dependency transition
```

## Does not establish

```text
PR-wide agreement across every admitted dependency source
direct/transitive dependency role
selected project environment
CI consumption
runtime installation
package exercise
compatibility/safety/action
```

---

# 6. `dependency/change.py` — source-independent PR-wide reconciliation

Source:
[`src/upgradepilot/dependency/change.py`](../../../src/upgradepilot/dependency/change.py)

## Responsibility

`change.py` answers:

> Do all admitted dependency-change interpretations safely support one canonical package/version transition for this PR?

It deliberately does not know how `uv.lock`, `requirements.txt`, or `pyproject.toml` are parsed internally.

This separation is fundamental:

```text
source-specific extractor
→ what does this exact source mean?

change.py
→ do admitted source meanings agree?
```

## Central types

### `DependencyChangeSourceEvidence`

Provenance for one admitted dependency-change source.

Typical fields include source path/format/extraction method and exact revision/blob/byte metadata where available.

### `ExtractedDependencyVersionChange`

One source-specific interpreted transition:

```text
package
normalized_package
old_version
proposed_version
source_evidence
```

### `DependencyChangeProblem`

Expected typed inability/ambiguity/problem from an admitted dependency source responsibility.

### `DependencyVersionChange`

The stronger canonical PR-wide reconciled transition.

For S001:

```text
normalized package: soupsieve
old: 2.6
proposed: 2.8.4
agreeing source evidence: exact admitted dependency-change provenance
```

## Main function

```python
compare_extracted_dependency_changes(...)
```

## Material control flow

```text
admitted extraction results
        ↓
collect unique source evidence
        ↓
find first blocking DependencyChangeProblem
        ↓
if problem exists → stop
        ↓
materialize successful extracted transitions
        ↓
require at least one success
        ↓
collect normalized package identities
        ↓
require exactly one package
        ↓
collect exact (old_version, proposed_version) pairs
        ↓
require exactly one transition
        ↓
construct DependencyVersionChange
```

## Why problems are checked before promotion

Suppose one admitted source says:

```text
soupsieve 2.6 → 2.8.4
```

but another admitted dependency source is malformed/ambiguous.

The stronger `DependencyVersionChange` should not mean:

```text
"one source looked good, therefore ignore the admitted problem"
```

A PR-wide reconciled claim is stronger than a file-level interpretation, so admitted contradictory/unreadable material must not be silently cancelled by one successful extraction.

## Important Python mechanisms learned

```python
Sequence[...]
```

Function accepts an ordered/general sequence contract instead of requiring one concrete list type.

```python
next((...), None)
```

Find one blocking problem without requiring a separate loop variable protocol.

```python
{... for ...}
```

Set comprehensions collapse values into unique identities for consensus checks.

```python
len(unique_values) == 1
```

The key reconciliation pattern: exactly one unique package and exactly one unique version pair.

Other material syntax:

```text
generator expressions
tuple materialization
tuple version pairs
tuple unpacking
sorted(...) for deterministic diagnostics
!r in formatted diagnostics
conditional expressions
list accumulation/deduplication
final tuple conversion
```

## Direct upstream/downstream relationship

```text
uv_lock.py / requirements.py / pyproject.py
→ ExtractedDependencyVersionChange | DependencyChangeProblem
        ↓
compare_extracted_dependency_changes(...)
        ↓
DependencyVersionChange | DependencyChangeProblem
```

The actual orchestration that gathers these source-specific results lives in `analysis.py`.

## Evidence state

```text
INTERPRETED admitted file-level results
→ RECONCILED PR-wide DependencyVersionChange
```

## Bounded product limitation

The current boundary expects one canonical dependency transition.

That means:

```text
current UpgradePilot bounded contract
= one canonical transition per accepted analysis
```

not:

```text
real dependency-update PRs universally contain only one package change
```

## Does not establish

```text
which project environment selects the package
whether CI consumes the package
whether the proposed version ran
compatibility/safety/action
```

---

# 7. `dependency/analysis.py` — orchestration and typed source-context construction

Source:
[`src/upgradepilot/dependency/analysis.py`](../../../src/upgradepilot/dependency/analysis.py)

## Responsibility

`analysis.py` is the **integration/orchestration boundary** for PR-wide dependency-change analysis.

It answers:

> Which admitted changed dependency sources should be routed to which source-specific interpreters, how should their results be reconciled, and what typed dependency-source contexts should travel with the canonical result?

It does not contain the deepest lockfile parsing semantics. It coordinates the modules that do.

## Central result type

```python
DependencyChangeAnalysis
```

Conceptually:

```text
DependencyChangeAnalysis
├── dependency: DependencyVersionChange
└── source_contexts: tuple[DependencySourceContext, ...]
```

A compatibility property such as `direct_requirements_install_path` can be projected from the typed source contexts, but those typed contexts remain the source of truth.

## Main function

```python
analyze_dependency_change(
    identity,
    changed_files,
    repository_client,
)
```

## Material orchestration flow

```text
PullRequestIdentity
+ changed files
+ repository client
        ↓
for each changed file
        ↓
route supported dependency source format
        ├── requirements → requirements extractor
        ├── pyproject optional-extra → pyproject extractor
        └── uv.lock → uv-lock extractor
        ↓
collect extraction results
        ↓
compare_extracted_dependency_changes(...)
        ↓
if DependencyChangeProblem → return problem
        ↓
_source_contexts(...)
        ↓
DependencyChangeAnalysis
```

## Important routing behavior

The module may need to acquire exact base/head content before calling a source-specific extractor.

For `uv.lock`, the source-specific interpretation remains in `uv_lock.py`.

For `pyproject.toml`, the analysis route also preserves the optional-extra name keyed by exact source evidence so that later context construction can recover the source-specific semantic scope.

## Important Python mechanisms learned

### Typed lists/dicts

Used to accumulate source-specific results and preserve source-evidence-to-scope associations.

### `for` + `continue`

The orchestration route can recognize one source format, process it, and continue without collapsing all formats into one giant conditional block.

### `pass`

Can represent a deliberate neutral/no-op branch where a changed file does not produce an admitted change under the current rule. `pass` is not automatically missing implementation.

### `isinstance(...)`

Used to distinguish expected problem/result variants after functions return union types.

### `**common`

Keyword-dictionary unpacking in `_source_contexts(...)` avoids repeating fields shared by several concrete typed contexts.

### frozen dataclass as dictionary key

Exact source evidence can be used as a dictionary key when immutable/hashable, allowing source-specific semantic detail (such as an optional-extra name) to be reattached later without contaminating the source-independent reconciliation model.

### explicit `RuntimeError`

Used when trusted internal state becomes impossible—not for normal external evidence uncertainty.

That distinction is important:

```text
untrusted/external ambiguity
→ typed domain problem / abstention

internal invariant unexpectedly broken
→ programming/runtime error
```

## Direct downstream relationship

After reconciliation:

```text
DependencyVersionChange
+
exact agreeing source evidence
        ↓
_source_contexts(...)
        ↓
typed DependencySourceContext values
```

Those concrete context classes live in `environment.py`.

## Evidence state

`analysis.py` itself is primarily orchestration. It does not deserve a stronger evidence verb merely for wrapping data.

The important progression is:

```text
DependencyVersionChange
= RECONCILED dependency transition

_source_contexts(...)
= attach/translate trusted source provenance into typed source context
```

## Does not establish

```text
selected environment membership
static CI consumption
runtime execution
compatibility/safety/action
```

---

# 8. `_source_contexts(...)` — reconciliation provenance → typed dependency-source context

This helper is inside:
[`src/upgradepilot/dependency/analysis.py`](../../../src/upgradepilot/dependency/analysis.py)

It is important enough to map separately because it is the bridge from a generic canonical transition to source-specific downstream reasoning.

## Conceptual signature

```python
def _source_contexts(
    identity: PullRequestIdentity,
    dependency: DependencyVersionChange,
    *,
    pyproject_optional_extras: dict[DependencyChangeSourceEvidence, str],
) -> tuple[DependencySourceContext, ...]:
```

## Control flow

```text
contexts = []
        ↓
for each evidence in dependency.source_evidence
        ↓
build common fields
repository
head revision
normalized package
exact source evidence
        ↓
branch by evidence meaning
        ├── uv_lock
        │   → UvLockDependencyContext(**common)
        │
        ├── pyproject_optional_extra
        │   → recover extra from side map
        │   → PyprojectOptionalExtraDependencyContext(extra=..., **common)
        │
        └── requirements/constraints
            → correct concrete context type
        ↓
return tuple(contexts)
```

## Why the revision is the head SHA

The context describes the dependency situation being evaluated in the proposed PR state.

Therefore:

```text
context.revision = identity.head_sha
```

while the attached source evidence can still preserve base/head provenance used to establish the transition.

## Why concrete context variants matter

The code could have used one generic record with many optional fields:

```text
source_path
optional_extra?
dependency_group?
constraints?
uv_lock?
...
```

But that would allow combinations of fields that were never actually established.

Concrete variants encode stronger valid-state boundaries:

```text
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
...
```

The type itself communicates which family of downstream reasoning is justified.

## S001 result

The real S001 branch is:

```text
source evidence file_format = "uv_lock"
        ↓
UvLockDependencyContext(
    repository="pydantic/pydantic",
    revision=<head SHA>,
    normalized_package="soupsieve",
    source_evidence=<exact uv.lock evidence>,
)
```

## Does not establish

The key rule:

```text
SOURCE CONTEXT
!=
SELECTED ENVIRONMENT CONTEXT
```

This helper does not invent `docs`, `docs-upload`, or any other project selector.

---

# 9. `dependency/environment.py` — typed dependency-source context models

Source:
[`src/upgradepilot/dependency/environment.py`](../../../src/upgradepilot/dependency/environment.py)

## Responsibility

This module represents **dependency-owned source context before workflow/runtime interpretation**.

It answers:

> What exact dependency-source/environment identity has already been established strongly enough that downstream logic can choose the correct next bounded reasoning mechanism?

It does not answer whether a workflow actually selected that environment.

## Relevant context types

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

and their union:

```text
DependencySourceContext
```

## S001 type

```python
@dataclass(frozen=True, slots=True)
class UvLockDependencyContext:
    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        return self.source_evidence.path
```

## S001 conceptual object

```text
UvLockDependencyContext

repository:
pydantic/pydantic

revision:
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a

normalized_package:
soupsieve

source_evidence:
exact uv.lock change provenance
```

## Why this object exists

Before this point, the canonical change can say:

```text
soupsieve 2.6 → 2.8.4
with agreeing source evidence
```

After source-context construction, downstream logic can additionally say:

```text
this canonical change is established in the uv-lock source-context family
```

That is effectively permission to use later **uv-specific membership reasoning**, provided the other required evidence is independently established.

Conceptually:

```text
UvLockDependencyContext
+
exact project metadata
+
independently established project selector
        ↓
future bounded uv membership analysis
```

## Evidence state

The transition has already been RECONCILED. The source context is best described as:

```text
dependency-source contextualized
```

Do not automatically read the learning vocabulary word `CONTEXTUALIZED` as meaning all environment relations are now known.

## Does not establish

```text
docs was selected
docs contains/reaches Soup Sieve
uv sync executed
CI consumed Soup Sieve
Soup Sieve was installed
Soup Sieve ran
exact 2.8.4 ran
compatibility/safety/action
```

---

# 10. `github/workflow_definition.py` — raw GitHub Actions YAML → provider IR

Source:
[`src/upgradepilot/github/workflow_definition.py`](../../../src/upgradepilot/github/workflow_definition.py)

Architecture decision:
[`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../../../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)

## Responsibility

This GitHub-owned module answers:

> What bounded GitHub Actions structure is statically declared in this exact workflow source?

It is a **provider-IR boundary**.

**IR = Intermediate Representation**: a typed representation placed between raw provider syntax and downstream domain interpretation.

The accepted dependency direction is:

```text
RepositoryTextFile.content
        ↓
PyYAML representation nodes
        ↓
UpgradePilot GitHub Actions static IR
        ↓
CI / Target / Dependency-domain consumers
```

## What PyYAML does versus what UpgradePilot does

PyYAML owns YAML grammar/parsing:

```text
MappingNode
SequenceNode
ScalarNode
```

UpgradePilot owns the bounded GitHub Actions interpretation:

```text
WorkflowDefinition
StepsJobDefinition
ReusableWorkflowJobDefinition
RunStepDefinition
UsesStepDefinition
JobProblem
StepProblem
```

Therefore this module is not “650 lines of a YAML parser from scratch.”

It contains three closely related layers:

```text
1. typed provider IR models
2. GitHub Actions structural extraction
3. private PyYAML node/safety machinery
```

## Main entry point

```python
parse_workflow_definition(source: RepositoryTextFile)
```

## Central IR hierarchy

```text
WorkflowDefinition
        ↓
JobEntry
├── StepsJobDefinition
├── ReusableWorkflowJobDefinition
└── JobProblem
        ↓
StepEntry
├── RunStepDefinition
├── UsesStepDefinition
└── StepProblem
```

## S001 transformation

Frozen S001 workflow fragment:

```yaml
docs-build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@...
    - uses: astral-sh/setup-uv@...
    - name: Install dependencies
      run: uv sync --all-packages --group docs
    - run: uv run python -c 'import docs.plugins.main'
    - run: ... uv run mkdocs build
```

becomes conceptually:

```text
WorkflowDefinition
        ↓
StepsJobDefinition(key="docs-build")
        ↓
steps[0] UsesStepDefinition(actions/checkout)
steps[1] UsesStepDefinition(astral-sh/setup-uv)
steps[2] RunStepDefinition(
    name="Install dependencies",
    command="uv sync --all-packages --group docs",
)
...
```

## Material parser flow

```text
parse_workflow_definition(...)
        ↓
workflow path admission
        ↓
_compose_workflow_yaml(...)
        ↓
PyYAML BaseLoader representation graph
        ↓
validate bounded node graph
        ↓
require workflow-root mapping
        ↓
extract material root fields
        ↓
require jobs mapping
        ↓
_parse_job(...) for each ordered job
        ↓
_parse_step(...) for each ordered step
        ↓
WorkflowDefinition
```

## Important type/model details

### `StaticScalarValue`

Preserves:

```text
text
contains_expression
source span
```

That allows downstream logic to distinguish:

```text
literal value
!=
expression-backed/dynamic value
```

without pretending to evaluate GitHub expressions.

### `source_index`

Preserves source order for jobs/steps.

It is static source provenance/order, not runtime identity.

### `SourceSpan`

Preserves line/column source location for diagnostics.

### local `JobProblem` / `StepProblem`

A malformed/unsupported local job or step does not automatically erase readable sibling structure.

That is stronger than either:

```text
one bad child → discard whole workflow
```

or:

```text
bad child → silently ignore it
```

## Important Python mechanisms

```python
isinstance(node, MappingNode)
```

Type/shape validation at the parser boundary.

```python
tuple(
    _parse_job(...)
    for ... in enumerate(...)
)
```

Ordered immutable IR construction.

```python
if (run_node is None) == (uses_node is None):
```

Requires exactly one of `run` or `uses` for the bounded step model:

```text
run present / uses absent → valid run step
run absent / uses present → valid uses step
both present → ambiguous
both absent → ambiguous
```

### `yaml.compose(..., Loader=yaml.BaseLoader)`

PyYAML builds low-level nodes without becoming UpgradePilot's domain model.

## Safety boundary

The module applies post-compose guards such as:

```text
maximum node visits
maximum nesting depth
recursive alias detection
unsupported node-kind rejection
```

A Plan-01 audit found one real non-blocking robustness gap:

```text
yaml.compose(...)
can itself encounter sufficiently pathological recursion
before UpgradePilot's post-compose depth validator runs
```

A composition-time `RecursionError` is therefore a reasonable bounded future fix/test candidate. It is not a reason to replace the architecture.

Other non-blocking audit ideas included:

```text
alias-occurrence/source-span precision
typed problem reason codes
stronger canonical workflow-path admission
```

These remain engineering observations, not Plan-01 implementation authorization.

## Direct downstream relationships

The IR is genuinely shared.

Examples:

```text
CI consumes WorkflowDefinition / StepsJobDefinition / RunStepDefinition
Target consumes the same provider IR
dependency environment-selection logic consumes RunStepDefinition
```

This validates that the abstraction is not one-caller indirection.

## Evidence state

```text
exact workflow source
→ parsed/validated bounded provider structure
→ static workflow definition evidence
```

## Does not establish

```text
workflow execution
job/step success
dependency semantics of command-line flags
selected-environment membership
runtime package installation/exercise
```

---

# 11. `dependency/workflow_context.py` — static path context shared by dependency observers

Source:
[`src/upgradepilot/dependency/workflow_context.py`](../../../src/upgradepilot/dependency/workflow_context.py)

## Responsibility

This dependency-owned helper module answers a narrower question:

> For one provider-owned `RunStepDefinition`, what static working-directory/path context can dependency observers safely use?

It prevents multiple dependency observers from independently reimplementing GitHub Actions working-directory precedence.

It deliberately does not become a full shell/runtime environment engine.

## Central type

```python
EffectiveWorkingDirectory
```

Conceptual fields:

```text
state
source
path
raw
```

States:

```text
repository_root
literal
unresolved
```

Sources:

```text
repository_root
workflow
job
step
```

## Precedence rule

```text
step working-directory
>
job default working-directory
>
workflow default working-directory
>
repository root
```

Why higher-precedence dynamic context becomes unresolved:

```text
step working-directory = dynamic expression
workflow default = "services/api"
```

The safe interpretation is not:

```text
"ignore dynamic step value and use lower workflow default"
```

because GitHub would apply the higher-precedence declaration if it resolves.

Instead:

```text
unresolved
```

## Other important helpers

### `resolve_repository_relative_path(...)`

Resolves one literal relative path against the effective working directory while keeping the result inside the repository boundary.

### `bounded_shell_segments(...)`

Splits only the bounded separators currently admitted by dependency observers:

```text
&&
||
;
newline
```

It is intentionally **not a shell AST/parser**.

Segment indices are static source-order locators, not runtime command identities.

## S001 result

Relevant project:

```text
pyproject.toml at repository root
```

Relevant install command has no material working-directory override.

Therefore:

```text
EffectiveWorkingDirectory
state = repository_root
path = None
```

The environment-selection observer also derives:

```text
project_root = None
```

so the command is safely bound to the root project.

## Does not establish

```text
filesystem existence beyond admitted evidence
actual runtime working directory
shell execution semantics
command execution/success
```

---

# 12. `dependency/environment_selection.py` — static command → typed project selector

Source:
[`src/upgradepilot/dependency/environment_selection.py`](../../../src/upgradepilot/dependency/environment_selection.py)

## Responsibility

This module answers:

> Does one static workflow run declaration visibly select the independently identified Python project, and which supported explicit extras/groups does it select?

This is **dependency/project semantics**, so it does not belong in the GitHub provider parser.

The ownership split is:

```text
github/workflow_definition.py
→ what workflow structure is declared?

dependency/environment_selection.py
→ what project-environment selection meaning does this run command carry?
```

## Main function

```python
observe_project_environment_selection(
    step: RunStepDefinition,
    *,
    project_file_path: str,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> ProjectEnvironmentSelectionObservation
```

## Central selector types

```text
OptionalExtraSelector
DependencyGroupSelector
AllOptionalExtrasSelector
AllDependencyGroupsSelector
```

Union:

```text
ProjectEnvironmentSelector
```

## Central result types

### `ProjectEnvironmentSelectionDeclaration`

One bounded command segment associated with the independently known project.

Conceptually:

```text
manager
operation
segment_index
project_root
selectors
```

### `ProjectEnvironmentSelectionObservation`

Overall static observation for one provider-owned run step:

```text
state
reason
detail
step_source_index
command
project_file_path
working_directory
declarations
```

## Three-state contract

```text
observed
→ admitted static declaration was safely interpreted

not_observed
→ source was safely inspected but no admitted project-selection declaration was present

unresolved
→ materially relevant syntax/context exists but cannot safely be interpreted at the current bounded rule
```

This is intentionally stronger than a Boolean.

```text
False
```

cannot distinguish:

```text
"not there"
```

from:

```text
"might be there but current evidence is ambiguous/dynamic"
```

## S001 control flow

Starting IR object:

```text
RunStepDefinition
command.text = "uv sync --all-packages --group docs"
```

### Step 1 — validate project file identity

```text
project_file_path = pyproject.toml
→ project root = repository root (`None` in this representation)
```

### Step 2 — resolve effective working directory

```text
step > job > workflow > repository root
→ S001 = repository root
```

### Step 3 — segment command

```python
enumerate(bounded_shell_segments(step.command.text))
```

S001 contains one relevant segment:

```text
segment_index = 0
segment = "uv sync --all-packages --group docs"
```

### Step 4 — recognize uv operation

Bounded regex admits:

```text
uv sync
uv run
```

S001 matches `uv sync`.

### Step 5 — shell-like tokenization

```python
shlex.split(segment, posix=True)
```

produces conceptually:

```python
[
    "uv",
    "sync",
    "--all-packages",
    "--group",
    "docs",
]
```

`shlex` is used because shell quoting matters; naive splitting on spaces would be less reliable.

### Step 6 — classify operation/arguments

```text
manager = uv
operation = sync
args = [--all-packages, --group, docs]
```

`--all-packages` is not treated as "all dependency groups" because uv workspace-package selection and dependency-group selection are different semantics.

### Step 7 — parse explicit selector

```text
--group docs
```

becomes:

```python
DependencyGroupSelector(
    name="docs",
    mode="include",
)
```

while:

```text
--only-group docs
```

would become:

```python
DependencyGroupSelector(
    name="docs",
    mode="only",
)
```

### Step 8 — bind command to exact project

For S001:

```text
working_directory.path = None
project_root = None
```

so the command is safely associated with the root `pyproject.toml`.

### Step 9 — construct declaration

Conceptually:

```python
ProjectEnvironmentSelectionDeclaration(
    manager="uv",
    operation="sync",
    segment_index=0,
    project_root=None,
    selectors=(
        DependencyGroupSelector("docs", mode="include"),
    ),
)
```

### Step 10 — construct observation

No unresolved details remain, and at least one declaration exists:

```text
state = observed
reason = project_environment_selection_declared
```

## Important Python mechanisms

### `Literal[...]`

Closed vocabulary for supported state/manager/operation/mode values.

### regex recognition

Used to identify the bounded command families worth deeper interpretation, not to implement a universal shell parser.

### `shlex.split(...)`

Shell-like lexical splitting that respects quoting better than plain string splitting.

### `enumerate(...)`

Preserves static segment order.

### list accumulation + `.extend(...)`

One run step may contain multiple admitted command segments/declarations.

### conditional expression

Used to distinguish `uv sync` argument handling from the more complicated `uv run` option prefix.

### `_split_option(...)`

Supports both:

```text
--group docs
--group=docs
```

### `_append_unique(...)`

Preserves selector order while avoiding exact duplicate selector values.

### `@property normalized_name`

Preserves original spelling while exposing canonical comparison identity.

For example:

```text
DependencyGroupSelector("Docs.Build").name
→ Docs.Build

normalized_name
→ docs-build
```

## Important abstention cases

### Dynamic selector

```text
uv sync --group "${{ matrix.group }}"
→ unresolved
```

Visible selector syntax is not equivalent to a known literal selector identity.

### `uv sync` without explicit selector

```text
uv sync
→ project command visible
→ selector tuple empty
→ overall unresolved
```

Why: default-group behavior requires separate project/config evidence.

### Wrong/ambiguous project root

```text
project_file_path = services/api/pyproject.toml
working-directory = services/api/tests
uv sync --group docs
→ unresolved under current bounded project-discovery rule
```

### Echoed command text

```text
echo "pip install -e .[dev]"
→ not_observed
```

A string mentioning a command is not itself a project-selection declaration.

### Positive + unsupported negative modifier

```text
uv sync --all-extras --no-extra mlx
```

can preserve the positive `AllOptionalExtrasSelector()` while the overall state remains unresolved because the negative modifier is outside the first bounded positive-selection rule.

This preserves partial truth without pretending the full environment is known.

## S001 final result

```text
ProjectEnvironmentSelectionObservation
state = observed

└── ProjectEnvironmentSelectionDeclaration
    manager = uv
    operation = sync
    project_root = repository root
    segment_index = 0

    └── DependencyGroupSelector
        name = docs
        mode = include
```

## Evidence state

```text
provider-owned static RunStepDefinition
→ dependency-owned static selection interpretation
→ OBSERVED project-environment selection declaration
```

## Does not establish

```text
docs contains/reaches Soup Sieve
uv sync executed
uv sync succeeded
Soup Sieve was installed
Soup Sieve was executed
CI dependency coverage
compatibility/safety/action
```

---

# 13. What directly calls what?

This section prevents the learning diagram from becoming a false call graph.

## Dependency-change orchestration

The approximate direct-call relationship is:

```text
analysis.py
│
├── repository client exact-file acquisition
│
├── source-specific extractor(s)
│   ├── requirements.py
│   ├── pyproject.py
│   └── uv_lock.py
│
├── change.py
│   └── compare_extracted_dependency_changes(...)
│
└── _source_contexts(...)
    └── constructs context classes defined in environment.py
```

So this portion is relatively close to a literal application/orchestration call chain.

## Workflow/provider path

The conceptual path is:

```text
RepositoryTextFile(workflow YAML)
→ parse_workflow_definition(...)
→ WorkflowDefinition / RunStepDefinition
```

Downstream consumers then use those typed provider objects.

`environment_selection.py` receives a `RunStepDefinition`; it does not need to parse YAML itself.

`workflow_context.py` is called by dependency observers to resolve static working-directory/path meaning.

## Cross-track relation

Plan 01 gives us two independently grounded facts:

```text
A. UvLockDependencyContext for normalized package soupsieve

B. ProjectEnvironmentSelectionObservation containing DependencyGroupSelector("docs")
```

The relation:

```text
"docs reaches soupsieve"
```

is **not** produced merely by placing those two objects beside each other.

It requires Plan-02 membership analysis over exact project/lock evidence.

---

# 14. Type/data transformation ladder

The most useful compact type ladder for Plan 01 is:

```text
EXTERNAL / PROVIDER EVIDENCE

GitHub API/repository response
        ↓
RepositoryTextFile

DEPENDENCY CHANGE

RepositoryTextFile(base uv.lock)
+
RepositoryTextFile(head uv.lock)
        ↓
ExtractedDependencyVersionChange
        ↓
DependencyVersionChange
        ↓
UvLockDependencyContext

STATIC WORKFLOW

RepositoryTextFile(workflow YAML)
        ↓
WorkflowDefinition
        ↓
StepsJobDefinition
        ↓
RunStepDefinition
        ↓
ProjectEnvironmentSelectionDeclaration
        ↓
ProjectEnvironmentSelectionObservation
        └── DependencyGroupSelector("docs")
```

This is a **type/evidence ladder**, not one universal function stack.

---

# 15. Evidence-state overlay on the source map

Use the learning vocabulary only where it clarifies claim strength.

```text
repository.py
ACQUIRED + provider VALIDATED exact source evidence
        ↓

uv_lock.py
INTERPRETED file-level dependency transition
        ↓

change.py
RECONCILED PR-wide dependency transition
        ↓

analysis.py / environment.py
attach typed dependency-source context
        ↓

workflow_definition.py
validated/typed static provider structure
        ↓

environment_selection.py
OBSERVED static project-environment selection declaration
```

Do not force every production object into exactly one vocabulary state. These words are a learning/claim-strength discipline, not a requirement to redesign the code around an enum.

---

# 16. Important ownership boundaries

## GitHub provider owns

```text
exact repository acquisition
GitHub Actions YAML/provider structure
workflow/job/step shape
run vs uses
source order/spans
dynamic-expression visibility
```

## Dependency domain owns

```text
what a dependency source means
canonical package/version transition
source-specific dependency context
pip/uv project selection meaning
working-directory/path context needed by dependency observers
later membership reasoning
```

## CI domain owns later

```text
workflow-level dependency consumption composition
direct changed-package invocation/exercise evidence
static CI coverage composition
runtime CI evidence/correlation at stronger stages
```

## Target domain owns separately

```text
Target-relevant environment/configuration interpretation
```

It may consume the GitHub provider IR without becoming a child of CI.

This is why the shared workflow IR belongs under `upgradepilot.github` rather than `ci`, `target`, or a generic `common` package.

---

# 17. Common source-reading mistakes to avoid

## Mistake 1 — treating the diagram as a literal call stack

Wrong:

```text
uv_lock.py directly calls change.py which directly calls workflow_definition.py...
```

Correct:

```text
some arrows are calls;
some are typed-data handoffs;
some are later evidence-composition relations.
```

## Mistake 2 — treating a class name as proof of stronger semantics

```text
UvLockDependencyContext
```

does not mean “the selected docs environment contains Soup Sieve.”

It means the canonical dependency transition came from the uv-lock source-context family.

## Mistake 3 — letting provider code become dependency-aware

`workflow_definition.py` should not decide that `--group docs` means a Python dependency-group selection.

It should preserve the `run:` command faithfully enough for the dependency owner to decide that.

## Mistake 4 — letting dependency observers reparse YAML

`environment_selection.py` should consume `RunStepDefinition`, not duplicate GitHub/YAML structure parsing.

## Mistake 5 — confusing source index with runtime identity

```text
step_source_index = 2
segment_index = 0
```

are static source/order locators.

They are not proof that runtime job instance X executed runtime command Y.

## Mistake 6 — assuming unresolved means negative

```text
unresolved
!=
not_observed
```

If a dynamic/unsupported declaration exists, the code should not collapse uncertainty into absence.

## Mistake 7 — treating implementation existence as design proof

The source is authoritative for current behavior.

It is not automatic proof that every field/helper/branch is optimal. Plan 01 deliberately audited several design choices while preserving the difference between:

```text
current behavior
rationale
engineering judgment
change authorization
```

---

# 18. Focused tests attached to this source map

These tests are not fully reproduced here; this section tells you which source responsibility each test suite protects.

## `tests/test_uv_lock_change.py`

Use to review:

```text
exact uv.lock transition extraction
provenance preservation
ambiguity/problem cases
```

## `tests/test_dependency_change.py`

Use to review:

```text
PR-wide reconciliation
one-package / one-transition consensus
problem propagation
```

## `tests/test_dependency_analysis.py`

Use to review:

```text
orchestration across source formats
DependencyChangeAnalysis construction
source-context translation
```

## `tests/test_github_workflow_definition.py`

Use to review:

```text
PyYAML representation boundary
duplicate keys
malformed YAML
recursive aliases / traversal bounds
multi-job preservation
RunStepDefinition vs UsesStepDefinition
local JobProblem / StepProblem recovery
```

## `tests/test_project_environment_selection.py`

Use to review:

```text
pip/uv selector observation
working-directory binding
literal vs dynamic selectors
observed / not_observed / unresolved
S001-style uv group recognition
```

Important precision:

The test named `test_s001_style_uv_group_and_all_extras_are_preserved` contains:

```text
uv sync --all-packages --group docs --all-extras
```

The exact historical frozen S001 command is:

```text
uv sync --all-packages --group docs
```

Therefore real S001 establishes:

```text
DependencyGroupSelector("docs")
```

without automatically adding `AllOptionalExtrasSelector()`.

The later Plan-01 mastery/review artifact will organize deferred independent test-explanation tasks. This source map only identifies where the tests belong.

---

# 19. S001 source trace in compact form

If you want to reconstruct Plan 01 quickly from source, use this trace:

```text
1. github/repository.py
   RepositoryTextFile
   exact base/head/source identity

2. dependency/uv_lock.py
   extract_uv_lock_changes(...)
   exact base/head uv.lock
   → ExtractedDependencyVersionChange

3. dependency/change.py
   compare_extracted_dependency_changes(...)
   admitted file-level results
   → DependencyVersionChange

4. dependency/analysis.py
   analyze_dependency_change(...)
   orchestration
   → DependencyChangeAnalysis
   → _source_contexts(...)

5. dependency/environment.py
   UvLockDependencyContext
   source-context family established

6. github/workflow_definition.py
   parse_workflow_definition(...)
   exact workflow YAML
   → WorkflowDefinition
   → StepsJobDefinition("docs-build")
   → RunStepDefinition("uv sync --all-packages --group docs")

7. dependency/workflow_context.py
   resolve_effective_working_directory(...)
   → repository-root working directory for S001

8. dependency/environment_selection.py
   observe_project_environment_selection(...)
   → uv sync recognized
   → --group docs parsed
   → DependencyGroupSelector("docs")
   → state="observed"
```

At this point stop.

Do **not** append this line yet:

```text
9. therefore docs contains Soup Sieve
```

That is precisely the next missing proof relation.

---

# 20. Plan-01 → Plan-02 seam

At the end of this source map we have two important typed facts:

```text
DEPENDENCY SIDE

UvLockDependencyContext
normalized_package = soupsieve
revision = exact head
source = uv.lock

WORKFLOW SELECTION SIDE

ProjectEnvironmentSelectionObservation
state = observed
selector = DependencyGroupSelector("docs")
project = root pyproject.toml
```

The next engineering question is not:

> Can we just say Soup Sieve is in docs because the historical case tells us so?

The product question is:

> What exact source logic can establish the membership relation from exact project metadata + lock graph + independently established selector?

That is the beginning of Plan 02:

```text
UvLockDependencyContext
+
exact pyproject metadata
+
DependencyGroupSelector("docs")
        ↓
uv selected-environment membership analysis
        ↓
expected real witness:

docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Only after that bridge exists can later CI composition ask whether the workflow statically consumed an environment that includes the changed dependency.

---

# 21. One-screen review table

| Source | Owner question | Main Plan-01 input | Main Plan-01 output | Proof-strength stop |
|---|---|---|---|---|
| `github/repository.py` | Can I acquire exact immutable repository text safely? | repo + SHA + path | `RepositoryTextFile` | no source semantics yet |
| `dependency/uv_lock.py` | What exact transition does this `uv.lock` evidence establish? | base/head lock evidence | `ExtractedDependencyVersionChange` | file-level interpretation only |
| `dependency/change.py` | Do admitted dependency-source interpretations agree? | extracted results/problems | `DependencyVersionChange` | PR-wide change, no env membership |
| `dependency/analysis.py` | How are source-specific results coordinated and contextualized? | identity + changed files + provider | `DependencyChangeAnalysis` | orchestration, not CI/env proof |
| `dependency/environment.py` | What dependency-source context is actually established? | reconciled change + provenance | `UvLockDependencyContext` | source context only |
| `github/workflow_definition.py` | What GitHub Actions structure is statically declared? | exact workflow YAML | `WorkflowDefinition` / `RunStepDefinition` | static structure only |
| `dependency/workflow_context.py` | What static project path context can observers safely use? | step + defaults | `EffectiveWorkingDirectory` | no runtime working dir |
| `dependency/environment_selection.py` | What project extra/group does this static command explicitly select? | `RunStepDefinition` + project path | `ProjectEnvironmentSelectionObservation` | selector declaration only |

---

# 22. Final mental model

Plan 01 teaches a disciplined architecture rather than one giant parser:

```text
ACQUIRE exact evidence
        ↓
INTERPRET each source inside its own responsibility
        ↓
RECONCILE stronger conclusions only when admitted evidence agrees
        ↓
PRESERVE typed context instead of inventing missing facts
        ↓
PARSE provider structure once at the provider boundary
        ↓
INTERPRET domain meaning in the owning domain
        ↓
STOP before the next unproven relation
```

For S001, that gives us:

```text
soupsieve 2.6 → 2.8.4
        ↓
exact uv.lock-backed canonical dependency change
        ↓
UvLockDependencyContext

AND independently:

exact docs-build workflow
        ↓
RunStepDefinition
"uv sync --all-packages --group docs"
        ↓
DependencyGroupSelector("docs")
```

The source map is complete when those two tracks are understood **without silently adding the missing membership bridge between them**.
