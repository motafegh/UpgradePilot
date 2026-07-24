# 02 — Module Map and Call Flow

## SMART objective

Within 30–40 minutes, explain the responsibility of every active module, trace one CLI request across them, and identify the correct module for five hypothetical changes.

## The architectural rule

UpgradePilot separates code by **engineering responsibility**, not by every tiny action or every GitHub endpoint.

Good separation:

```text
shared transport
PR/file acquisition
dependency interpretation
Actions acquisition
repository-file acquisition
workflow command reading
CI-authority interpretation
CLI orchestration
```

Bad fragmentation:

```text
get_run.py
get_job.py
parse_job.py
validate_job.py
print_job.py
```

The first makes the product flow readable. The second makes one concept harder to follow across many files.

## Active module map

### `github_api.py`

**Owns:** shared read-only GitHub HTTP and JSON trust handling.

Responsibilities:

- common request headers;
- optional authentication token;
- connect/read timeout;
- HTTP status classification;
- JSON decoding;
- top-level object/array checks;
- reusable required-field validators.

Does not know what a Pull Request, workflow, job, or dependency means.

Why: transport behavior should be consistent across focused GitHub clients without turning one file into a giant domain client.

### `github_client.py`

**Owns:** public Pull Request identity and changed-file acquisition.

Produces:

- `PullRequestIdentity`;
- `ChangedFile` records.

Central invariants:

- requested PR number equals returned PR number;
- exact base and head SHAs are preserved;
- every changed-file page is acquired;
- acquired record count equals PR metadata count.

### `dependency_change.py`

**Owns:** deterministic interpretation of validated patch evidence.

Produces either:

- `PinnedDependencyChange`; or
- `UnsupportedDependencyChange`.

It performs no network I/O.

Why: external acquisition failure must remain distinguishable from valid evidence that is outside the supported dependency grammar.

### `github_actions.py`

**Owns:** exact-head GitHub Actions run, job, and step-summary acquisition.

Produces:

- `WorkflowRun`;
- `WorkflowJob`;
- `WorkflowStep`.

Central invariants:

- workflow event is `pull_request`;
- run head SHA equals frozen PR head SHA;
- job run ID equals requested run ID;
- job head SHA equals frozen PR head SHA;
- pagination totals remain stable and complete.

It answers **what ran**, not what the run proves.

### `github_repository.py`

**Owns:** exact-run workflow path resolution and exact-head repository text acquisition.

Produces either:

- `RepositoryTextFile`; or
- `UnavailableRepositoryFile`.

Why this is separate from `github_actions.py`:

- Actions resources tell us about executions;
- repository contents tell us about definitions;
- both must be linked, but they have different endpoints, response shapes, and failure meanings.

### `workflow_commands.py`

**Owns:** bounded static reading of job and `run` command text from a workflow definition.

It is intentionally not a complete YAML parser.

Current supported shape:

- ordinary `jobs:` mapping;
- one statically identifiable job for sufficient authority;
- inline or block `run` commands;
- pip requirement flags;
- direct package or Python-module invocation.

Richer forms become unresolved.

### `ci_authority.py`

**Owns:** deterministic classification of what exact-head CI evidence proves.

Produces:

- overall `CIAuthorityResult`;
- per-workflow `WorkflowAuthorityAssessment`.

Possible states:

- `sufficient`;
- `insufficient`;
- `unresolved`.

It does not decide upgrade safety or maintainer action.

### `cli.py`

**Owns:** user-facing orchestration and presentation.

Responsibilities:

- parse repository and PR number;
- create focused clients;
- execute stages in the correct order;
- activate later stages only when earlier evidence permits;
- map failures to exit statuses;
- print factual and interpreted evidence transparently.

It should not contain domain parsing rules that belong in focused modules.

## Main call flow

```text
cli.main()
│
├─ GitHubReadClient.get_pull_request()
│  └─ PullRequestIdentity
│
├─ GitHubReadClient.get_changed_files()
│  └─ tuple[ChangedFile, ...]
│
├─ extract_pinned_dependency_change()
│  └─ PinnedDependencyChange or UnsupportedDependencyChange
│
└─ only when supported:
   ├─ GitHubActionsClient.get_exact_head_workflow_runs()
   │  └─ tuple[WorkflowRun, ...]
   │
   ├─ GitHubActionsClient.get_workflow_jobs()
   │  └─ tuple[WorkflowJob, ...]
   │
   ├─ GitHubRepositoryClient.get_workflow_definition()
   │  └─ RepositoryTextFile or UnavailableRepositoryFile
   │
   └─ evaluate_ci_authority()
      └─ CIAuthorityResult
```

## Why the order matters

Wrong order:

```text
acquire every possible CI and repository file
→ later discover dependency change is unsupported
```

Problems:

- unnecessary network requests;
- larger failure surface;
- harder reasoning;
- evidence collected without a defined interpretation target.

Current order:

```text
establish exact dependency identity first
→ conditionally acquire only relevant CI evidence
```

This is conditional-stage activation: later work starts only when earlier evidence establishes a reason to start it.

## Data records as contracts

The immutable dataclasses are handoff contracts between stages.

Example:

```text
untrusted PR JSON
→ validated PullRequestIdentity
→ later modules consume identity rather than raw JSON
```

Benefits:

- fewer repeated type checks;
- stable field names;
- easier tests;
- accidental mutation is prevented;
- clear boundary between untrusted external data and trusted internal records.

“Trusted” here means validated against current rules, not universally true or permanently correct.

## Where should a change go?

### Add retry/backoff for GitHub requests

Owner: `github_api.py`.

Reason: retry behavior concerns transport, not one domain resource.

### Support Poetry lockfile dependency changes

Owner: `dependency_change.py`, possibly with a new focused parser if justified.

Reason: this changes dependency interpretation, not GitHub acquisition.

### Acquire check suites from another GitHub endpoint

Owner: likely `github_actions.py` or a new focused check-acquisition module if responsibilities diverge materially.

### Trace `tox -e py` into `tox.ini`

Owner: new or extended configuration-tracing interpretation, not `github_actions.py`.

Reason: the run is already acquired; the missing work is understanding indirect command meaning.

### Change terminal wording

Owner: `cli.py`, unless the change alters a domain result or machine contract.

## What you must master

- why each module exists;
- the output contract of each stage;
- why raw JSON does not cross the acquisition boundary;
- why acquisition and interpretation are separate;
- why the CLI orchestrates but does not own every rule;
- where a new behavior belongs.

## Operationally understand

- import syntax;
- constructor calls for focused clients;
- tuple comprehensions and loops used to gather evidence;
- type annotations that describe records and unions.

## Active-recall exercise

Without looking, assign each change to a module:

1. GitHub returns invalid base64 text.
2. A patch contains two exact pinned dependency updates.
3. A workflow job belongs to a different head SHA.
4. A workflow invokes a shell script that later runs pytest.
5. CLI needs JSON output.

Expected ownership:

1. `github_repository.py` or shared decoding helper at that boundary.
2. `dependency_change.py`.
3. `github_actions.py`.
4. future indirect configuration/script tracing.
5. `cli.py` plus a stable machine-output representation if introduced.

## Completion evidence

This file is mastered when you can recreate the module map and correctly place a new responsibility without choosing a file merely because its name looks related.