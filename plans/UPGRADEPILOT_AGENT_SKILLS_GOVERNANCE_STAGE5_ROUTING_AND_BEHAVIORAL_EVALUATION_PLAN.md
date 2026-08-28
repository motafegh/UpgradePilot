# UpgradePilot Agent Skills Governance Stage 5 — Routing and Behavioral Evaluation Plan

**Plan status:** Structurally complete; executable repository-wide doctor run deferred to final post-merge local validation  
**Authority:** Non-controlling execution coordination; root `AGENTS.md`, admitted Skills, normal responsibility owners, and current user authorization remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Strengthen UpgradePilot's governance-evaluation harness so Skill selection and conditional-reference loading are represented explicitly as behavioral contracts and their objective structure is validated deterministically, without pretending that deterministic checks can execute or semantically grade an AI agent.

This stage also defines a repeatable manual baseline-vs-Skill pressure-test protocol. It does **not** introduce a client-specific model runner, model-evaluation CI gate, new operation Skill, or product behavior change.

## Entry evidence

The Stage 5 audit established:

- `governance_doctor.py` already provides a strong Layer-A deterministic validator for required files, Skill frontmatter, admitted Skill references, all six existing case banks, internal links, stable IDs, audit lifecycle, state leaks, and size observations;
- the case banks already place procedural Skill/reference surfaces in `owners_expected` / `owners_not_expected`, but the doctor previously treated those values only as generic strings;
- Stage 2 and Stage 3 introduced conditional Skill references whose load/no-load behavior is behaviorally important, but the doctor did not validate reference-routing coverage or include Skill reference Markdown files in its internal-link surface;
- Learning-by-Doing vs Learning-Only routing is materially clearer after Stage 4, while cross-operation collisions still needed direct pressure cases for Audit vs Planning, diagnosis vs Audit/Build, combined Planning→Build, and tiny factual work below the full-Skill threshold;
- a true live agent runner is not currently feasible without selecting a specific AI client/API/runtime and defining how it exposes Skill loading, tool traces, and context behavior;
- introducing such a client now would create client-specific coupling before the evaluation rubric is stable.

## Evaluation-layer boundary

```text
Layer A — deterministic structure
→ governance_doctor.py
→ validates files, schema, declared routing-target existence, coverage, links, IDs, lifecycle

Layer B — Skill/reference routing behavior
→ behavioral cases declare expected/not-expected procedural surfaces
→ deterministic doctor validates the declarations only
→ human/client trial evaluates whether the agent actually selected them

Layer C — trajectory/behavior
→ must_do / must_not_do / action mode / evidence and claim discipline
→ manual or future live-agent evaluation
→ never claimed as doctor-executed behavior
```

## Implementation decision: reuse the existing case schema

The entry plan initially considered adding four optional fields:

```text
skills_expected
skills_not_expected
references_expected
references_not_expected
```

Implementation inspection showed that this would duplicate information already represented by exact procedural paths in:

```text
owners_expected
owners_not_expected
```

The smaller design was therefore admitted:

```text
exact .agents/skills/.../SKILL.md path
or exact .agents/skills/.../references/*.md path

inside owners_expected / owners_not_expected
→ machine-readable routing contract marker
```

This keeps one case schema and avoids parallel owner/routing fields that could drift.

The doctor recognizes only exact Skill/reference-shaped paths as routing markers. Other owner prose remains ordinary behavioral context.

## Allowed modification boundary

Stage 5 modified only:

- `tools/agent-governance/governance_doctor.py`;
- `tools/agent-governance/README.md`;
- `tools/agent-governance/consistency_cases.json`;
- this plan.

The initially allowed Build/Audit/base/Learning case-bank edits were not needed because their existing exact Skill/reference paths already supply the required positive/negative contracts.

No root governance, Skill procedure, `OPERATING_GUIDE.md`, specification, ADR, product source/test, learning package, memory, or client-specific metadata changed.

## Implemented sequence

### 1. Formalize missing collision cases

`consistency_cases.json` now contains discriminating cross-operation cases for:

1. **Audit vs Planning** — evaluative review selects Audit and does not select Planning merely because recommendations may follow.
2. **Diagnosis vs Audit/Build** — bounded read-only failure diagnosis uses the project debugging method without automatically selecting Audit or Build.
3. **Combined Planning→Build** — an explicit request to plan and then implement selects both procedures in sequence.
4. **Tiny factual clarification** — a narrow factual lookup selects no full operation Skill merely because Skills exist.

These cases use exact Skill paths where positive/negative selection is part of the contract.

### 2. Add deterministic routing-contract validation

`governance_doctor.py` now:

- discovers admitted operation Skill paths;
- discovers one-level Markdown files under each Skill's `references/` directory;
- recognizes exact Skill/reference paths in case `owners_expected` / `owners_not_expected`;
- rejects an exact routing target that does not correspond to an admitted Skill or discovered reference;
- rejects a case that puts the same owner/routing target on both expected and not-expected sides;
- requires every admitted operation Skill to have at least one positive and one negative routing case across the existing banks;
- requires every discovered conditional Skill reference to have at least one positive and one negative routing case;
- includes conditional Skill reference Markdown files in internal-link validation;
- reports the number of discovered conditional Skill references.

The doctor does **not** inspect prompt wording and decide which Skill should have been selected. It validates the declared contract only.

### 3. Reuse existing conditional-reference and learning cases

No edits were needed to these banks because previous stages already created exact-path contracts:

```text
Build Source-Clarity reference
→ positive: BUILD-004
→ negative: BUILD-011

Audit conditional-probes reference
→ positive: AUDIT-008 / AUDIT-009
→ negative: AUDIT-005

Learning-by-Doing
→ positive exact Skill route already exists in the base/operation cases

Learning-Only
→ positive exact Skill route already exists in the Learning-Only/base cases

negative operation-Skill coverage
→ CONSISTENCY-012 explicitly excludes all five for a below-materiality factual lookup
```

### 4. Document repeatable manual pressure testing

`tools/agent-governance/README.md` now distinguishes:

```text
Layer A — deterministic structure
Layer B — routing behavior
Layer C — trajectory/behavior
```

It also records a client-neutral trial record and baseline-vs-Skill method.

For a baseline trial, remove only the target procedural Skill from the isolated trial context. Keep root authorization/safety and semantic responsibility owners intact so the comparison tests the Skill's incremental value rather than a different governance system.

One manual trial is one observed trajectory, not a pass rate.

### 5. Defer a live client runner

A live agent runner is **not admitted** in Stage 5.

Reconsider only when:

- a concrete supported client/runtime is selected;
- Skill/reference loading is observable or can be instrumented without duplicating semantic authority;
- the manual routing/behavior rubric has been exercised enough to stabilize;
- repeated trial cost/reliability is acceptable.

Model-based evaluation remains outside mandatory CI until then.

## Proof performed

### Diff proof

The doctor implementation commit was inspected directly. Its diff is limited to:

- one routing-path recognizer;
- Skill-reference discovery and routing-target mapping;
- objective case-routing collection/coverage checks;
- Skill-reference link checking;
- one reference-count observation.

Existing lifecycle, normative-ID, state-leak, frontmatter, owner-map, and size-report logic remained intact.

### Predicate proof

The new routing predicates were executed against synthetic repositories.

Observed results:

```text
complete five-Skill + two-reference positive/negative coverage
→ no routing-contract errors

remove Learning-Only negative coverage
→ detected:
  admitted Skill lacks a negative routing case

add unknown exact Skill path
→ detected:
  references unknown Skill routing target

remove positive Audit conditional-reference coverage
→ detected:
  conditional Skill reference lacks a positive routing case
```

This proves the new deterministic predicates themselves discriminate the intended structural failures.

It does **not** prove the final repository tree passes every doctor check.

### Behavioral-contract proof

The current case architecture now represents:

```text
Audit vs Planning
Diagnosis vs Audit/Build
Planning + Build sequencing
Learning-by-Doing vs Learning-Only
tiny factual lookup vs full Skills
Build conditional-reference positive/negative
Audit conditional-reference positive/negative
```

### Boundary proof

No deterministic check attempts to infer semantic Skill selection from natural-language prompt text.

The doctor verifies:

```text
declared routing target exists
+ positive/negative regression coverage exists
```

Agent execution remains a Layer-B/Layer-C evaluation responsibility.

## Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

is deferred until the Skills/governance branch is finalized, merged, and pulled locally.

No executable repository-wide PASS is claimed before that run.

## Pass condition

Stage 5 is structurally complete because:

- Skill/reference routing expectations have a machine-readable representation without expanding the case schema;
- deterministic target/coverage validation is implemented without semantic overreach;
- the four missing cross-operation collision families are represented;
- all five operation Skills have a designed positive/negative coverage path across the current banks;
- both current conditional Skill references have designed positive/negative coverage paths;
- Skill reference Markdown is included in link validation;
- a repeatable client-neutral manual baseline-vs-Skill protocol is documented;
- live runner admission is deferred with concrete reconsideration criteria;
- the diff remains inside the bounded Stage 5 responsibility.

Final repository-wide executable acceptance remains contingent on the post-merge local doctor run.

## Stop line

Stage 5 stops here.

Do not begin inside this plan:

- root `AGENTS.md` / `OPERATING_GUIDE.md` pruning;
- retrieval-practice/storage-strength pedagogy additions;
- client-specific invocation metadata;
- live model-evaluation CI;
- another Skill admission.
