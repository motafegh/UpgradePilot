# 01 — Flow and Boundaries

## SMART objective

In 25–30 minutes, reconstruct the complete current flow without notes, name its five boundaries, and state the current claim in five sentences or fewer.

## Current product question

> For this exact public Python dependency-update Pull Request, did at least one successful Continuous Integration path directly exercise the changed dependency?

Terms:

- **Pull Request (PR):** a proposed repository change.
- **Continuous Integration (CI):** automated build, check, or test jobs.
- **Application Programming Interface (API):** a defined software interface for requesting data or behavior.
- **Commit SHA:** Git's identifier for an exact repository revision. “Exact-head” means evidence belongs to the PR's exact head commit, not merely its branch or PR number.

## End-to-end flow

```text
1. repository + PR number
2. exact PullRequestIdentity
3. complete ChangedFile records
4. one supported PinnedDependencyChange
5. exact-head WorkflowRun / WorkflowJob records
6. workflow definition at the same head SHA
7. install and execution command evidence
8. CIAuthorityResult
```

## Five boundaries

### 1. Input

Is the local locator supported?

A valid `owner/repository` and positive PR number do not prove the remote resource exists.

### 2. Acquisition

Could GitHub evidence be obtained?

Examples: timeout, transport error, ambiguous `404`, forbidden/rate-limited, other HTTP error.

### 3. Response validation

Can a successful response be trusted under current rules?

Examples: invalid JSON, missing field, wrong type, wrong PR number, mismatched SHA, incomplete pagination.

`200 OK` is transport success, not evidence success.

### 4. Interpretation

What does validated evidence mean?

Examples:

- exact pin is supported;
- richer requirement syntax is unsupported;
- direct workflow exercise is sufficient;
- tox or multi-job evidence is unresolved.

Unsupported or unresolved is often a normal result, not a crash.

### 5. Claim

What conclusion is permitted?

Current permitted claim:

```text
At least one successful exact-head CI path directly exercised pytest.
```

Forbidden leap:

```text
Therefore the update is safe and should be merged.
```

## Facts, interpretations, recommendations

**Facts:** head SHA, changed filename, workflow status, job conclusion, command text.

**Interpretations:** supported dependency identity, sufficient/unresolved CI authority.

**Recommendations:** merge, targeted checks, investigate/block, defer, abstain.

The current source reaches interpretation and stops before recommendation.

## Why identity must flow forward

```text
PR head SHA
→ workflow-run head SHA
→ workflow-job head SHA
→ workflow-definition revision
```

Without this chain, UpgradePilot could combine dependency evidence, CI results, and workflow code from different commits.

## S004 reconstruction

```text
googlefonts/glyphsLib#1145
→ f3cda8...
→ requirements-dev.txt
→ pytest 9.0.2 → 9.0.3
→ Regression Tests directly installs requirements-dev.txt
→ Regression Tests directly runs pytest
→ Regression Tests: sufficient
→ Test + Deploy: unresolved
→ overall: sufficient
```

One sufficient workflow proves an existential claim: **at least one** CI path exercised the dependency. It does not erase the unresolved second workflow.

## Active recall

Close this file and answer:

1. Why is PR number alone insufficient identity?
2. Acquisition failure versus unresolved interpretation?
3. Why can overall authority be sufficient while one workflow is unresolved?
4. What does S004 prove?
5. What decision is still unauthorized?

## Pass condition

Draw the eight-stage flow and explain the five boundaries without reopening the file.