# 07 — SMART Study Plan

## Final outcome

After two focused sessions totaling about 2.5–3 hours, Ali will:

- reconstruct the current B2 flow and module map without notes;
- explain exact-head identity, completeness, and authority states;
- predict at least 9 of 10 readiness answers correctly;
- implement one central test modification after writing a prediction;
- run the focused and complete suites;
- localize any failure to the responsible boundary;
- state the S004 claim without safety or merge overclaim;
- identify minimum package/upstream evidence as the next product question.

Completion is based on outputs, not time spent.

# Session A — Understand and reconstruct

**Target:** 70–85 minutes, including one 10-minute break.  
**Output:** one personal reconstruction note.

## A1 — Flow, 15 minutes

Read `01-flow-and-boundaries.md`.

Close it and draw:

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

Explain acquisition versus interpretation and why authority is not recommendation.

**Pass:** all stages present; no safety claim.

## A2 — Modules, 20 minutes

Read `02-module-map.md`.

Inspect only module docstrings, public dataclasses, and public functions in `src/upgradepilot/`.

Write one sentence for:

```text
github_api.py
github_client.py
dependency_change.py
github_actions.py
github_repository.py
workflow_commands.py
ci_authority.py
cli.py
```

Answer:

1. Retry policy belongs where?
2. Tox tracing belongs where?
3. Why does Actions acquisition not decide authority?
4. Why is repository-definition acquisition separate?

**Pass:** 4/4 with reasoning.

## A3 — Break, 10 minutes

Leave the screen. Do not replace the break with browsing.

## A4 — Trust, 15 minutes

Read `03-evidence-trust-and-identity.md`.

Create this table:

| State | Example | Exception or result? | Why? |
|---|---|---|---|
| input rejected | | | |
| acquisition failed | | | |
| contradictory response | | | |
| valid but unresolved | | | |

**Pass:** unresolved is a normal result, not a generic exception.

## A5 — S004 authority, 15–20 minutes

Read `04-dependency-and-ci-authority.md`.

Write, from memory:

```text
pytest 9.0.2 → 9.0.3
Regression Tests → sufficient because ...
Test + Deploy → unresolved because ...
overall → sufficient because ...
not yet proven → ...
```

**Pass:** mention exact head, successful direct install, direct pytest invocation, existential overall claim, and missing recommendation evidence.

## Session A deliverable

One note containing:

- flow diagram;
- one sentence per module;
- four-state table;
- S004 explanation in five sentences or fewer.

Repair only weak sections before Session B; do not reread everything.

# Session B — Ownership and diagnosis

**Target:** 75–95 minutes, including one 10-minute break.  
**Output:** one predicted code/test modification and validation record.

## B1 — Code depth, 15 minutes

Read `05-ai-era-code-ownership.md`.

Mark each item:

- `M` must master;
- `O` operationally understand;
- `D` deferred.

Items:

```text
function contracts
dataclass purpose
union results
exception versus result
pagination invariant
regex internals
mock side_effect
async HTTP
full YAML parsing
failure localization
```

Expected emphasis: contracts, states, invariants, claims, and diagnosis are `M`; syntax details mostly `O`; async/full YAML are `D`.

## B2 — Written prediction, 10 minutes

Before editing, write:

```text
Change:
Expected result:
Responsible test/module:
Protected invariant:
Failure would localize to:
```

Recommended task in `tests/test_dependency_change.py`:

```text
-demo.package==1.0.0
+demo_package==1.1.0
```

Expected:

```text
supported
normalized package: demo-package
```

## B3 — Implement with AI assistance, 20 minutes

AI may locate the neighboring fixture, explain syntax, and review the test.

You decide:

- expected behavior;
- assertions;
- why it is central;
- whether the test changes only one meaningful variable.

Do not change production code unless a legitimate defect is revealed.

## B4 — Validate, 10 minutes

Run focused then complete tests:

```bash
python3 -m unittest tests.test_dependency_change -v
python3 -m unittest discover -s tests -v
```

Record:

- prediction correct or incorrect;
- focused result;
- full test count;
- failure, if any;
- production code changed or unchanged;
- boundary protected by the test.

## B5 — Break, 10 minutes

## B6 — Diagnosis, 15 minutes

Read `06-tests-diagnosis-and-design.md`.

Classify without notes:

1. changed-file count mismatch;
2. workflow run has wrong head SHA;
3. green tox-only workflow;
4. no successful exact-head jobs;
5. exact-head workflow definition unavailable;
6. one sufficient and one unresolved workflow.

Expected:

1. response/completeness error;
2. contradictory Actions evidence;
3. unresolved authority;
4. insufficient authority;
5. unresolved authority;
6. overall sufficient with unresolved detail preserved.

**Pass:** 6/6 and no recommendation claim.

## B7 — Final explanation, 10 minutes

Without notes, answer:

> How does UpgradePilot reach sufficient CI authority, and why is that not a merge recommendation?

Required terms:

- exact PR head SHA;
- complete changed-file evidence;
- supported pinned dependency;
- exact-head runs/jobs;
- exact-head workflow definition;
- direct install and invocation;
- sufficient versus unresolved;
- missing package/upstream and decision evidence.

# Ten-question readiness check

1. Why is branch name weaker than commit SHA?
2. Why is pagination a correctness rule?
3. Why can `200 OK` still be rejected?
4. Missing patch text: acquisition failure or unsupported evidence?
5. Why normalize distribution names?
6. Why is tox unresolved today?
7. Why not combine commands across jobs?
8. Why can overall authority be sufficient with an unresolved workflow?
9. What exactly did live S004 prove?
10. What evidence domain comes next?

Scoring:

- **9–10:** ready for the next increment.
- **7–8:** repair only weak sections and repeat the final explanation.
- **0–6:** repeat Session A in smaller chunks.

# Readiness gate

Proceed only when all are true:

- [ ] flow reconstructed without notes;
- [ ] module ownership assigned correctly;
- [ ] exact-head and pagination reasoning explained;
- [ ] sufficient/insufficient/unresolved distinguished;
- [ ] ownership test predicted before execution;
- [ ] focused and full suites run;
- [ ] one failure-localization explanation recorded;
- [ ] S004 claim stated without safety/merge overclaim;
- [ ] at least 9/10 readiness questions correct.

# Next product question

```text
Does the proposed package version exist,
which minimum package/upstream evidence is relevant,
and what conclusion does that evidence permit?
```

Do not begin by collecting every release fact. First define the minimum evidence required for the supported S004 decision path.

# Realistic ownership statement

Complete after study:

```text
I can explain:
I can predict:
I materially changed:
The tests established:
The live run established:
I still do not independently own:
The next product question is:
```

Do not promote introduced or operational knowledge to mastery without evidence.