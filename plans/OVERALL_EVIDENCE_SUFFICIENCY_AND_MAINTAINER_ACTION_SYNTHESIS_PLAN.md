# Overall Evidence Sufficiency and Maintainer Action Synthesis Plan

**Status:** admitted bounded planning/execution responsibility; live selection remains owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) Phase-7 synthesis handoff  
**B2 flow owner:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Current decision-model boundary:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Historical source material only:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)

## Authorization and proposal use

Plan maintenance authorizes planning and its directly necessary records. Product implementation requires accepted synthesis semantics and an authorized Build responsibility; updating this plan does not satisfy either condition by itself.

Use the September 10 [synthesis investigation](../proposals/2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md) for input distinctions and counterexamples, and the [LLM-assisted synthesis proposal](../proposals/2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md) for a possible later comparison. Both remain non-controlling. Their illustrative action mappings, field names, permission envelope, and architecture are not adopted by reference.

The [September 10 discussion and review](../working-memory/2026-09-08_overall-evidence-sufficiency-synthesis-orientation.md) supplies dated rationale. Its later investigation-to-synthesis correction qualifies earlier targeted-check examples: a useful check alone does not establish that the maintainer should be asked to perform it. Accepted boundaries remain owned by the Product Decision Model, especially §§11–14.

## Responsibility

Define, accept, implement, and prove the smallest transparent B2 synthesis responsibility that consumes already-earned heterogeneous investigation state and produces a bounded maintainer-facing action or honest abstention without manufacturing safety, completeness, or certainty.

The product boundary already fixes the allowed broad outcomes:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

This plan does **not** redefine those Charter outcomes. It determines the minimum admitted synthesis contract and method needed to decide among the outcomes that can be defensibly supported at the actual current B2 evidence boundary.

The intended responsibility is:

```text
PublicPullRequestInvestigation
+ mechanism-specific technical candidate/applicability results
+ CI/evidence authority
+ relevant repository/context evidence where admitted
+ acquisition/problem states
+ residual uncertainty / investigation-stop state
↓
overall evidence-sufficiency assessment
↓
bounded maintainer action OR abstention
↓
traceable decisive reasons + unresolved questions + claim limits
↓
human-readable and minimum machine-readable output
```

## Entry evidence

The responsibility is now earned because the current application path has two materially different technical mechanism families with executable deterministic proof:

- Python-support-drop reasoning with conditional target investigation and candidate-specific applicability;
- artifact-serviceability reasoning with exact old/proposed package evidence, bounded Target artifact-environment composition, and explicit unresolved exact compatibility where stronger evidence is unavailable.

The current `PublicPullRequestInvestigation` exposes heterogeneous typed evidence/results but no overall synthesis result. The CLI presents evidence at its owned proof strength and deliberately does not produce an overall maintainer recommendation.

The accepted Product Decision Model explicitly stops before mature synthesis/policy semantics and says that this later contract must be separately admitted and accepted. Therefore this responsibility begins with semantic/design work, not source implementation.

## Scope

In scope:

- define the smallest overall synthesis input/output contract around the real current investigation state;
- establish the minimum investigation-to-synthesis handoff, reusing existing owned facts before proposing missing state;
- distinguish overall evidence sufficiency from mechanism-specific applicability;
- define residual-uncertainty and abstention behavior;
- decide how the Charter outcome classes are permitted or prohibited by current evidence states;
- admit only the minimum repository/context evidence genuinely needed by the first synthesis method;
- preserve acquisition/problem/unsupported states without converting them into favorable inference;
- produce traceable decisive reasons, unresolved questions, required targeted checks when applicable, and claim limits;
- expose the accepted synthesis result through the normal application/CLI boundary;
- add minimum machine-readable state only where it materially improves deterministic proof and traceability;
- behavior-test materially different controlled states before any live proof;
- run the nearest and full deterministic suites after implementation.

## Explicit non-goals

Do not automatically introduce:

- objective upgrade-safety scoring;
- one opaque universal risk/confidence score;
- automatic merge, approval, commenting, or repository mutation;
- universal impact-candidate discovery or complete candidate-discovery coverage;
- arbitrary repository-wide policy engines;
- generic rule engines, planners, graph frameworks, agent orchestration, or workflow engines;
- numeric Value-of-Information optimization;
- new persistence/replay infrastructure unless a later separately admitted milestone requires it;
- broad new Target/artifact/CI mechanisms merely because synthesis observes unresolved evidence;
- package/repository/version/fixture-specific action rules;
- a learned/model-based synthesis method without first proving the deterministic transparent baseline and demonstrating a limitation.

