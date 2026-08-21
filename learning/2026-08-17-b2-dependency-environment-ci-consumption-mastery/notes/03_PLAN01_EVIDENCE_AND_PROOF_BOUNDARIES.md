# Plan 01 — Evidence and Proof Boundaries

**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Learning package:** `2026-08-17-b2-dependency-environment-ci-consumption-mastery`  
**Role:** compact proof-strength and evidence-state reference for Plan 01  
**Companion notes:** [`01_PLAN01_END_TO_END_LEARNING_NOTE.md`](01_PLAN01_END_TO_END_LEARNING_NOTE.md), [`02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md`](02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md)  
**Status:** Plan-01 content route complete; stronger membership/runtime propositions remain deferred

---

## 1. Why this file exists

UpgradePilot is an evidence-backed decision-support project. A recurring engineering risk is not merely parsing the wrong value; it is **claiming more than the evidence establishes**.

Plan 01 repeatedly crosses boundaries where a weaker fact is transformed into a stronger one:

```text
repository text
→ validated source evidence
→ interpreted file-level meaning
→ reconciled PR-wide meaning
→ typed source context
→ static workflow structure
→ static project-environment selection
```

Every arrow needs its own justification. The result of one stage must not be silently promoted into a stronger proposition owned by another stage.

This file is therefore a reference for two questions:

```text
WHAT DOES THIS RESULT ESTABLISH?
WHAT DOES THIS RESULT NOT ESTABLISH?
```

---

# 2. Learning evidence-state vocabulary

These labels are a **learning and reasoning vocabulary**. They are not a requirement that production source code define enums/classes with these exact names.

## 2.1 OBSERVED

Information has been seen in an external/upstream source, but the current responsibility has not yet established stronger identity, validity, or meaning.

Example:

```text
workflow text contains:
uv sync --all-packages --group docs
```

At first contact this is simply visible source text.

## 2.2 ACQUIRED

The required artifact has been successfully retrieved.

Example:

```text
exact base uv.lock retrieved
exact head uv.lock retrieved
```

Acquisition answers **“did we obtain the required artifact?”**, not whether its contents are semantically usable.

## 2.3 VALIDATED

The evidence has passed the identity/structure/provenance checks required by the current responsibility.

Examples include checking the admitted path/status, exact base/head availability, repository-file provenance, TOML shape, and bounded package-record structure.

```text
ACQUIRED
!=
VALIDATED
```

## 2.4 INTERPRETED

Validated evidence has been transformed into bounded domain meaning.

For S001:

```text
exact base/head uv.lock evidence
→ uv_lock.py
→ ExtractedDependencyVersionChange(
     package="soupsieve",
     old_version="2.6",
     proposed_version="2.8.4"
   )
```

That is a **file-level interpreted transition**.

## 2.5 RECONCILED

Multiple admitted interpretations/evidence sources have been compared and promoted only if they safely agree.

For Plan 01:

```text
ExtractedDependencyVersionChange values
→ change.py
→ DependencyVersionChange
```

The result is stronger because it is PR-wide canonical dependency-change meaning rather than one source-local interpretation.

```text
INTERPRETED
!=
RECONCILED
```

## 2.6 CONTEXTUALIZED

Established meaning has been attached to a larger typed context without inventing facts the context does not contain.

For S001:

```text
DependencyVersionChange
+ exact uv.lock source provenance
→ UvLockDependencyContext
```

This means the trusted transition is now connected to its dependency-source context.

It does **not** mean the workflow selected a particular dependency group or that Soup Sieve belongs to that group.

## 2.7 EXERCISED

Runtime evidence establishes that the relevant mechanism/path actually executed or was consumed at the exact strength claimed.

Plan 01 does not reach this state.

```text
static workflow definition
!=
EXERCISED runtime path
```

## 2.8 EVALUATED

Accumulated evidence has been assessed against a higher-level investigation/product question at the strength actually supported.

Plan 01 mostly builds the evidence prerequisites. Higher-level compatibility/safety/action evaluation lies later in the project route.

---

# 3. The Plan-01 proof ladder

The most useful compact ladder is:

```text
1. exact repository source exists
        ↓
2. source is admitted/validated
        ↓
3. source says Soup Sieve changed 2.6 → 2.8.4
        ↓
4. admitted dependency sources agree on that canonical transition
        ↓
5. transition is attached to uv.lock source context
        ↓
6. static GitHub workflow structure exposes a run command
        ↓
7. that command explicitly selects dependency group "docs"
        ↓
STOP — Plan 01

8. "docs" reaches Soup Sieve                    ← Plan 02
9. CI statically consumes that affected env      ← later Plan 02
10. runtime command/path actually executed        ← stronger runtime evidence
11. exact changed package/version was exercised   ← stronger still
12. compatibility/safety/action conclusion        ← later evaluation
```

