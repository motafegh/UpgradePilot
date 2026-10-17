# Investigator deployment/interface — consolidated study guide

**Date:** October 17, 2026
**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Purpose:** consolidated learner-owned study material for the deployment/model-interface qualification responsibility.
**Boundary:** this is a learning companion, not canonical D, not a qualification owner, and not a replacement for current `main` evidence. Reconcile it against final main evidence before merge.

## 1. The big picture

UpgradePilot is not merely asking, “Can this local model produce text?” The responsibility is to establish whether an exact local **deployment** can interact with the Investigator interface in a reproducible, inspectable and evidence-safe way before we spend real-case budget.

The most important lesson of the entire cycle is:

> **Declared / requested / intended is not the same as actually observed.**

Examples from our work:

- a rendered request measured 1817 tokens while the runtime consumed 1818 because a BOS token was being inserted;
- requested GPU offload did not prove the actual number of GPU-resident layers;
- an earlier “complete stateless history” retained results but omitted the exact requests that produced them;
- a model-generated ID that looked like a citation was not an eligible evidence reference;
- a syntactically valid final report could still make unsupported semantic claims;
- a model that passed under one backend/runtime/configuration was not automatically qualified after the backend changed.

The engineering discipline is therefore:

`request/configuration -> observe actual runtime -> retain exact evidence -> evaluate only what that evidence establishes`

Never substitute the left side for the right side.

---

## 2. Request-to-model execution pipeline

The practical local execution path is:

`UpgradePilot request -> chat-template rendering -> tokenizer/token IDs -> special-token handling -> context admission -> LM Studio orchestration -> llama.cpp/backend inference -> CPU/GPU/KV placement -> generation/sampling/thinking -> streamed result/usage -> SDK binding -> strict Investigator adapter/assessor`

### Chat template

The model is not normally given our Python objects directly. Its model-specific chat template converts system/user messages and schemas into the textual representation expected by that model family.

Different templates can materially change behavior. Therefore exact template identity/content is part of deployment identity.

### Tokenizer and tokens

A **token** is a unit from a model tokenizer’s vocabulary represented internally by an integer ID. A token is not necessarily a complete word.

Different models can tokenize the same text differently.

**BOS** = Beginning Of Sequence.
**EOS** = End Of Sequence.

Our 1817-versus-1818 observation mattered because it proved that the backend consumed a representation different from the one we believed we had measured. One token was not the capacity problem; the problem was broken correspondence between measurement and actual execution.

### LM Studio versus llama.cpp

LM Studio is the application/orchestration layer that loads models, exposes APIs/SDK behavior and configures inference.

The llama.cpp-based backend performs the lower-level local inference work.

They should not be treated as the same component.

---

## 3. Context, input and generation capacity

The **context window** is the total token capacity for the active sequence.

Within it we have:

- input/prompt tokens already present before generation;
- generated tokens produced afterward;
- an intentionally reserved output/generation allowance;
- a safety margin.

A useful admission rule is approximately:

`input + generation reserve + margin <= context capacity`

Passing this rule proves only that the request mathematically fits the declared envelope.

It does **not** prove:

- the model will use the entire reserve;
- it will finish correctly;
- it will avoid early EOS;
- it will generate valid JSON;
- it will reason correctly;
- it will avoid repetition;
- it will be fast enough;
- semantic claims will be supported.

A generation reserve is capacity, not actual generated-token count.

Reasoning/thinking tokens, when generated, also consume generation/context resources.

### RoPE

RoPE frequency base/scale affect positional interpretation and context behavior. We only need the conceptual relationship at this stage. Deliberate tuning belongs to explicit context-extension work, not routine qualification tuning.

---

## 4. Model weights, GPU offload and KV cache

### Model weights

Weights are the persistent trained parameters of the model.

### KV cache

The Key/Value cache is temporary attention state for tokens already processed in the current sequence. It lets inference reuse attention state instead of recomputing all previous token attention from scratch for every new generated token.

It grows with active context and can consume substantial memory.

Weights and KV cache are therefore different memory responsibilities.

### GPU offload

GPU weight offload means placing some model layers in GPU VRAM so those layers execute on the GPU. Other layers can remain CPU-executed using host/system memory.

A requested offload ratio is **not proof of actual placement**. LM Studio itself warns that the actual number of offloaded layers can differ according to dedicated GPU memory and runtime/model constraints.

