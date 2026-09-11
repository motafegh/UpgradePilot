# UpgradePilot Current Memory

**Last updated:** 2026-09-11  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** complete A-phase orientation/admission mapping for the `run targeted checks` maintainer action before any new synthesis implementation.
- **Mode:** Planning/Design orientation + Learning-by-Doing; Build for this new slice has not started.
- **Selected plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Accepted stable synthesis owner:** `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`.
- **Active working memory:** `working-memory/2026-09-11_targeted-check-action-admission.md`.
- **Previous working memory:** `working-memory/2026-09-11_synthesis-first-evaluator-build.md`.
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

## Current targeted-check admission question

The accepted `run targeted checks` permission requires all of these, not merely existence of a useful technical check:

```text
exact decision-critical unresolved proposition(s)
+ bounded maintainer-performable discriminating check(s)
+ outcome interpretation / stopping logic
+ no justified UpgradePilot-executable equivalent investigation first
+ no broader adaptive inquiry needed instead
+ no independently established block condition
```

S006 is the initial real-derived design-pressure anchor. It establishes a narrow Pydantic V1/V2 differential check for one exact qldebugger validator behavior gap, with explicit information value and claim limits, but S006 itself deliberately stopped before a maintainer action. Therefore:

```text
useful discriminating technical check exists
!=
Charter action `run targeted checks` is automatically permitted
```

A-phase must map every permission premise to current `PublicPullRequestInvestigation` evidence/producers and distinguish facts already available, safely derivable, genuinely missing, or owned by an earlier investigation responsibility.

## Trust restrictions still relevant

The separate correctness work remains the owner of these defects; synthesis must respect their proof-strength consequences when a future action attempts to rely on them:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is not established by current run/head checks.

## Remaining upstream/action-admission gaps

- targeted checks are now the selected A-phase responsibility: exact producer/derivation mapping and outsourcing boundary remain to be established before Build;
- declared-Python-support block path still needs normal-path proof of every premise in synthesis specification §7.4.1;
- merge still needs positive bounded discovery/context coverage;
- investigate still needs a proven adaptive inquiry distinction rather than generic uncertainty;
- defer still needs a specific outside/future responsibility plus re-entry trigger;
- unresolved Python post-attempt continuation and artifact exact wheel compatibility remain upstream responsibility gaps where applicable.

## Immediate continuation

Canonical Learning-by-Doing loop for the targeted-check slice:

```text
A — CURRENT: orient the accepted targeted-check permission, S006 design pressure, and current investigation producers; map each permission premise to real evidence and identify any genuine missing handoff facts.
B — NOT STARTED: implement only the smallest producer-grounded targeted-check permission/result increment if A proves it is justified.
C — NOT STARTED: preserve implementation/proof evolution if B begins.
D — NOT STARTED: inspect actual behavior/tests and transfer ownership of the implemented permission boundary.
E — NOT STARTED: repair remaining gaps and choose the next slice only after this action's bounded proof is understood.
```

Do not integrate the CLI or enable `run targeted checks` merely because S006 contains a good check. First prove the full maintainer-action permission at the current producer boundary.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
