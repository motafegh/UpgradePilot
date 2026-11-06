# Caller-Signature Native Pipeline — Living Learning and Mastery Roadmap

**Created:** 2026-11-02  
**Initial evidence horizon:** `7a9bef12fb65ee075dab645a638adf5a3955dc48`  
**Last synchronized main:** `bb3b2b10636734d5622727558053ec063df8d65f` — November 6, 2026; bounded native paging/view and transaction-local basis reuse now verified for retained HTTPX, connected retained qualification closed, and a matched page-timing study completed with **elapsed result inconclusive**. Next product handoff is a separately frozen normal-product attempt contract before any live provider call. Learning C1 remains conceptually covered; C2 is in progress. Product status ≠ learner mastery.
**Working branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`  
**Purpose:** living study/relearning roadmap for Ali's interactive learning track while UpgradePilot continues to evolve on `main`.  
**Authority boundary:** this file is a learning artifact, not the live project-position owner. `MEMORY.md`, current source/tests, accepted plans/specifications/ADRs, and dated evidence remain authoritative.

`UP-SKILL:upgradepilot-learning-artifact`

---

## 1. Learning method and anti-rabbit-hole rule

For every module use:

`verified real UpgradePilot case/problem → plain-language system responsibility/layer → what failed or needed explanation → how actual source/evidence flows and why our method exists → alternatives/failure/proof limits → proportionate learner reasoning → stop`

**Use descriptive lesson identity in every teaching turn.** The codes `A3`, `C2`, etc. are roadmap locators, **not vocabulary Ali must memorize**. Introduce each chunk as `code — meaningful responsibility (layer/component and what it handles)`, e.g. `C2 — Historical result reconstruction (native codec/result decoder: preserve and validate saved source-analysis evidence)`. Even when continuing a chunk, briefly locate it in the product flow and explain the immediate responsibility; do not refer to `A3` or `C2` alone or require recalling past code labels. Refer back by descriptive responsibility (e.g. “the imported-origin analyzer”) and only add its code when useful for navigation. The expanded module headings below supply those labels; avoid inventing alternative names that conflict with their actual ownership.

### Real-case-first teaching protocol

**Normal lesson opening must use an existing genuine source/evidence case**, not a generic `pkg/f` toy. Establish concretely: *which repository/dependency update or actual system incident; what source or saved result we genuinely possess; what happened or was observed; why the engineering issue matters; where it enters/leaves UpgradePilot; and which proof/unknowns remain.* Show a **small exact source snippet or a faithful selected record**, with a repository/evidence link and horizon when available. Introduce the abstraction or data structure only after that problem is understandable.

**Label realism/provenance accurately:**
- **Retained real public-source case** — genuine earlier repository/source/PR material with recorded provenance and gaps; historical retention is not fresh live provider observation.
- **Controlled replay/composition** — actual product pipeline operating on retained source bytes but authored provider inventory/HTTP responses; proves the controlled path, not authentic historical response capture or independent transfer.
- **Observed engineering failure/repair** — actual project evidence, negative run, correction and verification (e.g. the six-page native-access refusal and later bounded recovery).
- **Synthetic fixture / hypothetical illustration** — deliberately constructed to isolate an invariant or counterexample; not a real PR or an observed production failure.

Use **a real case as the narrative spine** and one related source path, actual findings, failure/recovery evidence and targeted tests. Use tiny fixtures only *after* the real case when necessary to distinguish a mechanism or prove a negative branch, and explicitly connect them back. Never present a corruption injected by a unit test as an observed real-case defect. If no adequate real retained evidence exists for a specific low-level behavior, **say exactly what is unobserved**, use the nearest relevant real case to explain the need, then a clearly labelled narrow test for the invariant; do not fabricate real observations or force a tangential case. If the real case is too complex, first orient with its real-world problem and then zoom in to the smallest explanatory slice. Avoid an entire repo walkthrough.

**Teach the causal chain behind each example and test.** Explain not just why a particular code line appears, but which real product or engineering pressure made that *behavior* worth supporting and testing. Use a short chain: observed source/use case or documented failure → engineering requirement/risk → selected implementation and alternative → reason for the specific test fixture and its assertions → what was and was not proved. A deliberately artificial fixture should still be tied to the real class of problems that motivated the design; the fixture's lack of business meaning does not mean the engineering mechanism lacks one. Distinguish documentary design motivation from reasoned hypotheses; when historical intent is unrecorded, identify the risk supported by implementation and tests without claiming to know the author's private motivation. Explain the context of repeated source calls and distinguish distinct lexical call sites from observed runtime execution. Keep the causal explanation proportional, using actual captured cases when available.

**Comprehension before quiz.** Before checking recall of an encoding index, version field or AST helper, establish the basic problem and concrete input → producer → retained material → consumer flow. Demonstrate why our chosen design helps, why an alternative could fail or cost more, and what this example actually proves. If Ali says the mechanism is still unclear, re-teach from the real case, not a reformulation of the toy example; do not treat immediate repetition or a guessed answer as mastery. Preserve feedback as a learning gap without altering prior covered-module truth. A real case should make the learner able to understand and challenge the engineering decision, not memorize the test's artificial scenario.

Use [Operating Guide §7.2](../OPERATING_GUIDE.md#72-ai-assisted-engineering-ownership) for depth and [§7.3.1](../OPERATING_GUIDE.md#731-practical-attempts-and-evidence) for practical attempts. For a selected activity, establish its prerequisites, let Ali attempt it before supplying the complete answer, then inspect the actual result and assistance needed. Teach new material first. Learning-Only does not authorize product changes; a proposed modification and an implemented/verified modification are different evidence.

Depth:

- **MUST OWN** — reason about, review, challenge, modify/test, and explain with limited assistance.
- **OPERATIONAL** — trace/debug/review safely; exact helper details may be looked up.
- **LOOKUP** — recognize and recover when needed; do not spend session time memorizing it.
- **DEFERRED** — real depth that does not unlock the current project responsibility.

Do not turn a module into a general course on Python ASTs, compilers, networking, packaging, GitHub APIs, `requests`, persistence, or static analysis unless a real UpgradePilot problem requires that depth.

### Mechanism-first teaching, relevant transfer and professional relevance

These **enhance existing learning chunks**; they are not new modules, quizzes, phases or checklists to exhaust for every minor function. `OPERATING_GUIDE.md` [§4.3](../OPERATING_GUIDE.md#43-rationale-necessity-and-engineering-judgment), [§7.2](../OPERATING_GUIDE.md#72-ai-assisted-engineering-ownership) and [§7.3](../OPERATING_GUIDE.md#73-professional-engineering-ownership-lens) remain the authoritative methodology; this roadmap says how to apply it on the caller-signature route.

**1. Implementation mechanism / engineering judgment.** When teaching a material product responsibility, go beyond naming its input/output: explain the concrete problem/requirement, *how our current implementation accomplishes it*, the relevant code mechanism (selected function/type/branch/state transition/data edge), why it exists or was chosen when justified by evidence, the meaningful alternative/trade-off, the failure it prevents or admits, and what tests do or do not prove. Show only representative source and enough Python syntax/control flow to let Ali reason, diagnose, review or propose a change later—**not a line-by-line tour**. Distinguish verified implementation fact, evidenced design rationale, current judgment and contract authority. Unknown or disputed rationale stays explicitly unknown; working code is not proof that the design is optimal.

**2. Related real-world engineering problems, when illuminating.** After the project case, connect the core mechanism to one relevant practical problem elsewhere (e.g., CI job timeouts, security-event evidence correlation, unreliable API calls, bounded static-analysis work, transactional checkpoint recovery), explaining *which principle transfers and what assumptions differ*. Prefer a verified real incident/example where appropriate; otherwise label a parallel case as an illustrative analogy, not externally confirmed history. Do not add loosely related technology courses or imply an analogy is new UpgradePilot evidence.

**3. Job-relevant engineering competence, when material.** Identify at most one or two specific professional capabilities exercised by the actual responsibility (e.g., causal diagnosis, bounded process isolation, provenance and trust validation, test design, persistence correctness, API recovery, architectural trade-offs or AI-assisted code review). Connect the capability to something Ali can explain, test, troubleshoot, challenge or modify; include a concise technical-communication/interview framing only if helpful. Never assert an unverified current job-market requirement, turn every symbol into a résumé keyword, assign hiring scores, or let hiring trends redirect the project's technical sequence. Career owns formal job-readiness/market assessment.

**Reusable teaching move, proportionate to the slice:**

`named real public-source or actual product incident → problem and its product-layer owner → exact observed source/result → our mechanism in selected code → rationale/credible alternative → real validation and proof limit → optional real-world/career transfer → one fair ownership attempt`

A clear example may combine several moves; skip transfer/hiring commentary where it would be filler. For a previously learned mechanism, use a changed **real** case or actual failure diagnosis before replaying a full lecture when such evidence exists. Do not assume prior lesson codes or raw structure names are remembered. Existing coverage and mastery evidence rules remain unchanged.


Status:

- ✅ covered interactively; no independent-mastery claim
- 🟡 introduced/partially covered
- ⬜ planned
- 🔁 revisit because `main` changed the learned responsibility

These marks describe lesson coverage. When actual evidence exists, separately preserve **practised with assistance** or **demonstrated with limited assistance**, naming the activity, result, help and transfer limit in the selected module or existing learning-continuity record. No new tracker is required. This amendment adds targets/opportunities, not evidence that Ali performed them; earlier coverage marks remain unchanged.

### Scoped depth targets and when they matter

A module's **MUST OWN** label is a target for its important responsibility, not every helper and not proof of achieved ability. The following scope distinctions refine those broad labels. State the ability needed now, the reason, supporting lookup detail and the next evidence/re-entry condition when selecting a module. The existing learning order remains the route; this table does not make every later target an immediate Build prerequisite.

| Responsibility | Ownership target and reason | Supporting depth / timing |
|---|---|---|
| Evidence meaning, bindings and local argument comparison (covered foundations) | MUST OWN the distinctions that prevent false origin, execution or compatibility claims; connect important branches to real calls/tests. | Tree-walking utilities, exact syntax APIs and incidental helpers are OPERATIONAL/LOOKUP until a change requires them. Coverage is not independent implementation evidence. |
| Correspondence and whole-file/paired work admission | MUST OWN conditional paths, old/proposed pairing, omission/refusal and why completion differs from coverage; needed to interpret or change the analyzer honestly. | Traversal/index implementation is OPERATIONAL initially; deepen the affected mechanism for modification or diagnosis. This is the selected learning responsibility, not a new route. |
| Worker execution and fixed reconstruction | MUST OWN input/result versus execution state, resource failure and corrupt/unsupported relationships; required for safe result and recovery interpretation. | Process-launch/codec plumbing is OPERATIONAL; OS/library internals are LOOKUP unless the selected failure/change depends on them. Learn through the corresponding modules. |
| Native families, method versions and Workspace recovery | MUST OWN evidence membership, producer-versus-codec meaning and confirmed publication/recovery boundaries; otherwise valid objects could support invalid claims. | Exact version strings and encoding helpers are LOOKUP; store/codec implementation is OPERATIONAL until modifying it. Learn these boundaries before owning their composition. |
| Shared acquisition policy and ledger | MUST OWN prefix/retry/byte/time accounting and the difference between account quota and local policy; needed to preserve invocation limits. | HTTP client APIs are OPERATIONAL; library transport internals are LOOKUP unless diagnosing them. This does not require a networking course first. |
| Target source context | MUST OWN exact target revision, selected/omitted files and candidate-versus-installed-origin meaning; needed to explain acquisition coverage. | TOML/requirements parser details are OPERATIONAL/LOOKUP until a genuine parsing responsibility requires depth. |
| Exact dependency source and partial receipts | MUST OWN association premises, version/sample distinction, cached failures and live-only versus retained observations; needed for source-progress composition. | Provider-specific helpers are OPERATIONAL/LOOKUP. Understand what a content hash establishes; cryptographic algorithm implementation is LOOKUP. |
| Ordinary source publication/application/profile/report/recovery | MUST OWN the source/publication, confirmed/attempted revision, report/file delivery and exact cold-opening claims when learned. | Connected source application and ordinary explicit CLI delivery are verified for their controlled and installed scope; F1/F2 remain learning-pending. Live-provider and usefulness gates remain distinct. |
| Task qualification and later runtime checkpoint | MUST OWN qualification/non-proof and adoption reasoning when that gate is reached. | New runtime observer design remains DEFERRED; recognize existing scoped CI/runtime evidence without speculating a new runner. |

Revisit a depth when a real change/failure needs it, a fair attempt exposes a missing prerequisite, or the responsibility changes. The teacher recommends the depth with its rationale before asking Ali to choose an unfamiliar trade-off. Preserve a gap and its consequence rather than either silently lowering the target or making unrelated internals compulsory.

### Practical opportunities within the existing route

Select an opportunity when its module and prerequisites are active; these examples are not a second execution order or a quota. Teach the concrete retained/observed case and the actual source or result **before** using controlled tests as supporting proof. A synthetic control is a secondary instrument, not the storyline; do not invent a production defect, pretend retained source is new live observation, or rewrite frozen evidence.

- **Correspondence/admission:** use retained LifeLog or Digimon to explain the paired/whole-file boundary, then inspect [the atomic native-group refusal test](../tests/test_source_correspondence.py). Let Ali predict which material remains retained and which work is unexamined under the authored limit before revealing the assertions. Interpret a related limit/case with reduced prompting; one guided answer does not establish broad analyzer ownership.
- **Acquisition ledger:** trace [the normal-prefix/later-client accounting test](../tests/test_caller_signature_acquisition.py), identify the charged timeout/retry and explain why a later stage does not receive another budget. Let Ali select a discriminating assertion or related-case check before presenting one; this controlled transport is not live provider proof.
- **Partial source receipts:** trace `examine_with_receipt` and [the failed-file preservation/no-retry test](../tests/test_caller_signature_source_acquisition.py). Distinguish earlier association/metadata/tag premises from unavailable text/hash and from the separate failed-association live-only limit. Ask for a related diagnosis or proposed source/test change; record whether it was only proposed or actually implemented and verified within authorization.
- **Connected source publication (now implemented, F1):** trace the controlled [`partial-source-before-analysis`](../tests/test_caller_signature_source_acquisition.py) and [`source-publication-failure`](../tests/test_caller_signature_source_acquisition.py) tests; predict what persists when the proposed file is unavailable or the later worker/write fails, then inspect assertions and the retained exact basis. Once F2 is built, use [`test_workspace_checkpoint_store.py`](../tests/test_workspace_checkpoint_store.py) for selected revision / lost acknowledgement distinctions; current store-only tests do not prove the CLI.

---

## 2. Main-sync protocol

When `main` advances:

1. compare current `main` with this roadmap's last synchronized horizon;
2. inspect `MEMORY.md`, active cycle/handoff, changed owners/tests/evidence;
3. classify new work:
   - extends a future module → add there;
   - changes a learned prerequisite → mark `🔁` and learn the delta before continuing;
   - creates a new architecture/trust/proof boundary → insert at the dependency-correct point;
   - implementation detail without current ownership value → LOOKUP/defer;
4. never erase historical learning truth or relabel passive coverage as mastery;
5. continue from the earliest module whose understanding is required by current architecture.

### Sync log

- `7a9bef12...` — native source/comparison families + checkpoint recovery qualified.
- `9c903926...` — **9 commits later**: product-owned acquisition policy/shared physical-request ledger, target source-context acquisition, exact dependency source acquisition/association/module receipts qualified. Source-family composition/Workspace source-progress publication and ordinary app/profile/CLI/report delivery remain next. A later combined-evidence/runtime-applicability design checkpoint is scheduled, not implemented.
- `834aeaa4` — November 3: scoped depth and practical-attempt method; documentation validation, not product qualification or independent learner reassessment.
- `58bdf1e4` — November 3: source-progress composer and connected application stage qualified. One shared PR prefix/transport ledger; target + old/proposed source receipts and repeated partial Workspace publication **before** analysis; exact published source basis to bounded worker; fresh-process partial recovery. Corrected write-failure handling preserves the original `OSError` and earlier committed progress. Retained verification: 1,041 product / 194 experiment API / 7 architecture and four installed composition controls; not rerun here.
- `c136d2a0` — November 3: explicit caller-signature CLI/report/source/save/offline-opening delivery cycle opened (not yet implemented).
- `e109875f` — November 4: storage/acknowledgement foundation, 63 host/store focused checks; CLI integration pending *at that historical horizon*.
- `8d6f3d09` — November 4: user delivery subsequently verified (explicit profile, CLI/report/source/save/exact offline opening), with 1,063 product, 194 experiment API, 7 architecture and 20 installed controls recorded at its milestone. Connected retained-case qualification is active in B: LifeLog/HTTPX/Digimon retained equivalence and ordinary controlled acquisition examined; HTTPX default adapter allocation 2 vs 4 corrected under unchanged global budgets (latest reported 1,064 product/194 API/7 architecture). Fixed source navigation and final qualification remain pending. No fresh live provider/usefulness claims. These are referenced dated proofs, not rerun by this learning update.
- `068ba7b4` — November 4: original retained qualification showed **six-page native refusal** at the 64MiB original-material closure guard, and fixed source-only navigation retrieved 14/20 required locations. Earlier acknowledged results remained readable. This **historical failed attempt is preserved**, not retrospectively passed.
- `38741c3c` — November 4: bounded repair accepted at the original policy, consumer caches a still-valid equal-native-boundary `ConsumerView` for repeated deliveries; `CheckpointStore.publish` reuses decoded immutable original bases only inside one locked transaction while retaining all historic validation and capacity accounting. The separately frozen retained HTTPX successor completes **60 unique pages**, all **four native witnesses**, with one view/basis and guarded cold recovery; `1,073` product, `194` API, `7` architecture and `57` installed controls at the cited proof horizon. Original six-page refusal remains a negative control; source-only baseline stays 14/20. Connected retained qualification closed; live-provider, human usefulness and broad adoption unproved. A [source-pinned learning companion](2026-11-04-bounded-native-navigation-and-view-reuse.md) now exists on main; use later in D4 rather than duplicate its full narrative here.
- `bb3b2b10` — November 6: frozen matched first-page comparison between consumer-only `6e98d0a0` and publication-reuse `38741c3c`, with six correctly delivered identical 4,873-byte first pages and preserved acknowledgements. Recorded paired **CPU median ratio 0.81265** (~18.7% less CPU in this limited scenario); *elapsed* timing remains **inconclusive** because all trials failed the frozen clock-consistency screens. This was measurement, not a new product optimization or proof of whole-workflow speed. Main's next step is the **contract review for a separately frozen native normal-product attempt**, not provider execution without the contract.

---

# PART A — Covered foundations

## A1 — Evidence meaning: imported origin, source correspondence, argument fit and runtime limits

**Status:** ✅  
**Depth:** MUST OWN

Own these separations:

`static imported origin ≠ source correspondence ≠ local argument fit ≠ runtime dispatch/execution/behavior`

Real anchor: Digimon Requests `2.32.4 → 2.33.0`; direct `requests.get(...)` locally binds while forwarded `request(..., **kwargs)` remains undetermined. Neither proves runtime compatibility.

## A2 — Analysis ownership: one caller-signature product kernel versus experimental adapters

**Status:** ✅  
**Depth:** OPERATIONAL

- qualified analyzer now has one product implementation under `caller_signature`;
- experiment modules are compatibility/adapters, not a second evolving analyzer;
- retained semantic equivalence and installed-wheel proof are stronger than source relocation alone;
- kernel proof is not complete product-feature proof.

## A3 — Imported-origin binding (`bindings.py`): possible source origins, control flow and traces

**Status:** ✅  
**Depth:** MUST OWN

Covered:

- `ImportFact` / `ReferenceFact` / `BindingAssessment`;
- established / conditional / unknown / unbound;
- lexical frames, branch fork/join, rebinding, aliases;
- delayed globals, `global`/`nonlocal`, wildcard imports;
- dynamic namespace operations and conservative mutation invalidation;
- unsupported flow degrades certainty rather than inventing a result;
- trace = provenance/source observations, not runtime execution history;
- resource truncation must weaken certainty.

## A4 — Source facts and argument reception (`analysis.py`): target calls, signatures and conditional outcomes

**Status:** ✅  
**Depth:** MUST OWN

Covered:

- source text → AST → `CallArguments` + `CallableSignature` + `SourceFacts`;
- stable fact identity from type/unit/span;
- parameter kinds and default presence;
- explicit/starred positional and named/`**kwargs` representation;
- binding facts join to calls by exact source span;
- parse/limit failure is not empty success;
- `compare_arguments()` does not choose dispatch;
- receiver modes: `as_written`, `one_receiver_assumed`, `unresolved`;
- result logic:
  - known contradiction → `rejected`;
  - no contradiction + complete checks → `bound`;
  - no contradiction + unresolved information → `undetermined`;
- remaining premises preserve dispatch/version/runtime/decorator uncertainty.

Real anchors: Digimon direct `get`, Requests forwarded `request(..., **kwargs)`, known unexpected-keyword rejection.

Revisit only if `analysis.py` semantics or result truth model changes.

---

# PART B — Correspondence lesson covered; one practical ownership check next

## B1 — Target-to-dependency correspondence (`correspondence.py`): source witness paths and bounded work admission

**Status:** ✅ Covered interactively; guided practice and gap repair completed; **independent mastery not established**  
**Depth:** MUST OWN its source relationship/admission contracts; detailed exotic traversal only when useful

### Conceptual core taught

- `PythonSourceModule` roles and exact source/module identity;
- how retained target calls are conditionally related to old/proposed dependency declarations;
- relationship path steps, root call, selected declaration role, candidate ID and premises;
- direct imported-call/module/member paths traced; initializer/class and factory/protocol routes introduced at operational depth, with exact edge mechanics deferred until a real case needs them;
- what is deliberately not modeled: effective exports, installed namespace, runtime dispatch, full MRO, execution;
- static import-component discovery and root priority;
- whole-file admission;
- atomic old/proposed groups and why torn comparison pairs are refused;
- fact/comparison structure budgets, pair budget and discovery-gap budget;
- retained vs scanned vs analyzed vs unexamined vs unresolved/no-candidate.

### Real anchors

- Digimon direct `requests.get` path;
- LifeLog: 28 retained texts, 10 analyzed Python units, 17 unexamined Python units + one non-Python;
- HTTPX/glyphsLib only where they add a genuinely new path concept.

### Lesson coverage versus remaining practice

We traced Digimon's `requests.get` origin → conditional old/proposed source declaration → local `bound` and forwarded `request(..., **kwargs)` `undetermined`, preserving witness steps and premises. For LifeLog, 28 texts were retained but only 10 Python units analyzed; 17 Python units and one non-Python unit remained outside full Python analysis. We covered whole-file admission, atomic old/proposed groups, two structural work allocations, omission reasons and the distinction between retained/scanned/analyzed/unexamined. **These are taught topics, not an independently assessed engineering result.**

**Guided B1 check (November 4):** Ali identified a definite proposed-version unexpected keyword and correctly refused to infer runtime failure. He initially could not explain atomic `max_facts=1` refusal, and conflated no comparison with an `undetermined` result. After explanation, he correctly identified both dependency units as `unexamined` for `aggregate_fact_budget` and separated absent evaluation from inconclusive comparison. In a changed conditional-rebinding example, he distinguished possible imported origin, selected old `bound`/proposed `rejected`, and missing runtime proof. This is assisted conversational understanding, not an independent test run or implementation demonstration. Revisit practical ownership when a real change requires it; do not block C1.

---

# PART C — Native analysis execution and integrity

## C1 — Bounded analysis execution (`worker.py`): exact input, child execution, run state and result coverage

**Status:** ✅ Covered interactively via guided understanding checks; **independent test/debugging ownership not demonstrated**  
**Depth:** MUST OWN

Anchors: `evidence.py`, `worker.py`, `result_codec.py`.

Own:

- `SourceAnalysisInput` = exact offline analysis material, not acquisition proof;
- `SourceAnalysisRun` lifecycle truth versus `SourceAnalysisResult` semantic coverage;
- completed / failed / timed_out / interrupted;
- completed does not imply complete file coverage;
- parent/child responsibilities, private exchange files, deadline, address-space/result-size limits, kill/reap;
- failed/timed-out runs cannot become empty success;
- installed module-origin proof versus dependency isolation.

Real anchor: LifeLog completed worker with 17 unexamined Python units.

**Guided C1 checks (November 4):** Ali distinguished `SourceAnalysisInput` exact source/role/limits, `SourceAnalysisRun` execution outcome and `SourceAnalysisResult` coverage; completed worker with unexamined files; timeout as failure rather than successful empty result; and original source durability across later failure. Clarified that confirmed Workspace publication—not callback invocation—establishes durable recovery. He correctly rejected a foreign result with unchanged source text but changed input limits. Parent/child boundary, private exchange, deadline, validation and evidence limits were taught. These were chat-based guided predictions, not an independently run test or code modification.

## C2 — Historical result reconstruction (`result_codec.py`, `native_codec.py`): source facts, trace/reference integrity and version guards

**Status:** 🟡 In progress; user reported the synthetic-first shared-trace explanation did **not** establish understanding. Re-teach from a retained real-source/result case before the next check; preserve prior introductory learning without treating it as independent mastery  
**Depth:** MUST OWN

Own:

- decode/reconstruction is not producer execution;
- exact input digest and source/fact/candidate references;
- shared trace referential integrity;
- malformed/foreign reference refusal;
- structural/byte guard meaning;
- node validity does not imply edge validity.

**Concrete re-entry sequence (real-evidence first):** Start with the retained public Python source material from [LifeLog/HTTPX/Digimon connected qualification](../working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification/README.md). Pick a specifically grounded result path: e.g. HTTPX's retained `TestClient(app)` → FastAPI/Starlette → old/proposed HTTPX witness paths (one native root, four witnesses) as recovered exactly through report/store/cold opening; or LifeLog's 28 retained files with 17 unexamined Python units. Point to exact source/result evidence rather than asserting uninspected details. Ask what must remain unchanged when that historical analysis is opened: source identity, selected call/declaration, ordered witness path, premises, outcomes and partiality. **Only after that** explain the result/native decoder and show a small actual source/test excerpt demonstrating one relevant invariant. A locally authored `from pkg import f; f(x=1); f(x=1)` shared-step test is a **synthetic regression fixture**, not a real observed corruption incident; its engineering motivation is recorded in the original native-representation cycle: retained cases contain many repeated binding-trace references (LifeLog: 6,041 references and 3,754 unique steps) requiring lossless space-aware encoding. Two lexical call sites referring to one import step provide a small discriminating test of that requirement, not a claim of two runtime executions or an actual production failure. use it only to isolate deduplicated trace-index mechanics if those details are needed. The swapped comparison `call_id` test is likewise an **injected negative regression**, not evidence of a real-world bug; the code validates that the selected invocation is at the actual unit/span of the retained witness path. Do not claim a particular real retained case exercised shared-step deduplication until its stored content demonstrates it. Explain which integrity obligations are central to later engineering ownership and which codec details are lookup-only. Resume only after user can connect the problem, production/persistence boundary and validation to the real case.

---

# PART D — Native families and Workspace lifecycle

## D1 — Native source evidence (`caller_signature_sources`): retained text, selection and acquisition provenance

**Status:** 🟡  
**Depth:** MUST OWN

Own the separation:

`exact source bytes` versus `premises/observations that justify source selection and association`.

Understand operationally: target receipts, dependency declarations/import candidates, release/source association, publisher observations, tag→commit, module request/receipt states, omissions/gaps, transport/work/limits, retention gaps.

Historical retained receipts may be incomplete and must never be upgraded into fresh provider proof.

Real anchor: glyphsLib remains valid for worker/protocol qualification but is not admitted to the source family because ordinary acquisition premises are missing.

## D2 — Native comparison evidence (`caller_signature_comparison`): exact source basis, run and local findings

**Status:** 🟡  
**Depth:** MUST OWN

- comparison family stores the recorded analysis run against exact source material;
- failed analysis is a recorded operation, not `not_evaluated`;
- completed analysis can remain partial;
- source bytes are not duplicated into a second store.

## D3 — Native format and method contracts: representation codec versus semantic producer version

**Status:** 🟡  
**Depth:** MUST OWN

- codec version = representation contract;
- producer method/version = semantic production contract;
- only admitted exact caller-signature producer pairs are supported;
- do not globally weaken older family version gaps.

## D4 — Workspace persistence and access: capture, evidence revisions, material bases, views and cold recovery

**Status:** 🟡  
**Depth:** MUST OWN

**Real failure → verified engineering repair, for when D4 is taught:** the [retained qualification cycle](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md) first recorded a native-page refusal after six deliveries, even though report/source evidence was available. The [pinned engineering learning note](2026-11-04-bounded-native-navigation-and-view-reuse.md) traces consumer → view/material basis → host → store and the accepted repair: reuse an equal-complete-native-boundary and currently valid view for distinct exact deliveries; reuse decoded immutable basis only per locked publication transaction, never to waive validation or capacity charges. A new retained task then completed 60 pages/all four native witnesses without changing the 64MiB guard. Learn why view versus delivery, cache lifetime, boundary equality, current authorization and source-only baseline 14/20 matter; contrast the rejected cap increase/per-root projection alternatives. The earlier six-page refusal remains historical truth. An analogous real-world problem is bounded paged access to immutable security/audit evidence. Do not pre-study the entire companion now; C2 remains the current lesson.

Own:

- family DAG: `investigation_inputs → caller_signature_sources → caller_signature_comparison`;
- `input_record_ids` are immutable material edges;
- unevaluated placeholders may rebind while pending; evaluated records keep actual captured inputs;
- source-only publication, recorded failed run, completed run are distinct states;
- schema2 host/store publication and fresh-process cold reconstruction;
- cold reconstruction does not reacquire/reanalyze.

---

# PART E — NEWLY IMPLEMENTED: product source acquisition

These modules were future work at the previous roadmap horizon and are now real product code. Learn them **after D**, because they feed the source family and make more sense once its provenance/lifecycle contract is understood.

## E1 — Provider acquisition policy (`acquisition.py`): shared requests, retry/deadline and byte limits

**Status:** ⬜  
**Depth:** MUST OWN

Anchors: `src/upgradepilot/caller_signature/acquisition.py`, `tests/test_caller_signature_acquisition.py`.

Own:

- explicit `AcquisitionPolicy` versus provider/account quota;
- one `AcquisitionSession` shared from the ordinary PR prefix through later source reads;
- every physical attempt is charged, including the narrow PyPI timeout retry;
- stage reservation preserves later GitHub capacity without resetting counters;
- GitHub and all-provider budgets, body limits, aggregate bytes, elapsed policy;
- auth/token changes identity/authentication, not invocation limits;
- allowed provider/host scope and redirect refusal;
- received HTTP body is not automatically admitted provider evidence;
- immutable transport snapshot is checkpoint-ready evidence, not Workspace publication;
- cooperative acquisition deadline differs from analysis worker process deadline.

Real controlled flow: normal prefix + later release recovery/source read share one ledger; the recorded six-attempt example is a controlled proof, not a live constant.

## E2 — Target repository source context: exact PR revision, selected declarations and import candidates

**Status:** ⬜  
**Depth:** MUST OWN

Anchor: `src/upgradepilot/target/source_context.py`.

Own:

- exact observed repository/head revision → commit/tree inventory → admitted complete files;
- declaration-first selection, changed-file priority, explicit excluded/omitted/gap states;
- dependency declarations are preserved without resolving extras/markers/versions;
- static import/reference extraction reuses `bindings.py`;
- declaration + import creates a **candidate**, not installed namespace/runtime dispatch proof;
- local namespace collision and truncated inventory prevent unsafe absence/association claims;
- source/file budgets preserve omissions explicitly.

Rabbit-hole guard: TOML/requirements parser syntax details are OPERATIONAL/LOOKUP unless a real parsing issue matters.

## E3 — Dependency source acquisition: old/proposed release association, modules and partial receipts

**Status:** ⬜  
**Depth:** MUST OWN

Anchor: `src/upgradepilot/caller_signature/source_acquisition.py`.

Own:

- exact release evidence + declared source/repository links + independent publisher provenance;
- declared-source association authorizes source examination only; it is not stronger upstream authority or installed-artifact identity;
- both tag spellings → unique commit → repository inventory → unique admitted module path → exact text;
- exact old/proposed version questions are separate from labelled constraint samples;
- run-local release/module caches prevent implicit retry;
- earlier successful premises remain available when a later read fails;
- failed source reads cannot admit text;
- source work counts admitted source bytes/questions, separate from provider transport accounting;
- native `ModuleSourceReceipt` records module_examined/refused/unavailable honestly.

Important current retention limit:

If association fails, v1 module receipt has no standalone durable release/publisher slot. Those observations can exist run-locally with explicit retention gaps; do not fabricate a complete association or durability claim.

Real controlled flow: target `demo` old/proposed acquisition with one shared session; 21 total / 17 GitHub requests belongs to that controlled test only.

---

# PART F — Connected source publication and ordinary CLI delivery verified; retained qualification active

**Product status and lesson status are separate.** F1 source-progress composition and F2 normal explicit CLI/report/Workspace delivery have verified controlled/installed proof. Neither is covered in this learning track yet. F3's retained-case qualification step is active on main; fresh real-provider, independent maintainer usefulness and adoption remain separately gated.

## F1 — Source-progress integration: receipt/catalog composition, Workspace publication and analysis handoff

**Implementation:** VERIFIED controlled connected stage, main `58bdf1e4`  
**Learning status:** ⬜ Planned  
**Depth:** MUST OWN material/identity/provenance, publication/failure and recovery boundaries; store plumbing OPERATIONAL

Anchors: [`source_progress.py`](../src/upgradepilot/caller_signature/source_progress.py), [`investigation.py`](../src/upgradepilot/investigation.py) `investigate_caller_signature_progress()`, [focused application tests](../tests/test_caller_signature_source_acquisition.py), [cycle record](../working-memory/2026-11-03_caller-signature-source-progress_cycle.md).

```text
one acquire_dependency_inputs() prefix + one AcquisitionSession
 → target and old/proposed source acquisition, partial module receipts
 → collect_source_progress() + CallerSignatureSources
 → NativeInvestigationCapture + publish_native_progress() checkpoints
 → admitted exact sources.analysis_input() for bounded run_source_analysis()
 → capture/publish source-based comparison or preserve earlier partial state
 → fresh-process cold revision recovery, no repeat producer work
