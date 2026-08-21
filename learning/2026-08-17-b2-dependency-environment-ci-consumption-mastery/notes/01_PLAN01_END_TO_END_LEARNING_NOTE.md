# Plan 01 — End-to-End Learning Note

**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Learning package:** `2026-08-17-b2-dependency-environment-ci-consumption-mastery`  
**Role:** polished study note for Plan 01  
**Status:** Plan-01 **content route complete**; formal ownership/reconstruction gates remain intentionally deferred  
**Related execution plan:** `../PLAN_01_S001_REAL_CASE_TO_FIRST_UPGRADEPILOT_EVIDENCE_MODELS.md`  
**Working learning history:** `../LEARNING_MEMORY.md`

---

## 1. What this note is for

This file is the main study artifact for Plan 01. It is not a transcript of the learning sessions and it is not the live project-state owner.

Its purpose is to let a future reader reconstruct the complete Plan-01 mental model from one real case:

```text
real dependency-update PR
→ understand the changed dependency
→ understand the lock/project evidence
→ understand the relevant CI workflow
→ acquire exact source evidence
→ interpret one file-level dependency transition
→ reconcile that transition across the PR
→ preserve typed dependency-source context
→ parse static GitHub Actions structure
→ interpret an explicit project-environment selector
```

The exact Plan-01 stop line is:

```text
real S001 dependency update
→ exact dependency/source evidence
→ bounded GitHub Actions workflow structure
→ static project-environment selection declaration
```

Plan 01 deliberately does **not** yet establish selected-environment membership, CI dependency consumption, runtime execution, or CI coverage. Those are stronger propositions for later plans.

---

# 2. The real case that anchors everything

S001 is a historical dependency-update case from `pydantic/pydantic`.

The changed dependency is:

```text
package: soupsieve
old version: 2.6
proposed version: 2.8.4
```

The relevant exact PR revisions preserved by the learning case are:

```text
base: 652a61ce4f9d7d76eaada31535807a485ece0e21
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
```

The important dependency path is documentation/tooling-related rather than Pydantic's normal runtime dependency path:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Another historical environment path also exists through `docs-upload`, but Plan 01 mainly follows the `docs` path because the preserved workflow contains an explicit docs-group synchronization command.

The first critical precision is therefore:

```text
Soup Sieve is a dependency reachable by Pydantic repository tooling
!=
Soup Sieve is a normal core Pydantic runtime dependency
```

This distinction matters throughout UpgradePilot because repository dependency relevance must not be confused with library-runtime ownership.

---

# 3. Chunk 1 — Soup Sieve, Beautiful Soup, direct and transitive dependency

## 3.1 Soup Sieve

Soup Sieve is a Python CSS-selector engine used with Beautiful Soup.

At the depth needed for this route:

```text
HTML/XML document
→ parsed by Beautiful Soup
→ elements can be queried with CSS-selector syntax
→ Soup Sieve provides selector-matching behavior
```

A CSS selector is a compact way to describe which document elements should be matched, for example by tag, class, id, ancestry, and related structural conditions.

We do not need Soup Sieve internals here. What matters is why it can appear in a Pydantic dependency update.

## 3.2 Direct versus transitive dependency

A **direct dependency** is declared directly by the project/environment under inspection.

A **transitive dependency** is reached through another dependency.

The S001 relationship is approximately:

```text
Pydantic docs group
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

So Soup Sieve is transitive on this path.

Important rule:

```text
transitive
!=
irrelevant
```

A transitive package can still be material to a dependency-update investigation if the selected environment reaches it.

But at this early point we only know the relationship conceptually from preserved case evidence. We have not yet proved that a particular workflow selects an environment that reaches Soup Sieve.

---

# 4. Chunk 2 — `uv`, dependency resolution, and `uv.lock`

## 4.1 What `uv` is at the needed depth

`uv` is a Python project/package management tool. For this route, the useful model is:

```text
project dependency declarations
→ dependency resolver
→ resolved package/version graph
→ uv.lock
→ uv sync / uv run
```

A **dependency resolver** determines a consistent set of package versions satisfying declared requirements and dependency relationships.

A **lockfile** records a resolved dependency state so later environments can reproduce the chosen resolution more deterministically than re-solving everything from scratch.

## 4.2 `uv.lock` is not an installed-environment inventory

One of the most important Plan-01 corrections is:

```text
package appears in uv.lock
!=
package is installed in every project environment
```

The lock can preserve packages needed by different:

```text
dependency groups
optional extras
workspace packages
dependency paths
platform/marker conditions
```

Therefore finding:

```text
soupsieve 2.8.4
```

inside the head `uv.lock` establishes useful resolved-dependency evidence, but does **not** by itself establish that the particular environment selected by docs CI contains or installs Soup Sieve.

This gives us the first major proof boundary:

```text
LOCK PRESENCE
!=
SELECTED-ENVIRONMENT MEMBERSHIP
```

## 4.3 The future membership question

Later, Plan 02 must connect:

```text
selected root/group: docs
+
exact project metadata
+
exact lock dependency graph
```

to the witness:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Plan 01 does not perform that proof yet.

---

# 5. Chunk 3 — CI, GitHub Actions, and Pydantic docs CI

## 5.1 CI

**CI = Continuous Integration.**

At the practical depth needed here, CI is automated repository checking/building/testing against a particular code revision.

Examples of CI work include:

```text
install dependencies
run tests
build documentation
lint code
build packages
perform platform-specific checks
```

CI is a mechanism, not a guarantee of compatibility. The exact claim strength depends on what was configured, what actually ran, what succeeded, and what can be correlated to the dependency under investigation.

## 5.2 GitHub Actions structure

The useful static hierarchy is:

```text
workflow
→ jobs
→ steps
```

Two important step forms are:

```yaml
- run: some shell command
```

and:

```yaml
- uses: owner/action@revision
  with:
    input: value
