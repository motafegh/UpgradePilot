# 01 — Purpose, Authority, and Non-Admission

**Depth target:** Operational understanding.  
**Primary question:** Why does `product-simulation/` exist, and what may it discover without silently becoming product architecture?

## 1. The problem being corrected

UpgradePilot had begun implementing bounded milestone slices before the complete product responsibility was concrete enough.

The failure pattern was:

```text
unclear whole-product responsibility
→ narrow implementation task
→ method selected around that local task
→ substantial code and testing
→ late discovery that the input, threat, responsibility, or control was wrong
```

M2-S02 was useful, but it revealed this deeper problem. A technically careful semantic-extraction experiment still could not answer foundational product questions such as:

- what begins a real run;
- what is supplied versus discovered;
- which evidence sources matter;
- how evidence authority is assigned;
- what happens when evidence is absent, stale, adversarial, contradictory, or irrelevant;
- how the complete investigation reaches a maintainer action;
- what state must persist after the report.

The correction is not to design the whole system speculatively. It is to perform the complete responsibility manually on real cases and observe what the product actually needs.

## 2. The practical purpose

`product-simulation/` answers two coupled questions:

1. **Product behavior:** What work must UpgradePilot perform to support a bounded maintainer decision?
2. **Artifact behavior:** What durable state must exist so that work can be audited, resumed, replayed, compared, rendered, reviewed, and corrected?

A complete narrative case can describe the first question, but it cannot by itself demonstrate the second.

## 3. Why this is a separate domain

The simulation has its own local authority because discovery would be weakened if it were forced to obey the current implementation boundary.

Inside the subtree, the local rules may permit:

- live public acquisition;
- source and dependency analysis;
- scripts and notebooks;
- local or container execution;
- models or agent workflows;
- temporary storage;
- human interpretation;
- methods associated with later milestones.

The purpose is to discover responsibilities and evidence needs, not to pretend those methods are already supported product behavior.

## 4. Authority order

The practical local order is:

1. external safety, law, privacy, credentials, permissions, and platform limits;
2. Ali's explicit current instruction;
3. `product-simulation/AGENTS.md`;
4. `SIMULATION_GOVERNANCE_AND_PLAN.md`;
5. the artifact and baseline specifications;
6. the active scenario and its evidence;
7. templates and coverage records;
8. other project-local documents.

This authority is scoped. It does not authorize target-repository mutation, unsafe execution, private evidence access, or changes to the stable project mission.

## 5. Four distinctions that must remain separate

### Discovery

A real case demonstrates that a responsibility, method, artifact, or distinction may be useful.

Example:

> Inspecting workflow path filters was materially useful in S002.

### Stable candidate

A pattern appears repeatedly and deserves further testing.

Example:

> Exact case identity freeze was necessary in both S001 and S002.

### Admission

The project explicitly accepts a consequential method, contract, or responsibility into controlling product design.

This requires evidence and an explicit owning artifact or architecture decision.

### Implementation

Source and tests establish executable behavior.

None of the first three states automatically implies the next.

```text
used in simulation
≠ generally useful
≠ stable product responsibility
≠ accepted architecture
≠ implemented capability
≠ reliable production behavior
```

## 6. Method freedom does not mean method indifference

A simulation method must still be justified.

For every material method, the case should preserve:

- the question being answered;
- why the method was selected now;
- credible alternatives;
- required environment and inputs;
- exact execution or source;
- output and side effects;
- what success establishes;
- what it does not establish;
- stop, switch, or escalation conditions;
- cost and adoption implications.

Method freedom removes premature milestone restrictions. It does not remove evidence discipline.

## 7. Example: connector-first inspection in S001

S001 used public source and GitHub inspection without local execution because the material questions could be answered from:

- exact pull-request revisions;
- lockfile dependency paths;
- target source and workflow definitions;
- tagged upstream metadata;
- advisory records;
- exact-head CI results.

This choice reduced unnecessary execution and supply-chain risk.

It does not establish:

- that connector-only analysis is always sufficient;
- that dynamic execution is unnecessary in other cases;
- that the target was safe;
- that a future product should use the same connector architecture.

## 8. Example: dynamic execution in S003

S003 may require an isolated reproduction if existing CI evidence cannot distinguish update-caused, pre-existing, flaky, environmental, or unrelated failure.

Using a container or local checkout would be evidence about the responsibility and comparison design. It would not automatically select containers as permanent architecture.

## 9. Common misconceptions

### “The simulation is just planning.”

Incorrect. It performs real evidence acquisition, investigation, decision construction, reporting, and artifact creation. It is manual execution, not only planning.

### “The simulation artifacts are future API schemas.”

Incorrect. Their logical responsibilities are being tested; exact fields and physical boundaries remain illustrative and non-binding.

### “A method used in three cases should be implemented.”

Not necessarily. Repetition strengthens the case for further evaluation, but admission also requires reliability, cost, security, maintainability, and boundary analysis.

### “Because M2-S03 is paused, the old implementation is rejected.”

Incorrect. It is retained as evidence and may later be corrected or resumed after simulation synthesis.

## 10. Read and inspect

Read these sections with this lesson open:

- `product-simulation/AGENTS.md` — scope, method freedom, external-action boundary;
- `SIMULATION_GOVERNANCE_AND_PLAN.md` — purpose, complete manual-system rule, method non-admission;
- `plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md` — the failure pattern and interruption rationale;
- `S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md` — product and implementation takeaways.

## 11. Prediction exercise

For each statement, classify it as discovery, stable candidate, admission, implementation, or proof:

1. S002 showed that workflow path filters can invalidate global interpretation of green CI.
2. The future production system stores workflow-analysis results in PostgreSQL.
3. A committed JSON schema is accepted as the public machine-report contract.
4. Source and tests implement deterministic machine-report rendering.
5. Two manual cases prove the renderer is reliable at production scale.

Expected reasoning:

1. discovery and repeated candidate with S001/S002 CI evidence;
2. unsupported architecture proposal;
3. admission only if explicitly approved by the owning specification;
4. implementation evidence;
5. unsupported proof claim.

## 12. Ownership checkpoint

Explain without quoting the documents:

1. What project failure caused the simulation interruption?
2. Why must product behavior and artifact behavior be discovered together?
3. Why can later-milestone methods be used now?
4. What prevents method freedom from becoming uncontrolled experimentation?
5. Give one example of a method that was useful but not admitted.
6. What evidence would be needed before that method became accepted architecture?

## 13. Current demonstrated depth

The repository demonstrates that Ali identified and required the simulation correction. Technical design, acquisition, artifact construction, and synthesis remain substantially AI-controlled. Reading and accepting this lesson does not change that ownership state.
