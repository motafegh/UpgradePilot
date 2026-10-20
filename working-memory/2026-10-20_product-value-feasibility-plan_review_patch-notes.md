# Product-value feasibility plan — review patch notes

**Date:** 2026-10-20  
**Status:** Review amendment request; non-controlling until incorporated by the owning plan/proposal/live-state artifacts  
**Subject:** `plans/PRODUCT_VALUE_AND_TRANSPARENT_BASELINE_FEASIBILITY_INVESTIGATION_PLAN.md` and any directly affected strategic/live handoff wording  
**Purpose:** Preserve the current bounded product-value/feasibility direction while correcting four material issues identified during review before investigation execution is authorized.

## 1. Review conclusion

The current plan is structurally strong and should **not** be redesigned wholesale. Preserve its central purpose and boundaries:

- one bounded decision/readiness investigation rather than another open-ended research programme;
- six-active-engineering-hour total ceiling;
- zero model predictions, zero model loading/GPU work, zero network acquisition, zero target execution and zero benchmark-arm execution during this investigation;
- comparison readiness before any expensive new interpretation subsystem;
- one real producer-to-consumer trace;
- reuse of accepted owners and current proposition/evidence/synthesis semantics rather than a parallel truth model;
- deterministic/source-relation work as a candidate, not the predetermined answer;
- honest `ready`, `partly ready`, `not ready`, `narrow`, `stop`, `defer` or `inconclusive` outcomes;
- no automatic follow-on Build, inference, benchmark, model/agent experiment or architecture expansion.

The following amendments refine that plan without changing its basic direction.

---

## 2. Required patch A — broaden scenario screening beyond S001–S006

### Problem

The plan currently hard-codes detailed readiness inventory around S001–S006. That is historically understandable because S001–S005 formed the original transparent-baseline programme and S006 was the later targeted-check experiment, but it is not a sufficiently justified boundary for the present product-value decision.

The product-simulation workspace now contains **S001–S016**. Later cases exercise responsibilities that are highly relevant to the current product and may be more discriminating for the next investment decision than some earlier scenarios:

- S007 — coordinated dependency/package-family reasoning and investigation pruning;
- S008 — artifact serviceability and source-fallback separation;
- S009 — publication/reproducibility/provenance contracts;
- S010 — multiple independently grounded mechanisms from one proposal;
- S011 — optional environments, platform activation and CI coverage;
- S012 — persisted-artifact producer-version provenance;
- S013 — prior state formation versus later no-sync exercise;
- S014 — command-completion state versus installation provenance;
- S015 — marker applicability across runtime environments;
- S016 — lock membership versus selected-environment reachability.

A fixed `S001–S006` denominator therefore risks selecting cases because of historical chronology rather than because they best discriminate the current product question.

### Required change

Replace the fixed deep `S001–S006` readiness cohort with a **two-level bounded screening design**:

```text
S001–S016
    ↓
lightweight eligibility / relevance / retained-evidence / mode screening
    ↓
smallest discriminating deep-readiness cohort
    ↓
detailed comparison-readiness / consumer-trace work
```

All sixteen cases should receive a light first-pass classification within the existing total time ceiling. This is not authorization to deeply analyze every case.

For the lightweight pass, capture only what is necessary to decide whether the scenario contributes a distinct product-value question:

1. current product-boundary eligibility;
2. mechanism/responsibility exercised;
3. retained evidence availability and obvious material gaps;
4. plausible evaluation mode: fresh product, retained replay, deterministic component proof, manual/historical evidence only, or unavailable;
5. whether the case adds a distinct comparison responsibility rather than duplicating another case;
6. material reviewer/oracle/exposure limitation;
7. provisional deep-readiness value.

Then select the **smallest discriminating deep cohort** based on responsibility coverage and decision value, not scenario number. The deep cohort should seek useful contrasts such as, where supported by retained evidence:

- baseline-sufficient / no-added-value control;
- misleading coarse baseline or false reassurance;
- source/API relation;
- CI/runtime/environment coverage;
- dependency/package/environment state;
- multi-mechanism reasoning;
- provenance or persisted-state boundary;
- justified unresolved/stopping behavior.

Do not require a fixed number of deep cases. A smaller cohort is acceptable if it covers the decision; a somewhat larger cohort is acceptable only within the unchanged six-hour ceiling and with a recorded reason.

### Important boundaries

- S003 remains useful historical failure/attribution pressure, but TypeScript/npm is outside the supported Python product boundary and must not count as Python runtime product coverage.
- Historical completion does not automatically make a case currently replayable or product-supported.
- Later cases must not be promoted into protected holdouts merely because they were not used in the recent Investigator experiment. They are already exposed project-development evidence.
- Missing or unusable retained material is a readiness finding, not permission to repair/reacquire it inside this investigation.
- Do not add S017+ or conduct new case discovery merely to improve coverage counts.

