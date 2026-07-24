# B2 Public PR Vertical Slice Plan

**Status:** Active  
**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Operating method:** [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md)  
**Technical evidence:** [`../working-memory/B2_TECHNICAL_PROGRESS.md`](../working-memory/B2_TECHNICAL_PROGRESS.md)

## Purpose

Build and understand the smallest credible real UpgradePilot path:

```text
public repository + Dependabot PR number
→ read-only public evidence acquisition
→ exact proposal and dependency identity
→ minimum relevant exact-head CI and public package/upstream evidence
→ bounded recommendation or honest abstention
→ concise traceable output
```

This is a lightweight implementation checklist, not a second roadmap or architecture document.

## Working style

For each bounded increment:

```text
real next responsibility
→ teach only the minimum blocking concepts
→ Ali predicts, questions, or challenges
→ implement one bounded capability
→ run deterministic tests and a safe real example where applicable
→ inspect actual success or failure
→ record only material evidence, limits, and continuation
```

Learning and ownership gates may be deferred only by Ali's explicit instruction. Deferral does not count as completion, mastery, or ownership evidence.

## Progress checklist

- [x] Accept `owner/repository` and PR number through one command.
- [x] Acquire public PR metadata through a read-only GitHub request.
- [x] Validate and print exact repository, PR, base SHA, head SHA, and changed-file count.
- [x] Handle input, timeout/transport, HTTP, and malformed-successful-response failures separately.
- [x] Add focused deterministic tests for successful identity construction and ambiguous `404`.
- [x] Install, test, and run the first increment successfully in Ali's WSL2 environment.
- [x] Acquire all changed-file records safely and validate their response shape.
- [x] Identify exactly one supported pinned Python dependency version change.
- [x] Produce an explicit unsupported state for ambiguous or unsupported dependency-change shapes.
- [ ] **Current:** validate exact-head GitHub Actions workflow, job, and step-summary acquisition in Ali's WSL2 environment.
- [ ] Establish whether the changed dependency was exercised by relevant CI commands.
- [ ] Acquire the minimum public package or upstream evidence required by the supported case.
- [ ] Produce the first bounded recommendation or honest abstention with reasons and limits.
- [ ] Keep concise human output consistent with minimum machine-readable state.
- [ ] Add captured-response or normalized-evidence tests for deterministic reruns.
- [ ] Complete at least one Ali-owned central modification, meaningful test, and diagnosis.

Mark an item complete only after the relevant source exists, deterministic tests pass, and required real-environment evidence or explanation has been observed.

## Current increment — Exact-head GitHub Actions acquisition

### Responsibility

```text
frozen pull-request head SHA
→ pull_request workflow runs for that exact SHA
→ latest-attempt jobs for each run
→ bounded step summaries
→ validated immutable evidence records
→ factual CLI output
```

### Design boundary

The GitHub path is separated into cohesive learning units:

```text
github_api.py       shared GET, timeout, HTTP, and JSON validation
github_client.py    PR identity and changed files
github_actions.py   workflow runs, jobs, and steps
cli.py              orchestration and presentation
```

The separation is by engineering responsibility, not one file per API call.

### Prepared deterministic proof

The assistant's isolated Python 3.13 check observed:

```text
18 deterministic tests passed
syntax compilation passed
```

The new tests protect:

- exact head-SHA and `pull_request` event binding;
- explicit empty workflow-run evidence;
- workflow-run pagination and total-count reconciliation;
- job run-ID and head-SHA binding;
- bounded step-summary parsing;
- malformed or contradictory successful responses.

### Required Ali validation

Run in WSL2:

```bash
git pull --ff-only origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

Inspect and record:

- full deterministic test count;
- exact PR head SHA;
- exact-head workflow-run count and names;
- job names, statuses, conclusions, and step counts;
- any authentication, rate-limit, schema, or availability failure.

### Deferred ownership gate

On 2026-07-24, Ali explicitly deferred the normalized-package identity learning exercise so implementation could continue. It remains unpassed and may be resumed later. No capability or ownership claim may be derived from that deferral.

### Stop boundary

This increment reports what ran for the exact commit. It does not yet decide what the CI evidence proves.

Do not yet:

- infer that the changed dependency was installed or exercised;
- treat green CI as upgrade safety;
- acquire package/upstream evidence;
- produce a merge, targeted-check, block, defer, or abstain recommendation;
- add persistence, replay infrastructure, services, agents, models, or deployment systems.

After live validation, the next increment is exact-head CI-authority interpretation through workflow definitions, installation commands, test commands, dependency paths, environments, and scope.

## Plan maintenance

Update this checklist only when observable implementation progress changes. Keep detailed commands, outputs, failures, environment facts, and learning-depth notes in `working-memory/B2_TECHNICAL_PROGRESS.md`.
