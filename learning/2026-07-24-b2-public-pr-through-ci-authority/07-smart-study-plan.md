# 07 — SMART Source-Driven Study Plan

## Final outcome

After three focused sessions totaling about 3.5–4.5 hours, Ali will be able to:

- reconstruct the complete B2 request-to-CI-authority flow without notes;
- assign each responsibility to the correct source module;
- explain the main public functions, inputs, trusted outputs, and stopping conditions;
- distinguish syntax that must be understood operationally from reasoning that must be mastered;
- trace the S004 live result through source code and tests;
- predict at least 9 of 10 readiness answers correctly;
- add one central test after writing a prediction;
- run focused and complete suites and localize a failure;
- state the exact permitted S004 claim without safety or merge overclaim;
- identify minimum package/upstream evidence as the next product question.

Completion is based on observable outputs, not time spent or pages read.

# Before Session A — setup, 5 minutes

```bash
cd ~/projects/UpgradePilot
git pull --ff-only origin main
source .venv/bin/activate
```

Open two editor groups:

```text
left: learning note
right: source or matching test
```

Create one personal study file outside the frozen snapshot with these headings:

```text
Flow reconstruction
Module contracts
Source mechanisms
Failure localization
Ownership modification
Final readiness answers
```

# Session A — Core flow and source ownership

**Target:** 80–100 minutes, including one 10-minute break.  
**Scope:** CLI, shared GitHub trust boundary, PR/changed files, dependency extraction.  
**Output:** one flow reconstruction plus four source-contract summaries.

## A1 — Reconstruct the whole path, 15 minutes

Read:

```text
01-flow-and-boundaries.md
```

Close it and draw:

```text
locator
→ PR identity
→ changed files
→ dependency identity
→ Actions runs/jobs
→ exact-head workflow definition
→ command evidence
→ CI authority
```

Explain:

- acquisition versus interpretation;
- exception versus bounded result;
- authority versus recommendation.

**Pass:** all stages are present, ordered, and no safety claim appears.

## A2 — Read `cli.py` with guidance, 20 minutes

Read the `cli.py` section of:

```text
08-guided-source-walkthrough-core.md
```

Then inspect in `src/upgradepilot/cli.py`:

1. module docstring;
2. `build_parser()`;
3. `main()` signature;
4. client construction;
5. PR → changed files → dependency sequence;
6. `isinstance(dependency_result, PinnedDependencyChange)` branch;
7. workflow and authority input comprehensions;
8. three exception handlers;
9. final output branches.

Write:

```text
cli.py owns:
Input:
Output:
Why CI is conditional:
Exit 2 means:
Exit 3 means:
Exit 4 means:
One responsibility that must not be added here:
```

**Pass:** correctly identify orchestration, conditional execution, and exit-code meaning.

## A3 — `github_api.py`, 20 minutes

Use the guided section, then inspect:

```text
GitHubAcquisitionError
GitHubResponseError
GitHubApiClient.__init__
_get()
_raise_for_status()
_read_json()
_get_json_object()
_get_json_array()
required_* validators
```

Explain aloud:

```text
Timeout
≠ HTTP 404
≠ HTTP 200 with malformed JSON
≠ HTTP 200 with contradictory domain identity
```

Record:

```text
Why Session injection exists:
Why type hints do not validate JSON:
Why bool must be rejected as int:
Why 404 remains ambiguous:
```

**Pass:** classify four failure examples correctly without looking at exception names.

## A4 — Break, 10 minutes

Leave the screen. Do not replace the break with browsing.

## A5 — `github_client.py`, 15–20 minutes

Read its section in the guided walkthrough and inspect:

```text
PullRequestIdentity
ChangedFile
get_pull_request()
get_changed_files()
_parse_pull_request()
_parse_changed_file()
validate_repository()
validate_pull_number()
```

Trace the pagination loop manually for:

```text
expected changed files: 101
page 1: 100 records
page 2: 1 record
```

Write:

```text
Why head SHA is stronger than branch name:
Why first-page success is incomplete:
Why final count must equal PR metadata:
Why patch may be None in a valid ChangedFile:
```

**Pass:** explain pagination as correctness protection, not performance optimization.

## A6 — `dependency_change.py`, 20 minutes

Read its guided section and inspect:

```text
PinnedDependencyChange
UnsupportedDependencyChange
DependencyChangeResult
extract_pinned_dependency_change()
normalize_package_name()
```

Follow the function in this order:

```text
no files
→ collect added/removed candidates
→ verify visible patch counts
→ require exactly one pair
→ require same file and modified status
→ normalize package identity
→ require changed version
→ supported result
```

Do not decode every regex symbol. Identify only:

- package capture;
- version capture;
- why `fullmatch` is used;
- why normalization collapses `.`, `_`, and `-`.

**Pass:** explain why missing patch, incomplete patch, ambiguity, and package mismatch are results rather than transport exceptions.

## Session A deliverable

Your study file must contain:

- complete flow diagram;
- contract summary for four modules;
- one pagination walkthrough;
- one exception-versus-result table;
- one five-sentence explanation of dependency extraction.

Do not proceed to Session B until you can point to the source statement responsible for each major transition.

# Session B — Exact-head CI evidence and authority reasoning

**Target:** 90–110 minutes, including one 10-minute break.  
**Scope:** Actions, exact-head repository files, workflow commands, authority evaluation.  
**Output:** four module contracts plus a source-level S004 trace.

## B1 — `github_actions.py`, 20–25 minutes

Read its section in:

```text
09-guided-source-walkthrough-ci.md
```

Inspect:

```text
WorkflowRun
WorkflowJob
WorkflowStep
get_exact_head_workflow_runs()
get_workflow_jobs()
_parse_workflow_run()
_parse_workflow_job()
```

Write:

```text
Why filter by head SHA:
Why validate head SHA again:
Why event must be pull_request:
Why total_count must remain stable:
Why steps=None differs from steps=():
```

**Pass:** explain server filtering versus local evidence validation.

## B2 — `github_repository.py`, 20 minutes

Inspect:

```text
RepositoryTextFile
UnavailableRepositoryFile
RepositoryFileEvidence
get_exact_head_workflow_file()
get_exact_head_text_file()
_validate_repository_path()
```

Trace:

```text
run ID
→ run detail
→ workflow path
→ contents endpoint with ref=head_sha
→ base64 bytes
→ UTF-8 workflow text
```

Explain why current default-branch workflow text would be weaker evidence.

**Pass:** distinguish optional-file 404 result from timeout or malformed-response exception.

## B3 — Break, 10 minutes

## B4 — `workflow_commands.py`, 25 minutes

Inspect in order:

```text
WorkflowCommandEvidence
inspect_workflow_commands()
_extract_job_definitions()
_extract_run_commands()
_command_installs_source_file()
_command_invokes_package()
```

Use one small workflow example and mark:

- `jobs:` boundary;
- job key;
- inline or block `run` command;
- pip requirement path;
- direct pytest invocation.

Write:

```text
Supported workflow subset:
Why exactly one job:
Why tox is unresolved:
Why custom scripts are unresolved:
Which syntax I only need operationally:
```

**Pass:** explain why the module is a shallow reader, not a complete YAML parser.

## B5 — `ci_authority.py`, 20 minutes

Inspect:

```text
CIAuthorityStatus
WorkflowAuthorityInput
WorkflowAuthorityAssessment
CIAuthorityResult
evaluate_ci_authority()
_assess_workflow()
```

Reconstruct the per-workflow decision order:

```text
definition unavailable
→ unresolved

revision mismatch
→ unresolved

workflow unsuccessful
→ insufficient

no successful job
→ insufficient

command evidence unresolved
→ unresolved

otherwise
→ sufficient
```

Then reconstruct the overall rule:

```text
one sufficient workflow exists
→ overall sufficient

no successful jobs anywhere
→ overall insufficient

successful CI exists but no sufficient workflow
→ overall unresolved
```

**Pass:** explain existential sufficient versus universal coverage.

## B6 — Trace S004 through source, 15 minutes

Without notes, write:

```text
pytest 9.0.2 → 9.0.3
exact head f3cda8...
Regression Tests:
  run/job evidence from:
  definition evidence from:
  install evidence found by:
  execution evidence found by:
  assessment:
Test + Deploy:
  why unresolved:
overall:
  why sufficient:
not proven:
```

**Pass:** preserve the unresolved workflow and avoid recommendation language.

# Session C — Tests, diagnosis, and bounded ownership