This is why our work preferred an actually observed stable placement, such as a fixed observed layer count, over trusting a nominal request like `1.0`.

The goal was not “maximum GPU at any cost.” It was a reproducible operating point whose actual state we could verify.

### Other runtime knobs we identified

These are important but mostly deferred from current optimization:

- evaluation/logical batch size: prompt/prefill work grouped logically;
- physical/micro-batch size: smaller physical execution chunks used to process the logical batch;
- maximum concurrent predictions: number of simultaneous inference requests;
- unified KV cache: shared KV-pool behavior across sequences;
- `mmap`: memory-mapped model-file loading/page-cache behavior;
- Flash Attention: optimized attention implementation affecting memory traffic and throughput;
- K/V cache quantization: lower-precision KV storage trading memory for possible precision/quality effects;
- speculative decoding: draft model proposes tokens and main model verifies them; this changes the decoding/deployment path and must be treated as a distinct configuration.

We recorded these for later performance work rather than turning current qualification into an uncontrolled parameter sweep.

---

## 5. Sampling and thinking mode

Generation is probabilistic unless constrained otherwise.

### Temperature

Temperature changes how concentrated the next-token probability distribution is.

Lower temperature generally makes sampling more deterministic/concentrated. Higher temperature allows more variation. It is not an “intelligence” setting.

### Top-k

Top-k limits candidate next tokens to the `k` highest-probability options.

### Top-p

Top-p keeps the smallest high-probability candidate set whose cumulative probability reaches approximately `p`.

### Thinking/reasoning mode

Thinking on/off can change:

- generation path;
- token usage;
- latency;
- reasoning-fragment behavior;
- visible response behavior;
- output quality;
- failure modes.

Therefore:

`same model + different thinking/sampler/runtime settings = different deployment configuration`

If a model fails under thinking-off and passes under thinking-on, we can say the later exact deployment qualified under the tested conditions. We cannot automatically say “thinking fixed the model,” especially if backend, samplers, batching or generation allowance also changed.

---

## 6. Stateless interaction design

Our current Investigator transport uses a **stateless model boundary**.

Stateless does not mean UpgradePilot forgets everything. It means the inference server/model is not trusted to own hidden conversational truth. Anything the model is allowed to rely on in the current call must be explicitly reconstructed into that call.

Conceptually:

`Workspace/product state -> select allowed working context -> construct complete request -> model call`

UpgradePilot owns durable state. The model receives an explicit temporary working set.

### Why request/result pairs matter

An earlier implementation retained prior observations/results but did not always retain the exact model request arguments that caused those observations.

For example, the model might later see:

`result: file not found`

without seeing:

`previous request: read_file(path="foo.toml")`

Then if it asks for `foo.toml` again, we cannot confidently call that a model repetition failure: the interface failed to give the model its exact previous action.

The repaired design therefore preserves whole chronological pairs:

`previous model request + returned observation`

The request preserves **intent/history**.
The observation preserves **what the system actually delivered**.

They have different authority.

---

## 7. Evidence and citation authority

This is one of the most important boundaries in UpgradePilot.

### Model request

A model request such as:

`read_source("foo.py")`

means only that the model attempted/requested that operation. It is not evidence about `foo.py`.

### Returned observation

A Workspace/tool observation is information the system actually returned. It has provenance and may carry typed references.

Observation still does not automatically equal semantic truth about every broader proposition. It is evidence with a particular scope.

### Delivered typed evidence reference

Only references actually delivered as eligible references by the system can authorize report citations.

### Internal native ID

An internal record/catalog/delivery/event ID is not automatically a citation reference. If it was not explicitly delivered as an eligible evidence reference, the model may not promote it into one.

### Final citation

A final model citation is valid only if it uses an eligible typed reference that was actually delivered in the relevant observation/history.

The authority chain is:

`model asks -> system returns observation -> observation delivers eligible typed reference -> report may cite that reference`

Not:

`model invents/mentions ID -> ID appears in later history -> ID becomes evidence`

A model-authored ID remains model-authored history even if it appears again in the next stateless request.

### Visible observation versus citable reference

A recent main-branch review refined this further: **the model may see an observation/problem even when that observation carries no eligible typed reference.**

Therefore:

- “the model did not cite it” does not necessarily mean “the model failed to see it”;
- we must check whether the interface actually provided a citable typed reference;
- we should not encourage the model to invent a citation for an uncitable observation;
- review language must distinguish visibility, citeability and semantic use.

