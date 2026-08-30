---
name: upgradepilot-build-implement
description: Implement substantive authorized UpgradePilot changes with bounded source/test preflight, responsibility and retention analysis, source/naming clarity, narrow-to-broad validation, Learning-by-Doing composition, and evidence-bounded handoff. Use for substantive Build/Implement responsibilities or when Ali explicitly invokes Build mode. Tiny clear local changes inside an understood responsibility may use the compact root/Operating-Guide route and escalate if material complexity appears.
---

# UpgradePilot Build and Implement

Use this Skill as the reusable procedure for **substantive authorized implementation work** in UpgradePilot.

**Skill provenance marker:** `UP-SKILL:upgradepilot-build-implement`

This Skill is **procedural and non-controlling**.

Root `AGENTS.md` owns authorization, operation routing, persistent safeguards, and artifact routing. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing, proportionality, rationale/necessity reasoning, debugging, evidence interpretation, and Source Clarity outcomes. Accepted specifications own stable behavior/invariants. Accepted ADRs own consequential durable method/structure. The selected plan owns bounded execution/proof/stop scope when a plan is justified. The Core specification owns `JUST-001` through `JUST-005`. The Naming Clarity specification owns naming/terminology quality. Active source/tests/commands/outputs establish implementation truth. `MEMORY.md` alone owns live continuation.

The Skill applies those owners; it does not redefine them. For substantive Build, consult the relevant `OPERATING_GUIDE.md` sections when their owned method/evidence/source-clarity/handoff responsibilities are material rather than relying only on this Skill's summaries.

## Activation and mutation boundary

Activate this Skill when either condition holds:

1. the authorized implementation responsibility is **substantive**—for example it introduces or materially changes behavior, spans meaningful ownership/contract/proof concerns, requires non-trivial diagnosis, or otherwise benefits from the full Build procedure; or
2. Ali explicitly invokes Build mode or explicitly asks to apply the full Build procedure.

Typical substantive requests include:

```text
implement / build a bounded responsibility
fix a non-trivial behavior or failure
refactor a material mechanism
update source/tests where ownership, contract, or proof is material
apply an approved implementation plan
use build mode
```

A tiny standalone change may stay on the compact root + `OPERATING_GUIDE.md` route when it is clear, familiar, local, reversible, and already inside an understood responsibility with no material ownership/contract/risk/proof uncertainty. Do not load the full Build Skill merely because the request contains words such as `fix`, `change`, or `update`.

If a lightweight change reveals a new responsibility, cross-file ownership issue, invariant/contract change, non-trivial diagnosis, material risk, or broader proof obligation, **escalate** to this full Skill before continuing materially.

Once this Skill is active for a substantive responsibility, ordinary child edits, tests, commands, reruns, and Learning-by-Doing micro-steps inside that same responsibility **inherit the active Build procedure**. Do not conceptually re-route or reload the full Skill for every child action. Re-evaluate only when the responsibility, owner, material risk, proof obligation, environment/topology, security/trust boundary, or user-selected mode changes materially.

### Conditional context routes during Build

Use the routing strengths from `AGENTS.md` / `OPERATING_GUIDE.md`:

**REQUIRED FOR THIS SUBSTANTIVE PROCEDURE**

- this Skill once the substantive Build route is selected;
- active source/tests and the exact plan/specification/ADR owners required by the implementation responsibility;
- relevant `OPERATING_GUIDE.md` sections when its project-wide method, evidence, Source-Clarity, debugging, proportionality, or handoff responsibilities are material.

**CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS**

- `ENVIRONMENT.md` when local execution/runtime/topology/local-service/freshness becomes material, including when an execution/network failure appears after Build has already started;
- `SECURITY.md` when credentials, secrets/private data, untrusted external execution/mutation, or transport boundaries become material;
- the applicable stable specification/ADR when a new decision would rely on or change accepted semantics/method rather than merely implement an already-settled contract;
- [Source Clarity application heuristics](references/source-clarity-heuristics.md) when the §8 clarity-pressure trigger is present;
- `.agents/skills/upgradepilot-planning-design/SKILL.md` only when Build exposes a **new substantive unresolved design responsibility** that must be resolved before safe implementation.

**DO NOT LOAD REFLEXIVELY**

- `ENVIRONMENT.md`, `SECURITY.md`, detailed Source-Clarity heuristics, Planning/Design, unrelated specifications/ADRs, or historical records merely because they exist or might become relevant later.

A review, audit, explanation, diagnosis, planning, or design request does **not** authorize source/test mutation merely because an obvious implementation change is visible.

For authorized Build work:

