# Case Candidate Screening 01

- **Status:** Proposal-support screening record — non-controlling
- **Owner:** Ali Rajabi
- **Recorded:** 2026-08-06
- **Scope:** bounded first pilot of the proposed case-selection matrix across real, real-derived, control, reserve, reject, and synthetic candidates
- **Authority:** none
- **Admission effect:** none — this record does **not** assign `S006`, admit a new case, change governance, change the active route, change implementation, or update `MEMORY.md`

## 1. Why this screening exists

The proposal package defines a hybrid case program and a weighted case-selection matrix. Before treating that machinery as useful, this pilot tests whether it actually distinguishes materially different candidate situations instead of rewarding every large dependency update.

The primary search objective for this pilot was intentionally demanding:

```text
real upstream behavior/API change
→ exact activation condition
→ affected target path demonstrably present
→ existing tests/CI do not already close the question
→ one specific additional investigation/check can distinguish meaningful outcomes
```

The central uncertainty for the Priority-1 search was:

> Can UpgradePilot identify a concrete upstream dependency behavior change that intersects a real target-repository code path, recognize whether existing evidence already covers that behavior, and recommend a narrowly targeted check only when the current evidence is insufficient?

This is narrower than “find a scary major-version bump.” A candidate that fails one of the links above is still useful if the failure teaches us something about case selection, but it should not be promoted into the wrong case family.

## 2. Capture boundary

This record is a research snapshot, not live project state.

At the beginning of the final screening pass:

- current `main` was observed at `5ef46e4352814528080cc179d91b58c1e54b45c8`;
- this proposal branch was at `24a6a699307c31636cc5620c840f4e809a4d4975` before this file was added;
- comparison reported the branch as **4 commits ahead and 553 commits behind** current `main`;
- the merge base remained `9e9308eee5d33d8d9fedca56308ed10f2ae32d38`.

That divergence is intentional for this research branch. Nothing in this file should be used as a substitute for current `MEMORY.md`, current route plans, or current implementation facts.

## 3. Screening rules used

The mandatory gates from `CASE_SELECTION_AND_COVERAGE_MATRIX.md` were applied before score interpretation:

1. named uncertainty;
2. existing-case gap;
3. product consequence;
4. safe boundary;
5. evidence feasibility;
6. honest negative-result value;
7. stop condition;
8. claim boundary;
9. correct case form;
10. synthetic realism basis when artificial evidence is used.

The weighted score is a comparison aid only. Mandatory gates override the numeric score.

This pilot also applied three stricter practical rules:

- **Target-owned activation only.** Vendored dependency source does not count as target usage.
- **Configured coverage is not executed coverage.** A workflow that is configured to run a path is evidence of intended coverage, but historical green/red status is not claimed when retained run data is unavailable.
- **One central uncertainty per candidate.** If dependency-graph conflict, acquisition failure, or another stronger uncertainty dominates, the candidate is reclassified instead of being forced into the direct-behavior family.

## 4. Candidate register

| ID | Candidate | Origin / role | Primary result | Indicative score | Recommendation |
| --- | --- | --- | --- | ---: | --- |
| C01 | `eduardoklosowski/qldebugger#27` Pydantic 1.10 → 2.x | untouched real / behavior comparator | exact behavior activation exists, but an exact target test already closes it | 64 | regression/control; do not admit as new discovery |
| C02 | qldebugger real-derived coverage-gap variant | real-derived / targeted-check isolation | same real behavior activation, with one controlled variable: the exact discriminating test is absent | 71 | strongest Priority-1 design candidate; blueprint only |
| C03 | `kubernetes-client/python#2106` urllib3 <2 → <3 | untouched real / reclassification | urllib3 is core transport, but a newly established dependency-graph/installability constraint dominates | 65 | reserve for graph/authority family |
| C04 | `cobrateam/splinter#1160` urllib3 <2 → <3 | untouched real / ordinary control | direct transport customization exists, but no exact removed-API trigger was found and relevant real integration coverage is configured | 36 | regression-only control |
| C05 | `pypa/pip-audit#620` urllib3 <2 → <3 | untouched real / corroborator | proposed change removes an explicit CacheControl/requests compatibility bound; duplicates graph-constraint uncertainty | early stop | reserve as corroborating evidence, not a new case |
| C06 | changed-head / supersession lifecycle blueprint | synthetic-authored / lifecycle validation | deterministic stale-evidence and rerun problem remains materially uncovered | 78 family score | strong later first-wave synthetic candidate; outside Priority-1 behavior track |

