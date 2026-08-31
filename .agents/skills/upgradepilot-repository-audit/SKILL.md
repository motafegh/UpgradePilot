---
name: upgradepilot-repository-audit
description: Critically audit or review UpgradePilot governance, plans, architecture, implementation, tests, evidence, or recent work while preserving read-only intent, separating authority from implementation truth, checking necessity and end-to-end ownership, and reporting evidence-backed findings proportionately.
---

# UpgradePilot Repository Audit

Use this Skill as the reusable procedure for materially evaluative UpgradePilot work such as:

```text
audit this implementation
review the recent design/code/tests
critically examine what we just built
audit governance/specification files
check whether this mechanism is justified
check whether the plan, design, source, and tests still agree
```

**Skill provenance marker:** `UP-SKILL:upgradepilot-repository-audit`

This Skill is **procedural and non-controlling**.

Root `AGENTS.md` owns authorization, operation routing, and repository-wide standing safeguards. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing, reasoning, proportionality, evidence interpretation, and implementation-retention method. Specifications, ADRs, plans, source/tests, `audits/README.md`, and other responsibility owners retain their own authority.

An audit finding is evidence and judgment. It does **not** authorize implementation, silently supersede another owner, or become live project state.

For substantive Audit, consult the relevant `OPERATING_GUIDE.md` sections when their owned reasoning, proportionality, evidence, retention, Learning-by-Doing, or handoff responsibilities are material rather than relying only on summaries in this Skill.

## Activation and action boundary

Activate this Skill when the user explicitly asks for audit/review/critical examination or when the selected task is materially evaluative across responsibility, correctness, necessity, ownership, proof, maintainability, or governance consistency.

Do not force-load the full Skill for a narrow factual lookup or ordinary explanation that does not require evaluative judgment.

For audit/review intent:

```text
inspect
→ reason
→ report
→ preserve a durable audit only when justified
→ STOP
```

Do **not** modify product source, tests, governance, plans, specifications, ADRs, or other project controls merely because the audit found a defect or obvious fix.

If the user separately and explicitly requests changes, that is a new/combined action boundary governed by root `AGENTS.md` and the applicable Planning/Build procedure.

### Conditional context routes during Audit

**REQUIRED FOR THIS SUBSTANTIVE PROCEDURE**

- this Skill once materially evaluative Audit/Review is selected;
- the exact owners and implementation/observed evidence required to answer the audit question;
- relevant `OPERATING_GUIDE.md` sections when its owned reasoning/evidence/proportionality responsibilities are material.

**CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS**

- `MEMORY.md` only when live continuation/selection is part of the audit question;
- `ENVIRONMENT.md` when runtime/topology/local-service/freshness facts materially affect observed truth or proof interpretation;
- `SECURITY.md` when credentials/private data/untrusted external execution or mutation/transport boundaries are part of the audited responsibility;
- applicable specifications/ADRs/plans when their owned semantics/method/sequence are actually part of the consistency chain;
- `audits/README.md` only when preserving/reusing a durable audit record becomes justified;
- [conditional audit probes](references/conditional-audit-probes.md) only when their Source-Clarity/maintainability or governance-system trigger is present;
- Planning/Design or Build only when the user separately authorizes those operations after or alongside Audit; Audit itself does not mutate.

**DO NOT LOAD REFLEXIVELY**

- live state, environment/security facts, every artifact layer, detailed probes, broad history, or mutating Skills merely because Audit is active.

Once the audit responsibility is established, ordinary inspection/reasoning steps inherit this route. Re-evaluate conditional owners only when evidence materially changes the owner, environment, security, proof, or operation boundary.

## Audit depth

Use one Skill at proportional depth rather than separate small/medium/large audit procedures.

### A. Bounded review

Use for one file, mechanism, plan question, design choice, test boundary, or local concern.

Typical shape:

```text
observation
→ assessment/finding
→ evidence
→ consequence
→ smallest justified disposition
```

Do not create a durable audit record merely because a bounded review happened.

### B. Cross-responsibility audit

Use when the question spans several modules/owners or asks whether a material design/implementation boundary is coherent.

