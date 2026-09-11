# UpgradePilot Current Memory

**Last updated:** 2026-09-11  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** strengthen exact GitHub Actions run/job attempt coherence before using richer CI execution evidence as an upstream prerequisite for targeted-check synthesis.
- **Mode:** Planning/Design orientation + Learning-by-Doing; bounded Build for the CI correction is authorized after A resolves the smallest enforceable correction shape.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Supporting historical investigation owner:** `plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`; that investigation established the attempt-binding question but did not itself authorize repair.
- **Accepted stable synthesis owner:** `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`.
- **Active working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Previous working memory:** `working-memory/2026-09-11_targeted-check-action-admission.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Accepted synthesis boundary

```text
PRODUCT DECISION MODEL
→ technical candidate / applicability / investigation / stopping

MAINTAINER ACTION SYNTHESIS
→ action-relative evidence sufficiency
→ one Charter action
→ decisive reasons / residual uncertainty / follow-up / claim limits
```

Every non-abstention action requires its own positive permission. The action family is not a severity ladder.

Stable meanings remain:

```text
MERGE AFTER NORMAL REVIEW
positive bounded evidence/context/coverage closure established
+ no material non-favorable condition remains

RUN TARGETED CHECKS
one or a small stable set of exact decision-critical unknowns
+ bounded discriminating maintainer-performable checks
+ enough outcome interpretation/stopping logic
+ no justified UpgradePilot-executable investigation should do the same work first
+ no broader adaptive inquiry or independent block condition defeats the permission

INVESTIGATE OR BLOCK — investigate disposition
material concern grounded
+ concrete broader/adaptive inquiry
+ not reducible to one stable bounded check set
+ no independent block condition established

INVESTIGATE OR BLOCK — block disposition
material exact current-proposal hold condition established strongly enough
that the proposal should not progress as-is

DEFER
specific useful outside/future responsibility or condition
+ concrete reassessment/re-entry trigger

ABSTAIN
no other Charter action positively justified at current proof strength
```

## Corrected action admission

The externally authored correction commit `a25d7f9b5a10d696f8d763e1b4c6d46ad53009e7` was reviewed and retained.

Most importantly:

- `PythonSupportDropImpactAssessment.applicability == established_applicable` does **not** by itself authorize `block`;
- a declared-Python-support hold additionally requires a real target support obligation, dependency/environment relationship, preserved upstream claim authority, and the resulting exact proposal-level conflict;
- grounding a model-derived upstream claim establishes source correspondence, not independent semantic corroboration;
- absence of a generic producer for a final action does not prove a narrow action-specific derivation is impossible.

At the currently reviewed producer boundary, no non-abstention runtime path has yet passed its complete action-specific admission proof.

## First evaluator implementation — completed bounded slice

Added:

- `src/upgradepilot/maintainer_action.py`
- `tests/test_maintainer_action.py`

Current implemented flow:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

The first evaluator intentionally admits only explained abstention and preserves the exact source investigation, decisive reasons, projected residual uncertainty, admission limitations, and claim limits.

No CLI/application integration has been added yet. No merge, targeted-check, investigate, block, or defer runtime branch exists yet.

## Synthesis implementation mental model

The current learning/ownership model is:

```text
scenario-specific technical complexity
→ investigation producers
→ normalized typed findings
→ generic action-permission semantics
→ maintainer-facing synthesis action
```

The deterministic baseline is the whole first transparent synthesis implementation, not one handwritten rule per repository/tool/environment scenario. Action permission conditions are established from lower-level propositions and typed evidence. `abstain` is the initial least-committal admitted action, not the bottom of a severity ladder. A future bounded LLM-assisted synthesis role remains a candidate only if later evidence demonstrates a real limitation; no LLM is required for the currently admitted evaluator.

## Validation state

Established on Ali's actual project environment for the first evaluator slice:

- local `main` synchronized through commit `4152117` before execution;
- project `.venv` active under Python 3.12.3 at `/home/motafeq/projects/UpgradePilot/.venv/bin/python`;
- focused synthesis suite passed: `2` tests, `OK`;
- broader repository unit suite passed: `530` tests in `0.143s`, `OK`;
- manual runtime inspection returned explained `abstain`, empty residual uncertainty for the supported-transition fixture, explicit limitations/claim limits, and preserved source-investigation identity;
- previously recorded source/static inspection remains established.

Therefore the first evaluator's executable-proof debt is closed at the unit-test boundary.

Still not established / not implemented:

- application/CLI integration behavior;
- any non-abstention runtime action;
- complete human-facing report projection;
- persistence/serialization;
- objective safety or complete discovery/context coverage.

## Targeted-check admission — paused on upstream evidence reliability

The accepted `run targeted checks` permission requires all of these, not merely existence of a useful technical check:

```text
exact decision-critical unresolved proposition(s)
+ bounded maintainer-performable discriminating check(s)
+ outcome interpretation / stopping logic
+ no justified UpgradePilot-executable equivalent investigation first
+ no broader adaptive inquiry needed instead
+ no independently established block condition
```

S006 remains the initial real-derived design-pressure anchor. It establishes a narrow Pydantic V1/V2 differential check for one exact qldebugger validator behavior gap, with explicit information value and claim limits, but S006 itself deliberately stopped before a maintainer action. Therefore:

```text
useful discriminating technical check exists
!=
Charter action `run targeted checks` is automatically permitted
```

The targeted-check A-phase mapped current producers and found that artifact serviceability already preserves exact wheel-compatibility uncertainty and deterministic reevaluation semantics, but no producer-grounded maintainer-outsource contract is yet established. Before asking the maintainer to perform that work, the system should first evaluate whether trustworthy existing/read-only CI execution evidence can resolve some of the proposition itself.

That route is currently blocked by the CI run/job attempt-coherence weakness described below. Therefore targeted-check synthesis B remains deliberately unstarted while the bounded upstream CI prerequisite is repaired.

## Current CI attempt-coherence responsibility

Current source establishes:

```text
WorkflowRun
→ preserves run_id + head_sha + run_attempt

