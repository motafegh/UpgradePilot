# B2/X1 EvidenceGapPlanner R2 — Planning Budget Envelope

**Date:** 2026-08-30  
**Status:** R2 SLICE COMPLETE — first-seam planning-budget semantics decided  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`  
**Previous R2 slice:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`

## 1. Why this slice exists

The historical experiment carries:

```text
remaining_steps: int
```

and deterministic admission rejects action selection when `remaining_steps <= 0`.

That is enough for a bounded pilot guard, but the name does not say what a "step" means and does not distinguish semantic investigation budget from lower-level operational retries/timeouts/resources.

Current experiment truth also includes categorical action `cost_class` values:

```text
local
low_network
moderate_network
local_model
```

The real A1 target-Python declaration action is currently `low_network`.

There is no current multi-action executor or trustworthy measured action-latency/cost dataset from which to invent a numerical optimizer.

## 2. First-seam decision — name the semantic budget explicitly

Use the working concept:

```text
planning_budget:
    remaining_investigations: int
```

rather than generic:

```text
remaining_steps
```

Meaning:

> the number of additional bounded planner-selected investigation executions that may still begin for the current planning responsibility.

This is **semantic planning budget**, not an HTTP-attempt counter, wall-clock stopwatch, token budget, or universal resource score.

## 3. When one investigation unit is spent

Freeze the first-seam lifecycle as:

```text
model proposes action
→ 0 investigation units spent

structured output parses
→ 0 spent

deterministic admission accepts
→ 0 spent

fresh pre-execution state/catalog/precondition revalidation passes
→ still 0 spent

bounded investigation execution actually begins
→ spend 1 investigation unit
```

Why execution start is the best current boundary:

1. a malformed/invented/rejected model proposal performed no investigation;
2. an action admitted at T1 may become stale before T2 execution and should not consume semantic investigation budget merely because it was once valid;
3. once real execution begins, time/network/compute may already be consumed even if no trusted result is eventually produced;
4. counting only successful typed results would incorrectly make costly failed executions appear free.

## 4. Provider/executor retries do not automatically spend new planner units

Example:

```text
EvidenceGapPlanner selects A1 once
→ A1 execution begins
→ spend 1 remaining_investigations unit
→ provider request times out
→ deterministic bounded retry
→ provider succeeds
→ domain result interpreted
```

Planner cost:

```text
1 investigation
```

not:

```text
2 model/planner investigations
```

The retries are operational attempts inside one admitted investigation responsibility.

Therefore:

```text
planner investigation budget
!= provider retry budget
```

Keep provider controls separately owned:

```text
request timeout
retry limit
backoff
rate-limit handling
provider-specific operational limits
```

## 5. Relationship to `consumed_actions`

Budget expenditure and consumed history are related but not identical.

### Trusted typed result/problem

```text
execution begins
→ spend 1 investigation unit
→ trusted typed result/problem produced
→ propositions/planning evidence update
→ action enters consumed_actions
```

### Transient acquisition failure after execution starts

```text
execution begins
→ spend 1 investigation unit
→ transient provider/acquisition failure
→ deterministic retry policy may run
→ no trusted domain result/problem produced
→ do NOT fabricate proposition evidence
→ do NOT automatically mark action consumed
```

The work still consumed one semantic execution opportunity because the bounded investigation actually ran and consumed real resources.

If deterministic retries are exhausted, the orchestration layer must not blindly present the exact same operationally unavailable action to the model as though nothing happened. A future execution-capable design must reflect current operational availability/defer state in the trusted catalog/control plane. The exact provider-unavailability policy is not required for the current non-executing first seam.

## 6. Why budget should eventually be an envelope, not one universal scalar

Different constraints answer different questions:

```text
remaining_investigations
→ how many additional semantic investigations may begin?

remaining_time_seconds
→ how much wall-clock decision time remains?

remaining_external_cost
→ how much paid/external resource spend remains?

provider_retry_limit
→ how many operational retries may one executor perform?
```

Collapsing them into one number such as:

```text
budget = 7
```

