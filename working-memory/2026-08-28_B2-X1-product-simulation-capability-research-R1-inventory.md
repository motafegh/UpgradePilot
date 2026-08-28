# B2/X1 Product-Simulation Capability Research — R1 Capability-Responsibility Inventory

**Date:** 2026-08-28  
**Status:** R1 COMPLETE — bounded capability inventory established; serious hypotheses admitted only for R2 discrimination  
**Plan:** `../plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`  
**R0 evidence-use map:** `2026-08-28_B2-X1-product-simulation-capability-research-R0-evidence-use-map.md`  
**Evaluated main revision:** `14ba589de18aa72b0f9098d5154cc722c494c256`  

## 1. R1 question

> Which real recurring investigation responsibilities could plausibly become bounded planner-visible capabilities, and which should remain deterministic orchestration, separate semantic-model responsibilities, or known-outside/defer responsibilities?

R1 is an inventory/admission slice. It does **not** decide the final action space, implement an action, call the planner, screen fresh public cases, or freeze v3.

---

## 2. Current product-owner map relevant to capability research

The active implementation already contains substantial deterministic evidence machinery. Candidate actions must not duplicate these owners merely to make the planner look richer.

### 2.1 Application sequencing

`src/upgradepilot/investigation.py` currently performs a fixed read-only sequence around one public dependency PR:

```text
exact PR + changed files
→ dependency transition/source contexts
→ exact-head CI runs/jobs + exact workflow definitions
→ project-environment sources
→ static environment selection / dependency consumption / CI coverage
→ proposed PyPI release
→ upstream repository
→ release interval/index/tag/changelog authority
→ bounded support-drop semantic extraction
→ grounded support-drop candidate
→ mechanism-specific Python-support impact/applicability
→ deterministic A1 target-Python-declaration selection
→ exact target declaration read
→ target relevance
→ updated applicability state
```

The application coordinates these owners; it does not own their parsing/domain semantics.

### 2.2 Dependency-environment and CI owners

Current deterministic source includes:

- `dependency/environment_selection.py` — static pip/uv project selectors, extras/groups, bounded uv package scope;
- `dependency/environment_membership.py` — source-established optional-extra/group membership versus static selection;
- `dependency/uv_lock_structure.py` / `dependency/uv_reachability.py` — admitted lock structure and selected-root reachability;
- `ci/consumption.py` — exact static CI consumption composition;
- `ci/dependency_exercise.py` — exact-head runtime-success evidence kept separate from static consumption/direct exercise.

The accepted proof ladder deliberately keeps these separate:

```text
transition
!= environment membership
!= static CI consumption
!= resolver satisfiability
!= command execution
!= installation success
!= exact runtime version observation
!= behavior exercise
!= behavior success
!= compatibility/safety
```

This means several apparently missing facts are **intentional proof boundaries**, not parser bugs.

### 2.3 Target artifact/environment owners

`target/artifact_environment.py` can interpret a bounded exact workflow definition into partial target environment facts such as literal runner, setup-python version, and direct dependency installation declaration.

It intentionally does not establish:

- expression/matrix evaluation;
- reusable-workflow expansion;
- exact wheel tags;
- runtime environment formation;
- command execution/success.

`impact/artifact_serviceability.py` already owns exact old/proposed PyPI wheel-inventory comparison and target-applicability composition, but its `TargetWheelCompatibilityEvidence` contract starts **after** exact target compatibility acquisition/interpretation. The module explicitly says a later increment must earn those tags from admitted target evidence.

### 2.4 Upstream semantic owner

`upstream/support_drop_extractor.py` is already a bounded LLM semantic extractor for one admitted upstream mechanism. It is not a planner. S010 demonstrates that broader multi-mechanism discovery may eventually require a richer semantic-discovery responsibility, but that must not be conflated with choosing the next investigation action.

### 2.5 First A1 owner

