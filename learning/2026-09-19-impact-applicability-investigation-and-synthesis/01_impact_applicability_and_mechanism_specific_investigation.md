# Impact, Applicability, and Mechanism-Specific Investigation

**Learning-artifact date:** 2026-09-19  
**Source/test evidence horizon:** main@e91b79908e21ad1529b5c8c3fd8dcf3841984deb  
**Roadmap responsibility:** Group 9 — impact, applicability, investigation, and maintainer-action synthesis  
**Package position:** Note 1 of 2  
**Current package boundary:** this note is stable/current; Note 2 on action-relative maintainer-action synthesis remains intentionally gated by the active end-to-end synthesis audit  
**Primary responsibility:** understand how UpgradePilot turns grounded mechanism evidence into a target-bound impact candidate, evaluates candidate-specific applicability through explicit propositions/paths, selects a discriminating mechanism-specific investigation only when justified, incorporates the result, and preserves the typed investigation state for later synthesis  
**Target depth:** **must master / own** candidate-versus-applicability separation, proposition/path logic, evidence/path/candidate-discovery coverage distinctions, open-world negative reasoning, mechanism-specific investigation selection, reevaluation, exact identity/provenance guards, and the boundary from technical investigation to later maintainer-action synthesis

The shortest mental model is:

~~~text
grounded mechanism evidence
+ exact dependency transition
+ exact target PR/revision
        ↓
mechanism-specific impact candidate
        ↓
candidate-specific propositions / paths
        ↓
established | refuted | unresolved | conflicted
        ↓
candidate applicability
        ↓
if material non-final state remains:
   select one justified discriminating investigation
   OR preserve uncertainty / stop
        ↓
new exact evidence
        ↓
reevaluate same proposition/candidate
        ↓
typed PublicPullRequestInvestigation
        ↓
LATER:
overall evidence sufficiency / maintainer-action synthesis
~~~

The most important boundary is:

~~~text
technical impact candidate
!= candidate applies to this target

candidate applies to this target
!= whole update is unsafe

candidate not applicable
!= whole update is safe

unresolved
!= automatically investigate

mechanism-specific investigation result
!= maintainer action
~~~

---

## 1. Where this responsibility sits in UpgradePilot

Earlier parts of the product establish exact identity and evidence:

~~~text
public dependency-update PR
→ exact repository / PR / base / head identity
→ exact dependency transition
→ dependency source contexts
→ CI evidence
→ exact package releases / upstream authority
→ target evidence
~~~

Group 9 begins when enough evidence exists to ask a more semantic question:

> **What specific technical impact mechanism is suggested by the exact update, does that mechanism apply to this exact target, and is another bounded investigation actually useful?**

This is not a generic risk score.

It is not:

~~~text
collect facts
→ assign danger number
→ choose action
~~~

The accepted product model is proposition-based and mechanism-specific.

---

## 2. Canonical decision-model owner

Stable semantics are owned by:

~~~text
docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
~~~

Its accepted reasoning spine is conceptually:

~~~text
exact transition identity
→ admitted mechanism evidence
→ zero or more technical impact candidates
→ candidate-specific applicability propositions
→ proposition evaluation
→ candidate applicability knowledge state
→ discriminating investigation when justified
→ observation/result
→ identity/scope validation
→ reevaluation
→ stop when no useful justified investigation remains
→ later overall sufficiency / maintainer-facing synthesis
~~~

The specification deliberately does **not** define:

~~~text
universal impact taxonomy
universal Boolean/rule engine
generic runtime agent planner
final maintainer policy
~~~

Current source implements only selected bounded mechanisms.

---

## 3. A technical impact candidate is not a conclusion

An impact candidate means roughly:

> **Grounded evidence supports a concrete mechanism/consequence hypothesis worth evaluating against the exact target.**

A candidate must preserve the evidential status of its parts.

It should not silently convert:

~~~text
mechanism evidence
→ target exposure established
→ consequence established
~~~

For the implemented Python-support mechanism, candidate creation produces statuses such as:

~~~text
mechanism_status   = established
exposure_status    = to_evaluate
activation_status  = to_evaluate
consequence_status = possible
~~~

This says:

~~~text
the upstream support-drop mechanism is grounded
BUT
whether the exact target is exposed/activated remains open
AND
the consequence remains possible rather than proven
~~~

Candidate formation is therefore a **controlled handoff from discovery into applicability reasoning**.

---

## 4. Candidates are mechanism-specific

Current implemented impact mechanisms include at least:

~~~text
Python-support drop
artifact serviceability / wheel-path loss
~~~

They do not share one universal candidate schema because their propositions differ.

### Python-support candidate

Core question:

> Did the dependency transition cross a grounded upstream Python-support drop, and does the exact target's declared Python range intersect that dropped line?

### Artifact-serviceability candidate

Core question:

> Did published wheel capabilities disappear, and does the exact target support a wheel path that existed before but is unavailable after the update?

