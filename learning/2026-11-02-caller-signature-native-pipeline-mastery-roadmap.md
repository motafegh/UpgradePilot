# Caller-Signature Native Pipeline — Living Learning and Mastery Roadmap

**Created:** 2026-11-02  
**Initial evidence horizon:** `7a9bef12fb65ee075dab645a638adf5a3955dc48`  
**Last synchronized main:** `b56ad634e421fb3d639141054da52260e83c7410` — November 8, 2026. Main implemented a deterministic maintainer report first view (`report.py`), passed 61 focused and 1,078 product tests, and reviewed exact HTTPX/OpenCV/Soup Sieve saved reports. Independent usefulness remains unmeasured. Reviewer packet revision 3 passed focused technical recheck; the new GitHub rehearsal is derived summary content, not authorized access to all owner-local original HTTPX files. Future F2/F3 lessons must read the new renderer, tests, Build cycle and reviewer protocol; C2 analyzer/decoder owners and present 10/14 guided coverage remain unchanged. [Separate learning-product audit register](2026-11-08-learning-to-product-engineering-audit-register.md) holds potential improvement questions, not approved defects.
**Working branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`  
**Purpose:** living study/relearning roadmap for Ali's interactive learning track while UpgradePilot continues to evolve on `main`.  
**Authority boundary:** this file is a learning artifact, not the live project-position owner. `MEMORY.md`, current source/tests, accepted plans/specifications/ADRs, and dated evidence remain authoritative.
**Audit observations:** [Learning-to-product engineering audit register](2026-11-08-learning-to-product-engineering-audit-register.md). Add evidence-backed candidates as lessons reveal them; review/merge selectively with separate approval, never automatically.

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

**Avoid repeating settled general safety questions.** After the learner has demonstrated the static-versus-runtime distinction, focus subsequent checks on the concrete source, identity, implementation mechanism, failure mode or alternative design. A sampled Starlette 1.10.0 declaration is not an exact installed-version witness, and a qualified new version must not silently erase the historical sample; track this question in [LPA-001](2026-11-08-learning-to-product-engineering-audit-register.md), not as an automatic product fix.

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

### Working Memory as engineering-decision evidence (use at each relevant module)

**The final implementation is the starting point for correctness; the dated Working Memory is the source of how we got there.** Before teaching the chosen real case or code path, open the smallest relevant `working-memory/` cycle and its specific evidence packet **when it materially explains the feature**. Extract: (1) original product need/observed pressure, (2) initial design and numeric/resource assumptions, (3) trial and actual measurements, (4) surprising failures, invalid hypotheses and rejected alternatives, (5) repair and engineering rationale, (6) final verification, non-proof and remaining design debt. Then reconnect each material turn to current source, accepted plan/ADR, focused tests and a real retained case. A failed probe and a corrected attempt are **separate historical facts**; do not retroactively overwrite either.

This is **targeted historical reconstruction, not automatic chronological reading**: select one or two especially instructive decisions per chunk; open additional cycles only to resolve a causal question. Label past snapshots, synthetic tests, controlled replays, private unobservable outputs, implementation assertions and independently verified results distinctly. The old Working Memory cannot override current code, accepted contracts or `MEMORY.md`'s live product position. Historical design intent can be taught when documented; otherwise distinguish plausible engineering rationale from the author's established reason. Do not force an error story where the original path was straightforward, or quiz before the real problem is understood.

**Explicit read-before-teaching reference map for every module:** [19-module Working Memory / design / source / proof map](2026-11-06-caller-signature-module-reference-map.md). At each chunk, **fetch and read** the relevant engineering history, governing plan/design, actual source and one discriminating proof before teaching. Linking is not the same as reading. This roadmap continues to own the lesson sequence/status/depth; the map owns precise file navigation. The brief entry table below is only a quick overview.

| Lesson responsibility | Working-memory entry point(s) | What to recover before source/test teaching |
|---|---|---|
| **A1 — Evidence meaning; A3 — imported-origin binding** | [Oct 4 ordered/scoped bindings](../working-memory/2026-10-04_2102_ordered-and-scoped-bindings_lbd-cycle.md); [Oct 28 checker Build](../working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md) | Real names/scope and conditional-import pressure, known failures/corrections, why traces preserve uncertainty rather than claim executed imports |
| **A2 — One product kernel** | [Nov 1 product-record/producer transfer](../working-memory/2026-11-01_caller-signature-native-representation-proof_cycle.md); [Nov 2 worker promotion](../working-memory/2026-11-02_native-caller-signature-analysis-worker_cycle.md) | Why one evolving owner replaced experimental duplication; ordering/proof corrections and what installed proof did not establish |
| **A4 — Source facts and local argument reception** | [Oct 28 design](../working-memory/2026-10-28_reusable-caller-signature-evidence_design-cycle.md); [Oct 28 Build](../working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md) | Real comparison need, the observed `inspect.Signature.bind` discrepancy, selected local checker rules, source/report evidence and early failure fixes |
| **B1 — Source correspondence** | [Oct 29 correspondence/ordinary retention](../working-memory/2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md); [Oct 30 protocol/factory paths](../working-memory/2026-10-30_protocol-factory-source-correspondence_build-cycle.md) | Why target call→dependency declaration paths and premises were required; supported and unresolved source patterns |
| **B1 — Bounded work and atomic source admission** | [Nov 1 LifeLog capacity/admission cycle](../working-memory/2026-11-01_analysis-capacity-and-work-admission_cycle.md); [admission design](../plans/CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md) | Initial 4,321-fact refusal; 5,443 measured facts; isolated 8,192-fact trial hitting the unchanged JSON structural guard; rejected naive cap increase; whole-file/paired admission and unexamined evidence |
| **C1 — Bounded analysis worker and execution truth** | [Nov 2 worker cycle](../working-memory/2026-11-02_native-caller-signature-analysis-worker_cycle.md) | Initial producer/worker wiring faults, timeout and foreign-exchange controls, installed-origin proof and the completed-but-partial LifeLog result |
| **C2 — Fixed result/native reconstruction** | [Nov 1 native representation cycle](../working-memory/2026-11-01_caller-signature-native-representation-proof_cycle.md); [Nov 2 result/worker cycle](../working-memory/2026-11-02_native-caller-signature-analysis-worker_cycle.md) | Why actual retained trace repetition motivated reference tables, how exact round-trip and corruption refusal were proved, and why opening cannot reanalyze |
| **D1–D3 — Native source/comparison families and codec-method contracts** | [Nov 2 native family/checkpoint cycle](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md) | Source receipt vs analyzed facts, family membership, producer/codec versions and negative reconstruction controls |
| **D4 — Workspace persistence, navigation and recovery** | [Nov 2 family/checkpoint cycle](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md); [Nov 4 retained navigation failure/repair](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md) | Exact revision/recovery semantics; six-page 64MiB refusal; view/basis reuse and preserved earlier acknowledged data; historical negative evidence versus successful successor |
| **E1 — Provider request budgets and ledger** | [Nov 2 acquisition-ledger cycle](../working-memory/2026-11-02_native-acquisition-ledger_cycle.md); [Oct 30 staged policy](../working-memory/2026-10-30_staged-source-acquisition-policy_build-cycle.md) | Why every physical request is charged, timeout/retry ownership, shared prefix and error paths without invented provider observations |
| **E2–E3 — Target/dependency source acquisition and partial receipts** | [Nov 2 source acquisition owner cycle](../working-memory/2026-11-02_native-source-acquisition-owners_cycle.md); [Oct 31 ordinary-source blocker](../working-memory/2026-10-31_ordinary-source-acquisition-blocker-resolution_cycle.md) | Exact source-version association, absent and partial module receipts, failure/recovery decisions and selected source-adapter budgets |
| **F1 — Source-progress application/publication** | [Nov 3 source-progress cycle](../working-memory/2026-11-03_caller-signature-source-progress_cycle.md) | Why source checkpoints precede analysis; publication failure correction and which data survives |
| **F2 — CLI/report/Workspace user delivery** | [Nov 3 delivery cycle](../working-memory/2026-11-03_caller-signature-user-delivery_cycle.md); [Nov 6 revision-guard correction](../working-memory/2026-11-06_caller-signature-cli-revision-guards_cycle.md) | Confirmed versus uncertain acknowledgements, exact offline opens, lost-report scenarios and guard grammar/proof (40- or 64-hex IDs) |
| **F3 — Product qualification, usefulness and adoption** | [Nov 4 connected retained qualification](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md); [Nov 6 host timing/traversal cycle](../working-memory/2026-11-06_independent-host-timing-and-retained-traversal_cycle.md) | Qualified case versus untouched transfer/human usefulness; original refusal/repair; count/CPU/elapsed-clock discrepancies and presently bounded timing/traversal evidence |
| **G1–G2 — Deferred combined/runtime and evidence-grounded AI decisions** | [Nov 3 AI direction planning](../working-memory/2026-11-03_evidence-grounded-ai-direction_planning-cycle.md); [implementation checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) | Read only at the accepted handoff: relevant real gap, prior negative model trials, combined evidence authority and proof/cost alternatives |

**Current re-entry:** C2 starts with actual retained LifeLog/HTTPX source and the Nov 1 native representation cycle. Trace the real repeat-reference pressure and exactly what was preserved; then inspect source codec and tests. Earlier LifeLog limit/admission experiments belong to B1/C1 prerequisite review, not a requirement to study all historical cycles before C2.

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

- `b56ad634` — November 8: eight main commits beyond the previous learning horizon, including the [first-view product Build](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) (new `Review at a glance` rendering, verified 61 focused/1,078 product tests) and [reviewer packet technical readiness](../working-memory/2026-11-08_maintainer-first-view-review-readiness_planning-cycle.md) (revision-3 rubric recheck, [GitHub remote rehearsal](../working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/README.md)). Independent human usefulness not measured; exact OpenCV tag inspection remains a scoped original-text CLI limitation. Product code changes touch report presentation and its tests, **not** C2 codec. F2/F3 references updated.

- `7a9bef12...` — native source/comparison families + checkpoint recovery qualified.
- `9c903926...` — **9 commits later**: product-owned acquisition policy/shared physical-request ledger, target source-context acquisition, exact dependency source acquisition/association/module receipts qualified. Source-family composition/Workspace source-progress publication and ordinary app/profile/CLI/report delivery remain next. A later combined-evidence/runtime-applicability design checkpoint is scheduled, not implemented.
- `834aeaa4` — November 3: scoped depth and practical-attempt method; documentation validation, not product qualification or independent learner reassessment.
- `58bdf1e4` — November 3: source-progress composer and connected application stage qualified. One shared PR prefix/transport ledger; target + old/proposed source receipts and repeated partial Workspace publication **before** analysis; exact published source basis to bounded worker; fresh-process partial recovery. Corrected write-failure handling preserves the original `OSError` and earlier committed progress. Retained verification: 1,041 product / 194 experiment API / 7 architecture and four installed composition controls; not rerun here.
- `c136d2a0` — November 3: explicit caller-signature CLI/report/source/save/offline-opening delivery cycle opened (not yet implemented).
- `e109875f` — November 4: storage/acknowledgement foundation, 63 host/store focused checks; CLI integration pending *at that historical horizon*.
- `8d6f3d09` — November 4: user delivery subsequently verified (explicit profile, CLI/report/source/save/exact offline opening), with 1,063 product, 194 experiment API, 7 architecture and 20 installed controls recorded at its milestone. Connected retained-case qualification is active in B: LifeLog/HTTPX/Digimon retained equivalence and ordinary controlled acquisition examined; HTTPX default adapter allocation 2 vs 4 corrected under unchanged global budgets (latest reported 1,064 product/194 API/7 architecture). Fixed source navigation and final qualification remain pending. No fresh live provider/usefulness claims. These are referenced dated proofs, not rerun by this learning update.
- `068ba7b4` — November 4: original retained qualification showed **six-page native refusal** at the 64MiB original-material closure guard, and fixed source-only navigation retrieved 14/20 required locations. Earlier acknowledged results remained readable. This **historical failed attempt is preserved**, not retrospectively passed.
- `38741c3c` — November 4: bounded repair accepted at the original policy, consumer caches a still-valid equal-native-boundary `ConsumerView` for repeated deliveries; `CheckpointStore.publish` reuses decoded immutable original bases only inside one locked transaction while retaining all historic validation and capacity accounting. The separately frozen retained HTTPX successor completes **60 unique pages**, all **four native witnesses**, with one view/basis and guarded cold recovery; `1,073` product, `194` API, `7` architecture and `57` installed controls at the cited proof horizon. Original six-page refusal remains a negative control; source-only baseline stays 14/20. Connected retained qualification closed; live-provider, human usefulness and broad adoption unproved. A [source-pinned learning companion](2026-11-04-bounded-native-navigation-and-view-reuse.md) now exists on main; use later in D4 rather than duplicate its full narrative here.
- `bb3b2b10` — November 6: frozen matched first-page comparison between consumer-only `6e98d0a0` and publication-reuse `38741c3c`, with six correctly delivered identical 4,873-byte first pages and preserved acknowledgements. Recorded paired **CPU median ratio 0.81265** (~18.7% less CPU in this limited scenario); *elapsed* timing remains **inconclusive** because all trials failed the frozen clock-consistency screens. This was measurement, not a new product optimization or proof of whole-workflow speed.
- `3569e8b3` — November 6: nine newer main commits prepare a frozen normal-product HTTPX attempt contract and verify optional CLI expected-base/head revision guards through retained ordinary composition; an independent host clock preflight qualified a separate method while one 60-page retained traversal is still in progress at this snapshot. New work changes CLI/report delivery and later qualification owners, **not** already-learned binding/comparison/worker semantics or C2 decoder behavior. No fresh provider calls, target runtime execution, positive whole-run elapsed claim or independent usefulness credit.
- `6a19fc69` — November 7: **live qualified paired HTTPX source task** after an original, separately preserved PyPI-transport partial attempt. [Original live partial](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) → [observed TLS timeout diagnosis](../working-memory/evidence/2026-11-06-pypi-transport-diagnosis/RESULTS.md) → [split-route proxy proof](../working-memory/evidence/2026-11-07-pypi-route-repair/RESULTS.md) → [live successor](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md). The successor acquired 24 retained files, 12 static witnesses (four exact-version HTTPX), three unexamined units and 147 gaps; local five-keyword fit depends on sampled Starlette `httpx2`-first/HTTPX-fallback and other source/runtime premises. Exact stored result/report/source cold-reopened; CI/runtime not evaluated. Limited explicit-profile pilot eligible; no independent user benefit or runtime guarantee.
- `a0204b3a` — November 7: **post-qualification CI/runtime applicability checkpoint completed**. [Cycle](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) compared July's bounded green Docker run (expired logs/no selected test-process proof), October's independently hash-verified exact-head empty CI-run response, and November's source-only result. One-response offline replay through current CI owners returned `no_successful_ci` / `no_exact_head_workflows` and runtime `no_admitted_candidate`; 41 focused tests pass. Historical applicability remains **unresolved**, no CI defect identified, no new runner/combined profile justified. A future decision-relevant target-owned test invocation with exact process/callable/loaded-file identity is the re-entry condition. Product next: existing evidence-grounded AI **design checkpoint**, not model execution.
- `852dd20b` — November 7: the current [maintainer-explanation planning cycle](../working-memory/2026-11-07_evidence-grounded-maintainer-explanation_planning-cycle.md) reviewed HTTPX's concise deterministic report/source explanation, then screened an OpenCV retained contrast. Both exposed tasks already supported concise defensible answers; no observed residual reason to execute a model comparison on these tasks. The product decision remains to select a genuinely unmet explanation task or defer, not to infer a new LLM benefit. Product code/tests unchanged. Current C2 learning receives a real-data guided walkthrough and progress checklist, independent from product evaluation.
- `772b67cb` — November 7: five newer main commits add a [read-only offline SQLite FTS5 retrieval exercise](../working-memory/2026-11-07_offline-evidence-retrieval_learning-cycle.md) on nine exposed HTTPX/OpenCV passages; seven frozen queries yield five hits and two lexical misses, later labelled source-aware rewrites recover the missed passages without upgrading the frozen score. A separately selected [CPU local semantic retrieval comparison](../working-memory/2026-11-07_offline-semantic-retrieval_learning-cycle.md) froze the cases/model/caps; its first launch failed on a 128-token SentenceTransformers wrapper guard **before embedding**, and a corrected successor is prepared separately. No product source/test or AI-generated explanation implementation changed. In this independent learning branch, C2 covers real 63-request transport receipts and source-acquisition limits; D4's production SQLite persistence is distinct from G2's in-memory FTS5 retrieval experiment.
- Current C2 continuation: one actual `proposed_dependency` witness (`0.28.1`) is traced across 12 ordered source steps from target `TestClient(app)` to HTTPX `Client.__init__`; all five forwarded keywords are recorded as `named_parameter`, while `one_receiver_assumed` and unresolved import/MRO/installed-runtime premises remain explicit. The selected target root has 2 proposed + 2 old + 4 constraint-sample witnesses; the two HTTPX paths per version are alternate re-export paths, not separate target calls. The curated JSON's `source-N` labels are opaque report source IDs; full per-ID filename mapping still requires the original retained source catalog, so it is separately open rather than inferred.
- `7058e065` — November 7: main added a proposed same-evidence deterministic-versus-LLM maintainer explanation comparison and a separately gated multi-agent investigation learning exercise. `MEMORY.md` selects review of the maintainer task and deterministic baseline next; no inference or model/agent execution, dependency change or product code/test change is authorized. The plan lists lexical search and optional SQLite FTS5/BM25 only if retrieval is shown to be the bottleneck. This learning sync adds the actual post-run HTTPX review-summary provenance to C2/F3 and explicit project-bound SQL/SQLite teaching under D4; it does not add a generic database course.

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

**Status:** 🟡 In progress. Real LifeLog/HTTPX data flow, identity/coverage, transport receipts and selected-witness semantics have been taught from retained evidence. November 8 guided clarifications also cover Python MRO/super() and the current static boundary, why constraint_sample is an adapter source sample rather than target resolution, how witness premises constrain claims and how existing CI/command/package-state runtime differs from missing caller-call-level runtime evidence. These are explained slices, not independent mastery. Exact opaque source-ID reconstruction, full report/cold-read limits and decoder refusal contract remain open.
**Depth:** MUST OWN

Own:

- decode/reconstruction is not producer execution;
- exact input digest and source/fact/candidate references;
- shared trace referential integrity;
- malformed/foreign reference refusal;
- structural/byte guard meaning;
- node validity does not imply edge validity.

**Next chunk, building on real source data:** Use the [LifeLog PR1 frozen Letterboxd file](https://github.com/VaHerinckx/LifeLog_Project/blob/2a0f4e2b6f8eae3a813edacc6095d78aa34c3197/pipeline/src/sources_processing/letterboxd/letterboxd_processing.py): the movie search at L187 and movie detail fetch at L212 are distinct genuine `requests.get` call sites. Shared import-table illustration was **not** the private actual call-trace JSON; [retained LifeLog trace totals](../working-memory/evidence/2026-11-01-native-caller-signature-record-proof/retained-results.json) independently substantiate the representation pressure. For the full result decoder, now also use [real live HTTPX PR20 saved source/report/cold recovery](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md): exact TestClient source root, re-export/forwarder, two versions' constructor witnesses, conditional fallback and premises. Show each field's true producer, saved form, source identity and decoded validation; inspect `result_codec.py`, `native_codec.py` and focused tests. Swapped call-ID or broken index tests are **injected negatives**, not observed real corruption. Keep all uncertainty and stop after a comprehensible slice; no stage-code memorization or synthetic-first teaching.


**Teaching-progress checklist (checked means source-backed material was presented and reviewed, NOT independent mastery):**

- [x] **LifeLog source → call facts → shared binding-trace table → historical decode.** Genuine Letterboxd movie-search/details operations; deliberately simplified saved table distinguished from unpublished actual call rows. The developer's duplication/capacity pressure and tests were explained.
- [x] **HTTPX real selected root → compared call → old/proposed signatures.** Target `TestClient(app)`, Starlette's forwarding `super().__init__`, saved path, receiver/premises and local `bound` outcomes shown; wrong-call-ID path check explained and learner gave the correct core refusal reasoning.
- [x] **Post-run JSON provenance versus original saved result.** `review_saved_task.py` opens an acknowledged Workspace revision and checks native/report/source consistency before writing a task-review summary; no rerun/network is implied by this reviewer.
- [x] **Exact identity and analysis coverage (this session's guided explanation).** `identity.base_sha`/`head_sha` name PR commits, `revision` selects a distinct Workspace capture; `acquisition_state=partial` versus `analysis_state=completed`; 24 retained files, 12 witnesses, 1,107 facts, three unexamined units and 147 discovery gaps were traced to saved source/worker objects and the real reviewer.
- [x] **Transport-ledger and partial acquisition — full recorded totals plus representative real receipts (guided).** HTTPX successor's 63 entries: 3 native-input, 14 target-context, 40 dependency-exploration and six source-closure requests; 45 GitHub/18 PyPI, 53 HTTP 200 and ten HTTP 404. Code in `AcquisitionSession._request_once` increments physical counters before dispatch, records `started` → `received` or `failed`, and charges both received 200 and received 404; HTTP received never automatically means admitted package/source provenance. Shared defaults were GitHub 50, total providers 100, 180-second cooperative deadline and 32 MiB aggregate bytes; actual 2,359,252 decoded bytes, no transport stop and `retry_policy=none`. The `acquisition_coverage` still names eight omitted candidates (including pytest/httpx2), deferred candidates and unresolved association premises. **Method's complete counts were inspected, not all 63 responses taught line by line.** This teaches C2's serialized receipt meaning; E1/E3 resource policy and source admission are still separate future lessons.
- [x] **Selected witness record semantics and target-root composition (guided).** Traced one actual 12-step proposed HTTPX 0.28.1 witness from target `TestClient(app)` through import/re-export, Starlette forwarding/base and HTTPX `Client.__init__`; interpreted `role`, exact source `version`, `one_receiver_assumed`, five `named_parameter` receptions, local `bound` outcome and unresolved dispatch/MRO/installed-version premises. Explained the eight selected target-root witnesses (four constraint samples, two old, two proposed), the twelve all-root total, and why two HTTPX witnesses per version are alternative re-export paths rather than separate target calls. The curated JSON carries opaque `source-N` identities, not every original filename.
- [x] **Python MRO and super() dispatch boundary (guided).** Explained MRO/C3 lookup with a real Starlette TestClient(httpx.Client) path; super() continues after the current class in the effective MRO. analysis.py records declared class bases, and correspondence retains declared-base/super() paths plus class_allocation_metaclass_and_mro_not_established / builtin_super_and_effective_mro_assumed; it does not calculate or prove the effective runtime MRO.
- [x] **constraint_sample source role and selection (guided).** select_exploration_version deterministically chooses the newest stable, non-prerelease/non-dev registry release satisfying the visible declared dependency specifier. The HTTPX record's sampled Starlette 1.10.0 source supplies intermediary adapter declarations/helpers for the call path. It is not proof that Starlette 1.10.0 was installed or activated in the target; constraints/markers, namespace mapping and full version ranges remain unproved.
- [x] **Witness premises: meaning and responsible improvement (guided).** Current candidate and comparison records preserve premise/limitation reason strings such as unresolved export, namespace, branch, MRO, receiver and runtime conditions. Explained why these must not be erased or converted to success. Future improvement should make material premises traceable to proposition, owner, status, exact scope, evidence reference and observation horizon, then resolve only with admitted evidence; no premise-resolution engine or product change was selected.
- [x] **Runtime capability layers and caller-signature gap (guided).** workflow_runtime_correlation.py matches bounded static workflow jobs/steps to runtime jobs/steps; runtime_execution.py assesses unmasked step and eligible exact-command execution; dependency_state.py composes a bounded RequirementSatisfiedAtCommandCompletion witness for a supported direct-requirements/pip family. None establishes that the HTTPX target test reached this Python call, which callable/MRO was used or which file was loaded. The November 7 HTTPX applicability checkpoint keeps that historical question unresolved and defers a new runtime producer until a decision-relevant target-owned observation exists.
- [ ] **Resolve opaque witness source IDs and reconstruct exact alternative edges.** Reopen the exact retained native report/source catalog, map each `source-N` to its source identity/path and revision, validate every path step against the correct source, then compare both old and both proposed paths to distinguish actual alternate re-export edges from shared steps. Do not infer a filename from `source-31` or any other ID in the curated summary.
- [ ] **Product task-review and proof limits.** Understand `baseline`, `report_route`, `report_native_fidelity`, `cold_verified`, `branch_states`, `action`, pilot disposition and unproved independent usefulness.
- [ ] **Decoder support and refusal contract.** Exact source/input digest, method/codec version, candidate/source reference consistency, corruption/foreign references, structural/byte bounds and no analyzer/network execution, with actual implementation plus narrowly constructed refusal tests.
- [ ] **Independent practical understanding check.** Given one exact saved finding and source, identify its owner, relationships, retained uncertainty and what corruption must be refused; only then reassess C2 mastery.

**November 8 discussion handoff:** the user's proposed installed-version detector and better premise resolution are logged as scoped hypotheses in [LPA-001/002](2026-11-08-learning-to-product-engineering-audit-register.md). An exact HTTPX dependency version is not an exact target-installed Starlette version. Do not overwrite the recorded `constraint_sample`, assert a detector is selected, or add mastery checkmarks from this discussion.

**Progress rule:** A teaching checkbox records an evidence-backed explained slice; it does not certify independent competence or raise the **6/19 covered interactively** module count. Mark later boxes only after their own small actual-evidence lesson, and preserve the source/test/historical gap references in the map. C2 now has **10/14 guided teaching slices explained**; the four new clarifications do not raise the 6/19 independent module-coverage count.

**Actual live structured artifact to learn:** [HTTPX successor `results.json`](../working-memory/evidence/2026-11-07-native-proxy-successor/results.json) (~55 KB) plus its [offline generator/reviewer](../working-memory/evidence/2026-11-07-native-proxy-successor/review_saved_task.py) and [narrative](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md). It is a curated post-run task-review summary generated after opening the real saved Workspace checkpoint/report and checking source/report/native fidelity; it is **not** the raw product event log, not the `caller-signature-analysis-result/1` worker exchange emitted by `result_codec.py`, and not the SQLite database. It reports 12 total witnesses while listing eight selected witnesses for the chosen target root. Trace identity/acquisition/work/path/premise/report/cold-recovery/disposition fields to their actual owners in C2, D1–D4, E1–E3 and F2–F3. Learn it in bounded groups, not as a 1,500-line memorization task.
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


**SQL/SQLite is an explicit MUST-OWN part of D4, not a separate general database course.** The production [`CheckpointStore`](../src/upgradepilot/workspace/checkpoint_store.py) uses Python's standard-library `sqlite3` module and a host-owned local `workspace.sqlite3` file. SQL is private to this persistence owner; callers exchange typed `CheckpointRevision` values. A durable local store is explicitly supplied; default Workspace publication can be volatile, so do not assume every invocation writes a database. This is SQLite (an embedded file database), not a remote database server or an ORM/SQLAlchemy layer.

**D4 SQL learning sequence (short, tied to the actual implementation):**
1. **Why SQLite rather than a pile of JSON/files?** Read the [October 8 file/SQLite experiment](../working-memory/evidence/2026-10-08-workspace-checkpoint-stores/README.md) and its [measured results](../working-memory/evidence/2026-10-08-workspace-checkpoint-stores/results.json): immutable shared records, coherent revision publication, held readers, backup and interruption trade-offs. Do not turn its workload-specific timings into a universal speed claim.
2. **Relational model and schema:** understand `payloads`, `records`, `record_inputs`, `revisions`, `revision_members`, `heads`, plus schema-2 lifecycle tables; primary/foreign keys, uniqueness, ordered membership and joins.
3. **Actual SQL and transaction:** read the parameterized `SELECT`/`INSERT` operations, `BEGIN IMMEDIATE`, conditional `heads` update and `COMMIT`; understand why a successor is published atomically and a competing/stale predecessor is refused rather than silently merged.
4. **Durability, version and recovery controls:** schema/application identity, foreign keys and immutable triggers, WAL/`synchronous=FULL`, bounded busy timeout, integrity checks, SQLite online backup and fresh-process reconstruction. Relate each to a real failure/negative test.

The historical [`sqlite-schema.sql`](../working-memory/evidence/2026-10-08-workspace-checkpoint-stores/sqlite-schema.sql) is an **experiment schema**, not the current production schema. The production schema is explicitly defined in `_TABLES`/`_LIFECYCLE_TABLES` inside `checkpoint_store.py`. No advanced SQL tuning, generic DBA curriculum, ORM or unrelated database technology unless a real project responsibility requires it. Separately, G2 mentions SQLite FTS5/BM25 as a *possible future text-retrieval exercise* only if a measured lexical-retrieval gap exists; that is distinct from the current Workspace persistence backend and is not selected or implemented.

**Later cost/historical-proof anchor:** [Completed 60-page instrumented raw access](../working-memory/evidence/2026-11-06-independent-host-timing/RESULTS.md) measured 2,380.532 host seconds; [AUDIT-015](../audits/2026-11-06_AUDIT-015_native-page-granularity-payload-and-publication-cost.md) notes the uncalibrated 4,096-character page default, repeated expression payload and expensive durable-delivery validation. Do not compare this full raw task to the ~43.820-second normal live invocation as a speedup: different workloads. The live paired question was answered with saved report/source, zero raw native pages; durability guarantees remain separate from candidate optimizations.
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


**Actual live transport case:** [First partial attempt](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) had two PyPI index timeouts. [Independent diagnosis](../working-memory/evidence/2026-11-06-pypi-transport-diagnosis/RESULTS.md) observed direct IPv4 TLS-handshake timeout, not a proven root network cause. [Verified alternate proxy route](../working-memory/evidence/2026-11-07-pypi-route-repair/RESULTS.md) isolated anonymous PyPI transport and direct authenticated GitHub without raising product budgets; [successor actual ledger](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) recorded 45 GitHub/63 total attempts and no implicit retry.
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


**Actual live dependency-source contrast:** first [target-only partial result](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) retained no selected old/new HTTPX modules after PyPI failure; the separate [live successor](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) established exact-version HTTPX declarations under source-association premises. FastAPI/Starlette remain *exploration samples* rather than target-installed version proof; eight omitted import candidates and other partiality remain visible.
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

**November 6 product continuation:** Optional CLI `--expected-base`/`--expected-head` now forward into the early PR prefix guard using the existing 40/64-hex revision-ID validator; mismatch refuses after one PR identity read, before source/worker/native publication. The [recorded red/green cycle](../working-memory/2026-11-06_caller-signature-cli-revision-guards_cycle.md) preserves the rejected 40-only assumption, observed failures and installed proof. This is a later F2 learning anchor, not a new prerequisite for C2.

**Critical ownership question:** Confirmed source revision A survives later report attempt B with lost acknowledgement. B may have been published; exact store inspection resolves that uncertainty, not a retry. A separate `--save-report` failure cannot erase an earlier confirmed Workspace report revision. Cold opening reads retained evidence without new network/AST/analysis/synthesis. Correct failure and unsupported-representation cases must refuse rather than silently fall back.

**Milestone boundary at the original small controlled F2 proof:** retained full-size navigation was not yet qualified then. Later F3 retained HTTPX evidence now qualifies its specific 60-page bounded native access and cold recovery (see D4 and F3), **not** unlimited paging, a fully successful source-only navigation baseline, live-provider behavior, independent usefulness or adoption.


**New live evidence boundary:** first [partial normal run](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) retained an acknowledged/cold-readable report despite missing pair; [successor run](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) recovered exact selected old/proposed witnesses and original source in a fresh installed process. Successful process, complete acquisition, saved revision, useful source answer and runtime action are independent claims; zero native raw pages were required for the selected report/source task.

**November 8 implementation — read when F2 is taught:** The [first-view Build](../working-memory/2026-11-08_maintainer-report-first-view_build-cycle.md) introduced deterministic `Review at a glance` in [`report.py`](../src/upgradepilot/report.py), retaining original saved reports, source IDs and fallbacks when role/version/root/comparison fields conflict. It is presentation, not a new evidence producer or action owner. The rendered offline HTTPX/OpenCV/Soup Sieve review and 61 focused/1,078 full-product tests passed. OpenCV's exact changed tags exist in saved selected facts but cannot be displayed by original-text-only `--show-source`; [LPA-004](2026-11-08-learning-to-product-engineering-audit-register.md) records the *conditional* typed-fact inspection opportunity.
## F3 — Product qualification: retained/live evidence, maintainer tasks, usability and adoption limits

**Product:** ✅ Connected retained qualification **plus one selected live installed HTTPX old/proposed pair and report/source task** verified; eligible for **limited explicit-profile pilot**. Runtime applicability, independent usefulness and broad adoption remain unproved.
**Learning:** ⬜ Not yet taught  
**Depth:** MUST OWN qualification, proof/non-proof and eventual task/adoption disposition

Owners: [active qualification cycle](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md), [qualified implementation plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md).

**Preserved retained history:** LifeLog/HTTPX/Digimon retained and authored-controlled qualification passed, with the older native six-page refusal and source-only 14/20 baseline remaining negative. A later [60-page raw task](../working-memory/evidence/2026-11-06-independent-host-timing/RESULTS.md) took 2,380.532 instrumented host seconds; [AUDIT-015](../audits/2026-11-06_AUDIT-015_native-page-granularity-payload-and-publication-cost.md) records deferred access/payload opportunities, not authorized changes.

**Live journey:** [Execution readiness](../working-memory/evidence/2026-11-06-native-product-execution-readiness/REVIEW.md) → [first live PyPI-timeout partial attempt](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md), which preserved 12 target files, source/report recovery, no HTTPX pair and abstention → [TLS-stage diagnosis](../working-memory/evidence/2026-11-06-pypi-transport-diagnosis/RESULTS.md) → [verified split route](../working-memory/evidence/2026-11-07-pypi-route-repair/RESULTS.md) → [separately activated successful live paired successor](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md). Successor: 45 GitHub/63 total requests, 24 files, 12 witnesses/five roots, **four exact-version HTTPX witnesses** in a selected TestClient root, three unexamined units, 147 gaps and eight omitted import candidates. Both versions' constructors accept five forwarded keywords under *sampled* Starlette `httpx2`-first fallback/receiver/dispatch premises. Saved witness paths/roles/outcomes and premises match native and cold report; runtime/CI `not_evaluated`, action `abstain`. Direct baseline: 38 source operations; report route: 26 bounded source reads plus a large decode, with zero raw pages; reviewer exposure and lack of human timing prevent independent usefulness claims. Limited pilot eligibility is **not** compatibility or merge permission.

**Post-live design disposition:** [Exact CI/runtime checkpoint](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) inspected July retained Docker CI with incomplete test-process proof and expired logs, October's exact-head 0-run result and November's source-only case. An offline replay of October's exact response through current CI owners passed 41 tests and correctly remained `no_successful_ci` / `no_exact_head_workflows`, runtime `no_admitted_candidate`. **Historical affected-path execution is unproved**, and no CI defect or basis for a new runtime runner/combined-profile Build was demonstrated. Next **product** handoff is the existing evidence-grounded AI design checkpoint; it must communicate missing facts, not fill them by inference.

Must distinguish historic retained exact inputs, controlled provider responses, outside-checkout installed proof, newly acquired real-provider observations, runtime applicability, maintainer usefulness and adoption. Successful controlled report delivery cannot prove all of them. No broad campaign or model/runtime experiment is activated by this module.


**November 8 independent-usefulness gate — not yet a pass:** [Reviewer packet technical readiness](../working-memory/2026-11-08_maintainer-first-view-review-readiness_planning-cycle.md) resolved an HTTPX rubric ambiguity in revision 3, with a [GitHub rehearsal handoff](../working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/README.md). The Git-visible HTTPX derivative is not the locally retained full report/source access. Eligible reviewers, equivalent permitted delivery and explicit execution remain open; participant outcomes and useful-task advantage have not been measured. Existing product plan owns the test, and [LPA-005](2026-11-08-learning-to-product-engineering-audit-register.md) only records this gate.
---

# PART G — Post-qualification design dispositions; learning later

## G1 — Combined evidence and runtime applicability: completed design checkpoint, historical gap preserved

**Product status:** ✅ **Design/checkpoint completed November 7**, [recorded cycle](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md). **Learning:** ⬜ Not yet covered; preserve current C2→D/E/F order before revisiting this.  
**Depth:** MUST OWN when reached.

Exact question: did the retained PR20 test process reach `tests/test_routes.py` L7 and the sampled Starlette HTTPX fallback/constructor? July's bounded green Docker run did not establish Python TestClient execution; October's exact-head GitHub Actions query returned zero runs, yielding `no_successful_ci`/`no_exact_head_workflows`; November's normal caller/signature profile retained static premises only. A hash-verified offline CI replay through current owners and 41 focused tests confirmed this classification; no new provider calls, no stronger runtime witness, no detected CI implementation defect.

**Disposition:** historical runtime applicability unresolved; do not implement a combined profile, runtime producer or target runner for this already-merged case. For a decision-relevant future case, first admit a target-owned test-process observation binding exact run/attempt/interpreter/checkout, reached call, loaded module/callable/file identity, installed artifact and relevant assertion; missing evidence stays missing. The [accepted §16 checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) governs. Product next: existing **evidence-grounded AI design checkpoint**, not agent execution.

## G2 — Evidence-grounded AI/retrieval and multi-agent investigation: proposed design prepared for review

**Product:** 🟡 The [comparison design](../plans/EVIDENCE_GROUNDED_MAINTAINER_EXPLANATION_COMPARISON_PLAN.md) is prepared for review, not execution. Current main selects review of the exposed HTTPX maintainer task and the strongest transparent deterministic baseline; a concrete presentation/interpretation gap must be established before any exact case/model/run contract. The [planning cycle](../working-memory/2026-11-07_evidence-grounded-maintainer-explanation_planning-cycle.md) also defines a separately gated two-worker/coordinator learning comparison. **Learning:** ⬜ DEFERRED until earlier evidence and Workspace modules are understood.

The plan separates evidence availability, retrieval, interpretation and presentation. It proposes same-material deterministic-versus-bounded-LLM comparison first; lexical selection before any semantic retrieval; optional SQLite FTS5/BM25 only if lexical misses are demonstrated; embeddings/reranking, LangChain/LangGraph and telemetry only when a measured task need earns them. The multi-agent exercise compares a single-agent control with source and CI workers plus a coordinator under the same total budget, but is a learning/product candidate, not an activated run. No model execution, new dependencies, product implementation, or broad RAG/agent architecture is authorized by this planning artifact.

**November 8 main update:** [maintainer first-view paired review](../working-memory/2026-11-08_maintainer-report-first-view_planning-cycle.md) compares exact saved HTTPX, OpenCV and Soup Sieve reports against concise sketches. It found a concrete presentation opportunity and one OpenCV wording correction, recommending a small task-focused view over existing report fields with explicit section selection and fallback; no renderer/build is selected. [Hybrid CI retrieval learning](../working-memory/2026-11-07_hybrid-ci-retrieval_learning-cycle.md) scored keyword 4/7 and embeddings/hybrid 6/7; one manager-environment evidence passage was missed, while the absent-proof control correctly withheld evidence. [Semantic retrieval successor](../working-memory/2026-11-07_offline-semantic-retrieval_learning-cycle.md) scored keyword 5/10, guided rewrites 7/10 and embeddings 9/10; embeddings still missed a short HTTPX fallback paraphrase and returned related material for a missing-runtime-proof query. These are bounded learning outcomes, not product adoption or general retrieval guarantees.

**New guided retrieval-history anchor:** [Offline FTS5 lexical case](../working-memory/2026-11-07_offline-evidence-retrieval_learning-cycle.md) actually selected five of seven known HTTPX/OpenCV evidence passages from nine read-only retained passages. The two original paraphrase misses are preserved; guided rewrites found them without changing the frozen result. Exact target/revision/version-role predicates controlled eligibility, while BM25 only ranked text. A later [CPU embedding contrast design/first failed pre-score attempt](../working-memory/2026-11-07_offline-semantic-retrieval_learning-cycle.md) froze the same evidence and a 384-token fit check, then stopped on a model-wrapper 128-token guard before any embedding result. A separately bound successor is not yet an evaluated answer at this horizon. No product integration, model-generated explanation or proven general retrieval benefit. **Do not confuse** G2's transient in-memory SQLite FTS5 table with D4's durable `CheckpointStore` SQLite database.

**Keep distinct from D4:** SQLite is already the product's explicit local Workspace persistence backend. SQLite FTS5 is only an optional future text-search exercise; do not infer it is currently part of Workspace or the product retrieval implementation.

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

**Learning-coverage snapshot (November 7, after live source, CI applicability and AI-design planning milestones):** 19 named modules = **6 covered interactively** (A1–A4, B1, C1), **5 introduced/in progress** (C2, D1–D4), **8 not yet studied** (E1–E3, F1–F3, G1–G2). **13 not yet covered**; among them G1/G2 are intentionally deferred design checkpoints, not immediate prerequisites. Implementation milestones do not automatically upgrade learning marks.

```text
COVERED INTERACTIVELY:  A1 A2 A3 A4 B1 C1  (6 of 19)
NOW:                    C2 historical result reconstruction and evidence-integrity validation (real HTTPX identity, coverage, transport, witness, MRO, constraint-sample, premise and runtime-boundary explanations covered; exact source-ID reconstruction and decoder contracts next)

NEXT:                   D1 D2 D3 D4 (previously introduced; continue)
                        E1 E2 E3 acquisition and exact provenance
                        F1 verified source-progress application
                        F2 verified user-facing CLI/report/Workspace delivery
                        F3 selected live HTTPX pairing/task qualified; broad usefulness/adoption unproved

LATER IN LEARNING:      G1 completed applicability checkpoint (historical execution unresolved)
                        G2 proposed comparison plan prepared for review; deterministic maintainer baseline review next; no model/agent execution
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
