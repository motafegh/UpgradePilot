# UpgradePilot Current Memory

**Last updated:** 2026-07-29 21:22 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md`](plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md)
- **Downstream dependent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Latest planning evidence:** [`working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md`](working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md)
- **Previous session synthesis:** [`working-memory/2026-07-29_1905_B2-python-support-relevance-session-synthesis.md`](working-memory/2026-07-29_1905_B2-python-support-relevance-session-synthesis.md)
- **Step 1 full validation:** [`working-memory/2026-07-29_B2-target-python-declaration-full-validation.md`](working-memory/2026-07-29_B2-target-python-declaration-full-validation.md)

For additional working-memory records created on 2026-07-29, include local `HHMM` after the date so same-day chronology remains visible. Existing files are not renamed merely to retrofit the convention.

## Why the selected plan changed

S001 is the selected real Python-support relevance proof case:

```text
pydantic/pydantic PR 13432
Soup Sieve 2.6 → 2.8.4
upstream: Drop support for Python 3.8.
target: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

The active dependency interpreter accepts only complete same-file exact-pin patches:

```text
package==old_version
→ package==new_version
```

S001 changes a structured `uv.lock` package record instead:

```toml
[[package]]
name = "soupsieve"
-version = "2.6"
+version = "2.8.4"
```

The current product therefore cannot establish S001's dependency identity and would stop before target Python, CI, package, upstream, or relevance work.

This is a foundational representation gap, not merely an S001 exception. Dependency identity controls every downstream evidence stage. The selected plan now corrects that foundation before further Python-support relevance implementation.

## Behavior-validated product boundary

Target-declaration Step 1 remains fully behavior-validated at product revision:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

The complete deterministic suite passed 72 tests, and one installed public read-only S004 command preserved the existing evidence pipeline while producing the expected target state.

UpgradePilot behavior-validly reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported same-file package==version transition
→ exact-head pyproject.toml target declaration evidence
→ available or explicit target-declaration problem state
→ exact-head workflow/job/step evidence
→ bounded CI-authority classification
→ exact PyPI package/version/file identity
→ PyPI-reported file provenance
→ matching GitHub upstream repository
→ exact proposed-version release and tag reference
→ bounded release body
→ concise CLI evidence report
→ unresolved_claim
```

Behavior-validated target evidence states:

```text
available
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

`requires-python` establishes only a declared Python installation-version specifier at one immutable revision. It does not establish CI execution, production runtime, active testing, dependency use, compatibility, safety, or a maintainer action.

## S004 validation result

The full S004 command used:

```text
repository: googlefonts/glyphsLib
PR: 1145
revision: f3cda8a94600e58d27f1bc17c99b7693718b6350
path: pyproject.toml
blob: 38d6a9efc4b94e2b733d3bbb848156449814ec94
result: project_table_absent
```

The file's Black `target-version` setting was correctly not treated as a PEP 621 project declaration. No range comparison or compatibility claim followed.

The first live attempt received HTTP 401 because a stale or invalid non-empty `GITHUB_TOKEN` was present. After `unset GITHUB_TOKEN`, the public command completed anonymously. No silent anonymous retry behavior is selected.

## Selected foundation direction

The recommended durable structure is:

```text
source-specific deterministic interpreters
→ representation-aware candidates
→ deterministic reconciliation
→ one canonical DependencyVersionChange
   or explicit unsupported, malformed, incomplete, ambiguous, multiple, or conflicting result
```

First admitted representations proposed by the selected plan:

```text
1. exact-pin requirements/constraints transitions
2. modified same-path uv.lock exact base/head transitions
```

The first boundary remains exactly one package version transition. Broad package-manager support, dependency graphs, role/path interpretation, and multi-package updates remain deferred to B4.

No architecture ADR or source implementation has been created yet because the durable decisions require Ali review.

## Critical downstream separation

The existing exact-pin result exposes a `source_file` that the CI-authority rule may prove was explicitly installed.

That meaning cannot be generalized to lockfiles:

```text
where a dependency change was established
≠
how CI consumed that dependency representation
```

The canonical dependency contract must preserve change evidence paths without treating them as CI install authority.

Expected first behavior:

- exact-pin CI authority remains unchanged for its admitted command form;
- `uv.lock` dependency identity may become available;
- `uv.lock` CI authority remains unresolved until a separate bounded `uv` consumption rule is selected and tested.

## Acquisition issue requiring decision

The repository text reader currently limits decoded files to 1,000,000 bytes.

S001's exact-head `uv.lock` blob is:

```text
def33fe05d78ab851ce91a33db5bc55a439873a1
```

The file is large and contains thousands of lines and extensive artifact metadata. Before `uv.lock` implementation:

1. measure exact S001 base/head byte sizes;
2. compare bounded contents and blob acquisition paths;
3. select a justified maximum;
4. preserve explicit too-large evidence;
5. do not remove limits merely to make S001 pass.

## Decisions awaiting Ali review

The selected plan recommends, but does not yet authorize source implementation of, these choices:

1. use one representation-neutral `DependencyVersionChange` downstream;
2. use source-specific interpreters plus deterministic reconciliation;
3. admit exact-pin requirements/constraints and modified same-path `uv.lock` first;
4. keep exactly one dependency transition in B2;
5. combine provenance for semantically identical candidates;
6. return conflict for different candidates without source-priority guessing;
7. abstain on duplicate normalized `uv.lock` package identities;
8. separate change evidence from CI consumption;
9. bound exact-pin eligibility to a requirements/constraints source family rather than arbitrary changed text;
10. measure and select a justified lockfile acquisition bound;
11. create a durable representation-policy ADR after approval and before code.

The detailed reasoning and alternatives are in the selected plan and latest planning record.

## Downstream Python-support direction retained

Ali previously approved the standards-based direction:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
```

UpgradePilot will not implement a general PEP 440 parser from scratch.

Accepted product meaning remains:

```text
declared_python_overlap
= at least one stable Python X.Y.Z release is admitted by requires-python
```

The exact line-overlap algorithm, unsupported cases, dependency bounds, and ADR have not yet been frozen. No `packaging` runtime dependency has been added.

The upstream path still requires:

```text
CandidateUpstreamClaimResult
→ untrusted model-facing structured output

GroundedPythonSupportDropClaim
→ deterministically validated comparator input
```

Instructor, Pydantic, OpenAI client, LM Studio, and a model remain unadopted. The local-LLM experiment remains paused.

## Upstream interval and CLI-order gaps retained

S001 exposes the required upstream interval:

```text
old_version exclusive
proposed_version inclusive
```

because the Python 3.8 support drop occurred in Soup Sieve 2.8 while the proposed version is 2.8.4.

The required eventual semantic order remains:

```text
trusted canonical dependency change
→ package and upstream identity
→ authoritative upstream interval evidence
→ candidate extraction
→ deterministic claim validation
→ valid Python support-drop claim?
    ├── no  → target Python investigation not activated
    └── yes → exact-head pyproject.toml
              → requires-python evidence
              → packaging-based comparison
```

Do not refactor target activation during the dependency-foundation plan.

## Not established

- representation-neutral dependency-change contracts;
- adapter/reconciler architecture acceptance;
- exact-pin source-family eligibility;
- exact base/head generic file acquisition;
- justified large-lockfile acquisition bounds;
- `uv.lock` interpretation;
- S001 dependency identity through the product;
- `uv` CI consumption authority;
- authoritative crossed-version upstream acquisition;
- frozen candidate and trusted support-drop types;
- reliable normalized Python support-drop extraction;
- admitted `packaging` dependency bounds;
- exact stable Python-line overlap algorithm;
- deterministic target/upstream relevance comparison;
- conditional target-investigation orchestration;
- compatibility or objective safety;
- merge, targeted-check, investigate/block, defer, or abstain action;
- Instructor, model, provider, or LLM product adoption;
- production readiness or Ali-owned mastery.

## Exact continuation

1. Review [`plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md`](plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md).
2. Accept, revise, or reject the eleven durable decisions listed above.
3. Do not write product source until those decisions are resolved.
4. After approval, create the representation-policy ADR and update the architecture register.
5. Freeze canonical change, candidate, evidence-source, reconciliation, and problem contracts.
6. Extract the existing exact-pin logic behind the admitted adapter while preserving S004 behavior.
7. Add deterministic reconciliation before adding another representation.
8. Add exact PR base/head repository-file acquisition and measure S001 lock sizes.
9. Implement bounded `uv.lock` interpretation with conservative ambiguity and multi-change abstention.
10. Integrate the canonical change into CLI orchestration without implying lockfile CI authority.
11. Run the complete deterministic suite and installed S004/S001 public commands.
12. Record behavior evidence and update this file.
13. Restore [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md) as the selected bounded plan only after the foundation passes its stop line.

## Relevant revisions

```text
Step 1 fully behavior-validated product revision:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Step 1 full validation evidence:
3f865529a77b001a8b70c4c0ea962f5bec3e3564

Dependency foundation plan created:
d8f983426fca77f0d918369429269fe6b77837c1

B2 gate generalized:
99addcfba51910f8c9843ad0ebfcb367a47ad044

Target Python relevance prerequisite added:
468a6709db20329d098da92d037e02c631700af8

21:22 planning evidence:
4204b001b7826856eeb71da591c3ef25ee8addc5
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
