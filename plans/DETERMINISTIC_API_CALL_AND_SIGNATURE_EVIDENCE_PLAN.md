# Deterministic API call and signature evidence plan

**Status:** Draft for discussion and decision. Plan authoring does not authorize execution, implementation or product adoption.  
**Responsibility:** qualify, design and, after separate activation, implement and evaluate bounded source-backed evidence connecting explicit Python call arguments with qualified callable signatures.  
**Parent:** [API change and target exposure feasibility plan](UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md). This child owns the structural call/signature increment; the parent retains ordinary trial acquisition, broader interpretation/exposure, independent admission and product-promotion gates.  
**Live selection and results:** [MEMORY.md](../MEMORY.md) alone. Dated execution and design reasoning belong in the selected working-memory record.

**Concrete design for review:** [reusable caller/signature experiment contract](../working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md). It specifies source/fact reuse, supported syntactic binding, curated versus ordinary correspondence, receiver premises, saved consumer/retention, finite limits and broader proof. It is a proposed experiment contract, not product adoption or implementation evidence.

## 1. Product purpose and bounded outcome

UpgradePilot must help a maintainer understand the effect of a dependency update on the exact target repository. A release-note statement or a successful CI job alone cannot establish that effect. A useful API explanation needs a justified relationship between a relevant caller and the changed interface.

The consumer question for this increment is:

> What arguments does this captured caller explicitly supply, what does the qualified captured callee accept, and which source, dispatch or version premise prevents applying that relationship to the actual target?

The preferred deliverable is one experiment-local, offline-readable evidence result with both machine-readable facts and a concise human view. It must expose source locations and limitations, distinguish an observed fact from a conditional relation, and make a real retained example easier to verify. Its result can be useful while the actual installed target framework remains unresolved.

The complete product responsibility still includes change meaning, indirect/wrapper paths, actual version resolution, environments, runtime effects and useful maintainer decisions. This increment covers explicit source structure and justified conditional relationships. It does not replace that broader responsibility or become complete API compatibility analysis because one mismatch is detected.

The narrowing is justified by demonstrated false source assertions and reusable existing AST/binding machinery. Dynamic/runtime questions remain temporarily outside this increment's positive proof, with explicit unresolved premises. Re-enter them only when a material consumer case identifies the missing proposition and an admitted method can resolve it proportionately.

## 2. Governing owners and evidence

Apply, rather than redefine:

- [Project Charter](../PROJECT_CHARTER.md): supported public Python dependency-review responsibility and claim limits.
- [Core specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md): identity, evidence boundaries and JUST-001 through JUST-005; earliest sufficient ownership and justified retention.
- [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md): technical candidates, candidate-specific applicability, coverage and permitted deterministic/semantic effects.
- [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md): real input extraction, variation and no fixture-specific semantic answers.
- [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md): declared-source bases, examination eligibility, proposal limits and experiment-first adoption boundary.
- [Naming Clarity](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md), [Operating Guide](../OPERATING_GUIDE.md) and [Security](../SECURITY.md): representation, learning/work method, untrusted source and execution safeguards.
- [Report/usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md): independent usefulness remains a separate evaluation, not a consequence of structural correctness.

Entry evidence includes the [source-access task review](../working-memory/evidence/2026-10-23-source-access-task-review/REVIEW.md) and [completed negative interpretation comparison](../working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md). They distinguish missing normal target premises from interpretation failures on richer delivered sources. These are exposed development observations, not independent utility or general reliability estimates. Do not rerun, repair or regrade their frozen results as part of this increment.

## 3. Reuse and simplest baseline

