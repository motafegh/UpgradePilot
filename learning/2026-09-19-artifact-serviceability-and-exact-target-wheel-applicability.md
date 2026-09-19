# Artifact Serviceability and Exact Target-Wheel Applicability — Current Learning Note

**Learning-artifact date:** 2026-09-19  
**Source/test evidence horizon:** main@57a2bcda54f7cbe4e7e8c47f0fb6a92bc51aba4a  
**Roadmap responsibility:** Group 7 — artifact serviceability and wheel-compatibility applicability  
**Artifact role:** current learning snapshot for the implemented artifact-serviceability mechanism, its exact target-evidence contract, normal application composition, and the presently missing normal target-wheel-tag producer  
**Target depth:** **must master / own** candidate-versus-applicability separation, exact wheel-tag reasoning, target evidence provenance, current normal-path reachability, and proof/non-proof boundaries; understand packaging.tags.Tag and parse_wheel_filename operationally; keep full packaging-tag generation internals and future acquisition design deferred

This note answers one central question:

> **How can UpgradePilot detect that a dependency update loses a published wheel capability without prematurely claiming that the loss actually affects the exact target repository environment?**

The shortest current mental model is:

~~~text
exact old PyPI release inventory
+ exact proposed PyPI release inventory
        ↓
interpret published wheel filenames/tags
        ↓
old tag set - proposed tag set
        ↓
target-agnostic ArtifactServiceabilityImpactCandidate
        ↓
exact target-owned supported wheel-tag evidence
        ↓
compare target tags against COMPLETE old and proposed wheel inventories
        ↓
established_applicable
or established_not_applicable
or unresolved
~~~

The most important boundary is:

~~~text
published wheel capability disappeared
!=
the exact target lost its compatible wheel path
~~~

And the current product has another equally important boundary:

~~~text
TargetWheelCompatibilityEvidence contract exists
!=
normal application can currently produce that evidence
~~~

---

## 1. Why artifact serviceability is a separate impact mechanism

Dependency-update impact is broader than source/API behavior.

A release can keep accepting the same Python version while changing how an environment can install it:

~~~text
old release
→ compatible prebuilt wheel exists

new release
→ that wheel capability disappears
→ source distribution may remain
~~~

That is not automatically:

~~~text
package is incompatible
source build fails
application behavior breaks
~~~

It is a more precise mechanism:

> **the prebuilt artifact path may have changed for some target environments.**

The real S008 ScenarioRunner/OpenCV case supplied this pressure. For the bounded CPython-3.6 Linux question, the old OpenCV release had a compatible prebuilt wheel while the proposed release did not; an sdist remained. The correct technical distinction was therefore:

~~~text
binary artifact path available
→
binary artifact path unavailable
+ source fallback remains
~~~

not “Python 3.6 is impossible” and not “source build fails.”

That product-simulation pressure is useful because it separates four propositions that must not be collapsed:

~~~text
interpreter/package metadata permits target
!=
compatible wheel is published
!=
source fallback is published
!=
source fallback succeeds in the exact target environment
~~~

Current artifact-serviceability code implements the wheel-transition/applicability part of that distinction.

---

## 2. Current responsibility owner

Primary owner:

~~~text
src/upgradepilot/impact/artifact_serviceability.py
~~~

It contains two distinct responsibilities.

### Candidate formation

build_artifact_serviceability_impact_candidate(...) asks approximately:

> Did exact old/proposed release evidence establish the loss of one or more published wheel compatibility tags?

This stage is deliberately **target-agnostic**.

### Applicability evaluation

evaluate_artifact_serviceability_impact(...) asks approximately:

> Given exact target-supported wheel tags, did the target have an old compatible wheel and does it now lack a compatible proposed wheel?

This stage is **target-specific**.

Do not merge these two questions mentally or architecturally.

---

## 3. Exact PyPI release inventories are the artifact-side evidence

The mechanism consumes:

~~~text
PackageReleaseEvidence(old version)
PackageReleaseEvidence(proposed version)
~~~

from:

~~~text
src/upgradepilot/pypi/release.py
~~~

