# B2 Target Python Support Relevance Plan

**Status:** Position-neutral bounded product plan  
**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Implement and prove the smallest product slice that connects one trusted dependency update and one authoritative upstream Python support-drop claim to the target repository's exact-revision Python declaration.

```text
trusted DependencyVersionChange
→ authoritative crossed-release upstream evidence
→ grounded Python X.Y support-drop claim
→ exact-head [project].requires-python
→ declared overlap | declared non-overlap | explicit unresolved/unsupported
```

This is a **target relevance** result. It is not compatibility, safety, or a merge/defer recommendation.

This plan is position-neutral. `../MEMORY.md` alone selects live continuation.

## Accepted owners this plan consumes

Do not re-decide or re-specify these accepted responsibilities here:

- dependency-version evidence method → [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- PEP 440/version-line method → [`../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)
- bounded local semantic extractor → [`../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
- responsibility-based Python structure → [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)
- core evidence/trust invariants → [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- minimum useful generality → [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

This plan coordinates when/how those responsibilities are connected and proven.

## Owning product question

For one trusted exact-version Python dependency update:

> When authoritative upstream evidence in the complete old-exclusive/proposed-inclusive release interval establishes a grounded claim that support for Python `X.Y` was dropped, does the target repository's exact-head `[project].requires-python` declaration include any stable Python `X.Y` release under the accepted version-line method?

## Scope boundary

### Upstream responsibility

Use bounded authoritative crossed-release sources with exact identity. The product must not rely only on the proposed release's final notes when a material change may have occurred earlier in the crossed interval.

The initial authority path may use exact release/tag/changelog evidence already admitted by the selected upstream plans/ADRs. Arbitrary documentation crawling, model-selected authority, or unbounded web search remains outside this slice.

### Target responsibility

The first target declaration source is:

```text
pyproject.toml at the exact PullRequestIdentity.head_sha
→ [project].requires-python
```

This declaration establishes only the project's declared Python installation-version specifier at that revision. It does not establish CI execution, production runtime, dependency use, compatibility, or update safety.

### Semantic responsibility

The local model produces only untrusted support-drop candidates according to ADR-0006. Deterministic validation remains the trust-admission boundary.

### Decision responsibility

This plan stops at target-Python relevance. Recommendation/decision mapping remains outside this responsibility until separately admitted.

## Required responsibility flow

```text
DependencyVersionChange
→ package/upstream identity and crossed-release authority
→ bounded authoritative source evidence
→ semantic candidate extraction
→ deterministic candidate validation
→ GroundedPythonSupportDropClaim?
    ├── no  → target Python responsibility not activated / unresolved
    └── yes → acquire exact-head pyproject.toml
              → interpret [project].requires-python
              → evaluate dropped-line relevance
              → overlap | outside declared range | unresolved/unsupported
```

Target Python acquisition must be conditional on a grounded support-drop claim. A reusable target-acquisition function may exist independently, but the application path must not imply that every dependency update requires this investigation.

## Target evidence outcomes

Preserve at least these materially different target states:

- declaration available;
- exact file unavailable;
- malformed TOML;
- `[project]` table absent;
- `requires-python` absent;
- `requires-python` invalid for the expected textual boundary;
- specifier valid but unsupported by the admitted exact-line method.

No unavailable/malformed state may be converted into an inferred target range.

## Relevance outcomes

The bounded comparator distinguishes:

- `declared_python_overlap` — at least one stable exact `X.Y.Z` witness is admitted by the declaration;
- `outside_declared_python_range` — the admitted method proves no stable exact version in the dropped line is allowed;
- `target_declaration_unresolved` — target evidence cannot support comparison;
- `upstream_claim_unresolved` — no trusted support-drop claim is available;
- `comparison_unsupported` — both inputs exist but the accepted method deliberately abstains.

None of these states may imply `safe`, `compatible`, `merge`, or equivalent claims.

## Work sequence

### Step 0 — Dependency-change prerequisite

Consume a behavior-valid representation-neutral `DependencyVersionChange` from the ADR-0004 responsibility. Do not begin end-to-end relevance proof while the selected real case is outside the admitted dependency-evidence boundary.

### Step 1 — Crossed-release source authority

Establish and test:

- old-exclusive/proposed-inclusive release interval;
- exact package/upstream identity;
- bounded authoritative release/tag/changelog source identity;
- source unavailable/conflict behavior;
- no model-selected source authority.

### Step 2 — Trusted support-drop boundary

Keep candidate semantic output and trusted grounded claims separate. Deterministic validation must reject or preserve unresolved state for malformed, ungrounded, wrong-direction, wrong-category, wrong-line, or out-of-interval candidates.

### Step 3 — Standards-based version method

Use ADR-0005. The detailed algorithm/dependency bounds belong to that ADR and its focused proof plan, not here.

### Step 4 — Deterministic target relevance

Prove the comparator with directly constructed trusted claims before any live model/runtime integration:

```text
GroundedPythonSupportDropClaim
+ TargetPythonDeclaration
→ relevance result
```

### Step 5 — Authoritative upstream acquisition

Acquire the exact bounded source needed for the selected real proof and preserve release/tag/revision/path/blob identity.

### Step 6 — Bounded semantic method evaluation

Evaluate/admit semantic extraction only where deterministic interpretation is inadequate. The accepted result of that evaluation is recorded by ADR-0006; future changes follow its reassessment triggers rather than being re-decided by this plan.

### Step 7 — Runtime integration and conditional orchestration

Use the dedicated bounded plan:

- [`B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)

It owns the deterministic source-window bridge, product adapter integration, application sequencing, and end-to-end proof needed to connect the accepted method into normal runtime.

### Step 8 — End-to-end bounded proof

Run the selected public proof through the active product path and establish only the target-relevance claim supported by reacquired evidence.

The proof must not turn target non-overlap into a compatibility/safety/merge claim.

## First proof case

The historical S001 case may be reused as an oracle without reopening simulation:

```text
target repository: pydantic/pydantic
PR: 13432
dependency: soupsieve
update: 2.6 → 2.8.4
upstream support drop: Python 3.8 introduced in crossed release 2.8
target declaration at exact PR head: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

The active product must reacquire/derive its own exact evidence. The historical case does not authorize package/repository/version hardcoding.

## Proof obligations

Before this responsibility can be considered behavior-valid, controlled and applicable live evidence must establish at least:

1. one trusted dependency change from generic admitted source rules;
2. exact crossed-release interval and upstream source identity;
3. no omission of a material intermediate crossed release merely because the final release body is sparse;
4. no model-selected source authority;
5. candidate semantic output cannot reach comparison without deterministic validation;
6. malformed/wrong-direction/wrong-category/ungrounded/out-of-interval candidate behavior remains unresolved;
7. target acquisition occurs at the exact PR head;
8. target unavailable/malformed/missing/unsupported states remain distinct;
9. no target range is inferred from unrelated workflows/classifiers/docs/tool settings;
10. comparison cannot run without both a trusted support-drop claim and valid admitted target declaration;
11. ADR-0005 supported/unsupported line semantics are covered by focused tests;
12. target acquisition is not activated before a grounded support-drop claim;
13. the selected public proof yields only the bounded expected relevance result;
14. known fixture values are not hardcoded into product logic;
15. active deterministic product regression remains green.

More detailed proof for dependency parsing, version mathematics, semantic model adoption, and Step 7 integration stays with their focused owners rather than being duplicated here.

## Modification boundary

Use the responsibility-based source layout controlled by ADR-0007. This plan may modify product modules/tests that own upstream authority/claim grounding, target declaration/relevance, application orchestration, and CLI presentation only when the selected step requires them.

Do not recreate old flat compatibility paths or create generic service/framework layers to satisfy this plan.

## Stop/reframe conditions

Stop or reframe if:

- trusted dependency identity cannot be established within the admitted source boundary;
- authoritative crossed-release evidence cannot be obtained without unbounded source search;
- release ordering/source authority cannot be established responsibly;
- semantic extraction cannot remain bounded and deterministically validated;
- target declaration cannot be interpreted under an auditable bounded method;
- the slice would need compatibility/safety reasoning to justify its relevance output;
- the next work would enter recommendation policy or another unauthorized responsibility.

## Completion condition

This plan's responsibility is complete only when the active read-only product path can connect a trusted dependency change to authoritative crossed-release evidence, admit or reject a bounded support-drop claim, conditionally inspect the exact target Python declaration, and return an honest relevance/unresolved state with deterministic regression and selected live proof.

Live selection/continuation remains in `../MEMORY.md`, not here.
