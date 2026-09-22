# Product Simulation Rebase — G1 Closure / G2 Bounded Handoff

**Date:** 2026-09-22  
**Status:** ACTIVE companion progression record; the [initial rebase working memory](2026-09-22_product-simulation-current-state-rebase.md) remains the branch-level anchor.  
**Branch:** `research/product-simulation-rebase-2026-09-22`  
**Mode:** Product Simulation research and analysis, parallel to `main`; `UP-SKILL:upgradepilot-working-memory`.

## 1. Starting point and corrected scope

The initial rebase reconstructed Phase A and later product changes against the older Product Simulation corpus. It identified G1 command/runtime truth, G2 exact CI-job → Target composition, G3 pip/uv package-state semantics, and G4 target wheel-tag witness feasibility. This workstream covers the whole current product, not only the current main workstream's Phase B question. Our independent research branch never owns changes to main product code/tests/specs/plans or root/main memory.

## 2. G1 meaningful progression — bounded screening completed

- **Black #5421 false positive corrected:** changed `pyproject.toml`'s optional `width-table` extra, but the successful `pip install .` step did not select it. Removed as changed-source consumption proof, preserved only as screened-out control.
- **Aruba #83:** two direct-source command shapes from distinct exact-head workflows: sole `-r requirements.txt` in `lint.yml`; second sequential `--requirement requirements.txt` in `test.yml`. Retained Test logs prove the second command ran in the observed run, but step success alone does not satisfy the current sole/first runtime strengthening rule. Preserve synthetic PR merge checkout vs bare head.
- **aiohttp #13785:** first-sequential install step uses exact changed `requirements/base.txt` through `-c`; current `-r`-only direct-source observer cannot admit that changed-source relation. The earlier sdist install logs multidict 6.9.0; never misattribute that result to the later slotscheck install. The real `-c` input is a substantive candidate product-breadth finding, not an authorized implementation change.
- Durable artifact: [G1 screening](../product-simulation/2026-09-22_G1_COMMAND_RUNTIME_REAL_CASE_SCREENING.md). G1 stopped after discriminating positive/conservative/source-breadth shapes, not arbitrary case count. No numbered scenario admitted.

## 3. G2 meaningful progression — complete at bounded search/design horizon

- **aiohttp #13785:** exact-head workflow has different static jobs and matrix-expanded runtime instances, but the selected changed requirement pin files enter the inspected relevant commands through `-c`. This is an upstream source-selection gap; the host cannot independently validate the current F4 positive `-r` path. Do not collapse runtime matrix instances into distinct static job keys.
- **Aruba #83:** `ruff`/`test` directly consume the changed source but belong to separate one-job workflow definitions; the unrelated Validate jobs do not consume it. This is cross-workflow identity pressure, not the missing same-workflow test.
- **Open WebUI #26494:** Dependabot changes `backend/requirements.txt` pytest `~=8.4.1 → ~=9.1.1`, head `ed99df86c8cb69e5848592f0af0df2fb0d3d0103`; matching `.github/workflows/backend.yaml` has only static key `format-check` with Python 3.11/3.12 matrix instances. They install Ruff independently, never visibly consume the changed requirements path; their observed formatting failures do not establish a pytest failure. This is a valuable non-consumer control, not F4 positive. Head-associated Python CI run `28488568057` had two failed formatting job instances.
- **MontePy #986:** multiple jobs and explicit state witness, but PR changes `pyproject.toml` build requirements consumed via project install, not an exact changed `-r` file. Retain for G3, not the narrow G2 proof.
- Durable artifacts: [G2 first screening](../product-simulation/2026-09-22_G2_MULTI_JOB_TARGET_FIRST_SCREENING.md) and [G2 non-consumer/stop](../product-simulation/2026-09-22_G2_NONCONSUMER_CONTROL_AND_STOP.md).
- **Bounded negative result:** no untouched host in this deliberately screened set met *all* gates for a clean same-workflow, multiple-STATIC-job, exact changed `-r`/`--requirement` source with inspectable relevant runtime evidence. This is not a population-prevalence claim. Do not force a positive case or continue broad low-information searches.
- Prepared [G2 real-derived controlled variant design](../product-simulation/2026-09-22_G2_REAL_DERIVED_JOB_COMPOSITION_VARIANT_DESIGN.md): freezes real Aruba PR and direct-source commands, *synthetically* combines consuming/non-consuming jobs into one workflow and contrasts declared Target environments. The altered workflow and runner contexts are explicitly not real Aruba observations. Expected identity, deduplication, missing-job, runtime proof boundaries and optional matrix controls are written. This is design-only; no replay/source or test change or target run was performed or authorized by it.

