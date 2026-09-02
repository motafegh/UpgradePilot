# Group 1 — UpgradePilot Product Thesis, Evidence Model, and Authority Model

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@40ea0f7500c331f012a75bb91203b7a5082c0fc2`  
**Roadmap responsibility:** Group 1 from `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** reusable study/relearning snapshot; not project-state, implementation, or execution authority  
**Target depth:** **must master / own** the product/evidence/claim boundaries; understand repository-artifact ownership operationally  

This note establishes the vocabulary needed for the rest of the whole-project relearning roadmap. It deliberately does **not** teach the detailed implementation mechanics of dependency parsing, uv reachability, target Python, CI parsing, impact candidates, applicability, agentic planning, or governance internals. Those are later groups.

---

## 1. The product in one accurate sentence

UpgradePilot is a **production-oriented, evidence-backed dependency-update decision-support system** for maintainers of public Python repositories receiving Dependabot pull requests.

Its job is not to decide that an update is objectively safe. Its job is to assemble relevant evidence, preserve where that evidence came from and what it actually establishes, keep uncertainty visible, and support a bounded maintainer-facing decision such as:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

The maintainer remains the decision owner. UpgradePilot does not automatically merge, approve, comment on, or otherwise mutate the target repository.

### The core product flow

At the highest level:

```text
public Python Dependabot PR
↓
identify the exact proposal / package / versions / target revision
↓
acquire relevant package, upstream, repository, dependency and CI evidence
↓
preserve source identity + time/revision + transformation context
↓
separate observations from interpretations and missing/degraded evidence
↓
reason only as strongly as the evidence permits
↓
produce a provenance-backed, uncertainty-aware decision report
↓
maintainer judgment
```

The crucial phrase is **only as strongly as the evidence permits**.

---

## 2. The technical thesis — what UpgradePilot is trying to prove useful

UpgradePilot's technical thesis is that a dependency-update decision can become more useful and better calibrated when it uses **repository-specific context**, **dependency-path evidence**, **upstream behavior changes**, and **available CI evidence**, instead of relying only on a shallow baseline such as:

```text
major/minor/patch version change
+
current CI conclusion
+
direct/transitive dependency label
+
release-note keywords
```

That thesis is intentionally a hypothesis about **decision usefulness and calibration**, not a claim that more data or more sophisticated AI is automatically better.

This leads to an important project rule:

```text
advanced method
!= automatically better method
```

A graph, LLM, learned model, agent, orchestration framework, service, or other advanced mechanism has to earn its place. The Charter requires an observable limitation, a simpler credible baseline, a bounded hypothesis, success/rejection criteria, explicit costs/failure modes, and comparative evidence before permanent adoption.

So UpgradePilot is not a project whose architecture is determined by a technology checklist. It is a product/evidence problem first.

---

## 3. The four layers you must not collapse

The most important mental model for the whole project is:

```text
OBSERVATION
!=
INTERPRETATION / INFERENCE
!=
EVIDENCE QUALITY / AUTHORITY
!=
DECISION
```

These layers can feed one another, but they are not interchangeable.

### 3.1 Observation

An observation is what was actually obtained from a source or execution.

Examples:

```text
the target pyproject.toml contains requires-python = ">=3.10"
```

```text
an upstream changelog states that Python 3.8 support was dropped
```

```text
a GitHub Actions workflow run concluded successfully
```

Observation answers:

> What did we actually see, from which source, for which exact case?

### 3.2 Interpretation / inference

Interpretation gives meaning to an observation.

Example:

```text
observation:
requires-python = ">=3.10"

interpretation:
Python 3.8 is outside that declared target Python range.
```

An inference combines observations and explicit reasoning.

Example:

```text
upstream source says Python 3.8 support was dropped
+
target declaration is >=3.10
→ this specific Python-3.8 support-drop concern does not intersect the declared target range
```

The inference is stronger than either raw observation, so it must be justified by the identities, scopes, and transformation rules involved.

### 3.3 Evidence quality / authority

