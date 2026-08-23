---
name: upgradepilot-build-implement
description: Implement authorized UpgradePilot changes with bounded source/test preflight, responsibility and retention analysis, source/naming clarity, narrow-to-broad validation, Learning-by-Doing composition, and evidence-bounded handoff. Use when Ali explicitly asks to change, implement, build, fix, refactor, or update executable project behavior or closely related implementation artifacts.
---

# UpgradePilot Build and Implement

Use this Skill as the reusable procedure for **authorized implementation work** in UpgradePilot.

This Skill is **procedural and non-controlling**.

Root `AGENTS.md` owns authorization, operation routing, persistent safeguards, and artifact routing. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing, proportionality, rationale/necessity reasoning, debugging, evidence interpretation, and Source Clarity outcomes. Accepted specifications own stable behavior/invariants. Accepted ADRs own consequential durable method/structure. The selected plan owns bounded execution/proof/stop scope when a plan is justified. The Core specification owns `JUST-001` through `JUST-005`. The Naming Clarity specification owns naming/terminology quality. Active source/tests/commands/outputs establish implementation truth. `MEMORY.md` alone owns live continuation.

The Skill applies those owners; it does not redefine them.

## Activation and mutation boundary

Activate this Skill when Ali explicitly asks to:

```text
change / implement / build
fix / refactor / update
modify source or tests
apply an approved implementation plan
use build mode
```

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

## 8. Source Clarity: global outcomes + Build-time heuristics

A material source change must satisfy the seven Source Clarity outcomes in `OPERATING_GUIDE.md` §6.

The compact acceptance question is:

> **Can a competent developer understand the component's responsibility, important data flow, non-obvious reasoning, ownership boundaries, and proof limits from the repository itself without relying on prior chat?**

If not, improve structure, naming, comments, docstrings, or local orientation proportionately.

The following are **optional application heuristics**, preserved from the former detailed Source Clarity contract. Apply only those that materially reduce ambiguity; do not mechanically satisfy all of them for every file.

### 8.1 Reader orientation / START-HERE

For a substantial or non-trivial module, make the important reading route discoverable near the top when useful:

```text
RESPONSIBILITY
→ what it deliberately does not own
→ normal upstream/caller
→ primary semantic/public entry point
→ important inputs/shapes
→ main stages
→ output/problem states
→ downstream consumer
→ proof boundary
```

Exact headings are optional. Small files do not need an architecture essay.

### 8.2 Bidirectional cross-file flow

For important values/evidence crossing modules, make both directions recoverable where needed:

```text
where did this come from?
what owner/type gives it meaning?
where is it transformed?
where does it go next?
what semantic/proof authority changes—or does not change?
```

Use exact source paths/types/functions only when they materially reduce search cost.

### 8.3 Imports and neighboring modules

Explain an import/library/module role only when its **project-local participation** is non-obvious and material.

Good explanation: why/how the dependency participates in this mechanism.

Avoid encyclopedia definitions and comments on ordinary imports.

### 8.4 Constants, domain literals, regexes, sentinels, structural devices

Explain when material:

- what domain concept the values/device represent;
- where the device is used;
- what decision it controls;
- why that rule belongs here;
- accepted/rejected shape for an admission regex when that boundary matters.

Do not narrate syntax character by character unless the exact grammar is itself maintenance-critical.

### 8.5 Decision-boundary “why” comments

Comments are especially valuable where code:

- rejects or abstains;
- short-circuits;
- refuses an inference;
- prefers one evidence source;
- keeps similar-looking states separate;
- applies precedence or a conservative branch.

Explain the ambiguity, failure mode, claim inflation, or ownership error the branch prevents.

### 8.6 Layer explanation at its narrowest owner

Prefer:

```text
module scope → orientation/data-flow map
callable/type docstring → stable input/output/ownership contract
first relevant domain use → practical terminology meaning
branch → branch-specific reasoning
inline comment → truly local clarification
```

One strong owning explanation plus precise references is better than repeated prose that can drift.

### 8.7 Semantic/proof transformations

When evidence is parsed, normalized, filtered, correlated, aggregated, narrowed, or promoted, state proportionately what is:

```text
retained
removed
strengthened
weakened
deliberately not inferred
```

Do not let representation change look like increased semantic authority when it is not.

### 8.8 Callable contracts and representative shapes

For a primary/public callable or non-trivial transformation, make important inputs/outputs/ownership/handoff clear when the signature alone is insufficient.

A small representative shape/example is useful when it reduces ambiguity, but it must illustrate the contract rather than imply only that literal fixture is supported.

### 8.9 Primary API versus auxiliary APIs

When several public callables coexist, identify the main semantic entry point when ambiguity would otherwise make the file hard to read. Distinguish admission predicates, acquisition gates, formatting helpers, compatibility shims, and other support functions from the primary transformation.

### 8.10 Structural grouping

For a large module, use names/order/spacing/lightweight section comments to make responsibility groups navigable, for example:

```text
public API
validation/admission
parsing/transformation
comparison/canonicalization
utilities
```

Do not add decorative banners to small files.

### 8.11 Types and narrowing as domain states

When a union, `Literal`, optional value, alias, protocol, or guard materially expresses evidence states/invariants, explain what **real project states** it represents and what successful narrowing allows later code to assume.

Do not teach generic typing syntax inside production comments.

### 8.12 Guard clauses as permissions

When semantically accurate, explain both:

```text
why failure stops
+ what passing the guard authorizes the next stage to trust/assume
```

This is valuable when guards form an evidence/proof ladder rather than independent defensive checks.

### 8.13 Non-obvious algorithms and data structures

Do not comment loops, comprehensions, `Counter`, sorting, sets, etc. merely because they are Python mechanisms.

Explain them when their choice carries a project semantic, invariant, ambiguity-handling strategy, or proof consequence.

### 8.14 Terminology collisions

Disambiguate only at points where similar words have materially different meanings and confusion could change interpretation.

### 8.15 Current / transitional / legacy surfaces

When old/new paths, compatibility aliases, projections, migration-only APIs, or transitional code coexist, make visible:

- which surface is current for new code;
- what remains only for compatibility/migration;
- which real responsibility still depends on it;
- removal/migration trigger when known.

Do not delete compatibility only to simplify documentation; retention remains a separate `JUST-*` decision.

### 8.16 Bounded clarity obligation when touching old code

When modifying older code, improve nearby ambiguity that is materially part of the touched responsibility. Do **not** turn a bounded change into a repository-wide documentation campaign.

### 8.17 Maintenance

Comments/docstrings are maintained code. Update or delete them when behavior, ownership, type shape, naming, data flow, or proof meaning changes.

Stale explanations are defects.

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

Do not copy routine status across several controls.

## 15. Completion check

Before treating a material Build increment as complete, confirm proportionately:

```text
mutation was authorized
+ selected responsibility stayed bounded
+ active source/tests were inspected
+ accepted owners were respected or conflicts surfaced
+ smallest adequate implementation was chosen
+ JUST-* / end-to-end ownership applied when material
+ naming/source clarity is sufficient for a competent maintainer
+ focused proof exists when meaningful/available
+ broader proof matches actual risk/claim scope
+ actual change/result was inspected
+ proof limitations are explicit
+ continuity updated only where responsibility changed
```

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