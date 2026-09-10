# Overall Evidence Sufficiency and Maintainer Action Synthesis — Research and Design-Support Investigation

**Recorded:** 2026-09-10  
**Status:** Exploratory, non-controlling research/design-support proposal. No synthesis semantics, action mappings, implementation method, specification change, or project-state change are accepted by this document.  
**Inspection snapshot:** `main` at `c4c08eaed1b036b55667fb318a3ec4236e647c11` (`docs: preserve first synthesis LbD findings`).  
**Authority:** [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md), [`MEMORY.md`](../MEMORY.md), the selected synthesis plan, accepted specifications, source/tests, and the normal repository ownership hierarchy remain controlling in their respective responsibilities.  
**Requested role:** adversarial second perspective for later review, learning, and design decisions by Ali.  
**Mutation boundary:** creation of this proposal only. No source, tests, specifications, plans, working memory, `MEMORY.md`, or other repository owner was changed.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-repository-audit`

---

## 1. Executive conclusion

The current repository has earned the synthesis responsibility, but it has **not yet earned a simple state-to-action lookup table**.

The strongest design conclusion from this investigation is:

```text
heterogeneous evidence/result state
!= one severity value
!= one enum-to-action mapping
```

A credible first synthesis method should instead evaluate a small set of transparent constraints over decision-bearing semantic state and then return:

```text
one primary Charter-facing action or abstention
+
traceable decisive reasons
+
material residual uncertainty/conflict
+
zero or more required checks
+
explicit rerun/future-condition trigger when justified
+
claim limits
```

This is still a **proposal**, not accepted project truth.

Several current findings materially constrain the design:

1. `merge after normal review` is best pressure-tested as **“no additional UpgradePilot-specific escalation is justified; return the PR to ordinary maintainer review”**, not as UpgradePilot making the final merge decision. The Charter label remains controlling and is not changed here.
2. Sufficiency is **action-relative**. Evidence can be sufficient to justify a block or a targeted check while remaining insufficient for the favorable outcome.
3. `run targeted checks` is justified by a concrete unresolved proposition plus a concrete discriminating maintainer operation, not by uncertainty in general.
4. `investigate` and `block` are operationally distinct enough that an internal/sub-disposition distinction deserves explicit pressure testing. A block can coexist with a required targeted check.
5. `defer` needs an explicit future/pending condition and rerun trigger. Current `acquisition_failed`, `no_successful_ci`, or generic missing-evidence states do not by themselves establish that semantics.
6. `abstain` should mean lack of sufficient UpgradePilot authority/method/boundary for a more specific action, not “anything went wrong.” Some current exceptions prevent synthesis from being reached at all and are operational failures, not automatically semantic abstentions.
7. A mechanism-local negative result is not global negative evidence. A complete artifact comparison with no candidate, a Python-support non-applicability result, green CI, or no model-extracted claim cannot independently authorize the favorable action.
8. The normal application result is a heterogeneous orchestration envelope, not a stable normalized synthesis input. Synthesis needs a deliberate semantic projection that preserves proof strength, authority, reliability, coverage, reachability, and finality without letting every non-`None` field become an action vote.
9. Current correctness findings create real action-permission restrictions. Synthesis cannot repair lost PR revision identity, mixed workflow-attempt identity, or command-text interpretation after those producers have already manufactured stronger-looking typed evidence.
10. Some important states reveal possible missing upstream investigation responsibilities. The strongest current examples are exact target wheel compatibility, candidate-discovery/coverage adequacy for favorable action, and possibly a pending/future-condition projection if `defer` is to be emitted. These do **not** automatically justify implementation or scope expansion.

A conservative first implementation could therefore reasonably withhold at least `merge after normal review` until its positive coverage/integrity requirements are accepted. This investigation also finds a credible reason to withhold `defer` unless a real pending/future-condition input becomes available. That is a design recommendation for review, not an implementation decision.

---

## 2. Method, scope, and inspected evidence

This investigation followed the repository's read-only Planning/Design and evaluative-review boundaries. It started from:

- [`AGENTS.md`](../AGENTS.md)
- [`MEMORY.md`](../MEMORY.md)
- [`OPERATING_GUIDE.md`](../OPERATING_GUIDE.md)
- [Planning/Design Skill](../.agents/skills/upgradepilot-planning-design/SKILL.md)
- [Learning-by-Doing Skill](../.agents/skills/upgradepilot-learning-by-doing/SKILL.md)
- [Repository Audit Skill](../.agents/skills/upgradepilot-repository-audit/SKILL.md)

The main controlling/supporting owners inspected include:

- [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)
- [`plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)
- [`working-memory/2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md`](../working-memory/2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md)
- [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)
- [`docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [`docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- [`plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)
- [`working-memory/2026-09-08_system-limitations-and-correctness-investigation.md`](../working-memory/2026-09-08_system-limitations-and-correctness-investigation.md)
- [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)
- [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- [`plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)
- [`working-memory/2026-09-08_artifact-serviceability-integration-proof.md`](../working-memory/2026-09-08_artifact-serviceability-integration-proof.md)
- historical/non-controlling [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- accepted [`docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)
- accepted [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)
- historical/non-controlling [`audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`](../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md)
- [`product-simulation/CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md`](../product-simulation/CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md)
- [`product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md)
- supporting exploratory [`proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md`](2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md)

Current source/tests inspected include at least:

- [`src/upgradepilot/investigation.py`](../src/upgradepilot/investigation.py)
- [`src/upgradepilot/cli.py`](../src/upgradepilot/cli.py)
- [`src/upgradepilot/dependency/change.py`](../src/upgradepilot/dependency/change.py)
- [`src/upgradepilot/dependency/direct_install.py`](../src/upgradepilot/dependency/direct_install.py)
- [`src/upgradepilot/ci/dependency_exercise.py`](../src/upgradepilot/ci/dependency_exercise.py)
- [`src/upgradepilot/github/actions.py`](../src/upgradepilot/github/actions.py)
- [`src/upgradepilot/github/pull_request.py`](../src/upgradepilot/github/pull_request.py)
- [`src/upgradepilot/pypi/release.py`](../src/upgradepilot/pypi/release.py)
- [`src/upgradepilot/upstream/claim.py`](../src/upgradepilot/upstream/claim.py)
- [`src/upgradepilot/upstream/repository.py`](../src/upgradepilot/upstream/repository.py)
- [`src/upgradepilot/target/python.py`](../src/upgradepilot/target/python.py)
- [`src/upgradepilot/target/relevance.py`](../src/upgradepilot/target/relevance.py)
- [`src/upgradepilot/target/artifact_environment.py`](../src/upgradepilot/target/artifact_environment.py)
- [`src/upgradepilot/impact/applicability.py`](../src/upgradepilot/impact/applicability.py)
- [`src/upgradepilot/impact/python_support.py`](../src/upgradepilot/impact/python_support.py)
- [`src/upgradepilot/impact/artifact_serviceability.py`](../src/upgradepilot/impact/artifact_serviceability.py)
- [`tests/test_investigation.py`](../tests/test_investigation.py)
- [`tests/test_ci_dependency_coverage.py`](../tests/test_ci_dependency_coverage.py)
- [`tests/test_python_support_impact.py`](../tests/test_python_support_impact.py)
- [`tests/test_python_line_specifier_method.py`](../tests/test_python_line_specifier_method.py)
- [`tests/test_artifact_serviceability.py`](../tests/test_artifact_serviceability.py)
- [`tests/test_target_artifact_environment.py`](../tests/test_target_artifact_environment.py)
- [`tests/test_direct_install_declaration.py`](../tests/test_direct_install_declaration.py)
- [`tests/test_pypi_client.py`](../tests/test_pypi_client.py)

This was source/document inspection rather than a new execution campaign. Existing executable findings are cited to their owning source/tests/working-memory records. This report does not claim that inspecting test text is equivalent to rerunning those tests, nor that synthetic reproduced failures establish public-case prevalence.

---

# Part I — Repository-grounded observations

## 3. The real current synthesis boundary is heterogeneous and only partly normalized

### 3.1 `PublicPullRequestInvestigation` is an orchestration result, not yet a synthesis contract

[`src/upgradepilot/investigation.py`](../src/upgradepilot/investigation.py) currently returns `PublicPullRequestInvestigation` with a mixture of:

```text
PR identity + changed files
canonical dependency result
raw-ish workflow run/job evidence
CI aggregate/per-workflow evidence
package and upstream evidence/problems
release/tag/changelog intermediate evidence
model/grounding-derived upstream support result
Python-support candidate / target investigation / applicability
old package evidence
artifact candidate
Target artifact-environment associations
artifact applicability
```

This is valuable application state, but the fields are not all equivalent decision facts. Some are authoritative observations, some are intermediate inputs, some are method outputs, some are problems, and some are mechanism-level conclusions.

**Repository-grounded observation:** there is no current top-level synthesis result, and [`src/upgradepilot/cli.py`](../src/upgradepilot/cli.py) deliberately renders typed evidence without manufacturing one.

**Design consequence:** the eventual synthesis should not treat the current application dataclass as an unstructured bag where every field can independently vote for an action. A smaller semantic projection is likely needed.

### 3.2 Current producer reachability matters

There are at least three materially different “input exists” situations:

```text
A. a typed result is normally returned in PublicPullRequestInvestigation
B. a domain type/result exists and can be tested, but normal application composition does not yet produce it
C. an exception prevents PublicPullRequestInvestigation from being returned at all
```

Examples:

- CI/package/mechanism problem states are often normal typed results.
- `TargetWheelCompatibilityEvidence` exists and can drive artifact applicability in mechanism tests, but the current public application path deliberately does not manufacture exact target wheel-tag compatibility from static Target facts.
- some GitHub acquisition/response failures are caught in the CLI before any application result reaches a future synthesis layer.

A synthesis design that ignores these reachability differences would advertise actions that the real producer cannot actually construct.

---

## 4. Reconstructed synthesis input space: decision states and proof strength

The table below is descriptive of current evidence, not a proposed runtime schema.

| Evidence family | Meaningful current state / proof strength | What it can establish | What it cannot establish | Synthesis pressure |
|---|---|---|---|---|
| PR/dependency identity | `PullRequestIdentity` + trusted `DependencyVersionChange` | bounded repository/PR/base/head identity and canonical package/version transition under current producer | dependency directness, usage, impact, safety, correct changed-file snapshot correspondence under the known mismatch defect | foundational admissibility and identity integrity must be explicit |
| Dependency problems | unsupported/missing/incomplete/malformed/ambiguous/multiple/conflicting/version-unchanged and representation-specific problems | why a trusted canonical transition was not established | a guessed transition or a generic “temporary” condition | foundational unsupported/invalid/conflict should not be mass-mapped to one action |
| CI aggregate | `supported_not_correlated` | at least one successful exact-head runtime run/job plus supported static changed-dependency consumption | matched static step runtime execution/success, exact changed version exercised, broad compatibility/safety | useful authority/context; not favorable proof by itself |
| CI aggregate | `no_successful_ci` | no completed successful exact-head job was found by the current evaluator | whether CI is genuinely absent, still pending, merely failed, or should be retried | cannot independently justify `defer`; pending semantics are missing |
| CI aggregate | `unresolved` | successful exact-head CI exists but admitted static evidence cannot establish required dependency consumption, or another bounded authority condition failed | negative dependency exercise or safety | may support a concrete check/investigation only after the unresolved proposition is identified |
| CI per-workflow static axes | consumption/direct exercise `supported`, `not_established`, `unresolved` | bounded static declaration/order facts | runtime step correlation and success | supports reasons/checks; should not be collapsed into one risk number |
| Exact PyPI release | `PackageReleaseEvidence` | exact package/version publication identity and bounded distribution metadata | target compatibility, runtime installability, update safety | authoritative package evidence for mechanism builders |
| PyPI release problems | `version_not_found`, `identity_mismatch`, `malformed_response`, `package_not_found_or_inaccessible`, `acquisition_failed` | materially different acquisition/identity failure meanings | one generic “missing” meaning; `acquisition_failed` does not prove a temporary/pending state | action mapping must preserve problem class and reachability |
| Upstream/repository evidence | available or explicit missing/unsupported/invalid/unavailable result classes | bounded source/repository authority inputs | semantic impact by itself | source authority and semantic interpretation must remain separate |
| Model-derived support interpretation | model proposal -> deterministic grounding -> `GroundedPythonSupportDropClaim` or problem/no accepted claim | attributed grounded semantic premise suitable for impact-candidate formation under accepted authority rules | independent truth, exhaustive absence of impact, permission for a less-cautious action from no returned claim | origin/authority/corroboration must survive synthesis projection |
| Python-support candidate | mechanism established, exposure/activation to evaluate | a bounded support-drop mechanism candidate exists | target applicability | candidate existence alone must not block or permit favorable action |
| Python-support applicability | `established_applicable` | represented necessary propositions establish target applicability for this bounded candidate | severity/materiality of the final maintainer action, global impact completeness | strong constraint, but action still depends on consequence/context/other evidence |
| Python-support applicability | `established_not_applicable` with sufficient path-model coverage | this bounded candidate is not applicable to the target under represented path semantics | no other technical mechanism exists | mechanism-local negative only |
| Python-support applicability | `unresolved` because target evidence missing/problem | decision-critical target proposition lacks sufficient evidence | negative applicability | often a candidate for a concrete check if the missing proposition is discriminable |
| Python-support applicability | `unresolved` because comparison method unsupported while target evidence exists | evidence exists but accepted method intentionally abstains on its semantics | that evidence is “missing” or that retry will fix it | method limitation requires different treatment from acquisition gap |
| Python investigation selection | concrete `acquire_exact_target_python_declaration` selection | UpgradePilot has an executable next evidence target under the current mechanism | permission to execute forever, maintainer-facing action | useful continuation signal only while valid |
| Python investigation selection | `None` after target acquisition/problem | selector has no next action under its current rule | that the candidate is resolved or that investigation has semantically “stopped” | `None` cannot be treated as resolution or sufficiency |
| Artifact candidate | `ArtifactServiceabilityImpactCandidate` | exact old/proposed publication comparison established a bounded published-wheel capability loss | exact target exposure, source-build failure, overall install failure | candidate-level concern only |
| Artifact builder negative | `None` after complete exact old/proposed comparison | no bounded published-wheel capability loss was observed by this mechanism | no other impact mechanism exists | local negative evidence only |
| Artifact builder problem | wheel filename/identity evidence problem | mechanism comparison could not be trusted/completed | absence of artifact concern | unresolved/invalid evidence, not negative evidence |
| Target artifact environment | available static runner/Python/install-declaration facts with limitations | bounded static repository configuration facts | runtime execution/success or exact target-supported wheel tags | context can guide investigation but not self-authorize compatibility |
| Target artifact environment | explicit file/workflow/ambiguity/unsupported problems | why static target extraction did not establish usable facts | target non-exposure | problem-specific uncertainty |
| Exact target wheel compatibility | domain evidence/problem types exist; real public application currently leaves exact compatibility unresolved | when separately supplied, can establish/refute bounded artifact applicability | source-build viability or all compatibility | strong candidate missing investigation responsibility, but not yet admitted acquisition path |
| Artifact applicability | currently normally unresolved on public path after candidate because exact compatibility is not established | preserves correct uncertainty | final maintainer consequence | key pressure case for targeted-check semantics |
| Applicability conflict | accepted generic `conflicted` semantics | decision-critical evidence/propositions disagree | which maintainer operation resolves it | may imply targeted check or broader investigation depending conflict shape |
| Candidate-discovery coverage | accepted conceptual responsibility, no current top-level adequate-coverage result | would bound how far mechanism-level negatives can support broader negative inference | universal ecosystem impact completeness unless explicitly justified | critical favorable-action gate remains open |
| Staleness/freshness | source timestamps/revisions exist in places; Core requires stale behavior where relevant | provenance/time facts where produced | one accepted universal staleness threshold or synthesis-ready stale classification | synthesis must not invent freshness policy |
| Operational acquisition exception | error exits before application result | that normal investigation could not construct required evidence/result | a semantic Charter action | requires outer failure-contract decision if it is ever to reach synthesis |

### 4.1 Five cross-cutting properties matter more than field count

Across these families, the decision-relevant distinctions repeatedly reduce to five questions:

```text
1. Admissibility / identity
   Is this an admitted case with a trustworthy canonical transition and exact identity?

2. Authority / integrity
   Is this evidence allowed to support the claim being considered, and is known provenance integrity intact?

3. Coverage / finality
   Is this a bounded negative, an established positive, an unresolved proposition,
   a conflict, or merely absence of a discovered candidate?

4. Continuation
   Is there a concrete UpgradePilot-executable next check, a maintainer-recommendable check,
   a known external future condition, or no justified continuation?

5. Reachability
   Can the normal current producer actually provide this state to synthesis,
   or does the run fail before synthesis exists?
```

These appear to be better synthesis axes than mirroring every source dataclass.

---

## 5. Repository-grounded reliability constraints

The separate correctness investigation has reproduced three input-integrity problems that matter directly to action permission. The owning record is [`working-memory/2026-09-08_system-limitations-and-correctness-investigation.md`](../working-memory/2026-09-08_system-limitations-and-correctness-investigation.md).

### 5.1 Changed-file patch / PR-revision correspondence

[`src/upgradepilot/github/pull_request.py`](../src/upgradepilot/github/pull_request.py) freezes PR base/head identity and reconciles changed-file count, but current changed-file records do not carry a head revision identity. The reproduced scenario shows the PR identity can be from head A while mutable changed-file patch data is later acquired from head B with the same count.

**Synthesis implication:** a valid `DependencyVersionChange` object is not sufficient, by type alone, to authorize a favorable action if its source identity chain is known to be vulnerable to this mismatch. Synthesis cannot reconstruct discarded revision correspondence.

### 5.2 Workflow run-attempt / job-attempt identity

[`src/upgradepilot/github/actions.py`](../src/upgradepilot/github/actions.py) preserves `WorkflowRun.run_attempt`, while `WorkflowJob` does not. Job acquisition uses `filter=latest` and validates run ID/head SHA, not attempt identity. The reproduced investigation demonstrates possible cross-attempt mixing.

**Synthesis implication:** current CI evidence may need an enforceable restriction or upstream repair before it can serve as a positive permission prerequisite. This does not erase independent package/upstream concerns that do not depend on the affected CI evidence.

### 5.3 Static command-text false positives

[`src/upgradepilot/dependency/direct_install.py`](../src/upgradepilot/dependency/direct_install.py) is intentionally bounded static declaration analysis, but the reproduced cases show some comments/quoted-data/separator combinations can become false-positive direct-install declarations and then influence CI and Target composition.

**Synthesis implication:** “typed static consumption supported” cannot be treated as immune to known producer defects. The smallest safe response is upstream repair, enforceable supported-input restriction, or withholding the affected permission—not a disclaimer inside the recommendation.

### 5.4 Reliability is action-relative too

A reliability defect need not force every possible result to become abstention. Example:

```text
independent grounded package/upstream evidence establishes a material concern
+
CI evidence is integrity-restricted
```

The CI evidence may be unusable for a favorable permission while the independent concern still supports a cautious action. Reliability should constrain the claims/actions that depend on the affected input, not globally erase unrelated evidence.

---

# Part II — Interpretations

## 6. Synthesis should compose semantic constraints, not mechanism votes

A mechanism result should contribute facts/constraints such as:

```text
bounded concern established
bounded candidate refuted/non-applicable
specific proposition unresolved
conflict exists
evidence authority restricted
concrete check exists
known future condition exists
```

It should not contribute an autonomous “vote” like `risk=7` or `action=block` unless that mechanism actually owns the maintainer decision, which current architecture intentionally does not.

This is especially important because the same technical state can support different maintainer operations depending on consequence and remaining discriminating evidence.

Example:

```text
artifact wheel-path loss established
+
proposed sdist exists
+
source-build viability unresolved
```

The artifact mechanism can establish the wheel-serviceability loss without establishing that the update is unusable. A precise source-build/install check may be more useful than an immediate block. Therefore:

```text
established_applicable
!= automatic investigate/block
```

### 6.1 Action-relative sufficiency is the most coherent current model

The active working memory already identifies this direction, and cross-mechanism pressure strengthens it:

```text
same evidence state
→ sufficient for targeted check
→ insufficient for ordinary-review favorable action
```

or:

```text
established concern
→ sufficient to withhold normal progression
→ still insufficient to explain exact root cause or remediation
```

A separate top-level `sufficient/insufficient` Boolean would therefore be misleading. A separate readiness/sufficiency enum should be added only if it encodes semantics not already represented by the selected action plus explicit reasons/limits.

### 6.2 Investigation stopping needs an explicit semantic projection

The accepted Product Decision Model already states that investigation stopping does not imply sufficiency. Current implementation adds another problem: selector absence is not a reliable stop reason.

[`tests/test_python_support_impact.py`](../tests/test_python_support_impact.py) demonstrates:

```text
target acquisition attempted
+
target evidence problem remains
+
applicability unresolved
+
select_python_support_drop_investigation(...) -> None
```

Therefore the synthesis layer must not interpret:

```text
selection is None
→ resolved
```

or even automatically:

```text
selection is None
→ no worthwhile investigation exists
```

A future decision-bearing projection may need to preserve why continuation ended, for example conceptually:

```text
resolved_no_further_check
unresolved_no_current_upgradepilot_check
upgradepilot_check_available
external_condition_pending
maintainer_check_available
```

These names are illustrative only; this report does not propose a source enum.

### 6.3 A bounded negative needs both local proof and claim scope

The product-simulation pressure around candidate-discovery coverage remains material.

```text
artifact comparison complete + no artifact candidate
```

is a strong negative **for that bounded artifact mechanism**.

Likewise:

```text
Python support candidate established_not_applicable
```

can be a strong negative **for that bounded candidate**.

Neither means:

```text
no UpgradePilot-relevant technical concern exists
```

unless the synthesis's broader claim has an accepted bounded discovery/coverage premise. This is the principal favorable-action difficulty.

---

# Part III — Proposed synthesis semantics

Everything in this part is a design proposal for review, not accepted semantics.

## 7. Proposed shape: one primary action plus orthogonal reasons/checks/limits

The simplest transparent structure that survived the pressure cases is:

```text
one primary Charter-facing action or abstention
+
optional internal sub-disposition where the Charter family is operationally broad
+
decisive reasons
+
residual uncertainty/conflict
+
required checks
+
rerun/future-condition trigger when justified
+
claim limits
+
evidence/provenance references
```

This is preferable to either:

```text
multiple equal actions
```

or:

```text
one universal action-precedence/severity ladder
```

because real states can be:

```text
block normal progression
AND
run this exact check before reassessment
```

The primary action answers **what the maintainer should do now**; secondary required checks/reasons explain how the state may be resolved.

## 8. `merge after normal review`

### Proposed operational meaning

Preserve the controlling Charter label, but interpret the product operation as:

```text
Within the explicitly admitted and trustworthy UpgradePilot investigation boundary,
no additional UpgradePilot-specific escalation is justified by the current evidence.
Return the pull request to the repository's ordinary maintainer review process.
```

This is consistent with the 2026-09-10 active working-memory finding and avoids implying that UpgradePilot itself owns the final merge decision.

### Proposed positive permission requirements

The favorable outcome should require **positive permission**, not merely absence of a detected problem. Candidate requirements to accept/reject explicitly are:

- admitted public Dependabot/Python dependency-transition identity is trustworthy;
- known input-integrity defects do not affect the evidence used for favorable permission, through proven repair or enforceable restriction;
- the set of synthesis-relevant mechanism/discovery responsibilities has an explicit bounded coverage statement adequate to the favorable claim;
- every material activated candidate is established not applicable/resolved, or its remaining uncertainty is explicitly non-decision-critical under an accepted rule;
- mechanism-local “no candidate” results are complete for their own bounded method;
- no decision-critical conflict remains;
- no required targeted check remains outstanding;
- any minimum CI/repository-context prerequisite selected for the favorable outcome is actually satisfied at its owned proof strength;
- model-derived absence is never used as standalone negative proof.

The exact coverage/CI/context prerequisites are unresolved project decisions. If they cannot be accepted now, the favorable action should remain unavailable.

### Evidence that should prohibit it

At minimum:

- established applicable material concern not otherwise resolved at the overall-action level;
- decision-critical unresolved/conflicted candidate;
- inadequate candidate-discovery/coverage basis for the claim being made;
- known integrity restriction on decision-critical evidence;
- outstanding required check;
- foundational unsupported/ambiguous/conflicting dependency identity;
- reliance on green CI, one non-applicable mechanism, no artifact candidate, or no model claim as the sole negative proof.

### Residual uncertainty that can coexist

Some residual uncertainty must remain because the Charter does not claim objective safety or universal mechanism exhaustion. The report can preserve:

```text
ordinary repository review requirements
out-of-scope mechanisms/technologies
explicitly bounded evidence blind spots that are not decision-critical under the accepted first method
```

However, a claim-limit sentence cannot convert **unknown decision-critical coverage** into acceptable residual uncertainty.

### Competing outcome

If one concrete unresolved proposition remains and a bounded check can discriminate it, `run targeted checks` is more informative. If UpgradePilot cannot establish an adequate favorable coverage boundary and no more specific action is justified, `abstain` may be the safer candidate.

### Counterexample

```text
artifact comparison finds no wheel-capability-loss candidate
+
Python support candidate is non-applicable
+
CI is green/supported_not_correlated
+
no accepted candidate-discovery coverage premise exists
```

A naïve “nothing bad found” rule emits the favorable action. That would overclaim because the mechanism-local negatives and green CI do not establish the broader negative claim.

---

## 9. `run targeted checks`

### Proposed operational meaning

```text
One or a small number of concrete decision-relevant propositions remain unresolved,
and a bounded maintainer-side check can materially discriminate the next action.
The check is a prerequisite or explicit decision aid, not generic advice to “test more.”
```

A “check” is broader than a test. It can be an evidence acquisition, exact compatibility determination, bounded build/install experiment, or other concrete observation if justified.

### Proposed positive permission requirements

- an exact unresolved proposition is named;
- that proposition materially affects the current overall action;
- a concrete check target is known;
- the check has a defensible relation to the proposition;
- prerequisites are known well enough that the recommendation is executable by a maintainer;
- the possible outcomes imply an explicit reassessment/rerun boundary;
- no independent established concern already makes “block” the more accurate primary current operation.

### Evidence that should prohibit it as the primary action

- broad/open-ended uncertainty with no concrete discriminating check;
- an explicitly pending external condition where the correct operation is to wait rather than perform a new check;
- unsupported/out-of-boundary state where UpgradePilot cannot responsibly prescribe the check;
- an independent established blocker that should determine the primary action, although the targeted check may remain secondary;
- a “check” that is merely optional information and would not change the action.

### Residual uncertainty that can coexist

Other non-decision-critical uncertainties may remain. The check itself may not resolve every mechanism; it only needs to discriminate the specific proposition controlling the current decision.

### Competing outcomes

- `investigate or block` when uncertainty is broad/conflicted or an established condition already warrants holding progression;
- `defer` when no maintainer check is needed now and a known external future condition is expected to resolve the evidence;
- `abstain` when no defensible check can be prescribed at the current method boundary.

### Counterexample

Current artifact pressure:

```text
published wheel capability loss established
+
exact target wheel compatibility unresolved
+
no stronger independent concern
```

A precise “establish exact target wheel compatibility” check is more informative than generic investigation, deferral, abstention, or a favorable action.

A second counterexample prevents overgeneralization:

```text
same artifact uncertainty
+
independent Python-support concern already established as materially blocking
```

Now the artifact compatibility check can remain required, but `run targeted checks` should not necessarily be the **primary** action because a separate reason already justifies withholding normal progression.

---

## 10. `investigate or block`

### Proposed operational meaning

This Charter family appears to contain two materially different maintainer operations.

Candidate internal distinction:

```text
investigate
→ material uncertainty/conflict warrants broader evidence gathering,
   and no single bounded targeted check is sufficient to resolve the decision.

block
→ current evidence is already sufficient to recommend that ordinary progression stop
   until a stated condition/evidence change occurs.
```

These can coexist in practice: investigation may happen while progression is blocked. The design question is which operation should be primary and how transparently that distinction must be encoded.

### Proposed positive permission for an `investigate` sub-disposition

- decision-critical unresolved/conflicted state exists;
- it cannot be reduced to one sufficiently discriminating targeted check;
- broader inquiry remains meaningful within the supported product/maintainer boundary;
- ordinary favorable progression would be too strong while that inquiry remains open.

### Proposed positive permission for a `block` sub-disposition

- evidence already establishes a material concern or integrity condition that makes ordinary progression too strong;
- the blocking proposition is independent of unresolved secondary details;
- the reason for lifting/reassessing the block can be stated.

### Evidence that should prohibit a blanket block

- candidate existence without target applicability;
- unresolved applicability when one simple concrete check can discriminate it and no independent blocker exists;
- mechanism applicability whose practical consequence remains materially open, such as a wheel-path loss where a viable source fallback may still resolve the maintainer concern under an accepted policy;
- a provider failure assumed to be risky without semantic evidence.

### Residual uncertainty that can coexist

A block can coexist with unresolved mechanism details because the evidence may already be sufficient for the cautious current operation. This is another reason sufficiency cannot mean “all questions answered.”

### Competing outcome

A concrete targeted check may coexist as a secondary required check. `defer` should not mask an established blocker merely because some other evidence is pending.

### Counterexample

```text
artifact candidate established
+
exact target compatibility unresolved
```

Blocking merely because the candidate exists would confuse mechanism generation with target applicability.

Another pressure case:

```text
artifact exact target wheel-path loss established
+
proposed sdist exists
+
source-build/install viability unresolved
```

This may still favor a targeted source-build check over an immediate block unless the accepted overall policy says the established prebuilt-wheel loss is independently material enough to block. The current repository does not yet settle that action-level materiality rule.

---

## 11. `defer`

### Proposed operational meaning

```text
The case remains inside the supported product boundary, but a named external/pending condition
must change before a more specific decision is useful. The product can state what condition
it is waiting for and when/why a rerun should occur.
```

`defer` should therefore be temporal/future-condition semantics, not a synonym for “uncertain.”

### Proposed positive permission requirements

- a decision-critical condition is explicitly known to be pending/temporarily unavailable;
- the condition is expected to change without a new broad maintainer investigation;
- a rerun trigger can be stated concretely, such as “when exact-head CI completes” or “after provider availability is restored,” **but only when the producer has evidence for that state**;
- no independent established blocker should determine a stronger/more informative primary action.

### Evidence that should prohibit it

- generic `acquisition_failed` without a retryability/pending contract;
- `no_successful_ci` alone;
- unsupported method semantics such as `===` Python comparison;
- invalid/malformed/conflicting evidence with no reason to believe time alone changes it;
- established concern that remains regardless of the pending evidence.

### Residual uncertainty that can coexist

The unresolved proposition can remain fully unresolved because the point of deferral is that the expected future condition is the appropriate next source of evidence.

### Competing outcome

- targeted check if a maintainer action can resolve the proposition now;
- investigate if broader inquiry is required;
- abstain if UpgradePilot lacks a defensible future-condition or action mapping.

### Counterexample

[`tests/test_pypi_client.py`](../tests/test_pypi_client.py) intentionally distinguishes timeout-driven `acquisition_failed` from missing/version/identity/malformed states. But `acquisition_failed` itself does not encode “known temporary and retry later.” Mapping every such result to `defer` would invent a temporal fact the producer does not currently supply.

Another counterexample is current CI: [`src/upgradepilot/ci/dependency_exercise.py`](../src/upgradepilot/ci/dependency_exercise.py) returns `no_successful_ci` when no completed-successful jobs are present. That can include very different runtime situations. The aggregate is not a trustworthy pending-state indicator.

---

## 12. `abstain`

### Proposed operational meaning

```text
UpgradePilot reached its semantic decision boundary but lacks enough supported authority,
method capability, or admissible evidence to select a more specific maintainer operation responsibly.
```

Abstention is a bounded product conclusion about UpgradePilot's authority, not a claim that the PR is safe/unsafe and not a generic catch-all exception handler.

### Proposed positive permission conditions

Candidate classes include:

- foundational input is outside the supported dependency-transition boundary;
- an accepted method intentionally does not support the semantics needed for the decision and no concrete maintainer check is justified;
- evidence integrity/authority is insufficient for any more specific action and cannot be safely narrowed through an accepted restriction;
- synthesis reaches a coherent state that does not map to another action under accepted first-version semantics.

### Evidence that should prohibit it

- a concrete discriminating maintainer check exists;
- a known external pending condition clearly supports deferral;
- an established blocker supports `investigate or block`;
- the run failed before synthesis could be constructed at all, unless the application contract is explicitly changed to normalize that failure into a semantic result.

### Residual uncertainty that can coexist

High uncertainty can coexist with abstention. The justified claim is only:

```text
UpgradePilot cannot responsibly select a stronger/more specific supported action here.
```

### Competing outcome

Unsupported dependency input is the main pressure case: it plausibly maps to `abstain`, but the current CLI also has explicit “unsupported” operational presentation before any synthesis exists. The project still needs to decide whether “unsupported” is a reason within an abstention result or a separate outer status.

### Counterexample

Artifact applicability unresolved because one exact compatibility proposition can be named and checked should **not** automatically abstain; the product can still provide a useful targeted action.

---

# Part IV — Counterexamples and cross-mechanism pressure

## 13. High-information pressure cases

### Case A — one concrete artifact proposition remains

```text
artifact wheel-capability loss = established
exact target wheel compatibility = unresolved
Python-support = no material competing concern
integrity = usable for these facts
```

**Candidate result:** `run targeted checks` with exact target wheel compatibility as the required proposition.

**Why it matters:** validates the current LbD finding without generalizing “unresolved = targeted check.”

### Case B — the same artifact gap plus an independent established concern

```text
Python-support applicability = established_applicable
artifact exact target compatibility = unresolved
```

If the Python concern is accepted as material enough to stop ordinary progression, the primary result may be `investigate or block`, with the artifact compatibility check preserved secondarily.

**Why it matters:** disproves “if a concrete check exists, targeted check always wins.”

### Case C — artifact applicability established, consequence still open

```text
old-only compatible wheel path loss = established for target
proposed sdist = available
source-build/install viability = unresolved
```

**Candidate result:** targeted source-build/install check may be more informative than immediate block, depending on accepted action-level materiality.

**Why it matters:** mechanism applicability does not automatically settle maintainer consequence.

### Case D — complete mechanism-local negatives but no broader coverage premise

```text
artifact complete comparison = no candidate
Python candidate = none or established_not_applicable
CI = supported_not_correlated
global/bounded candidate-discovery adequacy = not established
```

**Candidate result:** favorable action remains unavailable. Whether the first method should abstain or simply not implement this mapping is still a decision.

**Why it matters:** exposes the positive-proof requirement for `merge after normal review`.

### Case E — no model claim returned

```text
upstream semantic extraction = no accepted support-drop claim
artifact = no candidate
```

**Candidate result:** no favorable inference from the missing model claim alone.

**Why it matters:** Core authority rules prohibit turning absence of a model-derived claim into proof of no relevant risk.

### Case F — exact target evidence exists but accepted method is unsupported

[`docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md) deliberately excludes arbitrary equality `===`, epochs, locals, prerelease/dev/post forms, and >3 release components from its first exact stable-line method. [`tests/test_python_line_specifier_method.py`](../tests/test_python_line_specifier_method.py) protects those distinctions.

```text
target declaration = acquired and valid source evidence
comparison = unsupported under accepted bounded method
applicability = unresolved
```

**Candidate result:** this is a method-capability state, not missing evidence. A targeted maintainer check may be possible if a concrete standards-correct comparison can be named; otherwise abstention is more honest than defer.

**Why it matters:** disproves “all unresolved states are acquisition gaps.”

### Case G — CI is green-looking but proof strength is static/runtime mixed

```text
CI aggregate = supported_not_correlated
no material mechanism concern established
```

**Candidate result:** CI can support the evidence report and satisfy a future accepted CI prerequisite, but it cannot independently authorize the favorable action.

**Why it matters:** preserves ADR-0008's static/runtime proof boundary.

### Case H — no successful CI, but the run might merely be in progress

Current aggregate semantics can return `no_successful_ci` when there is no completed-successful job.

**Candidate result:** the aggregate alone does not justify `defer`. If a separately owned state establishes “exact-head CI is pending,” then `defer` becomes a credible candidate with a completion rerun trigger.

**Why it matters:** identifies a possible missing CI/pending projection rather than asking synthesis to infer runtime lifecycle ad hoc.

### Case I — provider acquisition failure plus independent blocker

```text
independent technical concern = established and material
another provider result = acquisition_failed / unavailable
```

**Candidate result:** do not let `defer` for the provider failure hide the independent blocker. Use `investigate or block` as primary if its permission is already satisfied; preserve reacquisition/rerun as secondary.

**Why it matters:** no first-match or “latest failure wins” policy.

### Case J — typed exact transition affected by known snapshot-integrity defect

```text
DependencyVersionChange object exists
but changed-file evidence cannot prove correspondence to frozen PR head under current known defect
```

**Candidate result:** favorable permission must be withheld. Depending on what evidence remains trustworthy and whether the run can be safely restricted/reacquired, the eventual action may be abstain or operational failure rather than a mechanism action.

**Why it matters:** typed shape is not proof of evidence integrity.

### Case K — CI evidence affected by attempt mixing, independent package concern unaffected

```text
CI authority = restricted due attempt identity
package/upstream evidence = independently trustworthy
Python concern = established from unaffected evidence
```

**Candidate result:** do not use CI to authorize favorable action, but do not erase the independent concern.

**Why it matters:** reliability constraints should be claim-relative.

### Case L — unresolved candidate with no further UpgradePilot-executable check but concrete maintainer check

```text
mechanism applicability = unresolved
UpgradePilot selector = none
maintainer can perform a concrete discriminating check
```

**Candidate result:** `run targeted checks` remains possible.

**Why it matters:** UpgradePilot execution admissibility and maintainer recommendability are separate accepted concepts.

### Case M — unresolved candidate with no UpgradePilot check and no concrete maintainer check

```text
material unresolved/conflicted state
no bounded discriminating check available
no explicit external pending condition
```

**Candidate result:** broader `investigate` or `abstain`, depending on whether meaningful inquiry remains inside the supported boundary. Not `defer` by default.

**Why it matters:** “investigation stopped” is not an action.

### Case N — exception prevents synthesis input construction

```text
GitHub acquisition/response exception
→ CLI error path
→ no PublicPullRequestInvestigation returned
```

**Candidate result:** current synthesis has no action to emit. This remains an operational run failure unless an outer application-result contract is separately designed.

**Why it matters:** advertised synthesis behavior must be producer-reachable.

---

# Part V — Possible missing investigation responsibilities

## 14. Gap classification

The table separates “UpgradePilot should perhaps learn this itself” from “tell the maintainer what to check.” None of these rows authorizes implementation.

| Exposed proposition/state | Candidate classification | Why | Scope/admission caution |
|---|---|---|---|
| Exact target wheel compatibility for artifact candidate | **Possible genuine missing UpgradePilot investigation responsibility** | current artifact domain already has exact target compatibility evidence/problem types and the normal integration repeatedly stops at this exact decision-relevant proposition | deriving arbitrary target tags safely may require OS/arch/interpreter/ABI facts not established by static runner/Python declarations; do not use current-host tags as target proof or expand into a universal environment engine |
| Source-build/install viability after target wheel-path loss with sdist present | **Maintainer-side targeted check first; possible later bounded product investigation only if repeatedly justified** | it can materially discriminate whether loss of a prebuilt wheel becomes a practical install concern | B2 explicitly excludes arbitrary target code/dependency execution; do not create a generic build/execution platform from this one gap |
| Python `requires-python` forms deliberately unsupported by ADR-0005 | **Accepted method boundary; not automatically a missing responsibility** | unsupported forms are intentional, standards-aware abstention rather than missing source evidence | reassess only when a real supported case requires the excluded form, per ADR trigger; do not broaden just for completeness |
| Exact-head CI genuinely still running/pending | **Possible missing CI/lifecycle projection if `defer` is required** | current aggregate `no_successful_ci` does not distinguish pending from absent/failed | synthesis should not inspect arbitrary raw statuses and invent a lifecycle policy if CI authority owner can expose the semantic fact more cleanly |
| Retryability/temporary provider condition | **Possible acquisition/application policy responsibility, not synthesis inference** | `acquisition_failed` does not say whether/when retry is expected to help | any retry/backoff/future-condition semantics need evidence and bounded policy; do not label every network error `defer` |
| Candidate-discovery/coverage adequacy for favorable action | **Genuine synthesis-adjacent missing responsibility/contract** | mechanism-local negatives cannot justify “no UpgradePilot-specific escalation” without a bounded statement of what was actually searched/evaluated and why that is adequate for the favorable claim | does not require universal impact discovery; a bounded coverage declaration may be enough, but must be positive and enforceable |
| Evidence staleness classification | **Potential evidence-quality responsibility, currently under-specified** | Core requires stale behavior where relevant, but no synthesis-ready general stale state/threshold was found | do not invent age thresholds inside synthesis; add only when a concrete evidence source/action requires freshness semantics |
| PR changed-file snapshot identity / workflow attempt identity / static command correctness | **Upstream correctness responsibilities** | synthesis cannot reconstruct lost provenance or parser meaning | consume proven repairs/restrictions or withhold affected permissions; do not duplicate producer logic in synthesis |
| Exceptions that prevent application result construction | **Outer application/run-result contract question** | synthesis cannot map states it never receives | do not swallow all operational failures into semantic abstention; decide separately whether the public product requires a normalized failed-run envelope |
| Repository-specific policy/materiality (for example whether wheel loss is blocking) | **Potential maintainer/policy-context responsibility; currently not owned strongly enough for generic inference** | technical applicability alone may not determine whether maintainers should block, test, or accept fallback | do not create a broad repository-policy engine merely to finish synthesis; first method may remain conservative or use only clearly owned context |

### 14.1 Strongest current candidate for product-owned follow-up: exact wheel compatibility

This gap is unusually well-formed because:

```text
artifact candidate already exists
+
Target context acquisition already exists
+
Artifact applicability already names exact compatibility as the missing proposition
+
mechanism tests already accept exact compatibility evidence/problem types
```

That is stronger evidence of a missing responsibility than merely noticing an interesting technology.

However, the current Target source intentionally stops before exact tags, and the artifact integration plan explicitly preserved that stop. Therefore the correct next design question is not “implement packaging.tags.” It is:

> What is the smallest authoritative evidence path that can establish the target's relevant wheel compatibility without pretending static runner labels or the current machine represent the target runtime?

Until that is answered and admitted, a maintainer-facing targeted check is the safer synthesis-level proposal.

### 14.2 Strongest current reason **not** to auto-expand: source fallback execution

Running arbitrary source builds/installations would introduce active target execution, environment isolation, reproducibility, potentially untrusted build logic, and new authority questions. That crosses the current B2 stop boundary much more strongly than exact static evidence acquisition.

Therefore source-build viability is currently a better example of:

```text
useful maintainer targeted check
!= automatically justified UpgradePilot automation
```

---

# Part VI — Candidate decision-matrix pressure cases

## 15. Research matrix

These rows are **proposals for pressure testing**, not accepted semantics and not a runtime rule table.

| Evidence/input state | Permitted action | Stronger/competing actions not justified | Decisive reason | Residual uncertainty/conflict | Required check/rerun trigger | Reliability/provenance constraint |
|---|---|---|---|---|---|---|
| Artifact wheel-capability-loss candidate established; exact target compatibility unresolved; no independent blocker | **Candidate: run targeted checks** | favorable; blanket block; generic defer; abstain | one exact decision-relevant proposition is missing and discriminable | source fallback/consequence may remain after compatibility is known | establish exact target wheel compatibility; reassess artifact applicability | old/proposed package identity and target association must be trustworthy |
| Same artifact gap + independent Python-support concern already established and accepted as materially blocking | **Candidate: investigate or block (block sub-disposition)** with artifact check secondary | targeted-check as sole primary; favorable; defer masking blocker | independent evidence is already sufficient to stop ordinary progression | artifact applicability still unresolved | exact artifact compatibility may still be required before reassessment | blocking evidence must be independent of restricted artifact/CI inputs |
| Exact target wheel-path loss established; proposed sdist exists; source viability unresolved; no other blocker | **Candidate: run targeted checks** if source viability would change maintainer disposition | favorable; automatic block solely from sdist uncertainty; defer | prebuilt artifact concern is real but practical fallback consequence remains discriminable | arbitrary build behavior remains open | bounded target source build/install check; rerun synthesis with result | do not infer `sdist exists -> build works` |
| Artifact comparison complete/no candidate; Python candidate established_not_applicable; broader discovery coverage not adequate | **No favorable permission yet; candidate abstain or leave mapping unimplemented pending coverage decision** | merge after normal review | only mechanism-local negatives are established | unknown whether admitted discovery coverage is adequate for broader negative claim | define/accept bounded discovery-coverage premise | mechanism completeness must not be promoted to global completeness |
| Same as above, but explicit accepted bounded discovery coverage, input integrity, required context/CI prerequisites, and no outstanding checks are all satisfied | **Candidate: merge after normal review** | stronger “safe/merge now” claim | no additional UpgradePilot-specific escalation is justified inside the accepted bounded investigation | ordinary maintainer review and out-of-scope risks remain | rerun if PR head/evidence changes | positive integrity/coverage gates must be enforceable, not disclaimers |
| CI `supported_not_correlated` with no other state specified | **No action from this fact alone** | favorable merely because CI is green; block merely because runtime correlation is absent | CI is supporting bounded authority/context, not overall policy | exact step execution/version exercise unresolved | only if selected overall semantics require stronger CI evidence | preserve ADR-0008 static/runtime proof boundary and attempt-integrity restriction |
| CI `no_successful_ci`; producer has no explicit pending-state fact | **No automatic defer; action depends on other evidence** | favorable from absence; defer inferred from enum alone | aggregate does not identify why no successful job exists | CI may be absent, failing, or pending | owner-specific check/rerun only if exact missing proposition is known | do not interpret raw lifecycle ad hoc when aggregate lacks semantics |
| Separately established exact-head CI is genuinely pending and decision-critical; no independent blocker | **Candidate: defer** | targeted new test; favorable; broad investigate | a named external future condition is expected to supply the needed evidence | result remains unknown until completion | rerun when exact-head CI reaches terminal state | pending fact must come from an authoritative producer, not guesswork |
| Package `acquisition_failed` without retryability/future-condition evidence | **Candidate mapping unresolved; likely abstain/operational failure or explicit reacquisition check, not automatic defer** | favorable; automatic defer | acquisition failure does not prove temporary/pending semantics | package evidence absent | only a separately accepted retry/reacquisition policy can name trigger | preserve typed provider problem and producer reachability |
| Exact proposed package `version_not_found` or identity mismatch | **Candidate: investigate or abstain depending transition/package authority contract** | favorable; generic defer | foundational package evidence contradicts or fails exact transition expectation | cause may be bad update identity, unavailable index state, or unsupported case | verify exact transition/package authority if a concrete check exists | do not collapse with timeout/malformed/missing |
| Python target evidence acquired; stable-line comparison intentionally unsupported (`===`, epoch/local/etc.) | **Candidate: targeted check if a concrete standards-correct maintainer check is available; otherwise abstain** | favorable; defer as if evidence were missing | evidence exists; accepted method lacks semantics | target applicability unresolved | concrete external comparison/evidence only if it can discriminate; otherwise no rerun promise | ADR-0005 explicitly owns the supported grammar |
| Foundational dependency result is unsupported/multiple/conflicting/ambiguous | **Candidate: abstain for synthesis, or keep as explicit unsupported outer state if that contract is preferred** | all specific maintainer recommendation actions | no trustworthy single admitted transition exists | exact update meaning unresolved | only source/dependency reconciliation can change state | do not guess one dependency or treat representation failure as risk evidence |
| Known PR patch/revision integrity defect affects canonical transition provenance | **Withhold favorable; candidate abstain/operational failure unless safely restricted or reacquired** | merge after normal review | decision-critical source identity is not trustworthy enough for positive permission | downstream results may inherit tainted transition identity | rerun only after proven snapshot-integrity correction/restriction | synthesis cannot reconstruct discarded head correspondence |
| Known workflow-attempt mixing restricts CI, but independent package/upstream evidence establishes a material concern | **Candidate: investigate or block from independent concern; CI limitation secondary** | favorable; defer solely for CI | independent concern remains decision-bearing even when CI is restricted | CI corroboration unresolved | CI rerun/correction only if it changes later disposition | claim-relative reliability; do not erase unaffected evidence |
| Material applicability unresolved; no UpgradePilot executable check; concrete maintainer check exists | **Candidate: run targeted checks** | favorable; abstain solely because UP cannot execute | maintainer-recommendability is distinct from UpgradePilot execution admissibility | product itself cannot close proposition | named maintainer check + reassessment trigger | check must stay within supported evidence/claim boundary |
| Material unresolved/conflicted state; no specific maintainer check; no known pending future condition; broader inquiry still meaningful | **Candidate: investigate sub-disposition** | targeted checks; defer; favorable | decision-critical state needs broader evidence gathering | conflict/uncertainty remains open | investigation target must be defined before any future targeted check | do not convert “more investigation” into a generic rule engine/planner |
| Material unresolved state; no specific check, no meaningful supported inquiry, no pending condition | **Candidate: abstain** | targeted checks; defer; favorable | UpgradePilot lacks authority/method for a more specific operation | uncertainty remains intentionally unresolved | none unless supported boundary/method later changes | investigation stop does not create sufficiency |
| GitHub exception prevents `PublicPullRequestInvestigation` construction | **No current synthesis action: operational run failure** | semantic abstain/defer fabricated after the fact | synthesis is unreachable in normal producer path | investigation incomplete | rerun according to outer CLI/application failure policy, if any | must not advertise a Charter mapping until a real result envelope carries the state |

### 15.1 What the matrix exposes

The matrix resists a universal order such as:

```text
merge < targeted < investigate < defer < abstain
```

or any reverse thereof.

Examples:

- a targeted check can be **mandatory before proceeding**, so it is not merely “less severe” than investigation;
- a block can coexist with a targeted check;
- defer is not severity at all—it is a temporal/future-condition operation;
- abstain is about method/authority, not maximum risk;
- favorable action has the strongest **positive proof burden** even though it looks least cautious.

The correct composition therefore appears closer to **constraints + action-relative permission** than precedence by severity.

---

# Part VII — Action interaction and precedence

## 16. Proposed deterministic composition strategy

A small transparent method could conceptually apply the following constraints. This is intentionally not source pseudocode and does not freeze rule order.

### 16.1 First: establish whether synthesis has a trustworthy admitted case

Ask:

```text
Can the case identity / canonical dependency transition be used at the claim strength
required by any candidate action?
```

If no, favorable and mechanism-specific overall claims are prohibited. Decide whether the public contract calls this abstention or an outer unsupported/operational result.

### 16.2 Second: collect decision-bearing constraints from each mechanism/context

For each mechanism/result, preserve:

```text
established concern
established local non-applicability / no-candidate result
unresolved proposition
conflict
method limitation
required check
coverage limit
input-integrity restriction
```

Do not ask mechanisms to vote on maintainer action.

### 16.3 Third: distinguish continuation kind

For each decision-critical unresolved item, ask:

```text
UpgradePilot check available?
Maintainer concrete check available?
Known external future condition?
Broader supported inquiry meaningful?
No justified continuation?
```

This separates targeted check, defer, investigate, and abstain more cleanly than an uncertainty level.

### 16.4 Fourth: choose one primary current maintainer operation under constraints

Candidate constraints:

```text
independent established blocker
→ cannot be hidden by a weaker/pending reason

a concrete required check
→ may be primary when it is the actual next operation,
   or secondary when another independent blocker already controls progression

known external pending condition
→ supports defer only when no more informative current action is already established

favorable action
→ only after all of its positive permission gates pass

no defensible more-specific action
→ abstain if synthesis was actually reached
```

This is not a numeric precedence scheme. It is a set of mutually checked permissions/prohibitions.

### 16.5 Fifth: preserve non-primary material reasons

Do not discard a second mechanism just because one action was selected.

Example result narrative:

```text
Primary: investigate or block (candidate internal disposition: block)
Decisive reason: Python-support concern established applicable and material.
Required secondary check: establish exact target wheel compatibility for the artifact candidate.
Residual uncertainty: artifact consequence unresolved.
Claim limit: CI static consumption is not runtime step proof.
Rerun trigger: new exact compatibility evidence or change in PR head.
```

This is substantially more traceable than “max severity = block.”

---

# Part VIII — Challenge to the current synthesis plan

## 17. What the current plan gets right

The selected plan already contains strong safeguards that should be preserved:

- first implementation may support only a subset of Charter outcomes;
- favorable action requires positive permission and may remain unavailable;
- action-relative sufficiency is pressure-tested instead of a generic score;
- targeted checks must name a discriminating proposition and can be prerequisites;
- competing reasons must not be resolved by accidental input order;
- typed acquisition problems and producer-unreachable exceptions are separated;
- correctness findings should constrain permissions without turning synthesis into a repair backlog;
- candidate-discovery incompleteness must not become global negative evidence;
- deterministic transparent composition is the baseline;
- accepted rules must be promoted to a stable specification before implementation.

This investigation does **not** recommend replacing that plan.

## 18. Missing or under-specified semantic questions

### 18.1 `defer` needs an explicit future-condition input, not just action wording

The plan correctly asks when to defer, but current source states generally do not expose a normalized fact such as:

```text
condition = exact_head_ci_pending
rerun_when = terminal
```

or:

```text
provider_state = known_temporary_outage
retry_after = ...
```

Without a trustworthy producer for the future condition, `defer` risks becoming a guess over missing evidence. The plan should treat “what fact authorizes temporal waiting?” as a first-class semantic acceptance question.

### 18.2 “Investigation-stop state” is not currently a stable input

The intended synthesis flow includes residual uncertainty / investigation-stop state, but current mechanism selectors do not provide one uniform reasoned stop contract. `None` can mean very different things.

Before implementation, the design needs either:

- a minimal normalized continuation/stop projection; or
- explicit per-mechanism interpretation that is small enough not to duplicate mechanism policy.

### 18.3 Favorable action requires a concrete coverage owner or coverage declaration

The plan already states candidate-discovery incompleteness must remain visible, but the current application has no obvious top-level object answering:

> What impact/discovery responsibilities were actually evaluated, with what bounded coverage, and why is that enough to say no additional UpgradePilot-specific escalation is warranted?

Without such a premise, favorable action may stay unavailable indefinitely. The missing responsibility need not be universal impact discovery; it can be an explicit bounded coverage contract.

### 18.4 Mechanism applicability does not yet define action-level materiality/consequence

Current applicability tells whether a represented technical path applies. It does not automatically answer:

```text
Is this concern material enough to block?
Can a fallback reduce the concern?
Is a targeted validation the better next maintainer operation?
```

The artifact sdist example makes this concrete. The synthesis design needs a bounded rule for action-level consequence/materiality or must deliberately remain conservative without inventing one.

### 18.5 Repository/context evidence is still abstract at the synthesis boundary

The plan says to admit only relevant repository/context evidence, which is correct. But no current general repository-policy owner should be silently created to answer every materiality question.

The design must identify the **first actually necessary context fact** before implementation. If none is trustworthy/needed for the first emitted actions, do not create a broad context subsystem merely because the synthesis diagram contains “repository/context.”

### 18.6 Model-origin semantics must survive any smaller synthesis input

A grounded support-drop claim is not independently confirmed truth. If a future synthesis projection stores only:

```text
python_support_applicability = established_applicable
```

and discards that a necessary premise originated from model-derived interpretation with bounded grounding, the decision layer can accidentally strengthen authority.

The plan already mentions AUTH/grounding rules; the actual projection design must prove that this provenance is not erased.

### 18.7 Staleness is required conceptually but not yet operationally uniform

The Charter/Core require explicit stale behavior where relevant, but this inspection did not find one accepted synthesis-ready universal freshness classification or threshold.

The design should therefore avoid either:

```text
all timestamps are fresh enough
```

or:

```text
older than N minutes = stale
```

until an owner/evidence need justifies that rule.

### 18.8 Some states may legitimately have no first-version action mapping

The plan allows first-version action subsets, but the matrix should explicitly permit:

```text
this state family is not yet implementable under accepted semantics
```

rather than forcing every observed enum into one Charter action just to make the table total.

The most obvious candidates are:

- favorable-looking all-negative current mechanism state without accepted discovery coverage;
- generic provider acquisition failure without future-condition/retry semantics;
- some unsupported foundational states until the project decides whether “unsupported” is nested abstention or outer result status.

---

# Part IX — Unresolved questions

## 19. Questions that should remain open until Ali reviews the pressure cases

1. **Favorable coverage:** What exact bounded discovery/coverage statement is sufficient to say “no additional UpgradePilot-specific escalation is warranted” without claiming universal mechanism exhaustion?
2. **Favorable CI requirement:** What minimum CI authority, if any, is a positive prerequisite for the first favorable action? `supported_not_correlated` is bounded evidence, not safety proof.
3. **Action-level materiality:** What turns an `established_applicable` technical mechanism into a maintainer-level block versus a targeted validation opportunity?
4. **Artifact fallback:** If target wheel loss is established but an sdist exists, is source-build viability a required check before blocking, optional context, or outside the first synthesis policy?
5. **Investigate/block representation:** Does the Charter family require an internal `investigate` versus `block` sub-disposition, or are reasons/checks sufficient to keep one runtime action unambiguous?
6. **Targeted-check interaction:** When a required targeted check coexists with an independent blocker, should the primary action be block with secondary check, or can `run targeted checks` represent “hold and check” adequately?
7. **Defer admission:** Should `defer` be excluded from the first implementation until a pending/future-condition producer exists?
8. **Provider retry semantics:** Which owner, if any, should classify retryability/temporary unavailability? Synthesis should not infer it from generic failures.
9. **Unsupported vs abstain:** Should unsupported foundational dependency transitions become `abstain` with an explicit reason, or remain a separate outer supported-domain result outside synthesis?
10. **Operational failure envelope:** Must every admitted CLI attempt eventually yield a Charter action/abstention, or may acquisition/runtime failures remain explicit non-semantic error exits?
11. **Stop semantics:** What minimum reasoned continuation/stop information must synthesis receive so selector absence cannot be misread?
12. **Model provenance:** What is the smallest representation that preserves model-origin/grounding/independent-corroboration limits across synthesis?
13. **Known correctness defects:** Which first-version actions actually depend on the affected evidence, and for each one will the project repair upstream, enforce a real restriction, or withhold permission?
14. **Staleness:** Which evidence sources need freshness semantics for the first synthesis method, and what owner should define them?
15. **Stable owner:** Should accepted synthesis semantics extend the Product Decision Model specification or live in a new focused synthesis specification? The plan correctly leaves this open.

---

# Part X — Recommended next examination and decision sequence

## 20. Suggested review order

This proposal recommends that the project make the next decisions in the following semantic order, still without implementation:

### Decision 1 — accept or reject the action-relative model

Confirm whether the central question is:

```text
What action is this evidence sufficient to justify now?
```

rather than:

```text
Is the case globally sufficient/insufficient?
```

If accepted, avoid a redundant global sufficiency Boolean unless later pressure demonstrates independent value.

### Decision 2 — define the minimum synthesis input projection

Do not choose source classes yet. First agree on which semantic properties must survive:

```text
admitted identity
input integrity/authority
mechanism finding + proof state
coverage/finality
continuation/check type
future-condition state where applicable
provenance/claim limits
producer reachability
```

Then map those properties back to existing source owners.

### Decision 3 — settle `run targeted checks` with the artifact pressure path

Use the current real sequence:

```text
wheel capability loss established
→ exact target compatibility unresolved
→ exact compatibility check
→ if wheel-path loss established and sdist exists, source-fallback viability question
```

Decide exactly when the first and second checks are maintainer-facing, when one becomes an UpgradePilot-owned investigation candidate, and when the state is material enough to block.

### Decision 4 — pressure `investigate` versus `block` with a mixed-mechanism case

Use one state where:

```text
Python support = established/material
artifact = unresolved with concrete check
```

This is the best current contrast for deciding whether an internal sub-disposition materially improves behavior.

### Decision 5 — decide whether `defer` is currently supportable

Require an explicit example with a **producer-owned pending future condition**. If none exists in the current semantic input, leave `defer` unavailable rather than synthesizing temporality from generic failure states.

### Decision 6 — define favorable positive permission last

Only after the cautious actions are clear, decide:

- bounded discovery coverage;
- integrity restrictions;
- minimum CI/context prerequisites;
- treatment of model-origin absence;
- outstanding-check prohibition;
- exact claim wording.

If these cannot be enforced, keep `merge after normal review` unavailable in the first method.

### Decision 7 — choose the stable semantic owner

Only after the matrix is coherent should accepted durable rules move to the appropriate specification owner. The proposal and working memory remain provenance, not authority.

---

# Part XI — Things that should not yet be implemented or promoted

## 21. Explicit non-promotions

Do **not** yet implement or promote as stable truth:

- a universal action severity/precedence ranking;
- a numeric risk/safety/confidence score;
- an LLM judge, agent planner, graph, workflow engine, or generic rule engine for synthesis;
- a global `sufficient` Boolean whose semantics duplicate the action;
- `selection is None -> investigation complete/resolved`;
- `investigation stopped -> evidence sufficient`;
- `green/supported CI -> favorable action`;
- `no model claim -> no relevant impact`;
- `one mechanism no candidate/non-applicable -> no overall concern`;
- `acquisition_failed -> defer`;
- `no_successful_ci -> defer`;
- `established_applicable -> block` without action-level consequence/materiality semantics;
- `sdist available -> source fallback works`;
- static runner/Python/install declarations -> exact target wheel compatibility;
- current-machine wheel tags -> arbitrary target compatibility;
- broad source-build/target execution infrastructure merely to close the artifact fallback question;
- arbitrary expansion of ADR-0005's intentionally unsupported Python specifier forms without a real supported-case trigger;
- a synthesis layer that re-parses raw commands, reconstructs PR snapshot identity, or repairs workflow-attempt provenance that its producers lost;
- a blanket “trusted input” disclaimer in place of enforceable reliability restrictions;
- a total action mapping for every current error/problem enum merely for completeness;
- a claim that all current impact mechanisms are exhausted;
- a Charter vocabulary change from this proposal;
- source/tests/specification/plan changes before Ali reviews and accepts the semantic decisions.

---

# Part XII — Proposed synthesis contract properties, not field names

## 22. Minimum information that appears necessary if semantics are accepted

This section deliberately names information responsibilities rather than Python classes.

A future result appears to need enough information to answer:

| Responsibility | Question |
|---|---|
| Primary action | What Charter-facing operation is justified now? |
| Internal disposition, if needed | Within `investigate or block`, is the current operation primarily broader inquiry or explicit hold/block? |
| Decisive reasons | Which established evidence/constraint actually permitted this action? |
| Prohibited stronger actions | Why is a more favorable/different action not justified? |
| Residual uncertainty/conflict | What material facts remain unresolved or conflicting after selecting the action? |
| Required checks | What exact proposition must a maintainer establish, and is the check a prerequisite or merely supporting? |
| Rerun/future trigger | What changed evidence or external condition justifies reassessment? |
| Coverage | What bounded mechanisms/discovery responsibilities were evaluated, and what does that coverage permit the result to claim? |
| Reliability/authority | Which inputs are usable/restricted/unusable for the selected claim, including model-origin limits? |
| Exact identity | Which repository/PR/head/dependency transition does the conclusion apply to? |
| Claim limits | What does the result explicitly not establish? |

The report does **not** recommend mirroring all of `PublicPullRequestInvestigation` in this result. Detailed evidence can remain linked/preserved through existing application/report structures while synthesis keeps only the decision-bearing projection necessary for deterministic composition and traceability.

---

# Part XIII — Final assessment

## 23. Main design recommendation

The current repository evidence supports continuing the selected synthesis plan. It does not support implementation yet.

The most credible simple baseline is:

```text
heterogeneous typed evidence
→ authority/integrity/coverage-aware semantic projection
→ explicit action-relative permission/prohibition constraints
→ one primary Charter action or abstention
→ secondary required checks + residual uncertainty + rerun trigger + claim limits
```

The baseline should **not** be described as “pick the worst result.” The decisive operation depends on the kind of uncertainty, whether a concrete check exists, whether a future condition is genuinely pending, whether an independent blocker exists, and what positive proof a favorable action requires.

The most consequential design issues still open are:

```text
1. favorable bounded coverage and positive permission;
2. action-level materiality/consequence;
3. investigate versus block representation;
4. defer's missing future-condition semantics;
5. explicit continuation/stop meaning;
6. producer reachability and reliability restrictions;
7. whether exact target wheel compatibility should become the next bounded investigation responsibility.
```

Those questions should be decided against the pressure cases above before any stable specification promotion or implementation.

This report intentionally leaves them open where repository evidence does not yet justify one answer.

---

## 24. Evidence-index summary

For future review, the highest-value direct owners for this proposal's conclusions are:

- Charter action vocabulary and claim limits: [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)
- active synthesis responsibility/acceptance gates: [`plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)
- current LbD semantic findings: [`working-memory/2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md`](../working-memory/2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md)
- candidate/applicability/investigation/coverage semantics: [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)
- authority/provenance/missing/conflict/model claim limits: [`docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- bounded generality: [`docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- current real application envelope: [`src/upgradepilot/investigation.py`](../src/upgradepilot/investigation.py)
- CI proof strength: [`src/upgradepilot/ci/dependency_exercise.py`](../src/upgradepilot/ci/dependency_exercise.py), [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)
- Python method-limit pressure: [`docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md), [`tests/test_python_support_impact.py`](../tests/test_python_support_impact.py), [`tests/test_python_line_specifier_method.py`](../tests/test_python_line_specifier_method.py)
- artifact exact-compatibility pressure: [`src/upgradepilot/impact/artifact_serviceability.py`](../src/upgradepilot/impact/artifact_serviceability.py), [`src/upgradepilot/target/artifact_environment.py`](../src/upgradepilot/target/artifact_environment.py), [`tests/test_artifact_serviceability.py`](../tests/test_artifact_serviceability.py), [`tests/test_target_artifact_environment.py`](../tests/test_target_artifact_environment.py)
- current integrity defects and their proof limits: [`working-memory/2026-09-08_system-limitations-and-correctness-investigation.md`](../working-memory/2026-09-08_system-limitations-and-correctness-investigation.md)
- candidate-discovery/context separation pressure: [`product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md), [`product-simulation/CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md`](../product-simulation/CROSS_CANDIDATE_CONTEXT_SYNTHESIS_PRESSURE_TEST_01.md)

No recommendation in this document should be treated as accepted project semantics until Ali reviews it and the accepted portion is deliberately promoted to the correct stable owner.