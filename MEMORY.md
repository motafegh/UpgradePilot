# UpgradePilot Current Memory

**Last updated:** 2026-08-10  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Completed bounded responsibility:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Completed Step 7 integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected next B2 responsibility:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md), with implementation still intentionally paused pending the post-reconciliation handoff decision.
- **Single reconciliation record:** [`working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md).
- **Conversation A:** CLOSED 2026-08-08 — dependency-update impact/problem model.
- **Conversation B:** CLOSED 2026-08-09 — target applicability/evidence/model-authority model.
- **Conversation C:** **CLOSED 2026-08-10** after two complementary pressure tests and explicit closure review — best next investigation/targeted-check selection.
- **Conversation D:** **not yet opened**.
- **Immediate session action:** create a cumulative learning note in `learning/` covering the complete decision-model journey through Conversation-C closure, including the concepts, cases, mental models, failure modes, authority boundaries, deterministic/semantic reasoning, applicability logic, investigation-selection method, and what must be understood/mastered/remembered.
- **Post-learning continuation:** perform the post-C implementation-handoff decision. Current default is to prefer a bounded implementation/evaluation slice of accepted A–C semantics before broad Conversation-D theory unless a concrete D dependency makes D necessary first.

The learning note is educational only and must not become a second live-state owner.

## Latest material verification

The accepted implementation baseline remains:

- post-reconciliation active product regression before Step 7B: **323 tests passed**;
- completed Step 6 experiment regression: **27 tests passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 7B focused/full active product regressions: **passed in WSL**;
- Step 7C focused/full regressions and corrected real S001 local-model proof: **passed**;
- real Step 7C Gemma inference grounded **Python 3.8 support dropped in Soup Sieve 2.8**, exact quote offsets `729:770`;
- Step 7D focused upstream-composition regression/full active regression: **reported green in WSL**;
- Step 7E focused application/CLI/topology tests/full regression: **reported green in WSL**;
- Step 7F controlled end-to-end test/full active regression: **reported green in WSL**;
- final normal-path S001 CLI proof: **passed**;
- exact target Pydantic head: `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`;
- exact target declaration: **`requires-python >=3.10`**;
- final bounded S001 relevance: **`outside_declared_python_range`**;
- CI dependency exercise remained honestly **unresolved / dependency_exercise_not_proven**;
- observed wall-clock duration for the complete final normal CLI proof: approximately **36.546 seconds**.

The accepted reconciliation baseline now additionally includes:

### Conversation A

```text
upstream change
+ target-relevant exposure/path
+ activation condition(s)
+ possible target-relevant consequence
= impact candidate
```

Key boundaries include:

```text
upstream change != target impact
target relevance != target ownership
one transition != one impact candidate
materiality != severity/likelihood/interestingness/harm
```

### Conversation B

Applicability is proposition-based per mechanism-specific candidate and exact target/revision/context.

Accepted conceptual knowledge states:

```text
established applicable
established not applicable
unresolved
conflicted
```

Positive applicability needs one sufficiently established complete viable path. Non-applicability requires elimination of every viable path. Missing evidence remains unresolved unless an adequate closed proposition-local evidence boundary supports genuine refutation.

Open-world reasoning is the safe default. Completeness is itself an evidence claim. Source identity/authority precede semantic interpretation. Prefer deterministic decision procedures where reliable and bounded grounded semantic reasoning where meaning genuinely requires it. LLM output cannot manufacture source authority, completeness, absence, applicability authority, or final maintainer action.

The semantic-heavy Kedro/Pluggy pressure test preserved:

```text
uses dependency
!= participates in affected mechanism
!= relies on specific changed property
```

### Conversation C

Conversation C now has an accepted bounded method for investigation selection:

```text
material unresolved proposition
+
uncertainty location/reason
↓
discriminating target(s)
↓
candidate investigations
↓
hard admissibility + context-validity boundary
↓
remove clearly dominated options
↓
qualitative comparison
    discrimination
    authority/scope/coverage
    pruning/shared-gate leverage
    cost/latency/invasiveness
    reproducibility
    complementarity/corroboration
↓
choose next investigation / small conditional bundle
OR justify no-further-investigation
↓
observation
↓
post-execution evidence validation
↓
return to proposition evaluation
OR refine/formulate candidate if a different mechanism is exposed
↓
repeat only while material uncertainty and a justified useful investigation remain
```

Accepted C principles include:

- `unresolved` alone is insufficient investigation input; uncertainty location/reason matters;
- identify the discriminating target rather than investigating the broad topic;
- relevant evidence is not automatically discriminating evidence;
- information gain is not automatically decision-relevant information gain;
- sufficient discrimination can mean resolution or material uncertainty reduction/pruning;
- hard admissibility precedes preference and hard failures are non-compensatory;
- feasibility/recoverability and theoretical discrimination are separate;
- use qualitative proposition-relative comparison rather than fake numeric VoI scoring;
- clearly dominated investigations may be removed using Pareto-style reasoning, but genuine trade-offs remain qualitative;
- candidate logic and shared-gate/pruning leverage can determine ordering;
- conditional/adaptive investigation strategies with bounded lookahead are preferred to static ranked checklists or complete investigation trees;
- complementarity/corroboration can add value even when broad semantics overlap;
- no universal cheap/static/semantic/dynamic ordering exists;
- a dynamic/interventional check may be the first substantive investigation when it directly targets the decisive high-leverage uncertainty after minimal admissibility pre-flight;
- successful execution does not automatically create admissible evidence;
- observation meaning is bounded by identity/context/temporal/contrast/reconstruction fidelity;
- proposal-level effect and causal mechanism attribution are different questions;
- proxy evidence may narrow uncertainty but cannot inherit exact-context authority;
- scope substitution is prohibited;
- historical reconstruction must earn enough fidelity; more elaborate reconstruction is not automatically better evidence;
- investigation results can return to B proposition evaluation or reveal candidate refinement/new candidate generation;
- `no further justified investigation` is a valid C outcome and preserves unresolved/conflicted state;
- C investigation stopping is distinct from Conversation-D overall evidence/output sufficiency.

### Conversation-C pressure tests

**Pressure Test 1 — C01 `grpcio-tools` artifact/code generation:** PASS with refinements.

It demonstrated that controlled old/new regeneration can rationally outrank cheaper static investigation when it directly targets a decisive generated-artifact difference and has strong pruning leverage. It exposed contrast validity, post-execution result validation, proposal-level effect versus mechanism attribution, and candidate-refinement feedback.

**Pressure Test 2 — C203 Buildtest/OpenSSL historical environment:** PASS with refinements.

It demonstrated that ideal historical evidence may be unrecoverable; proxy/context evidence can narrow without resolving; reconstruction must earn historical/context fidelity; escalation may correctly stop unresolved; and `no further justified investigation` is a first-class C outcome.

### Conversation-C closure

Closure review passed all recorded C criteria across direct deterministic, semantic-heavy/plugin, environment/historical, multi-hop/transitive, and artifact/code-generation topologies. No foundational contradiction remains that requires C to stay open.

Accepted new C decisions are recorded as **D-053 through D-070** in the reconciliation record. D-070 requires a post-C implementation-handoff check before automatically opening Conversation D.

## Behavior-valid Target-Python relevance path

```text
public repository + PR number
→ exact PR identity and complete changed-file evidence
→ trusted DependencyVersionChange
├── independent bounded CI dependency-exercise branch
└── upstream/target relevance branch
    → exact PyPI proposed release via PyPIReleaseClient
    → trusted upstream GitHub repository from project-link candidate + exact-file provenance agreement
    → package-wide PyPI release index via PyPIReleaseIndexClient
    → complete old-exclusive/proposed-inclusive crossed-release interval
    → canonical exact proposed-version Git tag
    → exact-commit changelog discovery and acquisition
    → authoritative tagged-changelog interval evidence
    → complete deterministic crossed-release Markdown source window
    → bounded local Gemma candidate extraction
    → deterministic exact-source reconstruction
    → validate_support_drop_candidates(...)
    → GroundedPythonSupportDropClaim?
        ├── no  → target Python remains inactive / explicit unresolved state
        └── yes → exact-head target pyproject.toml
                  → [project].requires-python
                  → deterministic target-Python relevance
```

The model does not own source authority, package/version identity, release ordering, exact source text/offsets, target relevance, compatibility, safety, or maintainer action.

## Completed bounded conclusion for S001

```text
Soup Sieve 2.6 -> 2.8.4
→ crossed release 2.8 explicitly drops Python 3.8 support
→ deterministic validation grounds that upstream claim
→ Pydantic exact PR head declares requires-python >=3.10
→ no stable Python 3.8.Z version is admitted by the target declaration
→ outside_declared_python_range
```

This means only that the grounded upstream Python 3.8 support-drop concern does not intersect the target's declared Python installation range under the accepted method. It does not mean the update is safe, universally compatible, sufficiently tested, or recommended for merge.

## Exact continuation

### 1. Cumulative learning consolidation

Create a new learning artifact under `learning/` pinned to the Conversation-C closure state.

It should teach and consolidate, rather than merely summarize:

- why the decision-model reconciliation was required;
- the A impact-candidate model;
- B applicability/proposition/evidence/open-vs-closed-world model;
- deterministic-versus-semantic/LLM authority boundaries;
- C uncertainty-location/discriminating-target/investigation-selection model;
- dominance/Pareto, pruning/shared-gate leverage, complementarity, adaptive sequencing, escalation, bounded lookahead;
- static/dynamic and observational/interventional evidence;
- differential testing and contrast validity;
- investigation validity/context/reconstruction fidelity;
- proxy evidence and scope substitution;
- proposal-level effect versus causal attribution;
- investigation-result candidate feedback;
- C no-further-investigation versus D sufficiency;
- S001, Kedro/Pluggy, pip-audit/CacheControl/urllib3, C01 grpcio-tools codegen, and C203 Buildtest/OpenSSL examples;
- rejected shortcuts and common reasoning failures;
- what must be memorized, what must be operationally understood, and what remains deferred;
- recall, transfer, diagnosis, and explanation prompts suitable for later review.

The learning artifact must not control project stage or continuation.

### 2. Post-C implementation handoff

After the learning note is complete, decide whether to:

```text
A. select a bounded implementation/evaluation slice that exercises accepted A–C semantics
```

or, only if concretely required:

```text
B. open Conversation D first
```

Current default: **A before broad D theory**, because further C abstraction is now lower-value than real implementation/evaluation feedback.

Do not begin implementation automatically without that selection step.

## Material blockers and caveats

No blocker remains for the completed Target-Python relevance responsibility.

The general decision/recommendation implementation remains intentionally paused only until the post-C handoff decision selects the next bounded responsibility.

The reusable LM Studio loopback/proxy caveat remains in `ENVIRONMENT.md`; stable local-inference and untrusted-source controls remain in `SECURITY.md`. Provider/model/deployment-contract changes remain reassessment events rather than silent substitutions.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging and substantial guided product-model reasoning; no formal mastery assessment**.

Recent learning exposure includes:

- exact PR/base/head evidence and representation-specific dependency extraction;
- domain evidence types versus application orchestration;
- independent CI and upstream investigation branches;
- PyPI exact-release identity versus package-wide release-index identity;
- publisher provenance and exact immutable source binding;
- bounded LLM semantic extraction versus deterministic trust admission;
- exact source reconstruction and quote offsets;
- target Python specifier/line relevance without compatibility overclaiming;
- scenario-specific proof versus generic product behavior;
- live end-to-end proof discovering interface/integration assumptions;
- Conversation-A impact/exposure/activation/consequence modeling;
- Conversation-B proposition logic, applicability states, necessary/sufficient and alternative paths, open/closed-world reasoning, negative evidence, universe of discourse, conflict normalization, deterministic/semantic boundaries, and model/maintainer authority;
- Conversation-C uncertainty-location/discriminating-target reasoning, resolution versus reduction, admissibility versus preference, qualitative dominance/Pareto comparison, logical pruning/shared-gate leverage, complementarity/corroboration, adaptive conditional sequencing, earned escalation, non-compensatory hard constraints, bounded lookahead, differential/interventional evidence, context/contrast/reconstruction fidelity, proxy evidence/scope substitution, and no-further-investigation semantics;
- two materially different Conversation-C pressure tests and explicit closure reasoning.

Record stronger ownership only after demonstrated explanation, modification, testing, diagnosis, or transfer to changed cases.
