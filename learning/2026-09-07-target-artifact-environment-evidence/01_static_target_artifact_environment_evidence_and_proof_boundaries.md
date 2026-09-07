# Static Target Artifact-Environment Evidence and Proof Boundaries

**Learning-artifact date:** 2026-09-07  
**Source/test evidence horizon:** `main@f76e8a770320763100183454fac49893abb9ff48`  
**Roadmap coordination:** **Target Python and target-environment evidence resolution** in `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** current frozen learning snapshot that complements, rather than replaces, `../2026-09-02-target-python-evidence-resolution/01_TARGET_PYTHON_EVIDENCE_RESOLUTION_CHAIN.md`  
**Target depth:** **must master / own** the target artifact-environment responsibility, its static-evidence boundary, provenance, typed abstention/limitation behavior, and relationship to later artifact applicability; understand the shared workflow intermediate representation and direct-install observer operationally; keep full GitHub Actions semantics, matrix evaluation, reusable-workflow expansion, and exact wheel-tag derivation deliberately deferred

This note answers one central question:

> **Given an exact GitHub Actions workflow definition, what target-side environment facts can UpgradePilot safely preserve for artifact reasoning without pretending that static configuration is runtime execution or exact wheel compatibility?**

The shortest current mental model is:

```text
exact workflow file at immutable PR head
→ shared GitHub Actions static interpretation
→ safely select one local steps job
→ preserve only literal Target-relevant facts
   - runner
   - setup-python version
   - direct changed-dependency installation declaration
→ preserve limitations / abstain when evidence is ambiguous
→ TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem

static target evidence
!= runtime execution
!= installed environment
!= exact wheel compatibility
!= artifact-serviceability applicability
```

---

## 1. Relationship to the existing target-Python learning artifact

The September target-Python artifact already teaches a different target-side proposition:

```text
exact target pyproject.toml
→ requires-python declaration
→ target Python relevance
→ Python-support applicability update
```

That remains valid and should not be rewritten merely because another target responsibility now exists.

The artifact-environment responsibility asks a different question:

```text
exact workflow definition
→ what runner / Python setup / dependency-installation declarations are statically visible?
```

Keep these separate:

```text
TARGET PYTHON DECLARATION
What Python range does the target project itself declare?

TARGET ARTIFACT ENVIRONMENT
What partial artifact-relevant environment facts does one exact workflow job visibly declare?
```

They can later contribute to neighboring reasoning, but one does not substitute for the other.

A useful ownership rule is:

> **Target-side evidence is not one generic “environment object.” Different exact sources establish different propositions and should retain separate owners.**

---

## 2. Current owner and responsibility

Current owner:

```text
src/upgradepilot/target/artifact_environment.py
```

Public entry:

```python
interpret_target_artifact_environment(
    evidence,
    *,
    dependency_source_file,
)
```

Inputs are deliberately strong and narrow:

```text
one exact RepositoryFileEvidence for a workflow definition
+
one independently established repository-relative dependency source path
```

The function does not discover arbitrary workflow files, parse pull-request identity from strings, or guess which dependency source matters. Those facts must already be owned upstream.

Its successful result is:

```text
TargetArtifactEnvironmentEvidence
```

and unsafe/unsupported interpretation becomes:

```text
TargetArtifactEnvironmentProblem
```

rather than a fabricated partial success.

---

## 3. Why this responsibility exists

Artifact-serviceability questions eventually care about the target environment in which a package might need to work.

For example, a workflow may visibly say:

```yaml
runs-on: ubuntu-22.04
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: "3.11"
  - run: pip install -r requirements-dev.txt
  - run: pytest
