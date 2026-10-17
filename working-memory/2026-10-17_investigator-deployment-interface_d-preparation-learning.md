# Investigator deployment/interface — D preparation learning companion

**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Base:** `main@a95c2369c71fcb8e8824f11181c04b1bb7042ac1`
**Date:** October 17, 2026
**Status:** ACTIVE — learning/D-preparation only; **not** the canonical D owner and **not** formal D completion.

## Purpose and boundary

This companion records targeted learning while the main deployment/model-interface cycle remains in B/Verification. It exists so the eventual formal D can review and consolidate already-owned understanding instead of repeating a long onboarding.

It must not:

- change `main`, live `MEMORY.md`, experiment code, model configuration, budgets or qualification outcomes;
- run or resume model inference;
- relabel failed/withheld/partial results;
- declare deployment qualification, semantic quality, usefulness, B completion, D completion or E disposition;
- replace the canonical deployment-cycle record or its evidence.

When B is actually complete, reconcile this companion against the final B evidence. Only supported learning should be folded into the canonical D record; stale questions/answers stay historical rather than being copied blindly.

## Minimal learning plan

### L1 — Real local-LLM execution pipeline

Own the concrete path:

`UpgradePilot request -> chat/template rendering -> tokenizer/token IDs -> special tokens -> context admission -> LM Studio/llama.cpp backend -> CPU/GPU/KV placement -> generation/sampling/thinking -> streamed fragments/usage -> SDK -> strict Investigator adapter`.

Target concepts: token, tokenizer, chat template, BOS/EOS, context window, input tokens, generation reserve, sampler, temperature/top-p/top-k, reasoning/thinking mode, backend, SDK, GPU offload, KV cache, requested versus actually applied configuration.

Use the real `1817 measured / 1818 runtime` prompt-count discrepancy and later small-Gemma BOS observations as the primary example.

#### Runtime-control subtopics placed into the existing questions

These are **not eleven new ownership questions**. They are deeper runtime topics to learn when their parent question or a later optimization responsibility makes them relevant.

- **Q3 — context/capacity:** RoPE Frequency Base and RoPE Frequency Scale. Learn their positional/context role at a conceptual level with Q3; defer tuning details unless we deliberately study context extension or positional scaling.
- **Q4 — runtime placement/memory/prefill:** evaluation batch size, physical/micro-batch size, max concurrent predictions, unified KV cache, `mmap`, Flash Attention, K-cache quantization type and V-cache quantization type. Learn enough under Q4 to understand what resource/runtime dimension each controls; detailed benchmarking belongs to a later performance responsibility.
- **Q5 — generation configuration:** speculative decoding belongs with next-token generation/sampling because it changes the decoding path and introduces a draft deployment. Learn the concept with Q5; do not treat it as part of current r6 unless explicitly selected/frozen.
- **Q10/Q13 — experiment identity:** if any material runtime control above changes between experimental revisions, decide whether that creates a different deployment/configuration and preserve comparability rather than pooling results blindly.

The current learning goal is therefore to know **what each knob controls and when it matters**, not to optimize every knob during interface qualification.

### L2 — Stateless history, observations and reference authority

Own why r5's earlier "complete stateless history" was incomplete and why r6 retains exact model request/result pairs.

Target distinctions:

- model request/intent != returned observation;
- observation != semantic truth;
- prior model request text != evidence authority;
- internal native record/delivery/catalog ID != delivered typed citation reference;
- canonical packed/accounting representation != model-visible presentation, while both must correspond losslessly;
- omitted evidence/history cannot remain silently usable.

### L3 — Qualification experiment mechanics

Own the chain:

`candidate -> exact deployment configuration -> preflight -> freeze -> independent canary sequence -> model calls -> strict assessor -> qualified/withheld/partial -> deployment disposition`.

Understand Raw versus Structured, short versus near-envelope, correction allowance, budgets, why one passing sequence does not qualify a deployment, why revisions r3/r4/r5/r6 remain separate, and why synthetic interface qualification does not establish semantic correctness or maintainer usefulness.

