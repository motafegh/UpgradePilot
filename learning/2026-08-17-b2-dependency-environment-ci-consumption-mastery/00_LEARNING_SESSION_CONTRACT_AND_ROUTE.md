# B2 Dependency Environment + CI Consumption — Real-Case Mastery Contract and Route

**Created:** 2026-08-17  
**Revised:** 2026-08-17 — background-first / first-contact, learning-plan anti-drift, pace/momentum, and learner-question handling rules added  
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

But we do **not** begin each step at the UpgradePilot abstraction. Before using a new real-world object or term in that chain, we first make it understandable enough to connect with the problem.

At every important step we should be able to answer, in this order:

```text
What is this thing in the real software world?
Why does this project use it?
What does it look like in THIS real case?
What problem/question does it create for us?
Why is the next UpgradePilot mechanism useful for that problem?
What exact proposition are we trying to establish?
What evidence enters?
Which source responsibility owns the transformation?
Which function/type performs it?
What object/state comes out?
What stronger claim is still NOT justified?
```

The end goal is **connected code-and-evidence ownership**, not passive familiarity with the note or memorized function names.

## 3. Roles

### Ali — learner, reasoner, and eventual owner

Ali should increasingly:

- connect a new technical object to its real purpose before reasoning about our abstraction of it;
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
- **go enough steps backward before a new subject so Ali can connect to it, understand the problem it creates, and understand why the solution helps**;
- treat first contact with a material package/tool/file/configuration/CI concept as a teaching boundary rather than assuming familiarity;
- show the real target-project example or historical fragment whenever available instead of only describing the abstraction;
- choose the smallest meaningful code slice that preserves the mechanism;
- open the exact source/function/test being discussed;
- explain unfamiliar syntax or technology when it becomes causally relevant;
- connect external target-project behavior to UpgradePilot's interpretation of it;
- ask Ali for predictions, explanations, or diagnoses at useful boundaries;
- correct misconceptions without jumping several conceptual layers ahead;
- distinguish what Ali must master from what only needs operational familiarity;
- progressively reduce assistance as Ali demonstrates control.

The assistant must not replace the real code/data flow with a simplified fictional example when a real case already exists.

The assistant must also not use shorthand such as `docs CI`, `lockfile`, `extra`, `workflow job`, `transitive dependency`, or a package name as though its practical meaning is already secure. If the term is new or only weakly familiar, briefly establish it first.

### Source/tests — implementation truth

Current `src/upgradepilot/` plus active tests are the implementation proof owner. Learning notes explain; they do not override the code.

### Product simulation — historical manual evidence

The manual case artifacts tell us what real-world problem/evidence shape motivated the implementation and what the historical investigation observed. They are used as **case truth/provenance for learning**, not as executable product contracts.

## 4. Background-first and first-contact rule

This is mandatory for this learning track.

When a material subject appears for the first time, do **not** immediately use it as a premise in UpgradePilot reasoning. First establish enough background to make the current problem intuitive.

Examples:

```text
soupsieve
uv.lock
pyproject.toml
GitHub Actions
CI
"docs CI"
optional extra
dependency group
transitive dependency
BFS
tox
uv-venv-lock-runner
```

For first contact, use the smallest useful backward-context ladder:

```text
1. WHAT IS IT?
   Plain technical definition, full name where relevant, and what category it belongs to.

2. WHY DOES IT EXIST / WHAT JOB DOES IT DO?
   The practical problem it solves in software projects generally.

3. WHY DOES THIS TARGET PROJECT USE IT?
   Pydantic / Dictare / ModelArrayIO-specific purpose.

4. WHAT DOES IT LOOK LIKE HERE?
   Show the exact historical file fragment, command, structure, dependency edge, workflow step,
   or representative real value from the frozen case whenever available.

5. WHAT PARTS OF IT MATTER NOW?
   Briefly identify the structure/fields/components we must understand now and defer the rest.

6. WHY DOES IT MATTER TO OUR QUESTION?
   Connect the real-world mechanism to the evidence problem UpgradePilot must solve.

7. ONLY THEN ENTER OUR CODE.
```

This rule is intentionally broader than UpgradePilot source code. The purpose is to let Ali first **connect with the issue**, then understand the actual problem, then understand the solution and **why the solution helps**.

The same rule applies to smaller mechanisms, not only headline concepts. For example, if a workflow uses `working-directory`, an editable install, a selector flag, or a lockfile field that materially changes interpretation, briefly establish what that smaller mechanism does before relying on it.

### Background depth limit

Background-first does **not** mean exhaustive background.

Teach enough backward context to make the current causal chain accurate and understandable, then return to the real case. Avoid both failures:

```text
TOO SHALLOW:
name-drop the concept and continue

TOO DEEP:
turn every encountered tool/package into a full independent course
```

The correct depth is:

```text
minimum complete background
→ real example
→ current problem
→ why our mechanism helps
```

