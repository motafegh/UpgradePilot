# 04 — SMART Study Sessions and Ownership Check

## Purpose

Use this as the execution guide for the two bounded study sessions in this snapshot. The goal is not to finish pages, memorize generated code, or repeat design claims. The goal is to demonstrate enough control of the current responsibility to explain the mechanism, defend the choice, challenge an alternative, and make the next central test yourself.

## Session ceilings

- **Session A — system, rationale, and source ownership:** 75–90 focused minutes.
- **Session B — tests, diagnosis, and ownership:** 45–60 focused minutes.

Time is a pacing constraint, not the pass condition. Stop earlier when every required proof is clear. Do not force both sessions into one sitting when attention or accuracy drops.

## SMART target

By the end of both sessions, produce five observable outputs:

1. one closed-book request-to-result flow;
2. one five-row design-decision table;
3. one function-level code trace;
4. one failure-classification map;
5. one predicted and authored normalized-package test.

These outputs are specific to the current B2 source baseline and directly prepare the remaining ownership gate.

# Session A — System, rationale, and source ownership

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

A classification without a reason is incomplete. Explain what the program genuinely knows in each case and why the next stage must or must not run.

## Block 2 — Defend the important design choices

**Suggested ceiling:** 20–25 minutes  
**Read:** selected cards from `05-design-reasoning-and-tradeoffs.md`

Do not read every card. Select five that map directly to the current source trace. Recommended set:

1. acquire PR metadata before changed files;
2. bind evidence to base/head SHAs;
3. paginate and reconcile the final file count;
4. separate acquisition from extraction;
5. return unsupported as data rather than an exception.

For each, complete one row:

| Decision | Why selected | Failure prevented | Rejected alternative | Remaining cost | Revisit trigger |
|---|---|---|---|---|---|

### Reasoning standard

A weak answer:

> We separate acquisition and extraction because they are in different files.

A passing answer:

> Acquisition validates external evidence and can fail because of transport, HTTP, schema, or completeness problems. Extraction interprets already validated records and may normally abstain when syntax is unsupported. Combining them would mix failure meanings and make deterministic extraction tests harder. The cost is more explicit hand-off types, but that is justified while these responsibilities remain distinct.

### Pass condition

For all five decisions, you can state:

```text
responsibility
→ chosen mechanism
→ failure prevented
→ alternative rejected
→ cost accepted
→ evidence needed to revisit
```

Do not claim that a choice is permanently best. Defend why it was the smallest credible choice for this stage.

## Block 3 — Trace the central code

**Suggested ceiling:** 30–40 minutes  
**Read:** `02-code-you-must-own.md` and the annotated study view

Use the educationally annotated commit so the comments and docstrings appear during study:

```bash
git show ed1bdc349bb096ba8f0acc7b7d4d70a6c286f872:src/upgradepilot/cli.py
git show ed1bdc349bb096ba8f0acc7b7d4d70a6c286f872:src/upgradepilot/github_client.py
git show ed1bdc349bb096ba8f0acc7b7d4d70a6c286f872:src/upgradepilot/dependency_change.py
```

Write one responsibility sentence and one design-reason sentence for each:

```text
cli.main
GitHubReadClient.get_pull_request
GitHubReadClient.get_changed_files
extract_pinned_dependency_change
normalize_package_name
```

Example form:

```text
Function responsibility:
    get_changed_files acquires and validates every changed-file record.

Why this boundary exists:
    completeness must be established before extraction, and HTTP/pagination
    failures must not be confused with unsupported dependency syntax.
```

Then identify where these invariants are protected:

- successful HTTP is not enough;
- all changed-file records must be acquired;
- patch evidence must be complete enough;
- package names must identify the same normalized distribution;
- unsupported analysis must not become an acquisition exception.

### Pass condition

You can point to the owning function for each invariant and explain why moving the rule to another layer would weaken responsibility clarity or failure diagnosis.

### Session A stop check

Stop Session A when you can:

- reconstruct the complete flow;
- defend five selected design choices;
- trace the five central functions;
- connect each central function to at least one protected invariant.

Do not continue merely to consume time. Repeat only the failed portion before Session B.

# Session B — Tests, diagnosis, and ownership

