# UpgradePilot Current Memory

**Last updated:** 2026-09-11  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** complete the first bounded deterministic maintainer-action synthesis evaluator at the currently admitted proof boundary, then obtain executable proof before choosing the next synthesis implementation slice.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Accepted stable synthesis owner:** `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`.
- **Active working memory:** `working-memory/2026-09-11_synthesis-first-evaluator-build.md`.
- **Previous working memory:** `working-memory/2026-09-11_synthesis-stable-semantic-acceptance.md`.
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
+ no justified UpgradePilot-executable investigation should do the same work first

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

At the currently reviewed producer boundary, no non-abstention path has yet passed its action-specific admission proof.

## First evaluator implementation

Added:

- `src/upgradepilot/maintainer_action.py`
- `tests/test_maintainer_action.py`

Current flow:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

The first evaluator intentionally admits only explained abstention.

`MaintainerActionSynthesis` preserves:

- the exact source `PublicPullRequestInvestigation` for traceability/provenance;
- decisive reasons;
- residual uncertainty projected from currently handled non-final states;
- evaluator/admission limitations;
- claim limits.

No CLI/application integration has been added yet. No merge, targeted-check, investigate, block, or defer runtime branch exists yet.

## Focused proof intent

The focused test file protects two current responsibilities:

1. a valid exact dependency transition does not default to favorable or another active maintainer action;
2. a typed dependency-analysis problem remains visible in the abstention reason and residual uncertainty.

A fixture error discovered during source inspection was corrected: `uv.lock` uses the admitted extraction method `exact_base_head_files`, not the invented `structured_lockfile` label.

## Validation state

Established:

- committed source/test diff inspected on current `main`;
- new test fixture reconciled with the actual dependency evidence vocabulary;
- Python 3.13 syntax compilation succeeded for local copies of the exact new source/test syntax;
- implementation diff since the corrected semantic baseline contains only the new synthesis module and focused test file.

Not yet established:

- focused unittest execution against the actual repository environment;
- broader regression suite;
- application/CLI integration behavior.

The assistant container cannot resolve `github.com`, so it could not clone the repository for test execution. GitHub reports no combined commit status or pull-request workflow run for the implementation commits. This remains explicit executable-proof debt, not a pass claim.

## Trust restrictions still relevant

The separate correctness work remains the owner of these defects; synthesis must respect their proof-strength consequences when a future action attempts to rely on them:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is not established by current run/head checks.

## Remaining upstream/action-admission gaps

- declared-Python-support block path needs normal-path proof of every premise in synthesis specification §7.4.1;
- merge needs positive bounded discovery/context coverage;
- targeted checks need an exact maintainer-performable discriminating check and stopping interpretation;
- investigate needs a proven adaptive inquiry distinction rather than generic uncertainty;
- defer needs a specific outside/future responsibility plus re-entry trigger;
- unresolved Python post-attempt continuation and artifact exact wheel compatibility remain upstream responsibility gaps where applicable.

## Immediate continuation

Canonical Learning-by-Doing loop for the first evaluator slice:

```text
A — DONE: oriented corrected action admission and selected explained abstention as the only currently admitted runtime action.
B — DONE: implemented the core result/evaluator and focused tests; corrected one invalid fixture during inspection.
C — DONE: implementation state and executable-proof debt preserved in working memory and this live handoff.
D — CURRENT: teach the real code/data flow and check Ali's ownership of abstention versus missing non-abstention implementation.
E — NEXT: repair any learning gap, obtain focused executable proof in an eligible environment, then choose the next bounded synthesis implementation slice.
```

Do not integrate the CLI or enable a non-abstention action before its own proof/admission prerequisites are satisfied.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`
