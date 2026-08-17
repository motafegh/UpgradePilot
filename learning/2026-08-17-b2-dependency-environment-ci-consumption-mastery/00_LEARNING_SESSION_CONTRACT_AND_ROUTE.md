# B2 Dependency Environment + CI Consumption — Real-Case Mastery Contract and Route

**Created:** 2026-08-17  
**Artifact role:** bounded learning-session contract, route, and artifact home  
**Learning scope:** B2 Dependency Environment and CI Consumption Evidence through the implemented Cluster-5 boundary  
**Technical implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Primary real-case spine:** S001 — Pydantic / Soup Sieve 2.6 → 2.8.4  
**Contrast case:** S011 — Dictare / NumPy 1.26.4 → 2.4.6 inside optional extra `mlx`  
**Transfer-pressure case:** S005 — ModelArrayIO / pytest 9.0.3 → 9.1.1 through tox + uv lock machinery

## 1. Purpose and authority boundary

This folder is our dedicated learning workspace for mastering the current B2 dependency-environment and CI-consumption implementation by following **real cases, real target-project evidence, real UpgradePilot source, and real tests**.

This file controls only the teaching/learning method and internal order for this learning package. It is **not**:

- a project-status owner;
- an implementation plan;
- an architecture/specification owner;
- authorization to change product behavior;
- a replacement for source/tests;
- a replacement for `MEMORY.md`.

For live project position, always consult `../../MEMORY.md`. For the project-wide learning/execution method, `../../OPERATING_GUIDE.md` remains controlling. Historical `product-simulation/` cases are discovery evidence; they are not restarted or treated as current product behavior.

The initial snapshot boundary for this package is:

```text
Clusters 0–4: validated green
Cluster 5: source/test implementation exists at f7fcd5e2...; validation was not yet recorded in the live memory snapshot
Cluster 6 ordinary application integration: not part of the implemented path being taught here
Tranche 2 static↔runtime correlation: not selected
```

If implementation changes while we are learning, do not silently rewrite old learning artifacts. Pin the relevant artifact to the source state it teaches and create a clearly identified continuation/update when needed.

## 2. Our learning objective

The goal is not to memorize Cluster 1, 2, 3, 4, and 5 as isolated implementation history.

We will become able to reconstruct this real evidence path:

```text
PUBLIC DEPENDENCY UPDATE
        ↓
exact dependency transition
        ↓
exact dependency source / environment context
        ↓
static workflow structure
        ↓
static project-environment selection
        ↓
selected-environment membership
        ↓
static dependency consumption
        ├──→ separate direct-package exercise evidence
        ↓
separate exact-head runtime CI authority
        ↓
bounded CI coverage state
```

At every arrow we must be able to answer:

```text
What exact proposition are we trying to establish?
What evidence enters?
Which source responsibility owns the transformation?
Which function/type performs it?
What object/state comes out?
What stronger claim is still NOT justified?
Why does the real target project make this proposition meaningful?
```

The end goal is **code-and-evidence ownership**, not passive familiarity with the note.

## 3. Roles

### Ali — learner, reasoner, and eventual owner

Ali should increasingly:

- predict the next state before seeing it;
- explain why a function/type exists;
- trace important inputs and outputs;
- distinguish evidence strength and failure states;
- read the central source instead of relying on summaries;
- explain important target-project tools/configuration when they affect the evidence chain;
- challenge a result that appears too strong or too weak;
- later modify or add a focused test/diagnostic at a central boundary when useful.

Typing or approving AI-generated code is not mastery by itself.

### AI assistant — guide, navigator, and reviewer

The assistant should:

- teach through the real case before general theory;
- choose the smallest meaningful code slice that preserves the mechanism;
- open the exact source/function/test being discussed;
- explain unfamiliar syntax or technology when it becomes causally relevant;
- connect external target-project behavior to UpgradePilot's interpretation of it;
- ask Ali for predictions, explanations, or diagnoses at useful boundaries;
- correct misconceptions without jumping several conceptual layers ahead;
- distinguish what Ali must master from what only needs operational familiarity;
- progressively reduce assistance as Ali demonstrates control.