No candidate is admitted by this table.

---

# 5. C01 — qldebugger Pydantic 1.10 → 2.x

## Locator

- repository: `eduardoklosowski/qldebugger`
- PR: `https://github.com/eduardoklosowski/qldebugger/pull/27`
- proposal: `pydantic = "^1.10"` → `pydantic = ">=1.10,<3.0"`
- exact PR commit inspected: `a454b47b8e483dffc825a3c9998f38e7634ec93b`
- parent: `b9e24267507d29c364d32e60f2bdc6075d91c395`
- Dependabot metadata identifies Pydantic as `direct:production`.

## Exact upstream behavior predicate

Pydantic V2 changed validator exception handling:

> Raising `TypeError` inside a validator no longer produces a `ValidationError`; the `TypeError` is raised directly.

Primary upstream reference:

- `https://docs.pydantic.dev/2.3/blog/pydantic-v2-alpha/`

This is a substantially better activation predicate than “Pydantic 2 contains breaking changes.” It names the exact input condition and the observable output difference.

## Exact target activation

At the exact PR head, `src/qldebugger/config/file_parser.py` contains:

```python
from pydantic import BaseModel, Field, validator

class ConfigLambda(BaseModel):
    @validator('handler', pre=True)
    def _split_handler(cls, v: Any) -> Tuple[str, str]:
        if not isinstance(v, str):
            raise TypeError('should be a str')
```

The repository therefore has a target-owned V1 validator that deliberately raises `TypeError` under a concrete input condition.

## Existing target evidence

The exact same PR head also contains an exact test in `tests/qldebugger/config/test_file_parser.py`:

```python
with pytest.raises(ValidationError) as exc_info:
    ConfigLambda(handler=<non-string integer>)
```

The test then asserts a Pydantic V1-style `type_error` entry.

The PR-head workflow `.github/workflows/check-commit.yml` is configured to run `make test` on Python 3.8, 3.9, 3.10, 3.11, and 3.12. `make test` runs the repository test tree through pytest.

Historical check-run retention for this exact head is currently unavailable through the inspected API (`0` retained check runs), so this record does **not** claim that the historical workflow was green or red.

## Historical outcome

The PR was closed rather than merged. The final Dependabot comment says that Pydantic was no longer updatable and the PR was no longer needed. That historical closure does not independently establish why the Pydantic-2 behavior was or was not acceptable.

## Screening judgment

This is a **real, exact behavior intersection**, but it fails the intended Priority-1 discovery gap:

- upstream behavior change: **yes**;
- exact target activation: **yes**;
- direct production dependency: **yes**;
- exact target test for the changed behavior: **yes**;
- need for UpgradePilot to invent a missing targeted check: **no**.

The correct behavior for UpgradePilot here would be to recognize that the existing test is already highly discriminating and avoid inventing redundant verification.

### Recommendation

**Regression/control, not a new full discovery case.**

This candidate is especially valuable because it demonstrates that a high-quality behavior-impact detector must be paired with coverage reasoning. “Affected code found” is not enough to justify “add targeted tests.”

### Indicative score

Positive evidence is high because realism, exact activation, and evidence feasibility are unusually strong. The score is reduced by duplication/control value and, more importantly, the mandatory case-selection gate overrides the score because the named missing-check uncertainty is already resolved by existing evidence.

Indicative comparative score: **64 — promising evidence, but wrong admission outcome for the Priority-1 discovery question.**

---

# 6. C02 — qldebugger real-derived coverage-gap variant

## Purpose

C01 provides an unusually clean real anchor, but the untouched repository already contains the exact test UpgradePilot would ideally recommend. Instead of searching indefinitely for a public repository with the same behavior and an accidentally perfect coverage gap, a one-variable real-derived variant can isolate the product question.

## Pedigree

