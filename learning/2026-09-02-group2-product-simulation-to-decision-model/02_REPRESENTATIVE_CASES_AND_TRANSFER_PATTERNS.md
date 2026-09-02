# Group 2 — Representative Product-Simulation Cases and Transfer Patterns

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@8f25bcb4e158f4f6e779ce63c264957f97e44771`  
**Roadmap responsibility:** Group 2 from `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** representative case/transfer companion; not a scenario catalog, benchmark oracle, product-state owner, or current implementation proof  
**Target depth:** understand the individual historical cases operationally; **must master / own** the reusable reasoning distinctions they pressure-tested  
**Companion:** [`01_PRODUCT_SIMULATION_PRESSURES_AND_DECISION_MODEL_EVOLUTION.md`](01_PRODUCT_SIMULATION_PRESSURES_AND_DECISION_MODEL_EVOLUTION.md)

This note teaches Group 2 through real cases.

The goal is **not** to memorize S001–S012. The goal is to look at a new dependency-update case and ask the right technical questions because you understand what these cases taught.

---

## 1. How to read a simulation case

For every case, separate five layers:

```text
1. CASE FACTS
   exact dependency transition + exact target/revision + observed evidence

2. PRESSURE
   what naive shortcut or missing responsibility the case exposed

3. BOUNDED CONCLUSION
   what the available evidence was sufficient to establish

4. NON-CLAIMS
   what remained unresolved / outside scope

5. TRANSFER PATTERN
   the reusable reasoning shape that survives beyond this package/repository
```

Do not learn the wrong lesson by copying the historical action alone.

Example:

```text
S004 → merge_after_normal_review
```

The lesson is **not**:

```text
patch + green CI → merge
```

The lesson is:

```text
confirm the baseline's authority-critical assumptions
→ if the exact changed responsibility is covered
→ and no material unresolved question remains
→ stop instead of manufacturing extra investigation
```

That distinction is the purpose of this artifact.

---

# Part I — The original baseline/full-investigation contrasts

## 2. S001 — concern can disappear after exact target applicability evidence

### Case shape

Historical S001 involved Soup Sieve `2.6 → 2.8.4` in Pydantic as a transitive documentation-tooling dependency.

The broader historical case contained advisory/support and documentation-path evidence. Later stronger product work reused S001 for one precise support-drop mechanism:

```text
upstream Soup Sieve 2.8 drops Python 3.8 support
+
target Pydantic revision declares requires-python >=3.10
```

### Naive shortcut under pressure

```text
upstream dropped Python support
→ compatibility concern
→ investigate/block broadly
```

### Better reasoning

First formulate the exact question:

```text
Does the dropped Python 3.8 support intersect the exact target's supported Python range?
```

Then use target-owned evidence:

```text
upstream affected line = Python 3.8

target declared line = Python >=3.10

intersection = none
```

For that candidate:

```text
activation/applicability proposition refuted
→ concern not applicable to declared target range
→ deeper work for this path has no value
```

### What this did not prove

It did not prove:

- the entire dependency update is safe;
- every other Soup Sieve mechanism is irrelevant;
- all runtime/deployment environments exactly follow the declaration;
- candidate discovery across the whole transition is complete.

### Transfer pattern

```text
upstream support/environment change
→ exact affected environment condition
→ exact target support/environment evidence
→ intersection / non-intersection / unresolved
→ investigate only if the candidate remains material
```

### Concept carried forward

**Upstream change != target impact.**

Closing one candidate/path does not close the whole dependency transition.

---

## 3. S002 — direct dependency does not mean directly exercised behavior

### Case shape

S002 involved HTTPX `0.27.2 → 0.28.1` in a Kubernetes Dashboard token API repository.

The target directly declared HTTPX, but the material compatibility path was adapter/framework-mediated. Docker install/build evidence existed while relevant Python tests did not provide the required exact behavior coverage.

### Naive shortcuts under pressure

