# 07 — S002 Case Lab: CI Authority and Missing Environment

**Depth target:** Implementation-adjacent understanding using a real case.  
**Case:** `Aidan-Wallace/kubernetes-dashboard-token-api#20` — HTTPX `0.27.2` → `0.28.1`.  
**Current outcome:** Run targeted checks; merge only after exact-head resolver capture, Ruff, and pytest pass.  
**Execution mode:** Complete retrospective artifact reconstruction.

## 1. Why S002 is educational

S002 challenges several dangerous shortcuts:

```text
direct dependency
+ green CI
+ merged PR
→ update was compatible
```

The case demonstrates that each term is incomplete:

- direct declaration does not describe functional use;
- green CI has authority only for the commands that ran;
- a compatible upstream branch existing does not prove target selection;
- a successful image build does not prove test behavior;
- a historical merge does not reveal the maintainer's technical basis.

## 2. Exact case boundary

Frozen identity:

- repository: `Aidan-Wallace/kubernetes-dashboard-token-api`;
- PR: `#20`;
- base SHA: `b065646e4b7b894964567950f9ad770b02c136c2`;
- head SHA: `391508134b083b8f54461c0b576e8f7985c6ecb4`;
- dependency: `httpx`;
- transition: `0.27.2` → `0.28.1`;
- changed path: `requirements.txt`;
- predecessor: PR `#17`, superseded by `#20`.

The historical merge remains context, not decision proof.

## 3. Multi-axis dependency role

HTTPX was simultaneously:

- directly declared in `requirements.txt`;
- not directly observed in application source;
- functionally used through FastAPI/Starlette `TestClient` in tests;
- installed in the production image because one shared requirements file was installed.

Observed functional path:

```text
tests/test_routes.py
→ fastapi.testclient.TestClient
→ starlette.testclient.TestClient
→ httpx.Client
```

A single label such as `direct`, `test-only`, or `runtime` would lose material information.

## 4. Upstream change relevance

HTTPX 0.28 removed the deprecated `app` argument from `Client` construction.

This matters only after joining the upstream change to the target path.

The target does not call `httpx.Client(app=...)` directly. Starlette's `TestClient` adapter may do so on the target's behalf.

This is adapter-mediated relevance:

```text
upstream API change
→ framework adapter implementation
→ target test behavior
```

## 5. Compatibility threshold

Primary tagged source showed:

- Starlette 0.36.3 passed `app=self.app` to HTTPX;
- Starlette 0.37.2 no longer passed that argument;
- FastAPI 0.115.2 required Starlette `>=0.37.2,<0.41.0`.

Therefore:

```text
old Starlette branch
→ expected incompatibility with HTTPX 0.28

fixed Starlette branch
→ removed-argument issue addressed
```

A compatible branch existed before the selected PR.

But the target's historical FastAPI and Starlette resolution was not preserved because those dependencies were unpinned and the old job logs later expired.

Correct finding:

> Compatibility was likely under a then-current fixed framework line, but the exact target environment and behavioral result were unconfirmed.

## 6. CI authority requires more than color

A CI result should be interpreted through:

```text
repository and revision
+ event and trigger
+ changed-path applicability
+ workflow and job
+ matrix and runner
+ exact commands
+ environment identity
+ result and retention state
+ responsibility exercised
```

### Docker workflow

The observed successful job:

- triggered for the PR;
- installed the shared requirements;
- built the Docker image;
- did not run Ruff;
- did not run pytest;
- did not initialize `TestClient` as a test responsibility.

Authority:

> The dependency set installed sufficiently for the image build at that time.

Not established:

> The TestClient route tests passed with HTTPX 0.28.1.

### Python workflow

The workflow contained:

- `ruff check .`;
- `pytest --cov`.

But its PR path filters excluded `requirements.txt`.

Because the dependency PR changed only that file, the decision-relevant Python workflow did not trigger.

## 7. Missing historical environment

The investigator attempted to retrieve the old Docker job logs to identify the resolved framework versions.

The endpoint returned HTTP 410.

The correct state is:

- log: expired/inaccessible;
- exact historical resolution: unrecoverable publicly;
- fresh resolution: not equivalent historical evidence;
- likely compatibility: remains conditional;
- next action: capture a new exact-head resolution and run the existing checks.