The assistant must not replace the real code/data flow with a simplified fictional example when a real case already exists.

### Source/tests — implementation truth

Current `src/upgradepilot/` plus active tests are the implementation proof owner. Learning notes explain; they do not override the code.

### Product simulation — historical manual evidence

The manual case artifacts tell us what real-world problem/evidence shape motivated the implementation and what the historical investigation observed. They are used as **case truth/provenance for learning**, not as executable product contracts.

## 4. Chunk-size rule

We proceed one **minimum-complete learning chunk** at a time.

A normal chunk should usually contain:

```text
1 primary question/proposition
+ 1 real-case evidence slice
+ 1 coherent source-code responsibility or a small connected function chain
+ the necessary supporting concept/tool context
+ 1 prediction / explanation / diagnosis from Ali
```

Do not make a chunk so small that inputs, mechanism, and output become disconnected. Do not make it so large that several independent propositions or major tools are introduced before Ali can reason about the first one.

When a function is large, stop at one meaningful responsibility branch. When several tiny helpers form one inseparable mechanism, keep them together.

We do **not** dump the whole end-to-end flow in one lecture. The full flow is the route; the conversation advances through it chunk by chunk.

## 5. The learning loop for every chunk

Use this sequence unless a simpler one is clearly better:

```text
A. REAL QUESTION
What are we trying to know in the target case?

B. REAL TARGET CONTEXT
What does Pydantic / Dictare / ModelArrayIO actually do here?
Why does this file, tool, CI job, dependency group, extra, or command exist?

C. RAW / HISTORICAL EVIDENCE
What did the product-simulation case observe?
What is observation versus interpretation?

D. UPGRADEPILOT INPUT
Which typed object/evidence enters the current code?
Show representative real values where available.

E. SOURCE WALK
Open the owning module and central function(s).
Trace important branches, helpers, invariants, and failure handling.
Do not explain every syntax line equally.

F. OUTPUT
Inspect the exact type/state/witness produced.

G. PROOF BOUNDARY
State what this output proves and what it deliberately does not prove.

H. TEST
Read at least one focused test that protects the mechanism or a critical edge.

I. ALI CHECK
Ali predicts, explains, diagnoses, compares, or later modifies/tests one central behavior.

J. CONNECT FORWARD
Only then show which next proposition consumes this result.
```

## 6. External technology rule — learn the target project, not only UpgradePilot

Whenever the real data flow crosses a tool, package, configuration format, CI mechanism, or dependency technology that materially affects interpretation, we pause and learn the **minimum complete real mechanism** needed to understand its effect.

Examples expected in this route include:

- Dependabot dependency-update PRs;
- Python package/distribution-name normalization;
- `pyproject.toml` and TOML;
- optional dependencies / extras and dependency groups;
- `uv`, `uv.lock`, universal lockfiles, project/workspace selection, `uv sync`, and `uv run` where encountered;
- GitHub Actions workflows, jobs, steps, `run`, defaults, working directories, and the difference between workflow definition and runtime run/job evidence;
- what a project's CI job is actually trying to validate and why that project has that job;
- transitive dependency graphs, nodes/edges, reachability, Breadth-First Search (BFS), `deque`, visited-state protection, and witness paths;
- Pydantic's documentation dependency path relevant to S001;
- Beautiful Soup / Soup Sieve / the selected documentation tooling when they become relevant to that path;
- Dictare's Apple-Silicon MLX optional stack and why `mlx` is conditional rather than default;
- `pip install -e ".[dev]"` versus installing an affected optional extra;
- tox and `uv-venv-lock-runner` at the operational depth required by S005;
- Python typing/dataclasses/private implementation types when they carry important semantic structure.

Rules:

1. Do not teach a technology merely because it appears by name; it must matter to the current evidence path or understanding.
2. Do not skip a material technology because UpgradePilot itself does not implement it.
3. Do not expand into a complete course on GitHub Actions, uv, tox, TOML, graph theory, etc. Learn enough to accurately reason about the real case, then return to the UpgradePilot flow.
4. If the external mechanism is still unclear after the minimum explanation, inspect the target project's exact historical configuration/evidence before proceeding.