Add only the relevant deeper traces:

- owner map;
- requirement/design/implementation relationship;
- producer → integration/composition → consumer trace;
- overlapping-evidence analysis;
- spec/ADR/plan/source/test consistency;
- alternatives/trade-offs;
- proof gaps and uncertainty.

### C. Governance-system audit

Use when the controls themselves are the subject.

Add:

- instruction ownership and authority boundaries;
- canonical owner vs deliberate reinforcement;
- activation/context cost;
- duplicate or conflicting semantic ownership;
- live-state leakage;
- deterministic-enforcement opportunities;
- behavioral regression coverage;
- unnecessary persistent agent machinery or client-specific duplication.

Do not turn a local implementation review into a governance-system audit without a material reason.

## Procedure

### 1. Establish the exact audit question

Identify:

- repository/ref/revision when material;
- exact responsibility or artifact set;
- inclusions and exclusions;
- whether the question is correctness, necessity, ownership, consistency, proof strength, maintainability, governance quality, or a combination;
- the audit depth actually justified.

Preserve explicit exclusions. Do not widen scope merely because adjacent issues are interesting.

### 2. Load only the needed owners

Start from root/nearest applicable `AGENTS.md` and load only responsibility owners that can answer the audit question.

Examples:

- stable product boundary/claims → `PROJECT_CHARTER.md`;
- stable technical invariants → applicable specification;
- consequential implementation/structural method → applicable ADR;
- bounded execution/proof sequence → selected plan;
- live continuation only when relevant → `MEMORY.md`;
- durable audit artifact rules only when preservation is justified → `audits/README.md`;
- implementation truth → active source/tests/commands/output/environment evidence.

Do not reflexively scan archives, superseded plans, old working-memory, proposals, learning packages, environment facts, or unrelated controls.

History is evidence only when a precise provenance/comparison/rationale question requires it. If an owner that was initially irrelevant becomes material because of what the audit uncovers, treat that as a conditional-routing trigger and consult the canonical owner before classifying the finding.

### 3. Establish implementation or observed truth independently

When actual behavior is part of the audit, inspect executable/observed evidence rather than accepting documentation claims as implementation proof.

Keep distinct:

```text
accepted requirement / invariant
accepted method / architecture decision
selected execution plan
actual source/test behavior
tool/experiment evidence
historical rationale or provenance
```

A specification may be right while implementation is wrong; implementation may reveal that a specification is stale; a plan may be stale without changing either; passing tests may preserve current behavior without establishing necessity.

Do not collapse these possibilities into one generic “mismatch.”

### 4. Build the smallest cross-owner consistency chain required

When several artifact layers are relevant, inspect the chain proportionately:

```text
Charter / admitted product boundary, when material
→ specification / stable required behavior
→ ADR / consequential implementation method, when one exists
→ selected plan / bounded execution and proof
→ active source/tests/evidence / implemented truth
→ live state only if continuation is part of the question
```

Not every responsibility needs every layer. Absence of an unnecessary ADR/plan is not a defect.

For each layer that does exist, ask:

- does it stay inside its responsibility?
- does it still agree with stronger/current owners where their responsibilities touch?
- has one layer silently superseded another without an owning change?
- is a historical or planning statement being treated as present implementation truth?

Classify the drift precisely: requirement drift, method/ADR drift, plan drift, implementation defect, test/proof gap, documentation drift, state leakage, or unresolved conflict.

### 5. Apply the relevant audit lenses

Do not mechanically run every lens. Select the lenses that can change the conclusion.

#### 5.1 Correctness

Ask:

- does observed behavior satisfy the admitted responsibility?
- are meaningful success/problem/failure states represented correctly?
- are important edge cases or ambiguity boundaries mishandled?
- do focused tests protect the intended contract or only incidental mechanics?

#### 5.2 Implementation fact vs rationale vs judgment

Keep four questions separate:

```text
CURRENT IMPLEMENTATION FACT
What source/tests actually do today.

RATIONALE / FAILURE MODE
What supported product need, ambiguity, risk, proof boundary, or compatibility obligation the mechanism is meant to serve.

ENGINEERING JUDGMENT
Whether the mechanism is correct, necessary, proportional, well-placed, too weak, too broad, redundant, or a simplification candidate.

AUTHORITY BOUNDARY
What artifact/action would be required to change the accepted behavior/design/implementation.
```