If the background itself contains another unfamiliar prerequisite, go back only as far as necessary to make the current subject coherent. Do not recursively open many unrelated concepts at once.

## 5. Chunk-size and anti-jump rule

We proceed one **minimum-complete learning chunk** at a time.

A normal chunk should usually contain:

```text
1 primary real question
+ the minimum background needed for that question
+ 1 real-case evidence slice
+ at most 1 main new mechanism/concept family
+ 1 coherent source-code responsibility OR preparation for that source responsibility
+ 1 prediction / explanation / diagnosis from Ali
```

Do not make a chunk so small that inputs, mechanism, and output become disconnected. Do not make it so large that several independent propositions or several unfamiliar technologies are introduced before Ali can reason about the first one.

If two unfamiliar concepts depend on each other, normally teach them sequentially rather than naming both and moving on. Example:

```text
first: what Soup Sieve is and why Pydantic has it
then: what uv.lock is and how Soup Sieve appears there
then: what CI/docs CI is and why a docs workflow can consume that environment
then: how UpgradePilot models those facts
```

When a function is large, stop at one meaningful responsibility branch. When several tiny helpers form one inseparable mechanism, keep them together.

We do **not** dump the whole end-to-end flow in one lecture. The full flow is the route; the conversation advances through it chunk by chunk.

## 6. The learning loop for every chunk

Use this sequence unless a simpler one is clearly better:

```text
A. ORIENT / STEP BACK
What new thing are we about to rely on?
What minimum background does Ali need first?

B. FIRST-CONTACT BACKGROUND
What is it?
Why does it exist?
What does it normally do?

C. REAL TARGET EXAMPLE
What does it look like in the exact Pydantic / Dictare / ModelArrayIO case?
Show the real fragment/command/structure when available.

D. REAL QUESTION / PROBLEM
What are we actually trying to know, and why is the raw real-world evidence insufficient by itself?

E. RAW / HISTORICAL EVIDENCE
What did the product-simulation case observe?
What is observation versus interpretation?

F. WHY OUR NEXT MECHANISM HELPS
Before source code, explain the missing relation/proposition the UpgradePilot mechanism is designed to establish.

G. UPGRADEPILOT INPUT
Which typed object/evidence enters the current code?
Show representative real values where available.

H. SOURCE WALK
Open the owning module and central function(s).
Trace important branches, helpers, invariants, and failure handling.
Do not explain every syntax line equally.

I. OUTPUT
Inspect the exact type/state/witness produced.

J. PROOF BOUNDARY
State what this output proves and what it deliberately does not prove.

K. TEST
Read at least one focused test that protects the mechanism or a critical edge when source has been introduced.

L. ALI CHECK
Ali predicts, explains, diagnoses, compares, or later modifies/tests one central behavior.

M. CONNECT FORWARD
Only then show which next proposition consumes this result.
```

Not every chunk needs source code. Early chunks may exist specifically to make the real case/tool/file understandable before our code appears.

## 7. External technology rule — learn the target project, not only UpgradePilot

Whenever the real data flow crosses a tool, package, configuration format, CI mechanism, or dependency technology that materially affects interpretation, we pause and learn the **minimum complete real mechanism** needed to understand its effect.

Examples expected in this route include:

- Dependabot dependency-update PRs;
- Soup Sieve itself: what it is, what it does, and why it appears in Pydantic's documentation dependency path;
- Beautiful Soup and the specific dependency relation relevant to S001;
- Python package/distribution-name normalization;
- `pyproject.toml` and TOML;
- optional dependencies / extras and dependency groups;
- `uv`: what role it plays as a Python project/package environment tool;
- `uv.lock`: why lockfiles exist, why uv uses a universal lock, its major structure at the depth needed here, and the exact S001/S005 fragments we reason from;
- project/workspace selection, `uv sync`, and `uv run` where encountered;
- CI (Continuous Integration) itself at the practical depth needed here;
- GitHub Actions workflows, jobs, steps, `run`, defaults, working directories, and the difference between workflow definition and runtime run/job evidence;
- **docs CI / documentation CI**: a CI workflow/job whose responsibility is to install/build/check a project's documentation toolchain, why a project such as Pydantic has it, and why passing docs CI can be relevant to a documentation-only dependency without proving unrelated runtime behavior;
- what each inspected project's CI job is actually trying to validate and why that project has that job;
- transitive dependency graphs, nodes/edges, reachability, Breadth-First Search (BFS), `deque`, visited-state protection, and witness paths;
- Pydantic's documentation dependency path relevant to S001;
- Dictare's Apple-Silicon MLX optional stack and why `mlx` is conditional rather than default;
- `pip install -e ".[dev]"` versus installing an affected optional extra;
- tox and `uv-venv-lock-runner` at the operational depth required by S005;
- Python typing/dataclasses/private implementation types when they carry important semantic structure.