```yaml
case_origin: real_derived
evidence_origin:
  - captured_real
  - mutated_real
evaluation_role:
  - product_discovery
  - contract_validation
  - method_comparison
```

## Real anchor preserved

Preserve unchanged:

- exact qldebugger PR identity and dependency proposal;
- exact production source containing the Pydantic V1 `@validator`;
- exact non-string activation condition;
- upstream Pydantic V2 TypeError semantic change;
- normal surrounding test suite and project structure.

## One controlled variable

The only intentional change is:

> the exact test that asserts non-string `handler` input becomes a `ValidationError` is absent from the captured target baseline.

No production code is changed.

## Frozen independent oracle

Before any UpgradePilot implementation is evaluated, freeze these externally grounded expectations:

1. the target validator raises `TypeError` for non-string input;
2. under Pydantic V1 that exception is converted into `ValidationError`;
3. Pydantic V2 raises the `TypeError` directly;
4. therefore a targeted check using a non-string `handler` input discriminates the behavior change;
5. a generic import test or ordinary valid-config test does not establish this behavior.

The untouched C01 test supplies strong external evidence that this exact invalid-input contract mattered to the real target repository.

## What UpgradePilot should have to infer

A successful future method should be able to connect:

```text
Pydantic V2 TypeError validator change
→ qldebugger @validator target path
→ target intentionally raises TypeError for non-string handler
→ ordinary happy-path validation does not resolve exception-shape compatibility
→ recommend one non-string-handler validation check
```

The targeted check should be narrow enough to answer the compatibility question rather than defaulting to “run the whole test suite.”

## Claim boundary

This variant can test:

- behavior-change extraction;
- target activation reasoning;
- missing-coverage recognition;
- targeted-check planning;
- whether a suggested check is discriminating.

It cannot prove:

- how frequently real repositories miss this kind of test;
- that UpgradePilot would discover every Pydantic V2 incompatibility;
- that the synthetic coverage gap represents qldebugger’s actual historical coverage;
- production reliability.

## Recommendation

**Strongest Priority-1 design candidate from this pilot, but still only a blueprint.**

Do not assign `S006` from this record. If Ali later admits this candidate, it should be constructed as a clearly labeled real-derived case, with the untouched real qldebugger evidence retained beside it as the external-validity anchor.

Indicative comparative score: **71 — strong candidate if the real-derived form and claim boundary are explicitly accepted.**

---

# 7. C03 — kubernetes-client/python urllib3 <2 → <3

## Locator

- repository: `kubernetes-client/python`
- PR: `https://github.com/kubernetes-client/python/pull/2106`
- exact PR head: `8de1e769f71775ef6bb457ee62ae8228c9f65ad4`
- parent: `ae7b5ddd219fe09b6ed0be715dcca3377a029584`
- changed file: `requirements.txt`
- proposal: `urllib3>=1.24.2,<2.0` → `urllib3>=1.24.2,<3.0`

## Strong target relevance

At the exact head, `kubernetes/client/rest.py` directly:

- imports urllib3;
- constructs `PoolManager` and `ProxyManager`;
- passes TLS, retry, timeout, and hostname-related configuration;
- sends requests through urllib3;
- catches urllib3 SSL errors;
- wraps urllib3 responses;
- still calls `HTTPResponse.getheaders()` / `getheader()`, which urllib3 2.0 deprecated.

urllib3 is therefore not incidental in this repository. It is core transport machinery.

## Why this is not the Priority-1 behavior case

The parent commit of #2106 is the merge result of `kubernetes-client/python#2105`, merged one day earlier. #2105 explicitly added the `<2.0` upper bound because the dependency graph was not installable with urllib3 2.x through `google-auth` compatibility.

In other words:

```text
#2105: intentionally establish <2.0 compatibility boundary
#2106: immediately propose widening the same boundary to <3.0
```

That dependency-graph/installability fact is a more immediate and decisive uncertainty than the target’s downstream urllib3 API behavior.

Forcing this into the direct-behavior family would mix two questions:

1. can the environment resolve/install safely?;
2. if it can, do target runtime paths behave compatibly?

The case-selection model should separate them.

## Recommendation

