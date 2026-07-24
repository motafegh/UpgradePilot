# 08 — SMART Study and Ownership Check

## Purpose

This is tomorrow's execution plan. It is session-based rather than day-based. Stop after a session if attention or energy drops; do not turn the material into passive reading.

## Final SMART outcome

After two focused sessions totaling approximately 2.5–3 hours, Ali will:

- reconstruct the current B2 flow and module map without notes;
- explain exact-head identity, pagination, evidence states, and CI authority;
- predict at least 8 of 10 self-check outcomes correctly;
- complete one central test modification with a written prediction;
- run the full suite and diagnose the protected boundary;
- explain what the live S004 result proves and does not prove;
- state the next product question: minimum package/upstream evidence.

Completion requires observable outputs, not time spent.

# Session A — Understand the system

**Target duration:** 75–90 minutes including one break.  
**Primary outcome:** reconstruct the architecture and reasoning without notes.

## A0 — Setup, 5 minutes

Open these side by side:

```text
learning/2026-07-24-b2-public-pr-through-ci-authority/
src/upgradepilot/
tests/
```

Create a temporary personal note titled:

```text
B2 reconstruction — 2026-07-25
```

Do not edit the learning snapshot.

## A1 — Mental model, 15 minutes

Read:

- `01-system-mental-model.md`;
- only the public headings/docstrings of `cli.py`.

Then close the note and draw:

```text
locator
→ PR identity
→ changed files
→ dependency identity
→ Actions evidence
→ workflow definition
→ command evidence
→ CI authority
```

Required spoken explanation:

- acquisition versus interpretation;
- exact-head meaning;
- sufficient versus unresolved;
- why authority is not recommendation.

**Pass condition:** complete flow with no missing stage and no safety claim.

## A2 — Module ownership, 20 minutes

Read:

- `02-module-map-and-call-flow.md`.

Inspect only:

- module docstrings;
- public dataclasses;
- public functions/methods.

Do not read every helper yet.

Write one sentence per module:

```text
github_api.py:
github_client.py:
dependency_change.py:
github_actions.py:
github_repository.py:
workflow_commands.py:
ci_authority.py:
cli.py:
```

Then answer without notes:

1. Where would retry policy belong?
2. Where would tox tracing belong?
3. Where would JSON CLI output belong?
4. Why does `github_actions.py` not decide authority?

**Pass condition:** at least 4/4 correct with reasoning.

## A3 — Break, 10 minutes

Leave the screen. Do not replace the break with unrelated browsing.

## A4 — Trust and identity, 20 minutes

Read:

- `03-evidence-acquisition-and-trust.md`.

Inspect:

- error classes and request methods in `github_api.py`;
- identity and pagination checks in `github_client.py` and `github_actions.py`;
- exact-head file retrieval in `github_repository.py`.

Write a four-row table:

| State | Example | Exception or result? | Why? |
|---|---|---|---|
| input rejected | | | |
| acquisition failed | | | |
| contradictory response | | | |
| valid but unresolved | | | |

**Pass condition:** unresolved is represented as a normal result, not a generic exception.

## A5 — Authority reasoning, 20 minutes

Read:

- `04-dependency-and-ci-authority.md`.

Inspect:

- `extract_pinned_dependency_change()`;
- `inspect_workflow_commands()`;
- `evaluate_ci_authority()`.

