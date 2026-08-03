# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is replacement state, not append-only history. It alone answers what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 5 plan:** [`plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`](plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–4 and deterministic Step 5A–5D.
- **Current responsibility:** remaining live S001 upstream-acquisition proof required to close parent Step 5.
- **Current state:** live proof runner implemented; user execution is required before Step 5 can be declared closed.
- **Step 5D validation record:** [`working-memory/2026-08-03_B2-step-5d-interval-authority-validation.md`](working-memory/2026-08-03_B2-step-5d-interval-authority-validation.md)
- **Live proof runner record:** [`working-memory/2026-08-03_B2-step-5-live-s001-proof-runner.md`](working-memory/2026-08-03_B2-step-5-live-s001-proof-runner.md)

## Last behavior-validated deterministic executable boundary

Step 5D deterministic behavior is validated through:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

The user reported the complete deterministic suite:

```text
Ran 312 tests in 0.053s

OK
```

The exact focused Step 5D summary was not supplied and is not invented. The complete discovery run contains the Step 5D integration cases.

## Deterministic Step 5A–5D closure

The implemented and behavior-validated deterministic chain is:

```text
PyPI project response
→ PyPIReleaseIndexClient
→ PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ CrossedReleaseIndexEvidence

explicit Git version tag
→ GitHubTagCommitClient.resolve_tag_to_commit(...)
→ GitHubTagCommitEvidence.resolved_commit_sha

resolved immutable commit
+ explicit repository path
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ ExactRepositoryTextFile

DependencyReleaseInterval
+ GitHubTagCommitEvidence
+ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

The Step 5D test proves the selected minimum S001-shaped path:

```text
complete crossed-release index
+ exact proposed-tag changelog
+ zero GitHub Release bodies
→ authority_basis = tagged_changelog
```

It also proves that individually valid evidence from different intervals is rejected with `identity_mismatch` rather than silently combined.

## Live S001 proof harness

Scenario-specific validation tooling now exists at:

```text
tools/live_s001_upstream_interval_proof.py
```

Its implementation commit is:

```text
14cf30c728a2d5a4b6cfd1f20b03afa8ba27571f
```

Later working-memory and `MEMORY.md` commits do not change the live proof code.

The runner deliberately lives outside `src/upgradepilot/`. It hardcodes only the selected S001 proof identities while invoking generalized production clients.

### Live identities

```text
package: soupsieve
interval: 2.6 → 2.8.4
upstream repository: facelessuser/soupsieve
explicit accepted tag: 2.8.4
explicit changelog path: docs/src/markdown/about/changelog.md
```

### Live flow

```text
real PyPI project JSON
→ release-index evidence
→ crossed-release selection

real refs/tags/2.8.4
→ exact tag object
→ resolved immutable commit

resolved commit
+ exact changelog path
→ strict path/blob/byte/UTF-8 file evidence
→ TaggedChangelogEvidence

crossed releases + tagged changelog
→ existing Step 1 authority assembler
→ AuthoritativeUpstreamIntervalEvidence
```

The runner prints the exact source URL, selected releases, tag ref/object type/object SHA, resolved commit SHA, tag peel depth, changelog path/blob/byte counts, authority basis, and admitted GitHub Release-body count.

It does **not** interpret changelog prose or evaluate target Python relevance.

## External preflight corroboration

Separate official-source inspection before the runner was added currently shows:

- PyPI release history includes `2.6`, `2.7`, `2.8`, `2.8.1`, `2.8.2`, `2.8.3`, and `2.8.4`;
- PyPI provenance for 2.8.4 identifies `facelessuser/soupsieve` and `refs/tags/2.8.4`;
- the provenance source commit is `28108ab805818c832d9568142a99844fd95a0d39`;
- `docs/src/markdown/about/changelog.md` exists at that exact commit.

This is corroboration only. It cannot substitute for observing UpgradePilot's own clients successfully traverse the real path.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only
python tools/live_s001_upstream_interval_proof.py
```

Optional environment input:

```text
GITHUB_TOKEN
```

A token is not required for product semantics; it may only improve public GitHub API rate limits. The proof is read-only.

### Expected success shape

Do not assert these as observed until the user supplies the runner output.

```text
LIVE STEP 5 PROOF: PASS
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

The exact tag object type/SHA, resolved commit, changelog blob SHA, byte counts, and any ignored non-PEP-440 keys are runtime observations and must be recorded from actual output.

If the live proof fails, preserve the exact stage/state/detail and diagnose only the demonstrated acquisition boundary. Do not weaken identity, byte, or authority rules merely to force S001 success.

If the live proof passes:

1. record the exact live evidence output;
2. close parent-plan Step 5 as behavior-validated for the selected S001 path;
3. return to `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md` and activate the next authorized parent-plan responsibility;
4. do not infer user mastery from product validation.

## Stop line

Until the live S001 proof is observed, do not begin:

- semantic support-drop extraction/model integration;
- target-Python or CLI acquisition-order changes;
- full S001 automated product execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- live S001 PyPI release-index acquisition by UpgradePilot;
- live S001 tag-to-commit resolution by UpgradePilot;
- live S001 exact changelog-file acquisition by UpgradePilot;
- live S001 `AuthoritativeUpstreamIntervalEvidence`;
- parent Step 5 closure;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–5.

## Learning state

Steps 1–5D are behavior-validated at the deterministic product level. The remaining live-source proof is execution evidence, not a mastery assessment.

Concepts exposed through Step 5 include:

- **source observation versus interpretation:** raw PyPI version identities are acquired before PEP 440 meaning is assigned;
- **Git reference versus immutable commit:** version-tag names require exact resolution before file evidence is frozen;
- **annotated-tag peeling:** tag objects are followed under cycle/depth bounds until a commit is reached;
- **tree/file identity:** the commit selects the source tree while the blob SHA identifies the exact file object;
- **reported versus decoded bytes:** GitHub metadata and actual decoded content must agree;
- **source retrieval time:** each network source carries its own acquisition time;
- **evidence identity joins:** repository, interval, commit, path, and source identity must agree before records can be composed;
- **acquisition versus authority:** exact records are inputs to the pre-existing Step 1 authority contract rather than authority by themselves;
- **deterministic proof versus live-source proof:** controlled tests prove code behavior while live acquisition proves the selected public path is actually obtainable.

Current depth:

```text
Steps 1–5D deterministic behavior validated
+ source/design/test exposure
+ live proof runner available
but
live S001 UpgradePilot acquisition not yet observed
no user-owned Step 5 end-to-end explanation recorded
no independent implementation proof
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