## 8. Why fresh resolution cannot silently replace history

A fresh install may resolve newer FastAPI or Starlette versions than the original job.

It can answer:

> Does the frozen target head work under the newly captured environment?

It cannot answer:

> Which exact environment produced the historical successful Docker build?

These are different evidence boundaries and may require a new run or comparison.

## 9. Decision sufficiency

### Why not merge immediately

- the exact TestClient path was decision-relevant;
- public CI did not run the relevant tests;
- the target's historical framework resolution was unavailable.

### Why not block indefinitely

- a corrected Starlette branch existed;
- a then-current FastAPI line required that branch;
- the dependency installation and image build succeeded;
- existing focused tests could resolve the remaining uncertainty.

### Proportionate action

1. install the frozen requirements in a trusted isolated checkout;
2. preserve the complete resolved package set;
3. run `ruff check .`;
4. run `pytest --cov`.

## 10. Follow-up transitions

- resolver captured and checks pass → merge after normal review;
- TestClient or route tests fail through the changed interface → investigate or block;
- checks unavailable or inconclusive → retain targeted-check or defer state;
- head, constraints, workflow, or resolution changes → new run or comparison;
- historical merge → record user action only.

## 11. Baseline comparison

The baseline saw:

- minor version category;
- passing overall CI;
- direct dependency;
- literal caution signals such as `deprecated` and `removed`.

It selected `run_targeted_checks`.

The full investigation selected the same action but added:

- exact TestClient path;
- old and fixed adapter branches;
- likely compatibility with unresolved environment;
- limited authority of Docker CI;
- skipped Python workflow;
- expired log state;
- exact resolver/Ruff/pytest checks;
- state transitions.

## 12. Superseded hypothesis

An early concern was that HTTPX 0.28 could directly break the target.

Later source comparison narrowed this:

```text
possible hard break
→ identify adapter threshold
→ compatible branch exists
→ exact target branch unknown
→ focused test required
```

The original concern remains visible as superseded rather than disappearing.

## 13. Source walk

Read in this order:

1. S002 `README.md`;
2. S002 `CASE.md` sections on dependency role, compatibility, CI authority, decision, and transitions;
3. `OPERATION_EVENTS.jsonl` operations 3–7;
4. `EVIDENCE_ITEMS.jsonl` records for target use, upstream source, workflows, run/job, and HTTP 410;
5. `CLAIMS_AND_INTERPRETATIONS.jsonl` records C02–C08;
6. `FINDINGS.json` F0–F8;
7. `BASELINE_RESULT.json`;
8. `DECISION.json`;
9. `FOLLOW_UP_STATE.json`;
10. `REVIEW_AND_OWNERSHIP.json`.

## 14. Lab tasks

### Task A — dependency-role matrix

Create a matrix for declaration, direct application use, adapter-mediated use, test responsibility, and deployment installation.

### Task B — CI authority map

For both workflows, record:

- trigger;
- changed-path applicability;
- exact commands;
- environment information;
- observed result;
- responsibility exercised;
- what remains untested.

### Task C — compatibility chain

Explain how HTTPX, Starlette, FastAPI, target constraints, and resolver identity connect.

### Task D — evidence-state correction

Rewrite these invalid statements:

- “No logs means the build environment did not exist.”
- “Green Docker CI proves the tests pass.”
- “A compatible FastAPI release proves the target used it.”
- “The merged PR confirms compatibility.”

### Task E — decision transition

For each possible targeted-check result, state which artifacts must be added or superseded and whether a new run is required.

## 15. Ownership checkpoint

Explain without opening the prepared human report:

1. How did the target use HTTPX?
2. Why is `direct dependency` an incomplete role description?
3. What exact upstream change mattered?
4. What source comparison identified the compatibility threshold?
5. Why was compatibility likely but unproven?
6. What did the Docker job prove?
7. Why did the Python workflow not run?
8. Why was HTTP 410 decision-relevant?
9. Why were the selected checks proportionate?
10. Under what change must the existing decision not be silently reused?

## 16. Current demonstrated depth

S002 demonstrates adapter-mediated relevance, CI-authority analysis, explicit retention failure, and proportionate targeted checks. It does not demonstrate the actual exact-head test result, historical resolver recovery, prospective execution, or Ali-owned technical analysis.