Each release record carries exact package/version identity plus its published distribution inventory, including fields such as:

~~~text
filename
package_type
URL
sha256
~~~

The candidate builder first verifies that both release records match the exact DependencyVersionChange:

~~~text
normalized package identity
old requested/published version == dependency old version
proposed requested/published version == dependency proposed version
~~~

Identity disagreement is not treated as “close enough.” It is rejected.

This preserves an important evidence rule:

> **Artifact reasoning must operate on the exact dependency transition being investigated, not merely releases with similar names or nearby versions.**

---

## 4. Wheel filenames encode compatibility capabilities

A wheel filename can encode one or more compatibility tags.

Conceptually, a tag has:

~~~text
interpreter
ABI
platform
~~~

Example:

~~~text
cp36-cp36m-manylinux1_x86_64
~~~

means a particular CPython/ABI/platform compatibility capability.

UpgradePilot uses packaging.utils.parse_wheel_filename(...), which produces packaging.tags.Tag values rather than inventing a wheel filename parser.

For every exact release inventory:

~~~text
published bdist_wheel files
→ parse filename
→ validate wheel package/version identity
→ PublishedWheelArtifact(filename, tags)
→ union all published tags
~~~

Malformed or identity-conflicting wheel filenames do not silently disappear. They produce:

~~~text
ArtifactServiceabilityEvidenceProblem
~~~

with states such as:

~~~text
wheel_filename_uninterpretable
wheel_identity_mismatch
~~~

That matters because ignoring a bad wheel record could manufacture a false comparison from an incomplete inventory.

---

## 5. Candidate formation is a set-difference question

Let:

~~~text
O = all exact compatibility tags published by old-release wheels
P = all exact compatibility tags published by proposed-release wheels
~~~

The first candidate trigger is:

~~~text
removed_tags = O - P
~~~

If:

~~~text
removed_tags = empty
~~~

the current bounded mechanism returns None, meaning:

> This mechanism did not observe loss of a published wheel compatibility tag.

That is not a global “no impact” verdict.

If one or more tags disappear, UpgradePilot constructs:

~~~text
ArtifactServiceabilityImpactCandidate
~~~

carrying:

~~~text
exact PR identity
exact dependency transition
exact old/proposed release evidence
target repository + immutable target revision
old/proposed interpreted wheel inventories
removed tags
added tags
old/proposed sdist availability
mechanism/exposure/consequence state
~~~

The initial states make the evidence strength explicit:

~~~text
mechanism_status   = established
exposure_status    = to_evaluate
consequence_status = possible
~~~

This means:

~~~text
published artifact transition
→ established

exact target exposure
→ not yet established

target consequence
→ only possible
~~~

---

## 6. Source-distribution fallback is preserved but not overread

The candidate also checks whether old/proposed releases publish an sdist.

If the proposed release still has an sdist, the possible consequence is approximately:

~~~text
target had compatible old wheel
+ no compatible proposed wheel
→ installation may move from prebuilt wheel to source fallback
~~~

But:

~~~text
sdist exists
!=
source build succeeds
~~~

Source-build success may depend on:

~~~text
compiler/toolchain availability
native libraries
platform headers
build backend behavior
target environment details
~~~

The artifact-serviceability candidate does not manufacture those facts.

This is the same lesson S008 exposed before implementation:

> **A changed installation obligation is itself meaningful technical impact, while success of the fallback path remains a separate proposition.**

---

## 7. Why removed tags alone do not establish target applicability

A tempting but incorrect shortcut is:

~~~text
old tag disappeared
→ target is affected
~~~

That is unsound.

Imagine:

~~~text
old release:
  cp36-cp36m-manylinux1_x86_64

proposed release:
  cp37-abi3-manylinux_2_17_x86_64
~~~

The old exact tag disappeared.

But one exact target environment might support only the old tag, while another target may support both the old tag and the proposed abi3 capability.

So applicability must compare the **target-supported tag set** with the **complete old and proposed inventories**.

The correct relation is:

~~~text
old compatible path:
old_published_tags ∩ target_supported_tags