### L4 — Failure diagnosis and repair discipline

For each real failure, identify the strongest justified class before deciding whether to repair, rerun, preserve, or withhold:

- experiment/interface defect;
- runtime/configuration correspondence failure;
- interruption/incomplete evidence;
- model interaction/instruction-following failure;
- reference/citation-use failure;
- generation/resource limit;
- semantic-quality problem.

Use actual examples: BOS +1 mismatch; LM Studio `terminated`; missing request arguments in history; MiMo repeated operations; Qwen9 Structured reports with no eligible citations; Gemma12 internal-record-ID citation; 2048-token exhaustion/repetition; reasoning-labelled fragments while thinking-off was required; requested GPU ratio versus variable actual layer placement.

### L5 — Per-model and cycle-state synthesis

After L1-L4, summarize each candidate only from retained evidence:

- Gemma 4 E2B
- Gemma 4 E4B
- MiMo-V2.6-Distill-Qwen-9B
- Qwen3.5-9B
- Gemma 4 12B
- Qwen3.8-27B

For each: what worked, what failed, failure class, what remains unknown, and what the next discriminating experiment is intended to establish. Keep interface qualification separate from real HTTPX/glyphsLib semantic comparison.

## Deferred runtime-performance learning/optimization queue

This queue prevents useful LM Studio/llama.cpp controls from being forgotten without turning the current qualification into a parameter sweep. It is **not automatically selected implementation work**.

When model/interface qualification is stable and a performance/resource responsibility is selected, revisit:

1. evaluation batch size and physical/micro-batch size — prompt/prefill throughput versus memory pressure;
2. Flash Attention — attention memory/throughput and actual-kernel verification rather than requested-setting assumptions;
3. KV-cache placement and K/V quantization — memory, speed and any quality/correctness trade-offs;
4. speculative decoding — main/draft compatibility, generation throughput, memory/accounting and deployment identity;
5. `mmap` — load/startup and host-memory/page-cache behavior if loading becomes a bottleneck;
6. max concurrent predictions + unified KV cache — only when concurrent investigators/agents or serving throughput becomes a real requirement;
7. RoPE base/scale — only for an explicit context-extension/positional-behavior question, not routine tuning.

For any selected benchmark, freeze model/template/context/sampler/reasoning/evidence task and change only the intended runtime dimension where possible. Measure at least prompt time/TTFT, generation throughput, RAM/VRAM, stability and correctness guardrails. Requested configuration never substitutes for observed applied/runtime state.

## Ownership questions

These questions are the learning gates. Answers may be brief, but should be in Ali's own words. They are not pass/fail trivia; unclear answers identify the next teaching target.

### A. Request-to-model fundamentals

**Q1.** Starting from an UpgradePilot Investigator request, what are the major steps before the model produces its first visible token? Where do the chat template, tokenizer, LM Studio, llama.cpp/backend, GPU/CPU placement and SDK each belong?

**Q2.** What is a token? What are BOS and EOS? Why could our rendered/tokenized request measure 1817 tokens while the runtime reports 1818, and why is that one-token difference important rather than harmless bookkeeping?

**Q3.** What is the difference between the context window, current input tokens and generation/output reserve? Why does `input + output reserve + margin < context` prove capacity admission but not prove that the model can generate the full reserve correctly or quickly? Runtime supplement: know that RoPE base/scale affect positional/context interpretation; detailed tuning is deferred unless context extension becomes an explicit responsibility.

**Q4.** What do GPU weight offload and KV-cache placement mean, and why did `requested offload ratio = 1.0` fail to prove actual full GPU placement for MiMo/Qwen9? Runtime supplement: identify the roles (not yet optimize) of evaluation batch size, physical/micro-batch size, max concurrent predictions, unified KV cache, `mmap`, Flash Attention and K/V cache quantization.