```text
direct dependency
→ direct use established
```

```text
build/install passed
→ changed behavior covered
```

```text
green CI
→ compatibility established
```

### Better reasoning

The material question was closer to:

```text
Does the exact target adapter/runtime path invoke the HTTPX behavior changed by the transition,
and is that path actually exercised by admitted evidence?
```

This requires separating:

```text
dependency declaration
→ possible target relationship

adapter/framework path
→ actual exposure mechanism

activation condition
→ changed behavior reached

CI/test evidence
→ coverage of that exact path
```

### Bounded outcome

The historical full simulation retained a targeted-check action because the relevant behavioral path remained insufficiently covered.

### What this did not prove

- that HTTPX 0.28.1 was definitely incompatible;
- that every direct dependency needs a targeted check;
- that direct imports are required for target relevance.

### Transfer pattern

```text
upstream API/behavior change
→ direct OR mediated target path
→ affected behavior activation
→ exact behavior coverage
→ targeted check only when the unresolved path can be discriminated
```

### Concept carried forward

**Presence/directness != exposure != activation != coverage.**

---

## 4. S003 — failing CI requires causal decomposition

### Case shape

S003 studied a TypeScript `5.9.3 → 7.0.2` update in `event-handler-loader`.

Observed public evidence included:

- `npm ci` failed before ESLint executed;
- retained TypeScript-ESLint `8.65.0` declared support for TypeScript `>=4.8.4 <6.1.0`;
- proposed TypeScript `7.0.2` lay outside that range;
- a same-base adjacent Dependabot PR passed installation/linting in a comparable environment.

The historical attribution was strongly supported as update-caused at the dependency-tree/installability layer, with explicit limits because exact local reproduction was unavailable.

### Naive shortcuts under pressure

```text
red workflow
→ update caused failure
```

```text
workflow named Linters
→ ESLint failed
```

```text
unrelated jobs passed
→ failed responsibility is less concerning
```

### Better reasoning

Decompose the observation:

```text
workflow
→ job
→ exact failing step
→ command
→ dependency relationship
→ exact versions/ranges
→ target install path
→ competing causal explanations
```

Then compare evidence for alternatives.

The result can be strong enough for the bounded action without claiming perfect causal certainty.

### What this did not prove

- the exact omitted npm diagnostic tail;
- identical failure under every npm/runner environment;
- permanent TypeScript-7 incompatibility;
- that dynamic local reproduction is always required.

### Transfer pattern

```text
observed failure
→ localize exact failed responsibility
→ identify mechanism/activation predicate
→ compare causal alternatives
→ preserve limiting evidence/confounders
→ calibrated attribution
```

### Concepts carried forward

```text
red CI != cause
```

```text
successful/failed broad workflow != exact responsibility semantics
```

```text
calibrated strong attribution can be useful without pretending certainty
```

---

## 5. S004 — stopping is a technical responsibility

### Case shape

S004 studied pytest `9.0.2 → 9.0.3` in glyphsLib as a deliberate **baseline-sufficient control**.

Evidence established:

- one pinned development dependency changed;
- tox installed the changed requirements;
- exact-head ordinary pytest responsibilities passed across relevant Python/OS cells;
- a regression workflow reinstalled the proposed requirements and passed a direct pytest regression command;
- official upstream material described 9.0.3 as a bug-fix/drop-in replacement;
- no material contradiction or unresolved decision question remained.

Both baseline and full simulation selected:

```text
merge_after_normal_review
```

### Naive shortcut under pressure

The dangerous mistake here is not excessive optimism. It is excessive investigation:

```text
we have more tools available
→ therefore run more checks
```

### Better reasoning

Precommit the authority/sufficiency questions and stop when they are answered:

```text
changed dependency consumed by owning path?
exact proposed version exercised?
relevant checks passed?
upstream evidence coherent?
material contradiction/gap left?
```

If all close and no new discriminating question exists:

```text
NO FURTHER INVESTIGATION
```

is correct.

### What this did not prove

```text
patch + green CI = safe
```

It proved that a small bounded authority-confirmation layer can be enough **for this exact case/question**.

### Transfer pattern

```text
baseline gives plausible action
→ verify its authority-critical assumptions
→ no material unresolved proposition
→ deeper stages non-activated
→ stop
```

### Concept carried forward

**More investigation != better decision support.**

Non-activation is a result, not missing work.

---

## 6. S005 — exact target evidence can overturn conservative keyword caution

### Case shape

S005 studied pytest `9.0.3 → 9.1.1` in ModelArrayIO.

The transparent baseline saw:

- minor update;
- passing CI;
- direct dependency;
- literal breaking/removal/deprecation wording.

It selected:

```text
run_targeted_checks
```

The full evidence instead established:

- exact pytest 9.1.1 lock consumption by the test path;
- exact matrix executions passed;
- the upstream breaking condition depended on `--doctest-modules` plus a specific fixture pattern;
- the target did not activate that condition;
- named deprecated surfaces were absent or used in supported form;
- no remaining target-specific uncertainty identified a useful check.

Full action:

```text
merge_after_normal_review
```

Classification:

```text
baseline_wrong_action
```

### Naive shortcut under pressure

```text
release notes say breaking/deprecated
→ targeted check required
```

### Better reasoning

```text
upstream statement
→ mechanism
→ activation predicate
→ target config/source/API surface
→ exact execution coverage
→ unresolved question OR closure
```

### What this did not prove

- caution language is generally unimportant;
- negative search alone proves absence;
- pytest 9.1.1 is universally safe.

### Transfer pattern

**Turn prose into candidate-specific activation propositions, then test those propositions against the exact target.**

### Concepts carried forward

```text
keyword signal != applicability
```

```text
targeted check requires a named unresolved target question
```

```text
full evidence may legitimately weaken a cautious action
```

---

# Part II — Investigation-selection pressure

## 7. S006 — when a bounded dynamic experiment is worth doing

### Case shape

The S006 qldebugger/Pydantic pressure involved an upstream Pydantic validator behavior change: `TypeError` handling changed across the major-version boundary.

The target had a Pydantic validator that intentionally raises `TypeError` for a non-string handler.

Static evidence could establish:

- the upstream behavior change;
- the exact target validator/framework integration;
- the relevant branch;
- that visible nearby tests did not settle the exact changed behavior.

### Candidate checks

Weak/non-discriminating options included:

- import-only check;
- valid-handler check;
- install-only resolution;
- broad unconstrained full-suite run.

The discriminating check was:

```text
bounded old/new differential reproduction
with the exact implicated branch/input
```

### Why execution was justified

Because plausible outcomes could materially change the owned behavior proposition.

```text
static evidence reaches its limit
+
exact behavioral branch can be activated safely/boundedly
+
old/new contrast has interpretable outcomes
→ select dynamic check
```

### Transfer pattern

Dynamic execution is not “stronger” by category. It is valuable when it uniquely discriminates the proposition.

---

## 8. S007 — when a previously sensible check should be cancelled

### Case shape

S007 involved BiomedParse with a proposed Torch-family change.

At admission, candidate investigations such as exact wheel metadata and a resolver dry-run were reasonable.

Then stronger authoritative source/build evidence established that retained TorchVision 0.21 release behavior pinned the corresponding Torch 2.6-family dependency while the target proposed `torch==2.8.0`.

The permitted Torch-version sets had no intersection for the owned package-family proposition.

### The key transition

```text
T1: resolver run could discriminate

new evidence arrives

T2: proposition deterministically refuted

→ resolver run becomes corroborative/redundant
→ do not execute merely because it was planned
```

### Transfer pattern

```text
candidate investigation value
= function(current admitted evidence state)
```

not:

```text
candidate investigation value
= fixed at planning time
```