The generic layer supplies applicability composition.

The mechanism layer decides:

~~~text
which propositions matter
what evidence owns them
what paths exist
what investigation could discriminate them
~~~

This is a crucial architecture choice:

> **Generalize the reasoning semantics, not every mechanism's domain facts.**

---

## 5. Generic applicability owner

Primary source:

~~~text
src/upgradepilot/impact/applicability.py
~~~

It intentionally models a small set of generic concepts.

### Proposition state

~~~text
established
refuted
unresolved
conflicted
~~~

### Evidence coverage

~~~text
sufficient
insufficient
unresolved
~~~

### Candidate applicability state

~~~text
established_applicable
established_not_applicable
unresolved
conflicted
~~~

### Path-model coverage

~~~text
sufficient
insufficient
unresolved
~~~

The module explicitly does not model:

~~~text
candidate-discovery completeness
final maintainer action
numerical scoring
generic rule engine
~~~

That boundary prevents one small deterministic composer from becoming an accidental universal decision engine.

---

## 6. Proposition state and evidence coverage are different

A proposition has both:

~~~text
state
evidence_coverage
~~~

Why separate them?

Because:

~~~text
unresolved because evidence is missing
~~~

is different from:

~~~text
unresolved despite having the exact evidence,
because the accepted comparison method cannot decide
~~~

Example from Python-support impact:

### Target file unavailable

~~~text
target declaration proposition:
state = unresolved
evidence_coverage = insufficient
~~~

The required target evidence was not established.

### Target declaration acquired but comparison unsupported

~~~text
target declaration proposition:
state = established
evidence_coverage = sufficient

activation proposition:
state = unresolved
evidence_coverage = sufficient
~~~

Here the evidence exists, but the deterministic comparison method cannot decide the activation proposition.

This distinction is highly important for investigation selection.

---

## 7. Applicability is path-based, not a flat checklist

A candidate can have one or more possible applicability paths.

A path is a conjunction:

~~~text
A AND B AND C
~~~

Current generic composer:

~~~text
evaluate_applicability_path(...)
~~~

applies bounded deterministic logic.

### One refuted necessary proposition eliminates the path

~~~text
established
+ refuted
+ unresolved
→ path = refuted
~~~

Because a necessary condition failed.

### All necessary propositions established

~~~text
established
+ established
+ established
→ path = established
~~~

### No refutation, but unresolved remains

~~~text
established
+ unresolved
→ path = unresolved
~~~

### No refutation, genuine conflict remains

~~~text
established
+ conflicted
→ path = conflicted
~~~

This is not a general SAT/logic engine.

It is the minimum deterministic logic needed for current explicit candidate paths.

---

## 8. Multiple paths represent alternatives

Suppose a candidate has alternative applicability routes:

~~~text
Path 1 = A AND B
Path 2 = A AND C
~~~

One refuted path does not eliminate the candidate while another path remains viable.

The candidate composer therefore evaluates all represented paths.

Current:

~~~text
evaluate_candidate_applicability(...)
~~~

uses rules such as:

### Any complete established path

~~~text
at least one path = established
→ candidate = established_applicable
~~~

Other unresolved/conflicted alternatives are preserved rather than erased.

### Every represented path refuted

This is enough for:

~~~text
established_not_applicable
~~~

only when:

~~~text
path_model_coverage = sufficient
~~~

Otherwise:

~~~text
all represented paths refuted
+ path-model coverage unresolved/insufficient
→ candidate remains unresolved
~~~

This prevents a false negative conclusion from an incomplete candidate model.

---

## 9. Three coverage questions must not collapse

The Product Decision Model distinguishes three different completeness questions.

### Evidence coverage

~~~text
Did the admitted evidence sufficiently cover proposition P?
~~~

### Path-model coverage

~~~text
Did this candidate represent the material alternative applicability routes?
~~~

### Candidate-discovery coverage

~~~text
Did impact discovery identify enough materially different impact mechanisms
before making a transition-level claim?
~~~

Therefore:

~~~text
evidence completeness
!= path-model completeness
!= candidate-discovery completeness
~~~

And:

~~~text
all discovered candidates not applicable
!= no material impact from the update
~~~

unless candidate-discovery coverage is independently justified.

Current generic applicability.py handles proposition/path composition.

It does **not** claim candidate-discovery completeness.

---

## 10. Open-world reasoning is the default

The specification's safe default is:

~~~text
not observed
→ unresolved / not observed within admitted scope
~~~

not:

~~~text
not observed
→ absent
~~~

Negative claims need proposition-local justification such as:

~~~text
explicit authoritative exclusion
complete bounded inventory
deterministic derivation from authoritative facts
~~~

This is why UpgradePilot frequently preserves:

~~~text
unresolved
not_established
evidence_insufficient
~~~

instead of converting missing evidence into favorable or unfavorable conclusions.

---

## 11. Python-support drop is the clearest complete implementation

