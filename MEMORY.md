# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
and the current environment remain the authority for actual behavior.

## Current responsibility

Manual end-to-end runtime simulation under
[`plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md),
using [`product-simulation/`](product-simulation/).

The current responsibility is to manually perform and document the complete
intended UpgradePilot runtime on materially different real public dependency-
update cases before further product implementation.

M2-S03 is paused, not rejected. Its retained plan is
[`plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md).
It may resume only after simulation synthesis and explicit approval of any
required corrections.

M2-S02 is closed with a negative local-model extraction disposition. Its record is
[`working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](working-memory/2026-07-22_M2-S02_llm-extraction-session.md).

## Manual simulation progress

### S001 — complete with retrospective execution retrofit

Navigation:
[`product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md)

Case: `pydantic/pydantic#13432`, Soup Sieve 2.6 → 2.8.4.

Outcome:

> Merge after normal maintainer review.

Material findings:

- one PR URL located the case; exact repository, PR, base, head, dependency, and
  version identity were then frozen;
- Soup Sieve was a transitive documentation-tooling dependency through
  `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- reviewed advisories affected 2.6 and were fixed by 2.8.4, but vulnerable-package
  presence and target exploitability remained separate;
- Pydantic's Python boundary was compatible;
- documentation CI exercised the resolved dependency path and succeeded;
- release notes, green CI, advisory data, or target usage alone were insufficient;
  the decision required joined evidence.

Correction:

- official advisory pages currently state publication on June 1, 2026;
- the exact Dependabot trigger remains unresolved;
- the original stronger security-trigger inference is superseded;
- the primary recommendation is unchanged.

S001 was investigated before the new progressive-record protocol. Its
`EXECUTION_TRACE.md` is an honest retrospective reconstruction with explicit gaps,
not a claim of contemporaneous live logging.

### S002 — complete progressive runtime

Navigation:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md)

Primary record:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md)

Case: `Aidan-Wallace/kubernetes-dashboard-token-api#20`, HTTPX 0.27.2 → 0.28.1.

Outcome:

> Run targeted checks; merge only if the exact-head Python checks pass under a
> captured dependency resolution.

Material findings:

- HTTPX was directly declared, functionally used through FastAPI/Starlette
  `TestClient`, and installed into the production image because test/runtime
  dependencies shared one requirements file;
- HTTPX 0.28 removed the deprecated `app` Client argument;
- Starlette 0.36.3 passed that argument, while 0.37.2 no longer did;
- FastAPI 0.115.2 required Starlette >=0.37.2, making a then-current resolution
  likely compatible but not proving the target's exact historical environment;
- Docker CI succeeded and proved installation/image construction only;
- the Python workflow defined Ruff and `pytest --cov`, but its path filter excluded
  `requirements.txt`, so the decision-relevant tests did not run for the PR;
- historical Docker logs expired with HTTP 410, leaving exact resolved
  FastAPI/Starlette versions unavailable;
- the predecessor HTTPX 0.28.0 PR was explicitly superseded by the 0.28.1 PR;
- the eventual merge is user-action history, not correctness evidence.

S002's most important product-model change:

> CI evidence must include changed-path trigger coverage, commands actually
> executed, responsibility exercised, exact revision, and tested environment
> identity. A green status alone cannot receive global decision authority.

S002 used `CASE.md` as the progressive primary record. Candidate screening,
approach rationale, expected outputs, failed log retrieval, superseded findings,
output/outcome distinctions, and result-to-next-action transitions are preserved.
No separate execution trace was needed.

## Cross-case evidence so far

```text
real PR locator
→ freeze exact case identity
→ classify declaration, functional use, and installation
→ acquire upstream/package/framework evidence
→ map repository-specific path
→ inspect CI triggers, commands, revision, and environment identity
→ preserve missing, contradictory, skipped, inaccessible, or expired evidence
→ construct bounded recommendation and targeted recovery action
→ produce human and conceptual machine results
→ record user follow-up and product-model changes
```

S001 demonstrates evidence joining across lock graph, advisories, repository use,
and relevant CI. S002 demonstrates adapter-aware compatibility, misleading/partial
green CI, skipped-check state, environment drift, supersession, and expired
evidence.

