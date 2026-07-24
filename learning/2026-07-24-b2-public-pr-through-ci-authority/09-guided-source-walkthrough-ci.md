# 09 — Guided Source Walkthrough: Actions Evidence, Exact-Head Files, Workflow Commands, and CI Authority

## Purpose

Use this file with:

```text
src/upgradepilot/github_actions.py
src/upgradepilot/github_repository.py
src/upgradepilot/workflow_commands.py
src/upgradepilot/ci_authority.py
```

This is the second half of the current source pipeline:

```text
proven dependency identity
→ exact-head Actions evidence
→ exact-head workflow definition
→ bounded command evidence
→ CI-authority classification
```

The central discipline is evidence provenance. Every interpretation must remain tied to the exact PR head SHA and must stop when the current rule cannot safely prove more.

# 1. `github_actions.py` — what ran for the exact commit?

## What this module owns

It acquires and validates:

- pull-request-triggered workflow runs for the frozen head SHA;
- latest-attempt jobs for each run;
- optional step summaries.

It does not decide whether the workflow installed or exercised the changed dependency.

## Public records

### `WorkflowRun`

Important fields:

```text
run_id
workflow_id
name
event
head_sha
status
conclusion
run_attempt
```

`status` and `conclusion` are separate because a run can be queued or in progress without a final conclusion.

### `WorkflowJob`

A job remains attached to:

- its `run_id`;
- the exact `head_sha`;
- its status and conclusion;
- its optional step summaries.

### `WorkflowStep`

Step records are summaries, not full logs. They establish names and outcomes but do not automatically reveal the actual shell command or runtime behavior.

## `get_exact_head_workflow_runs()`

The GitHub query includes:

```python
{
    "event": "pull_request",
    "head_sha": identity.head_sha,
    "per_page": 100,
    "page": page,
}
```

Why validate locally after filtering remotely?

```text
server-side filter
= acquisition convenience

local identity check
= evidence trust
```

A returned run with another event or SHA is contradictory evidence and must be rejected.

## Workflow-run pagination

The method tracks both:

```python
expected_total: int | None
records: list[WorkflowRun]
```

It rejects:

- totals above the bounded limit;
- `total_count` changing between pages;
- more records than declared;
- fewer final records than declared.

This protects completeness and consistency.

The expression:

```python
while expected_total is None or len(records) < expected_total:
```

means:

- acquire the first page before the total is known;
- continue until the complete declared set is acquired.

## `get_workflow_jobs()`

Before making the request, the code checks:

```python
if run.head_sha != identity.head_sha:
```

This prevents a caller from accidentally combining a PR identity with a run from another revision.

The query uses:

```text
filter=latest
```

because the current boundary evaluates the latest attempt rather than combining jobs across reruns.

Jobs are validated against both:

- requested run ID;
- frozen PR head SHA.

## Parsing methods

`_parse_workflow_run()` and `_parse_workflow_job()` are domain-specific trust boundaries.

They convert external dictionaries into immutable records only after checking:

- event;
- SHA;
- IDs;
- required fields;
- optional step shape.

`steps=None` means step summaries were absent. It does not mean zero steps. An empty tuple means an explicitly present empty array.

## What to master

Must master:

- exact-head and event binding;
- why local validation repeats server filters;
- run/job identity relationships;
- total-count reconciliation;
- absent steps versus empty steps.

Operationally understand:

- nested pagination loops;
- optional strings;
- tuple construction;
- parser helper methods.

## Matching tests

Read:

```text
test_acquires_runs_for_exact_head_and_event
test_empty_exact_head_result_is_explicit_not_successful_ci
test_rejects_run_for_different_head
test_acquires_all_workflow_run_pages
test_acquires_jobs_and_step_summaries_for_run
test_rejects_job_for_different_head
```

For each, identify the first unsafe conclusion that could occur if the check disappeared.

# 2. `github_repository.py` — what workflow definition belonged to that run?

## The factual gap this module closes

Actions run records tell us which workflow ran, but not the full workflow commands.

The evaluator therefore needs:

```text
run identity
→ workflow path used by that run
→ file content at the same head SHA
```

Reading the workflow from the current default branch would be unsafe because the file may have changed or moved after the PR run.

## Result union

```python
type RepositoryFileEvidence = (
    RepositoryTextFile | UnavailableRepositoryFile
)
```

This union encodes an important distinction:

- valid text was acquired;
- an optional exact-revision file was absent or inaccessible.

An ambiguous `404` for this optional interpretation input becomes a bounded unavailable result. Timeouts, rate limits, malformed payloads, or contradictory identity still raise exceptions.

## `get_exact_head_workflow_file()`

First invariant:

```python
run.head_sha == identity.head_sha
```

Then the client acquires run detail because that response carries the workflow path used by the actual execution.

The returned detail must agree on:

- run ID;
- workflow ID;
- head SHA;
- `pull_request` event;
- path under `.github/workflows/`.

