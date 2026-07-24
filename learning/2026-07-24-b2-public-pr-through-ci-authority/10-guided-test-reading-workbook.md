# 10 — Guided Test Reading and Diagnosis Workbook

## Purpose

Source files explain implementation. Tests define the behavior the project currently promises.

Study these files beside this workbook:

```text
tests/test_github_client.py
tests/test_dependency_change.py
tests/test_github_actions.py
tests/test_github_repository.py
tests/test_workflow_commands.py
tests/test_ci_authority.py
```

The goal is to predict a test's claim, identify its protected invariant, and localize a failure. Memorizing `unittest` or mock syntax is not required.

# 1. Read every test as Arrange → Act → Assert → Claim

For each test, complete:

```text
Test name:
Arrange — controlled input and dependencies:
Act — function or method called:
Assert — observable required result:
Claim — engineering invariant protected:
First module implicated by failure:
What this test does not prove:
```

The final question prevents overclaiming. A mocked test does not prove live GitHub behavior, broad format support, upgrade safety, or production readiness.

# 2. Understand the mock mechanism operationally

Typical pattern:

```python
session = Mock()
session.get.return_value = _response(payload)
client = GitHubReadClient(session=session)
```

Mental model:

```text
production client accepts a Session-like dependency
→ test injects a controlled substitute
→ no live request occurs
→ the response or failure can be chosen precisely
```

For pagination:

```python
session.get.side_effect = [first_page, second_page]
```

Consecutive calls receive consecutive responses.

Must master:

- why the dependency is injected;
- what behavior the payload controls;
- why one test should vary one meaningful condition.

Operationally understand:

- `Mock`;
- `return_value`;
- `side_effect`;
- `call_args` and `call_args_list`.

# 3. `test_github_client.py`

## Exact PR identity

Read `test_get_pull_request_builds_exact_identity`.

Expected claim:

```text
valid PR JSON
→ exact immutable identity
→ requested number, base/head SHAs, and changed-file count preserved
```

Question: what unsafe evidence mixing could occur if the returned PR number were not compared with the requested number?

## Ambiguous `404`

Read `test_404_preserves_nonexistence_or_access_ambiguity`.

Expected:

```text
GitHub 404
→ GitHubAcquisitionError
→ reason == "not_found_or_inaccessible"
```

The response does not prove whether the resource is absent or private/inaccessible.

## Changed-file pagination

Read `test_get_changed_files_acquires_all_pages`.

Before reading assertions, predict:

- number of HTTP calls;
- page values;
- final record count.

Protected invariant:

```text
the first successful page is not assumed complete
```

## Count disagreement

Read `test_get_changed_files_rejects_count_disagreement`.

This is a `GitHubResponseError`, not an unsupported dependency result, because a complete changed-file evidence set was never established.

# 4. `test_dependency_change.py`

These tests begin after acquisition by constructing validated `ChangedFile` records directly.

## Supported exact pin

Read `test_extracts_supported_exact_pinned_change`.

Predict before reading assertions:

```text
source_file
package
normalized_package
old_version
proposed_version
```

## Missing patch

Read `test_missing_patch_is_explicitly_unsupported`.

This is a normal result because the file record can be valid while interpretation evidence is insufficient.

## Incomplete patch

Read `test_patch_count_disagreement_is_incomplete_evidence`.

Protected invariant:

```text
visible patch additions/deletions agree with GitHub's per-file totals
```

## Ambiguity

Read `test_multiple_pinned_changes_are_ambiguous`.

The extractor must not select the first candidate. A wrong dependency identity would contaminate every later lookup.

## Range and package mismatch

Read:

```text
test_range_change_is_outside_exact_pin_support
test_different_package_names_are_unsupported
```

For each, explain why the result is unsupported rather than guessed.

# 5. `test_github_actions.py`

## Exact-head acquisition

Read `test_acquires_runs_for_exact_head_and_event`.

Inspect both:

- the query parameters sent;
- the validated returned record.

Server filtering narrows acquisition. Local checks establish trust.

## Empty result

Read `test_empty_exact_head_result_is_explicit_not_successful_ci`.

An empty tuple is valid evidence of no matching runs. It must not become successful CI.

## Wrong revision

Read:

```text
test_rejects_run_for_different_head
test_rejects_job_for_different_head
```

