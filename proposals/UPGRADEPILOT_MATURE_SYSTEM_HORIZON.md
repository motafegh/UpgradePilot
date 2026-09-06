# UpgradePilot Mature System Horizon

**Version:** 0.1  
**Recorded:** 2026-08-11  
**Owner:** Ali Rajabi  
**Status:** Evolving non-controlling mature-system horizon — partially grounded in accepted design, partially open, and intentionally revisable  
**Authority:** None by itself. This file synthesizes the mature product horizon; it does not override the Project Charter, route, selected plans, accepted specifications, ADRs, source/tests, or `MEMORY.md`.

## 1. Purpose

For broader maintainer journeys, operational completion, expansion choices, and balanced AI/backend/applied-ML learning outcomes, see the [End-to-End Product and Engineering Proposal](2026-09-05_UPGRADEPILOT_END_TO_END_PRODUCT_AND_ENGINEERING_PROPOSAL.md). It is a non-controlling companion and does not replace this horizon's reasoning-system orientation.

This file answers one orientation question:

> **If UpgradePilot matures successfully inside its product boundary, what whole system are we trying to grow toward, where do today's implemented slices belong, and which major responsibilities are still unresolved?**

It exists because the mature-system picture is otherwise distributed across the Charter, route, specifications, ADRs, A→C decision-model work, product-simulation evidence, bounded plans, source, tests, and dated records.

This is not a source-tree plan, implementation roadmap, or promise that every conceptual responsibility becomes a separate module, service, agent, model, graph, or directory.

Use it as:

- a whole-system orientation map;
- a design-discussion compass;
- a place to distinguish accepted responsibilities from open design questions;
- a way to understand where a bounded implementation slice sits inside the larger product;
- a reconciliation surface when new product-simulation evidence challenges the current horizon.

Do not use it as:

- live project state;
- authorization to implement future capabilities;
- a final mechanism taxonomy;
- an accepted architecture decision;
- proof that a capability exists.

## 2. Controlling sources this horizon must remain compatible with

This horizon is subordinate to the normal repository owners:

- `../PROJECT_CHARTER.md` — mission, user, supported decision, product boundary, evidence doctrine, claim limits;
- `../plans/UPGRADEPILOT_90_DAY_PLAN.md` — route stages, gates, stable end-to-end flow horizon;
- `../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md` — first public-PR vertical slice;
- `../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md` — currently admitted A→B→C decision foundation;
- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` — trust/evidence pipeline invariants;
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md` — variable-input generality and non-hardcoding boundary;
- accepted ADRs — durable implementation/structural choices already made;
- `../src/upgradepilot/` + `../tests/` — implemented product behavior;
- `../product-simulation/` and the active product-simulation branch — discovery/pressure-test evidence;
- `../MEMORY.md` — sole owner of live project position and continuation.

Historical ambition material, especially `2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md`, is useful input but is not inherited as accepted architecture. Its ideas must be reconciled through the product model earned since then.

## 3. Status legend

This file uses the following conceptual labels:

- **ACCEPTED** — responsibility/boundary is already established by controlling or accepted project artifacts.
- **IMPLEMENTED SLICE** — real product code/tests implement at least one bounded manifestation.
- **PARTIALLY DESIGNED** — important semantics exist, but mature scope/contract is not complete.
- **OPEN DESIGN** — mature responsibility is visible, but its contract/method is not yet sufficiently designed.
- **EXPERIMENTAL POSSIBILITY** — plausible method or enhancement that requires later evidence-gated admission.

A responsibility can carry more than one label. Example: a responsibility may be **ACCEPTED** as a product need while its mature method remains **OPEN DESIGN**.

## 4. Mature end-to-end system horizon