`impact/python_support.py` explicitly keeps `select_python_support_drop_investigation(...)` mechanism-specific and currently admits only:

```text
acquire_exact_target_python_declaration
```

The selector is intentionally deterministic until real evidence demonstrates shared investigation concepts beyond this first mechanism.

---

## 3. Candidate inventory summary

| ID | Candidate responsibility | Primary evidence | R1 disposition |
|---|---|---|---|
| CAND-01 | exact target Python declaration acquisition (A1) | S001 + current product | **deterministic owner better; retain as control/known action** |
| CAND-02 | exact-head resolver/currentness/satisfiability evidence | AUDIT-004 + S001/S002/S007 | **PROMOTE TO R2 serious hypothesis** |
| CAND-03 | bounded mediated CI/environment-consumption hop inspection | S002/S005/S011 + current CI/environment proof boundary | **PROMOTE TO R2 serious hypothesis, boundary unresolved** |
| CAND-04 | exact target artifact/wheel-environment evidence acquisition | S008 + current artifact-serviceability/target-environment owners | **PROMOTE TO R2 tentative hypothesis** |
| CAND-05 | targeted behavioral/differential reproduction | S006 | **known useful outside capability / DEFER for current executable catalog** |
| CAND-06 | persisted-artifact provenance/history acquisition | S012 | **known useful outside capability / DEFER; narrower public-provenance form remains hypothesis** |
| CAND-07 | repository-purpose / reproduction-context interpretation | S009 | **separate context/semantic responsibility; reject as generic planner action** |
| CAND-08 | upstream multi-mechanism discovery | S010 | **separate semantic-discovery responsibility; not planner action** |
| CAND-09 | generic pre-bound exact source/config read | A1 + CI/config cases | **deterministic owner better unless later real multi-source choice earns planner exposure** |
| CAND-10 | static↔runtime CI correlation / reusable-workflow completion | current product proof gaps | **separate deterministic evidence responsibility; not planner action at R1** |

No quota was used. Only candidates with independent evidence value survived to R2.

---

# 4. CAND-01 — exact target Python declaration acquisition (A1)

## C-01 planning uncertainty

Whether the exact target revision declares a Python range that can be compared with an already-grounded upstream support-drop line.

## C-02 evidence output

Existing typed result family:

```text
TargetPythonDeclaration
or
TargetPythonDeclarationProblem
```

## C-03 deterministic locator

Already exact/pre-bound:

```text
repository = target PR repository
revision = exact PR head
path = pyproject.toml
```

## C-04 bounded effect

Read-only exact repository-file acquisition.

## C-05 existing owner

Complete enough for current responsibility:

- repository exact-file provider;
- `target/python.py` interpretation;
- `target/relevance.py` comparison;
- `impact/python_support.py` mechanism-specific selection.

## C-06 recurrence/generality

Real and recurring for Python-support-drop candidates, but mechanism-specific.

## C-07 strongest simple deterministic baseline

Current code already implements it directly:

```text
support-drop candidate grounded
+ target declaration proposition unresolved/insufficient
+ target relevance absent
→ read exact target pyproject.toml
```

This policy is small, stable, and transparent.

## C-08 planner-value pressure

None established for the **standalone** A1 state. E3 proved the model can identify the gap, but the deterministic selector already owns the same simple policy.

A1 may still be one action inside a future richer action space; that does not make its current selector an LLM responsibility.

## C-09 engineering/learning value

Useful as a control for:

- closed action binding;
- structured outputs;
- deterministic admission;
- stale-state revalidation;
- multi-action comparison later.

Learning value does not override the deterministic baseline.

## C-10 claim limit

Acquires/interprets the exact target Python declaration only. It does not prove broader compatibility or safety.

### R1 disposition

**DETERMINISTIC OWNER BETTER.**

Do not promote A1 itself as evidence that LLM planning adds product value.

---

# 5. CAND-02 — exact-head resolver/currentness/satisfiability evidence