| Existing responsibility | Owning implementation | Consequence for this increment |
| --- | --- | --- |
| Exact target inventory, files, declarations and AST preparation | [api_target_context.py](../experiments/api_target_context.py) | Reuse source identity, acquisition/parse problems and bounded file selection; do not depend on successful CI or add a second target acquirer |
| Ordered/scoped imported origins, traces, explicit call keyword names and positional counts | [api_python_bindings.py](../experiments/api_python_bindings.py) | Inspect existing ReferenceFact/BindingAssessment before extending; do not create another keyword/import analyzer |
| Version-specific adapter examination and sampled-source limitations | [api_adapter_exploration.py](../experiments/api_adapter_exploration.py) | Preserve sample selection and association; a sample is not the installed version and does not exhaust a range |
| Ordinary experimental PR composition and manifests | [api_target_context_smoke.py](../experiments/api_target_context_smoke.py), [api_change_interpretation_trial.py](../experiments/api_change_interpretation_trial.py) | Select one consumer seam; ordinary trial reachability is separate from the normal product CLI and from curated source calibration |
| Retained source identity and bounded reading | [source_access.py](../src/upgradepilot/workspace/source_access.py) and existing retained trial readers | Check applicable source access/recovery before adding retention; a catalog's text and scope are frozen evidence, not canonical runtime state |

The first baseline is the existing source view plus existing call/binding facts, with the relationship reconstructed by the reviewer. Measure the bounded evidence burden and missing result against that baseline on the same source. If those facts already answer the consumer question adequately, prefer reuse or a small projection over a new analyzer.

The preferred alternative, if needed, is a small AST-derived signature/argument-relation extension. A new prompt/model trial is not a prerequisite or selected alternative implementation here. Importing the target for inspect.signature, executing constructors or installing dependencies would answer a different runtime question and is outside this plan's source-only boundary. A general static-analysis framework or solver needs independently demonstrated pressure; it is not the starting design.

## 4. Scope and permitted effects

The planned evidence path is:

```text
qualified retained source and declared association
→ existing AST and ordered/scoped call facts
→ qualified explicit signature facts where absent from current output
→ justified caller/callee source correspondence
→ bounded argument/signature relationship with missing premises
→ one saved experimental result and human-readable view
```

Keep these three levels separate in every consumer:

1. **Observed source fact:** a particular call supplies named keyword K; a complete captured signature declares particular parameter kinds or a **kwargs receiver.
2. **Conditional structural relation:** under an explicit caller/callee correspondence, this argument is or is not accepted by that signature under the admitted Python binding rules. An incompatible keyword can be diagnosed without claiming every other argument is valid.
3. **Actual target effect:** requires actual target/version/dispatch/activation evidence. It remains unresolved when that premise is missing; this increment does not manufacture it.

An absence claim requires adequate coverage of its exact source unit. Missing **kwargs or an omitted parameter cannot be inferred from a truncated signature, a text search or an excerpt whose completeness is unqualified. Seeing **kwargs permits keyword reception at that boundary; it does not prove the receiving implementation accepts its meaning or forwards it safely.

No source relationship becomes installed-package proof, successful execution, complete impact coverage, compatibility or action permission. Retain attribution and source-association strength even when the syntax transformation is deterministic. Different repositories/versions naturally have different revisions; validate each role and the correspondence, not an invented requirement that every source share one SHA.

## 5. Decisions to settle before implementation

The recommendations below guide qualification. They are not an already accepted schema or supported-construct contract.

