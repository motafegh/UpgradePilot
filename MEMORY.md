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
may be used, regardless of current milestone or implementation status. This may
include scripts, local checkout, package installation, tests, containers,
databases, SQL, models, LLMs, agents, static/dynamic analysis, and human review.

Simulation use does not admit the method into supported product architecture.
Target repositories must not be mutated without exact authorization. Untrusted
code must be isolated and its effects recorded.

## S001 — narrative complete; artifact retrofit required

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

Retrofit requirements:

- mark execution mode as retrospective artifact reconstruction;
- preserve operation-order and timestamp gaps;
- preserve unavailable raw connector outputs;
- materialize evidence, claims, findings, decision, reports, follow-up, and review;
- create the retrospective transparent baseline v0.1 result;
- do not claim historical JSON artifacts existed during the original case.

## S002 — narrative complete; artifact retrofit required

Navigation:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md)

Primary narrative:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md)

Case: `Aidan-Wallace/kubernetes-dashboard-token-api#20`, HTTPX 0.27.2 → 0.28.1.

Outcome:

> Run targeted checks; merge only if the exact-head Python checks pass under a
> captured dependency resolution.

Stable findings:

- HTTPX was directly declared, functionally used through FastAPI/Starlette
  `TestClient`, and installed into the production image;
- HTTPX 0.28 removed the `app` Client argument;
- Starlette 0.36.3 passed it; 0.37.2 no longer did;
- a then-current compatible FastAPI line existed, but exact target resolution is
  unavailable;
- Docker CI proved installation/image build only;
- Python tests did not trigger because `requirements.txt` was excluded;
- historical logs expired with HTTP 410;
- predecessor PR #17 was superseded by #20;
- eventual merge is historical action, not correctness proof.

Retrofit requirements:

- preserve candidate screening before identity freeze;
- preserve the HTTP 410 operation and inaccessible evidence state;
- materialize current evidence and finding IDs;
- preserve likely-compatible but unproven status;
- create decision transitions and follow-up state;
- create retrospective transparent baseline v0.1 result;
- record the limitation that progressive narrative structure does not by itself
  prove all durable artifacts were created during the original investigation.

## Baseline and thesis status

Current comparator:
`simulation-transparent-baseline-v0.1`.

It may use only:

- version-change category;
- current overall CI conclusion;
- dependency directness;
- literal release-note keyword signals.

The two cases qualitatively support the UpgradePilot thesis, but comparative
validation remains open until `BASELINE_RESULT.json` exists for each case.

Future case coverage must include:

- wrong baseline action;
- same action with materially weaker baseline reasoning;
- a simple case where the baseline is sufficient;
- unresolved comparison.

## Cross-case understanding so far

Repeated/stable candidates:

- a public PR locator can begin acquisition;
- exact case identity must be frozen before evidence is joined;
- dependency path is first-class evidence;
- CI authority requires trigger, commands, responsibility, revision, and
  environment identity;
- missing evidence may produce a specific next action;
- merge status is not correctness proof.

Contradicted assumptions:

- dependency role can be represented by one enum;
- green CI has global authority;
- advisory analysis is universally required;
- dynamic execution is always required;
- one complete `CASE.md` fully simulates the runtime;
- manual success proves automation feasibility.

## Immediate continuation

Do not select S003 yet.

1. Retrofit S001 with an honest manual runtime artifact bundle.
2. Validate JSON/JSONL syntax, IDs, references, provenance, baseline, reports,
   follow-up, and review state.
3. Retrofit S002 with the fullest recoverable bundle.
4. Validate it and compare defects with S001.
5. Update only the local simulation owner if the bundle model proves wrong.
6. Review both cases and assistance/ownership with Ali.
7. Then select S003: an actual failing dependency-update workflow requiring
   attribution among update-caused, pre-existing, flaky, environmental, and
   unrelated failure.
8. Create S003's narrative and artifacts progressively from the selected/frozen
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
- Ali required product-simulation-local governance to override conflicting
  project-local method and artifact restrictions.
- Ali required unrestricted method exploration within external safety and
  permission boundaries.
- S001 and S002 remain substantially AI-investigated and AI-documented under Ali's
  direction; independent Ali capability is not claimed.
- Retrofits must record AI/Ali roles separately from execution and factual review.

## Career boundary

Do not update Career for this ordinary project correction. Ali explicitly
initiates a Career review when durable capability, workload, or program state
should change.