```text
PUBLIC PYTHON DEPENDABOT PR
        │
        ▼
1. Admission + exact identity
   repository / PR / base / head / changed files / dependency / old→new
        │
        ▼
2. Public evidence acquisition
   PR + repository + package/index + upstream + target + CI/workflow evidence
        │
        ▼
3. Trust, normalization, provenance, and evidence-state handling
   raw/untrusted evidence → bounded trusted representations / explicit problems
        │
        ▼
4. Broad technical impact-candidate discovery
   "What materially relevant technical concerns might this update create
    for this exact target/context?"
        │
        ├─ mechanism-specific candidate A
        ├─ mechanism-specific candidate B
        ├─ mechanism-specific candidate C
        └─ potentially previously unseen justified candidate
        │
        ▼
5. Candidate grounding / formulation
   upstream mechanism
   + possible target exposure/relation
   + activation condition(s)
   + possible consequence
   + exact identity/provenance
        │
        ▼
6. Candidate-specific applicability
   propositions
   + evidence coverage
   + applicability paths
   + path-model coverage
        │
        ├─ established applicable
        ├─ established not applicable
        ├─ unresolved
        └─ conflicted
        │
        ▼
7. Discriminating investigation
   for material unresolved/conflicted state only
        │
        ├─ acquire missing exact evidence
        ├─ inspect target usage/context
        ├─ compare conflicting authority
        ├─ use an admitted targeted observation/check
        ├─ preserve non-dominated alternatives where appropriate
        └─ stop when no justified investigation remains
        │
        ▼
8. Observation feedback / candidate refinement
   validate evidential meaning
   → reevaluate propositions
   → refine/supersede candidate when the mechanism model itself changes
        │
        ▼
9. Cross-candidate + repository-context synthesis
   preserve applicable / eliminated / unresolved / conflicted candidates
   + contextual findings not reducible to one mechanism
   + candidate-discovery coverage limitations
        │
        ▼
10. Overall evidence sufficiency / residual uncertainty / policy relationship
        │
        ▼
11. Maintainer-facing synthesis
    merge after normal review
    / run targeted checks
    / investigate or block
    / defer
    / abstain
        │
        ▼
12. Traceable human + machine report
        │
        ▼
13. Reproducibility / replay / persistence / diagnosis / evaluation
```

The mature product is not expected to execute every box for every PR. Conditional activation and justified stopping are first-class behavior.

## 5. Responsibility map — what we know today

| # | Mature responsibility | Horizon state | Current understanding |
|---|---|---|---|
| 1 | Admission and exact PR/dependency identity | ACCEPTED + IMPLEMENTED SLICE | B2 has real public PR, base/head, changed-file and dependency-transition identity foundations. |
| 2 | Public evidence acquisition | ACCEPTED + IMPLEMENTED SLICE + future expansion | GitHub/PyPI/upstream/target/CI read-only evidence exists in bounded forms; B3 owns later robustness/broader acquisition. |
| 3 | Trust/provenance/evidence-state normalization | ACCEPTED + IMPLEMENTED SLICE | Raw evidence, source identity, grounding, mismatch/problem states, and deterministic trusted boundaries are central doctrine. |
| 4 | Broad impact-candidate discovery | OPEN DESIGN, responsibility identified | Mature product needs a way to discover plausible material mechanisms beyond one known family without one handcrafted interpreter per category. |
| 5 | Mechanism-specific technical impact-candidate formulation | ACCEPTED + PARTIALLY DESIGNED + IMPLEMENTED SLICE | A established candidate ≠ established applicability. Python support-drop is the first real candidate family. |
| 6 | Candidate-specific applicability / evidence / coverage | ACCEPTED + PARTIALLY DESIGNED + IMPLEMENTED SLICE | Proposition states, evidence coverage, paths, path-model coverage, and conservative negative inference are established for the first slice. |
| 7 | Discriminating investigation selection and stopping | ACCEPTED + PARTIALLY DESIGNED | Conversation C closed conceptually; first runtime C activation remains to be implemented. |
| 8 | Observation feedback / candidate refinement lineage | ACCEPTED invariant, limited implementation | Observations normally reevaluate propositions; material mechanism-model change may refine/supersede candidates with minimum lineage. |
| 9 | Cross-candidate and repository-context synthesis | OPEN DESIGN / emerging | Needed to combine multiple candidates and important target-context findings without forcing every finding into mechanism applicability. |
| 10 | Overall evidence sufficiency / residual risk / repository policy | OPEN DESIGN | Deliberately separated as later Conversation D territory. |
| 11 | Maintainer-facing action projection | ACCEPTED output family + OPEN DESIGN method | Five action classes are Charter-owned; exact evidence-to-action synthesis is not yet finalized. |
| 12 | Human/machine output and traceability | ACCEPTED + IMPLEMENTED SLICE | B2 already owns concise output and machine-readable traceability; mature report content grows with reasoning capability. |
| 13 | Replay/persistence/diagnosis/evaluation | ACCEPTED route horizon + mostly future | B3/B5 own robustness, replay, persistence, corpus evaluation, diagnostics, cost/stopping evidence when gates activate. |
| 14 | Advanced models/graphs/agents/learned methods | EXPERIMENTAL POSSIBILITY | X1 may compare them against simpler baselines only after a real product/evaluation limitation exists. |

