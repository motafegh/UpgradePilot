# UpgradePilot Product Simulation Workspace

**Status:** Active complete-runtime and artifact-lifecycle discovery workspace  
**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Controlling local plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Parent authorization:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)

## Purpose

This workspace manually performs the complete intended UpgradePilot runtime on
real public dependency-update cases before more product implementation proceeds.

The simulation must discover both:

1. **complete product behavior** — what the system investigates, concludes,
   reports, and asks the maintainer to do; and
2. **complete artifact behavior** — what invocation, identity, operation,
   evidence, interpretation, finding, decision, report, follow-up, review, and
   replay records the future system must create and preserve.

A complete `CASE.md` is required but is not sufficient by itself.

## Local governance

Inside `product-simulation/`, the local rules control simulation execution,
method selection, artifact organization, progressive recording, and completion
when another UpgradePilot project-local rule conflicts.

The workspace is not restricted by the current implementation, milestone,
currently activated contracts, or previously admitted tools. Any lawful, safe,
accessible, and materially useful method may be used for simulation, including
scripts, local execution, containers, databases, models, agents, static or
dynamic analysis, and human review.

Simulation use does not select permanent architecture or establish automated
capability.

## Controlling files

- [`AGENTS.md`](AGENTS.md) — local instruction routing, method freedom, and
  completion behavior;
- [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md) —
  complete local execution and governance plan;
- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md) —
  required logical runtime-artifact family and validation rules;
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)
  — versioned restricted comparator used to test the project thesis;
- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) — adaptable
  structure for one complete narrative and artifact-producing run;
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) — cross-case coverage, stability,
  review, baseline, and artifact status.

## Required scenario organization

The default manual scenario bundle is:

```text
product-simulation/scenarios/<case-id>/
├── README.md
├── CASE.md
└── artifacts/
    ├── RUN_MANIFEST.json
    ├── INVOCATION.json
    ├── CASE_IDENTITY.json
    ├── OPERATION_EVENTS.jsonl
    ├── EVIDENCE_ITEMS.jsonl
    ├── CLAIMS_AND_INTERPRETATIONS.jsonl
    ├── FINDINGS.json
    ├── BASELINE_RESULT.json
    ├── DECISION.json
    ├── MACHINE_REPORT.json
    ├── FOLLOW_UP_STATE.json
    ├── REVIEW_AND_OWNERSHIP.json
    ├── HUMAN_REPORT.md
    ├── raw/
    └── checks/
```

`CASE.md` remains the complete human-auditable story. The `artifacts/` bundle
represents the simulated system state. Neither substitutes for the other.

The exact file split is provisional rather than a frozen product schema. A case
may add, split, merge, or rename artifacts when real evidence demonstrates a
better boundary, but every required logical responsibility must remain visible
and indexed by `RUN_MANIFEST.json`.

## Progressive execution

For new cases, create artifacts during the investigation:

```text
selected and frozen
→ materially investigated
→ decision and reports completed
→ reviewed or explicitly pending review
```

Natural repository checkpoints must demonstrate progression. One commit per
operation is unnecessary, but creating the whole apparent history only after the
final decision is prohibited.

Every material operation must preserve:

```text
question and state
→ method and reason
→ expected output and stop/switch condition
→ exact execution
→ raw output or explicit failure
→ direct observation
→ interpretation and alternatives
→ finding/decision/product outcome
→ next action and reason
```

## Raw evidence

Use bounded preservation:

- exact source identity, revision, run, tag, URL, and retrieval time;
- full raw payload when safe, lawful, reasonably sized, and materially needed;
- otherwise a bounded material capture, hash where useful, and durable reference;
- explicit inaccessible, expired, private, excessive, or unrecoverable state;
- no invented historical outputs.

## Baseline and thesis comparison

Every case must produce `BASELINE_RESULT.json` using the current version of the
transparent baseline.

The case must compare:

- baseline action and reasons;
- full-investigation action and reasons;
- changed uncertainty;
- changed targeted action;
- changed evidence authority;
- additional cost;
- whether the baseline was sufficient or materially weaker.

The full investigation is not assumed to win.

## Review and ownership

Keep separate:

- execution status;
- factual review status;
- Ali review status;
- external or behavioral confirmation status;
- AI assistance and Ali-owned capability.

A merged target PR is historical action, not ground truth. A completed
AI-produced case is not evidence of Ali's independent capability.

## Completed narrative investigations

| Scenario | Narrative result | Manual outcome | Artifact-bundle status |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | Unified retrospective record with correction and operation reconstruction | Merge after normal review | Retrofit in progress; unavailable historical outputs and timestamps must remain explicit |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | Rechecked complete case with API/adapter and CI-authority analysis | Run targeted checks; merge only after exact-head Python checks pass | Complete retrospective reconstruction; 39-file bundle validated; Ali review and external behavior confirmation pending |

S001 correctly records June 1, 2026 advisory publication dates and leaves the
exact Dependabot trigger unresolved. S002 now preserves its full reconstructed
runtime bundle, including the HTTP 410 log failure, missing historical dependency
resolution, superseded hypothesis, baseline result, conditional decision, and
follow-up transitions.

S002 is artifact-lifecycle complete as a retrospective reconstruction. It does
not claim that the artifacts existed during the original investigation or that
the historical environment and target behavior were recovered.

## Open-world rule

No list of actors, methods, artifacts, evidence states, stages, decisions, or
outputs is closed. Real cases may add, split, reorder, merge, or remove current
concepts.

Do not force evidence into the current structure. Change the local specification
when reality demonstrates that the current model is wrong.

## Current next action

Do not select S003 yet.

1. Complete the parallel S001 retrospective artifact bundle.
2. Validate S001 against the same syntax, identity, reference, provenance,
   baseline, report, follow-up, and review controls already passed by S002.
3. Compare both retrofits for defects in the artifact model.
4. Amend only the owning local rule when the two bundles expose a real defect.
5. Review both cases and assistance/ownership state with Ali.
6. Then select S003: an actual failing test workflow requiring failure
   attribution.

S003 must create its narrative and runtime artifacts progressively from the
first selected-and-frozen checkpoint.