## C-01 planning uncertainty

Whether exact target dependency declarations/lock state are satisfiable/current under an admitted resolver context when static source/lock evidence cannot settle that proposition.

Representative questions:

```text
is the exact uv lock current against the exact project metadata?
can the exact declared graph resolve under the admitted uv context?
does a resolver failure establish an early package-constraint contradiction?
```

## C-02 evidence output

A future bounded result family could conceptually preserve:

```text
resolver_satisfiability = established | refuted | unresolved
+ exact repository/revision/project/lock/config identity
+ exact resolver operation/configuration
+ typed operational problem when no valid resolver observation exists
```

Exact product type names are not selected here.

## C-03 deterministic inputs/locators

Potentially pre-bindable:

- exact repository/revision;
- exact project root / `pyproject.toml`;
- exact `uv.lock`;
- admitted extras/groups/platform/Python projection where required;
- resolver operation such as `uv lock --check`;
- index/source configuration only when explicitly admitted.

The model should not invent repository paths, indexes, credentials, or shell commands.

## C-04 bounded effect

Potentially bounded and non-mutating with care, but it is **not equivalent to a passive file read**.

A resolver may access package indexes/metadata and can have environment/network effects. Future design must define an isolated/read-only execution boundary and distinguish:

```text
metadata-only/currentness check
from
install/build/target-code execution
```

R1 does not authorize execution.

## C-05 existing owner / missing owner

Current deterministic owners establish:

- lock structure;
- selected-root reachability;
- source/environment membership;
- static CI consumption.

They explicitly do **not** establish resolver satisfiability/currentness.

AUDIT-004 records this as a real deferred evidence opportunity rather than an implementation defect.

## C-06 recurrence/generality

Plausibly recurring for lock/project cases and coordinated dependency families. Evidence:

- S001 positive-side opportunity;
- S007 negative-side family contradiction where resolver was considered but pruned;
- S002 missing captured resolution for FastAPI/Starlette targeted-check confidence;
- broader dependency-environment proof ladder reserves resolver satisfiability as a distinct rung.

## C-07 strongest simple deterministic baseline

A trivial selector is possible when **resolver satisfiability is the only unresolved material proposition**:

```text
resolver proposition unresolved
→ run resolver check
```

That alone does not justify an LLM.

The serious planning question arises when resolver evidence competes with:

- cheaper authoritative static metadata that may already refute the proposition;
- exact source/config evidence that may settle a prerequisite first;
- target-environment selection needed to parameterize a meaningful resolver context;
- a bounded behavioral/runtime question that resolver success cannot answer;
- budget/attempt history.

S007 proves the action can become redundant after stronger static evidence arrives.

## C-08 planner-value pressure

**Real but not yet proven sufficient.**

The information value of a resolver check depends on current epistemic state. A fixed rule that always resolves can over-investigate; a rule that never resolves misses a distinct proof rung.

R2 must determine whether the realistic policy remains a small ordered rule set or becomes meaningfully contextual across candidates.

## C-09 engineering/learning value

Real concepts:

- information-gain planning;
- cost-aware action selection;
- prerequisites;
- stale-plan pruning;
- tool-result-aware replanning;
- execution/evidence authority separation;
- deterministic resolver result interpretation.

## C-10 authority / claim limit

Even a successful exact resolver observation establishes only declared constraint satisfiability/currentness under the admitted resolver context.

It does not establish:

- artifact availability everywhere;
- installation success;
- imports/tests/runtime behavior;
- target compatibility/safety;
- maintainer action.

### R1 disposition

**PROMOTE TO R2 — SERIOUS CAPABILITY HYPOTHESIS.**

Reason: independently valuable missing evidence class + recurring pressure + real action-pruning/information-value variation.

---

# 6. CAND-03 — bounded mediated CI/environment-consumption hop inspection

## C-01 planning uncertainty