## 6. Broad technical impact-candidate discovery — the major open middle

### 6.1 Responsibility

The mature discovery responsibility is approximately:

```text
trusted dependency transition
+
relevant upstream/package evidence
+
target/repository context available at that point
→ one or more justified mechanism-specific technical impact candidates
   OR an explicit bounded no-candidate / insufficient-discovery state
```

It must answer:

> **What materially relevant technical concerns are justified enough to evaluate for this dependency update and this target?**

It must not answer by silently collapsing discovery, applicability, overall sufficiency, and final maintainer action into one model prediction.

### 6.2 Candidate discovery is not the same as applicability

```text
DISCOVERY
What concerns should enter consideration?

APPLICABILITY
For candidate C, does its mechanism actually apply to this exact target/revision/context?
```

A discovery mechanism may propose a candidate whose exposure/activation remains unresolved. That is legitimate. The candidate must then pass the B-level evidence/applicability process.

### 6.3 Candidate discovery is expected to be hybrid, not one giant rule table

The mature method is not selected, but credible inputs may eventually include:

#### Deterministic structured signals

Useful where the meaning is machine-readable or mechanically validated, for example:

- version/support metadata;
- dependency constraints;
- release/yank state;
- exact dependency transition and interval crossings;
- declared environment/platform information;
- package/build metadata.

#### Bounded semantic interpretation

Useful where authoritative upstream evidence describes open-ended technical changes in natural language, for example:

- API removal/deprecation;
- changed exception/error semantics;
- changed defaults;
- framework lifecycle behavior;
- configuration migration;
- compatibility/support statements.

The generality requirement is not "one phrase list per category". Variable natural-language interpretation needs a credible generalization mechanism plus deterministic trusted-boundary validation.

#### Target-driven discovery

Candidate discovery may also be informed by target structure rather than upstream text alone:

- imports/references;
- framework/declarative hooks;
- configuration use;
- dependency role/path;
- build/install surfaces;
- test/development-tool usage;
- repository-purpose/context contracts.

A mature design still needs to decide when target evidence should create a new candidate versus only evaluate an already-discovered candidate.

#### Structural relationships

Dependency or usage graphs may become useful if real cases show that flat evidence cannot represent the relevant relation. A graph is a possible method, not yet the definition of candidate discovery.

### 6.4 Discovery output should remain structured and challengeable

A candidate should eventually preserve enough information to challenge independently:

```text
candidate identity
mechanism/change fact
candidate source evidence
exact dependency transition
exact target/revision/context
possible exposure/relation
activation condition(s)
possible consequence
which components are grounded vs hypothetical
discovery reason
```

Candidate generation must not self-authorize:

- target exposure;
- activation;
- applicability;
- candidate-discovery completeness;
- final maintainer action.

### 6.5 Candidate-discovery coverage is its own epistemic problem

Keep this distinct from evidence coverage and path-model coverage:

```text
EVIDENCE COVERAGE
Did admitted evidence sufficiently cover proposition P?

PATH-MODEL COVERAGE
Did candidate C represent its material alternative applicability routes?

CANDIDATE-DISCOVERY COVERAGE
Did discovery identify enough material candidate mechanisms
for the broader conclusion being attempted?
```

Therefore:

```text
all discovered candidates established not applicable
!= transition proven to have no material impact
```

unless candidate-discovery coverage is independently sufficient for that stronger claim.

The mature discovery design must eventually define what "enough discovery" means for bounded supported conclusions without pretending universal completeness is achievable.

## 7. Provisional mechanism-family horizon

The following families are **orientation hypotheses, not a frozen taxonomy**. Real cases may merge, split, rename, or invalidate them.

### 7.1 Runtime/API/behavioral compatibility

Examples:

- removed or changed API;
- changed return/error/exception behavior;
- changed defaults;
- protocol/contract semantics;
- framework/declarative lifecycle behavior;
- dependency-controlled callbacks/hooks.

Product-simulation evidence such as the Pydantic validator behavior case shows that framework-mediated exposure can matter without proving that `framework` deserves a permanent separate top-level family.

### 7.2 Runtime/platform support

Examples:

- Python-version support changes;
- supported operating systems/platforms;
- architecture/environment support;
- runtime floor/ceiling changes.

The current Python-support-drop implementation is the first bounded member of this horizon.

### 7.3 Dependency/resolution behavior

Examples:

- dependency constraints;
- transitive dependency effects;
- peer/conflicting requirements;
- resolver/installability changes;
- dependency-role/path interactions.

### 7.4 Packaging/build/installation behavior

Examples:

- build backend changes;
- wheel/sdist availability or behavior;
- extras/optional dependencies;
- installation requirements;
- build isolation/toolchain compatibility.

### 7.5 Configuration/tooling behavior

Examples:

- configuration schema changes;
- removed/renamed options;
- changed configuration defaults;
- plugin/tool integration;
- test/development-tool behavior where the dependency is itself part of the repository's operational/test surface.

### 7.6 Integration/operational contracts

Examples:

- client/service protocol expectations;
- serialization/format contract changes;
- external integration semantics;
- concurrency/async lifecycle assumptions.

These remain inside the Charter boundary only when they arise as dependency-update evidence for the supported public-Python maintainer decision; UpgradePilot does not become a generic integration-analysis platform.

## 8. Important dimensions that are NOT mechanism families

Several concerns cut across every technical mechanism and should not be confused with the mechanism taxonomy.

### 8.1 Evidence condition

```text
available
missing
inaccessible
invalid
unsupported
conflicting
rejected
stale
superseded
```

### 8.2 Epistemic proposition state

```text
established
refuted
unresolved
conflicted
```

### 8.3 Coverage dimension

```text
evidence coverage
path-model coverage
candidate-discovery coverage
CI/test/behavior-path coverage where relevant
```

### 8.4 Temporal/revision dimension

```text
base vs head
exact PR head
changed head
release/yank/supersession sequence
decision-time evidence vs later evidence
```

### 8.5 Dependency role / target surface

```text
runtime
development/test
build
optional/plugin
transitive/resolution path
framework-mediated
configuration-driven
```

These roles may affect exposure/applicability but should not automatically become separate top-level impact families.

### 8.6 Repository-context findings

A dependency update can create a material repository-context inconsistency even when a deeper technical-compatibility proposition remains unresolved.

Fresh S009 product-simulation evidence provides a useful example:

```text
repository declares a publication-reproduction environment
+
dependency pin changes
+
repository's declared publication environment is not reconciled
→ repository-context inconsistency can be established
```

A costly scientific reproduction run would answer a different question and may not be justified merely because technical behavior remains unresolved.

This suggests mature UpgradePilot needs a place for important context/policy/provenance findings that are **not forced into mechanism-specific applicability** and that can support justified stopping for the question actually owned.

## 9. Candidate lifecycle horizon

A mature candidate should be able to move through an explicit lifecycle without losing lineage:

```text
DISCOVER
candidate proposed from evidence/context
        ↓
NORMALIZE / GROUND
identity, provenance, mechanism evidence validated
        ↓
FORMULATE
exposure + activation + possible consequence made explicit
        ↓
EVALUATE APPLICABILITY
candidate-specific propositions and coverage
        ↓
INVESTIGATE IF NEEDED
select discriminating evidence/check
        ↓
REEVALUATE
new observation updates proposition state
        ↓
REFINE / SUPERSEDE IF NEEDED
candidate model changes because the mechanism understanding changed
        ↓
SYNTHESIZE
candidate contributes to broader decision context
```

Deduplication/relationship handling between overlapping candidates remains an open design question. The mature system should avoid double-counting semantically equivalent candidates while preserving materially distinct mechanisms.

## 10. A→B→C→D reasoning spine

The post-reconciliation mature reasoning spine is currently:

```text
A — technical impact-candidate formulation
    what mechanism-specific concern is justified enough to consider?

B — candidate-specific applicability / evidence / composition
    what is established/refuted/unresolved/conflicted for this exact candidate and target?

C — discriminating investigation selection / feedback / stopping
    what observation could materially change the non-final state, and is it worth/admitted to pursue?

D — later overall sufficiency / residual risk / repository policy / maintainer-facing synthesis
    what overall action, if any, is justified after considering the relevant candidate/context state?
```

Two mature responsibilities sit around this spine:

```text
BEFORE A
broad candidate discovery

AFTER C / INTO D
cross-candidate + repository-context synthesis
```

Those two areas are currently less designed than A→C and are major future architecture questions.

## 11. Mature synthesis must preserve more than one scalar

The mature system should not reduce the PR to a single opaque score too early.

A future synthesis state may need to preserve, conceptually:

```text
candidate set
├─ established applicable candidate(s)
├─ established not applicable candidate(s)
├─ unresolved candidate(s)
└─ conflicted candidate(s)

+ candidate-discovery coverage
+ material repository-context findings
+ CI/test/observation coverage
+ unavailable/failed investigations
+ stopped questions and their stop reasons
+ remaining uncertainty
+ repository policy/context when admitted
```

Only after that does later D-level reasoning project the state into the Charter's five maintainer-facing actions.

## 12. Mature investigation horizon

Conversation C established a key mature behavior:

```text
material unresolved OR genuine conflict
+
uncertainty/conflict reason
→ discriminating target
→ one justified next investigation / small conditional sequence
   OR no further justified investigation
   OR non-dominated alternatives
```

Keep three boundaries separate:

```text
EPISTEMIC VALUE
Would the evidence materially discriminate the proposition?

EXECUTION ADMISSIBILITY
May UpgradePilot itself perform the check under capability/security boundaries?

MAINTAINER-FACING RECOMMENDABILITY
Should the maintainer later be asked to perform it?
```

The last belongs to later synthesis/policy territory.

Mature stopping must also remain question-specific. An unresolved deeper question does not require investigation when another already-established finding fully resolves the currently owned question and the deeper observation cannot change that result.

## 13. Evidence acquisition, replay, and temporal behavior horizon

The mature system should preserve exact decision context rather than only latest-state evidence.

Expected long-horizon responsibilities include:

- exact base/head/revision identity;
- raw or durable evidence references when justified;
- acquisition problems and degraded states;
- changed-head detection;
- yanked/superseded release evidence;
- decision-time vs later-evidence distinction;
- deterministic replay of preserved runs/evidence;
- retry/idempotency/recovery behavior;
- stale/superseded-result handling.

These primarily align with B3/B5 route responsibilities and should support the decision system rather than become a separate generic data platform.

## 14. Evaluation horizon

A mature UpgradePilot cannot be validated only by "did the code run?" or "did one known case match?"

Future evaluation should increasingly measure questions such as:

- Did candidate discovery surface the materially relevant mechanism(s)?
- Did it invent unsupported candidates?
- Did equivalent evidence wording normalize to equivalent technical meaning?
- Did changed meaning remain distinguishable?
- Did target applicability correctly separate exposure/activation from upstream mechanism existence?
- Did negative inference respect evidence/path/discovery completeness?
- Did the system remain unresolved/abstain when evidence was insufficient?
- Did chosen investigations materially discriminate the uncertainty?
- Did it stop when more work could not change the owned conclusion?
- Did changed-head, stale, conflicting, and failed-source conditions degrade safely?
- Did final maintainer-facing synthesis remain traceable to evidence rather than model authority?
- Did broader methods materially improve over simpler baselines?

B5 is the natural route location for durable corpus/diagnostic/cost/stopping evidence. X1 is the comparison gate for advanced methods.

## 15. Advanced-method horizon — method candidates, not product definitions

The Charter allows later evidence-gated experiments in methods such as:

- grounded LLM semantic interpretation;
- broader semantic candidate discovery;
- structural/usage/dependency graphs;
- learned ranking/classification;
- bounded multi-agent investigation;
- richer differential or targeted execution methods.

The mature product responsibility must be defined independently of these technologies.

Example:

```text
PRODUCT RESPONSIBILITY
broad candidate discovery

POSSIBLE METHODS
bounded semantic model
+ deterministic metadata rules
+ target structural analysis
+ optional graph representation
```

Do not define the product as "an agent system" or "an impact graph" before comparative evidence shows that method is the best owner of the responsibility.