**Target:** 75–95 minutes, including one 10-minute break.  
**Scope:** test claims, mocks, failure localization, one Ali-authored test.  
**Output:** one predicted and executed test modification plus readiness score.

## C1 — Test-reading mechanism, 15 minutes

Read the opening sections of:

```text
10-guided-test-reading-workbook.md
```

For one test from each test module, identify:

```text
Arrange
Act
Assert
Claim
First responsible module if it fails
What it does not prove
```

**Pass:** six test claims described without confusing mocked proof with live proof.

## C2 — Prediction before editing, 10 minutes

Write:

```text
Change:
Expected result type:
Expected normalized package:
Protected invariant:
Failure would localize to:
Production code should change: yes/no and why
```

Task:

```text
removed: demo.package==1.0.0
added:   demo_package==1.1.0
```

Expected:

```text
PinnedDependencyChange
normalized_package == "demo-package"
```

## C3 — Implement, 20 minutes

Add one test in:

```text
tests/test_dependency_change.py
```

AI may help locate the neighboring fixture and review syntax.

You decide:

- expected behavior;
- assertions;
- why the test is central;
- whether only one meaningful variable changed.

Do not change production source unless the test reveals a legitimate defect.

## C4 — Validate, 10 minutes

```bash
python3 -m unittest tests.test_dependency_change -v
python3 -m unittest discover -s tests -v
```

Record:

```text
Prediction correct:
Focused result:
Complete test count:
Production code changed:
Protected invariant:
What passing still does not prove:
```

## C5 — Break, 10 minutes

## C6 — Diagnosis drill, 15 minutes

Complete the failure table in `10-guided-test-reading-workbook.md` without source.

Then answer:

1. changed-file count mismatch;
2. workflow run wrong head SHA;
3. green tox-only workflow;
4. no successful exact-head jobs;
5. exact-head workflow definition unavailable;
6. one sufficient and one unresolved workflow.

Expected classifications:

```text
response/completeness error
contradictory Actions evidence
unresolved authority
insufficient authority
unresolved authority
overall sufficient with unresolved detail retained
```

**Pass:** 6/6 and no recommendation claim.

## C7 — Final explanation, 10 minutes

Without notes, answer:

> How does UpgradePilot reach sufficient CI authority, which source modules establish each step, and why is that not a merge recommendation?

Required terms:

- exact PR head SHA;
- complete changed-file evidence;
- supported pinned dependency;
- exact-head runs and jobs;
- exact-head workflow definition;
- direct install and invocation;
- sufficient versus unresolved;
- missing package/upstream and decision evidence.

# Ten-question readiness check

1. Why is branch name weaker than commit SHA?
2. Why is pagination a correctness rule?
3. Why can `200 OK` still be rejected?
4. Missing patch text: acquisition failure or unsupported evidence?
5. Why normalize Python distribution names?
6. Why validate workflow SHA after server filtering?
7. Why not combine commands across jobs?
8. Why can overall authority be sufficient with an unresolved workflow?
9. Which modules produced the live S004 conclusion?
10. What evidence domain comes next?

Scoring:

- **9–10:** ready for package/upstream evidence.
- **7–8:** repair only weak modules and repeat final explanation.
- **0–6:** repeat the affected session in smaller chunks.

# Final readiness gate

Proceed only when all are true:

- [ ] flow reconstructed without notes;
- [ ] all eight source modules assigned correctly;
- [ ] one contract summary written per module;
- [ ] exact-head and pagination reasoning explained;
- [ ] exception, unsupported, insufficient, and unresolved distinguished;
- [ ] S004 traced through actual source functions;
- [ ] one test from every test module explained as Arrange/Act/Assert/Claim;
- [ ] ownership test predicted before editing;
- [ ] focused and full suites run;
- [ ] failure-localization drill completed;
- [ ] S004 claim stated without safety/merge overclaim;
- [ ] at least 9/10 readiness answers correct.

# Next product question

```text
Does the proposed package version exist,
which minimum package/upstream evidence is relevant,
and what conclusion does that evidence permit?
```

Do not begin by collecting every release fact. First define the minimum evidence required for the supported S004 path.

# Realistic ownership statement

Complete after study:

```text
I can explain:
I can trace in source:
I can predict:
I materially changed:
The deterministic tests established:
The live run established:
I still do not independently own:
The next product question is:
```

Do not promote introduced or operational knowledge to mastery without observable evidence.