**Reserve and reclassify.**

This is a strong candidate for a future dependency-graph / authority / conflicting-evidence case. It should not own the direct-behavior targeted-check uncertainty.

Indicative comparative score: **65**, but the correct-case-form gate prevents admission into the Priority-1 behavior family.

---

# 8. C04 — cobrateam/splinter urllib3 <2 → <3

## Locator

- repository: `cobrateam/splinter`
- PR: `https://github.com/cobrateam/splinter/pull/1160`
- exact proposal commit: `7f46679e227729ff649dc81222035dc9c7639550`
- pre-PR base: `e2a2c805f64363be131c9097e74630817c401ae8`
- merged as `5f4555d446b08e440781de1ca2c333141c4f4908`
- production requirement widened from urllib3 `<2.0` to `<3.0`.

## Real target usage

`splinter/driver/webdriver/remote_connection.py` imports urllib3, catches `MaxRetryError`, constructs a new `urllib3.PoolManager(timeout=...)`, and monkey-patches Selenium RemoteConnection request behavior.

`splinter/driver/webdriver/remote.py` installs that monkey patch into Selenium’s remote transport.

This is meaningful target-owned integration code.

## Coverage evidence

The exact workflow is configured to run a dedicated Selenium Remote job across Python 3.7–3.11. It starts a real Selenium server and runs `tests/test_webdriver_remote.py`, whose Remote browser classes inherit broad navigation tests such as visit, reload, redirect, back/forward, tab handling, and other webdriver operations.

Historical check-run data is no longer retained through the inspected API, so this record does not claim the historical jobs were green.

## Missing activation predicate

The screening pass did **not** find target-owned use of the clearest removed urllib3 2.0 APIs such as `Retry.method_whitelist` or `HTTPResponse.from_httplib`. The target uses urllib3 directly, but the major-version release notes alone do not establish that a removed API or changed behavior is activated by this repository.

## Recommendation

**Regression-only ordinary control.**

This candidate is valuable because it prevents a false selection rule:

> direct dependency + direct import + major release ≠ automatically a new discovery case.

Indicative comparative score: **36 — low-priority/regression-only.**

---

# 9. C05 — pypa/pip-audit urllib3 <2 → <3

## Locator

- repository: `pypa/pip-audit`
- PR: `https://github.com/pypa/pip-audit/pull/620`
- exact head: `0673f9c0515b6142e1fd4d977abe9b03fa8d5947`
- changed file: `pyproject.toml`

The patch removes this explicit compatibility bound:

```toml
# NOTE: constrained because CacheControl is incompatible with urllib3 ~= 2.0 by way of requests
urllib3 >= 1.26,< 2.0
```

and widens it to `<3.0`.

## Screening judgment

This provides independent real-world corroboration that urllib3 2.x proposals can collide with known transitive/dependency-graph compatibility constraints.

However, that is the same central family exposed more strongly by C03. Deep-investigating C05 as another full candidate would add acquisition cost without materially new decision evidence for this pilot.

## Recommendation

**Early-stop reserve as corroborating evidence.**

Do not assign a precise full score because the duplicate-family gate ended investigation early.

---

# 10. C06 — synthetic changed-head / supersession lifecycle blueprint

This candidate comes from the already proposed first-wave lifecycle family rather than the direct-behavior search.

## Scenario

```text
head A
→ acquire and analyze evidence for A
→ Dependabot PR rebases / changes to head B
→ previously acquired A evidence is now stale for the current PR head
→ system detects the mismatch
→ preserve run A and its provenance
→ start/recommend rerun for B
→ do not silently relabel A evidence as B evidence
```

## Pedigree

```yaml
case_origin: synthetic_authored
evidence_origin:
  - authored
  - generated
evaluation_role:
  - contract_validation
  - failure_validation
  - regression
```

## Independent invariants

Before implementation, freeze:

1. evidence belongs to an immutable exact revision;
2. a new PR head does not mutate the identity of the old run;
3. stale evidence cannot justify claims about the new head without explicit revalidation;
4. rerun/supersession lineage remains inspectable;
5. duplicate retry does not create contradictory “current” truth.

## Recommendation