Never invent an attractive rationale to make existing code or documents appear intentional.

If evidence establishes behavior but not rationale, say `UNCERTAIN / AUDIT NEEDED` and identify the smallest evidence that could discriminate further.

#### 5.3 “Why is this needed?” / necessity analysis

When necessity is material, use the project-wide reasoning sequence from `OPERATING_GUIDE.md`:

```text
1. proposition / design goal
2. necessity class
3. correct responsibility / owner / layer
4. evidence for the rationale
5. credible alternative / trade-off
```

Use the narrow reasoning vocabulary when helpful:

- **PROPOSITION-ESSENTIAL**;
- **CURRENT-IMPLEMENTATION REQUIREMENT**;
- **DEFENSIVE / BOUNDARY HARDENING**;
- **UNCERTAIN / AUDIT NEEDED**.

These are reasoning labels, not product enums.

Do not answer `why do we need X?` with only `because the code/tests/caller use X`.

#### 5.4 Retention / `JUST-*`

Apply Core `JUST-001` through `JUST-005` whenever an existing or proposed mechanism is being justified or retained.

The following are migration/regression evidence, not sufficient architectural authority by themselves:

```text
it already exists
passing tests use it
a caller consumes it
comments describe it
an old plan/ADR once used it
we already spent effort on it
an internal function can be called inconsistently
an artificial fixture can violate an upstream invariant
```

Require an independently admitted responsibility, proof need, material risk, or real compatibility/external obligation.

#### 5.5 End-to-end ownership

For a material field/check/transformation/validation/provenance value, do not decide ownership from the local file alone.

Trace only as far as needed:

```text
exact proposition / behavior supplied here
→ producer that creates the relevant fact/object
→ integration/composition path
→ earliest sufficient boundary already guaranteeing the proposition
→ downstream consumer/repetition
→ whether the later boundary is independently supported
→ concrete failure/proof loss/risk remaining without the repeat
→ KEEP / MOVE / NARROW / REMOVE
```

A later check may be justified when it joins independently produced evidence, proves a distinct cross-object/domain proposition, intentionally distrusts an upstream boundary, or controls a material risk not already controlled upstream.

Direct internal callability and fabricated inconsistent fixtures are not independent production contracts unless that alternate route is explicitly admitted and tested.

#### 5.6 Overlapping evidence

When multiple artifacts or evidence objects partially overlap, do not force a fake clean split.

Identify, when material:

```text
what each artifact directly establishes
where information overlaps
what is primary vs derived/duplicated
what current implementation actually consumes
what none of the artifacts can prove alone
what relation exists only when the artifacts are combined
```

This is especially important when independently valid evidence can still be incoherent when composed.

#### 5.7 Proof strength and claim boundaries

Distinguish:

- source fact;
- test-protected behavior;
- specification requirement;
- ADR decision;
- plan expectation;
- one-case/manual/tool evidence;
- experiment evidence;
- inference or engineering judgment;
- unsupported stronger claim.

State both what the evidence establishes and what it does not establish when overclaiming is plausible.

Do not promote one fixture, one public case, one developer tool, or one experiment pass into broader product correctness/compatibility/safety claims.

If runtime/topology/environment facts affect the proof class or explain a missing/failed execution surface, consult `ENVIRONMENT.md` before turning the immediate runner/tool state into a conclusion about the repository or local development environment.

#### 5.8 Complexity and proportionality

Apply Ceremony Tax to existing and proposed complexity.

Ask:

```text
what capability / risk / external obligation does this mechanism serve?
what evidence shows that need is real now?
what is the simplest adequate mechanism?
what maintenance/context/coordination cost does the current design impose?
what removal/reassessment trigger exists when material?
```

Do not call something overengineered merely because it is unfamiliar or sophisticated.

#### 5.9 Test value and suite proportionality

When tests or the test suite are materially under audit, evaluate them by **independent proof responsibility**, not by raw test count, file count, line coverage, or a preference for either more or fewer tests.

