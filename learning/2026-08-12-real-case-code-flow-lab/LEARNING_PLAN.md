# UpgradePilot Real-Case Code-Flow Learning Plan

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial `main` baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Workspace:** `learning/2026-08-12-real-case-code-flow-lab/`

## 1. Purpose

This plan governs a dedicated learning journey for understanding and progressively owning UpgradePilot's actual implementation while product development continues independently on `main`.

The learning target is **UpgradePilot itself**: its architecture, source code, data flow, contracts, evidence model, reasoning model, tests, failure modes, implementation choices, and the technical concepts required to understand those things correctly.

Real product-simulation cases are used as concrete examples, pressure cases, and realistic values that can be traced through the implemented product. They are **not** a curriculum to be studied case-by-case, and simulation artifacts do not become implementation truth.

The central learning strategy is:

```text
real UpgradePilot responsibility
+ real/current source and tests
+ concrete case values when useful
+ end-to-end data-flow tracing
+ just-in-time concept teaching
+ prediction / explanation / diagnosis / modification exercises
→ progressively stronger product and code ownership
```

This is a learning plan, not a second product roadmap, implementation authority, or replacement for repository governance.

---

## 2. Authority and boundaries

Repository authority remains unchanged.

- `PROJECT_CHARTER.md` owns product mission and permanent product boundary.
- repository governance/specifications/ADRs continue to control their respective concerns.
- `MEMORY.md` remains the sole live-state owner for project position and continuation.
- selected project plans remain the implementation-scope owners.
- current source, tests, and runtime evidence remain implemented truth.
- `product-simulation/` remains discovery and pressure evidence.
- this file controls only the organization and method of this learning workspace.

### This branch may contain

- learning plans;
- end-to-end code-flow traces;
- concept notes justified by current code;
- diagrams and compact maps;
- code-reading annotations or excerpts where useful;
- exercises and predictions;
- failure diagnoses;
- transfer/comparison notes;
- dated learning checkpoints;
- learning-local scratch examples when useful.

### This branch does not authorize

- changing product behavior;
- changing controlling project scope;
- modifying target repositories;
- replacing live `MEMORY.md` state;
- silently changing implementation decisions;
- introducing production abstractions merely because they are educationally convenient.

Production source/tests should not be changed on this branch merely for teaching. If an educational experiment requires code, prefer a learning-local scratch artifact unless an explicit current request authorizes a different action.

---

## 3. Branch operating model

`main` is the ongoing implementation branch. This learning branch is intentionally longer-lived and may accumulate learning artifacts while implementation proceeds in parallel.

### 3.1 Ownership split

```text
main
├── product implementation
├── tests
├── governance/specifications/ADRs
├── plans
├── MEMORY.md live state
└── implementation/runtime truth

learning/real-case-code-flows-2026-08-12
├── synchronized view of main
└── learning/2026-08-12-real-case-code-flow-lab/
    └── learning-specific artifacts
```

The learning branch does not become a competing product branch.

### 3.2 Synchronization rule

Before a meaningful learning block:

```text
check latest main
→ inspect material changes since our branch baseline
→ decide whether they affect the responsibility we are about to study
→ synchronize main into the learning branch when needed
→ record/know the exact source state being studied
→ continue learning
```

Preferred synchronization strategy is **merge current `main` into the learning branch**, preserving a visible history of when the learning workspace absorbed implementation changes. Avoid force-updating/rebasing a long-lived learning branch merely to appear linear.

Synchronization is required when:

- starting a new substantial learning session after implementation has continued;
- entering a subsystem that has changed since the last learning baseline;
- a current lesson depends on newly implemented behavior;
- a previously learned behavior has materially changed;
- a failure/observation cannot be interpreted safely against a stale source state.

Synchronization is **not** a ceremony to perform after every irrelevant commit. If `main` changes in an unrelated area while a bounded lesson is underway, the lesson may finish against its known commit and synchronize before the next affected block.