Whether a changed dependency environment is actually selected/consumed through one statically referenced mediation layer that the current direct workflow/environment model does not interpret.

Examples of mediation include:

```text
workflow
→ reusable workflow
→ environment selection

workflow
→ tox/nox/task runner configuration
→ dependency environment

workflow
→ repository script/config
→ exact install/sync selection
```

The candidate is **not** arbitrary shell tracing.

## C-02 evidence output

A bounded typed result should establish only the relevant static relation, for example:

```text
mediated consumption supported
or not established
or unresolved
```

with exact source/revision/hop identity and explicit limits.

## C-03 deterministic inputs/locators

To remain credible, the first mediation source should be identified from already-admitted static evidence:

- exact workflow/job/step;
- exact referenced reusable-workflow/config/script path or known task-runner configuration;
- exact target revision;
- exact changed dependency/environment identity.

The model must not receive arbitrary repository browsing/file-path authority.

## C-04 bounded effect

Read-only exact-source acquisition/interpretation can be safely bounded.

Executing the referenced script/task is **not** part of this candidate.

## C-05 existing owner / missing owner

Current product already owns:

- direct requirements installation declarations;
- explicit pip project selection;
- explicit uv extras/groups/scope;
- source environment membership;
- uv selected-root reachability;
- CI static consumption composition.

The accepted dependency-environment plan explicitly does **not** support generic tox/nox/Make/script/task-runner tracing and preserves S005 as transfer pressure rather than silently claiming mediated support.

So a real gap exists, but its correct reusable owner is not yet established.

## C-06 recurrence/generality

Plausibly recurring. Historical pressure includes:

- S005 tox + `uv-venv-lock-runner` mediation;
- S002 relevant Python checks existing in a workflow whose dependency-source relationship was not established by the green build path;
- S011 demonstrates why environment selection itself matters before interpreting test outcomes.

However only S005 currently gives a strong explicit task-runner mediation example. Fresh recurrence evidence is still desirable.

## C-07 strongest simple deterministic baseline

A deterministic graph/IR expansion could be superior if the supported mediation family is small and structural:

```text
known reusable-workflow reference
→ fetch exact referenced workflow
→ deterministic parse
```

or:

```text
known tox config
→ deterministic bounded interpreter
```

An LLM is not justified merely because there is another hop.

## C-08 planner-value pressure

Potential value arises when several pre-bound evidence hops are available and the system must decide which one is material before recursively expanding everything.

Risk of deterministic orchestration:

```text
support each mechanism
→ always traverse every referenced workflow/config/script
→ growing mechanism-specific expansion tree
→ over-investigation / combinatorial source acquisition
```

But this is still a hypothesis. R2 must separate **planner selection among admitted hops** from **the deterministic interpreter required to understand each hop**.

## C-09 engineering/learning value

- hierarchical planning;
- bounded graph traversal;
- information-value prioritization;
- tool/action catalogs with pre-bound references;
- stop/prune semantics;
- evidence lineage across delegation.

## C-10 authority / claim limit

Static mediated-consumption evidence remains static. It does not prove:

- execution;
- install success;
- exact runtime version;
- behavior exercise;
- compatibility.

### R1 disposition

**PROMOTE TO R2 — SERIOUS BUT BOUNDARY-UNRESOLVED HYPOTHESIS.**

R2 must reject it if the honest supported families are better handled by deterministic recursive composition with no meaningful action-choice policy.

---

# 7. CAND-04 — exact target artifact / wheel-environment evidence acquisition

## C-01 planning uncertainty

Whether the exact target environment is compatible with an old published wheel path that disappears or changes in the proposed release.

## C-02 evidence output

The current impact owner already defines the downstream contract conceptually:

```text
TargetWheelCompatibilityEvidence
or TargetWheelCompatibilityProblem
```

The missing responsibility is how exact target-supported tags/equivalent compatibility evidence are earned from repository-owned target evidence.