proposed compatible path:
proposed_published_tags ∩ target_supported_tags
~~~

The candidate's removed_wheel_tags are useful mechanism evidence, but applicability does **not** simply ask whether the target supports one removed tag.

---

## 8. The exact target-evidence contract

Current source defines:

~~~text
TargetWheelCompatibilityEvidence
~~~

with:

~~~text
repository
revision
source
supported_tags: frozenset[Tag]
~~~

This is deliberately a strong contract.

Its meaning is approximately:

> For this exact repository revision, target-owned evidence establishes this exact supported wheel-tag set.

It is not:

~~~text
runner label
Python major/minor label
UpgradePilot's own local sys_tags()
a guessed platform
a generic Linux + Python 3.11
~~~

Repository and revision must match the candidate. A witness for another target or another revision is rejected rather than reused.

The companion problem type preserves failure to establish exact compatibility:

~~~text
TargetWheelCompatibilityProblem
    evidence_unavailable
    evidence_insufficient
~~~

This distinction allows:

~~~text
target evidence contract exists
but exact target evidence unavailable
→ applicability remains unresolved
~~~

without inventing compatibility.

---

## 9. Applicability is a proposition path

evaluate_artifact_serviceability_impact(...) evaluates a bounded path with four central propositions:

~~~text
P1 — published wheel transition established
P2 — exact target wheel compatibility established
P3 — target had an old compatible published wheel
P4 — target lacks a compatible proposed published wheel
~~~

Conceptually:

~~~text
P1 established
+ P2 established
+ P3 established
+ P4 established
→ established_applicable
~~~

### Applicable example

Controlled target evidence:

~~~text
target tags = {cp36-cp36m-manylinux1_x86_64}
~~~

Old release publishes that capability; proposed release publishes no compatible capability.

Result:

~~~text
established_applicable
~~~

### Refuted because proposed release still serves the target

Controlled target evidence supports both an old tag and another tag published by the proposed release.

Result:

~~~text
established_not_applicable
~~~

This test protects the critical rule:

> **Losing one old exact tag does not establish serviceability loss when another proposed wheel still serves the same exact target.**

### Refuted because the target never had the old wheel path

If exact target tags do not intersect the old release's wheel tags:

~~~text
target_had_old_compatible_published_wheel
→ refuted
~~~

so the specific lost-prebuilt-wheel-path candidate is not applicable to that target.

### Unresolved

If exact target evidence is absent or insufficient:

~~~text
applicability.state = unresolved
~~~

That is the current normal production situation.

---

## 10. Static Target artifact-environment evidence is useful but weaker

A neighboring owner exists:

~~~text
src/upgradepilot/target/artifact_environment.py
~~~

It can preserve static workflow declarations such as:

~~~text
exact workflow repository/revision/path
selected job
literal runs-on value
literal setup-python version
direct changed-source installation declaration
limitations
~~~

A successful result explicitly carries:

~~~text
exact_wheel_compatibility_state = unresolved
~~~

This is not accidental.

For example:

~~~text
runs-on = ubuntu-22.04
python-version = 3.9
pip install -r requirements.txt
~~~

still does not fully establish:

~~~text
interpreter implementation
exact ABI
architecture
manylinux/musllinux compatibility
container/runtime detail
complete supported Tag set
~~~

Therefore:

~~~text
TargetArtifactEnvironmentEvidence
!=
TargetWheelCompatibilityEvidence
~~~

This is one of the most important ownership distinctions in this responsibility.

---

## 11. Current normal application composition

Current application owner:

~~~text
src/upgradepilot/investigation.py
~~~

For a supported dependency transition it roughly performs:

~~~text
proposed exact PyPI release
→ old exact PyPI release
→ build artifact-serviceability candidate
~~~

When a real candidate exists, current normal flow then does:

~~~text
candidate
→ evaluate_artifact_serviceability_impact(candidate)
   with NO exact target-wheel witness
→ applicability unresolved
~~~

and separately:

~~~text
supported direct-requirements CI relationship
→ compose partial static Target artifact-environment result(s)
~~~

