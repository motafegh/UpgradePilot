# UpgradePilot Product Decision Model — A→C Mastery Learning Note

**Snapshot date:** 2026-08-10  
**Snapshot scope:** Product-decision-model reconciliation through **Conversation C closure**  
**Reconciliation closure commit:** `7fedd79ecc97c71d025fd36bc4a0cfc31727a885`  
**C-closure live-memory sync:** `5870fc3962e684f9c19641b467e16da293176bad`  
**Post-learning live-memory handoff:** `76e77c95dd37145e331e7e3f09947ded3f8bbaa9`  
**Primary source record:** `../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`  
**Learning depth represented:** substantial guided product-model reasoning plus substantial implementation exposure; **not a mastery certification**  
**Authority:** educational snapshot only. This file does not control project position, implementation, safety, policy, or continuation. `../MEMORY.md` is the sole live-state owner.

---

# 1. What this note is for

This is not a transcript of the A/B/C conversations.

It is a reusable learning model for the engineering ideas that UpgradePilot has earned through implementation, challenge cases, pressure tests, and reconciliation.

You should be able to use this note later to:

- remember why the original `evidence → recommendation` idea was too weak;
- reconstruct the complete reasoning chain from a dependency-update PR to a bounded technical impact candidate;
- explain applicability using explicit propositions rather than vague risk labels;
- reason correctly about missing evidence, negative evidence, open-world/closed-world boundaries, and conflict;
- understand what deterministic code should own and what semantic/LLM reasoning may own;
- identify exactly *why* a proposition remains unresolved;
- choose or compare useful investigations without `collect everything`, fixed checklists, or fake numerical precision;
- know when a dynamic experiment is stronger than static inspection and when it is not;
- recognize invalid experiments, low-fidelity historical reconstruction, proxy evidence, and scope substitution;
- know when `no further justified investigation` is the correct result;
- preserve the boundary between Conversation C investigation stopping and Conversation D overall evidence/action sufficiency;
- transfer the model to a dependency/update case that is structurally different from the examples used here.

The goal is not to memorize every sentence. The goal is to own the **mental model, boundaries, and reasoning moves**.

---

# 2. Depth guide — what “learn this” means

The repository learning policy distinguishes levels of demonstrated understanding. For this snapshot, use three practical buckets.

## 2.1 Must remember almost verbatim

These are compact invariants that should become automatic:

```text
observation
!= interpretation
!= evidence quality
!= decision
```

```text
upstream change
!= target impact
```

```text
target relevance
!= target ownership
```

```text
missing evidence
!= negative evidence
```

```text
relevant evidence
!= sufficient/discriminating evidence
```

```text
LLM confidence
!= source authority
!= evidence completeness
!= semantic sufficiency
```

```text
uses dependency
!= participates in affected mechanism
!= relies on specific changed property
```

```text
successful investigation execution
!= valid evidence for the proposition
```

```text
proxy evidence
!= exact-context evidence
```

```text
no further justified investigation
!= not applicable
!= safe
!= overall evidence sufficient
```

These are the guardrails most likely to prevent serious reasoning errors.

## 2.2 Must understand operationally

You should be able to use these concepts on a new case with some support:

- impact candidate;
- exposure relationship/path;
- activation condition;
- possible consequence;
- applicability proposition;
- necessary versus sufficient condition;
- conjunction (`AND`) versus alternative (`OR`) paths;
- established applicable / established not applicable / unresolved / conflicted;
- open-world versus proposition-local closed-world reasoning;
- universe of discourse;
- complete bounded inventory;
- deterministic versus semantic reasoning;
- proposition formulation;
- discriminating target;
- resolution versus reduction;
- directional discrimination;
- admissibility versus preference;
- dominance / Pareto reasoning;
- pruning/shared-gate leverage;
- complementarity/corroboration;
- conditional/adaptive investigation strategy;
- bounded lookahead;
- observational versus interventional evidence;
- differential testing;
- contrast validity;
- reconstruction fidelity;
- proxy evidence;
- scope substitution;
- proposal-level effect versus causal mechanism attribution;
- investigation-result feedback into candidate refinement;
- C investigation stopping versus D sufficiency.

## 2.3 Must master later through ownership practice

Reading this note is not enough to claim mastery of:

- independently formulating complete impact candidates from unfamiliar release changes;
- independently deriving all necessary/alternative applicability propositions;
- proving a negative proposition using a correct bounded evidence universe;
- designing a safe and valid differential experiment;
- reconstructing a historical environment with justified fidelity;
- selecting the best investigation across multiple real options with limited assistance;
- modifying implementation/tests to encode the accepted A–C semantics;
- diagnosing when a real observation reveals a wrong candidate rather than merely an unresolved proposition;
- transferring the model to another ecosystem such as JavaScript, Rust, JVM, Go, native libraries, container images, OS packages, or cloud-managed dependencies.

Those require prediction, implementation/testing, diagnosis, and explanation—not passive review.

---

# 3. Why the reconciliation was necessary

UpgradePilot had already implemented a strong bounded evidence path for one specific concern: **target-Python support relevance**.

That implementation was much more disciplined than the earlier broad decision/recommendation framing.

The implemented slice had learned to distinguish:

```text
source identity
source authority
release identity
release interval
semantic claim extraction
grounding
exact source reconstruction
target declaration
target relevance
```

The old higher-level decision model still risked collapsing that careful evidence work into something like:

```text
some evidence
→ model thinks risk is low/high
→ merge/defer label
```

That would have thrown away the strongest lessons from the implementation.

The reconciliation therefore asked a deeper question:

> If the evidence engine is becoming rigorous, what is the correct whole-product reasoning model that sits above it?

The answer evolved through three closed conversations:

```text
Conversation A
What is a technical impact candidate?

Conversation B
How do we determine whether that candidate applies to the exact target/context?

Conversation C
When applicability remains unresolved, what should we investigate next?
```

Conversation D remains separate:

```text
Given all evidence and remaining uncertainty,
when is the overall evidence state sufficient to stop,
and what maintainer-facing synthesis/action is justified?
```

This separation is one of the most important product-design results.

---

# 4. The implemented evidence slice that motivated A–C

Before learning the abstract model, remember the concrete system path that exposed the need for it.

The behavior-valid target-Python path is conceptually:

```text
public repository + PR number
↓
exact PR identity + complete changed-file evidence
↓
trusted DependencyVersionChange
├── independent bounded CI dependency-exercise branch
└── upstream/target relevance branch
    ↓
    exact proposed PyPI release
    ↓
    trusted upstream GitHub repository association
    ↓
    package-wide release index
    ↓
    complete old-exclusive/proposed-inclusive crossed-release interval
    ↓
    canonical exact proposed-version Git tag
    ↓
    exact-commit changelog discovery/acquisition
    ↓
    authoritative tagged-changelog interval evidence
    ↓
    deterministic bounded Markdown source window
    ↓
    bounded local Gemma semantic candidate extraction
    ↓
    deterministic exact-source reconstruction
    ↓
    trusted grounded support-drop claim?
        ├── no → target-Python branch remains inactive/unresolved
        └── yes
            ↓
            exact target-head pyproject.toml
            ↓
            [project].requires-python
            ↓
            deterministic target-Python relevance
```

The key S001 result was:

```text
Soup Sieve 2.6 → 2.8.4
↓
2.8 explicitly drops Python 3.8 support
↓
Pydantic exact PR head declares requires-python >=3.10
↓
Python 3.8 is outside the target's declared installation range
↓
outside_declared_python_range
```

What this does **not** mean:

```text
update is safe
update is compatible in every other way
CI proves dependency exercise
maintainer should merge
```

This bounded result is an excellent example of disciplined engineering language:

> We answered one exact question strongly and refused to convert that into claims we had not proven.

That principle powers the whole A–C model.