```

Own: physical provider response versus admitted text; receipt versus **confirmed Workspace revision**; earlier successful premises surviving a failed later read; failed association's run-local-only publisher/release observations; an unavailable proposed source disallowing a paired result; last confirmed publication if later worker/store activity fails; precise material-version/method/record edges.

**Controlled proof anchors:**
- `test_application_publishes_partial_source_progress_before_analysis`: authored 21 physical / 17 GitHub requests with one prefix, three retained files and unavailable proposed receipt recover after interrupted analysis, no fabricated comparison.
- `test_application_analyzes_the_published_exact_version_pair`: authored 23-request forwarding case yields old `bound` and proposed `rejected` against captured exact source.
- `test_failed_source_publication_preserves_earlier_progress_and_stops_work`: repaired second publication masking the original `OSError`; earlier confirmed state survives, later work stops.
- [`test_published_source_and_failed_run_survive_fresh_process_without_producers`](../tests/test_caller_signature_workspace.py): cold opening cannot reacquire or rerun analysis.

**Retained verification:** 1,041 product, 194 API, 7 architecture and four installed composition controls passed at the dated milestone. Not newly rerun here. This is controlled composition/installed proof, **not a live-provider run, ordinary CLI report, runtime compatibility, or maintainer usefulness**.

Practice at F1: predict the surviving exact material and prohibited paired inference after failed proposed download, then identify the latest confirmed revision after a later worker/write failure. Read assertion/setup/results and name which trust boundary each test protects.

## F2 — User-facing evidence delivery: CLI profile, report/source save/open and exact revision recovery

**Implementation:** VERIFIED controlled/installed normal-path delivery, November 4 milestone  
**Learning status:** ⬜ Planned, now ready for study after F1  
**Depth:** MUST OWN confirmed/unknown revision, report/action and user-facing evidence claims

Owners: [user-delivery cycle](../working-memory/2026-11-03_caller-signature-user-delivery_cycle.md), [implementation plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md), [delivery source](../src/upgradepilot/caller_signature_delivery.py), [controlled tests](../tests/test_caller_signature_delivery.py).

**Implemented:** explicit `--evidence-profile caller-signature`; optional durable `--workspace-store`; report/source projection and `--save-report` with independent file-delivery acknowledgement; `--open-workspace PATH --revision ID` exact offline recovery and schema1 saved-report opening. `unacknowledged_revision` and `read_selected_revision` distinguish confirmed/unknown/missing/ambiguous/corrupt historical revisions. Controlled native root yields two conditional old/proposed witness outcomes and navigable original text. Full product 1,063, experiment API 194, architecture 7 and 20 installed controls passed at the delivery milestone. No new real-provider or human task claim.

**Critical ownership question:** Confirmed source revision A survives later report attempt B with lost acknowledgement. B may have been published; exact store inspection resolves that uncertainty, not a retry. A separate `--save-report` failure cannot erase an earlier confirmed Workspace report revision. Cold opening reads retained evidence without new network/AST/analysis/synthesis. Correct failure and unsupported-representation cases must refuse rather than silently fall back.

**Milestone boundary at the original small controlled F2 proof:** retained full-size navigation was not yet qualified then. Later F3 retained HTTPX evidence now qualifies its specific 60-page bounded native access and cold recovery (see D4 and F3), **not** unlimited paging, a fully successful source-only navigation baseline, live-provider behavior, independent usefulness or adoption.

## F3 — Product qualification: retained/live evidence, maintainer tasks, usability and adoption limits

**Product:** ✅ Connected retained-case qualification closed with bounded native paging repair at `38741c3c`; **live provider / independent task usefulness / broad adoption still pending**  
**Learning:** ⬜ Not yet taught  
**Depth:** MUST OWN qualification, proof/non-proof and eventual task/adoption disposition

Owners: [active qualification cycle](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md), [qualified implementation plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md).

Exact retained LifeLog/HTTPX/Digimon evidence and separately labelled authored-HTTP normal composition were qualified through ordinary application/report/store/cold opening; glyphsLib's missing historical receipts remain explicit. The accepted native acquisition default-four allocation was restored without changing global budgets. The **original** fixed navigation exposed two separate limits: source-only text retrieval found 14/20 ranges and native paging stopped after six deliveries at the 64MiB closure guard. The **new** exposed retained HTTPX native task, with the implemented valid-view/basis reuse, passes 60 exact pages and all four witnesses at the original limits, with guarded installed cold opening. The original failed attempt and incomplete source-only baseline remain recorded. The closed retained gate proves this case's bounded access, not general unlimited navigation, actual live provider, runtime dispatch or human usefulness. A later prospective matched first-page timing study showed lower CPU counters but failed elapsed-clock acceptance. **Next main responsibility:** freeze and review a normal-product attempt contract before any actual provider invocation; after that, separate live/task/adoption decisions retain their own evidence and authorization gates.

Must distinguish historic retained exact inputs, controlled provider responses, outside-checkout installed proof, newly acquired real-provider observations, runtime applicability, maintainer usefulness and adoption. Successful controlled report delivery cannot prove all of them. No broad campaign or model/runtime experiment is activated by this module.

---

# PART G — Scheduled later checkpoint, deliberately deferred now

## G1 — Combined evidence and runtime applicability: deferred design checkpoint

**Status:** ⬜ DEFERRED  
**Depth:** MUST OWN only when its plan gate is reached

Current main schedules this checkpoint **after connected product qualification/task disposition**, before optional source expansion/non-required case campaigns.

When reached, learn/design how existing static caller-signature evidence, CI/runtime command-completion state, installed package state, import/dispatch, affected-path exercise and behavior evidence can be combined without strengthening claims beyond exact identity/environment/time/material joins.

Do not pre-study speculative runtime observer design now. Reuse existing CI/static/target-owned evidence first; new runtime observation must be justified by a concrete unresolved proposition.

## G2 — Evidence-grounded AI/retrieval interpretation: deferred design checkpoint

**Implementation:** planning only, no new model/RAG/agent execution. **Learning:** ⬜ DEFERRED.

Owners: [project route](../plans/UPGRADEPILOT_90_DAY_PLAN.md#evidence-grounded-ai-design-checkpoint) and [planning record](../working-memory/2026-11-03_evidence-grounded-ai-direction_planning-cycle.md). Linked to the G1 disposition, **not another immediate Build prerequisite**. Earlier Investigator trials were inconclusive/negative. When selected, compare one exact maintainer evidence-interpretation task with a transparent same-material baseline and bounded model; test retrieval only if selection is the observed gap. Track unsupported claims, citations, missing facts, costs/failures/rollback and explicit disposition. Broad RAG infrastructure/tool-use agents/MLOps stay conditional.

---

## 3. Cross-cutting principles to keep throughout every module

1. **No invented evidence.** Missing/unsupported/unexamined/failed/not_evaluated are different states.
2. **Provenance before conclusion.** Exact bytes alone do not prove why they are the right source.
3. **Source evidence is not runtime evidence.**
4. **Local argument binding is not semantic compatibility.**
5. **Completion is not coverage.**
6. **Retained-but-unexamined is not absence.**
7. **Valid records need valid relationships.** Check graph edges, not only nodes.
8. **Resource bounds are part of semantics.** Refusal/partiality must remain explicit.
9. **Representation support is not producer authority.** Codec and semantic producer versions are separate.
10. **Historical evidence stays historical.** Do not backfill/regrade frozen captures merely to make newer product paths pass.
11. **One product owner per evolving responsibility.** Experiment compatibility must not become a second analyzer/acquirer.
12. **Installed proof has a precise boundary.** Outside-checkout execution is valuable but does not automatically prove dependency isolation, normal application integration, live-provider correctness, runtime compatibility, or usefulness.

---

## 4. Current learning order

**Learning-coverage snapshot (November 6, after teaching-method review):** 19 named modules = **6 covered interactively** (A1–A4, B1, C1), **5 introduced/in progress** (C2, D1–D4), **8 not yet studied** (E1–E3, F1–F3, G1–G2). **13 not yet covered**; among them G1/G2 are intentionally deferred design checkpoints, not immediate prerequisites. Implementation milestones do not automatically upgrade learning marks.

```text
COVERED INTERACTIVELY:  A1 A2 A3 A4 B1 C1  (6 of 19)
NOW:                    C2 historical result reconstruction and evidence-integrity validation (real-case re-teaching needed)