Rules:

1. A material new package/tool/configuration is never merely name-dropped on first contact. Give the background-first treatment before using it in reasoning.
2. Do not teach a technology merely because it appears by name; it must matter to the current evidence path or understanding.
3. Do not skip a material technology because UpgradePilot itself does not implement it.
4. Prefer the target project's exact historical file/command/structure over a generic invented example when available.
5. For structured files such as `uv.lock`, `pyproject.toml`, or workflow YAML, show the relevant real structure and briefly identify its parts before discussing our parser/model of it.
6. Do not expand into a complete course on GitHub Actions, uv, tox, TOML, graph theory, etc. Learn enough to accurately reason about the real case, then return to the UpgradePilot flow.
7. If the external mechanism is still unclear after the minimum explanation, inspect the target project's exact historical configuration/evidence before proceeding.

## 8. Depth classification

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

- Soup Sieve's practical selector role and its relation to Beautiful Soup in the S001 path, without reimplementing Soup Sieve;
- why lockfiles exist and the relevant `uv.lock` structure/semantics, without mastering uv's resolver internals;
- CI/GitHub Actions concepts required to understand the inspected jobs, including what a docs CI job is for;
- GitHub Actions provider syntax beyond the fields UpgradePilot reads;
- TOML parser internals;
- tox internals and runner plugin internals beyond the S005 mediation path;
- MLX internals beyond understanding why Dictare has an Apple-Silicon optional stack;
- general graph-algorithm theory beyond what explains our bounded traversal.

### DEFER DELIBERATELY

Unless a real code branch forces us there, defer:

- Soup Sieve parser/selector-engine implementation internals;
- uv's full resolver and lock-generation algorithms;
- universal package-manager modeling;
- generic CI-provider architecture;
- full GitHub Actions expression/matrix/reusable-workflow execution semantics;
- generic shell interpretation;
- universal dependency graph abstraction;
- static↔runtime step/job correlation (Tranche 2);
- resolver-satisfiability conclusions beyond the separately admitted future gate;
- behavioral compatibility/safety/action synthesis beyond the selected responsibility.

## 9. Learning-plan system — role, required contents, and anti-drift rules

The learning plans under this folder are **subordinate execution maps** for this contract. Their job is to keep the conversation oriented across many chunks so that subtle but important contract obligations are not forgotten when we are deep in code or a real-case tangent.

A learning plan is **not**:

- a replacement for this contract;
- a project implementation plan;
- authorization to modify product behavior;
- a new architecture/specification owner;
- implementation truth;
- a replacement for `MEMORY.md` as live project-position owner.

If a plan conflicts with this contract, this contract wins. If source/tests conflict with a learning plan's technical expectation, inspect the source/tests and correct the plan or create a pinned continuation rather than teaching the plan as truth.

### 9.1 Plan sizing and boundaries

Each plan should cover one coherent learning arc and contain a **proper number of chunks** for that arc.

Avoid both extremes:

```text
ONE GIANT PLAN
→ too easy to drift, too many distant reminders, weak local gates

ONE FILE PER TINY CHUNK
→ ceremony, fragmentation, loss of the end-to-end connection
```

A plan should normally end at a natural conceptual/evidence gate such as:

- real-case/background understanding is secure enough to enter our code;
- one coherent source responsibility has been traced and tested;
- one proof rung has been established and its boundary understood;
- a contrast/transfer case has tested whether the mental model generalizes;
- the implemented application boundary has been reached.

Plan boundaries follow **learning coherence**, not implementation Cluster numbers automatically.

### 9.2 Required contents of every learning plan

Every plan should contain, proportionately:

1. **Identity and scope**
   - plan purpose;
   - real case(s) used;
   - relevant implementation/source snapshot when source is involved;
   - where this plan begins and where it deliberately stops.

2. **Why this plan exists**
   - the connection/problem it is intended to make understandable;
   - prerequisite state expected from the previous plan;
   - what later reasoning would be weak if this plan were skipped.

3. **Chunk map**
   - numbered chunks;
   - main subject/question of each chunk;
   - only the main learning subjects, not a prewritten lecture;
   - expected real-case evidence or target-project material;
   - expected UpgradePilot source responsibility when applicable.

4. **First-contact/background reminders**
   - name material new packages, tools, files, commands, CI concepts, syntax, or mechanisms likely to appear;
   - flag which ones need the contract's background-first treatment before they may be used as premises;
   - do not fully teach them inside the plan.

5. **Source/code map**
   - likely source modules;
   - central classes/types/functions/helpers worth reading;
   - focused tests or test families that protect the mechanism;
   - target-project files/configuration/workflows that supply the real inputs.

6. **Subtle do-not-miss reminders**
   - short reminders for important distinctions that are easy to skip while talking;
   - especially proof boundaries, provenance/identity, target-project purpose, state distinctions, static-versus-runtime distinctions, and external-tool behavior that materially affects interpretation;
   - reminders should say what must not be silently assumed, not contain the full explanation.

