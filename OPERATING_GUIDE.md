# UpgradePilot Operating Guide

**Status:** Controlling project-local operating guide  
**Owner:** Ali Rajabi  
**Responsibility:** Learning, execution, context discipline, proportionality, blocker handling, assistance fading, evidence interpretation, and handoff inside UpgradePilot

## 1. Boundary

Use this guide for **how** Ali and AI reason, learn, decide, implement, test, diagnose, preserve evidence, control context, and stop.

Root `AGENTS.md` owns repository-wide instruction order, request-to-action authorization, artifact routing, and standing safeguards. Use the responsibility owner named there for mission, live state, environment, security, plans, specifications, ADRs, implementation, experiments, tools, evidence, and history.

This guide is not a live-state owner. `MEMORY.md` alone owns selected continuation and current handoff.

Implementation truth must come from the evidence owner appropriate to the claim. Product, experiment/evaluation, and developer-tool proof classes remain distinct; documentation and accepted decisions do not by themselves prove implementation.

## 2. Core working loop

```text
real product responsibility
→ identify the smallest blocking concept or decision
→ build the minimum accurate mental model
→ Ali predicts, reasons, questions, or challenges
→ perform one bounded action
→ inspect actual evidence
→ separate observation, interpretation, and uncertainty
→ diagnose or revise
→ Ali modifies, tests, selects, or explains
→ preserve only material evidence and assistance
→ update MEMORY.md if live continuation changed
→ continue or stop
```

The unit of work is a real product responsibility, failure, evidence problem, or consequential decision—not a detached technology topic.

## 3. Context engineering

Treat working context as a finite attention budget. Use the **smallest sufficient context** for the selected responsibility.

Prefer this order:

```text
responsibility owner
→ relevant implementation/evidence
→ discriminating supporting material
```

Guidelines:

- load live state, environment, history, proposals, old working records, or unrelated specifications only when the question actually requires them;
- retrieve precise historical material for a precise provenance/comparison question rather than scanning all history;
- isolate a substantial tangent when it no longer blocks or materially informs the selected responsibility;
- preserve durable state in its normal repository owner rather than relying on conversation memory or repeated summaries;
- treat generated summaries as navigation aids, not replacements for inspectable source/evidence when that source remains available;
- when the client permits tool selection, expose/use only tools relevant to the task and add broader capability only when needed.

Context minimization must not hide a required owner, security boundary, proof obligation, or material counterevidence. The goal is high signal, not arbitrary brevity.

## 4. Universal Ceremony Tax Rule

> **Ceremony is a tax. Pay it only when it unlocks a tangible capability, controls a material risk, or satisfies a real external obligation that a simpler mechanism cannot adequately address.**

Ceremony includes mandatory process, approval, review, meeting, handoff, checklist, document, report, evidence record, abstraction, interface, framework, automation, infrastructure, dashboard, compatibility layer, control, or coordination beyond the direct product or learning action.

A tangible capability is observable and testable. Examples include:

- legal or regulatory compliance;
- security, privacy, access control, or destructive-action protection;
- auditability/provenance required for a real decision;
- reproducibility needed for another person or environment;
- failure detection, recovery, rollback, or diagnosis;
- compatibility support for an actual boundary;
- coordination required by demonstrated scale;
- protection of supported behavior through a justified test/CI gate;
- ownership evidence required for a material capability claim;
- user-visible behavior that cannot be delivered safely without the control.

Before adding or retaining consequential ceremony, identify through concise reasoning:

```text
Unlocked capability, controlled risk, or external obligation:
Evidence it is needed:
Simplest adequate mechanism:
Cost imposed:
Observable proof:
Removal or reassessment trigger:
```

Do not create a separate form merely to apply this rule.

Do not add ceremony when the justification is only professionalism, generic best practice, completeness, possible future scale, portfolio appearance, or proof that a process was followed. Necessary ceremony should remain proportional, preferably reversible, and removable when its reason disappears.

## 5. Session proportionality

Use the least ceremonial mode that protects safety, continuity, learning, ownership, and evidence.

### 5.1 Lightweight continuation

Use for a small reversible action inside an understood responsibility.

```text
Responsibility:
Observable result:
Action:
Proof:
Stop or continue condition:
```

Examples include one test change, one validation-error inspection, rerunning a known safe command, one bounded correction, or confirming one understood invariant.