```

`run:` is a direct shell-command declaration.

`uses:` invokes a packaged GitHub Action. `with:` supplies inputs to that Action.

The two forms must not be treated as interchangeable.

## 5.3 Real S001 `docs-build`

The frozen S001 workflow fragment contains:

```yaml
docs-build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@<pinned SHA>
    - uses: astral-sh/setup-uv@<pinned SHA>
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: uv sync --all-packages --group docs
    - run: uv run python -c 'import docs.plugins.main'
    - run: PYTHONPATH="$PWD${PYTHONPATH:+:${PYTHONPATH}}" uv run mkdocs build
```

The important dependency-selection declaration is:

```bash
uv sync --all-packages --group docs
```

The workflow is configured to:

```text
check out the repository
→ prepare uv/Python
→ synchronize a project environment including group docs
→ import docs-related code
→ run an MkDocs build
```

But reading this YAML only gives **static definition evidence**.

Critical boundary:

```text
workflow definition
!=
runtime execution
!=
runtime success
```

So the correct wording is:

> The workflow is statically configured to synchronize the docs group and invoke an MkDocs build.

It would be too strong to say merely from the YAML:

> The docs group was successfully synchronized and Soup Sieve executed.

---

# 6. Evidence-state vocabulary used in this learning route

To avoid vague language such as “UpgradePilot knows,” we use a learning/evidence vocabulary.

These labels are explanatory language, not a requirement that production code contain enums/classes with these names.

```text
0. OBSERVED
Information has been seen from an external/upstream source.

1. ACQUIRED
The required artifact has been successfully retrieved.

2. VALIDATED
The artifact passed the identity/structure/integrity checks required by the current responsibility.

3. INTERPRETED
Validated evidence has been transformed into bounded domain meaning.

4. RECONCILED
Multiple admitted interpretations/evidence items have been checked for agreement or explicit conflict.

5. CONTEXTUALIZED
Established meaning has been connected to a larger source/project/environment/workflow context.

6. EXERCISED
Runtime evidence establishes execution/consumption at the exact strength claimed.

7. EVALUATED
Accumulated evidence has been assessed against a higher-level product/investigation question.
```

Never silently promote evidence:

```text
OBSERVED != VALIDATED
ACQUIRED != VALIDATED
VALIDATED != INTERPRETED
INTERPRETED != RECONCILED
STATIC CONTEXT != EXERCISED RUNTIME PATH
```

This vocabulary becomes particularly useful in Chunk 4.

---

# 7. Chunk 4 — exact dependency transition and typed source context

Chunk 4 follows the source path:

```text
github/repository.py
→ dependency/uv_lock.py
→ dependency/change.py
→ dependency/analysis.py
→ dependency/environment.py
```

Its job is to establish:

```text
what dependency changed?
+
which exact dependency source established that fact?
```

It still does not establish selected-environment membership or runtime behavior.

---

## 7.1 `github/repository.py` — acquire exact repository evidence

Important type:

```python
RepositoryTextFile
```

Important acquisition responsibilities include obtaining exact repository files at immutable revisions, such as the pull-request base and head.

For S001:

```text
base uv.lock
@ base commit SHA

head uv.lock
@ head commit SHA
```

### Important provenance concepts

A runtime-acquired repository text file can preserve information such as:

```text
repository
path
revision
blob SHA
returned path
reported byte count
decoded byte count
retrieval time
content
```

These fields do not all serve the same role.

Useful mental model:

```text
repository + path + immutable revision
→ identifies which exact repository file was requested

blob SHA
→ Git/GitHub content-object provenance handle

reported byte count vs decoded byte count
→ acquisition consistency / defensive transport check

size limit
→ bounded resource-safety contract
```

Important engineering lesson:

```text
more metadata
!=
automatically stronger evidence
```

A provenance field should be justified by the identity, ambiguity, integrity, consistency, or resource-bound failure mode it protects.

Also, do not overstate the blob SHA. The provider preserves/validates the returned blob identifier but does not at this boundary independently recompute the Git blob hash from decoded bytes.

### Evidence state

At this stage the repository provider is primarily responsible for:

```text
ACQUIRING
+
VALIDATING
```

exact source evidence.

---

## 7.2 `dependency/uv_lock.py` — interpret exact lockfile changes

Primary function:

```python
extract_uv_lock_changes(...)
```

High-level flow:

```text
changed-file record
+
exact base/head uv.lock evidence
        ↓
repository-relative basename/path admission
        ↓
modified-status admission
        ↓
base/head availability checks
        ↓
source-evidence construction
        ↓
independent base/head TOML parsing
        ↓
package-record validation
        ↓
normalized package grouping
        ↓
base/head comparison
        ↓
require exactly one supported transition
        ↓
