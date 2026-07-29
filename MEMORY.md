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
- **Latest Step 1 evidence:** [`working-memory/2026-07-29_B2-target-python-declaration-step-1.md`](working-memory/2026-07-29_B2-target-python-declaration-step-1.md)
- **Latest semantic review:** [`working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md`](working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-independent-review.md)

The local-LLM semantic experiment remains paused after a successful narrow v1.3 correction. No model, prompt contract, provider, or model runtime has been adopted into product source.

Target-relevance Step 1 has source and controlled-test implementation:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

The focused controlled reconstruction passed 12 relevant tests. One connector-backed exact-revision public file check produced the expected `project_table_absent` result. The complete repository suite and one full installed-command execution have not yet been run for these commits, so Step 1 is not yet the new fully behavior-validated product revision.

## Established product boundary

The last fully behavior-validated product revision reaches:

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

Implemented but awaiting full-repository validation:

```text
supported dependency change
→ exact-head pyproject.toml
→ available or explicit target-declaration problem state
→ concise CLI target evidence
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

The implemented target evidence states are:

```text
available
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

`requires-python` establishes only a declared Python installation-version specifier at one immutable revision. It does not establish CI execution, production runtime, active testing, affected dependency usage, compatibility, safety, or a maintainer action.

The public exact-revision check used:

```text
repository: googlefonts/glyphsLib
revision: f3cda8a94600e58d27f1bc17c99b7693718b6350
path: pyproject.toml
blob: 38d6a9efc4b94e2b733d3bbb848156449814ec94
result: project_table_absent
```

The file's Black `target-version` setting was correctly not treated as a PEP 621 project declaration.

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

## Current validation gap

The Step 1 source and controlled tests exist, but this session could not run a direct Git checkout. The repository also reported no workflow runs for the direct commits.

Therefore the following remain required before Step 1 is treated as fully behavior-validated:

1. run the complete repository test suite from the actual checkout;
2. run one complete read-only UpgradePilot command through the installed package;
3. inspect the target declaration output and confirm existing PR, CI, package, and upstream behavior remains intact;
4. preserve the exact commands, outputs, and revision in dated evidence.

The previous fully reported product-suite result remains 64 passing tests at the earlier behavior-validated revision.

## Exact continuation

From a clean current repository checkout:

1. synchronize `main` without rewriting or discarding work;
2. run the complete deterministic suite:

```text
python -m unittest discover -s tests -v
```

3. if the suite passes, run the installed public command for the existing S004 control:

```text
upgradepilot googlefonts/glyphsLib 1145
```

4. independently inspect the raw output and confirm:

```text
target file requested at the PR head SHA
→ target declaration: project_table_absent
→ no range comparison
→ no compatibility or safety claim
→ existing CI, package, and upstream evidence still presented
```

5. record the full-suite and command evidence in a dated working-memory file;
6. update `MEMORY.md` only after that review establishes the new behavior-validated revision;
7. stop and present the deterministic Python range-method alternatives to Ali for a separate decision.

Do not implement yet:

- a Python version-range evaluator;
- an upstream support-drop input or model adapter;
- renewed prompt tuning;
- LLM product integration;
- relevance-to-decision policy;
- any new runtime dependency.

## Relevant revisions

```text
last fully behavior-validated product revision:
bc5aafece111802f1e777dd2b8151ccad1fd822e

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

Step 1 execution evidence:
c316357e87f8c0335333d4387f191a1dc9a82203
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its own stable responsibility or dated evidence changes.
