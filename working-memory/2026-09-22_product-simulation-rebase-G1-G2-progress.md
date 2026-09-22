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


## 6. Reality-check principle — theoretical counterexample != justified product complexity

Ali added a critical Product Simulation responsibility: some synthesis/design counterexamples being handled by the main workstream may be logically valid but uncommon, artificial, or effectively absent in real supported repositories. Product Simulation must test that possibility rather than assuming every constructed counterexample deserves first-class implementation complexity.

### Required distinction

For any counterexample or proposed safeguard, keep these questions separate:

```text
Can this happen?
!=
Have we observed it in real supported repositories?
!=
How often / broadly does it appear?
!=
Does it materially change a maintainer decision?
!=
Is handling it worth the product complexity?
```

A synthetic counterexample proves only possibility unless tied to real evidence.

### Empirical classification

When evaluating a concern, classify the evidence proportionately:

- **observed-real:** exact public case exists in a supported boundary;
- **real-derived:** grounded in real repository shapes but the decisive combination is synthetic;
- **plausible-unobserved:** semantics permit it, but bounded search has not found a real instance;
- **synthetic-only:** useful for correctness pressure, not evidence of real-world incidence;
- **prevalence-unknown:** one/few real examples exist but frequency cannot be inferred;
- **ordinary-control:** nearby real cases do not exhibit the feared condition.

Do not turn absence in a bounded sample into a population claim. Record the search boundary and uncertainty.

### Complexity / priority test

Research should help main distinguish:

```text
high consequence + real/recurrent evidence
→ strong implementation pressure

high consequence + rare/unknown incidence
→ may justify a bounded fail-closed rule or explicit limitation rather than broad machinery

low consequence + rare/synthetic-only
→ strong candidate for deferral/non-support

common ordinary case + theoretical counterexample only
→ protect the ordinary path from being made unusable by over-conservative design
```

Frequency is not the only criterion: a rare case can still matter when the failure is severe, the supported contract explicitly promises it, or the safeguard is cheap and local. Conversely, theoretical correctness alone does not justify a large architecture expansion.

### Product Simulation consequence

For current and future main-workstream synthesis counterexamples, Product Simulation should deliberately search for:

1. at least one exact real occurrence when feasible;
2. ordinary controls that show the nearby normal shape;
3. negative/bounded-search evidence when no occurrence is found;
4. consequence if mishandled;
5. implementation cost/scope implied by supporting it;
6. the narrowest defensible response: support, fail closed, explicit non-support, defer, or investigate further.

This becomes a standing cross-cutting track alongside the main-signal, coverage-gap, forward-pressure, and control tracks.

The objective is not to prove main wrong or right. It is to prevent both **under-engineering real problems** and **over-engineering hypothetical ones**.

## 7. Broad evidence-portfolio pass — first results

The broadened research strategy was executed across main-signal, coverage-gap, forward-pressure, and control questions rather than serially finishing one gap family.

### G3 / reality-check result

A bounded public-workflow search showed materially uneven incidence across package-manager semantic families. Exact-string discovery found no `PIP_DRY_RUN` workflow hits, while `PIP_CONSTRAINT`, `UV_CONSTRAINT`, and `UV_NO_SYNC` produced many public workflow matches. These are query-specific discovery counts, not prevalence estimates.

Sharper inspection confirmed that the B4 environment-propagation mechanism itself is real:

- LocalStack CLI writes `PIP_CONSTRAINT=...` to `GITHUB_ENV` for later steps;
- historical trading_calendars does the same before later pip installation;
- diwire explicitly syncs, then writes `UV_NO_SYNC=1` to `GITHUB_ENV`, then uses later `uv run` steps;
- NVIDIA cuda-python demonstrates shell-local `PIP_CONSTRAINT` / `PIP_BUILD_CONSTRAINT` exports before later pip commands.

The practical conclusion is not `ambient semantics are rare` or `common`. It is that **different counterexample families have different empirical support**, so implementation priority should follow exact real evidence and consequence rather than theoretical possibility alone.

Durable artifact: `product-simulation/2026-09-22_G3_REALITY_CHECK_AMBIENT_SEMANTICS.md`.