| Decision | Recommended starting point | Required resolution |
| --- | --- | --- |
| Consumer and baseline | One offline experimental structured result and concise view beside existing facts/source | Name the exact caller/entry point and a real reviewer task; show why existing output alone is insufficient |
| Source qualification | Exact retained file bytes through existing readers, with role/revision/path/hash and coverage | Verify recoverable bytes and source-unit completeness; classify real excerpts separately; no invented omitted code |
| Signature representation | AST-defined parameter names/kinds, required/default presence, *args/**kwargs and source location | Settle binding of functions, constructors, bound methods and implicit receiver arguments; avoid executing defaults or annotations |
| Argument representation | Reuse existing keywords/counts/binding facts; extend only for missing discriminating structure | Explicitly distinguish positional arguments, * expansion, named keywords, ** expansion and duplicate/positional-only restrictions |
| Source correspondence | An explicit evidence-backed relation with provenance and unresolved dispatch/version premises | Distinguish a deliberately supplied source pair in curated mode from a relationship discovered in the ordinary trial; no answer-path injection |
| Unsupported constructs | Preserve specific unresolved premises while retaining independently valid facts | Decide how decorators, wrappers, inheritance/MRO, super(), dynamic mutation and incomplete snippets affect each proposed conclusion |
| Serialization and recovery | Reuse the experimental manifest/saved-result boundary if it fits | Define method/format identity, source references, unsupported historical fields, recovery validation and compatibility before changing writers/readers |
| Placement and authority | Experiment-local cohesive extension and tests; product imports only where contracts match | Justify each new field/validation through producer → consumer; do not create a generic truth-state framework or duplicate native domain evaluators |

Do not parse ellipsis-filled excerpts by silently filling bodies or signatures. A source-derived fragment can be examined only with a declared extraction/remapping method and adequate coverage for its proposition; otherwise preserve a useful limitation. Do not equate a literal spelling such as super().__init__ with a resolved target without sufficient class/dispatch evidence. A curated pairing can support a conditional comparison while actual dispatch remains unknown.

Before coding, record the selected construct set, result contract, consumer, limits and alternatives/disposition in dated design evidence referenced from this plan. Promote to a specification or ADR only if the decision actually changes stable product semantics or a consequential durable method. Otherwise retain an experiment-local design under existing owners. Resolve material scope/proof changes with Ali rather than silently shrinking the task to the easiest passing fixture.

Use the linked concrete design to review these decisions as one coherent contract rather than reopen each as an abstract questionnaire. Its two scopes distinguish explicit-keyword reception from complete syntactic binding, and retain source/receiver/dispatch/version premises independently. Exact source readiness already established in the [dated retained inspection](../working-memory/evidence/2026-10-26-explanation-source-and-analysis-gaps/retained-source-inspection.json) may be reused after checking material identities; do not repeat qualification from zero or treat historical checks as new execution.

## 6. Ordered execution and decision boundaries

### Qualify the sources and existing result baseline

When this investigation is activated, inspect retained HTTPX old/proposed constructors, older/newer Starlette calls and target-context evidence through their actual readers. Freeze the chosen inputs, source roles/hashes, coverage and current method identities before new result inspection. Public review pointers locate evidence; they are not substitutes for readable source bytes. Keep copied PR prose, historical manually selected excerpts, richer retained source packets and normal captures distinguishable.

Build a small source-readiness and baseline assessment: available evidence, unsupported units, existing reusable facts, missing relation, concrete consumer and discriminating expected/forbidden conclusions. Expected conclusions belong to review material, not producer inputs. No new acquisition follows automatically if source qualification fails. Return a reuse, useful extension, narrower justified scope, defer or stop recommendation.

### Settle and review the action contract

Resolve §5 into one bounded contract. Choose the consumer and supported constructs together; do not write a signature inventory without its use or assume complete static dispatch. State how every material unknown affects a conclusion and which facts remain useful despite it. Define exact local resource ceilings and the result/omission behavior before execution, not after a failure.

The design-review outcome must include one thin example of the intended human/machine result with its source pointers and target limitation. A hand-authored example is a design illustration, never executable evidence. Discuss this contract with Ali before the separate implementation decision. This plan's preparation does not count as completion of this source-qualification/design step.

### Implement the smallest complete evidence-to-consumer increment

Only after implementation is separately authorized, inspect the current source/tests again and apply the admitted Build procedure. Reuse existing parsing/binding/source/manifest owners. Add only missing facts, correspondence assessment, conditional relation and the chosen view/recovery route needed by the accepted contract. Coordinate producer, writer, reader and consumer changes as one responsibility; internal callability alone is not a public contract.

Default modification boundary: experiments/ and experiments/tests/, plus directly necessary dated evidence and documentation. A small new experiment module is justified only if existing owners cannot coherently contain the new responsibility. Product runtime must not import experiments. A reusable product-provider change, normal report schema change, native Workspace family or product migration requires its own admitted responsibility rather than expansion of this implementation.

### Verify behavior and expose the real-case result

Run the focused checks in §7, then the relevant inclusive experiment suites. Freeze new outputs separately from all historical captures/results. Render and reopen the result without acquisition, inference, adapter re-exploration or source mutation. Review all required/forbidden claims, source locations, omissions and target limitations against the actual frozen material.

Compare with the same-input baseline. State which reviewer task is now easier to verify and which burden remains. A same-assistant exposed review is development evidence, not independent usefulness. Do not claim broader semantic success from deterministic fact extraction.

### Decide scope completion and the next responsibility

Return a bounded disposition: reuse sufficient, accept as experiment-local evidence capability, revise, defer or reject. Acceptance requires the consumer/proof conditions in §9; unresolved findings can be correct but an all-unknown result does not establish the proposed structural capability.

Normal trial composition, new target-source acquisition, a model comparison, normal-product migration and independent utility are distinct later selections. If the chosen consumer is initially curated/offline, name exactly what the ordinary acquisition path can already supply and its smallest missing premise. The parent plan's ordinary PR-to-exposure goal remains incomplete until normally reachable; do not present curated pairing as normal-product integration.

## 7. Required contrasts and proof strategy

Use the smallest real and controlled set that discriminates the selected contract. The following obligations are concrete entry pressure; qualification may find a source unavailable, which must remain recorded rather than replaced by an assumed positive case.

| Contrast | Expected evidence behavior | Claim prohibited |
| --- | --- | --- |
| Retained older Starlette call and old/proposed HTTPX constructors | Show explicit app forwarding and accepted-signature difference under the qualified source pairing | Actual target installed this sampled framework or the target was observed failing |
| Retained newer Starlette call with the proposed constructor | Preserve its absence of explicit app forwarding when complete call coverage supports it | Whole-update compatibility or no further concerns |
| Retained cert parameter and copied deprecation context | Preserve the visible signature fact and distinguish attributed deprecation from removal | Reproduce the earlier false cert-removal assertion |
| Rebinding, restored alias, unrelated local scope and conditional imported origin | Reuse current positive/conditional/unknown distinctions without stale origin attribution | Treat name spelling or possible origin as established dispatch |
| Parameter kinds, positional-only names, keyword-only arguments, defaults and duplicate binding | Apply only reviewed Python binding rules; distinguish a proven mismatch from incomplete binding analysis | Name-set subtraction alone establishes complete argument compatibility |
| Caller *args/**kwargs and callee **kwargs | Retain expansions, definite explicit facts and unresolved keys/semantics | Invent expanded keys, forwarding, values or behavior |
| Decorated callables, wrappers, multiple inheritance and super dispatch | Admit a justified static relation or explain its missing premise | Silently assume a runtime receiver or MRO |
| Partial/truncated source, wrong source-role/version binding, missing file and malformed syntax | Preserve scoped problems; refuse unsupported absence or relation assertions | Repair missing code, select convenient conflicting source or infer global absence |
| Budgets, Unicode positions, recovery and untrusted source text | Preserve byte/line identity, explicit omissions and saved-result behavior | Treat source instructions as authority or hide unexamined work as complete |

Constructed controls must vary names/modules/keywords independently of HTTPX to demonstrate supported syntactic behavior rather than expected-answer matching. They supplement real retained contrasts and cannot replace them for the real-case outcome. A second materially different real API case remains the parent's prerequisite for broader claims; do not recast a renamed fixture as that case.

Validation proceeds from representation/AST and relation-unit checks to existing binding/target/adapter tests, then consumer serialization/offline composition and the relevant inclusive trial suite. Existing anchors include [binding tests](../experiments/tests/test_api_python_bindings.py), [target-context tests](../experiments/tests/test_api_target_context.py), [adapter tests](../experiments/tests/test_api_adapter_exploration.py) and [proposal-boundary tests](../experiments/tests/test_api_change_interpretation.py). Exact commands and new test names follow the admitted implementation; do not invent them before the design.

Product regression and installed-package proof are required when an admitted change affects product/packaging boundaries. An experiment-only change requires focused/inclusive experiment and consumer proof, not a gratuitous full product rerun. Known unrelated experiment failures remain disclosed and separated by baseline comparison when material; do not repair them to make this trial's denominator green.

## 8. Resource, preservation and execution limits

- Plan drafting and the initial retained-source design qualification require zero model calls, paid operations, target installs/builds/tests or target writes. Initial qualification uses retained inputs; new live acquisition requires a separately selected need and bounded contract.
- Use existing file/source/binding/exploration limits without relaxing them to fit a known case. Freeze the limits actually used. Current source anchors include target-context ceilings of200 Python files/2MiB, binding32 origins/128 trace steps, and adapter maxima4 release samples/2 hops/12 module attempts; these are implementation anchors to recheck, not permission to acquire that amount under this plan.
- Proposed initial design-qualification ceiling: one focused session, up to4 hours of active investigation. If source readiness or consumer value is still undecidable, preserve the exact blocker and a smallest discriminating follow-up; do not continue open-ended archaeology or automatically enlarge scope.
- Before Build, set and justify explicit per-file, per-case aggregate, candidate/relationship, output and monotonic elapsed-work ceilings for the selected supported set. Inherit existing limits where adequate. This document does not fabricate performance guarantees before measurements.
- Record successful, refused, partial, failed and unattempted work, latency/resource observations, code/input/method identities and omissions. Retain reviewed public-safe manifests/examples and attribution; existing private raw evidence remains outside Git under Security. Local retention is not an off-machine backup claim.
- Opening or comparing a saved result is read-only and offline. Preserve historical source bytes, reports, model outputs and review labels. No silent correction, retry/regrade or overwrite of a frozen result.

## 9. Acceptance, rejection and stopping

The experiment-local increment is acceptable only when:

1. its source/readiness and supported-construct contract are explicit and the selected positive real evidence is available;
2. existing facts are reused or each extension has a justified producer/consumer responsibility;
3. required observed facts and at least the intended real conditional relation are correct, inspectable and preserved through the selected saved consumer;
4. supported negative controls and material unresolved cases retain the right scope, with zero decision-critical invented arguments/signature removals, dispatch/version bindings or action claims;
5. same-input comparison demonstrates a concrete verification benefit over existing facts/source view, with exposure and unmeasured utility limits disclosed;
6. focused/inclusive and offline recovery proof pass for the changed boundary, historical artifacts remain unchanged, and ordinary-path gaps are explicitly stated;
7. method/cost limitations and the adopt-as-experiment, reuse, revise, defer or reject disposition are recorded without promoting the result into broader product acceptance.

Stop before implementation if qualification cannot support a useful bounded result or if a design choice changes an accepted higher owner's semantics. Stop after the bounded consumer result/disposition; do not automatically start another parser family, model/prompt trial, generic call graph, source archive, normal-product cutover or action-permission change.

Explicit exclusions: arbitrary Python interpretation, complete call-graph/MRO solving, installed-version inference from constraints, execution-based reflection, package-specific argument rules, natural-language expected-answer parsing, new dependencies/frameworks/agent machinery, target execution, global compatibility judgments and independent-utility claims from exposed assistant review.

## 10. Discussion and maintenance

The first discussion should settle the consumer milestone, whether existing facts already meet it, the proposed qualification ceiling, admissible source/construct boundaries and the exact design-to-Build decision. Later routine implementation details need not repeatedly reopen those settled decisions.

Change this plan when its responsibility, supported proof scope, consumer, limits, accepted owner or promotion boundary materially changes. Keep implementation results, current phase and selected continuation in dated evidence and MEMORY rather than turning this plan into a second live-state tracker. No new master plan or ADR is required merely because Ali requested this standalone child file.
