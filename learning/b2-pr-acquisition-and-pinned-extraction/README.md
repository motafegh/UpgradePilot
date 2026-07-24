# B2 Learning Snapshot — PR Acquisition and Pinned Dependency Extraction

**Status:** Frozen educational snapshot  
**Recorded:** 2026-07-24  
**Behavioral source/test baseline:** `0ea16d0fbc51312fc70ac6a257e3c97550baeacc`  
**Observed environment:** Ali's WSL2 environment, Python 3.12, editable `.venv` installation  
**Observed proof:** 12 deterministic tests passed; live `googlefonts/glyphsLib#1145` acquisition identified `requirements-dev.txt` and `pytest 9.0.2 → 9.0.3`

## Purpose

This package teaches the exact UpgradePilot responsibility that existed at this point:

```text
public repository + PR number
→ read-only PR metadata acquisition
→ exact proposal identity
→ complete changed-file acquisition
→ patch-evidence classification
→ one exact pinned Python dependency update
→ supported result or explicit unsupported state
```

It is not a transcript, source-code copy, general Python course, or claim of mastery.

## Snapshot rule

This package belongs to the source and tests named above.

Later source improvements must not cause these files to be rewritten merely to match the new implementation. Create a new dated learning snapshot when later work introduces a materially different responsibility, mechanism, or ownership boundary.

Correct this package only for a factual error, unsafe instruction, or broken reference. Record any such correction explicitly.

To inspect the exact historical source later:

```bash
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:src/upgradepilot/github_client.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:src/upgradepilot/dependency_change.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:tests/test_github_client.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:tests/test_dependency_change.py
```

## Study order

### Session A — System and source ownership

Recommended ceiling: **60–75 focused minutes**.

1. [`01-request-to-evidence-flow.md`](01-request-to-evidence-flow.md)  
   Build the complete product and evidence mental model.
2. [`02-code-you-must-own.md`](02-code-you-must-own.md)  
   Learn the central code boundaries and the Python syntax that matters in an AI-assisted engineering workflow.

Expected output: one closed-book flow and one function-level code trace.

### Session B — Tests, diagnosis, and ownership

Recommended ceiling: **45–60 focused minutes**.

3. [`03-tests-and-failure-diagnosis.md`](03-tests-and-failure-diagnosis.md)  
   Understand what each test category protects, what mocks prove, and how to localize failures.
4. [`04-study-session-and-ownership-check.md`](04-study-session-and-ownership-check.md)  
   Perform the measurable checks and author the next ownership test.

Expected output: one bounded failure map and one predicted, authored, and executed normalized-package test.

Do not force both sessions into one sitting when attention or accuracy falls. Completion is based on demonstrated outputs, not time spent or pages read.

## SMART outcome for this snapshot

By the end of the two bounded sessions, Ali should be able to:

- **Specific:** trace the current CLI-to-dependency-result flow and identify the owner of each validation boundary;
- **Measurable:** reconstruct the flow without notes, classify the provided failure cases, explain four test claims, and predict and author the normalized-package test;
- **Achievable:** work only with the current two source responsibilities and their 12 validated tests;
- **Relevant:** prepare for modifying and diagnosing the current extraction boundary rather than memorizing incidental syntax;
- **Time-bounded:** use the stated session ceilings as review checkpoints while treating demonstrated understanding—not elapsed time—as the pass condition.

## Depth expected now

### Must master now

- acquisition versus extraction;
- exact base/head proposal identity;
- transport, HTTP, response-shape, schema, and evidence-consistency boundaries;
- pagination and changed-file count reconciliation;
- patch addition/removal semantics;
- supported versus unsupported as explicit product outcomes;
- the current function-to-function execution path;
- what deterministic tests and one live smoke run do and do not prove;
- how to add and diagnose one meaningful extraction test.

### Understand operationally

- `dataclass(frozen=True, slots=True)`;
- Python 3.12 type aliases and union types;
- `Mapping`, `Any`, tuples, lists, and keyword-only parameters;
- regular-expression `fullmatch` for the current narrow grammar;
- dependency injection through a mockable Requests session;
- `unittest`, `Mock`, `side_effect`, and `assertRaises`.

### Deferred deliberately

- Requests connection-pool, TLS, DNS, and HTTP/2 internals;
- Git's diff algorithm internals;
- complete Python requirement grammar and resolver behavior;
- retry/backoff and rate-limit recovery;
- captured-response replay infrastructure;
- CI authority, PyPI/upstream evidence, recommendations, persistence, services, agents, and models.

## Related active files

- [`../../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- [`../../working-memory/B2_TECHNICAL_PROGRESS.md`](../../working-memory/B2_TECHNICAL_PROGRESS.md)
- [`../../src/upgradepilot/github_client.py`](../../src/upgradepilot/github_client.py)
- [`../../src/upgradepilot/dependency_change.py`](../../src/upgradepilot/dependency_change.py)
- [`../../tests/test_github_client.py`](../../tests/test_github_client.py)
- [`../../tests/test_dependency_change.py`](../../tests/test_dependency_change.py)

The active files may later change. The commit pinned at the top controls this learning snapshot.