No separate start/end record is required unless material evidence would otherwise be lost.

### 5.2 Standard learning or implementation session

Use for a new concept, responsibility, or meaningful increment.

```text
brief orientation
→ prerequisite check
→ minimum-complete explanation
→ Ali reasoning or prediction
→ bounded action
→ inspect evidence
→ correct the model
→ ownership-bearing change or check
→ concise evidence update
```

Name the responsibility, expected observable result, prerequisite depth, bounded action, proof, limitations, and stop condition. Store live continuation only in `MEMORY.md`.

### 5.3 Formal session

Use only for:

- milestone or major responsibility transitions;
- consequential architecture, data, evaluation, security, or adoption decisions;
- material blockers;
- formal capability assessment;
- destructive, credential-sensitive, paid, externally mutating, privacy-sensitive, or untrusted-code work;
- durable handoff where `MEMORY.md` and dated evidence are both necessary.

De-escalate after the consequential issue is resolved.

## 6. Technical operating modes

### Decision mode

Use when a consequential choice remains unresolved.

```text
responsibility and constraints
→ simplest credible baseline
→ credible alternatives
→ trade-offs and failure modes
→ discriminating evidence
→ Ali challenges, selects, or approves
→ ADR only when the accepted decision is durable and cross-cutting
```

Do not ask Ali to choose among unfamiliar names without first providing the mental model needed to evaluate them.

Before comparing methods:

- name the complete product responsibility that owns the proof slice;
- distinguish the tested category from the method's required operating domain;
- reject methods based on accumulating known phrases, exact grammars, fixture rules, or one handcrafted interpreter per category when the responsibility is broader;
- explain how each candidate extends, abstains, and creates a replacement cliff.

Incremental delivery may limit implementation now; it must not silently reduce the design horizon to the next fixture.

### Bounded exploration mode

Use when a question may materially affect the selected responsibility but it is unclear whether a decision is required. Set a question, information goal, scope ceiling, evidence sought, and return condition. Exploration must not silently become architecture or a new route.

### Execution mode

Use after the decision exists:

```text
one selected action
→ execute
→ inspect evidence
→ continue, repair, or reopen the decision only when evidence requires it
```

### **NON-NEGOTIABLE SOURCE CLARITY CONTRACT**

> **Active UpgradePilot source must explain itself from the repository. A competent developer should not need prior chat history, a working-memory archaeology session, or private project lore to understand what a file owns, how important data reaches it, what it produces, why non-obvious logic exists, and where the result goes next. If those facts remain materially ambiguous after reading the relevant source, the source is not documented clearly enough.**

This contract applies whenever source code is created or materially modified. It complements `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`: **clear comments do not excuse vague names or unnecessarily obscure structure. Prefer expressive names and structure first; use documentation to preserve responsibility, relationships, invariants, reasoning, proof limits, and non-obvious mechanism.**

Apply the following rules proportionately.