The important current composition shape is therefore:

~~~text
candidate
├── immediate impact assessment without TargetWheelCompatibilityEvidence
│   └── unresolved applicability
│
└── partial static Target environment composition
    └── runner/Python/install declaration evidence
        but exact_wheel_compatibility_state remains unresolved
~~~

The static Target results are not currently passed back into the impact evaluator—and even if they were, they are not the exact tag witness required by that evaluator.

### Current production bottleneck

The current system has:

~~~text
exact target-wheel compatibility CONTRACT
~~~

but no admitted normal producer that establishes:

~~~text
supported_tags: frozenset[Tag]
~~~

for the exact target environment/revision.

That is a **missing evidence producer**, not a reason to weaken the impact contract.

---

## 12. CI consuming-job specificity is a separate issue

Current CI evidence can preserve the exact supported consuming job:

~~~text
workflow revision
workflow path
job_key
step identity
dependency source
command occurrence
~~~

But current Target composition calls:

~~~text
interpret_target_artifact_environment(
    definition,
    dependency_source_file=...
)
~~~

without passing the already-known CI job_key.

Target then independently accepts only a one-job workflow. With multiple jobs it may return:

~~~text
ambiguous_target_job_selection
~~~

The current integration test deliberately preserves this behavior even when CI already knows which job consumed the dependency.

This is a real composition limitation:

~~~text
available CI relationship
→ not transferred into Target selection
~~~

However, the September 19 re-audit corrected an important assumption:

> **Fixing consuming-job → Target handoff would improve static Target environment selection, but it would still not produce exact target-supported wheel tags.**

So keep two bottlenecks separate:

~~~text
Bottleneck A
CI job identity not transferred to Target
→ limits partial static Target environment interpretation

Bottleneck B
no normal exact target-wheel-tag producer
→ blocks target-specific artifact applicability
~~~

B is the stronger proposition required by the artifact impact evaluator.

Do not repair A and then claim B is solved.

---

## 13. Candidate-gated Target work

The application intentionally does not compose Target artifact-environment evidence for every dependency update.

Current integration tests preserve:

~~~text
no real artifact-serviceability candidate
→ target_artifact_environment_results = ()
~~~

This is useful proportionality.

The current Target artifact-environment work exists to help evaluate a real artifact candidate; it is not a generic reconstruct-every-CI-environment subsystem.

That keeps the evidence graph demand-driven:

~~~text
mechanism pressure exists
→ acquire/interpret mechanism-relevant target context
~~~

rather than:

~~~text
dependency update exists
→ reconstruct every possible environment fact
~~~

---

## 14. Independent evidence branches remain independent

A historical implementation lesson remains important.

Once the proposed release is available, the application has sibling branches:

~~~text
proposed release
├── artifact branch
│   └── exact old release → artifact candidate
│
└── upstream semantic branch
    └── repository/release/changelog/support reasoning
~~~

If old-release acquisition fails:

~~~text
artifact candidate unavailable
~~~

but independently earned upstream evidence can continue.

Likewise, an upstream changelog/source problem does not erase an already established artifact candidate.

This teaches a general UpgradePilot rule:

> **One evidence branch failing should not destroy unrelated evidence already earned by another branch unless the failed proposition is genuinely a prerequisite.**

The investigation tests preserve these distinctions.

---

## 15. What current tests establish

### Artifact-serviceability owner tests

tests/test_artifact_serviceability.py protects, among other things:

- exact removed wheel tags form a target-agnostic candidate;
- unchanged wheel-tag capability does not manufacture a candidate;
- malformed wheel evidence becomes a typed problem;
- exact dependency/release identity is enforced;
- no exact target compatibility evidence keeps applicability unresolved;
- exact controlled target tags can establish applicability;
- a different compatible proposed tag can refute the loss;
- absence of an old compatible target wheel can refute the loss;
- insufficient target evidence remains unresolved;
- target repository/revision mismatch is rejected.

### Application integration tests

tests/test_investigation.py protects current composition such as:

~~~text
real candidate
→ unresolved artifact impact without target witness

