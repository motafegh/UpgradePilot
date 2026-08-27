# UpgradePilot Agent Skills Governance Stage 5 — Routing and Behavioral Evaluation Plan

**Plan status:** Authorized bounded execution plan  
**Authority:** Non-controlling execution coordination; root `AGENTS.md`, admitted Skills, normal responsibility owners, and current user authorization remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Strengthen UpgradePilot's governance-evaluation harness so Skill selection and conditional-reference loading are represented explicitly as behavioral contracts and their objective structure is validated deterministically, without pretending that deterministic checks can execute or semantically grade an AI agent.

This stage also defines a repeatable manual baseline-vs-Skill pressure-test protocol. It does **not** introduce a client-specific model runner, model-evaluation CI gate, new operation Skill, or product behavior change.

## Entry evidence

The Stage 5 audit established:

- `governance_doctor.py` already provides a strong Layer-A deterministic validator for required files, Skill frontmatter, admitted Skill references, all six existing case banks, internal links, stable IDs, audit lifecycle, state leaks, and size observations;
- the case banks already encode many Skill-routing expectations indirectly through `owners_expected` / `owners_not_expected`, but there is no explicit schema for **Skill selected / Skill not selected**;
- Stage 2 and Stage 3 introduced conditional Skill references whose load/no-load behavior is behaviorally important, but the doctor does not currently validate reference-routing contracts or include Skill reference Markdown files in its internal-link surface;
- Learning-by-Doing vs Learning-Only routing is now materially clearer, but the harness still needs cross-operation collision cases such as Audit vs Planning, diagnosis without accidental Audit/Build mutation, combined Planning→Build, and tiny factual work below the full-Skill threshold;
- a true live agent runner is not currently feasible without selecting a specific AI client/API/runtime and defining how it exposes Skill loading, tool traces, and context behavior;
- introducing such a client now would create client-specific coupling before the evaluation rubric is stable, contrary to the proposal's gradual-admission rule.

## Evaluation-layer boundary

```text
Layer A — deterministic structure
→ governance_doctor.py
→ validates files, schema, target existence, coverage, links, IDs, lifecycle

Layer B — Skill/reference routing behavior
→ behavioral cases with explicit expected/not-expected Skills and references
→ deterministic doctor validates the contract structure only
→ human/client trial evaluates whether the agent actually selected them

Layer C — trajectory/behavior
→ must_do / must_not_do / action mode / evidence and claim discipline
→ manual or future live-agent evaluation
→ never claimed as doctor-executed behavior
```

## Allowed modification boundary

This stage may modify only:

- `tools/agent-governance/governance_doctor.py`;
- `tools/agent-governance/README.md`;
- `tools/agent-governance/consistency_cases.json` for missing cross-operation routing collisions;
- `tools/agent-governance/build_cases.json` for explicit conditional-reference routing fields;
- `tools/agent-governance/audit_cases.json` for explicit conditional-reference routing fields;
- `tools/agent-governance/cases.json` and/or `tools/agent-governance/learning_only_cases.json` only where existing cases are the narrowest owner for explicit Learning-by-Doing / Learning-Only Skill-selection contracts;
- this plan to record structural completion.

No root governance, Skill procedure, `OPERATING_GUIDE.md`, specification, ADR, product source/test, learning package, memory, or client-specific metadata is in scope.

## Execution sequence

### 1. Add optional explicit routing fields to the case contract

Admit these optional behavioral-contract fields:

```text
skills_expected
skills_not_expected
references_expected
references_not_expected
```

They supplement rather than replace the existing fields.

Rules:

- values are lists of strings;
- Skill values use admitted Skill names, not prose aliases;
- reference values use repository-relative paths to real Skill reference Markdown files;
- the same Skill/reference may not appear on both expected and not-expected sides of one case;
- deterministic validation proves only that the contract is structurally coherent and points to real admitted surfaces.

### 2. Add deterministic routing-contract validation

Extend `governance_doctor.py` to:

- validate the optional field types;
- reject unknown/unadmitted Skill names;
- reject overlapping expected/not-expected Skill sets;
- validate that reference paths exist and remain under `.agents/skills/`;
- reject overlapping expected/not-expected reference sets;
- include Skill reference Markdown files in internal-link checking;
- require every admitted operation Skill to appear in at least one explicit positive routing contract and one explicit negative routing contract across the case banks;
- require every discovered conditional Skill reference to appear in at least one positive and one negative reference-routing contract.

