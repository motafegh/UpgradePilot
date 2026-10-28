# Reusable Python caller/signature evidence design

**Artifact:** proposed experiment contract, prepared for review; not implemented product behavior or a new accepted specification/ADR.  
**Responsibility:** extract inspectable call and declared-signature facts from qualified Python source, compare supported argument binding under an explicit correspondence, and preserve the result for offline review.  
**Execution owner:** [caller/signature plan](../../../plans/DETERMINISTIC_API_CALL_AND_SIGNATURE_EVIDENCE_PLAN.md).  
**Progression:** [design cycle](../../2026-10-28_reusable-caller-signature-evidence_design-cycle.md).  
**Input qualification:** [seven-file retained inspection receipt](../2026-10-26-explanation-source-and-analysis-gaps/retained-source-inspection.json).

## 1. Product purpose and minimum useful generality

The owning product responsibility is the Charter's evidence-backed, project-specific dependency-update explanation. This increment supplies structural evidence for one mechanism family: arguments supplied by a Python call versus parameters accepted by a declared Python callable. It does not replace natural-language change interpretation, target applicability evaluation, CI/runtime-state owners or maintainer decision authority.

The consumer question is: **which supplied arguments fit or conflict with this captured signature, under which source relationship, and which missing premise prevents a stronger target conclusion?** The first reviewer task compares older/newer captured Starlette calls with old/proposed HTTPX initializers. The algorithm must consume source syntax and identity, not HTTPX/package/keyword constants, expected removals or a reviewer verdict.

Variation includes modules and aliases, parameter names/kinds/order/default presence, positional and keyword argument shapes, different captured versions, rebindings, incomplete evidence and unresolved correspondence. A different library using the same supported forms needs different evidence, not another package-specific rule. New Python constructs may need a new method version and proof. [Minimum Useful Generality](../../../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) controls this distinction.

The baseline is today's retained source view plus existing call/binding facts and manual comparison. The selected extension earns its place by making a correct, recoverable conditional binding comparison inspectable without requiring the reviewer to reconstruct it from separate files. The baseline has not been independently measured for task benefit, and this design is not a usefulness result.

## 2. Owners, reuse and placement

| Responsibility | Existing owner / proposed local extension | Reason |
| --- | --- | --- |
| Exact target, source identity, bounded retained reading | [source_access.py](../../../src/upgradepilot/workspace/source_access.py), existing catalog reader/constructors | Reuse data-only retained text and scope semantics; a digest is not source completeness or source authority |
| Ordered/scoped import-origin assessment | [api_python_bindings.py](../../../experiments/api_python_bindings.py) | Reuse BindingAssessment and its established/conditional/unknown/unbound distinctions |
| Supplied keyword names and syntactic positional count | Same ReferenceFact producer | Already implemented; no second keyword/import analyzer |
| Missing argument shape and declared parameter facts | Proposed cohesive `experiments/api_call_signature.py` extension | Exact call spans, starred items and ordered parameters are needed for supported binding; avoid changing shared legacy fields unless necessary |
| Curated pair validation, comparison and saved view | Proposed `experiments/api_call_signature_trial.py` | One experiment runner and offline consumer; no product import of experiments |
| Ordinary experimental source discovery | [api_target_context_smoke.py](../../../experiments/api_target_context_smoke.py) and [api_adapter_exploration.py](../../../experiments/api_adapter_exploration.py) | Existing producers remain responsible for acquired paths, source association, sampled releases and omissions |
| Actual target installation/execution and applicability | Existing independent owners; unestablished by this method | No version inference, dynamic dispatch solution, CI inference or action promotion |
| Normal report/native Workspace integration | Separate product adoption responsibility | Experimental output is not serialized as an accepted product finding |

These file names are implementation hints, not a new package architecture. Keep extraction and binding together until actual size/cohesion evidence justifies separation. Add no dependency, generic rule engine, graph solver, framework or global result-state hierarchy.

Existing trace steps already contain exact AST spans. Join a newly inspected call node to the unique matching reference trace using source identity and full span; do not assume line/expression uniquely identifies a call. If a legacy or exhausted trace cannot support that join, retain syntax facts but mark the imported-origin join unavailable. Never assign an established binding to the first similar call on a line. This avoids manufacturing precision or unnecessarily changing binding manifest v2.

## 3. Input and selection modes