### 3.3 Conflict policy

If synchronization produces a conflict:

- for `src/`, `tests/`, governance, plans, ADRs, and `MEMORY.md`, current `main` is presumptively authoritative;
- learning artifacts in this workspace are preserved unless they are factually invalid or intentionally superseded;
- never resolve a source conflict by making the learning branch's old implementation silently win;
- inspect semantic conflicts rather than resolving blindly.

### 3.4 Study-baseline recording

Every substantial dated learning artifact should identify the exact commit or synchronized baseline it describes when implementation details matter.

A learning note may become historical as `main` evolves. That is acceptable. Do not silently rewrite old evidence to pretend it always described current code. Create a new checkpoint or explicitly update/correct the old artifact when justified.

### 3.5 Merge-back policy

Nothing in this learning branch is automatically destined for `main`.

When an artifact becomes sufficiently useful and accurate, we may later decide explicitly whether to:

- merge it into `main`;
- copy/refine only selected material;
- keep it solely on the learning branch;
- supersede or archive it.

The learning process must remain free to contain exploratory explanations and exercises without forcing every artifact into production history.

---

## 4. Core learning principles

### 4.1 Learn the product through responsibilities, not isolated technology chapters

The primary unit of study is a real UpgradePilot responsibility or data flow.

Do not make the curriculum:

```text
Python
→ dataclasses
→ GitHub API
→ packaging
→ CI
→ LLMs
```

Instead:

```text
real product flow
→ encounter a technical mechanism
→ learn the minimum accurate model required
→ inspect how UpgradePilot implements it
→ use it in the flow
→ revisit it at greater depth when later responsibilities demand more
```

Technical concepts are therefore learned in context and revisited progressively.

### 4.2 Product-simulation cases are specimens, not lessons

S001-S009 and future cases may supply:

- real repositories/PRs;
- dependency transitions;
- evidence values;
- contrasting mechanisms;
- known difficult conditions;
- examples that pressure a current abstraction.

But the learning question is always something like:

> How does current UpgradePilot represent, acquire, transform, reason about, or stop on this information?

not:

> What happened in simulation case S00X?

One case may support several lessons; several cases may be used as contrasts inside one lesson. No sequential case-completion requirement exists.

### 4.3 Bound the supported learning scope, not the known fixture

A real case gives concrete values, but explanations must identify the actual responsibility boundary represented by the code.

Do not teach a fixture-specific accident as if it were the design.

When code is intentionally mechanism-specific, say so. When behavior is actually generic inside a supported domain, identify why. When an abstraction has not yet been earned, do not invent one for pedagogical neatness.

### 4.4 Trace data, not just call graphs

A function-call graph alone is insufficient.

For each important hop, understand:

- the concrete incoming value;
- its Python type/contract;
- who produced it;
- what facts it is allowed to mean;
- the function/method consuming it;
- important branches/guards;
- returned type/value/state;
- the next consumer;
- what became established;
- what remained unresolved;
- what the step deliberately does **not** prove.

### 4.5 Observation, interpretation, evidence quality, and decision stay separate

Learning artifacts must preserve the same epistemic separation as the product.

A useful trace distinguishes:

```text
raw/public observation
→ validated/normalized evidence
→ interpretation
→ proposition/candidate reasoning
→ applicability state
→ investigation/stop choice
→ later synthesis/maintainer action
```

Do not collapse missing evidence into negative evidence, or a technical observation into a recommendation.

### 4.6 Read code selectively but deeply

Do not study every source line equally.

Prioritize:

1. public/domain contracts and dataclasses;
2. orchestration boundaries;
3. validation and identity guards;
4. important decision branches;
5. evidence/problem unions;
6. state transitions;
7. tests that encode intended semantics;
8. failure paths that expose responsibility boundaries.

Boilerplate, obvious plumbing, and repeated syntax can be summarized unless they contain a material concept.

---

## 5. Standard learning-session loop