ExtractedDependencyVersionChange
```

For S001:

```text
base soupsieve = 2.6
head soupsieve = 2.8.4
```

becomes one file-level interpreted transition.

### Important output type

```python
ExtractedDependencyVersionChange
```

Conceptually:

```text
one source-specific file-level interpretation
+
exact source provenance
```

This is **not** PR-wide canonical truth yet.

### Important Python mechanisms learned here

Only syntax carrying the mechanism matters.

#### `parts[-1]`

Negative indexing:

```python
parts[-1]
```

means the final path component, i.e. basename.

So a supported path can be:

```text
uv.lock
backend/uv.lock
some/subdir/uv.lock
```

provided the repository-relative path is otherwise admitted.

It does not mean only root `uv.lock` is accepted.

#### Guard clauses / early returns

The function repeatedly rejects unsupported states early rather than allowing unsafe assumptions to propagate.

Pattern:

```python
if unsupported_condition:
    return DependencyChangeProblem(...)
```

This keeps the successful path trustworthy and localizes expected abstention.

#### `isinstance(...)` + assertion after guard

Union-typed evidence may first be checked with `isinstance(...)`. After a guard proves which variant remains, an assertion can document an internal invariant for the type checker and future maintainer.

The assertion is not evidence validation by itself; the earlier control flow established the state.

#### `_MISSING` sentinel and identity checks

A sentinel object distinguishes:

```text
field genuinely absent
```

from legitimate values that may otherwise resemble an empty/default value.

Identity comparison:

```python
value is _MISSING
```

asks whether this is the exact sentinel object.

#### `defaultdict`, sets, `Counter`, tuples

These support grouping/comparison while preserving bounded deterministic semantics:

```text
package records
→ group by normalized identity
→ compare canonicalized groups
→ detect one exact transition
```

### Proof boundary

`uv_lock.py` can establish:

```text
INTERPRETED file-level transition:
soupsieve 2.6 → 2.8.4
```

It does **not** establish:

```text
direct/transitive membership
selected dependency group
CI consumption
runtime installation
runtime exercise
compatibility
safety
```

---

## 7.3 `dependency/change.py` — reconcile file-level meanings across the PR

`change.py` is a source-independent reconciliation boundary.

Important types:

```text
DependencyChangeSourceEvidence
→ provenance for one admitted dependency source

ExtractedDependencyVersionChange
→ one source-specific interpreted transition

DependencyChangeProblem
→ explicit problem/abstention state

DependencyVersionChange
→ canonical PR-wide reconciled transition
```

Primary function:

```python
compare_extracted_dependency_changes(...)
```

### Reconciliation algorithm

```text
collect unique source evidence
        ↓
if any admitted DependencyChangeProblem exists
→ stop with that problem
        ↓
require at least one successful extraction
        ↓
collect normalized package identities
        ↓
require exactly one normalized package
        ↓
collect exact (old_version, proposed_version) pairs
        ↓
require exactly one exact transition pair
        ↓
promote to DependencyVersionChange
```

For S001:

```text
file-level interpretation:
soupsieve 2.6 → 2.8.4
        ↓
reconciliation succeeds
        ↓
DependencyVersionChange(
    normalized_package="soupsieve",
    old_version="2.6",
    proposed_version="2.8.4",
    ...
)
```

### Why a problem blocks reconciliation

A stronger canonical result should not silently ignore malformed or unsupported **admitted** evidence from another source.

Bad rule:

```text
one successful extraction
+
one admitted source problem
→ ignore problem and claim consensus
```

Current safer rule:

```text
material admitted problem
→ do not promote to trusted PR-wide DependencyVersionChange
```

### Important Python mechanisms

Useful constructs include:

```text
Sequence[...]
generator expressions
next(..., None)
isinstance(...)
tuple materialization
set comprehensions
len(set) == 1 consensus checks
(old_version, proposed_version) tuple pairs
tuple unpacking
sorted(...) for deterministic diagnostics
!r in formatted diagnostics
list accumulation/deduplication
immutable tuple output
```

### Evidence state

```text
uv_lock.py
INTERPRETED file-level transition
        ↓
change.py
RECONCILED PR-wide canonical transition
```

### Bounded product limitation

Current reconciliation supports one canonical dependency transition per investigated PR slice.

That is a bounded product contract, not a universal claim that real pull requests cannot update multiple dependencies.

---

## 7.4 `dependency/analysis.py` — orchestration, not deep uv analysis

This was an important correction during the learning journey.

`analysis.py` does not contain the deep source-specific `uv.lock` comparison algorithm.

Its responsibility is primarily:

```text
orchestration
+
integration
+
typed source-context construction
```

Primary result type:

```python
@dataclass(frozen=True, slots=True)
class DependencyChangeAnalysis:
    dependency: DependencyVersionChange
    source_contexts: tuple[DependencySourceContext, ...]
```

Mental model:

```text
dependency
→ WHAT changed canonically?

source_contexts
→ WHAT KIND OF exact dependency source established that fact?
```

For S001:

```text
dependency:
soupsieve 2.6 → 2.8.4

source_contexts:
UvLockDependencyContext(...)
```

### `analyze_dependency_change(...)`

The function coordinates source-specific owners:

```text
for each changed file
→ route supported requirements files to requirements extractor
→ route pyproject.toml to pyproject optional-extra extractor
→ route uv.lock to uv-lock extractor
→ collect source-specific results
→ call compare_extracted_dependency_changes(...)
→ if reconciliation fails, return the problem
→ otherwise build DependencyChangeAnalysis
```

Best ownership summary:

```text
repository.py
"give me the exact evidence"

uv_lock.py
"what does this exact uv.lock evidence mean?"

change.py
"do all admitted dependency-change meanings agree?"