### Concept carried forward

**Plan/check generation != execution obligation.**

Every newly admitted material observation can change which investigation is worth doing next.

---

## 9. Three different “stop” meanings

S006/S007 and related pressure cases help distinguish three endpoints.

### Stop A — resolved

```text
proposition settled
→ no further check needed
```

S007 is the clearest example.

### Stop B — path pruned

```text
necessary proposition refuted
→ downstream branch cannot change path result
→ prune
```

S001-style Python-support non-intersection is a clean example.

### Stop C — unresolved but no justified investigation remains

```text
material proposition still unresolved
+
remaining checks lack scope / authority / discrimination / proportionality
→ preserve unresolved
→ stop
```

Historical-environment pressure cases demonstrate why this endpoint is necessary.

These may share presentation language such as “no next check,” but they must not share the same knowledge meaning.

---

# Part III — Later transfer cases widen the model

## 10. S008 — local mechanism closure does not prove transition discovery completeness

The later candidate-discovery pressure test reused S008 as an artifact-serviceability example.

Its owned narrow question concerned a real OpenCV package-artifact transition where an old CPython-3.6 Linux wheel path existed while the proposed release lacked the same compatible binary path and retained source-distribution fallback.

For that narrow mechanism, exact package artifact evidence was enough.

A native source build was correctly pruned because it would answer a different consequence question.

But:

```text
S008 mechanism question resolved
!= entire OpenCV transition fully discovered
```

### Transfer pattern

**Candidate investigation stopping is local to the owned candidate/question.**

A broader statement such as “no other material target impact exists” requires a separate candidate-discovery coverage argument.

Detailed artifact-serviceability implementation belongs to Group 7.

---

## 11. S009 — material repository context is not automatically a technical candidate

The candidate-discovery pressure test used S009 to show a different coverage plane.

S009 established a repository reproducibility/provenance inconsistency around a pandas transition while separate technical compatibility/numerical-result questions remained independent.

The lesson is:

```text
material repository-purpose/context finding
!= mechanism-specific technical impact candidate
```

A mature decision system may need both, but forcing every useful context fact into the same candidate taxonomy would destroy meaning.

### Transfer pattern

Keep responsibility boundaries even when multiple evidence classes are decision-relevant.

---

## 12. S010 — first candidate found does not mean discovery is complete

### Case shape

S010 used a real NumPy requirement broadening:

```text
numpy >=1.26,<2.0
→ numpy >=1.26,<3.0
```

in a transitive runtime area.

It grounded at least two materially distinct mechanisms:

- one around a NumPy-2 `numpy.lib.pad` surface with an existing `<2` target guard that the proposal removed;
- another around a different `np.vstack` compatibility mechanism for which the target already had a local compatibility shim.

### Naive shortcut under pressure

```text
find one valid NumPy compatibility candidate
→ transition understood
```

### Better reasoning

```text
DISCOVERY
→ identify materially distinct mechanisms

THEN

CANDIDATE-SPECIFIC EVALUATION
→ evaluate target relation / activation / mitigation for each
```

One candidate being mitigated does not make it disappear from discovery history.

### Other useful distinction

The PR broadened an allowed range rather than replacing one exact old version with one exact proposed version.

```text
constraint broadening
!= exact version replacement
```

Do not hallucinate one exact resolved NumPy-2 version merely to fit a simpler transition model.

### Transfer pattern

```text
one dependency transition
can produce multiple mechanism-specific candidates
with different target states
```

---

## 13. S011 — optional dependency declaration, environment formation, activation, and behavior coverage are separate

### Case shape

S011 studied NumPy inside Dictare's optional `[mlx]` dependency family.

The repository supported an Apple-Silicon MLX path, but inspected standard and macOS workflows installed `.[dev]`, not `.[mlx]`.

### Naive shortcuts under pressure

```text
optional dependency declared
→ dependency installed
```