Why check the path prefix?

Because this method claims to retrieve a GitHub Actions workflow definition, not any arbitrary repository file.

## `get_exact_head_text_file()`

The contents request binds the lookup to:

```python
params={"ref": identity.head_sha}
```

This `ref` is the provenance anchor.

The code validates:

- response describes a regular file;
- returned path equals requested path;
- blob SHA is present;
- encoding is `base64`;
- encoded content is text;
- decoded bytes stay below a bounded limit;
- bytes decode as UTF-8.

## Base64 mechanism

GitHub's contents API provides file bytes encoded as base64.

The code removes whitespace before strict decoding:

```python
compact_content = "".join(encoded_content.split())
raw_content = base64.b64decode(compact_content, validate=True)
```

You need operational understanding only:

```text
base64 text
→ decoded bytes
→ UTF-8 source text
```

You do not need to memorize the encoding algorithm.

## Repository path validation

`_validate_repository_path()` rejects:

- empty paths;
- absolute paths;
- trailing slash;
- empty segments;
- `.` and `..` traversal segments.

This is both correctness and boundary protection.

## What to master

Must master:

- why run-specific path is used;
- why the file is fetched at exact head SHA;
- unavailable optional evidence versus malformed evidence;
- path and revision consistency.

Operationally understand:

- URL quoting;
- base64 decoding;
- UTF-8 decoding;
- file-size bound.

## Matching tests

Read:

```text
test_resolves_workflow_path_and_decodes_exact_head_text
test_rejects_workflow_run_detail_identity_mismatch
test_ambiguous_404_becomes_explicit_unavailable_file
```

Explain why only the third produces a normal evidence result.

# 3. `workflow_commands.py` — a deliberately shallow workflow reader

## Why this is not called a YAML parser

The module supports only a narrow indentation-based subset sufficient for the first rule:

- a visible `jobs:` mapping;
- direct job keys;
- inline or block `run:` commands;
- pip requirement installation;
- direct package invocation.

It does not claim complete YAML semantics.

This naming and scope are important. Calling it a full parser would make its results sound more authoritative than they are.

## `WorkflowCommandEvidence`

The result carries:

- `supported` or `unresolved`;
- stable reason and detail;
- observed job count;
- optional install and execution commands.

The commands are retained as traceable evidence for output and later diagnosis.

## `inspect_workflow_commands()`

The first step:

```python
jobs = _extract_job_definitions(text)
```

Then two guards:

```text
jobs mapping unreadable
→ unresolved

job count not exactly one
→ unresolved
```

Why exactly one job?

Because combining installation from job A with execution from job B could claim a path that never existed in one runtime environment.

## Command search

For the single job, the code independently searches for:

```text
install command
execution command
```

Both must exist.

If only one exists, the result remains unresolved and preserves whichever command was found.

## `_extract_job_definitions()`

Read the mechanism, not every regex symbol:

1. split text into lines;
2. find `jobs:`;
3. determine indentation of direct child jobs;
4. record where each job starts;
5. slice each job body;
6. extract its `run` commands.

The parser treats indentation as structure. Rich YAML features can defeat this shallow model, which is why unsupported shapes remain unresolved.

## `_extract_run_commands()`

It supports:

```yaml
run: pytest
```

and block commands:

```yaml
run: |
  pip install -r requirements-dev.txt
  pytest
```

The index-based loop is used because block commands consume multiple following lines.

## Installation detection

`_command_installs_source_file()`:

- splits shell command chains;
- requires a pip-install form;
- searches `-r` or `--requirement` arguments;
- normalizes path separators and leading `./`;
- compares with the exact changed source file.

It does not infer installation from an unrelated setup tool or custom script.

## Direct invocation detection

`_command_invokes_package()` recognizes bounded prefixes such as:

```text
pytest
python -m pytest
uv run pytest
poetry run pytest
coverage run -m pytest
```

It strips leading environment-variable assignments before comparison.

It does not assume `tox -e py` indirectly invokes pytest. That requires configuration tracing not implemented here.

## Important syntax to understand operationally

Named regex groups:

```python
(?P<indent>...)
```

allow code to retrieve a captured part by name.

Generator passed to `next(..., None)`:

```python
next((command for command in commands if condition), None)
```

means “return the first matching command, otherwise `None`.”

You should be able to read this. Memorization is unnecessary.

## What to master

Must master:

- exact supported subset;
- why one-job restriction exists;
- why direct install and direct invocation are both required;
- why tox, scripts, reusable workflows, and richer YAML remain unresolved;
- why evidence commands are retained.

Operationally understand:

- indentation scanning;
- regex groups;
- shell segmentation;
- generator expressions;
- path normalization.

## Matching tests

Read:

```text
test_reads_named_step_block_commands
test_reads_dash_run_block_commands
```

Then inspect `tests/test_ci_authority.py` for tox and multi-job cases, because those protect the reader's stopping boundaries.

