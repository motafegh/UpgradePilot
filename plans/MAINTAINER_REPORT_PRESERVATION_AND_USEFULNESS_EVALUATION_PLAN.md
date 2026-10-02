# Maintainer Report, Preservation and Usefulness Evaluation Plan

**Status:** prepared conditional plan; not implementation authorization or a passed usefulness gate.
**Responsibility:** deliver and assess a faithful report of one normal dependency-update investigation, preserve the named result boundary, and determine whether it helps maintainers.
**Selection gate:** [Product Direction and Maintainer Utility Investigation](PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md).
**Project route:** [Evidence-Derived Learning and Building Plan](UPGRADEPILOT_90_DAY_PLAN.md).
**Live selection:** [MEMORY.md](../MEMORY.md) alone.

## 1. Full responsibility and first increment

The supported user must be able to identify the exact update, understand material findings and their sources, distinguish what remains unknown, and identify a justified next step where one exists. The user must be able to inspect the same named result later. Final actions remain subject to the accepted [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) contract.

The first delivery trial is a normal-path human report plus a versioned saved-result representation, with meaningful incomplete/degraded/unsupported behavior and a declared evaluation protocol. It is not a new evidence acquisition engine.

Important deferred responsibilities:

- full raw-response capture, recomputation of deterministic reasoning, execution resume and cross-run query infrastructure;
- broad impact discovery and comprehensive workflow/environment coverage;
- new action permissions, AI-written final synthesis, patch generation and target writes;
- web/API interfaces, multi-repository operations and private/multi-ecosystem input.

These are distinct proof obligations rather than conveniences removed to pass a small test. Saved-result reopening makes a report inspectable, but cannot reproduce unrecorded acquisition or reasoning. Known coverage limits must remain visible rather than disappearing from the evaluation denominator. If independent users need recomputation or richer impact evidence before the output is useful, revise the trial or activate the exact missing responsibility rather than declare success.

## 2. Entry conditions and contract decisions

Before implementation selection:

1. the direction comparison selects independent report utility as a justified trial;
2. exact normal producer/source boundaries have been traced;
3. report required states, source references, supported claims and availability distinctions are accepted through the correct semantic owner;
4. saved-result version/identity/reopen/error semantics have a clear owner;
5. an evaluation protocol freezes case selection, input mode, criteria and baseline before result inspection;
6. unresolved design decisions and authorized Build scope are explicit.

Use the [Core Pipeline](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) and Naming Clarity specifications. Extend an existing semantic owner when it fits; create a report specification only if the public report/serialization responsibility genuinely cannot be owned cleanly there. Do not invent an ADR for ordinary rendering; a consequential persistence or package-boundary choice may require one.

The [existing replay proposal](../proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md) informs alternatives, not an accepted schema or storage decision.

## 3. Proposed report contract to resolve before Build

The following are design requirements to evaluate and promote, not already implemented public fields:

| Report concern | Required design decision / proof |
| --- | --- |
| Exact identity | Repository, PR, base/head, dependency transition and relevant observed revisions remain distinguishable |
| Findings | Material meaning and supporting evidence; candidate, grounded interpretation, observation and applicability are not flattened |
| Coverage/availability | Supported, unsupported, not evaluated, not activated, no admitted candidate and unresolved outcomes remain distinguishable where material |
| Runtime strength | Static consumption, runtime correlation and command-completion package state retain their separate propositions; no implicit later-use/behavior claim |
| Unknowns | Explain material uncertainty and its consequence; empty projected uncertainty is not global closure |
| Next checks | Only producer-grounded, discriminating proposed checks with interpretation and stop/re-entry logic; allow no justified check |
| Actions | Existing admitted action or explicit unavailable/not evaluated synthesis; do not manufacture non-abstention or represent operational failure as semantic abstention |
| Sources | Recoverable references of correct evidence class, with explicit missing source content rather than fabricated citations |
| Saved result | Named schema/method version, run identity, exact input/configuration identity actually available, output integrity and explicit unsupported/corrupt versions |
| Failure/exit behavior | Result printed, partial result, acquisition failure and action disposition must not be confused |

Do not require every output to have a finding or check. Honest limitations can pass faithfulness while failing usefulness. No report field may claim producer facts that the investigation did not retain; either record that absence or admit a precise producer-retention change.

## 4. Design and implementation sequence

### Establish the baseline and proof boundary

Capture the current CLI output under exact declared input conditions. Freeze a product/case identity manifest separately from expected findings and forbidden claims. Use existing development cases as such; do not call them blind or protected once their conclusions informed design.

Inspect `PublicPullRequestInvestigation`, `cli.py`, `maintainer_action.py`, their focused tests and the normal evidence producers. Record which facts exist but are not presented, versus facts unavailable to the producer. Include runtime-state and static-only CI boundaries.

