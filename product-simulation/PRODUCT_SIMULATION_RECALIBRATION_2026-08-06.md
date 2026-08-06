# Product Simulation Recalibration — 2026-08-06

**Status:** Dated discovery recalibration; non-controlling  
**Owner:** Ali Rajabi  
**Scope:** Reinterpret the role and priorities of `product-simulation/` after major UpgradePilot implementation and design progress without rewriting S001–S005 history

## 1. Why recalibration is necessary

The July S001–S005 cycle was intentionally performed before the current product evidence engine
existed. It discovered important logical responsibilities and contrasts, then closed D1 at the
planning depth required at that time.

Since then UpgradePilot has implemented and behavior-validated a substantially deeper public-PR
path, including:

- exact PR/base/head and changed-file identity;
- supported dependency-change extraction across admitted Python representations;
- bounded CI dependency-exercise evidence;
- exact PyPI release and package-wide release-index responsibilities;
- upstream repository association with provenance corroboration;
- exact Git tag/commit and changelog acquisition;
- crossed-release interval authority;
- bounded local semantic extraction with deterministic grounding;
- exact target `requires-python` interpretation;
- deterministic target-Python applicability/relevance;
- conditional orchestration and explicit unresolved states;
- live S001 end-to-end validation that exposed real integration/generalization defects.

The product has therefore moved from mainly asking what evidence and artifacts a dependency
review requires to asking what sits **between evidence and eventual maintainer-facing action**.

A separate progressive design discussion is now examining that future product model. This
workspace should stay informed by that discussion while retaining freedom to discover
counterexamples, alternatives, and responsibilities the discussion has not yet named.

## 2. Critical role clarification

Product simulation is **aligned with UpgradePilot, not bounded by its current plans or design**.

That means:

- current product behavior and design records are important context;
- simulation should not accidentally reason from superseded assumptions;
- current implementation limitations should not be mistaken for the outer product horizon;
- current design hypotheses should not be encoded as expected answers;
- a real case may reveal that a plan, taxonomy, action model, or architecture is incomplete;
- simulation may explore future failure, temporal, security, evaluation, operational, or
  reasoning responsibilities before implementation admits them.

The complementary boundary is equally important:

> Product simulation may discover or recommend product/design changes, but it does not make
> those changes controlling by itself.

Adoption still belongs to the charter, plans, specifications, ADRs, source/tests, or other
normal owner for the affected responsibility.

## 3. What remains valid from the historical program

The following principles survive the recalibration strongly:

- real cases are essential for external realism and discovering irregularities;
- one case should not silently become a universal schema;
- exact identity, provenance, time/revision, and missing/degraded evidence matter;
- observation, interpretation, finding, and decision should remain distinguishable;
- conditional investigation and explicit non-activation are first-class behaviors;
- stopping is a technical result, not lack of effort;
- the transparent baseline is useful as a comparator and can be sufficient, wrong, or merely
  weaker in explanation;
- targeted checks require a named unresolved question rather than generic caution;
- repeated execution and causal attribution should activate only when needed;
- historical merge/action state is not objective truth;
- synthetic evidence is valuable for isolation but cannot replace real-world validation;
- case count is not a quality metric.

## 4. What changes after recalibration

### 4.1 Historical action labels lose privileged status

S001–S005 retain their recorded historical actions exactly as evidence of the D1 process.
They are not automatic labels for the current or future product.

For example, later production evidence for S001 now supports a bounded conclusion about a
Python support-drop concern being outside the target's declared Python range while CI exercise
remains unresolved. That does not reproduce or falsify the historical `merge after normal
review` label mechanically; it demonstrates that improved evidence can narrow what the system
is justified in claiming.

### 4.2 Case value is no longer centered mainly on action-class novelty

A future case may be highly valuable even when no final maintainer action is selected yet.
It may reveal:

- a new impact/problem shape;
- an activation condition;
- an applicability rule;
- a useful target surface;
- a failure of negative evidence;
- a discriminating investigation;
- a stopping condition;
- a temporal or authority transition;
- a new uncertainty structure;
- an evaluation or recovery invariant.

### 4.3 The current high-value reasoning lens

A useful interrogation pattern is:

```text
upstream/change signal
→ possible impact or concern
→ activation condition
→ exact target surface/path/configuration
→ applicability evidence
→ coverage / contradiction / uncertainty
→ decision-relevant open question
→ useful next investigation/check, if any
→ sufficiency / stopping
→ maintainer-facing consequence or unresolved state
```

This is a **simulation lens**, not an accepted product architecture. Cases are allowed to show
that this decomposition is incomplete or wrong.

## 5. Relationship to the progressive decision-model discussion

The active design working record is:

`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`

When relevant, simulation work should refresh that record before making consequential
recommendations because it is being appended progressively in another session.

Product simulation can contribute evidence to its four broad conversations:

1. impact/problem model;
2. applicability and investigation activation;
3. best next investigation or targeted check;
4. sufficiency, stopping, and maintainer-facing result.

But simulation may also explore beyond those four conversations if a material case reveals a
new responsibility. The working record is a coordination surface, not a ceiling.

## 6. Re-reading S001–S005

The next useful interpretation of S001–S005 is not another action summary. It is to ask, for
each case:

- what possible impact or problem existed;
- what upstream/evidence signal suggested it;
- what condition would make it activate;
- what target surface determined applicability;
- what evidence covered or failed to cover that surface;
- what uncertainty remained;
- which investigation actually discriminated between possible conclusions;
- which deeper investigation would have added little value;
- why the case could or could not stop;
- what reusable reasoning pattern was exposed.

That re-analysis is preserved separately in
[`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md).

## 7. Hybrid case strategy retained and simplified

Use a four-level evidence ladder when useful:

1. **untouched real cases** — occurrence, context, external validity, unexpected irregularities;
2. **real-derived controlled variants** — isolate one variable while retaining real structure;
3. **fully synthetic scenarios** — control timing, state, failure, security, or rare conditions;
4. **generated/property-based cases** — systematic invariant and state-transition coverage.

The preferred loop is:

```text
real case reveals uncertainty
→ controlled variant isolates it
→ method/implementation behavior becomes testable
→ real evidence challenges or validates the result
→ observed irregularities become future controlled regressions
```

Use the least artificial level that can answer the question safely and discriminatingly.

## 8. Status of July 31 candidate screening

[`CASE_CANDIDATE_SCREENING_01.md`](CASE_CANDIDATE_SCREENING_01.md) remains preserved exactly as
the July 31 screening result.

Its strongest candidate — theHarvester Requests `2.31.0 → 2.32.0 → 2.32.2` — remains a
high-value real temporal/yank/correction/supersession sequence.

However, the screening's priority order is no longer a standing S006 recommendation because
the product's largest immediate design uncertainty has shifted toward impact, activation,
applicability, investigation choice, and sufficiency.

Therefore:

- do not delete or rewrite the screening;
- retain theHarvester as a strong temporal/lifecycle candidate;
- do not assign S006 from that screening by inertia;
- select future cases through the recalibrated framework and the evidence available at the
  time of selection.

## 9. Recalibrated candidate priority families

Current evidence suggests this discovery priority order, subject to change when new evidence
appears:

1. **real API/runtime behavioral impact + demonstrable target usage + incomplete/ambiguous
   coverage**;
2. **real activation/applicability contrast** where concerning upstream behavior applies or
   does not apply depending on target configuration/usage;
3. **targeted-check discrimination** where one specific check can materially change what is
   known;
4. **sufficiency/stopping contrast** where deeper analysis should deliberately remain inactive;
5. **temporal/yanked/supersession sequence**, including the retained theHarvester candidate;
6. **controlled acquisition/retry/security/recovery variants** attached to real anchors when
   possible.

This is a discovery ranking, not an implementation roadmap.

## 10. What this recalibration does not do

It does not:

- create S006;
- choose a final impact taxonomy;
- choose the final decision architecture;
- change the project charter or its current action vocabulary;
- change `MEMORY.md` or the implementation route;
- authorize source implementation;
- invalidate S001–S005;
- import the old case-program proposal branch wholesale;
- claim the current reasoning lens is complete.

## 11. Working principle going forward

The workspace should optimize for **discriminating evidence**, not agreement with current
plans and not novelty for its own sake.

A strong simulation result should make at least one of these clearer:

- what can happen;
- when it matters;
- how we know it matters to this target;
- what evidence would change our understanding;
- what additional work is worth doing;
- when further work is not worth doing;
- what remains unresolved;
- what the product should consider learning, representing, testing, or refusing to claim.