# 4. `ci_authority.py` — what does the evidence permit us to claim?

## Input assembly

`WorkflowAuthorityInput` keeps together:

```text
one validated run
+ that run's jobs
+ that run's exact-head workflow definition evidence
```

This avoids interpreting unrelated records as one path.

## Per-workflow result

`WorkflowAuthorityAssessment` contains:

- workflow name and path;
- `sufficient`, `insufficient`, or `unresolved`;
- stable reason and human detail;
- optional commands that support or partially support the result.

## Overall result

`CIAuthorityResult` preserves every per-workflow assessment while adding an overall classification.

This prevents the overall status from hiding unresolved workflows.

## `evaluate_ci_authority()`

### No workflows

```text
no exact-head workflows
→ insufficient
```

This is insufficient because required positive CI evidence does not exist.

### Build all assessments first

```python
assessments = tuple(
    _assess_workflow(...) for workflow_input in workflow_inputs
)
```

The evaluator does not stop after the first workflow. It preserves the complete available assessment set.

### Existential sufficient rule

```python
sufficient = next(
    (item for item in assessments if item.status == "sufficient"),
    None,
)
```

If one workflow is sufficient, the overall status is sufficient.

The claim is existential:

```text
at least one successful exact-head CI path directly exercised the dependency
```

It is not universal:

```text
all workflows exercised the dependency
```

### No successful jobs

If no workflow input contains a completed successful job:

```text
overall insufficient
```

There is no successful runtime path available to establish exercise.

### Successful CI but no proof

If successful jobs exist but none meets the direct rule:

```text
overall unresolved
```

Evidence exists, but the current interpreter cannot safely prove dependency exercise.

## `_assess_workflow()`

Decision order matters:

1. unavailable definition → unresolved;
2. definition revision mismatch → unresolved;
3. unsuccessful workflow → insufficient;
4. no successful job → insufficient;
5. inspect commands;
6. command reader unresolved → unresolved;
7. otherwise sufficient.

Why does order matter?

Because the evaluator must not parse commands from unavailable or mismatched evidence, and it must distinguish failed runtime evidence from unreadable interpretation evidence.

## `assert isinstance(definition, RepositoryTextFile)`

The earlier branch already handled `UnavailableRepositoryFile`. The assertion communicates that the remaining union member must be `RepositoryTextFile`.

This is an internal type/control-flow invariant, not external evidence validation.

## What to master

Must master:

- per-workflow versus overall result;
- sufficient, insufficient, and unresolved semantics;
- existential overall sufficient rule;
- why unresolved details remain visible;
- why sufficient authority is not upgrade safety or recommendation.

Operationally understand:

- `Literal` status aliases;
- tuple comprehensions;
- `next(..., None)`;
- `any(...)` over nested generators;
- type narrowing through `isinstance` and `assert`.

## Matching tests

Read:

```text
test_sufficient_when_single_job_installs_and_invokes_dependency
test_green_tox_workflow_remains_unresolved_without_config_trace
test_multiple_jobs_remain_unresolved_to_avoid_cross_job_inference
test_no_successful_exact_head_jobs_is_insufficient
test_unavailable_workflow_definition_is_unresolved
```

For each test, write the exact status and reason you expect before reading the assertion.

# 5. Trace the live S004 result through the code

Use the observed output:

```text
pytest 9.0.2 → 9.0.3
Regression Tests → sufficient
Test + Deploy → unresolved
overall → sufficient
```

Reconstruct the path:

## `Regression Tests`

```text
GitHubActionsClient
→ exact-head successful run and successful job

GitHubRepositoryClient
→ run-specific workflow path
→ workflow text at f3cda8...

workflow_commands
→ one job
→ requirements-dev.txt installed
→ pytest directly invoked

ci_authority
→ per-workflow sufficient
```

## `Test + Deploy`

```text
successful exact-head run
→ six jobs / multiple job definitions
→ shallow rule refuses cross-job inference
→ per-workflow unresolved
```

## Overall

```text
one sufficient assessment exists
→ overall sufficient
→ unresolved second workflow is retained
```

Permitted claim:

> At least one successful exact-head CI path directly exercised pytest.

Not permitted:

- every workflow exercised pytest;
- the dependency update is safe;
- the PR should be merged;
- all relevant environments were covered.

# CI walkthrough completion check

You pass when, without notes, you can answer:

1. Why does Actions acquisition validate SHA after filtering by SHA?
2. Why do run ID, workflow ID, event, and SHA all matter?
3. Why fetch workflow text at the exact PR head?
4. Why can a workflow-file `404` be a normal unavailable result?
5. Why does the shallow command reader require exactly one job?
6. Why is tox unresolved today?
7. What makes a workflow insufficient rather than unresolved?
8. Why can overall authority be sufficient with an unresolved workflow?
9. What exact claim does S004 permit?
10. Which module should change if future work adds tox configuration tracing?

Then continue to `10-guided-test-reading-workbook.md`.