Primary source:

~~~text
src/upgradepilot/impact/python_support.py
~~~

Its flow starts only after upstream reasoning has already produced:

~~~text
GroundedPythonSupportDropClaim
~~~

That claim is not model speculation.

It is the downstream result of the upstream authority/grounding chain.

The impact layer consumes that trusted result rather than redoing upstream semantic extraction.

---

## 12. Candidate creation binds exact identities

Current builder:

~~~text
build_python_support_drop_impact_candidate(...)
~~~

inputs:

~~~text
PullRequestIdentity
DependencyVersionChange
GroundedPythonSupportDropClaim
~~~

Before constructing the candidate, it verifies that the grounded claim's release interval matches:

~~~text
normalized package
old version
proposed version
~~~

of the exact dependency transition.

A mismatch raises an error.

This prevents:

~~~text
valid support-drop claim from transition A
+
dependency transition B
→ synthetic impact candidate
~~~

The candidate then binds:

~~~text
target_repository = pull_request.repository
target_revision   = pull_request.head_sha
~~~

So later target evidence must belong to the exact analyzed head revision.

---

## 13. Candidate creation establishes mechanism, not target applicability

The Python-support candidate stores propositions conceptually like:

~~~text
Exposure:
the exact target revision declares a Python installation range
relevant to the support-drop mechanism

Activation:
the exact target declaration admits at least one stable
Python X.Y.Z version from the dropped X.Y line

Possible consequence:
the proposed dependency may no longer support part
of the target's declared Python installation range
~~~

At creation time:

~~~text
mechanism = established
exposure = to_evaluate
activation = to_evaluate
consequence = possible
~~~

This is the correct evidence strength.

The grounded upstream claim alone cannot self-authorize target impact.

---

## 14. Pre-acquisition applicability is explicitly unresolved

Current evaluator:

~~~text
evaluate_python_support_drop_impact(candidate)
~~~

with no target relevance yet constructs an applicability path with:

~~~text
P1 upstream support drop crossed
   → established / sufficient

P2 exact target Python declaration established
   → unresolved / insufficient

P3 target declared range intersects dropped line
   → unresolved / insufficient
~~~

Result:

~~~text
candidate applicability = unresolved
~~~

This is valuable because the system knows **where** the uncertainty lives.

It is not a generic:

~~~text
need more data
~~~

It is a proposition-specific evidence gap.

---

## 15. Investigation begins from a material discriminating gap

Current selector:

~~~text
select_python_support_drop_investigation(...)
~~~

does not ask:

> What could we investigate in general?

It asks a much narrower question:

> Is this unresolved candidate specifically blocked because the exact target Python declaration has not yet been acquired?

Positive selection requires conditions including:

~~~text
assessment target relevance is still absent
candidate applicability is unresolved
exact target declaration proposition is unresolved
its evidence coverage is insufficient
~~~

Then it selects exactly one current investigation kind:

~~~text
acquire_exact_target_python_declaration
~~~

with exact:

~~~text
repository
revision
path = pyproject.toml
proposition_key
~~~

This is a mechanism-specific discriminating investigation.

---

## 16. Investigation selection is not unresolved → investigate

This is one of the most important rules.

The selector does **not** say:

~~~text
candidate unresolved
→ always investigate
~~~

It requires an identified proposition gap and an admitted evidence acquisition that can discriminate it.

Consider three different unresolved states:

### Missing target file evidence

~~~text
target declaration not yet acquired
→ selected read can discriminate
→ investigation selected
~~~

### Target file read attempted but unavailable

~~~text
TargetPythonDeclarationProblem exists
→ target_relevance exists
→ same acquisition is NOT selected again
~~~

The system preserves unresolved state rather than looping.

### Exact target declaration exists but comparison method unsupported

~~~text
evidence coverage = sufficient
activation proposition unresolved
→ same target-file acquisition does not help
→ do not select it again
~~~

This is evidence-directed investigation, not activity for its own sake.

---

## 17. Investigation selection remains mechanism-specific on purpose

Current Python-support selector knows:

~~~text
pyproject.toml
[project].requires-python
target repository/revision
support-drop activation proposition
~~~

This is not abstracted into a universal investigation planner.

The source docstring explicitly preserves that boundary:

> The first discriminating-investigation selector remains mechanism-specific until a second real mechanism demonstrates which investigation concepts are genuinely shared.

This reflects UpgradePilot's minimum-useful-generality discipline.

Do not create a generic investigation framework because one mechanism has one useful read.

The separate bounded evidence-gap planning experiment is a different responsibility and does not automatically replace this deterministic current path.

---

## 18. The application executes the selected read deterministically

Primary application owner:

~~~text
src/upgradepilot/investigation.py
~~~

Once the Python-support selector returns an investigation, application composition verifies:

~~~text
selected repository == pull request repository
selected revision   == pull request head SHA
~~~

Then it executes the already-admitted exact-head read:

~~~text
repository_client.get_exact_head_text_file(
    pull_request,
    "pyproject.toml"
)
~~~

and passes the returned evidence through:

~~~text
interpret_target_python_declaration(...)
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
~~~

This is an important control pattern:

~~~text
reasoning selects bounded evidence target
→ application rechecks exact authority/identity
→ deterministic provider capability executes
→ domain interpreter evaluates result
→ candidate is reevaluated
~~~

Selection is not execution authority by itself.

---

## 19. Target relevance is a separate bounded proposition owner

Primary source:

~~~text
src/upgradepilot/target/relevance.py
~~~

Its responsibility is deliberately narrow:

> Does the grounded dropped Python major/minor line intersect the exact target revision's declared [project].requires-python range?

Possible states include:

~~~text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
~~~

Its module docstring explicitly says relevance is **not**:

~~~text
compatibility
safety
merge readiness
maintainer recommendation
~~~

This separation prevents a target range overlap from becoming a global upgrade verdict.

---

## 20. Overlap can establish bounded candidate applicability

After exact target declaration evidence is acquired, suppose:

~~~text
upstream grounded claim:
Python 3.9 support dropped in crossed interval

target requires-python:
>=3.9
~~~

If the accepted deterministic specifier method finds at least one stable Python 3.9.Z version admitted by the target declaration:

~~~text
target relevance = declared_python_overlap
~~~

The Python-support applicability path becomes:

~~~text
upstream drop = established
target declaration = established
activation overlap = established
~~~

Therefore:

~~~text
candidate applicability = established_applicable
~~~

The conclusion is bounded:

> The Python-support-drop candidate applies to the exact target's declared Python installation range.

It is not:

~~~text
the application definitely runs on the dropped version
the build fails
tests fail
upgrade is unsafe
block the update
~~~

---

## 21. Non-overlap can establish bounded non-applicability

Suppose the grounded dropped line is:

~~~text
Python 3.9
~~~

while the exact target declaration is:

~~~text
>=3.10
~~~

Under the accepted deterministic comparison:

~~~text
target relevance = outside_declared_python_range
~~~

The activation proposition is refuted.

Because the current Python-support candidate has one represented bounded path and path-model coverage is declared sufficient for that candidate:

~~~text
candidate applicability = established_not_applicable
~~~

Meaning:

> This specific Python-support-drop mechanism does not apply through the target's declared Python installation range.

It does **not** mean:

~~~text
no other impact mechanism applies
the whole dependency update is safe
merge is justified
~~~

Candidate-discovery coverage remains a separate question.

---

## 22. Missing target declaration remains unresolved after investigation

If:

~~~text
pyproject.toml unavailable
requires-python missing/unreadable under admitted method
~~~

the target interpreter can produce:

~~~text
TargetPythonDeclarationProblem
~~~

Then target relevance becomes:

~~~text
target_declaration_unresolved
~~~

Applicability remains:

~~~text
unresolved
~~~

But note the difference from pre-acquisition state.

Before the read:

~~~text
exact target declaration not yet acquired
~~~

After a failed/insufficient read:

~~~text
the selected acquisition was attempted
and produced a typed target evidence problem
~~~

The selector therefore does not repeatedly request the same read.

This prevents an infinite investigate-again loop.

---

## 23. Unsupported comparison is not missing evidence

A target declaration may be successfully acquired but use a specifier shape outside the accepted deterministic comparison method.

Then:

~~~text
target declaration proposition
→ established / sufficient

activation proposition
→ unresolved / sufficient
~~~

Why sufficient coverage?

Because the evidence itself exists.

The uncertainty is now methodological:

~~~text
accepted comparator cannot resolve this shape
~~~

That is different from evidence absence.

This distinction matters because reacquiring the same file cannot fix it.

---

## 24. Exact target revision is enforced during reevaluation

When target relevance is supplied to:

~~~text
evaluate_python_support_drop_impact(...)
~~~

the evaluator verifies that target evidence refers to:

~~~text
candidate.target_revision
~~~

A different revision is rejected.

Likewise target relevance must be derived from:

~~~text
candidate.upstream_claim
~~~

not another support-drop claim.

This is cross-object provenance validation.

The general rule is:

> **A logically valid result from the wrong transition or revision is not valid evidence for this candidate.**

---

## 25. Upstream unresolved state cannot be smuggled into a grounded candidate

The Python-support candidate requires:

~~~text
GroundedPythonSupportDropClaim
~~~

not a generic unresolved upstream result.

If a caller tries to reevaluate a grounded candidate with:

~~~text
upstream_claim_unresolved
~~~

the impact layer rejects the inconsistent state.

This prevents an impossible object graph:

~~~text
candidate exists because upstream mechanism was grounded
+
assessment says same upstream mechanism is unresolved
~~~

Typed contracts are being used to preserve reasoning coherence, not merely code organization.

---

## 26. PublicPullRequestInvestigation is the typed evidence envelope

