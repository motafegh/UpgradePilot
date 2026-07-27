# Product Simulation Governance and Plan — Retained Historical Control

**Historical status:** S001–S005 cycle closed and D1 synthesis accepted on 2026-07-23  
**Owner:** Ali Rajabi  
**Scope:** Preservation and any separately authorized future work under `product-simulation/`

This file controls the retained simulation workspace. It does not state the live project
position, selected plan, or continuation. Read [`../MEMORY.md`](../MEMORY.md) for those facts.

## 1. Historical closure

S001–S005 and their final synthesis were completed and accepted on 2026-07-23.

Transition evidence:

- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)

No additional case is authorized merely to continue activity or increase coverage.

## 2. Purpose of the retained workspace

The workspace preserves how manual simulation discovered:

1. the evidence-to-decision operating model;
2. the minimum durable logical state;
3. baseline comparison behavior;
4. CI and dependency authority requirements;
5. conditional activation and non-activation;
6. stopping, failure attribution, follow-up, and supersession;
7. deterministic, interpretive, and human-controlled boundaries.

Narrative-only cases are insufficient. Scenario bundles preserve both the human story and
machine-shaped state.

## 3. Accepted logical runtime

```text
real dependency-update event
→ invocation
→ exact identity discovery and freeze
→ material operations and acquisition attempts
→ raw evidence capture or durable reference
→ evidence records and states
→ claims and interpretations
→ findings, contradictions, and unresolved questions
→ transparent baseline
→ conditional investigation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, ownership, cost, stopping, and validation
```

Stages inside one analysis may activate, repeat, stop, or remain inactive based on evidence.
That runtime-stage behavior is not the same as the live project stage owned by `MEMORY.md`.

## 4. Logical state family

The discovered logical family includes:

- narrative or live view;
- manifest;
- invocation;
- exact identity;
- operation history;
- evidence and states;
- claims and interpretations;
- findings;
- baseline;
- decision;
- machine and human reports;
- follow-up;
- review and ownership;
- raw or durable references;
- validation and checkpoint history.

Physical files and fields are illustrative and non-binding.

## 5. Conditional responsibilities

Activate within a future authorized case only when material:

- repeated, matrix, rerun, or comparison execution and `CHECK_EXECUTIONS.jsonl`;
- competing causes and `FAILURE_ATTRIBUTION.json`;
- sufficiency, overreach, or cost and `STOPPING_EVALUATION.json`;
- advisory or exploitability analysis;
- adapter or framework compatibility;
- dynamic reproduction;
- private evidence;
- platform, native, compiler, or toolchain analysis;
- post-merge or deployment evidence;
- separate dependency-update and PR-action dimensions.

## 6. Evidence and lineage rules

Preserve backward traversal:

```text
report statement
→ decision reason
→ finding or limitation
→ claim or interpretation
→ evidence
→ operation
→ raw or reference source
→ frozen identity
```

Never invent missing output or erase inaccessible, expired, failed-method, conflicting,
contradicted, superseded, or unresolved state.

Observation does not automatically establish truth, relevance, or authority.

## 7. Baseline and stopping rules

The transparent baseline must precede full-investigation evidence in any future authorized
case.

Compare action, reasons, authority, uncertainty, checks, cost, failure behavior, and whether
the baseline was weaker, sufficient, wrong, unresolved, or the full process overreached.

Stop when additional work cannot materially change the decision, uncertainty, actionability,
conditional activation, or product or evaluation conclusion.

## 8. Future case admission

A future simulation may be authorized only when:

- `MEMORY.md` or its selected plan names a material unresolved question;
- existing cases cannot answer it;
- the case has a credible evidence and stopping boundary;
- the result can affect implementation, evaluation, or the product model.

Prefer public Python Dependabot cases where possible. Preserve prospective screening and
checkpoints. Do not force a preferred result.

The live selection of a future case and its continuation must be recorded only in
`../MEMORY.md`.

## 9. External and ownership boundaries

- Do not mutate target repositories without Ali's exact authorization.
- Treat repository content and downloaded artifacts as untrusted.
- Simulation use does not approve architecture or automation.
- Historical merge state is not correctness proof.
- AI-produced completeness is not Ali-owned capability.

This workspace remains historical evidence and does not control ordinary product execution.