A session should normally follow this shape, adapting when the responsibility demands otherwise.

### Step 1 — Refresh context minimally

- check current `main` and current `MEMORY.md` when live state matters;
- inspect relevant changes since the last learning baseline;
- synchronize if the current lesson would otherwise be stale;
- open only the source/tests/specs/evidence needed for the chosen responsibility.

Do not rescan the entire repository without a concrete reason.

### Step 2 — State the product responsibility

Before source detail, answer:

- What is UpgradePilot trying to know/do here?
- Why does this responsibility exist in the product flow?
- What is the input boundary?
- What output/state must the responsibility provide?
- What must it *not* claim?

### Step 3 — Show the end-to-end map first

Give a compact map such as:

```text
PR locator
→ PullRequestIdentity
→ changed files
→ DependencyVersionChange
→ package/upstream evidence
→ technical impact candidate
→ applicability
→ investigation/observation
→ reevaluation
```

This map is orientation, not the full lesson.

### Step 4 — Zoom into one bounded segment

Teach one manageable segment at a time. Avoid dumping the entire flow into one explanation.

For the segment, use the standard flow-trace frame in Section 6.

### Step 5 — Teach concepts just in time

When a new concept becomes necessary, explain it using the concept contract in Section 7, then immediately reconnect it to the actual code/value.

### Step 6 — Ali predicts or challenges

Before every result is revealed, use prediction selectively where it has real learning value, for example:

- What state should this proposition have with this evidence?
- Should the selector acquire more evidence or stop?
- Which exact branch should execute?
- What information would be lost if these two dataclasses were merged?
- Should this artifact fact establish target applicability?

Prediction is not required for trivial syntax or mechanical plumbing.

### Step 7 — Inspect source and tests together

Source tells us how behavior is implemented; tests often expose the intended semantic boundary more clearly.

For important behavior, connect:

```text
requirement / invariant
↕
source branch or contract
↕
test assertion / fixture variation
```

### Step 8 — Use failures as learning evidence

When a test/runtime failure occurs:

```text
observe exact failure
→ identify owning responsibility
→ distinguish symptom from cause
→ form competing explanations when needed
→ inspect discriminating evidence
→ diagnose
→ explain why the correction belongs at that boundary
→ verify with focused + relevant regression evidence
```

A failure that teaches an important boundary may deserve its own learning note.

### Step 9 — Ownership action

Where useful, require one bounded action such as:

- explain a returned object in own words;
- predict a changed-case result;
- modify a learning-local example;
- identify a missing guard;
- write/adjust a focused test with guidance;
- diagnose a deliberately introduced discrepancy;
- compare two implementation alternatives;
- reconstruct the data flow without looking at the map.

Passive reading alone does not establish ownership.

### Step 10 — Close with limits and next connection

End the bounded lesson with:

- what is now understood;
- what remains unresolved or deferred;
- which source/test owns the truth;
- how this segment connects to the next product responsibility;
- whether a durable learning artifact is justified.

---

## 6. Standard real-code flow-trace frame

For important stages, use this recurring representation:

```text
REAL INPUT / EXAMPLE
↓
Python object or public evidence
↓
producer / acquisition boundary
↓
function called
↓
important code mechanism / guard / branch
↓
returned object or explicit problem/state
↓
next consumer
↓
what this establishes
↓
what this does NOT establish
```

For concrete traces, also record where useful:

- source file and symbol;
- relevant test file/test method;
- exact example values;
- important field values before/after;
- state transition;
- failure alternative;
- provenance/revision identity;
- why this boundary exists architecturally.

### Example shape

```text
Concrete dependency transition
  package = "..."
  old_version = "..."
  proposed_version = "..."

↓ DependencyVersionChange

build_<mechanism>_impact_candidate(...)

↓

<Mechanism>ImpactCandidate
  mechanism_status = established
  exposure_status = to_evaluate
  consequence_status = possible

↓

evaluate_<mechanism>_impact(...)

↓

CandidateApplicabilityAssessment
  state = unresolved

Why unresolved?
  exact target proposition is not yet established.

What this proves:
  enough evidence exists to formulate the technical candidate.

What this does not prove:
  that the exact target is affected.
```

