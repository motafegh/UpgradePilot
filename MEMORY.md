# UpgradePilot Current Memory

**Last updated:** 2026-07-29  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Parent decision plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected next bounded plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Latest semantic review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md)

The local-LLM semantic experiment is paused after a successful narrow v1.3 correction. No model, prompt contract, provider, or model runtime has been adopted into product source.

The target Python-support relevance plan is selected for review. Product implementation under that plan has not started.

## Established product boundary

UpgradePilot behavior-validly reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported exact pinned Python dependency update
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
- target-repository relevance for an upstream change;
- target-repository compatibility or objective safety;
- evidence sufficiency or stopping;
- merge, targeted-check, investigate/block, defer, or abstain action.

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

## Verified semantic evidence

### State-contract v1.2 Gate A

The exact weak behavior-change case passed 3/3:

```text
Compatibility behavior was adjusted for older environments.
→ resolved
→ interface_or_behavior_change / changed_unspecified
```

This establishes repeatability only for that frozen case.

### State-contract v1.2 Gate B

The generic behavior-change contrast passed.

The compatibility-assurance case failed because Gemma emitted one correct claim and one invalid extra claim:

```text
correct: compatibility_assurance / compatibility_assured
invalid extra: support_boundary_change / compatibility_assured
```

The failure was classified as claim over-partitioning plus an invalid category/change-state pair.

### State-contract v1.3 correction

The exact compatibility-assurance case passed 3/3 after adding one claim-partition rule:

> Emit one claim per distinct supported category/change-state proposition. Combine clauses that jointly support the same proposition.

Independent raw-evidence review confirmed:

```text
clean preflight: passed
same prompt/schema/request identity: confirmed
finish_reason: stop for all three
structure validation: passed
semantic oracle evaluated: true
semantic oracle: passed
post-unload loaded models: none
product tests: 64 passed
manifest: 134/134 verified
```

## What v1.3 establishes

The corrected rule prevents the exact backward-compatible/no-migration sentence from being split into an invalid second claim.

It supports retaining that rule in the experimental contract.

## Detected gaps

The semantic experiment has not established:

1. broad release-note reliability;
2. reliable Python-version support-drop extraction;
3. a normalized Python `X.Y` value usable by deterministic comparison;
4. target-side Python declaration acquisition;
5. a selected deterministic Python specifier evaluator;
6. target relevance;
7. evidence sufficiency or maintainer action;
8. model or product adoption.

The current experimental claim schema contains a free-text subject, not the dedicated normalized `python_line` required by the target-relevance comparator.

The remaining frozen Gate B cases and Gate C were not completed under v1.3.

## Prompt-tuning pause decision

Further sentence-by-sentence prompt tuning is paused.

Reason:

```text
The extractor has been improved for isolated synthetic cases,
but UpgradePilot still cannot show whether an extracted claim
matters to the target repository.
```

Continuing prompt work now would optimize an isolated component before proving product value. Prompt or model work may resume only when a concrete target-relevance case exposes an extraction blocker that deterministic validation cannot solve.

Deferred during this pause:

- remaining Gate B cases;
- Gate C;
- broader semantic corpus;
- Qwen or larger-model comparison;
- Instructor, Pydantic, or OpenAI runtime dependencies;
- LLM integration into the public command.

## Selected target-relevance responsibility

The next bounded question is:

> When an authoritative upstream release explicitly states that support for Python `X.Y` was dropped, does the target repository's exact-head `[project].requires-python` declaration include that Python line?

First upstream scope:

```text
support_boundary_change / support_dropped
+ normalized Python X.Y
+ exact source quote
```

First target source:

```text
pyproject.toml at PullRequestIdentity.head_sha
→ [project].requires-python
```

This source was selected because the existing repository client already reads bounded UTF-8 files at the immutable PR head, and Python 3.12 provides `tomllib` without a new dependency.

Authority limit:

`requires-python` establishes a declared installation-version specifier. It does not establish CI execution, production runtime, active testing, affected dependency usage, compatibility, safety, or a maintainer action.

The first relevance outcomes are limited to:

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

## Plan status and implementation boundary

The target-relevance plan was audited and tightened to:

- start with support drops only;
- use declared range rather than claiming exercised support;
- preserve explicit target evidence failures;
- require a separate range-method decision;
- reject safety language;
- stop if the narrow evidence does not affect a later decision.

No source or test implementation has been performed for this plan.

## Exact continuation

1. Present the audited target-relevance plan to Ali with its purpose, evidence meaning, limits, sequence, and detected risks.
2. Do not implement until Ali has reviewed the plan.
3. After approval, implement only Step 1:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

4. Stop before implementing:

- a Python version-range evaluator;
- an upstream support-drop adapter;
- renewed prompt tuning;
- LLM product integration;
- relevance-to-decision policy;
- any new runtime dependency.

Those require the evidence from Step 1 and a separate bounded method decision.

## Relevant revisions

```text
last behavior-validated product revision:
bc5aafece111802f1e777dd2b8151ccad1fd822e

v1.3 evidence:
151f015edb698b95d9da69a7a463c7326818cb83

v1.3 independent review created:
479f6ebe453bc9c20bb83bb30a78f7110644614a

v1.3 independent review completed:
6565fa61053f48953768b9fef5805cb3169dd0d3

target relevance plan created:
434095c78b982568f1459ee918f0caaa5c11c3fa

target relevance plan tightened:
9682c146feca4fceef28ece12844493a1e68b14d
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.