# UpgradePilot Current Memory

**Last updated:** 2026-07-29 19:05 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Parent decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected bounded plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Latest session synthesis:** [`working-memory/2026-07-29_1905_B2-python-support-relevance-session-synthesis.md`](working-memory/2026-07-29_1905_B2-python-support-relevance-session-synthesis.md)
- **Step 1 full validation:** [`working-memory/2026-07-29_B2-target-python-declaration-full-validation.md`](working-memory/2026-07-29_B2-target-python-declaration-full-validation.md)
- **Latest semantic review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md)

For additional working-memory records created on 2026-07-29, include local `HHMM` after the date so same-day chronology remains visible. Existing files are not renamed merely to retrofit the convention.

## Behavior-validated product boundary

Target-relevance Step 1 is fully behavior-validated at revision:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

The complete deterministic suite passed 72 tests, and one complete installed public read-only command preserved the existing evidence pipeline while producing the expected target state.

UpgradePilot behavior-validly reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported exact pinned Python dependency update
→ exact-head pyproject.toml target declaration evidence
→ available or explicit target-declaration problem state
→ exact-head workflow/job/step evidence
→ bounded CI-authority classification
→ exact PyPI package/version/file identity
→ PyPI-reported file provenance
→ matching GitHub upstream repository
→ exact published release and tag reference
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

The full command used:

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

## Selected deterministic range direction

Ali approved the standards-based direction:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
```

UpgradePilot will not implement a general PEP 440 parser from scratch.

Responsibility split:

```text
packaging
→ standards-correct version/specifier parsing and candidate membership

UpgradePilot
→ bounded meaning of whether a stable Python X.Y line overlaps a declaration
```

Accepted semantic meaning:

```text
declared_python_overlap
= at least one stable Python X.Y.Z release is admitted by requires-python
```

The exact existential algorithm and unsupported cases are not yet frozen. Arbitrary finite patch enumeration without a completeness argument is not accepted. No `packaging` runtime dependency has yet been added.

## Upstream contract and Instructor boundary

The upstream path requires two separate types:

```text
CandidateUpstreamClaimResult
→ untrusted model-facing structured output

GroundedPythonSupportDropClaim
→ deterministically validated comparator input
```

The trusted input must preserve:

```text
category = support_boundary_change
change_state = support_dropped
normalized Python X.Y
exact immutable source identity
exact contiguous source quote
old dependency version
proposed dependency version
```

Controlled tests must construct the trusted type directly without LM Studio, Instructor, or an LLM.

Instructor may later be evaluated as an adapter for Pydantic-to-JSON-Schema generation, OpenAI-compatible LM Studio requests, typed parsing, mechanical grounding context, and diagnostics. It is not semantic truth, source authority, target relevance, range evaluation, evidence sufficiency, or decision authority. Instructor, Pydantic, OpenAI client, and a model remain unadopted dependencies/deployments.

The local-LLM experiment remains paused. Gemma v1.3 established only its exact corrected compatibility-assurance case; it did not establish reliable Python support-drop extraction.

## First end-to-end proof case

Historical product-simulation scenario S001 already contains the required real contrast. No new simulation case is currently needed.

```text
target: pydantic/pydantic
PR: 13432
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
dependency: soupsieve
update: 2.6 → 2.8.4

target declaration:
requires-python = ">=3.10"

upstream tagged changelog:
Drop support for Python 3.8.

expected relevance:
outside_declared_python_range
```

S001 is historical evidence and an oracle, not current automated proof. The current product must reacquire exact identities and produce the result without rewriting completed simulation records.

The expected result proves only that Python 3.8 is outside Pydantic's declared installation range at the exact PR head. It does not prove compatibility, safety, or merge authorization.

## Upstream interval gap

S001 exposed that the exact proposed-version release body alone can be too narrow.

```text
Soup Sieve 2.6 → 2.8.4
support drop introduced in 2.8
2.8.4 release body contains only 2.8.4 fixes
```

Required upstream change boundary:

```text
old_version exclusive
proposed_version inclusive
```

Admitted bounded source order:

1. exact GitHub Release bodies for relevant crossed releases when identities and ordering are established;
2. exact tagged upstream changelog at the proposed tag, preserving relevant section, path, revision, and blob;
3. package metadata as corroboration where applicable.

Dependabot-copied release notes may locate or corroborate a claim but must not silently become upstream authority. Arbitrary source search and model-selected authority remain prohibited.

## Temporary CLI-order debt

Current temporary order:

```text
supported dependency update
→ target pyproject.toml acquisition
→ CI evidence
→ package evidence
→ upstream release evidence
```

This order was accepted only to isolate and behavior-validate target acquisition.

Required final semantic activation order:

```text
supported dependency update
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

Target Python investigation is conditional work. The final CLI must expose non-activation and must not acquire `pyproject.toml` for every supported dependency update merely because the parser exists.

Do not refactor the order before upstream interval authority, claim contracts, and comparator inputs are frozen enough to preserve existing behavior and tests.

## Not established

- authoritative crossed-version upstream acquisition in product source;
- frozen candidate and trusted support-drop types;
- reliable normalized Python support-drop extraction;
- admitted `packaging` dependency bounds;
- exact stable Python-line overlap algorithm;
- deterministic target/upstream relevance comparison;
- conditional target-investigation orchestration;
- evidence sufficiency or stopping beyond this relevance slice;
- compatibility or objective safety;
- merge, targeted-check, investigate/block, defer, or abstain action;
- Instructor, model, provider, or LLM product adoption.

## Exact continuation

1. Review the revised [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
2. Record the durable `packaging` dependency/method decision in the appropriate owner; create an ADR only if required by repository rules for a cross-cutting dependency commitment.
3. Freeze upstream interval/source evidence types and unresolved/conflict states.
4. Freeze `CandidateUpstreamClaimResult` and `GroundedPythonSupportDropClaim` independently of Instructor and model runtime.
5. Freeze the exact `packaging`-based stable Python-line overlap algorithm, including patch boundaries, compound specifiers, exclusions, wildcards, compatible-release operators, pre-releases, and unsupported cases.
6. Implement deterministic comparison using manually constructed trusted claims first.
7. Use controlled S001 evidence to prove:

```text
Python 3.8 support dropped
+ target requires-python >=3.10
→ outside_declared_python_range
```

8. Implement bounded authoritative upstream interval acquisition for S001.
9. Determine whether semantic extraction is required; when required, compare the bounded Instructor adapter without treating adapter success as model or product adoption.
10. After claim extraction and comparison are behavior-validated, move target Python acquisition behind the valid grounded support-drop activation condition.
11. Run S001 through the complete current product path.
12. Stop before compatibility, safety, evidence-sufficiency, or maintainer-action policy.

## Relevant revisions

```text
Step 1 fully behavior-validated product revision:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Step 1 full validation evidence:
3f865529a77b001a8b70c4c0ea962f5bec3e3564

revised target Python support relevance plan:
ff3936939020acd1a9f033e1296b3b5633f649da

19:05 session synthesis:
1b09648356cb132852a27321eed70abafc7dd94e

v1.3 semantic evidence:
151f015edb698b95d9da69a7a463c7326818cb83

v1.3 independent review completed:
6565fa61053f48953768b9fef5805cb3169dd0d3
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.