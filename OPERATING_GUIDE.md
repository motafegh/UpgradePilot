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

> **Active UpgradePilot source must actively orient its reader from the repository itself. A competent developer opening a non-trivial file should not have to reconstruct the execution route by searching the repository or remembering prior chat: the source should make clear where to start, what normally calls the file, what important data enters and in what shape, how that data moves through the main stages, what the file returns or emits, where that result goes next, why non-obvious mechanisms exist, and what stronger claims the file deliberately does not make. If those facts are only technically recoverable after repository archaeology, the source is not documented clearly enough.**

This contract applies whenever source code is created or materially modified. It complements `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`: **clear comments do not excuse vague names or unnecessarily obscure structure. Prefer expressive names and structure first; use documentation to preserve orientation, responsibility, data flow, relationships, invariants, reasoning, proof limits, and non-obvious mechanism.**

Apply the following rules proportionately.

- **`SOURCE-CLARITY-001 — Reader independence is the acceptance standard.`** Write for a competent Python developer who has opened the repository for the first time. Do not assume the reader remembers a previous conversation, implementation session, plan debate, or hidden rationale. When necessary context lives elsewhere, name the exact owning module/type/function/specification rather than leaving an unexplained implicit dependency.
- **`SOURCE-CLARITY-002 — Give non-trivial modules an explicit START-HERE map.`** Near the top of a non-trivial file, actively orient the reader rather than merely making facts recoverable somewhere in prose. Make the following visible when applicable: **what the module owns; what it deliberately does not own; the primary public entry point(s); the normal caller/upstream producer; important input types and representative shape; the main internal stage sequence; output/result types and important normal/problem states; and the next downstream consumer/handoff.** A preferred mental structure for substantial transformation modules is `RESPONSIBILITY → UPSTREAM/INPUT ORIGIN → PUBLIC API → INPUT SHAPES → INTERNAL PIPELINE → OUTPUT/PROBLEM STATES → DOWNSTREAM → PROOF BOUNDARY`. Exact headings are optional, but the information should be immediately recognizable without reading every helper first.
- **`SOURCE-CLARITY-003 — Make cross-file flow navigable in both directions.`** When a value, evidence object, state, or decision crosses module boundaries, identify the real handoff where it matters: **who creates or calls into this layer; which module owns the important input type; which public function receives it; its important type/shape; which internal stage transforms it; which module owns the output/result type; which function/type receives the result next; and what semantic authority changes or deliberately does not change.** Prefer exact source paths/types/functions when they materially reduce search cost. A reader should be able to answer both “where did this come from?” and “where does this go next?” from the owning explanations.
- **`SOURCE-CLARITY-004 — Explain project-specific library/import roles, not encyclopedia definitions.`** Minimal import-layer orientation is explicitly permitted and often useful when an imported library, container, type, or neighboring module plays a material role in this file. Prefer a short grouped comment such as “`tomllib` parses the exact lock evidence; `Counter` later compares repeated lock records without positional pairing” or “these dependency imports define the source-independent output contract.” Do not comment every ordinary import, define what a standard-library module generally is, or paraphrase syntax. The useful question is **why/how this dependency participates in this UpgradePilot file and which part of the flow needs it.**
- **`SOURCE-CLARITY-005 — Explain constants, domain literals, regexes, and structural devices as operational rules.`** For a materially non-obvious `frozenset`, regex, sentinel, threshold, lookup table, literal category, bounded traversal limit, type-narrowing construct, canonicalization step, or conservative branch, explain enough for a new maintainer to understand **what domain concept the values represent, where the device is used, what decision its result controls, and why that rule exists here.** If literals contain ecosystem/domain vocabulary such as `editable`, `virtual`, marker categories, or resolver states, briefly decode those terms at the first useful location and explain why those categories are included/excluded. If a regex defines an admission boundary, explain the accepted/rejected shape and what match/no-match means for the later flow; character-by-character regex narration is unnecessary unless the exact grammar itself is maintenance-critical.
- **`SOURCE-CLARITY-006 — Preserve the why at decision boundaries.`** Where code rejects, abstains, short-circuits, prefers one evidence source, deliberately refuses inference, or keeps two similar-looking states separate, document the ambiguity/failure/claim inflation that the branch prevents. These comments are often more valuable than comments on the happy path.
- **`SOURCE-CLARITY-007 — Educational depth is selective, high-value, and explicitly permitted.`** Longer comments or docstrings are appropriate—and may be preferable—when a compact explanation would hide a high-value concept, algorithm, invariant, evidence/proof distinction, cross-file relationship, or transferable engineering mechanism that a maintainer should understand rather than merely trust. Connect that depth directly to this implementation: **why we use it here, how it participates in the mechanism, what invariant or decision it protects, and what would break or become falsely claimed if it were misunderstood.** Comment length is earned by conceptual, maintenance, or learning value—not by how visually complicated a line happens to look. A difficult-looking regex or expression does not automatically deserve a long explanation, while a simple-looking branch may deserve one when it encodes an important semantic boundary. Do not make every section equally verbose and do not turn production files into generic beginner textbooks.
- **`SOURCE-CLARITY-008 — Use layered explanation instead of comment density.`** Put the **START-HERE architecture/data-flow map** at module scope; stable input/output/type contracts in callable/type docstrings; domain-term explanation at the first location where the term affects behavior; branch-specific reasoning beside the branch; and only highly local clarifications inline. Avoid repeating the same explanation at several levels. One strong owning explanation plus precise references is better than duplicated prose that can drift.
- **`SOURCE-CLARITY-009 — Keep data semantics visible through transformations.`** When raw evidence becomes normalized, typed, filtered, correlated, aggregated, or converted into another proof class, state what information is retained, discarded, strengthened, weakened, or deliberately not inferred. A reader following the data flow should not have to guess whether a transformation changes only representation or also changes semantic authority.
- **`SOURCE-CLARITY-010 — State proof and engineering limits.`** Explain what a result establishes, what it does not establish, which later layer owns the stronger conclusion, and why strictness or abstention exists where that distinction is material. This is especially important in UpgradePilot because similar-looking evidence states can support very different claims.
- **`SOURCE-CLARITY-011 — Comments and docstrings are maintained code.`** When behavior, ownership, naming, data flow, type shape, or proof meaning changes, update the nearby explanation in the same change. A stale architectural, data-flow, or proof comment is a defect. Delete comments that no longer add truthful information.
- **`SOURCE-CLARITY-012 — Touching code creates a bounded clarity obligation.`** When modifying older code, audit the responsibility you touched. If a nearby import, constant, sentinel, type, helper, branch, cross-file handoff, domain term, input/output contract, or proof boundary is materially ambiguous to a new developer, improve it in the same bounded change. Do not silently expand this into an unrelated repository-wide comment rewrite.
- **`SOURCE-CLARITY-013 — Important callable contracts make input, output, ownership, and handoff explicit.`** For a primary/public callable and for a non-trivial internal transformation, the docstring should make clear, proportionately: **what each important input means; where it normally comes from; which module/type owns it; its relevant shape or state variants; what transformation/question the callable owns; what it returns on success and on normal evidence problems; which module/type owns the returned contract; and which later function/layer normally consumes the result.** Formal `Args`/`Returns` sections are optional; explicit prose is sufficient. Trivial predicates/accessors do not need ceremonial contracts when the signature and one-line docstring already answer these questions.
- **`SOURCE-CLARITY-014 — Domain vocabulary that changes behavior must be locally decoded.`** Do not assume a competent Python developer also knows every uv, packaging, GitHub Actions, resolver, wheel-tag, marker, or project-specific term. When a domain term materially explains a branch, field, literal, or invariant, give its practical meaning at the first relevant source location and connect it to the decision being made. Keep the explanation local and implementation-specific rather than building a generic textbook glossary.
- **`SOURCE-CLARITY-015 — Show representative data shapes when type names alone are not enough.`** For important boundaries, include a small representative shape/example when it materially reduces ambiguity: for example a `ChangedFile` with the fields this module actually reads, a base/head repository-file pair, a simplified parsed record, or a success/problem result shape. The example must illustrate the real contract without becoming fixture-specific documentation or implying that only that literal case is supported.
- **`SOURCE-CLARITY-016 — Distinguish the primary semantic API from auxiliary public APIs.`** When a module exports several callables, identify which function is the main transformation developers should read first and distinguish admission predicates, acquisition gates, formatting helpers, compatibility shims, or other public support functions from that main semantic entry. A public symbol is not automatically an equal entry point. This distinction should be visible in the START-HERE map and, where useful, in nearby docstrings or section structure.
- **`SOURCE-CLARITY-017 — Give substantial modules visible structural grouping.`** When a file is large enough that scrolling obscures the execution model, group related functions/types into recognizable responsibility sections such as **public API, evidence/provenance validation, parsing, comparison, canonicalization, and utilities**. Use names, ordering, spacing, or lightweight section comments—whichever is simplest and clearest. Do not add decorative banners to small files or create section ceremony that says nothing about responsibility.
- **`SOURCE-CLARITY-018 — Explain meaningful type shapes and narrowing in project terms.`** When a union, `Literal`, optional value, alias, protocol, or narrowing step materially expresses an evidence state or invariant, explain **what real states the type represents, why those states are kept distinct here, and what a successful guard/narrowing step permits later code to assume.** Do not teach generic typing syntax. For example, explain that `RepositoryTextFile | UnavailableRepositoryFile` models acquisition success and typed acquisition failure as normal evidence states; do not merely define what a union is.
- **`SOURCE-CLARITY-019 — Treat guard clauses as evidence permissions when that is their semantic role.`** For an important early-return gate, explain not only why failure stops but also **what passing the gate authorizes the next stage to trust or assume.** Examples include: availability passing permits exact text handling; provenance validation permits bytes to support semantic parsing; schema validation permits fields to be interpreted with the admitted schema meaning. This makes the proof ladder visible in control flow instead of presenting guards as unrelated checks.
- **`SOURCE-CLARITY-020 — Explain non-obvious control flow and data structures only when they carry project semantics.`** Loops, comprehensions, tuple unpacking, set operations, `Counter`, `defaultdict`, sorting, and similar constructs do not deserve comments merely because they are Python mechanisms. Explain them when their use encodes a meaningful algorithm, invariant, evidence rule, or ambiguity-handling strategy—for example, using `Counter` as a multiset so repeated lock records are order-independent while duplicate counts remain significant. Prefer the semantic reason over syntax narration.
- **`SOURCE-CLARITY-021 — Disambiguate terminology collisions at the point of risk.`** When the same or similar word has materially different meanings across neighboring layers or ecosystem formats, identify the collision and state which meaning applies here. Examples include Git commit revision versus `uv.lock` internal revision, static workflow job versus runtime job, package source versus repository source, or package version versus lock schema version. Do this where confusion could change interpretation; do not create a glossary of harmless synonyms.
- **`SOURCE-CLARITY-022 — Mark current, transitional, and legacy APIs explicitly.`** When compatibility aliases, projections, old/new parallel paths, or migration-only APIs coexist, make the lifecycle visible: **which API is current for new code, which surface is retained for compatibility, what responsibility still depends on it, and what event/migration removes it when that is known.** Transitional code must not look equally canonical to a new reader. Do not delete compatibility surfaces merely to simplify comments; lifecycle changes remain separate behavioral/design decisions.

