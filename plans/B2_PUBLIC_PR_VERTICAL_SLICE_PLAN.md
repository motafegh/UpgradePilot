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

This plan is a lightweight implementation checklist, not a second roadmap or architecture document.

## Working style

For each bounded increment:

```text
real next responsibility
→ teach only the minimum blocking concepts
→ Ali predicts, questions, or challenges
→ implement one bounded capability
→ run deterministic tests and a safe real example where applicable
→ inspect the actual success or failure
→ classify must-master, operational, deferred, and Ali-owned learning
→ Ali explains, modifies, tests, or diagnoses one central boundary
→ record only material evidence and continuation
```

Do not study every source line equally. Deepen code, syntax, tools, or internals only when they are central to the active responsibility, diagnosis, safety, target career, or ownership transfer.

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
- [ ] Acquire exact-head GitHub Actions workflow/check evidence.
- [ ] Establish whether the changed dependency was exercised by the relevant CI commands.
- [ ] Acquire the minimum public package or upstream evidence required by the supported case.
- [ ] Produce the first bounded recommendation or honest abstention with reasons and limits.
- [ ] Keep concise human output consistent with minimum machine-readable state.
- [ ] Add captured-response or normalized-evidence tests for deterministic reruns.
- [ ] **Current:** complete at least one Ali-owned central modification, meaningful test, and diagnosis.

Mark an item complete only after the relevant source exists, deterministic tests pass, and required real-environment evidence or explanation has been observed. A checkbox does not by itself establish mastery or production readiness.

## Current increment

### Responsibility

```text
validated changed-file acquisition and pinned dependency extraction
→ Ali-owned central test or rule modification
→ rerun deterministic proof
→ explain the protected boundary
```

### Completed implementation proof

Observed in Ali's WSL2 environment on 2026-07-24:

- all 12 active deterministic tests passed;
- the real `googlefonts/glyphsLib#1145` command acquired `requirements-dev.txt`;
- the command identified `pytest 9.0.2 → 9.0.3`;
- source, deterministic tests, and live public evidence now satisfy the acquisition and extraction proof boundary.

### Remaining ownership proof

Ali must materially add or change one central extraction test or rule, predict its outcome before execution, rerun the suite, and explain why the behavior is supported or unsupported.

The selected next ownership exercise is the normalized-package identity boundary: equivalent Python distribution spellings using `.`, `_`, or `-` must compare as the same package under the current normalization rule.

### Stop boundary

Do not add CI interpretation, PyPI/upstream acquisition, persistence, replay infrastructure, services, agents, models, or final recommendation logic until the ownership exercise is completed and reviewed.

## Plan maintenance

Update this checklist only when observable implementation progress changes. Keep detailed commands, outputs, failures, environment facts, and learning-depth notes in `working-memory/B2_TECHNICAL_PROGRESS.md`, not here.