7. **TODO/checklist**
   - chunks and material checkpoints should be trackable;
   - use local markers such as `[ ]`, `[~]`, and `[x]` when useful;
   - these markers track this learning package only and do not replace project live state.

8. **Gates / stop conditions**
   - each major chunk or chunk group should have an observable understanding/ownership gate;
   - a gate should normally require Ali to explain, predict, compare, trace, diagnose, or later modify/test something meaningful;
   - recognition immediately after an explanation is not enough for mastery;
   - gates are normally **sufficient-to-proceed gates**, not demands for perfect or exhaustive mastery before movement.

9. **Depth and deferral**
   - call out main items expected to be MUST MASTER versus UNDERSTAND OPERATIONALLY when material;
   - record nearby depth deliberately deferred so a tangent does not silently expand the route.

10. **Pace / fast path**
    - identify the minimum understanding required to move safely into the next chunk or source responsibility;
    - identify which gaps can remain `[~]` and be revisited just-in-time;
    - state what kind of misconception would actually block progress and trigger a repair;
    - do not require optional deepening before continuing the build-oriented route.

11. **Completion / handoff condition**
    - state what Ali should be able to connect or reconstruct before the next plan begins;
    - state the next plan's dependency without pre-teaching its details;
    - where useful, state what implementation/building work this learning now makes safer or more intelligible.

### 9.3 Per-chunk plan entry shape

A plan's chunk entry should usually be compact and look conceptually like:

```text
Chunk N — Main subject / real question

Main subjects:
- ...

Real case / target material:
- ...

Background-first flags:
- ...

UpgradePilot source/functions/tests:
- ...

Do not miss / do not assume:
- ...

Ali gate:
- ...

Pace / proceed when:
- ...

Status: [ ]
```

Not every field needs many bullets. The purpose is recall and routing, not bureaucracy.

### 9.4 Anti-drift checklist for plans and live teaching

Before beginning a planned chunk, the assistant should quickly re-read that chunk's plan entry and check:

```text
Are we still answering the planned real question?
Is there a new material term/tool/package we are about to assume instead of teach first?
Have we shown the real target example before our abstraction where available?
Are we jumping across more than one major unfamiliar mechanism?
Do we know which real source/function/test will carry this chunk, if source is part of it?
Are we preserving the proposition/proof boundary rather than jumping to a stronger conclusion?
Is there a subtle plan reminder we have not yet covered?
Are we spending more depth here than the next real step actually requires?
What is the Ali gate before we continue?
```

At the end of a chunk, check:

```text
Was the main question actually answered?
Can Ali connect background → real case → problem → our mechanism?
Was the important code/data flow traced at the planned depth?
Did we state what the result does NOT prove?
Did Ali perform the planned ownership action?
Is any confusion truly blocking the next step, or can it be marked [~] and revisited when causally relevant?
```

If a **blocking** gate is not met, briefly repair that chunk before moving on. If the remaining gap is non-blocking, mark it `[~]`, preserve what should be revisited, and continue rather than converting the gate into a perfection loop.

### 9.5 What plans should deliberately NOT contain

Do not turn plans into prewritten textbooks. They should not contain:

- exhaustive explanations of every future concept;
- copied whole source files or whole simulation artifacts;
- detailed line-by-line code commentary before we reach the code;
- invented target-project examples when exact real evidence is available;
- speculative function behavior not checked against the pinned source;
- giant vocabulary lists unrelated to the current causal chain;
- premature solutions to questions Ali should reason through during the session.

The plan preserves the **route, important reminders, sources, and gates**. The actual learning happens interactively, chunk by chunk.

### 9.6 Plan lifecycle and change rule

Plans are written from the best inspected evidence available at creation time.

- Pin source-sensitive plans to a commit/snapshot when appropriate.
- If implementation changes materially, do not silently reinterpret an old plan as current truth.
- Make the smallest justified plan correction when only routing/wording was wrong.
- Create a clearly identified continuation/update when the technical path materially changed.
- Do not create plan files until Ali has approved the proposed plan breakdown when approval is explicitly pending.

### 9.7 Pace, momentum, and return-to-building rule

This learning track exists **in service of the ongoing learning-by-doing build**. It must improve our ability to make the next implementation decisions; it must not become a long prerequisite curriculum that delays the project until every surrounding concept feels complete.

The default operating principle is:

```text
learn the minimum complete causal mechanism
→ verify one meaningful understanding/ownership check
→ move to the next real evidence/code boundary
→ deepen later when the build actually requires it
```

Use three practical gate states:

```text
GREEN
Core relation is understood well enough to reason safely about the next step.
Proceed.

YELLOW / [~]
There is a real but non-blocking gap, weak recall, or optional depth still worth revisiting.
Record it and proceed; revisit when the next code/problem makes it relevant.

RED
A misconception or missing prerequisite would make the next interpretation/code reasoning materially wrong.
Repair only that blocking part, then resume forward movement.
```

Momentum rules:

1. **No perfection prerequisite.** MUST MASTER means eventual ownership across the route, not that every item must be perfected before touching the next source file.
2. **One meaningful check is normally enough to proceed.** Do not repeatedly drill the same point unless the check exposes a causal misunderstanding.
3. **Background stays just-in-time.** Teach enough to make the current real case and next source responsibility coherent; defer adjacent theory.
4. **Touch real evidence and code early and repeatedly.** Do not spend a long sequence of sessions only discussing terminology when the next real artifact can safely anchor the concept.
5. **Do not finish every nearby topic before building.** A recorded `[~]` is acceptable when the missing depth is not required for the next implementation decision.
6. **Prefer forward reconstruction over repeated recap.** Revisit older material when a later mechanism actually depends on it, which provides spaced reinforcement without stopping momentum.
7. **Plans are not a queue that must be exhausted before implementation resumes.** When the current learning has made the next authorized building step understandable and safe, return to building; continue the remaining learning just-in-time alongside future implementation.
8. **Re-anchor when the project moves.** If main implementation advances and a later plan is now behind the useful frontier, inspect the new state and adapt the remaining learning route instead of completing obsolete study for its own sake.
9. **No arbitrary time quota is required.** Pace is determined by causal necessity and demonstrated understanding, not by filling a fixed number of sessions or spending a predetermined duration on a topic.
10. **Every plan should point forward.** Its completion/handoff should make clear what next code, implementation decision, or future project responsibility the learned material enables us to approach with better judgment.

The balance we want is:

```text
not blind speed
not academic completeness

but:
accurate enough → evidence-backed → user understands the important mechanism → keep building
```

## 10. Artifact rules for this folder

All reusable learning artifacts produced by this learning track belong under this folder unless another existing durable learning owner is clearly better.

Use numbered names in learning order. Learning-plan files should use a clear `PLAN_` or numbered plan naming scheme once their breakdown is approved. Other learning artifacts may follow the learned route, for example:

```text
00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
PLAN_01_...
PLAN_02_...
01_S001_REAL_CASE_BACKGROUND.md
02_S001_UV_LOCK_AND_ENVIRONMENT_BACKGROUND.md
03_S001_DOCS_CI_AND_WORKFLOW_BACKGROUND.md
04_S001_DEPENDENCY_SOURCE_CONTEXT_CODE_TRACE.md
05_S001_WORKFLOW_SELECTION_CODE_TRACE.md
06_S001_UV_MEMBERSHIP_CODE_TRACE.md
07_CLUSTER5_CI_CONSUMPTION_AND_COVERAGE_TRACE.md
08_S011_OPTIONAL_EXTRA_CONTRAST.md
09_S005_TOX_UV_TRANSFER_PRESSURE.md
10_SESSION1_MASTERY_CHECK.md
```

These filenames are illustrative, not mandatory paperwork. Create an artifact only when it preserves reusable understanding, a corrected misconception, a meaningful code trace, a learning plan, or an ownership exercise that would otherwise be lost.

Each substantive learning artifact should record, where relevant:

- source/test commit or exact files it teaches;
- real case/evidence references;
- accurate mental model;
- important background concepts first encountered there;
- exact target-project fragment/command/structure when it materially supports understanding;
- central source functions/types when source is part of that artifact;
- inputs → transformation → outputs;
- proof limits/failure states;
- target-project/tool context that matters;
- mastery depth actually demonstrated;
- unresolved/deferred depth.

Do not duplicate live project status here. Do not copy whole source files or whole simulation artifacts into learning notes; link to and quote only the exact relevant pieces.

## 11. Session 1 — full real-case journey through the current implemented point

### Session-1 objective

By the end of Session 1, Ali should be able to walk a real dependency update from the manual target evidence through the implemented Cluster-5 domain/CI machinery and explain where the current product flow still stops.

We use **S001 as the continuous positive spine**, not a sequence of artificial fixtures. S011 then proves that Ali's model can distinguish a real non-selection case. S005 checks that the model does not overfit to direct `uv sync` syntax.

The opening is deliberately slower than the original contract, but it must remain compact. We first understand the real-world objects that make S001 meaningful, then enter UpgradePilot source without turning those first contacts into standalone courses.

### Chunk 1 — S001 orientation + first contact with Soup Sieve

Start only from the real event:

```text
pydantic/pydantic
PR #13432
Soup Sieve 2.6 → 2.8.4
```

Before discussing `uv.lock`, CI, graph traversal, or UpgradePilot types, establish:

- what Pydantic is at the level needed for this case;
- what Soup Sieve is;
- what CSS-selector matching means at a practical level;
- how Soup Sieve relates to Beautiful Soup;
- why a Pydantic repository can contain Soup Sieve even though Pydantic's normal runtime does not directly depend on it;
- the exact S001 documentation-tooling relationship discovered manually.

Use the frozen S001 evidence, not an invented dependency story.

**Sufficient-to-proceed condition:** Ali can explain in his own words what Soup Sieve does and why its presence in Pydantic can be documentation/tooling-related rather than core runtime use. Do not require deeper Soup Sieve knowledge before moving on.

### Chunk 2 — first contact with `uv` and `uv.lock`

Only after Soup Sieve itself makes sense, introduce `uv` and its lockfile.

Teach briefly:

- what a Python package/project environment tool does;
- what dependency resolution means;
- why lockfiles exist;
- what `uv.lock` is;
- why uv calls it a universal/cross-environment lock rather than a list of packages for one single CI job;
- the major structure relevant to us: package records, versions, dependency edges, optional/dev/group-related relationships, source information, and markers where present;
- the **exact historical S001 `uv.lock` fragments** for the Pydantic workspace/docs chain and Soup Sieve record;
- later, when useful, compare those with the S005 lock case.

Do not teach the full uv resolver.

**Sufficient-to-proceed condition:** Ali can look at the relevant real lock fragments and explain why `soupsieve appears in uv.lock` does not yet tell us which environment selected/installed it. Resolver internals remain deferred.

### Chunk 3 — first contact with CI, GitHub Actions, and “docs CI”

Do not assume `docs CI` is familiar terminology.

Teach in sequence:

```text
CI = Continuous Integration
→ why repositories run automated checks on changes
→ GitHub Actions as one CI/workflow platform
→ workflow
→ job
→ step
→ run command
→ documentation-specific job/workflow
→ "docs CI"
```

Then inspect the exact historical Pydantic workflow evidence and explain:

- what Pydantic's documentation job/workflow is trying to validate;
- why it needs documentation dependencies;
- how documentation CI differs from normal runtime tests conceptually;
- why a passing docs workflow can be relevant to Soup Sieve while still not proving unrelated Pydantic runtime behavior;
- what the historical S001 investigation wanted to know about that workflow.

**Sufficient-to-proceed condition:** Ali can explain what `docs CI` means, why Pydantic has it, and why its dependency environment is relevant to Soup Sieve. Full GitHub Actions knowledge is not required.

### Chunk 4 — exact dependency change + source context

Now enter UpgradePilot source for the first time in this route.

Trace the current dependency analysis/change/source-context path that turns exact PR/file evidence into a canonical dependency transition plus typed source context.

Focus on:

```text
DependencyVersionChange
DependencyChangeAnalysis.source_contexts
UvLockDependencyContext
```

Understand package normalization, exact source identity, and why a universal lock source is not yet an environment-membership claim.

Before each type/function is used, explain the real-world fact it is preserving and why plain strings/booleans would lose useful evidence.

**Sufficient-to-proceed condition:** Ali can state the input/output and proof boundary of the canonical change + source context. Incidental implementation syntax may remain `[~]` unless it affects the mechanism.

### Chunk 5 — real GitHub Actions workflow structure and project-environment selection

Return to the exact S001 workflow now that CI/docs CI is already understood.

Follow:

```text
RepositoryTextFile
→ provider-owned GitHub Actions static workflow IR
→ RunStepDefinition / effective working-directory context
→ observe_project_environment_selection(...)
→ ProjectEnvironmentSelectionDeclaration
```

Before using `working-directory`, selector flags, or static workflow IR as premises, briefly explain what each means in normal workflow execution and show the real relevant command/structure.

Study the selector types and the shared working-directory precedence.

**Sufficient-to-proceed condition:** Ali can read the relevant real run command and predict the typed selection without claiming it executed. Exhaustive provider syntax remains deferred.

### Chunk 6 — `pyproject.toml` + `uv.lock`: two evidence owners for one membership question

If `pyproject.toml`, TOML, dependency groups, or optional extras are not already secure, give their first-contact background before using them.

Then learn why both files are required:

```text
pyproject.toml → selected environment identity / project metadata
uv.lock        → exact resolved package relationships
```

Show the relevant real S001 project/lock fragments before our parsers.

Then inspect the bounded parsers and exact-source/provenance validation performed before semantic use.

**Sufficient-to-proceed condition:** Ali can explain why one file alone cannot safely answer the full selected-environment membership proposition. Parser internals beyond the evidence relation may remain deferred.

### Chunk 7 — S001 dependency graph traversal and witness

Before the traversal code, establish only the necessary graph background:

```text
package = node
"A depends on B" = directed edge A → B
transitive dependency = reached through one or more intermediate packages
reachability = can we get from selected root to changed package?
```

Then trace `evaluate_uv_selected_environment_membership(...)` through the central internal stages:

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