```text
macOS workflow exists
→ Apple-Silicon MLX environment covered
```

```text
workflow passes
→ optional stack compatible
```

### Better proposition chain

```text
OPTIONAL ENVIRONMENT FORMED?
extra actually installed/resolved?
↓
RUNTIME ACTIVATION CONDITIONS SATISFIED?
platform + architecture + package availability + configuration/selection?
↓
BEHAVIOR PATH EXERCISED?
relevant runtime behavior tested?
```

S011’s activation shape included multiple conjunctive conditions. That demonstrates compositional applicability without requiring a universal Boolean engine.

### Transfer pattern

```text
declaration
!= environment formation
!= runtime activation
!= behavior coverage
```

### Concept carried forward

CI evidence is proposition-relative. A workflow can be strong evidence for one question and useless for another.

Detailed CI/environment implementation belongs to Groups 5 and 8.

---

## 14. S012 — current revision can be necessary but still insufficient target context

### Case shape

S012 studied scikit-learn `1.7.2 → 1.8.0` in a Freqtrade/FreqAI persistence path.

The target can persist model/feature/label pipeline state and load it in a later run. Such state may contain scikit-learn-owned objects.

Authoritative upstream evidence established that persisted scikit-learn state is not supported for loading under a different scikit-learn version.

### Naive shortcuts under pressure

```text
current source + current dependency environment
→ complete target context
```

```text
fresh install/test passes
→ old persisted artifacts compatible
```

```text
no artifact history found in repository
→ no old artifact exists
```

### Better reasoning

For this mechanism, applicability may require two different dependency-version identities:

```text
producer environment/version
→ persisted artifact
→ consumer environment/version
```

So:

```text
fresh-state compatibility
!= persisted-state compatibility
```

The exact current repository revision remains necessary, but target-relevant state can extend outside the repository tree when the application intentionally persists and reuses it.

### If dynamic testing were later needed

The discriminating check would need to instantiate the candidate’s actual activation conditions:

```text
artifact created under exact old dependency environment
→ preserved
→ loaded under exact proposed environment
→ observe result
```

A fresh-state test would answer the wrong proposition.

### Transfer pattern

**Investigation setup must reproduce the mechanism-specific activation boundary, not merely execute nearby code.**

---

# Part IV — Cross-case transfer model

## 15. Case-to-concept matrix

| Case / pressure | Main reusable lesson | Dangerous shortcut rejected |
|---|---|---|
| S001 | target applicability can refute a concerning upstream mechanism | upstream change ⇒ target impact |
| S002 | mediated exposure and exact behavior coverage matter | direct dependency / green build ⇒ behavior covered |
| S003 | failing CI requires causal decomposition | red CI ⇒ update caused failure |
| S004 | stop when authority-critical questions close | more investigation ⇒ more quality |
| S005 | exact target evidence can overturn coarse caution | breaking keyword ⇒ targeted check |
| S006 | dynamic differential execution can uniquely discriminate behavior | dynamic always overkill / full suite always best |
| S007 | investigation value changes as evidence changes | planned check ⇒ must execute |
| S008 | local candidate closure does not establish transition discovery breadth | candidate resolved ⇒ transition understood |
| S009 | context/provenance can matter outside technical-candidate taxonomy | every material finding ⇒ technical candidate |
| S010 | one transition can contain multiple independent mechanisms | first candidate found ⇒ discovery complete |
| S011 | environment formation precedes activation and behavior coverage | optional declaration / platform label ⇒ coverage |
| S012 | applicability may depend on historical persisted state | current revision/environment ⇒ all active target state |

This table is a learning map, not an accepted universal scenario taxonomy.

---

## 16. One new case: the reasoning sequence to apply

When you meet a new dependency-update PR, do not start with:

```text
Is this risky?
```

Use a more disciplined sequence.

### Step 1 — freeze identity

```text
What exact PR, target revision, dependency transition, proposal shape and relevant environment/context are we reasoning about?
```