## 16. Relationship to the 90-day route

A useful mature mapping is:

### B2 — prove the central semantic spine on one real vertical slice

- public PR identity;
- dependency transition;
- minimum evidence;
- first mechanism-specific candidate;
- applicability foundation;
- first discriminating investigation;
- bounded decision/output.

### B3 — make acquisition/replay behavior robust

- evidence preservation;
- failed/partial acquisition;
- changed head;
- retry/recovery;
- deterministic replay;
- broader required public acquisition.

### B4 — expand deterministic context and decision support

Expected pressure areas include:

- more real technical mechanism families;
- repository usage/exposure interpretation;
- dependency role/path;
- activation mapping;
- broader candidate discovery contract;
- targeted checks;
- richer stopping and abstention behavior;
- conditional analysis.

### B5 — persistence, diagnosis, and evaluation

- justified durable run/evidence state;
- queries/diagnostics;
- staged corpus;
- discovery/applicability/investigation evaluation;
- cost/stopping/coverage evidence;
- temporal supersession/idempotence where needed.

### X1 — evidence-gated advanced method comparison

Only after a concrete limitation exists:

- LLM/semantic-discovery alternatives;
- graph alternatives;
- learned ranking;
- agentic investigation;
- other advanced methods.

### C1 — harden the supported mature core

- reproducible setup;
- representative normal/failure/changed/early-stop cases;
- secure configuration;
- diagnostics/recovery;
- explicit limitations;
- implementation ownership and defensible portfolio claims.

## 17. Conceptual architecture boundaries — not folder commitments

As the product matures, responsibilities may eventually cluster approximately like:

```text
application / orchestration
│
├─ identity + acquisition providers
├─ evidence trust / normalization
├─ semantic interpretation
├─ candidate discovery
├─ mechanism-specific impact models
├─ target context / applicability
├─ investigation
├─ synthesis / decision
├─ output / traceability
└─ persistence / replay / evaluation support
```

This diagram names responsibilities, not required Python package names.

Do not infer that mature source must contain folders named `discovery/`, `decision/`, `graph/`, or `planner/`. Source structure should follow demonstrated implementation ownership when those responsibilities activate.

## 18. Major open design questions

These are the highest-value mature-system questions currently visible.

### Candidate discovery

1. What exact input boundary activates broad candidate discovery?
2. How much upstream evidence should be collected before discovery versus requested after a candidate emerges?
3. Can one structured candidate schema span materially different mechanisms without becoming vague?
4. When should deterministic structured signals directly create candidates?
5. What semantic generalization method can discover previously unseen technical change categories?
6. When can target structure create a candidate rather than only evaluate exposure?
7. How are duplicate/overlapping candidates normalized and related?
8. What justifies candidate-discovery coverage sufficient for a bounded absence claim?
9. When should discovery stop?

### Mechanism families

1. Which currently observed families are genuinely distinct responsibilities?
2. Which are merely different target exposure surfaces or dependency roles?
3. How many materially different real cases are needed before freezing a reusable abstraction?

### Cross-candidate synthesis

1. How should multiple applicable/unresolved/conflicted candidates coexist?
2. How should repository-context findings interact with technical candidates?
3. How should discovery-coverage limitations constrain global conclusions?
4. How should one decisive concern interact with unrelated unresolved candidates?

### Later D semantics

1. What constitutes overall evidence sufficiency for each action family?
2. How does repository policy/context enter without replacing evidence truth?
3. How is residual uncertainty/risk represented without fake precision?
4. When does investigation stopping become decision stopping?
5. How should abstention differ from defer or investigate/block?

### Evaluation

1. What is the practical oracle for candidate discovery quality?
2. How do we label ambiguous real cases without circular designer preference?
3. How do product-simulation cases, controlled variants, and held-out real cases divide roles?
4. What failure rate/coverage/cost evidence is enough to admit a broader method?

## 19. Product-simulation relationship

Product simulation is a principal challenge/evidence source for this horizon, not authority over it.

Use new simulation cases to ask whether the horizon:

- misses a materially different impact mechanism;
- incorrectly treats an exposure surface as a mechanism family;
- conflates evidence with exposure;
- requires an investigation that cannot change the owned conclusion;
- cannot represent contextual findings outside mechanism applicability;
- mishandles stale/superseded/retry/conflict behavior;
- assumes candidate-discovery completeness from a narrow family set;
- needs a new cross-candidate/synthesis responsibility.

