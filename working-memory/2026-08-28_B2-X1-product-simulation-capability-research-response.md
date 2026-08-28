# B2/X1 Product-Simulation Capability Research Response

**Date:** 2026-08-28  
**Status:** MAIN-FACING RESEARCH RESPONSE — delegated capability research complete for current evidence boundary  
**Research branch:** `product-simulation/2026-08-28-main-support-lab`  
**Evaluated main revision:** `14ba589de18aa72b0f9098d5154cc722c494c256`  
**Main-side request:** `2026-08-28_B2-X1-product-simulation-capability-research-handoff.md`  
**Execution plan:** `../plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`  
**Supporting records:** R0 evidence-use map; R1 capability inventory; R2 planner-value discrimination; R3 targeted case discovery

## A. Executive finding

### Bottom line

The research found **several real missing or incomplete investigation capabilities**, but it did **not** find evidence strong enough to promote a second capability into **LLM-owned planner selection**.

The most serious candidate was exact-head resolver/currentness/satisfiability evidence. That capability is independently useful and already has a clear proof boundary from `AUDIT-004`. However, after comparing it against the strongest deterministic policy and screening fresh public cases, the observed selection policy still looks small enough for deterministic ownership:

```text
if stronger/cheaper trusted evidence already settles the proposition
→ prune resolver work

else if resolver/currentness is the material unresolved proof rung
    and exact resolver context is safely bound
→ run one bounded deterministic resolver/currentness check

else
→ stop / defer / unresolved according to the owned question
```

The research did **not** find a credible supported public case where:

```text
resolver/currentness action
+
another independently admitted read-only action
+
state/history/budget-dependent information-value trade-off
→ non-trivial choice that a small deterministic policy handles poorly
```

Therefore the main recommendation is:

> **Do not expand the X1 action catalog merely to create multi-action agentic planning. Keep the first evidence-refined planner seam as a bounded experimental/control seam if its learning/evaluation value remains useful, but do not claim general adaptive-planner product value yet. Build/admit real deterministic evidence capabilities when their product responsibility is independently justified; reopen richer planner selection when two or more such capabilities naturally coexist and real cases demonstrate non-trivial selection/sequencing value.**

This is not a recommendation to keep UpgradePilot permanently minimal. It is a recommendation to let capability growth **earn** planner complexity from product evidence.

### Research disposition

```text
strong new planner-visible capability found
→ NO

real product capability opportunities found
→ YES

meaningful richer planner responsibility proven now
→ NO

fresh holdout candidate safely reserved
→ NO

v3 should be frozen now
→ NO recommendation to freeze from this research
```

A valid main-side outcome is therefore handoff path **C**, or a narrow form of path **B** if main chooses to retain the first seam for learning/pilot evidence while explicitly acknowledging that adaptive action-selection value remains unproven.

---

## B. Candidate capability table

| Candidate capability / responsibility | Real evidence | Planning uncertainty | Bounded input/output boundary | Current/missing owner | Planner-value result | Authority / proof limit | Recommended disposition |
|---|---|---|---|---|---|---|---|
| **Exact target Python declaration acquisition (A1)** | S001 + current product + E3/E4 | exact target Python range missing before support-drop relevance can be resolved | pre-bound repo/revision/`pyproject.toml` → typed declaration/problem | current deterministic owner exists | model can reason about it, but deterministic selector already owns the small policy better | declaration/range relevance only; not compatibility | **Retain as control/first action; do not use as planner-value proof** |
| **Exact-head resolver/currentness/satisfiability evidence** | AUDIT-004; S007 pruning; `fastapi-new#38`; Dependabot uv failure reports | whether exact declared graph/lock is current/satisfiable under admitted resolver context | pre-bound repo/revision/project/lock/context → established/refuted/unresolved + typed acquisition problem | evidence owner missing/deferred; proof semantics known | real evidence value, but LLM selection not shown superior to small state policy | resolver satisfiability/currentness only; not install/runtime/compatibility | **Promote as deterministic product capability/design study when route selects it; do NOT promote as planner action yet** |
| **Mediated CI/environment-consumption interpretation** | S005; S002; S011 | whether changed environment is actually consumed through tox/nox/reusable/task mediation | exact statically referenced bounded source → supported/not-established/unresolved relation | generic mediation interpreter intentionally unsupported | current hard problem is deterministic interpretation, not planner choice | static relation only; not execution/runtime proof | **Keep as deterministic evidence-capability gap; not planner action** |
| **Target artifact/wheel-environment evidence acquisition** | S008; S011; target-environment design handoff; current `target/artifact_environment.py` | which exact target environment facts establish applicability of artifact transition | exact workflow/job → partial provenance-carrying target facts → exact compatibility only when earned | bounded deterministic first owner already exists | no evidence that model source selection is needed at current support depth | target artifact/environment proposition only; not source-build/runtime success | **Continue deterministic capability evolution when selected; not planner action** |
| **Targeted behavioral/differential reproduction** | S006 | whether mapped upstream behavior changes exact target behavior | pre-bound target symbol/input/versions → old/new observation/problem | no safe general executor admitted | potentially high planner value only after safe execution capability exists | one targeted observation; executes target/dependency code | **DEFER as known outside capability** |
| **Persisted-artifact provenance/history acquisition** | S012 | whether reused artifact was produced under old dependency environment | known artifact/run identity → producer/consumer provenance or unavailable | no general public provenance owner | selection value unproven; accessible recurrence weak | absence of repository history != no artifact | **DEFER; reconsider narrower public provenance capability if real cases recur** |
| **Repository-purpose/reproduction-context interpretation** | S009 | whether exact versions are part of a declared reproducibility/publication contract | bounded source evidence → grounded context proposition | semantic/context owner missing | useful context for planner state, but `read purpose` is not a credible action | context != technical compatibility | **Separate context/semantic responsibility; reject generic planner action** |
| **Upstream multi-mechanism discovery** | S010 | which independent mechanisms exist across one dependency transition | bounded upstream evidence → grounded mechanism candidates | current support-drop extractor is mechanism-specific | can create richer planner state, but this is semantic discovery rather than action selection | candidate discovery != target applicability/decision | **Separate model/semantic-discovery responsibility; not planner action** |