analysis.py
"coordinate the owners and package the trusted result"
```

### Neutral pyproject edit

A `pyproject.toml` file can change for reasons unrelated to dependency extras. A pyproject extraction result explicitly representing “no relevant optional-extra change” is treated as neutral rather than automatically blocking another valid dependency source.

This is different from a malformed/unsupported admitted dependency problem.

### Source-specific side context

For pyproject optional-extra evidence, `analysis.py` temporarily preserves a mapping from exact source evidence to the extra name so generic reconciliation can remain source-independent while later context construction can restore the source-specific meaning.

This is a layering tradeoff, not an accidental dictionary.

---

## 7.5 `_source_contexts(...)` — generic provenance to typed source context

After `change.py` has produced a trusted `DependencyVersionChange`, `_source_contexts(...)` translates its provenance into source-specific context types.

Simplified shape:

```python
common = {
    "repository": identity.repository,
    "revision": identity.head_sha,
    "normalized_package": dependency.normalized_package,
    "source_evidence": evidence,
}
```

Then, for uv-lock evidence:

```python
UvLockDependencyContext(**common)
```

### `**common`

Dictionary unpacking into keyword arguments:

```python
UvLockDependencyContext(**common)
```

is approximately equivalent to:

```python
UvLockDependencyContext(
    repository=...,
    revision=...,
    normalized_package=...,
    source_evidence=...,
)
```

This syntax removes repeated constructor spelling; it does not change evidence semantics.

### Why head revision?

The produced source context describes the proposed PR state, so it uses the exact head revision. The source evidence itself still preserves the base/head provenance used to establish the transition.

### Internal invariant versus external evidence problem

If trusted pyproject optional-extra evidence reaches `_source_contexts(...)` but the extra name that `analysis.py` was responsible for preserving has disappeared, the code raises an internal `RuntimeError`.

That is different from a normal `DependencyChangeProblem`:

```text
external repository ambiguity/unsupported evidence
→ typed domain problem

internally impossible state after earlier program promises
→ programming invariant failure
```

---

## 7.6 `dependency/environment.py` — `UvLockDependencyContext`

Important S001 type:

```python
@dataclass(frozen=True, slots=True)
class UvLockDependencyContext:
    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence
```

Conceptual S001 instance:

```text
repository: pydantic/pydantic
revision: exact PR head
normalized_package: soupsieve
source_evidence: exact uv.lock provenance
```

Its meaning is narrow:

> The canonical dependency transition was established from exact `uv.lock` source evidence for this repository/head/package identity.

It does **not** mean:

```text
Soup Sieve belongs to docs
Soup Sieve belongs to every uv group
CI selected docs
CI installed Soup Sieve
Soup Sieve executed
```

Critical distinction:

```text
TYPED SOURCE CONTEXT
!=
SELECTED ENVIRONMENT CONTEXT
```

So a careful evidence-state description is:

```text
DependencyVersionChange
→ RECONCILED transition

analysis.py + environment.py
→ source-contextualized provenance
```

Selected-environment contextualization requires independent workflow/project evidence.

---

# 8. Chunk 4 end-to-end path

By the end of Chunk 4 we can explain:

```text
exact base/head uv.lock files
        ↓
RepositoryTextFile
ACQUIRED + VALIDATED
        ↓
uv_lock.py
INTERPRETED file-level transition
        ↓
ExtractedDependencyVersionChange
        ↓
change.py
RECONCILED PR-wide transition
        ↓
DependencyVersionChange
        ↓
analysis.py
orchestration + source-context translation
        ↓
environment.py
UvLockDependencyContext
```

Result:

```text
WHAT CHANGED?
soupsieve 2.6 → 2.8.4

WHERE DID THE DEPENDENCY FACT COME FROM?
exact uv.lock evidence
```

Still missing:

```text
WHICH PROJECT ENVIRONMENT DOES THE WORKFLOW SELECT?
```

That is Chunk 5.

---

# 9. Chunk 5 — bounded GitHub Actions IR and project-environment selection

Chunk 5 follows:

```text
github/workflow_definition.py
→ dependency/workflow_context.py
→ dependency/environment_selection.py
```

This crosses an important ownership boundary:

```text
GitHub provider owns workflow structure
Dependency owns project/dependency selection semantics
```

---

## 9.1 Why `workflow_definition.py` exists

The source is large, but it is **not** implementing YAML parsing from scratch.

It uses PyYAML:

```python
import yaml
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode
```

Selected pipeline:

```text
raw GitHub Actions YAML
        ↓
PyYAML YAML parser
        ↓
MappingNode / SequenceNode / ScalarNode
        ↓
UpgradePilot bounded GitHub Actions structural interpretation
        ↓
typed provider IR
```

**IR = Intermediate Representation.**

Here it means a typed model sitting between raw provider syntax and downstream domain interpretation.

Why not just expose dictionaries or PyYAML nodes?

Because downstream CI/Target/Dependency code should reason in provider-domain terms such as:

```text
WorkflowDefinition
StepsJobDefinition
RunStepDefinition
UsesStepDefinition
```

not in parser-library terms.

---

## 9.2 Important workflow IR types

Simplified hierarchy:

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

For S001, the important structure is approximately:

```text
WorkflowDefinition
└── StepsJobDefinition(key="docs-build")
    ├── UsesStepDefinition(actions/checkout@...)
    ├── UsesStepDefinition(astral-sh/setup-uv@...)
    ├── RunStepDefinition(
    │     source_index=2,
    │     name="Install dependencies",
    │     command="uv sync --all-packages --group docs"
    │  )
    ├── RunStepDefinition(... import docs.plugins.main ...)
    └── RunStepDefinition(... uv run mkdocs build ...)