### Settle projection and preservation ownership

Prefer a faithful projection over the existing typed investigation. Presentation cannot rerun parsers, establish applicability, invent checks or recreate provider authority. Share the semantic result between human and saved output rather than maintaining two inference paths.

Choose an explicit serialization boundary; do not blindly serialize every dataclass or freeze internal type shapes as a public API. Compare inspectable file export with storage only where real query/lifecycle needs exist. Define schema-version compatibility, incomplete writes, result identity and redaction at that boundary.

Reopening a saved report must make its observation time/revisions and stale-now status understandable. It must not make live requests or imply fresh validation. Full deterministic replay requires recorded recomputation inputs and a separately admitted gate.

Promote settled framework-independent semantics and consequential methods before Build follows. Stop here if an owning decision is unresolved.

### Implement only after authorization

Expected edit anchors: `src/upgradepilot/cli.py`, the typed investigation consumer boundary, and `src/upgradepilot/maintainer_action.py` only if uncertainty/action projection changes are selected. Keep `investigation.py` orchestration-only unless precise input retention is independently necessary. Introduce a responsibility-named report module only when real implementation needs it; no speculative package tree.

Relevant existing tests: `tests/test_cli.py`, `tests/test_maintainer_action.py`, `tests/test_investigation.py`, and runtime-state composition tests where that seam matters. Add serialization/reopening tests at the actual implementation owner once admitted.

### Verify normal producer and consumer composition

Required contrasts:

- normally produced supported evidence with material findings;
- static-only CI and an admitted command-completion state, preserving different proof strength;
- unresolved runtime semantics and no admitted runtime candidate;
- semantic-provider unavailable/no claim/invalid claim, kept distinct;
- unsupported dependency transition and acquisition failure before result formation;
- artifact applicability unavailable at the exact target-evidence boundary;
- saved result reopened offline, malformed/version-incompatible input and interrupted publication.

Use fixtures to isolate a state; they do not prove normal acquisition, public prevalence or independent user benefit. A fixture-built positive runtime witness is labeled controlled proof. Obtain representative normal-path evidence for externally claimed product coverage, or record that debt.

Run focused checks first, then the justified product regression and installed CLI checks. A renderer need not require fresh model inference unless semantic-provider behavior changed. No tool/experiment result becomes a product pass.

## 5. Independent usefulness evaluation

Reuse [the report development evaluator](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md) and its case/rubric files. Update evaluation machinery only when separately authorized. Preserve separate comparability, claim discipline, finding coverage, stopping and usability results.

Predeclare:

- normal product-output versus curated-evidence presentation mode;
- exact cases/revisions, supported capabilities and unavailable inputs;
- baseline current CLI and, for an outcome study, ordinary PR/CI/release-note review with equivalent decision-time information;
- tasks, reviewer independence, assistance, order controls and time/error recording;
- required findings/unknowns and forbidden stronger claims, hidden from producers;
- success/rejection criteria and where outputs/judgments are preserved.

Minimum scoped acceptance: zero critical false/misattributed claims, all required bounded findings/unknowns preserved, and independent reviewers correctly recover exact update, important finding, supporting source, proof limit and justified next step or absence of one. Demonstrate concrete added utility on contrasting development cases relative to baseline. Do not assert a percentage/time improvement without a suitable measured comparison. Sample size and recruitment must match the strength of the intended claim; a small study establishes bounded usability, not population benefit.

For later discovery/model generalization claims, establish protected evaluation with repository/release-family/time separation, human-adjudicated labels and decision-time inputs. Merge status and future incident history are not direct labels for a correct recommendation. Do not repurpose contaminated development cases as unseen evaluation.

If independent reviewers are unavailable, implementation/faithfulness may be verified while usefulness remains explicit debt. Do not mark the entire plan passed or block unrelated deterministic work under a falsely completed gate. If a report is faithful but adds no useful assistance, simplify/revise it or activate the precise discovery/coverage prerequisite; more polished prose is not a remedy by itself.

## 6. Completion, stop and subsequent responsibilities

Report the gates independently: contract/design accepted; authorized implementation verified; saved-result reopening verified; independent usefulness established or unproven. Complete this plan only for the selected declared outcome with its required gates met. MEMORY.md records the exact live stopping point.

Further entry conditions:

- deterministic replay: users/evaluation need recomputation and exact captured inputs can support it;
- discovery: material omitted changes prevent useful findings;
- coverage/runtime observation: a scoped missing fact blocks a useful conclusion/check;
- action admission: positive permission becomes normally reachable, through the synthesis owner;
- migration: a concrete breaking-change remedy has independent verification evidence.

Stop before another capability build. No database, graph, model, agent, broad resilience framework or target mutation follows automatically from a successful report trial.
