---
name: upgradepilot-learning-only
description: Run standalone UpgradePilot learning/mastery sessions with product mutation paused by routing to applicable package-local learning owners, real source/tests/evidence, and project-wide teaching principles. Use when Ali stops project work to study, master, reconstruct, or critically understand existing code, tests, plans, design, concepts, tools, evidence, or governance and learning itself is the selected responsibility rather than an overlay on progressing Build/Planning/Audit work.
---

# UpgradePilot Learning Only

Use this Skill as the reusable procedure for **Learning-Only** work: sessions where the selected responsibility is understanding/mastery and product mutation is paused.

**Skill provenance marker:** `UP-SKILL:upgradepilot-learning-only`

This Skill is **procedural and non-controlling**.

Root `AGENTS.md` owns authorization and operation routing. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing/teaching principles, proportionality, rationale/necessity reasoning, evidence interpretation, prerequisite repair, assistance fading, and handoff. Package-local learning contracts own their specialized learning invariants. Package execution plans and mastery/depth maps own exact local sequence and intended depth. Package `LEARNING_MEMORY.md` owns package learning continuity when such a memory exists. Active source/tests/commands/outputs remain implementation truth. Root `MEMORY.md` alone owns live product/project continuation.

The Skill routes among those owners; it does not replace or copy them. For substantive Learning-Only work, consult the relevant `OPERATING_GUIDE.md` sections when their owned teaching/evidence/proportionality/assistance-fading/handoff responsibilities are material rather than relying only on this Skill's summaries.

## Activation and no-mutation boundary

Activate this Skill when Ali explicitly selects Learning-Only behavior or clearly asks to study/master existing project material without progressing product implementation, for example:

```text
stop building and teach me this
pause implementation; I want to understand it first
just learn this code/design/plan
let's study what we already implemented
use learning-only mode
I want to master this responsibility before we continue
```

Use Learning-Only as the primary procedure when learning/mastery itself is the selected responsibility. Do not layer Learning-by-Doing onto the session merely because the learning is substantive; the shared teaching principles already come from `OPERATING_GUIDE.md`. Learning-by-Doing is instead the overlay for real project work progressing under another primary operation.

If Build/Implement or another mutating operation was previously active, an explicit learning pause switches the action boundary immediately:

```text
product/source/test/governance mutation
→ PAUSED

read/inspect/trace/explain/compare/diagnose for learning
→ allowed within the selected learning scope
```

Do not continue an obvious implementation change merely because the next edit is known.

Do not manufacture a product mutation, fake failure, artificial refactor, or unnecessary test rewrite as learner-ownership evidence.

Learning artifacts may be created or updated only when Ali's learning request actually includes/authorizes that artifact work and the applicable package/global ownership rules justify it. Learning-Only does not silently authorize repository writes merely because learning continuity could be recorded.

A later explicit request to resume building exits Learning-Only and routes to the appropriate Planning/Design, Build/Implement, Audit, or other primary operation. Do not carry Learning-Only's no-mutation boundary into a newly authorized Build request, and do not treat a learning session as prior authorization for that Build work.

### Conditional context routes during Learning-Only

**REQUIRED FOR THIS SUBSTANTIVE PROCEDURE**

- this Skill once standalone Learning-Only is selected;
- relevant `OPERATING_GUIDE.md` teaching/evidence/proportionality sections;
- the exact real source/tests/specification/ADR/plan/evidence needed for the selected learning responsibility.

**CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS**

- package-local learning contract/navigation/depth map/`LEARNING_MEMORY.md` only when a dedicated package actually applies and the current learning responsibility depends on its route/continuity;
- root `MEMORY.md` only when current product continuation or a return-to-building decision is material;
- `ENVIRONMENT.md` when reusable local execution/runtime/topology/service facts are themselves material to the learning/diagnostic question;
- `SECURITY.md` when credentials/private data/untrusted external execution or mutation/transport boundaries are material to what is being learned or diagnosed;
- `.agents/skills/upgradepilot-repository-audit/SKILL.md` when a concrete material correctness/necessity/ownership/cross-owner review becomes the primary read-only responsibility;
- Planning/Design or Build only after Ali explicitly changes the action boundary and authorizes that work.

