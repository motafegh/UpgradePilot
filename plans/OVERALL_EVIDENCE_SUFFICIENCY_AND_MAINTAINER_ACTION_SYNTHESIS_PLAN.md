# Overall Evidence Sufficiency and Maintainer Action Synthesis Plan

**Status:** admitted bounded planning/execution responsibility; live selection remains owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) Phase-7 synthesis handoff  
**B2 flow owner:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Current decision-model boundary:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Historical source material only:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)

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

This plan does **not** redefine those Charter outcomes. It determines the minimum admitted synthesis contract and method needed to decide among them at the actual current B2 evidence boundary.

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

## Already-owned semantics

The plan must consume, not redefine, these accepted boundaries:

1. **Charter outcome set and claim limits.** The supported action classes are fixed by `PROJECT_CHARTER.md`; the system does not claim objective safety or replace maintainer judgment.
2. **Mechanism-specific technical truth.** Candidate formulation, applicability, investigation, and stopping semantics remain owned by the Product Decision Model and their mechanism modules.
3. **Missing evidence is not negative evidence.** Unavailable/unresolved/unsupported states cannot silently become absence, non-applicability, or a favorable overall action.
4. **Investigation stop is not overall sufficiency.** A candidate may remain unresolved with no further justified UpgradePilot investigation; synthesis must decide separately what maintainer-facing output is justified.
5. **Repository context is not technical applicability.** Material context may affect overall action without being inserted into one mechanism-specific candidate.
6. **Observation, interpretation, and decision remain distinct.** Synthesis consumes attributed evidence/results and must retain their proof class and limitations.

## Unresolved design questions

These are the real questions to resolve before implementation:

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

Define the smallest state model that distinguishes at least:

```text
sufficient for one bounded action
insufficient with a known actionable evidence gap
material unresolved/conflicted state
unsupported/out-of-admitted-domain state
```

Avoid a generic boolean `sufficient` if it collapses materially different stopping/action behavior.

### Action-permission boundaries

For each Charter outcome, determine:

- what the action means operationally;
- what evidence conditions are minimally required;
- what evidence states make the action too strong;
- what unresolved/conflicting states force a weaker action;
- whether the action asks UpgradePilot to acquire more evidence, asks the maintainer to run a targeted check, or simply communicates an abstention/defer/block state;
- what changed evidence requires a rerun.

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

## Semantic acceptance gate

Because the accepted Product Decision Model intentionally leaves mature synthesis/policy semantics open, implementation must not begin until the new stable synthesis semantics are accepted at the correct owner.

The design step must determine whether to:

- extend `UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` with a bounded accepted synthesis section; or
- create a separate focused synthesis specification if ownership would be clearer.

A plan alone must not become the stable semantic owner.

No ADR is required merely for the synthesis rules. Create/update an ADR only if a consequential implementation method or structural commitment is selected beyond ordinary deterministic Python composition.

## Design and pressure sequence

### Recover actual heterogeneous inputs

Trace the current `PublicPullRequestInvestigation` fields and their proof meanings, including:

- dependency problem/supported transition state;
- CI coverage/authority state;
- package/upstream acquisition states;
- Python-support candidate/applicability/investigation state;
- artifact-serviceability candidate/applicability/Target state;
- explicit unavailable/problem/unresolved states.

Record which facts are genuinely synthesis-relevant and which remain presentation/debug evidence only.

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

### Pressure the contract against materially different states

Before source implementation, apply the proposed contract/method to a small diverse controlled set including at least:

1. Python-support established not applicable with no material competing concern;
2. Python-support established applicable or materially blocking;
3. artifact-serviceability candidate with applicability still unresolved because exact target compatibility is unavailable;
4. no artifact candidate after a complete old/proposed comparison;
5. material CI insufficiency/unresolved authority;
6. acquisition/provider problem;
7. unsupported dependency-change input;
8. multiple heterogeneous candidate results with different finality strengths;
9. unresolved candidate with no further UpgradePilot-executable investigation;
10. a concrete case where a specific maintainer-facing targeted check is justified rather than generic “investigate more.”

The objective is not to invent one rule per case. Use these states to expose whether the method has a coherent responsibility-level contract.

### Accept synthesis semantics

Promote only the durable accepted rules to the appropriate specification owner, with dated reasoning/provenance preserved in working memory.

Do not implement while the difference among `run targeted checks`, `investigate or block`, `defer`, and `abstain` remains semantically ambiguous.

## Implementation sequence after semantic acceptance

Only after the semantic gate is resolved:

1. create the smallest cohesive synthesis/domain owner rather than embedding decision policy in `cli.py`;
2. consume the typed investigation result or a deliberately smaller stable synthesis input derived from it;
3. preserve exact identity/provenance needed for traceability;
4. return one typed overall synthesis result;
5. connect it through the normal application boundary without reimplementing mechanism-specific semantics;
6. extend CLI presentation with the bounded action, decisive reasons, unresolved questions/checks, and claim limits;
7. add minimum machine-readable state only if justified by current B2 proof/output needs;
8. preserve the existing evidence report rather than replacing it with only a recommendation line.

Source filenames/package placement are execution decisions and should follow current ownership/architecture evidence rather than this plan pre-creating a package hierarchy.

## Proof obligations

Focused controlled tests must establish at minimum:

- each supported Charter outcome used by the first admitted method has an explicit tested permission boundary;
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

After focused tests:

```text
synthesis owner tests
→ application/investigation integration tests
→ CLI/output tests
→ nearest affected evidence/impact regressions
→ full deterministic suite
```

Run a safe live read-only public-PR proof only after deterministic contrast tests establish the method is not fixture-specific and only when the live claim depends on network evidence.

## Pass condition

This responsibility passes when evidence shows:

```text
current heterogeneous PublicPullRequestInvestigation state
→ accepted transparent synthesis semantics
→ deterministic bounded synthesis implementation
→ one typed overall sufficiency/action result
→ traceable human-facing action or abstention
→ materially different controlled outcomes proven
→ focused + nearest + full deterministic suites green
→ no objective-safety or automatic-maintainer-action claim
```

## Stop line

Stop this plan when one bounded B2 synthesis method can transparently produce the admitted maintainer action/abstention states required by the first credible public-PR flow and the method has been pressure-tested against heterogeneous real current evidence shapes.

Then re-evaluate the B2 vertical-slice gate. Do not automatically continue into:

- more impact mechanisms;
- broader repository-policy modeling;
- advanced learned/LLM synthesis;
- persistence/evaluation-corpus expansion;
- B3/B4 breadth;
- framework/agent experimentation.

Open any of those only when the remaining B2/core outcome shows a concrete blocking responsibility.

## Maintenance

Change this plan only when the synthesis responsibility, semantic-acceptance gate, execution sequence, proof obligations, pass condition, or stop line changes. `MEMORY.md` alone owns the exact live continuation and current evidence status.

`UP-SKILL:upgradepilot-planning-design`
