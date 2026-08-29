# UpgradePilot Current Memory

**Last updated:** 2026-08-29  
**Authority:** sole owner of the live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation and historical design are evidence to inspect, not authority to preserve unchanged.

```text
real responsibility / proof need / material risk / learning value
→ identify the earliest sufficient owner
→ keep or grow mechanisms that add real capability
→ refine redundant ownership/representation
→ avoid both over-engineering and under-engineering
```

Do **not** optimize UpgradePilot for minimum mechanism count. The target is a powerful, evidence-backed system with clear authority ownership. Complexity is welcome when it buys real product capability, better reasoning/investigation behavior, stronger observability/replay, meaningful failure handling, or valuable engineering learning. Complexity is unwanted when it is redundant, ceremonial, speculative, or does not change a real responsibility.

Canonical governance owners remain `AGENTS.md`, `OPERATING_GUIDE.md`, the controlling specifications, and the active operation/Learning-by-Doing skill.

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Mode:** Learning-by-Doing / Building is active. The earlier temporary Learning-Only pause is over.
- **Current engineering state:** evidence-first exploration E1–E5 and the delegated product-simulation capability research are complete and now integrated on `main`. No product `src/upgradepilot` planner integration has been authorized.
- **Current design record:** `working-memory/2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md`.
- **Current product-simulation response:** `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`.
- **Research integration:** branch `product-simulation/2026-08-28-main-support-lab` was fast-forward integrated into `main` through research head `0a5abdf60a0d21c3b626747afefc8286b0184c8d` before this memory reconciliation.
- **Selected continuation:** main must now make the explicit X1 disposition from the reconciled E1–E5 + product-simulation evidence. Do not continue simulation merely for more cases.
- **Current blocker:** no technical blocker. The remaining blocker is a product/design ownership decision: what honest planner responsibility, if any, should proceed toward a fresh v3 evaluation.
- **Do not:** fabricate a second planner action, freeze v3 before the candidate responsibility is selected, reuse the old v2 protected set as an uncontaminated final scorecard, or begin product planner integration merely because the first seam worked.

## Why the route changed

The earlier accepted strict X1 architecture/protocol remains valuable engineering work, but the project deliberately ran an evidence-first sequence before treating every prior safeguard/field as mandatory.

The governing distinction is now:

```text
FIRST-SEAM CONTROL CONTRACT
!=
FINAL PLANNER CAPABILITY CEILING
```

The first seam has been refined so trusted metadata remains deterministic and the LLM focuses on reasoning. This is **not** a directive to keep the eventual LLM responsibility trivial. The completed product-simulation research tested whether real richer planning responsibilities already justify expansion beyond the first seam.

## Evidence-first E1–E5 results

### E1 — existing support-drop semantic boundary

Evidence owner:

`working-memory/2026-08-28_B2-X1-E1-support-drop-semantic-probes.md`

Findings:

- a forced exact candidate containing a semantically negated support-drop sentence can still pass deterministic source/provenance grounding, proving that grounding does not independently prove English semantics;
- the adopted local model/prompt handled the selected live negation, future-drop, and instruction-shaped cases without false promotion in the executed slice;
- no additional product guard was justified from that small live slice alone.

### E2 — state origin / raw-text projection

Evidence owner:

`working-memory/2026-08-28_B2-X1-E2-s001-state-origin-and-projection.md`

Real S001 result:

```text
small proposition/action projection
→ raw external changelog text absent

nested PythonSupportDropImpactAssessment
→ raw tagged-changelog source_quote present

small projection
→ still carries model-influenced semantic state
```

Therefore raw-text carryover and semantic carryover are different channels. Direct planner prompt-injection exposure through the known upstream changelog route is a projection choice, not inevitable.

### E3 — minimally constrained real S001 planning

Evidence owner:

`working-memory/2026-08-28_B2-X1-E3-minimally-constrained-s001-planner.md`

With no closed action catalog, no JSON Schema, no deterministic admission, and no raw changelog prose, `gemma-4-e4b-it-ud` correctly identified the missing exact target Python declaration as the next useful evidence gap.

This established that the typed proposition representation can support the core S001 reasoning without the full strict guardrail stack creating that reasoning ability.

### E4 — incremental control comparison

Evidence owner:

`working-memory/2026-08-28_B2-X1-E4-incremental-constraint-comparison.md`

Controlled findings:

```text
E4.1
same frozen E3 state
+ one trusted action descriptor
→ exact action-id binding

E4.2
same E4.1 planner input
+ strict JSON Schema only
→ same correct decision in machine-readable form

E4.3
same E4.2 result
+ existing deterministic admission
→ current valid action admitted
→ invented action rejected as unknown_action
→ stale formerly-valid action rejected as target_proposition_not_actionable
```

Responsibilities now have direct evidence:

