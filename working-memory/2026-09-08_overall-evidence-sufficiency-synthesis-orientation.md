# Overall Evidence Sufficiency and Maintainer Action Synthesis — Orientation Working Memory

**Date:** 2026-09-08  
**Session status:** ACTIVE — September 10 proposal reconciliation and authorized plan refinement recorded; investigation-to-synthesis handoff precedes further action pressure; semantic acceptance remains open
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-08_artifact-serviceability-integration-proof.md`](2026-09-08_artifact-serviceability-integration-proof.md)

## Why this responsibility is now earned

The prior artifact-serviceability integration plan is closed with deterministic WSL proof. The normal application path now carries two materially different technical mechanism families:

```text
Python-support-drop
+
artifact-serviceability
→ heterogeneous mechanism-specific evidence/applicability state
```

The parent B2 foundation explicitly says to stop deepening those mechanisms once credible heterogeneous technical state exists and identify the concrete synthesis/output blocker.

The B2 vertical-slice owner names the next responsibility as:

```text
technical candidate results
+ CI/evidence authority
+ relevant repository/context evidence
+ residual uncertainty
→ overall sufficiency assessment
→ bounded recommendation or abstention
```

## Stable owners recovered

### Charter

`PROJECT_CHARTER.md` fixes the broad supported action family:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

It also prohibits objective-safety claims, repository mutation, and replacement of maintainer judgment.

### Product Decision Model

`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` owns technical-candidate/applicability/investigation semantics and explicitly stops before mature synthesis/policy.

Its boundary is:

```text
INVESTIGATION
Should we acquire more evidence, what next check is worth pursuing,
and has worthwhile investigation stopped?

