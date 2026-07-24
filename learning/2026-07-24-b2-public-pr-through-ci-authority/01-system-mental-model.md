# 01 — System Mental Model

## SMART objective

Within 25–35 minutes, reconstruct the complete current UpgradePilot flow from memory, identify the five major boundaries, and explain the current claim in no more than five sentences.

## The product question at this stage

UpgradePilot is currently answering a bounded question:

> For this exact public Python dependency-update Pull Request, did at least one successful Continuous Integration path directly exercise the changed dependency?

Definitions:

- **Pull Request (PR):** a proposed set of repository changes.
- **Continuous Integration (CI):** automated jobs that build, check, or test proposed changes.
- **Application Programming Interface (API):** a defined interface through which software requests structured data or behavior from another system.
- **Commit SHA:** Git's commit identifier, derived using the Secure Hash Algorithm family. Practically, it identifies the exact repository revision being analyzed.

The name “exact-head” means evidence is attached to the Pull Request's exact current head commit, not merely to a branch name or PR number.

## The complete flow

```text
1. User locator
   repository + PR number

2. Proposal identity
   repository, PR number, base SHA, head SHA, changed-file count

3. Dependency identity
   complete changed-file records
   → patch evidence
   → one package==old to package==new change

4. CI execution evidence
   pull_request workflow runs for the exact head SHA
   → jobs
   → step summaries

5. CI definition evidence
   exact workflow path used by each run
   → workflow text at the same head SHA

6. CI authority interpretation
   successful run/job
   + changed requirements file installed
   + changed package directly invoked
   → sufficient authority
```

## Five boundaries you must distinguish

### 1. Input boundary

Question: Is the user's locator locally supported?

Examples:

- supported: `googlefonts/glyphsLib` and PR number `1145`;
- rejected: malformed repository text or a non-positive PR number.

A valid locator does not prove the remote repository or PR exists.

### 2. Acquisition boundary

Question: Did GitHub return a usable response?

Possible categories include:

- timeout;
- transport failure;
- forbidden or rate-limited;
- not found or inaccessible;
- other HTTP error.

Acquisition answers whether data could be obtained, not whether the data proves the product claim.

### 3. Response-validation boundary

Question: Is the successful response structurally and semantically trustworthy?

Examples:

- required field missing;
- field has the wrong type;
- returned PR number differs from requested PR number;
- workflow or job head SHA differs from the frozen PR head;
- paginated count disagrees with metadata.

A `200 OK` HTTP response is not proof that the payload is usable.

### 4. Interpretation boundary

Question: What does validated evidence mean under the currently supported rules?

Examples:

- exact pinned dependency change is supported;
- range requirement is unsupported;
- multiple dependency candidates are ambiguous;
- workflow commands prove direct exercise;
- tox-only or multi-job workflow remains unresolved.

Unsupported or unresolved evidence is not necessarily malformed.

### 5. Claim boundary

Question: What conclusion is permitted?

Current permitted conclusion:

```text
At least one successful exact-head CI path directly exercised pytest.
```

Current forbidden leap:

```text
Therefore the update is safe and should be merged.
```

## Facts versus interpretations

Facts are directly acquired or deterministically derived:

- PR head SHA;
- changed filename;
- workflow status;
- job conclusion;
- workflow command text.

Interpretations apply a rule to facts:

- dependency update is supported;
- CI authority is sufficient;
- workflow evidence is unresolved.

Recommendations require additional evidence and policy:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

The current source stops before recommendation.

## Why identity flows forward

Every later fact must refer to the same proposal revision:

```text
PullRequestIdentity.head_sha
→ workflow-run head_sha
→ workflow-job head_sha
→ workflow-definition revision
```

Without this chain, UpgradePilot might combine:

- dependency evidence from one commit;
- CI results from an older commit;
- workflow commands from a newer default branch.

That would create a convincing but false conclusion.

## Current S004 mental model

```text
googlefonts/glyphsLib#1145
→ exact head f3cda8...
→ requirements-dev.txt
→ pytest 9.0.2 to 9.0.3
→ two successful workflow runs
→ Regression Tests directly installs requirements-dev.txt
→ Regression Tests directly invokes pytest
→ Regression Tests authority: sufficient
→ Test + Deploy authority: unresolved
→ overall authority: sufficient
```

One sufficient workflow can establish that **at least one** CI path exercised the dependency. The unresolved second workflow remains visible because evidence is not erased merely because the overall result is sufficient.

## Active-recall check

Close this file and answer:

1. Why is PR number alone insufficient identity?
2. What is the difference between acquisition failure and unresolved interpretation?
3. Why can one workflow be sufficient while another remains unresolved?
4. What does the current result prove?
5. What recommendation is still forbidden?

## Completion evidence

This file is mastered when you can draw the six-stage flow and explain the five boundaries without reopening the notes.