### Retained calibration entry

Proposed public experiment entry: `python -m experiments.api_call_signature_trial compare --sources CATALOG --target TARGET --pairs SELECTIONS --output RESULT`. Names are design-level interface choices; implementation may simplify them without weakening the boundary.

- `CATALOG` is a host-admitted existing source catalog, decoded with the exact expected investigation target. Its source scopes supply independent repository/revision/capture-basis/coverage identities.
- `TARGET` is the existing exact target representation, not a new target grammar. A source catalog bound to another target is refused.
- Each pair selects a caller source/file/exact AST call span, a callee source/file/qualified definition span, and a labelled receiver-binding premise. Selectors locate evidence; they contain no accepted/rejected answer, removed keyword list or positive installed-version claim.
- Source selectors are legitimate curated calibration input only. Every such result carries `curated_pair` visibly. Supplying the correct source pair does not prove discovery, dispatch or ordinary PR reachability.
- Parse full qualified files. Do not patch excerpts, insert missing bodies or infer completeness from successful parsing. A recorded acquisition/coverage problem blocks affected absence claims even if the remaining text parses.

A generic source selection is necessary to perform a conditional comparison. It is not a substitute for an automated source-discovery responsibility. That separate boundary must consume ordinary PR/provider evidence without receiving the expected paths, framework versions or answer.

### Ordinary experimental composition

Design the core operation to accept source objects and existing references from `PublicPRContextTrial` without package-specific arguments. Ordinary candidate generation starts only from established imported references and acquired source/module identities. Conditional origins remain alternatives, not a selected winner. Module-path/re-export observations may supply explicit source-chain evidence; they do not establish an installed distribution namespace or solve arbitrary import execution.

An acquisition object can be examined in memory, but its saved manifest currently lacks full file bodies. The initial implementation must report `source_text_unavailable` rather than fetch missing files or relabel manifest hashes as text. Wiring a fresh ordinary trial into this method requires a separately bounded source/retention change. No default network fallback is part of either compare or open.

Automatic cross-file/callable correspondence is not silently admitted by the calibration runner. Before ordinary discovery acceptance, implement and prove the selected structural import/re-export/definition route with the existing producers, source/namespace limitations, target exposure and omission accounting. If that route cannot discover a material relationship, the ordinary-path goal remains incomplete even if curated comparisons pass.

## 4. Facts and correspondence contract

Use small experiment-local immutable records, with explicit serialization; the following names describe responsibilities rather than mandate an inheritance hierarchy.

| Record | Minimum material contents and consumer |
| --- | --- |
| Source unit | Catalog/source/file identity, repository, revision, path, UTF-8 digest, role, capture basis, adequate/limited unit coverage; enables location, integrity and qualified absence |
| Call arguments | Exact full call span; ordered positional syntax items classified ordinary/starred; ordered explicit keyword names and double-starred items with spans; reference to existing binding assessment when uniquely joined; needed for binding and honest expansion limits |
| Callable signature | Exact definition/header span and lexical owner; function/async-function/constructor-definition kind; ordered parameter names and kinds; default-present boolean; variadic parameter identities; decorator/class-context limitations; needed for binding, not default-value execution |
| Correspondence | Caller/callee IDs, `curated_pair` or evidence-derived source-link basis, source-chain references, receiver mode/premise, version/source-selection limitations; prevents a supplied pair or lexical path becoming runtime identity |
| Comparison | Per-check findings, scoped binding outcome/completeness, both source references, remaining premises, method identity and proof class; supplies saved review and a future native projection |

Lines are1-based; AST columns are0-based UTF-8 byte offsets, following existing trace semantics. Internal IDs include source content identity and full span, so same-line or same-named definitions cannot collide. A distinct captured old/proposed source role cannot be silently replaced merely because the path/qualified name matches.

Retain default **presence**, not evaluated values. Retain no argument values or annotation semantics for this responsibility. Original text already supplies inspectability. Decorators and class context are evidence/limitations, not execution permission. A complete signature fact can be extracted from a decorated definition while its effective runtime signature remains unresolved.

### Receiver binding and constructors

Comparison is against a declared function signature with an explicit receiver mode:

- `as_written`: supplied positional items bind from the first declared positional parameter; no receiver is inserted.
- `one_receiver_assumed`: one implicit positional receiver precedes source call arguments. The condition is shown in every resulting comparison. Do not infer it merely from a parameter named `self` or `cls`.
- `unresolved`: parameter-specific keyword facts may survive, but full argument binding cannot be claimed.