LATER SYNTHESIS / POLICY
Given all candidates, repository context, observations, failures, and remaining uncertainty,
is the overall evidence state sufficient for a maintainer-facing output and how do policy/
residual-risk considerations affect that output?
```

The specification says that mature synthesis contract is intentionally outside its current accepted scope until separately admitted and accepted.

### Current implementation

`PublicPullRequestInvestigation` currently returns detailed typed evidence/results, including:

- dependency result;
- CI coverage;
- package/upstream evidence and problem states;
- Python-support impact/investigation/relevance state;
- artifact candidate/Target/applicability state.

It does not contain an overall sufficiency or maintainer-action result.

The CLI renders the evidence at its typed proof strength and deliberately does not manufacture an overall recommendation.

There is no current top-level synthesis/decision module in `src/upgradepilot/`.

## Historical source material

`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md` remains superseded and non-controlling, but it contains useful earlier pressure around:

- action-relative sufficiency;
- explicit unresolved/conflicting states;
- reasons/checks/claim limits;
- preserving acquisition problems;
- avoiding a generic safety score;
- controlled contrasts before a live proof.

Those ideas must be re-evaluated against the now-richer real implementation rather than copied as accepted semantics.

## Planning conclusion

A new consequential plan is justified because:

1. this is a new B2 responsibility with several semantic and implementation decisions;
2. the stable synthesis contract is not yet accepted anywhere;
3. wrong action semantics could cause overclaiming at the product boundary;
4. the current heterogeneous evidence finally provides enough real pressure to design the method from implementation truth rather than one fixture.

Created plan:

`plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`

## Current unresolved design questions

The immediate design responsibility is **not** source code. It is to define and pressure the smallest synthesis contract around the actual current typed states.

We must resolve:

1. What exact typed result should represent one Charter action or abstention, sufficiency/readiness, decisive reasons, residual uncertainty, required targeted checks, and claim limits?
2. What is the minimum sufficiency-state model that does not collapse actionable gaps, unresolved/conflicted state, and unsupported cases?
3. What are the permission/stop boundaries for the five Charter outcomes?
4. Which repository/context evidence is genuinely needed now, if any, beyond the current investigation result?
5. How should multiple mechanism results combine without an opaque score, double counting, or false candidate-discovery completeness?
6. Should accepted synthesis semantics extend the current Product Decision Model specification or live in a separate focused synthesis specification?

## Simplest credible baseline

Start with deterministic transparent composition over typed state:

```text
owned typed evidence/result state
→ explicit sufficiency/action conditions
→ bounded action or abstention
→ decisive reasons + unresolved limits/checks
```

Do not start with an LLM, graph, generic policy engine, numeric score, or agent planner.

## First semantic pressure pass

The first pass suggests that the five Charter actions should be distinguished by **what the current evidence is sufficient to justify**, not by a generic risk score.

### Merge after normal review

Tentative meaning:

```text
current admitted evidence is sufficient to continue ordinary maintainer review
without a known decision-critical unresolved/conflicted/material established concern
inside the supported B2 reasoning boundary
```

This must remain a bounded recommendation, not a claim that the update is safe or that candidate discovery is globally complete.

A complete comparison with no artifact-serviceability candidate can support this action for that mechanism; it does not prove no other mechanism exists.

### Run targeted checks

Tentative meaning:

```text
a specific unresolved decision-relevant proposition remains
+
a concrete maintainer-facing check could materially discriminate it
+
that check is sufficiently specific and justified to recommend now
```

This must name the actual check/target. Generic “test more” or “investigate further” is not enough.

This action is distinct from UpgradePilot's own automated-investigation selection: the product may have reached its execution boundary while still having enough evidence to recommend a concrete maintainer check.

### Investigate or block

Tentative meaning:

```text
an established applicable material concern
OR a decision-critical conflict/uncertainty is strong enough that proceeding normally
would be too strong until resolved
```

The first pass described this as stronger than `run targeted checks`. The supervision review corrected that assumption: a targeted check can itself be a prerequisite to proceeding. The distinction must be established from the proposition, justified maintainer action and competing reasons, rather than a universal severity ordering.

### Defer

Tentative meaning:

```text
the case is inside the admitted product domain
but a decision-critical condition is temporarily unavailable/pending/not yet mature enough
for a stronger action
+
a later rerun or external state change could reasonably improve the decision
```

Examples may include temporary provider unavailability or pending evidence, but this must be pressure-tested. `defer` should mean “not now; revisit when the blocking state changes,” not generic uncertainty.

### Abstain

Tentative meaning:

```text
the product cannot responsibly select another supported action at the current method boundary
```

Likely triggers include unsupported/out-of-domain input or a state where the method lacks a defensible action mapping and no more specific bounded recommendation is justified.

Abstention is not failure. It is the explicit product behavior when UpgradePilot lacks authority to decide more strongly.

## Sufficiency-model insight from the first pass

A separate global `sufficient/insufficient` boolean appears too weak because evidence can be:

```text
sufficient to recommend a targeted check
but insufficient to recommend normal review
```

or:

```text
sufficient to justify blocking
while still leaving technical uncertainty unresolved
```

Therefore **sufficiency is action-relative**.

Current hypothesis:

- the selected action itself should encode what the evidence is sufficient to justify;
- the result should preserve decisive reasons, residual uncertainty/conflict, required checks, and claim limits;
- a separate top-level sufficiency enum should be added only if pressure tests show it carries non-duplicative semantics.

Do not freeze this hypothesis yet.

## Pressure against current heterogeneous states

First-pass mapping to test further:

```text
no material established concern + adequate admitted evidence
→ possible merge-after-normal-review candidate

established applicable material concern
→ investigate-or-block candidate

artifact candidate + exact applicability unresolved
→ targeted-check / defer / block depends on whether a concrete discriminating check exists,
   whether the gap is temporary, and how decision-critical the candidate is

complete artifact comparison + no candidate
→ mechanism contributes no bounded artifact concern; does not establish global absence

CI supported_not_correlated
→ useful bounded CI evidence, but not runtime step correlation or safety proof

CI unresolved/no successful CI
→ may weaken normal-review permission; exact action depends on whether the gap is actionable,
   temporary, or method-limiting

provider/acquisition problem
→ likely defer if temporary/retryable and decision-critical; abstain if method cannot responsibly
   proceed or classify the case more specifically

unsupported dependency transition
→ abstain/unsupported rather than guess

heterogeneous results with different finality
→ strongest decision-critical unresolved/established concern may constrain action, but synthesis
   must not flatten everything into one score

unresolved candidate + no further UpgradePilot-executable investigation
→ does not become not-applicable; may still support targeted maintainer check, defer, block, or
   abstain depending on evidence/action semantics
