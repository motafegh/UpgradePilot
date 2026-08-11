# UpgradePilot Seven-Concept Foundation — Pre-A→C Implementation Study Note

**Study-note date:** 2026-08-10  
**Purpose:** Teach the minimum seven concepts Ali should operationally understand before returning to the approved B2 A→C implementation foundation.  
**Conceptual baseline:** post-Conversation-A/B/C reconciliation and post-AUDIT-003 corrections, including the approved [`../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).  
**Primary deep reference:** [`2026-08-10-product-decision-model-a-b-c-mastery-note.md`](2026-08-10-product-decision-model-a-b-c-mastery-note.md).  
**Authority:** educational artifact only. This file does not select implementation, change project scope, authorize execution, or replace source/tests. `../MEMORY.md` alone owns live continuation.  
**Target depth:** **operational understanding with guidance** across all seven concepts, with selected parts approaching implementation-adjacent understanding. This note is **not** a mastery certification.

---

# 1. Why this note exists

The A→C discussions covered many ideas. Relearning every detail before implementation would be inefficient.

This note therefore compresses the preparation target to seven concepts that have the highest leverage over the next implementation phase:

1. **Evidence vs inference vs authority**
2. **Open-world reasoning and completeness**
3. **Necessary/sufficient conditions and AND/OR paths**
4. **Impact candidate: mechanism → exposure → activation → consequence**
5. **Applicability: established / refuted / unresolved / conflicted**
6. **Discriminating target and investigation selection**
7. **Deterministic vs semantic responsibility and LLM authority**

These seven concepts are not arbitrary theory. Together they explain the core pre-D reasoning chain that UpgradePilot is preparing to implement:

```text
trusted evidence
↓
technical impact candidate
↓
explicit propositions / applicability paths
↓
justified applicability state
↓
remaining uncertainty or genuine conflict
↓
discriminating target
↓
next justified investigation / justified stop
↓
new evidence or preserved uncertainty
```

The goal is not to memorize every sentence in this document. The goal is to be able to **reason correctly when the code later embodies these ideas**.

---

# 2. How to study this note

For each concept, use four passes:

```text
PASS 1 — recognition
Can I explain the terminology in my own words?

PASS 2 — reasoning
Can I solve the small examples without looking at the answer?

PASS 3 — transfer
Can I apply the concept to a different dependency-update case?

PASS 4 — implementation readiness
Can I predict what state or test the code should produce?
```

Do not judge understanding by whether a paragraph “feels familiar.”

A stronger test is:

> Can I use the idea correctly when the facts are changed?

At the end of every concept there is a **minimum mastery check**. If those checks are reasonably comfortable, the concept is ready to move into implementation practice.

---

# 3. Concept 1 — Evidence vs inference vs authority

## 3.1 The central mental model

The first concept is the foundation for everything else:

```text
observation
!= interpretation
!= evidence quality / authority
!= decision
```

These layers are related, but they are not interchangeable.

### Observation

An **observation** is something obtained from a source or execution.

Examples:

```text
pyproject.toml contains: requires-python = ">=3.10"
```

```text
an upstream changelog contains a sentence saying Python 3.8 support was dropped
```

```text
a CI workflow completed successfully
```

Observation answers:

> What did we actually see?

It does not yet answer what the observation means for the dependency-update decision.

### Interpretation / inference

An **interpretation** assigns meaning to an observation.

Example:

```text
observation:
requires-python = ">=3.10"

interpretation:
Python 3.8 is outside the target project's declared supported installation range.
```

An **inference** is a conclusion derived from one or more observations plus rules or reasoning.

Example:

```text
upstream dropped Python 3.8 support
+
target requires Python >=3.10
→ that particular Python-3.8 support-drop concern does not intersect the declared target range
```

That is already stronger than merely reading two files.

### Evidence

In everyday language, “evidence” can mean almost anything informative. In UpgradePilot, treat it more carefully.

Evidence is an observation or derived record being used to support or challenge a specific proposition.

The same observation can be useful evidence for one proposition and useless for another.

Example:

```text
CI passed
```

may be evidence that:

```text
the exact workflow run completed successfully
```

but it may be poor evidence for:

```text
the changed dependency was exercised
```

and almost certainly insufficient evidence for:

```text
the dependency update is safe
```

This is **proposition-relative evidence**: evidence quality depends on the question being asked.

### Authority

**Authority** asks:

> Why is this source entitled to establish this kind of fact?

Examples:

- the exact target `pyproject.toml` at the frozen PR head has strong authority for the target's declaration at that revision;
- an upstream tagged changelog may have authority for what the upstream project says changed;
- an LLM summarizing that changelog does not become the upstream authority;
- a random blog post does not automatically establish exact package behavior;
- a historical maintainer merge does not establish that the update was technically correct.

Authority belongs to the source/evidence relationship, not to the confidence of the interpreter.

```text
LLM confidence
!= source authority
```

## 3.2 Provenance

**Provenance** means the origin and transformation history of evidence.

Think:

```text
Where did this come from?
Which exact object/version/revision did it belong to?
What transformations happened before I received this record?
```

Useful provenance can include:

```text
repository
PR number
base SHA
head SHA
package
old version
proposed version
upstream repository
tag / commit
source file
text span / offsets
observation time
transformation method
```

Why provenance matters:

```text
same branch name today
!= same commit yesterday
```

```text
same package name
!= same package version
```

```text
same command executed now
!= same historical environment
```

Without provenance, a correct fact can be attached to the wrong case.

## 3.3 Grounding and corroboration

These are easy to confuse.

### Grounding

**Grounding** connects an interpreted/extracted claim back to exact source content.

Example:

```text
LLM claim:
Python 3.8 support was dropped

↓ grounding

exact source span:
upstream changelog text corresponding to that claim
```

Grounding answers:

> Did the generated claim actually correspond to the cited source?

It does **not** necessarily answer:

> Is that source claim independently true?

### Corroboration

**Corroboration** uses additional, meaningfully independent evidence to support the same claim.

Example:

```text
tagged changelog states support was dropped
+
release metadata or another authoritative upstream source independently supports the same change
```

Grounding and corroboration are therefore different:

```text
grounding
= claim ↔ cited source correspondence

corroboration
= independent evidence supports claim
```

A literal source match is not independent corroboration.

## 3.4 UpgradePilot example

Consider the implemented Target-Python relevance path:

```text
Observation A:
upstream changelog text exists

Semantic interpretation:
text means Python 3.8 support was dropped

Grounding:
claim reconstructs exactly to authoritative source span

Observation B:
target exact-head pyproject.toml says requires-python >=3.10

Deterministic interpretation:
Python 3.8 is outside that declared range

Bounded result:
outside_declared_python_range
```

What is **not** justified:

```text
therefore the whole dependency update is safe
therefore all compatibility concerns are absent
therefore CI is sufficient
therefore maintainer should merge
```

That is the practical purpose of separating observation, interpretation, authority, and decision.

## 3.5 Common reasoning failures

### Failure 1 — source says X, therefore X is universally true

Wrong because source authority is scoped.

An upstream changelog is authoritative for an upstream claim, but not automatically proof of every target consequence.

### Failure 2 — LLM found the right sentence, therefore interpretation is correct

Wrong because grounding does not guarantee semantic correctness.

### Failure 3 — CI passed, therefore update is compatible

Wrong because a passing workflow proves only what that workflow actually exercised with adequate authority.

### Failure 4 — same fact appeared twice, therefore corroborated

Wrong if both records derive from the same original source.

### Failure 5 — high-confidence model answer becomes evidence authority

Wrong. Model confidence is not source authority or completeness.

## 3.6 Minimum mastery check

You should be able to answer these without looking back:

1. What is the difference between an observation and an interpretation?
2. Why can the same observation be strong evidence for one proposition and weak evidence for another?
3. What is provenance?
4. What does grounding prove, and what does it not prove?
5. Why can an LLM not self-assign source authority?
6. Why does `outside_declared_python_range` not mean “safe to merge”?

---

# 4. Concept 2 — Open-world reasoning and completeness

## 4.1 The core problem

Software evidence is often incomplete.

UpgradePilot may search files, inspect release notes, inspect CI, inspect dependency relations, or query public metadata. Failure to find something does not automatically prove it does not exist.

The default discipline is:

```text
not observed
!= absent
```

This is the practical meaning of the **Open-World Assumption (OWA)**.

## 4.2 Open-World Assumption (OWA)

Full form: **Open-World Assumption**.

Practical meaning:

> The evidence currently known to the system may be incomplete, so lack of evidence is not automatically evidence of absence.

Why “open world”?

Because the universe of relevant facts is treated as still open to undiscovered information.

Example:

```text
UpgradePilot searches two files for a plugin registration
and finds nothing.
```

Under open-world reasoning:

```text
not found
→ unresolved
```

not:

```text
not found
→ plugin definitely not registered
```

## 4.3 Closed-World Assumption (CWA)

Full form: **Closed-World Assumption**.

Practical meaning:

> Within a specifically justified complete universe, anything absent from that complete universe may be treated as absent for that proposition.

Why “closed world”?

Because the relevant universe has been bounded and shown complete enough for the question.

Example:

Suppose the repository defines all supported entry points in one authoritative configuration section, and we have proven we read the complete section at the exact target revision.

Then:

```text
complete bounded entry-point inventory
+
entry X absent
→ evidence for X not being configured
```

The important rule is:

```text
CWA is local, not global
```

You do not declare the whole repository “closed world.” You justify completeness for one proposition and one bounded universe.

## 4.4 Universe of discourse

The **universe of discourse** is the exact set of objects over which a claim is being made.

Example:

> “There is no affected plugin registered.”

Before that negative statement is justified, ask:

```text
What counts as a plugin registration?
Which files/configurations are allowed to define it?
Did we inspect the complete relevant set?
For which exact revision?
```

The bounded answer defines the universe of discourse.

Without a justified universe, negative conclusions are dangerous.

## 4.5 Completeness is itself an evidence claim

A critical principle:

```text
completeness
is not an assumption;
it is something that needs evidence
```

If code says:

```text
for file in files_found:
    ...
```

that loop only proves something about `files_found`.

It does not prove `files_found` contains every relevant file.

This distinction is central to trustworthy negative inference.

## 4.6 Three different completeness / coverage questions

The A→C reconciliation identified three distinct coverage problems.

### 1. Evidence coverage

Question:

> Did the admitted evidence sufficiently cover proposition P?

Example:

```text
Proposition:
target declares Python 3.8 support

Evidence coverage question:
did we inspect the authoritative exact-head target declaration(s) needed to answer that?
```

### 2. Path-model coverage

Question:

> Did our candidate model include the material alternative applicability paths before claiming the candidate is not applicable?

Example reality:

```text
(A AND B) OR C
```

but our model represents only:

```text
A AND B
```

If `B` is refuted, the represented path closes.

But candidate-level non-applicability is not justified if `C` was a material omitted path.

Therefore the corrected rule is:

```text
established not applicable
requires:
1. every represented viable path sufficiently eliminated
AND
2. sufficient path-model coverage for the candidate-level claim
```

If:

```text
all represented paths refuted
+
path-model coverage unresolved
```

then preserve:

```text
represented paths refuted
+
coverage limitation unresolved
```

Do **not** output an unqualified `established not applicable`.

### 3. Candidate-discovery coverage

Question:

> Did we discover enough material impact candidates to make a transition-level claim such as “no relevant impact”?

Suppose UpgradePilot discovers candidates C1 and C2 and both are not applicable.

That does not automatically mean:

```text
transition has no material impact
```

because candidate C3 may never have been discovered.

Therefore:

```text
all discovered candidates not applicable
!= transition-level absence of impact
```

without separately justified candidate-discovery coverage.

## 4.7 Strong negative-evidence patterns

There is no universal list, but three recurring patterns are useful.

### Explicit authoritative exclusion

Example:

An authoritative target configuration explicitly disables or excludes the relevant mechanism.

### Complete bounded inventory

Example:

All admitted entry points are known from a complete authoritative registry, and the relevant entry is absent.

### Deterministic derivation from authoritative facts

Example:

```text
target requires Python >=3.10
upstream dropped only Python 3.8
→ set intersection is empty
```

This is stronger than “we searched for Python 3.8 and did not find it.”

## 4.8 Common reasoning failures

### Failure 1 — grep found nothing, so feature absent

Usually open-world unless search-space completeness is established.

### Failure 2 — all modeled paths closed, so candidate definitely not applicable

Only if path-model coverage is sufficient.

### Failure 3 — all discovered candidates not applicable, so update has no impact

Requires candidate-discovery coverage, which the first B2 slice does not claim universally.

### Failure 4 — model did not generate a concern, so no concern exists

Directly invalid under the project authority rules.

### Failure 5 — source unavailable, so proposition false

Unavailable evidence normally creates unresolved/degraded state, not refutation.

## 4.9 Minimum mastery check

You should be able to explain:

1. OWA vs CWA in practical software-analysis terms.
2. Why CWA must be proposition-local.
3. What “universe of discourse” means.
4. Why completeness itself needs evidence.
5. Evidence coverage vs path-model coverage vs candidate-discovery coverage.
6. Why all represented paths being refuted is not always enough for candidate-level non-applicability.
7. Why all discovered candidates being non-applicable does not prove the update has no relevant impact.

---

# 5. Concept 3 — Necessary/sufficient conditions and AND/OR paths

## 5.1 Why logic matters here

Applicability is not a vague “risk score.”

A candidate applies because certain propositions are true in a particular logical structure.

To reason correctly, you need a practical understanding of:

- proposition;
- necessary condition;
- sufficient condition;
- conjunction (`AND`);
- disjunction (`OR`);
- alternative path.

No formal logic degree is required. But the mental model must be precise.

## 5.2 Proposition

A **proposition** is a statement that can be evaluated as supported/refuted/unresolved/conflicted within an evidence boundary.

Examples:

```text
P1: the proposed dependency transition crosses a Python 3.8 support drop
P2: the exact target declares a range that includes at least one Python 3.8 stable release
P3: the affected plugin is registered in this target configuration
```

A proposition should be specific enough that evidence can bear on it.

Bad proposition:

```text
this update seems risky
```

Better proposition:

```text
the target's declared Python range intersects the upstream-dropped Python 3.8 line
```

## 5.3 Necessary condition

A condition `N` is **necessary** for proposition/path `P` when `P` cannot hold without `N`.

Logical form:

```text
P → N
```

Practical consequence:

```text
if N is refuted
→ P cannot hold through that path
```

Example:

For a Python-support-range candidate, target-range intersection is necessary for that specific support-drop concern to apply.

If the target range provably excludes Python 3.8:

```text
intersection refuted
→ that path closes
```

## 5.4 Sufficient condition

A condition `S` is **sufficient** for conclusion `P` when establishing `S` is enough to establish `P`.

Logical form:

```text
S → P
```

Important:

A condition can be sufficient without being necessary.

Example:

Suppose candidate applicability has two independent complete paths:

```text
Path 1
OR
Path 2
```

Establishing Path 1 may be sufficient for applicability even if Path 2 remains unresolved.

Path 1 is not necessary because Path 2 could also establish applicability.

## 5.5 AND / conjunction

`AND` means all required components of that path must hold.

```text
A AND B AND C
```

If one necessary component is refuted:

```text
A established
B refuted
C established
→ path refuted/closed
```

If one necessary component is unresolved:

```text
A established
B unresolved
C established
→ path unresolved
```

Do not silently treat unresolved as false.

## 5.6 OR / disjunction

`OR` represents alternatives.

```text
B OR C
```

At least one complete alternative may be enough.

Example:

```text
A AND (B OR C)
```

Equivalent path view:

```text
Path 1 = A AND B
Path 2 = A AND C
```

Now suppose:

```text
A established
B refuted
C unresolved
```

Then:

```text
Path 1 closed
Path 2 unresolved
→ candidate not established applicable
→ candidate not established not applicable
→ unresolved
```

Refuting `B` alone is insufficient because alternative `C` remains viable.

## 5.7 One complete path can establish applicability

Suppose:

```text
Path 1 = established
Path 2 = conflicted
```

If Path 1 is independently a complete sufficient applicability route, the candidate can be established applicable.

Why?

Because applicability requires at least one complete viable path.

The unnecessary alternative's conflict may still be preserved in explanation, but it does not erase the already-established complete route.

This is why a simplistic rule such as:

```text
if any conflict exists → whole candidate conflicted
```

can be wrong.

## 5.8 Non-applicability is asymmetric

Positive applicability and non-applicability have different burdens.

Positive:

```text
one complete sufficiently established path
→ applicability may be established
```

Negative:

```text
every represented viable path sufficiently eliminated
+
path-model coverage sufficient
→ candidate non-applicability may be established
```

The negative direction is harder because omitted alternatives matter.

## 5.9 Mixed unresolved/conflicted alternatives

Consider:

```text
Path 1 = unresolved
Path 2 = conflicted
```

A single scalar label may hide useful information.

The implementation may eventually expose a candidate-level state, but it must not erase the fact that the remaining alternatives are unresolved for different reasons.

This is why the plan says not to assume one four-state precedence table is automatically lossless.

The important principle is:

> Preserve enough path/proposition detail to explain why the candidate is non-final.

## 5.10 Common reasoning failures

### Failure 1 — confuse necessary with sufficient

“Dependency is installed” may be necessary for some mechanism but not sufficient for activation.

### Failure 2 — refute one OR branch and close the entire candidate

Wrong if another viable branch remains.

### Failure 3 — require every alternative to be established for positive applicability

Wrong when one complete path is already sufficient.

### Failure 4 — collapse unresolved to false

This converts ignorance into negative evidence.

### Failure 5 — collapse conflict to unresolved without preserving why

Conflict means credible evidence points in incompatible directions after normalization; unresolved may simply mean required evidence is missing/insufficient.

## 5.11 Minimum mastery check

Solve these mentally:

### Case A

```text
P = A AND B
A established
B refuted
```

Result: path closed/refuted.

### Case B

```text
P = A AND (B OR C)
A established
B refuted
C unresolved
```

Result: candidate unresolved, not non-applicable.

### Case C

```text
Path 1 established
Path 2 conflicted
```

If either path is independently sufficient, applicability can be established while preserving Path 2's conflict.

### Case D

```text
all represented paths refuted
path-model coverage unresolved
```

Result: do not assign unqualified established-not-applicable.

You should be able to explain **why**, not only give the label.

---

# 6. Concept 4 — Impact candidate: mechanism → exposure → activation → consequence

## 6.1 Why this concept exists

A dependency changed.

That fact alone does not tell us how the target is affected.

The key A-conversation correction was:

```text
upstream change
!= target impact
```

Instead, UpgradePilot reasons through a **technical impact candidate**.

Accepted mental model:

```text
UPSTREAM CHANGE MECHANISM
+
TARGET-RELEVANT EXPOSURE / PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET-RELEVANT CONSEQUENCE
=
MECHANISM-SPECIFIC IMPACT CANDIDATE
```

The whole proposition is the candidate.

## 6.2 Upstream change mechanism

The **mechanism** is the specific changed behavior/property in the dependency.

Bad mechanism description:

```text
major update
```

Better:

```text
urllib3 2.x no longer supports OpenSSL versions earlier than 1.1.1
```

Better:

```text
code generator behavior changed such that identical inputs/options may produce different generated artifacts
```

Better:

```text
plugin wrapper result/exception semantics changed
```

Why mechanism matters:

Target relevance depends on what actually changed, not merely how large the version jump appears.

## 6.3 Exposure relationship/path

**Exposure** asks:

> Through what technical relationship can that upstream mechanism matter to the target?

Exposure is broader than direct function calls.

Possible patterns include:

```text
direct call/use
transitive dependency path
framework/plugin dispatch
inverted control
build/code-generation tooling
committed generated artifacts
environment/native-library coupling
resolver/installation constraints
```

Important:

```text
target relevance
!= target ownership
```

The affected behavior may live entirely inside dependencies or environment layers while still affecting the target.

### Example: grpcio-tools

Mechanism:

```text
generator behavior may differ between old/proposed versions
```

Exposure:

```text
target owns .proto inputs and a generation script that invokes grpc_tools.protoc
```

The target may never import `grpc_tools` at runtime. The exposure is artifact-generation, not direct runtime use.

## 6.4 Activation condition

**Activation** asks:

> What must actually be true in the exact target/context for the exposure path to become relevant?

Examples:

```text
target actually runs the generator
```

```text
affected plugin is installed and registered
```

```text
the relevant lifecycle hook executes
```

```text
environment provides affected OpenSSL version
```

```text
target's supported Python range includes an upstream-dropped Python line
```

Presence does not equal activation:

```text
dependency exists
!= affected mechanism activated
```

This distinction is especially important for plugin/framework and environment cases.

## 6.5 Possible consequence

The **consequence** is the target-relevant technical difference that could result if mechanism + exposure + activation hold.

Examples:

```text
installation failure
import failure
generated API/typing artifact change
runtime hook behavior difference
protocol/schema difference
supported-environment reduction
```

The consequence should be technical and bounded.

Bad:

```text
update is dangerous
```

Better:

```text
target may become uninstallable on an environment the target declares as supported
```

## 6.6 Candidate formulation does not establish candidate truth

A major audit guard:

```text
candidate formulation
!= establishment of candidate components
```

Suppose an LLM proposes:

```text
The target may be exposed through plugin registration.
```

That does not establish plugin registration.

The candidate can contain a hypothesis that B must later evaluate.

Similarly:

```text
candidate says activation condition = Python 3.8 is in target range
```

does not mean Python 3.8 is actually in the target range.

Candidate formulation identifies **what would need to be true**, not necessarily what already is true.

## 6.7 Mechanism-specific candidates

One dependency transition may produce multiple distinct candidates.

Example:

A large package update might involve:

```text
Candidate 1 — Python-support drop
Candidate 2 — changed runtime API behavior
Candidate 3 — changed build artifact generation
```

Do not collapse these into one vague “risk candidate,” because each may have different:

- evidence;
- exposure path;
- activation conditions;
- applicability state;
- investigation.

## 6.8 UpgradePilot Target-Python anchor

The approved first implementation anchor can be mentally expressed as:

```text
MECHANISM
upstream transition crosses a Python support drop

EXPOSURE / RELATION
exact target declares an installation Python range potentially intersecting that dropped line

ACTIVATION
at least one stable Python version admitted by target belongs to the dropped upstream line

POSSIBLE CONSEQUENCE
proposed dependency may no longer support part of the target's declared installation range
```

For S001:

```text
upstream dropped Python 3.8
+
target requires Python >=3.10
→ activation relation is refuted under the accepted bounded method
```

This closes this specific concern, not every possible concern about the update.

## 6.9 Common reasoning failures

### Failure 1 — version bump category becomes mechanism

“Major update” is not enough.

### Failure 2 — dependency presence becomes exposure/activation proof

Installed does not mean affected path is active.

### Failure 3 — direct target code ownership required

False. Exposure may be transitive, framework-mediated, artifact-mediated, or environment-mediated.

### Failure 4 — possible consequence treated as observed consequence

Candidate consequence is counterfactual/possible until evidence establishes more.

### Failure 5 — one aggregate candidate for every upstream change

This makes applicability and investigation ambiguous.

## 6.10 Minimum mastery check

Given any new dependency update, you should be able to ask:

1. What exact upstream behavior/property changed?
2. Through what target-relevant technical relation could it matter?
3. What must be true to activate that relation?
4. What target-relevant consequence could occur?
5. Which of those components are already established, and which remain hypotheses?

If you cannot answer those separately, the candidate is probably still too vague.

---

# 7. Concept 5 — Applicability: established / refuted / unresolved / conflicted

## 7.1 What applicability asks

Conversation A asks:

> What technical concern could exist?

Conversation B asks:

> Does this mechanism-specific candidate apply to this exact target, revision, and context?

Applicability is therefore **candidate-specific** and **context-specific**.

Do not ask vaguely:

```text
Is this dependency risky?
```

Ask:

```text
Does candidate C apply to target T at exact revision/context R?
```

## 7.2 Proposition states

For individual propositions, use these conceptual states:

### Established

Evidence is sufficient within the admitted boundary to support the proposition.

### Refuted

Evidence is sufficient within the admitted boundary to establish the proposition is false.

### Unresolved

Available evidence is insufficient to establish or refute the proposition.

Common causes:

- evidence not yet acquired;
- source unavailable;
- evidence incomplete;
- interpretation unsupported;
- required completeness not justified.

### Conflicted

Credible evidence about the **same normalized proposition** remains genuinely contradictory after normalizing identity, revision, scope, and time.

Important:

Two observations from different revisions are not automatically a conflict.

Example:

```text
version 1 config says X
version 2 config says not-X
```

That may simply describe change over time.

Conflict exists when evidence claiming to describe the same proposition/context remains incompatible.

## 7.3 Candidate-level applicability states

The candidate-level conceptual states are:

```text
established applicable
established not applicable
unresolved
conflicted
```

### Established applicable

At least one complete viable applicability path is sufficiently established.

Remember:

```text
applicable
!= consequence observed
```

It means the candidate's mechanism/path/activation conditions are sufficiently present for the concern to be applicable—not that the consequence definitely occurred.

### Established not applicable

The corrected requirement is deliberately strict:

```text
1. every represented viable applicability path sufficiently eliminated
AND
2. path-model coverage sufficiently justified for this candidate-level negative claim
```

If all modeled paths are closed but you are not justified in believing the model contains the material alternatives, the unqualified state is too strong.

### Unresolved

A material required proposition/path/coverage question remains non-final without genuine contradictory evidence.

### Conflicted

Genuine decision-relevant contradiction remains after normalization.

## 7.4 Missing evidence is not refutation

One of the most important rules:

```text
missing evidence
!= not applicable
```

Example:

```text
target declaration file unavailable
```

does not mean:

```text
target does not support Python 3.8
```

It means the relevant proposition cannot currently be resolved from that evidence path.

## 7.5 Applicable is not consequence-proven

Suppose:

```text
upstream OpenSSL floor changed
+
target environment definitely uses affected OpenSSL version
```

That may establish applicability of the compatibility concern.

It still does not automatically establish:

```text
the application definitely crashes in every execution
```

Applicability answers whether the mechanism can materially bear on this target/context under the candidate logic.

It is not always equivalent to observed failure.

## 7.6 Conflicted vs unresolved

Unresolved:

```text
we do not have enough evidence
```

Conflicted:

```text
we have credible evidence pointing both ways for the same normalized proposition
```

Why distinguish them?

Because the next investigation may differ.

For unresolved evidence, we may need to obtain the missing authoritative fact.

For conflict, we may need to discriminate which source/context is valid, current, complete, or properly scoped.

## 7.7 State transitions are evidence-driven

Do not think of states as workflow labels that progress automatically:

```text
unresolved → established
```

only when new evidence justifies the transition.

Time spent, number of searches, or repeated model confidence does not upgrade the state.

## 7.8 UpgradePilot examples

### Example A — target range excludes dropped Python line

```text
upstream support-drop claim established
exact target declaration established
range intersection deterministically refuted
sufficient path-model coverage for this bounded candidate
→ established not applicable for this candidate
```

Again, not “update safe.”

### Example B — target declaration not available

```text
upstream claim established
target declaration proposition unresolved
→ candidate unresolved
```

### Example C — two same-context authoritative target declarations disagree

After identity/revision/scope normalization, if both remain credible and contradictory:

```text
→ conflicted
```

Then C can investigate the conflict.

## 7.9 Common reasoning failures

### Failure 1 — `unresolved` treated as cautious `false`

Still wrong.

### Failure 2 — `applicable` treated as observed consequence

Too strong.

### Failure 3 — any disagreement labeled conflict

Normalize identity/revision/scope/time first.

### Failure 4 — all represented paths closed → not applicable, ignoring path coverage

This is exactly what the final plan correction prevents.

### Failure 5 — candidate non-applicability becomes transition-level no-impact

Requires candidate-discovery coverage, which is a separate claim.

## 7.10 Minimum mastery check

You should be able to explain:

1. Proposition state vs candidate applicability state.
2. Established vs refuted vs unresolved vs conflicted.
3. Why applicable does not mean consequence observed.
4. Why unresolved does not mean false.
5. Why conflict requires normalized same-context contradiction.
6. The two-part requirement for `established not applicable`.
7. Why one candidate being not applicable says nothing definitive about undiscovered candidates.

---

# 8. Concept 6 — Discriminating target and investigation selection

## 8.1 What Conversation C is trying to solve

When B cannot reach a final applicability state, the naive response is:

```text
collect more information
```

That is too vague and often wasteful.

Conversation C asks a sharper question:

> What observation could materially change the proposition state, and which investigation is justified to obtain it?

The input is:

```text
material non-final proposition
(unresolved OR genuine conflict)
+
uncertainty/conflict location or reason
```

## 8.2 Uncertainty location

Before choosing a check, identify **where the uncertainty actually lives**.

Example:

```text
Candidate:
Python-support drop may intersect target range

Known:
upstream support drop established

Unknown:
exact target Python declaration not yet acquired
```

The uncertainty is not:

```text
“Python compatibility generally”
```

It is:

```text
exact target declaration at exact head
```

This precision prevents generic investigation checklists.

## 8.3 Discriminating target

A **discriminating target** is the missing fact, relation, observation, or counterfactual outcome whose resolution could materially change the justified state.

Why “discriminating”?

Because the target should help discriminate among competing possibilities.

Example:

```text
possibility 1:
target range includes Python 3.8

possibility 2:
target range excludes Python 3.8
```

Discriminating target:

```text
the authoritative exact-head requires-python declaration
```

Obtaining unrelated release notes may be relevant to the project but not discriminating for this uncertainty.

## 8.4 Relevant vs discriminating evidence

Important distinction:

```text
relevant evidence
!= discriminating evidence
```

Evidence can be relevant but unable to change the proposition state.

Example:

Another blog post discussing Python versions may be relevant to the topic but not authoritative or discriminating for the target's exact declaration.

The best next investigation is not necessarily the one that collects the most information.

It is the one that most usefully reduces the decision-relevant uncertainty within the admitted constraints.

## 8.5 Resolution vs reduction

An investigation does not need to fully resolve the proposition to be valuable.

### Resolution

The result can establish or refute the proposition.

### Reduction

The result narrows possibilities, eliminates paths, or changes which investigation is useful next.

Example:

A static inventory may not resolve whether a runtime mechanism activates, but it may prove one suspected path impossible and therefore prune expensive dynamic tests.

## 8.6 Candidate investigations

An **investigation** is a bounded evidence-acquisition, analysis, execution, or observation action intended to discriminate a specific uncertainty/conflict.

Examples:

```text
read exact-head target configuration
inspect authoritative dependency path
compare old vs proposed generated artifacts
observe exact environment version
run a bounded compatibility test in an admitted environment
```

Do not generate investigations from “tools we have.”

Generate them from:

```text
uncertainty location
→ discriminating target
→ candidate way to observe that target
```

## 8.7 Three boundaries around an investigation

A major refinement:

### 1. Epistemic investigation value

Question:

> If correctly obtained, would this observation materially discriminate the proposition?

This is primarily Conversation C.

### 2. UpgradePilot execution admissibility

Question:

> May UpgradePilot itself execute this investigation under capability, authorization, security, environment, cost, and non-mutation boundaries?

This is stricter.

A useful test can be epistemically good but not executable by UpgradePilot.

### 3. Maintainer-facing recommendability

Question:

> Should the final product later recommend that the maintainer run this check?

This can depend on policy, risk tolerance, urgency, cost, and final output semantics, so it crosses into later Conversation D.

Therefore:

```text
useful check
!= UpgradePilot may execute it
!= maintainer should necessarily be told to run it
```

## 8.8 No universal static-first or dynamic-first rule

Sometimes static inspection is best.

Sometimes direct experimentation is best.

### Static example

If an authoritative exact-head configuration directly answers whether a feature is enabled, running the software may be unnecessary.

### Dynamic / interventional example

In C01, if the key uncertainty is:

```text
Do old vs proposed grpcio-tools generate materially different committed artifacts from identical relevant inputs/options?
```

then a controlled differential regeneration may directly discriminate the proposition better than reading more source text.

The correct ordering depends on discrimination, fidelity, cost, safety, and pruning leverage.

## 8.9 Differential testing

**Differential testing** compares behavior under controlled old/new conditions.

Typical form:

```text
same relevant input/context
+
old dependency
→ output O1

same relevant input/context
+
proposed dependency
→ output O2

compare O1 vs O2
```

The purpose is to isolate the effect of the changed dependency as much as practical.

But a difference proves only what the contrast design supports.

## 8.10 Contrast validity

**Contrast validity** asks whether the compared conditions differ in the intended variable rather than uncontrolled confounders.

Bad differential test:

```text
old dependency on machine A
vs
new dependency on machine B with different Python/toolchain/configuration
```

Observed differences may come from many causes.

Better:

```text
same frozen inputs/options/environment
change only old vs proposed dependency where practical
```

## 8.11 Proposal-level effect vs mechanism attribution

Suppose old vs new dependency produces different output.

That can support:

```text
proposal-level effect exists under this experiment
```

but not necessarily:

```text
we know the exact internal causal mechanism
```

Causal attribution may require additional evidence.

Do not overclaim.

## 8.12 Investigation stopping

Valid Conversation-C outcomes include:

```text
selected next investigation / small conditional sequence
```

```text
no further justified investigation
```

```text
multiple admissible non-dominated alternatives remain
```

### No further justified investigation

This is valid when, for example:

- no discriminating observation is recoverable;
- available checks are invalid for the exact context;
- execution would violate security/authorization;
- remaining sources are incapable of materially changing the state;
- historical environment cannot be reconstructed with justified fidelity.

Important:

```text
no further justified investigation
!= proposition refuted
!= candidate not applicable
!= update safe
!= overall evidence sufficient
```

It often means uncertainty must remain.

## 8.13 Do not blindly retry failed acquisition

The approved plan now makes a crucial distinction.

### Evidence not yet acquired

Example:

```text
exact target declaration has not yet been requested
```

Then C may select:

```text
read exact-head target declaration
```

as the next investigation.

### Same acquisition already attempted and failed/unavailable

Then:

```text
same failed check
→ do not automatically select again
```

Retry only with a concrete justification such as:

- transient failure has cleared;
- malformed request was corrected;
- bounded retry condition is now satisfied.

Otherwise:

```text
choose materially different justified investigation
OR
no further executable investigation
+
preserve unresolved/conflicted state
```

This prevents infinite “try the same thing again” loops.

## 8.14 Non-dominated alternatives

Sometimes two investigations have genuine trade-offs:

```text
I1 = cheap, low-invasive, moderate discrimination
I2 = expensive, invasive, stronger discrimination
```

Neither clearly dominates the other.

If choosing depends on policy/maintainer preferences not owned by C, C should preserve:

```text
multiple non-dominated alternatives
```

rather than inventing a numerical ranking.

## 8.15 Candidate refinement and lineage

Sometimes an investigation reveals the original candidate itself was incomplete or wrong.

Then:

```text
Candidate V1
→ triggering observation
→ Candidate V2 / refined candidate
```

Preserve minimum lineage so the system can explain why the hypothesis changed.

But the first Target-Python implementation does **not** need to manufacture a refinement example. The invariant activates when refinement naturally occurs.

## 8.16 Minimum mastery check

You should be able to answer:

1. What is an uncertainty location?
2. What is a discriminating target?
3. Relevant vs discriminating evidence?
4. Resolution vs reduction?
5. Why can a useful investigation still be non-executable by UpgradePilot?
6. Why is there no universal static-first/dynamic-first order?
7. What does a differential test prove, and what may it not prove?
8. When is `no further justified investigation` legitimate?
9. Why should a failed exact acquisition not be selected repeatedly without retry justification?
10. Why can C legitimately return multiple non-dominated alternatives?

---

# 9. Concept 7 — Deterministic vs semantic responsibility and LLM authority

## 9.1 Why this matters

UpgradePilot deals with two broad kinds of reasoning:

1. questions that can be answered mechanically from validated inputs;
2. questions requiring interpretation of software meaning or natural language.

Treating both the same creates either brittle handcrafted semantics or excessive LLM authority.

The preferred direction is:

```text
deterministic acquisition / identity / scope
↓
bounded semantic reasoning where meaning is irreducible
↓
grounding / deterministic validation where possible
↓
bounded trusted result
↓
deterministic composition where logic is explicit
```

This is sometimes described as a **deterministic shell around bounded semantic reasoning**.

## 9.2 Deterministic responsibility

A deterministic method applies explicit rules to validated inputs and produces reproducible results.

Good deterministic candidates include:

```text
exact SHA equality
version-range membership
set intersection
canonical identity validation
changed-file membership
source-span reconstruction
complete bounded inventory membership
explicit logical composition
```

Example:

```text
Does requires-python >=3.10 admit any stable Python 3.8.Z version?
```

Once the specifier and method boundary are defined, this can be evaluated deterministically.

## 9.3 Semantic responsibility

Semantic reasoning is needed when meaning cannot safely be reduced to a small mechanical rule.

Examples:

```text
Does this changelog passage mean support for Python 3.8 was removed?
```

```text
Does this plugin implementation rely on the changed wrapper-result semantics?
```

```text
Is this generated-artifact difference materially relevant to the target interface?
```

A language model may help with these bounded interpretation tasks.

But its output remains a **derived claim**, not source truth.

## 9.4 Why not make everything deterministic?

A common temptation is to write keyword rules:

```text
if "drop" and "Python 3.8" in text:
    support_drop = True
```

This may work on known fixtures but fails on:

- different wording;
- negation;
- future vs current change;
- subject ambiguity;
- “support added” vs “support removed”;
- indirect language.

Deterministic validation is valuable, but fixture-specific semantic answers are not a general semantic method.

## 9.5 Why not ask an LLM everything?

Opposite temptation:

```text
LLM, read all evidence and tell us whether to merge.
```

This gives the model too many responsibilities:

- source authority;
- completeness;
- identity;
- logical composition;
- policy;
- safety;
- final action.

Those responsibilities require different evidence and controls.

A model must not self-assign:

```text
source authority
evidence completeness
applicability authority
execution authorization
safety
final maintainer action
```

## 9.6 Structured output is not trust

An LLM can return perfect JSON and still be wrong.

```text
schema-valid
!= semantically correct
!= authoritative
```

Deterministic schema validation answers only:

> Did the output satisfy the declared structure/types/invariants?

It does not answer:

> Is the extracted meaning true?

That requires grounding, evidence authority, and possibly corroboration or further proposition evaluation.

## 9.7 Current UpgradePilot example

The support-drop extractor illustrates the intended pattern:

```text
authoritative bounded changelog interval
↓
local LLM extracts a bounded support-drop candidate
↓
exact source reconstruction / grounding
↓
trusted grounded claim or explicit problem state
↓
exact target declaration acquisition
↓
deterministic version-range relevance
```

The LLM does not directly decide:

```text
target applicability overall
safety
merge recommendation
```

Its responsibility is much narrower.

## 9.8 Deterministic composition

Once candidate propositions and logical structure are explicit, some composition can be deterministic.

Example:

```text
Path 1 = A AND B
Path 2 = A AND C
```

Given bounded proposition states and explicit path rules, composition should not require an LLM to “feel” whether the candidate applies.

But do not overengineer:

```text
minimum deterministic composition needed by the selected slice
!= build universal rule engine / SAT solver / graph engine
```

## 9.9 Model absence is not negative evidence

If the semantic model fails to generate a claim:

```text
no claim generated
```

that does not mean:

```text
no relevant mechanism exists
```

This is a direct application of open-world reasoning and model-authority limits.

A model's failure to notice something cannot manufacture candidate-discovery completeness.

## 9.10 Common reasoning failures

### Failure 1 — “deterministic” confused with “authoritative”

A perfectly deterministic calculation over wrong/stale evidence is still wrong for the target proposition.

### Failure 2 — semantic model output treated as trusted source fact

It remains attributed/derived until validated within the accepted evidence boundary.

### Failure 3 — JSON schema treated as truth validation

Structure is not semantics.

### Failure 4 — handcrafted phrase list promoted into general semantic architecture

May be useful as baseline/test oracle, not necessarily accepted product method.

### Failure 5 — LLM asked to perform final policy/action synthesis before D is defined

Premature authority leak.

### Failure 6 — model found no issue, therefore no issue exists

Invalid without candidate-discovery completeness.

## 9.11 Minimum mastery check

You should be able to explain:

1. What types of questions belong in deterministic code?
2. What types may require semantic reasoning?
3. Why deterministic does not mean authoritative?
4. Why schema-valid model output is not trusted meaning?
5. What “deterministic shell around bounded semantic reasoning” means.
6. Which authorities an LLM must not self-assign.
7. Why absence of an LLM-generated claim is not negative evidence.
8. Why explicit proposition/path composition should usually be deterministic once logic is known.

---

# 10. The seven concepts as one connected model

The seven concepts are not separate subjects. They form one reasoning chain.

## 10.1 Start with evidence discipline

```text
source observation
↓
identity + provenance + authority
↓
interpretation / derived claim
↓
grounding / validation
```

Concepts used:

- evidence vs inference vs authority;
- deterministic vs semantic responsibility.

## 10.2 Form an impact candidate

```text
upstream mechanism
+
exposure/path
+
activation
+
possible consequence
```

Concept used:

- impact candidate.

Candidate formulation does not establish its components.

## 10.3 Derive propositions and logical paths

```text
Candidate C
↓
P1 AND (P2 OR P3)
```

Concept used:

- necessary/sufficient conditions and AND/OR paths.

## 10.4 Evaluate applicability honestly

```text
P1 established
P2 refuted
P3 unresolved
→ C unresolved
```

Concepts used:

- applicability states;
- open-world reasoning;
- completeness/coverage.

## 10.5 If non-final, investigate the right uncertainty

```text
unresolved P3
↓
why unresolved?
↓
discriminating target
↓
candidate investigation
↓
select / preserve alternatives / stop
```

Concept used:

- discriminating target and investigation selection.

## 10.6 Feed valid evidence back

```text
investigation result
↓
validate identity/context/fidelity
↓
reevaluate proposition
```

If the observation reveals a different mechanism:

```text
Candidate V1
→ observation
→ Candidate V2
```

with lineage.

---

# 11. End-to-end worked example — Python support drop

This example intentionally uses the mechanism that the approved first implementation slice plans to reuse.

## Step 1 — observation and authority

Upstream authoritative evidence indicates:

```text
Python 3.8 support was dropped in a crossed release.
```

The semantic claim is grounded to exact source content.

This establishes a bounded upstream mechanism claim. It does not establish target impact.

## Step 2 — impact candidate

```text
MECHANISM
upstream drops Python 3.8 support

EXPOSURE
proposed dependency is used by a target whose declared installation range may include Python 3.8

ACTIVATION
target range admits at least one stable Python 3.8 release

POSSIBLE CONSEQUENCE
proposed dependency may not support part of the target's declared installation range
```

## Step 3 — propositions

Possible bounded propositions:

```text
P1: upstream Python-3.8 support drop is established for exact transition
P2: exact target declaration is established
P3: target declaration admits stable Python 3.8
```

Candidate path:

```text
P1 AND P2 AND P3
```

## Step 4A — target declaration acquired and excludes Python 3.8

```text
P1 established
P2 established
P3 refuted deterministically
```

If this candidate's path-model coverage is sufficient for the bounded support-range candidate:

```text
→ established not applicable for this candidate
```

Claim limit:

```text
this support-range concern does not apply
!= whole update safe
```

## Step 4B — target declaration not yet acquired

```text
P1 established
P2 unresolved because evidence not yet acquired
```

C identifies:

```text
uncertainty location = target declaration
```

Discriminating target:

```text
exact-head authoritative requires-python declaration
```

Candidate investigation:

```text
read exact-head pyproject.toml using admitted read-only repository interface
```

This is justified because it has not yet been attempted and directly discriminates the proposition.

## Step 4C — exact acquisition already failed

If the same exact-head read has already failed/unavailable:

```text
remaining unresolved state
!= justification to repeat identical request forever
```

Ask:

```text
Is there a concrete retry justification?
```

If yes, bounded retry may be justified.

If no:

```text
materially different investigation?
```

If none exists within the admitted boundary:

```text
no further executable investigation
+
preserve unresolved state
```

Still no final maintainer action—that belongs later.

---

# 12. Transfer example — code-generation dependency

Suppose a dependency update changes `grpcio-tools`.

Do not copy the Python-support logic.

Use the same seven concepts.

## Evidence / authority

Observe exact dependency transition and authoritative upstream change information.

## Candidate

```text
MECHANISM
generator behavior changed

EXPOSURE
target invokes grpc_tools.protoc on committed source schemas

ACTIVATION
generation is run with relevant inputs/options

CONSEQUENCE
old and proposed versions may produce materially different generated artifacts
```

## Applicability propositions

Possible propositions:

```text
P1 generator is actually part of target's artifact-production path
P2 relevant generation inputs/options are known
P3 proposed version changes output for those inputs/options
```

## Investigation

If P3 remains unresolved, discriminating target may be:

```text
old-vs-proposed generated artifact difference under controlled identical inputs/options
```

A bounded differential regeneration could have high discrimination.

But execution admissibility is separate: UpgradePilot cannot run arbitrary target code merely because the experiment is useful.

This demonstrates transfer: same reasoning model, different technical mechanism.

---

# 13. Seven dangerous shortcuts to recognize immediately

Memorize these as warning signs.

## Shortcut 1

```text
source says X
→ X establishes final decision
```

Missing interpretation, scope, authority, and policy boundaries.

## Shortcut 2

```text
not found
→ absent
```

Open-world failure unless completeness is justified.

## Shortcut 3

```text
one path refuted
→ whole candidate not applicable
```

Fails when alternatives exist.

## Shortcut 4

```text
dependency changed
→ target impacted
```

Missing mechanism/exposure/activation/consequence.

## Shortcut 5

```text
missing evidence
→ not applicable
```

Confuses unresolved with negative evidence.

## Shortcut 6

```text
still unresolved
→ run more/random checks or repeat failed check
```

Investigation must target a discriminating uncertainty and avoid unjustified retry loops.

## Shortcut 7

```text
LLM says confident answer
→ trusted semantic/evidence/action authority
```

Model authority leak.

---

# 14. What to memorize vs what to understand vs what to defer

## 14.1 Memorize these compact invariants

```text
observation != interpretation != evidence quality != decision
```

```text
LLM confidence != source authority
```

```text
missing evidence != negative evidence
```

```text
not observed != absent without justified completeness
```

```text
upstream change != target impact
```

```text
presence/use != activation
```

```text
one established complete path can establish applicability
```

```text
candidate-level not-applicable requires:
all represented viable paths eliminated
+ sufficient path-model coverage
```

```text
all discovered candidates not applicable
!= transition has no impact
```

```text
relevant evidence != discriminating evidence
```

```text
useful investigation
!= UpgradePilot may execute it
!= maintainer should necessarily be told to run it
```

```text
successful execution != valid evidence
```

```text
no further justified investigation
!= not applicable
!= safe
!= overall evidence sufficient
```

```text
schema-valid model output != trusted semantic truth
```

## 14.2 Understand operationally before implementation

You should be able to use:

- OWA/CWA and bounded completeness;
- universe of discourse;
- necessary/sufficient conditions;
- AND/OR path reasoning;
- four proposition states;
- candidate mechanism/exposure/activation/consequence;
- candidate-level applicability;
- three coverage layers;
- uncertainty location;
- discriminating target;
- investigation selection and stopping;
- differential-test and contrast-validity basics;
- deterministic vs semantic responsibility;
- model authority boundaries.

## 14.3 Defer deeper theory until implementation earns it

You do **not** need to master now:

- formal theorem proving;
- SAT/SMT solving;
- general graph algorithms;
- Bayesian decision theory;
- numerical Value of Information optimization;
- formal causal inference;
- general-purpose adaptive planning;
- event sourcing;
- universal dependency-impact taxonomy;
- autonomous agent architecture.

If real implementation later requires one of these, learn it at that point.

---

# 15. Final self-test — implementation-readiness questions

Do not treat this as an exam. Use it to expose weak spots before coding.

## Concept 1 — evidence / authority

1. A changelog says “Python 3.8 support removed.” What is the observation, what is the interpretation, and what is the source authority?
2. If an LLM correctly quotes that sentence, what did grounding establish?
3. Why does that still not establish target impact?

## Concept 2 — completeness

4. A repository search finds no reference to API `foo()`. Why is “target never uses foo” usually too strong?
5. What evidence would let you make a closed-world negative claim?
6. Explain evidence coverage vs path-model coverage vs candidate-discovery coverage.

## Concept 3 — logic

7. For `A AND (B OR C)`, what happens if `A=established`, `B=refuted`, `C=unresolved`?
8. What happens if Path 1 is established and Path 2 is conflicted, assuming either path alone is sufficient?
9. Why is non-applicability harder to establish than applicability?

## Concept 4 — impact candidate

10. For an OpenSSL requirement change, identify mechanism, exposure, activation, and possible consequence.
11. Why is “dependency is installed” usually not enough to establish activation?
12. Can target impact exist when no target-owned line directly calls the changed dependency? Explain.

## Concept 5 — applicability

13. What is the difference between `unresolved` and `conflicted`?
14. Why does `applicable` not mean the consequence definitely occurred?
15. What two things are required for unqualified `established not applicable`?

## Concept 6 — investigation

16. What is a discriminating target?
17. Why can more evidence fail to be useful?
18. When may the same failed investigation be retried?
19. Why can C return multiple non-dominated investigations?
20. What is the difference between proposal-level effect and mechanism attribution?

## Concept 7 — deterministic / semantic

21. Why should version-range intersection be deterministic?
22. Why may interpreting arbitrary release-note language require semantic reasoning?
23. Why is schema-valid model output not trusted truth?
24. Name at least four authorities an LLM cannot self-assign.
25. What does “deterministic shell around bounded semantic reasoning” mean in UpgradePilot?

If you can answer most of these accurately **in your own words and explain why**, you have enough conceptual preparation to begin implementation-adjacent learning without repeating the full A→C discussions.

---

# 16. One final mental model to carry into the next phase

When you later read or write the A→C implementation, keep asking these questions in order:

```text
1. WHAT DID WE ACTUALLY OBSERVE?
   source, identity, revision, provenance

2. WHAT DOES IT MEAN?
   deterministic interpretation or bounded semantic claim

3. WHAT TECHNICAL CANDIDATE DOES IT SUPPORT?
   mechanism + exposure + activation + consequence

4. WHAT MUST BE TRUE FOR THAT CANDIDATE TO APPLY?
   explicit propositions + AND/OR paths

5. WHAT STATE IS ACTUALLY JUSTIFIED?
   established / refuted / unresolved / conflicted
   with correct evidence/path/discovery coverage

6. IF NON-FINAL, WHAT EXACT FACT WOULD CHANGE THE STATE?
   discriminating target

7. WHAT IS THE BEST JUSTIFIED WAY TO OBSERVE THAT FACT?
   select investigation / alternatives / stop

8. WHAT AUTHORITY DOES THE RESULT REALLY HAVE?
   validate context, fidelity, grounding, limits

9. WHAT MAY WE CLAIM — AND WHAT MUST REMAIN UNKNOWN?
```

That nine-question loop is the practical bridge between the seven concepts and the code that will eventually implement them.

---

# 17. Related references

Use these only when a concept needs deeper reconstruction; this note is intended to be the first study artifact.

- [`2026-08-10-product-decision-model-a-b-c-mastery-note.md`](2026-08-10-product-decision-model-a-b-c-mastery-note.md) — broader A→C mastery/relearning snapshot from original Conversation-C closure.
- [`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md) — detailed accepted decision-model semantics and post-audit amendments.
- [`../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) — critical review that exposed important implementation guards.
- [`../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) — approved bounded implementation responsibility that these concepts prepare for.
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — stable evidence/trust/authority invariants.
- [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — generality and anti-fixture-hardcoding requirements.

Do not use these references as a requirement to relearn everything. Open them only when one of the seven concepts needs deeper evidence or historical context.
