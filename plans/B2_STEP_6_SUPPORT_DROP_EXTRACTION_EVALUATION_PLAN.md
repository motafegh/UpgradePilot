# B2 Step 6 — Python Support-Drop Extraction Evaluation Plan

**Status:** Bounded execution plan for parent Step 6  
**Parent:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Prerequisites:** Steps 1–5 behavior-validated  
**Trusted output boundary:** `CandidateUpstreamClaimResult` → `validate_support_drop_candidates(...)`  
**First live proof case:** S001 — Soup Sieve `2.6 → 2.8.4`

## Purpose

Determine the smallest credible way to turn admitted authoritative upstream text into the **untrusted candidate structure** already defined by Step 2.

The current responsibility is narrow:

```text
AuthoritativeUpstreamIntervalEvidence
→ inspect admitted upstream prose
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only one semantic meaning is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = X.Y
introduced_in_version = exact trusted crossed release
```

This step does not broaden back into the older four-category semantic vocabulary. It does not compare the target repository, reorder the CLI, make compatibility/safety claims, or choose a maintainer action.

## Why Step 6 is still needed

Step 5 established **what exact upstream text is authoritative**. It did not establish what that natural-language text means.

For S001, the exact tagged changelog contains a human-readable statement equivalent to:

```text
Drop support for Python 3.8.
```

The trusted Step 2 validator can verify a proposed category, direction, Python line, introduced release, exact quote, and source span. It deliberately does not discover those semantic fields itself.

Therefore Step 6 owns candidate extraction only.

## Existing evidence that constrains the method

Earlier B2 experiments already established several reusable findings:

- JSON Schema constrains representation, not semantic correctness;
- exact source quotation does not prove correct interpretation;
- small local models previously produced material false dropped-support claims;
- package/fixture-shaped regular expressions are not an accepted product semantic architecture;
- caller-supplied manual claims remain valid test oracles but do not perform the automated responsibility;
- a bounded LLM is a credible experiment direction only when deterministic validation and explicit abstention remain downstream.

Those historical experiments used a broader semantic responsibility than the current Step 6 slice. Their numeric scores are historical evidence, not automatic rejection of every current deployment.

## Method decision before model work

### Deterministic phrase or regex extraction

A deterministic phrase baseline may be used in evaluation, but it is **not selected production behavior**.

Reason:

```text
known phrase match
≠ general semantic extraction
```

Even this narrow support-drop meaning can appear as:

```text
Drop support for Python 3.8.
Python 3.8 is no longer supported.
Support for Python 3.8 has been removed.
Python 3.8 support ends in this release.
Require Python 3.9 or newer.
```

and must remain distinct from:

```text
Add support for Python 3.8.
Python 3.8 remains supported.
Python 3.8 support will be dropped in a future release.
Do not drop support for Python 3.8.
```

A growing phrase table would move fixture knowledge into production logic and would handle negation, tense, and equivalent wording poorly.

### Current Step 6 direction

The selected **evaluation direction** is therefore:

```text
bounded structured LLM candidate extraction
→ existing deterministic Step 2 grounding/validation
```

This is an experiment direction, not yet product model adoption.

## Step 6A — Freeze the narrow semantic corpus and oracle

Before scoring any model, create a small corpus dedicated only to the current claim contract.

Required classes:

1. direct dropped-support wording;
2. paraphrased dropped-support wording;
3. raised minimum-Python wording that semantically means an older line is no longer supported;
4. support-added control;
5. continued-support control;
6. negated drop control;
7. future/planned drop control;
8. ambiguous support wording;
9. no Python-support claim;
10. multiple dropped Python lines;
11. one valid claim plus unrelated fixes;
12. instruction-shaped/malicious text near a legitimate release statement;
13. exact historical S001 tagged-changelog excerpt.

The expected candidate result and expected deterministic Step 2 outcome must be frozen before model scoring.

Known S001 text is an oracle/calibration case, not the extraction algorithm.

## Step 6B — Reconfirm local inference environment

Reuse the existing LM Studio evaluation direction only after the current environment is observed.

Capture from Windows/LM Studio and WSL2:

- LM Studio CLI/server identity;
- server port and reachability from the active UpgradePilot environment;
- downloaded and loaded model inventory;
- current GPU memory state;
- exact candidate model identifier and load configuration;
- one `/v1/models` response from WSL2.

Do not record tokens or unrelated private prompts.

Do not download a model without explicit user approval.

## Step 6C — Smallest adapter smoke

Prefer **direct HTTP using the already-installed `requests` dependency** for the first smoke unless evidence shows a missing capability.

Why:

- UpgradePilot already depends on `requests`;
- LM Studio exposes an OpenAI-compatible JSON-Schema endpoint;
- the request/response boundary remains directly observable;
- adding OpenAI, Pydantic, or Instructor before proving need would widen runtime dependencies prematurely.