### Budget implication

Keep the **same six-hour total ceiling**. Reallocate the existing first two-hour readiness budget approximately as:

- fast S001–S016 screening first;
- remaining readiness time for the selected deep cohort.

Do not expand the total budget merely because the inventory now starts from sixteen cases.

---

## 3. Required patch B — make bounded multi-role / multi-agent decomposition an explicit candidate

### Problem

The accepted strategic discussion intentionally preserved multi-role/multi-agent methods as a serious future candidate, but the current feasibility plan makes this too implicit under a broad label such as `focused semantic diagnostic`.

That risks losing an important conclusion from the prior experiments:

- autonomous Agent behavior sometimes acquired useful evidence that Fixed policy missed and sometimes used less observed input/time;
- nevertheless semantic/recommendation failures persisted;
- supplied complete evidence plus a single interpretation/report call also remained inadequate;
- the older Fixed method already had multiple stages, so "more stages" alone is not a demonstrated remedy.

The correct unresolved hypothesis is therefore not "more agents are smarter." It is whether **responsibility isolation, scoped context and typed handoffs** materially improve semantic proposition handling and validation compared with the current single-pass responsibility shape.

### Required change

Make **bounded multi-role semantic interpretation / validation** an explicit alternative in the first decision gate rather than hiding it inside a generic semantic-diagnostic bucket.

The alternatives should distinguish at least:

1. reuse/repair of an existing deterministic owner or projection;
2. bounded deterministic source-fact/relation derivation;
3. single-pass semantic interpretation diagnostic/improvement;
4. **bounded multi-role semantic interpretation/validation experiment**;
5. materially different deployment/model test when a specific residual question justifies it;
6. positive action-permission/synthesis work where existing producer facts can satisfy it;
7. finite product-versus-transparent-baseline comparison where ready;
8. narrow/defer/stop.

This investigation must **not run** the multi-role option. It has zero model-call allowance. It should only decide whether that option becomes the next experiment worth paying for.

### Candidate hypothesis to preserve

A later bounded multi-role experiment, if selected, should test something like:

```text
same bounded evidence
+
explicit responsibility separation
+
smaller/scoped role contexts
+
typed proposition/evaluation handoffs
+
independent challenge/validation responsibility

versus

one model response carrying relation-building,
interpretation, uncertainty handling and recommendation/reporting together
```

Potential roles may include:

```text
Investigator / evidence selector
        ↓
Relation / proposition analyst
        ↓
Validator / skeptic
        ↓
Synthesis owner
```

But these are **responsibilities**, not mandatory processes, models, agents or frameworks. A first comparison may deliberately use the same underlying model in multiple isolated calls so that role decomposition can be studied without immediately confounding it with model-family differences.

Do not preselect an agent framework, swarm, shared-chat design, memory framework or different model per role. Those remain later implementation choices only if the role experiment itself is selected and justified.

### Decision criteria for whether multi-role deserves the next experiment

The feasibility findings should say explicitly whether current evidence suggests that the remaining bottleneck is plausibly improved by responsibility decomposition. Useful indicators include:

- important facts/relations are already available but one-pass interpretation loses, invents or conflates them;
- a distinct validation responsibility could reject false propositions while retaining supported findings and justified unknowns;
- smaller role-specific contexts could remove irrelevant competing material;
- a staged handoff would expose exactly which responsibility failed.

Counterevidence should also be recorded:

- earlier Fixed work already used staged responsibilities and still failed;
- adding calls/roles increases cost and creates new handoff/failure modes;
- same-model agreement is not independent evidence;
- an always-reject/always-unresolved validator is not useful;
- deterministic/native owners may solve a specific problem more cheaply.

The gate may therefore select multi-role, defer it, reject it for the current gap, or leave it unresolved.

---

## 4. Required patch C — correct the recommendation-evidence adequacy rule

### Problem

The current plan contains wording equivalent to:

> an asserted/inferred recommendation with no supporting recommendation evidence is inadequate.

As a universal rule, this is too structural and can recreate a limitation already identified in the recent interpretation experiments.

Citation-count/list-presence is not semantic entailment. Conversely, a legitimate bounded abstention, uncertainty statement or targeted inquiry may be justified by an explicitly established **missing observation / unresolved premise**, for which there is not necessarily a source citation proving the absence itself.

### Required change

Replace the blanket empty-list rule with a **material-premise / semantic-support rule**.

Recommended meaning:

> Any recommendation, reassurance, compatibility/risk conclusion or requested action is semantically inadequate when a material premise is unsupported, contradicted, stronger than the admitted evidence, or when the result suppresses a decision-critical unresolved premise. Nonempty citations do not cure this. A scoped abstention, uncertainty statement or bounded next-evidence request may remain adequate when it explicitly names the unresolved/missing observation and does not promote that absence into a factual technical conclusion.

