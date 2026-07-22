# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
and the current environment remain the authority for actual behavior.

## Current responsibility

Manual end-to-end runtime simulation under
[`plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md),
using the dedicated [`product-simulation/`](product-simulation/) workspace.

The current responsibility is to manually perform and document the complete
intended UpgradePilot runtime on materially different real public dependency-
update cases before further product implementation.

M2-S03 is paused, not rejected. Its retained implementation plan is
[`plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md).
It may resume only after the simulation synthesis is reviewed and any required
corrections are explicitly approved.

M2-S02 is closed with a negative local-model extraction disposition. Its detailed
record is
[`working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](working-memory/2026-07-22_M2-S02_llm-extraction-session.md).

## Manual simulation progress

### S001 complete with execution retrofit

Use the scenario navigation first:

[`product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md)

The scenario contains:

- [`CASE.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) — complete result, evidence model, report, variants, and product implications;
- [`EXECUTION_TRACE.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/EXECUTION_TRACE.md) — retrospective operation lineage, exact retained tools/arguments, reasons, expected and actual outputs, failures, superseded interpretations, and continuation.

S001 manually executes the complete intended runtime for
`pydantic/pydantic#13432`, a Dependabot lockfile update from Soup Sieve 2.6 to
2.8.4.

Manual outcome:

> Merge after normal maintainer review.

Material findings:

- one PR URL was sufficient as the invocation locator; exact repository, PR,
  base, head, dependency, and version identities were then discovered and
  frozen;
- Soup Sieve was a transitive documentation-tooling dependency, not a Pydantic
  runtime dependency;