```text
confirm bounded mutation responsibility
→ inspect applicable owners + active source/tests
→ form the smallest adequate change model
→ implement
→ inspect actual changed source/tests/diff
→ validate from narrow to broader proof as justified
→ state proof + limitations
→ update only owners whose responsibility actually changed
→ STOP at the selected boundary
```

Do not use Build mode to silently begin a new responsibility, speculative refactor, unrelated cleanup, dependency/framework adoption, destructive Git operation, or external-target mutation.

## 1. Establish the exact implementation responsibility

Before materially editing behavior, establish proportionately:

- the exact outcome/responsibility being changed;
- whether implementation is actually authorized;
- applicable specification invariants;
- applicable ADR/method constraints;
- selected plan boundary/proof/stop line when one exists;
- active source path and public/primary entry point;
- focused tests or nearest executable checks that protect the responsibility;
- expected result/proof boundary;
- prohibited/unrelated scope.

Do not require a written ceremony for a tiny understood edit. The purpose is to prevent scope and owner mistakes, not to produce a form.

If a specification, ADR, plan, or current implementation appears inconsistent inside another owner's responsibility, stop and reconcile/surface that conflict rather than silently choosing whichever artifact is easiest to follow.

Normal implementation design choices remain inside Build when accepted responsibility/semantics/architecture are already settled. Examples include a small helper boundary, local function signature, or test shape. If implementation instead reveals a material contract that must be decided, unresolved ownership/layer placement, consequential architecture/method alternatives, or a plan that no longer makes execution unambiguous, treat that as a **new substantive design responsibility**: compose/reconsider Planning/Design for that decision, then return to Build if mutation remains authorized. Do not load Planning/Design for every local implementation choice.

## 2. Inspect executable truth before changing it

For behavior-bearing work, inspect the **active executable constructs and relevant tests** before editing.

Use comments/docstrings as orientation, but do not infer source ownership solely from prose, AI summaries, old plans, or historical records.

Recover only the execution model needed for the selected change:

```text
normal caller / producer
→ important input/type/state
→ primary/public entry point
→ main transformation/control-flow stages
→ output/problem state
→ downstream consumer / proof boundary
```

Read more only when the responsibility or evidence requires it. Do not scan the repository reflexively.

## 3. Separate implementation fact, rationale, judgment, and authority

Apply `OPERATING_GUIDE.md` §4.3 for material mechanisms.

Keep distinct:

```text
CURRENT FACT
what source/tests actually do

RATIONALE / FAILURE MODE
what proposition, ambiguity, proof need, compatibility obligation, or material risk is demonstrably being addressed

ENGINEERING JUDGMENT
whether the mechanism is correct, necessary, proportionate, well placed, redundant, too weak, or too broad

AUTHORITY
which owner may change the accepted requirement/method/execution contract
```

Never invent an original or design rationale because the current code needs an explanation.

When the question is **why a mechanism is needed**, use proportionately:

```text
proposition / design goal
→ necessity class
→ correct owner/layer
→ supporting evidence
→ credible alternative/trade-off
```

Use the Operating Guide's necessity vocabulary as reasoning aids only. The Core `JUST-*` rules remain the normative retention owner.

## 4. Apply the implementation-retention burden

When touching a material existing or proposed mechanism, do not assume it earns retention because it already exists.

Apply Core `JUST-001` through `JUST-005`:

```text
admitted responsibility / proof / material risk / real compatibility need
→ exact proposition supplied by this mechanism
→ whether that proposition is already guaranteed more simply elsewhere
→ callers/tests as migration + regression pressure
→ smallest adequate owner/mechanism
→ KEEP / MOVE / NARROW / REMOVE
```

Current callers, tests, comments, historical design, prior effort, or direct internal callability do not independently prove architectural necessity.

This is not a deletion quota. Preserve the smallest mechanism whose independent reason survives review.

### Cross-layer fields/checks/metadata/validation

Before retaining or adding a material cross-layer mechanism, trace only as far as needed:

```text
exact proposition
→ producer
→ integration/orchestration/composition boundary
→ earliest sufficient owner
→ downstream consumer
→ independently supported later boundary, if any
→ concrete failure/proof loss/material risk without the repeat
→ KEEP / MOVE / NARROW / REMOVE
```

A downstream repeat needs its own reason. Manually fabricated inconsistent fixtures or arbitrary direct calls are not independent production contracts unless that route is explicitly supported and tested as such.

When independently produced evidence branches are combined, do not remove a repeated-looking value until you know whether the **relationship itself** is a real cross-branch coherence proposition.

## 5. Form the smallest adequate change

Prefer the smallest implementation that satisfies the admitted responsibility and proof need.

