# Product Direction and Maintainer Utility Investigation Plan

**Status:** admitted planning/investigation responsibility; implementation requires separate authorization.
**Responsibility:** compare action-led, advisor-led and hybrid dependency-update assistance, select a justified product sequence, and reconcile its execution owners.
**Project route:** [Evidence-Derived Learning and Building Plan](UPGRADEPILOT_90_DAY_PLAN.md).
**Product boundary:** [Project Charter](../PROJECT_CHARTER.md).
**Live selection:** [MEMORY.md](../MEMORY.md) alone.
**Procedure:** Planning/Design with the canonical Learning-by-Doing cycle.

## 1. Question and completion outcome

For a maintainer reviewing a public Python Dependabot update, which sequence best delivers useful, evidence-backed assistance: earn an action first, explain findings and next checks first, or combine an independently useful report with actions when positively justified?

Hybrid means findings, evidence, limits and justified next checks remain useful even when no final action permission is earned. It does not mean two competing decision engines, general autonomous repository work, or weaker action permissions.

Complete this investigation with:

- a source-grounded comparison using contrasting existing real cases;
- an explicit preferred direction, its counterarguments and remaining user-value uncertainty;
- the smallest admitted outcome and its important omissions;
- a disposition for the existing journey/synthesis/runtime/experiment plans;
- one selected follow-up plan or one exact unresolved decision with a discriminating check;
- correct promotion to the route, specification or ADR only where its responsibility changes.

Plan preparation is not independent usefulness validation. A defensible direction can be selected for a bounded trial while its value remains unproven.

## 2. Owners and entry evidence

Stable semantics remain in the [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md), [Core Pipeline](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) and [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) specifications. This plan does not redefine them.

Use the [unbounded review](../working-memory/2026-10-02_1855_unbounded-product-capability-and-improvement-review.md), [AUDIT-009](../audits/2026-10-02_AUDIT-009_post-runtime-state-delta-readiness.md), and exact normal producer → investigation → CLI/synthesis source as the initial evidence basis. Reconcile material changes before comparison; do not rerun an entire audit merely because the session changed.

Focused additional inputs:

- [Evidence/AI architecture proposal](../proposals/2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md): discovery, context and method alternatives, not adoption authority.
- [Run preservation/replay proposal](../proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md): export, capture, replay and recovery are distinct promises.
- [Report development evaluation](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md): development cases and rubric, not measured product utility.
- [Action-led journey](END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md) and [synthesis plan](OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md): retain their useful action proof obligations without inheriting their presentation ordering automatically.

The unbounded review pins the unmerged simulation research branch and its state-proof handoff. Inspect its exact revision when using its Python marker, prior-sync, already-satisfied or selected-extra observations. Neither branch reachability nor a simulation conclusion proves current automated capability. Missing branch evidence stays unavailable; do not silently merge research to obtain a convenient case.

## 3. Comparison method

First write the maintainer task in plain language: understand what matters about the exact proposed update and choose a justified next step. Distinguish a useful explanation, a proposed check, an admitted action and an executed repair.

| Alternative | First independently assessable outcome | Main benefit | Main risk / rejection pressure |
| --- | --- | --- | --- |
| Action-led | One normal-path positively justified action with reasons | Direct operational disposition; clear permission gate | Useful evidence/reporting may wait indefinitely for a stronger action premise |
| Advisor-led | Findings, sources, unknowns and justified next checks | Assistance can be useful before final decision closure | A polished report may leave all important reasoning to the user or produce speculative checks |
| Hybrid | Advisor output plus independently admitted action/abstention | Retains report value and action discipline | More projection/policy complexity; vague output can obscure what the engine actually established |

The hybrid route is the initial engineering hypothesis, not a predetermined evaluation winner. Explicitly consider retaining the action-led route or narrowing to an evidence explorer if the cases do not justify stronger assistance.

