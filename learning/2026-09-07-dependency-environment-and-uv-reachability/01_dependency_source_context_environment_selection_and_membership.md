# Dependency Source Context, Environment Selection, and Static Membership

**Learning-artifact date:** 2026-09-07  
**Source/test evidence horizon:** `main@a6587bf2c4756702f1cb6506e60925652ce22c2e`  
**Roadmap coordination:** **Dependency declarations, environments, and `uv.lock` reachability** in `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** current frozen learning snapshot that complements the August dependency-environment/CI learning material rather than rewriting it  
**Target depth:** **must master / own** source provenance, source-context ownership, static environment selection, membership semantics, and proof boundaries; understand TOML/PEP 508/shell-parsing mechanics operationally; keep parser/library internals lookup-assisted

This note answers one central question:

> **Once UpgradePilot has established which dependency changed and from which exact source, how does it preserve that source-specific environment meaning and relate it to what a workflow statically selects—without pretending that configuration is runtime execution?**

The shortest current mental model is:

```text
changed-file evidence
→ source-specific dependency extraction
→ DependencyVersionChange
+ exact DependencySourceContext

workflow run declaration
→ static project/direct-install selection evidence

source context + static selection
→ bounded membership / relation result

all of the above
!= runtime execution / installation / package exercise / safety
```

---

## 1. Why this responsibility exists

A dependency name and version transition are not enough to answer environment questions.

The same package can be changed in materially different source contexts:

```text
requirements/docs.txt
constraints/runtime.txt
pyproject.toml optional extra "docs"
uv.lock
```

Those sources do not mean the same thing.

For example:

```text
soupsieve changed in pyproject optional extra "docs"
```

already establishes more source-scoped meaning than:

```text
soupsieve changed somewhere in the repository
```

But it still does **not** establish:

```text
a workflow selected "docs"
the installation command executed
soupsieve was installed
tests imported or exercised soupsieve
the upgrade is compatible
```

UpgradePilot therefore keeps several propositions separate instead of jumping from “dependency changed” to “CI covers the dependency.”

---

## 2. Current control/data flow

The current dependency-analysis entry is:

```python
analyze_dependency_change(...)
```

in:

```text
src/upgradepilot/dependency/analysis.py
```

At a high level:

```text
PullRequestIdentity + complete ChangedFile records
        ↓
recognize admitted dependency source formats
        ↓
source-specific extraction
        ↓
compare all extracted results across the PR
        ↓
DependencyVersionChange
        ↓
translate exact source provenance into typed DependencySourceContext values
```

The resulting application-facing dependency result is not merely the change itself:

```text
DependencyChangeAnalysis
├── dependency: DependencyVersionChange
└── source_contexts: tuple[DependencySourceContext, ...]
```

That second field matters because downstream environment reasoning needs to know **how the change was established**, not merely which package/version changed.

---

## 3. Source-specific extraction: same outcome family, different evidence semantics

Current source extraction supports several bounded forms.

### 3.1 Exact requirements / constraints patches

Owner:

```text
src/upgradepilot/dependency/requirements.py
```

The current rule is deliberately narrow:

```text
admitted requirements/constraints path
+ complete GitHub patch
+ exactly one removed package==version line
+ exactly one added package==version line
+ same normalized package
→ ExtractedDependencyVersionChange
```

Important source evidence:

```text
file_format = exact_requirement
extraction_method = changed_file_patch
```

The extractor also verifies that the additions/deletions visible in the patch match GitHub's changed-file counts before trusting the patch as complete evidence.

That protects this distinction:

```text
partial patch snippet
!= complete dependency transition evidence
```

#### Requirements vs constraints context

After PR-wide comparison, `analysis.py` preserves whether the admitted path belongs to the requirements family or constraints family:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
```

That difference is retained instead of flattening both into one generic “dependency file” context because later installation/CI reasoning may legitimately treat them differently.

---

### 3.2 `pyproject.toml` optional-extra transition

Owner:

```text
src/upgradepilot/dependency/pyproject.py
```

The current rule compares complete exact base/head files and supports one conservative PEP 621 transition:

```text
[project.optional-dependencies]
extra exists on both sides
+ exactly one removed requirement
+ exactly one added requirement
+ same normalized package
+ same dependency extras / marker / URL identity
+ both sides use one exact non-wildcard ==version pin
→ exact dependency version transition inside one extra
```

The successful result preserves both:

```text
ExtractedDependencyVersionChange
+
source extra name
```

which later becomes:

```text
PyprojectOptionalExtraDependencyContext(extra=...)
```

A useful subtlety is that unrelated `pyproject.toml` metadata changes are neutral. If the optional-dependency surface is unchanged, the extractor returns a dedicated no-change result rather than manufacturing a dependency-analysis failure.