A later rung may depend on earlier rungs, but earlier rungs do not automatically imply later ones.

---

# 4. Result-by-result proof boundary

## 4.1 `RepositoryTextFile`

### Establishes

When strong runtime provenance has been validated, it represents repository text bound to an immutable revision and path, with GitHub/file provenance metadata.

Important identity/provenance concepts:

```text
repository + path + revision
→ which immutable repository file was requested

blob SHA
→ Git object/content provenance handle supplied by GitHub

reported/decoded byte counts
→ acquisition consistency + resource-bound evidence
```

### Does NOT establish

```text
the file has dependency meaning
that a package changed
that a workflow command executed
that the blob hash was independently recomputed from decoded bytes
```

---

## 4.2 `ExtractedDependencyVersionChange`

Owned by source-specific extraction such as `dependency/uv_lock.py`.

### Establishes

For one admitted dependency source:

```text
normalized package identity
old version
proposed version
exact source provenance
```

S001:

```text
soupsieve 2.6 → 2.8.4
from exact base/head uv.lock evidence
```

### Does NOT establish

```text
PR-wide agreement across all admitted dependency sources
direct/transitive status
selected dependency group/extra
CI consumption
runtime installation/exercise
compatibility or safety
```

---

## 4.3 `DependencyVersionChange`

Owned by `dependency/change.py` after reconciliation.

### Establishes

The admitted dependency-change interpretations agree on:

```text
one normalized package
one exact old → proposed transition
```

and preserve the agreeing source evidence.

For S001:

```text
canonical PR-wide transition:
soupsieve 2.6 → 2.8.4
```

### Does NOT establish

```text
which environment contains the package
which workflow selects that environment
whether CI consumed the package
whether runtime used the proposed version
compatibility/safety/action
```

Important rule:

```text
successful extraction from one source
+
material problem in another admitted source
!=
trustworthy canonical reconciliation
```

That is why `change.py` preserves problems rather than letting one successful source silently cancel contradictory/invalid admitted evidence.

---

## 4.4 `UvLockDependencyContext`

Owned by `dependency/environment.py`, constructed from trusted provenance by `analysis.py`.

### Establishes

The canonical dependency transition is connected to an exact `uv.lock` source context for the repository/head/package identity.

A useful mental model is:

```text
UvLockDependencyContext
= permission to use uv-lock-specific environment/membership reasoning later
```

### Does NOT establish

```text
docs group selected Soup Sieve
docs group contains/reaches Soup Sieve
uv sync executed
Soup Sieve was installed
Soup Sieve was exercised
```

Critical inequality:

```text
SOURCE CONTEXT
!=
SELECTED ENVIRONMENT CONTEXT
```

---

## 4.5 `WorkflowDefinition` / `RunStepDefinition`

Owned by `github/workflow_definition.py`.

### Establishes

Bounded static GitHub Actions source structure, for example:

```text
job: docs-build
step index: 2
run command:
uv sync --all-packages --group docs
```

The provider IR can preserve jobs, step kinds, static scalar values, source ordering/spans, defaults, and supported dynamic structure without importing dependency semantics into GitHub ownership.

### Does NOT establish

```text
what --group docs means to the Python project
that the step ran
that the job succeeded
that the environment was formed
that Soup Sieve was present
```

Critical inequality:

```text
STATIC WORKFLOW DEFINITION
!=
RUNTIME WORKFLOW INSTANCE
```

---

## 4.6 `ProjectEnvironmentSelectionObservation`

Owned by `dependency/environment_selection.py`.

For exact S001 static input:

```text
uv sync --all-packages --group docs
```

bound to root `pyproject.toml`, the important result is:

```text
state = observed
manager = uv
operation = sync
selectors = (DependencyGroupSelector("docs", mode="include"),)
```

### Establishes

The static run declaration is safely bound to the independently identified project and explicitly includes dependency group `docs`.

### Does NOT establish

```text
that "docs" reaches Soup Sieve
that uv sync executed
that sync succeeded
that Soup Sieve was installed
that Soup Sieve was directly exercised
```

Critical inequality:

```text
DependencyGroupSelector("docs")
!=
Soup Sieve is a member of docs
```