## 7. Depth classification

At each meaningful boundary classify material into these buckets.

### MUST MASTER

Ali should eventually be able to explain, trace, test, and diagnose these with limited assistance:

- the proposition ladder and why each rung is separate;
- provenance/exact identity before semantic interpretation;
- dependency source context versus environment membership;
- optional extra / dependency group identity and selection;
- static workflow selection versus runtime execution;
- the working-directory/context precedence that changes which project file a command refers to;
- S001 `uv.lock` selected-environment reachability and its exact witness path;
- direct versus transitive membership;
- `member/supported` versus `not_established` versus `unresolved`;
- why bounded-analysis failure must not become a negative fact;
- consumption versus direct exercise versus runtime CI authority;
- exact external-consumption rebinding/provenance guards;
- why `successful exact-head CI + static consumption` currently yields `supported_not_correlated`, not matched-command runtime success;
- the central source functions/types that own those transformations;
- the focused tests that discriminate the important states;
- the current ordinary-application integration gap at the Cluster-5 boundary.

### UNDERSTAND OPERATIONALLY

Ali should confidently recognize and reason with these without needing to reimplement their internals:

- GitHub Actions provider syntax beyond the fields UpgradePilot reads;
- uv's broader resolver/lock implementation;
- TOML parser internals;
- tox internals and runner plugin internals beyond the S005 mediation path;
- MLX internals beyond understanding why Dictare has an Apple-Silicon optional stack;
- Beautiful Soup / Soup Sieve internals beyond their dependency/use relationship relevant to S001;
- general graph-algorithm theory beyond what explains our bounded traversal.

### DEFER DELIBERATELY

Unless a real code branch forces us there, defer:

- universal package-manager modeling;
- generic CI-provider architecture;
- full GitHub Actions expression/matrix/reusable-workflow execution semantics;
- generic shell interpretation;
- universal dependency graph abstraction;
- static↔runtime step/job correlation (Tranche 2);
- resolver-satisfiability conclusions beyond the separately admitted future gate;
- behavioral compatibility/safety/action synthesis beyond the selected responsibility.

## 8. Artifact rules for this folder

All reusable learning artifacts produced by this learning track belong under this folder unless another existing durable learning owner is clearly better.

Use numbered names in learning order, for example:

```text
00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
01_S001_REAL_CASE_AND_DEPENDENCY_ENVIRONMENT.md
02_S001_WORKFLOW_SELECTION_CODE_TRACE.md
03_S001_UV_MEMBERSHIP_CODE_TRACE.md
04_CLUSTER5_CI_CONSUMPTION_AND_COVERAGE_TRACE.md
05_S011_OPTIONAL_EXTRA_CONTRAST.md
06_S005_TOX_UV_TRANSFER_PRESSURE.md
07_SESSION1_MASTERY_CHECK.md
```

These filenames are illustrative, not mandatory paperwork. Create an artifact only when it preserves reusable understanding, a corrected misconception, a meaningful code trace, or an ownership exercise that would otherwise be lost.

Each substantive artifact should record:

- source/test commit or exact files it teaches;
- real case/evidence references;
- accurate mental model;
- central source functions/types;
- inputs → transformation → outputs;
- proof limits/failure states;
- target-project/tool context that matters;
- mastery depth actually demonstrated;
- unresolved/deferred depth.

Do not duplicate live project status here. Do not copy whole source files or whole simulation artifacts into learning notes; link to and quote only the exact relevant pieces.

## 9. Session 1 — full real-case journey through the current implemented point

### Session-1 objective

By the end of Session 1, Ali should be able to walk a real dependency update from the manual target evidence through the implemented Cluster-5 domain/CI machinery and explain where the current product flow still stops.

We use **S001 as the continuous positive spine**, not a sequence of artificial fixtures. S011 then proves that Ali's model can distinguish a real non-selection case. S005 checks that the model does not overfit to direct `uv sync` syntax.

### Chunk 1 — S001 before UpgradePilot: understand the real project situation