```

`source_index` preserves static source ordering/location. It must not be confused with runtime step identity.

---

## 9.3 `parse_workflow_definition(...)`

High-level path:

```text
RepositoryTextFile
        ↓
verify .github/workflows/*.yml|yaml path
        ↓
compose YAML with PyYAML
        ↓
require workflow-root mapping
        ↓
extract jobs mapping
        ↓
parse each job
        ↓
parse each step
        ↓
WorkflowDefinition
```

The parser is intentionally bounded. It does not implement the entire GitHub Actions platform.

It preserves readable structure and emits typed local problems where useful instead of either silently ignoring ambiguity or destroying every readable sibling.

Examples:

```text
bad whole workflow
→ WorkflowDefinitionProblem

one bad job
→ JobProblem while readable sibling jobs survive

one bad step
→ StepProblem while readable sibling steps survive
```

This is strong evidence-preservation behavior.

---

## 9.4 `run` versus `uses`

A bounded step must declare exactly one of `run` or `uses`.

The implementation effectively rejects both invalid shapes:

```text
run + uses together
→ ambiguous

neither run nor uses
→ ambiguous for current bounded step model
```

Then it constructs either:

```python
RunStepDefinition(...)
```

or:

```python
UsesStepDefinition(...)
```

For our S001 dependency-selection path, the important output is the `RunStepDefinition` whose command text is:

```bash
uv sync --all-packages --group docs
```

---

## 9.5 Workflow parser engineering audit summary

The architecture was audited rather than accepted merely because it exists.

### Strong decisions

```text
PyYAML instead of home-grown YAML grammar
provider-owned typed IR
shared CI + Target consumer boundary
static definition separated from runtime Actions evidence
local JobProblem / StepProblem preservation
duplicate material-key detection
source spans
bounded traversal/depth logic
```

### One real robustness gap found

Current order is approximately:

```text
yaml.compose(...)
        ↓
_validate_composed_node_graph(...)
```

The custom depth/node guard runs **after** PyYAML composition. Pathologically deep YAML can therefore trigger a Python `RecursionError` during `yaml.compose(...)` before UpgradePilot's post-compose guard runs.

That is a real bounded hardening gap, but not a reason to rewrite the architecture. The likely proportional fix is to normalize composition-time recursion failure into the controlled parser-problem boundary and add a regression test.

### Smaller future audit ideas

```text
anchor/alias occurrence-span precision
closed/typed problem reason codes
canonical repository-path validation for workflow paths
```

These are improvement candidates, not Plan-01 blockers.

---

# 10. `dependency/workflow_context.py` — effective working-directory context

A project-selection command only has useful meaning if it can be bound to the correct project.

The static working-directory precedence is:

```text
step working-directory
>
job defaults.run.working-directory
>
workflow defaults.run.working-directory
>
repository root
```

If a higher-precedence declaration is dynamic/unresolvable, the code must not fall through and pretend a lower-precedence directory applies.

For S001:

```text
root project file: pyproject.toml
project root: repository root
relevant step working directory: repository root
```

So the static `uv` command can be safely bound to the root Pydantic project.

Important boundary:

```text
static effective working-directory interpretation
!=
runtime filesystem/execution proof
```

---

# 11. `dependency/environment_selection.py` — interpret explicit project selectors

Primary function:

```python
observe_project_environment_selection(...)
```

Its input includes:

```text
one provider-owned RunStepDefinition
+
independently established pyproject.toml path
+
workflow/job run defaults where relevant
```

Its output is:

```python
ProjectEnvironmentSelectionObservation
```

The observer supports a bounded set of explicit project-selection patterns, including local-project pip installs and selected `uv sync` / `uv run` extra/group flags.

Its module-level proof boundary is explicit:

```text
visible static selector
!= command execution
!= environment formation
!= lock-member reachability
!= changed-package exercise
```

---

## 11.1 Bind to the independently known project

For S001:

```text
project_file_path = "pyproject.toml"
```

Repository-relative path validation produces:

```text
project root = repository root
```

The effective working directory is also repository root.

So:

```text
command project root == independently established project root
```

This prevents the unsafe shortcut:

```text
saw "--group docs" somewhere
→ assume it belongs to whichever project we are investigating
```

---

## 11.2 Bounded shell segmentation

The run command is split only across currently admitted static separators such as:

```text
&&
||
;
newline
```

This is intentionally **not** a complete shell Abstract Syntax Tree (AST).

For S001:

```bash
uv sync --all-packages --group docs
```

contains one segment:

```text
segment_index = 0
```

The segment index preserves static ordering only.

---

## 11.3 Recognize `uv sync`

A bounded regular expression recognizes commands shaped like:

```text
uv sync ...
uv run ...
```

For S001:

```text
manager = uv
operation = sync
```

The code intentionally does not interpret arbitrary `uv` subcommands as project-environment selection.

---

## 11.4 `shlex` tokenization

The command is tokenized with Python's `shlex` rather than naïve whitespace splitting.

For:

```bash
uv sync --all-packages --group docs
```

we obtain approximately:

```python
[
    "uv",
    "sync",
    "--all-packages",
    "--group",
    "docs",
]
```

`shlex` matters because shell-like quoting can preserve spaces inside one logical argument.

We only need shell tokenization at this bounded operational depth; full shell interpretation is deliberately deferred.

---

## 11.5 Why `uv sync` and `uv run` differ

For `uv sync`, the remaining arguments are all uv-sync arguments.

For `uv run`, eventually arguments belong to the child command being executed. The parser therefore has bounded logic to stop interpreting child-command options as if they were uv selector options.

This prevents a command such as:

```bash
uv run pytest --group application-argument
```

from being blindly treated as selecting uv dependency group `application-argument`.

---

## 11.6 Parse `--group docs`

The selector parser supports both styles:

```bash
--group docs
```

and:

```bash
--group=docs
```

For S001:

```text
option = --group
value = docs
```

The value is checked for dynamic GitHub expression syntax and bounded literal-name validity.

A dynamic selector such as:

```yaml
uv sync --group "${{ matrix.group }}"
```

must not be promoted into a literal group identity.

For literal `docs`, the parser constructs:

```python
DependencyGroupSelector(
    name="docs",
    mode="include",
)
```

`--only-group docs` would instead preserve:

```python
mode="only"
```

This matters because source spelling and selection semantics should not be flattened.

---

## 11.7 `--all-packages` is not `--all-groups`

The real command includes:

```bash
--all-packages
```

This does **not** become an `AllDependencyGroupsSelector`.

`--all-packages` concerns workspace-package behavior; it does not semantically mean “include every dependency group.”

The observer only turns supported positive dependency-environment selectors into selector objects.

This is a good example of precise command semantics preventing keyword-driven overinterpretation.

---

## 11.8 Final S001 declaration

The core static declaration is conceptually:

```python
ProjectEnvironmentSelectionDeclaration(
    manager="uv",
    operation="sync",
    segment_index=0,
    project_root=None,  # repository root
    selectors=(
        DependencyGroupSelector(
            name="docs",
            mode="include",
        ),
    ),
)
```

The outer observation becomes:

```python
ProjectEnvironmentSelectionObservation(
    state="observed",
    ...,
    declarations=(declaration,),
)
```

The exact S001 proposition is:

> The static Pydantic workflow visibly declares `uv sync` for the repository-root Python project with dependency group `docs` explicitly included.

---

# 12. `observed` vs `not_observed` vs `unresolved`

A Boolean would be too weak because “no” and “cannot safely determine” are different evidence states.

The observer therefore uses:

```text
observed
not_observed
unresolved
```

## 12.1 `observed`

Meaning:

> An admitted static declaration was found and interpreted safely.

Real S001:

```bash
uv sync --all-packages --group docs
```

→ `DependencyGroupSelector("docs")`

→ `state="observed"`

## 12.2 `not_observed`

Meaning:

> The static command was inspectable but contained no admitted project-selection declaration.

Example:

```bash
echo "pip install -e .[dev]"
```

The text mentions a pip command, but the actual command is `echo`.

Correct result:

```text
not_observed
```

not a false installation declaration.

## 12.3 `unresolved`

Meaning:

> Material project-selection structure is present, but current bounded evidence is insufficient to interpret it safely.

Examples:

### Dynamic group

```bash
uv sync --group "${{ matrix.group }}"
```

The observer knows a group selector exists but does not know the literal selected group.

### `uv sync` with no explicit selector

```bash
uv sync
```

The command is bound to a project, but default-group selection can depend on separate project/config evidence. The workflow command alone is insufficient to state the exact complete environment.

### Wrong/uncertain project-discovery context

If a command starts from a location that does not safely bind to the independently established project root, the observer must not guess uv's parent/nested project-discovery behavior.

### Positive + unresolved modifier

A command may preserve a positive selector while still receiving overall `unresolved` state if another material unsupported modifier changes the complete interpretation.

This is a valuable evidence pattern:

```text
preserve established partial fact
+
preserve unresolved material ambiguity
```

rather than either erasing the positive fact or overstating total understanding.

---

# 13. Representative selector test and its proof boundary

A focused test uses an S001-style command:

```bash
uv sync --all-packages --group docs --all-extras
```

and asserts approximately:

```text
state = observed
manager = uv
operation = sync
selectors include DependencyGroupSelector("docs")
selectors include AllOptionalExtrasSelector()
```

Important precision:

The exact frozen S001 command is:

```bash
uv sync --all-packages --group docs
```

It does **not** contain `--all-extras`.

Therefore the real S001 selector result relevant to this note is specifically:

```python
DependencyGroupSelector("docs")
```

not `AllOptionalExtrasSelector()`.

### What the focused test protects

It protects the invariant:

> Explicit supported uv environment selectors in a statically project-bound run declaration are preserved as typed project-environment-selection evidence.

### What it does not prove

The test does not prove:

```text
command execution
uv synchronization success
selected-group membership for Soup Sieve
package installation
CI success
package exercise
compatibility
safety
```

---

# 14. Full Plan-01 data/evidence flow

The complete learning route is now:

```text
S001 real dependency-update case
soupsieve 2.6 → 2.8.4
        ↓
understand repository dependency path
        ↓
understand uv + universal lockfile semantics
        ↓
understand Pydantic docs-build workflow
        ↓
exact base/head repository evidence
        ↓
repository.py
ACQUIRED + VALIDATED
        ↓
uv_lock.py
INTERPRETED file-level dependency transition
        ↓
ExtractedDependencyVersionChange
        ↓
change.py
RECONCILED PR-wide dependency transition
        ↓
DependencyVersionChange
        ↓
analysis.py
ORCHESTRATION + typed provenance translation
        ↓
environment.py
UvLockDependencyContext
        ↓
workflow_definition.py
bounded GitHub Actions static IR
        ↓
StepsJobDefinition("docs-build")
        ↓
RunStepDefinition(
  "uv sync --all-packages --group docs"
)
        ↓
workflow_context.py
static project-root binding
        ↓
environment_selection.py
interpret explicit selector
        ↓
DependencyGroupSelector(
  name="docs",
  mode="include"
)
        ↓
ProjectEnvironmentSelectionObservation(
  state="observed"
)
```

---

# 15. What Plan 01 establishes

By the end of the Plan-01 content route we can establish and explain these separate propositions:

## Proposition A — dependency transition

```text
soupsieve 2.6 → 2.8.4
```

is the reconciled dependency transition admitted from exact source evidence.

## Proposition B — dependency source context

The transition was established from exact `uv.lock` evidence at the proposed PR state.

## Proposition C — static workflow structure

The exact static `docs-build` workflow contains a `RunStepDefinition` whose command is:

```bash
uv sync --all-packages --group docs
```

## Proposition D — static project-environment selection

That command is statically bound to the root Pydantic project and explicitly includes dependency group:

```text
docs
```

represented as:

```python
DependencyGroupSelector("docs")
```

---

# 16. What Plan 01 deliberately does NOT establish

This section is as important as the positive result.

Plan 01 does **not** prove:

```text
DependencyGroupSelector("docs")
→ soupsieve is a member of docs
```

It also does not prove:

```text
workflow definition
→ command executed

command declaration
→ uv sync succeeded

uv.lock contains soupsieve
→ docs reaches soupsieve

successful CI
→ exact soupsieve version was installed

package installation
→ package was directly exercised

package exercise
→ behavioral compatibility

compatibility evidence
→ safety/action recommendation
```

Compact proof ladder:

```text
dependency transition
!= environment membership
!= static environment selection
!= static dependency consumption
!= runtime execution/success
!= exact-version runtime witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

Plan 01 reaches the **static environment-selection** stage. Later plans continue the ladder.

---

# 17. The critical missing bridge into Plan 02

At Plan-01 completion we possess two independently established facts:

```text
FACT A
changed dependency:
soupsieve 2.6 → 2.8.4
source context:
uv.lock
```

and:

```text
FACT B
static workflow selection:
DependencyGroupSelector("docs")
```

We still need to establish the relationship:

```text
docs
→ ...
→ soupsieve
```

That is not a trivial join. It requires exact project/lock membership reasoning.

Plan 02 therefore asks:

> Given the independently observed `docs` selector, does the exact selected project environment actually reach the changed package in the exact project/lock dependency graph?

For S001 the expected witness is:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Only after establishing that relation can later CI-consumption logic connect static environment selection to the changed dependency.

---

# 18. Source ownership map to retain

This compact responsibility map is worth memorizing conceptually:

```text
src/upgradepilot/github/repository.py
→ acquire exact immutable repository evidence

src/upgradepilot/dependency/uv_lock.py
→ interpret exact uv.lock transition semantics

src/upgradepilot/dependency/change.py
→ reconcile admitted dependency-transition meanings across the PR

src/upgradepilot/dependency/analysis.py
→ coordinate source-specific extraction/reconciliation and construct analysis result

src/upgradepilot/dependency/environment.py
→ preserve typed dependency-source contexts

src/upgradepilot/github/workflow_definition.py
→ translate static GitHub Actions YAML structure into provider-owned typed IR

src/upgradepilot/dependency/workflow_context.py
→ resolve bounded static working-directory/path context for dependency observers

src/upgradepilot/dependency/environment_selection.py
→ interpret explicit static Python project-environment selectors
```

The key architectural rule is:

```text
provider syntax owner
!=
domain meaning owner
```

For example:

```text
GitHub owns RunStepDefinition
Dependency owns what --group docs means
```

---

# 19. Important Python concepts from Plan 01

These are the Python mechanisms that materially carried the behavior. They are not a general Python syllabus.

## Typed dataclasses

```python
@dataclass(frozen=True, slots=True)
```

Used heavily for evidence/domain value objects.

Operational meaning:

```text
@dataclass
→ generated data-oriented constructor/equality/repr behavior

frozen=True
→ intended immutable value object after construction

slots=True
→ fixed declared attributes / reduced accidental dynamic attribute surface
```

The design benefit is not merely memory optimization; immutable typed evidence is easier to reason about than freely mutated dictionaries.

## Union types

```python
A | B
str | None
```

Used to make result/evidence states explicit.

Example mental model:

```text
successful domain result
OR
explicit problem result
```

rather than exception-driven control flow for every expected evidence limitation.

## `isinstance(...)`

Used for runtime narrowing across unions:

```python
if isinstance(result, DependencyChangeProblem):
    return result
```

This makes typed problem propagation explicit.

## Early returns

Expected unsupported/ambiguous states exit early rather than allowing unsafe downstream assumptions.

## Comprehensions and sets

Useful for normalized consensus checks such as:

```text
how many distinct normalized packages?
how many distinct exact version-transition pairs?
```

## Tuples

Used for immutable returned collections and exact pair representation.

## `enumerate(...)`

Preserves static source indices while iterating jobs, steps, or command segments.

## `**mapping`

Unpacks a dictionary into keyword arguments for repeated constructor fields.

## Regular expressions

Used only for bounded command-shape recognition, not full shell parsing.

## `shlex`

Used for shell-like tokenization with quoting awareness.

Important limit:

```text
shlex tokenization
!=
full shell semantics
```

---

# 20. Engineering-design lessons from Plan 01

The learning route also produced several reusable engineering judgments.

## 20.1 Implementation truth is not automatic design truth

Current source/tests tell us what the implementation does. They do not prove every design decision is optimal.

When evaluating code, ask:

```text
what responsibility does this abstraction own?
what failure mode does this validation protect?
what ambiguity is this metadata resolving?
what coupling would appear if this helper/type disappeared?
```

Do not refactor merely because a file is large or because helper functions exist.

## 20.2 Helpers should earn navigation cost

A helper is justified when it meaningfully isolates:

```text
responsibility
transformation
complexity
invariant
reused behavior
or a valuable semantic name
```

The `uv_lock.py` helper audit found no reason to refactor solely from helper count.

## 20.3 Shared IR is justified when multiple consumers need the same provider structure

`workflow_definition.py` is shared by CI and Target. It avoids duplicated GitHub/YAML parsing while keeping domain conclusions outside the provider layer.

That is a real abstraction seam, not speculative generalization.

## 20.4 Static evidence strength must stay static

A major architectural correction in UpgradePilot is preserving:

```text
static declaration
!= runtime execution
!= runtime success
```

This rule should remain visible whenever workflow configuration is interpreted.

## 20.5 Preserve partial positive facts without erasing unresolved ambiguity

`environment_selection.py` demonstrates a strong evidence pattern:

```text
known positive selector
+
material unsupported modifier
→ preserve positive selector
→ mark overall interpretation unresolved
```

That is usually better than either discarding all useful evidence or pretending the whole state is understood.

---

# 21. Current mastery status

Plan-01 **content** has been covered through its intended stop line.

Current honest status:

```text
Chunk 1 — content covered
Chunk 2 — content covered
Chunk 3 — content covered
Chunk 4 — content covered; formal source/test ownership gates deferred
Chunk 5 — content covered; independent reconstruction/test gate deferred
```

Therefore:

```text
PLAN 01
[~] CONTENT ROUTE COMPLETE
```

It should not yet be described as fully mastered/green because the learning contract includes user-owned reconstruction/test evidence that was deliberately postponed to preserve momentum.

Deferred work includes representative independent reconstruction of important source responsibilities and focused-test reasoning without relying on the teaching walkthrough.

Those deferred checks are non-blocking unless a later step makes a missing concept causally necessary.

---

# 22. Fast review checklist

Before moving far beyond Plan 01, a learner should be able to recognize or eventually explain these statements correctly.

### Real case

```text
S001 = Pydantic historical Soup Sieve 2.6 → 2.8.4 update
```

### Dependency relationship

```text
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

### Lockfile boundary

```text
soupsieve in uv.lock
!=
soupsieve in every environment
```

### CI boundary

```text
workflow YAML
!=
runtime execution
```

### Source pipeline

```text
repository.py
→ exact evidence

uv_lock.py
→ interpreted file-level transition

change.py
→ reconciled PR-wide transition

analysis.py
→ orchestration

environment.py
→ typed source context
```

### Workflow pipeline

```text
workflow YAML
→ workflow_definition.py
→ RunStepDefinition
→ environment_selection.py
→ DependencyGroupSelector("docs")
```

### Main Plan-01 non-proof

```text
DependencyGroupSelector("docs")
!=
proof that docs reaches soupsieve
```

That missing relation begins Plan 02.

---

# 23. One-page mental model

If almost everything else is forgotten, reconstruct Plan 01 from this:

```text
REAL CASE
pydantic/pydantic S001
soupsieve 2.6 → 2.8.4

        │
        ▼

WHY IS SOUPSIEVE RELEVANT?
docs tooling can reach it transitively

        │
        ▼

WHAT DOES THE LOCK TELL US?
soupsieve exists in the resolved lock graph
but lock presence != selected-environment membership

        │
        ▼

WHAT DOES THE WORKFLOW STATICALLY DECLARE?
docs-build contains:
uv sync --all-packages --group docs

        │
        ▼

WHAT EXACTLY CHANGED?
repository.py acquires exact base/head uv.lock
uv_lock.py interprets 2.6 → 2.8.4
change.py reconciles that to PR-wide DependencyVersionChange

        │
        ▼

WHERE DID THAT FACT COME FROM?
analysis.py + environment.py preserve:
UvLockDependencyContext

        │
        ▼

WHAT ENVIRONMENT DOES THE WORKFLOW SELECT?
workflow_definition.py creates RunStepDefinition
environment_selection.py interprets:
DependencyGroupSelector("docs")

        │
        ▼

WHAT IS STILL MISSING?
proof that selected docs environment reaches soupsieve

        │
        ▼

PLAN 02
exact membership / graph-reachability reasoning
```

---

# 24. Final Plan-01 conclusion

Plan 01 teaches a disciplined evidence progression rather than one large conclusion.

For S001 we now understand how UpgradePilot can separately establish:

```text
1. a real dependency update exists;
2. exact source evidence identifies soupsieve 2.6 → 2.8.4;
3. the file-level transition is interpreted;
4. admitted source meanings are reconciled into one PR-wide transition;
5. exact uv-lock source context is preserved;
6. the static GitHub Actions workflow is represented as typed provider structure;
7. the relevant run command is bound to the correct project;
8. the command explicitly selects dependency group docs.
```

The disciplined stopping point is equally important:

```text
changed package = soupsieve
+
selected group = docs
```

still does **not** prove:

```text
docs contains/reaches soupsieve
```

That relationship requires a new evidence responsibility rather than assumption.

That is the correct handoff from Plan 01 to Plan 02.