```

Those declarations are useful evidence:

```text
runner label     = ubuntu-22.04
Python label     = 3.11
changed source   = directly named by a pip installation declaration
```

But they still do not prove:

```text
the job ran
the setup-python step succeeded
Python 3.11 was actually installed
pip installed the changed package successfully
a particular wheel tag was compatible
the package imported or executed
the dependency upgrade is safe
```

Without a dedicated target owner, downstream code could be tempted to jump directly from workflow text to a stronger runtime or compatibility conclusion.

This module exists to prevent that jump.

---

## 4. Provider-owned workflow structure stays separate from Target semantics

`artifact_environment.py` does **not** parse YAML itself.

It delegates workflow structure to the shared GitHub Actions owner:

```text
exact RepositoryTextFile
→ parse_workflow_definition(...)
→ WorkflowDefinition | WorkflowDefinitionProblem
```

The shared workflow representation can preserve richer provider structure such as:

```text
jobs
runs-on values
steps
uses references
with inputs
strategy
container
run defaults
source spans
reusable-workflow jobs
```

The Target module then interprets only the subset required by its own proposition.

Architecture:

```text
GitHub provider responsibility
→ what does the static workflow source structurally contain?

Target artifact-environment responsibility
→ which of those structural facts are safe Target-relevant evidence now?
```

This is the same producer/consumer separation used elsewhere in UpgradePilot:

> **Do not make a downstream domain module re-parse an external format when a provider-owned structural representation already exists.**

---

## 5. Exact workflow provenance survives into the Target result

A successful result preserves:

```text
repository
revision
workflow_path
job
```

These fields identify the exact source of the target facts.

The current result does not copy provider transport metadata merely because it is available. Transport details do not establish a separate Target proposition.

This keeps provenance strong without turning every downstream value into a duplicate provider record.

The important invariant is:

```text
Target fact
→ traceable to exact repository + immutable revision + workflow path + job
```

That exact identity becomes especially important when later application composition combines dependency source, package release, workflow evidence, and artifact reasoning.

---

## 6. Current job-selection boundary

The shared workflow representation can contain multiple jobs, job problems, or reusable-workflow jobs.

The current Target interpreter intentionally accepts only one safely selected **local steps job**.

Conceptually:

```text
exact workflow
→ exactly one local steps job
→ interpret Target facts
```

If the workflow contains multiple jobs, the result is not a parser failure. It is a Target-level selection problem:

```text
state = ambiguous_target_job_selection
```

Why?

Because the workflow may be perfectly valid while UpgradePilot lacks a proposition-specific rule for choosing which job is the relevant target environment.

Similarly, a reusable-workflow job becomes:

```text
state = unsupported_target_job
```

because resolving the delegated workflow source is a separate evidence responsibility.

This distinction is important:

```text
provider can read the workflow
!=
Target can safely select a unique relevant environment
```

---

## 7. Runner evidence: literal only

The current Target rule establishes a runner fact only from one literal scalar `runs-on` declaration.

Example:

```yaml
runs-on: ubuntu-22.04
```

can become:

```text
TargetArtifactEnvironmentFact(
    value="ubuntu-22.04",
    source="runs-on declaration at line ...",
)
```

But richer forms are not collapsed into a guessed platform.

Dynamic or non-single-literal runner structure becomes a limitation such as:

```text
runner_not_single_literal
```

or, when no statically usable runner is identified:

```text
runner_not_statically_identified
```

### Why source locators matter

The result preserves a human-readable source locator alongside the value.

That gives later explanation/debugging a path back to the exact declaration without pretending the locator itself is runtime proof.

---

## 8. Python-version evidence: only `actions/setup-python` literal input

The current Target interpreter looks for one literal, non-dynamic `actions/setup-python@...` step and its `python-version` input.

Example:

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.11"
```

can establish:

```text
python_version.value = "3.11"
```

A value merely appearing elsewhere is not promoted.

For example:

```yaml
- uses: actions/setup-python@v5
  env:
    python-version: "3.11"
```

is not the admitted `with.python-version` proposition, so the current result keeps Python version unobserved.

Likewise:

```yaml
python-version: ${{ vars.PYTHON_VERSION }}
```

is structurally visible but not a literal Target fact. The result preserves:

```text
python_version = None
limitations += setup_python_version_not_literal
```

### Multiple setup steps

More than one relevant setup-python step is not silently reduced to “the last one” or “the first one.” The current Target slice treats that as unsupported/ambiguous.

General lesson:

> **When source order does not itself establish semantic selection, do not use list position as authority.**

---

## 9. Direct installation declaration: compose an existing dependency observer

The Target module does not implement another pip-command parser.

It reuses:

```text
src/upgradepilot/dependency/direct_install.py
```

through:

```python
observe_direct_installation_declaration(...)
```

For every static run step, the shared dependency observer asks whether the independently established dependency source path is directly named in a supported pip requirements-file installation declaration.

Example:

```text
dependency source = requirements-dev.txt
workflow command  = pip install -r requirements-dev.txt
→ observed
```

The Target result then preserves:

```text
dependency_installation_declaration = observed
installation_declaration_source = "pip install -r requirements-dev.txt"
```

### Working-directory context still matters

A command such as:

```yaml
defaults:
  run:
    working-directory: backend
...
- run: pip install -r ../requirements-dev.txt
```

can still resolve to the same exact dependency source through the shared working-directory/path logic.

If the working directory is dynamic and the path relation cannot be established safely, the result becomes:

```text
dependency_installation_declaration = unresolved
limitations += changed_dependency_installation_declaration_unresolved
```

not a guessed observation.

---

## 10. `observed`, `not_observed`, and `unresolved` are different

The installation declaration has three states:

```text
observed
not_observed
unresolved
```

### `observed`

A supported static run declaration visibly names the exact independently established dependency source.

### `not_observed`

The bounded static run declarations were interpretable but did not establish such a declaration.

### `unresolved`

Potentially relevant source text exists, but path/working-directory context or another admitted relation cannot be resolved safely.

These are not runtime states.

In particular:

```text
not_observed
!= package definitely was not installed

observed
!= installation executed or succeeded
```

This is an epistemic distinction, not merely an enum-design preference.

---

## 11. Strategy and container context are preserved as limitations

The shared workflow representation may safely preserve a matrix/strategy or container declaration while the Target interpreter still lacks sufficient semantics to use it as a complete target environment.

Current behavior is deliberately additive:

```text
known literal facts
+
explicit limitation
```

rather than either:

```text
reject the whole readable workflow
```

or:

```text
guess the effective environment
```

Examples:

```text
strategy_context_not_interpreted
container_context_not_interpreted
```

A job can therefore still preserve a literal runner or direct installation declaration while stating that strategy/container context remains outside the current Target interpretation.

This is a useful partial-evidence pattern:

> **Preserve independently established facts even when another material part of the proposition remains unresolved, provided the result clearly carries the limitation.**

---

## 12. Problems versus limitations

The current API deliberately distinguishes two kinds of incompleteness.

### Target-level problem / abstention

Examples:

```text
file_unavailable
workflow_definition_unreadable
ambiguous_target_job_selection
unsupported_target_job
```

These mean the current Target proposition cannot be interpreted safely as a successful evidence object.

### Successful partial evidence with limitations

Examples:

```text
runner_not_single_literal
setup_python_version_not_literal
strategy_context_not_interpreted
container_context_not_interpreted
changed_dependency_installation_declaration_not_observed
changed_dependency_installation_declaration_unresolved
```

These mean some Target facts are still safely preservable, but the result must expose what is missing.

This avoids flattening all uncertainty into one generic `None` or one generic error.

---

## 13. Exact wheel compatibility is deliberately unresolved

Every successful `TargetArtifactEnvironmentEvidence` currently carries:

```text
exact_wheel_compatibility_state = "unresolved"
```

That default is not a placeholder to be casually replaced from runner/Python labels.

Why?

A statement like:

```text
runner = ubuntu-22.04
python = 3.11
```

is not enough by itself to establish a complete exact wheel compatibility tag set.

