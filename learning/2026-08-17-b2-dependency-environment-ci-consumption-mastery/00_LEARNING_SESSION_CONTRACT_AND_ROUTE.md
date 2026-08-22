# B2 Dependency Environment + CI Consumption — Real-Case Mastery Contract and Route

**Created:** 2026-08-17  
**Revised:** 2026-08-22 — governance consolidated; rule ownership clarified; evidence-overlap, necessity-classification, fair-checkpoint, and interruption/resume rules added  
**Artifact role:** global learning contract for this package  
**Learning scope:** B2 Dependency Environment and CI Consumption Evidence through the implemented Cluster-5 boundary  
**Primary real-case spine:** S001 — Pydantic / Soup Sieve 2.6 → 2.8.4  
**Contrast case:** S011 — Dictare / NumPy 1.26.4 → 2.4.6 inside optional extra `mlx`  
**Transfer-pressure case:** S005 — ModelArrayIO / pytest 9.0.3 → 9.1.1 through tox + uv lock machinery

## 1. Purpose and authority boundary

This folder is the dedicated learning workspace for mastering the current B2 dependency-environment and CI-consumption capability through **real cases, real target-project evidence, real UpgradePilot source, and real tests**.

This contract owns only the **global teaching/learning method and durable learning rules** for this package. It is not:

- live project-state authority;
- product implementation authorization;
- an architecture/specification owner;
- implementation truth;
- a replacement for source/tests;
- a replacement for `../../MEMORY.md`.

Authority and responsibility:

```text
../../MEMORY.md
→ live project position and selected continuation

../../OPERATING_GUIDE.md
→ project-wide learning/execution rules

this contract
→ global learning invariants for this package

PLAN_XX_....md
→ plan-specific route, traps, source/test targets, and gates

PLAN_XX_MASTERY_AND_DEPTH_MAP.md
→ required depth and explicit deferrals

LEARNING_MEMORY.md
→ current learning position, demonstrated understanding, open gaps, and exact continuation

current source/tests
→ implementation truth

product-simulation/
→ historical manual evidence, not executable product truth
```

`CAREER_DAY30_OWNERSHIP_HANDOFF.md` remains an active subordinate ownership/evidence overlay. It strengthens how current-source understanding, test understanding, legitimate modifications, and real failure diagnosis are evidenced, but it does not change technical sequencing or authorize product work.

A learning rule has **one normal owner**. Plans inherit this contract automatically and should specialize it rather than repeat it. Silence in a plan does not disable a contract rule.

## 2. Core rules to actively enforce every session

These are the high-salience rules that should remain mentally active even when the detailed reference sections are not open.

1. **Real case before abstraction when available.** Use exact target evidence, commands, files, source, and tests rather than fictional stand-ins.
2. **Background first for genuinely new material.** Establish the minimum accurate real-world meaning before using a package/tool/file/configuration as a premise.
3. **One minimum-complete chunk at a time.** Do not jump across several unfamiliar propositions or technologies in one teaching block.
4. **Ali may stop, challenge, backtrack, or question the premise at any point.** Resolve that local issue before advancing.
5. **Learner checkpoints must be fair.** Do not require implementation details that have deliberately not been taught yet.
6. **Source/tests are implementation truth, not automatic design truth.** Learn what the code does and separately audit why it is shaped that way.
7. **Read executable responsibility, not just names/comments.** Teach material Python syntax/control flow in context; do not explain every line equally.
8. **Keep evidence strength explicit.** State what a result establishes and what stronger claim remains unjustified.
9. **Do not manufacture ownership evidence.** No forced mutations, fake failures, or artificial debugging exercises.
10. **Assistance fades with repeated mechanisms.** First contact may be guided; later transfer should increasingly begin with Ali's prediction/reasoning.
11. **Challenge necessity, not only correctness.** A field/check/artifact may be proposition-essential, implementation-specific, defensive, or still unjustified.
12. **Inherit, do not repeat.** Global rules stay here; plans contain only local specialization; mastery maps contain depth; learning memory contains continuity.

## 3. Roles

### Ali — learner, reasoner, and eventual owner

Ali should increasingly be able to:

- connect a technical object to its real purpose before reasoning about our abstraction;
- predict or reconstruct a material state before seeing the exact answer when enough context exists;
- trace important real inputs → source responsibility → output/problem state;
- explain why a central function/type exists;
- distinguish observation, interpretation, uncertainty, and proof strength;
- read central executable source rather than rely on summaries/docstrings;
- explain representative tests as setup → action → assertion → protected behavior → non-proof;
- challenge overclaims, weak claims, redundant checks, brittle abstractions, or questionable premises;
- distinguish implementation fact from engineering judgment;
- later participate in legitimate source/test changes or real failure diagnosis when the live project naturally provides the opportunity.

Typing volume and approving AI-generated code are not mastery by themselves.

### AI assistant — guide, navigator, reviewer, and engineering critic

The assistant should:

- start from the real case and go backward only as far as needed for a correct mental model;
- show exact historical/current fragments when available;
- name the owning repository source path/module for code slices being explained;
- choose the smallest coherent executable responsibility that preserves the mechanism;
- explain material syntax and program semantics together;
- ask predictions/reconstructions only when prerequisites are already available;
- distinguish what must be mastered from what is operational/navigation/deferred;
- correct its own earlier oversimplification explicitly when a learner challenge exposes one;
- reduce assistance on repeated mechanisms;
- inspect provider/caller/tests/spec/history when a current design choice cannot be justified from source alone.

The assistant must not replace real code/data flow with a simplified fictional example when real evidence exists.

### Source/tests — implementation truth, not design authority

Source/tests establish what the current product actually does. They do not automatically establish that every current design choice is optimal, proportionate, permanent, or logically necessary.

For a material design choice, distinguish:

```text
CURRENT IMPLEMENTATION FACT
What the source/tests actually require today.

RATIONALE / FAILURE MODE
What bug class, ambiguity, trust-boundary issue, compatibility concern, or product requirement the choice appears to protect.

ENGINEERING JUDGMENT
Whether the protection appears essential, defensive, transitional, redundant, too weak, or a plausible simplification/refactor candidate.

AUTHORITY BOUNDARY
A critique does not change product behavior. Product mutation still requires normal live authorization and validation.
```

Do not justify something merely because it exists in source.

## 4. Engineering-necessity classification

When a material field, check, artifact, invariant, or design constraint matters to the lesson, classify it as narrowly as evidence allows:

```text
PROPOSITION-ESSENTIAL
Logically necessary to establish the proposition being claimed.

CURRENT-IMPLEMENTATION REQUIREMENT
Required by the current source/design, but another valid architecture could establish the proposition differently.

DEFENSIVE / BOUNDARY HARDENING
The invariant should normally already hold upstream, but this boundary revalidates it to fail closed if callers/providers/caches/tests violate it.

UNCERTAIN / AUDIT NEEDED
The rationale or necessity is not yet sufficiently established.
```

Do not teach **"the system needs X"** when the evidence supports only **"the current implementation requires X."**

This classification does not require every line to receive a label. Use it when necessity or proportionality is material to understanding or design judgment.

## 5. Overlapping-evidence rule

Multiple artifacts may carry partially overlapping facts. Do not force an artificially clean division such as `A tells X / B tells Y` when the real evidence is richer.

For a material multi-artifact proposition, identify where useful:

```text
what each artifact directly declares/observes
where their information overlaps
which information is primary versus derived/duplicated
what the current implementation actually consumes from each
what none of them can establish alone
```

Also distinguish the **selection proposition** from information merely existing in project/lock artifacts. For example, dependency/group information inside a file does not by itself prove that an inspected CI command selected that environment.

## 6. Example-state labeling

When a hypothetical materially affects the learner's model of normal system behavior, identify its status:

```text
NORMAL / EXPECTED PATH
what correct ordinary operation should produce

FAILURE / INVALID INPUT
an invariant violation or malformed/misbound state that should not normally occur

TEST FIXTURE
a deliberately constructed case used to protect a branch/invariant

HYPOTHETICAL DESIGN CASE
an architecture thought experiment, not a claim about current operation
```

Defensive guards must not be taught as though their failure states are expected normal pipeline behavior.

## 7. Background-first and first-contact rule

When a material subject is new or weakly familiar, do not immediately use it as a premise. Use the smallest useful ladder:

```text
1. WHAT IS IT?
2. WHY DOES IT EXIST / WHAT JOB DOES IT DO?
3. WHY DOES THIS TARGET PROJECT USE IT?
4. WHAT DOES IT LOOK LIKE IN THIS REAL CASE?
5. WHICH PARTS MATTER NOW, AND WHICH ARE DEFERRED?
6. WHY DOES IT MATTER TO OUR CURRENT QUESTION?
7. ONLY THEN ENTER UPGRADEPILOT CODE.
```

This applies to headline concepts and smaller mechanisms when they materially change interpretation: `uv.lock`, `pyproject.toml`, optional extras, dependency groups, GitHub Actions `uses:` actions, working directories, selector flags, BFS, tox, `uv-venv-lock-runner`, and similar mechanisms.

Background depth limit:

```text
minimum complete background
→ exact real example
→ current problem
→ why our mechanism helps
→ return to the active route
```

Do not name-drop unfamiliar material and continue. Do not turn every encountered technology into a standalone course.

## 8. Minimum-complete chunk and anti-jump rule

A normal chunk should usually contain:

```text
1 primary real question
+ minimum prerequisite/background
+ 1 real-case evidence slice
+ at most 1 main new mechanism/concept family
+ 1 coherent source responsibility OR preparation for it
+ 1 meaningful Ali prediction/explanation/diagnosis/critique
```

Keep inseparable tiny helpers together; stop large functions at a meaningful responsibility boundary. The complete route may be broad, but each conversation step stays locally coherent.

Use GREEN / YELLOW `[~]` / RED reasoning:

```text
GREEN
core relation is sound enough to proceed

YELLOW / [~]
real non-blocking gap remains; preserve and continue

RED / [!]
missing prerequisite or misconception would make the next reasoning materially unreliable; repair only that blocking part
```

No perfection prerequisite. One meaningful ownership check is normally enough to proceed if the causal model is sound.

## 9. Standard chunk learning loop

Use this sequence when applicable; simplify when a chunk does not need every stage:

```text
A. ORIENT / STEP BACK
B. FIRST-CONTACT BACKGROUND
C. EXACT REAL TARGET EXAMPLE
D. REAL QUESTION / PROPOSITION
E. RAW / HISTORICAL EVIDENCE
F. WHY THE NEXT UPGRADEPILOT MECHANISM HELPS
G. REPRESENTATIVE REAL UPGRADEPILOT INPUT
H. SOURCE WALK
I. OUTPUT / PROBLEM STATE
J. PROOF / NON-PROOF BOUNDARY
K. REPRESENTATIVE TEST
L. ALI OWNERSHIP CHECK
M. CONNECT FORWARD
```

Not every chunk needs source code. Early chunks may exist to make the real object/tool/configuration understandable before source appears.

### Source-walk rule

When source is part of the chunk:

- state the owning source path/module;
- orient around the responsibility before syntax;
- read the actual executable constructs that carry behavior;
- explain material signatures, types/unions, dataclass fields, guards, early returns, branches, loops/comprehensions, `isinstance` narrowing, collections, assertions/invariants, helper calls, and rebinding checks only where they matter;
- comments/docstrings may orient but cannot replace executable-code reconstruction;
- do not explain incidental punctuation or every helper equally;
- connect one representative focused test when meaningful;
- if a meaningful test does not exist, state that explicitly;
- apply the engineering-necessity classification where a design/check is material or challenged.

A source file can contain several learning depths at once. File length is never the mastery metric.

## 10. Learner checkpoints — fairness and type

Consequential prompts should be fair with respect to already established material. Where useful, distinguish:

```text
RECALL
material has already been taught or demonstrated

REASONING / PREDICTION
Ali has enough premises; the exact result/source answer has not yet been shown

SOURCE RECONSTRUCTION
the mechanism has already been inspected and Ali reconstructs it

OPEN ENGINEERING CRITIQUE
several defensible answers may exist; reasoning/proportionality matters more than matching current code
```

Do not ask a checkpoint whose correct answer depends on implementation details deliberately reserved for a future step.

Prediction-before-answer remains desirable when the prerequisites are genuinely available. Do not turn every line into a quiz.

## 11. Learner interruption, questions, and resume protocol

Questions, objections, partial answers, and premise challenges are part of the learning evidence.