Use at least three distinct responsibility pressures rather than three near-duplicate package updates. Prefer existing cases such as:

1. Pydantic/Soup Sieve: exact acquisition with static CI and degraded semantic-provider evidence;
2. Kubernetes Dashboard Token API/HTTPX or glyphsLib/pytest: Docker or shell/environment continuity limits;
3. CARLA/OpenCV wheel fallback or Freqtrade/scikit-learn persisted state: distinguish published artifacts from actual target/environment/history evidence.

These are development/design cases. Select exact inputs, revisions and proof class before judging outputs. A historical curated packet may teach richer semantics than the normal producer supplies; mark that difference. Never inject simulation conclusions into normal input as though acquired by the product.

For each case and alternative record:

- facts normally supplied, omitted and unresolved;
- what the user could learn or do, with exact supporting evidence;
- action/check prerequisites that remain absent;
- whether the apparent benefit requires a new producer, clearer presentation, or better reasoning;
- the cheapest credible way to discriminate competing explanations;
- error risk, traceability, adoption friction and maintenance consequences.

A proposed check must identify the unresolved proposition, plausible observations and their interpretation. If producers cannot justify such a check, a truthful limitation may be the only supported output. Do not call every unknown actionable.

### Inspectable comparison rubric

Apply the same rubric to all three alternatives, first per case and then in a cross-case synthesis. Each judgment must cite exact case/source evidence, explain its consequence, and distinguish observed behavior from a design expectation or untested user-value hypothesis. Record missing evidence as **unknown**, not as a weak result. Freeze these criteria before inspecting comparative outputs; justify any later revision and apply it to every alternative.

| Dimension | Qualitative judgment | Evidence / question to record |
| --- | --- | --- |
| Maintainer utility | Strong / moderate / weak / unknown | What important reasoning or next-step burden does this remove? Independent utility evidence or only a plausible benefit? |
| Truthfulness / claim discipline | Preserved / at risk / violated / unknown | Are identity, uncertainty, coverage strength and action prerequisites preserved? Where could false confidence arise? |
| Normal-producer reachability | Strong / moderate / weak / unknown | Which useful outputs are normally reachable now, conditional, or dependent on curated inputs? |
| New evidence burden | Low / moderate / high / unknown | Name the missing proposition, extra producer/observation and proof needed; distinguish presentation work from evidence acquisition. |
| Coverage dependency | Low / moderate / high / unknown | How much value survives incomplete impact/runtime coverage, and which material omissions defeat it? |
| Evaluation feasibility | Strong / moderate / weak / unknown | Can independent review discriminate useful, faithful output from plausible prose? Name the oracle/reviewer and practical access gaps. |
| Complexity / maintenance | Low / moderate / high / unknown | What additional policy, projection, storage or coordination must be maintained versus the simplest credible baseline? |
| Reversibility | Strong / moderate / weak / unknown | Can the trial be rejected or changed without losing evidence or committing to a costly public contract/migration? |
| Learning / product leverage | Strong / moderate / weak / unknown | What reusable understanding or capability does it establish for the maintainer/product? Keep learner mastery separate from AI-produced artifacts. |

Strong means the stated responsibility is substantially supported, moderate means a meaningful but conditional or partial contribution, and weak means little supported contribution or a material obstacle. Burden judgments describe concrete required work, not imagined future scale. Labels organize reasoning; they are not scores, votes or additive weights. Preserve case disagreements instead of averaging them away.

## 4. Capability relationships and activation