Only when traversal is reached, teach BFS (Breadth-First Search), `deque`, visited protection, path/depth bounds, direct versus transitive membership, and why analysis limits yield `unresolved` rather than false.

**Sufficient-to-proceed condition:** Ali can manually narrate the witness path and explain the important traversal state transitions. General graph theory and minor helper syntax do not block progress.

### Chunk 8 — from dependency membership to CI static consumption

First state the real missing question:

> Even if we established that the selected docs environment contains Soup Sieve, how do we safely bind that fact to the exact static CI location that selected it?

Then trace Cluster-5 composition:

```text
selected-environment membership
→ dependency/environment_membership.py where applicable
→ compose_project_environment_consumption(...)
→ StaticDependencyConsumptionEvidence
```

Understand why Dependency owns extra/group membership and CI only consumes that domain fact.

Inspect the exact package/workflow/job/step/command/segment rebinding checks that prevent valid evidence from being attached to the wrong static location.

**Sufficient-to-proceed condition:** Ali can explain why a supported membership witness still needs exact CI provenance/location binding before becoming CI consumption evidence.

### Chunk 9 — whole-workflow inspection + CI coverage result

Trace:

```text
inspect_workflow_dependency_evidence(...)
→ consumption evidence
+ direct package invocation locations
+ structural/source problems

then

evaluate_dependency_ci_coverage(...)
```

Before using these labels, establish their practical meanings one at a time:

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

**Sufficient-to-proceed condition:** Ali can explain exactly what remains uncorrelated and why green CI cannot upgrade the claim by itself.

### Chunk 10 — S011 contrast: optional extra before our comparison code

Switch to the real Dictare case only after the S001 positive path is understood:

```text
numpy 1.26.4 → 2.4.6
inside [project.optional-dependencies].mlx

normal PR/macOS test workflows:
pip install -e ".[dev]"
```

Before tracing UpgradePilot, learn in order:

- what a Python optional dependency/extra is and why projects use one;
- what Dictare's MLX/Apple-Silicon stack is for;
- why `mlx` is a real activation path despite being optional;
- what `pip install -e ".[dev]"` means at the practical level;
- why installing `dev` is not the same as installing `mlx`;
- why a macOS CI job does not automatically mean the MLX dependency environment exists.

Then predict and trace:

```text
affected extra = mlx
selected extra = dev
→ not_established
```

and its downstream CI-coverage consequence.

**Sufficient-to-proceed condition:** Ali can contrast `not_established` here with an `unresolved` analysis failure and explain why green standard CI is non-discriminating for this affected extra. MLX implementation details remain deferred.

### Chunk 11 — S005 transfer pressure: tox and mediated uv-lock use

Use the real ModelArrayIO case:

```text
pytest 9.0.3 → 9.1.1
changed source: uv.lock

tox latest environments
→ uv-venv-lock-runner
→ pytest
```

Before asking the architecture question, first establish:

- what tox is and why Python projects use it;
- what a tox environment is;
- what `uv-venv-lock-runner` is doing at the operational depth supported by the case;
- how a CI workflow can indirectly create/use a uv-locked environment through tox rather than containing a direct `uv sync` command itself.

Then ask:

> Would an architecture that equates `uv.lock consumption` with seeing direct `uv sync` in a GitHub Actions run step generalize to this case?

The expected lesson is architectural, not automatic implementation support. If current code does not interpret this mediation, preserve that boundary instead of pretending it does.

**Sufficient-to-proceed condition:** Ali can explain why S005 is transfer pressure and where current support should abstain/defer rather than overclaim. Tox/plugin internals do not need independent mastery.

### Chunk 12 — current application boundary: where the real flow stops today

Finally inspect the ordinary orchestration path in `src/upgradepilot/investigation.py` and the relevant CLI/tests.

First remind the distinction between:

```text
a capability implemented in a domain module
```

and:

```text
the normal application/orchestration path actually invoking that capability
```

Then contrast:

```text
implemented typed Cluster-5 dependency/CI machinery
```

with:

```text
ordinary application path still using the legacy CI evaluator before Cluster-6 migration
```

This is essential: a domain function existing and passing focused tests does not mean the normal public-PR application already calls it.

**Sufficient-to-proceed condition:** Ali can identify the integration seam and explain what is implemented versus what the ordinary application has not yet adopted at this snapshot. This is also a natural handoff back toward future building.

## 12. Session behavior rules

### 12.1 Learner question / issue handling and rule extraction

Questions, objections, partial answers, and confusions raised while studying are part of the learning evidence, not interruptions to be ignored or answered mechanically.

When Ali raises a question or issue during a chunk, the assistant should use this order:

```text
1. CHECK THE PREMISE / WORDING
   If the question or current understanding contains a material misconception, overloaded term,
   or imprecise ownership claim, correct that first. Preserve what was already correct.

2. ANSWER AT CURRENT-ROUTE DEPTH
   Explain or teach only enough to resolve the question for the current causal step.
   Do not use a useful question as permission to open an unrelated theory branch.

3. RETURN TO THE ACTIVE CHUNK
   Explicitly reconnect the answer to the real case/question we were studying so the route does not drift.

4. EXTRACT DURABLE PROCESS LEARNING WHEN PRESENT
   If the question exposes a reusable teaching/learning rule, recurring terminology trap,
   or process improvement, update this contract at a meaningful boundary rather than relying on memory.

5. RECORD SESSION-SPECIFIC DISCOVERY SEPARATELY
   If the discovery is important for this learning package but is not a reusable contract rule,
   preserve it in `LEARNING_MEMORY.md` as a correction, `[~]` item, artifact seed, or continuation note.
```

Additional rules:

- Do not treat every question as evidence that the whole chunk failed; determine whether the remaining issue is GREEN, YELLOW `[~]`, or RED/blocking.
- A learner answer may satisfy part of a gate while the learner's follow-up question reveals another part that is still uncertain. Record both rather than forcing an all-or-nothing judgment.
- When terminology is overloaded across tools or domains, name the collision explicitly before reasoning from it. Example: GitHub Actions `environment` (deployment target/protection context) is not automatically the same thing as a Python dependency/project environment.
- If Ali explicitly asks to go deeper into one subject, that authorization overrides the normal depth limit for that subject only; afterward, return to the active route unless he changes the route itself.
- Questions may improve the contract, plans, or memory, but they do not silently change product architecture or implementation authorization.

During the session:

- Ali may stop, challenge, ask for a smaller piece, or ask to go backward at any point.
- If a missing prerequisite blocks understanding, repair it immediately at the minimum complete depth, then explicitly return to the original chain.
- If Ali already understands a background concept well enough, compress the first-contact explanation; do not force ceremony.
- If Ali says a term is unfamiliar, treat that as evidence that more backward context is required before proceeding, but teach only the amount needed for the current causal step.
- Do not answer a confusion by introducing several new abstractions at once.
- Prefer real commands, structures, file fragments, objects, and function calls over abstract prose.
- When showing code, distinguish syntax that Ali must master from syntax that is incidental to the mechanism.
- Revisit earlier material when later evidence reveals that the mental model was incomplete.
- Do not mark mastery merely because Ali recognized an explanation immediately after reading it.
- At the start of a planned chunk, re-read its plan entry and apply the anti-drift checklist from Section 9.
- Do not move past a genuinely blocking gate merely because all listed subjects were mentioned.
- Conversely, do not keep a chunk open for perfection when the remaining gap is non-blocking; mark it `[~]` and preserve momentum.
- Normally use one meaningful prediction/explanation/diagnosis to test readiness, then proceed if the causal model is sound.
- Do not require all learning plans to finish before returning to implementation; when the next authorized building step becomes understandable and safe, building may resume and remaining learning can continue just-in-time.

## 13. Session-1 mastery evidence

Session 1 is educationally successful when Ali can, with decreasing assistance:

1. explain what Soup Sieve is and why it appears in the real Pydantic case;
2. explain what `uv.lock` is, identify the relevant parts of a real fragment, and explain why lock presence is not environment selection;
3. explain CI, GitHub Actions at the necessary level, and what Pydantic's docs CI is for;
4. reconstruct the S001 real dependency/environment path from the target project side;
5. identify the central UpgradePilot type/function at each later proposition boundary;
6. explain its important input and output using real case values;
7. distinguish positive, not-established, and unresolved evidence;
8. explain the S001 membership witness and why it is transitive;
9. explain static consumption versus direct exercise versus runtime authority;
10. use S011 to predict why `mlx` is not established by a `dev` install;
11. use S005 to identify an architecture-overfitting risk;
12. identify the current Cluster-5 → Cluster-6 integration seam;
13. read and explain at least one central focused test without relying entirely on the learning note;
14. later perform at least one ownership-bearing prediction, test modification, or diagnosis at a central boundary when justified.

This does not automatically establish independent mastery of uv, GitHub Actions, packaging, graph algorithms, tox, or the entire B2 route. Record only the depth actually demonstrated. Some mastery evidence may be accumulated during later building rather than forced before implementation resumes.

## 14. Starting point

After the learning-plan breakdown is approved and the corresponding plan files are created, begin with the first approved plan and its first chunk only.

The first learning content still begins from:

```text
S001 orientation
→ what Soup Sieve actually is
→ why Pydantic has it in this real case
```

Do **not** yet jump to `uv.lock`, docs CI, BFS, Cluster-4 traversal, or Cluster-5 composition in the same opening chunk.

Only after that first connection is secure do we proceed to the next planned chunk. The first-contact chunks should remain compact so that we reach real UpgradePilot source quickly and then continue learning alongside the code.