This is an important example of our broader discipline: evaluate the model only against what the interface truly made available and authoritative.

---

## 8. Canonical representation versus model-readable presentation

UpgradePilot may keep canonical packed bytes/structures for:

- exact accounting;
- hashing;
- omission decisions;
- admitted event identity;
- eligible-reference identity;
- reproducibility.

The model-visible prompt can present the same admitted information in a more readable layout such as:

`fixed protocol -> current phase/menu -> request/result pair 1 -> request/result pair 2 ...`

The formats may differ.

What must not differ is the admitted meaning/data.

The readable presentation must not silently:

- add evidence;
- remove evidence;
- alter reference IDs;
- mutate request arguments;
- change observation content;
- invent hidden state;
- misleadingly reorder interactions.

So:

`canonical format != presentation format`

while:

`canonical admitted content == faithfully represented model-visible content`

---

## 9. Stateful LM Studio chats: relevant future alternative

LM Studio now provides stateful chat continuation using response/thread identifiers.

This is directly relevant because it could avoid resending the whole visible conversation payload on every call.

But stateful convenience raises architectural questions for UpgradePilot:

- can old or invalidated evidence remain visible in server-managed history?
- can we enforce current reference eligibility?
- can we reconstruct effective context after restart/unload/failure?
- what exactly persists?
- does the feature reduce model prompt processing or only HTTP payload size?
- does it reuse KV state, and if so under what conditions? This must be measured rather than inferred from a response ID.
- can Raw/Structured experimental isolation remain reproducible?

A promising future architecture would keep the Workspace as canonical authority and treat server state only as a disposable acceleration/convenience layer, but that is not selected or proven.

Current qualification therefore remains explicitly reconstructed/stateless.

---

## 10. Streaming and SSE

UpgradePilot already streams model output through the LM Studio SDK `PredictionStream`:

- visible fragments can be retained incrementally;
- partial visible output is not lost merely because final completion later fails;
- reasoning-labelled fragments can be detected and filtered before persistence;
- success configuration/usage metadata is captured when available.

LM Studio’s REST streaming/SSE interface exposes a richer typed event lifecycle including prompt-processing, reasoning, tool-call, message, error and final events.

Potential future value:

- better prompt-processing and time-to-first-token observability;
- cleaner reasoning-channel detection;
- richer error/interruption diagnostics;
- possible cross-check of usage/timing;
- explicit native tool events.

But REST/SSE/native-tool behavior is a different transport/protocol condition. It should be compared later, not silently inserted into the current frozen qualification.

---

## 11. Candidate, deployment, preflight, canary and semantic case

These levels must stay distinct.

### Model candidate

The model asset being considered, e.g. Gemma 12B or Qwen 27B.

### Deployment/configuration

The candidate plus the exact execution conditions, such as:

- exact GGUF/hash;
- runtime/backend version;
- template;
- tokenizer/special-token behavior;
- context;
- generation limit;
- sampler;
- thinking mode;
- weight placement;
- KV placement/precision;
- transport;
- relevant batching/runtime controls.

The same candidate can therefore have multiple different deployments.

### Preflight

Preparation/inspection without using the result as live model qualification. It answers whether exact identities/configuration/request shapes fit and are ready for a bounded run.

### Canary qualification sequence

A controlled synthetic interaction that actually calls the model and checks whether the deployment can operate the Investigator interface correctly.

It can test tool use, required operations, references, finishing, report production, request/history handling and context pressure.

It establishes bounded **interface operability**, not real dependency-update correctness.

### Real semantic case assignment

Later, the qualified deployment receives real HTTPX/glyphsLib evidence and must investigate an actual dependency-update problem.

That asks a different question: can it reason correctly and use evidence usefully in a real case?

The chain is:

`candidate -> exact deployment -> preflight/freeze -> synthetic canary qualification -> real semantic case`

Success at one level does not automatically prove the next.

---

## 12. Why Raw and Structured, short and near-envelope

### Raw versus Structured

Raw-oriented access mainly gives bounded source navigation such as reading/searching sources.

Structured-native access additionally gives product-owned dependency/CI/native views/pages.

The experiment asks whether structured native evidence access changes evidence use relative to raw-oriented navigation.

A deployment may operate Raw correctly but mishandle Structured references or records, so both treatments must qualify independently.

### Short versus near-envelope

Short sequences test the protocol under low/moderate context pressure.