### Important classification result

The research repeatedly reinforced:

```text
real missing capability
!= planner-visible capability

useful LLM reasoning
!= LLM should own execution policy

richer semantic discovery
!= richer investigation planning

read-only operation
!= automatically useful model tool
```

---

## C. Meaningful planner-state examples

No new product schema or v3 oracle is proposed. These are research sketches showing what would have to become real before richer planner ownership is justified.

### C1. Current deterministic-first resolver shape

Bounded question:

> Does the exact proposed dependency set remain satisfiable/current under the admitted target resolver context, and is a resolver observation still needed?

Representative trusted state:

```text
propositions:
- package_family_constraint_coherence
    state = unresolved
    coverage = insufficient

- exact_static_dependency_metadata_available
    state = established

- resolver_context_bound
    state = established

attempts:
- none

budget:
- 1
```

Possible capabilities:

```text
A = inspect already-admitted authoritative static package metadata
B = run exact bounded resolver/currentness check
```

If A is known cheaper/authoritative and can settle the same necessary proposition, a deterministic policy can choose A first. S007 then shows B becoming stale/redundant after A refutes coherence.

This is good orchestration behavior, but not yet evidence that an LLM policy is needed.

### C2. Negative resolver-selection case — `fastapi/fastapi-new#38`

Bounded question:

> Is an additional resolver/currentness investigation needed to establish that the exact pytest update is represented in the target test environment?

Trusted/manual design evidence:

```text
PR changes only pytest 9.0.0 → 9.0.2 in uv.lock
pytest belongs to exact tests dependency group
exact workflow runs uv sync --locked --no-dev --group tests
exact-head downstream required checks succeed
```

Planner distinction:

```text
shallow heuristic:
uv.lock changed
→ choose resolver

better reasoning:
stronger exact-head environment/CI evidence already addresses the practical proof rung
→ no extra resolver action merely for redundancy
```

This is a useful test of **information-value stopping**, but a small deterministic policy can still express it once the evidence owners exist.

### C3. What a genuinely planner-worthy future state would need

A future case would be materially stronger if it had something like:

```text
planning question:
Which bounded investigation most efficiently resolves whether this update is technically applicable to the target?

propositions:
- declared_constraint_satisfiability = unresolved
- target_environment_scope = unresolved
- artifact_availability_for_candidate_environment = unresolved
- static_upstream_constraint_conflict = unresolved

allowed capabilities:
A = acquire exact authoritative package-family metadata
B = acquire exact target environment witness
C = run exact bounded resolver/currentness check

attempt history:
A previously returned incomplete evidence

budget:
2
```

and real cases demonstrated that:

```text
state variant 1 → A first
state variant 2 → B first
state variant 3 → C first
state variant 4 → STOP/DEFER
```

with no small stable deterministic ordering handling the supported state space cleanly.

The current corpus/search did **not** establish this shape.

---