## C-03 deterministic inputs/locators

Potentially pre-bindable:

- target repository/revision;
- exact workflow/config source candidates;
- job/environment identity;
- dependency transition and old/proposed release inventories.

## C-04 bounded effect

Static exact-file acquisition is read-only.

A dynamic environment probe would require a separately admitted execution boundary and is not part of R1.

## C-05 existing owner / missing owner

Existing partial owners:

- `target/artifact_environment.py` extracts bounded static runner/Python/install facts from one selected local steps job;
- `impact/artifact_serviceability.py` consumes exact target compatibility evidence but does not acquire it.

Current target interpreter abstains on multiple jobs, reusable workflows, expression/matrix complexity, and exact wheel-tag derivation.

The normal `investigation.py` path does not currently integrate artifact-serviceability target acquisition.

## C-06 recurrence/generality

Artifact-serviceability is an admitted product mechanism with S008 pressure, so target-environment evidence is independently useful. Recurrence beyond the initial mechanism exists conceptually for platform/Python artifact compatibility, but richer real-case evidence is limited.

## C-07 strongest simple deterministic baseline

A deterministic target-environment interpreter/selector may be the correct owner if exact job/environment selection follows clear structural criteria.

The LLM is unnecessary if the policy is simply:

```text
one known workflow/job
→ parse it
→ derive target compatibility
```

## C-08 planner-value pressure

Potentially non-trivial when:

- several workflows/jobs/platforms are present;
- one environment matches the removed wheel family while others do not;
- a cheaper static witness can settle the target proposition before a dynamic probe;
- reusable workflow/matrix expansion competes with other evidence paths.

This has not yet been demonstrated strongly enough to call the action planner-owned.

## C-09 engineering/learning value

- evidence-source selection;
- multi-environment prioritization;
- prerequisite planning;
- bounded target-state projection;
- cost-aware static-before-dynamic investigation.

## C-10 authority / claim limit

Target wheel compatibility does not establish source-build success, runtime behavior, or overall compatibility.

### R1 disposition

**PROMOTE TO R2 — TENTATIVE HYPOTHESIS.**

It may be rejected in R2 as deterministic target evidence acquisition unless a real multi-witness/action-choice distinction survives.

---

# 8. CAND-05 — targeted behavioral / differential reproduction

## C-01 planning uncertainty

Whether a mapped upstream behavior change produces an observable difference on the exact target path after static evidence establishes mechanism + target relation but not behavior.

S006 is the strongest preserved example.

## C-02 evidence output

A bounded old/new differential could produce:

```text
observed behavior under old dependency
observed behavior under proposed dependency
exact input/target symbol/environment
or typed execution problem
```

## C-03 deterministic inputs

S006 demonstrates that repository/revision, target symbol, input, dependency versions, and observation surface can in principle be pre-bound.

## C-04 bounded effect / safety

This is the blocker for current executable promotion.

The check executes target/dependency code. Root governance explicitly forbids executing unknown target code merely to inspect it without a separately justified safe responsibility/boundary.

S006 itself did **not** execute the dynamic reproduction.

## C-05 existing owner

No general sandboxed targeted-check executor is currently admitted.

## C-06 recurrence/generality

The reasoning pattern is recurring and valuable, but safe executable support is not established.

## C-07 deterministic baseline

Given a single already-identified discriminating check, selection can be deterministic. Planner value would arise only among several safe checks with different information value/cost/prerequisites.

## C-08 planner-value pressure

Conceptually strong but currently blocked by capability admission, not planner reasoning.

## C-09 learning value

Potential future exposure to:

- experiment design;
- active information gathering;
- sandboxed tool execution;
- differential testing;
- semantic retry/failure classification.

## C-10 claim limit

One differential observation is target/check-specific, not universal compatibility proof.

### R1 disposition

**KNOWN USEFUL OUTSIDE CAPABILITY → DEFER.**

