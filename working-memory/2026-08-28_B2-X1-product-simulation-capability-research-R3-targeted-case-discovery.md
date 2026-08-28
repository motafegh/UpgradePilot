# B2/X1 Product-Simulation Capability Research — R3 Targeted Fresh-Case Discovery

**Date:** 2026-08-28  
**Status:** R3 COMPLETE — targeted search found useful contrast/design evidence but no credible non-trivial competing-action case; no holdout candidate frozen  
**Plan:** `../plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`  
**R2 planner-value record:** `2026-08-28_B2-X1-product-simulation-capability-research-R2-planner-value.md`  
**Evaluated main revision:** `14ba589de18aa72b0f9098d5154cc722c494c256`

## 1. R3 question

> Can we find a real public supported-boundary Python Dependabot case where exact-head resolver/currentness evidence and at least one other independently justified bounded read-only investigation are both genuinely plausible, and where the correct selection/order changes with proposition state, prerequisite evidence, attempt history, or information value rather than following a small deterministic rule?

R3 deliberately searched for a **discriminating planner-value case**, not merely any repository containing `uv.lock` or a resolver failure.

---

## 2. Search method

The search used a bounded combination of:

- public web search to discover recent/known Dependabot + uv/resolution cases;
- GitHub PR identity reads;
- changed-filename inspection;
- exact PR file patches only after a case was intentionally moved into design research;
- exact-head repository files/workflows when needed to classify the planning shape;
- public Dependabot-core issue evidence as design context only, not as untouched evaluation cases.

Screening order was intentionally:

```text
identity / package-manager / changed-file topology
→ basic supported-domain suitability
→ reserve or reject
→ only then deeper mechanism/CI inspection for design-research-used cases
```

This was intended to preserve the option of a future holdout if a genuinely suitable low-exposure case appeared.

No target repository was mutated, commented on, approved, rerun, closed, or merged.

---

## 3. Acquisition barrier encountered

During broad GitHub issue/PR search, GitHub returned a **secondary rate-limit** response.

Classification:

```text
provider/search acquisition barrier
!= candidate evidence
!= repository failure
!= resolver evidence
```

Response:

- stopped hammering the global GitHub search endpoint;
- continued with public web discovery plus direct bounded GitHub reads for already-identified candidates;
- did not weaken the screening question to compensate for the rate limit.

This barrier affected search breadth, not the correctness of exact evidence fetched for the cases that were inspected.

---

## 4. Candidate screening ledger

### 4.1 `langchain-ai/langchain#39187`

**Exposure:** PR body + changed filenames inspected.  
**Classification:** `rejected_or_unsuitable` for the current R3 question.

Observed topology:

- grouped Dependabot minor/patch update;
- multiple dependencies;
- multiple workspace/package directories;
- several `pyproject.toml` + `uv.lock` pairs changed.

Why rejected:

The current UpgradePilot product horizon is one public dependency-update decision, and this PR is a grouped multi-dependency/multi-workspace update. It is interesting future orchestration pressure but would change too many variables at once for the present resolver-selection question.

Do not use it to manufacture a multi-action planner claim.

---

### 4.2 `rendercv/rendercv#745`

**Exposure:** full PR metadata/body.  
**Classification:** `rejected_or_unsuitable`.

Reason:

The PR updates a GitHub Action (`actions/upload-pages-artifact`), not a Python package dependency. It is outside the supported Python Dependabot boundary for this research.

---

### 4.3 `rendercv/rendercv#739`

**Exposure:** full PR metadata/body + changed filenames.  
**Classification:** `rejected_or_unsuitable` for R3 resolver pressure.

Identity:

```text
repository: rendercv/rendercv
PR: #739
head: cf3f01cb6cd7cc0889193ae59cf58b205b87acdd
dependency: pymupdf 1.26.5 → 1.27.2.3
package manager: pip
changed files: pyproject.toml only
```

Reason:

No `uv.lock`/resolver-currentness topology exists. The release has interesting artifact/platform behavior, but that belongs to artifact-serviceability/target-environment evidence rather than the R3 resolver-selection question.

---

## 5. Design case D-R3-01 — `fastapi/fastapi-new#38`

**Exposure:** intentionally deep enough for design research: PR metadata/body, changed filenames, exact lock patch, exact-head `pyproject.toml`, exact-head test workflow, exact-head check-run summary.  
**Classification:** `design_research_used`; not a future untouched holdout.

### Identity

```text
repository: fastapi/fastapi-new
PR: #38
base: a7ca2b92789825e785266ac23b0766bdc7500518
head: 0ff6ff640293ee7543d4629f63848b08e9634756
dependency: pytest 9.0.0 → 9.0.2
package manager: uv
changed files: uv.lock only
```

The lock patch changes only the pytest package entry/version/artifact records relevant to the Dependabot update.