## 4. Current route and handoff

**R1/R2:** first current-product / simulation coverage rebase recorded in initial anchor. **R3/R4:** four gap families identified. **G1:** bounded screening closed. **G2:** bounded screening and alternative real-derived fixture *design* closed; no new numbered scenario or public F4 acceptance claim. **G3:** next active evidence family, reusing the earlier Salt/MontePy/Sigstore/Aruba exact-public-case research, especially ambient semantic selectors versus operational variables and post-install state proof. Do not repeat broad discovery before checking prior evidence. **G4:** deferred bounded witness-feasibility search.

**Next research slice:** write a tightly sourced, non-controlling G3 synthesis/research artifact from exact proposal/revision/workflow/job/log evidence, keeping four propositions separate: command execution, effective package-manager semantics, installer-result operation, independent target-owned state. Distinguish later mutation and log-retention evidence limits; stop when further cases cease to discriminate. Optionally hand off the observed aiohttp `-c` source-consumption gap to main as a *proposal for owner review*, never implement or change accepted product semantics from this branch. The G2 controlled fixture can be replayed by the F4 owner only if separately selected/authorized on then-current main.

**Branch boundary:** no product source/tests/stable specs/plans, root `MEMORY.md`, main workstream working memory, target repositories or external CI were mutated. No merge yet; reconcile with current `main` only for an explicitly authorized integration. This record supersedes its earlier same-workflow positive-search next-action as of this bounded stopping point.

## 4. 2026-09-22 main-workstream re-sync before G3

Before starting G3, the parallel main branch was re-read from the research branch's merge-base forward.

### What changed on main

Since this research branch split, main advanced through ten commits. The substantive repository delta is concentrated in working-memory/design records rather than product source/tests/specifications:

- `working-memory/2026-09-21_runtime-install-command-semantic-eligibility.md` progressed from B2/B3 into **B4 ambient/effective-semantics fail-closed design**;
- `working-memory/2026-09-22_b4-environment-evidence-data-flow-learning.md` was added and expanded with concrete environment-flow/proof cases.

No new product implementation was observed in this main-only delta.

Main's current Phase-B tracker is:

```text
B1 — DONE: command-local semantic-eligibility contract accepted;
            ordinary command+success cannot close effective runtime state
B2 — DONE: separate dependency-owned semantic evidence object
            + CI identity composition accepted
B3 — DONE: first bounded pip/uv semantic matrix accepted
B4 — IN PROGRESS: ambient/effective-semantics fail-closed boundary
B5 — PENDING: command-success → dependency-state proof contract
B6 — PENDING: smallest implementation + proof slice
```

### Material proof refinements relevant to Product Simulation

Main now explicitly distinguishes:

```text
command-local package-manager semantics
!=
effective ambient/process semantics
!=
exact command execution
!=
resulting package state
```

Important B4 relationships:

```text
declared_for
→ written_to (only if exact write execution is established)
→ propagates_to later same-job step
→ overridden/transformed by later applicable values
→ received_by exact package-manager process
→ interpreted_as pip/uv semantics
→ supports_or_defeats the state-proof proposition
```

A proven `GITHUB_ENV` write establishes at most an inherited baseline for later steps in the same job. It does not automatically prove that the exact pip/uv process received that value, because step env, shell-local overrides/wrappers, command-line precedence, and other transformations may intervene.

Main also preserves the existing runtime-strengthening boundary: a successful enclosing step does not prove execution of an arbitrary internal `GITHUB_ENV` write or later pip/uv command. Existing exact-occurrence/runtime-strengthening rules must be reused rather than bypassed.

### Effect on our research route

**G1 remains valid.** The new main work reinforces, rather than supersedes, the G1 finding that exact occurrence structure/execution is an independent proof gate.

**G2 remains valid.** Exact consuming job identity still matters, and environment propagation is same-job scoped; therefore job identity becomes even more important when reasoning about ambient package-manager state.

**G3 should now be refined before broadening.** The next Product Simulation question is no longer merely:

```text
do PIP_*/UV_* settings matter?
```

It is:

> In real public CI, which package-manager-relevant environment/config facts can be positively tied to the exact dependency-consuming pip/uv process, through what source/propagation/override chain, and how often do those facts materially change the package-state inference?

G3 screening should deliberately seek distinct evidence shapes:

1. **direct literal step/job/workflow env → exact pip/uv consumer**;
2. **earlier `GITHUB_ENV` write → later same-job consumer**, with evidence about whether the write occurrence executed;
3. **later shell/command-line override** that changes the effective value;
4. **ordinary control** with no visible relevant ambient modifier, while preserving that absence of visibility is not complete effective-state proof;
5. **direct runtime package-state witness** (`pip freeze`, equivalent target-owned state evidence) as a separate stronger path.

Salt's `PIP_CONSTRAINT` case is therefore especially relevant to B4 because it demonstrates a material ambient semantic modifier. MontePy remains useful for the distinct direct-state-witness path. Sigstore helps separate operational `UV_*` variables from semantically relevant modifiers. Aruba remains an ordinary control/installer-result case.

### What not to do

- Do not treat the B4 graph vocabulary as an implemented graph schema.
- Do not invent a generic environment resolver from Product Simulation.
- Do not assume a visible `GITHUB_ENV` write occurred merely because the enclosing step succeeded.
- Do not equate a propagated step baseline with the exact value received by the package-manager process.
- Do not let G3 duplicate G1 execution-correlation research; compose the evidence boundaries instead.
- Do not re-open G1/G2 merely because main progressed.

### Branch-sync decision

No merge/rebase from main is required yet for this research-only continuation because the main-only changes are design/learning records and do not create source conflicts with the Product Simulation artifacts. Their conclusions are now explicitly incorporated into this research route.

Before eventual branch integration, reconcile again with then-current main.

## 5. Route correction — broad Product Simulation research, guided by main rather than bounded by it

Ali corrected the interpretation of the main-workstream re-sync.

The Product Simulation responsibility is not to narrow itself to the current main workstream's immediate B4/G3 question. Its value is broader:

```text
current main progress
→ improves our vocabulary, evidence questions, and prioritization

BUT

Product Simulation
→ independently explores the wider current/future product surface
→ looks for real-world counterexamples, missing responsibilities, adjacent failure modes,
   ordinary controls, and future evidence needs
→ feeds useful findings back to main when mature
```

Therefore the correct research strategy is:

### Broad, but selective

Continue researching across the wider coverage-gap inventory, not only G3:

- command/runtime truth and source-consumption breadth;
- CI job/environment identity and composition;
- package-manager semantics and installed-state proof;
- target/artifact/platform compatibility evidence;
- acquisition/authentication/retention degradation;
- evidence applicability and cross-stage composition;
- uncertainty, stopping, abstention/action boundaries;
- additional real-world seams discovered during screening even if main has not reached them yet.

The standard for breadth is information value, not case count.

A new case/family remains useful when it can:

1. expose a current or likely future product blind spot;
2. challenge an assumption with a realistic counterexample;
3. establish an ordinary control showing a suspected problem is uncommon/non-material in that shape;
4. compare competing evidence/proof approaches;
5. reveal an evidence source or workflow shape the current design has not considered;
6. help a later main-workstream decision even if it is not today's active implementation question.

### Use main as a moving research signal

Recent main work should influence Product Simulation in three ways:

1. Sharpen questions — e.g. B4's distinction between propagated step state and exact-process effective state makes future ambient-semantics case collection more precise.
2. Expose new research opportunities — when main introduces a new proof boundary or hypothesis, deliberately seek real cases that validate or break it.
3. Avoid stale duplication — if main has already resolved a question strongly, spend research effort on the unresolved edges and neighboring assumptions instead of repeating the same proof.

It should not become a fence around the Product Simulation scope.

### Revised continuation model

Do not execute a simple serial roadmap such as:

```text
finish G3 completely
→ then G4
→ then stop
```

Prefer a portfolio model:

```text
MAIN-SIGNAL TRACK
→ research questions directly useful to current main progress

COVERAGE-GAP TRACK
→ unresolved responsibilities from the whole-product rebase

FORWARD-PRESSURE TRACK
→ plausible future seams/counterexamples not yet active on main

CONTROL TRACK
→ ordinary real-world cases used to test whether suspected risks are actually material/common enough to matter
```

Cases may inform more than one track, but their propositions and claim limits remain separate.

### Immediate implication

G3 remains highly valuable and should continue, especially using Salt/MontePy/Sigstore/Aruba plus newly screened cases.

However, in parallel we should continue scanning for high-information evidence in G4 and any newly exposed cross-cutting seams rather than artificially postponing them until G3 is exhausted.

The next Product Simulation phase should therefore be a broader evidence portfolio pass, periodically re-synced with main, with promotion based on discriminating value rather than strict family sequence.

This section supersedes the earlier wording that G3 should be refined before broadening. The correct rule is:

> Broaden intelligently, while using current main progress to make the broader research more precise and useful.