**Strong later first-wave synthetic candidate.**

The existing matrix family score is approximately **78**. It remains outside the direct-behavior Priority-1 question, so this pilot does not promote it ahead of C02 solely because of score.

---

# 11. Search paths that were deliberately rejected

## 11.1 Requests 2.32 custom-adapter search

Requests 2.32 introduced a promising concrete family around custom `HTTPAdapter` behavior and connection/TLS-context handling. The search therefore looked for the intersection:

```text
real Requests 2.31 → 2.32 Dependabot PR
AND
repository-owned HTTPAdapter subclass/customization
```

Several update PRs were easy to find, but sampled target repositories such as `rtCamp/wp-cloud-atomic-sdk` and `DACCS-Climate/marble_client_python` did not expose the required adapter activation in the screening search.

The screening stopped instead of treating the package-level release note as target evidence.

## 11.2 urllib3 removed-API search

Global searches for identifiers such as `method_whitelist` produced many vendored copies of urllib3 itself. Those are not target-owned usage and were rejected as false activation evidence.

Repository-specific checks for several urllib3-update candidates also found no matching removed-API use.

This is an important search-method result:

> Dependency source copied into a repository must not be mistaken for application-owned reliance on that API.

---

# 12. What the pilot proved about the matrix

The pilot produced materially different outcomes from superficially similar dependency updates:

1. **qldebugger** — exact target behavior impact exists, but exact existing coverage already resolves it;
2. **qldebugger real-derived** — one controlled coverage variable produces a clean targeted-check planning problem;
3. **Kubernetes client** — direct runtime usage exists, but dependency-graph compatibility is the stronger uncertainty and changes the case family;
4. **Splinter** — direct integration exists, but no exact changed behavior predicate was established and broad integration coverage is already configured;
5. **pip-audit** — another graph-bound case is real but duplicative, so it should stop early;
6. **changed-head synthetic** — rare lifecycle conditions remain appropriate for synthetic deterministic validation.

That is the desired behavior from a selection system. The matrix is not merely ranking package-update size or code-search hit count.

## 12.1 Important negative result

The bounded real search did **not** find an untouched public candidate that simultaneously satisfied all of these:

- exact upstream behavior change;
- exact target activation;
- evidence that existing baseline does not already close the behavior;
- one clearly discriminating missing targeted check;
- no stronger competing central uncertainty.

This negative result should be preserved. It supports the hybrid-case model instead of weakening the admission gate to force an all-real case.

---

# 13. Recommended next decision

## Priority-1 direct behavior + targeted check

The strongest candidate from this pilot is **C02: the qldebugger real-derived one-variable coverage-gap variant**.

Why:

- its real anchor is strong and independently inspectable;
- the upstream semantic change is precise;
- the target activation is exact and target-owned;
- the original target test provides an independent oracle that the behavior mattered;
- the controlled variant changes one variable only;
- the expected targeted check is specific and falsifiable;
- claim boundaries are easy to state honestly;
- no public repository must be mutated.

This is **not yet an admission decision**.

If Ali accepts C02 later, the next action should be:

```text
admit one central uncertainty
→ assign S006 only then
→ create fresh short-lived case branch from latest main
→ preserve untouched qldebugger anchor evidence
→ construct the one-variable real-derived fixture/snapshot
→ freeze expected behavior and stop boundary before implementation evaluation
```

## Priority-2 lifecycle

Keep C06 as the next strong synthetic candidate for changed-head / stale-evidence / supersession behavior.

## Separate graph/authority track

Keep C03, with C05 as corroborating evidence, for a separate dependency-graph/authority case. Do not combine that uncertainty with C02.

---

# 14. Admission decision from this record

**No case is admitted.**

Specifically:

- no `S006` identifier is assigned;
- no target repository is mutated;
- no runtime schema or implementation is created;
- no governance or `AGENTS.md` file is changed;
- no `MEMORY.md` update is made;
- no route/plan authority is changed;
- no merge or pull request is performed;
- the proposal package remains non-controlling.

The pilot’s output is a decision aid: **C02 is the strongest Priority-1 candidate to discuss/admit next, while C03 and C06 remain strong candidates for different uncertainty families.**
