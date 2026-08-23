# UpgradePilot Operating Guide

**Status:** Controlling project-local operating guide  
**Owner:** Ali Rajabi  
**Responsibility:** Project-wide Learning-by-Doing method, context discipline, proportionality, implementation-retention reasoning, debugging, assistance fading, evidence interpretation, source-clarity outcomes, completion, and handoff

## 1. Boundary and relationship to operation Skills

Use this guide for **how** Ali and AI normally learn and work together inside UpgradePilot. Learning-by-Doing is the project's default philosophy for substantive work and may compose with Audit, Planning/Design, Build/Implement, debugging, testing, source review, and evidence review.

Root `AGENTS.md` owns repository-wide instruction order, request-to-action authorization, artifact routing, operation routing, and standing safeguards. The applicable responsibility owner remains authoritative for mission, live state, environment, security, plans, specifications, ADRs, implementation, experiments, tools, evidence, and history.

Agent Skills under `.agents/skills/` own reusable **procedures** for recurring operation families. They may specialize how this guide and other owners are applied; they do not replace this guide's project-wide Learning-by-Doing principles or redefine another owner's semantics.

This guide is not a live-state owner. `MEMORY.md` alone owns selected continuation and current handoff.

Implementation truth must come from the evidence owner appropriate to the claim. Product, experiment/evaluation, and developer-tool proof classes remain distinct; documentation and accepted decisions do not by themselves prove implementation.

## 2. Core Learning-by-Doing working loop

```text
real product responsibility / real question / real failure
→ identify the smallest blocking concept, decision, or evidence gap
→ build the minimum accurate mental model
→ Ali predicts, reasons, questions, challenges, or chooses
→ perform one bounded action appropriate to the primary operation
→ inspect actual evidence
→ separate observation, interpretation, uncertainty, and proof strength
→ diagnose, revise, or continue
→ Ali explains, modifies, tests, selects, or critiques at the appropriate depth
→ preserve only material evidence/learning/continuation
→ continue or stop
```

The unit of work is a real product responsibility, design decision, source mechanism, failure, or evidence problem—not a detached technology topic.

Learning-by-Doing does **not** require every operation to contain coding. It applies equally when the real work is planning, architecture/design, auditing, reading source, debugging, testing, interpreting evidence, or implementing.

If Ali explicitly requests Learning-Only, product mutation is paused and the applicable Learning-Only/package-local learning procedure takes precedence for the learning route while this guide still supplies the project-wide teaching/evidence principles.

## 3. Context engineering

Treat working context as a finite attention budget. Use the **smallest sufficient context** for the selected responsibility and operation.

Prefer:

```text
applicable operation procedure
→ exact responsibility owner
→ relevant implementation/evidence
→ discriminating supporting material
```

Guidelines:

- load live state, environment, history, proposals, old working records, or unrelated specifications only when the question actually requires them;
- retrieve precise historical material for a precise provenance/comparison question rather than scanning all history;
- use package-local learning contracts/plans/memory only when that learning package is actually active/material;
- isolate a substantial tangent when it no longer blocks or materially informs the selected responsibility;
- preserve durable state in its normal repository owner rather than relying on conversation memory or repeated summaries;
- treat generated summaries as navigation aids, not substitutes for inspectable source/evidence;
- expose/use only tools relevant to the task when the client permits tool selection.

Context minimization must not hide a required owner, authorization boundary, proof obligation, material counterevidence, or the operation procedure the user explicitly invoked. The goal is high signal, not arbitrary brevity.

## 4. Universal Ceremony Tax Rule

> **Ceremony is a tax. Pay it only when it unlocks a tangible capability, controls a material risk, or satisfies a real external obligation that a simpler mechanism cannot adequately address.**

Ceremony includes mandatory process, approval, review, checklist, document, report, evidence record, abstraction, interface, framework, automation, infrastructure, compatibility layer, control, or coordination beyond the direct product or learning action.

Before adding or retaining consequential ceremony, establish proportionately:

```text
capability / risk / obligation
→ evidence it is real
→ simplest adequate mechanism
→ cost imposed
→ observable proof
→ removal/reassessment trigger when material
```

Do not add ceremony merely for professionalism, generic best practice, completeness, possible future scale, portfolio appearance, or proof that a process was followed. Necessary ceremony should remain proportional and removable when its reason disappears.

### 4.1 Implementation retention burden

Apply the same proportionality discipline to existing implementation.

> **Existing code is evidence to inspect, not authority to preserve.**

A field, check, type, helper, abstraction, metadata value, alias, compatibility surface, dependency, caller, test, comment, historical design, or prior effort earns retention only by serving a current admitted responsibility, proof need, material risk, or real compatibility/external obligation.

When a material mechanism is under review, establish:

```text
admitted responsibility / proof / risk / compatibility need
→ exact fact or behavior supplied by the mechanism
→ whether that fact is already established more simply elsewhere
→ migration/regression pressure from callers/tests
→ smallest adequate retained mechanism
→ KEEP / MOVE / NARROW / REMOVE
```