---

# 5. Evidence-system foundations you should never skip

## 5.1 Observation, interpretation, evidence quality, decision

These are four different layers.

### Observation

Something we obtained from the world.

Examples:

```text
pyproject.toml contains `requires-python = ">=3.10"`
CI job loads `python/3.9-anaconda-2021.11`
plugin source contains `@hookimpl(wrapper=True)`
```

### Interpretation

What the observation means semantically.

Example:

```text
`requires-python >=3.10`
means Python 3.8 is outside the declared target install range
```

### Evidence quality

Whether the observation and interpretation are good enough for the proposition being evaluated.

Questions include:

```text
Is this the exact PR head?
Is the source authoritative?
Is the observation from the correct time/context?
Is the evidence complete enough for a negative claim?
Is the semantic interpretation grounded?
```

### Decision

What the system/maintainer is justified in doing or communicating after combining evidence and policy.

The critical rule is:

```text
observation
!= interpretation
!= evidence quality
!= decision
```

A system that collapses these layers becomes difficult to inspect and easy for an LLM to overclaim.

---

# 6. Authority, provenance, identity, and grounding

## 6.1 Authority

**Authority** means: why this source is entitled to establish the kind of fact we are using it for.

Examples:

- an exact target file at the frozen PR head is authoritative for that target revision's declaration;
- an upstream tagged changelog can be authoritative for release claims if provenance/identity are verified;
- random blog commentary is not automatically authoritative for an exact package behavior;
- an LLM is not a source authority just because it summarizes an authoritative source.

## 6.2 Provenance

**Provenance** means where evidence came from and how it is connected to the object being evaluated.

Example:

```text
PyPI metadata says project repository = X
exact distribution-file provenance independently corroborates X
```

This is stronger than trusting one convenient metadata field blindly.

## 6.3 Identity

Identity is not just a package name.

Relevant identities can include:

```text
repository
PR
base SHA
head SHA
dependency name
old version/range
proposed version/range
upstream repository
release/tag/commit
source file/blob
observation time
environment identity
```

Why identity matters:

```text
same package name
!= same version

same branch name
!= same commit

same module name today
!= same historical environment
```

## 6.4 Grounding

**Grounding** ties a derived claim back to exact evidence.

For semantic extraction:

```text
model says Python 3.8 support was dropped
↓
code reconstructs exact canonical source span
↓
claim remains attached to exact source identity/offsets
```

Grounding is necessary, but remember:

```text
exact source match
!= automatically correct semantic interpretation
```

A model can select a real sentence and still misunderstand it.

---

# 7. Deterministic reasoning versus semantic reasoning

This distinction appears everywhere in UpgradePilot.

## 7.1 Deterministic reasoning

A procedure is deterministic when the same validated inputs and rules produce the same result.

Examples:

```text
version A is inside/outside specifier S
SHA matches expected commit
file belongs to changed-file set
entry point is in complete inventory
exact text span matches source
set intersection is empty/non-empty
```

Deterministic does **not** mean authoritative.

A deterministic transformation over a bad source is still a bad evidence chain.

```text
deterministic transformation
!= authoritative evidence
```

## 7.2 Semantic reasoning

Semantic reasoning handles meaning that cannot be safely reduced to simple mechanical rules.

Examples:

```text
Does this release-note sentence describe removing support?
Does this plugin implementation rely on the changed wrapper-result behavior?
Does this generated diff represent an API/typing/runtime material change?
```

LLMs can be useful here.

But semantic output should be:

```text
attributed
grounded
bounded
uncertainty-preserving
```

not self-authorizing.

## 7.3 Preferred design direction

```text
deterministic evidence acquisition / identity / scope
↓
bounded semantic interpretation where needed
↓
grounding / deterministic validation where possible
↓
bounded proposition evaluation
↓
deterministic composition where logic is explicit
```

A useful phrase is:

> **deterministic shell around bounded semantic reasoning**

Why the name makes sense:

- the semantic core handles the genuinely language/meaning-heavy part;
- the surrounding shell keeps identity, evidence scope, mechanical invariants, and composition inspectable.

This is a design principle, not a requirement to literally create a class named `DeterministicShell`.

---

# 8. Conversation A — what is the thing we are investigating?

Conversation A prevented a major conceptual error: treating every upstream change as if it were already a target impact.

## 8.1 The counterfactual intuition

A dependency update is fundamentally a comparison between two target worlds:

```text
Target + old dependency world
vs
Target + proposed dependency world
```

The technical question is:

> Could a target-relevant property differ because of the dependency transition?

Possible properties include:

- runtime behavior;
- installability/resolution;
- build behavior;
- supported environment;
- data/schema/protocol/artifact behavior;
- performance/resource behavior;
- security behavior;
- test/dev-tool behavior when genuinely coupled to the changed dependency.

## 8.2 Impact candidate

Accepted definition:

> **A technical impact candidate is a target-relevant proposition that the proposed dependency transition could cause or enable a technical consequence through a technical relationship with the target under relevant activation conditions.**

The compact model:

```text
UPSTREAM CHANGE
+
TARGET-RELEVANT EXPOSURE/PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET-RELEVANT CONSEQUENCE
=
IMPACT CANDIDATE
```

The whole expression is the candidate.

It is not:

```text
change
→ impact candidate event
→ exposure
```

The candidate is the complete proposition.

---

# 9. Conversation A terminology

## 9.1 Upstream change mechanism

The specific behavior/property change in the dependency.

Examples:

```text
urllib3 removes OpenSSL <1.1.1 support
Pluggy changes wrapper/result semantics
grpcio-tools changes code-generation behavior
```

Do not use a vague label like `major version update` when the actual mechanism matters.

## 9.2 Exposure relationship/path

**Exposure** is the target-relevant relationship/path through which the changed behavior/property can reach or matter to the target.

Why the word makes sense:

> It describes how the target is exposed to the changed mechanism.

But exposure is broader than a direct function call.

Examples:

```text
direct target API call
transitive dependency path
framework/plugin dispatch
build/code-generation path
generated artifact later consumed at runtime
environment/native-library requirement
resolver relationship
```

Important:

```text
target relevance
!= target ownership
```

The affected code can live entirely in dependencies and still matter to the target.

## 9.3 Activation condition

An **activation condition** is what must hold in the exact target/context for the candidate pathway to matter.

Examples:

```text
affected plugin is installed
plugin is registered
relevant lifecycle hook is reached
environment uses affected OpenSSL version
generator is actually run
specific platform is selected
```

Presence is not activation.

```text
dependency installed
!= changed mechanism activated
```

## 9.4 Possible consequence

The target-relevant technical difference that could happen if the mechanism reaches the target under the activation conditions.

Examples:

```text
import failure
hook result/exception behavior difference
generated API/typing artifact change
install/resolution failure
runtime protocol difference
```

Do not confuse consequence with upstream change.

---

# 10. Materiality

Materiality asks whether a concern matters to the decision/investigation.

Do not collapse it into:

```text
severity
likelihood
interestingness
harm
```

A low-severity issue can still be material if it changes what check is required.

A scary-sounding issue can be immaterial to the target if the activation path is refuted.

A useful counterfactual test is:

> If this impact candidate were present versus absent, could the required investigation, uncertainty state, or maintainer-facing result meaningfully change?

If no, it may not be material for this decision.

---

# 11. Why one dependency update can create multiple candidates

An upstream version interval can contain many changed mechanisms.

Example: urllib3 1.x → 2.x included changes involving:

```text
OpenSSL/platform support
Python support
removed APIs
TLS behavior
HTTP semantics
```

Therefore:

```text
one dependency transition
!= one aggregate impact candidate
```

A better model is:

```text
version transition
→ zero or more mechanism-specific impact candidates
→ each candidate gets its own applicability/evidence reasoning
```