Evidence is always evidence **for a proposition**.

The same observation can be strong evidence for one proposition and weak or irrelevant evidence for another.

For example:

```text
CI passed
```

may strongly support:

```text
this exact observed workflow run concluded successfully
```

but may not establish:

```text
the changed dependency was exercised by the relevant job/step
```

and does not establish:

```text
the update is safe
```

This is **proposition-relative evidence**.

Authority asks why the source is entitled to establish the kind of fact being claimed. A target repository file at the exact PR revision may have authority for the target's declaration at that revision. An upstream changelog may have authority for what the upstream project says changed. A model summarizing that changelog does not become the upstream authority merely because its summary is correct.

### 3.4 Decision

A decision is a bounded conclusion about what should happen next.

Examples include:

- enough evidence exists for merge after normal review;
- one targeted check is justified;
- a concern remains unresolved and should block/investigate;
- evidence is insufficient, so defer or abstain.

The decision layer must not silently upgrade weak evidence into certainty.

---

## 4. Two different meanings of “authority” in UpgradePilot

The word **authority** appears in two related but different engineering contexts. Keeping them separate prevents a lot of confusion.

### 4.1 Repository-artifact authority

This asks:

> Which repository artifact owns this kind of rule or fact?

Examples:

- `PROJECT_CHARTER.md` owns mission, primary user, supported decision, product boundary, evidence doctrine, admission rules and claim limits.
- accepted specifications own stable framework-independent technical behavior/invariants.
- ADRs own accepted consequential implementation/structural methods.
- a plan owns one bounded execution/investigation sequence, proof obligations and stop line.
- source/tests/commands/outputs establish implemented behavior and observed proof.
- working-memory/audits/product-simulation preserve dated reasoning, pressure evidence and history.
- learning artifacts preserve reusable understanding.
- `MEMORY.md` alone owns live project position and continuation.

This is an **ownership/navigation** question.

### 4.2 Evidence/source authority

This asks:

> Which source is entitled to support proposition P about the dependency-update case?

Examples:

- exact target repository configuration may establish a target declaration;
- PyPI metadata may establish published package/release facts within its scope;
- upstream project material may establish an attributed upstream claim;
- an observed CI run may establish facts about that run at the strength actually observed;
- an LLM interpretation cannot self-assign higher source authority.

This is an **epistemic/evidence** question: what can we know, and how strongly?

### Why both matter

A repository specification may authoritatively require UpgradePilot to preserve provenance, while the evidence inside one particular run may still be weak or unavailable.

Conversely, a strong external source fact does not become a project requirement merely because the fact is authoritative for the case.

So:

```text
repository owner authority
!=
case evidence authority
```

Both must be correct for trustworthy engineering.

---

## 5. The repository authority map you need for later groups

You do not need to memorize every governance file. You do need to know what kind of question each major artifact can answer.

| Artifact type | What it can authoritatively tell you | What it cannot prove by itself |
|---|---|---|
| `PROJECT_CHARTER.md` | What product is being built, for whom, supported outcomes, boundaries, evidence doctrine, claim limits | That a feature is implemented or currently live |
| Accepted specification | Required framework-independent behavior, invariants, accepted technical semantics | Which concrete method was chosen; whether implementation passes |
| ADR | Which consequential implementation/structural method was accepted, plus rationale/trade-offs | That code exists, runs, integrates, or passes tests |
| Plan | What one bounded responsibility should do, in what order, with what proof and stop line | Stable product semantics, architecture ownership, or implemented truth |
| Source | What implementation logic currently exists at the inspected revision | That all required behavior is correct, sufficiently tested, or product-valid |
| Tests / commands / outputs | What specific behavior was exercised/observed under their exact scope | More than the exercised cases, environments, assertions and observations support |
| Working-memory / audit / product-simulation | How a dated conclusion was reached, pressure evidence, alternatives, failures, reasoning history | Current stable rule unless promoted to the canonical owner |
| Learning artifact | Reusable teaching/relearning model tied to its evidence horizon | Current product truth or learner mastery |
| `MEMORY.md` | Live selected position, latest material verification, blocker and continuation | Stable product semantics that belong elsewhere |

