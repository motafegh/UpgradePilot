# Group 2 — Product Simulation Pressures and Decision-Model Evolution

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@8f25bcb4e158f4f6e779ce63c264957f97e44771`  
**Roadmap responsibility:** Group 2 from `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** reusable study/relearning snapshot; product-simulation records are historical discovery evidence, while current accepted semantics remain owned by the current Charter/specifications  
**Target depth:** **must master / own** the decision-model concepts and why they were needed; understand individual historical simulation mechanics operationally  
**Companion:** [`02_REPRESENTATIVE_CASES_AND_TRANSFER_PATTERNS.md`](02_REPRESENTATIVE_CASES_AND_TRANSFER_PATTERNS.md)

This note answers one question:

> **How did real UpgradePilot product-simulation pressure turn an initially coarse evidence-to-action idea into the current impact-candidate → applicability → discriminating-investigation model?**

It is organized by engineering pressure, not by file or date. The companion note uses representative cases to practise the model.

---

## 1. The correct mental model for product simulation

Product simulation was not a hidden product implementation and not a source of permanent rules merely because many cases were studied.

Its engineering role was:

```text
real dependency-update case
→ preserve exact evidence and uncertainty
→ compare a simple transparent baseline with deeper investigation
→ expose where the simple model succeeds, fails, overreaches, or lacks authority
→ identify repeated responsibilities and contradicted assumptions
→ pressure-test candidate concepts against different cases
→ promote only sufficiently stable accepted semantics to their durable owner
```

That means three things must remain separate:

```text
PRODUCT-SIMULATION RESULT
historical discovery / pressure evidence

CURRENT ACCEPTED SEMANTICS
Product Decision Model specification and other canonical owners

CURRENT IMPLEMENTATION
source + tests + observed execution evidence
```

A simulation can explain **why a product responsibility became necessary** without proving that the responsibility is implemented today.

---

## 2. Why the transparent baseline mattered

The transparent baseline was deliberately weak but coherent.

It could see only four input families:

1. version-change category;
2. overall current CI conclusion;
3. dependency directness;
4. literal release-note keyword signals.

Its rules were intentionally inspectable. For example:

```text
failing/mixed CI
→ investigate_or_block

missing/unknown CI
→ run_targeted_checks

major/pre-release/caution keyword
→ run_targeted_checks

ordinary patch/minor + passing CI + known directness + no caution keyword
→ merge_after_normal_review
```

The point was **not** to make this the final decision engine.

The point was to create a reproducible comparator for the Charter thesis:

```text
Does repository-specific context + dependency-path evidence
+ upstream behavior + scoped CI evidence
materially improve the decision over a simple restricted comparator?
```

The baseline therefore created an important scientific/engineering discipline:

```text
full investigation must earn its extra cost
```

not:

```text
more analysis is automatically better
```

### Comparison dimensions were richer than “same action or different action”

A full investigation could add value by changing:

- action;
- reasoning quality;
- uncertainty location;
- targeted-check specificity;
- evidence authority;
- failure-state visibility;
- auditability/actionability;
- cost/over-investigation behavior.

So:

```text
same final action
!=
same decision-support quality
```

This became visible immediately in S001–S003.

---

## 3. Pressure 1 — broad action is too coarse to represent evidence quality

The first simulation cycle produced three cases where the transparent baseline and full investigation chose the same broad action, yet the full reasoning was materially different.

### S001/S002 cross-case lesson

The early cross-case review already contradicted shortcuts such as:

```text
green CI has global authority
```

```text
direct import is the only meaningful dependency relationship
```

```text
merge history proves correctness
```

```text
full investigation has value only if it changes the broad action
```

S001 showed a transitive documentation/tooling relationship and later became a strong example of a concerning upstream Python-support change becoming irrelevant to the exact target’s declared Python range.

S002 showed a direct dependency with adapter/framework-mediated behavior where build/install evidence existed but relevant Python behavior was not adequately exercised.

The lesson was not “S001 merge, S002 check.” The reusable lesson was:

```text
source signal
→ exact target relationship
→ exact activation/relevance question
→ scoped evidence
→ bounded conclusion
```

### S003 strengthened this with failing CI

S003 showed that red CI is also too coarse.

The useful reasoning had to descend from:

```text
workflow failed
```

into:

```text
which job?
which step?
which command?
which dependency relationship?
which exact proposed version?
which environment?
which competing cause?
```

The full investigation localized the failure to `npm ci`, connected the proposed TypeScript version to an incompatible retained peer-support range, and used a same-base adjacent comparison to strengthen attribution.

Therefore:

```text
red CI
!=
update caused failure
```

and:

```text
green CI
!=
relevant changed responsibility exercised
```

This is one origin of the later proposition-relative evidence doctrine.

---

## 4. Pressure 2 — deeper investigation must sometimes stop

If every case always activates every possible investigation, the product becomes expensive, noisy, and epistemically worse.

S004 was deliberately selected as a baseline-sufficient control.

The baseline and full investigation both selected:

```text
merge_after_normal_review
```

But the important result was not merely action equality. The full process confirmed the authority-critical assumptions with a small evidence set:

```text
changed dependency is really on the owning test path
+
exact proposed dependency is exercised
+
relevant exact-head checks pass
+
upstream information is coherent
+
no decision-critical contradiction/gap remains
→ stop
```

Conditional investigations such as exploitability analysis, local reproduction, platform analysis, and generic targeted checks were deliberately **not activated**.

This established a crucial product responsibility:

> **Non-activation and justified stopping are affirmative technical results.**

So the product needs to represent not only:

```text
what did we investigate?
```

but also:

```text
why is another investigation not justified?
```

This later becomes Conversation-C investigation/stopping semantics.

---

## 5. Pressure 3 — coarse caution can be wrong in the conservative direction

A trustworthy system must be able to become **less cautious** when exact evidence refutes the reason for caution.

S005 created the first S001–S005 broad action change:

```text
transparent baseline
→ run_targeted_checks

full evidence
→ merge_after_normal_review
```

The baseline reacted to literal `breaking`, `removals`, and `deprecations` language.

The full investigation instead decomposed the upstream text into actual activation predicates and asked whether the exact target used them.

The reusable pattern became:

```text
upstream statement
→ exact changed mechanism
→ activation condition
→ target configuration/source/usage surface
→ exact execution/evidence coverage
→ unresolved question OR closure
```

The target did not use the relevant doctest configuration, named deprecated surfaces were absent or used compatibly, and exact lock-backed pytest 9.1.1 matrix cells passed.

No remaining target-specific uncertainty could name a useful check.

Therefore:

```text
caution keyword
!= target impact
```

and:

```text
targeted check is justified
only if it answers a named unresolved question
```

This is an important bridge from the early baseline to the later impact/applicability model.

---

## 6. Pressure 4 — “dependency changed” needed an intermediate technical object

The early evidence-to-decision framing still had a conceptual hole:

```text
dependency changed
→ ???
→ target-specific conclusion
```

The product needed a way to represent **what could technically happen and through what target relationship** without prematurely claiming that it actually applies.

The later reconciliation introduced the technical impact candidate.

Current accepted conceptual form:

```text
UPSTREAM CHANGE MECHANISM
+
TARGET-RELEVANT EXPOSURE / PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET-RELEVANT CONSEQUENCE
=
TECHNICAL IMPACT CANDIDATE
```

The important word is **candidate**.

A candidate may contain hypotheses that still require evidence.

```text
candidate contains exposure X
!= exposure X established

candidate contains activation condition Y
!= Y active

candidate names possible consequence Z
!= Z observed
```

This prevented a semantic extractor, human analyst, or future model from turning candidate generation into self-authorized truth.

### S006 sharpened exposure vs activation

The S006 qldebugger/Pydantic case made the distinction concrete.

A Pydantic validator behavior change reached the target through framework/declarative integration.

The useful decomposition was approximately:

```text
upstream validator behavior change
→ target exposure: Pydantic validator/framework integration
→ activation: affected dependency version + non-string handler input
→ possible consequence: observable exception contract changes
→ evidence: tests/workflow/differential execution
```

This showed:

```text
dependency version selected
!= target exposure surface
```

and:

```text
tests/CI can be evidence in one case
but part of the exposure surface in a test-tool dependency case
```

The model therefore had to be responsibility/mechanism-specific rather than driven by a universal exposure taxonomy.

---

## 7. Pressure 5 — applicability must be proposition-based, not a vague relevance score

Once an impact candidate exists, UpgradePilot needs to decide whether the candidate applies to the exact target/revision/context.

The accepted model uses candidate-specific propositions and paths.

Possible candidate states are:

- **established applicable**;
- **established not applicable**;
- **unresolved**;
- **conflicted**.

The hard protections are more important than the labels:

```text
applicable != consequence proven
```

```text
not applicable != missing evidence
```

```text
unresolved != negative evidence
```

```text
dependency present != mechanism activated
```

### Why explicit logic matters

A candidate may require:

```text
A AND B AND C
```

or have alternative paths:

```text
A AND (B OR C)
```