That missing relation is the Plan-02 membership problem.

---

# 5. `observed` vs `not_observed` vs `unresolved`

The project-environment selector boundary deliberately uses three states rather than a Boolean.

## `observed`

A supported declaration is visible and can be interpreted safely.

Example:

```text
uv sync --group docs
→ DependencyGroupSelector("docs")
→ observed
```

## `not_observed`

The source was readable, but no admitted project-selection declaration was found.

Example:

```text
echo "pip install -e .[dev]"
```

The text mentions a pip command, but the actual command is `echo`, so UpgradePilot must not promote the quoted text into a selection declaration.

## `unresolved`

Materially relevant syntax is present, but the bounded observer cannot safely determine its exact meaning.

Examples:

```text
uv sync --group "${{ matrix.group }}"
→ group identity is dynamic
→ unresolved

uv sync
→ project-bound uv command exists
→ exact default-group selection needs separate config/project evidence
→ unresolved

uv sync --all-extras --no-extra mlx
→ positive selector is visible
→ material negative selector is outside current bounded rule
→ preserve the positive fact but overall state remains unresolved
```

The essential rule is:

```text
UNKNOWN / UNRESOLVED
!=
NEGATIVE FACT
```

Do not convert inability to prove something into proof that it is absent.

---

# 6. High-value inequalities to memorize

These are the Plan-01 proof boundaries worth retaining long term:

```text
repository dependency
!= core library runtime dependency

transitive dependency
!= irrelevant dependency

package appears in uv.lock
!= package belongs to every environment

lock presence
!= selected-environment membership

acquired evidence
!= validated evidence

validated evidence
!= interpreted domain meaning

file-level interpreted change
!= PR-wide reconciled change

source context
!= selected environment

static workflow definition
!= runtime execution

successful runtime workflow/job
!= exact changed-package exercise

RunStepDefinition("uv sync --group docs")
!= DependencyGroupSelector("docs")
until Dependency performs the interpretation

DependencyGroupSelector("docs")
!= docs reaches Soup Sieve

missing/ambiguous evidence
!= negative evidence
```

---

# 7. Common overclaims and corrected wording

## Overclaim

> Pydantic uses Soup Sieve.

### Better

> Pydantic's documentation/tooling dependency path reaches Soup Sieve transitively.

---

## Overclaim

> Soup Sieve is in `uv.lock`, so docs CI installs it.

### Better

> `uv.lock` contains Soup Sieve, but selected-environment membership must be established separately.

---

## Overclaim

> The workflow exercises the docs environment.

### Better

> The static workflow is configured to synchronize the `docs` dependency group and later invoke documentation commands.

Use runtime/exercise language only when runtime evidence supports it.

---

## Overclaim

> `UvLockDependencyContext` means Soup Sieve belongs to the docs environment.

### Better

> `UvLockDependencyContext` preserves that the canonical transition came from exact `uv.lock` evidence and enables later uv-specific membership analysis.

---

## Overclaim

> `uv sync` with no selector means no dependency group was selected.

### Better

> The bounded command observer cannot establish exact default-group selection from command text alone; project/config evidence is required, so the result is unresolved.

---

# 8. S001 at the Plan-01 stop line

At the end of Plan 01 we have two important independently established facts:

```text
DEPENDENCY FACT

DependencyVersionChange
→ soupsieve 2.6 → 2.8.4

source context
→ UvLockDependencyContext
```

and:

```text
STATIC WORKFLOW-SELECTION FACT

docs-build run step
→ uv sync --all-packages --group docs
→ DependencyGroupSelector("docs")
→ observed static project-environment selection
```

What remains missing is the bridge:

```text
DependencyGroupSelector("docs")
        ?
        ↓
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

Plan 02 owns that membership/reachability question.

Therefore the correct Plan-01 conclusion is:

```text
WHAT CHANGED?
ESTABLISHED

WHERE DID THE CHANGE EVIDENCE COME FROM?
ESTABLISHED

WHICH PROJECT ENVIRONMENT DOES THE STATIC WORKFLOW EXPLICITLY SELECT?
ESTABLISHED: docs

DOES THAT SELECTED ENVIRONMENT REACH THE CHANGED PACKAGE?
NOT YET ESTABLISHED — Plan 02

DID CI ACTUALLY EXECUTE/INSTALL/EXERCISE THE CHANGED PACKAGE?
NOT ESTABLISHED BY PLAN 01
```

That boundary is the most important thing this reference file exists to protect.