For a suspicious test or family, trace proportionately:

```text
test / test file
→ exact current behavior, failure, boundary, regression, invariant, or composition seam protected
→ whether nearby tests already establish that same proof adequately
→ whether this test protects a distinct source shape, trust boundary, failure class, or cross-layer relationship
→ cheapest adequate proof layer and responsibility-owned test home
→ KEEP / SHRINK / MERGE / RENAME / MOVE / REMOVE
```

Treat these as common duplication/ceremony signals, not automatic deletion rules:

- the same function branch repeated in several files with materially equivalent fixtures/assertions;
- plain record/dataclass construction followed only by read-back assertions;
- successful imports followed only by `is not None` assertions;
- package-manager/environment facts re-tested without a distinct UpgradePilot contract;
- tests named only for a historical step/phase after the behavior has a permanent responsibility owner;
- implementation-shape assertions with no accepted behavior/compatibility reason.

Conversely, do **not** collapse a boundary/integration test merely because all constituent units have unit tests. A test may uniquely protect composition, authority binding, unresolved-state propagation, source identity, or a real cross-module regression.

Before recommending deletion or merge, identify any unique behavior/proof that would be lost and where it will remain protected. The target is the **smallest sufficient proof set**, not an arbitrary reduction percentage.

If the user separately authorizes test cleanup in the same request, finish the evaluative classification first, then transition through the Build procedure for the actual mutations and focused/broader regression validation. Do not let an Audit finding silently mutate tests.

#### 5.10 Source clarity and maintainability

Use the seven Source Clarity outcomes in `OPERATING_GUIDE.md` plus the Naming Clarity specification. Review outcomes, not comment volume, and let names/structure carry responsibility before comments compensate for ambiguity.

**CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS:** load [the conditional audit probes](references/conditional-audit-probes.md) and apply its Source-Clarity / maintainability family when source readability or maintainability is materially part of the audit and deeper probes are needed—for example non-obvious cross-file flow, semantic/proof transformations, decision boundaries, API/type-state ambiguity, domain vocabulary, or current/transitional/legacy surfaces.

For an ordinary audit without material Source-Clarity pressure, **DO NOT LOAD REFLEXIVELY** the deeper probes merely because source files are being inspected.

#### 5.11 Governance quality

When governance, agent controls, Skills, or the governance evaluation harness itself is materially under audit, **CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS:** load [the conditional audit probes](references/conditional-audit-probes.md) and apply its governance-system quality family for questions such as canonical ownership, deliberate reinforcement, activation/context cost, routing distinctness, state leakage, deterministic enforcement, behavioral coverage, or persistent agent machinery.

Do **not** load governance-system probes for an ordinary implementation/design audit merely because governance files exist in the repository.

### 6. Classify findings precisely

Keep separate when material:

```text
OBSERVATION
what was directly inspected

EVIDENCE / CONTEXT
where the observation came from and its proof class

INTERPRETATION
what the evidence most strongly implies

UNCERTAINTY
what remains unresolved

FINDING
correctness / ownership / necessity / proof / maintainability / governance conclusion

CONSEQUENCE
why it matters to the admitted responsibility

DISPOSITION
KEEP / MOVE / NARROW / REMOVE / FIX / RE-SPECIFY / RE-PLAN / REASSESS / DEFER / NO CHANGE

NEXT DISCRIMINATING CHECK
only when more evidence is actually needed
```

Use severity only when it helps prioritize impact. Severity reflects project consequence, not rhetorical intensity.

### 7. Choose the smallest justified disposition

Prefer the minimum change in responsibility needed to resolve the issue.

Examples:

- implementation defect under a sound specification → implementation/test change;
- accepted behavior itself is wrong/outdated → specification change before implementation follows;
- durable implementation method changed → ADR update/supersession when justified;
- execution sequence/proof became stale → plan update;
- comment/doc drift only → documentation correction;
- unsupported concern → preserve uncertainty or request one discriminating check rather than inventing a redesign.

An audit recommendation still does not authorize the change.

### 8. Preserve durable audit evidence only when warranted