supported direct-requirements relationship
→ partial TargetArtifactEnvironmentEvidence
→ exact wheel compatibility still unresolved
→ artifact impact still has target_evidence = None

no candidate
→ no Target artifact-environment composition

multi-job workflow
+ supported CI consumption
→ Target ambiguous_target_job_selection
→ artifact applicability remains unresolved
~~~

These are fixture-backed executable contracts of intended behavior.

### Proof boundary for this learning-authoring session

This authoring session inspected current source/tests and directly relevant history. It did **not** execute a fresh test suite.

A historical September 8 integration proof reported focused/nearest/full deterministic success after two stale test fixtures were repaired. That proof established the integration boundary at that historical horizon; it is not a fresh 2026-09-19 test run.

Therefore this note claims current **source/test contract inspection**, not fresh executable validation.

---

## 16. Engineering progression worth retaining

The useful progression is not the chronology of every commit. It is the change in the engineering model:

~~~text
real product-simulation pressure
→ wheel availability is distinct from Python support metadata
→ target-agnostic published-artifact candidate introduced
→ exact target-wheel compatibility contract introduced
→ static Target workflow environment owner added
→ normal investigation composes candidate + partial Target context
→ exact target tags remain deliberately unresolved
→ later re-audit distinguishes CI→Target job handoff from the stronger missing tag producer
~~~

Two corrected assumptions matter.

### Correction 1 — static runner/Python labels are not exact wheel compatibility

The product deliberately resisted:

~~~text
ubuntu + Python 3.x
→ guess supported wheel tags
~~~

because the target proposition is stronger than those labels prove.

### Correction 2 — choosing the right CI job is not enough

The later re-audit showed:

~~~text
exact consuming job
→ useful for selecting the relevant static Target job

but
→ still not exact supported wheel tags
~~~

This is a general evidence-design lesson:

> **Improving an earlier relationship does not automatically satisfy a stronger downstream proposition. Trace the exact evidence required by the consumer before selecting a repair.**

---

## 17. Current fact, evidenced rationale, judgment, and open boundary

### Current implementation fact

UpgradePilot can:

~~~text
acquire exact old/proposed PyPI releases
→ interpret exact published wheel tags
→ establish a target-agnostic wheel-capability-loss candidate
→ preserve sdist fallback presence
→ evaluate applicability when exact TargetWheelCompatibilityEvidence is supplied
~~~

Normal application currently does **not** produce that exact target compatibility evidence, so artifact applicability remains unresolved.

### Evidenced rationale

Current source docstrings, tests, the target evidence owner, historical integration records, S008 pressure, and the current-system audit consistently preserve the same evidence boundary:

~~~text
package artifact evidence
!= target environment evidence

partial static target context
!= exact wheel compatibility

candidate
!= applicable impact
~~~

### Engineering judgment

The strong target-evidence contract is preferable to inferring tags from weak labels. The current cost is unresolved normal-path applicability.

That unresolved state is honest and therefore currently better than a falsely precise result.

### Open product boundary

A later selected responsibility may ask:

> What trustworthy observation can establish the exact target-supported wheel-tag set for the exact repository revision/environment?

That question is **not answered by this learning artifact**, and this artifact does not authorize implementation of a producer.

Possible acquisition mechanisms must be evaluated only when the parent product/synthesis work establishes that this exact proposition is decision-critical.

---

## 18. Depth calibration

### Must own

- candidate formation and target applicability are separate propositions;
- a removed published tag is mechanism evidence, not target applicability;
- applicability compares exact target tags with **complete old and proposed wheel inventories**;
- sdist presence does not prove source-build success;
- exact target compatibility evidence must preserve repository/revision/source provenance;
- static Target runner/Python/install facts are weaker than TargetWheelCompatibilityEvidence;
- current normal application has no admitted producer for exact target supported tags;
- CI→Target job handoff and exact wheel-tag production are separate gaps;
- unresolved applicability is currently the truthful normal result.

### Understand operationally