Primary type:

~~~text
PublicPullRequestInvestigation
~~~

in:

~~~text
src/upgradepilot/investigation.py
~~~

It preserves the heterogeneous outputs of the current read-only investigation sequence.

Important fields include categories such as:

~~~text
PR / changed files
dependency result
workflow + CI coverage
proposed/old PyPI release evidence
upstream repository / release interval / tag / changelog evidence
grounded support-drop result
target Python evidence / relevance
pre-investigation Python-support impact
selected Python-support investigation
post-investigation Python-support impact
artifact-serviceability candidate
Target artifact-environment evidence
artifact-serviceability impact
~~~

This object is not a final verdict.

It is a typed record of what the current evidence graph established, failed to establish, or attempted.

---

## 27. Investigation composition preserves branch independence

The application does not treat the evidence graph as one all-or-nothing pipeline.

For example, after proposed release evidence:

~~~text
artifact-serviceability branch
and
upstream semantic branch
~~~

can progress independently.

If old release acquisition fails:

~~~text
artifact candidate branch stops
BUT
upstream support-drop branch can continue
~~~

If changelog/upstream semantic evidence fails:

~~~text
already-established artifact candidate is not erased
~~~

This is important because later synthesis should see the strongest truthful set of independently earned evidence.

A local branch problem is not automatically a global stop.

---

## 28. Current Python-support normal application path

The implemented normal path is approximately:

~~~text
DependencyVersionChange
        ↓
proposed exact PackageReleaseEvidence
        ↓
trusted UpstreamRepositoryEvidence
        ↓
release interval
        ↓
exact release index / crossed releases
        ↓
exact proposed tag → immutable commit
        ↓
changelog path + exact tagged changelog
        ↓
AuthoritativeUpstreamIntervalEvidence
        ↓
support-drop semantic extraction
        ↓
deterministic grounding
        ↓
GroundedPythonSupportDropClaim
        ↓
PythonSupportDropImpactCandidate
        ↓
pre-investigation applicability = unresolved
        ↓
select exact target pyproject read
        ↓
TargetPythonDeclaration / Problem
        ↓
TargetPythonRelevanceResult
        ↓
post-investigation applicability
~~~

This is the clearest implemented realization of the Product Decision Model's current reasoning spine.

---

## 29. Artifact serviceability demonstrates transfer without identical investigation logic

Group 7 already teaches the artifact-serviceability mechanism in detail.

Its relevance here is architectural.

It reuses the same generic applicability types:

~~~text
PropositionAssessment
evaluate_applicability_path
evaluate_candidate_applicability
~~~

but supplies different propositions:

~~~text
published wheel transition established
exact target wheel compatibility established
target had old compatible wheel
target lacks proposed compatible wheel
~~~

This confirms that the generic applicability layer is not Python-support-specific.

However, artifact-serviceability currently does **not** have the same complete normal investigation-selection path.

Current normal flow lacks a producer for exact:

~~~text
TargetWheelCompatibilityEvidence.supported_tags
~~~

So its applicability remains unresolved.

The important lesson is:

~~~text
second mechanism reuses applicability semantics
!= every mechanism must reuse the same investigation selector
~~~

---

## 30. Unresolved artifact applicability does not automatically select investigation

This is a useful transfer test.

Artifact-serviceability has a real unresolved proposition:

~~~text
exact target wheel compatibility
~~~

But current product does not automatically say:

~~~text
unresolved
→ run something
~~~

Why not?

Because a trustworthy normal producer/investigation for exact target-supported wheel tags has not yet been admitted.

This demonstrates the Product Decision Model principle:

> **Investigation requires a justified discriminating capability, not merely an unresolved state.**

The absence of an investigation is therefore not necessarily a bug.

It can be the correct stop boundary.

---

## 31. Candidate applicability is mechanism truth, not transition-level closure

Consider a dependency update with two discovered candidates:

~~~text
Python-support candidate
→ established_not_applicable

artifact-serviceability candidate
→ unresolved
~~~

It is invalid to conclude:

~~~text
Python-support candidate not applicable
→ update safe
~~~

because:

1. another discovered mechanism remains unresolved;
2. candidate-discovery completeness is not generally established;
3. overall evidence sufficiency is a later responsibility;
4. maintainer-action permission is a later responsibility.

Likewise:

~~~text
one candidate = established_applicable
~~~

does not automatically map to:

~~~text
block
investigate
defer
~~~

The action depends on later action-relative semantics and positive permission.

---

## 32. Why the generic applicability layer is deliberately small

A more ambitious design could have introduced:

~~~text
generic rule DSL
Boolean AST
graph execution engine
SAT solver
universal candidate schema
universal investigation planner
~~~

Current product evidence did not require those.

The implemented layer instead owns only:

~~~text
typed proposition state
typed evidence coverage
conjunctive path composition
alternative-path candidate composition
path-model coverage
~~~