## D. Fresh-case and exposure inventory

### D1. Historical/design research corpus

R0 established that all S001–S012 are materially historical/design-exposed. They remain valuable capability evidence but should not be called untouched v3 holdouts.

Especially useful non-E1–E5-tuned historical cases:

- **S002** — CI/source relationship and targeted-check confidence;
- **S003** — install/resolution failure attribution contrast, but non-Python ecosystem;
- **S009** — repository-purpose/reproduction contract;
- **S010** — multi-mechanism discovery breadth.

### D2. New R3 design-research-used cases

#### `fastapi/fastapi-new#38`

```text
head: 0ff6ff640293ee7543d4629f63848b08e9634756
pytest 9.0.0 → 9.0.2
package manager: uv
changed: uv.lock only
```

Used deeply enough to establish the negative resolver-selection pattern. It is **not** a holdout.

#### `evoila/meho#1768`

```text
head: 4fa217ab7aae36a37c7cc906573f323a33d4512d
cryptography 48.0.0 → 49.0.0
package manager: uv
changed:
- backend/pyproject.toml
- backend/uv.lock
```

Used to distinguish successful lock/resolution state from separate artifact/API mechanism questions. It is **not** a holdout.

### D3. Screened/rejected new cases

- `langchain-ai/langchain#39187` — grouped multi-dependency/multi-workspace change; too many variables for current supported question.
- `rendercv/rendercv#745` — GitHub Actions ecosystem, not Python dependency.
- `rendercv/rendercv#739` — pip/manifest-only topology; no resolver-currentness pressure for this question.
- `slettmayer/oebb-mcp-server#25` — lock-only Ruff update and locked CI pattern; corroborative but not materially different from the negative resolver-selection case.

### D4. Public resolver design context that is not a clean PR holdout

Dependabot-core reports including #12087, #12788, #13891, #14119, and #15842 show real uv resolver/currentness/updater failure modes such as:

- incompatible attempted versions;
- manifest/lock update mismatch;
- local filesystem package resolution failure;
- dependency-name normalization/case mismatch;
- updater invocation bugs.

These are useful evidence for failure taxonomy and resolver capability value.

They are poor v3 protected candidates because the oracle/failure is already explicitly published, and several failures prevent Dependabot from creating a normal PR at all.

### D5. Holdout result

```text
reserved_holdout_candidate count = 0
```

This is intentional.

No low-exposure case matched the eventual planner-value question strongly enough to reserve without either consuming it for design or forcing an irrelevant holdout.

Main should select/freeze future v3 holdouts only after deciding the honest candidate claim. A new targeted search can then preserve candidates before deep analysis.

---

## E. Recommendation back to main

### E1. Do not add a second planner action now

The delegated research did not establish a second capability whose **selection policy** belongs to the LLM.

Adding resolver/currentness merely to obtain a multi-action catalog would violate the handoff's central requirement because the current evidence supports the capability more strongly than it supports model-owned selection.

### E2. Preserve the first seam as a control/pilot, not as proof of general planner value

The evidence-first E1–E5 sequence established real engineering value in:

- typed planner state;
- bounded natural-language reasoning;
- closed capability binding;
- structured output;
- deterministic admission;
- explicit stop/defer/unresolved semantics.

Those are useful and reusable.

But S001/A1 remains a case where deterministic sequencing already performs the next-step selection well.

Therefore the honest current claim is still narrow:

```text
LLM can reason over bounded typed evidence state
and bind to an admitted capability / no-tool disposition

but

material product advantage over strong deterministic sequencing
has not yet been demonstrated
```

### E3. Let deterministic capability growth continue where independently justified

Several product capabilities deserve future work independently of X1:

1. resolver/currentness/satisfiability evidence when selected by product route;
2. supported mediated environment/CI-consumption interpretation families when recurrence justifies them;
3. richer target-environment evidence acquisition;
4. potentially broader semantic mechanism discovery;
5. eventually safe targeted behavioral checks if a proper execution boundary is admitted.

These should be designed at their correct owners, not built as planner tools first.

### E4. Reopen richer planner evaluation when capability composition becomes real

A strong reassessment trigger is:

```text
at least two independently admitted bounded capabilities
+
real cases where both are plausible
+
relative information value/order changes with trusted state/history/budget
+
small deterministic sequencing becomes materially brittle/combinatorial
```

At that point the existing X1 learning—closed catalog, structured output, deterministic admission, no-tool states, stale-plan and retry boundaries—becomes directly reusable for a genuinely richer planner.

### E5. Fresh v3 recommendation