This avoids giant vague labels such as:

```text
urllib3 impact = high
```

---

# 12. Exposure can be multi-hop, inverted, temporal, or environment-mediated

## 12.1 Multi-hop — pip-audit / CacheControl / urllib3

The important path was not simply:

```text
pip-audit → urllib3
```

Target evidence documented a concern through CacheControl/Requests, and the incompatible interaction involved CacheControl assumptions about an urllib3 `HTTPResponse` property.

Conceptually:

```text
pip-audit
→ CacheControl
→ Requests/urllib3
→ CacheControl assumption about HTTPResponse.strict
```

This teaches:

```text
target-owned dependency edge
!= changed-dependency edge
!= actual incompatible interaction
!= full propagation path
```

## 12.2 Inverted control — Kedro / Pluggy

A framework can call target/plugin code rather than the target simply calling the framework.

```text
Kedro defines lifecycle contract
→ Pluggy manager/discovery/registration
→ hook call
→ Pluggy chooses implementations/wrappers/order
→ plugin-owned code executes
→ result/exception returns
→ Kedro continues
```

This teaches that:

```text
direct API contact
!= dynamic discovery
!= control-flow dispatch
!= plugin presence
!= executed implementation
```

## 12.3 Artifact-mediated temporal coupling — grpcio-tools

A development dependency can disappear from the final runtime environment but still change committed runtime artifacts.

```text
grpcio-tools
→ generation execution
→ generated Python/gRPC/type artifacts
→ committed package source
→ later runtime consumer
```

The dependency affects future behavior through a materialized artifact.

## 12.4 Environment-mediated — Buildtest/OpenSSL

A dependency can have a requirement that matters through the target's external environment rather than target source code.

```text
urllib3 2
→ requires OpenSSL >=1.1.1
→ target runs in externally managed HPC/Conda environment
→ exact native SSL version determines activation
```

This is why `grep target source` is not a universal investigation strategy.

---

# 13. Conversation B — does the candidate apply here?

Conversation B separates:

```text
possible technical candidate
```

from:

```text
candidate actually applicable to this exact target/revision/context
```

This is crucial.

A credible upstream change and a plausible path do not automatically establish applicability.

---

# 14. World truth versus justified knowledge state

A useful distinction:

```text
WORLD-LEVEL QUESTION
Does the candidate actually apply?
```

versus:

```text
SYSTEM-LEVEL QUESTION
What state is justified by the evidence we currently have?
```

UpgradePilot must reason about the second honestly.

Accepted conceptual knowledge states:

## 14.1 Established applicable

At least one complete viable applicability path is sufficiently established.

## 14.2 Established not applicable

Every viable applicability path is sufficiently eliminated.

## 14.3 Unresolved

A material proposition required to determine applicability cannot currently be established or refuted within the supported evidence boundary.

## 14.4 Conflicted

Credible evidence about the same normalized proposition genuinely contradicts after identity/revision/context/time/scope normalization.

These are conceptual semantics, not necessarily the final runtime enum names.

---

# 15. Proposition-based applicability

Instead of asking:

```text
Is this upgrade risky?
```

ask explicit propositions.

For Kedro/Pluggy, a pressure-test decomposition included:

```text
P1 — affected Pluggy version selected
P2 — relevant Pluggy hook-dispatch path exists
P3 — implementation using affected wrapper mechanism exists
P4 — implementation registered/participating
P5 — relevant lifecycle hook reachable in required sense
P6 — implementation actually relies on the specific changed wrapper/result/exception property
```

Why propositions are useful:

- each can be tied to evidence;
- each can be established/refuted/unresolved/conflicted;
- missing evidence remains visible;
- logical composition becomes inspectable;
- the LLM cannot hide the decision in one opaque score.

---

# 16. Necessary versus sufficient conditions

This is basic logic you must understand well.

## 16.1 Necessary condition

N is necessary for P when:

```text
P → N
```

Meaning:

> If P is true, N must be true.

Equivalent useful rule:

```text
not N
→ not P
```

But:

```text
N is true
```

alone does **not** prove P.

Example:

```text
plugin must be installed for plugin-specific wrapper behavior to occur
```

Plugin installed is necessary, but not sufficient to prove the behavior is affected.

## 16.2 Sufficient condition/set

A sufficient set contains enough established facts to justify the proposition.

The exact sufficient set is candidate-specific.

Do not invent a universal dependency-update checklist.

---

# 17. AND/OR candidate logic

For:

```text
A AND B AND C
```

if B is refuted, that path closes.

For:

```text
A AND (B OR C)
```

refuting B does not close the candidate while C remains viable.

Therefore:

```text
positive applicability
→ one complete viable path sufficiently established
```

while:

```text
non-applicability
→ every viable path eliminated
```

This asymmetry matters later in Conversation C because it creates **pruning leverage**.

---

# 18. The most important negative-evidence rule

```text
not observed
!= absent
```

Under an open-world assumption:

```text
not observed
→ unresolved
```

Only when you have a justified complete boundary can absence become negative evidence.

Examples of strong bounded negative-evidence patterns:

1. explicit authoritative exclusion;
2. complete bounded inventory;
3. deterministic derivation from authoritative facts.

Example:

```text
complete exact installed entry-point inventory
contains no plugin satisfying proposition X
```

can be strong negative evidence **for that exact inventory universe**.

But:

```text
grep target repo found nothing
```

cannot prove:

```text
no dynamic plugin exists anywhere
```

---

# 19. Open-world versus closed-world reasoning

## 19.1 Open-world assumption (OWA)

Practical meaning:

> The fact that we have not observed something does not mean it does not exist.

This is the safe default for repositories, environments, plugins, dynamic imports, external systems, and incomplete searches.

## 19.2 Closed-world assumption (CWA)

Practical meaning:

> Within a proven complete bounded universe, absence from that universe can be treated as false/absent.

UpgradePilot does **not** label a whole repository globally open-world or closed-world.

Closed-world reasoning is proposition-local.

Example:

```text
Universe:
all entry points returned by exact environment's complete package metadata inventory
```

Within that universe, absence may be meaningful.

---

# 20. Universe of discourse

**Universe of discourse** means the exact bounded set of things your proposition talks about.

Why the formal term matters:

If you do not define the universe, a negative claim often silently expands beyond the evidence.

Example:

Good:

```text
No direct call to X exists in all tracked Python files parsed at revision R.
```

Bad expansion:

```text
Target can never reach X.
```

The first claim may be mechanically justified.

The second includes dynamic imports, plugins, generated code, dependencies, runtime configuration, etc.

Rule:

> **Claims must not exceed the justified universe of discourse.**

---

# 21. Completeness is itself an evidence claim

This principle deserves its own section.

To use absence as refutation, you first need evidence that the search/inventory boundary is complete enough for the proposition.

Therefore:

```text
search result
```

and:

```text
search completeness
```

are different claims.

An LLM cannot create completeness by saying:

```text
I am 95% confident nothing else exists.
```

Model confidence is not evidence coverage.

---

# 22. Conflict must be normalized before calling it conflict

Suppose one source says:

```text
Python 3.9 supported
```

and another says:

```text
Python 3.9 unsupported
```

Before declaring `conflicted`, check:

```text
same package version?
same target revision?
same platform?
same environment?
same observation time?
same meaning of "supported"?
```

Different contexts are not necessarily contradictory.

Conflict is proposition-scoped after normalization.

---

# 23. Kedro/Pluggy — the semantic-heavy lesson

The pressure test forced us to distinguish three levels:

```text
uses dependency
!= participates in affected mechanism
!= relies on specific changed property
```

Example:

Kedro using Pluggy does not prove that:

- an affected wrapper implementation exists;
- that wrapper is registered;
- it participates in the relevant hook call;
- the hook executes;
- the implementation relies on the exact result/exception semantic that changed.

