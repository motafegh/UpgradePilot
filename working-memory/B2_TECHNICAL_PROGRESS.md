# B2 Technical Progress

**Status:** Living technical evidence; non-controlling  
**Current plan:** [`../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Update rule:** Change only when implementation evidence, environment state, learning depth, failure diagnosis, or the immediate technical action materially changes.

## Current environment

Observed in Ali's development environment on 2026-07-24:

```text
Platform: WSL2 / Linux shell
Repository: ~/projects/UpgradePilot
Python: 3.12
Virtual environment: .venv
Install mode: editable (`python -m pip install -e .`)
Primary invocation: `python -m upgradepilot ...` or installed `upgradepilot ...`
Network scope: public GitHub REST API, read-only
Authentication used for first live run: none
```

Environment-specific facts belong here unless they become portable setup requirements. Do not treat WSL2 as a product runtime requirement merely because it is Ali's current development environment.

## Implemented path

```text
CLI repository + PR number
→ local locator validation
→ `GitHubReadClient`
→ read-only GitHub pull-request request
→ timeout/transport and HTTP handling
→ JSON-object and required-field validation
→ `PullRequestIdentity`
→ concise terminal output
```

Current source:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/github_client.py
tests/test_github_client.py
```

## Observed execution evidence

Initial command after activating the existing virtual environment failed with:

```text
ModuleNotFoundError: No module named 'requests'
```

Diagnosis:

- activating `.venv` selected that environment;
- the editable UpgradePilot package still pointed to the repository source;
- the newly declared `Requests` dependency had not been installed into the environment;
- rerunning `python -m pip install -e .` synchronized package metadata and dependencies.

Observed successful validation:

```text
python -m unittest discover -s tests -v
→ 2 tests passed

python -m upgradepilot googlefonts/glyphsLib 1145
→ live public request succeeded
→ exact base/head identity and changed-file count printed
```

Validated S004 identity:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Base SHA: 044f19e4b1437bfc4343592486f4e3c6040306d9
Head SHA: f3cda8a94600e58d27f1bc17c99b7693718b6350
Changed files: 1
```

This proves the first live request-to-validated-identity path in Ali's WSL2 environment. It does not prove dependency extraction, CI authority, recommendation correctness, production readiness, or independent ownership.

## Current learning depth

### Must master now

- CLI input → client → HTTP response → validated identity → output execution path;
- local validation versus remote-resource existence;
- transport failure versus HTTP failure versus malformed successful response;
- explicit connect/read timeouts;
- optional token handling through an environment variable;
- external JSON as untrusted data;
- why exact base and head SHAs identify the proposal being analyzed;
- what mocked tests prove versus what a live request proves.

### Understand operationally

- `argparse` command construction;
- editable installation behavior;
- `dataclass(frozen=True, slots=True)` meaning;
- dependency injection through an optional Requests session;
- basic `unittest.mock` usage;
- current regular-expression and type-hint syntax.

### Deferred deliberately

- Pydantic until validation complexity creates a concrete need;
- retry/backoff and broader rate-limit recovery until acquisition robustness work;
- async HTTP and HTTP/2;
- TLS, DNS, and connection-pool internals;
- persistent storage, services, queues, agents, models, and deployment infrastructure.

### Ownership evidence so far

Ali has:

- selected the real-flow-first learning path;
- correctly explained ambiguous `404`, timeout, and insufficient-evidence behavior;
- authorized and executed the first increment;
- diagnosed the missing dependency after inspecting the actual failure;
- challenged whether every source line needs equal learning depth;
- required explicit post-run learning and ownership review.

The source remains substantially AI-authored. Ownership must continue through central explanation, modification, meaningful tests, and diagnosis.

## Immediate technical action

Learn the minimum complete model for GitHub changed-file pagination and patch semantics, then implement:

```text
PullRequestIdentity
→ validated changed-file records
→ one exact pinned dependency update
→ explicit unsupported result for other shapes
```

The current proof and checklist are owned by `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`.