### Exact-head declaration

`pyproject.toml` establishes:

```text
[dependency-groups]
tests = [
  coverage[toml],
  mypy,
  pytest>=8.3.5,
  ruff,
  smokeshow,
]
```

So pytest is explicitly part of the target `tests` dependency group.

### Exact-head CI consumption

`.github/workflows/test.yml` uses a Python/OS matrix and contains:

```text
uv sync --locked --no-dev --group tests
→ uv run bash scripts/test.sh
```

The coverage-combine job also performs:

```text
uv sync --locked --no-dev --group tests
```

and the fan-in `alls-green` job depends on successful coverage combination.

Exact-head check-run evidence includes successful `coverage-combine` and `alls-green` results.

### What this case establishes for research

The strongest bounded interpretation is:

```text
lock-only pytest update
+ exact project group says pytest belongs to tests
+ exact workflow statically consumes locked tests group
+ exact-head required downstream checks succeeded
→ a separate resolver/currentness check is not automatically the highest-value next action
```

Important proof limit:

Current UpgradePilot does not yet own full trusted static↔runtime step correlation for every workflow. R3 therefore treats the above as **manual design evidence**, not as a claim that current product source already emits a stronger exact resolver-satisfiability proposition.

### Planner-pressure result

This is a strong counterexample to the shallow heuristic:

```text
uv.lock changed
→ run resolver
```

It supports a more general principle:

> Existing exact-head CI/environment evidence may already make a separate resolver/currentness action redundant or lower value.

However this case still does **not** create two genuinely competing planner actions. Once the evidence is assembled, a small deterministic policy can prune resolver work.

---

## 6. Design case D-R3-02 — `evoila/meho#1768`

**Exposure:** full PR metadata/body + changed filenames + exact `backend/pyproject.toml` patch + exact `backend/uv.lock` patch.  
**Classification:** `design_research_used`; not a future untouched holdout.

### Identity

```text
repository: evoila/meho
PR: #1768
base: 980cb16ff311a5cdca29282a68be159bc6ff947c
head: 4fa217ab7aae36a37c7cc906573f323a33d4512d
dependency: cryptography 48.0.0 → 49.0.0
package manager: uv
changed files:
- backend/pyproject.toml
- backend/uv.lock
```

The manifest raises the dev dependency floor:

```text
cryptography>=42.0
→ cryptography>=49.0.0
```

and the lock updates to cryptography 49.0.0 with the new release artifact set.

### Why this is useful but not the desired R3 winner

The PR itself already contains a manifest + lock update consistent with a successfully produced proposed environment. The upstream release also contains several separate changes, including platform wheel removals and behavioral/API changes.

That makes the case useful evidence for this distinction:

```text
resolver/lock success or currentness
!= artifact-serviceability
!= API/behavior compatibility
```

But the case does not show that a custom resolver action and another investigation are simultaneously unresolved and competing. The resolver-like rung is already substantially addressed by the update's produced lock state; the remaining interesting questions are different mechanisms.

A later public issue in the same repository describes a different future update (`presidio-anonymizer`) blocked by cryptography constraints. That issue is useful **resolver-failure design context**, but it is not evidence that PR #1768 itself had that failure and must not be conflated with this PR.

### Planner-pressure result

Again, richer dependency-update reasoning exists, but the observed shape is closer to:

```text
one proof rung already settled
→ investigate another mechanism-specific proposition
```

than to non-trivial choice among several simultaneously admitted planner actions.

---

## 7. Additional public design context — not holdout material

Several public Dependabot/uv reports were found that demonstrate resolver/currentness importance but are too oracle-exposed, private, or lack an actual created PR for future protected use.

### Dependabot-core #12788

Public report: uv updater could change a lock entry while failing to change the corresponding manifest floor as native uv would.

Use:

- design evidence that manifest/lock consistency/currentness can be a real proposition;
- **not** holdout material because the bug report states the failure and expected result explicitly.

### Dependabot-core #14119

Public report: case mismatch between dependency spelling in `pyproject.toml` and `uv.lock` caused Dependabot update failure even though native uv worked.

Use:

- design evidence for updater/resolver acquisition failure taxonomy;
- no PR was created, so it is not a normal UpgradePilot PR decision case.

### Dependabot-core #13891

Public report: local filesystem package dependencies caused uv lockfile update failure.

Use:

- design evidence that resolver context can depend on local/path package availability;
- not a clean public PR case and heavily oracle-exposed.

### Dependabot-core #15842

Public report: a Dependabot-core uv invocation bug passed version numbers positionally to `uv lock` and blocked updates.

Use:

- provider/updater failure evidence;
- not evidence of target dependency incompatibility;
- no normal UpgradePilot PR exists when update creation itself fails.

### Dependabot-core #12087

Public report: attempted uv updates can fail because target versions are incompatible with the existing declared graph.

