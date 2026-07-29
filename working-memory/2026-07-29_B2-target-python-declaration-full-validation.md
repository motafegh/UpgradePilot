# B2 Target Python Declaration — Full Validation Evidence

**Date:** 2026-07-29  
**Validated repository revision:** `75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15`  
**Scope:** `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`, Step 1 only

## Validation purpose

Close the remaining validation gap for:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

This validation does not authorize or establish Python version-range evaluation, upstream support-drop extraction, target relevance, compatibility, safety, evidence sufficiency, or a maintainer action.

## Repository test suite

Command:

```bash
python -m unittest discover -s tests -v
```

Result:

```text
----------------------------------------------------------------------
Ran 72 tests in 0.022s

OK
```

This supersedes the previous controlled-reconstruction-only result for Step 1. The complete deterministic repository suite passed at the validated revision.

## Initial live-command authentication failure

Command:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

Initial result:

```text
Acquisition failed.
Reason: http_error
Detail: GitHub returned HTTP 401 while acquiring pull-request evidence.
HTTP status: 401
```

Network reachability was independently present. The failure was caused by a stale or invalid `GITHUB_TOKEN` environment value. UpgradePilot correctly used a configured non-empty token as a Bearer credential; GitHub rejected that credential.

The token value was not printed or recorded.

## Successful anonymous public command

Commands:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Result:

```text
UpgradePilot public pull-request evidence
Repository: googlefonts/glyphsLib
PR: 1145
Title: Bump pytest from 9.0.2 to 9.0.3
Author: dependabot[bot]
State: closed
Merged: true
Base: main @ 044f19e4b1437bfc4343592486f4e3c6040306d9
Head: dependabot/pip/pytest-9.0.3 @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Changed-file records: 1
Changed file: requirements-dev.txt (modified)
Dependency change: supported
Source file: requirements-dev.txt
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
Target Python declaration: project_table_absent
Target Python source: pyproject.toml @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Target Python blob SHA: 38d6a9efc4b94e2b733d3bbb848156449814ec94
Target Python detail: pyproject.toml did not contain a [project] table.
Exact-head workflow runs: 2
Workflow: Regression Tests | status=completed | conclusion=success | jobs=1
  Job: test | status=completed | conclusion=success | steps=12
Workflow: Test + Deploy | status=completed | conclusion=success | jobs=6
  Job: test (3.14, ubuntu-latest) | status=completed | conclusion=success | steps=10
  Job: test (3.10, windows-latest) | status=completed | conclusion=success | steps=10
  Job: lint | status=completed | conclusion=success | steps=8
  Job: test (3.10, ubuntu-latest) | status=completed | conclusion=success | steps=10
  Job: test (3.14, windows-latest) | status=completed | conclusion=success | steps=10
  Job: deploy | status=completed | conclusion=skipped | steps=0
CI authority: sufficient
CI authority reason: exact_head_dependency_exercised
CI authority detail: Workflow 'Regression Tests' installed 'requirements-dev.txt' and directly invoked 'pytest' in successful exact-head CI.
  Authority workflow: Regression Tests | status=sufficient | reason=source_installed_and_dependency_invoked
    Install evidence: python -m pip install --upgrade pip
python3 -m venv generate
. ./generate/bin/activate && pip install -r requirements.txt -r requirements-dev.txt
    Execution evidence: . ./regression/bin/activate && pytest --run-regression-tests tests/regression_test.py -n auto
  Authority workflow: Test + Deploy | status=unresolved | reason=multiple_or_zero_workflow_jobs
Package evidence: available
Published package: pytest==9.0.3
Distribution files: 2
Upstream source: available
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Provenance unavailable files: none
Accepted tag: 9.0.3
Release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

## Validation conclusions

The complete installed command confirmed:

1. the target file was requested and reported at the immutable PR head SHA;
2. the exact file blob identity was retained;
3. valid TOML without a PEP 621 `[project]` table produced `project_table_absent`;
4. no Python range comparison occurred;
5. no compatibility, safety, or maintainer-action claim was introduced;
6. existing PR, dependency, CI-authority, package, provenance, and upstream-release output remained intact;
7. an unresolved workflow-authority path remained visible beside the sufficient path rather than being erased;
8. the upstream semantic state remained `unresolved_claim`.

## Authentication observation

For a public-repository read-only command, an invalid configured token is worse than no token because GitHub returns HTTP 401 instead of allowing anonymous access. The immediate safe operational workaround is scoped token removal:

```bash
env -u GITHUB_TOKEN upgradepilot googlefonts/glyphsLib 1145
```

or current-shell removal:

```bash
unset GITHUB_TOKEN
```

This evidence does not authorize changing the token-loading contract. Any product change to authentication diagnostics or fallback behavior requires a separately selected responsibility and security review; silently retrying without a rejected credential could mask credential problems.

## Step 1 closure

Step 1 is fully behavior-validated at revision `75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15` through:

- the complete 72-test deterministic suite;
- one complete installed public read-only command;
- independent inspection of target, CI, package, and upstream output.

The next authorized activity is to present and review deterministic Python specifier-range method alternatives. No range evaluator, upstream support-drop adapter, prompt tuning, model integration, relevance policy, or new runtime dependency is implemented by this record.