Passing tests show what behavior is currently protected; they do not establish that the mechanism producing that behavior is necessary. Current consumers show migration impact; they do not independently prove that the consumed field or abstraction belongs in the product contract.

Avoid circular reasoning such as `X must stay because Y uses X` when Y's dependence on X is itself under review. Trace the need outward until it reaches an independently admitted responsibility, proof boundary, material risk, or real compatibility obligation.

This is a retention burden, not a deletion quota. Preserve a mechanism whose independent reason survives review, but prefer the smallest adequate mechanism.

The accepted normative owner is `JUST-001` through `JUST-005` in `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.

### 4.2 End-to-end responsibility trace before local retention

Do not decide material ownership from the local file alone. A real proposition may still be redundant at the layer where it is re-established.

For a cross-layer mechanism, trace only as far as needed:

```text
1. exact proposition / behavior supplied here
2. producer that first creates the relevant fact/object
3. integration/orchestration path that binds related inputs
4. earliest boundary already guaranteeing the proposition
5. downstream consumer repeating/carrying it
6. whether that consumer is an independently supported boundary
7. concrete failure, proof loss, or material risk remaining without the repeat
8. KEEP / MOVE / NARROW / REMOVE
```

Prefer the **earliest sufficient owner** unless a later layer has an independently admitted reason to distrust, recombine, or prove a distinct cross-object/domain proposition.

Direct internal callability and manually fabricated inconsistent fixtures are not enough to justify duplicate production validation. If an alternate invocation/composition route is intentionally supported, make that support explicit and test it as a contract; otherwise treat it as misuse/fixture pressure rather than architectural authority.

This trace is required for material cross-layer retention/addition decisions. It is not a request to scan the entire repository for every local edit.

## 5. Session and operation proportionality

Use the least ceremonial route that protects authorization, continuity, learning, ownership, and evidence.

### 5.1 Lightweight continuation

Use for a small reversible action inside an understood responsibility:

```text
responsibility
→ observable result
→ bounded action
→ proof
→ stop/continue condition
```

No separate plan/audit/working record is required unless material decision value or handoff evidence would otherwise be lost.

### 5.2 Standard substantive work

Use for a new concept, responsibility, design slice, meaningful implementation increment, or non-trivial review:

```text
brief orientation
→ prerequisite/owner check
→ minimum-complete explanation or design model
→ Ali reasoning/prediction/challenge
→ bounded primary operation
→ inspect evidence
→ correct the model
→ ownership-bearing explanation/change/check
→ concise evidence/handoff update when justified
```

### 5.3 Formal work

Escalate only for consequential architecture/data/evaluation/security/adoption decisions, major responsibility transitions, material blockers, destructive/credential-sensitive/external mutation, formal capability assessment, or durable multi-session handoff that cannot be represented safely by the lighter route.

De-escalate after the consequential issue is resolved.

### 5.4 Operation-specific procedures

The primary operation determines the detailed procedure:

- Audit/Review → repository-audit Skill and later refinements under `.agents/skills/`;
- Planning/Design → `plans/README.md` plus the admitted Planning/Design Skill when available;
- Build/Implement → applicable plan/specification/ADR/source/tests plus the admitted Build/Implement Skill when available;
- Learning-Only → applicable package-local learning contract/plan/memory plus the admitted Learning-Only Skill when available.

Learning-by-Doing normally overlays those procedures instead of competing with them.

## 6. Source Clarity acceptance outcomes

**Source clarity is part of implementation quality, not optional polish.** Materially created or changed source should let a competent developer recover the important execution model from the repository without needing prior chat history or hidden project lore.

Apply these outcomes proportionately together with the Naming Clarity specification:

1. **Responsibility and orientation** — a non-trivial file makes clear what it owns, what it does not own, where a reader should start, and which public/primary entry point matters most.
2. **Upstream → transformation → downstream flow** — important cross-file values/evidence make their origin, main transformation stages, result/problem states, and downstream handoff navigable in both directions.
3. **Input/output/type ownership** — important callables/types make the meaning, normal origin/shape, owning module, returned contract, and downstream consumer clear where signatures alone are insufficient.
4. **Non-obvious reasoning** — comments/docstrings explain project-specific invariants, domain literals, regex/admission boundaries, algorithms, guards, precedence, conservative branches, and important terminology collisions when misunderstanding them would change behavior or maintenance decisions. Explain semantic purpose, not syntax.
5. **Semantic/proof transformations** — when evidence is parsed, normalized, filtered, correlated, aggregated, narrowed, or promoted, make clear what information/authority is retained, discarded, strengthened, weakened, or deliberately not inferred.
6. **Selective educational depth** — longer implementation-specific explanation is explicitly permitted when a concept, algorithm, invariant, cross-file relationship, or proof boundary has high maintenance/learning value. Do not turn every file into a textbook or comment every ordinary mechanism.
7. **Truthfulness and maintenance** — comments/docstrings are maintained code. Transitional/legacy/current APIs must be distinguishable when they coexist, and explanations must change or disappear with the behavior/ownership they describe.

Prefer expressive naming and structure first, then layered explanation at the narrowest useful owner. One strong owning explanation plus precise references is better than repeated prose that can drift.

A material source change is incomplete when the repository still leaves important responsibility, flow, non-obvious reasoning, or proof limits ambiguous to a competent new maintainer.

Detailed Build-time and Audit-time application procedures belong in their operation Skills rather than expanding this section into a universal checklist.

## 7. Teaching, explanation, and ownership

For important new terms/concepts, include only the depth needed for the current responsibility, normally covering when useful:

- full form/abbreviation;
- practical meaning and why the name makes sense;
- owning component/layer;
- relevant inputs, outputs, state, and boundaries;
- relationship to the real product flow;
- important failure modes/trade-offs;
- depth required now versus deliberately deferred.

Simplification may narrow scope but must not falsify mechanism. Analogies must reconnect to the real system.

Teach one minimum-complete concept or responsibility at a time. Do not name-drop unfamiliar material and continue as though it were understood; do not turn every encountered technology into a standalone course.

After meaningful work, distinguish only what matters:

- **Must master** — central concepts/mechanisms Ali should explain, modify, test, and diagnose for the responsibility;
- **Understand operationally** — material Ali should recognize/use safely without reproducing internals;
- **Deferred deliberately** — real depth that does not unlock current work;
- **Ali-owned practice** — a meaningful prediction, explanation, modification, test, diagnosis, design choice, or critique that transfers control of a central boundary.

Do not infer learner ownership from typing AI-provided code, approving an AI-selected design, running a command, immediate repetition, or passing AI-generated tests.

## 8. Prerequisite repair

Classify encountered material as:

- **required core** — the selected responsibility directly depends on it;
- **supporting operational** — needed to work safely but not itself the target capability;
- **deferred core** — important later, but only an operational layer is needed now;
- **optional exploration** — not required for the dependency chain.

When blocked:

```text
exact missing link
→ why it blocks current work
→ minimum complete teaching/practice
→ one meaningful verification
→ explicit return to the original responsibility
```

If prerequisite repair materially displaces the selected responsibility, reassess whether it has become a separate bounded responsibility. Elapsed time alone does not create a new route, course, or plan.

## 9. Assistance fading

Use demonstrated depth of the **specific responsibility**, not a global impression:

- **D0–D1:** AI may propose decomposition; Ali understands, predicts, questions, and challenges.
- **D2:** AI presents bounded alternatives; Ali selects and explains the action.
- **D3:** Ali proposes decomposition, tests, and diagnostic checks; AI reviews/corrects.
- **D4:** Ali controls the technical sequence/evidence plan; AI acts mainly as reviewer.
- **D5:** Ali operates independently across changed contexts and uses AI selectively.

Fade assistance on repeated mechanisms. Restore explanation when a changed context exposes a genuine prerequisite/model gap rather than treating reduced assistance as a fixed entitlement.

## 10. Evidence interpretation and proof limits

Keep separate:

1. observed evidence;
2. source/execution context;
3. interpretation;
4. remaining uncertainty;
5. conclusion or next discriminating action.

For a meaningful result, state what it establishes and what stronger claim remains unjustified.

Record assistance honestly when relevant: AI-generated, AI-assisted, Ali-directed, Ali-verified, or Ali-owned at a stated narrow scope.

Specifications, ADRs, plans, docs, comments, and model agreement may define or explain intent; they do not substitute for implementation/proof evidence.

## 11. Debugging and failure learning

Use the smallest discriminating chain:

```text
symptom
→ affected boundary
→ strongest supported hypothesis
→ discriminating check
→ root cause/model gap
→ smallest repair
→ failing case
→ relevant unchanged case
→ nearest integration proof
```

Do not change multiple layers before localizing the likely failure. When a failure was not predicted, state that and identify the model gap it revealed.

A failed run is learning evidence only when we understand what failed, why the check discriminated, and what changed in the model. A passing run proves only the behavior actually exercised.

## 12. Commands, tools, and environment

For a new or consequential operation, explain proportionately:

- command/tool purpose;
- important arguments/paths;
- reads, writes, and side effects;
- credentials/network/cost/privacy/destructive risk when material;
- expected output categories;
- what success would and would not prove.

For repeated safe operations, use a concise reminder unless misunderstanding or capability evidence requires more.

`tools/` contains developer-operated diagnostics/live proofs/maintenance/governance diagnostics. Tool success does not become product behavior unless the corresponding product responsibility exists under `src/upgradepilot/` and is protected by product proof.

Use `ENVIRONMENT.md` for reusable local execution facts and `SECURITY.md` for the compact secrets/untrusted-evidence/credential/external-action boundaries when those risks are material.

## 13. Completion, stopping, and handoff

Stop when:

- selected proof and learning/ownership requirements are sufficient;
- the next action would begin an unauthorized responsibility;
- evidence requires a decision/blocker escalation;
- concentration/comprehension/diagnostic quality materially declines;
- safety, legality, privacy, credentials, or cost make continuation inappropriate.

Do not begin consequential work merely to fill time.

Update only the normal owner whose responsibility changed. Preserve dated material execution/validation reasoning in `working-memory/` when it has future handoff value. Preserve reusable understanding in `learning/`. Keep live position and exact continuation in `MEMORY.md` only.