### S013 promoted — LangChain real no-sync/prior-sync case

LangChain PR #40646 passed every V2 admission gate and was promoted as S013:

`product-simulation/scenarios/S013-langchain-anyio-uv-no-sync-prior-sync-state/`.

Key sequence:

`Dependabot anyio lock update → ambient UV_NO_SYNC=true → explicit uv sync → anyio 4.15.1 installed → later uv run tests under no-sync`.

Observed CI used synthetic PR merge commit `63e06a2ba490c0bcdc7de672d38e5210f7cc0650`, not bare head `3908f2b...`; this identity is preserved explicitly.

S013's main discriminating result:

`visible UV_NO_SYNC` does not globally defeat dependency-state evidence when an earlier explicit state-forming sync is positively established. Conversely, the later no-sync `uv run` must not be credited with the earlier state formation.

This exposes a cross-cutting temporal composition seam:

`earlier bounded state evidence → later state-preserving exercise evidence`.

Supporting artifacts:

- `product-simulation/S013_CANDIDATE_SCREENING.md`
- `product-simulation/S013_POST_CASE_SYNTHESIS.md`
- scenario README + four evidence JSON files.

### G4 feasibility result

TileDB-Py provides a concrete real target-owned exact wheel-tag witness. Its CI executes `pip debug --verbose` after selecting matrix OS/Python environments, and runtime logs show materially different compatible-tag sets for Linux, Windows, and macOS.

This answers the mechanism-feasibility question positively:

`runner/Python labels != exact compatible tags`, while a target-owned runtime `pip debug --verbose` can directly emit the exact compatible-tag set.

It does not select a product acquisition/parsing architecture.

Durable artifact: `product-simulation/2026-09-22_G4_EXACT_WHEEL_TAG_WITNESS_FEASIBILITY.md`.

### Historical coverage register decision

`product-simulation/SCENARIO_COVERAGE.md` was inspected but intentionally not rewritten. It explicitly records historical D1 S001–S005 coverage/acceptance rather than acting as a live scenario registry. Adding S013 there would blur that owner boundary.

### Current portfolio route

Next high-information jobs are:

1. **G4 supported-update bridge:** find an UpgradePilot-supported Python dependency-update case that naturally emits exact compatible-tag evidence, rather than only a general CI mechanism example.
2. **B4 propagation-to-process bridge:** trace one current real `GITHUB_ENV` package-manager control all the way into the exact later pip/uv process and determine where proof becomes unresolved.
3. **retargeting reality check:** sample real `PIP_TARGET`/equivalent retargeting use to determine whether main's retargeting concern is decision-relevant or mostly edge pressure.
4. **forward-pressure scan:** keep looking for new real seams outside today's main question, promoting only discriminating cases.
5. **periodic main resync:** use new main progress to refine questions, never to restrict Product Simulation scope.

No product source/tests/specification/plan/root-memory mutation was performed.
## 8. Second portfolio pass — retargeting, G4 bridge, and latest-main reality check

### Main re-sync

Main advanced again with two B4 design records:

- multiple same-variable `GITHUB_ENV` writes ordered by positively established execution;
- step-local `env:` overriding an inherited/global `GITHUB_ENV` baseline before shell/CLI/package-manager interpretation.

These remain design/learning evidence; no product source implementation was added in the observed main-only delta.

### Reality check against those new B4 cases

Product Simulation tested incidence rather than treating the synthetic examples as automatically high-priority.

Observed-real:

- single package-manager control propagated through `GITHUB_ENV`;
- literal workflow/job/step package-manager env;
- shell-local package-manager assignments/exports;
- later no-sync execution after earlier explicit state formation.

Plausible-unobserved in the bounded inspected sample:

- two same-variable package-manager `GITHUB_ENV` writes before one consumer;
- same package-manager variable propagated through `GITHUB_ENV` and then overridden by step-local `env:`;
- exact `PIP_DRY_RUN` workflow/GITHUB_ENV shapes.

Many broad search hits were false relationship signals: the file contained both a package-manager variable and `GITHUB_ENV`, but the environment-file write targeted a different variable. This reinforces the rule `co-occurrence != data-flow relation`.