- **`SOURCE-CLARITY-001 — Reader independence is the acceptance standard.`** Write for a competent Python developer who has opened the repository for the first time. Do not assume the reader remembers a previous conversation, implementation session, plan debate, or hidden rationale. When necessary context lives elsewhere, name the exact owning module/type/function/specification rather than leaving an unexplained implicit dependency.
- **`SOURCE-CLARITY-002 — Orient the reader before local detail.`** A non-trivial module should make its responsibility, deliberate non-responsibilities, important inputs/outputs, and material upstream/downstream relationships recoverable near the top of the file. The reader should know what question the module answers before reading its helpers line by line.
- **`SOURCE-CLARITY-003 — Make cross-file flow navigable.`** When a value, evidence object, state, or decision crosses module boundaries, document the real handoff where it matters: who creates it, its important type/shape, which function consumes or transforms it next, and what semantic meaning changes or deliberately does not change. Prefer exact source paths/types/functions when they materially reduce search cost.
- **`SOURCE-CLARITY-004 — Document contracts, not merely syntax.`** For important functions/helpers/types, explain the practical contract: inputs, outputs, invariants, side effects, precedence, abstention/stopping behavior, expected problem states, and why this responsibility belongs in this layer. Do not spend comments paraphrasing obvious Python statements.
- **`SOURCE-CLARITY-005 — Explain non-obvious constants and structural devices.`** Non-obvious `frozenset` values, regexes, sentinels, thresholds, lookup tables, literals, bounded traversal limits, type-narrowing constructs, canonicalization steps, or conservative branches must state the domain concept they encode, why the shape/value matters, and what later behavior depends on it.
- **`SOURCE-CLARITY-006 — Preserve the why at decision boundaries.`** Where code rejects, abstains, short-circuits, prefers one evidence source, deliberately refuses inference, or keeps two similar-looking states separate, document the ambiguity/failure/claim inflation that the branch prevents. These comments are often more valuable than comments on the happy path.
- **`SOURCE-CLARITY-007 — Educational depth is selective but explicitly permitted.`** Longer comments or docstrings are appropriate when a compact explanation would hide a high-value concept, algorithm, invariant, Python mechanism, evidence/proof distinction, or cross-file relationship that a developer must understand to maintain the code safely. Such explanation should connect the concept directly to this implementation—**what it means here, why we use it here, and what would break or become falsely claimed if it were misunderstood.** Do not make every section equally verbose and do not turn production files into generic beginner textbooks.
- **`SOURCE-CLARITY-008 — Use layered explanation instead of comment density.`** Put module responsibility and architectural orientation at module scope; stable callable/type contracts in docstrings; branch-specific reasoning beside the branch; and only highly local clarifications inline. Avoid repeating the same explanation at several levels. One strong owning explanation plus precise references is better than duplicated prose that can drift.
- **`SOURCE-CLARITY-009 — Keep data semantics visible through transformations.`** When raw evidence becomes normalized, typed, filtered, correlated, aggregated, or converted into another proof class, state what information is retained, discarded, strengthened, weakened, or deliberately not inferred. A reader following the data flow should not have to guess whether a transformation changes only representation or also changes semantic authority.
- **`SOURCE-CLARITY-010 — State proof and engineering limits.`** Explain what a result establishes, what it does not establish, which later layer owns the stronger conclusion, and why strictness or abstention exists where that distinction is material. This is especially important in UpgradePilot because similar-looking evidence states can support very different claims.
- **`SOURCE-CLARITY-011 — Comments and docstrings are maintained code.`** When behavior, ownership, naming, data flow, type shape, or proof meaning changes, update the nearby explanation in the same change. A stale architectural, data-flow, or proof comment is a defect. Delete comments that no longer add truthful information.
- **`SOURCE-CLARITY-012 — Touching code creates a bounded clarity obligation.`** When modifying older code, audit the responsibility you touched. If a nearby import, constant, sentinel, type, helper, branch, cross-file handoff, or proof boundary is materially ambiguous to a new developer, improve it in the same bounded change. Do not silently expand this into an unrelated repository-wide comment rewrite.

#### **Source-clarity completion check**

Before treating a material source change as complete, the implementer should be able to answer **yes** to the applicable questions without relying on chat history:

1. **Can a new developer state what this file owns and does not own?**
2. **Can they identify the important inputs, outputs, and normal/problem states?**
3. **Can they follow material data/evidence across the next relevant file boundary without guessing?**
4. **Are non-obvious constants, sentinels, algorithms, precedence rules, and conservative branches explained where needed?**
5. **Do names themselves carry as much meaning as reasonably possible before comments are required?**
6. **Do comments explain purpose, relationships, invariants, decisions, and proof limits rather than narrating syntax?**
7. **Where the logic has high learning value, is there enough implementation-specific explanation for a maintainer to learn the mechanism rather than merely trust it?**
8. **Would changing the code later make it obvious which nearby explanation must also be updated?**

The target is not maximum comment volume. The target is **minimum ambiguity with proportionate explanatory depth**.

### Tangent mode

Use when a question does not block or materially affect selected work. Record only the relationship and a reconsideration trigger when useful, isolate substantial follow-up, then return.

## 7. Teaching and explanation

For an important new technical term, include when useful:

- full form and abbreviation;
- practical meaning;
- why the name makes sense;
- owning component/layer;
- inputs, outputs, state, and boundaries;
- relationship to the product flow;
- important failure modes/trade-offs;
- depth required now and depth deliberately deferred.

Simplification may narrow scope but must not falsify mechanism. Analogies must reconnect to the real system.

Teach one minimum-complete concept or responsibility at a time. Avoid monolithic lectures, blind guessing, and fragments too small to preserve relationships.

### 7.1 Post-run review

After a meaningful implementation, test, command, or failure, classify only relevant material:

- **Must master** — central concepts, paths, failure boundaries, source behavior, syntax, or tools Ali must explain, modify, test, and diagnose for the selected responsibility;
- **Understand operationally** — material Ali must recognize and safely use without internal reproduction;
- **Deferred deliberately** — real depth that does not unlock the selected responsibility;
- **Ali-owned practice** — a meaningful prediction, explanation, modification, test, or diagnosis that transfers control of a central boundary.

Do not teach every line equally. A successful run still requires explaining what was proved, important source behavior, limitations, and the next ownership-bearing action. A failed run should localize the failure, identify the revealed model gap, and select the smallest justified repair.

Update durable learning only for reusable understanding; update `MEMORY.md` only when live continuation changes.

## 8. Commands and tools

For a new or consequential operation, explain:

- command/tool purpose;
- important flags, paths, reads, writes, and side effects;
- credentials, network, cost, privacy, or destructive risk;
- expected output categories;
- what success would and would not prove.

For a familiar changed operation, explain only changed arguments/context/risk. For repeated safe operations, use a concise reminder unless misunderstanding or capability evidence requires more.

Repository `tools/` contains developer-operated diagnostics, live proofs, explicit validation runners, maintenance utilities, and governance diagnostics. Tool success does not become product behavior unless the corresponding responsibility exists under `src/upgradepilot/` and is protected by product tests.

Follow root `AGENTS.md` and `SECURITY.md` for authorization, credentials, untrusted code/data, and external actions. Never execute untrusted public repository code merely to inspect it.

## 9. Debugging

```text
symptom
→ affected boundary
→ strongest supported hypothesis
→ discriminating check
→ root cause
→ smallest repair
→ failing case
→ relevant unchanged case
→ nearest integration proof
```

Do not change multiple layers before localizing the likely failure. When a failure was not predicted, state that and identify the model gap it revealed.

## 10. Prerequisite repair

Classify encountered material as:

- **required core** — the selected responsibility directly depends on it;
- **supporting operational** — needed to work safely but not itself a target capability;
- **deferred core** — important later, but only an operational layer is needed now;
- **optional exploration** — not required for the dependency chain.

When blocked:

1. identify the exact missing link;
2. explain why it blocks selected work;
3. teach/practise the minimum complete mechanism;
4. verify through one meaningful action;
5. return explicitly to the original responsibility.

If prerequisite repair materially displaces the selected responsibility, reassess whether it has become a separate bounded responsibility or needs explicit rebounding. **Elapsed time alone does not create a new route, course, or plan.**

## 11. Assistance fading

Use demonstrated depth of the specific responsibility:

- **D0–D1:** AI may propose decomposition; Ali understands, predicts, questions, and challenges.
- **D2:** AI presents bounded alternatives; Ali selects and explains the action.
- **D3:** Ali proposes decomposition, tests, and diagnostic checks; AI reviews/corrects.
- **D4:** Ali controls the technical sequence and evidence plan; AI acts mainly as reviewer.
- **D5:** Ali operates independently across changed contexts and uses AI selectively.

Do not infer ownership from immediate repetition, typing AI-provided code, approving an AI-selected design, running a command, or passing AI-generated tests.

## 12. Evidence and ownership

Separate:

1. observed evidence;
2. execution/source context;
3. interpretation;
4. remaining uncertainty;
5. conclusion or next discriminating action.

Record assistance honestly as applicable:

- AI-generated;
- AI-assisted;
- Ali-directed;
- Ali-verified;
- Ali-owned at a stated narrow scope.

Use extended ownership assessment only for central milestone capabilities, disputed claims, D3+ assessments, or explicit Career review.

## 13. Completion and stopping

Stop when:

- selected proof and ownership requirements are sufficient;
- the next action would begin an unauthorized responsibility;
- evidence requires a decision/blocker escalation;
- concentration, comprehension, or diagnostic quality materially declines;
- safety, legality, privacy, credentials, or cost make continuation inappropriate.

Do not begin consequential work merely to fill remaining hours.

## 14. Updates and handoff

Root `AGENTS.md` owns repository-wide update routing. Update only the normal owner whose responsibility changed; do not propagate routine progress across several controls.

Preserve dated material execution/validation reasoning in `working-memory/` when it has future handoff value. Preserve reusable understanding in `learning/`. Keep live position and exact continuation in `MEMORY.md` only.
