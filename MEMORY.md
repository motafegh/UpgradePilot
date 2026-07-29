# UpgradePilot Current Memory

**Last updated:** 2026-07-29  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Parent decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected bounded plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 1 implementation evidence:** [`working-memory/2026-07-29_B2-target-python-declaration-step-1.md`](working-memory/2026-07-29_B2-target-python-declaration-step-1.md)
- **Step 1 full validation:** [`working-memory/2026-07-29_B2-target-python-declaration-full-validation.md`](working-memory/2026-07-29_B2-target-python-declaration-full-validation.md)
- **Latest semantic review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md)

The local-LLM semantic experiment remains paused after a successful narrow v1.3 correction. No model, prompt contract, provider, or model runtime has been adopted into product source.

Target-relevance Step 1 is fully behavior-validated at revision `75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15`:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

The complete deterministic suite passed 72 tests. One complete installed public read-only command preserved the existing PR, dependency, CI-authority, package, provenance, and upstream-release evidence while producing the expected `project_table_absent` target state.

## Established product boundary

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

Not established:

- adopted release-prose interpretation;
- reliable Python support-drop extraction with normalized `python_line`;
- deterministic Python specifier evaluation;
- target-repository relevance for an upstream change;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action;
- model or product adoption.

## Target declaration responsibility

The admitted target source is only:

```text
pyproject.toml at PullRequestIdentity.head_sha
→ [project].requires-python
```

The behavior-validated target evidence states are:

```text
available
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

`requires-python` establishes only a declared Python installation-version specifier at one immutable revision. It does not establish CI execution, production runtime, active testing, affected dependency usage, compatibility, safety, or a maintainer action.

The public full-command validation used:

```text
repository: googlefonts/glyphsLib
PR: 1145
revision: f3cda8a94600e58d27f1bc17c99b7693718b6350
path: pyproject.toml
blob: 38d6a9efc4b94e2b733d3bbb848156449814ec94
result: project_table_absent
```

The file's Black `target-version` setting was correctly not treated as a PEP 621 project declaration. No range comparison or compatibility claim followed.

## Live-command authentication observation

The first installed-command attempt received HTTP 401 because a stale or invalid non-empty `GITHUB_TOKEN` was present. Network reachability was available. After:

```bash
unset GITHUB_TOKEN
```

the same public read-only command completed anonymously.

For public commands, the current safe operational form when a local token is known to be invalid is:

```bash
env -u GITHUB_TOKEN upgradepilot <owner/repository> <pull-number>
```

The token value was not exposed. No authentication behavior change is selected. Silently retrying anonymously after credential rejection is not authorized because it could conceal a credential or permission problem.

## Frozen model responsibility

The experimental model may propose bounded, explicitly attributed candidate claims from authoritative release text. It does not select authority, target relevance, evidence sufficiency, stopping, safety, or maintainer action.

Supported experimental categories remain:

```text
fix_or_remediation
→ fixed

compatibility_assurance
→ compatibility_assured

support_boundary_change
→ support_added | support_dropped

interface_or_behavior_change
→ deprecated | removed | future_removal | changed_unspecified
```

Any other category/change-state pair is invalid.

The v1.3 claim-partition correction passed its exact compatibility-assurance case 3/3 and remains retained in the experimental contract. It does not establish broad release-note reliability or Python support-drop extraction.

Further sentence-by-sentence prompt tuning remains paused. Prompt or model work may resume only when a concrete target-relevance case exposes an extraction blocker that deterministic validation cannot solve.

Deferred during this pause:

- remaining Gate B cases;
- Gate C;
- broader semantic corpus;
- Qwen or larger-model comparison;
- Instructor, Pydantic, or OpenAI runtime dependencies;
- LLM integration into the public command.

## Step 1 validation closure

The behavior-validated evidence is:

```text
complete deterministic suite: 72 passed
installed public command: completed
exact target revision and blob: preserved
target result: project_table_absent
range comparison: not performed
compatibility or safety claim: not made
existing evidence pipeline: preserved
```

Step 1 is closed. Do not add further target-declaration acquisition breadth merely because another source exists. Workflows, classifiers, tox configuration, documentation, deployment files, and tool-specific Python settings remain outside the admitted source unless a later selected uncertainty requires their own authority rules.

## Exact continuation

1. Present the deterministic Python specifier-range method alternatives to Ali.
2. Compare at least:

```text
A. standards-based PEP 440 evaluation
   → use a maintained implementation such as packaging.specifiers.SpecifierSet
   → broad standards alignment
   → new runtime dependency and its admission burden

B. deliberately narrow accepted grammar
   → support only explicitly selected simple requires-python forms
   → deterministic local implementation
   → abstain on every unsupported construct
   → risk of accidental partial PEP 440 reimplementation must remain controlled

C. no range comparison yet
   → keep target declaration as evidence only
   → return comparison_unsupported for every case
   → no dependency or parser risk, but no target-overlap value
```

3. Explain semantics for deciding whether a Python `X.Y` line is included by a declaration, including patch-version handling, pre-releases, exclusions, compatible-release operators, wildcards, and compound specifiers where applicable.
4. Compare correctness, authority, dependency cost, security and upgrade burden, failure modes, abstention behavior, test proof, and reversibility.
5. Obtain Ali's approval before selecting or implementing a range method.
6. After approval, record the bounded method decision in the appropriate owner; create an ADR only if the accepted dependency or method is durable and cross-cutting.
7. Stop before upstream support-drop input work until the range method is separately accepted and behavior-validated.

Do not implement yet:

- a Python version-range evaluator;
- a `packaging` or other runtime dependency;
- an upstream support-drop input or model adapter;
- renewed prompt tuning;
- LLM product integration;
- relevance-to-decision policy.

## Relevant revisions

```text
Step 1 fully behavior-validated product revision:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Step 1 full validation evidence:
3f865529a77b001a8b70c4c0ea962f5bec3e3564

v1.3 semantic evidence:
151f015edb698b95d9da69a7a463c7326818cb83

v1.3 independent review completed:
6565fa61053f48953768b9fef5805cb3169dd0d3

target relevance plan tightened:
9682c146feca4fceef28ece12844493a1e68b14d

target declaration parser:
89cb0ea4fa827aec6ed5504370d4c2a9e6f3a6e0

target declaration tests:
5cf20e1281598933a20d7832a178895e624d6a42

CLI target declaration integration:
44628e625d9cb9d4aa6a73d8c229f732611fe63a

CLI orchestration tests:
bc028f28be629717c634a3cb4b79895ddaac5fc2
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