```text
typed proposition projection
→ reasoning context

closed trusted action catalog
→ capability binding

JSON Schema
→ machine-readable output shape / parsing reliability

deterministic admission
→ execution-time catalog/state/precondition revalidation
```

E4.3 also showed that the model need not redundantly echo trusted action metadata such as repository, revision, path, target proposition, or result families. Trusted code can rebind those after action lookup.

### E5 — no-tool semantics

Executed development controls:

```text
d-s004-stop      → stop       PASS
d-s006-defer     → defer      PASS
d-conflict       → unresolved PASS
```

All three meanings remained distinguishable with only a small structured no-tool result.

Therefore `stop`, `defer`, and `unresolved` remain useful loop semantics and should not be collapsed into one null-action state.

## Evidence-refined first-seam candidate

Current candidate control flow:

```text
TRUSTED STATE
bounded planning question
+ ordered typed propositions
+ attempt history
+ remaining budget
+ closed trusted action descriptors
        ↓
LLM PLANNER
        ↓
STRICT RESULT
state = choose_action | stop | defer | unresolved
action_id = trusted ID | null
explanation = non-empty text
        ↓
DETERMINISTIC PARSE
        ↓
IF choose_action
trusted action lookup/rebinding
→ repository/revision/path/target/result families/preconditions remain deterministic
→ fresh deterministic admission
→ exact bounded read-only capability or rejection
        ↓
IF no-tool
no capability execution
→ preserve explicit disposition + explanation as untrusted planner evidence
        ↓
DETERMINISTIC DOMAIN LOGIC
acquisition / interpretation / evidence promotion / proof strength / trusted state update
```

This is the current **control seam**, not the intended upper bound of future planner power.

## Design principles after reconciliation

Retain for the first seam:

- bounded trusted planning question;
- typed proposition projection;
- closed trusted action authority;
- pre-bound exact locators/identity internally;
- structured output;
- deterministic admission;
- explicit `stop | defer | unresolved` semantics;
- attempt history / remaining budget;
- oracle isolation and development/protected separation;
- selected local LM Studio/no-proxy checkpoint boundary.

Refine representation/ownership:

- model output should not echo trusted action-owned metadata merely so code can compare the echo;
- model-facing proof/limitation fields are not mandatory unless a richer future responsibility demonstrates value;
- keep human semantic review focused on decision-changing reasoning/proof errors rather than deterministic metadata already enforced structurally.

Remove from the **first seam only**, not forever:

- raw/near-raw upstream prose when typed projection already answers the planning need;
- a synthetic `untrusted_evidence_notes` channel created only to pressure prompt injection;
- planner-visible verbose hard-constraint tuples whose invariants are enforced structurally.

Defer until justified:

- richer action descriptor optimization;
- model retries/routing/frameworks;
- production integration;
- richer raw-evidence reasoning;
- broader multi-action/multi-turn machinery.

Important: `defer` here means “add when real capability/failure evidence earns it,” not “prefer a permanently small planner.”

## Evaluation protocol consequence

Historical protocol:

`plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

remains preserved and valuable, but it is **not an uncontaminated final scorecard for the reconciled candidate**.

Reason:

- S001 protected material was deliberately used during E3/E4 to learn about reasoning, action binding, schema shape, and admission;
- the candidate result contract materially changed from the old strict `AgentPlanResult` shape;
- v2's own contamination rules prohibit tuning from protected outcomes and then reusing the same protected set as final evidence.

Therefore a fresh v3 is required **only if** main selects an X1 candidate responsibility that should proceed to final planner-quality evaluation.

Do not edit v2 in place and pretend the protected boundary remained intact.

## Product-simulation capability research result

Execution plan:

`plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`

Main-facing response:

`working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`

Supporting records:

- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R0-evidence-use-map.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R1-inventory.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R2-planner-value.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R3-targeted-case-discovery.md`

Research conclusion:

```text
real missing / incomplete investigation capabilities found
→ YES

second capability justified as LLM-owned planner selection
→ NO

general adaptive-planner product value proven
→ NO

fresh v3 holdout safely reserved
→ NO
```

The strongest candidate was **exact-head resolver/currentness/satisfiability evidence**. It is a real product evidence opportunity with a known proof boundary, but current evidence still supports a compact deterministic selection policy better than an LLM-owned planner policy.

Other investigated responsibilities—mediated CI/environment consumption, target artifact/environment evidence, targeted behavioral differential execution, persisted-artifact provenance, repository-purpose context, and upstream multi-mechanism discovery—remain real or potentially valuable responsibilities, but none currently justifies being manufactured into a second planner action.

The research therefore recommends:

- retain the first seam as an experimental/control seam if main still values the X1 learning/pilot evidence;
- do not expand the action catalog merely to create multi-action agentic behavior;
- build/admit deterministic or semantic evidence capabilities when their own product responsibility is independently justified;
- reopen richer planner selection when two or more such capabilities naturally coexist and real cases show non-trivial prioritization/sequencing/state/history/budget trade-offs that a small deterministic policy handles poorly.