The final semantic question can remain unresolved even when P1–P5 are established.

That is not a model failure.

It is honest evidence reasoning.

Important rule:

> If the changed-property ↔ target-behavior relationship cannot be sufficiently grounded, remain unresolved instead of generating a probabilistic-looking applicability verdict.

---

# 24. Conversation C — what should we investigate next?

Conversation B can end with:

```text
candidate applicability unresolved
because proposition P6 unresolved
```

That is not yet useful enough for a product.

Conversation C asks:

> Which additional evidence/check could materially improve the justified state, and is that investigation worth doing?

This is not the same as:

```text
collect more evidence
```

or:

```text
run every available test
```

Conversation C is about **investigation selection**.

---

# 25. Evidence source, investigation, check, observation

Keep these distinct.

## 25.1 Evidence source

Where information can come from.

Examples:

```text
source file
lockfile
CI log
runtime environment
package metadata
historical manifest
upstream docs
issue discussion
```

## 25.2 Investigation

The deliberate activity used to answer a question.

Example:

```text
reconstruct exact resolved dependency graph
```

## 25.3 Check

A bounded operation/question/result boundary.

Example:

```text
Is plugin X present in the complete exact entry-point inventory?
```

## 25.4 Observation/result

What the investigation produces.

Example:

```text
entry point `foo.bar` maps to package X version Y
```

The flow is:

```text
SOURCE
↓
INVESTIGATION/CHECK
↓
OBSERVATION
↓
EVIDENCE VALIDATION/INTERPRETATION
↓
PROPOSITION EVALUATION
```

---

# 26. `Unresolved` is not enough — locate the uncertainty

These are all `unresolved`, but they require different investigations:

```text
exact historical environment version missing
```

```text
semantic meaning ambiguous
```

```text
external plugin inventory incomplete
```

```text
runtime reachability unobserved
```

```text
credible sources genuinely conflict
```

Therefore Conversation C starts from:

```text
MATERIAL UNRESOLVED PROPOSITION
+
UNCERTAINTY LOCATION / REASON
```

This is one of the most important C concepts.

---

# 27. Discriminating target

Accepted definition:

> **The missing fact, relation, observation, or counterfactual outcome whose resolution could materially change the proposition state or another decision-relevant investigation state.**

Why the name makes sense:

> It is the thing that would discriminate between materially different hypotheses/states.

Examples:

### Buildtest

```text
Exact historical SSL implementation/version
```

### Kedro

```text
Whether the exact participating implementation relies on the changed Pluggy property
```

### pip-audit

```text
Exact resolved transitive path to the incompatible interaction
```

### grpcio-tools code generation

```text
Whether old and proposed generator worlds produce different relevant artifacts
```

Bad investigation design:

```text
uncertain about OpenSSL
→ grep more Python source
```

Better:

```text
uncertain about exact OpenSSL version
→ seek exact environment/runtime/package evidence
```

---

# 28. Relevant evidence versus discriminating evidence

Example proposition:

```text
Did exact historical environment use OpenSSL <1.1.1?
```

Observation:

```text
CI ran on Perlmutter
```

Relevant? Yes.

Discriminating between `<1.1.1` and `>=1.1.1`? No.

A result such as:

```text
ssl.OPENSSL_VERSION = OpenSSL 1.1.1k
```

would discriminate strongly.

Therefore:

```text
relevance
!= discrimination
```

---

# 29. Directional discrimination

An investigation can be strong in one outcome direction and weak in another.

Example:

```text
Search for an affected wrapper implementation
```

If you find one exact witness:

```text
strong positive evidence for existence
```

If you find none in an incomplete search:

```text
weak/no negative evidence
```

So ask:

```text
What could a positive result justify?
What could a negative result justify?
What could an ambiguous/no-result justify?
```

Do not assign one generic `discrimination_score` and pretend both directions are symmetric.

---

# 30. Resolution versus reduction

An investigation can be worth doing even if it does not fully resolve the proposition.

## Resolution

```text
unresolved
→ established / refuted
```

## Reduction

```text
broad unresolved space
→ narrower unresolved space
```

Useful reductions include:

```text
3 viable paths → 1 viable path
open evidence universe → bounded inventory
unclear next question → exact discriminating target
expensive downstream checks → pruned
```

This matters because multi-step investigation planning would be impossible if every individual check had to fully resolve the final proposition.

---

# 31. Decision-relevant information gain

The concept of **Value of Information (VoI)** is useful conceptually.

But UpgradePilot does not need a fake numeric VoI optimizer.

The important rule is:

```text
information gain
!= decision-relevant information gain
```

Example:

```text
thousands of lines of upstream history
```

may add information but not answer the missing proposition.

One exact runtime/version observation may radically change the justified state.

---

# 32. Admissibility versus preference

This is the core comparison architecture.

First ask:

> Is this investigation even valid to consider?

Only then ask:

> Which admissible investigation is preferable?

## 32.1 Hard admissibility questions

Examples:

```text
Does it target a material unresolved proposition?
Can result be bound to exact proposal/revision/context?
Can the result become interpretable evidence?
Is the capability actually available?
Is execution authorized/safe?
Can the observation's context/contrast/reconstruction support the claim?
```

If a hard condition fails:

```text
reject the investigation
```

Do not compensate with:

```text
but it would be very informative
```

This is a **non-compensatory constraint**.

---

# 33. Feasibility and recoverability

An investigation can be theoretically perfect but impossible.

Example:

```text
Read the exact historical `ssl.OPENSSL_VERSION` from a CI environment that was deleted in 2023.
```

Excellent discrimination.

Potentially zero recoverability.

Therefore:

```text
theoretical discrimination
!= feasibility
```

Also:

```text
historical fact existed
!= evidence recoverable today
```

Recoverability currently belongs under feasibility conceptually; no dedicated runtime field is required.

---

# 34. Qualitative comparison without fake numerical scoring

After hard admissibility, compare options using relevant dimensions such as:

```text
discrimination direction/power
scope/context alignment
authority
coverage
cost
latency
invasiveness
risk
reproducibility
pruning/shared-gate leverage
complementarity/corroboration
```

These dimensions do not need arbitrary weights like:

```text
0.27 * discrimination + 0.18 * cost + ...
```

Qualitative comparison can be rigorous if the reasoning is explicit.

---

# 35. Dominance and Pareto reasoning

## 35.1 Dominance

Investigation A dominates B for one proposition/context when:

```text
A is no worse on all material dimensions
AND
A is materially better on at least one
AND
A introduces no compensating disadvantage
```

Then B can often be removed.

## 35.2 Pareto dominance

**Pareto dominance** is the formal decision-analysis idea behind this.

The non-dominated options form a **Pareto frontier**.

Practical UpgradePilot use:

> Remove clearly inferior choices without pretending that genuine trade-offs can be reduced to one number.

Example:

```text
I1 cheaper but weaker
I2 more expensive but much more discriminating
```

Neither necessarily dominates.

We still need qualitative reasoning.

---

# 36. Candidate logic creates pruning leverage

Suppose candidate logic is:

```text
A AND B AND C AND D
```

If A can be cheaply refuted:

```text
entire path closes
```

No need to investigate B/C/D.

For:

```text
A AND (B OR C)
```

refuting A closes all paths.

Refuting B leaves C.

Therefore an unresolved proposition can have high **shared-gate leverage**.

Why the name makes sense:

> Many downstream paths depend on the same gate.

This can make an earlier check extremely valuable even when it is not the deepest semantic question.

---

# 37. Investigation order is not logical order

The propositions may be written:

```text
P1, P2, P3, P4, P5, P6
```

That does not mean the investigation order must be:

```text
P1 → P2 → P3 → P4 → P5 → P6
```

A later proposition may be:

- easier to measure;
- more discriminating;
- a shared gate;
- capable of pruning most downstream work.

Likewise:

```text
cheapest-first
```

is not universal.

---

# 38. Conditional/adaptive investigation strategy

Accepted definition:

> **A bounded rule for selecting the next admissible investigation based on the current proposition/candidate state and observations already obtained.**

Example:

```text
check complete plugin inventory
↓
affected plugin absent?
├── yes → close path
└── no
    ↓
    inspect exact implementation semantics
    ↓
    still ambiguous?
    ├── no → return to B
    └── yes → consider targeted differential execution
```

This is better than a fixed checklist because each observation changes what is worth doing next.

---

# 39. Bounded lookahead

Adaptive planning can explode into huge decision trees.

This is **state-space explosion**:

```text
many propositions
× many possible observations
× many candidate checks
× many branches
```

UpgradePilot's accepted defense is **bounded lookahead**:

> Think far enough ahead to understand pruning, escalation, and complementarity; choose the next justified investigation or small conditional bundle; observe; then re-plan.

This is similar to a receding-horizon planning idea, but we do not need a general planning engine.

---

# 40. Complementarity, redundancy, corroboration

Two checks can be valuable together.

## 40.1 Complementarity

Example:

```text
source inspection
+
runtime trace
```

Source tells you possible/intended structure.

Trace tells you actual participation.

Together they may resolve what neither alone can.

## 40.2 Redundancy

Two checks that merely repeat the same weak observation may add little.

Example:

```text
grep lockfile
+
grep same lockfile differently
```

## 40.3 Corroboration

A second source can support the same broad fact but still add evidential value because it improves:

```text
authority
independence
coverage
conflict detection
reproducibility
```

Therefore:

```text
same semantic conclusion
!= automatically redundant evidence
```

---

# 41. Static versus dynamic evidence

## Static investigation

Examples:

```text
source inspection
AST analysis
lockfile/resolution graph
metadata/config
changelog/docs
```

Strengths often include:

```text
safe
cheap
reproducible
broad over a bounded artifact
```

Weaknesses can include:

```text
may not establish runtime participation
may not resolve semantic behavior
```

## Dynamic investigation

Examples:

```text
unit/integration test
runtime trace
build
resolver simulation
differential execution
```

Strengths can include:

```text
closer to actual behavior
strong counterfactual discrimination
```

Weaknesses can include:

```text
narrow path coverage
environment sensitivity
nondeterminism
execution risk
cost
```

Accepted rule:

```text
dynamic != universally stronger
static != universally weaker
```

There is no universal static-first or dynamic-first hierarchy.

---

# 42. Observational versus interventional evidence

## Observational

You inspect an existing fact.

Examples:

```text
historical CI log
lockfile
source file
package metadata
```

## Interventional

You deliberately change/run something and observe the effect.

Examples:

```text
install old dependency, run target
install proposed dependency, run same target
regenerate artifacts under both worlds
inject configuration to reach candidate path
```

Dependency updates are naturally counterfactual, so interventional checks can be powerful.

But they must be valid and safe.

---

# 43. Differential testing

A clean differential test tries to compare:

```text
same target revision
same relevant environment
same input/context
old dependency world
vs
proposed dependency world
```

This can strongly answer:

> Does the proposal world produce a materially different observation?

But differential testing has limits:

- path coverage;
- environment mismatch;
- nondeterminism;
- resolver/transitive changes;
- ambiguous mechanism attribution;
- unsafe execution;
- setup cost.

A differential test is powerful, not magical.

---

# 44. Pressure Test 1 — grpcio-tools code generation

This was the adversarial case designed to break the naive heuristic:

```text
cheap structural check first
→ dynamic later
```

The real case:

```text
dominodatalab/container-runtime-interface-api#101
grpcio-tools ~=1.73 → ~=1.80
```

The target has a generation script:

```text
grpc_tools.protoc
→ --python_out
→ --mypy_out
→ --grpc_python_out
→ committed src/cri_api artifacts
```

Ordinary CI installs development dependencies but does not explicitly rerun the generation script.

The central proposition became:

> With the same relevant target inputs/options, does old versus proposed generation produce different relevant generated artifacts?

Compare:

```text
I1 more target structure inspection
I2 upstream release/source semantic analysis
I3 controlled old/new regeneration + artifact diff
```

I3 is more expensive than I2.

But I3 directly targets the decisive proposition.

If outputs are identical:

```text
artifact-difference path closes
→ deeper consequence analysis pruned
```

Therefore a non-cheapest dynamic check can be the best first **substantive** investigation.

This destroyed any universal:

```text
static → semantic → dynamic
```

rule.

---

# 45. Contrast validity

Pressure Test 1 exposed a subtle danger.

The generation process involves more than one tool/component.

Different old/new environments could vary in:

```text
grpcio-tools
protobuf
mypy-protobuf
formatter versions
resolver outcome
```

If the outputs differ, what caused the difference?

That is an experimental-design problem.

Accepted concept:

> **Contrast validity** — whether the old-versus-new comparison actually represents the distinction asked by the proposition, with other materially relevant differences controlled or explicitly accounted for.

A target-specific experiment can still be invalid.

```text
target-specific experiment
!= valid experiment
```

---

# 46. Proposal-level effect versus causal mechanism attribution

These are different questions.

## Proposal-level effect

```text
What happens to the target under the real old versus proposed dependency worlds?
```

Transitive resolver changes may legitimately be part of the proposal world.

## Mechanism attribution

```text
Did this exact changed dependency property cause the observed difference?
```

This requires stronger causal controls.

Therefore:

```text
decision-relevant discrimination
!= causal attribution
```

This is important because UpgradePilot may not always need perfect causal isolation before discovering that a proposal changes the target materially.

---

# 47. Post-execution evidence validation

Suppose an experiment runs successfully.

That does **not** mean its output is valid evidence.

The result could be:

```text
confounded
unstable
wrong environment
wrong proposal identity
insufficiently reproducible
not actually tied to the proposition
```

Therefore:

```text
investigation execution success
!= evidence admission
```

The result itself must pass scope/context/meaning validation.

---

# 48. Investigation result can reveal a wrong candidate

Imagine a differential test shows a difference.

Later analysis reveals the difference is caused by another transitive mechanism, not the mechanism originally represented.

Then the observation should not be forced into the current proposition.

Accepted feedback:

```text
INVESTIGATION RESULT
↓
Does it bear on current proposition?
├── yes → B proposition evaluation
└── no; reveals different/incomplete mechanism
    → refine/formulate impact candidate
    → derive new propositions
```

This makes the whole system iterative rather than a rigid one-way pipeline.

---

# 49. Pressure Test 2 — Buildtest / historical OpenSSL

This tested the opposite problem:

> What if the ideal evidence is highly discriminating but may no longer exist?

Real case:

```text
shahzebsiddiqui/buildtest-1#74
urllib3 ==1.26.* → ==2.0.*
```

urllib3 2.0 removes support for OpenSSL earlier than 1.1.1.

The target CI path:

```text
load NERSC module python/3.9-anaconda-2021.11
↓
conda create child env with python=3.9
↓
activate child env
↓
setup/install target dependencies
↓
run regression
```

The exact historical child environment's OpenSSL version was not established.

The decisive proposition:

> Did the exact relevant historical child environment use OpenSSL <1.1.1?

Ideal evidence:

```text
ssl.OPENSSL_VERSION
conda list --explicit
conda env export
exact historical package manifest
solver transaction record
```

But the child environment was deleted and no exact retained artifact was established.

---

# 50. Proxy evidence

Stock Anaconda 2021.11 metadata can be authoritative for the stock distribution.

It is not automatically authoritative for the exact NERSC child environment created later.

Accepted concept:

> **Proxy evidence** — evidence about a related but non-identical context that can constrain/narrow the target proposition without inheriting exact-context authority.

Examples:

```text
stock distribution metadata
current environment with same module name
generic vendor documentation
similar historical environment
```

Proxy evidence can be useful.

It just cannot be silently promoted.

---

# 51. Scope substitution

A dangerous failure mode:

Original hard proposition:

```text
Did exact historical Buildtest child environment use OpenSSL <1.1.1?
```

Easier neighboring proposition:

```text
Did stock Anaconda 2021.11 ship OpenSSL >=1.1.1?
```

The second may be answerable.

But it does not resolve the first.

**Scope substitution** means answering the easier neighboring question and pretending it solved the original.

Rejected:

```text
easier proposition answered
→ original proposition resolved
```

A narrower proposition may be useful, but must remain separately scoped.

---

# 52. Reconstruction fidelity

Suppose exact historical evidence is missing.

Can we recreate the environment?

Maybe.

But:

```text
same command today
!= same historical solve
```

Why?

Historical state can depend on:

```text
solver version
channel state/repodata
available package builds
module customization
system/native libraries
package indexes
transitive dependencies
```

Accepted concept:

> **Reconstruction fidelity** — how adequately the reconstructed environment represents the exact historical context whose property we are trying to infer.

Important:

```text
reproducible reconstruction
!= historically faithful reconstruction
```

You can perfectly reproduce today's approximation and still fail to reconstruct 2023.

---

# 53. Investigation validity / context fidelity

Contrast validity and reconstruction fidelity are instances of a broader rule:

> **An investigation result cannot receive stronger evidential meaning than the identity, context, temporal, contrast, and reconstruction fidelity of the observation permits.**

This is the durable general principle.

Practical questions:

```text
Is this the correct target revision?
Is this the same relevant environment?
Is this observation from the right time?
Does the experiment isolate/account for relevant differences?
Does the reconstruction faithfully represent the historical context?
```

---

# 54. More investigation effort can make evidence worse, not better

A common intuition is:

```text
more work
→ more certainty
```

Not always.

An elaborate historical reconstruction may accumulate assumptions:

```text
assumed channel state
assumed solver behavior
assumed package build
assumed system library
```

Then the result can look sophisticated while becoming less tied to the original proposition.

Rule:

```text
more elaborate reconstruction
!= more justified evidence
```

Investigation effort must earn evidential value.

---

# 55. No further justified investigation

Conversation C can legitimately end with:

```text
no additional supported investigation is currently justified
```

Reasons may include:

```text
non-discriminating checks
unrecoverable evidence
unsafe execution
unsupported capability
insufficient context fidelity
excessive cost for negligible decision value
reconstruction cannot answer original proposition
```

This is not epistemic surrender.

It is disciplined stopping.

The proposition remains:

```text
unresolved
```

unless B-level evidence changes it.

---

# 56. Conversation C stopping versus Conversation D sufficiency

This boundary must be automatic in your mind.

## Conversation C asks

```text
Should we acquire more evidence?
If yes, what investigation is worth doing next?
```

C can stop because there is no worthwhile supported next investigation.

## Conversation D asks

```text
Given everything we know and still do not know,
is the overall evidence state sufficient to stop the whole assessment,
and what maintainer-facing output/action is justified?
```

Therefore:

```text
C investigation stop
!= D evidence sufficiency
```

And especially:

```text
no more useful automated check
!= safe to merge
```

---

# 57. The complete accepted A→C flow

Use this as your main mental model:

```text
PUBLIC DEPENDENCY-UPDATE PR
↓
EXACT PROPOSAL / TARGET / VERSION / REVISION IDENTITY
↓
AUTHORITATIVE UPSTREAM CHANGE EVIDENCE
↓
ZERO OR MORE MECHANISM-SPECIFIC IMPACT CANDIDATES
    upstream mechanism
    + target-relevant exposure/path
    + activation condition(s)
    + possible target consequence
↓
DERIVE CANDIDATE-SPECIFIC APPLICABILITY PROPOSITIONS
↓
ADMIT/VALIDATE EVIDENCE
↓
EVALUATE PROPOSITIONS
    established
    refuted
    unresolved
    conflicted
↓
COMPOSE ACCORDING TO CANDIDATE LOGIC
↓
CANDIDATE APPLICABILITY STATE
↓
IF MATERIAL UNCERTAINTY REMAINS:
    identify uncertainty location/reason
    ↓
    identify discriminating target
    ↓
    generate candidate investigations
    ↓
    hard admissibility + context-validity gate
    ↓
    remove clearly dominated options
    ↓
    qualitative comparison
        discrimination
        authority/scope/coverage
        pruning leverage
        cost/risk/latency/invasiveness
        reproducibility
        complementarity
    ↓
    choose next check / small conditional strategy
    OR stop investigation
    ↓
    observe
    ↓
    validate result as evidence
    ↓
    current proposition?
        yes → proposition evaluation
        no/new mechanism → candidate refinement
    ↓
    repeat only while justified
↓
CONVERSATION-C INVESTIGATION STOP
↓
CONVERSATION-D OVERALL SUFFICIENCY / MAINTAINER SYNTHESIS
```

If you can explain every arrow and why the boundaries exist, you understand the architecture conceptually.

---

# 58. What the LLM may and may not own across A–C

## Good LLM responsibilities

Potentially:

```text
interpret semantic release-note meaning
formulate candidate hypotheses/propositions with grounding
compare difficult software semantics
propose candidate investigations
summarize exact evidence with attribution
explain uncertainty
```

## Responsibilities the LLM must not self-assign

```text
source authority
proposal identity
exact version ordering
complete repository/environment coverage
absence from incomplete search
closed-world completeness
final proposition state from raw confidence alone
hard safety authorization
credential/execution policy
final maintainer merge/defer authority
```

## Strong pattern

```text
semantic model proposes/interprets
↓
deterministic/evidence/safety machinery validates what can be validated
↓
bounded evaluator assigns justified proposition state
↓
mechanical composition where logic is explicit
```

This is how you use AI strongly without turning it into an oracle.

---

# 59. Rejected mental models — learn why they fail

## 59.1 “Major version means high risk”

Fails because version magnitude does not establish target-relevant mechanism, exposure, or activation.

## 59.2 “Target imports dependency, therefore change applies”

Fails because dependency use does not establish participation in the affected mechanism or reliance on the changed property.

## 59.3 “We searched and found nothing, therefore not applicable”

Fails under open-world reasoning unless the search universe is proven complete enough.

## 59.4 “LLM confidence 0.95 means the claim is strong”

Fails because confidence does not create authority, completeness, or semantic correctness.

## 59.5 “Run all tests and see”

Fails because tests may not activate the mechanism, may be narrow, may be confounded, and may not establish why a result occurred.

## 59.6 “Static first, dynamic later”

Fails because a high-leverage direct experiment can be the best first substantive check.

## 59.7 “Dynamic is stronger than static”

Fails because static evidence can be complete/authoritative for declarative bounded questions while dynamic tests can be narrow or invalid.

## 59.8 “Cheapest first”

Fails when a slightly more expensive check directly resolves a shared high-leverage gate.

## 59.9 “Strongest possible check first”

Fails when a cheap check can prune the expensive one or when the strongest check is unsafe/unrecoverable.

## 59.10 “Current environment with same name proves historical environment”

Fails because identity/time/context may have changed.

## 59.11 “Rebuild historical commands today”

Fails because historical solver/package/index/system state may differ.

## 59.12 “No more useful investigation means safe”

Fails because C stopping only means investigation has reached its justified boundary; D still owns overall sufficiency/output.

---

# 60. Technical terms worth knowing outside UpgradePilot

These are general engineering/decision-analysis terms the project now uses meaningfully.

## Counterfactual

A comparison of what would happen under alternative worlds/conditions.