Initial direct function comparisons use `as_written` under the stated caller/callee pairing. Method/initializer comparisons may use `one_receiver_assumed` only as an explicit conditional premise. A structurally justified future descriptor/binding proof can discharge that premise through its own evidence; this contract does not label an assumption established.

For HTTPX, inspect the actual `Client.__init__` definition. The captured Starlette `super().__init__` comparison explicitly assumes that it reaches that initializer with a bound receiver. Record the enclosing class/base expression as source context, but retain existing unknown dynamic-reference binding. No general MRO solution, effective class-call signature, metaclass behavior or `__new__` acceptance follows. The outer `TestClient(app)` call and inner forwarded `app=` remain different calls.

## 5. Supported checks and unresolved states

Binding follows the local Python3.12 syntax/parameter rules, not runtime reflection on third-party code. References: [calls](https://docs.python.org/3.12/reference/expressions.html#calls), [function definitions](https://docs.python.org/3.12/reference/compound_stmts.html#function-definitions), and the positional-only name-collision case in [PEP570](https://peps.python.org/pep-0570/#semantic-corner-case). Newer syntax the local parser cannot read is a scoped unsupported-syntax result, not evidence the source is invalid in its own environment.

| Situation | Initial behavior |
| --- | --- |
| Ordinary positional/explicit keyword arguments; complete signature; specified receiver; no unpacking | Bind positions and keyword-eligible names; account for default presence, excess positions, missing required parameters and duplicate assignments. Preserve each exact finding |
| Positional-only, positional-or-keyword and keyword-only parameters | Respect kinds; naming a positional-only parameter in a keyword does not fill its positional slot |
| Callee `*args` / `**kwargs` | Recognize additional reception at that boundary; do not claim anything about body semantics or forwarding |
| Positional-only name also supplied as keyword with callee `**kwargs` | Keyword may enter the mapping independently; assess the positional-only slot separately. Do not reject by name alone |
| Caller `*args` / `**kwargs` | Preserve every expansion as unknown; do not evaluate even literal containers in the initial method. Suppress full-binding success and checks that require their contents |
| Definite explicit unexpected keyword, despite caller expansions | Retain the scoped rejection if a complete signature cannot receive that name. Expansions cannot make an unsupported explicit keyword accepted. This is not proof of which runtime error occurs first |
| Decorated/wrapped definitions, arbitrary object methods, `super()`, inheritance, metaclasses, dynamic mutation | Keep declared syntax facts and curated conditional comparisons; effective dispatch/signature stays unresolved without separately admitted evidence |
| Class-private parameter names requiring name mangling | Retain source spelling and explicit unsupported-binding reason in the initial method; no unreviewed spelling-to-effective-name substitution |
| Missing/corrupt/wrong-target text, ambiguous selector, incomplete signature, unsupported syntax | Record the specific problem; no inferred absent parameter, guessed callee, repaired source or successful full binding |

The first implementation has two check scopes: **explicit-keyword reception** and **complete syntactic argument binding**. The second is available only for the expansion-free, fully specified supported input. This prevents one keyword mismatch from being presented as a complete binder, and prevents unknown expansions from erasing independently definite evidence.

Dynamic expansions, class-private mangling, runtime descriptors/MRO and ordinary source discovery are temporary method exclusions or separately owned premises, not permanent product exclusions. Their cost is explicit: affected cases can lack a complete binding result or normal automatic reachability. Re-enter a construct when a real decision-critical case needs it, qualified inputs exist and a reviewed generic rule/proof fits its owner. Semantics/behavior changes are outside this structural method, while remaining inside the broader product responsibility. These exclusions do not remove the obligation to deliver meaningful positive, refuting and specific unresolved explanations through the eventual admitted product flow.

Use comparison-local outcomes:

- `rejected`: at least one definite binding violation under the stated pairing/receiver premises. Other checks can remain unknown.
- `bound`: all supported syntactic binding checks complete with no violation; no unknown expansions or receiver binding. This does not mean call execution, compatible behavior or a safe update.
- `undetermined`: no definite rejection, but at least one premise or required binding check is unresolved.

Each keyword finding separately says named-parameter reception, variadic-keyword reception, no receiver for that name, or undetermined, with references. No candidate-wide not-applicable conclusion is derived from one successful comparison or the absence of one keyword in a different call. These are local experiment results, not a replacement PropositionState or action evaluator.

### Binding algorithm obligation

Read the caller's AST and callee's parameter kinds, then perform the supported Python slot assignment under the explicit receiver premise. The algorithm must not subtract untyped name sets. It must distinguish duplicate assignment, position-only restrictions, optional parameters and variadic reception. With expansions, return partial checks conservatively instead of guessing values/counts; record affected missing/duplicate/positional checks as unattempted or unresolved. No first-error ordering or argument-expression evaluation is claimed. A small trusted synthetic binder oracle may validate the rule implementation; never import or execute retained target/framework code to obtain it.

Do not treat `inspect.Signature.bind` as an unquestioned sole oracle or implementation shortcut. On the observed local Python3.12.3 runtime, a trusted control `def f(value=0, /, **options)` accepts `f(value=2)` using the default positional-only value and receiving the keyword in `options`, while `inspect.signature(f).bind(value=2)` rejects it. The [design validation receipt](validation.json) preserves this local discrepancy; it is not a claim about every Python version or a defect in UpgradePilot's existing owners. Fourteen other helper controls passed, which did not establish universal helper fidelity. Implement the small documented slot-binding rules and check this corner against trusted, side-effect-free, locally authored function calls. Such controls execute no third-party source and do not measure target behavior. Defaults/annotations/argument expressions from retained sources remain unevaluated.

## 6. Retained HTTPX worked design cases

These are source-backed **design expectations**, not new analyzer outputs or repaired historical model judgments. The receipt already qualified full files and existing keyword facts. Preserve the original model packet, source captures and reviews unchanged.

| Pair / contrast | Expected local result | Missing premise / forbidden conclusion |
| --- | --- | --- |
| Older captured Starlette call → old HTTPX initializer | Explicit `app` is received by the named parameter; assess remaining supplied keywords and receiver mode separately | Does not establish actual installed Starlette, actual dispatch or successful execution |
| Same older call → proposed HTTPX initializer | `app` has no receiving parameter or `**kwargs`; definite conditional keyword rejection | No observed target failure, installed-version conclusion or whole-call error-order claim |
| Newer captured Starlette call → proposed initializer | Exact complete call has no explicit `app` keyword; that particular forwarding mismatch is absent in this call | No claim that the outer constructor rejects app, no global non-use or whole-update compatibility |
| Old/proposed HTTPX signatures: `cert` remains present | Keep the named-parameter fact in both inspected definitions | Signature presence neither refutes deprecation nor establishes behavior/meaning |
| Target TestClient use → FastAPI re-export → selected Starlette source | Display acquired source facts and selected-source basis separately from conditional inner comparison | Never promote the sampled/reference Starlette to the target's installed version |

The saved human view must answer: what differs, where it connects to the inspected source, which lines support it, what remains missing, and what specific next evidence could resolve that premise. For this case, actual target environment/framework identity and dispatch are unresolved; suggest their investigation without claiming a particular unavailable observation or auto-running checks.

## 7. Saved consumer and integrity boundary

One bounded JSON result contains `format=caller-signature-evidence/1`, method identity and analyzer/runtime configuration, exact target, source-selection/proof class, catalog reference, source facts, correspondences, comparisons, coverage/omissions, and problems/attempt disposition. The method identity is separate from format identity so algorithm changes cannot masquerade as the same transformation. Freeze input/method hashes before each official comparison.

Retain a minimal subset using existing source-catalog constructors: selected source scopes and **complete files actually needed for extraction and cited chains**, including relevant target/declaration context. Record its relationship to the original catalog. Preserve its exact bytes as a companion and bind its digest in the result; do not copy the whole2632-file catalog or raw model prompt. Seven selected files are already qualified, but this design does not mutate or copy them into Git. Private source stays in host-owned storage; reviewed public receipts contain identities and facts only.

`open --result RESULT` renders historical saved findings read-only with the bound companion catalog. Source inspection uses existing readers/spans. Do not acquire, run models, execute code, reanalyze or silently recompute a changed method on open. Explicit reanalysis is a new attempt with its own identity; it does not overwrite the saved record. This is experiment reopening, not canonical Workspace recovery or deterministic replay acceptance.

At independently combinable file boundaries validate bounded JSON shape, format/method identity, exact target, source-catalog digest and material IDs/spans/references. No pickles, dynamic deserialization, external URL following or embedded absolute source-path opening. Source text is untrusted data; terminal output follows existing sanitization. Hash equality checks recorded bytes, not producer honesty, source association authority or semantic correctness. Avoid duplicating provider/schema checks inside each binding rule.

Missing/corrupt companions, unknown format/method or broken material references produce explicit reopen problems. An intact saved summary may be displayed only with its limitation; never label unavailable text inspectable or damaged comparisons validated. Historical manifests lacking source bytes remain readable through their existing owners and are not silently upgraded to this format.

A useful result has both structured comparisons and a concise human view. Both project the same saved facts; prose must not invent arguments, omit material premises or call `bound` compatible. The consumer cannot turn a proposal into a finding or change maintainer-action permission.

## 8. Initial finite limits and failure behavior

These are proposed experiment ceilings, to freeze before implementation proof; they are not measured performance guarantees or a new product retention policy.

| Boundary | Ceiling / rationale |
| --- | --- |
| Source-profile input | Existing64MiB catalog reader/4MiB per-file/20,000-file limits; no relaxation or whole-catalog reanalysis |
| Selected comparison material | At most32 files and4MiB total UTF-8 text, plus existing exact target/scopes; comfortably includes the qualified195,501-byte seven-file case without defining a seven-file-only mechanism |
| AST/derived work | At most100,000 AST nodes per selected file,250,000 per case,4,096 call/signature records combined and256 selected pairs; deterministic ordering with omitted counts/identities |
| Shared binding | Existing32 origins/128 trace steps; exhausted traces cannot become positive source correspondence |
| Serialized saved result and selected-source companion | At most16MiB each, checked on serialized bytes; no silent clipping that changes the result's claims |
| Worker | Initial60s monotonic total per comparison attempt and512MiB worker address-space ceiling on the WSL test host; standard-library subprocess/resource controls, no external framework or target execution |
| Selected design responsibility | Retained-source work only; zero target acquisition/installs/tests, model calls or source refresh. Official docs inspection is design reference research, not acquisition into a case |

Bound the parsing/analysis worker as a whole; checking elapsed time only after `ast.parse` is insufficient to enforce a timeout. The parent owns deadline/termination, attempted/completed/unknown disposition and public-safe problems. A killed worker supplies no invented partial comparisons. Completed records may be retained only if the runner actually received/validated them before termination. If host limit enforcement is unavailable, fail the bounded execution entry explicitly rather than advertise enforcement.

Do not fetch to repair missing source, enlarge ceilings because the known case fails, or silently sample a convenient passing subset. A cap/syntax/source problem may leave independently supported facts available but prevents affected completeness/absence claims. If the chosen limits obstruct useful real coverage, retain the observation and revise the design deliberately.

## 9. Discriminating implementation proof

Before execution freeze the real/calibration inputs, method/code IDs, selected limits, expected and forbidden conclusions, comparison baseline and cost accounting. Expected answers are review/test material, never source-discovery or production inputs.

| Proof class | Required discriminating evidence |
| --- | --- |
| Retained real conditional evidence | All five contrasts in §6; exact old/new source-role preservation, actual existing keyword reuse, no invented cert removal or installed-version upgrade |
| Generality within syntax | Vary module/function/keyword names independently, aliases and file layout; same meaning preserves normalized binding, changed parameter kind/default/callee changes the appropriate result |
| Ordinary binder controls | Required/default parameters, positional-only and keyword-only, too many positional values, positional-plus-keyword duplicate, callee `*args`/`**kwargs`, same positional-only name in `**kwargs`, optional positional-only parameter left at its default while its name enters `**kwargs`; do not use the locally divergent inspect helper as sole oracle |
| Partial evidence | Caller expansions, missing receiver premise, conditional binding, unknown dynamic call, truncated/broken source, unsupported syntax; keep definite facts and refuse unsupported complete success |
| Identity/selection | Several calls on one line, same qualified definition in different revisions, wrong roles, ambiguous spans, trace exhaustion; no first-match choice or silent v2-manifest precision upgrade |
| Saved boundary | Round-trip and cold offline open/source view; missing/corrupt/wrong-target companion, unknown version, changed method and source text, source-span integrity and output sanitization; zero hidden network/reanalysis |
| Boundedness | Exact cap boundary, one over, timeout and worker failure; preserve omitted/unattempted work and termination truth |
| Ordinary experimental discovery | Existing PR acquisition and adapter evidence actually supplies supported source/correspondence without known-answer selectors; absent source/unknown namespace stays missing. This is separately required for ordinary-path claims |
| Additional real case | A materially different real API interaction with readable pinned source and target/caller basis; choose/freeze it before observing new method output. A renamed fixture is not that case |

A second real case must vary a relevant structural dimension, such as direct function calls versus an adapter initializer, positional/keyword kind changes versus a removed keyword, or callee variadic reception. Prefer already retained evidence; if none qualifies, record source readiness and arrange a separately bounded acquisition decision. Do not invent a ready second case or rerun frozen model cases. Unsupported real cases remain in the coverage account, not replaced after seeing failure.

Run focused new extraction/binding checks first, existing binding/target/adapter/proposal-boundary tests next, then saved-consumer and inclusive experiment proof appropriate to the actual files changed. Product/installed-package proof becomes necessary when product/packaging is changed. Historical12-test and908-test results are not new implementation proof. No test count alone establishes independent maintainer benefit.

## 10. Implementation sequence and product adoption

1. Freeze this reviewed contract and concrete inputs; reuse completed qualification instead of repeating the source investigation. Implement full-file extraction and the bounded binder with source-linked controls.
2. Implement the retained calibration entry, saved comparison/selected-source companion and cold offline human/source view as one coherent experimental consumer. Compare against existing source/fact review on the same inputs; report actual benefits/errors/cost with exposed-review limits.
3. Earn broader evidence using the required controls and a separately frozen materially different real case. Fix demonstrated method defects; preserve original failed outputs and new method identities. A narrow passing case is not acceptance of unsupported constructs.
4. Close the ordinary experimental acquisition/retention/correspondence path before claiming PR-driven automatic discovery. Reuse existing owners; missing source does not justify loosening stronger upstream provenance or runtime admission.
5. Before normal product adoption, settle minimal native evidence-family/closure, owner versioning and direct Workspace-to-report projection with the third migration discussion. Implement in `src/` with active tests; product never imports experiments. Decide product source-acquisition/report compatibility and independently assess utility at their proper gates.

This ordering provides a useful offline structural result before requiring all Workspace migration, while keeping ordinary target reachability and product delivery as explicit unfinished obligations. Passing step2 does not complete the agreed maintainer-facing milestone. No automatic new model experiment, universal Python analyzer, full Workspace migration, semantic-role adoption or stronger action permission follows from this contract.

## 11. Alternatives and decisions retained for review

- **Manual source/fact inspection:** baseline retained; minimal implementation cost but repeats the relationship reconstruction and permits the exposed semantic errors. If the extension adds no concrete inspectability/error-prevention value, prefer baseline/reuse and reject the increment.
- **Keyword-name subtraction only:** insufficient as the complete design because parameter kinds, duplicates, receivers and variadic reception change binding. Retained as one explicitly scoped check inside the fuller binder.
- **Construct a stdlib Signature and delegate all binding:** credible simpler candidate, but the local optional-positional-only/variadic-keyword disagreement makes unqualified delegation or helper-only acceptance unreliable. A special-case compatibility patch would hide method responsibility in runtime behavior; prefer a small explicit binder with documented, trusted-control proof. Reconsider delegation only with demonstrated rule equivalence at the supported runtime boundary.
- **Runtime reflection or package execution:** answers different runtime questions, with installation/execution effects; not selected for source-only evidence.
- **Generic static-analysis/MRO framework or another model:** no demonstrated need to extract declared parameter syntax or run supported binding rules. Re-enter when material real cases expose missing dispatch/meaning that prevents useful coverage, with separate proof/cost/authority design.
- **Whole Workspace migration first:** not shown necessary for a curated offline consumer; no permission to defer minimal normal-product integration indefinitely.

The selected design is recommended for experiment implementation review. Exact implementation names may change; supported semantics, source/receiver premises, proof limits, budgets and product-adoption boundary cannot drift silently. Consequential scope changes return to this owner/plan discussion. No new accepted specification/ADR is required while this remains an experiment under existing source/proposal/Workspace owners.