The exact fields differ by mechanism; the frame should not force unrelated mechanisms into identical schemas.

---

## 7. Concept-teaching contract

When an important term, abbreviation, or technical label is materially introduced, explain:

1. **Full form/name.**
2. **Practical meaning.**
3. **Why it has that name / what distinction the term encodes.**
4. **Owning component or standard.**
5. **Inputs and outputs/boundaries.**
6. **How it appears in current UpgradePilot.**
7. **Common confusion or failure mode.**
8. **Depth required now.**
9. **What is intentionally deferred.**

Avoid harmful oversimplification, but do not front-load specialist detail that the current responsibility does not require.

### Depth categories inside a lesson

Use these practical labels when useful:

- **Must master now** — central to reasoning about or owning the current responsibility.
- **Operationally understand now** — enough depth to use/read safely; deeper internals can wait.
- **Recognize now** — know what it is and why it appears; not yet expected to manipulate independently.
- **Deferred** — useful later but not required for the current flow.

These lesson-local categories complement the repository-wide demonstrated-depth labels; they do not claim mastery automatically.

---

## 8. Demonstrated learning depth

Use the existing repository learning-depth vocabulary accurately:

- **introduced** — terminology and broad mechanism recognized;
- **operationally understood with guidance** — bounded flow can be traced/used safely with support;
- **implementation-adjacent** — source and tests can be read/evaluated with guidance;
- **ownership practice** — one central behavior was predicted, modified/tested, executed, and explained;
- **independently demonstrated** — responsibility controlled across changed cases with limited assistance.

Do not upgrade depth merely because:

- an explanation was read;
- AI wrote code;
- a test was executed;
- the user agreed with an answer;
- a test happened to pass.

Evidence of depth comes from explanation, prediction, transfer, diagnosis, modification/testing, and reduced assistance across changed cases.

---

## 9. Code-reading method

When reading an important source file, use a layered approach.

### Layer A — File responsibility

Explain why the file/package exists and what it owns versus neighboring modules.

### Layer B — Public contracts

Identify important:

- dataclasses;
- enums/Literal states;
- protocols/interfaces;
- result unions;
- function signatures;
- invariant-enforcing constructors/guards.

### Layer C — Main execution path

Trace the normal relevant path with concrete values.

### Layer D — Decision branches and failure paths

Inspect branches that materially change meaning, such as:

- identity mismatch;
- unavailable evidence;
- malformed public data;
- unsupported comparison;
- unresolved proposition;
- explicit conflict;
- no-op/`None` because no candidate is justified.

### Layer E — Tests as executable semantics

Identify which tests prove which boundary and which behavior remains untested or intentionally outside scope.

### Layer F — Syntax only where it matters

Teach Python syntax deeply when it carries architectural/semantic meaning, for example:

- frozen dataclasses;
- type unions;
- `Literal` state spaces;
- pattern/branch structure;
- comprehensions/set operations that implement evidence comparison;
- exception versus explicit evidence-problem results;
- dependency injection/default clients;
- immutability/hashability where relied upon.

Do not turn every import or obvious assignment into a syntax lecture.

---

## 10. Test and diagnosis method

Tests are part of the learning material, not merely a final correctness button.

For an important test, answer:

- What product claim is this test protecting?
- Which values are deliberately varied?
- Which values are irrelevant noise?
- What false implementation would this test catch?
- What does a green result **not** prove?

### Failure diagnosis discipline

Use the recent artifact-serviceability parser issue as the model:

```text
real-style evidence rejected
→ inspect the parser call and failing test
→ discover validate_order=True imposed canonical formatting lint
→ compare that strictness against owned product responsibility
→ determine UpgradePilot needs parseable compatibility evidence, not formatting lint
→ remove responsibility-inappropriate strictness
→ keep malformed-wheel and identity validation
→ rerun focused + nearest regression + full suite
```

The lesson is not only the API option. The deeper lesson is **validation strictness must match the product responsibility**.

---

## 11. Artifact policy for this workspace

Do not generate notes merely because a session occurred.

Create a durable artifact only when it preserves material understanding that would otherwise be easy to lose, such as:

- a complete real code/data flow;
- a difficult concept boundary;
- a corrected misconception;
- a significant failure diagnosis;
- a comparison that explains an architecture decision;
- an ownership exercise/result;
- a dated checkpoint before implementation materially changes.

Prefer several focused artifacts over a giant transcript-like document.

### Suggested naming

Use dated names when tied to implementation state, for example:

```text
2026-08-12-current-runtime-map.md
2026-08-13-pr-to-dependency-transition-flow.md
2026-08-14-python-support-applicability-loop.md
2026-08-15-artifact-serviceability-flow.md
2026-08-16-two-mechanism-transfer-comparison.md
```

Dates/examples are illustrative; artifacts are created only when justified.

### Every substantial artifact should normally include

- responsibility;
- source baseline/commit;
- relevant source/tests;
- concrete example values when useful;
- accurate mental model;
- important invariants/boundaries;
- what was demonstrated versus merely explained;
- deferred depth;
- one useful recall/transfer/diagnosis/ownership action where appropriate.

Do not duplicate whole governing documents or source files. Link/reference owners.

---

## 12. Learning journey

The journey follows the actual product flow and current implementation maturity. It can evolve as `main` advances, but changes should preserve the method above.

### Stage 0 — Current runtime and architecture map

**Goal:** build enough orientation to navigate the real system without prematurely learning every package.

Cover:

- public PR investigation entrypoint;
- major responsibility-oriented source packages;
- where acquisition, evidence, target interpretation, impact reasoning, applicability, and orchestration currently live;
- major result/problem contracts;
- relation between source, tests, plans, and evidence.

Expected output:

```text
compact current architecture/data-flow map
+ ability to locate the owner of a given value/responsibility
```

Do not attempt exhaustive architecture documentation.

### Stage 1 — Real PR input to exact dependency transition

Use a suitable real product-simulation case only as a source of concrete values.

Trace:

```text
repository + pull number
→ PullRequestIdentity
→ exact base/head identity
→ changed files
→ dependency-change analysis
→ DependencyVersionChange
```

Concepts likely encountered:

- exact revision identity;
- public evidence acquisition;
- provenance;
- domain objects versus provider/API payloads;
- parsing/validation;
- explicit evidence problems;
- dependency transition identity;
- orchestration boundaries.

Learning target: explain how a remote PR becomes a trustworthy, bounded dependency-change fact and what uncertainty remains.

### Stage 2 — Exact-head CI, package, and upstream evidence branches

Continue the same product flow into the evidence needed by current reasoning mechanisms.

Trace selectively:

```text
DependencyVersionChange
├→ exact-head CI evidence
└→ package/upstream release evidence
```

Focus on:

- why evidence identity must match the exact PR/release/revision;
- acquisition versus interpretation;
- evidence authority;
- relevant CI versus generic CI existence;
- PyPI release evidence contracts;
- upstream repository/release/tag/changelog evidence where current flow uses it;
- explicit unavailable/malformed/conflicting states.

Do not learn every GitHub/PyPI API field. Learn the fields UpgradePilot actually admits and why.

### Stage 3 — Mechanism 1: Python-support reasoning loop

This is the first deep reasoning-flow study because the runtime loop is implemented and verified.

Trace end-to-end:

```text
grounded Python-support-drop claim
→ build PythonSupportDropImpactCandidate
→ initial applicability evaluation
→ unresolved target proposition
→ discriminating investigation selection
→ exact target pyproject.toml acquisition
→ TargetPythonDeclaration interpretation
→ Target-Python relevance
→ reevaluate same candidate
→ post-observation applicability
```

