# Synthesis Producer Reachability and Correctness — Working Memory

**Date:** 2026-09-11  
**Session status:** CONTINUED  
**Continued by:** [2026-09-11_synthesis-stable-semantic-acceptance.md](2026-09-11_synthesis-stable-semantic-acceptance.md)

**Lifecycle reconciliation (2026-09-11):** The conclusions and continuation below describe this dated checkpoint. Consult the successor and repository `MEMORY.md` for continuation; historical learning labels do not establish unrecorded learner ownership.

**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_synthesis-action-permission-matrix.md`](2026-09-11_synthesis-action-permission-matrix.md)

## Session anchor

The action-family semantics are now coherent enough for design use. This slice asks a different question:

> For every fact the synthesis matrix needs, what does the current normal application actually produce, what is safely derivable, what is genuinely missing, and what current correctness limitation prevents the fact from authorizing a maintainer action?

This remains Planning/Design evidence only. It does not change stable semantics, fix product defects, or implement synthesis.

## Minimum mental model

Keep these two responsibilities separate:

```text
SEMANTICS
What evidence should justify an action?

REACHABILITY
Does the normal product actually produce trustworthy evidence satisfying that permission?
```

A semantic permission can be correct while currently unreachable. That is preferable to weakening the permission until current code happens to satisfy it.

## Current application result boundary

`PublicPullRequestInvestigation` already preserves typed state for:

- exact pull-request identity and changed-file records;
- dependency change or typed dependency problem;
- exact-head workflow run/job evidence and CI dependency-coverage result;
- proposed/old package evidence;
- upstream repository / crossed-release / tag / changelog / interval evidence;
- grounded Python-support-drop claim or problem;
- Python pre-investigation applicability, selected exact target-Python read, target result/relevance, and post-investigation applicability;
- artifact-serviceability candidate/result;
- partial static target artifact-environment evidence;
- final artifact applicability result, which currently remains without exact target wheel-tag evidence in the normal path.

The CLI renders those typed results. It does not yet produce an overall synthesis object or maintainer action.

## Producer / derivation / gap map

| Synthesis-relevant fact | Current normal producer | Classification | Consequence |
|---|---|---|---|
| PR/base/head identity | `github.pull_request` → `PullRequestIdentity` | **available** | reusable directly, subject to source-specific correspondence limits below |
| dependency transition + source evidence | `dependency.analysis` | **available but source-strength dependent** | exact-file `uv.lock` / pyproject paths use exact base/head files; exact-requirements/constraints extraction consumes changed-file patch text |
| candidate proposition/applicability state | mechanism modules | **available** | consume typed states; do not reinterpret mechanism truth in synthesis |
| Python pre-acquisition unresolved state | `impact.python_support` | **available** | exact reason/location preserved in proposition state |
| selected Python investigation | `select_python_support_drop_investigation` | **available** | mechanism-local UpgradePilot-executable acquisition, not a maintainer check |
| Python investigation attempted in normal synchronous path | selection + non-null target result/relevance | **derivable** | no new generic `attempted` flag needed for the current path |
| Python final local stop after `established_applicable` / `established_not_applicable` | post-assessment final state | **derivable** | no generic stop flag needed merely to restate a final proposition |
| Python unresolved after attempted target read | post-assessment + typed target/relevance problem | **available** | uncertainty is preserved correctly |
| whether another justified UpgradePilot investigation exists after that unresolved attempt | none | **genuinely missing** | synthesis cannot infer continuation or stopping from `selector == None`; selector suppresses repeat once target evidence exists, not all future investigations |
| whether a useful outside responsibility exists after unresolved Python attempt | none | **genuinely missing** | do not fabricate `defer` or maintainer check |
| artifact old/proposed published wheel transition | package + artifact-serviceability module | **available** | exact package-side candidate evidence exists |
| partial target artifact environment | CI relation + `target.artifact_environment` | **available at static declaration strength** | runner/Python/install declaration may narrow context but cannot become exact wheel compatibility |
| exact target wheel compatibility | typed contract exists (`TargetWheelCompatibilityEvidence`) | **no normal producer** | focused tests can inject it, but normal product cannot satisfy artifact exact applicability |
| artifact-specific next investigation / selector | none | **genuinely missing responsibility** | this is not a synthesis-field gap; investigation capability/ownership is absent |
| candidate-discovery coverage adequate for broad favorable conclusion | none | **no admitted generic producer** | `merge after normal review` cannot use “all implemented candidates look fine” as positive coverage |
| generic repository-purpose/policy/provenance context | none | **no admitted generic producer** | S009 proves such context can matter; synthesis must not manufacture absence |
| concrete maintainer-performable targeted check | none in current normal mechanisms | **not currently produced** | Python selector is product-execution selection, not maintainer recommendation; targeted-check action is semantically defined but not generally reachable yet |
| grounded broader/adaptive maintainer investigation program | none | **not currently produced** | `investigate` semantics are coherent but normal producer reachability is absent |
| specific outside/future responsibility + reassessment trigger | none generically | **not currently produced** | `defer` must not be inferred from missing capability alone |
| decisive reasons / residual uncertainty / provenance | distributed typed results | **mostly derivable/projectable** | synthesis can project these; no generic planner state is required |
| overall action | none | **intentionally missing implementation** | admitted only after stable synthesis semantics are accepted |

## Source-strength correction: dependency identity is not uniformly trustworthy

The separate correctness investigation confirmed a PR patch/revision correspondence defect, and the current source still has the same shape.

### Patch-backed requirement / constraint path

`GitHubPullRequestClient.get_pull_request(...)` freezes head A. `get_changed_files(...)` later acquires `/pulls/{n}/files` by PR number and retains filename/status/count/patch but no head/revision correspondence. `dependency.analysis` passes exact-requirements patch text directly to the requirements extractor and then assigns the frozen identity head to the resulting source context.

Therefore:

```text
requirements/constraints patch accepted
+
initial PR head = A
!=
patch proven to belong to A
```

Until corrected or enforceably restricted, a patch-derived dependency transition MUST NOT authorize a maintainer action that depends on exact proposal/revision correspondence.

### Exact-file structured paths

The `uv.lock` and admitted pyproject optional-extra paths use exact base/head repository-file acquisition against the frozen identity before extraction.

The confirmed patch mismatch does not by itself invalidate those exact-file paths.

This distinction allows a narrow trust restriction instead of disabling every dependency source.

## CI correctness restrictions that survive on current main

Three confirmed/source-reproduced issues are material to synthesis permission.

### 1. Static command-recognition false positives

`bounded_shell_segments(...)` splits text on separators without shell comment/quote semantics. `observe_direct_installation_declaration(...)` can therefore promote install-looking text inside a comment or quoted separator payload into a positive requirements-install declaration.

The supporting diagnostic reproduced positive CI/Target evidence for cases such as:

```text
pip install wheel # -r requirements-dev.txt
```

and quoted separator data containing an apparent `pip install -r ...` segment.

Consequence:

> Current positive direct-requirements consumption/Target formation evidence cannot by itself authorize a favorable or other stronger action until the command-recognition owner is corrected or an enforceable safe-input restriction exists.

### 2. Workflow run/job attempt mixing

`WorkflowRun` preserves `run_attempt`, but `get_workflow_jobs(...)` requests `filter=latest`; `WorkflowJob` does not preserve attempt identity. Current validation checks run ID and head SHA only.

A rerun can therefore combine a captured attempt-N run with jobs from a later attempt while still passing identity checks.

Consequence:

> Current CI success/failure classification is not sufficiently attempt-coherent to serve as decisive synthesis authority without correction or a producer-grounded restriction.

### 3. Patch/revision mismatch

The dependency-source limitation above can contaminate every downstream branch when the canonical dependency transition came from mutable patch text.

Consequence:

> Synthesis needs a trust gate on the dependency source/evidence class before any action permission is considered.

## What these restrictions do NOT mean

Do not infer:

- every CI result is wrong;
- every public PR experiences a race;
- exact-file dependency extraction is invalid;
- current evidence should be discarded rather than preserved at its actual proof strength;
- fixes are authorized by this synthesis slice.

The correct synthesis stance is:

```text
preserve affected evidence
+
record limitation
+
do not let that evidence satisfy a permission requiring stronger trust
```

The originating correctness plan retains repair ownership.

## Action reachability after producer reconciliation

### `merge after normal review`

**Not generally reachable in V1 from current producers.**

Reason:

- no generic producer establishes bounded candidate-discovery coverage;
- no generic producer establishes material repository-purpose/context coverage;
- current CI authority has confirmed attempt/coherence and command-recognition limits;
- absence of a known concern cannot substitute for positive favorable coverage.

The action remains valid Charter semantics, but should remain unavailable whenever its positive horizon cannot be producer-grounded.

### `run targeted checks`

**Semantic shape exists; general normal producer is absent.**

The existing Python investigation selection is an UpgradePilot-executable pre-acquisition read. It must not be projected as a maintainer check merely because it is a concrete check.

A future maintainer-check recommendation needs a producer-grounded decision-critical proposition + concrete maintainer-performable discriminating check after the product-execution boundary has been resolved.

### `investigate`

**Semantic shape exists; broader inquiry-program producer is absent.**

Current mechanism results can expose unresolved state, but unresolved state alone is insufficient. No normal result currently says that a grounded broader/adaptive maintainer inquiry exists with a concrete scope/stopping logic.

### `block`

**Potentially producer-grounded for narrow trusted cases, pending stable acceptance.**

The strongest current candidate route is:

```text
trusted exact dependency transition
+
authoritative validated upstream Python support drop
+
exact target Python declaration
+
post-investigation applicability = established_applicable
```

That state establishes a proposal-relative declared-support conflict without depending on CI success. It is therefore the clearest current source shape that could satisfy the block permission after stable synthesis semantics accept that mapping.

Restrictions:

- do not use patch-derived dependency identity until its revision correspondence is trustworthy;
- do not turn `established_applicable` into a universal severity rule for other mechanisms;
- artifact wheel-loss candidate alone cannot block while exact target applicability remains unresolved.

### `defer`

**Not generally reachable from current producers.**

A known missing capability is not enough. Current normal results do not generically produce both a specific useful outside/future responsibility and a concrete reassessment trigger.

### `abstain`

**Derivable as the honest fallback once synthesis exists.**

Typed problems, unsupported/unresolved states, missing permission prerequisites, and claim limits already provide enough material to explain why no stronger action is justified.

Abstain does not require inventing a new investigation capability; it requires preserving why stronger permissions failed.

## Operational reachability: investigation may fail before synthesis can run

The normal application calls workflow-run/job acquisition before later package/upstream branches. Provider acquisition/response exceptions propagate out of `investigate_public_pull_request(...)`; the CLI catches them and exits instead of returning a `PublicPullRequestInvestigation`.

Therefore some operational acquisition failures currently mean:

```text
no complete investigation result returned
→ synthesis layer has no input
→ Charter abstention is not yet reachable through the normal result path
```

This is a source-level reachability fact, not yet a correctness verdict about how the application should degrade. The separate correctness investigation still owns that classification/repair question.

## Smallest missing handoff state

The producer trace argues against a universal planner/stop enum.

The smallest genuine synthesis-relevant handoff gap is specifically for **material non-final post-investigation propositions**:

```text
current proposition state/reason
+
what investigation was attempted and what result/problem was obtained
+
whether another justified UpgradePilot-executable investigation remains, if established
+
if none remains, whether a specific useful maintainer/outside responsibility is known, if established
```

Final proposition states do not need this extra structure merely to say investigation stopped. Artifact exact-compatibility lacks an investigation owner entirely and should be solved at that responsibility rather than patched by synthesis metadata.

Do not introduce a capability registry, universal action planner, generic stop-reason enum, or graph engine from this gap alone.

## Design conclusion of this slice

The current synthesis problem is now narrower than it looked:

```text
MOST TECHNICAL TRUTH
already exists in typed results