Near-envelope sequences exercise larger histories, more observations, later evidence, omission/packing behavior and final reports closer to capacity limits.

A short pass does not prove a realistic long interaction will work.

---

## 13. Why one pass cannot qualify a whole deployment

If a deployment passes Raw-short but fails Raw-long and both Structured conditions, the correct statement is:

> Raw-short qualified under the tested condition.

Not:

> the deployment qualified.

This prevents us from cherry-picking only favorable conditions.

It is especially important before the later Raw-versus-Structured semantic comparison. If Structured already fails mechanically, a later semantic Raw-versus-Structured difference would be confounded by interface incapability.

---

## 14. Versioned experiment conditions and non-pooling

When we materially change:

- stateless history representation;
- transport;
- thinking mode;
- samplers;
- generation allowance;
- backend/runtime;
- batching/context behavior;
- other execution controls that can affect results;

we have a new experimental/deployment condition.

Old results remain evidence about the old condition.
New results become evidence about the new condition.

Do not erase old failures, and do not pool materially different conditions into one success rate as if they were identical.

This prevents “change things until it passes” from masquerading as stable qualification.

---

## 15. Failure diagnosis

Before reacting to a failure, determine the strongest justified class.

### Interface/experiment defect

Example: previous observations were retained but exact previous requests were omitted.

Repair the interface, then rerun under the repaired condition. Do not blame the model for information we failed to provide.

### Runtime/configuration correspondence failure

Example: rendered token count differs from actual runtime prompt count, or requested GPU placement differs from actual placement.

First establish actual correspondence.

### Interruption/incomplete evidence

Example: transport terminates with incomplete/unknown final usage.

Retain what was observed and mark the assignment incomplete/withheld. Do not reinterpret it as a completed semantic model failure.

### Model interaction/instruction-following failure

After the interface is complete/correct, repeated operations, skipped required operations or refusal to follow the closed protocol become evidence about that exact deployment.

### Reference/citation-use failure

Examples:

- using an internal record ID instead of delivered typed reference;
- inventing references;
- omitting required eligible citations.

### Generation/resource failure

Example: output reaches its generation cap while repeating rather than completing.

Do not automatically assume the cap was too small. Distinguish insufficient budget from wasteful/repetitive behavior.

### Semantic-quality problem

The model can use the correct tools, correct references and correct JSON while still claiming more than its evidence establishes.

Therefore:

`mechanically/interface valid != semantically correct != useful maintainer advice`

---

## 16. Tuning versus experimental overfitting

Some tuning is legitimate when:

1. a specific observed symptom exists;
2. there is a justified hypothesis;
3. a bounded setting is changed;
4. the new configuration is versioned separately;
5. prior failure remains retained;
6. we do not reinterpret correlation as cause.

Weak evaluation looks like:

`failure -> tweak prompt -> increase tokens -> change sampler -> change thinking -> change runtime -> eventually pass -> declare model good`

That can overfit the deployment to the canary/evaluation rather than establish general behavior.

---

## 17. What the actual model runs taught us so far

Avoid memorizing revision numbers. Think in terms of three meaningful experimental horizons.

### A. Complete six-candidate thinking-off cohort on the earlier backend

All six selected models were actually tested across Raw/Structured and short/near-envelope synthetic sequences.

Observed interface outcomes:

- Gemma 12B: 4/4 interface sequences qualified.
- Qwen 27B: 4/4 qualified.
- Qwen 9B: both Raw sequences passed; both Structured sequences were withheld because reports omitted eligible citations.
- Gemma E2B: 0/4.
- Gemma E4B: 0/4.
- MiMo 9B: 0/4.

Important semantic observations remained separate from those interface dispositions. For example, an interface-qualified report could still make an unsupported “proceed/update-ready” inference.

### B. Native thinking-on follow-up for E2B/E4B/MiMo on the newer backend

At separately declared native sampler/thinking configurations:

- Gemma E2B: 2/4, overall withheld.
- Gemma E4B: 4/4, canary-qualified at that exact configuration/runtime.
- MiMo 9B: 2/4, overall withheld.

This does **not** prove thinking alone caused Gemma E4B’s improvement because backend, sampler, generation allowance and other runtime conditions also changed.

### C. Current-runtime completion after backend changed

Because the backend/runtime changed, earlier passes could not simply be inherited as current-runtime qualification.

At the latest consolidated learning horizon:

- Qwen 9B has completed 4/4 current-runtime interface canaries.
- Gemma 12B has completed 4/4 current-runtime interface canaries.
- Qwen 27B has completed both short current-runtime sequences; its two long sequences remain pending at this horizon.

Semantic review still remains separate. Qwen 9B’s Raw-long report made an unsupported proceed recommendation. Gemma 12B’s reports included broader readiness/informativeness issues despite interface passes. A later review refined some criticism: a visible failure observation may have had no citable typed reference, so absence of citation should not be treated as proof the model failed to see it.

The real HTTPX/glyphsLib semantic comparison remains unactivated at this horizon.

---

## 18. What interface qualification does and does not establish

A qualified synthetic interface sequence can establish that the deployment, under that exact configuration, successfully:

- received/measured the intended request;
- interacted through the closed tool protocol;
- performed required synthetic operations;
- respected reference rules sufficiently for the assessor;
- completed and published the bounded report.

It does not establish:

- dependency compatibility;
- correctness on a real repository;
- recommendation/action permission;
- maintainer usefulness;
- general semantic reliability;
- superiority over another model;
- production performance under concurrency;
- optimal sampling/context/offload settings.

This separation is intentional.

---

## 19. The central evidence discipline

Several distinctions should now be automatic:

- **request != observation**;
- **observation != broad semantic truth**;
- **visible observation != necessarily citable typed reference**;
- **internal ID != citation authority**;
- **valid citation != proof that the claim is entailed by that evidence**;
- **valid JSON != correct reasoning**;
- **interface qualification != semantic correctness**;
- **semantic correctness != maintainer usefulness/action permission**;
- **requested configuration != applied runtime configuration**;
- **applied configuration != successful behavior**;
- **mathematical capacity fit != actual generation adequacy**;
- **same model asset != same deployment**;
- **old deployment pass != current-runtime pass after material runtime change**.

This chain is the core of the cycle.

---

## 20. How to reason about future failures

For any future result, ask in this order:

1. **What exact deployment was tested?**
2. **Did the runtime actually apply what we requested?**
3. **Was the model given complete allowed context/history?**
4. **What observations were actually returned?**
5. **Which observations had eligible typed references?**
6. **Did the model satisfy the interface/protocol?**
7. **Did the final claims stay within the evidence?**
8. **What remains unknown?**
9. **Is the problem ours (interface/runtime), the deployment’s behavior, or unresolved?**
10. **What is the smallest discriminating next experiment, if another experiment is justified?**

Do not jump directly from “the report looks wrong” to “change model settings.”

---

## 21. What remains before formal D/E

Our learning preparation is largely complete. We should not invent more learning questions merely to continue the exercise.

The correct sequence is:

1. let the current bounded main qualification finish;
2. inspect the final retained main evidence;
3. update the per-model/configuration dispositions from that final evidence;
4. compare what actually happened against the earlier A2 expectations;
5. identify only genuinely new learning gaps;
6. reconcile this learning branch so stale statements are not merged;
7. fold only supported learner-owned conclusions into canonical D;
8. close/defer remaining gaps through E;
9. only then select/activate the next responsibility, including any real semantic comparison.

The temporary learning branch should therefore not be merged blindly before final reconciliation.

---

## 22. Compact mental model

If only one model of the whole cycle is remembered, use this:

### Product/evidence side

`Workspace owns durable evidence/state`

`model request = intent`

`returned observation = delivered data`

`typed delivered reference = citation authority`

`validator/evaluator = decides whether output is admissible/supported`

### Runtime side

`model asset + exact runtime/template/context/placement/sampler/thinking/transport = deployment`

`requested configuration -> verify actual applied state`

`canary pass -> interface readiness only`

`real-case evidence review -> semantic question`

`independent product/usefulness evaluation -> maintainer/action question`

### Scientific side

`observe -> classify -> preserve -> hypothesize -> bounded change -> separate result`

Never:

`assume -> tune until pass -> merge everything -> overclaim`

---

## Final learner-owned statement

The purpose of this qualification work is not to find settings that make every model pass. It is to learn exactly which local deployment configurations can operate UpgradePilot’s Investigator interface, under which observed runtime conditions, with which failure modes and evidence limits.

The system must preserve a strict distinction between what we intended, what the runtime actually did, what evidence the model actually received, what references were actually authoritative, what the model actually produced, and what those outputs truly establish.

That discipline is what lets later semantic and maintainer-facing evaluation mean something.