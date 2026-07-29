# B2 Python Support Relevance — Session Synthesis

**Local timestamp:** 2026-07-29 19:05 +03:30  
**Route:** B2 — Public PR vertical slice  
**Controlling plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Session scope:** close target-declaration Step 1, audit the complete relevance path, select the deterministic range method, identify the first end-to-end case, and correct the remaining plan

## Working-memory naming note

Multiple working-memory records may be created on the same date. For subsequent records created on 2026-07-29, include local `HHMM` after the date:

```text
YYYY-MM-DD_HHMM_<topic>.md
```

This preserves visible chronological ordering when several records share one date. Existing same-day records are not renamed merely to retrofit this convention.

## Session starting position

At the beginning of the session:

- local-LLM prompt tuning was paused after the narrow Gemma v1.3 correction;
- no model, provider, structured-output adapter, or LLM runtime was adopted into product source;
- the target Python relevance plan was selected;
- target-side `[project].requires-python` acquisition had not yet been implemented;
- the product still ended at `unresolved_claim` after exact PR, CI, package, provenance, and upstream-release evidence.

## Step 1 implementation completed

The session implemented the target-declaration responsibility only:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

Added or changed:

- `src/upgradepilot/target_python.py`;
- `src/upgradepilot/cli.py`;
- `tests/test_target_python.py`;
- `tests/test_cli.py`.

The target interpreter preserves:

```text
available
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

The existing GitHub repository client remains acquisition-only. TOML interpretation is kept in the focused target module, and CLI code owns orchestration and presentation.

Step 1 revisions:

```text
89cb0ea4fa827aec6ed5504370d4c2a9e6f3a6e0  target parser
5cf20e1281598933a20d7832a178895e624d6a42  parser tests
44628e625d9cb9d4aa6a73d8c229f732611fe63a  CLI integration
bc028f28be629717c634a3cb4b79895ddaac5fc2  CLI orchestration tests
```

## Step 1 validation completed

Ali ran the complete deterministic suite:

```text
Ran 72 tests
OK
```

The first live CLI attempt failed with HTTP 401 because a stale or invalid non-empty `GITHUB_TOKEN` was present. Network reachability was available. After:

```bash
unset GITHUB_TOKEN
```

the public command completed anonymously:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

The complete installed command preserved:

- exact PR identity and changed file;
- one supported pinned pytest update;
- exact-head workflow, job, step, and command evidence;
- sufficient bounded CI authority;
- exact PyPI package and file identity;
- provenance coverage;
- exact upstream GitHub release and tag;
- `unresolved_claim` as the semantic stopping state.

Target result:

```text
Target Python declaration: project_table_absent
Target Python source: pyproject.toml @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Target Python blob SHA: 38d6a9efc4b94e2b733d3bbb848156449814ec94
```

This was correct because the file was valid TOML but had no PEP 621 `[project]` table. Black's `target-version` was correctly not promoted into project declaration evidence.

Validation records:

```text
3f865529a77b001a8b70c4c0ea962f5bec3e3564  full validation evidence
f30c3a424f951cc6a8558bd1bad1791b86257efc  Step 1 closure in MEMORY.md
```

Step 1 is fully behavior-validated at:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

## Deterministic range-method decision

Ali agreed that UpgradePilot should use the maintained `packaging` implementation rather than write a general PEP 440 parser from scratch.

Selected direction:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
```

Reason:

- PEP 440 includes compound specifiers, exclusions, wildcards, compatible-release operators, patch boundaries, pre-releases, and other edge cases;
- a local general parser would create unnecessary correctness and maintenance risk;
- `packaging` is the standards-aligned implementation used by Python packaging tooling.

Important separation:

```text
packaging owns standards-correct parsing and candidate membership
UpgradePilot owns the product meaning of Python-line overlap
```

Accepted product meaning:

```text
declared_python_overlap
= at least one stable Python X.Y.Z release is admitted by requires-python
```

The exact existential algorithm is not yet frozen. It must not rely on arbitrary finite patch enumeration without a completeness argument. Unsupported semantics must produce `comparison_unsupported`.

No `packaging` dependency has yet been added to product source.

## Upstream claim contract and Instructor

The session clarified that Instructor is related to the upstream claim contract, but does not own it.

Potential Instructor responsibility:

```text
Pydantic response model
→ JSON Schema request construction
→ LM Studio OpenAI-compatible request
→ typed Pydantic parsing
→ optional mechanical validation context and diagnostics
```

Instructor is not:

- the model;
- semantic truth;
- grounding authority;
- source authority;
- range evaluator;
- target relevance evaluator;
- evidence-sufficiency policy;
- maintainer decision engine.

The product requires two distinct layers:

```text
CandidateUpstreamClaimResult
→ untrusted model-facing structured result

GroundedPythonSupportDropClaim
→ deterministically validated comparator input
```

The trusted support-drop input must preserve:

```text
category = support_boundary_change
change_state = support_dropped
normalized Python X.Y
exact source identity
exact contiguous source quote
old dependency version
proposed dependency version
```

