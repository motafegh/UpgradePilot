# Overall Evidence Sufficiency and Maintainer Action Synthesis Plan

**Status:** admitted bounded planning/execution responsibility; live selection remains owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) Phase-7 synthesis handoff  
**B2 flow owner:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Accepted synthesis semantics:** [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)  
**Current decision-model boundary:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Supporting correctness owner:** [`SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)  
**Product-simulation evidence authority:** [`../product-simulation/AGENTS.md`](../product-simulation/AGENTS.md) and [`../product-simulation/README.md`](../product-simulation/README.md)  
**Historical source material only:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)

## Authorization and position neutrality

This plan coordinates the admitted synthesis responsibility and the producer/evidence prerequisites that materially constrain it. Updating the plan authorizes planning and directly necessary planning records only. Source/test implementation still requires the normal Build/Implement authorization and proof route.

`MEMORY.md` alone selects what is live. This plan may record durable dependency/order relationships and cite dated completed evidence, but it must not become a second owner of the exact current step, branch head, test result, or handoff.

The September 10 synthesis investigation and LLM-assisted proposal remain non-controlling design inputs:

- [`../proposals/2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md`](../proposals/2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md)
- [`../proposals/2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md`](../proposals/2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md)

Their illustrative classes, field names, action mappings, framework choices, and architecture are not adopted by reference.

## Responsibility

Define, incrementally implement, and prove the smallest transparent synthesis path that consumes already-earned heterogeneous investigation state and emits one bounded maintainer-facing action or honest abstention without manufacturing safety, completeness, provenance, or certainty.

The Charter owns the public outcome family:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

The accepted maintainer-action synthesis specification owns the stable framework-independent permission semantics. This plan owns execution coordination:

```text
trustworthy producer evidence
+ mechanism-specific technical results
+ investigation/continuation state
+ admitted repository/context evidence
+ acquisition/problem states
↓
action-relative evidence sufficiency
↓
one positively justified Charter action OR abstention
↓
decisive reasons + residual uncertainty + checks/re-entry conditions + claim limits
↓
traceable human/machine presentation
```

The plan does not redefine mechanism-specific applicability or investigation semantics and does not treat synthesis as a generic risk score.

## Reconciled implementation baseline

The plan originally began before stable synthesis semantics and before any synthesis evaluator existed. Dated evidence now establishes a later baseline that future work must consume rather than rediscover.

### Stable synthesis semantics are already accepted

[`../working-memory/2026-09-11_synthesis-stable-semantic-acceptance.md`](../working-memory/2026-09-11_synthesis-stable-semantic-acceptance.md) records the acceptance of a distinct maintainer-action synthesis specification. The durable rules include:

```text
action sufficiency is action-relative
+ every emitted action needs positive permission
+ actions are not a severity ladder
+ missing/unsupported/correctness-limited evidence cannot satisfy permission
+ semantic availability and producer reachability are distinct
+ deterministic transparent composition is the baseline
```

The combined Charter family `investigate or block` retains the accepted internal distinction `investigate | block`.

A new action permission that changes stable semantics must be reconciled with the specification owner. A producer/reachability implementation that merely satisfies already-accepted semantics does not require re-specifying those semantics in this plan.

### The deterministic evaluator exists but is intentionally abstention-only

`src/upgradepilot/maintainer_action.py` now provides the first bounded synthesis result and evaluator. Its public action type currently admits only:

```text
abstain
```

The evaluator preserves decisive reasons, residual uncertainty, limitations, claim limits, and the source investigation. No non-abstention permission is implemented merely because the action exists in the Charter.

This is a preparatory baseline, not completion of the overall synthesis responsibility.

### Exact CI run/job attempt coherence is a completed producer prerequisite

The dated run-attempt working memory records the repair of the earlier mixed-attempt risk. Exact job acquisition now binds the frozen PR head, workflow run ID, run attempt, and jobs from that same attempt.

Do not reopen this responsibility without concrete regression evidence. The completed repair proves same-attempt run/job identity; it does not by itself prove static-step identity, dependency installation, artifact choice, compatibility, or maintainer action.

### Bounded CI static↔runtime correlation is a completed producer foundation

[`../working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`](../working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md) records the first admitted bridge:

```text
exact-head static workflow declaration
+ exact-attempt runtime jobs/steps
+ bounded unambiguous name/order correlation
→ static user-defined step ↔ runtime step identity
```

`src/upgradepilot/ci/dependency_exercise.py` now distinguishes:

```text
supported_not_correlated
supported_runtime_correlated
```

The stronger state means an already-supported static consuming step is safely related to a runtime step that GitHub reports completed/successfully, with visible `continue-on-error` masking excluded. It still does not prove exact resolved dependency version, selected wheel/sdist, exact artifact tags, behavioral compatibility, complete target coverage, or any maintainer action.

Unsupported matrix/reusable/dynamic-name shapes remain conservative correlation limits rather than guessed positives.

## Product-simulation evidence and case-admission discipline

Use product simulation as an independent discovery and pressure-testing arm:

```text
real / real-derived evidence
→ discovered distinction or failure pressure
→ main Planning/Design evaluates transfer
→ accepted stable rule, if any, moves to its correct owner
→ implementation follows only through the normal Build gate
```

Historical case actions are evidence from their recorded question/evidence horizon; they are not runtime policy.

### High-value transfer anchors

Retain these design-pressure roles:

- **S003** — block-like proposal hold: present proposal failure/constraint conflict can be established strongly enough to withhold normal progression without proving permanent incompatibility.
- **S004/S005** — favorable bounded-review pressure: favorable output depended on positive identity/evidence/target closure, not merely `nothing bad found` or green CI.
- **S006** — targeted-check shape: one exact decision-critical unresolved proposition plus one bounded discriminating check, subject to the product-vs-maintainer execution boundary.
- **S007** — investigation staleness/pruning: a previously plausible check can become unnecessary after stronger evidence resolves the owned proposition.
- **S008** — artifact serviceability: wheel-path loss, source fallback, source-build viability, exact target compatibility, and stopping must remain distinct.
- **S009** — repository purpose/provenance context can be decision-relevant without becoming technical applicability.
- **S010** — multiple mechanisms, different target handling, context, and bounded discovery coverage pressure cross-candidate synthesis.
- **S011** — an owned coverage/environment question can be settled while deeper compatibility remains unresolved.
- **S012** — concrete historical/provenance evidence can be required while the useful evidence responsibility remains outside current product capability.
- **Conversation-C / Buildtest-OpenSSL pressure** — unresolved state can remain honest when no sufficiently authoritative supported investigation remains; do not fabricate activity.
- **Cactus #198 screening evidence** — broader adaptive inquiry can be materially different from a fixed targeted-check set and from an already-established block condition.
- **B2/X1 no-tool transfer** — disposition depends on the owned question, evidence, admitted capabilities, action history, and known outside responsibility; unresolved state alone does not select an action.

### Real, real-derived, synthetic, and source/test evidence must remain distinguishable

Every contrast used to admit or change an action permission must be identifiable as:

```text
real public/preserved evidence
real-derived controlled variant
synthetic/generated semantic control
current source/test implementation evidence
```

Synthetic controls may isolate a branch or falsify a heuristic, but they do not establish public-case prevalence, production reliability, a new domain capability, or a maintainer-action permission whose positive prerequisites have not survived real/real-derived pressure.

### New simulation work is gap-driven

Do not create another numbered case merely because a new implementation question appears. First establish:

1. the exact product-semantic/evidence question;
2. which existing cases/evaluations were checked;
3. why they do not discriminate the remaining alternatives;
4. what evidence could change the decision;
5. the least artificial adequate case/control form;
6. the claim limit and stop condition.

## Accepted action-permission model

The action family is pressure-tested enough that future work should focus on producer reachability and trustworthy evidence rather than repeatedly redefining the basic action meanings.

| Charter action | Accepted positive-permission shape | Important prohibition / current pressure |
|---|---|---|
| `merge after normal review` | positive bounded identity/evidence/coverage/context closure for the stated recommendation horizon; no material stronger-action condition remains | absence of a known concern, one non-applicable candidate, or green CI is insufficient; current generic discovery/context coverage is not generally producer-grounded |
| `run targeted checks` | one or a small stable set of exact decision-critical unresolved propositions plus concrete bounded maintainer-performable discriminating checks; no justified UpgradePilot-executable investigation should perform the same work first | generic uncertainty is not a check; missing product automation does not automatically outsource work |
| `investigate or block` — investigate | material target-relevant concern plus grounded broader/adaptive inquiry with concrete scope and stopping/pruning logic; no independent current-proposal hold condition established | unresolved state, missing CI, major-version severity, or incomplete discovery alone do not justify investigate |
| `investigate or block` — block | material exact proposal-level problem/constraint/failure established strongly enough that normal progression should be withheld for the current proposal as-is | block is proposal-relative, not permanent incompatibility; other investigation may aid remediation but is not required to justify the hold |
| `defer` | decision-critical unresolved state plus no justified current UpgradePilot investigation plus a specific useful outside/future responsibility/condition and concrete re-entry trigger | generic insufficient evidence or missing capability is not defer |
| `abstain` | no stronger action is positively justified and no grounded useful targeted check, broader inquiry, or specific defer responsibility can be supported | abstain is not a negative safety finding and must preserve uncertainty/claim limits |

Do not convert this into a total severity order.

## Relationship with supporting correctness work

The separate system-limitations/correctness plan remains the owner of broad detection and classification. This synthesis plan consumes only established findings that materially constrain an action permission or a producer premise it needs.

For every material affected premise choose the smallest sound response:

```text
verified upstream repair
OR
enforceable supported-input restriction at the actual owner
OR
withhold the affected permission
```

A disclaimer, manually fabricated trusted fixture, or downstream identity label does not enforce provenance in the normal path.

The 2026-09-12 E inventory distinguishes four classes:

```text
correctness / provenance defect
→ can create wrong or misattributed evidence

evidence / architecture bottleneck
→ remains conservative but blocks a stronger useful claim

deliberate safety / coverage limit
→ intentionally rejects unsupported/ambiguous cases

future product / observability gap
→ useful capability not yet implemented
```

Do not treat all four as one backlog or remove conservative limits merely for breadth.

## Reliability reinforcement route

When the synthesis path relies on a producer whose evidence can currently be false or misattributed, correctness reinforcement outranks feature expansion. The following ordered route is durable because later stronger evidence should not be layered on top of known incorrect premises. `MEMORY.md` still selects when each bounded child responsibility is live.

### Frozen-revision coherence for requirements/constraints evidence

**Problem:** `PullRequestIdentity` freezes base/head SHAs, but the requirements/constraints extraction path consumes patch text from the mutable PR changed-files endpoint. The provider passes the frozen identity object, yet the endpoint request itself is keyed only by repository/PR number and the current completeness check verifies file count rather than patch-to-SHA correspondence.

Failure shape:

```text
identity captured at head A
+ PR advances to head B
+ changed-file count remains equal
+ changed-file patch now reflects B
→ B dependency transition can be attributed to revision A
```

This is a provenance/snapshot-coherence defect, not merely missing feature coverage.

**Bounded responsibility:** ensure every admitted requirements/constraints dependency transition used downstream is provably tied to the investigation's frozen base/head snapshot.

**Design must remain open until the child A-phase compares the smallest sound mechanisms.** Candidate mechanisms may include exact base/head file acquisition and comparison, an exact commit comparison source, or another producer-level method that actually proves correspondence. Do not freeze a repair merely because current code already has a patch parser.

**Likely owners/evidence:**

- `src/upgradepilot/github/pull_request.py`
- `src/upgradepilot/github/repository.py`
- `src/upgradepilot/dependency/analysis.py`
- `src/upgradepilot/dependency/requirements.py`
- focused provider/dependency/application tests

**Proof obligations:**

```text
stable frozen snapshot
→ supported requirement transition remains correctly extractable

head changes A → B between identity and mutable PR-file reads
→ no B patch can be accepted/stamped as A evidence

same changed-file count across the race
→ must not bypass the protection

exact-file uv.lock / admitted pyproject paths
→ remain correct and unregressed

unsupported/ambiguous file forms
→ continue to stop explicitly rather than guess
```

**Stop line:** repair revision correspondence only. Do not add CI/log interpretation, wheel semantics, action permission, reporting redesign, or general repository snapshot infrastructure unless the selected mechanism genuinely requires a smaller shared owner.

### Static shell/direct-install semantic correctness

**Problem:** bounded command-text splitting can currently promote install-looking text inside comments or quoted separator payloads into positive direct-requirements consumption.

Confirmed pressure includes shapes such as:

```text
pip install -r requirements-dev.txt                 → valid positive shape
pip install wheel # -r requirements-dev.txt         → must not become positive requirements consumption
echo "note; pip install -r requirements-dev.txt"    → must not become positive requirements consumption
```

The runtime-correlation bridge can amplify this defect: correct proof that a step ran does not repair a wrong static interpretation of what the step meant.

**Bounded responsibility:** define and implement the smallest sound command-recognition boundary that prevents known false positives inside the supported syntax domain while preserving explicit unresolved/unsupported behavior for shell forms the product cannot interpret safely.

Do not assume a full shell parser is necessary. Compare narrower grammar/support restrictions and parser mechanisms under the Ceremony Tax and Minimum Useful Generality rules.

**Likely owners/evidence:**

- `src/upgradepilot/dependency/direct_install.py`
- related workflow command/context owners
- dependency-CI/Target consumers that rely on positive direct-install evidence
- focused false-positive/true-positive/application integration tests

**Proof obligations:** comments/quoted data/separator payloads cannot satisfy positive installation semantics; admitted real install declarations remain supported; ambiguous syntax remains unresolved rather than guessed; the stronger runtime-correlated CI path cannot promote a false static semantic premise.

**Stop line:** command meaning only. Do not combine this repair with matrix support, logs, exact package installation proof, Target redesign, or maintainer-action admission.

### Reassess resilience only after fresh discrimination

CI/provider acquisition failure containment remains a source-traced architecture risk: an exception can prevent later independent evidence and leave no `PublicPullRequestInvestigation` for synthesis. The E inventory did not fresh-reproduce every current-main failure class after the recent CI work.

Treat this as:

```text
source-traced resilience risk
→ run the smallest fresh discriminating proof when it becomes decision-relevant
→ only then classify/repair
```

Do not label it a confirmed current defect merely from historical source pressure.

## Evidence/architecture bottlenecks after correctness is trustworthy

Correctness repair does not imply that every conservative evidence gap should immediately be expanded. Reassess these against the next decision-critical proposition.

### Preserve the already-known consuming job into Target composition

Current supported CI consumption evidence can already identify an exact static `job_key`, while Target artifact-environment interpretation can re-solve job selection from the whole workflow and return ambiguity under its conservative one-job rule.

Potential direction:

```text
CI-supported exact consuming job
→ preserve that relationship through application composition
→ interpret target facts for that exact job
```

Before implementation, trace earliest sufficient ownership and ensure CI identity does not become Target semantics. This is a composition bottleneck, not currently classified as false-evidence behavior.

### Produce exact runtime dependency/artifact evidence only for a selected proposition

The current bridge does not reveal:

- exact dependency version resolved/installed;
- wheel versus sdist selection;
- artifact filename/tags;
- resolver/install output;
- exact runtime target tags.

Job logs, workflow artifacts, or another runtime source may become justified only after selecting the precise proposition they must establish. Do not add a generic log-ingestion subsystem merely because the data exists.

### Exact target wheel compatibility remains without a normal producer

Artifact-serviceability owns an exact compatibility concept, but the normal application does not currently produce the exact target wheel-tag witness needed to make that proof concrete. Static runner/Python declarations are not exact wheel tags.

Treat this as an upstream evidence-production responsibility. Do not weaken the compatibility proposition so current static data can satisfy it.

### Correlation breadth is case-driven

Matrix jobs, reusable workflows, missing/dynamic names, and other excluded static↔runtime shapes remain explicit conservative limitations. Expand only when a real case or a selected product claim requires that breadth and a sound mapping rule is available.

### Other bounded coverage limits remain intentional until pressured

Examples include:

- Target's narrow matrix/container/dynamic setup support;
- Target composition currently centered on direct-requirements consumption;
- bounded dependency-source formats and single coherent transition selection;
- finite changed-file acquisition bounds.

A conservative unsupported result is not a defect merely because a wider implementation is imaginable.

## Durable journey / dependency order

The following sequence is the preferred dependency order when the corresponding work is selected. It is not the live-state owner.

```text
accepted synthesis semantics
+ abstention-only evaluator
+ exact-attempt CI identity
+ bounded static↔runtime correlation
        ↓
repair frozen-revision requirements/constraints provenance
        ↓
repair static command-recognition false positives
        ↓
re-audit the evidence path and retire/supersede corrected trust restrictions
        ↓
select the next decision-critical evidence bottleneck
    ├─ exact consuming-job → Target composition
    ├─ exact runtime version/artifact witness
    ├─ exact target wheel compatibility producer
    └─ another bounded producer gap proven more important
        ↓
re-evaluate non-abstention action reachability
        ↓
admit one action path at a time through normal producer proof
        ↓
application/CLI/machine-readable integration for admitted paths
        ↓
reassess the first credible public-PR synthesis flow
```

The order is intentionally **not**:

```text
support every GitHub/Python shape
→ collect every possible runtime datum
→ then decide what the product needs
```

## Incremental non-abstention action admission

No non-abstention action should be implemented merely to complete the vocabulary. For each action, trace:

```text
accepted semantic permission
→ exact required premises
→ normal producer(s)
→ application composition
→ trust/provenance restrictions
→ synthesis evaluator
→ human/machine output
→ focused positive + defeater proof
```

### `run targeted checks`

Before enabling:

- derive one exact decision-critical maintainer check or stable small set;
- prove why its possible observations materially change the recommendation;
- prove why an admitted UpgradePilot-executable investigation should not perform the same work first;
- preserve interpretation/stopping/reassessment conditions.

S006 is the primary shape pressure, not an automatic runtime rule.

### `investigate`

Before enabling:

- prove a material grounded concern;
- produce a broader/adaptive inquiry whose next evidence action can depend on intermediate findings;
- provide concrete scope and stopping/pruning logic;
- show no independent current-proposal hold already makes block sufficient.

Cactus #198 supplies design pressure but not a frozen runtime recommendation.

### `block`

Before enabling:

- prove an exact proposal-level hold condition through trustworthy normal producers;
- preserve proposal-relative claim limits;
- prove that further inquiry is not required to justify withholding the current proposal as-is.

Do not infer block from an applicability enum, model-grounded quote, major-version number, green/red CI label, or artifact wheel-loss candidate alone.

### `defer`

Before enabling:

- prove a decision-critical unresolved proposition;
- prove no justified admitted UpgradePilot investigation can currently resolve it;
- identify a specific useful outside/future responsibility or condition;
- preserve a concrete re-entry/reassessment trigger.

Missing capability alone is not defer.

### `merge after normal review`

Before enabling:

- prove exact identity/trust for all decisive evidence;
- positively establish the bounded evidence/mechanism/context horizon relied upon;
- close or explicitly show non-defeating status for all decision-critical concerns inside that horizon;
- prove known blind spots do not defeat the bounded favorable permission;
- preserve residual uncertainty and claim limits.

`nothing bad found`, green CI, or all currently implemented candidates looking fine is insufficient.

### `abstain`

The existing evaluator remains the honest fallback while stronger permissions are unavailable. Future changes must continue to preserve identity, decisive reasons, material residual uncertainty, limitations, and claim limits. Operational exceptions that prevent an investigation result from being constructed are not automatically semantic abstention.

## Scope

In scope:

- maintain the accepted synthesis input/output contract and positive-permission discipline;
- map required action premises to real producers and authority/provenance;
- coordinate action-critical upstream correctness repairs or enforceable restrictions;
- preserve mechanism-specific technical truth instead of reinterpreting it in synthesis;
- preserve unsupported/unavailable/conflicted states without favorable inference;
- admit the minimum repository/context evidence genuinely needed by a permission;
- pressure action rules with real/real-derived evidence before synthetic convenience;
- add one non-abstention path only when its producer-grounded permission is proven;
- expose accepted synthesis meaning consistently through the application and presentation boundaries;
- prove materially different states and relevant defeaters;
- use the root A→B→C→D→E Learning-by-Doing cycle for each substantive producer/action slice.

## Explicit non-goals

Do not automatically introduce:

- objective upgrade-safety scoring;
- one opaque universal risk/confidence score;
- automatic merge/approval/comment/repository mutation;
- generic repository-wide policy engines;
- universal candidate-discovery completeness claims;
- generic planners, capability registries, workflow engines, graph frameworks, or agent orchestration;
- numeric Value-of-Information optimization;
- persistence/replay infrastructure merely to support the next local repair;
- job-log/artifact ingestion before a precise evidence proposition requires it;
- complete shell grammar support when a smaller sound supported subset is adequate;
- matrix/reusable/dynamic-name correlation merely for breadth;
- arbitrary Target/artifact/CI expansion merely because synthesis observes unresolved evidence;
- package/repository/version/case-specific action rules;
- learned/model-based synthesis before a demonstrated responsibility-level limitation of the deterministic baseline;
- new product-simulation cases without a named surviving evidence gap.

## Producer and action proof obligations

### Correctness/provenance repairs

A repair passes only when it proves the defect is impossible within the admitted supported path, not merely when a happy-path test is green.

For revision coherence, prove the mutable-PR race/constant-file-count contrast cannot misattribute evidence. For command semantics, prove comments/quoted data cannot satisfy positive installation semantics while supported declarations remain recognized.

Each repair must validate focused owners first, then nearest application/consumer regressions, then the full deterministic suite when product code changes justify it.

### Action permissions

For every implemented non-abstention path prove:

- the positive permission through the **normal** producer path;
- removal/contradiction of each material premise defeats or weakens the action correctly;
- correctness-limited evidence cannot satisfy the permission;
- unsupported/missing/conflicting evidence is not silently favorable;
- mechanism-specific applicability remains owned by its domain module;
- candidate/context/discovery limits are not hidden;
- competing material reasons survive selection;
- action/sub-disposition/check/re-entry semantics remain coherent;
- exact repository/PR/revision/dependency identity survives;
- human and machine output represent the same decision;
- no output says or implies objective safety from green CI or narrow negative evidence;
- behavior generalizes across semantic state families rather than S-numbers, repositories, packages, or versions.

### Investigation/operational failure reachability

For any acquisition/problem state advertised as synthesis input, prove that the normal application can actually return it. If an exception prevents `PublicPullRequestInvestigation` construction, keep it as an operational failure unless/until a separately admitted resilience change establishes a typed result path.

## Validation order

For product implementation slices, use the smallest useful narrow-to-broad route:

```text
focused producer/domain tests
→ nearest composition/application tests
→ synthesis evaluator tests where affected
→ CLI/output tests where affected
→ nearest evidence/impact regressions
→ full deterministic suite
```

Safe live read-only public-PR proof is optional and justified only when the claim depends on network behavior that deterministic tests cannot establish.

For plan/spec/working-memory-only changes, validate owner/link consistency, readable Markdown, whitespace, and governance checks when proportionate. Documentation validation does not prove runtime behavior.

## Future LLM comparison boundary

The LLM-assisted proposal remains outside the admitted baseline implementation. Keep the deterministic method runnable and inspectable.

Re-entry requires:

```text
observed responsibility-level limitation of deterministic synthesis
+ bounded hypothesis
+ frozen cases/rubric
+ explicit cost/failure/rejection conditions
+ separate admission
```

Distinguish possible later comparisons:

1. deterministic decision + deterministic report;
2. same decision with bounded model-assisted reporting;
3. model-assisted selection among explicitly justified permitted alternatives, constrained by deterministic evidence/permission boundaries.

Better wording is not evidence of better decision quality. If a model selects materially different actions, it owns part of recommendation policy and must be admitted/evaluated accordingly. A validator that checks only schema/action membership/reference IDs does not establish semantic grounding.

Framework/agent re-entry requires separate demonstrated orchestration pressure; heterogeneity or anticipated rule growth is insufficient.

## Pass condition

This responsibility passes when evidence establishes:

```text
accepted action-relative synthesis semantics
+ trustworthy decisive producer evidence for each implemented action
+ action-critical correctness restrictions repaired or enforceably excluded
+ deterministic bounded synthesis evaluator
+ at least the first credible required maintainer-facing non-abstention path(s) admitted through normal producer proof
+ one typed overall synthesis result preserving reasons/uncertainty/limits
+ coherent application/presentation integration for admitted paths
+ materially different permission/defeater states proven
+ nearest + full deterministic suites green for product changes
+ no objective-safety or automatic-maintainer-action claim
```

Completion does not require every Charter action to be runtime-reachable. It requires every implemented action to have a trustworthy evidence-backed positive permission and every unavailable action to remain impossible to emit accidentally.

Completion also does not require every supporting correctness/capability item to be fixed. Only the producer premises materially needed by the admitted first credible synthesis flow must be trustworthy or enforceably excluded.

## Stop line

Stop this plan when one bounded B2 synthesis method can transparently produce the admitted maintainer action/abstention states required by the first credible public-PR flow and the decisive evidence premises are trustworthy at their claimed proof strength.

Then re-evaluate the B2 vertical-slice gate. Do not automatically continue into:

- every remaining system-limitations item;
- complete GitHub Actions/workflow-shape support;
- more impact mechanisms merely for breadth;
- universal repository-policy/context modeling;
- generic log/artifact ingestion;
- advanced learned/LLM synthesis;
- persistence/evaluation-corpus expansion;
- additional product-simulation cases without a named unresolved evidence gap;
- B3/B4 breadth;
- framework/agent experimentation.

Open later work only when a concrete remaining product outcome establishes its necessity.

## Maintenance

Change this plan only when the synthesis responsibility, accepted semantic owner, producer/trust boundary, reliability dependency order, product-simulation admission relationship, action-reachability sequence, proof obligations, pass condition, or stop line materially changes.

`MEMORY.md` alone owns the exact live continuation and current evidence status.

`UP-SKILL:upgradepilot-planning-design`