Must understand:

- technical impact candidate versus established target applicability;
- `PropositionAssessment`;
- proposition states: established / refuted / unresolved / conflicted;
- evidence coverage;
- conjunctive applicability paths;
- `ApplicabilityPathAssessment`;
- candidate applicability composition;
- path-model coverage;
- why all-known-paths-refuted requires sufficient path-model coverage before claiming not applicable;
- discriminating investigation;
- no-blind-repeat behavior;
- evidence acquired but method still unable to resolve;
- exact target Python declaration versus upstream package support claim.

Use changed examples to verify the distinctions:

- overlap;
- outside declared range;
- missing target declaration;
- malformed declaration;
- unsupported comparison;
- already-attempted acquisition.

### Stage 4 — Mechanism 2: Artifact serviceability

Use S008-like concrete evidence values, but study current UpgradePilot artifact-serviceability code.

Trace Increment 1:

```text
DependencyVersionChange
+ old PackageReleaseEvidence
+ proposed PackageReleaseEvidence
→ distribution inventory
→ parse wheel filenames
→ wheel Tag sets
→ old/new set comparison
→ removed/added published compatibility tags
→ old/proposed sdist presence
→ target-agnostic ArtifactServiceabilityImpactCandidate or explicit problem/None
```

Must understand:

- wheel versus source distribution (sdist);
- wheel filename structure at the depth used by the code;
- Python interpreter tag;
- ABI (Application Binary Interface) tag;
- platform tag;
- `packaging.tags.Tag`;
- compressed tag parsing;
- package/version identity validation;
- set difference as artifact-inventory comparison;
- why a removed published tag is not yet a target loss;
- why an sdist existing is not evidence that a source build succeeds;
- parseability versus canonical-format linting;
- explicit evidence problem versus absence of a justified candidate.

Use the real parser failure/correction as a diagnosis lesson.

### Stage 5 — Compare the two implemented mechanisms

Once both mechanisms are understood individually, compare them.

Ask:

- What is genuinely shared?
- What is merely structurally similar?
- Which concepts belong to generic applicability composition?
- Which candidate/evidence semantics must remain mechanism-specific?
- Why is `current state → justified investigation/stop → observation → reevaluation` a reusable responsibility pattern without yet implying a generic planner?
- What evidence earned the existing shared applicability types?
- What abstractions would currently be premature?

This stage should explicitly connect implementation experience to architecture judgment.

### Stage 6 — Follow Artifact Serviceability Increment 2 when it lands

Before study:

```text
refresh main
→ inspect implementation diff and MEMORY change
→ synchronize branch
→ identify the exact new responsibility
```

Then extend the artifact flow into:

```text
target-agnostic artifact candidate
→ exact target artifact-environment evidence
→ compatibility propositions
→ candidate applicability
→ investigation/stop behavior as implemented
```

Critical boundary:

> Do not use UpgradePilot's local runtime environment as a proxy for a remote target environment.

Learn exactly which target evidence the implementation admits and why it is sufficient/refuting/unresolved.

### Stage 7 — Continue through later B2 convergence

As implementation advances, follow the real product toward:

- multi-mechanism orchestration if/when earned;
- candidate-specific investigation lifecycle;
- investigation stopping;
- technical result handoff;
- repository/context synthesis;
- overall evidence sufficiency and residual uncertainty;
- maintainer-facing recommendation/abstention;
- traceable output and replay.

Do not pre-teach unimplemented architecture as though it already exists. Mature-system horizon documents may orient us, but current source/tests determine what can be traced as implementation truth.

---

## 13. Use of S006/S007/S009 and other contrasting cases

These cases are valuable as **short counterexamples and transfer pressure**, not separate required modules.

Examples:

