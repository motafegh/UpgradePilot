# Exact-Revision Requirements/Constraints Evidence Coherence — Working Memory

**Date:** 2026-09-12 → 2026-09-13  
**Session status:** CLOSED  
**Primary mode:** Learning-by-Doing + Planning/Design + Build/Implement + ownership review  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-12_ci-static-runtime-correlation-bridge.md`](2026-09-12_ci-static-runtime-correlation-bridge.md)  
**Continued by:** [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Responsibility

This cycle repaired a requirements/constraints provenance defect that could create mixed-snapshot dependency evidence:

```text
PR identity freezes head A
+
changed-file patch is later acquired from the mutable PR files endpoint
+
PR advances to head B while changed-file count remains the same
→ B patch content can be interpreted while the dependency source context is attributed to A
```

This was more foundational than broader downstream evidence work because later exact-head CI/runtime evidence cannot repair a dependency transition whose source revision identity is already wrong.

The defect was specific to patch-backed requirements/constraints evidence. `uv.lock`, admitted pyproject evidence, workflow definitions, and other exact repository-text paths already use immutable SHA-bound acquisition where required.

## Starting execution path

Before the repair:

```text
GitHubPullRequestClient.get_pull_request(...)
→ PullRequestIdentity(base_sha, head_sha, changed_files, ...)

GitHubPullRequestClient.get_changed_files(identity)
→ mutable GET /repos/{repository}/pulls/{number}/files
→ ChangedFile(..., patch=...)

analyze_dependency_change(identity, changed_files, repository_client)
→ requirements/constraints consumes ChangedFile.patch directly
→ extract_exact_requirement_changes(...)
→ source context later receives identity.head_sha
```

The important asymmetry was:

```text
requirements/constraints
→ semantic version transition came directly from mutable ChangedFile.patch

uv.lock / admitted pyproject
→ changed-file inventory admitted the path, but semantic content came from exact base/head repository files
```

## A — pre-implementation investigation/design — DONE

### Selected invariant

Every `ChangedFile` collection admitted from the mutable PR-files endpoint must be accepted only when the pull-request provider can establish that the collection corresponds to the already-frozen `PullRequestIdentity` strongly enough for the current product responsibility.

Selected mechanism: **provider-owned snapshot fence**.

```text
frozen PullRequestIdentity A
→ acquire all PR-file pages
→ validate each changed-file head locator against A.head_sha
→ re-read PR identity after acquisition
→ require base_sha + head_sha + changed_files still equal A
→ only then return ChangedFile records
```

Earliest sufficient owner: `GitHubPullRequestClient.get_changed_files(...)`.

Dependency parsing and maintainer-action synthesis must not reconstruct GitHub provenance downstream.

### Why this mechanism was selected

Current source already made `get_changed_files(...)` responsible for PR-files acquisition, response interpretation, pagination, and complete-count checking. The missing proposition was snapshot correspondence.

A real public `googlefonts/glyphsLib#1145` response showed a useful provider locator:

```text
PR head_sha
= f3cda8a94600e58d27f1bc17c99b7693718b6350

requirements-dev.txt contents_url
= .../contents/requirements-dev.txt?ref=f3cda8a94600e58d27f1bc17c99b7693718b6350
```

The separate changed-file `sha` was correctly treated as a Git blob identity, not the PR head commit SHA.

### Alternatives considered

**Exact base/head requirements-file reads** were not selected first because mutable PR-files path discovery would remain and requirements extraction would need a new whole-file comparison/diff contract. That was larger than the actual snapshot-binding defect.

**Exact base→head commit comparison** remained a conceptually stronger immutable source but was not selected first because replacing the current provider could narrow existing changed-file detail breadth, while adding a second changed-file inventory would create duplicate provider/reconciliation responsibility.

It remains a fallback only if later evidence proves the client-side fence insufficient.

### Validation metadata decision

No `contents_url` or duplicate `head_sha` was added to durable `ChangedFile` state merely because the provider used it for admission:

```text
untrusted external response
→ provider validates repository/path/head relationship
→ trusted ChangedFile keeps only downstream-needed fields
```

### Claim limit established in A

The fence is a client-side observable snapshot-consistency contract, not transactional or cryptographic linearizability across GitHub endpoints.

A theoretical ABA-style mutation:

```text
A → B → A
```

can evade observation if all fields return to the original values before the final read. Solving that stronger threat would require a stronger immutable evidence source and was not justified by the admitted product horizon.

## B — bounded Build implementation — DONE

Ali explicitly authorized Build after A.

### Product implementation

Primary owner changed:

- `src/upgradepilot/github/pull_request.py`

Implementation commits:

- `48b2b204` — add provider-owned changed-file snapshot fence;
- `7a8fed2b` — preserve GitHub repository case-insensitive identity while keeping file-path comparison exact.

Final behavior:

```text
PullRequestIdentity A
→ acquire PR-files pages when changed_files > 0
→ require each changed-file contents_url to identify:
     GitHub API host
     same repository identity
     exact returned filename
     ref == A.head_sha
→ retain complete-count check
→ re-read PR identity even when changed_files == 0
→ require final base_sha/head_sha/changed_files == A
→ only then return tuple[ChangedFile, ...]
```

### Build-time refinement — repository case semantics

Implementation review found a compatibility edge:

```text
caller: GoogleFonts/glyphsLib
provider locator: googlefonts/glyphsLib
```

