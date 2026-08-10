# AUDIT-003 — Post-Conversation-C Product Decision-Model Audit — REVIEWED / RECONCILIATION APPLIED

**Audit date:** 2026-08-10  
**Audit type:** whole-product domain-model / evidence-authority / implementation-handoff / proportionality audit  
**Primary inspected C-closure baseline:** `5870fc3962e684f9c19641b467e16da293176bad` (`Sync live memory after Conversation C closure`)  
**Conversation-C closure commit:** `7fedd79ecc97c71d025fd36bc4a0cfc31727a885` (`Close Conversation C investigation-selection reconciliation`)  
**Publication-time `main` baseline:** `989d9234c9a5beea831ac33163fb9c7b5d35c4c2` (`Correct mastery note challenge-branch references`)  
**Primary audited record:** [`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)  
**Disposition at audit time:** preserve Conversations A, B, and C as closed; do not reopen them wholesale; record bounded conceptual amendments, plan-reconciliation requirements, and document-ownership corrections that should be considered before accepted A–C semantics are turned into new product implementation.  
**Authority:** non-controlling audit evidence only. This record does not change the Charter, plan, specification, ADR, implementation, or live continuation. `../MEMORY.md` remains the sole live-state owner.

> **Post-review status — 2026-08-10:** This audit was subsequently reviewed finding-by-finding against the governing project artifacts and current implementation evidence. Its substantive findings were accepted with bounded refinements and applied to the single reconciliation record in commit `4923ca94fc241e4675751c3f251b730f324d11d8`, with the resulting live-state/handoff synchronized in `MEMORY.md` in commit `62962f4a15e516e1643863208943dd03addbab14`. Conversations A/B/C remain closed. This status means the **audit review and reconciliation amendments are complete**; it does **not** mean every downstream recommendation is already implemented. In particular, reconciliation of `B2_TRANSPARENT_DECISION_METHOD_PLAN.md` remains the next live project task owned by `MEMORY.md`.

---

## 1. Audit question

Conversation C was formally closed after two complementary pressure tests and an explicit closure review. The audit question is therefore not:

> Can another reviewer invent more concepts after C closed?

It is:

> **Do the accepted A–C concepts, decisions, pressure-test conclusions, implementation-handoff assumptions, and owning project artifacts remain coherent when challenged against the controlling product boundary, the B2 route, the selected Transparent Decision plan, stable technical invariants, current implementation behavior, and the actual frozen evidence behind the C pressure tests?**

The review intentionally treats all AI-written conclusions as challengeable evidence rather than authority. It also follows the opposite discipline:

> **Do not manufacture defects merely because the model is detailed or unfamiliar.**

A finding is recorded only where a concrete ambiguity, authority leak, coverage gap, plan mismatch, implementation risk, or ownership defect could materially affect later behavior or reasoning.

---

## 2. Scope

### 2.1 Primary inspected responsibilities

```text
Conversation A
technical impact-candidate semantics

Conversation B
candidate-specific applicability propositions
evidence sufficiency / negative inference
open-vs-closed-world reasoning
model / deterministic authority boundaries

Conversation C
uncertainty-location reasoning
discriminating targets
investigation admissibility
qualitative comparison / dominance
pruning / complementarity
adaptive sequencing / escalation
context / contrast / reconstruction fidelity
no-further-investigation semantics
C/D boundary

Post-C handoff
relationship to B2
relationship to the Transparent Decision plan
relationship to Conversation D
```

### 2.2 Project owners and evidence inspected

Primary project records:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)
- [`../AGENTS.md`](../AGENTS.md)
- [`../MEMORY.md`](../MEMORY.md)
- [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)
- [`../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- [`../src/upgradepilot/investigation.py`](../src/upgradepilot/investigation.py)
- selected active tests and bounded implementation evidence needed to test whether the reconciliation contradicts implemented behavior.

Frozen external pressure-test anchors were independently rechecked at their recorded identities:

```text
C01
repository: dominodatalab/container-runtime-interface-api
PR: #101
transition: grpcio-tools ~=1.73 -> ~=1.80
frozen head: 034f0a82e2c06526212353a1258f59f159538914

C203
repository: shahzebsiddiqui/buildtest-1
PR: #74
transition: urllib3 ==1.26.* -> ==2.0.*
frozen head: 73f4cd7024b4afd3c7dd1d19c2202a3aaa1a9719
```

### 2.3 Explicit exclusions

This audit did not:

- modify source, tests, plans, specifications, ADRs, Charter, `MEMORY.md`, or the reconciliation record;
- reopen product-simulation cases or treat product-simulation conclusions as controlling truth;
- run arbitrary target-repository code;
- create a runtime schema, planner, graph engine, scoring system, Boolean AST, or agent architecture;
- decide Conversation D;
- define final maintainer action semantics;
- claim universal ecosystem coverage from the pressure-test set;
- treat passing documentation review as proof of implementation.

---

## 3. Freshness note at publication time

The detailed audit was performed against the post-C closure/live-memory state at:

```text
5870fc3962e684f9c19641b467e16da293176bad
```

Before this audit record was published, `main` advanced to:

```text
989d9234c9a5beea831ac33163fb9c7b5d35c4c2
```

The intervening work created and corrected the cumulative educational A–C learning note and updated live continuation. In particular, the earlier sequencing suggestion:

```text
create cumulative learning note first
```

has already been satisfied and must **not** be treated as an outstanding audit action.

At publication time:

- Conversations A/B/C remain closed;
- Conversation D remains unopened;
- `MEMORY.md` now selects the post-C implementation-handoff decision as the immediate project action;
- the selected `B2_TRANSPARENT_DECISION_METHOD_PLAN.md` remains textually on its pre-reconciliation method structure;
- this audit's substantive model/plan findings therefore remain relevant unless a later commit explicitly resolves them.

Any later assistant using this audit must re-read `MEMORY.md`, the current reconciliation record, and the current selected plan before applying a recommendation.

---

# 4. Executive audit verdict

## 4.1 What passed

The audit did **not** find a foundational reason to discard or reopen the A–C model.

### Conversation A — PASS

The accepted relation remains technically useful and correctly scoped:

```text
UPSTREAM CHANGE
+
TARGET-RELEVANT EXPOSURE/PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET CONSEQUENCE
=
IMPACT CANDIDATE
```

It prevents the invalid shortcut:

```text
dependency changed
=> target affected
```

while admitting direct, multi-hop, framework/plugin, artifact, environment, and dependency-owned paths without freezing a universal taxonomy.

### Conversation B — PASS with a coverage amendment

The proposition-scoped knowledge model remains strong:

```text
established applicable
established not applicable
unresolved
conflicted
```

The following protections are especially valuable and should remain:

```text
applicable != consequence proven
missing evidence != not applicable
non-observation != refutation without justified completeness
source authority != semantic meaning
LLM confidence != evidence completeness
```

### Conversation C — PASS with boundary amendments

The accepted C method remains coherent:

```text
material non-final proposition state
+
uncertainty/conflict location
↓
discriminating target(s)
↓
candidate investigations
↓
hard boundary
↓
qualitative comparison / pruning / complementarity
↓
next check / small conditional bundle / justified stop
↓
observation
↓
evidence validation
↓
proposition reevaluation or candidate refinement
```

The pressure tests stress materially different failure modes and support the main method rather than merely repeating the same topology.

### C closure — KEEP CLOSED

The findings below are **closure amendments / implementation guards**, not evidence that Conversation C must be reopened wholesale.

A/B/C should reopen only if a new implementation or challenge case exposes a genuinely foundational contradiction.

---

# 5. Verified pressure-test grounding

## 5.1 C01 — artifact/code-generation case

The frozen PR really changes:

```text
grpcio-tools ~=1.73
→ ~=1.80
```

at exact head:

```text
034f0a82e2c06526212353a1258f59f159538914
```

The target's frozen `bin/update-proto.sh` invokes:

```text
python -m grpc_tools.protoc
```

against vendored `.proto` inputs and writes generated Python, typing, and gRPC output under committed `src/cri_api` paths.

The frozen CircleCI configuration installs dependencies and runs lint, typing, unit tests, integration tests, and build/publish behavior, but does not explicitly rerun that generation script.

Therefore the pressure-test question:

> Does controlled old-versus-proposed generation produce a materially different generated-artifact set for the same relevant inputs/options?

is grounded in a real artifact-mediated coupling rather than an invented hypothetical.

The case legitimately supports C conclusions about:

- direct interventional discrimination sometimes outranking cheaper static work;
- pruning leverage;
- contrast validity;
- post-execution evidence validation;
- proposal-level effect versus mechanism attribution;
- observations feeding candidate refinement.

## 5.2 C203 — historical environment case

The frozen PR really changes:

```text
urllib3 ==1.26.*
→ ==2.0.*
```

at exact head:

```text
73f4cd7024b4afd3c7dd1d19c2202a3aaa1a9719
```

The Dependabot/upstream evidence includes the urllib3 2.x OpenSSL compatibility change, including removal of support for OpenSSL versions earlier than 1.1.1 and import failure for incompatible OpenSSL.

The exact frozen NERSC/Perlmutter CI path does:

```text
module load python/3.9-anaconda-2021.11
conda create -p ... python=3.9
source activate ...
source setup.sh
pip install ...
run regression tooling
```

but does not preserve an exact historical solved OpenSSL observation such as `ssl.OPENSSL_VERSION`, an explicit environment manifest, solver transaction, or equivalent exact record.

Therefore the pressure-test conclusion that the ideal historical discriminating observation may be unrecoverable is credible. The case legitimately supports:

- proxy evidence narrowing without acquiring exact-context authority;
- reconstruction fidelity as an evidence constraint;
- same command today not implying same historical solve;
- more reconstruction work not automatically producing better evidence;
- a valid `unresolved + no further justified investigation` endpoint.

## 5.3 Audit consequence

Conversation C was not closed on fabricated case premises. The remaining concerns are about the **scope and implementation meaning of its accepted principles**, not the legitimacy of its two closure pressure-test anchors.

---

# 6. Findings

## AUDIT-003-F1 — Candidate formulation must not smuggle established truth

**Classification:** conceptual guard / model-authority boundary  
**Severity:** moderate; should be explicit before generic candidate-generation implementation  
**Disposition:** amend accepted reasoning or implementation contract; do not reopen A.

Conversation A defines an impact candidate using upstream mechanism, target-relevant exposure/path, activation conditions, and possible consequence.

A future semantic candidate generator could accidentally blur:

```text
candidate includes an exposure hypothesis
```

with:

```text
exposure established
```

or:

```text
candidate includes activation condition X
```

with:

```text
X is active in the exact target context
```

Recommended durable guard:

```text
candidate formulation
!= establishment of candidate components
```

and, where useful:

```text
candidate hypothesis
→ B derives/evaluates explicit propositions
→ evidence establishes/refutes/leaves unresolved/conflicted
```

This is already implicit in the A→B separation; the audit recommends making it explicit before implementation can accidentally allow an LLM-generated candidate to self-authorize applicability facts.

---

## AUDIT-003-F2 — Three completeness questions must remain distinct

**Classification:** evidence/negative-inference correctness  
**Severity:** high within future negative/applicability conclusions  
**Disposition:** add explicit coverage guard before generic non-applicability or transition-level negative conclusions.

Conversation B deeply models evidence completeness but later implementation must distinguish at least:

```text
1. EVIDENCE COVERAGE
Did the evidence universe sufficiently cover proposition P?

2. PATH-MODEL COVERAGE
Did the candidate formulation represent the material alternative applicability paths
before claiming every viable path was eliminated?

3. CANDIDATE-DISCOVERY COVERAGE
Did the impact-discovery responsibility find enough material candidates
before making any transition-level "no relevant impact" conclusion?
```

The current B rule:

```text
candidate non-applicable
when every viable applicability path is eliminated
```

is sound only relative to the candidate/path model actually represented.

Failure mode:

```text
reality: (A AND B) OR C
model:   A AND B

B refuted
→ implemented model closes candidate
→ but omitted C was still viable
```

Likewise:

```text
all discovered candidates not applicable
!=
transition has no material target impact
```

unless candidate-discovery coverage is itself justified.

Recommended durable guard:

```text
evidence completeness
!= path-model completeness
!= candidate-discovery completeness
```

and:

```text
candidate-level non-applicability
must not silently become
transition-level absence of impact
```

without an independently justified discovery/coverage boundary.

This aligns with the existing core invariant that absence of a model-derived claim cannot become evidence that no relevant risk exists.

---

## AUDIT-003-F3 — C input must include materially conflicted states, not only `unresolved`

**Classification:** internal semantic consistency  
**Severity:** moderate  
**Disposition:** wording/contract refinement; C remains closed.

Conversation C is repeatedly framed as beginning from:

```text
MATERIAL UNRESOLVED PROPOSITION
+
UNCERTAINTY LOCATION / REASON
```

but its own examples include:

```text
credible evidence genuinely conflicted
```

and Conversation B defines `conflicted` separately from `unresolved`.

A conflict-resolution investigation is clearly within C's purpose.

Recommended formulation:

> **C starts from a material proposition whose justified state still requires discrimination, including unresolved or genuinely conflicted states, plus the location/reason of the uncertainty or conflict.**

No new runtime state is required.

---

## AUDIT-003-F4 — Investigation recommendability and UpgradePilot execution admissibility are different

**Classification:** product-boundary / authorization / targeted-check semantics  
**Severity:** high for B2 targeted-check output  
**Disposition:** must be resolved before C semantics directly control targeted-check recommendation behavior.

Conversation C's hard-admissibility reasoning includes capability availability and safety/security/authorization boundaries.

That is correct for **UpgradePilot executing a check**.

However the Charter's supported maintainer outcome family explicitly includes:

```text
run targeted checks
```

while also prohibiting target-repository mutation and replacement of maintainer judgment.

A check may therefore be:

```text
useful and responsibly recommendable to the maintainer
```

while being:

```text
unavailable or unauthorized for UpgradePilot to execute autonomously
```

Example class:

```text
Run this exact compatibility/regeneration/runtime check
inside the repository's real CI/environment.
```

If C uses one undifferentiated `admissible investigation` concept, it may incorrectly discard a valid maintainer-facing targeted check because the product itself cannot execute it.

Recommended conceptual split:

```text
INVESTIGATION / CHECK RECOMMENDABILITY
Can UpgradePilot responsibly identify and explain this check as a useful next maintainer action?

AUTOMATED EXECUTION ADMISSIBILITY
May UpgradePilot itself execute the check under current capability, safety,
security, authorization, cost, and environment boundaries?
```

The second should normally be stricter.

This amendment preserves the Charter's read-only/non-mutating product boundary while allowing targeted checks to remain a genuine product output.

---

## AUDIT-003-F5 — C needs an explicit non-dominated-alternatives outcome

**Classification:** C/D authority boundary / qualitative decision correctness  
**Severity:** moderate-to-high  
**Disposition:** add as a valid C output before implementing a selector that assumes one unique best investigation.

C correctly rejects fake numerical precision and allows genuine qualitative trade-offs.

Consider:

```text
I1: lower cost / lower invasiveness / adequate discrimination
I2: higher cost / higher invasiveness / materially stronger discrimination
```

Neither necessarily dominates.

The choice may depend on:

- repository policy;
- maintainer risk tolerance;
- urgency;
- available budget/time;
- downstream action stakes.

Those are not all C-owned epistemic facts.

Recommended C result families:

```text
1. selected next investigation / small conditional sequence

2. no further justified investigation

3. multiple admissible non-dominated alternatives;
   preference requires maintainer / policy / later decision-context input
```

C should not manufacture a unique best choice when the residual preference is actually human/policy-relative.

---

## AUDIT-003-F6 — `No further justified investigation` needs a policy-relative cost/value guard

**Classification:** C/D responsibility boundary  
**Severity:** moderate  
**Disposition:** refine D-067-style wording; no reopening required.

C can safely stop when a candidate investigation is:

- impossible;
- unavailable/unrecoverable;
- non-discriminating;
- unsafe;
- unauthorized for the attempted execution boundary;
- incapable of valid context/contrast/reconstruction fidelity;
- unable to produce interpretable evidence for the proposition.

A harder case is:

```text
investigation is admissible and highly discriminating
but expensive / slow / invasive
```

Calling that investigation `disproportionately costly` requires a value comparison:

```text
disproportionate relative to what decision stakes / policy / budget?
```

If C does not own that policy, it should preserve the trade-off rather than invent a universal utility judgment.

Recommended rule:

> C may stop directly on hard inadmissibility or inadequate decision-relevant discrimination. When the remaining issue is a genuine value/cost/risk trade-off among admissible options, preserve the alternatives and expose the policy/maintainer dependency instead of pretending the epistemic method alone determines preference.

---

## AUDIT-003-F7 — Deterministic candidate composition needs minimum four-state semantics before code

**Classification:** implementation readiness / deterministic semantics  
**Severity:** high before generic B composition code  
**Disposition:** define minimum bounded composition rules in the reconciled implementation plan/specification when implementation is selected; do not create a general Boolean engine.

D-044-style reasoning says candidate applicability composition should be deterministic once proposition states and logic are explicit.

That direction is sound.

However implementation still needs bounded behavior for combinations of:

```text
established
refuted
unresolved
conflicted
```

including alternative paths.

Example:

```text
A = established
B = conflicted
C = refuted

A AND (B OR C)
→ ?
```

and:

```text
one complete path established
another alternative path conflicted
→ candidate applicability?
```

A likely principle is that one sufficiently established complete viable path establishes applicability even if an unnecessary alternative remains conflicted, while non-applicability requires closure of all alternatives. But this must be explicitly accepted and tested rather than inferred independently by each implementation site.

The audit does **not** recommend:

- a universal Boolean AST;
- a rule engine;
- a graph framework;
- generic SAT/logic machinery.

Only the minimum deterministic composition semantics required by the bounded implementation should be specified and proved.

---

## AUDIT-003-F8 — Candidate refinement needs lineage rather than silent mutation

**Classification:** provenance / reasoning-history integrity  
**Severity:** moderate  
**Disposition:** preserve supersession/refinement lineage when D-066-style behavior is implemented.

Conversation C correctly allows an investigation result to reveal that the original candidate was incomplete or represented the wrong mechanism.

Failure mode:

```text
Candidate V1
→ observation contradicts/exposes incompleteness
→ implementation silently edits V1 into V2
→ later report cannot explain what hypothesis actually led to the check
```

Recommended conceptual behavior:

```text
Candidate V1
↓
Observation O exposes missing/different mechanism
↓
Candidate V2 refines/supersedes V1
```

Preserve enough lineage to explain:

- the original formulation;
- the observation that triggered refinement;
- the refined/new candidate;
- why the relationship changed.

No event-sourcing system or persistence framework is implied. This is a provenance requirement, not an infrastructure recommendation.

---

## AUDIT-003-F9 — The selected Transparent Decision plan is materially stale against accepted A–C semantics

**Classification:** plan / implementation-handoff mismatch  
**Severity:** high before new decision-layer implementation  
**Disposition:** reconcile the existing plan before implementing from it; do not replace it merely to create a new artifact.

At publication time `MEMORY.md` still selects:

```text
plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md
```

as the next B2 responsibility, with implementation paused pending the post-C handoff decision.

The plan still describes the older method shape:

```text
validated PR/dependency/CI/package/upstream evidence
→ decision-relevant interpretation
→ evidence-sufficiency/stopping
→ maintainer action/abstention
```

and separates:

```text
acquisition
→ dependency interpretation
→ evidence interpretation
→ sufficiency
→ decision
→ presentation
```

This does not yet explicitly represent the accepted post-reconciliation responsibilities:

```text
A impact-candidate formulation
B candidate-specific proposition/applicability evaluation
C uncertainty-location / discriminating-target / targeted-investigation selection
C observation-validity / feedback / stopping semantics
D later overall sufficiency/action synthesis
```

The plan's own maintenance rule says to update it when the decision responsibility, method sequence, proof obligations, or stop line changes.

Those have materially changed.

Therefore:

> **Do not begin generic decision-layer implementation from the current Transparent Decision plan unchanged.**

Recommended action after authorization:

- update the existing plan rather than creating a parallel replacement;
- preserve B2 scope;
- add only the A–C responsibilities actually required for the first bounded implementation/evaluation slice;
- explicitly separate work that still belongs to Conversation D;
- update proof obligations for four-state composition, coverage guards, targeted-check recommendation semantics, and C observation/result behavior as actually admitted.

---

## AUDIT-003-F10 — B2 should implement only the thin credible manifestation of A–C

**Classification:** scope / proportionality  
**Severity:** high as an anti-overdesign boundary  
**Disposition:** preserve route; constrain implementation plan.

The 90-day route and B2 vertical-slice plan define B2 as the smallest credible real public-PR-to-decision path.

B4 later owns broader context/decision-support expansion including richer dependency role/path, target relevance, conditional checks, action changes, and stopping behavior.

Therefore the accepted process decision:

```text
stage boundaries do not constrain whole-product reasoning
```

must not be misread as:

```text
all whole-product concepts explored in A–C must be implemented in B2
```

For the B2 implementation/evaluation slice, do **not** automatically add:

- generic investigation planner;
- arbitrary dependency graph engine;
- universal environment reconstruction;
- generic differential-test executor;
- universal plugin/framework analysis;
- general-purpose candidate generator covering the Python ecosystem;
- numerical ranking/VoI system;
- complete investigation taxonomy;
- autonomous target execution.

B2 should implement only the minimum behavior needed to exercise the accepted semantics through the admitted vertical slice and obtain real feedback.

---

## AUDIT-003-F11 — “Implement before broad D” is sound only for an A–C slice, not a final recommendation engine

**Classification:** implementation/D sequencing  
**Severity:** high for handoff clarity  
**Disposition:** preserve current default with explicit boundary.

The post-C judgment that more abstract C theory is lower-value than implementation feedback is technically sound.

Recommended interpretation:

```text
bounded A–C implementation/evaluation slice before broad D
= justified default
```

But:

```text
complete final five-action recommendation engine before D
= not yet justified
```

Conversation D still owns:

- overall evidence sufficiency;
- final stopping relative to output;
- unresolved/conflicted evidence interaction with action;
- repository-policy relationship;
- maintainer-facing synthesis/action semantics.

Therefore a pre-D implementation slice may implement/test:

- candidate representation or bounded formulation;
- proposition state/evaluation mechanics;
- minimum deterministic composition;
- unresolved/conflicted state preservation;
- one targeted-check/investigation representation;
- C selection/stop behavior for an admitted case;
- observation/evidence feedback;
- explanation/traceability needed to learn from the slice.

It should not silently decide D by implementing final action sufficiency under another name.

---

## AUDIT-003-F12 — No Charter change is currently justified

**Classification:** non-finding / mission-control boundary  
**Severity:** preserve  
**Disposition:** keep `PROJECT_CHARTER.md` unchanged unless later D/implementation evidence proves mission or supported-decision change is required.

The reconciliation contains the hypothesis that UpgradePilot may be better understood internally as an:

```text
evidence-driven impact and investigation system
```

rather than a primary five-label classifier.

That does **not** currently contradict the Charter.

A coherent architecture can be:

```text
INTERNAL PRODUCT CORE
evidence
→ impact
→ applicability
→ investigation
→ sufficiency

MAINTAINER-FACING PROJECTION
→ merge after normal review
→ targeted checks
→ investigate/block
→ defer
→ abstain
```

The internal reasoning model can become much richer than the output vocabulary without changing the product mission.

Do not modify the Charter merely because the classifier framing proved too shallow as an internal architecture.

---

## AUDIT-003-F13 — The reconciliation record still contains live-state wording outside `MEMORY.md`

**Classification:** governance ownership / maintainability  
**Severity:** moderate  
**Disposition:** convert to dated historical handoff wording when the reconciliation record is next edited for substantive corrections.

`AGENTS.md` makes `MEMORY.md` the sole owner of current project position and immediate continuation.

The reconciliation record nevertheless contains a section titled approximately:

```text
Exact current continuation after C closure
```

and records an immediate next action.

That wording can become stale—and did become stale once the learning note was completed.

Recommended form:

```text
C-closure handoff recorded 2026-08-10
```

with wording such as:

> At C closure, the proposed handoff was...

rather than presenting the working-memory record as live continuation.

The reasoning history should remain; only its authority/time framing needs correction.

---

## AUDIT-003-F14 — `MEMORY.md` carries more duplicated A–C theory than its live-state responsibility needs

**Classification:** context efficiency / owner separation  
**Severity:** low-to-moderate  
**Disposition:** compress opportunistically when `MEMORY.md` is next materially updated; do not perform churn merely for line count.

After C closure, `MEMORY.md` contains a substantial duplicated summary of:

- A semantics;
- B states/open-world rules;
- C method;
- C pressure tests;
- many accepted C principles.

The reconciliation record already owns that detailed historical reasoning.

`MEMORY.md` primarily needs to answer:

```text
Where are we?
What has materially been verified?
What is blocked?
What responsibility/decision is selected next?
What continuation-relevant constraints must not be forgotten?
```

A leaner live-state form could retain:

```text
A CLOSED — reference / stable decision range
B CLOSED — reference / stable decision range
C CLOSED — reference / D-053...D-070 / pressure-test references
D unopened
selected plan/responsibility
latest implementation proof
current blocker/handoff
exact continuation
```

plus only the few conceptual reminders that materially control the immediate decision.

This is a context-quality recommendation, not an instruction to erase useful reasoning or rewrite `MEMORY.md` immediately.

---

## AUDIT-003-F15 — Reconciliation authority wording should distinguish control, live state, description, and implemented truth

**Classification:** authority clarity  
**Severity:** low-to-moderate  
**Disposition:** clarify when the reconciliation record is next amended.

The reconciliation groups several artifacts together as active/normative material even though they own different authority classes.

A clearer relationship is:

```text
CONTROLLING / NORMATIVE WITHIN RESPONSIBILITY
AGENTS
Project Charter
selected plan
accepted specifications
accepted ADRs for their decisions

LIVE-STATE AUTHORITY
MEMORY

DESCRIPTIVE / NAVIGATION
README and similar entry points

IMPLEMENTED TRUTH
source/tests/commands/outputs/environment evidence
```

This aligns the reconciliation record with the responsibility routing already established in root governance and reduces the chance that a descriptive README or plan is treated as executable truth.

---

# 7. Non-findings and complexity that should be preserved

The audit explicitly rejects the following “simplifications” because they would erase useful domain distinctions.

## 7.1 Do not collapse the impact model into one generic `risk` object

Keep the conceptual distinctions among:

```text
upstream change
exposure/path
activation
possible consequence
applicability proposition
```

They exist to prevent false inference, not to create architecture ceremony.

## 7.2 Do not remove `unresolved` or `conflicted` merely to simplify state

Those states protect evidence honesty and are required by the product's uncertainty doctrine.

## 7.3 Do not replace open-world reasoning with search-success heuristics

```text
not found
!= absent
```

without a justified proposition-local coverage boundary.

## 7.4 Do not give LLMs direct source/evidence/applicability/maintainer authority

The deterministic-shell / bounded-semantic responsibility split remains one of the strongest accepted directions in the project.

## 7.5 Do not impose a universal static/semantic/dynamic check ordering

The two C pressure tests specifically show why both:

```text
static-first
```

and:

```text
dynamic-first
```

are invalid as universal rules.

## 7.6 Do not create numerical VoI merely because qualitative comparison has trade-offs

The absence of fake precision is a strength. Where qualitative trade-offs remain policy-relative, surface them rather than inventing an optimizer.

## 7.7 Do not open Conversation D merely because C closed

C closure does not mechanically activate D. The post-C handoff should decide whether a bounded implementation/evaluation slice can now produce more useful evidence first.

---

# 8. Relationship to the current implementation

The active implementation does not contradict the strongest accepted A/B boundaries.

`src/upgradepilot/investigation.py` already demonstrates useful responsibility separation:

- CI evidence remains an independent branch;
- upstream semantic work is separately composed;
- exact package/repository/release/tag/changelog evidence is preserved through explicit states;
- target-Python acquisition is conditionally activated by a grounded upstream support-drop claim;
- unresolved/problem states do not silently become safety or recommendation.

The existing Target-Python relevance slice therefore serves as real implementation evidence for the project's preference for:

```text
authoritative acquisition / identity
→ bounded semantic extraction where needed
→ deterministic validation
→ narrowly scoped relevance result
```

But it is only one proven slice. It does **not** prove a universal candidate/applicability/investigation engine.

No source change follows automatically from this audit.

---

# 9. Recommended correction package before new generic decision-layer implementation

This is a **review disposition**, not an authorized implementation plan.

If the user/`MEMORY.md` later selects reconciliation work before implementation, the smallest coherent package is:

1. **Keep A/B/C formally closed.**
2. Add the candidate-formulation guard from `AUDIT-003-F1`.
3. Add the three-completeness distinction from `AUDIT-003-F2`.
4. Generalize C input to unresolved **or conflicted / still-disputed** proposition states (`F3`).
5. Split targeted-check recommendability from UpgradePilot automated execution admissibility (`F4`).
6. Add non-dominated alternatives as a valid C outcome (`F5`).
7. Refine cost/value stopping so C does not invent policy-relative utility (`F6`).
8. Define only the minimum deterministic four-state candidate/path composition semantics required by the selected slice (`F7`).
9. Preserve candidate refinement/supersession lineage (`F8`).
10. Reconcile the existing Transparent Decision plan against accepted A–C semantics before new decision-layer code (`F9`).
11. Bound the first implementation/evaluation slice to B2 rather than implementing every whole-product C concept (`F10`).
12. Keep the pre-D implementation default only for an A–C slice; do not implement final D sufficiency/action semantics prematurely (`F11`).
13. Leave the Charter and route unchanged unless later evidence requires mission/gate changes (`F12`).
14. When those records are next substantively edited, correct working-memory live-state wording and authority classification (`F13`, `F15`).
15. Compress `MEMORY.md` only when useful to continuation/context quality rather than as cosmetic churn (`F14`).

Because the cumulative learning note was completed before publication of this audit, **do not repeat “create the learning note first” as an outstanding action**.

---

# 10. Suggested post-audit sequence

This sequence is advisory and must be revalidated against current `MEMORY.md` before use:

```text
AUDIT-003
↓
review / accept / reject the bounded findings
↓
if accepted, reconcile the A–C record + Transparent Decision plan
without reopening A/B/C wholesale
↓
select the smallest B2 A–C implementation/evaluation responsibility
↓
implement + test + inspect changed-case behavior
↓
use real feedback to decide whether a concrete D dependency exists
↓
open only the necessary Conversation-D reasoning
```

The important sequencing principle is:

```text
correct accepted semantics enough to implement safely
→ get real behavioral evidence
→ then expand theory only where behavior exposes a real need
```

not:

```text
model the entire product domain completely before coding
```

and not:

```text
code against the stale pre-reconciliation plan because it is already selected
```

---

# 11. Reassessment triggers

Re-read this audit when any of the following occurs:

1. `B2_TRANSPARENT_DECISION_METHOD_PLAN.md` is materially revised after A–C reconciliation.
2. A generic impact-candidate or applicability representation is about to enter product source.
3. Negative applicability or transition-level “no impact” behavior is introduced.
4. Targeted-check recommendation or automated investigation execution is implemented.
5. Candidate/path logical composition is introduced.
6. Investigation results are allowed to refine or generate candidates.
7. Conversation D is proposed/opened.
8. Charter action vocabulary or product mission is proposed for change.
9. A new real case contradicts one of the A/B/C closure assumptions.
10. A later implementation demonstrates that one audit finding is unnecessary, wrong, or already naturally resolved by a simpler design.

When a finding is resolved, prefer linking the later plan/spec/ADR/source/validation record rather than rewriting this historical audit into a post-fix document.

---

# 12. Final audit conclusion

The post-C decision-model work survives critical review.

The most important conclusion is **not** that the project needs another large conceptual phase. The accepted A–C structure is coherent enough to build from, and the C closure pressure tests are grounded in real contrasting cases.

The concrete work remaining before new generic decision-layer implementation is narrower:

```text
coverage semantics
+
C authority/recommendation boundaries
+
minimum composition semantics
+
candidate-refinement provenance
+
Transparent Decision plan reconciliation
+
B2 implementation-scope discipline
```

The audit therefore recommends:

> **Preserve A/B/C closure, make the bounded corrections explicit, reconcile the selected B2 plan, then obtain implementation/evaluation feedback before expanding into broad Conversation-D theory.**

No finding in this audit independently authorizes repository changes beyond preserving this audit record itself.