If one necessary proposition in a conjunctive path is refuted, that path closes.

But refuting `B` does not close the whole candidate when `C` remains a viable alternative.

The current specification deliberately does **not** require a universal Boolean/SAT/rule engine. The point is to encode only the explicit logic the candidate actually needs.

---

## 8. Pressure 6 — negative conclusions require coverage, not confidence

A major reconciliation step was recognizing that “we did not see it” can mean many different things.

The safe default is open-world reasoning:

```text
not observed
→ unresolved / not established within admitted scope
```

not:

```text
not observed
→ absent
```

A stronger negative claim needs a justified bounded universe or other sufficiently strong negative evidence.

Later audit/pressure testing made three different coverage questions explicit.

### 8.1 Evidence coverage

```text
Did the admitted evidence sufficiently cover proposition P?
```

This controls whether non-observation can support a negative proposition.

### 8.2 Path-model coverage

```text
Did the candidate represent the material alternative applicability paths
before claiming all viable paths were eliminated?
```

### 8.3 Candidate-discovery coverage

```text
Did discovery identify enough material mechanism-specific candidates
before making a broader transition-level claim?
```

Therefore:

```text
evidence completeness
!= path-model completeness
!= candidate-discovery completeness
```

and:

```text
all discovered candidates not applicable
!= transition proven to have no material target impact
```

unless discovery coverage for that stronger conclusion is separately justified.

### S008/S009 pressure exposed the discovery problem

The candidate-discovery pressure test showed that a narrow S008 artifact-serviceability question could be completely resolved while the broader OpenCV transition still had other possible mechanisms.

S009 showed that material repository-purpose/provenance context can be decision-relevant without being forced into the technical-candidate taxonomy.

The lesson is claim-relative:

> **Coverage is always coverage of some explicit object/conclusion under some admitted channels and known blind spots.**

Not “the repository is completely understood.”

---

## 9. Pressure 7 — investigation must discriminate, not merely collect information

Once a candidate remains unresolved or conflicted, the naive next step is:

```text
collect more evidence
```

That is too weak.

The accepted investigation model asks:

```text
Where exactly is the uncertainty/conflict?
What missing fact or observation could materially change the state?
Which supported check can discriminate that question?
```

That missing fact/observation is the **discriminating target**.

So:

```text
relevant evidence
!= discriminating evidence
```

and:

```text
information gain
!= decision-relevant information gain
```

### S006 — dynamic execution was genuinely discriminating

Static evidence could identify the Pydantic behavior change and the affected target code path, but it could not settle the exact changed exception behavior.

A bounded old/new differential reproduction directly activated the implicated branch.

This showed that dynamic execution can be the best check **when the proposition is behavioral and the experiment is tightly aligned**.

### S007 — a planned execution lost its value before it ran

S007 initially had plausible next investigations such as exact wheel metadata or a resolver dry-run.

Then stronger authoritative static evidence established a deterministic package-family contradiction.

The result became:

```text
check useful at T1
+
new evidence at T2 resolves proposition
→ re-evaluate check value
→ do not execute redundant check
```

This is a major design lesson:

> **An investigation plan is not an execution obligation. Investigation value is stateful and must be recomputed as evidence changes.**

---

## 10. Different reasons for “no next investigation” must remain explainable

Cross-case pressure exposed at least three different stop meanings.

### Resolved before further execution

S007:

```text
new evidence resolves/refutes proposition
→ further check redundant
→ stop
```

### Path closed/pruned

S001-like Python-support concern:

```text
necessary applicability proposition refuted
→ deeper branch cannot change this path
→ prune
```

### Still unresolved, but no worthwhile supported investigation remains

Historical-environment examples can reach:

```text
important proposition unresolved
+
available checks lack exact scope/authority/discrimination
→ preserve unresolved
→ stop
```

These can share an operational surface such as “no next check,” but their knowledge states are different.

The current Product Decision Model therefore permits:

```text
unresolved or conflicted
+
no further justified investigation
```

without rewriting it as:

```text
not applicable
safe
or overall evidence sufficient
```

---

## 11. Pressure 8 — investigation validity is separate from execution success

A check can run successfully and still fail as evidence.

The accepted rule is:

```text
successful execution
!= valid evidence for proposition P
```

Result use depends on:

- identity;
- scope/context;
- temporal fidelity;
- contrast validity;
- reconstruction fidelity;
- authority/provenance;
- what the observation actually supports.

A modern reproduction of a historical environment does not automatically become exact historical evidence merely because the same command succeeds.

Likewise, a broad test suite that passes may be non-discriminating if it never activates the implicated branch.