Do not create a current planner action until a separately justified safe execution capability exists.

---

# 9. CAND-06 — persisted-artifact provenance/history acquisition

## C-01 planning uncertainty

Whether a concrete persisted artifact selected after an update was produced under the old dependency environment and contains dependency-owned state relevant to a cross-version persistence boundary.

## C-02 evidence output

Potential evidence includes:

- artifact identity;
- producer run/environment/version provenance;
- consumer selection/reuse identity;
- typed unavailable/unknown history.

## C-03 deterministic inputs/locators

Possible only when an artifact/run/release/model identifier is already known. Arbitrary deployment discovery must not become model-created browsing authority.

## C-04 bounded effect

Public CI/release/artifact metadata may be read-only and bounded. Private deployment history may require credentials/private data and a different authorization boundary.

## C-05 existing owner

No general artifact-history/provenance acquisition owner currently exists.

## C-06 recurrence/generality

S012 proves the applicability concept, not a recurring accessible public acquisition path. More evidence is needed before general capability admission.

## C-07 deterministic baseline

If a single known public artifact/run is already bound, metadata acquisition is straightforward deterministic provider work.

## C-08 planner-value pressure

Potentially valuable only when several provenance sources/paths compete or when the planner must decide whether history is worth acquiring versus stopping/defer. Not yet evidenced.

## C-09 learning value

- temporal/stateful applicability;
- provenance graphs;
- history-aware planning;
- private/public evidence boundaries.

## C-10 claim limit

Unknown artifact history must stay unknown; lack of repository artifact history is not proof that no old artifact exists.

### R1 disposition

**KNOWN USEFUL OUTSIDE CAPABILITY → DEFER.**

A narrower public-artifact-provenance capability may be reconsidered if fresh real cases establish recurrence and planner choice.

---

# 10. CAND-07 — repository-purpose / reproduction-context interpretation

S009 establishes that exact versions can be part of a repository's reproducibility contract independently of technical compatibility.

The useful responsibility is real, but the naive planner action:

```text
read README / requirements comments
```

is not a credible capability boundary.

The hard part is semantic/context interpretation:

```text
what repository contract is declared?
which exact version is part of that contract?
what does the proposed update make inconsistent?
```

That looks more like a typed context-extraction/synthesis responsibility than next-action planning.

A planner may later consume a trusted/grounded context proposition when deciding what investigation matters. It should not gain arbitrary file-selection authority merely to discover purpose.

### R1 disposition

**REJECT AS GENERIC PLANNER ACTION; RETAIN AS SEPARATE CONTEXT/SEMANTIC RESPONSIBILITY HYPOTHESIS.**

Use S009 in R2 as pressure on planning-question/context relevance, not as an excuse to invent `read_repository_purpose`.

---

# 11. CAND-08 — upstream multi-mechanism discovery

S010 establishes:

```text
one dependency transition
→ multiple independently grounded mechanisms
→ distinct target handling states
→ first valid candidate found != discovery complete
```

This is highly relevant to a more powerful UpgradePilot because richer candidate discovery can create the state a planner must later prioritize.

But the primary responsibility is semantic discovery/extraction from upstream/target evidence, not selection among already-admitted investigation actions.

Current product has only a support-drop-specific semantic extractor. A future broader mechanism-discovery model could be valuable, but it would be a separate model boundary with its own grounding/evaluation requirements.

### R1 disposition

**SEPARATE SEMANTIC-DISCOVERY RESPONSIBILITY; NOT A PLANNER ACTION.**

Important architectural implication for later synthesis:

```text
richer semantic candidate discovery
may be a prerequisite for
richer planner action/state value
```

Do not collapse both responsibilities into one generic agent.

---

# 12. CAND-09 — generic pre-bound exact source/config acquisition

The pattern:

```text
unresolved proposition
+ deterministic code already knows exact relevant file
→ read exact file
```