### Why `packaging.requirements.Requirement` matters

PEP 508 requirement strings can contain package identity, extras, version specifiers, environment markers, and direct references. Reusing `Requirement` lets UpgradePilot parse that accepted syntax rather than inventing another partial parser.

But the current **change rule** remains stricter than the parser capability:

```text
parser can understand broad PEP 508 syntax
!=
UpgradePilot currently accepts every PEP 508 edit as a safe dependency-version transition
```

That is an important engineering pattern: a library parser can be broad while the product's admitted semantic rule remains intentionally narrow.

---

### 3.3 `uv.lock` source context

When exact base/head `uv.lock` evidence establishes the dependency transition, `analysis.py` preserves:

```text
UvLockDependencyContext
```

This context means approximately:

```text
this exact package/version transition was established from this exact uv.lock source
at this repository/head revision
```

It does **not** mean:

```text
this package is reachable from every uv environment
```

That missing proposition belongs to the selected-root reachability responsibility taught in the second note of this package.

---

## 4. `DependencySourceContext`: preserve facts that were actually earned

Owner:

```text
src/upgradepilot/dependency/environment.py
```

Current variants include:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

Each carries the common trusted core:

```text
repository
revision
normalized_package
source_evidence
```

and only adds source-specific facts when those facts were independently established.

For example:

```text
PyprojectOptionalExtraDependencyContext
→ may carry extra="docs"

UvLockDependencyContext
→ does NOT invent an extra/group merely because uv supports them
```

This is a strong ownership rule:

> **Translate evidence into the narrowest typed context that preserves what the source actually established. Do not enrich it with facts owned by another source or later inference.**

---

## 5. Source context is not environment execution

The docstrings across these types intentionally repeat the non-claim because it is easy to overread the evidence.

A source context can establish:

```text
which exact source produced the dependency change
which repository/revision owns that source
which optional extra/group was affected when the source itself proves that scope
```

It does not establish:

```text
workflow selection
command execution
resolver success
installation success
runtime version
package exercise
behavioral compatibility
```

This is the same UpgradePilot evidence doctrine applied at a smaller technical boundary:

```text
source declaration fact
!= runtime fact
```

---

## 6. Static project-environment selection

Owner:

```text
src/upgradepilot/dependency/environment_selection.py
```

This module starts from provider-owned static workflow run steps and observes a deliberately bounded set of project selectors.

The main public observation is:

```python
observe_project_environment_selection(...)
```

It can recognize currently admitted forms such as:

```text
pip / python -m pip install of the local project
uv sync
uv run
explicit optional extras
explicit dependency groups
--all-extras
--all-groups
bounded --all-packages scope
```

It also preserves:

```text
project_root
operation
manager
segment_index
selectors
package_scope
```

### Current selector types

```text
OptionalExtraSelector
DependencyGroupSelector
AllOptionalExtrasSelector
AllDependencyGroupsSelector
```

The names are normalized for comparison while original spelling remains available where useful.

### Why only positive explicit selectors?

The current rule is designed around what static text can establish safely.

Dynamic project paths, unsupported negative/targeting options, ambiguous working-directory context, or uv commands whose default-group behavior would require additional project/config evidence remain unresolved instead of being guessed.

That means:

```text
uv sync --group docs
→ useful explicit selection evidence

uv sync
→ does not automatically become “all relevant groups selected”
```

because uv defaults can depend on project/config state that this bounded observer does not own.

---

## 7. Working-directory and path resolution are part of the evidence relation

A command like:

```bash
pip install -r requirements/docs.txt
```

cannot be compared safely with a known dependency source without understanding its effective working directory.

Likewise:

```bash
uv --project services/api sync --group docs
```

must bind to the correct repository-relative project root.

The project therefore uses shared workflow-context helpers to resolve bounded shell segments and effective working-directory/path context.

The important conceptual lesson is:

> **Textual equality of path strings is not enough when command interpretation depends on execution context.**

But the current observer still stops at static command meaning—it does not claim the command ran.

---

## 8. Direct requirements-file installation observation

Owner:

```text
src/upgradepilot/dependency/direct_install.py
```

Main function:

```python
observe_direct_installation_declaration(...)
```

Its responsibility is narrower than general command interpretation:

```text
one static run step
+ one independently established dependency-source path
→ does this step visibly declare pip installation from that exact requirements source?
```

Example shape:

```text
known dependency source = requirements/docs.txt
workflow command = pip install -r requirements/docs.txt
→ observed direct requirements install declaration
```

A dynamic path or unresolved working directory becomes:

```text
unresolved
```

and a different requirements path becomes:

```text
not_observed / not established for this source
```

Again:

```text
static direct-install declaration
!= runtime installation success
```