Start from:

```text
pydantic/pydantic
PR #13432
Soup Sieve 2.6 → 2.8.4
changed source: uv.lock
```

Inspect the manual S001 case/evidence and establish:

- why Soup Sieve exists in the relevant Pydantic dependency path;
- why the relevant environment is documentation-related rather than "everything in uv.lock";
- what CI/doc workflow question the historical case was actually asking;
- observation versus interpretation versus later decision.

Teach the target-side packages/tools encountered here before touching our membership code.

**Stop condition:** Ali can explain why `Soup Sieve appears in uv.lock` does not mean `the relevant CI environment consumes Soup Sieve`.

### Chunk 2 — exact dependency change + source context

Trace the current dependency analysis/change/source-context path that turns exact PR/file evidence into a canonical dependency transition plus typed source context.

Focus on:

```text
DependencyVersionChange
DependencyChangeAnalysis.source_contexts
UvLockDependencyContext
```

Understand package normalization, exact source identity, and why a universal lock source is not yet an environment-membership claim.

**Stop condition:** Ali can state the input/output and proof boundary of the canonical change + source context.

### Chunk 3 — real GitHub Actions workflow structure and project-environment selection

Inspect the exact S001 workflow evidence and first learn what that workflow/job is for in Pydantic.

Then follow:

```text
RepositoryTextFile
→ provider-owned GitHub Actions static workflow IR
→ RunStepDefinition / effective working-directory context
→ observe_project_environment_selection(...)
→ ProjectEnvironmentSelectionDeclaration
```

Study the selector types and the shared working-directory precedence.

**Stop condition:** Ali can read a relevant run command and predict the typed selection without claiming it executed.

### Chunk 4 — `pyproject.toml` + `uv.lock`: two evidence owners for one membership question

Before code traversal, learn why both files are required:

```text
pyproject.toml → selected environment identity / project metadata
uv.lock        → exact resolved package relationships
```

Then inspect the bounded parsers and exact-source/provenance validation performed before semantic use.

**Stop condition:** Ali can explain why one file alone cannot safely answer the full selected-environment membership proposition.

### Chunk 5 — S001 graph traversal and witness

Trace `evaluate_uv_selected_environment_membership(...)` through the central internal stages:

```text
validate exact source identity
→ parse project
→ parse lock
→ bind exact workspace package
→ convert selector into selected roots
→ traverse selected roots
→ return membership state + witness
```

Use the real S001 witness:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Learn node/edge modeling, BFS-style `deque` traversal, visited protection, path/depth bounds, direct versus transitive membership, and why analysis limits yield `unresolved` rather than false.

**Stop condition:** Ali can manually narrate the witness path and explain the relevant traversal code and state transitions.

### Chunk 6 — from dependency membership to CI static consumption

Trace Cluster-5 composition:

```text
selected-environment membership
→ dependency/environment_membership.py where applicable
→ compose_project_environment_consumption(...)
→ StaticDependencyConsumptionEvidence
```

Understand why Dependency owns extra/group membership and CI only consumes that domain fact.

Inspect the exact package/workflow/job/step/command/segment rebinding checks that prevent valid evidence from being attached to the wrong static location.

**Stop condition:** Ali can explain why a supported membership witness still needs exact CI provenance/location binding before becoming CI consumption evidence.

### Chunk 7 — whole-workflow inspection + CI coverage result

Trace:

```text
inspect_workflow_dependency_evidence(...)
→ consumption evidence
+ direct package invocation locations
+ structural/source problems

then

evaluate_dependency_ci_coverage(...)
```

Keep these axes independent:

```text
STATIC CONSUMPTION
STATIC DIRECT EXERCISE
RUNTIME AUTHORITY
```

For S001, understand why transitive docs-environment consumption can be supported while direct Soup Sieve exercise remains `not_established`.

Then combine separate successful exact-head CI authority only to the strength actually justified:

```text
successful exact-head CI
+ supported static consumption
→ supported_not_correlated
```

**Stop condition:** Ali can explain exactly what remains uncorrelated and why green CI cannot upgrade the claim by itself.