The conclusion is not to reject main's correctness rules. It is to avoid allowing currently synthetic-only collision shapes to justify broad infrastructure without stronger real pressure.

### Retargeting reality check

Public workflow discovery shows CLI retargeting (`pip install --target`, `--user`, `--prefix`) is clearly a real CI pattern. Equinor's reusable Python workflow is a concrete `--target` example.

However, recent Dependabot controls inspected so far (Elastic Rally #2189 and sqlalchemy-cockroachdb #308) contain retargeted tooling/published-package commands that are **not** the exact changed-dependency consumer. This makes retargeting real as a semantic class while leaving the stronger supported-update relationship unresolved.

Durable artifact: `product-simulation/2026-09-22_RETARGETING_REALITY_CHECK.md`.

### G4 bridge

TileDB-Py proves exact runtime compatible-tag witness feasibility today, but its inspected historical Python Dependabot PR #865 predates the `pip debug --verbose` witness. p4p #81 similarly lacks that witness at the exact proposal revision.

Therefore G4 currently has:

`real witness mechanism` + `real dependency updates` but not yet `one exact supported-update case composing both`.

This gap was appended to the G4 artifact rather than filled with mismatched revisions.

### Route from here

Continue the portfolio, with priority determined by new information:

1. look for one exact supported update whose relevant changed-dependency consumer is truly retargeted;
2. look for a current dependency update naturally exposing exact wheel tags;
3. continue reality-checking new main synthesis counterexamples, especially when they start synthetic;
4. search broader forward seams rather than staying only inside B4;
5. periodically re-read main but keep this branch independent.

## 9. Main sync + B5 pressure test

### Main sync

Latest `main` was merged into this research branch with merge commit `6386e52686556da27545693869bc54ffb4f552db`.

Synced main head at that point:

`42828b29c3be01e0b102189349f422007a529d96` — `Record B5 dependency-state proof contract candidate`.

After sync the research branch was 0 commits behind main. Main itself was not modified.

Main-owned changes brought in by the sync were limited to:

- `MEMORY.md`;
- `working-memory/2026-09-21_runtime-install-command-semantic-eligibility.md`;
- `working-memory/2026-09-22_b4-environment-evidence-data-flow-learning.md`.

### Latest main state

B4 is now closed. Main moved to B5.

B5's current owned question is:

> Under what exact evidence composition may one semantically admitted dependency-consuming command occurrence plus exact successful runtime execution justify the bounded proposition that the proposed version was satisfied/present at the admitted command-completion boundary?

The current candidate uses positive premises P1-P7: exact dependency identity, exact source/environment relation, exact static consumption, command-local eligibility, effective-semantics closure, exact runtime success, and manager operation guarantee.

The intended positive claim is deliberately `satisfied/present at command completion`, not `installed by this command`. Later persistence, exercise, compatibility, safety, artifact identity, and maintainer action remain non-claims.

### S014 — direct real B5 pressure case

Product Simulation searched specifically for a real successful command where the proposed version was already satisfied rather than freshly installed.

Found: `HaitamELF/production-ready-cicd#11`.

Dependabot transition:

`requirements-tooling.txt: pip==26.1.2 → pip==26.2.1`.

The workflow blob is identical at base and head. The exact dependency-audit command is:

`python -m pip install -r requirements-tooling.txt`.

Natural base/head pair:

- base run `35755384469`, job `106839725526`: setup-python provides pip 26.2.1, then the command collects pip 26.1.2, uninstalls 26.2.1, and installs 26.1.2;
- PR run `35756041967`, job `106841940374`: the same command reports `Requirement already satisfied: pip==26.2.1 ... (26.2.1)` and does not freshly install pip.

Observed PR runtime used synthetic merge commit `65bbb07fd28cdbdc224d3ed655af96f3480ec429`, not bare head `9ee04438...`.

Durable result:

`successful exact pip command` does not imply `proposed version newly installed by this command`.

The strongest common proposition is exactly B5's proposed wording:

`exact requested version satisfied/present at command completion`.

### Additional proof-route seam

S014 also exposes a distinction main should preserve:

`operation-guarantee inference` and `direct runtime state observation` are different proof routes.

The PR log directly reports the exact version as already satisfied. If direct state witnesses are later admitted, they should have their own trust/identity contract rather than being forced through the state-producing-command route. A command could be defeated as a state producer while an independent direct state witness still establishes preexisting state.

This is conceptual pressure only; current Product Simulation does not authorize log ingestion or implementation.

Artifacts:

- `product-simulation/S014_CANDIDATE_SCREENING.md`
- `product-simulation/scenarios/S014-production-ready-cicd-pip-already-satisfied-vs-installed/`
- `product-simulation/S014_POST_CASE_SYNTHESIS.md`.

### Updated next route

Main-signal priority now shifts from generic B4 counterexample search to B5 evidence-route pressure:

1. test whether B5's operation-guarantee route has realistic counterexamples or manager-specific edge conditions;
2. search for direct state witnesses beyond pip's `Requirement already satisfied` output and compare their trust/identity needs;
3. preserve later-state continuity as separate from command-completion state;
4. continue the broader G4/retargeting/forward-pressure portfolio in parallel;
5. re-sync whenever main materially advances.
## 10. Latest B5 refinement sync + S015 marker-applicability pressure

### Main B5 refinement synced

Main advanced to `71e9a1ea84cc26397be895810393e1ca4a38154e` (`Refine B5 asymmetric state-proof contract`) and was merged into this branch with merge commit `f7589b7203e3d266ac6c59c7222e09b1964e11c0`.

The refinement makes the command-derived state proof explicitly asymmetric:

- complete positive path may establish requirement satisfaction at command completion;
- missing premise, unsupported semantics, or runtime non-success does not establish package absence;
- an explicit semantic defeater rejects the occurrence as the positive witness but still does not prove package absence.

This aligns with S014 and became the target for the next real-case pressure pass.

### S015 — marker-scoped requirement applicability

Found and admitted `jawah/charset_normalizer#769`.

Relevant exact transition in `ci-requirements.txt`:

`pytest==8.3.5 ; python_full_version == '3.8.*'`

→

`pytest==9.0.3 ; python_full_version == '3.8.*'`.

Base/head CI workflow blob is identical (`760ab82d...`). Observed PR runtime uses synthetic merge commit `ddf477c2e71894890245a780ea17d2368d4ad64d`.

Discriminating matrix evidence:

- Python 3.9 job `85302679286`: same requirements file and same install command succeed; pip explicitly ignores the changed `python_full_version == '3.8.*'` pytest requirement and installs the separate Python-3.9 pytest version.
- Python 3.8 job `85302679272`: the marker applies; pip attempts `pytest==9.0.3` and fails with `No matching distribution found`.

### Current product projection

Inspection of `src/upgradepilot/dependency/requirements.py` shows the current exact-requirement extractor accepts only bare whole-line `package==version` pins. Marker-decorated lines do not match `_PINNED_REQUIREMENT_PATTERN`.

Therefore current UpgradePilot conservatively rejects this real proposal before B5 rather than accidentally overclaiming it.

That current limitation is safe but materially real.

### Durable invariant

If marker-bearing exact requirements are ever admitted:

`file consumed + command success` is still insufficient.

The proof must preserve:

`exact package/version + marker + justified selected runtime environment → requirement applicability`.

Only then may B5 command-success/state semantics apply.

This also strengthens the earlier G2 matrix finding: one static job key can expand into rows with different active dependency requirements.

### B5 asymmetry validation

The Python 3.8 failure blocks the positive command-derived state proposition but does not prove package absence. The Python 3.9 success proves only requirements applicable in Python 3.9 and cannot be borrowed to prove the Python-3.8-scoped proposal.

Artifacts:

- `product-simulation/S015_CANDIDATE_SCREENING.md`
- `product-simulation/scenarios/S015-charset-normalizer-marker-scoped-pytest/`
- `product-simulation/S015_POST_CASE_SYNTHESIS.md`.

### Next B5 pressure target

Seek the uv/scoped-operation analogue:

`selected lock/project source + successful uv sync/run`

where the exact changed dependency is excluded by group/package selector or another admitted scope rule.

The question is whether the current/future P2/P7 design keeps lock identity separate from the subset actually synchronized. This should be investigated with real dependency-update evidence before adding new product complexity.