This is enough for the current mechanisms.

The advantage is traceability:

~~~text
which proposition failed?
which evidence owner?
was evidence insufficient?
was a path refuted?
was the path model incomplete?
~~~

The result remains understandable without a hidden score or opaque rule graph.

---

## 33. Established not applicable is stronger than we did not see relevance

For candidate-level non-applicability, current semantics require:

~~~text
every represented viable path refuted
+
path-model coverage sufficient
~~~

This is intentionally stricter than:

~~~text
no path established
~~~

Why?

Because:

~~~text
unresolved path
!= refuted path
~~~

and:

~~~text
all known paths refuted
+ unknown material path may exist
!= candidate globally eliminated
~~~

Tests in:

~~~text
tests/test_impact_applicability.py
~~~

explicitly protect this distinction.

---

## 34. Conflict is preserved rather than averaged away

A proposition or viable path can be:

~~~text
conflicted
~~~

This is not treated as:

~~~text
50/50
low confidence
unresolved by default
~~~

If no path is established and at least one viable path remains genuinely conflicted:

~~~text
candidate state = conflicted
~~~

Other unresolved alternatives remain preserved in the returned path detail.

This matters because contradictory evidence is different from missing evidence.

The current Python-support implementation does not need every generic conflicted state today, but the generic contract preserves it.

---

## 35. Investigation stopping is as important as investigation selection

A useful investigation loop must know when **not** to continue.

Current Python-support flow stops selecting its target-file read when:

~~~text
target relevance already exists
~~~

even if applicability is still unresolved.

This means:

~~~text
investigation attempted
→ new evidence/problem recorded
→ reevaluate
→ if same acquisition no longer discriminates, stop
~~~

The system does not equate:

~~~text
unresolved result
with
permission to repeat or broaden investigation indefinitely
~~~

This is a key anti-agentic-overreach rule.

---

## 36. Product-simulation pressure behind the model

Earlier product-simulation work exposed several distinct shapes.

Examples include:

### Python-support range

A documented support drop can be meaningful only if the exact target declaration overlaps the dropped line.

This supports:

~~~text
mechanism evidence
+ exact target activation
→ bounded applicability
~~~

### Artifact transition

Loss of a wheel path can matter independently of Python support metadata.

This supports multiple mechanism-specific candidates rather than one generic compatibility flag.

### Expensive observation may be unnecessary

S008 showed that once the owned artifact-transition proposition is resolved from exact package evidence, a source-build observation answers a **different** proposition.

Therefore:

~~~text
more dynamic evidence
!= automatically more useful evidence
~~~

Investigation must be proposition-relative.

---

## 37. Current tests establish the stable Note-1 responsibility

### Generic applicability tests

~~~text
tests/test_impact_applicability.py
~~~

protect:

- complete established path → established applicable;
- all refuted paths + sufficient path coverage → established not applicable;
- all refuted paths + insufficient/unresolved path coverage → unresolved;
- unresolved necessary proposition → unresolved path;
- conflicted proposition → conflicted path;
- one established alternative can establish applicability without erasing conflicted alternatives;
- a refuted necessary proposition eliminates its conjunctive path;
- empty path/candidate composition is rejected.

### Python-support impact tests

~~~text
tests/test_python_support_impact.py
~~~

protect:

- candidate binds target identity without self-authorizing exposure;
- pre-acquisition applicability is unresolved;
- missing exact target declaration selects the bounded investigation;
- attempted target evidence problem prevents reselection of the same acquisition;
- overlap establishes bounded applicability;
- non-overlap establishes bounded non-applicability;
- missing target evidence remains unresolved with insufficient coverage;
- unsupported comparison remains unresolved despite sufficient acquired evidence;
- mismatched dependency transition is rejected;
- different target revision is rejected;
- unresolved upstream state cannot be smuggled into a grounded candidate.

### Investigation integration tests

~~~text
tests/test_investigation.py
~~~

protect the application composition and branch relationships.

This learning-authoring session is inspecting current source/tests. It is **not** executing a fresh test suite.

---

## 38. What Note 1 proves about normal-path reachability

Current normal production composition can actually reach the Python-support reasoning sequence.

That matters because a domain contract alone does not prove the application can produce the required inputs.

Current investigation.py composes:

~~~text
real DependencyVersionChange
→ real PyPI/upstream authority chain
→ GroundedPythonSupportDropClaim
→ impact candidate
→ pre-investigation assessment
→ mechanism-specific selection
→ exact target file acquisition
→ relevance
→ reevaluated impact assessment
~~~

So this is not merely a library API exercised by isolated fixtures.

The normal application has an integrated producer/consumer path for this mechanism.

---

## 39. What remains less complete in normal production

The same is not true for every mechanism/proposition.

Artifact-serviceability normal production currently reaches:

~~~text
artifact candidate
→ initial unresolved applicability
→ partial static Target artifact-environment context
~~~

but not:

~~~text
exact TargetWheelCompatibilityEvidence
→ exact supported wheel tags
→ final artifact applicability
~~~

This demonstrates why normal-producer reachability must be audited independently from type/API existence.

An implemented evaluator accepting a strong evidence type does not prove the application can produce it.

---

## 40. Boundary to maintainer-action synthesis

This note stops at:

~~~text
typed technical investigation
+ mechanism-specific applicability states
+ residual mechanism uncertainty
~~~

It does **not** teach or freeze the current maintainer-action synthesis layer.

That is deliberate.

The stable Product Decision Model itself ends with:

~~~text
INVESTIGATION STOP
↓
LATER OVERALL SUFFICIENCY / POLICY / MAINTAINER-FACING SYNTHESIS
~~~

Why separate them?

Because:

~~~text
technical fact:
candidate applicable

is different from

policy/action permission:
which maintainer action is positively justified?
~~~

The active 2026-09-19 audit is still validating the latter responsibility's producer reachability and uncertainty-preservation behavior.

Therefore Group 9 Note 2 remains gated.

---

## 41. Common reasoning mistakes to avoid

### Mistake 1

~~~text
grounded upstream problem exists
→ target is affected
~~~

Correction:

~~~text
grounded mechanism
→ candidate
→ target applicability still needs exact target propositions
~~~

### Mistake 2

~~~text
no target overlap
→ update safe
~~~

Correction:

~~~text
this bounded candidate is not applicable
!= all mechanisms closed
~~~

### Mistake 3

~~~text
unresolved
→ investigate
~~~

Correction:

~~~text
material unresolved proposition
+ justified discriminating capability
→ investigation may be selected
~~~

### Mistake 4

~~~text
target file read failed
→ keep selecting same read
~~~

Correction:

~~~text
attempt/result already recorded
→ same acquisition may no longer discriminate
→ preserve unresolved state and stop
~~~

### Mistake 5

~~~text
all represented paths refuted
→ not applicable
~~~

Correction:

~~~text
also require sufficient path-model coverage
~~~

### Mistake 6

~~~text
implemented evidence type exists
→ normal product can produce it
~~~

Correction:

~~~text
trace producer → composition → consumer
~~~

---

## 42. Engineering progression worth retaining

The useful progression is:

~~~text
early desire:
understand dependency-update risk
        ↓
pressure from real cases:
different mechanisms fail differently
        ↓
correction:
do not collapse everything into one compatibility/risk label
        ↓
impact candidates:
mechanism established, target applicability separate
        ↓
generic minimum composer:
proposition state + evidence coverage + paths
        ↓
coverage correction:
evidence coverage != path coverage != candidate-discovery coverage
        ↓
open-world rule:
missing evidence != negative evidence
        ↓
Python-support implementation:
exact target declaration becomes the first discriminating investigation
        ↓
stopping correction:
unresolved != automatically repeat investigation
        ↓
second mechanism transfer:
artifact serviceability reuses applicability semantics
but exposes a different missing evidence producer
        ↓
current boundary:
technical investigation state is ready for later action-relative synthesis,
but does not itself choose the action
~~~

The transferable lesson is:

> **Separate mechanism discovery, target applicability, evidence acquisition, and action policy so each stronger conclusion is earned by the proposition that actually supports it.**

---

## 43. Current fact, rationale, judgment, and open boundary

### Current implementation fact

UpgradePilot has:

~~~text
generic deterministic applicability composition
+
one fully integrated mechanism-specific Python-support
candidate/investigation/reevaluation flow
+
artifact-serviceability as a second mechanism reusing applicability semantics
~~~

### Evidenced rationale

The Product Decision Model specification, current source/tests, product-simulation pressure, and current source reconstruction consistently support:

~~~text
candidate != applicable
applicable != consequence proven
not applicable != missing evidence
unresolved != negative evidence
unresolved != automatic investigation
technical applicability != maintainer action
~~~

### Engineering judgment

The current generic layer is proportionate.

It generalizes only the concepts already shared by real mechanisms while leaving domain propositions and investigation logic mechanism-specific.

### Open boundary

The next note must answer a different question:

> Given the heterogeneous PublicPullRequestInvestigation, what exact action-relative evidence sufficiency and positive permission justify a maintainer-facing action or abstention?

That responsibility is intentionally not frozen here because the active audit is still testing its normal-path reachability and uncertainty handling.

---

## 44. Depth calibration

### Must own

- impact candidate versus target applicability;
- mechanism-specific candidate design;
- proposition state versus evidence coverage;
- conjunctive path semantics;
- alternative path semantics;
- evidence coverage versus path-model coverage versus candidate-discovery coverage;
- open-world negative reasoning;
- why all represented paths refuted is insufficient without path-model coverage;
- pre-acquisition unresolved state;
- mechanism-specific discriminating investigation;
- why unresolved does not automatically authorize investigation;
- why the same acquisition is not repeatedly selected after an attempted result/problem;
- exact transition/revision/claim identity guards;
- candidate applicability versus transition-level safety;
- typed investigation state versus later maintainer-action synthesis.