GitHubActionsClient.get_workflow_jobs(...)
→ requests run-level jobs with filter="latest"

WorkflowJob
→ preserves run_id + head_sha
→ does not preserve attempt identity
```

Current checks prove run ID and frozen PR-head coherence, but do not prove that the consumed jobs belong to the same `run_attempt` represented by the `WorkflowRun`. A rerun can therefore create a mixed-attempt evidence risk even when run ID and head SHA are unchanged.

This issue was intentionally recorded but not repaired by the September 8 correctness investigation. It is now action-critical because stronger CI execution/log evidence must not be attached to an uncertain attempt identity.

The selected bounded invariant is:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact run attempt
+ jobs acquired from that same attempt
→ coherent factual CI execution evidence
```

This repair alone does **not** establish static-to-runtime step correlation, dependency installation, wheel compatibility, complete CI coverage, safety, or a maintainer action.

## Trust restrictions still relevant

The separate correctness work identified three established reliability concerns that synthesis must respect at actual proof strength:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is not established by current run/head checks — **this is the currently selected bounded repair responsibility**.

Repairing item 3 does not silently repair items 1 or 2.

## Remaining upstream/action-admission gaps

- CI attempt coherence is the live upstream prerequisite selected from targeted-check A-phase;
- after that repair, decide whether a second bounded read-only CI evidence slice can establish a positive dependency/wheel-serviceability witness without reconstructing a target environment;
- targeted-check synthesis must then resume with the resulting producer boundary and still prove the full maintainer-action permission;
- declared-Python-support block path still needs normal-path proof of every premise in synthesis specification §7.4.1;
- merge still needs positive bounded discovery/context coverage;
- investigate still needs a proven adaptive inquiry distinction rather than generic uncertainty;
- defer still needs a specific outside/future responsibility plus re-entry trigger;
- unresolved Python post-attempt continuation and artifact exact wheel compatibility remain upstream responsibility gaps where applicable.

## Immediate continuation

Canonical Learning-by-Doing loop for the CI attempt-coherence slice:

```text
A — CURRENT: re-anchor the GitHub Actions provider/type/test boundary, earlier attempt-mixing finding, downstream CI consumers and authoritative specific-attempt job API semantics; select the smallest enforceable same-attempt correction and discriminating rerun test.

B — NOT STARTED: implement only the bounded same-attempt acquisition correction at the existing provider boundary; preserve exact head/run identity; add stable-attempt and rerun contrasts; propagate representation only where genuinely required; do not add logs or wheel semantics in the same slice.

C — NOT STARTED: preserve exact implementation/test evidence, surprises, proof strength and remaining non-proof.

D — NOT STARTED: learn from the actual provider → typed job evidence → CI-consumer flow and verify ownership of what attempt coherence proves and does not prove.

E — NOT STARTED: repair remaining gaps, then decide whether the next justified slice is a read-only positive CI execution/wheel witness or a return to targeted-check synthesis. Do not silently start that next responsibility before D/E closes.
```

Do not integrate the CLI, enable `run targeted checks`, parse job logs, or reconstruct target environments during this attempt-coherence slice.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`