Exact wheel compatibility can depend on more specific facts such as:

```text
Python implementation and ABI
platform/architecture details
manylinux/musllinux/macOS/Windows compatibility semantics
container/runtime context
exact interpreter/environment identity
wheel tag interpretation
```

The current Target owner does not claim those facts.

Therefore:

```text
literal runner
+ literal setup-python label
+ visible installation declaration
!= TargetWheelCompatibilityEvidence
```

This is one of the most important boundaries in the current artifact-serviceability integration plan.

---

## 14. Relationship to artifact serviceability

Artifact serviceability is a neighboring, separate responsibility owned by:

```text
src/upgradepilot/impact/artifact_serviceability.py
```

At a high level, that mechanism can reason about published artifacts and whether a potentially relevant wheel-serviceability change exists.

The target artifact-environment owner can contribute target-side context, but it does not own the final applicability result.

Keep the sequence conceptually separated:

```text
published artifact evidence
→ artifact-serviceability candidate

exact target workflow evidence
→ partial TargetArtifactEnvironmentEvidence

only admitted exact target compatibility evidence, when available
→ target-specific artifact applicability evaluation
```

At this snapshot, the current static Target evidence is **not** automatically transformed into exact wheel compatibility evidence.

Therefore target-specific artifact applicability can legitimately remain unresolved even after useful runner/Python/install facts have been collected.

---

## 15. Current application-composition horizon

The normal application result now contains an additive field for preserving dependency-source-associated target artifact-environment results:

```text
target_artifact_environment_results
```

with an application-level association type shaped as:

```text
DependencySourceArtifactEnvironmentResult
├── dependency_source
└── target_environment
```

Why associate the result with the dependency source?

Because one pull-request investigation can have several dependency source contexts and several workflow definitions. A target observation must not float free of the exact source proposition it was interpreted against.

However, at the pinned snapshot:

```text
result contract for target artifact environments
→ present

standalone target artifact-environment interpreter/tests
→ present

normal PublicPullRequestInvestigation composition of those target results
→ not yet implemented
```

That is an important learning boundary. Do not read the presence of the result field as evidence that the full application flow already populates it.

The selected integration plan explicitly treats target artifact-environment composition as the next bounded implementation responsibility.

This frozen artifact therefore teaches the existing owner and the current integration seam without claiming the next composition work is complete.

---

## 16. Representative current test flow

A focused test provides a compact representative flow:

```yaml
jobs:
  test:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements-dev.txt
      - run: pytest
```

with:

```text
dependency_source_file = requirements-dev.txt
```

The intended interpreted result includes:

```text
repository = example/project
revision = exact immutable test revision
workflow_path = .github/workflows/ci.yml
job = test
runner = ubuntu-22.04
python_version = 3.11
dependency_installation_declaration = observed
installation_declaration_source = pip install -r requirements-dev.txt
exact_wheel_compatibility_state = unresolved
```

The last line is as important as the observed facts.

The test teaches:

```text
we learned useful target configuration
AND
we still did not earn exact compatibility
```

---

## 17. Failure and uncertainty examples protected by tests

Current focused tests preserve several important boundaries.

### Literal platform/Python but no direct changed-source install

```text
runner known
Python known
install declaration not observed
exact compatibility unresolved
```

### Dynamic Python expression

```text
runner known
Python literal not established
install declaration may still be observed
exact compatibility unresolved
```

### Multiple jobs

```text
workflow structurally valid
Target job choice ambiguous
→ TargetArtifactEnvironmentProblem
```

### Matrix strategy

```text
readable strategy exists
current Target slice does not evaluate it
→ partial evidence + strategy limitation
```

### Container declaration

```text
container structure readable
not interpreted into complete target environment
→ partial evidence + container limitation
```

### Dynamic working directory

```text
possible install command visible
exact source path cannot be resolved safely
→ installation declaration unresolved
```

### Reusable workflow