Before adding a new abstraction, compatibility layer, helper family, dependency, service, framework, package layer, validation layer, or durable metadata field, ask:

```text
what capability / proof / risk / compatibility obligation requires it?
→ can an existing owner satisfy that more simply?
→ what cost/complexity does the new mechanism add?
→ what evidence will show it is working?
```

Do not build around stale implementation structure merely to minimize local edits. Migration cost matters, but existing architecture is evidence rather than authority.

When automated logic could be overfit to known examples, use the Minimum Useful Generality specification rather than writing fixture-specific rules disguised as implementation progress.

## 6. Learning-by-Doing pre-change model when material

When Learning-by-Doing is active and the mutation is ownership-bearing—not a trivial repeated edit—establish a concise pre-change model before or around implementation:

```text
what is changing?
why is this the correct owner/layer?
what important behavior must remain unchanged?
what result do we expect?
what will the selected test/check prove and not prove?
```

Ali should have a fair opportunity to predict, explain, challenge, choose, modify, test, or diagnose only after the needed premises are established.

Do not turn every small edit into a quiz or require Ali to manually type implementation for ownership evidence.

## 7. Implement with responsibility-bearing structure and names

Prefer clarity in this order:

```text
responsibility placement
→ structure/control flow
→ precise types/interfaces
→ responsibility-bearing names
→ comments/docstrings where ambiguity remains
```

Use `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` as the naming owner.

In particular:

- prefer concrete action + object function names;
- name data types for the fact/evidence they contain;
- avoid generic `manager`, `processor`, `handler`, `interpreter`, `reconciler`, `context`, `canonical`, or `foundation` when a more concrete responsibility can be stated;
- use one primary term per concept where possible;
- prefer precise length over ambiguous brevity;
- when renaming, preserve or deliberately migrate affected imports/tests/diagnostics/docs/evidence as applicable;
- do not mass-rewrite historical records merely for vocabulary uniformity.

Comments must not compensate for vague ownership or unnecessarily obscure structure.

## 8. Source Clarity: core outcome + conditional application reference

A material source change must satisfy the seven Source Clarity outcomes in `OPERATING_GUIDE.md` §6.

The compact acceptance question is:

> **Can a competent developer understand the component's responsibility, important data flow, non-obvious reasoning, ownership boundaries, and proof limits from the repository itself without relying on prior chat?**

Prefer responsibility-bearing structure and naming before adding comments/docstrings. Improve stale nearby explanation when it is materially part of the touched responsibility, and maintain comments/docstrings when the behavior or ownership they describe changes.

For a small already-clear change, **DO NOT LOAD REFLEXIVELY** the deeper Source Clarity guidance merely because Build is active.

**CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS:** load [the Source Clarity application heuristics](references/source-clarity-heuristics.md) before finalizing a material source change when one or more of these clarity pressures are present:

- a substantial/non-trivial module needs reader orientation;
- important data or evidence crosses files and its upstream/downstream flow is not obvious;
- evidence is parsed, normalized, narrowed, correlated, promoted, or otherwise transformed in a way that can change semantic/proof interpretation;
- project-specific literals, regexes, guards, algorithms, sentinels, or decision boundaries need non-obvious reasoning explained;
- several public/auxiliary APIs, structural groups, or ownership layers make navigation ambiguous;
- types/narrowing encode meaningful domain or evidence states;
- current/transitional/legacy surfaces coexist;
- a material terminology collision or other documentation ambiguity could change maintenance decisions.

Apply only the heuristics relevant to the actual pressure. The reference is not a checklist, and the Naming Clarity specification remains the naming/terminology owner.

## 9. Tests are responsibility proof, not architecture authority

For a material code-bearing responsibility, connect the changed source to at least one meaningful focused test/check when one exists.

Understand the test as:

```text
setup / evidence state
→ action
→ assertion/result
→ behavior protected
→ stronger claims not established
```

If no meaningful focused test exists, say so rather than implying the responsibility is protected.

Tests/callers still do not prove that the mechanism they exercise belongs in the architecture.

When changing a contract, update tests to protect the admitted behavior rather than preserving obsolete implementation mechanics solely to keep old tests green.

## 10. Validate narrow first, then broaden by claim/risk

Start with the closest discriminating validation for the changed responsibility.

Broaden when justified by:

- the selected plan;
- a shared/cross-module boundary;
- unchanged consumers that narrow tests cannot protect;
- migration/compatibility pressure;
- the claim scope being broader than one unit;
- a failure indicating a wider affected boundary.

Typical progression:

```text
focused test / static check
→ nearest integration proof
→ broader regression suite required by the plan/risk
```