Use:

- direct support for resolver satisfiability as a meaningful evidence class;
- not a fresh UpgradePilot PR case because the failure occurs before normal PR creation.

### `slettmayer/oebb-mcp-server#25`

Dependabot uv PR updating Ruff 0.16.2 → 0.16.3; changed `uv.lock` only. Repository documentation states the test path uses `uv sync --locked`, intentionally making lock drift fail CI.

Use:

- corroborative design pressure similar to `fastapi-new#38`;
- no need for deeper inspection because it does not add a materially different R3 shape.

Classification: `screened_only` / not reserved.

---

## 8. What the search did NOT find

Within the bounded search, no credible public case was found with all of these properties simultaneously:

```text
single supported Python dependency-update PR
+
resolver/currentness proposition materially unresolved
+
resolver check safely/boundedly available
+
at least one other independently justified read-only investigation also materially unresolved
+
correct first action changes with trusted state/history/budget
+
small deterministic ordering is demonstrably inadequate
```

This absence is not proof that such cases never exist.

It is sufficient for the current research decision because the burden is to justify planner expansion from real evidence, not to assume expansion and search indefinitely until a fitting case appears.

---

## 9. Holdout decision

R3 assigns **no `reserved_holdout_candidate`**.

Reason:

- promising public cases inspected deeply enough to answer the research question are now design-exposed;
- lightly screened cases did not match the target planner-value shape strongly enough to reserve;
- reserving an irrelevant case merely to ensure a future v3 pool would invert the research method.

This is a positive preservation decision:

```text
no suitable holdout found
→ preserve no fake holdout
→ main can later run targeted discovery after an honest candidate claim is selected
```

---

## 10. R3 findings

### R3-F1 — resolver/currentness is a real capability but still lacks evidence for LLM-owned selection

**CONFIRMED / NARROWED.**

Public evidence shows that resolver/currentness can matter materially. But the cases found split mostly into:

```text
A. stronger exact locked-CI / lock-update evidence already exists
→ resolver check redundant/lower value

B. manifest/lock/resolver consistency itself is the obvious missing proof rung
→ resolver/currentness check is directly indicated
```

That policy remains expressible by small deterministic state rules.

### R3-F2 — the strongest negative case is valuable

`fastapi-new#38` demonstrates that “lock changed” is not enough to justify a resolver action. Existing exact-head group membership + locked CI + successful downstream checks can make another resolver observation unnecessary.

This strengthens UpgradePilot's anti-over-investigation requirement.

### R3-F3 — richer mechanism breadth does not automatically create richer planner action choice

`meho#1768` has multiple relevant upstream concerns, but those concerns are separate mechanism/applicability responsibilities. A richer semantic candidate set may eventually feed a planner; it does not itself prove that multiple planner-visible investigation actions currently exist.

### R3-F4 — failed Dependabot update creation is not a normal product PR case

Many of the clearest resolver conflicts prevent Dependabot from creating the PR at all.

That is important product-horizon evidence:

```text
Dependabot updater/resolver failure
!= public PR investigation state
```

UpgradePilot's current charter centers on public Dependabot PRs, so these failures should not be smuggled into the first planner action space merely because they demonstrate resolver technology.

### R3-F5 — no holdout should be manufactured

**CONFIRMED.**

No case deserves reservation solely to make v3 appear prepared.

---

## 11. R3 gate result

The R2 resolver hypothesis does **not** survive as a justified new planner-visible action on current evidence.

Disposition:

```text
resolver/currentness capability itself
→ independently useful future deterministic evidence capability

LLM-owned choice of when to invoke it
→ NOT JUSTIFIED YET
```

Therefore R4 deep case investigation is **not activated** for a promoted multi-action candidate.

There is no reason to create a controlled variant merely to manufacture the missing competition; that would answer a synthetic question chosen after the desired architecture rather than establish external product need.

---

## 12. What would reopen the planner-expansion question

A future real case can reopen CAND-02 if it shows:

1. two or more independently admitted read-only capabilities;
2. neither is trivially prerequisite/obviously stronger;
3. their relative information value changes with trusted state/history/budget;
4. a fixed policy becomes materially brittle or combinatorial across supported cases;
5. exact authority/execution remains deterministic.

Until then, keep resolver evidence as a product capability opportunity, not an LLM action quota.

---

## 13. R3 stopping decision

Stop targeted case discovery here.

Reason:

```text
multiple relevant public uv/Dependabot shapes screened
+ one strong negative resolver-selection design case established
+ resolver-failure evidence exists but commonly before PR creation
+ no real non-trivial competing-action case found
+ continued search is increasingly likely to become architecture-seeking rather than question-driven
```

The research program can now skip R4/R5 candidate-deepening unless main or new evidence selects a different justified candidate responsibility, and proceed to R6 synthesis of the negative-but-decision-useful result.