### Chunk 8 — S011 contrast: same machinery, different answer

Switch to the real Dictare case:

```text
numpy 1.26.4 → 2.4.6
inside [project.optional-dependencies].mlx

normal PR/macOS test workflows:
pip install -e ".[dev]"
```

Learn first:

- what a Python optional extra is;
- what Dictare's MLX/Apple-Silicon stack is for;
- why `mlx` is a real activation path despite being optional;
- why a macOS CI job does not automatically mean the MLX dependency environment exists.

Then predict and trace:

```text
affected extra = mlx
selected extra = dev
→ not_established
```

and its downstream CI-coverage consequence.

**Stop condition:** Ali can contrast `not_established` here with an `unresolved` analysis failure and can explain why green standard CI is non-discriminating for this affected extra.

### Chunk 9 — S005 transfer pressure: do not overfit the architecture to direct uv commands

Use the real ModelArrayIO case:

```text
pytest 9.0.3 → 9.1.1
changed source: uv.lock

tox latest environments
→ uv-venv-lock-runner
→ pytest
```

Learn tox and the uv lock runner only to the operational depth needed to see the mediated environment-formation path.

Ask:

> Would an architecture that equates `uv.lock consumption` with seeing direct `uv sync` in a GitHub Actions run step generalize to this case?

The expected lesson is architectural, not automatic implementation support. If current code does not interpret this mediation, preserve that boundary instead of pretending it does.

**Stop condition:** Ali can explain why S005 is transfer pressure and where current support should abstain/defer rather than overclaim.

### Chunk 10 — current application boundary: where the real flow stops today

Finally inspect the ordinary orchestration path in `src/upgradepilot/investigation.py` and the relevant CLI/tests.

Contrast:

```text
implemented typed Cluster-5 dependency/CI machinery
```

with:

```text
ordinary application path still using the legacy CI evaluator before Cluster-6 migration
```

This is essential: a domain function existing and passing focused tests does not mean the normal public-PR application already calls it.

**Stop condition:** Ali can identify the integration seam and explain what is implemented versus what the ordinary application has not yet adopted at this snapshot.

### Chunk 11 — Session-1 ownership check

Without following the note line-by-line, Ali reconstructs the flow for S001 and predicts S011.

Minimum checks:

1. Given exact S001 input/evidence, name the key typed object produced at each proposition boundary.
2. Explain the real Pydantic docs/environment path and the witness to Soup Sieve.
3. Explain `member`, `not_established`, and `unresolved` with one real or code-grounded example each.
4. Explain static declaration, static consumption, direct exercise, and runtime authority as separate propositions.
5. Diagnose at least one intentionally altered input: wrong workflow revision, wrong group/extra, dynamic selector, or changed package identity.
6. Read one central focused test and predict its outcome before reading the assertion.
7. Explain why S005 prevents a direct-`uv sync`-only mental model.
8. Point to the current application integration seam rather than claiming end-to-end CLI support that is not present.

If useful, Ali then makes one small learning-only prediction/test exercise. Product code is not changed merely to complete a learning ceremony.

## 10. How later sessions extend this route

Session 1 establishes the current end-to-end mental model and source ownership through the implemented Cluster-5 boundary.

Later sessions should be chosen from demonstrated gaps, for example:

- deeper code mastery of one central module;
- focused test-writing/diagnosis practice;
- changed-case transfer across a different group/extra/workspace shape;
- Cluster-5 validation review if it becomes relevant;
- Cluster-6 integration learning after that implementation actually exists;
- resolver-satisfiability evidence only when the selected project work admits that responsibility.

Do not pre-create a curriculum for speculative future implementation.

## 11. Success condition for this learning track

This track is successful when Ali can move through the real code/evidence chain and answer, without relying on memorized prose:

```text
What do we know?
Why do we know it?
Which exact evidence/source owns it?
Which function/type transforms it?
What state/witness comes out?
What does that state NOT prove?
How would the answer change for S011 or another credible variation?
Where does the current product integration actually stop?
```

That is the mastery target. The number of files read or chunks completed is not the target.