```text
provider can represent delegation
Target does not expand delegated workflow source
→ unsupported target job
```

### Unavailable/malformed exact workflow

These remain explicit source/definition problems rather than empty evidence objects.

---

## 18. Engineering progression and why the split matters

The earlier target-Python responsibility answered an important applicability question using an exact target project declaration.

Artifact-serviceability pressure exposed a different need:

```text
“What target environment does the real project appear to configure for dependency installation/testing?”
```

A tempting but unsafe shortcut would be:

```text
read runs-on + setup-python
→ infer exact wheel compatibility
```

The current architecture instead inserts a bounded evidence owner:

```text
workflow source
→ partial target artifact-environment evidence
→ explicit limitations
→ exact compatibility remains unresolved
```

That preserves useful information without overclaiming.

The reusable engineering lesson is:

> **When a downstream mechanism needs stronger evidence than an available source actually proves, first model the strongest truthful intermediate proposition. Do not force the source into the downstream conclusion.**

This is the same broader UpgradePilot discipline seen across dependency evidence, CI proof, and planner authority.

---

## 19. Important implementation mechanisms

### Must understand operationally

**Frozen dataclasses**  
`TargetArtifactEnvironmentFact`, `TargetArtifactEnvironmentEvidence`, and `TargetArtifactEnvironmentProblem` are immutable typed evidence values. The important lesson is explicit evidence shape and provenance, not memorizing decorator syntax.

**Literal union states**  
Small `Literal[...]` state sets make expected evidence outcomes explicit and reviewable.

**Shared workflow intermediate representation**  
The Target module consumes already-parsed workflow structure instead of reparsing YAML. Understand producer/consumer ownership; detailed parser internals are lookup-level.

**Source spans / human-readable locators**  
Literal facts retain where they came from, improving explanation/debugging while remaining source evidence only.

**Composition of existing observers**  
Direct dependency installation uses the existing dependency-domain observer instead of duplicating command/path semantics.

**`isinstance` narrowing across typed results**  
Expected provider/domain result variants are distinguished explicitly. Learn what each branch means; exact typing syntax can remain lookup-assisted.

### Deferred / lookup-level

```text
full GitHub Actions expression evaluation
matrix expansion
reusable-workflow execution semantics
container runtime resolution
complete shell semantics
full wheel-tag compatibility derivation
packaging tag internals
actual runner image contents
```

Those should be learned when a real admitted responsibility requires them.

---

## 20. Focused tests and proof/non-proof

Primary focused test owner:

```text
tests/test_target_artifact_environment.py
```

It protects:

```text
literal runner/Python/install facts
provenance preservation
exact wheel compatibility remains unresolved
dynamic Python does not become a literal fact
wrong mapping location does not become setup-python input
multiple jobs become target-selection ambiguity
strategy/container become limitations
working-directory resolution composes with the direct-install observer
dynamic working directory preserves unresolved state
reusable workflow becomes target abstention
malformed workflow remains shared-definition problem
unavailable exact workflow remains explicit problem
invalid dependency-source path is rejected as an independent semantic input
```

The application source at this snapshot additionally demonstrates that the target-result association contract exists but is not yet populated by normal orchestration.

### What this authoring session did not prove

This learning-authoring session did **not** execute the focused tests or any broader suite.

Therefore this note does not claim a fresh PASS result.

Even when the focused tests pass, they do not prove:

```text
real workflow execution
installation success
complete target environment formation
exact wheel compatibility
artifact applicability
package exercise
behavioral compatibility
upgrade safety
```

---

## 21. Current fact, rationale, judgment, and re-entry triggers

### Current implementation fact

UpgradePilot has a bounded static target artifact-environment interpreter built on the shared GitHub Actions workflow representation. It preserves literal runner/Python facts, direct changed-source installation declaration state, exact workflow provenance, typed limitations/problems, and an explicitly unresolved exact-wheel-compatibility state.

### Evidenced rationale