SMALL NON-FINAL HANDOFF
missing for unresolved post-attempt continuation/stopping

ARTIFACT EXACT COMPATIBILITY
missing upstream investigation capability, not downstream synthesis interpretation

FAVORABLE COVERAGE / GENERIC CONTEXT
not currently produced, therefore favorable permission stays unavailable

CORRECTNESS-LIMITED EVIDENCE
must be prevented from satisfying permissions above its proof strength
```

This is coherent enough to move to the stable synthesis-semantic owner/acceptance question without designing a generic orchestration layer.

## Historical activity labels (not canonical learning-cycle completion)

```text
Slice: synthesis producer reachability + correctness restrictions

A — DONE:
    separated semantic permission from runtime producer reachability.

B — DONE:
    traced PublicPullRequestInvestigation, Python support-drop flow, artifact flow, CI coverage, Target artifact environment, CLI, focused application tests, and accepted Product Decision Model boundaries.

C — DONE:
    reconciled confirmed correctness findings against current main source instead of importing stale findings blindly.

D — DONE:
    classified needed synthesis facts as available, derivable, genuinely missing, absent producer, or operationally unreachable.

E — DESIGN CONCLUSION:
    no generic planner state is justified; the real missing synthesis handoff is narrow, while artifact/favorable-coverage gaps belong to upstream producer responsibilities.

F — NEXT:
    choose the correct stable specification owner, express the accepted synthesis contract/permissions at that owner, pressure the whole contract once, then hand off to Build only if the acceptance gate passes.
```

## Immediate continuation

```text
producer/reachability map complete
→ choose stable synthesis semantic owner
→ write the smallest stable contract
→ whole-matrix acceptance pressure
→ update live state
→ Build/Implement only after acceptance
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
