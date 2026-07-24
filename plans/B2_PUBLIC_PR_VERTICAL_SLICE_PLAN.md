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
- [ ] **Current:** acquire all changed-file records safely and validate their response shape.
- [ ] Identify exactly one supported pinned Python dependency version change.
- [ ] Produce an explicit unsupported state for ambiguous or unsupported dependency-change shapes.
- [ ] Acquire exact-head GitHub Actions workflow/check evidence.
- [ ] Establish whether the changed dependency was exercised by the relevant CI commands.
- [ ] Acquire the minimum public package or upstream evidence required by the supported case.
- [ ] Produce the first bounded recommendation or honest abstention with reasons and limits.
- [ ] Keep concise human output consistent with minimum machine-readable state.
- [ ] Add captured-response or normalized-evidence tests for deterministic reruns.
- [ ] Complete at least one Ali-owned central modification, meaningful test, and diagnosis.

Mark an item complete only after the relevant source exists, deterministic tests pass, and required real-environment evidence or explanation has been observed. A checkbox does not by itself establish mastery or production readiness.

## Current increment

### Responsibility

```text
validated PR identity
→ retrieve changed files and patches
→ recognize one exact pinned Python dependency update
```

### Initial supported form

```text
-package==old_version
+package==new_version
```

The first implementation must require:

- exactly one supported dependency change;
- the same normalized package name on removed and added lines;
- explicit old and proposed versions;
- no repository-specific or S004-specific hardcoding;
- explicit unsupported behavior when the shape is ambiguous, missing, truncated, or outside the supported form.

### Required proof

- deterministic successful changed-file acquisition test;
- deterministic supported pinned-change extraction test;
- deterministic unsupported-shape test;
- all active tests pass in WSL2;
- the real `googlefonts/glyphsLib#1145` command reports `requirements-dev.txt` and `pytest 9.0.2 → 9.0.3`;
- Ali explains patch semantics and materially changes or adds one central extraction test or rule.

### Stop boundary

Do not add CI interpretation, PyPI/upstream acquisition, persistence, replay infrastructure, services, agents, models, or final recommendation logic during this increment.

## Plan maintenance

Update this checklist only when observable implementation progress changes. Keep detailed commands, outputs, failures, environment facts, and learning-depth notes in `working-memory/B2_TECHNICAL_PROGRESS.md`, not here.