NEXT:                   D1 D2 D3 D4 (previously introduced; continue)
                        E1 E2 E3 acquisition and exact provenance
                        F1 verified source-progress application
                        F2 verified user-facing CLI/report/Workspace delivery
                        F3 verified retained-case qualification; live/task/usefulness gates later

LATER AT PLAN HANDOFF:  G1 combined evidence/runtime applicability
                        G2 evidence-grounded AI/LLM/retrieval checkpoint
```

### Flow understanding and ownership evidence

Flow understanding is established at the demonstrated scope when Ali can trace a real case across:

`PR/input → bounded source acquisition/provenance → source-family publication → bounded analysis → comparison evidence → Workspace recovery → normal user-facing result`

and can explain, for each boundary:

- who owns it;
- what exact evidence enters/leaves;
- what failure/unknown states mean;
- the main engineering mechanism and code/data flow, why its placement/rationale is justified (or uncertain), and a credible trade-off when material;
- what the evidence proves;
- what it does **not** prove;
- where to inspect or test it when behavior changes.

For ownership-bearing completion at a selected scope, also preserve an actual meaningful practical attempt with its result, assistance and limitations. Lessons and questions should use full descriptive responsibility/layer names rather than expecting roadmap-code memorization; prefer real retained/source/incident evidence over synthetic test fixtures. Relevant evidence can include selecting and interpreting a discriminating test, causal diagnosis, or a justified modification with appropriate verification. Stronger implementation/transfer claims require corresponding action and changed-context or reduced-assistance evidence; explaining where a test lives or proposing a change alone does not establish implementation ownership.

If this evidence remains unavailable, record the ownership gap explicitly while retaining truthful lesson coverage and any justified continuation. No historical checkmark is automatically promoted or erased. Memorizing every helper/API, owning every advanced internal before product work continues, and a new cross-project capability score are not required. Use an illuminating real-world transfer and one or two concrete professional capabilities when they improve this selected lesson; neither is a mastery claim or an extra curriculum gate.