**DO NOT LOAD REFLEXIVELY**

- every package under `learning/`, root live memory, environment/security owners, Audit, Learning-by-Doing, or mutating Skills merely because learning is substantive.

Once the learning responsibility is established, ordinary teaching/inspection chunks inherit this route. Re-evaluate only when the learning package, owner, environment/security boundary, proof need, or selected operation changes materially.

## 1. Identify the exact learning responsibility

Start with the real subject Ali wants to understand:

- one source responsibility or data flow;
- one test/proof boundary;
- one specification/ADR/design decision;
- one bounded plan and its sequencing/proof logic;
- one evidence model;
- one tool/CI/dependency mechanism;
- one failure/debugging model;
- one governance mechanism;
- or one bounded package learning continuation.

Do not begin by teaching an entire technology, module, plan family, or repository unless that breadth is genuinely the selected learning responsibility.

Use a **meaningful engineering responsibility/mechanism** as the learning unit rather than raw file size.

## 2. Discover the applicable learning owner before inventing a route

When a dedicated learning package clearly applies, inspect only the package controls needed to recover its route.

Preferred package-routing roles:

```text
package learning contract / package-level learning owner
→ package navigation / mastery-depth index when present
→ package LEARNING_MEMORY.md or equivalent learning-continuity owner when continuity matters
→ exact selected execution/learning plan
→ matching depth/mastery map when present
→ exact source/tests/evidence required for the active chunk
```

These are **responsibility roles**, not globally required filenames. Discover the package's actual filenames, plan naming, navigation structure, and local sequence from that package's own controls. Do not assume one package's file layout or route applies to another.

Do not reconstruct a package route from conversation memory when its learning files already own that route.

Do not scan every folder under `learning/` merely because Learning-Only is active. Find the package that matches the selected subject or explicit user reference; if no dedicated package exists, use the generic project-wide method without creating one merely for symmetry.

Package-specific routes, case order, chunk templates, technology depth assignments, evidence vocabularies, quotas, or other local mechanics remain local unless separately promoted through the normal governance process.

## 3. Keep project memory and learning memory separate

Two memory responsibilities may coexist:

```text
MEMORY.md
→ live project/product position and continuation

package LEARNING_MEMORY.md
→ package learning position, demonstrated understanding, open learning gaps, exact learning continuation
```

When resuming a learning package, use `LEARNING_MEMORY.md` for **learning continuation**.

If the package learning memory contains copied/datable project context, do not treat that copy as the current project-state authority. Load root `MEMORY.md` only when current product continuation or a return-to-building decision is actually material.

Do not update root `MEMORY.md` merely because the learner advanced through a lesson. Do not push root project status into package learning memory as a substitute for the live-state owner.

## 4. Load the smallest real evidence needed

Learning-Only should prefer real UpgradePilot material when it adequately demonstrates the mechanism:

```text
real source / executable constructs
real focused tests
real specifications / ADRs / plans when learning their owned decisions
real target or product-simulation evidence when appropriate to the package
real command/test output when safely inspectable
```

Synthetic material is secondary. Use it only when:

- no adequate real example exists;
- a counterexample isolates one mechanism more clearly;
- or the real example is too entangled for first contact.

When a synthetic or non-normal example is used, label its state when confusion would matter:

```text
NORMAL PATH
FAILURE / INVALID STATE
TEST FIXTURE
HYPOTHETICAL DESIGN CASE
SYNTHETIC TEACHING EXAMPLE
```

Reconnect the example to the real UpgradePilot mechanism before drawing project conclusions.

Do not teach a defensive/test-only failure as though it were the normal production path.

If a material environment/security/owner condition emerges while inspecting real evidence, consult its conditional owner before teaching the immediate tool/output state as a project fact.