### The key rule

There is no useful universal ranking such as:

```text
spec > ADR > plan > source > test > history
```

Instead, ask:

> **Which artifact owns the exact responsibility I am asking about?**

For example:

```text
“What does UpgradePilot mean by evidence provenance?”
→ Charter/Core specification

“Why does the code use this consequential parser/structure?”
→ relevant accepted ADR + source/history when needed

“What should this bounded increment implement and prove?”
→ selected plan

“What does the program actually do at this revision?”
→ source/tests/commands/outputs

“Why did we reject the earlier approach?”
→ directly relevant working-memory/audit/history
```

This responsibility-based model is much safer than treating documentation as one total precedence stack.

---

## 6. What the Core specification adds to the Charter

The Charter defines the product-level doctrine. The Core specification turns that doctrine into technical invariants that admitted implementation must preserve.

The most important Group 1 invariants are these ideas:

```text
raw/source evidence must remain distinct from normalized/trusted form
```

```text
observation, interpretation, evidence quality and decision must remain distinct
```

```text
material evidence must retain exact repository / revision identity where applicable
```

```text
material normalized evidence and factual claims need provenance to origin + time/revision + transformation
```

```text
missing, inaccessible, stale, conflicting, invalid, rejected, unsupported and not-applicable are not one generic “failure” state
```

```text
plan/specification/ADR acceptance does not prove implementation
```

```text
model output cannot assign its own evidence authority or decision effect
```

```text
grounding a model claim to source content is not independent corroboration
```

These are not stylistic preferences. They protect the product from manufacturing certainty while evidence passes through multiple transformations.

---

## 7. Provenance: the chain that makes evidence auditable

**Provenance** means the origin and transformation history needed to know what a record really represents.

For material evidence, ask:

```text
Where did this come from?
Which repository / PR / package / version / revision did it belong to?
When was it observed?
What parsing, normalization, extraction or model step changed its representation?
What authority is the transformed result still allowed to carry?
```

Why this matters:

```text
same branch name
!= same commit
```

```text
same package
!= same release
```

```text
same command text
!= same historical environment
```

```text
grounded model claim
!= independently confirmed fact
```

A technically correct statement attached to the wrong revision or context is still bad evidence for the decision being made.

---

## 8. Missing evidence is a first-class result

UpgradePilot deliberately avoids the reasoning shortcut:

```text
not observed
→ false
```

The safe default is closer to:

```text
not observed
→ unresolved / not established within the admitted evidence scope
```

A stronger negative conclusion needs a justified bounded universe or another independently sufficient form of negative evidence.

This is why the project keeps distinct states such as:

- missing;
- inaccessible;
- stale;
- conflicting;
- invalid;
- rejected;
- unsupported;
- not applicable.

These states have different meanings and different consequences.

For example:

```text
could not read target evidence
!=
target evidence refutes the concern
```

and:

```text
candidate established not applicable
!=
we failed to find evidence of applicability
```

Detailed open-world reasoning, path coverage and investigation mechanics belong to later groups. For Group 1, own the rule that **absence of evidence must not be silently rewritten as negative evidence**.

---

## 9. A real UpgradePilot reasoning example

Consider a public Dependabot PR proposing a dependency update.

Suppose the available evidence includes:

```text
A. upstream changelog says Python 3.8 support was dropped
B. target pyproject.toml at the exact PR head says requires-python = ">=3.10"
C. current CI run passed
D. an LLM summary says “low compatibility risk”
```

Now classify each item correctly.

### A — upstream changelog

This is an observation from an upstream source. It can support an attributed upstream claim about the dependency release.

It does **not** by itself establish target impact.

```text
upstream change
!= target impact
```

### B — target `requires-python`

This is target-owned declaration evidence at a particular revision.

A deterministic comparison can support a bounded inference such as:

```text
Python 3.8 is outside the target's declared >=3.10 range
```

