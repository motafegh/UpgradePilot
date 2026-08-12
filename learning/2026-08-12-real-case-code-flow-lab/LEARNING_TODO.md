# UpgradePilot Learning TODO

**Purpose:** Small operational checklist for the real-case code-flow learning journey.  
**Branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial source baseline:** `main@7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Broad method/guardrails:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)

This file answers three practical questions:

1. **What have we actually covered?**
2. **What are we learning now?**
3. **What is the next proper learning step?**

It is intentionally much smaller and more operational than `LEARNING_PLAN.md`.

---

## Status convention

- `[x]` — covered to the completion condition written for that item.
- `[ ]` — not yet completed.
- `▶ CURRENT` — the next learning item we should actively work on.
- `NEXT` — likely immediate continuation after the current item.
- `WAIT FOR MAIN` — useful future learning work whose implementation is not yet present or not yet mature enough on `main`.

A checkbox is not marked merely because a file was opened or an explanation was read. Mark it when we can trace/explain the stated responsibility at the required depth and any named exercise has been completed.

---

# 0. Learning workspace setup

- [x] Create dedicated learning branch from current `main`.
- [x] Create dedicated workspace under `learning/2026-08-12-real-case-code-flow-lab/`.
- [x] Write broad learning method and branch operating plan in `LEARNING_PLAN.md`.
- [x] Create this operational TODO/checklist.

**Checkpoint:** learning work is isolated from production implementation and has an explicit method + trackable next-action list.

---

# 1. Current-system orientation

## 1.1 Runtime map — `▶ CURRENT`

- [ ] Identify the main runtime entry/orchestration function used for a public PR investigation.
- [ ] Identify the major responsibility-oriented packages currently involved in the B2 flow.
- [ ] Draw a compact map of how these areas connect without trying to learn every file:
  - GitHub/public PR acquisition;
  - dependency-change analysis;
  - CI evidence;
  - PyPI/package/upstream evidence;
  - target evidence;
  - impact candidate formulation;
  - applicability reasoning;
  - investigation selection/feedback.
- [ ] Explain which layer owns **orchestration** versus which modules own domain-specific reasoning.
- [ ] Explain why this map is navigation context rather than an architectural claim that every future mechanism must use exactly the same shape.

**Completion condition:** Ali can point to the current orchestration entry point and verbally navigate from public PR input to the two implemented impact mechanisms without needing to memorize individual lines.

**Artifact:** only create a compact runtime map if it materially improves recall.

---

## 1.2 Core object/contract orientation — `NEXT`

- [ ] Identify the important domain/evidence objects encountered before impact reasoning begins.
- [ ] For each important object, state:
  - who creates it;
  - what facts it is allowed to claim;
  - what provenance/identity it preserves;
  - who consumes it next.
- [ ] Distinguish a successful evidence/domain object from an explicit problem/unresolved state.
- [ ] Explain why raw external data is not automatically trusted product evidence.

**Completion condition:** Ali can explain the difference between external payload/data, normalized evidence, interpretation, and later reasoning state using one current source example.

---

# 2. Real PR → exact dependency transition

Use one suitable product-simulation case only as a source of realistic concrete values. We are learning current UpgradePilot code, not studying the case itself.

## 2.1 Public PR identity

- [ ] Start with a concrete repository + PR number.
- [ ] Trace the call that acquires PR identity.
- [ ] Inspect the relevant `PullRequestIdentity` fields.
- [ ] Explain base revision vs head revision and why exact revision identity matters.
- [ ] Identify what evidence/provenance is preserved at this step.

**Completion condition:** Given a PR locator, Ali can explain what exact identity UpgradePilot must establish before reasoning about changed code/evidence.

---

## 2.2 Changed-file evidence

- [ ] Trace how changed files are acquired for the exact PR.
- [ ] Identify the input/output objects and important guards.
- [ ] Explain why changed-file presence is an observation, not yet a dependency-change conclusion.
- [ ] Inspect at least one relevant test covering this boundary.

**Completion condition:** Ali can distinguish “GitHub reports these changed files” from “UpgradePilot has established dependency X changed from A to B.”

---

## 2.3 Dependency-change analysis

- [ ] Trace `analyze_dependency_change(...)` from changed-file evidence into dependency reasoning.
- [ ] Identify how a `DependencyVersionChange` is formed.
- [ ] Follow concrete old version → proposed version values through the object.
- [ ] Identify explicit non-success/problem states around this analysis.
- [ ] Read the nearest tests together with the source.
- [ ] Explain why exact dependency/version identity becomes a shared input to later CI/upstream/impact reasoning.

**Completion condition:** Ali can trace a concrete PR from locator to `DependencyVersionChange` and explain every ownership boundary on that path.

**Ownership exercise:** predict one input variation that should *not* produce a valid `DependencyVersionChange`, then verify against source/test behavior.

---

# 3. Dependency transition → evidence branches

## 3.1 Exact-head CI evidence

- [ ] Trace the CI acquisition branch from `DependencyVersionChange`/PR identity.
- [ ] Identify workflow runs, jobs, and workflow-definition evidence used by current code.
- [ ] Explain **exact-head authority**: why CI from some other revision is not interchangeable with CI for the investigated head.
- [ ] Trace `evaluate_dependency_ci_exercise(...)` at a conceptual + source level.
- [ ] Distinguish “CI exists/passed” from “CI exercised the dependency-relevant proposition.”
- [ ] Inspect nearest CI-evidence tests.

**Completion condition:** Ali can explain what current CI evidence does and does not establish for an UpgradePilot dependency investigation.

---

## 3.2 PyPI release evidence

- [ ] Trace `PackageReleaseEvidence` acquisition through the PyPI client.
- [ ] Inspect `DistributionFile` and the important preserved fields.
- [ ] Explain package identity normalization vs requested/published version identity.
- [ ] Explain why distribution filename, package type, URL, and SHA256 are evidence data rather than incidental strings.
- [ ] Identify important explicit PyPI evidence problems/validation guards.
- [ ] Inspect nearest PyPI release tests.

**Completion condition:** Ali can explain how an external PyPI response becomes bounded UpgradePilot release evidence and where identity validation occurs.

---

## 3.3 Upstream release/changelog evidence

- [ ] Trace current upstream repository/release interval handling used by the Python-support mechanism.
- [ ] Understand crossed-release / proposed-tag / changelog acquisition at the level required by current code.
- [ ] Identify what exact upstream evidence is required before a Python-support-drop claim can be grounded.
- [ ] Separate changelog text from the semantic claim UpgradePilot derives from it.

**Completion condition:** Ali can explain the path from exact dependency transition to grounded upstream support-change evidence without treating upstream prose as automatically authoritative interpretation.

---

# 4. Mechanism 1 — Python-support impact/applicability/investigation loop

This is the first complete implemented reasoning loop and therefore a major learning checkpoint.

## 4.1 Grounded Python-support-drop claim

- [ ] Trace the evaluator that converts bounded upstream evidence into a `GroundedPythonSupportDropClaim`.
- [ ] Inspect the concrete fields/provenance it preserves.
- [ ] Explain why a grounded upstream support drop is still **not** the same thing as target applicability.

**Completion condition:** Ali can state exactly what the claim establishes and what remains unknown about the target repository.

---

## 4.2 Build `PythonSupportDropImpactCandidate`

- [ ] Trace `build_python_support_drop_impact_candidate(...)`.
- [ ] Identify candidate identity, mechanism status, exposure/activation state, and possible consequence.
- [ ] Explain **impact candidate** in practical UpgradePilot terms.
- [ ] Explain why candidate formulation does not manufacture exposure/activation/consequence truth.

**Completion condition:** Ali can explain why UpgradePilot creates a candidate before it knows whether the target is actually affected.

---

## 4.3 Generic applicability composition

- [ ] Read `PropositionAssessment`.
- [ ] Read `ApplicabilityPathAssessment`.
- [ ] Read `CandidateApplicabilityAssessment`.
- [ ] Learn proposition states:
  - established;
  - refuted;
  - unresolved;
  - conflicted.
- [ ] Learn evidence coverage states:
  - sufficient;
  - insufficient;
  - unresolved.
- [ ] Trace `evaluate_applicability_path(...)` for a conjunctive path.
- [ ] Trace `evaluate_candidate_applicability(...)` across paths.
- [ ] Distinguish evidence coverage from path-model coverage.
- [ ] Explain why “all known paths refuted” only establishes non-applicability when path-model coverage is sufficient.
- [ ] Work through at least three hand-computed proposition/path examples before checking code output.

**Completion condition:** Ali can independently compute the expected path/candidate state for simple proposition combinations and explain the role of coverage.

---

## 4.4 Pre-investigation Python applicability

- [ ] Trace `evaluate_python_support_drop_impact(candidate)` before target evidence exists.
- [ ] Identify which propositions are established from upstream evidence.
- [ ] Identify which target propositions remain unresolved.
- [ ] Explain why missing target evidence is **not negative evidence**.
- [ ] Explain why the candidate remains unresolved rather than applicable/not-applicable.

**Completion condition:** Ali can predict the pre-investigation applicability state and justify it proposition by proposition.

---

## 4.5 Discriminating investigation selection

- [ ] Trace `select_python_support_drop_investigation(...)`.
- [ ] Identify the exact unresolved proposition it is trying to discriminate.
- [ ] Understand the selected target repository, exact revision, path, and reason.
- [ ] Explain **discriminating investigation**: acquire evidence because it can change a material unresolved state.
- [ ] Explain the no-blind-repeat behavior.
- [ ] Use an S006/S007-style contrast only to test the mental model of “investigate vs stop/prune.”

**Completion condition:** Ali can explain why `pyproject.toml` is selected in the current unresolved state and when the same acquisition should not be selected again.

---

## 4.6 Exact target Python declaration

- [ ] Trace exact-head repository-file acquisition for `pyproject.toml`.
- [ ] Trace `interpret_target_python_declaration(...)`.
- [ ] Understand `[project].requires-python` parsing.
- [ ] Inspect explicit problems:
  - file unavailable;
  - malformed TOML;
  - project table absent;
  - `requires-python` absent;
  - invalid specifier.
- [ ] Explain why a problem state is preserved rather than coerced into “target unaffected.”

**Completion condition:** Ali can trace target-file evidence into either `TargetPythonDeclaration` or an explicit unresolved/problem state.

---

## 4.7 Target relevance + reevaluation

- [ ] Trace `evaluate_target_python_relevance(...)`.
- [ ] Understand the current relevance states:
  - declared Python overlap;
  - outside declared Python range;
  - target declaration unresolved;
  - upstream claim unresolved;
  - comparison unsupported.
- [ ] Explain why target Python relevance is narrower than compatibility/safety/final merge recommendation.
- [ ] Feed relevance back into `evaluate_python_support_drop_impact(...)`.
- [ ] Trace pre-investigation → selected investigation → observation → post-investigation result in `PublicPullRequestInvestigation`.
- [ ] Explain why pre, selection, and post states are preserved separately.

**Completion condition:** Ali can trace the first mechanism end-to-end and explain each state transition without collapsing observation, applicability, and final maintainer action.

**Ownership exercise:** given a changed target `requires-python` declaration, predict whether applicability becomes established, refuted, or remains unresolved before inspecting the evaluator result.

---

# 5. Mechanism 2 — Artifact serviceability Increment 1

## 5.1 Packaging vocabulary needed by current code

- [ ] Learn **wheel** at the depth needed here.
- [ ] Learn **sdist — source distribution** at the depth needed here.
- [ ] Learn wheel compatibility tag components:
  - Python interpreter tag;
  - ABI — Application Binary Interface tag;
  - platform tag.
- [ ] Understand `packaging.tags.Tag` as used by current code.
- [ ] Understand compressed wheel tag components enough to read the real test fixture.
- [ ] Explicitly defer broader Python packaging internals not needed for current responsibility.

**Completion condition:** Ali can read a representative wheel filename and explain what compatibility dimensions its tags encode.

---

## 5.2 Parse exact old/proposed release inventories

- [ ] Trace `build_artifact_serviceability_impact_candidate(...)` or current equivalent entry.
- [ ] Follow exact old and proposed `PackageReleaseEvidence` into the mechanism.
- [ ] Trace `parse_wheel_filename(...)`.
- [ ] Understand package/version identity validation against release evidence.
- [ ] Understand `PublishedWheelArtifact` and its `frozenset[Tag]`.
- [ ] Understand explicit problems:
  - wheel filename uninterpretable;
  - wheel identity mismatch.

**Completion condition:** Ali can explain how a PyPI distribution filename becomes validated compatibility-tag evidence rather than merely a parsed filename.

---

## 5.3 Compare artifact tag sets

- [ ] Trace old tag set − proposed tag set → removed tags.
- [ ] Trace proposed tag set − old tag set → added tags.
- [ ] Understand old/proposed sdist-presence flags.
- [ ] Explain why unchanged tag sets return no artifact-serviceability candidate.
- [ ] Walk the current main test fixture by hand before checking assertions.

**Completion condition:** Ali can manually derive the removed/added `Tag` sets from a simple old/proposed release inventory.

---

## 5.4 Artifact-serviceability candidate semantics

- [ ] Inspect `ArtifactServiceabilityImpactCandidate` fields/statuses.
- [ ] Explain why this candidate is **target-agnostic** in Increment 1.
- [ ] Explain these guards precisely:

  `removed published wheel tag != exact target loses a compatible wheel`

  `proposed sdist exists != source fallback succeeds`

- [ ] Separate:
  - package/interpreter metadata admissibility;
  - binary artifact availability;
  - source fallback availability;
  - source-build success;
  - application/runtime success.
- [ ] Use the S008 facts only as a concrete real-world example of these distinctions.

**Completion condition:** Ali can explain exactly what Increment 1 establishes and why target applicability is deliberately still pending.

---

## 5.5 Learn from the wheel-ordering failure/correction

- [ ] Reconstruct the failing test condition around the compressed platform tag.
- [ ] Understand what `validate_order=True` was checking.
- [ ] Explain why canonical formatting/order lint was stricter than UpgradePilot's owned evidence-admission responsibility.
- [ ] Explain why normal `parse_wheel_filename()` parsing is the corrected boundary.
- [ ] Inspect how the unchanged failing test became regression evidence after the correction.
- [ ] State the general engineering lesson: validation strictness must match the responsibility being owned, not an unrelated stronger property.

**Completion condition:** Ali can explain the bug, the incorrect mental model behind it, and why the fix is principled rather than merely “make the test pass.”

---

# 6. Cross-mechanism architecture checkpoint

Complete only after Sections 4 and 5 are understood from actual code.

- [ ] Compare Python-support and artifact-serviceability candidate structures.
- [ ] Identify genuinely shared applicability concepts.
- [ ] Identify mechanism-specific evidence and semantics that should remain separate.
- [ ] Compare lifecycle shape:

  `current state → justified investigation/stop → observation → reevaluation`

- [ ] Explain why this lifecycle may be reusable without prematurely creating a universal planner/type hierarchy.
- [ ] Inspect `PublicPullRequestInvestigation` field-per-mechanism pressure.
- [ ] Explain **evidence-earned abstraction** with these two concrete mechanisms.
- [ ] Identify at least one abstraction that current evidence supports and one that would still be premature.

**Completion condition:** Ali can argue for/against a proposed shared abstraction using actual responsibilities from both mechanisms rather than aesthetics or duplication alone.

**Ownership exercise:** review one hypothetical “generic impact engine” proposal and identify which current distinctions it risks erasing.

---

# 7. Artifact Serviceability Increment 2 — `WAIT FOR MAIN`

Do not fabricate this implementation in the learning branch. When `main` implements it, sync first and then expand these tasks against actual source/tests.

Expected responsibility to learn:

`exact target artifact-environment evidence → establish/refute/leave unresolved whether the target had an old compatible wheel path absent in the proposed release`

Provisional checklist to refine after implementation lands:

- [ ] Sync learning branch with the relevant `main` commit(s).
- [ ] Identify the admitted target-environment evidence source(s).
- [ ] Understand why local UpgradePilot `sys_tags()` must not proxy a remote target environment.
- [ ] Trace target environment evidence into propositions.
- [ ] Trace artifact-serviceability candidate applicability.
- [ ] Inspect investigation/stop behavior if present.
- [ ] Compare the completed artifact loop with the Python-support loop.

---

# 8. Later B2 convergence — `WAIT FOR MAIN`

Add/expand concrete tasks only when these responsibilities are implemented enough to learn from real code:

- [ ] cross-candidate technical synthesis;
- [ ] repository/context synthesis;
- [ ] overall evidence sufficiency;
- [ ] residual uncertainty;
- [ ] maintainer-facing recommendation / abstention;
- [ ] traceable output;
- [ ] rerun/replay behavior where applicable.

**Guard:** do not convert the mature-system horizon into a syllabus before implementation gives us concrete ownership boundaries.

---

# Recurring branch-sync TODO

Run this check before beginning a new major section or whenever parallel implementation has materially advanced.

- [ ] Check latest `main` commit and `MEMORY.md`.
- [ ] Compare `main` with `learning/real-case-code-flows-2026-08-12`.
- [ ] Determine whether changes affect the learning section we are about to study.
- [ ] If material, sync `main` into the learning branch before continuing.
- [ ] Re-read only changed responsibility/source/tests needed for the next learning task.
- [ ] Update this TODO if implementation materially adds/removes/reorders a learning responsibility.

These recurring items are reset as needed; they are operational checks rather than one-time mastery items.

---

# Current position

**Current learning task:** `1.1 Runtime map`.

**Immediate sequence:**

```text
1.1 Runtime map
→ 1.2 core object/contract orientation
→ 2.1 public PR identity
→ 2.2 changed-file evidence
→ 2.3 DependencyVersionChange
```

Do not skip ahead merely because later mechanisms are more interesting. The first trace should establish enough end-to-end navigation and object ownership that later impact/applicability code has concrete inputs and context.

---

# Updating this checklist

During learning:

1. check an item only after its completion condition is actually met;
2. add a short sub-item if an unexpected concept/failure becomes necessary;
3. do not expand the checklist with speculative future architecture;
4. when `main` materially evolves, revise upcoming unchecked items to match current implementation;
5. preserve already completed learning truth unless later work reveals it was factually wrong—in that case record the correction rather than silently pretending the earlier understanding was correct;
6. periodically create a focused learning artifact only when the understanding is worth preserving beyond this checklist.