## 5. Establish minimum accurate background

For genuinely unfamiliar material, provide only the background needed to reason about the selected responsibility correctly.

Normally cover, when material:

- full form / practical meaning of a new term;
- why the term/name makes sense;
- what layer/component owns it;
- important inputs/outputs/states;
- its place in the real UpgradePilot flow;
- important failure/proof boundaries;
- depth needed now versus deliberately deferred.

Do not name-drop unfamiliar technologies and immediately use them as premises.

Do not turn every encountered dependency, file format, library, CI system, or Python mechanism into a standalone course.

If a package mastery/depth map exists, defer to it for the intended depth and its project-local rationale.

## 6. Teach one minimum-complete chunk at a time

Prefer:

```text
one real question
→ one coherent responsibility/mechanism
→ one relevant evidence/input state
→ one executable transformation or decision boundary
→ one result/problem state
→ one representative proof/non-proof boundary
```

Avoid both extremes:

- jumping across several unfamiliar mechanisms in one teaching block;
- fragmenting one coherent mechanism into meaningless line-by-line trivia.

A large file may contain several depth levels. Mastering one responsibility does not imply mastering the whole module.

## 7. Make checkpoints fair and ownership-bearing

Ali may stop, challenge, question, or backtrack at any point.

Ask prediction/reconstruction/critique questions only when the needed premises have already been established. Do not quiz deliberately deferred implementation details.

Good ownership-bearing opportunities include:

- predict what an evidence transformation should preserve;
- reconstruct an input → transformation → output path;
- explain why a test discriminates one proposition;
- classify a claim's proof strength/non-proof;
- challenge whether a field/check belongs at this layer;
- compare two understood design alternatives;
- identify what evidence would resolve an uncertainty.

Apply the canonical AI-assisted engineering-ownership rule in `OPERATING_GUIDE.md` §7.2. Mastering a code-bearing responsibility is not source memorization: use understanding/tracing, reasoning, review/challenge, meaningful direction or modification, proof/test interpretation, debugging, and engineering decisions as ownership evidence. Incidental syntax/library/API details may remain operational or recognize/lookup-level when justified rather than becoming artificial mastery gates.

Immediate repetition, agreement, command execution, AI-assisted typing, or passing AI-generated tests do not by themselves demonstrate learner ownership.

When an already-taught mechanism later reappears naturally in the active package or Learning-Only session, and the needed premises remain available, use a brief retrieval/reconstruction before replaying the previous explanation when that helps assess retained understanding. If retrieval exposes a real gap, restore the missing explanation and continue from the corrected model. Do not impose a global schedule, repetition quota, or artificial exercise sequence; package-local mastery/depth rules remain authoritative inside their scope.

Fade assistance on repeated mechanisms using the project-wide model in `OPERATING_GUIDE.md`; restore explanation when a changed context reveals a genuine model/prerequisite gap.

## 8. Read executable responsibility, not comments alone

Comments/docstrings may orient the lesson, but material source ownership requires reading the executable constructs that establish the behavior.

For a selected code-bearing responsibility, recover proportionately:

```text
normal producer/caller
→ important input/type/state
→ primary/public entry point
→ material control/data-flow stages
→ important branch/problem state
→ output/result
→ downstream consumer/proof boundary
```

Use expressive source documentation as a navigation aid, not as proof that the implementation behaves as described.

For a material code-bearing ownership target, connect the source to at least one meaningful focused test when such a test exists. Explain the test as:

```text
setup / evidence state
→ action
→ assertion / result
→ protected behavior
→ what the test does NOT prove
```

If no meaningful focused test exists, state that explicitly instead of manufacturing a test-ownership claim.

## 9. Preserve technical independence and engineering judgment

Learning current code/design is not endorsement of it.

For material mechanisms, keep distinct:

```text
CURRENT IMPLEMENTATION FACT
what source/tests actually do/protect

RATIONALE / FAILURE MODE
what proposition, ambiguity, proof need, compatibility obligation, or material risk is demonstrably addressed

ENGINEERING JUDGMENT
whether the mechanism seems correct, necessary, proportionate, well placed, redundant, too weak, or too broad

AUTHORITY BOUNDARY
what may actually change the accepted contract/design/implementation
```

Never invent a rationale simply to make the existing implementation sound intentional.

When the question is **why is X needed?**, use the project-wide reasoning method:

```text
proposition / design goal
→ necessity class
→ correct responsibility/owner/layer
→ evidence for the rationale
→ credible alternative/trade-off when one exists
```

Useful reasoning labels remain:

- proposition-essential;
- current-implementation requirement;
- defensive / boundary hardening;
- uncertain / audit needed.

These are reasoning aids, not product enums. When actual implementation retention is at issue, the Core `JUST-*` specification remains normative.

Evaluate Ali's hypothesis, an earlier assistant's explanation, comments, tests, and current code by the same evidence standard. Do not optimize for agreement.

## 10. Overlapping evidence must be taught accurately

When several evidence artifacts contain overlapping facts, do not force a simplistic `artifact A tells X / artifact B tells Y` story if the real implementation is more subtle.

Establish proportionately:

```text
what each artifact directly establishes
→ where information overlaps
→ which fact is primary / derived / repeated
→ what the current implementation actually consumes
→ what relation is established only when independently produced branches are combined
→ what none of the artifacts proves alone
```

A repeated value is not automatically redundant. A relation between independently produced evidence branches may be the actual proposition under test.

When the question becomes a material correctness/necessity/ownership audit rather than a learning explanation, compose or transition to the Audit procedure while preserving Learning-Only's no-product-mutation boundary.

## 11. Apply end-to-end ownership reasoning when material

If the lesson reaches a field/check/transformation whose ownership is questioned, apply the canonical retention/end-to-end reasoning rather than explaining the local code in isolation.

Trace only as far as needed:

```text
exact proposition
→ producer
→ integration/composition
→ earliest sufficient owner
→ downstream consumer
→ independent later boundary/risk, if any
```

Current callers/tests/direct callability/fabricated fixtures are not automatic architectural justification.

Learning-Only may identify a likely simplification or defect, but it must not implement the change without a new authorized Build/Planning action boundary.

## 12. Prerequisite repair stays local

When a prerequisite gap blocks the selected learning question:

```text
exact missing link
→ why it blocks this responsibility
→ minimum complete background/practice
→ one meaningful verification
→ explicit return to the original learning subject
```

Do not silently turn prerequisite repair into a new learning package or long detour.

If the prerequisite genuinely becomes a separate multi-session learning responsibility, use the normal learning-artifact admission boundary rather than creating a package automatically.

## 13. Real failures and debugging during Learning-Only

A real unexpected failure encountered during read-only learning/diagnosis may be valuable evidence.

When safe and practical:

```text
symptom
→ boundary
→ strongest supported hypothesis
→ discriminating read-only check
→ model correction / root-cause understanding
```

Do not manufacture failures to demonstrate ownership.

If the failure makes local runtime/topology/service facts material, consult `ENVIRONMENT.md`; if credentials/private data/untrusted external execution/transport become material, consult `SECURITY.md`. Keep the diagnosis read-only while Learning-Only is active.

Do not repair product code while Learning-Only is active. If Ali chooses to fix the discovered issue, explicitly transition to Planning/Build as appropriate.

## 14. Learning plans, designs, and specifications without implementing them

Learning-Only is not code-only.

When the subject is a plan/specification/ADR/design:

- explain that artifact's exact responsibility;
- distinguish stable requirement, durable method, bounded execution coordination, implementation truth, and live state;
- inspect source/tests only when needed to compare intended versus implemented behavior;
- explain why sequence/gates/proof/stop lines exist when the evidence supports the rationale;
- do not execute the plan or modify source merely because the route becomes understandable.

If an existing plan conflicts with a specification/ADR in the latter's responsibility, surface the conflict rather than teaching the plan as higher authority.