```

## Remaining design pressure before acceptance

The first pass is coherent enough to continue but not yet stable enough for specification promotion.

Next design questions:

1. Define the boundary among `run targeted checks`, `investigate or block`, and `defer` using concrete current evidence states.
2. Define positive evidence and bounded-coverage prerequisites for `merge after normal review`; if they cannot be justified and enforced, leave merge unavailable initially. Claim limits alone do not establish permission.
3. Decide what repository/context evidence is minimally required before any favorable action can be emitted.
4. Decide the minimal typed result fields after action semantics stabilize.
5. Then choose the stable specification owner and promote accepted semantics before implementation.

Do not implement until those semantics are accepted and promoted to the correct stable owner.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`


## Supervision review incorporated — 2026-09-08

Ali requested review of this plan alongside the separate limitations investigation, then explicitly requested that the necessary additions be written and pushed. Review baseline was `eec75a18efd79c37e744622e5e1be08c3d050754`. The judgment was to continue semantic design with focused guidance before specification acceptance and implementation, not restart the responsibility.

Updated the existing plan with:

- a dependency on assessing the relevance of the three [reproduced input-integrity findings](2026-09-08_system-limitations-and-correctness-investigation.md), without importing their repairs into this workstream automatically;
- positive favorable-action prerequisites and explicit permission to withhold merge in the first method;
- explicit model-origin/grounding/corroboration and negative-inference contrasts under the existing Core rules;
- required-check semantics and competing-reason pressure, correcting the earlier assumption that targeted checks are necessarily optional;
- a distinction between typed acquisition problems and exceptions that prevent the application result from reaching synthesis;
- one semantic acceptance checklist, concrete additional contrasts and corresponding proof obligations.

These are planning requirements, not accepted synthesis semantics, completed repairs or new runtime proof. A supported-input restriction must be enforceable in the real producer path; neither a disclaimer nor a fictional input projection resolves missing identity. The initial method may support a subset of Charter actions. No action mapping, source package, new database, framework or broad reliability overhaul was selected.

The main workstream retains ownership of semantic design and its acceptance gate. The separate investigation retains its own record and outstanding questions. No product source/tests, stable specification or live MEMORY.md was changed by this review incorporation.

Review-incorporation learning cycle:

A — DONE: explained why input integrity and action-relative permission matter before synthesis consumes existing typed state.
B — DONE: amended the plan and corrected this orientation's targeted-check/favorable-action wording.
C — DONE: preserved review origin, changes and limitations here.
D — explanation supplied; learner response pending. Useful question: why can a valid typed finding still be insufficient to permit a favorable recommendation?
E — design may continue through the revised acceptance checkpoint; implementation remains behind that gate.

Documentation validation passed: local Markdown links, balanced code fences, `git diff --check` and governance doctor. These checks do not establish semantic acceptance or product correctness.

Provenance for review incorporation: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`.

## Learning-by-Doing semantic finding — 2026-09-10

During the first synthesis-design learning step, Ali challenged the practical meaning and product value of the Charter outcome `merge after normal review`.

The discussion exposed a material semantic risk: if interpreted literally as “UpgradePilot tells the maintainer to do the same normal review they already perform and then merge,” the outcome both understates UpgradePilot's added value and can overstate UpgradePilot's authority by sounding like a final merge decision.

Current **design finding, not yet accepted stable semantics**:

```text
The favorable outcome should represent:

bounded UpgradePilot investigation completed
+
no UpgradePilot-specific escalation is justified by the admitted evidence state
↓
return the PR to the repository's ordinary maintainer review process
```

The product value is therefore not the phrase “normal review” itself. The value is the preceding evidence work and decision compression:

```text
collect and preserve relevant evidence
→ identify or eliminate bounded technical concerns at their owned proof strength
→ surface material uncertainty and missing evidence
→ decide whether a special targeted check / investigation / defer / abstention is justified
→ when none is justified, communicate that no additional UpgradePilot-specific escalation is warranted
```

This must remain distinct from stronger claims:

```text
no UpgradePilot-specific escalation warranted
!= update proven safe
!= all possible impact mechanisms exhausted
!= repository review requirements already satisfied
!= maintainer should merge immediately
```

The existing Charter label `merge after normal review` remains controlling until stable product semantics are deliberately changed through the correct owner. During synthesis design, consider whether the accepted internal/action semantics should be expressed more clearly as something like `proceed_with_normal_review` or another term that preserves the Charter outcome while avoiding an implication that UpgradePilot owns the final merge decision.

This finding strengthens the existing requirement that each synthesis action must have an explicit operational meaning and positive permission boundary before implementation. It should be revisited when the decision matrix reaches the favorable-action row; do not freeze a rename or Charter change from this working-memory note alone.

LbD state for this finding:

```text
A — favorable action wording/value problem identified and grounded in Charter boundaries
B — semantic design finding established; no stable rule or source implementation selected
C — finding preserved in active working memory
D — learner challenge materially corrected the working mental model
E — return to the first artifact-serviceability reasoning point, carrying this action-authority distinction forward
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`

## First artifact-serviceability synthesis pressure — 2026-09-10

The first concrete Learning-by-Doing pressure case used the current artifact-serviceability implementation rather than a hypothetical policy example.

Observed current technical state:

```text
published wheel capability loss = established
exact target wheel compatibility = unresolved
artifact-serviceability applicability = unresolved
```

The important proof boundary is that the established package-level candidate does not itself establish target exposure. Static Target artifact-environment facts such as runner, setup-Python declaration, or dependency-installation declaration also do not establish the exact target-supported wheel-tag set.

Ali reasoned that this state should lead to a **targeted check** because the missing proposition is concrete and discriminable: establish exact target wheel compatibility and use it to determine whether the target had an old compatible wheel path that is absent from the proposed release.

Current **provisional synthesis mapping, not yet accepted stable semantics**:

```text
material candidate established
+
applicability unresolved because one exact decision-relevant proposition is missing
+
a concrete bounded check can discriminate that proposition
↓
run targeted checks
```

This pressure also clarified that `targeted check` is intentionally broader than `targeted test`. A test may be one acquisition method, but synthesis should identify the proposition/check needed rather than prematurely prescribe a technical mechanism unless that mechanism is itself established and justified.

The case currently argues against stronger or less useful outputs:

```text
proceed/merge-style favorable action
→ too strong because a material candidate remains unresolved

investigate or block
→ not established merely from candidate existence; target applicability is still unresolved

defer
→ weak fit when a concrete discriminating check is already known and available

abstain
→ weak fit because UpgradePilot can still provide a useful bounded next action
```

This is one pressure-tested state family only. It does not yet establish a universal targeted-check rule across all mechanisms or failure states.

### Consequence depth exposed by the same case

Ali then correctly identified the next possible proposition if target wheel-path loss becomes established: whether a proposed source distribution (`sdist`) offers a usable fallback.

Preserve the distinction:

```text
proposed sdist exists
!=
source build/install succeeds on the relevant target
```

Therefore even after wheel-serviceability loss is established, the final consequence may remain unresolved when a source fallback exists but its target viability has not been established. This may produce another concrete targeted-check situation, but that mapping must be pressure-tested rather than assumed.

## Open semantic finding: `investigate` versus `block` — 2026-09-10

Ali challenged the Charter-facing outcome `investigate or block` because the two terms can encode materially different maintainer operations.

Current distinction to pressure-test:

```text
investigate
→ a material concern, conflict, or unresolved state warrants broader evidence gathering,
   but no single bounded targeted check is yet sufficient to resolve the decision

block
→ current evidence is already sufficient to recommend that normal progression stop,
   at least until a stated condition/evidence change occurs
```

These are related rather than literal opposites: investigation can be the work performed while progression is withheld. However, combining them into one undifferentiated runtime action could hide whether UpgradePilot is primarily recommending **more inquiry** or an actual **stop disposition**.

Do **not** resolve this from wording alone. The next design work must pressure-test at least these possibilities:

```text
A. retain one Charter-facing `investigate or block` outcome,
   but preserve an explicit internal/sub-disposition distinction;

B. conclude that one runtime outcome can still represent both because the user-facing
   reasons/checks make the operational distinction sufficiently explicit;

C. if real cases show the distinction changes product behavior materially and cannot be
   represented cleanly under the current outcome, propose refinement at the correct stable owner.
```

No Charter, plan, or stable specification change is justified yet. This remains an open synthesis-design finding to be evaluated through the decision matrix and concrete evidence states.

### Current continuation

Resume the artifact-serviceability pressure path rather than branching into a detached naming exercise:

```text
exact target wheel-path loss established
+
proposed sdist exists
+
source-build/install viability unresolved
↓
pressure whether another concrete targeted check is justified,
and contrast that state with one where a concern is already strong enough to stop normal progression
```

That contrast should help sharpen both the targeted-check boundary and the `investigate`/`block` distinction.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`