When Ali pauses at a specific section/question:

```text
1. check/correct the premise or overloaded wording
2. answer only the local uncertainty at current-route depth
3. explicitly correct any earlier oversimplification
4. re-establish the corrected mental model
5. do NOT automatically advance to later material
6. resume from the paused position only when ready
```

If a prerequisite is missing, repair the minimum blocking part and return to the original chain.

A grounded challenge to the teacher's premise, artifact requirement, invariant, defensive check, example normality, or question framing can be **positive ownership evidence**. Resolve the premise before forcing downstream reasoning that assumes it.

If Ali explicitly requests deeper treatment of one subject, that overrides the normal depth limit for that subject only; afterward return to the active route unless the route itself changes.

Questions may improve this contract, plans, or `LEARNING_MEMORY.md`; they do not silently authorize product architecture/source changes.

## 12. External technology depth rule

Learn external technology only to the depth required for the current real evidence chain. Examples include:

- Soup Sieve / Beautiful Soup relationship;
- package/distribution normalization;
- TOML / `pyproject.toml` project/dependency structure;
- optional extras and dependency groups;
- `uv`, `uv.lock`, `uv sync`, `uv run`, workspace/project selection;
- CI and GitHub Actions workflow/job/step semantics;
- documentation CI;
- graph node/edge/reachability, BFS, `deque`, visited/path state;
- Dictare MLX optional environment;
- tox and `uv-venv-lock-runner` mediation;
- Python typing/dataclasses/private records where they carry UpgradePilot semantics.

Prefer exact target-project fragments over generic invented examples. Defer full uv resolver internals, full TOML grammar, complete GitHub Actions runtime semantics, full tox/plugin internals, broad graph theory, generic shell interpretation, and unrelated technology internals unless later work makes them causally necessary.

## 13. Depth and mastery policy

The detailed depth owner is `00_PLAN_MASTERY_AND_DEPTH_INDEX.md` plus each plan's mastery companion.

Global depth vocabulary:

```text
OWN / MASTER
reconstruct selected responsibility from real input → executable mechanism → states/output → representative test → proof boundary, with reduced assistance

STRONG WORKING UNDERSTANDING
follow and explain an important supporting component when source is open

NAVIGATE / RECOGNIZE
know role/location/when to inspect; no broad ownership target

OPERATIONAL BACKGROUND
understand external technology enough for correct project reasoning

DEFER
no present learning investment unless later work makes it causally necessary
```

At OWN / MASTER depth, when material, Ali should also be able to distinguish current implementation fact from proposition-essential requirements, defensive hardening, uncertain rationale, and plausible alternative design.

Mastery does **not** mean memorizing line numbers, reproducing large files from memory, reading every helper/test, mastering every external tool, or avoiding AI assistance.

The normal engineering standard is: with the repository open, Ali can locate the responsibility, read material code, explain important control flow/states, understand representative tests, predict meaningful changed behavior, and participate intelligently in a later change or diagnosis.

## 14. Plan ownership and anti-drift

Plans are subordinate execution maps. They own **local route and specialization**, not global learning method.

Each plan should proportionately contain:

- identity, scope, prerequisite, stop line;
- real cases/evidence;
- compact chunk map;
- plan-specific first-contact flags/traps;
- source/functions/tests expected for each chunk;
- subtle do-not-assume reminders;
- sufficient-to-proceed gates;
- depth/deferral and handoff condition;
- legitimate ownership opportunities only where they naturally fit.

Plans should not become textbooks, duplicate this contract, copy whole source/case artifacts, pre-answer learner checkpoints, or create artificial mutations/failures.

Before a chunk, quickly check:

```text
Are we still answering the planned real question?
Are we about to assume an unfamiliar material term/tool?
Have we used the real target example where available?
Are we introducing more than one major new mechanism?
Which source responsibility/test owns this step?
Are we preserving the proof boundary?
Are we going deeper than the plan's mastery map requires?
Is the next learner checkpoint actually fair?
```

After a chunk, check:

```text
Was the real question answered?
Can Ali connect background → real case → problem → mechanism?
Was material executable code/test meaning understood at the required depth?
Was proof/non-proof explicit?
Did Ali perform one meaningful ownership action?
Is any remaining gap truly RED, or can it remain [~]?
```

