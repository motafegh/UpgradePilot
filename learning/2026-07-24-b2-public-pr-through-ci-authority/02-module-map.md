# 02 — Module Map

## SMART objective

In 25–35 minutes, explain every active module in one sentence, trace one CLI request across them, and correctly place four hypothetical changes.

## Separation rule

Split by meaningful engineering responsibility, not by every API call.

```text
shared transport
PR/file acquisition
dependency interpretation
Actions acquisition
repository-definition acquisition
workflow command reading
CI-authority interpretation
CLI orchestration
```

## Modules

### `github_api.py`

Shared read-only GitHub HTTP/JSON trust boundary:

- headers and optional token;
- timeout;
- HTTP error classification;
- JSON and top-level shape validation;
- reusable required-field helpers.

It must remain unaware of PRs, workflows, dependencies, and authority.

### `github_client.py`

Acquires and validates:

- `PullRequestIdentity`;
- all `ChangedFile` records.

Key rules: exact PR identity, base/head SHA preservation, complete pagination, changed-file count reconciliation.

### `dependency_change.py`

Interprets validated patches without network I/O.

Returns:

- `PinnedDependencyChange`; or
- `UnsupportedDependencyChange`.

Acquisition success and supported interpretation remain different states.

### `github_actions.py`

Acquires exact-head:

- `WorkflowRun`;
- `WorkflowJob`;
- `WorkflowStep` summaries.

It answers **what ran**, not what the run proves.

### `github_repository.py`

Links an exact workflow run to:

- its workflow path;
- workflow file content at the same PR head SHA.

Execution evidence and repository-definition evidence use different GitHub resources, so they are separate responsibilities.

### `workflow_commands.py`

Reads a deliberately narrow subset of workflow command structure:

- ordinary `jobs:` mapping;
- inline/block `run:` commands;
- pip requirements-file installation;
- direct package/module invocation.

Richer forms become unresolved; this is not a complete YAML parser.

### `ci_authority.py`

Classifies exact-head CI evidence as:

- `sufficient`;
- `insufficient`;
- `unresolved`.

It does not decide upgrade safety or maintainer action.

### `cli.py`

Owns:

- input parsing;
- execution order;
- conditional activation of later stages;
- exit-code mapping;
- transparent human output.

It orchestrates domain modules rather than absorbing their rules.

## Main call flow

```text
cli.main()
├─ GitHubReadClient.get_pull_request()
├─ GitHubReadClient.get_changed_files()
├─ extract_pinned_dependency_change()
└─ when supported:
   ├─ GitHubActionsClient.get_exact_head_workflow_runs()
   ├─ GitHubActionsClient.get_workflow_jobs()
   ├─ GitHubRepositoryClient.get_workflow_definition()
   └─ evaluate_ci_authority()
```

Later network work activates only after a supported dependency identity exists. This avoids requests without an interpretation target.

## Records as handoff contracts

```text
untrusted JSON
→ runtime validation
→ immutable dataclass
→ downstream module
```

`frozen=True` prevents normal field reassignment. `slots=True` fixes the expected attribute set. These controls reduce accidental mutation; they do not make external evidence universally true.

## Where should a change go?

- Retry/backoff policy → `github_api.py`.
- Poetry/lockfile interpretation → `dependency_change.py` or a justified new parser.
- Trace `tox -e py` into configuration → future indirect configuration tracing, not Actions acquisition.
- Add machine-readable CLI output → `cli.py` plus a stable result representation if needed.

## Must master

- why each module exists;
- its input/output contract;
- why raw JSON does not cross acquisition boundaries;
- why acquisition and interpretation are separate;
- where a new responsibility belongs.

## Operationally understand

- relative imports;
- constructing focused clients;
- tuples and loops gathering evidence;
- type annotations describing records/results.

## Active recall

Write one sentence for each active module without looking. Then answer:

1. Why does `github_actions.py` not classify authority?
2. Why does `github_repository.py` exist separately?
3. Where would tox tracing belong?
4. What should remain in `cli.py`?

## Pass condition

Recreate the module map and place all four hypothetical changes correctly with reasoning.