Dependency updates are naturally counterfactual:

```text
old dependency world
vs
proposed dependency world
```

## Necessary condition

Must be true if the proposition is true.

## Sufficient condition

Enough to establish a proposition.

## Open-world assumption

Non-observation does not imply false/absent.

## Closed-world assumption

Within a complete bounded universe, non-membership/absence can imply false/absent.

## Universe of discourse

The exact set of objects your claim is about.

## Provenance

Where evidence came from and how it is connected to the assessed object.

## Grounding

Binding a derived claim to exact source evidence.

## Determinism

Same validated input/rules produce same output.

## Value of Information (VoI)

Decision-analysis idea measuring the usefulness of gaining information before a decision. UpgradePilot uses the intuition qualitatively, not a numeric optimizer.

## Pareto dominance

Option A is no worse on all relevant dimensions and better on at least one.

## Pareto frontier

Set of options that are not clearly dominated by another.

## Short-circuit evaluation

Programming analogy: in `A AND B`, if A is false, B may not need evaluation. UpgradePilot uses the analogy for investigation pruning, while recognizing that it must decide which unknown fact is worth acquiring first.

## Adaptive planning

Future actions depend on observations received during execution.

## State-space explosion

The number of possible states/branches grows combinatorially and becomes impractical to plan exhaustively.

## Bounded lookahead / receding horizon

Plan enough ahead to select a good next action, then re-plan after observing the result.

## Internal/contrast validity

Experimental-design idea: whether the observed effect can legitimately be attributed to the intended contrast rather than uncontrolled differences.

## Confounder

Another changing factor that can explain an observed difference.

## Corroboration

Independent/supporting evidence that improves confidence/authority/coverage beyond simple repetition.

---

# 61. What is still intentionally deferred

Do not mistake deferred implementation detail for missing conceptual understanding.

The project has **not** accepted:

```text
final runtime applicability enum/schema
universal Boolean expression language
complete exposure taxonomy
universal investigation taxonomy
numeric VoI score
universal investigation planner
complete decision tree representation
autonomous arbitrary executor
hard/soft dimension scoring schema
context-fidelity scoring formula
universal evidence-completeness engine
universal semantic proposition evaluator
graph database/runtime
final maintainer action vocabulary
final repository-policy schema
```

Why defer these?

Because the project follows:

```text
real evidence
→ just-enough semantics
→ implementation/evaluation feedback
→ refinement
```

Building framework machinery before it is earned would recreate the overdesign problem the reconciliation is trying to avoid.

---

# 62. What you should be able to explain from memory

Without reading, try to answer these aloud.

1. Why is an upstream release-note change not automatically a target impact?
2. What four components make an impact candidate?
3. Why does target relevance not require target ownership?
4. What is the difference between exposure and activation?
5. Why can one dependency transition yield multiple impact candidates?
6. What is the difference between world truth and system knowledge state?
7. Define the four applicability knowledge states.
8. Why does one established path suffice for positive applicability?
9. Why must every viable path be eliminated for non-applicability?
10. Why is missing evidence not negative evidence?
11. What is the open-world assumption?
12. When can closed-world reasoning be justified?
13. What is a universe of discourse?
14. Why is completeness itself an evidence claim?
15. What can deterministic reasoning own well?
16. What can semantic reasoning/LLMs own usefully?
17. Why can LLM confidence not establish source authority or completeness?
18. Explain `uses dependency != participates in affected mechanism != relies on specific changed property`.
19. Why is `unresolved` alone insufficient input for Conversation C?
20. What is a discriminating target?
21. Relevant evidence versus discriminating evidence?
22. Resolution versus reduction?
23. What is directional discrimination?
24. Why does admissibility precede preference?
25. What does non-compensatory hard constraint mean?
26. What is dominance/Pareto reasoning useful for?
27. What is pruning/shared-gate leverage?
28. Why can investigation order differ from logical proposition order?
29. What is a conditional/adaptive investigation strategy?
30. What is bounded lookahead?
31. Complementarity versus redundancy versus corroboration?
32. Static versus dynamic evidence: why is neither universally stronger?
33. Observational versus interventional evidence?
34. What is differential testing?
35. What is contrast validity?
36. Proposal-level effect versus causal mechanism attribution?
37. Why can a successful experiment still produce invalid evidence?
38. What is proxy evidence?
39. What is scope substitution?
40. What is reconstruction fidelity?
41. Why does more reconstruction effort not necessarily mean better evidence?
42. When is `no further justified investigation` correct?
43. Why does that not mean `not applicable` or `safe`?
44. What is the exact C/D boundary?
45. How can an investigation result force candidate refinement rather than merely proposition evaluation?

If you can answer these accurately and use examples, you have strong conceptual command of A–C.

---

# 63. Transfer exercises — use the model on unfamiliar cases

Do not look for one “correct” answer. Practice explicit reasoning.

## Exercise 1 — native extension ABI update

A Python dependency updates a native extension and now requires a newer glibc.

Target source never imports any glibc API directly.

Questions:

1. formulate one impact candidate;
2. identify exposure/path;
3. identify activation condition;
4. identify possible consequence;
5. derive 3–5 applicability propositions;
6. identify one discriminating target;
7. compare static platform metadata versus runtime/container probe;
8. explain when a current container is invalid proxy evidence for production.

## Exercise 2 — database driver protocol behavior

A database driver changes default TLS verification semantics.

Target calls the driver through an ORM.

Questions:

1. direct dependency edge versus actual changed interaction?
2. what intermediary semantics matter?
3. which proposition could be a shared gate?
4. what evidence could establish target configuration activation?
5. when might a differential integration test be preferable to reading more source?
6. what confounders could invalidate the test?

## Exercise 3 — frontend build tool

A Node build dependency changes generated asset hashing.

The dependency is not in production runtime.

Questions:

1. explain artifact-mediated exposure;
2. formulate old/new counterfactual;
3. choose between changelog inspection and deterministic rebuild+diff;
4. what would make rebuild+diff invalid?
5. if only filenames differ but contents/runtime behavior do not, which proposition activates next?

## Exercise 4 — plugin ecosystem

A framework update changes callback ordering.

The target loads third-party plugins dynamically.

Questions:

1. what is the universe of discourse for plugin presence?
2. what evidence would justify absence?
3. why is target-repo grep insufficient?
4. what does `participates in affected mechanism` mean here?
5. what semantic proposition might remain after structural facts are established?

## Exercise 5 — historical cloud image

A CI job in 2022 used a cloud-hosted runner image with mutable label `ubuntu-latest`.

A dependency update requires a newer system library.

Questions:

1. what exact historical proposition matters?
2. what would ideal evidence look like?
3. what evidence today is only proxy evidence?
4. how would you judge reconstruction fidelity?
5. when would you stop unresolved?

---

# 64. Diagnosis exercises — spot the reasoning bug

## Case A

> “We searched the repository and found no `wrapper=True`, so the Pluggy wrapper change is not applicable.”

Bug:

```text
incomplete search universe promoted to negative evidence
```

Possible external plugins/dynamic entry points remain.

## Case B

> “The LLM is 98% confident urllib3 2 breaks this project.”

Bug:

```text
model confidence promoted to applicability/evidence authority
```

Need exact mechanism, exposure, activation, propositions, evidence.

## Case C

> “The new dependency version passed CI, so the update is safe.”

Bugs can include:

```text
CI may not exercise the changed mechanism
passing observation != global compatibility
compatibility != final policy/merge action
```

## Case D

> “Current Anaconda 2021.11 environment uses OpenSSL 1.1.1, therefore the 2023 NERSC child environment did too.”

Bug:

```text
proxy/context substitution + temporal identity overclaim
```

## Case E

> “A differential test produced different files, so grpcio-tools itself changed generation behavior.”