### Understand operationally

- PropositionAssessment;
- ApplicabilityPathAssessment;
- CandidateApplicabilityAssessment;
- Python-support candidate statuses;
- target relevance states;
- the pyproject.toml acquisition/reevaluation flow;
- PublicPullRequestInvestigation as the heterogeneous evidence envelope;
- artifact-serviceability as transfer evidence for generic applicability.

### Lookup-level

- exact helper function names;
- every detail/reason string;
- full Python specifier implementation;
- every upstream acquisition helper;
- every investigation dataclass field;
- all product-simulation chronology.

### Deferred deliberately

- generic investigation planner;
- universal impact mechanism registry;
- generic rule/graph engine;
- exact target wheel-tag producer;
- overall evidence sufficiency;
- non-abstention action admission;
- maintainer-action synthesis implementation changes.

---

## 45. Fast relearning route

Use this sequence:

~~~text
1. Recall:
   candidate != applicability != maintainer action.

2. Open:
   docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
   and reread the reasoning spine + three coverage questions.

3. Open:
   impact/applicability.py
   and explain:
   proposition state,
   evidence coverage,
   path composition,
   path-model coverage.

4. Read:
   tests/test_impact_applicability.py
   especially:
   all paths refuted + insufficient coverage.

5. Open:
   impact/python_support.py
   and trace:
   candidate
   → pre-acquisition assessment
   → investigation selection
   → post-evidence reevaluation.

6. Read:
   tests/test_python_support_impact.py
   for overlap, non-overlap, missing evidence,
   unsupported comparison, and no repeated acquisition.

7. Open:
   target/relevance.py
   and state exactly what relevance means and does not mean.

8. Open:
   investigation.py
   and trace the normal Python-support path.

9. Compare:
   artifact-serviceability Group-7 note
   and explain why it reuses applicability but lacks the same normal evidence producer.

10. Stop at:
   later overall sufficiency / maintainer-action synthesis.
~~~

---

## 46. Ownership / transfer questions

Without looking at this note, explain:

1. Why does a grounded Python-support drop create a candidate rather than an already-applicable impact?
2. What is the difference between proposition state and evidence coverage?
3. Why can every represented applicability path be refuted while candidate-level non-applicability still remains unresolved?
4. What is the difference between path-model coverage and candidate-discovery coverage?
5. Why is not observed normally unresolved rather than refuted?
6. What exact evidence gap causes the Python-support target-file investigation to be selected?
7. Why is the same pyproject.toml acquisition not selected again after it returns a typed problem?
8. Why can an unsupported specifier comparison have sufficient evidence coverage but unresolved proposition state?
9. Why does exact target revision identity matter during reevaluation?
10. Why does established_not_applicable for the Python-support candidate not justify a merge recommendation?
11. Why does artifact serviceability reuse the generic applicability layer without automatically reusing the Python-support investigation selector?
12. What would need to be true before adding a generic investigation-planning abstraction would be justified?

### Transfer exercise

Suppose:

~~~text
Grounded support-drop claim:
Python 3.9 dropped

Target A:
requires-python = ">=3.10"

Target B:
pyproject.toml unavailable

Target C:
requires-python uses a validly acquired shape
that the current comparator does not support
~~~

For each target, predict:

~~~text
target-declaration proposition state/coverage
activation proposition state/coverage
candidate applicability
whether the exact target-file acquisition should be selected now
~~~

Then explain why the three unresolved/non-applicable outcomes imply different next actions at the **investigation** layer without yet choosing any maintainer-facing action.

---

## 47. Evidence anchors

Pinned source/test horizon:

~~~text
main@e91b79908e21ad1529b5c8c3fd8dcf3841984deb
~~~

Canonical stable semantics:

~~~text
docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
~~~

Primary current source:

~~~text
src/upgradepilot/impact/applicability.py
src/upgradepilot/impact/python_support.py
src/upgradepilot/target/relevance.py
src/upgradepilot/investigation.py
~~~

Transfer/reference mechanism:

~~~text
src/upgradepilot/impact/artifact_serviceability.py
learning/2026-09-19-artifact-serviceability-and-exact-target-wheel-applicability.md
~~~

Primary current tests:

~~~text
tests/test_impact_applicability.py
tests/test_python_support_impact.py
tests/test_investigation.py
~~~

Current source-reconstruction evidence:

~~~text
working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md
~~~

Useful earlier learning prerequisites:

~~~text
learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md
learning/2026-09-02-target-python-evidence-resolution/
~~~

This artifact intentionally stops before the current maintainer-action synthesis responsibility.

It is a learning snapshot, not a specification, live-state owner, or product-change authorization.

UP-SKILL:upgradepilot-learning-artifact
UP-SKILL:upgradepilot-repository-audit