Plans are not a queue that must be exhausted before building resumes. If live project state makes a later plan stale, re-anchor instead of completing obsolete study for ceremony.

## 15. Career ownership overlay — reference, do not duplicate

`CAREER_DAY30_OWNERSHIP_HANDOFF.md` owns the detailed Career evidence protocol. This contract preserves only the package-level invariants:

```text
CURRENT-SOURCE UNDERSTANDING
must come from executable source reconstruction, not docstrings alone

REPRESENTATIVE TEST UNDERSTANDING
must include setup/action/assertion/protected behavior/non-proof, not merely green status

OWNERSHIP-BEARING MODIFICATION
only when live project work legitimately selects a change; Ali forms a pre-change model and inspects the actual post-change diff/test/result

REAL FAILURE DIAGNOSIS
only when a real relevant failure/unexpected result occurs; do not manufacture one
```

AI assistance remains allowed and should be represented honestly. Career evidence never creates implementation authority or delays legitimate project progress merely to fill categories.

## 16. Learning-memory and artifact rules

`LEARNING_MEMORY.md` is a working continuity file, not a second contract or project-status owner. Update it at meaningful boundaries, corrections, discoveries, session stops, and demonstrated ownership changes—not after every message.

Use:

```text
[ ] not started / not demonstrated
[~] partial or non-blocking gap
[x] sufficient for current route
[!] blocking misconception/question
```

Record what was actually demonstrated, not what was merely explained by the AI.

Reusable notes under this folder may preserve real case references, source/test anchors, code/data flow, proof boundaries, corrections, engineering-audit findings, depth demonstrated, and deferred depth. Do not duplicate live project status or copy whole source/case artifacts.

Historical learning artifacts stay pinned to their dated/source context. If implementation or understanding changes, preserve history and add a current correction/continuation rather than silently rewriting history unless the old artifact itself is explicitly a mutable working file.

## 17. Evidence-state and proof-language discipline

Use the narrowest accurate evidence verb when the distinction matters:

```text
0 OBSERVED
1 ACQUIRED
2 VALIDATED
3 INTERPRETED
4 RECONCILED
5 CONTEXTUALIZED
6 EXERCISED
7 EVALUATED
```

These are reasoning/teaching labels, not required production enums. Do not silently promote evidence between states.

In particular:

```text
observed != validated
acquired != validated
validated != interpreted
interpreted file evidence != reconciled PR-wide evidence
contextualized static evidence != runtime exercise
an earlier state != evaluated compatibility/safety/action
```

Prefer source/responsibility-specific language over vague statements such as "UpgradePilot knows X."

For every material output where overclaiming is plausible, separate:

```text
WHAT THIS RESULT ESTABLISHES
from
WHAT THIS RESULT DOES NOT ESTABLISH
```

Source-specific states such as `member`, `not_established`, `unresolved`, and `supported_not_correlated` remain the actual domain result vocabulary; the 0–7 labels only describe evidence strength across the journey.

## 18. Package learning objective and route boundary

The reusable conceptual path is:

```text
PUBLIC DEPENDENCY UPDATE
→ exact dependency transition
→ exact dependency source/environment context
→ static workflow structure
→ static project-environment selection
→ selected-environment membership
→ static dependency consumption
├─ separate direct-package exercise evidence
→ separate exact-head runtime CI authority
→ bounded CI coverage state
```

This package deliberately does not promote that chain into resolver satisfiability/currentness, static↔runtime step correlation, exact runtime-version witness, behavioral compatibility, safety, or maintainer action unless a later separately authorized responsibility establishes those propositions.

The detailed execution sequence lives in `PLAN_01_...` through `PLAN_04_...`; this contract does not duplicate those chunk routes.

## 19. Change rule

If a future learning issue exposes a reusable global rule, change this contract at a meaningful boundary. If it is plan-specific, update the owning plan. If it is only current continuity, update `LEARNING_MEMORY.md`. If it is a product behavior/architecture issue, route it through normal project authority instead of turning the learning contract into a product spec.

The target is:

```text
accurate enough
→ grounded in real evidence
→ Ali reasons before key answers
→ executable source/tests understood at the required depth
→ engineering judgment applied
→ proof limits preserved
→ keep moving with the real build
```