Do not run broad validation merely for ceremony when it cannot add relevant evidence.

If execution is unavailable, explicitly distinguish static/source review from runtime validation. Never convert “not execution-validated” into a PASS.

If local execution, runtime topology, service reachability, environment freshness, or an unexpected network/runner failure becomes material while validating, **CONDITIONAL — LOAD `ENVIRONMENT.md`** before concluding which validation surfaces are unavailable or classifying the immediate failure. If credential/proxy/private-data/external-action boundaries become material, load `SECURITY.md` as well. Do not infer environment truth solely from one tool/container failure when the repository already has a reusable environment owner.

## 11. Debugging during Build

For an unexpected failure, use the Operating Guide's discriminating chain:

```text
symptom
→ affected boundary
→ strongest supported hypothesis
→ discriminating check
→ root cause / model gap
→ smallest repair
→ failing case
→ relevant unchanged case
→ nearest integration proof
```

When safe/practical, form the hypothesis **before** immediately patching the failure.

Do not edit several layers randomly to make the suite green.

Never manufacture a failure, bug, or unnecessary mutation merely to create learning/ownership evidence.

If the failure contradicts the expected model, state the model gap it exposed.

When the failure introduces a new environment/topology, security/trust, accepted-semantics, or independent design question, treat that as a material routing checkpoint and load/reconsider the applicable conditional owner/procedure before continuing the repair.

## 12. Post-change inspection and Learning-by-Doing ownership

After meaningful AI-assisted implementation, inspect the **actual changed source/tests/diff/result** rather than assuming the intended patch is what was produced.

When Learning-by-Doing is active, compare it with the pre-change model:

```text
intended change
vs actual change

expected owner/layer
vs actual owner/layer

behavior expected to remain unchanged
vs evidence inspected

expected proof
vs result + non-proof
```

This is a learning/ownership mechanism and an implementation-quality check. It is not required as a formal written matrix for tiny familiar edits.

Do not infer learner ownership from AI-generated code, manual typing, agreement, running a command, or passing AI-generated tests alone.

If Ali explicitly says to stop building and learn the existing result, **stop product mutation** and transition to Learning-Only behavior.

## 13. Proof and claim discipline

After validation, separate:

```text
observed evidence
→ execution/source context
→ interpretation
→ remaining uncertainty
→ supported claim
```

Do not claim:

- runtime success from static inspection;
- specification compliance solely because documentation changed;
- universal correctness from one test/case;
- compatibility from one fixture;
- product regression from experiment-only checks;
- production readiness without corresponding evidence;
- learner ownership from implementation completion.

A passing test proves the behavior actually exercised and no stronger claim by default.

## 14. Update only the correct continuity/evidence owners

After Build work:

- source/tests own implemented truth;
- `working-memory/` gets dated execution/validation reasoning only when future handoff value justifies it;
- `learning/` gets reusable understanding only when appropriate;
- `MEMORY.md` changes only if live continuation materially changed;
- a plan changes only if its bounded sequence/proof/stop responsibility changed;
- a specification changes only if accepted stable semantics changed;
- an ADR changes only if the accepted durable method/structure changed;
- an audit changes only if its lifecycle/finding responsibility actually changed.

Do not copy routine status across several controls. Do not create or expand working-memory merely to record this Skill's provenance marker.

## 15. Completion check

Before treating a material Build increment as complete, confirm proportionately:

```text
mutation was authorized
+ selected responsibility stayed bounded
+ active source/tests were inspected
+ accepted owners were respected or conflicts surfaced
+ newly triggered conditional owners were consulted when material
+ smallest adequate implementation was chosen
+ JUST-* / end-to-end ownership applied when material
+ naming/source clarity is sufficient for a competent maintainer
+ focused proof exists when meaningful/available
+ broader proof matches actual risk/claim scope
+ actual change/result was inspected
+ proof limitations are explicit
+ continuity updated only where responsibility changed
```

When this full Skill was materially used, include `UP-SKILL:upgradepilot-build-implement` once in the normal completion/handoff provenance when practical. This records claimed Skill activation only; the actual Build trajectory and proof establish compliance.

## Stop line

Stop when the selected responsibility and required proof are complete, or when continuing would begin:

- a new responsibility;
- unrelated cleanup/refactor;
- speculative abstraction;
- dependency/framework/service adoption not already authorized;
- accepted-semantic or architecture change that needs its proper owner/decision;
- destructive/external/credential-sensitive work outside the authorized boundary;
- product mutation after Ali has switched to Learning-Only.

Do not broaden implementation merely because the adjacent change looks convenient.