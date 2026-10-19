# UpgradePilot Investigator Responsibility Decomposition and Evidence-to-Decision Product Direction

**Date:** 2026-10-19  
**Status:** Proposed strategic direction — evidence-backed, non-controlling until explicitly accepted  
**Owner:** Ali Rajabi  
**Scope:** Reconcile the completed Investigator/LLM experiments with UpgradePilot's accepted evidence, decision, Workspace, validation and maintainer-action architecture; propose the next product-development direction without selecting an implementation topology, framework, model, agent stack or new runtime work.  
**Live-state authority:** [`../MEMORY.md`](../MEMORY.md) remains the sole owner of selected continuation.  

---

## 1. Executive proposal

UpgradePilot should **end the current prompt/instruction-tuning line as a development method** and shift its center of gravity from a monolithic `LLM Investigator → recommendation` shape toward an **evidence/proposition-first hybrid product architecture with explicit responsibility decomposition**.

The proposed direction is:

```text
CANONICAL INVESTIGATION WORKSPACE
        │
        │ exact observations / native assessments / source material
        ▼
MECHANICAL / DETERMINISTIC PREPARATION WHERE JUSTIFIED
        │
        │ source facts, explicit relations, configuration/dependency structure
        ▼
CANDIDATE PROPOSITIONS
        │
        ├──────────────► bounded semantic interpretation where needed
        │
        ▼
PROPOSITION EVALUATION / VALIDATION
        │
        │ established / refuted / unresolved / conflicted
        ▼
EVALUATED PROPOSITIONS / CANDIDATE STATE
        │
        ▼
MAINTAINER-ACTION SYNTHESIS
        │
        ▼
PROVENANCE-BACKED DECISION REPORT
```

This proposal does **not** reject autonomous investigation, LLMs, or multi-agent methods. The accumulated evidence supports a narrower conclusion:

> **Autonomy can improve acquisition and investigation efficiency, but one model should not be expected to own evidence discovery, relation extraction, interpretation, validation, stopping, adequacy and recommendation authority as one undifferentiated responsibility.**

The proposed architecture therefore retains autonomy where it earns value, introduces deterministic structure where the relation is genuinely mechanical, keeps semantic interpretation bounded and attributed, and requires independent evaluation/decision authority before model-derived findings can affect maintainer action.

The immediate recommended next technical responsibility is **not another prompt, context, model or discovery experiment**. It is to design a **general deterministic source-fact/relation baseline** that can establish a bounded class of explicit source relationships with provenance and honest unresolved states, and that feeds the accepted proposition/evaluation architecture rather than becoming a second truth path.

A later bounded multi-role or multi-agent experiment remains a strong candidate once the proposition/evaluation interfaces are explicit enough to test responsibility separation rather than simply adding more model calls.

---

## 2. Why a strategic proposal is needed now

UpgradePilot has reached a genuine method-selection turning point.

Recent work successfully removed several confounders from the Investigator experiments:

- strict evidence identity and request-local typed references;
- complete retained source/native packets;
- lossless model presentation;
- measured context fit;
- bounded run control and cancellation handling;
- exact freeze/activation;
- complete usage accounting for the final cohorts;
- source-aware semantic review against frozen obligations.

These controls were necessary because earlier failures could be blamed on acquisition, navigation, interface/reference mistakes, budget exhaustion, timeout semantics or interrupted execution. The final completed experiments no longer permit that explanation for the observed semantic failures.

At the same time, older broader-agency research showed that adaptive Agent behavior sometimes found useful evidence that a fixed policy missed and consumed less input/time in the observed pairs. Therefore the evidence also does not justify the opposite simplification that "agents are useless" or that all reasoning should become deterministic.

The project now needs a product-level reconciliation of those two facts:

```text
useful agency exists
+
monolithic semantic/recommendation authority is unreliable
+
mechanical relationships should not be repeatedly rediscovered by an LLM
+
open-ended software meaning still requires semantic interpretation
=
responsibility decomposition, not method absolutism
```

Without an explicit proposal, the project risks oscillating between two rabbit holes:

1. repeatedly tuning a single Investigator prompt/model/context until exposed development cases pass; or
2. reacting to model failures by hardcoding fixture-shaped deterministic rules that cannot satisfy the owning product responsibility.

Both would conflict with the project evidence doctrine and minimum-useful-generality requirements.

---

## 3. Controlling project constraints

This proposal is intentionally subordinate to existing accepted owners. It does not replace them.

### 3.1 Charter

The [Project Charter](../PROJECT_CHARTER.md) defines UpgradePilot as an evidence-backed dependency-update decision system for maintainers of public Python repositories. It explicitly requires separation of observation, inference and missing evidence; provenance-backed uncertainty-aware decision reporting; a deterministic bounded recommendation or abstention in the supported core; staged evaluation; and technology admission only after an observed limitation, simpler baseline, bounded hypothesis and rejection gate.

The Charter also explicitly allows later experiments involving grounded LLM synthesis or bounded multi-agent investigation when comparative evidence justifies them. Therefore this proposal neither introduces multi-agent work outside the product boundary nor treats it as automatically required.

### 3.2 Core evidence and authority invariants

The [Core Pipeline and Contract Specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) already requires:

- observation, interpretation, evidence quality and decision to remain distinct (`OBS-001`);
- model-derived claims to retain authority/transformation identity (`AUTH-001`);
- grounding not to become independent corroboration (`AUTH-002`, `GROUND-001`);
- uncorroborated model-derived claims not to independently justify less-cautious recommendations (`AUTH-003`);
- absence of a model-derived claim not to become negative evidence (`AUTH-004`);
- model output not to assign its own authority or decision effect (`AUTH-005`);
- evidence, model/agent proposals, assessment results and report presentation to remain distinguishable;
- future investigators not to reconstruct structured evidence by parsing report prose when structured owning state exists.

This proposal makes those invariants more operational for the next architecture stage; it does not add a competing trust doctrine.

### 3.3 Product Decision Model

The [Product Decision Model Specification](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) already defines the accepted reasoning spine:

```text
admitted evidence
→ mechanism-specific candidate
→ candidate-specific propositions / applicability paths
→ proposition evaluation
   established / refuted / unresolved / conflicted
→ bounded composition
→ investigation where justified
→ observation validation
→ reevaluation / candidate refinement
→ later synthesis
```

It explicitly states that model-generated candidates cannot self-authorize applicability, evidence completeness or final decision effect, and it prefers deterministic procedures for genuinely mechanical questions while permitting bounded semantic reasoning for irreducible software meaning.

The proposal therefore recommends implementing closer to the already accepted semantics instead of asking one model report to implicitly perform all of them at once.

### 3.4 Canonical Investigation Workspace

[ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) establishes one canonical evolving Workspace while preserving native authority, proposal/evaluation separation and synthesis action authority. It already states that:

- semantic proposals are not truth;
- structural admission is not evaluation;
- procedural finish is not adequacy;
- native facts do not require redundant generic model evaluation;
- evaluator projections must include relevant counterevidence/unknowns rather than inherit proposer citations as their whole boundary;
- no model, agent topology, discovery policy or adequacy method is selected by the ADR.

This proposal is therefore a compatible direction for how future consumers/proposers/evaluators can use the Workspace.

### 3.5 Maintainer-action authority

The [Maintainer Action Synthesis Specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) owns final action permission after technical investigation. It requires positive permission, prohibits fallback from "nothing bad found" to favorable action, and disallows upstream mechanism-specific findings from acquiring maintainer-action authority merely because they exist.

A model report recommendation is consequently not the architectural decision owner even when the report is source-correct.

### 3.6 Minimum useful generality

The [Minimum Useful Generality Specification](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) prohibits fixture-specific semantic transformations from becoming product behavior. The deterministic baseline proposed here must therefore operate over a declared **generic relation grammar/domain**, not encode special rules such as "HTTPX app removal means failure" or one parser per exposed dependency/case.

---

## 4. Evidence base: what the experiments actually showed

The direction in this proposal is not derived from one failed prompt. It follows a sequence of increasingly controlled experiments.

### 4.1 Broader Fixed/Agent research: autonomy showed value but did not yield advice-ready decisions

The completed broader-agency Contract-2 comparison is retained on branch `codex/broader-llm-agency-research-2026-10-05`:

- [reviewed Contract-2 comparison](https://github.com/motafegh/UpgradePilot/blob/codex/broader-llm-agency-research-2026-10-05/working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/README.md)
- accepted research checkpoint commit `cde0ea99`

The selected comparison used Gemma12 and Qwen35 across HTTPX/pytest cases with Fixed and Agent policies. Its key findings were:

- **8/8 mechanically valid final reports**;
- **0/8 advice-ready** after source-aware review;
- no uniformly superior discovery policy;
- Agent sometimes found material evidence that Fixed missed;
- Agent used less input and elapsed time in all four descriptive Fixed-vs-Agent pairs;
- both policies still produced wrong version association, capture-authority inflation, incomplete applicability reasoning, weak stopping and unsupported recommendations;
- the HTTPX Agent could receive relevant `TestClient(app)` evidence and still fail to form the decisive source/applicability relationship.

This evidence rejects two simplistic conclusions:

```text
Agent is always better than fixed retrieval     — not established
Agent is useless / should be removed             — contradicted by useful discovery evidence
```

The stronger supported conclusion is:

> adaptive investigation can be useful, but its output still requires separate semantic/evidential evaluation before recommendation authority.

### 4.2 Broader interpretation-only work: retrieval was not the sole bottleneck

The same research line later supplied relevant evidence directly to bounded interpretation calls. Those calls still mixed correct release facts with wrong pin attribution, CI authority inflation and unsupported installed-version/compatibility conclusions.

That result already suggested that acquisition/navigation was not the sole bottleneck. It motivated the main-branch successor to isolate interpretation more rigorously.

### 4.3 Main supplied-evidence capability diagnostic: complete evidence still produced semantic failure

The completed main-branch diagnostic is recorded in:

- [`../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/README.md`](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/README.md)
- [`../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/review-adjudication.json`](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/review-adjudication.json)

The clean cohort completed all five roles with known usage:

- 66,920 input tokens;
- 4,373 generated tokens;
- 1,028.44 prediction seconds;
- zero unknown usage;
- **0/4 semantically adequate cases**.

The decisive sources were already delivered. Failures therefore could not reasonably be attributed to autonomous navigation not finding them.

Observed failure patterns included:

- missing the supplied `app` parameter removal and caller relationship;
- substituting the adjacent `verify` type-hint change;
- inventing forwarded behavior not present in the supplied call;
- promoting historical/static CI evidence into stronger executed-coverage conclusions;
- producing decision-critical reassurance with missing or non-entailing support.

### 4.4 Instruction-only evidence-first comparison: clearer instructions improved some facts but did not solve the responsibility

The final instruction-only comparison is recorded in:

- [`../working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md`](../working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md)
- implementation `9c6b3720`;
- activation `523ca28d`;
- completed result `b2948711`.

Only the model-facing task goal changed. Evidence, model, schema, reference policy, publication path, reviewer obligations and runtime point remained controlled.

The cohort again completed all five roles with known usage:

- 67,590 input tokens;
- 5,833 generated tokens;
- 1,262.634 prediction seconds;
- zero unknown usage;
- **0/4 semantically adequate cases**.

There were real local improvements:

- HTTPX PR withdrew the earlier `likely safe` reassurance;
- newer consumer correctly observed that `verify` was not forwarded;
- older consumer noticed that `app` was forwarded.

But material failures remained:

- HTTPX PR still omitted the consumer/framework/signature relationship;
- newer consumer still failed to establish the material `app` relation and closed around another parameter;
- glyphsLib still promoted unresolved CI coverage and cited sources that did not entail the workflow claims;
- older consumer noticed `app`, then invented `cert` removal and several nonexistent forwarded arguments while missing the actual `app` mismatch.

The candidate consumed **33.39% more generated tokens** and **22.77% more measured prediction time** than the previous supplied-evidence reference while remaining 0/4 adequate.

This is strong evidence for a stop line on further instruction-only tuning of this same responsibility.

---

## 5. What the evidence establishes

The project can now support the following bounded findings.

### 5.1 Mechanical validity is not semantic adequacy

Across multiple cohorts, models can satisfy schemas, use valid typed citations and produce complete reports while still asserting relations that the cited evidence does not support.

Therefore:

```text
schema valid
+
citation valid
!=
semantic entailment
```

### 5.2 Complete evidence does not guarantee correct relation construction

The final supplied-evidence experiments remove discovery as the explanation for those cases. The model can have the decisive passages and still select an adjacent detail, invent a call relationship or fail to connect the relevant source chain.

### 5.3 Clearer instructions can change behavior without solving the underlying responsibility

The instruction-only candidate improved several local behaviors. That is useful evidence that task framing matters. But improvement without adequate material relation coverage does not justify further open-ended prompt tuning.

### 5.4 Context size is not the sole explanation

Large PR packets may worsen salience/attention pressure, but smaller captured-consumer cases also failed on basic supplied source relations. Reducing packet size is useful engineering but cannot be treated as the demonstrated semantic cure.

### 5.5 Autonomous investigation has demonstrated useful behavior

The older Agent arms sometimes acquired better evidence than Fixed and used less input/time in the observed pairs. Autonomy should therefore remain a candidate tool for evidence acquisition, hypothesis formation and discriminating follow-up.

### 5.6 Autonomous investigation has not earned unilateral recommendation authority

Neither broader Agent nor supplied-evidence one-shot reports produced advice-ready results in the reviewed development cases. Agent usefulness and decision authority must therefore remain separate questions.

### 5.7 Mechanical relationships should not be repeatedly rediscovered semantically when a generic deterministic owner can establish them

Exact signatures, explicit call arguments, set differences, source identity and many configuration relationships are examples of questions for which deterministic extraction can be both cheaper and more inspectable, provided the supported boundary is explicit and dynamic/ambiguous cases remain unresolved.

### 5.8 Existing project semantics already favor proposition-level evaluation

The Product Decision Model, Workspace and Core specifications already separate proposals, observations, evaluations, applicability state and action permission. The experiments indicate that implementation should now lean more directly on that architecture.

---

## 6. What the evidence does **not** establish

The project must also preserve the following non-conclusions.

### 6.1 It does not prove LLMs cannot perform useful semantic interpretation

The experiments cover selected local models, operating points and exposed development fixtures. Other methods, deployments or structured inputs may perform better.

### 6.2 It does not prove autonomous agents are worse than fixed methods

The broader comparison was mixed on discovery and showed descriptive efficiency benefits for Agent. The correct conclusion is to constrain its authority, not delete useful agency.

### 6.3 It does not prove a deterministic system can solve the full product responsibility

A deterministic source-fact/relation baseline can cover explicit mechanical relations. It cannot be assumed to understand open-ended software behavior, dynamic binding, implicit framework semantics, natural-language upstream changes or complete candidate discovery.

### 6.4 It does not establish a particular multi-agent topology

No evidence currently chooses a number of agents, orchestration framework, critic pattern, messaging protocol or model assignment. A responsibility split should precede framework selection.

### 6.5 It does not establish protected-case generalization

HTTPX and glyphsLib material is exposed development evidence. Any method tuned with these cases must be frozen before new unseen qualification material is selected.

### 6.6 It does not grant product action permission

Even a source-correct experimental report does not bypass the accepted evaluation and Maintainer Action Synthesis boundaries.

---

## 7. Diagnosis: the overloaded responsibility is the architectural problem to address

The current Investigator experiments have effectively asked one model invocation or one agent policy to perform too many logically distinct responsibilities:

```text
find evidence
→ decide what is relevant
→ extract facts
→ form source relationships
→ infer applicability
→ notice counterevidence
→ preserve uncertainty
→ decide whether more evidence is needed
→ stop
→ synthesize recommendation
```

Failure anywhere in this chain can contaminate everything downstream. Worse, a final polished report can hide the location of the failure.

The evidence suggests the next product question should no longer be:

> How do we make this one Investigator answer correctly?

It should be:

> Which responsibilities can be established deterministically, which require bounded semantic interpretation, which need independent evaluation, and which owner is permitted to turn evaluated technical state into maintainer action?

This is not a retreat from intelligent agents. It is the trust architecture required to use them productively.

---

## 8. Proposed responsibility architecture

### 8.1 Layer A — Canonical observations and native assessments

**Owner:** canonical Workspace plus existing native evidence/evaluator owners.

Inputs include:

- exact repository/PR/base/head/dependency-transition identity;
- retained source passages/files;
- package/dependency facts;
- CI/workflow/runtime native records and assessments;
- acquisition problems and evidence limitations;
- provenance, revision and transformation identity.

This layer remains the evidence authority. It does not ask a model to restate facts that already have a native owner merely to make them "AI-readable."

### 8.2 Layer B — Deterministic/mechanical evidence preparation where justified

**Proposed responsibility:** derive explicit facts/relations whose meaning is mechanically available under a bounded grammar.

Examples:

```text
old function parameters
new function parameters
added / removed parameter names
explicit keyword arguments forwarded by a captured call
literal import/re-export relationships where statically explicit
workflow step → explicit command
configuration environment → explicit dependency-input file
exact set / identity / membership relations
```

Every derived item must preserve:

- source identity;
- source spans or equivalent exact basis;
- transformation/method identity;
- supported grammar/domain;
- completeness/partiality limits;
- unresolved dynamic/alias/binding conditions.

A deterministic transformation is not an authoritative source and must not claim dynamic behavior it did not establish.

### 8.3 Layer C — Candidate propositions

A candidate proposition is an attributed claim that may be evaluated, not a new observation merely because it was generated by deterministic code or a model.

Conceptually:

```text
CandidateProposition
- identity
- statement / normalized relation
- proposition kind / scope
- exact target/revision/context
- basis references
- producer/method identity
- current evidential status of components
- missing observations / unresolved bindings
- lineage / predecessor when refined
```

Examples:

```text
P1: captured caller forwards keyword `app`
P2: compared new callee signature does not accept keyword `app`
P3: the target uses the captured caller implementation at the relevant revision/runtime
```

P1/P2 may be mechanically supported for exact source captures. P3 may remain unresolved. The system must not collapse them into "target is incompatible" without candidate-specific evaluation.

### 8.4 Layer D — Bounded semantic interpretation

LLMs remain useful when the required meaning is not adequately mechanical, for example:

- identifying a plausible mechanism from upstream natural-language changes;
- interpreting unusual framework or integration semantics;
- relating several already-established facts into a candidate consequence;
- explaining why an unresolved binding matters;
- forming hypotheses about what evidence would discriminate a proposition;
- summarizing evaluated state for a later consumer.

Model output at this layer is **proposal/interpretation**, not truth or action permission.

The semantic role should receive a working set appropriate to its responsibility rather than every available artifact by default. When exact original evidence is needed, it should remain addressable from the Workspace.

### 8.5 Layer E — Proposition evaluation / validation

Evaluation decides what the evidence actually supports for one proposition/candidate under the Product Decision Model.

Accepted states remain:

```text
established
refuted
unresolved
conflicted
```

The evaluator must be able to consider relevant counterevidence/unknowns and cannot simply accept the proposer's chosen citations as sufficient proof.

The evaluator may be:

- an existing native deterministic evaluator;
- deterministic validation for a mechanical proposition;
- a bounded semantic evaluator when necessary;
- a future specialized model/role, if separately admitted and qualified.

"Independent" here means independent **authority/evidential responsibility**, not necessarily a different vendor/model/process.

### 8.6 Layer F — Maintainer-action synthesis

Only evaluated technical state reaches action synthesis. The [Maintainer Action Synthesis Specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) remains controlling.

No Investigator, interpreter, relation extractor or validator may silently convert its output into:

- merge permission;
- low-risk reassurance;
- targeted-check permission;
- investigate/block permission;
- defer;
- abstention semantics.

Synthesis consumes accepted technical meaning and applies action-relative permission.

---

## 9. Multi-role and multi-agent direction

### 9.1 Distinguish a role from an agent

A **role** is a bounded responsibility with declared inputs, outputs, authority and stop conditions.

An **agent** is an actor with some adaptive freedom to choose actions/tools/next observations within a role.

Therefore:

```text
multi-role architecture
!= automatically a multi-agent framework
```

A first multi-role experiment may use the same local model multiple times with isolated contexts and typed handoffs. Later, different models or deterministic owners may fill different roles if evidence justifies that complexity.

### 9.2 Recommended conceptual roles

The following are candidate responsibilities, not a selected process topology:

#### Investigator / acquisition role

Purpose:

- identify potentially relevant evidence;
- pursue a discriminating question;
- request additional bounded observations;
- form investigation hypotheses;
- stop under declared budget/coverage conditions.

Authority:

- may propose relevance and next evidence;
- may not establish semantic truth, adequacy or maintainer action merely through discovery.

#### Relation / proposition role

Purpose:

- consume bounded observations/mechanical facts;
- formulate explicit candidate propositions and unresolved bindings;
- distinguish direct fact from inferred relationship.

Authority:

- proposals only until evaluated.

#### Validator / skeptic role

Purpose:

- assess proposition support against admitted evidence and relevant counterevidence/unknowns;
- reject invented relations;
- preserve unresolved/conflicted state;
- identify the exact missing observation when possible.

Authority:

- proposition evaluation within its admitted domain;
- no maintainer action permission unless separately owned by synthesis.

#### Synthesis role

Purpose:

- consume evaluated state under accepted deterministic action semantics;
- produce the bounded maintainer-facing result.

A model may assist explanation, but action permission remains governed by the synthesis owner.

### 9.3 Why this is preferable to an immediate free-form swarm

A free-form multi-agent conversation would introduce additional uncontrolled variables:

- repeated evidence/context;
- untracked semantic authority transfer;
- disagreement-resolution policy;
- extra sampling opportunities;
- unclear provenance of final propositions;
- higher cost and harder causal attribution.

Responsibility decomposition should therefore precede agent-framework adoption.

### 9.4 Why multi-role remains promising

It directly addresses several demonstrated failures:

- smaller responsibility-specific contexts reduce attention competition;
- typed intermediate products expose where meaning first goes wrong;
- a validator can reject an interpreter's invented relation before synthesis;
- autonomous discovery can be retained without inheriting action authority;
- different methods can be compared per responsibility instead of replacing the entire product method at once.

---

## 10. Working-set and context strategy

The recent 22k–25k-token supplied-evidence cases show that complete raw-ish delivery can be expensive. Stateful transport would reduce retransmission in multi-turn workflows, but it would not remove the information from the model's attention context when later reasoning still depends on it.

The proposed long-term direction is therefore **explicit working state**, not opaque chat memory.

Example:

```text
Established observations / evaluated propositions
- dependency declaration: pytest 9.0.2 → 9.0.3 [R1]
- workflow `tests` invokes `tox -e py` [R2]
- tox env uses requirements-dev input [R3]

Unresolved
- exact installed pytest identity in retained CI execution [R4]
- exact job/runtime correlation for native coverage assessment [R5]

Current discriminating question
- can admitted runtime evidence establish the target proposition?

Available original evidence
R1..R17 (addressable from Workspace)
```

This structure should not be a lossy AI summary masquerading as evidence. Each item must retain basis/provenance and authority state. Original evidence stays canonical and addressable.

---

## 11. Proposed immediate baseline: general deterministic source-fact/relation extraction

The next bounded technical design should focus on one narrow but product-relevant responsibility exposed repeatedly by the experiments:

> **Can UpgradePilot mechanically establish explicit source-level signature/call relationships, with provenance and honest unresolved cases, without encoding fixture-specific answers?**

### 11.1 Candidate supported grammar

A first design may consider bounded Python source constructs such as:

- function/method definitions with explicit named parameters;
- explicit call expressions with literal positional/keyword argument syntax;
- import/re-export identity only where syntactically explicit and source-bound;
- before/after signature comparison for exact captured definitions;
- set relations among explicit parameter/argument names.

### 11.2 Candidate outputs

For example:

```text
SourceFact:
  callee_old.accepted_keywords = {...}
  callee_new.accepted_keywords = {...}
  captured_call.explicit_keywords = {...}

Relation:
  removed_keywords = old - new
  forwarded_removed_keywords = captured_call.explicit_keywords ∩ removed_keywords
```

The baseline must **not** directly output:

```text
"upgrade incompatible"
"safe"
"target affected"
```

Those are later applicability/decision propositions requiring additional bindings.

### 11.3 Required unresolved cases

The baseline must preserve unresolved/unsupported states rather than guess when analysis depends on:

- dynamic `**kwargs` content;
- aliases that cannot be resolved under the admitted source boundary;
- decorators/metaprogramming that change effective signatures;
- runtime monkey-patching;
- dynamic dispatch/overloads where exact target binding is not established;
- partial/missing source captures;
- generated/native-extension behavior outside the supported grammar.

### 11.4 Generality proof

The baseline should be tested on representative variation, not only HTTPX:

- equivalent calls with different parameter names;
- added vs removed parameters;
- caller does and does not forward a removed keyword;
- positional/keyword variations within supported scope;
- `**kwargs` unresolved cases;
- alias/import variation where supported;
- changed meaning and irrelevant parameters;
- partial/malformed source;
- unrelated dependency/repository examples.

The exposed HTTPX case can remain a regression fixture, but it cannot be the acceptance horizon.

### 11.5 Why this baseline is strategically useful even if narrow

It would provide:

1. an inspectable answer to a repeatedly failed relation-extraction responsibility;
2. a smaller and cleaner semantic input for later interpretation;
3. explicit evidence about where deterministic analysis ends;
4. a real proposition/evaluation interface to test multi-role architecture against;
5. a simpler baseline required by the Charter before adding more model complexity.

---

## 12. Recommended experiment sequence after strategic acceptance

This proposal recommends the following **decision sequence**, not automatic implementation.

### Stage 0 — Close the current instruction-tuning line

Record that the completed instruction-only comparison is the final bounded prompt-only development attempt for this responsibility unless materially new evidence justifies reopening it.

Do not automatically run:

- another prompt variant;
- worksheet v2;
- a seed sweep;
- a larger context point;
- autonomous discovery again;
- another model merely because Gemma failed.

### Stage 1 — Design the deterministic source-fact/relation baseline

Write a separate bounded plan defining:

- exact responsibility;
- supported grammar;
- source/provenance contract;
- unresolved cases;
- representative generality fixtures;
- integration point into Workspace/proposition evaluation;
- success and rejection gates;
- implementation cost/cleanup.

### Stage 2 — Establish the proposition handoff

Define the minimum representation by which mechanical facts and semantic proposals enter candidate-specific evaluation without creating a competing truth path.

Prefer existing Product Decision Model / Workspace semantics over a new generic knowledge framework.

### Stage 3 — Compare interpretation methods on structured responsibility inputs

Only after Stage 1/2 create meaningful structured inputs, compare the smallest credible interpretation alternatives. Candidate arms may include:

- deterministic facts + one bounded semantic interpreter;
- deterministic facts + separate interpreter/validator roles using the same model;
- deterministic facts + different qualified local deployment for the interpretation role;
- a simpler deterministic-only result for the subset it actually supports.

Do not bundle several changes into one arm unless the experiment explicitly tests the bundle.

### Stage 4 — Bounded multi-role experiment if justified

If a single interpreter still produces unsupported propositions, test responsibility separation directly:

```text
same canonical observations
→ proposition role
→ validator role
→ deterministic synthesis boundary
```

Use typed handoffs, no free-form agent-to-agent authority inheritance, frozen budgets and explicit disagreement handling.

### Stage 5 — Protected holdout qualification

Once a method bundle performs adequately on exposed development fixtures:

1. freeze exact method/policy;
2. select new unseen dependency-update material under declared eligibility rules;
3. freeze review obligations before output;
4. run without semantic tuning;
5. treat material method changes as a new qualification horizon.

### Stage 6 — Reintroduce autonomous discovery on top of validated interpretation/evaluation

Only when the downstream proposition/evaluation path is credible should the project ask:

> Does autonomous Investigator evidence selection improve usefulness, coverage or cost over simpler acquisition policies without degrading semantic/authority discipline?

This preserves the useful older Agent evidence while avoiding the earlier confound where acquisition and semantic quality failed together.

---

## 13. Alternatives considered

### 13.1 Continue prompt engineering

**Disposition: reject as immediate continuation.**

Reason: two controlled supplied-evidence cohorts are 0/4 adequate, with the clearer-instruction candidate more expensive and still materially wrong. Prompt framing remains a legitimate implementation detail but no longer justifies another standalone experiment on exposed fixtures.

### 13.2 Increase context further

**Disposition: defer.**

Reason: smaller source-pair cases also fail material relations. Context pressure may matter operationally, but current evidence does not make capacity the primary semantic bottleneck.

### 13.3 Switch immediately to a stronger model

**Disposition: credible later comparison, not first response.**

Reason: old Qwen35 broader-agency work also produced non-advice-ready reports, and changing deployment without first improving responsibility boundaries would leave the same authority problem. A stronger model may later be appropriate for a bounded interpretation role.

### 13.4 Build a multi-agent swarm now

**Disposition: do not select.**

Reason: responsibility separation is promising, but a free-form swarm would add communication, authority and evaluation problems before the intermediate contracts are defined.

### 13.5 Remove LLMs and build a deterministic static analyzer for everything

**Disposition: reject.**

Reason: open-ended upstream semantics, framework behavior, candidate discovery and contextual interpretation exceed a simple mechanical grammar. Deterministic methods should own the questions they can actually establish, not expand until they silently replace unsupported semantics.

### 13.6 Return immediately to autonomous discovery

**Disposition: defer.**

Reason: older Agent work showed useful discovery, but the supplied-evidence results show interpretation/validation remains a dependency. Reintroducing autonomy now would again mix failure sources.

### 13.7 Use report prose as the integration surface

**Disposition: reject.**

Reason: Core §6.2 and ADR-0012 already require structured evidence/proposals/evaluations to remain available to future consumers rather than reconstructing meaning from human prose.

---

## 14. Research-infrastructure stop line

The recent run-control, reference, retention, freeze/activation and accounting work was necessary to obtain trustworthy evidence. It should now enter a **maintenance-only posture** unless a selected future experiment exposes a blocking correctness gap.

Do not continue generic polishing of:

- cancellation mechanics;
- token accounting edge cases;
- freeze metadata;
- context-fit machinery;
- experiment retention ceremony;
- provider wrapper abstractions;

merely because they can be improved.

Retain them when they are necessary to run a selected bounded experiment correctly. Apply the Core `JUST-*` invariants: existing effort and tests do not themselves justify further expansion.

---

## 15. Success and rejection gates for the proposed direction

### 15.1 Deterministic source-relation baseline success

A baseline is promising only if it:

- handles a declared useful grammar across representative variation;
- preserves exact source/provenance/transformation identity;
- distinguishes supported relations from unresolved dynamic cases;
- does not contain dependency/repository/fixture-specific answer rules;
- exposes a usable proposition/evaluation boundary;
- is simpler/more reliable than asking the LLM to rediscover the same mechanical relation;
- preserves existing product semantics and does not claim target applicability/action.

### 15.2 Deterministic baseline rejection/narrowing

Narrow or reject it if:

- useful generality requires an expanding fixture/category parser;
- dynamic Python behavior makes the declared grammar too weak to help real cases;
- integration cost exceeds the semantic burden it removes;
- it duplicates an existing native owner;
- downstream consumers still need to reparse the same source to trust the relation.

### 15.3 Multi-role experiment success

A future multi-role method should not be called successful because agents agree. It must demonstrate:

- materially higher source/proposition correctness;
- preserved uncertainty and authority boundaries;
- validator rejection of false/invented relations;
- useful disagreement/unresolved handling;
- bounded cost and failure behavior;
- no silent recommendation authority transfer;
- performance on frozen protected material before product adoption.

### 15.4 Multi-role rejection

Reject or simplify it if:

- roles merely restate one another;
- validator output is highly correlated with proposer errors without adding discriminating evidence;
- extra calls add cost without improved adequacy;
- provenance/authority becomes harder to inspect;
- a single bounded method plus deterministic validation performs equivalently.

---

## 16. Risks and mitigations

### Risk 1 — deterministic creep into semantic hardcoding

**Failure:** each new dependency/update pattern produces another parser/rule.

**Mitigation:** define grammar around source constructs/relations, not known outcomes; enforce Minimum Useful Generality; keep unsupported meaning unresolved.

### Risk 2 — proposition explosion / knowledge-graph overengineering

**Failure:** introduce a universal graph/ontology before product need.

**Mitigation:** use the minimum candidate/proposition representation already implied by the Product Decision Model and Workspace; add graph structure only when real relations require it.

### Risk 3 — multi-agent complexity becomes a new rabbit hole

**Failure:** orchestration/framework work overtakes product evidence quality.

**Mitigation:** roles before agents; same-model sequential calls before frameworks; one bounded comparison; strict stop/rejection gates.

### Risk 4 — model-derived propositions gain hidden authority

**Failure:** a typed model output looks trustworthy because it is structured.

**Mitigation:** preserve producer/method identity; evaluation owner is explicit; schema validity never equals semantic support.

### Risk 5 — validator becomes ceremonial

**Failure:** validator simply agrees with proposer or only checks citations syntactically.

**Mitigation:** give validator the proposition, relevant basis, counterevidence/unknowns and frozen evaluation question; measure contradiction detection and unresolved preservation.

### Risk 6 — autonomy value is accidentally lost

**Failure:** deterministic redesign makes investigation rigid and misses useful adaptive evidence selection.

**Mitigation:** retain autonomous investigation as a future acquisition responsibility; reintroduce it after downstream interpretation/evaluation is qualified.

### Risk 7 — exposed development cases become hidden acceptance tests

**Failure:** method is repeatedly tuned until HTTPX/glyphsLib pass and then described as general.

**Mitigation:** explicitly label them development fixtures; freeze method before protected cases; material post-freeze change resets qualification.

### Risk 8 — product usefulness remains abstract

**Failure:** architecture becomes internally rigorous but does not help maintainers.

**Mitigation:** after method qualification, test the complete maintained output against the Charter action responsibility and maintainer usefulness, not just proposition accuracy.

---

## 17. Expected maintainer-facing effect of the proposed architecture

The internal machinery exists to produce a concise result like:

```text
Update
httpx 0.27.x → 0.28.x

Established
- captured new HTTPX Client signature no longer accepts `app` [evidence]
- one captured older Starlette TestClient call explicitly forwards `app` [evidence]

Unresolved
- the target's actual installed FastAPI/Starlette implementation is not established by the retained target evidence

Technical state
- the supplied source pair establishes a conditional source-level incompatibility path for the older captured caller
- target applicability remains unresolved until the target framework/runtime binding is established

Useful next evidence
- establish the target's actual FastAPI/Starlette binding at the relevant revision, or execute the relevant target test under the proposed dependency environment if that check is admitted

Maintainer action
- determined later by the accepted synthesis permissions from evaluated technical state
```

The product should not expose the maintainer to 25k-token prompts, internal agent debates or experiment accounting. Those mechanisms exist only to make the concise result trustworthy.

---

## 18. Architectural compatibility and required future decisions

### 18.1 No Charter change is required by this proposal

The mission, user, supported actions, frozen product boundary and claim limits remain unchanged.

### 18.2 No immediate ADR is required

This proposal does not yet select a consequential implementation structure such as a new model topology, graph, service or persistence mechanism. ADR-0012 already provides the canonical Workspace authority boundary.

A new/amended ADR may become appropriate only after evidence selects a durable proposition/evaluator/agent topology that is consequential enough to own architecturally.

### 18.3 A separate implementation plan is required

If Ali accepts the direction, the next artifact should be a bounded design/implementation plan for the deterministic source-fact/relation baseline and proposition handoff. This proposal itself does not authorize Build.

### 18.4 Mature-system horizon may later be reconciled

The [Mature System Horizon](UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md) already describes broad discovery as hybrid and distinguishes discovery from applicability. After the next bounded design earns evidence, that non-controlling horizon may be updated to reflect the more explicit proposition/evaluation and responsibility-decomposition direction.

---

## 19. Proposed decision record

If accepted, record the strategic decision approximately as:

> UpgradePilot retains the hybrid evidence-first architecture and canonical Workspace. The completed broader-agency and supplied-evidence experiments do not justify continued monolithic prompt tuning or immediate autonomous-discovery optimization. Autonomous investigation remains a credible acquisition/investigation responsibility because prior Agent arms demonstrated useful adaptive evidence discovery and descriptive efficiency, but agent/model outputs do not receive semantic, adequacy or maintainer-action authority by themselves. The next product-development direction is evidence/proposition-first responsibility decomposition: use deterministic methods for justified mechanical facts/relations, bounded semantic interpretation for irreducible meaning, explicit candidate propositions, admitted proposition evaluation/validation, and separate maintainer-action synthesis. Multi-role/multi-agent execution remains a serious future experiment after the proposition/evaluation interfaces exist. The immediate next bounded design is a general deterministic source-fact/relation baseline with provenance, supported-grammar limits and unresolved dynamic cases. No new prompt/model/agent run is selected by accepting this direction.

---

## 20. Questions deliberately left open

This proposal does not pre-decide:

1. the exact Python representation of candidate/evaluated propositions;
2. whether the first source-relation baseline should use `ast`, CST tooling or another bounded parser;
3. how much alias/import/call binding belongs in the first supported grammar;
4. which proposition evaluations are fully deterministic versus semantic;
5. whether semantic interpretation and validation should use the same model or different deployments;
6. whether a future multi-role method should be sequential calls, true autonomous agents or another topology;
7. whether stateful model transport is worthwhile after explicit working-state/projection design;
8. how protected holdout cases should be selected and scored;
9. when autonomous discovery is mature enough to reconnect to the proposition path;
10. whether/when a consequential topology warrants a new ADR.

These are future bounded decisions. Keeping them open prevents this proposal from turning evidence-backed direction into premature architecture.

---

## 21. Proposed immediate next step

If this proposal is accepted:

1. update live memory to record the instruction-tuning stop line and strategic direction;
2. retain the completed negative experiments unchanged;
3. write a bounded plan for **general deterministic source-fact/relation baseline + proposition handoff**;
4. review that plan before implementation;
5. do not run another model/agent experiment until that next plan establishes why the run is the smallest discriminating test.

This is the smallest course correction that uses what the project has learned without discarding the useful Workspace, evidence, run-control, Agent-discovery and semantic-reasoning work already earned.

---

## 22. Reference index

### Controlling / accepted product owners

- [Project Charter](../PROJECT_CHARTER.md)
- [Core Pipeline and Contract Specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [Product Decision Model Specification](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)
- [Maintainer Action Synthesis Specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)
- [Minimum Useful Generality Specification](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- [ADR-0012 — Canonical Investigation Workspace and recovery boundary](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md)
- [Mature System Horizon](UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md)

### Current main-branch experiment evidence

- [AUDIT-011 — Investigator experiment validity/progress](../audits/2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md)
- [Completed supplied-evidence capability diagnostic](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/README.md)
- [Capability diagnostic review adjudication](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/review-adjudication.json)
- [Instruction-only comparison plan](../plans/INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md)
- [Completed instruction-only comparison/source audit](../working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md)
- [Evidence-first interpretation Build cycle](../working-memory/2026-10-19_investigator-evidence-first-interpretation-build_lbd-cycle.md)

### Broader-agency research evidence

- Branch: `codex/broader-llm-agency-research-2026-10-05`
- [Completed repaired Fixed/Agent Contract-2 comparison](https://github.com/motafegh/UpgradePilot/blob/codex/broader-llm-agency-research-2026-10-05/working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/README.md)
- [Evidence-interface / interpretation diagnostic](https://github.com/motafegh/UpgradePilot/blob/codex/broader-llm-agency-research-2026-10-05/working-memory/evidence/2026-10-07-broader-agency-evidence-interface/README.md)
- Completed comparison checkpoint commit: `cde0ea99`

---

## 23. Bottom line

UpgradePilot should not conclude that intelligence must be removed from the product. It should conclude that **intelligence must be placed behind explicit evidence and authority boundaries**.

The project has now accumulated enough evidence to stop asking one model to rediscover every mechanical relationship, validate its own interpretation and recommend action in the same responsibility.

The proposed direction is therefore:

```text
use deterministic structure where meaning is genuinely mechanical
+
use LLM/agent capability where semantic/adaptive reasoning adds value
+
make model outputs propositions rather than authority
+
validate/evaluate before decision
+
keep maintainer-action synthesis separate
+
qualify each responsibility against simpler baselines and protected evidence
```

That direction preserves the useful lessons from both the successful engineering work and the negative experiments, while moving the project back toward its real objective: **reliable, explainable and useful dependency-update decision support for maintainers.**