Reconstruct S004:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
Regression Tests → sufficient because ...
Test + Deploy → unresolved because ...
overall → sufficient because ...
```

**Pass condition:** mention exact-head, successful job, install command, direct pytest invocation, and existential overall claim.

## Session A output

Save the reconstruction note containing:

- complete flow diagram;
- one sentence per module;
- four-row state table;
- S004 reasoning in five sentences or fewer.

If any item is incomplete, start Session B by repairing it rather than rereading everything.

# Session B — Code ownership and diagnosis

**Target duration:** 75–100 minutes including one break.  
**Primary outcome:** make and validate one meaningful modification.

## B1 — Code depth, 20 minutes

Read:

- `05-code-and-syntax-to-own.md`.

For each construct, mark:

```text
M = must master
O = operationally understand
D = deferred
```

Items:

- function contracts;
- dataclass options;
- union result types;
- `isinstance` result narrowing;
- pagination loops;
- regular-expression internals;
- async HTTP;
- complete YAML parsing;
- mock `side_effect`;
- exception translation.

Expected focus:

- contracts, result states, invariants, diagnosis: M;
- detailed syntax and mocks: mostly O;
- async/full YAML: D.

## B2 — Design challenge, 15 minutes

Read:

- `06-design-reasoning-and-tradeoffs.md`.

Choose two proposals and write:

```text
proposal:
responsibility served:
simplest baseline:
risk controlled:
cost added:
evidence needed to admit it:
```

Recommended proposals:

- add PyYAML;
- add tox tracing;
- add retry/backoff;
- add a database.

**Pass condition:** decision is based on product evidence, not preference for simplicity or sophistication.

## B3 — Ownership prediction, 10 minutes

Before changing code, write this prediction:

```text
Change:
Expected result:
Responsible module/test:
Protected invariant:
Failure would localize to:
```

Recommended ownership task:

Add a test to `tests/test_dependency_change.py` for:

```text
-demo.package==1.0.0
+demo_package==1.1.0
```

Expected result:

```text
supported dependency change
normalized package: demo-package
```

Do not run the test before recording the prediction.

## B4 — Implement with AI assistance, 20 minutes

You may ask AI to:

- locate the best neighboring test;
- explain fixture fields;
- propose the smallest test body;
- review your test for accidental overreach.

You must personally decide:

- expected behavior;
- assertions;
- why the rule is central;
- whether the test isolates one variable.

Do not change production code unless the predicted supported behavior fails for a legitimate defect.

## B5 — Validate, 10 minutes

Run the focused test first, then the full suite:

```bash
python3 -m unittest tests.test_dependency_change -v
python3 -m unittest discover -s tests -v
```

Record:

- focused result;
- full test count;
- any failure;
- whether production code changed;
- whether prediction was correct.

## B6 — Break, 10 minutes

## B7 — Diagnosis practice, 15 minutes

Read:

- `07-tests-diagnosis-and-claims.md`.

Without notes, diagnose:

1. changed-file count mismatch;
2. workflow run with wrong head SHA;
3. successful tox-only workflow;
4. no successful exact-head jobs;
5. workflow definition unavailable at exact head;
6. one sufficient and one unresolved workflow.

Required answers:

1. response/completeness error;
2. contradictory Actions evidence;
3. unresolved authority;
4. insufficient authority;
5. unresolved authority;
6. overall sufficient while retaining unresolved detail.

**Pass condition:** 6/6 classifications and no recommendation claim.

## B8 — Final explanation, 10 minutes

Explain aloud, without notes:

> UpgradePilot receives a repository and PR number. How does it reach sufficient CI authority, and why is that not yet a merge recommendation?

Your answer must include:

- exact PR head SHA;
- complete changed-file acquisition;
- supported pinned dependency identity;
- exact-head workflow run/job evidence;
- exact-head workflow definition;
- direct install and invocation evidence;
- sufficient/unresolved distinction;
- missing package/upstream and decision evidence.

# Ten-question readiness check

Answer without reading the notes.

1. Why is a branch name weaker than a commit SHA?
2. Why is pagination part of evidence correctness?
3. Why can a successful HTTP response still be rejected?
4. Why is missing patch text not a transport failure?
5. Why normalize Python distribution names?
6. Why does a tox command remain unresolved today?
7. Why must install and execution evidence not be combined across jobs automatically?
8. Why can overall authority be sufficient when one workflow is unresolved?
9. What does the live S004 result prove?
10. What evidence is needed next before a bounded recommendation?

## Scoring

- **9–10 correct:** ready for the next product increment.
- **7–8 correct:** repair only the weak sections, then repeat the explanation.
- **0–6 correct:** repeat Session A in smaller chunks before continuing.

# Readiness gate for the next increment

You are ready to proceed to package/upstream evidence when all are true:

- [ ] complete flow reconstructed without notes;
- [ ] module responsibilities correctly assigned;
- [ ] exact-head and pagination reasoning explained;
- [ ] sufficient/insufficient/unresolved states distinguished;
- [ ] ownership test predicted and implemented;
- [ ] complete deterministic suite passes;
- [ ] one failure-localization explanation recorded;
- [ ] S004 claim stated without safety or merge overclaim;
- [ ] at least 9/10 readiness questions answered correctly.

# Next product question

After the readiness gate, the next implementation work should answer:

```text
Does the proposed package version exist,
what public package/upstream evidence is relevant,
and what does that evidence permit UpgradePilot to conclude?
```

Do not start by collecting every possible release fact. First define the minimum evidence needed for the supported S004 decision path.

# Final ownership statement template

Complete this after the study:

```text
I can now explain:

I can predict:

I materially changed:

The tests established:

The live run established:

I still do not independently own:

The next product question is:
```

This statement should be realistic. Do not upgrade “introduced” or “operationally understood” knowledge to mastery without evidence.