R4/R5 deep simulation/schema work was intentionally not activated because no candidate crossed the planner-value gate. This is an evidence-based stop, not missing work.

## Fresh-case / contamination boundary

Do not use as fresh v3 protected evidence:

- S001 action/replay material used in E2–E4 and v2;
- S004 and S006 no-tool material used directly in E5;
- S005/S007/S008/S011/S012 plus the synthetic unresolved/injection control frozen into v2's protected set.

All S001–S012 are historical/design-exposed product-simulation evidence and should not be casually represented as untouched holdouts.

S002, S003, S009, and S010 were not part of the v2 protected set and were not used for model-result-driven tuning in E1–E5, so they remain useful design research evidence, but they are still historically analyzed cases.

The latest targeted public-case discovery did not reserve a fresh v3 holdout. Future holdout discovery should occur only after main selects the exact candidate claim to evaluate, with exposure tracked from first screening.

## Environment facts relevant to continuation

- WSL remains the control plane.
- LM Studio is available locally at `127.0.0.1:12345` for the current checkpoint.
- Adopted/candidate model used in E1–E5: `gemma-4-e4b-it-ud`.
- Local LM Studio traffic uses a Requests session with ambient proxy inheritance disabled.
- Public GitHub acquisition can be disrupted by a stale ambient `GITHUB_TOKEN` or WSL proxy variables; confirmed direct public GitHub access succeeds without those contaminated environment values.
- During R3 targeted discovery, GitHub search also hit a secondary rate limit; this was treated as an acquisition barrier rather than case evidence.
- Reusable environment instructions are owned by `ENVIRONMENT.md`.

No cloud/paid fallback is part of the current X1 checkpoint.

## Current evidence/proof limits

E1–E5 plus the completed product-simulation capability research do **not** prove:

- production reliability;
- general planner superiority over deterministic orchestration;
- correct selection across several real actions;
- product adoption value;
- compatibility/safety/merge authority;
- that all future planner responsibilities should exclude raw evidence;
- that every strict mechanism omitted from the first seam is permanently unnecessary.

They **do** establish:

- the first seam can expose useful bounded LLM reasoning while deterministic code owns capability identity/admission;
- `stop | defer | unresolved` remain meaningful no-tool semantics;
- real product capability opportunities exist beyond A1;
- current evidence does not justify promoting a second capability into LLM-owned action selection merely to make the system more agentic;
- richer planner evaluation should reopen only when real capability composition creates a non-trivial policy problem.

## Selected next decision

Main now owns the next decision:

```text
E1–E5 evidence
+ completed product-simulation capability research
→ decide honest X1 responsibility/disposition
```

Current evidence supports two serious directions more strongly than general adaptive-planner adoption:

```text
A. RETAIN AS LIMITED PILOT / CONTROL SEAM
   preserve the first planner seam for bounded learning/evaluation value
   without claiming general adaptive-planner product superiority

B. DEFER RICHER X1
   preserve the evidence and resume richer planner work only when
   multiple independently justified capabilities create a real
   selection/sequencing problem
```

A deterministic resolver/currentness capability may be considered separately if the normal product route selects that evidence responsibility; doing so must not be presented as proof that an LLM planner should select it.

If main selects a candidate that should proceed to planner-quality evaluation:

```text
select exact candidate responsibility/action space
→ stabilize candidate design
→ find/reserve fresh claim-specific holdout material
→ freeze fresh v3
→ execute protected evaluation
→ explicit RETAIN AS PILOT / REJECT / DEFER disposition
```

General adaptive-planner `ADOPT` remains unjustified from the current evidence.

## Historical continuity

The previous long root memory, which contains the detailed R7 baseline, earlier Phase-0/1/2/3A state, audits, and the temporary Learning-Only continuation, is preserved exactly at:

`working-memory/2026-08-28_B2-X1-pre-evidence-first-root-memory-snapshot.md`

Use that snapshot and its referenced dated working memories for historical detail. Do not treat its old “Learning-Only active / LM Studio pending” continuation lines as current state.

Key current records:

- `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`
- `working-memory/2026-08-28_B2-X1-E1-support-drop-semantic-probes.md`
- `working-memory/2026-08-28_B2-X1-E2-s001-state-origin-and-projection.md`
- `working-memory/2026-08-28_B2-X1-E3-minimally-constrained-s001-planner.md`
- `working-memory/2026-08-28_B2-X1-E4-incremental-constraint-comparison.md`
- `working-memory/2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-handoff.md`
- `plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R0-evidence-use-map.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R1-inventory.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R2-planner-value.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-R3-targeted-case-discovery.md`
- `working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`

Historical plans remain available as prior design/evaluation evidence; current continuation is governed by this memory plus the current evidence-first reconciliation and completed product-simulation response.