Instructor remains an optional experiment comparison only if it materially reduces schema/diagnostic code after the direct smoke works.

First-pass retries must remain disabled.

The smoke proves only:

```text
WSL2 → LM Studio transport
+ selected model identity
+ strict structured response shape
```

It does not prove semantic adoption.

## Candidate output shape

The model-facing representation must map mechanically into the existing Step 2 dataclasses rather than redefining the trusted contract.

Conceptually:

```text
CandidateUpstreamClaimResult
├── state
├── package
├── normalized_package
├── old_version
├── proposed_version
├── candidates[]
│   ├── category
│   ├── change_state
│   ├── python_line
│   ├── introduced_in_version
│   ├── source_kind
│   ├── source_release_version
│   ├── source_quote
│   ├── quote_start
│   └── quote_end
└── detail
```

The extraction adapter may propose these values. `validate_support_drop_candidates(...)` remains the trust boundary.

## Source input boundary

For the first Step 6 proof, use the exact `TaggedChangelogEvidence` already admitted by Step 5.

Do not perform arbitrary web/document search.

The model must receive enough deterministic context to identify version sections without granting it authority:

```text
package identity
old/proposed versions
trusted crossed-release versions
source kind
exact changelog text
```

The source text is untrusted data. Embedded instructions inside it do not override the extraction task or output contract.

## Step 6D — Scored semantic evaluation

For each candidate deployment and corpus case, record separately:

- transport success/failure;
- schema/JSON success/failure;
- candidate structure;
- Step 2 deterministic grounding result;
- semantic oracle result;
- false positive;
- false negative;
- wrong direction;
- wrong Python line;
- wrong introduced release;
- wrong or invented quote/span;
- latency;
- finish reason and token counts when available.

Use temperature `0` and no automatic retry in first-pass scoring.

Run repeated trials for decision-critical controls, especially:

- added vs dropped;
- negated drop;
- future drop;
- S001 positive claim.

## Adoption gate

A deployment/adapter may be proposed for the active product path only if:

1. every accepted candidate survives the existing deterministic source/span/interval validator;
2. no wrong-direction support claim survives on the frozen critical controls;
3. no negated or future drop is converted into a current support drop;
4. S001 produces the correct candidate identity and exact grounded span;
5. ambiguous/no-claim cases abstain rather than guess;
6. repeated critical runs do not produce materially inconsistent trusted outcomes;
7. latency/resource use is recorded and acceptable for one read-only dependency investigation;
8. the method materially improves on the previously rejected local deployments;
9. model/adapter/provider identity is explicit and reproducible enough for the project boundary.

A schema-valid response is not sufficient.

## Possible Step 6 outcomes

Step 6 must end in exactly one evidence-backed disposition:

```text
adopt_bounded_extractor
retain_experiment_only
reject_candidate_deployment
defer_semantic_automation
reconsider_extraction_method
```

Only `adopt_bounded_extractor` authorizes adding a normal-runtime extraction adapter. If that choice creates a durable model/provider/client dependency, record the appropriate ADR before product activation.

## Modification boundary

Before adoption, prefer experiment/support artifacts such as:

```text
experiments/
tools/
tests/ for deterministic harness contracts only
working-memory/
```

Do not modify merely to perform the evaluation:

```text
src/upgradepilot/cli.py
src/upgradepilot/target_python.py
src/upgradepilot/target_python_relevance.py
```

Do not weaken `src/upgradepilot/upstream_claim.py` to accommodate model mistakes.

## Educational focus

Step 6 introduces several distinct layers that must not collapse into “the AI understood it”:

```text
transport
→ can bytes reach the model server?

structured generation
→ did output follow the requested JSON shape?

semantic extraction
→ did the candidate represent the prose correctly?

grounding
→ does its exact quote/span exist in trusted source text?

trust admission
→ does deterministic Step 2 validation admit it?

product activation
→ is the extractor reliable enough to use in normal runtime?
```

Current learning depth should remain `introduced + implementation/evaluation exposure` until the user can explain these boundaries and interpret failure evidence independently.

## Validation cadence

Proceed in bounded increments:

```text
6A frozen corpus/oracle
→ review deterministic tests
→ 6B environment observation
→ 6C transport/schema smoke
→ 6D scored semantic evaluation
→ adoption disposition
```

Do not select a production model because one S001 prompt succeeds.

## Stop line

Stop Step 6 before:

- target Python acquisition/relevance comparison;
- CLI conditional orchestration;
- full S001 product execution;
- general release-note summarization;
- four-category decision semantics;
- cloud fallback;
- model download without approval;
- agent frameworks/tool calling/RAG;
- compatibility, safety, merge, or maintainer-action logic.

Step 7 begins only after the support-drop extraction path has an explicit validated disposition.