That can refute or resolve **this particular support-drop concern** under the exact proposition being evaluated.

It still does not prove that the whole dependency update is safe.

### C — passing CI

This observation establishes only what the exact CI evidence really covers.

Without additional proof, do not silently convert:

```text
workflow/run passed
```

into:

```text
changed dependency was exercised in every relevant path
```

or:

```text
all compatibility concerns were tested
```

or:

```text
update is safe
```

### D — LLM summary

The model may provide useful bounded semantic interpretation, but the model is not the source authority and cannot assign itself stronger evidence status or final policy effect.

```text
model confidence
!= source authority
!= evidence completeness
!= decision authority
```

### What may be justified?

A disciplined conclusion may be something like:

```text
This specific Python-3.8 support-drop concern is not applicable to the target's
exact declared >=3.10 Python range at this revision.
```

What is **not** justified merely from A+B+C+D:

```text
therefore no other material impact exists
therefore CI covers all affected behavior
therefore the dependency update is objectively safe
therefore the model's “low risk” label is authoritative
```

This is the central UpgradePilot discipline: **make the smallest conclusion that the evidence actually earns**.

---

## 10. Why passing tests and successful execution are not universal proof

A test result is evidence about what the test exercised.

A passing test can prove, within its exact setup, that:

- the tested input produced the expected output;
- an asserted invariant held;
- a known failure branch behaved as expected;
- an integration path worked in that environment.

It does not automatically prove:

- all inputs in the product domain;
- all repositories;
- all dependency mechanisms;
- all target environments;
- all hidden branches;
- product safety;
- production readiness;
- that the tested architecture is the best architecture;
- that Ali independently owns the mechanism.

This is why UpgradePilot keeps **proof scope** explicit.

The same rule applies to experiments:

```text
pilot ran successfully
!= method adopted
```

and to documentation:

```text
plan/spec/ADR says behavior should exist
!= behavior implemented
```

---

## 11. Minimum Useful Generality — cases are evidence, not the product boundary

UpgradePilot uses real product-simulation cases heavily, but a known case is not allowed to redefine an automated responsibility around itself.

The controlling principle is:

> **Bound the supported domain, not the known fixture.**

Practical consequences:

- one passing fixture proves that fixture;
- caller-supplied interpretation cannot replace an interpretation responsibility the system claims to automate;
- exact known wording, package names, versions or expected answers cannot be the sole basis of accepted behavior;
- ambiguous or unsupported meaning should remain unresolved/degraded instead of guessed;
- variable-input automated behavior needs representative variation evidence;
- generality remains bounded to the admitted Python/Dependabot product horizon—universalization is not required.

This protects the project from a common learning-project failure: building something that appears intelligent only because it memorizes the examples used to develop it.

Detailed generality proofs belong with the concrete mechanisms in later groups.

---

## 12. Claim discipline — what UpgradePilot may and may not say

The Charter's default claim is **production-oriented**, not production-ready.

Do not jump from project evidence to claims such as:

- “this dependency update is safe”;
- “UpgradePilot is production-ready”;
- “the LLM/agent was successfully adopted” merely because a pilot ran;
- “the planned behavior is implemented” because a specification or plan exists;
- “Ali mastered the mechanism” because AI-generated code passed tests or a learning note exists.

The correct language tracks the evidence state:

```text
implemented
measured
experimentally observed
accepted as method
rejected
deferred
unresolved
not yet proven
```

This is not excessive caution. It is the difference between an auditable engineering claim and a portfolio story that outruns the evidence.

---

## 13. Existing learning material reused by reference

This Group 1 note is fresh because the whole-project roadmap needs one stable entry point that combines the **product thesis**, **evidence discipline**, and **repository authority model** at the current evidence horizon.

It does not replace earlier useful snapshots.

Use these for deeper follow-up rather than duplicating them here:

- `2026-08-10-seven-concept-foundation-pre-a-c-implementation.md` — deeper treatment of evidence vs inference vs authority, provenance, grounding/corroboration, open-world reasoning, applicability logic and deterministic/semantic responsibility.
- `2026-08-10-product-decision-model-a-b-c-mastery-note.md` — detailed historical mastery snapshot for the A→C product-decision-model reconciliation.

Those files remain frozen educational snapshots at their recorded horizons. They do not control current implementation or continuation.

---

## 14. Depth map for Group 1

### Must master / own

You should be able to explain and apply these without relying on wording from the note:

```text
UpgradePilot supports a maintainer decision; it does not establish objective update safety.
```

```text
observation != interpretation != evidence quality/authority != decision
```

```text
evidence is proposition-relative
```

```text
provenance preserves origin + revision/time + transformation context
```

```text
missing/unavailable evidence != negative evidence
```

```text
upstream change != target impact
```

```text
CI passed != dependency exercised everywhere != update safe
```

```text
model output != source authority != final decision authority
```

```text
plan/spec/ADR != implementation proof
```

```text
source/tests establish implemented/observed truth only within their actual scope
```

### Understand operationally

- the difference between Charter, specification, ADR, plan, source/tests, history, learning and live memory;
- why automated behavior needs bounded generality beyond one fixture;
- why advanced methods must beat simpler credible baselines before adoption;
- why evidence states and claim wording must preserve uncertainty.

### Recognize / lookup-level

- exact invariant IDs such as `OBS-001`, `PROV-001`, `AUTH-*`, `GEN-*`;
- exact ADR numbering;
- exact plan names outside the selected learning roadmap.

Know where to find them; do not memorize their identifiers.

### Deliberately deferred to later groups

- detailed impact-candidate and applicability path mechanics;
- candidate/evidence/path coverage distinctions in depth;
- dependency/version/upstream parsing implementation;
- uv lock/reachability and environment ownership;
- target-Python/environment implementation;
- artifact serviceability;
- GitHub Actions/CI parsing and proof mechanics;
- deterministic decision synthesis;
- end-to-end application composition;
- B2/X1 agentic orchestration;
- full AI-assistance/governance architecture.

---

## 15. Fast relearning route

If you return weeks later, use this route:

1. Re-read Sections **1-4** to recover the product thesis and the two meanings of authority.
2. Re-read the table in Section **5** to recover repository ownership.
3. Trace the real example in Section **9** and ask what each evidence item actually proves.
4. Rehearse the invariants in **Must master / own**.
5. If decision-model concepts feel weak, open `2026-08-10-seven-concept-foundation-pre-a-c-implementation.md` before moving to Group 2.

---

## 16. Ownership / transfer questions

You should be able to answer these before treating Group 1 as relearned:

1. A Dependabot PR has green CI. What exactly can you claim before inspecting CI scope and dependency exercise?
2. An upstream changelog states that support for Python 3.8 was dropped. What additional target evidence is needed before this becomes a target-impact conclusion?
3. An LLM extracts the right changelog sentence with 99% confidence. Why does that not give the model source authority?
4. A specification requires behavior X, but no source/test evidence was inspected. What is established and what is not?
5. A test passes for S001. Why does that not automatically establish general capability across the admitted responsibility?
6. A working-memory record contains the original rationale for a design that was later promoted to an ADR. Which artifact should you consult first for the accepted method, and when would you return to the working-memory?
7. What is the difference between repository-artifact authority and evidence/source authority?
8. What is the smallest defensible conclusion in the A+B+C+D example from Section 9?

---

## 17. Primary evidence anchors

Current/pinned owners inspected for this artifact:

- `../PROJECT_CHARTER.md`
- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/README.md`
- `../docs/architecture/README.md`
- `../plans/README.md`
- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `README.md`
- `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`

Reused historical learning snapshots:

- `2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`
- `2026-08-10-product-decision-model-a-b-c-mastery-note.md`

No broad working-memory scan was needed for Group 1 because the stable product/evidence/authority semantics are already promoted to canonical owners. No bounded Audit was required: the inspected owners were materially consistent for this responsibility.