This prevents “tool worked” from becoming “question answered.”

---

## 12. Pressure 9 — candidate discovery and applicability must survive wider transfer

Later S010–S012 cases are useful because they stress the same decision model in very different mechanisms.

### S010 — more than one real mechanism in one transition

A NumPy requirement broadening exposed at least two independently grounded mechanisms in the same transitive runtime area, with different target handling states.

This directly supports:

```text
first valid candidate found
!= discovery complete
```

It also shows why candidate deduplication must preserve mechanism identity rather than collapsing everything into “NumPy compatibility.”

### S011 — optional dependency environment formation precedes behavior coverage

S011 showed:

```text
optional dependency declared
!= optional dependency installed
!= runtime activation
!= behavior path exercised
```

A macOS workflow was not compatibility evidence for the MLX optional stack because it did not install that extra.

This reinforces candidate-specific activation and proposition-relative CI coverage.

### S012 — target context can include historical persisted state

S012 showed that exact current repository revision and current environment can still be incomplete when the target intentionally reloads state produced by an earlier dependency environment.

```text
fresh-state compatibility
!= persisted-state compatibility
```

Producer-version provenance can therefore be a necessary applicability input for some mechanisms.

These cases do not justify universal optional-dependency, temporal, provenance-graph, or artifact engines. They show that the **same semantic discipline transfers** without requiring one universal mechanism taxonomy.

---

## 13. The current accepted reasoning spine

All of this pressure is now condensed into the Product Decision Model specification.

The current accepted semantic spine is:

```text
PUBLIC DEPENDENCY-UPDATE PR
↓
EXACT PROPOSAL / TARGET / DEPENDENCY / VERSION / REVISION IDENTITY
↓
ADMITTED EVIDENCE ABOUT THE EXACT TRANSITION
↓
ZERO OR MORE MECHANISM-SPECIFIC TECHNICAL IMPACT CANDIDATES
↓
CANDIDATE COMPONENTS KEEP THEIR EVIDENTIAL STATUS
↓
DERIVE CANDIDATE-SPECIFIC APPLICABILITY PROPOSITIONS / PATHS
↓
EVALUATE
    established / refuted / unresolved / conflicted
↓
COMPOSE ONLY THE EXPLICIT LOGIC REQUIRED BY THAT CANDIDATE
↓
CANDIDATE KNOWLEDGE STATE
    established applicable
    established not applicable
    unresolved
    conflicted
↓
IF MATERIAL NON-FINAL STATE REMAINS
    locate uncertainty/conflict
    → identify discriminating target
    → choose justified investigation / small conditional sequence
       OR preserve non-dominated alternatives
       OR stop because no justified investigation exists
↓
OBSERVE RESULT
↓
VALIDATE RESULT IDENTITY / SCOPE / CONTEXT / CONTRAST / EVIDENTIAL MEANING
↓
REEVALUATE PROPOSITION
OR REFINE / SUPERSEDE CANDIDATE WITH LINEAGE
↓
REPEAT ONLY WHILE MATERIAL NON-FINAL STATE + USEFUL JUSTIFIED INVESTIGATION REMAIN
↓
INVESTIGATION STOP
↓
LATER OVERALL SUFFICIENCY / POLICY / MAINTAINER-FACING SYNTHESIS
```

### The boundary at the end matters

Candidate applicability and investigation stopping do **not** silently decide the entire maintainer action policy.

In particular:

```text
epistemically useful investigation
!= UpgradePilot-authorized execution
!= maintainer-facing check recommendation
```

Those boundaries may interact later, but they are not one responsibility.

---

## 14. How discovery evidence became durable knowledge

The engineering lifecycle is important:

```text
S001–S005 simulation discovery
→ repeated responsibilities + contradicted assumptions
→ D1 bounded runtime-responsibility synthesis
→ later rebase through impact/applicability/investigation concepts
→ S006/S007 and other pressure tests challenge the model
→ post-Conversation-C audit identifies bounded semantic guards
→ accepted reconciliation amendments
→ stable semantics promoted to Product Decision Model specification
```

Do not reverse that arrow.

Current sessions should normally read the Product Decision Model specification first for accepted semantics and return to simulation/audit/history only when learning **how the model was earned**, comparing alternatives, or challenging a current assumption.

---

## 15. What the simulations did *not* prove

Even the large simulation corpus does not establish:

- representative frequency of dependency-update failure modes;
- complete candidate recall;
- target safety;
- production readiness;
- final production schemas or persistence architecture;
- that every conditional investigation belongs in every case;
- that dynamic testing is always strongest;
- that static evidence is always enough;
- that LLM/agent planning is required;
- that more evidence always improves a decision;
- that the historical full-investigation decisions are universal policy labels;
- learner mastery from AI-authored scenario completion.

