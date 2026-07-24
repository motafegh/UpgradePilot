# 04 — SMART Study Sessions and Ownership Check

## Purpose

Use this as the execution guide for the two bounded study sessions in this snapshot. The goal is not to finish pages or memorize generated code. The goal is to demonstrate enough control of the current responsibility to make and explain the next central test yourself.

## Session ceilings

- **Session A — system and source ownership:** 60–75 focused minutes.
- **Session B — tests, diagnosis, and ownership:** 45–60 focused minutes.

Time is a pacing constraint, not the pass condition. Stop earlier when every required proof is clear. Do not force both sessions into one sitting when attention or accuracy drops.

## SMART target

By the end of both sessions, produce four observable outputs:

1. one closed-book request-to-result flow;
2. one failure-classification table;
3. one function-level code trace;
4. one predicted and authored normalized-package test.

These outputs are specific to the current B2 source baseline and directly prepare the remaining ownership gate.

# Session A — System and source ownership

## Block 1 — Reconstruct the system flow

**Suggested ceiling:** 15–20 minutes  
**Read:** `README.md` and `01-request-to-evidence-flow.md`

Close the files and write:

```text
input
→ ...
→ supported or unsupported dependency result
```

Your flow should contain, in correct order:

- local input validation;
- PR metadata acquisition;
- exact base/head identity;
- changed-file pagination;
- file-record validation;
- count reconciliation;
- patch classification;
- pinned extraction;
- output.

### Pass condition

You can explain why these are three different outcomes:

```text
request timeout
metadata/file-count disagreement
valid file record with absent patch
```

Expected classification:

```text
acquisition failure
evidence-consistency failure
unsupported extraction due to missing patch evidence
```

## Block 2 — Trace the central code

**Suggested ceiling:** 35–45 minutes  
**Read:** `02-code-you-must-own.md` and the pinned source baseline

Use:

```bash
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:src/upgradepilot/cli.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:src/upgradepilot/github_client.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:src/upgradepilot/dependency_change.py
```

Write one responsibility sentence for each:

```text
cli.main
GitHubReadClient.get_pull_request
GitHubReadClient.get_changed_files
extract_pinned_dependency_change
normalize_package_name
```

Then identify where these invariants are protected:

- successful HTTP is not enough;
- all changed-file records must be acquired;
- patch evidence must be complete enough;
- package names must identify the same normalized distribution;
- unsupported analysis must not become an acquisition exception.

### Pass condition

You can point to the owning function for each invariant without searching the whole repository.

### Session A stop check

Stop Session A when you can reconstruct the flow and trace the five central functions. Do not continue merely to consume time. If either output is weak, repeat only the failed portion before Session B.

# Session B — Tests, diagnosis, and ownership

## Block 3 — Read tests as executable claims

**Suggested ceiling:** 20–25 minutes  
**Read:** `03-tests-and-failure-diagnosis.md` and both pinned test files

Use:

```bash
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:tests/test_github_client.py
git show 0ea16d0fbc51312fc70ac6a257e3c97550baeacc:tests/test_dependency_change.py
```

Choose four tests:

- one identity test;
- one pagination/completeness test;
- one supported extraction test;
- one unsupported extraction test.

For each, state:

```text
protected invariant
source owner
what the test does not prove
```

### Pass condition

You do not describe a test as proving “the feature works.” You name its bounded claim and limitation.

## Block 4 — Ownership exercise

**Suggested ceiling:** 25–35 minutes

### Predict before editing

Patch:

```diff
-demo.package==1.0.0
+demo_package==1.1.0
```

Prediction:

```text
result type: PinnedDependencyChange
normalized package: demo-package
old version: 1.0.0
proposed version: 1.1.0
```

Why:

```text
runs of '.', '_', and '-'
→ normalized to '-'
→ lowercase comparison
```

### Author the test

Add one test to:

```text
tests/test_dependency_change.py
```

Suggested name:

```python
def test_equivalent_normalized_package_names_are_supported(self) -> None:
```

Required assertions:

- result is `PinnedDependencyChange`;
- `normalized_package == "demo-package"`;
- `old_version == "1.0.0"`;
- `proposed_version == "1.1.0"`.

Use the existing `_record` helper and existing supported-result test as patterns. Write the test yourself rather than copying a completed solution.

### Run proof

```bash
python3 -m unittest discover -s tests -v
git diff -- tests/test_dependency_change.py
```

### Diagnose before repairing

If the test fails, classify the failure before editing source:

| Observed result | First hypothesis |
|---|---|
| `package_mismatch` | package normalization is wrong or not applied consistently |
| `no_supported_pinned_change` | pinned requirement grammar rejected one spelling |
| supported result with wrong normalized name | result construction or normalization output is wrong |
| unrelated error | test arrangement, import, or environment problem |

### Ownership pass condition

You can explain:

1. why the two raw names are different strings;
2. why they identify the same normalized package under the current rule;
3. why this test protects a real dependency-identity boundary;
4. which source function owns the behavior;
5. what the passing test still does not prove.

## Closed-book final check

Answer without notes:

1. Why does UpgradePilot acquire PR metadata before changed files?
2. Why is the head SHA part of evidence identity?
3. Why must changed-file count reconciliation happen before extraction?
4. Why is `patch=None` not a transport failure?
5. Why is `pytest>=9.0.2` unsupported rather than invalid Python syntax?
6. Why does the extractor return a result union instead of raising for every unsupported case?
7. What is the difference between a mocked pagination test and the live S004 run?
8. Which code boundary would you inspect for equivalent package names?

## Honest depth labels after the sessions

Use the strongest label actually supported:

- **Introduced:** you recognize the terms and broad flow.
- **Operationally understood with guidance:** you can trace and classify with the notes available.
- **Ownership practice:** you authored the test, predicted the result, interpreted execution, and explained the boundary.
- **Independently controlled:** not established by these sessions.

The expected realistic outcome is **ownership practice for one normalized-package test boundary**, not broad Python, HTTP, GitHub API, or dependency-analysis mastery.

## Stop line

Do not begin CI acquisition, upstream evidence, recommendation logic, replay infrastructure, persistence, or broader dependency grammar during these study sessions.

After the ownership test passes and is reviewed, return to the active B2 plan for exact-head GitHub Actions evidence.