is independently useful, but A1 demonstrates why it is usually a deterministic acquisition primitive rather than planner intelligence.

If several exact pre-bound sources are available and their information value depends on current state, the **selection among those sources** may later be planner-relevant. The underlying exact-file capability remains deterministic provider work.

### R1 disposition

**DETERMINISTIC OWNER BETTER UNTIL REAL MULTI-SOURCE CHOICE IS DEMONSTRATED.**

No generic arbitrary-file action is admitted.

---

# 13. CAND-10 — static↔runtime CI correlation / reusable-workflow completion

Several current proof gaps concern deterministic evidence semantics, not action planning:

- mapping static workflow declarations to runtime step execution;
- reusable-workflow expansion;
- expression/matrix interpretation;
- stronger target job/environment selection.

These are potentially valuable product capabilities, but their core responsibility is evidence acquisition/interpretation correctness. An LLM planner should not substitute for missing deterministic/source semantics.

A planner may later choose **whether** a supported correlation/expansion capability is worth invoking. First the capability itself must have an admitted deterministic evidence boundary.

### R1 disposition

**SEPARATE DETERMINISTIC EVIDENCE RESPONSIBILITY; NOT A PLANNER ACTION AT R1.**

---

## 14. R1 gate result

Three candidates survive for R2, at different confidence:

### Strongest

**CAND-02 — exact-head resolver/currentness/satisfiability evidence**

Why it survives:

- independent evidence class already identified by AUDIT-004;
- current product explicitly does not own it;
- S007 proves a resolver can be useful at one state and redundant at another;
- proof strength is clearly bounded;
- potential for cost/information-value/prerequisite reasoning exists.

### Serious but boundary-unresolved

**CAND-03 — bounded mediated CI/environment-consumption hop inspection**

Why it survives:

- real S005 gap;
- current accepted support intentionally stops before generic task-runner/delegation tracing;
- read-only exact-source form is plausible;
- several possible mediation paths may create meaningful prioritization.

Why it remains uncertain:

- deterministic recursive composition may be the correct owner;
- recurrence beyond the known mediation patterns must be established;
- parser/interpreter capability must remain separate from planner selection.

### Tentative

**CAND-04 — exact target artifact/wheel-environment evidence acquisition**

Why it survives:

- artifact-serviceability is already an admitted mechanism;
- downstream evidence contract exists while acquisition remains incomplete;
- multiple workflow/job/platform witnesses could make source selection non-trivial.

Why tentative:

- current real evidence may support a deterministic target-environment owner better than LLM planning;
- meaningful multi-witness choice has not yet been demonstrated.

---

## 15. R1 rejected/deferred set is itself a finding

R1 rejects the idea that every useful missing responsibility should become an LLM tool.

Current classification:

```text
real capability
!= planner-visible capability

missing evidence owner
!= model should own evidence semantics

semantic discovery
!= investigation planning

safe read-only metadata acquisition
!= arbitrary browsing authority

valuable dynamic check
!= currently admitted executable action
```

This separation is essential if a future planner is to be powerful without becoming a generic agent platform.

---

## 16. R1 proof limits

R1 does not prove that:

- CAND-02/03/04 should be implemented;
- the LLM should select any of them;
- a second action is now justified;
- resolver execution is currently safe/authorized;
- mediation can be generalized across tox/nox/scripts;
- target wheel tags can be established statically in enough cases;
- multi-action planning outperforms deterministic sequencing;
- fresh protected cases exist.

Those are R2/R3 questions.

---

## 17. R1 stopping decision

Stop inventory expansion here.

Reason:

```text
three materially different candidates survived the admission gate
+
several attractive but incorrectly-owned candidates were explicitly rejected/deferred
+
more brainstorming without deterministic-baseline comparison would add breadth, not discriminating evidence
```

If `MEMORY.md` continues to select this delegated research, proceed to **R2 planner-value discrimination** on CAND-02, CAND-03, and CAND-04 only.