- the actual path required lock-graph analysis:
  `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- two reviewed high-severity denial-of-service advisories affected 2.6 and were
  fixed by 2.8.4;
- vulnerable-package presence and target exploitability remained separate;
- Pydantic's Python `>=3.10` boundary was compatible with Soup Sieve 2.8.4's
  Python `>=3.9` requirement;
- PR documentation CI exercised the resolved dependency path and succeeded;
- release notes, green CI, advisory data, or target usage alone were
  insufficient; the decision required their joined evidence;
- the exact Dependabot trigger remains unresolved; a security trigger is
  plausible but is not established by the public evidence;
- the current M2 decision vocabulary is narrower than the real decision
  supported by this case, which is evidence for later synthesis rather than
  immediate implementation expansion.

### S001 factual correction

Fresh official-source verification during the execution retrofit corrected an
original timing error:

- both official advisory pages currently state publication on **June 1, 2026**,
  not July 9;
- they were therefore published more than one month before the July 10 PR, not
  one day before it;
- the original strong security-trigger inference is superseded.

The affected/patched ranges remain `<=2.8.3` and `>=2.8.4`, so the primary
recommendation is unchanged.

### S001 execution-record status

S001 was originally investigated and then documented. Its execution trace is an
honest best-effort retrospective reconstruction, not a claim of contemporaneous
live logging.

The trace preserves:

- exact retained GitHub connector operations and material arguments;
- selection reasons and expected outputs;
- actual material results;
- repeated review-thread retrieval that did not help;
- unreadable/truncated response-search attempts and the switch to bounded file
  retrieval;
- empty merge-SHA workflow/status lookups;
- the provisional `docs-upload`-only hypothesis and its lock-graph correction;
- proposed commands that were not run;
- details that cannot be recovered exactly.

S002 must use its active `CASE.md` progressively from selection onward rather
than relying on another retrospective reconstruction.

## Verified current implementation

The repository currently provides:

- strict case identity and evidence contracts;
- attributed Python-support claim contracts with application-assigned
  `model_derived` authority and transformation identity;
- mechanical evidence grounding that checks evidence eligibility, exact unique
  quotation, version presence, and duplicate candidates;
- deterministic decision outcomes limited to `run_targeted_checks` or `abstain`;
- an LM Studio structured-output extractor retained for experiments;
- an input-risk detector and evaluator retained for experimental evidence;
- live semantic and decision-effect evaluators with preserved JSON artifacts.

The normal extraction orchestration is:

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

- `gemma-4-e2b-it`: 9/14 correct grounded claims and 11/14 correct decision
  effects in the complete run;
- `qwen3-4b-instruct-2507`: 8/14 correct grounded claims and 10/14 correct
  decision effects in the complete run;
- repeated false dropped-support claims materially changed downstream decisions.

Keep raw evidence preservation, strict schemas, quotation, provenance,
model-derived authority, bounded deterministic effects, and explicit unresolved
states.

Reject from normal M2 runtime both tested deployments, the mandatory
second-model risk gate, and phrase/category regexes used as semantic
interpreters. Retain the implementations and results as negative experiment
evidence.

## Evidence and truth boundary

```text
source observation
→ attributed source claim
→ interpretation
→ corroborated / contradicted / irrelevant / unresolved finding
→ bounded decision
```

Accepted release-note evidence means the source was recorded and is eligible for
processing. It does not make every source statement true. Grounding proves that
an extracted claim corresponds to cited source content; it does not independently
corroborate that claim.

S001 further demonstrates that package, repository, dependency-path, advisory,
and exact CI evidence may all be required before an upstream claim receives a
repository-specific decision effect.

The execution retrofit further demonstrates that evidence lineage without
operation lineage can allow an incorrect source-timing inference to survive into
a polished result.

## Immediate continuation

1. review S001's scenario README, execution trace, and `CASE.md` together;
2. challenge whether every material approach, failure, switch, and result-to-next-
   action link is now represented honestly;
3. verify that the corrected advisory timing does not require another decision or
   product-model change;
4. select a second real case that materially contrasts with S001;
5. prefer a direct runtime dependency update with an API or behavior change and
   failing or conflicting CI;
6. create S002's `CASE.md` at selection time and update it progressively through
   current state → approach/reason → operation → output → interpretation →
   outcome → continuation;
7. update scenario coverage only from actual evidence;
8. use at least ten materially different cases and continue when major
   uncertainty remains;
9. after synthesis, decide the smallest corrected implementation responsibility
   and whether M2-S03 should resume unchanged, be revised, or be replaced.

Do not implement product code, select permanent architecture, or resume M2-S03
while the manual simulation plan is current.

All lists in the simulation workspace are non-exhaustive starting prompts. Real
case evidence may add, split, reorder, remove, or redefine actors, inputs,
evidence, stages, methods, outputs, states, and diagrams.

## Ownership and assistance

- Ali identified that manually supplied semantics did not satisfy automated
  extraction and required real local-model testing.
- Ali required both Qwen and Gemma evaluation and challenged conclusions based on
  output shape, token counts, and adversarial wording.
- Ali identified the decisive difference between a source claim and corroborated
  truth, causing the runtime architecture and threat model to be corrected.
- Ali rejected narrow phrase/grammar fixes and required responsibility-level,
  whole-project planning.
- Ali identified that incremental implementation without a concrete complete
  runtime model was causing local rabbit holes and authorized the manual product
  simulation responsibility.
- Ali identified that S001 did not preserve exact operational execution and
  required reasons, tools, commands, failures, switches, and result lineage to be
  added alongside the completed case.
- S001 was selected, investigated, reasoned, documented, and retrofitted
  substantially by AI under Ali's direction; independent Ali ownership has not
  been claimed.
- The implementation, tests, evaluators, and earlier records are substantially
  AI-generated under Ali's direction; independent ownership has not been claimed.

## Career boundary

Do not update Career for ordinary project progress. Ali explicitly initiates a
Career review for capability, workload, strategy, or durable program changes.

## Detailed evidence

Use current source/tests, the closed M2-S02 plan and working record, the paused
M2-S03 plan, the current manual simulation plan, scenario records and coverage,
evaluation artifacts, specifications, Git history, and actual command outputs.

Do not copy this continuation into stable entrypoints or Career.