Bug:

```text
decision-relevant difference promoted to causal attribution without contrast control
```

## Case F

> “There is no further useful automated check, therefore recommend merge.”

Bug:

```text
C investigation stopping promoted to D overall sufficiency/action
```

---

# 65. A practical checklist for your own reasoning — not a product runtime checklist

When *you* analyze a dependency-update case during study, ask:

```text
1. What exact proposal/revision/version am I talking about?
2. What authoritative upstream mechanism changed?
3. What is the target-relevant exposure/path?
4. What conditions activate that pathway?
5. What target consequence could occur?
6. Is this one candidate or multiple mechanism-specific candidates?
7. What explicit applicability propositions are required?
8. Which are necessary? Which are alternatives?
9. What evidence supports/refutes each proposition?
10. Is absence being inferred? If yes, is the evidence universe complete enough?
11. Which propositions remain unresolved/conflicted?
12. Why exactly are they unresolved?
13. What is the discriminating target?
14. What candidate investigations can observe/test it?
15. Which investigations fail hard admissibility?
16. Are any remaining options clearly dominated?
17. Which option has the most useful discrimination/pruning leverage for justified cost/risk?
18. Do complementary checks matter?
19. What will different outcomes cause us to do next?
20. Is the investigation/experiment/reconstruction context valid enough for the claim?
21. Does the observation update the current proposition or reveal a different candidate?
22. Is another investigation still materially worth doing?
23. If not, preserve unresolved and stop C honestly.
24. Do not jump from C stopping to final maintainer action.
```

This checklist is for learning/reasoning. It is **not** an accepted universal machine pipeline/schema.

---

# 66. Compact case map

## S001 — Soup Sieve / Pydantic

Primary lesson:

```text
authoritative support-drop claim
+
exact target declared Python range
→ deterministic relevance
```

Teaches bounded question answering and not overclaiming safety.

## Kedro / Pluggy

Primary lesson:

```text
framework use
!= affected mechanism participation
!= reliance on changed semantic
```

Teaches dynamic plugin/inverted control and semantic-heavy unresolved state.

## pip-audit / CacheControl / urllib3

Primary lesson:

```text
target-owned edge
!= full transitive impact path
```

Teaches multi-hop exposure and intermediary incompatibility.

## C01 grpcio-tools code generation

Primary lesson:

```text
dev-only dependency
→ generation
→ committed artifact
→ later runtime
```

Teaches artifact-mediated coupling, differential regeneration, contrast validity, and non-cheapest first investigation.

## C203 Buildtest / OpenSSL

Primary lesson:

```text
exact historical environment fact missing
→ proxy evidence narrows
→ reconstruction must earn fidelity
→ possibly stop unresolved
```

Teaches recoverability, reconstruction fidelity, proxy evidence, scope substitution, and no-further-investigation.

---

# 67. What “good UpgradePilot reasoning” now sounds like

Bad:

> urllib3 2 is risky because it is a major update.

Better:

> urllib3 2 removes support for OpenSSL earlier than 1.1.1. The target has a proven external Perlmutter/Conda execution pathway, so an environment-mediated impact candidate exists. Applicability depends on whether the exact historical child environment used an affected OpenSSL version. That fact is currently unresolved. The next useful investigation should target the exact historical SSL/package state; generic source search is weak. If exact historical evidence is unrecoverable, proxy metadata may narrow but cannot resolve the proposition, and reconstruction is justified only if it can attain adequate historical fidelity.

That is the level of precision the project is aiming for.

---

# 68. What “good bounded LLM usage” sounds like

Bad:

> Ask the model: “Is this dependency safe to update?”

Better:

```text
1. bind exact proposal/version/source identity deterministically
2. give bounded authoritative source text to semantic model
3. ask model for a narrow attributed semantic proposition/candidate
4. reconstruct/validate exact evidence deterministically where practical
5. derive exact target-specific propositions
6. let deterministic procedures own mechanical questions
7. let semantic reasoning handle only irreducible meaning
8. preserve unresolved/conflict when evidence is insufficient
9. model may propose investigations, but safety/authority/capability validate them
10. final maintainer action remains outside model self-authority
```

This is AI-assisted engineering, not AI-as-oracle engineering.

---

# 69. One-page memory sheet

If you remember only one block, remember this:

```text
EXACT IDENTITY FIRST.

UPSTREAM CHANGE
is not TARGET IMPACT.

IMPACT CANDIDATE =
mechanism
+ exposure/path
+ activation conditions
+ possible target consequence.

APPLICABILITY =
explicit candidate-specific propositions
+ scoped evidence
+ honest knowledge states.

Positive applicability:
one complete viable path can suffice.

Non-applicability:
every viable path must be closed.

Missing evidence is unresolved.
Absence requires a justified complete boundary.

LLM:
use for hard meaning,
not for authority/completeness/final action.

When unresolved:
find WHERE uncertainty lives.
Find the DISCRIMINATING TARGET.

Generate checks against that target,
not against the broad topic.

ADMISSIBILITY FIRST:
identity, authority, capability, safety,
context validity.

Then compare qualitatively:
discrimination,
pruning leverage,
cost/risk,
coverage,
reproducibility,
complementarity.

No universal cheap/static/dynamic ordering.
Use adaptive sequencing + bounded lookahead.

A successful experiment can still be invalid evidence.
Proxy evidence can narrow but not substitute exact context.
Historical reconstruction must earn fidelity.

Investigation result may update a proposition
or reveal a different candidate.

Stop investigating when no justified useful check remains,
but PRESERVE unresolved.

C investigation stopping
is not D overall sufficiency
and is not a merge/safety decision.
```

---

# 70. Suggested study/relearning sequence

When you revisit this note later, do not reread everything every time.

## Fast 15-minute recall

Read:

1. Sections 2, 5, 8, 14, 24, 32, 38, 53, 56, 57, 69.
2. Answer 10 random questions from Section 62 aloud.
3. Explain one case from Section 66 without looking.

## 45–60 minute review

1. Reconstruct A from Sections 8–12.
2. Reconstruct B from Sections 13–23.
3. Reconstruct C from Sections 24–56.
4. Draw the full A→C flow yourself.
5. Do one transfer exercise.

## Deep mastery session

1. Pick a real new dependency-update PR.
2. Freeze exact identity.
3. Formulate one mechanism-specific candidate.
4. Derive propositions.
5. Identify evidence boundaries.
6. Locate uncertainty.
7. Generate 2–4 candidate investigations.
8. Compare them qualitatively.
9. Predict outcomes and pruning.
10. Execute/inspect one bounded check if authorized.
11. Explain why the result is or is not admissible evidence.
12. Record what you got wrong before checking the model.

That is much stronger learning than rereading notes passively.

---

# 71. Snapshot boundaries and references

This note reflects the repository understanding at Conversation-C closure.

It intentionally does not claim:

- Conversation D semantics are complete;
- the final maintainer-facing action vocabulary is known;
- the A–C method has been implemented as a general runtime planner/evaluator;
- the method has been proven across every dependency ecosystem;
- the learner has independently demonstrated mastery.

Primary repository references on `main`:

- `working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`
- `MEMORY.md`
- `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- `docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`
- `learning/bounded-llm-semantic-extraction.md`

Challenge-screening evidence used by the reconciliation is preserved on branch `agent/product-simulation-case-screening-01`, not on `main`:

- `product-simulation/CHALLENGE_CASE_SCREENING_01.md`
- `product-simulation/CHALLENGE_CASE_SCREENING_02.md`
- related handoff evidence on that same branch.

Those screening artifacts are non-controlling challenge evidence; the accepted A–C conclusions are consolidated in the main reconciliation record.

When later implementation changes the decision model materially, preserve this as the 2026-08-10 educational snapshot rather than silently rewriting it into a different historical state.