would erase meaning and make action trade-offs hard to interpret.

Therefore keep the architectural shape extensible as a **planning budget envelope**, while admitting only dimensions that have real evidence and planning value.

## 7. Time budget — valuable future dimension, not first-seam fiction

The user-proposed time dimension is a strong future candidate.

It becomes genuinely useful when:

```text
multiple admitted actions are plausible
+
their expected latency differs materially
+
a real remaining time constraint exists
+
the estimates are trustworthy enough to support planning
```

Example future state:

```text
remaining_time_seconds = 40

A: static check
estimated latency = low

B: behavioral reproduction
estimated latency = high
```

Then time can change which evidence has the best decision-relevant value inside the resource envelope.

Current first seam does not yet have the required competing action space or trustworthy latency estimates.

Decision:

```text
remaining_time_seconds
→ NOT required in first-seam model context
→ preserve as planned extensibility
→ collect real timing telemetry during later R4/R5 implementations where useful
```

This follows:

```text
measure first
→ understand variance/ownership
→ then decide whether timing belongs in planner policy
```

not:

```text
invent estimates
→ make model reason over fake precision
```

## 8. Cost/resource dimensions follow the same admission test

A future model-visible budget dimension earns inclusion only when all are true:

1. the resource is actually bounded/measured;
2. current admitted actions materially differ on it;
3. the planner can change its choice based on that difference;
4. capability descriptors expose a trustworthy compatible resource profile;
5. exposing the value does not transfer executor/provider authority to the model.

Potential examples:

```text
remaining_time_seconds
remaining_external_cost
compute class / GPU requirement
network acquisition class
```

Do not add them merely because they are conceivable.

## 9. Relationship to action `cost_class`

Historical action descriptors already contain:

```text
cost_class = local | low_network | moderate_network | local_model
```

This is evidence that resource characteristics are a recognized planning concept.

However the current taxonomy is coarse and the first X1 catalog has only one real independently justified action. Therefore it does not yet establish non-trivial cost-aware LLM planning.

R2 should reconsider action-resource descriptors in the next capability-descriptor slice:

```text
which cost/latency/resource fields help the model understand capability trade-offs now?
which are useful only later when multiple actions coexist?
which should remain executor-only?
```

## 10. First-seam candidate schema

```text
planning_budget:
    remaining_investigations: int  # non-negative
```

Model-visible because it changes whether another semantic investigation may be selected.

System/evaluator may separately retain richer telemetry:

```text
elapsed_time
provider request attempts
provider retry count
request latency
model latency
execution latency
external cost if any
```

Those do not automatically become planner inputs.

## 11. R4/R5 learning and telemetry pressure

During the ordinary-Python and LangGraph implementation comparison, preserve enough timing/trace evidence to learn rather than guess, for example where proportionate:

```text
planner model-call latency
admission/revalidation latency
framework orchestration overhead
capability execution latency when execution exists
retry counts / provider latency when applicable
```

This telemetry supports:

- implementation comparison;
- future time-budget design;
- observability learning;
- separating framework overhead from model/provider latency.

Do not turn one development run into a stable latency SLA.

## 12. LbD concepts earned in this slice

- semantic budget vs operational resource policy;
- lifecycle accounting;
- execution-start commitment point;
- planner action vs provider retry;
- multi-dimensional resource envelopes;
- measurement/telemetry before optimization;
- qualitative cost classes vs quantitative estimates;
- value-of-information under resource constraints;
- avoiding false precision.

## 13. Next R2 slice

Continue with the **allowed capability descriptor** boundary.

Questions:

```text
What does the model need to know about each admitted capability to compare its evidence value?

Which fields remain deterministic-only authority metadata?

Should mutation_class still be model-visible when current seam admits only read-only capabilities?

Does target_proposition duplicate information already expressed by purpose/preconditions?

Should the current coarse cost_class be visible now?

How should future time/cost/resource profiles extend the descriptor without inventing precision?
```

After that, construct the final R2 projection table/rendered examples and decide whether R2 can close.