## Planner / investigation → synthesis boundary correction — 2026-09-10

A later Learning-by-Doing review deliberately re-opened the previous bounded `EvidenceGapPlanner` work and the parent B2 investigation owner before continuing synthesis. This exposed an important responsibility boundary that must constrain the earlier provisional targeted-check mappings.

The earlier planner responsibility is **adjacent to synthesis but not the same decision owner**:

```text
mechanism/domain evaluation
→ what is currently known about a technical proposition/candidate?

EvidenceGapPlanner / investigation responsibility
→ what decision-relevant evidence gap remains?
→ is another UpgradePilot-executable investigation worthwhile/admissible?
→ execute/select it or preserve a justified stop/no-action state

later overall synthesis
→ given the resulting heterogeneous evidence, repository/context evidence,
   acquisition/problem state and residual uncertainty,
   what maintainer-facing action or abstention is justified?
```

The Product Decision Model / parent B2 responsibility further requires three distinct questions to remain separate:

```text
EPISTEMIC INVESTIGATION VALUE
Would another observation materially discriminate the owned proposition?

UPGRADEPILOT EXECUTION ADMISSIBILITY
May UpgradePilot itself perform that investigation within its supported capability,
security, authorization and environment boundaries?

MAINTAINER-FACING RECOMMENDABILITY
After considering the resulting investigation state, should the maintainer be asked
to perform a concrete check?
```

The third question belongs to later synthesis/action reasoning. Therefore an unresolved proposition plus a useful check does **not by itself** justify the Charter action `run targeted checks`.

### Correction to the earlier targeted-check pressure

The earlier artifact-serviceability pressure remains useful, but its provisional mapping was incomplete. The corrected pressure sequence is:

```text
specific decision-relevant proposition unresolved
+
concrete discriminating observation/check exists
↓
first ask whether UpgradePilot still has a justified executable investigation for it
```

Then:

```text
justified UpgradePilot-executable investigation exists
→ investigation/planner responsibility should pursue or select it first
→ synthesis should consume the resulting state rather than prematurely outsource it

no further justified UpgradePilot-executable investigation
OR the useful check lies outside the supported UpgradePilot execution boundary
+
the maintainer can perform one concrete, decision-relevant check
→ `run targeted checks` becomes a plausible synthesis action candidate
```

This does not imply that every missing proposition must be automated. It prevents synthesis from silently converting a missing UpgradePilot investigation responsibility into maintainer work.

The source-fallback example must therefore be re-read conditionally:

```text
wheel-path loss established
+ proposed sdist exists
+ source-build/install viability unresolved
↓
first determine whether target-specific source-build/install viability is an admitted,
justified UpgradePilot investigation or lies outside the current execution boundary
↓
only then pressure maintainer-facing targeted-check semantics
```

The earlier historical targeted-check discussion is retained above because it records how the boundary was discovered. This section supersedes any reading of that earlier provisional mapping as a complete permission rule.

## Mechanism conclusion != overall maintainer action

The same review strengthened another boundary already implied by the parent plan:

```text
mechanism-specific established concern
!= automatic top-level `block`
```

For example:

```text
target-specific artifact-serviceability loss established
```

can be a valid technical conclusion without by itself establishing that the overall maintainer action must be `block`. Overall synthesis must still consume the materially relevant repository/context evidence, other mechanism results, evidence quality/authority, investigation state and residual uncertainty required by the accepted action semantics.

Likewise, an established concern should not be weakened merely because other mechanisms report no concern. The synthesis task is to preserve heterogeneous proof strength and determine which action is **permitted by the whole decision-relevant state**, not to average mechanism outputs.

This yields the architecture-level mental model:

```text
technical mechanism truth
→ investigation / evidence-gap state
→ heterogeneous evidence handoff
→ overall action permission
```

## Deterministic synthesis authority remains the V1 baseline

The planner review also raised whether maintainer-action selection should itself become an LLM/planner decision. Current design finding: **no evidence presently justifies that move**.

The first synthesis implementation should remain a deterministic, inspectable decision model over trusted typed state:

```text
owned typed evidence / investigation / context state
→ explicit action permission + prohibition conditions
→ one bounded Charter action or abstention
→ decisive reasons
+ unresolved questions/conflicts
+ required maintainer checks when applicable
+ claim limits
+ evidence/provenance references
```