Current source docstrings, focused tests, the target/artifact integration plan, and the application contract consistently preserve the boundary between static declaration evidence and stronger runtime/compatibility claims.

### Engineering judgment

The current owner is deliberately narrower than the eventual product question. That is a strength at this evidence horizon because it creates a trustworthy intermediate proposition instead of hiding uncertainty inside inferred compatibility labels.

Its main cost is that later consumers need another explicit evidence step before target-specific artifact applicability can be established.

### Reopen / extend when real pressure requires

```text
proposition-specific selection across multiple jobs
matrix expansion/evaluation
reusable-workflow source resolution
container-aware target interpretation
exact interpreter/ABI/platform compatibility evidence
runtime workflow/job evidence
installed-package/runtime-version evidence
```

Do not add those simply to make the Target model look complete.

---

## 22. Fast relearning route

Use this sequence when returning later:

```text
1. Recall: target Python declaration != target artifact environment != exact wheel compatibility.
2. Open target/artifact_environment.py and inspect the evidence/problem dataclasses.
3. Trace interpret_target_artifact_environment(...).
4. Explain why workflow YAML belongs to the shared GitHub Actions parser, not this module.
5. Trace literal runner and setup-python extraction.
6. Trace direct dependency installation through dependency/direct_install.py.
7. Inspect the literal-job test plus one ambiguity/dynamic-context test.
8. Confirm exact_wheel_compatibility_state remains unresolved.
9. Open investigation.py and verify whether target_artifact_environment_results is merely contracted or actually populated at the snapshot you are studying.
10. State what evidence would be required before artifact applicability could become stronger.
```

---

## 23. Ownership / transfer questions

Without looking at this note, explain:

1. Why is an exact target `requires-python` declaration a different proposition from a workflow's setup-python version?
2. Why does `artifact_environment.py` consume the shared workflow representation instead of parsing YAML directly?
3. Why can a workflow with multiple valid jobs produce a Target-level ambiguity rather than a workflow parse error?
4. What exactly does `dependency_installation_declaration = observed` prove?
5. Why is a dynamic working directory stronger uncertainty than simple non-observation?
6. Why can runner and Python facts be preserved even when strategy/container context is not interpreted?
7. Why does `ubuntu-22.04 + Python 3.11` not automatically establish exact wheel compatibility?
8. What is the difference between a `TargetArtifactEnvironmentProblem` and successful evidence carrying limitations?
9. Why should dependency-source identity remain attached when target environment results are composed into the application result?
10. At this snapshot, does the presence of `target_artifact_environment_results` in `PublicPullRequestInvestigation` mean the application already populates it? Why not?

Transfer exercise:

> A workflow has two jobs: one tests Python 3.11 on Ubuntu and another tests Python 3.12 on Windows. Both directly install the changed requirements file. Describe what new proposition-specific selection or multi-environment semantics UpgradePilot would need before the current single-job Target interpreter could truthfully represent this workflow, and explain why “pick the first job” would be unsound.

---

## 24. Source and evidence anchors

Pinned current horizon:

```text
main@f76e8a770320763100183454fac49893abb9ff48
```

Primary current source:

```text
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/dependency/direct_install.py
src/upgradepilot/github/workflow_definition.py
src/upgradepilot/investigation.py
```

Focused tests:

```text
tests/test_target_artifact_environment.py
```

Adjacent owner intentionally not taught deeply here:

```text
src/upgradepilot/impact/artifact_serviceability.py
```

Roadmap / integration anchors:

```text
plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md
plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md
```

Complementary existing target-Python learning snapshot:

```text
learning/2026-09-02-target-python-evidence-resolution/01_TARGET_PYTHON_EVIDENCE_RESOLUTION_CHAIN.md
```

This file is a frozen learning snapshot. It does not control the live project position, authorize the pending application composition, or claim more proof than the pinned source/tests support.

`UP-SKILL:upgradepilot-learning-artifact`