## 15. Package-local specialization wins inside its learning responsibility

When a package contract/plan/depth map gives a stronger or more specific learning rule within its scope, apply that rule rather than flattening it into the generic Skill.

For example, a package may own:

- exact real-case progression;
- exact evidence vocabulary;
- explicit technology depth;
- package checkpoints/gates;
- local audit focus;
- exact learning continuation.

Those local rules remain local unless separately promoted through the normal governance process.

Do not copy package-specific detail into this Skill merely because it worked well in one package.

## 16. Learning memory update discipline

When a package learning memory is part of the explicitly authorized learning workflow, update it only for continuity-relevant learning facts such as:

- exact learning position/pause;
- demonstrated understanding at the package's evidence standard;
- material correction/model change;
- blocking or non-blocking learning gap;
- exact next learning continuation;
- small local engineering observation when the package contract permits it.

Do not turn `LEARNING_MEMORY.md` into polished notes, project live state, an audit archive, or a second contract.

Do not mark understanding as demonstrated solely because the assistant explained it and Ali acknowledged it.

If the learning request does not authorize learning-artifact mutation, keep the session read-only and report the continuation in conversation instead.

Do not create or expand a learning-memory/artifact solely to preserve this Skill's provenance marker.

## 17. Composition with Audit and Learning-by-Doing

### Audit inside Learning-Only

Normal Learning-Only includes proportionate critical reasoning. Do not invoke a full formal Audit Skill for every helper or explanation.

Use the Audit procedure when:

- Ali explicitly asks for an audit;
- a concrete material correctness/necessity/ownership question becomes primary;
- cross-owner consistency needs structured review;
- or a durable finding may need formal preservation.

Audit remains read-only unless a separate mutation request exists.

### Relationship to Learning-by-Doing

Both modes share global teaching principles, real evidence, technical independence, prerequisite repair, assistance fading, and proof discipline through `OPERATING_GUIDE.md`.

They differ at the action boundary:

```text
Learning by Doing
→ real project work progresses or is materially clarified under another primary operation
→ Learning-by-Doing may overlay that operation

Learning Only
→ product mutation is paused
→ mastery/understanding is the selected primary responsibility
→ the Learning-by-Doing overlay is not additionally required merely because the session is substantive
```

Do not collapse the two modes merely because both include teaching.

## 18. Return-to-building transition

When Ali explicitly decides to resume project work:

1. stop treating package learning continuation as product authorization;
2. inspect root `MEMORY.md` if live project continuation is material;
3. identify the new primary operation;
4. load its admitted procedure and exact owners;
5. preserve any learning-derived hypothesis as evidence/judgment, not as an already accepted product decision;
6. implement only within the newly authorized boundary.

If Learning-Only exposed an unresolved design concern, it may justify Planning/Audit before Build rather than immediate mutation.

## Compact session shape

A typical Learning-Only session can be as small as:

```text
exact subject / package continuation
→ minimum background
→ one real mechanism
→ Ali reasoning/challenge
→ real source/test/evidence trace
→ proof + non-proof / engineering judgment
→ continue / backtrack / defer / return-to-building decision
```

Use the smallest shape that preserves learning quality and the no-mutation boundary.

## Stop conditions

Stop or backtrack when:

- Ali challenges a premise that must be resolved before advancing;
- a prerequisite gap blocks the current mechanism;
- the package's local gate says not to proceed;
- evidence is insufficient to distinguish current fact from rationale/judgment;
- continuing would require product mutation;
- the next action belongs to another primary operation;
- or the selected learning chunk is sufficiently demonstrated for its intended depth.

When this full Skill was materially used, include `UP-SKILL:upgradepilot-learning-only` once in the normal completion/handoff provenance when practical. Marker presence records claimed Skill activation only; the actual no-mutation boundary, owner selection, teaching/evidence behavior, and transition discipline establish compliance.

Do not create a new learning package, plan, memory, audit, or implementation change merely to make the session look complete.