**Q5.** What do temperature, top-p and top-k control at a high level? Why must a model-specific native-mode follow-up with different sampling/thinking settings be treated as a different deployment configuration rather than pooled with r6? Generation supplement: understand speculative decoding and why enabling a draft model changes the decoding/deployment configuration.

### B. Stateless history and evidence/reference authority

**Q6.** What do we mean by a "complete stateless request"? Why was r5's earlier representation not actually a complete interaction history even though previous observations were included?

**Q7.** Explain the difference among: previous model request, Workspace observation, delivered evidence reference, internal native record ID and a final citation. Which of these can authorize a report citation, and why?

**Q8.** Why is it acceptable for r6 to keep canonical packed bytes for accounting while presenting the same information to the model in a more readable fixed-first request/result format? What correspondence must still be preserved?

**Q9.** Suppose a previous model request contains a forged-looking typed reference ID, but no returned observation delivered that reference. Why must that ID remain ineligible even though the current stateless request lets the model see its own old request?

### C. Qualification design

**Q10.** What is the difference between a model candidate, a deployment/configuration, a canary sequence and the later semantic case assignment? Include why material runtime controls can be part of deployment identity when they change execution behavior/resources.

**Q11.** Why do we test both Raw and Structured treatments and both short and near-envelope sequences? What distinct failure would each dimension help expose?

**Q12.** Why does `Raw short qualified` not mean the whole deployment is qualified? What must be true before a deployment can be admitted to the later paired semantic comparison?

**Q13.** Why can't we simply combine successes from r3/r4/r5/r6 as if they were one experiment? What kinds of protocol/configuration changes make the revisions non-poolable? Apply the same reasoning to later runtime optimizations instead of silently pooling materially different configurations.

### D. Reading failures correctly

**Q14.** Classify each of these and state what it establishes versus what it does not establish:

1. prompt usage is rendered-token-count +1;
2. LM Studio returns `Chat response error: terminated` with unknown final usage;
3. MiMo repeatedly performs the same operation;
4. Qwen9 Structured reaches a report but cites no eligible evidence;
5. Gemma12 cites an internal native record ID instead of the delivered typed reference;
6. a report reaches the 2048-token ceiling while repeating claims;
7. reasoning-labelled fragments appear while the frozen deployment requires thinking off.

**Q15.** When is a failure evidence that our interface should be repaired, and when should it remain a genuine model/deployment failure? Why is "change things until the model passes" scientifically weak?

**Q16.** What is the difference between an interface-qualification success and semantic correctness? Use the Qwen9 Raw result as an example: how can an interface pass coexist with overbroad/unsupported claims?

### E. Current evidence and next discriminating work

**Q17.** In your own words, what did r3, r4, r5 and the partially published r6 each teach us? Name the main reason each revision existed rather than listing every commit.

**Q18.** Based on the currently published checkpoint, what is established and not established for each of the six candidates? Do not infer final r6 results that are not published.

**Q19.** Why can a bounded native-mode follow-up for E2B/E4B/MiMo be technically justified without erasing their r6 failures? Why must native-mode outcomes remain separate from r6 and from the later semantic comparison?

**Q20.** Before formal D closes, what should we compare between A2 expectations and actual B evidence? Which surprises materially changed our understanding of the model/runtime/interface boundary?

## Suggested learning order

Use this sequence unless a live B result later makes another dependency more urgent:

1. Q1-Q5 with the real request-to-first-token pipeline; cover only the conceptual runtime supplements needed now.
2. Q6-Q9 with r5 -> r6 stateless-history repair.
3. Q10-Q13 with the actual qualification/freeze design.
4. Q14-Q16 using real failure records one by one.
5. Q17-Q20 only after the mechanics are understood; use them as synthesis/D-preparation.
6. Revisit the deferred runtime-performance queue only when a performance/resource/concurrency/context-extension responsibility is selected; do not delay current D merely to benchmark every LM Studio knob.

