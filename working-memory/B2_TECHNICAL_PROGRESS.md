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
Install mode: editable (`python3 -m pip install -e .`)
Primary invocation: `python3 -m upgradepilot ...` or installed `upgradepilot ...`
Network scope: public GitHub REST API, read-only
Authentication used for live runs: none
```

Environment-specific facts belong here unless they become portable setup requirements. Do not treat WSL2 as a product runtime requirement merely because it is Ali's current development environment.

## Implemented path

```text
CLI repository + PR number
→ local locator validation
→ read-only PR metadata acquisition
→ transport, HTTP, JSON, and required-field validation
→ exact `PullRequestIdentity`
→ paginated changed-file acquisition
→ changed-file response and count reconciliation
→ patch-evidence classification
→ one exact pinned Python dependency extraction
→ supported result or explicit unsupported state
→ concise terminal output
```

Current source:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/github_client.py
src/upgradepilot/dependency_change.py
tests/test_github_client.py
tests/test_dependency_change.py
tests/README.md
```

## Observed execution evidence

Earlier environment synchronization failure:

```text
ModuleNotFoundError: No module named 'requests'
```

Diagnosis and repair:

- activating `.venv` selected the intended environment;
- the editable package still referenced repository source;
- the newly declared `Requests` dependency had not yet been installed in that environment;
- rerunning `python3 -m pip install -e .` synchronized package metadata and dependencies.

Observed changed-file increment validation on 2026-07-24:

```text
python3 -m unittest discover -s tests -v
→ 12 tests passed in 0.002s

python3 -m upgradepilot googlefonts/glyphsLib 1145
→ live public PR metadata acquisition succeeded
→ one changed-file record acquired and reconciled
→ requirements-dev.txt reported as modified
→ exact pinned dependency update extracted
```

Validated live S004 evidence:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Base SHA: 044f19e4b1437bfc4343592486f4e3c6040306d9
Head SHA: f3cda8a94600e58d27f1bc17c99b7693718b6350
Changed-file records: 1
Changed file: requirements-dev.txt (modified)
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
```

This proves the current read-only request-to-validated-dependency-identity path in Ali's WSL2 environment for one supported public PR. It does not prove CI authority, target relevance, upgrade safety, recommendation correctness, broader dependency syntax support, production readiness, or independent ownership.

## Current learning depth

### Must master now

- manual CLI input → PR metadata → exact proposal identity → changed-file records → patch evidence → dependency identity → output;
- local locator validity versus remote-resource existence;
- transport failure versus HTTP failure versus malformed successful response;
- why exact base and head SHAs identify the proposal being analyzed;
- why PR `changed_files` count and acquired records must reconcile before interpretation;
- pagination as completeness protection rather than only performance behavior;
- unified patch markers: context, removed line, added line, and hunk header;
- acquisition success versus unsupported extraction;
- missing patch evidence versus malformed or incomplete patch evidence;
- exact pinned `package==version` support and explicit abstention outside that boundary;
- what mocked deterministic tests prove versus what a live request proves.

### Understand operationally

- `argparse` command construction;
- editable installation behavior;
- `dataclass(frozen=True, slots=True)` meaning;
- dependency injection through an optional Requests session;
- `unittest.mock` page simulation;
- current regular-expression and type-alias syntax;
- Python distribution-name normalization using runs of `.`, `_`, and `-` as equivalent separators.

### Deferred deliberately

- broad requirements-file parsing, extras, markers, URLs, editable installs, and arbitrary constraints;
- full diff parsing and Git internals;
- exact-head workflow/check acquisition and CI authority interpretation until ownership closure;
- Pydantic until validation complexity creates a concrete need;
- retry/backoff and broader rate-limit recovery until acquisition robustness work;
- async HTTP and HTTP/2;
- TLS, DNS, and connection-pool internals;
- persistent storage, services, queues, agents, models, and deployment infrastructure.

### Ownership evidence so far

Ali has:

- selected and corrected the real-flow-first route;
- correctly explained ambiguous `404`, timeout, incomplete evidence, and unsupported extraction states;
- predicted pagination stopping and count-reconciliation behavior;
- distinguished valid changed-file acquisition from absent patch evidence;
- explained the request-to-metadata-to-changed-file-to-extraction mental model;
- installed and executed the changed-file increment in WSL2;
- produced the full passing deterministic and live outputs.

The current source remains substantially AI-authored. The remaining ownership gate for this increment is one Ali-authored central test or rule modification, its predicted result, successful rerun, and explanation of the protected boundary.

## Immediate technical action

Ali adds one deterministic test for the normalized-package identity rule:

```text
removed: demo.package==1.0.0
added:   demo_package==1.1.0
expected: supported change for normalized package demo-package
```

Then:

1. predict the result and why it should be supported;
2. implement the test in `tests/test_dependency_change.py`;
3. run the full deterministic suite;
4. explain what failure would localize if the test did not pass;
5. only after review proceed to exact-head GitHub Actions workflow/check evidence.

The current proof and checklist are owned by `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`.