#### **Source-clarity completion check**

Before treating a material source change as complete, the implementer should be able to answer **yes** to the applicable questions without relying on chat history:

1. **If a new developer opens this file, can they immediately identify where to start and the primary semantic entry point?**
2. **If several public APIs exist, can they distinguish the primary transformation from auxiliary gates/helpers and any transitional/legacy surfaces?**
3. **Can they tell what normally calls this file and where the important inputs originate?**
4. **Can they see which modules own the important input/output types and, where useful, a representative data shape?**
5. **Can they follow the main internal data-flow stages without first reading every helper?**
6. **For a substantial file, does the physical/function grouping reinforce that flow instead of obscuring it?**
7. **Can they identify the output/result types, normal/problem states, and where the result goes next?**
8. **Can they state what this file owns and does not own?**
9. **Are material import/library roles explained where doing so reduces project-specific ambiguity without turning imports into a glossary?**
10. **Are non-obvious constants, domain literals, regex admission rules, sentinels, algorithms, precedence rules, and conservative branches explained in terms of their actual use and decision effect?**
11. **Are unfamiliar domain terms and material terminology collisions decoded where they affect interpretation?**
12. **Do names themselves carry as much meaning as reasonably possible before comments are required?**
13. **Do comments explain project-specific purpose, relationships, invariants, decisions, and proof limits rather than narrating syntax or giving generic library/language definitions?**
14. **For important functions, are input meaning/origin/ownership, output shape/states/ownership, transformation responsibility, and downstream handoff clear?**
15. **Where type annotations or narrowing express evidence states, can the reader tell what real states exist and what later assumptions a successful guard permits?**
16. **For important guard clauses, is both the stopping reason and the permission established by passing the gate clear?**
17. **When data is transformed, can the reader tell what semantic authority was retained, changed, or deliberately not inferred?**
18. **When a loop/container/control-flow mechanism is explained, does the explanation capture the project algorithm/invariant rather than Python syntax?**
19. **Where the logic has high learning value, is there enough implementation-specific explanation for a maintainer to learn the mechanism rather than merely trust it?**
20. **Is explanatory length justified by conceptual/maintenance/learning value rather than the surface complexity of the code?**
21. **Would changing the code later make it obvious which nearby explanation must also be updated?**

The target is not maximum comment volume or minimum comment volume. The target is **minimum ambiguity, fast file orientation, high information density, and proportionate explanatory depth**.

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