Preserve these distinctions:

```text
citation exists
!= cited source entails the material premise
```

```text
no recommendation citation
!= automatically inadequate
```

```text
missing observation explicitly preserved
!= negative evidence
```

The frozen historical experiment results must remain unchanged; this patch governs future comparison/readiness review criteria rather than retroactively regrading old runs.

---

## 5. Required patch D — make explicit review/authorization mandatory before Build

### Problem

The plan correctly avoids unnecessary document proliferation and says that a findings packet may contain a complete next-action contract without necessarily requiring another plan. That is reasonable.

However, the handoff must not be interpretable as:

```text
FINDINGS contains complete contract
→ implementation may begin automatically
```

### Required change

Add an explicit rule:

> Even when the findings packet contains a complete next-action contract and no separate plan document is necessary, that contract requires explicit review/acceptance before any Build, source/test modification, benchmark execution, model/agent inference, network acquisition, target execution or product-action admission begins.

This is an authorization boundary, not a requirement to generate redundant paperwork.

A complete findings contract may be sufficient as the artifact presented for decision; it is **not self-authorizing**.

`MEMORY.md` must remain the live owner of the selected continuation after that decision.

---

## 6. Things that should remain unchanged

Do **not** use these patch notes to reopen or weaken the following decisions:

- the accepted hybrid evidence/authority architecture;
- separation of observations, proposals, evaluations, proposition truth state and maintainer-action permission;
- current Workspace/evidence ownership and `PropositionState`/`PropositionAssessment` semantics where they already fit;
- current abstain-only synthesis boundary unless a separately admitted positive-action responsibility proves its prerequisites;
- discontinuation of automatic prompt/instruction tuning on the exposed Investigator line;
- preservation of the completed negative/inconclusive Investigator evidence without retry/regrading;
- product-vs-transparent-baseline value as the first strategic question;
- six-active-hour total ceiling for this investigation;
- zero model calls/GPU/network/target execution/benchmark execution during this investigation;
- missing data as a finding rather than a repair obligation;
- no automatic parser, validator, multi-agent framework, model sweep, discovery optimization or protected-corpus campaign;
- deterministic source relations as a candidate rather than the selected product architecture;
- future protected qualification only after an exact method is frozen, using newly protected material rather than exposed development scenarios;
- learner D/E debt remains separate from engineering completion.

---

## 7. Expected revision surface

The parallel assistant should inspect and revise **only the owning artifacts actually affected**. At minimum:

1. `plans/PRODUCT_VALUE_AND_TRANSPARENT_BASELINE_FEASIBILITY_INVESTIGATION_PLAN.md`
   - replace fixed S001–S006 deep inventory with S001–S016 light screen → selected deep cohort;
   - explicitly add bounded multi-role interpretation/validation as an alternative;
   - correct the recommendation-evidence rule;
   - add explicit pre-Build authorization language;
   - reconcile time allocation without increasing the six-hour ceiling.

2. `working-memory/2026-10-20_product-value-and-baseline-feasibility-investigation-planning_lbd-cycle.md`
   - record the review correction and why the original six-case boundary/multi-role wording changed;
   - preserve that no investigation execution occurred during revision.

3. `MEMORY.md`
   - update only if needed to reflect the revised prepared-plan scope; do not claim investigation execution or select a next implementation.

4. `proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md`
   - revise only if the assistant finds an actual inconsistency. The accepted strategic proposal already preserves multi-role as conditional and source-relation work as non-predetermined; do not churn it merely to mirror plan wording.

Do not modify product source/tests, historical simulation artifacts, experiment outputs, accepted specifications/ADRs or frozen evidence to satisfy this documentation patch.

---

## 8. Verification expected after revision

Before presenting the revision for review, verify that:

- the plan names S001–S016 as the lightweight screening universe;
- it does **not** require deep analysis of all sixteen;
- deep-cohort selection is based on discriminating responsibility/value coverage and remains bounded by the same six-hour ceiling;
- S003 is still excluded from supported Python product coverage while retained as historical pressure evidence;
- multi-role/multi-agent decomposition is explicit as a candidate but receives zero calls during this feasibility investigation;
- the plan does not preselect source relations, a model, an agent framework or a positive action;
- semantic adequacy is based on material premise support, contradiction and unresolved-state preservation rather than citation-list cardinality;
- a complete findings/action contract still requires explicit acceptance before execution;
- existing owners are reused and no duplicate proposition/evaluation vocabulary is introduced without justification;
- no benchmark, inference, network acquisition, target execution, product source/test change or historical-evidence mutation occurred while applying the patch;
- `MEMORY.md` continues to state only the actually authorized continuation.

---

## 9. Decision status

These patch notes request revision of the prepared investigation plan. They do **not** authorize the six-hour investigation itself.

After the owning plan and handoff are revised, review the resulting diff and decide whether to authorize execution.