### Step 2 — identify a mechanism, not a vague topic

```text
What changed upstream or in the dependency relationship?
What possible target consequence follows through which relationship?
```

Form a candidate without self-authorizing its components.

### Step 3 — derive candidate-specific propositions

Examples:

```text
Is the affected API actually reached?
Is the optional environment formed?
Does the target support the dropped Python line?
Does the exact old artifact path disappear?
Is the historical persisted artifact selected after update?
```

### Step 4 — classify current proposition evidence

```text
established?
refuted?
unresolved?
conflicted?
```

Do not turn missing evidence into refutation.

### Step 5 — ask the right coverage question

```text
Do I have enough evidence coverage for this proposition?
Did I model the material alternative paths?
Am I making a broader transition-level claim that also needs candidate-discovery coverage?
```

### Step 6 — if non-final, find the discriminating target

```text
What exact missing fact/observation could materially change the state?
```

### Step 7 — compare checks by evidence value first

A useful check needs adequate:

- state-changing/discriminating potential;
- scope/context match;
- authority/provenance;
- interpretable outcomes;
- supported execution/acquisition boundary.

Then use cost/risk/latency/invasiveness to choose among adequate options.

### Step 8 — re-evaluate after every material observation

```text
Does the previously planned check still have value?
Did a path close?
Did a new mechanism appear?
Did the candidate need refinement/supersession?
```

### Step 9 — stop correctly

Stop can mean:

- resolved;
- path pruned;
- unresolved but no justified check remains.

None of these means “the whole update is safe.”

---

## 17. Transfer drills

These are not quizzes for certification. They are quick reasoning checks.

### Drill A — green CI but wrong environment

A dependency changes inside optional group `gpu`, while CI installs only the default group.

Do not say:

```text
green CI → compatible
```

Ask:

```text
Was the gpu environment formed?
If not, what proposition does green CI actually support?
```

S011 is the transfer anchor.

### Drill B — scary release note, irrelevant activation

Upstream removes behavior enabled only by config flag `legacy_mode=true`. Exact target configuration disables it.

The right move is not generic extra testing. First establish whether alternative activation paths exist and whether target evidence is complete enough for the proposition.

S005/S001 are the transfer anchors.

### Drill C — a planned test becomes redundant

You plan a resolver run, then authoritative package metadata proves the relevant version constraints have empty intersection.

Recompute investigation value. Do not run the resolver merely for procedural completeness.

S007 is the transfer anchor.

### Drill D — first candidate looks severe

You find one clear ABI/package-artifact problem in a large dependency transition.

If your final claim is only about that candidate, investigate it. If your final claim is “no other material concern exists,” you now have a separate candidate-discovery coverage obligation.

S008/S010 are the transfer anchors.

### Drill E — fresh tests pass but users may load old state

A library update passes clean training/tests, but the application reloads serialized models created months earlier.

Fresh-state success does not answer cross-version persisted-state compatibility.

S012 is the transfer anchor.

---

## 18. What not to memorize or generalize

Do not turn these cases into rules such as:

- transitive dependency is low risk;
- direct dependency is high risk;
- patch update should merge;
- major update should block;
- exact matrix green means safe;
- peer conflict always requires a resolver run;
- dynamic testing is superior to static evidence;
- optional dependency always needs dedicated CI;
- persisted artifacts always require migration;
- every transition needs exhaustive candidate discovery;
- every mechanism needs its own permanent parser/type/enum.

The project repeatedly learned the opposite lesson:

> **Responsibility, proposition, evidence scope, activation, and proof boundary decide what is needed. Case labels do not.**

---

## 19. Relationship to current accepted semantics

The historical cases above are pressure evidence.

The current semantic owner is:

- `../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`

Use it when asking:

```text
What must current admitted impact/applicability/investigation reasoning mean?
```

Use product-simulation history when asking:

```text
Why was this distinction needed?
Which real cases broke the simpler model?
What alternative or shortcut failed under pressure?
```

Do not use an old case action to override the current specification or current implementation evidence.

---

## 20. Existing frozen learning material to reuse

For deeper concept study:

- [`../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md)

For the detailed historical A→C reconciliation:

- [`../2026-08-10-product-decision-model-a-b-c-mastery-note.md`](../2026-08-10-product-decision-model-a-b-c-mastery-note.md)

For current Group 1 evidence/authority vocabulary:

- [`../2026-09-02-group1-product-thesis-evidence-authority-model.md`](../2026-09-02-group1-product-thesis-evidence-authority-model.md)

This Group 2 package intentionally references rather than rewrites those snapshots.

---

## 21. Depth map

### Must master / own

You should be able to take an unfamiliar case and distinguish:

- upstream mechanism;
- target relationship/exposure;
- activation condition;
- possible consequence;
- proposition state;
- evidence scope/authority;
- evidence vs path-model vs candidate-discovery coverage;
- discriminating target;
- useful vs merely relevant investigation;
- justified stopping reason;
- local candidate closure vs broader transition claim.

### Understand operationally

Know what each representative S001–S012 case contributed and be able to explain why at least S004, S005, S006, S007, S010, S011, and S012 require different reasoning.

### Recognize / lookup-level

- exact PR/repository/run IDs;
- exact scenario artifact layouts;
- package-specific API details not needed for the transfer pattern;
- historical validation counts.

### Deliberately deferred

- current source implementation of these semantics — Group 9;
- exact dependency/environment implementation — Groups 4–6;
- artifact serviceability — Group 7;
- CI/workflow implementation — Group 8;
- agentic investigation orchestration — Group 12.

---

## 22. Fast relearning route

If returning later:

1. Read the matrix in Section **15**.
2. Re-read **S004 + S005** to remember sufficiency versus action revision.
3. Re-read **S006 + S007** to remember why investigation value is proposition- and state-dependent.
4. Re-read **S010–S012** to remember that the model transfers beyond the first Python-support/API cases.
5. Trace the nine-step new-case reasoning sequence in Section **16** without looking at the examples.
6. Return to the companion Note 1 only if you need the full historical pressure-to-model evolution.

---

## 23. Ownership / transfer questions

1. S001 closes one Python-support concern. Why can’t that become “no material update impact”?
2. In S002, why is a direct dependency declaration weaker than evidence that the affected adapter/runtime path is actually exercised?
3. In S003, why did same-base comparison evidence strengthen causality without creating absolute proof?
4. What exactly makes S004 a stopping case rather than a “patch updates are safe” case?
5. In S005, what gave the full investigation authority to remove the baseline’s targeted-check requirement?
6. Why was differential execution a good choice in S006 but resolver execution unnecessary in S007?
7. What coverage question does S010 add beyond candidate-specific applicability?
8. Why does S011 require “environment formed?” before “behavior covered?”
9. Why can S012 require two dependency-version identities in the same applicability question?
10. Pick any new dependency-update scenario and identify one observation that is relevant but not discriminating.

---

## 24. Primary evidence anchors

Early comparative cycle:

- `../../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`
- `../../product-simulation/SCENARIO_COVERAGE.md`
- `../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`
- `../../product-simulation/S003_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S004_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S005_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`

Decision-model rebase / investigation pressure:

- `../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`
- `../../product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md`
- `../../product-simulation/CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`
- `../../product-simulation/CONVERSATION_C_HANDOFF_S007_2026-08-09.md`
- `../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`

Later transfer anchors:

- `../../product-simulation/S010_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S011_POST_CASE_SYNTHESIS.md`
- `../../product-simulation/S012_POST_CASE_SYNTHESIS.md`

Current accepted semantics:

- `../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`

Historical audit evidence:

- `../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`

The audit is referenced as already-recorded historical pressure/reconciliation evidence. No new Audit operation was required for Group 2.