- what Tag(interpreter, abi, platform) represents;
- what parse_wheel_filename(...) contributes;
- why set intersection/difference is the core comparison mechanism;
- how exact old/proposed PackageReleaseEvidence enters candidate formation;
- why application gates Target composition on a real candidate;
- how repository/revision mismatch protects provenance.

### Lookup-level

- full Python wheel filename grammar;
- complete manylinux/musllinux/macOS/Windows tag semantics;
- exact packaging API internals;
- every proposition/reason string;
- every test fixture constructor.

### Deferred deliberately

- design of a normal target wheel-tag producer;
- runtime log/artifact acquisition;
- general environment reconstruction;
- source-build execution;
- broad matrix/reusable-workflow Target support;
- maintainer-action permission based on this mechanism.

---

## 19. Fast relearning route

When returning later:

~~~text
1. Recall:
   published wheel loss != target applicability.

2. Open:
   src/upgradepilot/impact/artifact_serviceability.py

3. Trace:
   build_artifact_serviceability_impact_candidate(...)
   → removed/added tag sets
   → candidate.

4. Trace:
   evaluate_artifact_serviceability_impact(...)
   → target evidence
   → old intersection
   → proposed intersection
   → applicability.

5. Inspect:
   tests/test_artifact_serviceability.py
   - missing target witness
   - applicable exact target
   - alternate proposed compatible tag
   - target identity mismatch.

6. Open:
   src/upgradepilot/target/artifact_environment.py
   and explain why exact_wheel_compatibility_state stays unresolved.

7. Open:
   src/upgradepilot/investigation.py
   and verify the current normal ordering:
   candidate → unresolved impact evaluation;
   partial Target composition separately.

8. Inspect the multi-job investigation test and explain:
   job-selection specificity can improve Target context
   but does not itself create exact wheel tags.
~~~

---

## 20. Ownership and transfer questions

Without looking at this note, explain:

1. Why does old_tags - proposed_tags establish a candidate but not target applicability?
2. Why does applicability compare the target against complete old/proposed tag inventories instead of only removed_wheel_tags?
3. What does an sdist preserve, and what does it not prove?
4. Why is ubuntu-22.04 + Python 3.9 not equivalent to an exact supported wheel-tag set?
5. Why must TargetWheelCompatibilityEvidence.repository/revision match the candidate?
6. What is the difference between TargetArtifactEnvironmentEvidence and TargetWheelCompatibilityEvidence?
7. Why can fixing multi-job Target selection still leave artifact applicability unresolved?
8. Why is None from candidate construction different from an evidence problem?
9. Why is it useful that an unrelated upstream-source failure does not erase an already established artifact candidate?
10. If a future producer uses a target-side command to emit supported tags, what provenance would need to be preserved before the impact evaluator could trust it?

### Transfer exercise

Suppose:

~~~text
old release tags:
  cp311-cp311-manylinux_2_17_x86_64

proposed release tags:
  cp311-abi3-manylinux_2_17_x86_64

exact target tags:
  both of the above
~~~

The old exact tag disappeared, but the proposed abi3 wheel still intersects the target-supported set.

Predict the correct applicability state and explain why merely checking the removed-tag set would produce the wrong conclusion.

---

## 21. Evidence anchors

Current source/test horizon:

~~~text
main@57a2bcda54f7cbe4e7e8c47f0fb6a92bc51aba4a
~~~

Primary current source:

~~~text
src/upgradepilot/impact/artifact_serviceability.py
src/upgradepilot/pypi/release.py
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/investigation.py
~~~

Focused/current tests:

~~~text
tests/test_artifact_serviceability.py
tests/test_target_artifact_environment.py
tests/test_investigation.py
~~~

Directly relevant engineering history:

~~~text
working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md
working-memory/2026-09-07_2149_target-artifact-environment-composition.md
working-memory/2026-09-08_artifact-serviceability-integration-proof.md
working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md
~~~

Current critical review:

~~~text
audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md
~~~

Representative product pressure:

~~~text
product-simulation/S008_POST_CASE_SYNTHESIS.md
~~~

This is a learning artifact, not a specification, live-state owner, or implementation authorization.

UP-SKILL:upgradepilot-learning-artifact