- **S006-style pressure:** static evidence may be insufficient; a targeted dynamic observation may have discriminating value.
- **S007-style pressure:** authoritative static evidence may resolve a proposition and make a previously considered investigation unnecessary/stale.
- **S009-style pressure:** repository provenance/reproducibility context may matter later to synthesis without being technical applicability itself.

Use them when they help answer an implementation/design question already present in current UpgradePilot.

---

## 14. Learning checkpoints and transfer

After a substantial mechanism, test understanding through a different but related situation.

Possible transfer actions:

- predict proposition/path/candidate states for changed evidence;
- identify which evidence owner should answer a new proposition;
- explain whether a proposed investigation is discriminating or redundant;
- compare missing evidence with explicit negative evidence;
- diagnose a target identity mismatch;
- explain why a package-level fact cannot establish target applicability;
- inspect a new wheel tag inventory and predict the candidate outcome;
- locate the proper source owner for a new requirement;
- identify an abstraction that is tempting but not yet evidence-earned.

Transfer matters more than memorizing scenario-specific values.

---

## 15. Questions we should repeatedly ask

During code learning, repeatedly use these questions:

1. **What exact fact/state does this object represent?**
2. **Who is authoritative for that fact?**
3. **What exact identity/provenance does it preserve?**
4. **What transformed raw input into this object?**
5. **What failure/problem states can occur instead?**
6. **What does the next function assume?**
7. **What becomes established after this step?**
8. **What remains unresolved?**
9. **Are we confusing missing evidence with negative evidence?**
10. **Are we confusing candidate formulation with applicability?**
11. **Is this investigation actually discriminating?**
12. **Would new evidence make the planned investigation stale?**
13. **Does this abstraction serve the full responsibility or only the current fixture?**
14. **Which test protects this semantic boundary?**
15. **What would break or become misleading if this boundary were removed?**

---

## 16. Things we deliberately avoid

This learning journey should not drift into:

- reading every file sequentially;
- memorizing all product-simulation cases;
- creating a parallel project tracker;
- rewriting existing documentation into learning notes;
- teaching unrelated computer-science topics before they are needed;
- treating all source lines as equally important;
- inventing generic architecture to make lessons look tidy;
- equating test green with complete understanding;
- equating AI-generated code with user ownership;
- treating current local machine characteristics as evidence about remote targets;
- making final maintainer recommendations from intermediate technical facts;
- allowing old learning artifacts to override current source/tests or `MEMORY.md`.

---

## 17. Initial execution sequence

At the current baseline, the first sessions should proceed in this order:

```text
1. Current runtime/architecture orientation
2. PR input → PullRequestIdentity → changed files → DependencyVersionChange
3. Relevant evidence branches needed by the current implemented mechanisms
4. Full Python-support candidate/applicability/investigation/reevaluation loop
5. Artifact Serviceability Increment 1 data flow and parser diagnosis
6. Two-mechanism architecture/transfer comparison
7. Refresh/sync main
8. Continue into Artifact Serviceability Increment 2 when implemented
```

The sequence is intentionally adjustable if `main` materially advances before a stage begins. We follow the current product responsibly, not this list mechanically.

---

## 18. Completion condition for this learning plan

This plan is not complete because every source file was read or every simulation was discussed.

It succeeds when the learning branch demonstrates progressively stronger ability to:

- navigate current UpgradePilot architecture;
- trace important values end-to-end through real code;
- explain the contracts and state transitions accurately;
- distinguish evidence, interpretation, candidate, applicability, investigation, synthesis, and recommendation;
- read central source and tests with decreasing assistance;
- predict behavior under changed inputs;
- diagnose meaningful failures;
- recognize responsibility boundaries and premature abstractions;
- connect newly implemented mechanisms into the existing mental model;
- preserve useful learning artifacts without creating a competing source of project truth.

The long-term target is practical ownership of the project through repeated learning-by-building and learning-by-diagnosing, not memorization of a frozen implementation snapshot.