This distinction is later consumed by CI reasoning, but the deeper CI proof boundary belongs to the dedicated CI learning group rather than this note.

---

## 9. Static membership for project-source extras/groups

Owner:

```text
src/upgradepilot/dependency/environment_membership.py
```

Current public function:

```python
evaluate_project_source_environment_membership(...)
```

It compares two independently established facts:

```text
SOURCE FACT
changed dependency belongs to project optional extra/group X

SELECTION FACT
static workflow declaration selects extra/group Y
```

Then it determines whether the selector establishes membership of the affected environment.

### Optional-extra example

```text
source context:
  changed dependency belongs to optional extra "Docs"

workflow declaration:
  pip install ".[docs]"
```

The normalized names compare equal, so the static membership result can be:

```text
member
reason = affected_optional_extra_selected
```

### Non-selected example

```text
source extra = docs
visible selectors = test
```

Result:

```text
not_established
```

That means only:

> The visible positive selector does not establish selection of the affected source environment.

It does **not** mean the environment was absent at runtime.

### Root mismatch

If the source context belongs to one project root while the workflow declaration is bound to another, the result becomes:

```text
unresolved
```

rather than forcing a false yes/no relation.

---

## 10. A useful separation: selection vs membership

Keep these responsibilities distinct:

```text
ENVIRONMENT SELECTION
What project/extra/group does the static command visibly select?

ENVIRONMENT MEMBERSHIP
Does that selected environment correspond to the source-established environment containing the changed dependency?
```

This separation prevents the workflow parser from needing to know dependency-source semantics and prevents dependency extraction from needing to understand workflow command syntax.

That is a recurring UpgradePilot architecture pattern:

```text
producer establishes one fact
consumer establishes another fact
small relation owner compares them
```

---

## 11. Why `uv.lock` membership is not handled here

The current project-source membership module only owns source-established optional extras/dependency groups.

A `uv.lock` change is different because the target package may be transitively reachable through lock graph structure.

For uv the responsibility is therefore:

```text
UvLockDependencyContext
+
ProjectEnvironmentSelectionDeclaration
+
exact uv.lock structural evidence
→ selected-root reachability
```

That is not a simple name-equality membership problem, so it has its own owner:

```text
src/upgradepilot/dependency/uv_reachability.py
```

The next note teaches that mechanism.

---

## 12. Real UpgradePilot pressure: optional environment vs mediated dependency

Two recurring real pressures help anchor this design.

### Optional-environment pressure

A dependency can be changed inside an optional extra such as documentation tooling.

The important questions become:

```text
which source environment contains the changed dependency?
which environment does CI statically select?
do those two facts correspond?
```

This is why preserving the optional-extra name from `pyproject.toml` matters.

### Mediated/transitive pressure

A changed package in `uv.lock` can be reached only through another selected package chain.

That cannot be represented honestly as:

```text
package appears in lock
→ therefore selected environment contains it
```

The project had to grow from simple source/environment matching toward explicit graph-backed reachability. That evolution is preserved rather than hidden by the current abstraction.

---

## 13. Engineering progression from the older August snapshot

The August learning artifacts remain useful historical snapshots. They captured the project when environment and CI-consumption reasoning was earlier and less structurally separated.

The current design has since sharpened several boundaries:

```text
dependency transition provenance
→ typed source contexts

workflow command parsing
→ explicit static project selectors

project source context + selector
→ small membership relation

uv lock context + selector
→ separate graph-backed reachability responsibility
```

The lesson is not that the earlier artifacts were “wrong.” They captured the evidence horizon available then.

The reusable engineering lesson is:

> **When new cases reveal that one broad notion such as “dependency environment” contains several independently provable propositions, split the responsibilities around those propositions instead of stretching one generic model.**

---

## 14. Important Python/library mechanisms

### Must understand operationally

**`dataclass(frozen=True, slots=True)`**  
Used for small trusted evidence/context values. Frozen values make accidental mutation harder while evidence flows between owners.

**`tomllib`**  
Python standard-library TOML parser used for exact `pyproject.toml` and `uv.lock` semantics. Parsing TOML does not itself establish UpgradePilot domain meaning.

**`packaging.requirements.Requirement`**  
Parses PEP 508 requirement syntax. UpgradePilot then applies narrower accepted semantic rules on top.

**package/extra normalization**  
User spelling such as `my_pkg`, `my-pkg`, or case variants may represent the same Python packaging identity. Comparison should use normalized identity while preserving source spelling when useful for explanation.

**`shlex.split(...)`**  
Used for bounded shell-like tokenization of static commands. It is not a shell executor.

**typed union results**  
Current APIs often return success/problem or observed/not-observed/unresolved states rather than throwing exceptions for every expected evidence limitation.

### Lookup-level