This should be **spec-driven deterministic composition**, not an arbitrary pile of coding-time `if/else` guesses. The decision matrix and accepted specification should establish the permission boundaries before implementation.

An LLM may later contribute around this authority boundary where independently justified — for example, proposing investigations, interpreting bounded messy context, or helping render explanations — but:

```text
LLM/model recommendation
!= trusted permission to emit a maintainer action
```

Do not reopen ordinary-Python/LangGraph/LangChain planner/framework work merely because synthesis is now being designed. A future re-entry requires evidence that the deterministic synthesis baseline is materially inadequate or that another independently useful AI responsibility has been earned.

## Resulting handoff question and revised continuation

The previous `Current continuation` above is now superseded as the active route by this more precise design step.

Before finalizing decision-matrix rows for individual maintainer actions, identify the **smallest typed investigation/planner → synthesis handoff state** needed to distinguish at least:

```text
proposition/candidate final vs non-final
useful discriminating investigation exists vs none identified
UpgradePilot-executable/admissible vs outside execution boundary
selected/attempted investigation state where relevant
successful semantic result vs typed acquisition/problem result vs operational failure
retry justified vs no blind retry
no further justified UpgradePilot-executable investigation
concrete maintainer-facing check available vs none
```

Do not invent a new generic planner or duplicate existing owned state merely to create this handoff. First inspect which of these facts are already represented by current Product Decision Model / `PublicPullRequestInvestigation` contracts and identify only genuine synthesis-input gaps.

Then resume action pressure with the corrected sequence:

```text
current heterogeneous evidence
+ investigation/planner handoff state
+ required repository/context evidence
↓
action-relative sufficiency
↓
explicit permission/prohibition conditions
↓
Charter action or abstention
```

These are **design findings and corrected pressure-test boundaries, not accepted stable synthesis semantics**. No Charter, stable specification, plan, source/tests, or `MEMORY.md` change is authorized by this record alone.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`

## Proposal reconciliation and authorized plan refinement — 2026-09-10

Ali requested a repository synchronization, governance review, and independent examination of the two September 10 proposals alongside this discussion. After receiving the findings, Ali explicitly requested modification of the existing synthesis plan to incorporate the useful material and make progression concrete. This authorizes the planning refinement and necessary continuation records, not product implementation or automatic acceptance of proposed action semantics.

### Evidence recovered before the edit

The review fetched all configured remotes/tags and fast-forwarded `main` from `81f83f96` to `da8c4223d08ec6b4f8aed651fc5306da25c64654`. Local HEAD matched `origin/main` and the working tree was clean at that checkpoint. The incoming changes were two proposal files, this working record, and the selected plan; no product source changes were included.

Read both proposals in full:

- [Overall synthesis investigation](../proposals/2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md), recorded against `c4c08ea`;
- [LLM-assisted synthesis proposal](../proposals/2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md), recorded against `409fcc8`.

Reconciled them with Charter/Core/Product Decision Model/Minimum Useful Generality rules, the selected and parent plans, actual investigation/CLI/mechanism/provider source, and focused tests. The first proposal's prominent targeted-check examples do not consistently include the later investigation-handoff correction, although later sections recognize the distinction. Neither proposal's labels, classes, architecture, or action matrix becomes accepted by reference.

The source adds a concrete handoff distinction: `investigate_public_pull_request` retains `python_support_drop_investigation_selection` from the pre-acquisition assessment after performing the read and reevaluation. It is a recorded selection, not necessarily pending work. Calling `select_python_support_drop_investigation` on a post-acquisition assessment can instead return `None` with unresolved applicability. Preserve attempted action, resulting knowledge/problem, and justified or unknown continuation rather than interpreting either field in isolation.

Verification at `da8c4223d08ec6b4f8aed651fc5306da25c64654`:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m unittest tests.test_investigation tests.test_python_support_impact tests.test_artifact_serviceability tests.test_ci_dependency_coverage -q
```

Result: **53 tests passed**. Separately executed the three inspected Python reproducer blocks preserved in the [correctness investigation record](2026-09-08_system-limitations-and-correctness-investigation.md), using the same virtual environment with `-B` and `PYTHONPATH=src`. Each diagnostic prohibits real Requests network calls and verifies source hashes remain unchanged.