| Responsibility | Entry condition | Proof responsibility | Owning route |
| --- | --- | --- | --- |
| Report, saved-result boundary and usefulness study | Direction comparison justifies independent report value; report contract can be specified | Faithful normal-path projection, reopenable result and separately adjudicated usefulness | [Prepared report plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md) |
| Broad impact discovery | A material omitted impact family threatens the selected user outcome | Structural/semantic/combined comparison with omission-sensitive protected cases | Reuse AI research; prepare a bounded discovery plan only on selection |
| Runtime/coverage expansion | A real-case missing fact materially changes a finding, check or admitted action | Correct revision/environment/time scope; static inference versus observation comparison | Reuse specialist plan where scope fits; reconcile changed entry conditions first |
| Maintainer action | One permission has normally reachable positive premises | Accepted action semantics and closest-defeater contrasts | Existing synthesis plan |
| Migration assistance | A known relevant breaking change and credible independently verifiable remedy | Before/after behavior with independent oracle and review | Separate bounded plan on activation; Charter review if product/effect boundary changes |
| Planner/agent reuse | Adaptive inquiry is needed and fixed-route baseline is inadequate | Requalified experimental contracts and comparative benefit | Existing planner/orchestration experiment plans |

Report usefulness and discovery experiments need not await a non-abstention action. Conversely, a report does not earn action permission. Experiment repair is necessary before relying on affected comparisons; it is not a universal prerequisite to direction or report design.

The larger horizon remains visible: grouped/transitive changes, other bots/ecosystems, private repositories, remediation and integrations. Their omission from the first selected trial is temporary non-admission, not a conclusion that they lack value. Re-enter through demonstrated user need, missing capability and explicit Charter/authorization reconciliation where appropriate.

## 5. Owner reconciliation and decision gate

Prepare a short direction decision with: selected user outcome, compared alternatives, exact case evidence, assumptions, counterevidence, admitted first responsibility, deferred capabilities and reassessment trigger. Preserve it in the cycle record; promote stable accepted conclusions to their normal owners.

Include the completed rubric for each alternative and explain which dimensions actually discriminate the choice. A truthfulness violation or an unsupported action premise excludes that proposed output regardless of other benefits; an unresolved risk needs a concrete mitigation/proof gate. Weak current reachability does not automatically reject a valuable future direction, but its missing producers and evidence cost must be explicit.

Select the smallest trial with a credible maintainer benefit, preserved claim discipline, and a feasible independent evaluation route. Defend it against the strongest competing alternative and the most adverse case; state what observation would reverse the preference. Three development cases support a trial choice, not a general utility claim. If alternatives remain indistinguishable or a decisive dimension is unknown, leave the direction open and select one practical discriminating check rather than declaring a winner by intuition.

The decision must resolve:

1. whether useful reporting before action admission is the selected delivery trial;
2. whether saved-result export is required in that trial, and precisely what replay is deferred;
3. which report/check requirements need specification work before Build;
4. whether the previous journey is retained, revised, narrowed or explicitly superseded;
5. which outcome would justify expansion or rejection.

Do not create a universal program owner above the Charter and project route. Add a staged plan family only when separately selected responsibilities have different gates/dependencies and one plan would obscure them.

## 6. Allowed changes, proof and stop

Allowed: planning records, focused plan/route/navigation reconciliation and explicitly necessary semantic-design documents within the user's planning authorization. Any accepted product-semantic change must be decided visibly through its specification/Charter owner; a new plan cannot silently accept it.

Not authorized by this plan: product/experiment/test implementation, target execution/mutation, dependencies, model substitution, database/service/framework adoption or unreviewed ecosystem expansion.

Planning validation checks: references resolve; each responsibility has one owner; entry/exit dependencies are coherent; no current-state claims outside MEMORY.md except dated evidence; proposed output facts/checks trace to producers; report usefulness is not conflated with action permission; omitted capabilities have an honest cost and re-entry condition.

Pass means the comparison and chosen trial are sufficiently grounded to select an execution responsibility, or the unresolved decision has one practical discriminating check. It does not mean hybrid value, model accuracy or production readiness has been measured.

Stop after the direction decision and owner reconciliation. Build begins only through separate authorization and its substantive procedure. MEMORY.md records selection; the cycle's D/E checks understanding and records deferred learning/proof without inventing closure.