## Relationship with supporting correctness investigations

The separate [`SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md) and its dated working-memory record remain an independent supporting workstream.

This synthesis responsibility may consume **established findings** from that workstream when they materially constrain whether evidence can authorize a maintainer action. It must not silently absorb the investigation itself.

Therefore this plan does **not** normally:

- rerun the correctness investigation campaign;
- take ownership of its pending questions;
- repair every parser/provider/CI/acquisition defect it identifies;
- expand Target, CI, acquisition, or parser scope merely because a reliability limitation exists;
- wait for every supporting investigation question to finish before making synthesis progress.

When an established correctness finding materially affects an action-permission rule, choose the smallest justified disposition:

```text
upstream correction with matching proof
OR
enforceable supported-input restriction
OR
withhold the affected action permission
```

A pending or unrelated correctness question is not automatically a prerequisite for synthesis. It becomes a blocking dependency only when the synthesis method actually requires the affected evidence proposition and no enforceable restriction can preserve correctness.

This plan may record such a dependency or restriction, but the originating investigation remains owned by its separate plan/record.

## Already-owned semantics

The plan must consume, not redefine, these accepted boundaries:

1. **Charter outcome set and claim limits.** The supported action classes are fixed by `PROJECT_CHARTER.md`; the system does not claim objective safety or replace maintainer judgment.
2. **Mechanism-specific technical truth.** Candidate formulation, applicability, investigation, and stopping semantics remain owned by the Product Decision Model and their mechanism modules.
3. **Missing evidence is not negative evidence.** Unavailable/unresolved/unsupported states cannot silently become absence, non-applicability, or a favorable overall action.
4. **Investigation stop is not overall sufficiency.** A candidate may remain unresolved with no further justified UpgradePilot investigation; synthesis must decide separately what maintainer-facing output is justified.
5. **Repository context is not technical applicability.** Material context may affect overall action without being inserted into one mechanism-specific candidate.
6. **Observation, interpretation, and decision remain distinct.** Synthesis consumes attributed evidence/results and must retain their proof class and limitations.

## Unresolved design questions

These are the real questions to resolve before implementation.

### Overall synthesis contract

Determine the smallest typed result that can represent:

- one bounded Charter action or abstention;
- overall evidence-sufficiency/readiness state;
- decisive evidence-backed reasons;
- residual uncertainty or conflicts;
- required targeted checks when the action is `run targeted checks`;
- explicit reason for deferral or abstention;
- claim limits / what is not established;
- exact repository/PR/revision/dependency identity required for traceability.

Do not choose field names from historical plans merely for compatibility.

### Sufficiency model

Pressure action-relative sufficiency as the baseline design hypothesis: what is this evidence sufficient to recommend? Determine whether the selected action plus reasons and limits already carries that meaning. Add a separate sufficiency/readiness field only if a concrete consumer or contrast demonstrates independent value.

The representation must preserve distinctions such as:

```text
sufficient for one bounded action
insufficient with a known actionable evidence gap
material unresolved/conflicted state
unsupported/out-of-admitted-domain state
```

Avoid a generic boolean `sufficient` if it collapses materially different stopping/action behavior.

### Investigation-to-synthesis handoff

Map necessary facts to their normal producer, composition path, and consumer before choosing new types. Begin with these source/test anchors:

- `src/upgradepilot/investigation.py` and `tests/test_investigation.py`;
- `src/upgradepilot/impact/python_support.py` and `tests/test_python_support_impact.py`;
- `src/upgradepilot/impact/artifact_serviceability.py`, `src/upgradepilot/target/artifact_environment.py`, and their focused tests;
- `src/upgradepilot/ci/dependency_exercise.py`, provider result types, and `src/upgradepilot/cli.py` for supporting evidence and failure reachability.

The September 10 review established two distinct interpretation hazards to recheck at implementation entry: the application retains the Python check selection made before acquisition, while calling the selector on the resulting assessment can return `None` even when applicability remains unresolved. A recorded selection is not necessarily pending work; selector absence is not proof of resolution or justified stopping.

For each decision-relevant non-final proposition, determine only the information needed to distinguish:

```text
what is unresolved or conflicted, and why
what observation could materially discriminate it
whether an admitted, worthwhile UpgradePilot investigation remains
what was selected/attempted and what knowledge or problem resulted
whether retry is justified, outside scope, or unsupported
why no further justified UpgradePilot-executable investigation remains, if established
whether a concrete maintainer check or known external future condition remains
```

Keep epistemic value, UpgradePilot execution admissibility, and maintainer recommendability separate under Product Decision Model §11.4. Do not turn a missing automation capability into a mandatory expansion or a maintainer recommendation by default. If a justified admitted investigation remains, return the dependency to its investigation owner before finalizing the affected maintainer-check recommendation. This does not require exhausting every conceivable investigation or delaying an independently justified conclusion.

Classify each needed fact as already available, derivable without new interpretation, genuinely missing, or unreachable because the application fails first. Record unknown continuation explicitly; do not fill it with a fictional stop reason. Prefer a small explicit projection or direct consumption over a generic planner, capability registry, universal stop enum, or duplicated mechanism interpretation.

### Action-permission boundaries

For each Charter outcome that the first method intends to emit, determine:

- what the action means operationally;
- what positive evidence conditions are minimally required;
- what evidence states make the action too strong;
- what unresolved/conflicting states force a weaker action;
- whether investigation must continue upstream, or the resulting state permits a maintainer check, investigation/block, defer, abstention, or favorable output;
- what changed evidence requires a rerun.

Treat action, any sub-disposition, decisive reason, required check, and evidence relationship as one coherent recommendation. Membership in the Charter action family alone does not establish permission for every meaning inside that family.

### Repository/context admission

Inspect the current real repository/context evidence before adding a new owner. Admit only context that can materially alter the first bounded synthesis result and whose semantics/provenance are clear.

Do not invent a broad repository-policy subsystem merely because B2 eventually needs repository context.

### Cross-candidate relationship

Decide the minimum rule for consuming multiple mechanism-specific results without:

- flattening them into one score;
- double-counting equivalent evidence;
- treating one completed candidate as complete candidate discovery;
- treating one unresolved candidate as automatically blocking every possible bounded output.

The first synthesis method may be deliberately conservative if candidate-discovery coverage remains open.

## First synthesis implementation scope

The Charter defines the **supported outcome family**. It does not require the first synthesis implementation to emit every outcome before a defensible permission boundary exists.

The first method must implement only the subset of outcomes whose semantics and positive/negative permission rules pass the semantic acceptance gate.

No subset is preselected by this plan. Favorable output may remain unavailable without enforceable positive prerequisites; `defer` may remain unavailable without a supported future-condition input. Other actions also require their own accepted rules.

This is not a permanent narrowing of the Charter. It is a staged implementation rule:

```text
Charter outcome exists
!=
first synthesis method is already justified to emit it
```

If later evidence establishes a credible positive permission boundary for `merge after normal review`, add it through the same accepted synthesis contract rather than redesigning the whole method.

Conversely, do not force an outcome into the first implementation merely for outcome-count completeness.

## Input reliability and action-permission constraints

The [separate investigation record](../working-memory/2026-09-08_system-limitations-and-correctness-investigation.md) contains bounded executable findings for command-text false positives, PR patch/revision mismatch, and workflow run-attempt mixing. Revalidate their relevance against the implementation snapshot used for synthesis; neither typed objects nor previously green suites establish that these concerns have been corrected. Their recorded synthetic reproductions establish behavior, not public-case frequency or overall recommendation failure.

Before using affected evidence to permit an action, choose and justify one of: an upstream correction with matching proof, an enforceable supported-input restriction, or withholding the affected permission. A restriction is adequate only if the normal acquisition/composition path can actually establish it; a disclaimer or an assumption of stable inputs is not enforcement. Do not ask synthesis to reconstruct provenance discarded by its producers or duplicate provider/domain interpretation.

This reconciliation does not authorize this workstream to repair every investigation finding or absorb the separate reliability investigation.

Apply this assessment to every affected claim, including targeted checks and blocking reasons. Withholding only favorable output is insufficient if a cautious recommendation depends on an untrustworthy dependency transition or target association. Conversely, a restricted CI observation does not erase an independently supported package finding; demonstrate the claimed independence through actual provenance.

Record each material dependency as: affected proposition/action → producer owner → correction, enforceable restriction, or withheld permission → proof needed before use. Do not claim that attaching identity labels or testing a manually fabricated “trusted” input enforces the restriction in normal acquisition.

### Favorable-action prerequisites

Define positive evidence requirements for `merge after normal review`, including the admitted case boundary, relevant repository/context facts, and treatment of discovery coverage and evidence integrity.

Pressure the September 10 interpretation “no additional UpgradePilot-specific escalation is justified within the admitted investigation boundary; return to ordinary maintainer review.” Explain what evidence work earns that result and how it differs from a final merge decision. This remains a semantic question for acceptance, not a Charter rename selected by the plan.

The following cannot alone meet that requirement:

- “no known concern”;
- one non-applicable mechanism;
- a complete artifact comparison with no candidate;
- green CI;
- absence of a model-extracted claim.

A claim-limit sentence cannot replace missing positive evidence.

Universal impact discovery is not required, but the accepted method must justify why its bounded coverage is adequate for the action it recommends. If no credible permission can be established at the first implementation boundary, leave merge unavailable and explicitly test that restriction.

Identify which owner can establish what mechanisms/evidence were actually evaluated, their bounded coverage and omissions, and why the proposed favorable claim is justified. A list of mechanism names is not an adequacy proof. Do not require a new coverage subsystem when a smaller enforceable contract suffices.

### Model-derived evidence

Apply Core AUTH-001 through AUTH-005 and GROUND-001 explicitly at the synthesis input projection and decision boundary. Preserve the distinction between model-derived interpretation, source grounding, independent corroboration, and absence of a returned claim.

A deterministic applicability result does not silently upgrade its originating semantic premise into independently established truth. Determine the minimum provenance/authority representation needed from actual producers before freezing a smaller synthesis input.

### Targeted checks and competing reasons

A concrete targeted check may be a prerequisite to proceeding, not merely an optional improvement. Specify its discriminating proposition, target, prerequisite role, and how its possible outcomes lead to reassessment.

First apply the investigation handoff above. Then establish maintainer feasibility, the check's decision value, and whether its possible outcomes could change the overall disposition. “A test might help” is not a sufficient permission rule.

Recommending a check does not execute it or pre-authorize a later favorable decision.

Define the boundary between `run targeted checks` and `investigate or block` without assuming a universal severity ordering over all five Charter outcomes.

Pressure cases in which multiple reasons suggest different actions, such as a required check alongside an established concern or temporarily unavailable evidence. Explain which reasons determine the selected action and preserve remaining material reasons rather than selecting the first matching rule by accident.

For `investigate or block`, compare an explicit sub-disposition against one action whose structured reasons/checks convey the operation unambiguously. If neither preserves a material distinction, propose a change to the correct stable owner rather than silently changing the Charter. A required check may itself require holding progression; do not assume that check and block are mutually exclusive or universally severity-ordered.

### Consequence, repository context, and temporal conditions

Applicability does not by itself settle the practical consequence or permission to block. Use the artifact case to identify the smallest context fact that changes the action: for example, whether source fallback is permitted and relevant on the exact target. Do not invent repository policy, risk tolerance, or a generic severity score. If a necessary context fact has no supported producer, keep that limitation explicit and constrain the proposed action.

For `defer`, require a named decision-critical pending/future condition, evidence supporting that classification, and a concrete reassessment trigger. Compare genuinely pending exact-head CI with `no_successful_ci`, and supported retry conditions with generic `acquisition_failed`. Time alone does not repair unsupported methods, malformed evidence, or identity conflicts. Identify the smallest CI/acquisition owner needed if this action is to be admitted; otherwise withhold it without expanding the workstream.

Define freshness constraints only for evidence and actions that need them, at the responsible owner. Preserve exact revisions and relevant observation context; do not invent one universal age threshold or assume timestamps alone establish freshness.

### Acquisition failures and producer reachability

Inventory separately:

1. typed problems already returned within `PublicPullRequestInvestigation`;
2. exceptions that prevent that result from being returned.

In the current application shape, some acquisition exceptions may reach the CLI before package analysis and synthesis could run. A fabricated investigation result carrying an error does not prove that the normal producer can supply it.

For each failure class included in synthesis, either demonstrate the existing producer-to-synthesis path or separately resolve the minimum application failure contract needed to make it reachable.

If that orchestration work is deferred, state the operational error/output behavior and exclude the unsupported synthesis promise. Do not relabel every execution failure as semantic abstention, or assume every missing/forbidden/malformed source is temporary and therefore warrants `defer`.

## Semantic acceptance gate

Because the accepted Product Decision Model intentionally leaves mature synthesis/policy semantics open, implementation must not begin until the new stable synthesis semantics are accepted at the correct owner.

The design step must determine whether to:

- extend `UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` with a bounded accepted synthesis section; or
- create a separate focused synthesis specification if ownership would be clearer.

A plan alone must not become the stable semantic owner.

Before implementation, the semantic acceptance checkpoint must establish:

- an input-state map separating usable, affected/unreliable, unavailable, and unreachable-by-current-producer states;
- a producer-grounded handoff separating recorded selection, attempted investigation, resulting knowledge/problem, and justified continuation;
- a disposition and proof boundary for each relevant reproduced input-integrity concern;
- explicit permitted outcomes for the first method;
- explicit unavailable outcomes, including the positive prerequisites required before they can be enabled;
- authority-preserving treatment of semantic inputs and negative inference;
- required-check semantics and conflict/competing-reason selection;
- coherent action/sub-disposition/reason/check relationships, with necessary consequence/context and temporal facts tied to real owners;
- the reachable acquisition-failure contract and any explicitly excluded operational cases;
- concrete contrasting examples supporting those decisions;
- accepted rules promoted to the correct specification owner.

### Required pre-implementation decision matrix

Before implementation, preserve a compact decision matrix in the active dated working memory.

The matrix must make the accepted synthesis boundary inspectable in terms such as:

| Evidence / input state, producer and investigation endpoint | Proposed / accepted action and any sub-disposition | Stronger or competing actions prohibited | Decisive reason and required context | Residual uncertainty / conflict | Required check or supported rerun trigger | Reliability / provenance constraint |
|---|---|---|---|---|---|---|
| one reachable typed-state family; otherwise explicitly hypothetical | distinguish proposal from accepted rule | actions not justified by this state | evidence-backed permission | remaining material unknowns | concrete next condition where applicable | real producer restriction or required correction |

The matrix is design/acceptance evidence, **not** a second semantic owner and not a runtime rule table that must be copied literally into source.

Use it to expose contradictions before coding:

```text
same material state
→ accidentally permits incompatible actions
```

or:

```text
stronger action
→ lacks positive prerequisite
```

or:

```text
reliability limitation
→ is being hidden by a disclaimer instead of enforced
```

Rows should represent coherent typed state families and meaningful contrasts, not one row per fixture, repository, package, or known test case.

Keep this checkpoint outcome in dated working memory. An unresolved item may be deferred only with an explicit, enforceable restriction on the first method's behavior; it must not silently become an assumed premise. Decide the public behavior for admitted states outside an action rule: justified abstention, explicit unsupported result, or operational error as appropriate. An unavailable action does not justify an undefined successful output or a catch-all conversion of defects to abstention.

No ADR is required merely for the synthesis rules. Create/update an ADR only if a consequential implementation method or structural commitment is selected beyond ordinary deterministic Python composition.

## Design and pressure sequence

### Recover actual heterogeneous inputs

Trace `PublicPullRequestInvestigation` through its real producers for dependency identity, CI, package/upstream evidence, both mechanisms, Target evidence, and problem states. Apply the handoff analysis before assigning maintainer actions.

**Output:** one compact map in dated working memory: needed semantic fact → existing owner/field → actual producer path → proof/authority → usable, derivable, missing, affected, or unreachable. Separate presentation/debug data from decision inputs. Retain model origin, grounding and corroboration distinctions; do not infer them from an applicability enum alone.

**Exit:** for the Python acquisition path and artifact compatibility gap, explain what is known, what was attempted, and what continuation is justified or unknown. Name only genuine missing handoff responsibilities. A type name, field inventory, or domain-only fixture is insufficient.

### Define the smallest transparent baseline

Start from deterministic explicit conditions over typed state, not an LLM or generic planner.

The baseline must be explainable as:

```text
owned evidence/result state
→ explicit sufficiency/action condition
→ bounded action or abstention
→ decisive reasons + unresolved limits
```

If deterministic transparent composition cannot credibly satisfy the admitted responsibility, record the exact limitation before proposing a more advanced method.

**Output:** a small composition hypothesis over the mapped facts. Prefer explicit constraints and action-relative permission to mechanism votes, a global sufficiency boolean, a universal severity ladder, or one rule per case. No new class hierarchy or separate permission-envelope object is required at this point.

**Exit:** identify what the method must decide, which input distinctions make that possible, and which semantics remain open. Anticipated complexity alone does not activate an LLM experiment.

### Build and pressure the decision matrix

Before selecting field names or source layout, map the real heterogeneous state families into the required pre-implementation decision matrix.

Work in the contrast order below. Use real source states first; label future/domain-only inputs explicitly. Reuse already-established discussion findings without treating them as accepted rules or repeating completed orientation unnecessarily.

**Output:** proposed rows, their counterexamples, and unresolved decisions, followed by Ali's accepted choices when established. For each emitted action, state positive permission, prohibitions, evidence dependencies, required checks and reassessment conditions. Preserve secondary concerns after choosing a primary operation.

**Exit:** every selected first-version action has a coherent meaning and supporting contrasts; every unresolved question has a bounded next check or enforceable scope restriction. Do not manufacture rules to fill every Charter category.

### Pressure the contract against materially different states

| Order | Contrast to examine | Decision it must resolve |
|---|---|---|
| Investigation handoff | Python declaration not acquired; selected and acquired successfully; acquired with a problem; valid evidence with unsupported comparison | Recorded action versus remaining work; knowledge state versus execution result; no blind retry or invented stop reason |
| Exact artifact applicability | Published wheel loss with unresolved exact target compatibility; justified admitted UpgradePilot check available versus outside its execution boundary | When investigation continues upstream and when a concrete maintainer check becomes recommendable |
| Artifact consequence | Exact target wheel-path loss with sdist present but source viability unresolved; contrast absent fallback and an established relevant repository constraint | Which consequence/context actually permits a check, broader investigation, or block; sdist existence is not build success |
| Competing mechanisms | The artifact check alone versus the same check plus an independently justified material Python-support concern | Primary operation, investigate/block distinction, required secondary checks, and evidence independence |
| Temporal versus method boundary | Producer-established pending exact-head CI versus `no_successful_ci`; supported retry condition versus generic acquisition failure; unsupported comparison despite available evidence | Whether `defer` is supportable and why waiting, checking, investigating, or abstaining differ |
| No useful product continuation | Unresolved/conflicted candidate with no further justified UpgradePilot check; concrete maintainer check versus broader useful inquiry versus neither | Targeted-check, investigation, and abstention boundaries without equating stopping with sufficiency |
| Favorable permission | Complete artifact comparison with no candidate, Python non-applicability, and bounded CI support; contrast absent model claim and any proposed adequate bounded-coverage/context case | Positive favorable prerequisites; local negatives versus broader claim; unavailable favorable output if prerequisites cannot be enforced |
| Foundational and operational failures | Unsupported/ambiguous/conflicting dependency transition; reachable typed provider problem; exception before the application result exists | Supported-domain result versus semantic abstention versus operational failure, with real producer reachability |

Exact wheel compatibility is a candidate missing investigation responsibility, not an automatic implementation prerequisite. Its evidence path must establish the relevant target's compatibility; static runner/Python declarations or current-host wheel tags cannot stand in for it. Source-build/install execution remains outside this plan's admission and must not be added merely to close a fallback question.

These are contrast families, not a fixture count or a completed decision matrix. Combine equivalent cases only when no independent semantic/proof distinction is lost.

### Supporting-investigation contrasts are constraints, not a repair backlog

Use established correctness findings only where they pressure the same synthesis/action-permission boundary. Examples may include:

- real command arguments versus comments/quoted data that the current recognizer incorrectly admits;
- coherent revision/attempt evidence versus recorded mixed-evidence sequences;
- a grounded but uncorroborated model-derived claim, independently supported evidence, and no returned semantic claim;
- a required discriminating check versus an optional informational check, including a competing material concern;
- a typed provider problem versus an exception that prevents application-result construction;
- favorable-looking narrow results with insufficient discovery/context evidence versus a case satisfying every admitted favorable-action prerequisite, if such an action is supported.

These contrasts are **not automatically implementation prerequisites** and do not turn this plan into the owner of reliability repairs.

For each such finding, ask only:

```text
Does this finding materially constrain an action permission used by the first synthesis method?
```

If **no**, keep it in the supporting investigation and continue synthesis.

If **yes**, choose the smallest accepted response:

```text
consume a proven upstream fix
OR
enforce a supported-input restriction
OR
withhold the affected permission
```

Do not rerun the entire supporting investigation campaign or repair unrelated defects merely to complete this pressure sequence.

Use actual producer/composition seams when a reliability contrast is required. Preserve the distinction among proposed semantic examples, executable synthetic proofs, and observed public cases. Reuse the separate investigation's exact inputs and proof limits rather than treating those findings as already repaired.

The objective is not to invent one rule per case. Use these states to expose whether the method has a coherent responsibility-level contract.

**Output:** the affected-action dependency dispositions alongside the same matrix. No second reliability tracker is needed.

**Exit:** every evidence premise used for an emitted action is supported or enforceably restricted at its actual owner; blocked premises remain unavailable. Unrelated repairs and investigation questions remain with their separate workstream.

### Accept synthesis semantics

Promote only the durable accepted rules to the appropriate specification owner, with dated reasoning/provenance preserved in working memory.

Do not implement while the difference among the first method's admitted actions remains semantically ambiguous.

**Output:** the accepted matrix and owner references, the minimum input/output contract, first-version available/unavailable actions, and explicit proof debt. Choose the stable specification owner using the acceptance gate above. Do not copy the entire proposal or matrix into a specification.

**Exit:** accepted semantics are promoted, necessary producer changes/restrictions are identified and scoped, and there is a concrete first Build slice with its proof boundary. The plan's existence or Ali's authorization to refine it is not evidence that these semantic choices have been accepted.

For each substantive design slice, complete the root A → B → C → D → E learning cycle proportionately. Preserve the engineering finding and cycle state in the active record, teach from the actual contrast, and use Ali's response to repair gaps before moving to the next substantive decision. Live selection remains in `MEMORY.md`.

## Implementation sequence after semantic acceptance

Only after the semantic gate is resolved:

1. resolve any separately authorized, action-critical producer handoff/reliability prerequisite at its existing owner, or prove the accepted restriction; do not construct fictional normalized inputs downstream;
2. create the smallest cohesive synthesis/domain owner rather than embedding decision policy in `cli.py`;
3. consume the typed investigation result or a deliberately smaller stable synthesis input derived from it, preserving necessary identity, authority, and investigation outcome;
4. implement the accepted transparent composition and return one typed synthesis result;
5. connect it through the normal application boundary without reimplementing mechanism-specific semantics;
6. render the action, decisive reasons, uncertainty, required checks and claim limits from that result; presentation must not independently select a different action;
7. expose the minimum machine-readable state needed for B2 proof/traceability and preserve detailed evidence alongside the recommendation.

Source filenames/package placement are execution decisions and should follow current ownership/architecture evidence rather than this plan pre-creating a package hierarchy.

## Proof obligations

Focused controlled tests must establish at minimum:

- each Charter outcome actually supported by the first admitted method has an explicit tested permission boundary;
- outcomes deliberately unavailable in the first method cannot be emitted accidentally;
- unresolved/missing/conflicting evidence cannot produce a stronger action than the accepted semantics allow;
- unsupported dependency input does not guess;
- mechanism-specific applicability is not overwritten by synthesis;
- candidate-discovery incompleteness is not silently treated as “no other impact exists”;
- a specific targeted-check action names the discriminating maintainer-facing check rather than generic investigation prose;
- `defer`, `investigate or block`, and `abstain` remain distinguishable when the accepted semantics require them;
- acquisition problems remain traceable through the synthesis reason set;
- exact repository/PR/revision/dependency identity survives the synthesis boundary;
- the human output makes the action, decisive reasons, uncertainty, required checks, and claim limits understandable;
- no output says or implies “safe” merely from green CI or one non-applicable mechanism;
- equivalent normalized evidence does not change decision meaning merely because its source representation differs;
- behavior is not hardcoded to known package/repository/version/case identities.

The focused proof must also establish that:

- recorded selection is not mistaken for pending work, and absence of reselection is not treated as resolution or proof of no useful investigation;
- admitted remaining product investigation is not silently outsourced as a maintainer check, while a supported execution boundary can leave a useful maintainer check;
- each required action/sub-disposition/reason/check/evidence relationship is coherent, not merely composed of individually valid enum values or references;
- when defer is supported, its future-condition evidence and rerun trigger are present; generic missing evidence does not satisfy them;
- known affected evidence cannot authorize an action through an unenforced “trusted input” assumption;
- no returned model claim is not converted into “no relevant risk,” and uncorroborated model-derived evidence cannot independently justify a less cautious action;
- required checks remain prerequisites in the typed result and human explanation;
- competing reasons are handled by the accepted semantics rather than input ordering;
- equivalent evidence reordered or represented through different supported source forms does not change decision meaning, and secondary material concerns survive selection;
- each advertised acquisition-failure outcome is reachable through normal composition, or remains explicitly an operational error outside synthesis;
- if merge remains unavailable in the first method, favorable-looking controlled inputs cannot accidentally emit it;
- supporting correctness findings not required by an admitted action remain outside this implementation rather than becoming accidental scope expansion.

After focused tests:

```text
synthesis owner tests
→ application/investigation integration tests
→ CLI/output tests
→ nearest affected evidence/impact regressions
→ full deterministic suite
```

Run a safe live read-only public-PR proof only after deterministic contrast tests establish the method is not fixture-specific and only when the live claim depends on network evidence.

Document-only planning validation consists of owner/link consistency, readable Markdown, whitespace checks, and the existing governance doctor. It proves document integrity, not action semantics, runtime behavior, learner ownership, or correction of any input defect. Do not rerun the product suite merely because plan prose changed.

## Future LLM comparison boundary

The LLM proposal remains a candidate outside this implementation. Keep the deterministic method runnable. Re-entry requires an observed responsibility-level limitation, a bounded hypothesis, frozen cases/rubrics, explicit cost/failure/rejection conditions, and separate admission under the Charter. Neither heterogeneity nor anticipated rule growth proves the baseline inadequate.

If re-entry is earned, distinguish these comparisons where relevant:

1. deterministic decision and deterministic report;
2. the same decision with bounded model-assisted reporting;
3. model-assisted selection among explicitly justified alternatives, with deterministic constraints and fallback.

This separates decision improvement from communication improvement. Better maintainer comprehension/actionability may justify report assistance even when the action is unchanged; attractive wording alone is not measured utility. A model selecting materially different permitted actions owns part of recommendation policy and must be admitted/evaluated as such.

Before adopting any permission-envelope/validation design, define what its checks actually establish. Action membership, schema validity, existing reference IDs, and mandatory-field presence do not establish that arbitrary model prose follows from the evidence. Bind action, sub-disposition, decisive reasons, checks and evidence relationships; distinguish mechanically checkable constraints from semantic quality that remains model-derived and requires evaluation. Avoid a validator that merely reconstructs the entire decision system after the model. Preserve model-origin premises through both synthesis stages.

Use the smallest representation and ordinary composition justified by that future experiment. This plan does not pre-create the proposal's named classes, model calls, retries, framework, or separate permission engine. Framework re-entry needs its own demonstrated orchestration pressure. After comparison, record adopt, retain-as-pilot, reject, or defer at the owning checkpoint; baseline completion alone does not automatically select the experiment.

## Pass condition

This responsibility passes when evidence shows:

```text
current heterogeneous PublicPullRequestInvestigation state
→ accepted transparent synthesis semantics
→ explicit first-version outcome scope
→ coherent decision matrix
→ deterministic bounded synthesis implementation
→ one typed overall sufficiency/action result
→ traceable human-facing action or abstention
→ materially different controlled outcomes proven
→ focused + nearest + full deterministic suites green
→ no objective-safety or automatic-maintainer-action claim
```

Completion does not require every Charter outcome to be emitted by the first method. It requires every **implemented** outcome to have an accepted, evidence-backed permission boundary and every deliberately unavailable stronger outcome to remain impossible to emit accidentally.

## Stop line

Stop this plan when one bounded B2 synthesis method can transparently produce the admitted first-version maintainer action/abstention states required by the first credible public-PR flow and the method has been pressure-tested against heterogeneous real current evidence shapes.

Then re-evaluate the B2 vertical-slice gate. Do not automatically continue into:

- more impact mechanisms;
- completion of every separate correctness-investigation item;
- broader repository-policy modeling;
- advanced learned/LLM synthesis;
- persistence/evaluation-corpus expansion;
- B3/B4 breadth;
- framework/agent experimentation.

Open any of those only when the remaining B2/core outcome shows a concrete blocking responsibility.

## Maintenance

Change this plan only when the synthesis responsibility, semantic-acceptance gate, first-version outcome scope, decision-matrix requirement, execution sequence, proof obligations, pass condition, or stop line changes. `MEMORY.md` alone owns the exact live continuation and current evidence status.

`UP-SKILL:upgradepilot-planning-design`