Consult `audits/README.md` when a finding has future review/reassessment value that would otherwise be lost.

Rules:

- reuse an existing audit when the same question already has a durable record;
- do not create an audit merely because review occurred;
- compact audit is the default for one bounded durable concern;
- formal audit is justified only for several findings, consequential cross-owner review, or meaningful follow-up/lifecycle needs;
- audit records remain non-controlling;
- accepted conclusions must be promoted to the actual specification/ADR/plan/implementation owner rather than left only in an audit record.

Do not create or expand a durable audit artifact solely to preserve this Skill's provenance marker.

### 9. Report exact evidence and limitations

Prioritize material findings over exhaustive commentary.

State:

- inspected revision/scope when material;
- exact files/symbols/tests/evidence supporting conclusions;
- important exclusions;
- what was not inspected;
- what could not be proven;
- where the conclusion is engineering judgment rather than directly observed fact.

Do not manufacture certainty.

### 10. Stop at the audit boundary

For audit/review-only work, stop after the findings, dispositions, and any justified audit record.

Do not begin fixing, refactoring, rewriting plans, or changing governance in the same action unless the user also explicitly requested those mutations.

## Learning-by-Doing composition

When substantive Audit runs under Learning-by-Doing, the primary operation remains Audit and therefore remains read-only unless separate change intent exists.

Use `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` only when the full learning/action cycle is useful or the user explicitly invokes it.

During composition:

- orient the real responsibility before criticizing it;
- explain unfamiliar mechanisms only to the depth required for the audit;
- let Ali predict, challenge, classify necessity, or propose a discriminating check when prerequisites are available;
- evaluate Ali's hypothesis, current code, previous assistant claims, and documents by the same evidence standard;
- correct earlier assistant oversimplification explicitly when evidence disproves it;
- do not confuse Ali's agreement with technical validation;
- do not turn the audit into a course on every inspected file.

Normal Learning-by-Doing critical thinking does not automatically require this full Audit Skill. Activate the full Audit procedure when evaluation itself is material or explicitly requested.

## Output shape

For a bounded review, prefer:

```text
scope
→ material observation/finding
→ evidence
→ consequence
→ smallest disposition
→ limitation, if any
```

For a deeper audit, use a compact findings structure such as:

```text
scope + inspected revision
owner/consistency map when material
material findings ordered by impact
  - observation/evidence
  - interpretation + uncertainty
  - consequence
  - recommended disposition
proof/architecture implications
explicit exclusions/limitations
```

Do not require finding IDs or a formal audit template when a short evidence-backed review is sufficient.

## Anti-patterns

Do not:

- mutate the repository merely because an audit found a fix;
- treat plans/specifications/ADRs/comments as implementation proof;
- preserve a mechanism only because callers/tests/history use it;
- invent design rationale from current code shape;
- decide cross-layer ownership from one local file;
- treat fabricated fixtures or unsupported direct calls as production contracts;
- require every artifact layer to exist;
- call every overlap duplication when the relation is independently meaningful;
- treat every learning critique as a formal audit;
- create a durable audit record for every observation;
- reward documentation/comment volume rather than clarity outcomes;
- scan the entire repository when a bounded evidence slice can answer the question;
- generalize one case beyond its proof strength;
- let a recommendation silently become authority.

## Completion check

Before closing a material audit, confirm proportionately:

```text
exact question answered or explicitly left uncertain
+ implementation/observed truth independently established where relevant
+ applicable owners distinguished
+ newly triggered conditional owners/references consulted when material
+ necessity/ownership/proof lenses applied where material
+ test value/duplication assessed by independent proof responsibility when tests are in scope
+ cross-owner consistency checked when the question spans owners
+ findings distinguish observation from interpretation/judgment
+ smallest justified disposition identified
+ durable audit record created/reused only when warranted
+ no unauthorized mutation occurred
```

When this full Skill was materially used, include `UP-SKILL:upgradepilot-repository-audit` once in the normal completion/handoff provenance when practical. Marker presence records claimed Skill activation only; the actual read-only trajectory, owner selection, evidence, findings, and stopping behavior establish compliance.