Fresh examples should update this horizon when they change the whole-system understanding, not merely because a new case was added.

## 20. Horizon update policy

Update this file when one of these changes materially:

- a mature product responsibility is added, removed, split, or merged;
- broad candidate-discovery understanding changes;
- a provisional mechanism family is strongly supported, reclassified, or rejected;
- A/B/C/D responsibility boundaries change;
- new simulation evidence exposes a missing cross-cutting dimension;
- route evolution materially changes where a mature responsibility belongs;
- a previously open mature responsibility becomes accepted design;
- an experimental method is adopted and changes the mature architecture.

Do **not** update it for:

- every source commit;
- every passing test;
- one new fixture;
- live next-action changes;
- ordinary progress within a responsibility whose mature role did not change.

`MEMORY.md` remains the sole live-state owner.

## 21. Version 0.1 conclusions

At v0.1, the mature UpgradePilot horizon is strong enough to say:

1. **UpgradePilot is not a Python-support-drop analyzer.** That mechanism is the first implementation specimen inside a broader evidence-backed dependency-update decision system.
2. **The central mature reasoning spine is now visible:** candidate discovery → A candidate formulation → B applicability/coverage → C investigation/stopping → later D synthesis/action.
3. **A→C is substantially clearer than the responsibilities immediately before and after it.** Broad candidate discovery and cross-candidate/final synthesis are the largest design gaps.
4. **Mechanism families should be discovered and pressure-tested, not frozen from intuition.** Product-simulation evidence already shows runtime/API behavior, platform support, dependency/resolution, configuration/tooling, build/install, and contextual contrasts worth testing.
5. **Evidence condition, temporal state, coverage, target surface, dependency role, and repository context are orthogonal dimensions, not automatically impact families.**
6. **Candidate-discovery coverage must become a first-class mature concern.** Finding no applicable discovered candidate is not sufficient to prove no material impact.
7. **Mature stopping is question-specific.** More technical execution is not automatically better evidence if it cannot change the owned conclusion.
8. **Advanced technology is downstream of responsibility design.** Graphs, models, agents, learned ranking, and richer execution remain methods to evaluate—not definitions of the product.
9. **This horizon should evolve deliberately.** Its value is to keep the whole organism visible while individual implementation slices remain narrow and evidence-gated.

---

## Appendix A — Current concrete anchor inside the horizon

The first implemented specimen currently occupies this path:

```text
grounded authoritative upstream Python-support drop
        ↓
PythonSupportDropImpactCandidate
        ↓
exact target Python declaration / TargetPythonRelevanceResult
        ↓
explicit candidate-specific propositions
        ↓
declared-installation-range applicability path
        ↓
CandidateApplicabilityAssessment
        ↓
PublicPullRequestInvestigation.python_support_drop_impact_result
```

Current next conceptual expansion from that anchor is the first real C activation:

```text
candidate applicability unresolved
because exact target declaration evidence has not yet been acquired
        ↓
discriminating target = exact target Python declaration
        ↓
select admitted read-only exact-head acquisition
        ↓
observation
        ↓
reevaluate candidate applicability
```

This anchor validates part of the mature horizon. It does not define its final breadth.

## Appendix B — Historical ambition reconciliation note

The July 20 ambition proposal described three central future ideas:

```text
Upgrade Impact Graph
Decision-Time Machine
Targeted Check Planner
```

The mature horizon preserves the useful questions behind them but does not inherit those names as architecture commitments.

Post-reconciliation interpretation is closer to:

```text
"Upgrade Impact Graph" ambition
→ broad candidate discovery
+ target exposure/context relationships
+ mechanism-specific candidate representation
+ possible future graph method if justified

"Decision-Time Machine" ambition
→ exact identity/provenance
+ decision-time evidence
+ temporal supersession/replay
+ B3/B5 robustness

"Targeted Check Planner" ambition
→ Conversation C discriminating investigation selection
+ execution admissibility
+ stopping
+ later D maintainer recommendability
```

This is an example of the purpose of the horizon: preserve useful ambition while replacing premature solution labels with the product responsibilities now supported by stronger evidence.