Do **not** freeze a richer multi-action v3 from the current research because the action-space claim is not yet earned and no holdout was preserved.

If main instead wants a final quality decision on the **narrow first-seam pilot**, it may choose to design a fresh v3 for that narrow claim using newly discovered protected material. But product simulation does not recommend investing in a general-adaptive-planner v3 before a real additional planner responsibility exists.

### E6. Suggested main-side decision framing

The evidence supports a decision among:

```text
RETAIN AS LIMITED PILOT
→ keep X1 first-seam machinery/learning as an experimental bounded planner interface
→ make no general adaptive-planner claim
→ revisit after real capability composition emerges

DEFER RICHER X1
→ preserve the research and return to independently justified deterministic product capability work
→ reactivate richer planning when trigger conditions appear
```

The research does **not** support:

```text
ADOPT GENERAL ADAPTIVE PLANNER
or
ADD SECOND ACTION FOR EVALUATION AESTHETICS
```

Main remains the owner of the actual X1 disposition and route continuation.

---

## F. Methods, barriers, and reusable engineering findings

### F1. Strongest-baseline discipline materially changed the candidate list

R1 initially surfaced resolver, mediated CI consumption, and target artifact environment as plausible candidates.

R2 demoted two after reconstructing their strongest deterministic owners:

- mediated CI/config interpretation is presently an evidence-semantics problem;
- target-environment evidence already has a bounded deterministic acquisition design.

Without this step, the research could easily have wrapped real deterministic responsibilities in unnecessary LLM tools.

### F2. Search contamination discipline prevented fake holdouts

Cases were classified by actual exposure rather than by whether they appeared in E1–E5.

This prevented the incorrect inference:

```text
not used in latest model tuning
→ fresh protected evidence
```

### F3. GitHub secondary rate limiting was an acquisition barrier

A global GitHub search attempt hit a secondary rate limit.

It was handled by:

- stopping repeated global-search calls;
- continuing via public web discovery and direct bounded GitHub reads;
- preserving the failure as method evidence rather than interpreting it as candidate evidence.

### F4. PR-creation boundary matters

Several strong resolver failures occur inside Dependabot update generation and therefore produce **no public PR**.

This means resolver technology can be highly important while still lying partly outside UpgradePilot's current public-PR investigation horizon.

That boundary should be preserved when judging product value.

### F5. Capability composition is the likely future source of real planner value

The research did not show that one complicated tool creates useful agency.

The stronger hypothesis is:

```text
several independently justified deterministic capabilities
+ typed epistemic state
+ changing information value / prerequisites / attempts / budget
→ model planning may earn its place at the composition boundary
```

That is a future reassessment hypothesis, not a current architecture decision.

---

## G. R4/R5 activation disposition

The research plan defined R4 deep case investigation and R5 candidate planner-state/lifecycle sketches only for candidates that survived the earlier gates.

R3 produced no promoted multi-action planner candidate.

Therefore:

```text
R4 deep promoted-candidate simulation
→ NOT ACTIVATED

R5 promoted-candidate lifecycle/schema sketch
→ NOT ACTIVATED as product-candidate work
```

The small research sketches in Section C are sufficient to explain what evidence would be required to reopen the question. Building a controlled multi-action simulation after failing to find real need would invert the evidence-first method.

---

## H. Claim limits

This research does **not** establish that:

- LLM planning will never add product value;
- resolver/currentness evidence is unimportant;
- deterministic sequencing is always superior;
- richer target-environment or mediation support should not be built;
- the first X1 seam should be deleted;
- the local model is generally reliable;
- no future public case can justify multiple actions;
- v3 should never exist;
- the current main route must take one specific disposition.

It establishes only the current evidence-backed boundary:

> **No independently justified richer planner action-space/selection responsibility was demonstrated strongly enough to expand X1 now. Real capability growth should continue at correct deterministic/semantic owners, and richer planner evaluation should reactivate when actual capability composition creates a non-trivial planning problem.**

---

## I. Research completion / stop line

The delegated research is complete for the current question because:

- historical and planner-evaluation exposure is mapped;
- serious candidate capability families were inventoried;
- each was compared with the strongest simple deterministic owner;
- one real missing capability survived long enough for targeted external validation;
- new public cases were screened and two were consumed as useful design evidence;
- the search produced no real non-trivial competing-action case;
- no holdout was manufactured;
- all material methods/barriers/negative findings are preserved;
- further searching without a changed hypothesis is increasingly likely to become architecture-seeking rather than decision-changing research.

Main can now use this response to decide the honest X1 disposition and whether/when a fresh v3 is worth freezing.