- Static commands: both the comment-only requirement and quoted-separator text still earned `observed`, `supported_not_correlated`, and one Target association; real/unrelated/echo-only controls retained their expected distinctions.
- PR correspondence: a same-count patch from simulated head B was still accepted and attributed to captured head A; stable-head and count-mismatch controls remained distinct.
- Workflow attempts: captured successful attempt 1 combined with mixed-success/failure jobs from attempt 2 still produced `supported_not_correlated`; coherent failed attempt 2 produced `unresolved`; wrong-run identity was rejected.

These are bounded synthetic reproductions, not fixes, live incidents, frequency estimates, or overall recommendation failures. Passing the focused suite does not establish the absent integrity guarantees. Restrictions must follow every dependent claim, including cautious recommendations; merely disabling favorable output does not repair an incorrect transition-to-revision binding.

### Planning changes and reasoning

Refined the existing [synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md), preserving its deterministic-first scope and specification-before-implementation gate:

- Put the minimum producer-grounded investigation handoff before action mapping, with concrete source anchors and a compact fact/owner/reachability map as its output.
- Added ordered semantic contrasts and explicit outputs/exits for design steps. Separate candidate existence, exact target applicability, source-fallback consequence, and competing material concerns.
- Required coherent action/sub-disposition/reason/check relationships, maintainer feasibility, bounded coverage, necessary repository context, and evidence for deferral/freshness claims.
- Removed the illustrative first-version action subset as a potential implied selection. Every emitted action needs accepted permission; favorable output and defer can remain unavailable, but supported public input behavior must still be defined.
- Made reliability restrictions claim-dependent and kept repairs with existing owners. Operational failures remain distinct from semantic abstention; hypothetical inputs do not prove normal producer reachability.
- Added focused handoff/composition proof requirements while preserving normal integration/CLI/nearest/full validation after implementation. Document-only validation does not require another product test campaign.
- Kept LLM synthesis outside implementation scope with an observed-limitation admission trigger. A later comparison should distinguish deterministic output, model-assisted reporting with a fixed decision, and model-assisted action selection. Selection among materially different permitted actions remains policy influence. Schema/reference checks do not prove arbitrary prose follows from evidence; relationship checks and semantic evaluation have separate proof limits.

The LLM validation concern is also consistent with [JSONSchemaBench](https://arxiv.org/abs/2501.10868), inspected during review, which evaluates output quality separately from schema compliance. That research does not establish that an LLM improves UpgradePilot synthesis. Report assistance may earn admission through measured comprehension/actionability even when it does not change the action; fluent wording alone is insufficient.

Reconciled `MEMORY.md` with the later September 10 discussion and this plan refinement. The earlier dated findings above remain historical/provisional evidence. No proposal, Charter, stable specification, source/test, framework, or external target was changed. No commit or push was performed by this refinement.

### Validation and learning handoff

Planning validation passed: 18 local Markdown links across the three changed documents, code-fence balance, unique plan headings, `git diff --check`, focused cross-file/owner review, and `.venv/bin/python -B tools/agent-governance/governance_doctor.py` (PASS). An initial whitespace check flagged two edited Markdown hard-break lines; those trailing spaces were removed before the passing check. No product tests were rerun for the prose changes. These checks establish document integrity, not semantic acceptance, learner ownership, or corrected product behavior.

```text
Slice: reconcile proposals into the bounded synthesis plan
A — DONE: oriented the handoff-first sequence and distinction between planning requirements and accepted action semantics.
B — DONE: revised the existing plan with evidence-based constraints, concrete contrasts, outputs, gates and future-method boundaries.
C — DONE: preserved review evidence and reasoning here; reconciled the compact live continuation in MEMORY.md.
D — explanation supplied; learner response PENDING: why can a recorded selected check not alone tell synthesis whether more product investigation remains?
E — PENDING: repair any gap from Ali's response, then orient the bounded handoff map before resuming artifact action pressure.
```

As of this handoff, the next substantive design slice is the map for Python declaration acquisition and the artifact exact-compatibility gap. Existing source observations can be reused; no broad restart or generic planner is needed. The semantic matrix is not yet accepted and source implementation remains unselected.

Provenance: `UP-SKILL:upgradepilot-repository-audit` and `UP-SKILL:upgradepilot-workstream-supervision` for the preceding review; `UP-SKILL:upgradepilot-planning-design` and `UP-SKILL:upgradepilot-working-memory` for this authorized refinement.