Do not infer semantic routing from prose or regex-match prompts. Coverage is objective; whether the agent obeys the contract remains behavioral evaluation.

### 3. Formalize the missing collision cases

Use `consistency_cases.json` for cross-operation routing because these are system-level collisions, not one operation's internal procedure.

Add discriminating cases for:

1. **Audit vs Planning** — an evaluative review request should select Audit and not Planning merely because recommendations may follow.
2. **Diagnosis vs Audit/Build** — a bounded read-only failure diagnosis should use the project debugging method without automatically selecting Audit or Build when neither evaluation nor mutation is requested.
3. **Combined Planning→Build** — an explicit request to plan and then implement should select both procedures in sequence rather than letting Planning implement or Build skip material planning.
4. **Tiny factual clarification** — a narrow factual lookup should select no full operation Skill merely because the repository has Skills.

Do not create a separate routing case bank unless this existing cross-system bank proves insufficient.

### 4. Annotate existing learning and conditional-reference cases

Use existing discriminating cases rather than duplicating them:

- existing Learning-by-Doing composition case → explicit Learning-by-Doing positive / Learning-Only negative routing contract;
- existing admitted Learning-Only switch or no-dual-loading case → explicit Learning-Only positive / Learning-by-Doing negative routing contract;
- Build Source-Clarity positive and no-trigger cases → explicit reference expected/not expected;
- Audit Source-Clarity/governance-system positive and no-trigger cases → explicit reference expected/not expected.

### 5. Document a repeatable manual pressure-test protocol

Update the evaluation README with a client-neutral protocol that records, per trial:

- repository revision;
- case ID;
- client/model/configuration;
- trial type: baseline-without-target-Skill or current-with-Skill;
- selected primary operation;
- observed Skills/references loaded when observable;
- action mode;
- must-do / must-not-do outcomes;
- relevant tool/context/artifact behavior;
- evidence/claim violations;
- result and limitations.

For baseline-vs-Skill tests, remove only the target procedural Skill from the isolated trial context. Do **not** remove root authorization/safety/semantic owners, because that would test a different governance system rather than the Skill's incremental value.

Do not claim statistical performance from one manual trial.

### 6. Explicitly defer a live client runner

Record that a live runner is **not admitted in this stage** because the active environment does not provide one portable mechanism to invoke an agent with observable Skill-selection traces across supported clients.

Reconsider when:

- a concrete supported client/runtime is selected;
- Skill/reference load observability is available or can be instrumented without semantic duplication;
- the routing/behavior rubric has been exercised manually enough to stabilize;
- cost/reliability justify automation.

## Proof obligations

### Structural proof

Confirm:

- optional routing fields are accepted and validated;
- unknown Skill names and nonexistent/out-of-scope reference paths would fail the doctor;
- positive/negative coverage exists for all five admitted Skills;
- positive/negative coverage exists for every discovered conditional Skill reference;
- Skill reference Markdown files are included in link checking;
- existing case IDs remain unique across all banks.

### Behavioral-contract proof

Inspect cases and confirm the four missing collision families are represented and existing Learning/Build/Audit cases carry the intended explicit routing contracts.

### Boundary proof

Confirm no deterministic check attempts to decide whether a prompt semantically *should* route to a Skill. The doctor validates declared contracts, not LLM behavior.

### Diff/scope proof

Compare this plan commit with the final Stage 5 tip and confirm only allowed files changed.

### Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

is deferred until the Skills/governance branch is finalized, merged, and pulled locally. No executable PASS is claimed before that run.

## Pass condition

Stage 5 is structurally ready when:

- Skill/reference routing expectations are explicit in the case schema;
- deterministic target/coverage validation is implemented without semantic overreach;
- the missing cross-operation collision cases exist;
- Build/Audit conditional references have positive and negative routing contracts;
- Learning-by-Doing/Learning-Only have explicit positive/negative Skill-selection contracts;
- a repeatable client-neutral manual baseline-vs-Skill protocol is documented;
- a live runner remains deferred with a concrete reconsideration trigger;
- the diff remains inside the allowed boundary.

## Stop line

After routing/evaluation structure and manual protocol are complete, stop.

Do not begin:

- root `AGENTS.md` / `OPERATING_GUIDE.md` pruning;
- retrieval-practice/storage-strength pedagogy additions;
- client-specific invocation metadata;
- live model-evaluation CI;
- another Skill admission.