Repository identity is case-insensitive on GitHub, while repository file paths remain case-sensitive. The final check therefore compares owner/repository case-insensitively while keeping the path and head ref exact.

This avoided introducing an unrelated repository-locator regression.

### Focused proof

Focused owner:

- `tests/test_github_client.py`

Test commits:

- `4d76dcb8` — initial snapshot-fence proof family;
- `9c3a4d0c` — repository-case proof;
- `ba4bbdfb` — explicit multi-page drift rejection.

Focused tests discriminate:

```text
stable matching locator + stable post-read
→ accepted

same-count head A→B locator mismatch
→ rejected

base/head/count drift after acquisition
→ rejected

multi-page acquisition + later head drift
→ rejected

missing/malformed contents_url
→ rejected

wrong repository/path locator
→ rejected

repository case-only difference
→ accepted

count disagreement
→ rejected

zero-file snapshot + post-read drift
→ rejected
```

The proof also protects that `contents_url` remains provider-only validation metadata rather than becoming a durable `ChangedFile` field.

### Executable validation — GREEN

Ali synchronized local `main`, activated the project virtual environment, and ran the planned narrow-to-broad sequence:

```text
focused GitHub provider proof
→ 13 tests passed

nearby regressions
→ 15 tests passed
   covering exact requirements extraction,
   dependency analysis,
   exact PR base/head repository-file behavior,
   and investigation composition

full deterministic suite
→ 566 tests passed
```

Interpretation:

- focused controlled cases establish the intended fence behavior;
- immediate consumers remained green;
- the complete current deterministic product test horizon remained green.

Non-proof retained:

- no transactional snapshot isolation claim;
- no elimination of theoretical ABA;
- no claim that every possible live GitHub behavior is modeled by deterministic tests.

## C — progressive state preservation — DONE

The cycle preserved:

```text
original mixed-snapshot failure
→ design alternatives and selection
→ implementation ownership
→ build-time repository-case refinement
→ real external response-shape evidence
→ focused/nearby/full executable proof
→ explicit non-claims
→ handoff
```

`MEMORY.md` was reconciled separately as the compact live-state owner throughout the cycle.

## D — post-action learning / ownership review — DONE

D was intentionally completed in two substantive rounds rather than being split into a nested mini-cycle.

The integrated review covered transferable engineering concepts:

- TOCTOU (Time Of Check To Time Of Use) race reasoning;
- evidence provenance and revision identity;
- provider trust boundary versus dependency semantic boundary;
- why requirements were more exposed than exact-file `uv.lock` semantics;
- why per-file locator validation and final PR reread prove different propositions;
- validation-only metadata versus durable domain state;
- fail-closed evidence admission;
- minimal sufficient design rather than strongest imaginable mechanism;
- layered validation and proof boundaries;
- the remaining ABA limitation.

Ali's ownership-check answers were sufficient to close D:

1. same-count A→B drift is dangerous because count equality cannot reveal that returned file evidence belongs to a different head;
2. snapshot correspondence belongs at the provider boundary so downstream consumers do not each reimplement GitHub provenance checks;
3. Ali initially described the two checks as double safety; the important refinement is that they establish different propositions:
   - per-file `contents_url` binds the individual file to the frozen head;
   - final PR reread detects observable base/head/count drift across the overall acquisition window;
4. deterministic tests cover modeled scenarios and cannot control or prove all external/concurrent service behavior.

No D discussion exposed a new correctness defect in the repaired responsibility.

### A→E granularity preference established

Ali explicitly clarified the desired Learning-by-Doing rhythm:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-steps.

Apply this as a proportionality preference, not as permission to skip material reasoning, proof, or preservation.

## E — bounded gap review / next-slice selection — DONE

E rechecked the repaired responsibility against its final proof and non-proof boundary.

### Closure decision

No remaining exact-revision correctness gap justifies reopening A/B:

- the reproduced same-count mixed-head failure is now rejected;
- base/head/count drift, pagination, malformed locators, and zero-file drift are covered;
- nearby consumers and the 566-test deterministic horizon are green;
- D exposed no hidden ownership/correctness gap;
- the ABA limitation is an explicit non-claim, not unfinished work;
- exact commit comparison remains a stronger fallback, not currently earned complexity.

Therefore this exact-revision requirements/constraints provenance responsibility is **CLOSED A→E**.

### Next selected responsibility

The next confirmed correctness responsibility remains **static shell/direct-install false-positive recognition**.

Prior controlled evidence established false positives such as:

```text
pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

Current source still supports that diagnosis:

```text
workflow_context.bounded_shell_segments(...)
→ textual split over &&, ||, ;, newline
→ no shell quote/comment awareness

direct_install.observe_direct_installation_declaration(...)
→ consumes those segments before pip/-r interpretation
```

A nearby shared consumer, `dependency/environment_selection.py`, also uses the same bounded segment helper. Therefore the next A stage must determine the earliest sufficient owner rather than assuming a direct-install-only patch.

New active record:

- [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Final cycle state

```text
Slice: exact-revision requirements/constraints evidence coherence

A — DONE
B — DONE
C — DONE
D — DONE
E — DONE

CYCLE — CLOSED
```

## Durable non-reentry conditions

Do not reopen this cycle merely because a stronger mechanism exists. Re-entry requires concrete evidence such as:

- regression of the implemented provider fence;
- real GitHub response semantics incompatible with the admitted locator contract;
- a product requirement that makes the ABA/transactional limitation material;
- evidence that exact commit comparison or another immutable source has become necessary for a selected proposition.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