## Block 4 — Read tests as executable reasoning claims

**Suggested ceiling:** 20–25 minutes  
**Read:** `03-tests-and-failure-diagnosis.md` and the annotated test view

Use:

```bash
git show ed1bdc349bb096ba8f0acc7b7d4d70a6c286f872:tests/test_github_client.py
git show ed1bdc349bb096ba8f0acc7b7d4d70a6c286f872:tests/test_dependency_change.py
```

Choose four tests:

- one identity test;
- one pagination/completeness test;
- one supported extraction test;
- one unsupported extraction test.

For each, state:

```text
protected invariant
why this case is discriminating
source owner
why a mock or live run is appropriate
what the test does not prove
```

### Pass condition

You do not describe a test as proving “the feature works.” You name its bounded claim, explain why this input would expose the targeted defect, and state its limitation.

## Block 5 — Ownership exercise

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
raw names differ
→ runs of '.', '_', and '-' normalize to '-'
→ comparison uses the normalized distribution identity
→ versions differ
→ all other supported invariants remain satisfied
```

### Defend the rule before testing it

Answer:

1. Why would raw string equality produce a false mismatch?
2. Why do we normalize the package name but not claim that the versions are safe or correctly ordered?
3. Why is this rule inside deterministic extraction rather than GitHub acquisition?
4. Why is one focused test preferable to broadening the entire requirement grammar now?
5. What evidence would justify changing the normalization rule later?

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

Use the existing `_record` helper and supported-result test as patterns. Write the test yourself rather than copying a completed solution.

### Run proof

```bash
python3 -m unittest discover -s tests -v
git diff -- tests/test_dependency_change.py
```

### Diagnose before repairing

If the test fails, classify the failure before editing source:

| Observed result | First hypothesis | Why |
|---|---|---|
| `package_mismatch` | package normalization is wrong or not applied consistently | parsing succeeded, but identity comparison rejected the pair |
| `no_supported_pinned_change` | pinned requirement grammar rejected one spelling | no candidate reached package comparison |
| supported result with wrong normalized name | result construction or normalization output is wrong | supported path executed with incorrect evidence fields |
| unrelated error | test arrangement, import, or environment problem | failure occurred outside the targeted extraction rule |

### Ownership pass condition

You can explain:

1. why the two raw names are different strings;
2. why they identify the same normalized package under the current rule;
3. why this test protects a real dependency-identity boundary;
4. which source function owns the behavior and why;
5. which plausible alternative would be weaker;
6. what the passing test still does not prove.

## Closed-book final check

Answer without notes:

1. Why does UpgradePilot acquire PR metadata before changed files?
2. Why is the head SHA part of evidence identity?
3. Why must changed-file count reconciliation happen before extraction?
4. Why is a short final page not the only completeness proof?
5. Why is `patch=None` not a transport failure?
6. Why is `pytest>=9.0.2` unsupported rather than invalid Python syntax?
7. Why does the extractor return a result union instead of raising for every unsupported case?
8. Why was an injectable Requests session chosen for this stage?
9. Why do we use both mocked tests and one live S004 run?
10. Why are retry, persistence, and CI interpretation deferred?
11. Which code boundary owns equivalent package names, and why there?
12. Give one current choice that should be revisited only after new evidence, and name that evidence.

## Honest depth labels after the sessions

Use the strongest label actually supported:

- **Introduced:** you recognize the terms and broad flow.
- **Operationally understood with guidance:** you can trace, classify, and repeat the provided reasons with notes available.
- **Reasoning with guidance:** you can compare selected alternatives and identify costs and revisit triggers.
- **Ownership practice:** you authored the test, predicted the result, interpreted execution, and defended the boundary.
- **Independently controlled:** not established by these sessions.

The expected realistic outcome is **reasoning with guidance across the current B2 design and ownership practice for one normalized-package test boundary**, not broad Python, HTTP, GitHub API, dependency-analysis, or architecture mastery.

## Stop line

Do not begin CI acquisition, upstream evidence, recommendation logic, replay infrastructure, persistence, retry policy, or broader dependency grammar during these study sessions.

After the ownership test passes and is reviewed, return to the active B2 plan for exact-head GitHub Actions evidence.