The cases are **contrasting engineering evidence**, not an oracle corpus.

---

## 16. Existing learning material reused rather than duplicated

Two older learning snapshots remain valuable:

- [`../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md) — deeper concept-level teaching of evidence/authority, open-world reasoning, logic, impact candidates, applicability, discriminating investigation, and deterministic/semantic boundaries.
- [`../2026-08-10-product-decision-model-a-b-c-mastery-note.md`](../2026-08-10-product-decision-model-a-b-c-mastery-note.md) — detailed frozen A→C reconciliation snapshot.

This Group 2 note does not replace them. Its distinct responsibility is to make the **case-pressure → accepted-model evolution** recoverable as part of the whole-project roadmap.

---

## 17. Depth map

### Must master / own

Be able to reason with these without memorizing prose:

```text
same action != same decision-support quality
```

```text
upstream change != target impact
```

```text
technical impact candidate != established applicability
```

```text
presence/use != activation
```

```text
not observed != absent
```

```text
evidence coverage != path-model coverage != candidate-discovery coverage
```

```text
relevant evidence != discriminating evidence
```

```text
successful execution != valid evidence
```

```text
planned check != obligation to execute
```

```text
no further justified investigation
can coexist with unresolved/conflicted state
```

```text
local candidate closure != transition-level proof of no impact
```

### Understand operationally

- why the transparent baseline was necessary;
- how S004 guards against over-investigation;
- how S005 demonstrates action-revision authority;
- how S006/S007 distinguish when execution gains or loses discriminating value;
- why later S010–S012 transfer cases strengthen the model without forcing universal abstractions;
- how historical simulation findings are promoted into current canonical specifications.

### Recognize / lookup-level

- exact scenario run IDs;
- individual artifact filenames inside historical simulation bundles;
- exact audit finding IDs;
- all case-specific tools/packages/configuration details.

### Deliberately deferred

- current implementation of impact/applicability/investigation under `src/upgradepilot/` — Group 9;
- CI parser/workflow implementation — Group 8;
- artifact-serviceability implementation — Group 7;
- B2/X1 model-driven evidence-gap planning — Group 12;
- full governance/evaluation-system engineering — Group 13.

---

## 18. Fast relearning route

1. Re-read Sections **2–5** to recover why the baseline and S001–S005 mattered.
2. Re-read Sections **6–10** to recover candidate → applicability → coverage → investigation.
3. Re-read Section **13** and redraw the accepted reasoning spine from memory.
4. Open the companion case note and explain why S004, S005, S006, and S007 require different investigation behavior.
5. If any concept remains fuzzy, use the older seven-concept note rather than expanding this artifact into a full theory tutorial.

---

## 19. Ownership / transfer questions

1. Why did S001–S003 still add product value when the broad baseline action did not change?
2. What exactly did S004 prove about stopping, and what did it **not** prove about patch updates with green CI?
3. Why was S005 allowed to move from `run_targeted_checks` to `merge_after_normal_review` without becoming reckless?
4. Why is an impact **candidate** intentionally weaker than an impact conclusion?
5. Give an example where a target exposure exists but the activation condition is false.
6. Why are evidence coverage, path-model coverage, and candidate-discovery coverage three different proof obligations?
7. Why can a dynamic test be the best investigation in S006 but unnecessary in S007?
8. How can `unresolved + no further justified investigation` be a correct endpoint?
9. Why does S010 matter even if one strong candidate was already found?
10. Why do S011 and S012 argue for candidate-specific context instead of one universal “dependency used” flag?

---

## 20. Primary evidence anchors

Current accepted owner:

- `../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`

Primary simulation/discovery anchors inspected at this horizon:

- `../../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`
- `../../product-simulation/SCENARIO_COVERAGE.md`
- `../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`
- `../../product-simulation/S003_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S004_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S005_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`
- `../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`
- `../../product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md`
- `../../product-simulation/CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`
- `../../product-simulation/CONVERSATION_C_HANDOFF_S007_2026-08-09.md`
- `../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`
- `../../product-simulation/S010_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S011_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S012_POST_CASE_SYNTHESIS.md`
- `../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`

Historical audit/simulation records above explain how accepted semantics were pressure-tested; they do not replace the current specification.

No new bounded Audit was required while authoring this note: the inspected historical records and current specification were materially coherent, and the earlier AUDIT-003 findings are already part of the recorded historical reconciliation path.