- complete PEP 508 grammar;
- every uv CLI option;
- `shlex` implementation internals;
- TOML parser internals;
- advanced Python typing internals.

---

## 15. Focused tests and what they protect

Current relevant test owners include:

```text
tests/test_exact_requirement_change.py
tests/test_pyproject_optional_extra_change.py
tests/test_dependency_analysis.py
tests/test_dependency_environment.py
tests/test_project_environment_selection.py
tests/test_project_source_environment_membership.py
tests/test_direct_install_declaration.py
```

They protect propositions such as:

```text
exact requirements patch completeness and one-change boundary
conservative optional-extra transition extraction
PR-wide source comparison and source-context preservation
selector parsing and project-root/package-scope behavior
normalized extra/group membership
root mismatch → unresolved
direct requirements-path declaration observation
```

### Proof/non-proof

Reading these current tests establishes what behavior the repository intends to protect at this snapshot.

This learning-artifact authoring session did **not** execute those tests, so this note does not manufacture a fresh aggregate PASS claim.

Even a passing focused family would establish only the exercised static/source contracts, not:

```text
runtime command execution
installation success
complete environment formation
package exercise
compatibility
upgrade safety
```

---

## 16. Current facts, rationale, judgment, and future improvement

### Current implementation fact

UpgradePilot currently preserves dependency source provenance as typed source contexts, observes a bounded set of static workflow environment selectors, and evaluates project-source extra/group membership separately from uv graph reachability.

### Evidenced rationale

Source docstrings, the reconciliation design, tests, and the historical learning snapshots consistently support the reason for these boundaries: different sources prove different facts, and static declarations must not be promoted to runtime truth.

### Engineering judgment

The current decomposition is stronger than a generic “environment” record because it makes unsupported inference harder and gives future consumers narrow typed contracts.

The cost is more concepts/types and more explicit handoffs. That cost is justified only while the distinctions continue to carry real evidence meaning.

### Reopen/improve when

Revisit the boundaries if real product responsibility requires:

```text
additional dependency source formats
full dependency-group source extraction
richer uv default-group/config interpretation
runtime installation evidence
resolver/environment formation evidence
```

Do not add those mechanisms merely for completeness.

---

## 17. Fast relearning route

When returning later:

```text
1. Recall: dependency change != environment selection != runtime execution.
2. Open dependency/analysis.py and trace source evidence → source_contexts.
3. Open dependency/environment.py and name what each context may and may not claim.
4. Open environment_selection.py and trace one explicit optional-extra/group command.
5. Open environment_membership.py and compare source environment vs selected environment.
6. Inspect one project-selection test and one membership test.
7. Then continue to this package's uv reachability note.
```

---

## 18. Ownership / transfer questions

Without looking at the note, explain:

1. Why is `DependencyVersionChange` alone insufficient for environment reasoning?
2. Why can a `PyprojectOptionalExtraDependencyContext` carry an extra name while a `UvLockDependencyContext` should not invent one?
3. Why does `uv sync` with no explicit extra/group remain potentially unresolved under the current observer?
4. What is the difference between static environment selection and source-environment membership?
5. Why does `not_established` not mean “the package definitely was not installed at runtime”?
6. Why is direct requirements-file installation observation separate from dependency extraction?
7. If a workflow selects the correct extra but never runs, which current layer is allowed to claim that it executed? Answer: none of the source/selection/membership owners in this note.

Transfer exercise:

> Imagine a monorepo has `services/api/pyproject.toml` with extra `docs`, while a workflow command selects root-project `.[docs]`. Predict why the current membership relation should not simply return `member` based on the shared extra name.

---

## 19. Source and evidence anchors

Current source/test horizon:

```text
main@a6587bf2c4756702f1cb6506e60925652ce22c2e
```

Primary current source:

```text
src/upgradepilot/dependency/analysis.py
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/requirements.py
src/upgradepilot/dependency/pyproject.py
src/upgradepilot/dependency/environment.py
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/dependency/environment_membership.py
src/upgradepilot/dependency/direct_install.py
```

Focused tests:

```text
tests/test_exact_requirement_change.py
tests/test_pyproject_optional_extra_change.py
tests/test_dependency_analysis.py
tests/test_dependency_environment.py
tests/test_project_environment_selection.py
tests/test_project_source_environment_membership.py
tests/test_direct_install_declaration.py
```

Historical/reconciliation evidence:

```text
learning/2026-08-17-Cluster1-5-B2 Dependency Environment and CI Consumption Evidence.md
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md
```

The exact historical plan/file names above are provenance only. Current navigation and concepts in this artifact use semantic responsibility names.

This file is a frozen learning snapshot, not live project-state authority and not authorization to modify product code.

`UP-SKILL:upgradepilot-learning-artifact`
