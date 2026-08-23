# Group 5 — Build / Implement Mode Plan

**Artifact role:** detailed redesign plan for authorized source/test implementation work  
**Likely new procedural surface:** `.agents/skills/upgradepilot-build-implement/SKILL.md`  
**Related owners:** root `AGENTS.md`, `OPERATING_GUIDE.md`, selected plan/specification/ADR, Core `JUST-*`, Naming Clarity specification, source/tests/evidence

---

## 1. Objective

Create one reliable Build/Implement procedure for authorized product changes that:

- enters implementation only when the request permits mutation;
- inspects active source/tests before editing executable behavior;
- keeps changes bounded to the selected responsibility;
- applies source/naming clarity without checklist-driven comment inflation;
- challenges unnecessary existing/proposed mechanisms through `JUST-*`;
- validates from narrow to appropriate broader proof;
- preserves Learning-by-Doing during normal project work;
- updates only the correct continuity/evidence owners.

---

## 2. Baseline audit

Build-related rules are currently distributed across:

- root critical safeguards;
- `OPERATING_GUIDE.md` execution/debugging/source-clarity sections;
- Core `JUST-*` invariants;
- Naming Clarity specification;
- selected plans/ADRs/specifications;
- source/tests themselves.

This distribution is not inherently wrong, but there is no single reusable procedural entry point that tells an assistant how to combine them during implementation.

The Source Clarity Contract is particularly large in always-on context: 22 rules plus a 21-question completion checklist. Its intent is valuable, but a build assistant may respond mechanically by increasing comment volume rather than improving orientation and maintainability.

---

## 3. Canonical responsibility boundary

### Build Skill owns procedure

It should own:

- implementation preflight;
- exact responsibility/file/test boundary;
- source/test inspection sequence;
- change execution discipline;
- application of `JUST-*`, source clarity, naming clarity;
- validation sequence;
- change summary/proof/handoff.

### Specifications/ADRs/plans remain semantic/design/execution owners

The Skill references them. It does not restate them as independent rules.

### Source/tests remain implementation truth

The Skill cannot treat plan/spec/ADR prose as proof that a change was successfully implemented.

---

## 4. Target Build flow

```text
1. confirm mutation intent and bounded responsibility
2. load selected plan/spec/ADR only as needed
3. inspect active source/tests before changing behavior
4. trace relevant input → responsibility → output/data flow
5. identify existing mechanisms under retention pressure
6. choose smallest adequate implementation change
7. implement with expressive structure/naming/source clarity
8. add/update focused tests
9. run narrow discriminating validation
10. run broader required validation only when justified
11. inspect proof and limitations
12. update working-memory/MEMORY/plan owner only when their responsibility changed
13. stop at the selected responsibility boundary
```

---

## 5. Implementation preflight

Before materially editing source, establish proportionately:

- exact responsibility/outcome;
- allowed files/modules when bounded by plan;
- applicable specification invariants;
- applicable ADR/method decisions;
- current implementation path;
- existing tests protecting the behavior;
- expected proof;
- prohibited scope.

Do not require a ceremonial written preflight for tiny understood changes. The Skill must support proportionality.

---

## 6. Existing implementation and retention discipline

Apply Core `JUST-001` through `JUST-005` directly.

When touching a material mechanism, ask:

```text
what admitted responsibility/proof/risk/compatibility does this earn?
what does it actually supply?
is the same proposition already established elsewhere?
is this the earliest sufficient owner?
what would concretely fail or become unprovable if removed/narrowed?
```

Tests/callers are evidence of regression/migration impact; they are not automatic proof that the architecture should remain unchanged.

### Cross-layer mechanisms

For material fields/checks/metadata/transformations, use:

```text
producer
→ integration/composition
→ earliest sufficient guarantee
→ downstream consumer
→ independent later boundary, if any
```

Only duplicate validation/propagation when that later boundary has an independently admitted reason.

---

## 7. Source Clarity redesign for Build

### Universal outcomes stay compact in `OPERATING_GUIDE.md`

A material source change should leave a competent developer able to recover:

1. what the file/component owns and does not own;
2. where important inputs come from and what they mean;
3. the main transformation/control-flow responsibility;
4. what outputs/problem states leave the component and where they go;
5. why non-obvious invariants/branches/algorithms exist;
6. how transformations affect semantic/proof authority;
7. what the implementation does not prove or decide.

### Build Skill owns detailed application guidance

Use structure/names first, then comments/docstrings only where they reduce material ambiguity.

The Skill should retain useful concepts from the existing 22-rule contract as **application heuristics**, such as:

- START-HERE orientation for substantial modules;
- bidirectional cross-file data-flow navigation;
- input/output ownership and representative shapes where type names are insufficient;
- project-specific explanation of imports/domain literals/regexes only when material;
- decision-boundary “why” comments;
- semantic transformation/proof-limit explanations;
- explicit current/transitional/legacy API status when applicable;
- documentation maintenance in the same change.

Do not require every heuristic for every file.

### Completion question

Replace the 21-question checklist with a compact acceptance test:

> Can a competent developer understand the component's responsibility, important data flow, non-obvious reasoning, ownership boundaries, and proof limits from the repository itself without relying on prior chat?

If not, improve structure/naming/documentation proportionately.

---

## 8. Naming clarity

Continue to use `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` as the naming/terminology owner.

The Build Skill should apply it before adding comments to compensate for vague identifiers.

Rules:

- prefer responsibility-bearing names;
- avoid generic `manager`/`processor`/`handler` unless the domain responsibility truly warrants them;
- use one term per concept where possible;
- explicitly disambiguate terminology collisions that change interpretation;
- domain-specific examples are guidance, not excuses to hardcode known fixtures.

---

## 9. Testing and proof

### Narrow first

Start with the closest test/check that discriminates the changed responsibility.

### Broaden when justified

Broader suite/integration proof is required when:

- the selected plan requires it;
- the change crosses shared boundaries;
- the narrow proof cannot establish compatibility with unchanged consumers;
- the risk/claim scope is broader than one unit.

### Preserve proof classes

Do not claim:

- specification compliance solely because docs were updated;
- universal correctness from one case;
- compatibility from one passing fixture;
- learner ownership from AI-generated passing tests.

---

## 10. Learning-by-Doing composition

Normal Build work should remain educational without blocking execution.

The Skill should:

- orient the relevant source/data flow before material edits;
- explain high-value mechanisms and decisions, not every line;
- invite Ali to predict/diagnose/modify/test at a depth appropriate to prior exposure;
- explicitly explain what tests prove after meaningful runs;
- reduce assistance on repeated mechanisms;
- preserve technical independence if Ali challenges the design.

If Ali explicitly pauses building to learn existing code, transition to Learning-Only rather than continuing source mutation.

---

## 11. Debugging inside Build

Use the existing compact debugging discipline:

```text
symptom
→ boundary
→ strongest supported hypothesis
→ discriminating check
→ root cause
→ smallest repair
→ failing case
→ unchanged case
→ nearest integration proof
```

Do not edit multiple layers before localizing the likely failure unless evidence itself shows a cross-layer cause.

A material unexpected failure should identify the model gap it exposed.

---

## 12. Update/handoff routing

After implementation:

- source/tests contain implemented truth;
- dated execution/validation reasoning goes to `working-memory/` only when future handoff value justifies it;
- reusable understanding goes to `learning/` only when appropriate;
- `MEMORY.md` changes only if live continuation changed;
- plan/spec/ADR changes only if their owned responsibility actually changed;
- do not propagate routine status through several controls.

---

## 13. Expected modifications/creations

Likely files:

```text
.agents/skills/upgradepilot-build-implement/SKILL.md
AGENTS.md
OPERATING_GUIDE.md
tools/agent-governance/cases.json
possibly Naming Clarity specification only if audit finds ambiguous normative/example separation
```

The Core `JUST-*` specification should normally remain semantically unchanged; this group operationalizes it.

---

## 14. Behavioral regression cases

### BUILD — bounded implementation

Must inspect relevant source/tests and make focused changes.

### BUILD — unnecessary existing helper

Must not retain solely because tests/callers exist.

### BUILD — duplicate downstream validation

Must trace ownership before keeping/adding it.

### BUILD — source clarity

Must improve orientation/meaning without mechanically commenting ordinary syntax.

### BUILD — plan/spec/ADR mismatch

Must surface/reconcile owner conflict rather than silently choosing one.

### BUILD + Learning-by-Doing

Must teach material mechanisms without replacing actual implementation with lecture.

### BUILD — explicit learning pause

Must stop mutation and transition to Learning-Only.

---

## 15. Acceptance criteria

Group 5 passes when:

- Build Skill is the reliable implementation procedure;
- mutation requires appropriate user intent;
- active source/tests are inspected before behavior edits;
- `JUST-*` and producer/integration/consumer analysis are operationalized;
- Source Clarity becomes outcome-driven rather than checklist-volume-driven;
- Naming Clarity remains the naming owner;
- validation is proportional and proof claims are bounded;
- Learning-by-Doing composition is explicit;
- no product semantics were changed merely to simplify governance.

---

## 16. Stop line

Do not use Build mode to expand into a new responsibility, speculative refactor, dependency/framework adoption, or unrelated cleanup without the normal planning/authorization boundary.