Controlled comparator tests must construct the trusted type directly without LM Studio, Instructor, or an LLM. Instructor, Pydantic, OpenAI client, and a selected model remain separate adapter/deployment decisions.

## Existing product-simulation case identified

No new simulation case is currently needed. Historical scenario S001 already contains the desired semantic contrast:

```text
target: pydantic/pydantic
PR: 13432
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
dependency: soupsieve
update: 2.6 → 2.8.4
```

Exact target evidence at the PR head:

```toml
[project]
requires-python = ">=3.10"
```

Target `pyproject.toml` blob:

```text
8271997ab85caa1af522954812a2749784432dc7
```

Exact tagged upstream changelog evidence:

```text
2.8:
Drop support for Python 3.8.
```

Expected first relevance result:

```text
outside_declared_python_range
```

This proves only that Python 3.8 is outside Pydantic's declared installation range at the exact PR head. It does not prove compatibility, safety, or merge authorization.

S001 remains completed historical discovery evidence. A future current-product execution should reacquire its exact identities and use it as the first automated proof case without reopening or rewriting the simulation.

## Upstream source-boundary gap discovered

S001 exposed a material gap in the previous final-release-only semantic source boundary.

The update crosses:

```text
2.6 → 2.8.4
```

The Python support drop appears in the 2.8 changelog section, while the exact 2.8.4 release body contains only 2.8.4 fixes.

Therefore:

```text
proposed-version release body only
→ can miss a material change introduced in an intermediate crossed release
```

The required upstream responsibility is now:

```text
authoritative changes for:
old_version < release <= proposed_version
```

Admitted bounded source priority:

1. exact GitHub Release bodies for relevant crossed releases when identities and ordering are established;
2. exact tagged upstream changelog at the proposed tag, preserving version section, path, revision, and blob;
3. package metadata as corroboration where applicable.

Dependabot release-note copy may locate or corroborate a claim, but must not silently replace authoritative upstream evidence. Arbitrary source search and model-selected authority remain prohibited.

## Temporary CLI-order debt

The current CLI performs target Python acquisition immediately after identifying a supported dependency update:

```text
supported dependency update
→ target pyproject.toml acquisition
→ CI evidence
→ package evidence
→ upstream release evidence
```

This was acceptable as a temporary Step 1 implementation order because target acquisition needed isolated proof.

It is not the intended final activation order. Target Python investigation is conditional work and should run only after a grounded upstream Python support-drop claim exists.

Required final semantic order:

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

The final CLI must expose non-activation explicitly. It must not read `pyproject.toml` for every supported dependency update merely because the parser exists.

Do not refactor this order before the upstream contract, interval authority, and comparator inputs are frozen enough to preserve existing product behavior and tests.

## Plan audit and revision

The existing [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md) remains the correct owner. Creating a parallel plan would duplicate responsibility.

The plan was revised to include:

- old-version-exclusive/proposed-version-inclusive upstream interval semantics;
- admitted upstream source authority and provenance;
- the two-layer candidate/trusted claim contract;
- Instructor's bounded adapter role;
- the accepted `packaging` direction;
- stable Python-line overlap meaning and algorithm proof requirement;
- conditional target-investigation activation;
- the temporary versus required CLI order;
- S001 as the first end-to-end proof case;
- revised work sequence, proof obligations, rejection conditions, and stop line.

Plan revision:

```text
ff3936939020acd1a9f033e1296b3b5633f649da
```

## Current exact continuation

1. Review and accept the revised controlling plan.
2. Record the durable `packaging` dependency/method decision in the appropriate owner; create an ADR only if required by the repository's cross-cutting dependency rules.
3. Freeze the upstream interval/source evidence types and unresolved states.
4. Freeze `CandidateUpstreamClaimResult` and `GroundedPythonSupportDropClaim` independently of Instructor or model runtime.
5. Freeze the exact `packaging`-based stable Python-line overlap algorithm, including unsupported cases and proof against incomplete enumeration.
6. Implement deterministic comparison using manually constructed trusted claims first.
7. Use S001 fixtures to prove:

```text
Python 3.8 support dropped
+ target requires-python >=3.10
→ outside_declared_python_range
```

8. Implement bounded authoritative upstream interval acquisition for S001.
9. Evaluate whether semantic extraction is required and, if so, compare the bounded Instructor adapter without treating it as automatic adoption.
10. After claim extraction and comparison are validated, move target Python acquisition behind the valid support-drop activation condition.
11. Run S001 through the complete current product path.
12. Stop before compatibility, safety, evidence-sufficiency, or maintainer-action policy.

## Not authorized yet

Do not yet implement:

- a home-grown general PEP 440 parser;
- an unreviewed or unbounded `packaging` dependency addition;
- Instructor, Pydantic, OpenAI client, or LM Studio integration into the active package;
- arbitrary changelog/document search;
- model-selected source authority;
- support-added or broad release-semantic extraction;
- compatibility or safety conclusions;
- merge, targeted-check, investigate, defer, or abstain policy from this relevance result;
- target repository mutation.