Both represent contradictory successful responses and therefore raise `GitHubResponseError`.

## Pagination and jobs

Read:

```text
test_acquires_all_workflow_run_pages
test_acquires_jobs_and_step_summaries_for_run
```

Distinguish:

```text
run/job identity and outcomes
versus
step names and outcomes
versus
actual workflow commands
```

These tests do not prove dependency exercise.

# 6. `test_github_repository.py`

## Exact-head workflow text

Read `test_resolves_workflow_path_and_decodes_exact_head_text`.

Trace:

```text
run detail request
→ exact workflow path
→ contents request with ref=head_sha
→ base64 decoding
→ RepositoryTextFile
```

Protected invariant:

```text
the interpreted workflow definition belongs to the same run and revision
```

## Identity mismatch

Read `test_rejects_workflow_run_detail_identity_mismatch`.

Production checks:

- run ID;
- workflow ID;
- event;
- head SHA.

One contradiction is enough to reject the response.

## Unavailable file

Read `test_ambiguous_404_becomes_explicit_unavailable_file`.

Only the bounded ambiguous `404` becomes `UnavailableRepositoryFile`. Timeout, rate limit, and malformed payloads still raise acquisition or response errors.

# 7. `test_workflow_commands.py`

Read:

```text
test_reads_named_step_block_commands
test_reads_dash_run_block_commands
```

For each identify:

- workflow text shape;
- extracted job count;
- install command;
- execution command;
- final status and reason.

These tests prove two supported surface shapes. They do not establish complete YAML support.

Deferred shapes include reusable workflows, anchors, custom actions, scripts, and complex expressions.

# 8. `test_ci_authority.py`

Before reading each assertion, predict:

```text
status:
reason:
why:
```

## Direct evidence

`test_sufficient_when_single_job_installs_and_invokes_dependency`

Expected: sufficient, because one successful exact-head workflow directly installs the changed source file and invokes the package.

## Tox indirection

`test_green_tox_workflow_remains_unresolved_without_config_trace`

Expected: unresolved. Green is an outcome; the current evidence does not expose the indirect command path.

## Multiple jobs

`test_multiple_jobs_remain_unresolved_to_avoid_cross_job_inference`

Protected invariant:

```text
do not combine commands from separate runtime environments into one fictional path
```

## No successful jobs

`test_no_successful_exact_head_jobs_is_insufficient`

Expected: insufficient because the required successful execution evidence does not exist.

## Definition unavailable

`test_unavailable_workflow_definition_is_unresolved`

Expected: unresolved because runtime evidence may exist, but commands cannot be established.

# 9. Failure-localization drill

| Symptom | First responsible boundary |
|---|---|
| Repository locator rejected before request | `github_client.py` input validation |
| Timeout | `github_api.py` acquisition |
| `200` returns wrong top-level shape | `github_api.py` JSON shape validation |
| Returned PR number differs | `github_client.py` PR identity |
| Changed-file count differs | `github_client.py` completeness |
| Patch absent | `dependency_change.py` unsupported result |
| Two exact-pin pairs | `dependency_change.py` ambiguity |
| Workflow run wrong SHA | `github_actions.py` identity |
| Run detail wrong workflow ID | `github_repository.py` identity |
| Workflow has multiple jobs | `workflow_commands.py` unresolved boundary |
| No successful exact-head jobs | `ci_authority.py` insufficient classification |
| One sufficient and one unresolved workflow | `ci_authority.py` overall aggregation |

Complete the table without source. Open only the module where your answer was uncertain.

# 10. Ownership test

Before editing, write:

```text
Change:
Expected result type:
Expected normalized package:
Protected invariant:
Failure would localize to:
Production code should change: yes/no and why
```

Add one test for:

```text
demo.package==1.0.0
→ demo_package==1.1.0
```

Expected observable result:

```text
PinnedDependencyChange
normalized_package == "demo-package"
```

Run:

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
Invariant protected:
What this passing test still does not prove:
```

# Completion gate

You pass when you can:

- identify Arrange, Act, Assert, and Claim in one test from each test module;
- distinguish mocked proof from live proof;
- predict CI-authority statuses before reading assertions;
- localize every failure in the table;
- add the normalized-package test after a written prediction;
- explain why one passing test increases bounded ownership but not mastery of the entire codebase.