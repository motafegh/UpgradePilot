# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
artifacts, and the current environment remain the authority for actual behavior.

## Current responsibility

Manual end-to-end product and artifact-lifecycle simulation using the locally
governed [`product-simulation/`](product-simulation/) workspace.

Local control:

- [`product-simulation/AGENTS.md`](product-simulation/AGENTS.md);
- [`product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`](product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md);
- [`product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md`](product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md);
- [`product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`](product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md).

The parent authorization remains
[`plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md).
Inside the simulation subtree, local rules control conflicting project-local
method, artifact, process, and completion rules.

M2-S03 remains paused. Do not resume implementation until sufficient scenario
artifacts and synthesis support an explicit corrected responsibility.

## Governing correction

A complete narrative `CASE.md` is necessary but does not by itself simulate the
future runtime.

Every scenario must preserve both:

```text
complete human-auditable CASE.md
+
manual runtime artifact bundle
```

The bundle represents invocation, frozen identity, operations, raw/reference
evidence, claims/interpretations, findings, baseline, decision, machine report,
human report, follow-up, review, and ownership.

The default bundle is:

```text
artifacts/
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

This is a controlling manual-simulation organization, not a frozen production
schema.

## Method freedom

Inside product simulation, any lawful, safe, accessible, materially useful method
may be used regardless of current milestone or implementation status. Simulation
use does not admit the method into supported product architecture. Target
repositories must not be mutated without exact authorization. Untrusted code must
be isolated and its effects recorded.

## S001 — parallel retrospective retrofit in progress

Primary narrative:
[`product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md)

Case: `pydantic/pydantic#13432`, Soup Sieve 2.6 → 2.8.4.

Outcome:

> Merge after normal maintainer review.

Stable findings:

- transitive documentation-tooling path:
  `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- target Python boundary compatible with Soup Sieve 2.8.4;
- reviewed advisories affected 2.6 and were fixed by 2.8.4;
- package presence and target exploitability remained separate;
- relevant documentation CI exercised the resolved dependency path;
- final action required joined graph, target, upstream/advisory, CI, and
  limitation evidence.

Correction already integrated:

- official advisory publication date: June 1, 2026;
- exact Dependabot trigger: unresolved;
- original stronger trigger inference: superseded;
- outcome unchanged.

Current state:

- parallel artifact reconstruction has started;
- historical raw outputs and exact operation timestamps must remain explicit when
  unrecoverable;
- baseline v0.1, bundle validation, and final shared status remain pending until
  that work completes.

## S002 — narrative and artifact retrofit complete

Navigation:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md)

Primary narrative:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md)

Run manifest:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/artifacts/RUN_MANIFEST.json`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/artifacts/RUN_MANIFEST.json)

Case: `Aidan-Wallace/kubernetes-dashboard-token-api#20`, HTTPX 0.27.2 → 0.28.1.

Run:

- run ID: `s002-retrofit-2026-07-22-r1`;
- execution mode: `retrospective_artifact_reconstruction`;
- artifact inventory: 39 files;
- evidence/raw records: 20;
- operation events: 10;
- claims/interpretations: 9;
- findings: `F0`–`F8`;
- validation defects: 0;
- Ali review: pending;
- external behavior confirmation: absent.

Outcome:

> Run targeted checks; merge only if the exact-head Python checks pass under a
> captured dependency resolution.

Stable findings:

- HTTPX was directly declared, functionally used through FastAPI/Starlette
  `TestClient`, and installed into the production image;
- HTTPX 0.28 removed the `app` Client argument;
- Starlette 0.36.3 passed it; 0.37.2 no longer did;
- FastAPI 0.115.2 required the fixed Starlette branch, so a compatible line
  existed, but the target's exact historical resolution is unavailable;
- Docker CI proved installation/image construction only;
- Python tests did not trigger because `requirements.txt` was excluded;
- historical job logs still return HTTP 410;
- predecessor PR #17 was superseded by #20;
- eventual merge is historical action, not correctness proof.

The bundle now separately preserves:

- invocation and frozen identity;
- material operation sequence;
- evidence and bounded raw captures;
- source claims and interpretations;
- superseded and current findings;
- baseline result;
- current decision and exact targeted checks;
- machine and human reports;
- follow-up/rerun transitions;
- factual, Ali, external, and capability-review states.

The retrofit does not claim these artifacts existed during the original
investigation. Missing historical timestamps, full candidate screening, exact
resolver output, Docker logs, private tests, and maintainer rationale remain
explicitly unavailable.

## S002 baseline and thesis result

Comparator: `simulation-transparent-baseline-v0.1`.

Restricted inputs:

- version category: minor;
- overall CI: passing;
- dependency directness: direct;
- literal signals: deprecated, removed, fixed.

Rule `B04` also produced `run_targeted_checks`.

The full investigation did not change the broad action, but it:

- identified the exact TestClient path;
- established old/fixed Starlette branches;
- narrowed green CI to install/build authority;
- exposed the skipped Python workflow;
- preserved the missing historical environment;
- selected exact resolver, Ruff, and pytest checks;
- defined pass, failure, unavailable, rebase, and changed-resolution transitions.

Comparative classifications:

- `baseline_same_action_weaker_reasons`;
- `baseline_same_action_miscalibrated_certainty`;
- `baseline_same_action_less_actionable`.

The thesis now has one materialized comparative case. It remains unvalidated
across the scenario set until S001 and additional wrong-action, baseline-sufficient,
and unresolved cases exist.

## Cross-case understanding so far

Repeated/stable candidates:

- a public PR locator can begin acquisition;
- exact case identity must be frozen before evidence is joined;
- dependency path is first-class evidence;
- CI authority requires trigger, commands, responsibility, revision, and
  environment identity;
- missing evidence may produce a specific next action;
- merge status is not correctness proof.

Contradicted or narrowed assumptions:

- dependency role can be represented by one enum;
- green CI has global authority;
- advisory analysis is universally required;
- dynamic execution is always required;
- one complete `CASE.md` fully simulates the runtime;
- manual success proves automation feasibility;
- full investigation must change the broad action to provide value.

## Immediate continuation

Do not select S003 yet.

1. Complete and validate the parallel S001 runtime artifact bundle.
2. Compare the S001 and S002 bundle structures, failure states, and baseline
   behavior.
3. Correct only the owning local specification when that comparison exposes a
   real artifact-model defect.
4. Review both cases, conclusions, and assistance/ownership with Ali.
5. Then select S003: an actual failing dependency-update workflow requiring
   attribution among update-caused, pre-existing, flaky, environmental, and
   unrelated failure.
6. Create S003's narrative and artifacts progressively from the selected/frozen
   checkpoint.

## Verified implementation boundary

The current codebase still has narrow M2 contracts and experiments, including:

- trusted case identity and early evidence contracts;
- model-derived Python-support claim authority;
- deterministic decisions limited to `run_targeted_checks` and `abstain`;
- retained model and input-risk experiments with JSON artifacts.

Those contracts do not define the complete simulation artifact family. Manual
simulation may explore broader future responsibilities without representing them
as implemented behavior.

## Ownership and assistance

- Ali identified that narrative-only scenarios do not model the complete runtime
  artifact lifecycle.
- Ali required product-simulation-local governance and unrestricted method
  exploration within external safety and permission boundaries.
- S002 evidence acquisition, reasoning, artifact construction, and validation
  remain substantially AI-controlled under Ali's direction.
- AI factual review is complete; Ali review is pending.
- Independent Ali capability is not claimed from S002.
- S001 and future cases must record AI/Ali roles separately from execution,
  factual review, external confirmation, and capability evidence.

## Career boundary

Do not update Career for this ordinary project correction. Ali explicitly
initiates a Career review when durable capability, workload, or program state
should change.