## Verified current implementation

The repository currently provides:

- strict case identity and evidence contracts;
- attributed Python-support claim contracts with application-assigned
  `model_derived` authority and transformation identity;
- mechanical evidence grounding for eligibility, exact unique quotation, version
  presence, and duplicate candidates;
- deterministic decision outcomes currently limited to `run_targeted_checks` or
  `abstain`;
- an LM Studio structured-output extractor retained for experiments;
- an input-risk detector and evaluator retained for experimental evidence;
- live semantic and decision-effect evaluators with preserved JSON artifacts.

Normal experimental extraction orchestration:

```text
accepted release-note EvidenceItem
→ untrusted schema-constrained candidate attributed claims
→ mechanical source grounding
→ model-derived attributed claims
→ deterministic bounded decision
```

No current model has shell, filesystem, GitHub, credential, tool, mutation, or
merge authority. JSON Schema constrains output shape; it does not establish
semantic truth.

## M2-S02 final disposition

Both tested local deployments were rejected for normal semantic extraction:

- `gemma-4-e2b-it`: 9/14 correct grounded claims and 11/14 correct decision effects;
- `qwen3-4b-instruct-2507`: 8/14 correct grounded claims and 10/14 correct decision
  effects;
- repeated false dropped-support claims materially changed downstream decisions.

Keep raw evidence preservation, strict schemas, quotation, provenance,
model-derived authority, bounded deterministic effects, and explicit unresolved
states.

Reject from normal M2 runtime both tested deployments, the mandatory second-model
risk gate, and phrase/category regexes used as semantic interpreters. Retain them
as negative experiment evidence.

## Evidence and truth boundary

```text
source observation
→ attributed source claim
→ interpretation
→ corroborated / contradicted / irrelevant / unresolved finding
→ bounded decision
```

Accepted release-note evidence means the source was recorded and is eligible for
processing. It does not make every statement true. Grounding proves correspondence
to cited content; it does not independently corroborate the claim.

Evidence lineage without operation lineage can allow an incorrect inference to
survive into a polished result. S002 additionally shows that CI status without
trigger/command/environment lineage can create a false favorable conclusion.

## Immediate continuation

1. review S002's scenario README and progressive `CASE.md`;
2. challenge the dependency-role classification, framework threshold, CI authority,
   missing evidence, and targeted-check outcome;
3. verify that every material approach, failure, supersession, and
   result-to-next-action transition is represented honestly;
4. update S002 only if review finds a real evidence or reasoning defect;
5. select S003 because it addresses the highest-value remaining uncertainty:
   an actual failing dependency-update workflow requiring attribution among
   update-caused, pre-existing, flaky, environmental, and unrelated failure;
6. continue using one live progressive `CASE.md` per normal scenario;
7. update coverage only from actual case evidence;
8. use at least ten materially different cases and continue when major uncertainty
   remains;
9. after synthesis, decide the smallest corrected implementation responsibility
   and whether M2-S03 should resume unchanged, be revised, or be replaced.

Do not implement product code, select permanent architecture, or resume M2-S03
while the manual simulation plan is current.

## Ownership and assistance

- Ali identified the difference between source claims and corroborated truth and
  required responsibility-level product planning.
- Ali identified that incremental implementation lacked a complete runtime model
  and authorized manual product simulation.
- Ali required exact operational reasons, tools, failures, switches, and result
  lineage after S001 exposed that gap.
- Ali requested a new non-duplicate full case and authorized repository delivery.
- S001 and S002 were substantially selected, investigated, reasoned, and documented
  by AI under Ali's direction; independent Ali ownership is not claimed.
- The implementation, tests, evaluators, and earlier records are substantially
  AI-generated under Ali's direction unless a narrower ownership claim is
  explicitly evidenced.

## Career boundary

Do not update Career for ordinary project progress. Ali explicitly initiates a
Career review for capability, workload, strategy, or durable program changes.

## Detailed evidence

Use current source/tests, the closed M2-S02 plan and record, the paused M2-S03
plan, the current simulation plan, scenario records and coverage, evaluation
artifacts, specifications, Git history, and actual command outputs.

Do not copy this continuation into stable entrypoints or Career.