Avoid answering all twenty at once. Work in small groups, correct misconceptions immediately, and record only stable learner-owned conclusions.

## Learner-owned conclusions

### Q1 — request to validated output

Ali's explanation, reviewed October 17: UpgradePilot first renders its request through the selected model's chat template, then tokenizes that rendered representation into token IDs. LM Studio orchestrates the loaded local deployment and llama.cpp performs the underlying inference. Model layers may be placed partly in GPU VRAM while remaining layers are CPU-executed from system RAM. The model generates subsequent tokens, the LM Studio SDK carries the streamed result/configuration/usage back to Python, and UpgradePilot's adapter/validators decide whether the generated output is admissible. Refinement retained: LM Studio and llama.cpp are different layers, and GPU weight offload should not be described as a separate "offload to RAM" operation.

**Q1 status:** OWNED at the current learning depth.

### Q2 — tokens, BOS/EOS and runtime correspondence

Ali's explanation, reviewed October 17: a token is a unit selected from the specific model tokenizer's vocabulary and represented by an ID; tokenization can differ between models. BOS/EOS are special sequence-boundary tokens. The important meaning of the `1817 measured / 1818 runtime` discrepancy was not the capacity cost of one token but evidence that our assumed input/runtime model did not yet exactly correspond to what the backend actually consumed. Therefore the extra transformation had to be identified/represented rather than dismissed.

**Q2 status:** OWNED at the current learning depth.

### Q3 — context capacity versus demonstrated behavior

Ali's explanation, reviewed October 17: the context window is the total token capacity available to the model for the sequence; input tokens occupy capacity before generation and an output reserve is capacity intentionally kept available for possible generation. `input + reserve + margin <= context` establishes admission/capacity fit only. It does not establish correct model behavior, successful use of the full reserve, semantic quality, latency or generation performance. Refinement retained: reserved output capacity is not the same as actual generated-token count.

**Q3 status:** OWNED at the current learning depth. RoPE base/scale remain a queued deeper supplement rather than a prerequisite for this ownership.

## Formal-D reuse criteria

When canonical B/Verification is complete:

1. Rebase/reconcile this branch against the final B evidence; do not assume the current `a95c2369` horizon is final.
2. Review Q1-Q20 and mark which answers are genuinely owned, partially owned, contradicted by later B evidence or still open.
3. Map owned learning into canonical D responsibilities:
   - actual runtime/interface model versus A2 expectations;
   - failure ownership and repair decisions;
   - evidence limits and deployment dispositions;
   - remaining unknowns/debt.
4. Do not copy temporary branch statements that became stale.
5. Merge only the supported D learning/conclusions after canonical D is selected; leave implementation and experiment evidence owned by their main-branch records.
6. Do not make deferred runtime-performance optimization a blocker for D unless final B exposes it as necessary to interpret a qualification result.

## Progress

- [ ] L1 request-to-model pipeline owned
- [ ] L2 stateless history/reference authority owned
- [ ] L3 qualification mechanics owned
- [ ] L4 failure diagnosis/repair discipline owned
- [ ] L5 per-model/current-state synthesis owned
- [x] Q1 answered/reviewed
- [x] Q2 answered/reviewed
- [x] Q3 answered/reviewed
- [ ] Q4-Q5 answered/reviewed
- [ ] Q6-Q9 answered/reviewed
- [ ] Q10-Q13 answered/reviewed
- [ ] Q14-Q16 answered/reviewed
- [ ] Q17-Q20 answered/reviewed
- [ ] Q3 supplement: RoPE base/scale reviewed if/when context-extension work is selected
- [ ] Q4 supplement: batch/concurrency/unified-KV/mmap/Flash/KV-quantization reviewed at appropriate depth
- [ ] Q5 supplement: speculative decoding reviewed at appropriate depth
- [ ] Deferred runtime-performance characterization selected/reviewed if product needs justify it
- [ ] Reconciled against completed B evidence
- [ ] Folded into formal canonical D
