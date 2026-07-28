# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Completed bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Selected supporting re-evaluation plan:** [`plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)
- **Detailed evidence walkthrough:** [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- **Decision synthesis record:** [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- **Upstream semantic-boundary proposal:** [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- **Local LM Studio re-evaluation record:** [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)
- **Last behavior-validated repository revision in Ali's environment:** `bc5aafece111802f1e777dd2b8151ccad1fd822e`.
- **CLI integration validation closure:** `4ff281565593f5e74f5f79491497c9b36363050f`.
- **Transparent-decision plan revision:** `2a6664f4fae17583afdfcdd59889f5fa3cd0ef06`.
- **Evidence walkthrough latest revision:** `27a72c5a36501eca16eca946777f1f4253d8232c`.
- **Decision synthesis revision:** `71e0a14735c39aceccd476412f746b21a5a3dce6`.
- **Semantic-boundary proposal revision:** `5b553602e9777292e8fb9359237aa55ea689d55e`.
- **Local-LM re-evaluation plan revision:** `010f667293d6acdfc71841200737a5b1c7e3dfc7`.
- **Local-LM working-record revision:** `3ffc59600e83625ea2fde55a6f9712bfaf2fb083`.

B2 Increment D — Minimum package and upstream evidence — is complete. B2 Increment E — Transparent decision — remains selected under its dedicated bounded plan. Ali approved proceeding with a bounded local-LLM experiment direction, not automatic model adoption. The re-evaluation must preserve the prior UpgradePilot rejection of `gemma-4-e2b-it` and `qwen3-4b-instruct-2507`, compare current candidate deployments against that negative evidence, and earn adoption through semantic, grounding, and downstream decision-effect proof. Current LM Studio environment inventory is the immediate blocker. No semantic interpretation method, decision contract, recommendation policy, active model/provider dependency, or recommendation code has yet been approved or implemented.

Ali should continue to be onboarded through the real evidence-to-decision and model-evaluation paths. Explain every new model, configuration, schema, failure category, measurement, and transition through the concrete responsibility it serves.

## Verified integrated product evidence

Observed in Ali's WSL2 Python 3.12 environment after pulling revision `bc5aafece111802f1e777dd2b8151ccad1fd822e`.

### Complete deterministic suite

```text
Ran 64 tests in 0.021s
OK
```

This includes the four CLI orchestration tests and the previous 60 source, acquisition, parsing, identity, reconciliation, and CI-authority tests.

### Integrated public command

```text
command: python3 -m upgradepilot googlefonts/glyphsLib 1145
repository: googlefonts/glyphsLib
PR: 1145
exact dependency: pytest 9.0.2 → 9.0.3
exact head: f3cda8a94600e58d27f1bc17c99b7693718b6350
CI authority: sufficient
package evidence: available
published package: pytest==9.0.3
distribution files: 2
upstream source: available
upstream repository: pytest-dev/pytest
provenance coverage: 2 of 2 files
provenance unavailable files: none
accepted tag: 9.0.3
release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
claim state: unresolved_claim
```

The command preserved all previously validated PR, dependency, workflow, job, and CI-authority output and continued through package and upstream evidence in one execution.

## Permitted claims

### CI authority

> At least one successful exact-head CI path installed the changed requirements file and directly exercised pytest.

### Package identity

> PyPI published an exact release record for `pytest==9.0.3`, including the exact wheel and source-distribution identities and SHA-256 digests.

### Upstream source authority

> PyPI reports provenance for both exact `pytest==9.0.3` distribution files identifying `pytest-dev/pytest`; that repository agrees with the package's well-known Source candidate; and the exact `9.0.3` tag resolves to a published GitHub Release and exact tag-reference object.

### Integrated product path

> The public UpgradePilot command behavior-validly connects exact PR and dependency identity, bounded exact-head CI authority, exact PyPI package/file identity, PyPI-reported publisher provenance, matching upstream repository identity, and an exact GitHub Release/tag reference into one concise evidence report.

These claims do not establish:

- independent cryptographic verification of the PyPI attestation envelopes;
- complete CI coverage;
- release-prose meaning;
- target-repository compatibility or objective upgrade safety;
- a merge, targeted-check, investigate/block, defer, or abstain recommendation.

## Behavior-validated boundary

```text
public repository + PR number
→ validated locator and exact PR identity
→ complete changed-file acquisition
→ one supported exact pinned Python dependency update
→ exact-head workflow runs, jobs, and steps
→ exact-run workflow path
→ workflow definition at the same head SHA
→ bounded command evidence
→ sufficient, insufficient, or unresolved CI authority
→ trusted exact package + proposed version
→ official PyPI exact-release request
→ normalized package and exact-version validation
→ immutable distribution filename, URL, package type, and SHA-256 records
→ publisher-supplied project-link candidates
→ bounded per-file PyPI Integrity acquisition
→ PyPI-reported publisher identities
→ one canonical GitHub Source candidate
→ Source candidate and publisher repository agreement
→ accepted exact-version tag form
→ published GitHub Release
→ exact tag-ref object type and SHA
→ bounded release body
→ concise public CLI presentation
→ unresolved_claim; no semantic interpretation or recommendation
```

## Current implementation responsibilities

```text
json_contract.py       source-neutral JSON runtime value contracts
pypi_api.py            shared bounded mechanics for focused PyPI JSON clients
pypi_client.py         exact package/version and immutable distribution-file evidence
pypi_provenance.py     exact-file PyPI-reported provenance and publisher identities
github_api.py          GitHub HTTP/JSON boundary and GitHub-specific contract adapters
github_client.py       PR identity and changed files
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head repository-file acquisition
github_release.py      published release and exact tag-ref evidence
upstream_source.py     source/provenance/repository/version reconciliation
dependency_change.py   dependency interpretation
workflow_commands.py   bounded workflow command reading
ci_authority.py        deterministic CI-authority classification
cli.py                 complete evidence-stage orchestration and concise presentation
```

No source module yet owns release-claim interpretation, evidence sufficiency, investigation stopping, or maintainer-action evaluation.

## Accepted authority boundaries

### Shared mechanics rule

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

### Upstream source rule

```text
PyPI exact package/version/file identity
+ PyPI-reported exact-file publisher provenance
+ matching canonical GitHub Source candidate
+ one exact-version GitHub Release/tag reference
```

Stable constraints:

- project URL labels identify candidate intent only;
- a Source candidate alone is not upstream authority;
- provenance is queried for every exact distribution file;
- at least one usable exact-file provenance record is required;
- all usable GitHub publisher repositories must agree;
- valid non-GitHub provenance is unsupported, not malformed;
- Source and provenance repository identities must match;
- exactly one of `<version>` or `v<version>` may resolve;
- tag-reference object type and SHA are preserved;
- release body meaning remains unresolved in current code;
- UpgradePilot does not independently verify attestation cryptography;
- compatibility, safety, and final recommendation remain unestablished.

## Increment D completion

The completed minimum package and upstream evidence plan reached its stop line:

- exact package/version evidence is exposed through the public command;
- project-controlled exact-release source evidence is exposed through the public command;
- explicit unavailable, unsupported, mismatched, ambiguous, malformed, and acquisition-failed states are preserved;
- no package-specific runtime answer or recommendation was introduced;
- deterministic and live proof both passed.

The completed plan must not be extended informally into semantic interpretation.

## Increment E selected responsibility

The selected transparent-decision plan controls the movement from validated evidence to one bounded maintainer action or abstention:

```text
validated evidence
→ bounded decision-relevant interpretation
→ evidence sufficiency and stopping
→ maintainer action or abstention
→ reasons, uncertainty, required checks, and claim limits
```

The stable product responsibility remains broader than S004. S004 is the first control and live-proof candidate, not the product scope or hidden expected answer.

### Design progress recorded

The concrete evidence walkthrough now classifies:

- exact dependency/change identity as an admission requirement;
- direct successful exact-head dependency exercise as target-specific decision support;
- package/provenance/source/release binding as an authority prerequisite;
- filenames, historical merge status, and unclassified version shape as context rather than decision authority;
- contradiction evaluation, evidence sufficiency, stopping, and maintainer action as remaining unimplemented responsibilities.

The first contract draft proposes typed decision inputs, an explainable decision result, charter-aligned action vocabulary, evidence-readiness distinctions, a stopping rule, and materially different contrast cases.

The semantic-boundary proposal adds:

- four upstream claim categories: `fix_or_remediation`, `compatibility_assurance`, `interface_or_behavior_change`, and `support_boundary_change`;
- semantic states: `resolved`, `no_decision_relevant_claim`, `unresolved`, and `conflicting`;
- source-span grounding and deterministic validation invariants;
- a proposal to use the already acquired exact GitHub Release body as the first semantic source and not add pytest-specific release-document searching;
- a proposal that explicit compatibility assurance is supporting rather than universally mandatory for ordinary review;
- deterministic phrase matching as a disposable baseline only;
- bounded local LLM structured extraction with deterministic validation as the selected experiment direction, not yet adopted product behavior;
- deterministic sufficiency, stopping, and maintainer-action evaluation remaining outside model control.

The local-LM re-evaluation records add:

- the prior M2 local deployments and their decision-effect failures as controlling negative comparison evidence;
- Sentinel's environment, WSL2, timeout, model-routing, and token-budget lessons as operational reference only;
- current LM Studio JSON-Schema, model-management, logging, and load-estimation capabilities;
- a direct-HTTP, OpenAI-client, LM Studio SDK, and LangChain transport comparison;
- exact environment inventory and model eligibility requirements;
- a broader four-category corpus, repeated critical-case scoring, and adoption/rejection gates;
- an explicit prohibition on restoring archived M2 source or treating schema-valid output as semantic success.

The local LLM experiment direction is approved. Candidate model, quantization, client/dependency, source input limit, schema representation, ADR, and product adoption remain unresolved.

## Exact continuation

Follow [`plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md) under the parent transparent-decision plan. Do not implement recommendation code or active semantic product code yet:

1. Ali runs the read-only Windows PowerShell and WSL2 environment-capture commands in [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md);
2. preserve the LM Studio version/server status, downloaded and loaded model JSON, GPU state, and exact WSL2 `/v1/models` reachability result;
3. inspect the inventory and select at most three eligible local candidate deployments; do not download a new model without Ali's explicit approval after inventory review;
4. run `lms load --estimate-only` for candidate context/offload configurations and freeze one serial load configuration per candidate;
5. choose the smallest experiment transport after comparing direct `requests`, the OpenAI client, and LM Studio SDK; reject LangChain/agent orchestration unless new evidence proves a missing responsibility;
6. perform one strict non-streaming JSON-Schema smoke request per candidate and preserve diagnostics and LM Studio logs;
7. freeze expected claims and downstream effects for the broader four-category semantic corpus before scored runs;
8. implement only the minimum experiment harness required for repeated semantic, grounding, and decision-effect measurement;
9. compare results with the historical rejected deployments and present an adopt, retain-as-experiment, reject, defer, or reconsider-method decision to Ali;
10. create an ADR and active product implementation only after explicit adoption approval;
11. do not begin Increment F machine-readable/replay expansion until the transparent decision boundary is behavior-validated.

## Product boundaries affecting continuation

Do not yet:

- independently claim cryptographic attestation verification;
- search arbitrary tag patterns or package-specific release paths;
- recursively search repository trees without a separately admitted source-format rule;
- interpret release prose through package-specific phrases or fixture wording;
- produce compatibility, safety, merge, targeted-check, investigate/block, defer, or abstain recommendations before the decision method is approved;
- treat the historical maintainer merge, manual S004 answer, or previous model outputs as correctness proof;
- hardcode pytest, version `9.0.3`, the known release URL, announcement path, control-case wording, or expected outcome;
- restore or import archived M2 source, tests, classes, Pydantic/OpenAI dependencies, or decision rules;
- download a new local model without Ali's explicit approval after inventory review;
- add an active model/provider dependency, semantic service, persistence, replay infrastructure, agents, queues, RAG, embeddings, or deployment layers before method evidence and adoption approval;
- enable LM Studio CORS for the Python/WSL2 flow or expose the server beyond localhost without reviewing authentication and firewall boundaries;
- mutate a target repository or require private access.

## Detailed dated evidence

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)
- [`working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md`](working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md)
- [`working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md`](working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md)
- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- [`working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md`](working-memory/2026-07-28_B2-local-lm-studio-semantic-reevaluation.md)

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when that file's stable route, requirement, decision, source behavior, test behavior, or dated historical evidence changes.
