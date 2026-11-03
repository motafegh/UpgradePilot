# Caller-Signature Native Pipeline — Living Learning and Mastery Roadmap

**Created:** 2026-11-02  
**Initial evidence horizon:** `7a9bef12fb65ee075dab645a638adf5a3955dc48`  
**Last synchronized main:** `834aeaa4` — November 3 method/depth clarification; product source unchanged from `9c903926`.
**Working branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`  
**Purpose:** living study/relearning roadmap for Ali's interactive learning track while UpgradePilot continues to evolve on `main`.  
**Authority boundary:** this file is a learning artifact, not the live project-position owner. `MEMORY.md`, current source/tests, accepted plans/specifications/ADRs, and dated evidence remain authoritative.

`UP-SKILL:upgradepilot-learning-artifact`

---

## 1. Learning method and anti-rabbit-hole rule

For every module use:

`real UpgradePilot case → responsibility boundary → essential code/data flow → important uncertainty/failure states → proof/non-proof → ownership check → stop`

Use [Operating Guide §7.2](../OPERATING_GUIDE.md#72-ai-assisted-engineering-ownership) for depth and [§7.3.1](../OPERATING_GUIDE.md#731-practical-attempts-and-evidence) for practical attempts. For a selected activity, establish its prerequisites, let Ali attempt it before supplying the complete answer, then inspect the actual result and assistance needed. Teach new material first. Learning-Only does not authorize product changes; a proposed modification and an implemented/verified modification are different evidence.

Depth:

- **MUST OWN** — reason about, review, challenge, modify/test, and explain with limited assistance.
- **OPERATIONAL** — trace/debug/review safely; exact helper details may be looked up.
- **LOOKUP** — recognize and recover when needed; do not spend session time memorizing it.
- **DEFERRED** — real depth that does not unlock the current project responsibility.

Do not turn a module into a general course on Python ASTs, compilers, networking, packaging, GitHub APIs, `requests`, persistence, or static analysis unless a real UpgradePilot problem requires that depth.

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
| Ordinary source publication/application/profile/report/recovery | MUST OWN the selected composition and its evidence/failure claims when implemented; it delivers the actual user workflow. | Forthcoming ordinary-path work is orientation-only before implementation. Report plumbing is initially OPERATIONAL; deepen touched mechanisms. Do not pretend the connected path exists yet. |
| Task qualification and later runtime checkpoint | MUST OWN qualification/non-proof and adoption reasoning when that gate is reached. | New runtime observer design remains DEFERRED; recognize existing scoped CI/runtime evidence without speculating a new runner. |

Revisit a depth when a real change/failure needs it, a fair attempt exposes a missing prerequisite, or the responsibility changes. The teacher recommends the depth with its rationale before asking Ali to choose an unfamiliar trade-off. Preserve a gap and its consequence rather than either silently lowering the target or making unrelated internals compulsory.

### Practical opportunities within the existing route

Select an opportunity when its module and prerequisites are active; these examples are not a second execution order or a quota. Use retained real cases and existing controls before authoring a disposable variant. No fabricated production defect or frozen-evidence rewrite is needed.

- **Correspondence/admission:** use retained LifeLog or Digimon to explain the paired/whole-file boundary, then inspect [the atomic native-group refusal test](../tests/test_source_correspondence.py). Let Ali predict which material remains retained and which work is unexamined under the authored limit before revealing the assertions. Interpret a related limit/case with reduced prompting; one guided answer does not establish broad analyzer ownership.
- **Acquisition ledger:** trace [the normal-prefix/later-client accounting test](../tests/test_caller_signature_acquisition.py), identify the charged timeout/retry and explain why a later stage does not receive another budget. Let Ali select a discriminating assertion or related-case check before presenting one; this controlled transport is not live provider proof.
- **Partial source receipts:** trace `examine_with_receipt` and [the failed-file preservation/no-retry test](../tests/test_caller_signature_source_acquisition.py). Distinguish earlier association/metadata/tag premises from unavailable text/hash and from the separate failed-association live-only limit. Ask for a related diagnosis or proposed source/test change; record whether it was only proposed or actually implemented and verified within authorization.
- **Connected source publication, once implemented:** follow one actual source-progress revision through a later analysis/delivery failure. Let Ali identify the last confirmed boundary and select evidence that could distinguish it from an unacknowledged successor. Derive the exact source/test anchor from that implementation instead of inventing the future path now.

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
- `834aeaa4` — November 3: merged the shared learning-method/depth clarification from main, refined scoped targets/practice and completion criteria here, and preserved prior module coverage. Product source and November 2 qualification horizon are unchanged; this is not a fresh product run or learner reassessment.

---

# PART A — Covered foundations

## A1 — Caller-signature evidence mental model

**Status:** ✅  
**Depth:** MUST OWN

Own these separations:

`static imported origin ≠ source correspondence ≠ local argument fit ≠ runtime dispatch/execution/behavior`

Real anchor: Digimon Requests `2.32.4 → 2.33.0`; direct `requests.get(...)` locally binds while forwarded `request(..., **kwargs)` remains undetermined. Neither proves runtime compatibility.

## A2 — Product-kernel ownership transfer

**Status:** ✅  
**Depth:** OPERATIONAL

- qualified analyzer now has one product implementation under `caller_signature`;
- experiment modules are compatibility/adapters, not a second evolving analyzer;
- retained semantic equivalence and installed-wheel proof are stronger than source relocation alone;
- kernel proof is not complete product-feature proof.

## A3 — `bindings.py`: scoped imported-origin analysis

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

## A4 — `analysis.py`: source facts + local argument comparison

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

# PART B — NEXT: correspondence and bounded work admission

## B1 — `correspondence.py` + work admission

**Status:** 🟡  
**Depth:** MUST OWN

### Learn

- `PythonSourceModule` roles and exact source/module identity;
- how retained target calls are conditionally related to old/proposed dependency declarations;
- relationship path steps, root call, selected declaration role, candidate ID and premises;
- direct imported-call, module/member, initializer/class and supported factory/protocol paths;
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

### Exit condition

Explain why a completed bounded analysis can legitimately leave files unexamined without meaning either “analysis failed” or “there is no evidence there.”

---

# PART C — Native analysis execution and integrity

## C1 — Typed input → bounded worker → run/result

**Status:** 🟡  
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

## C2 — Fixed reconstruction + evidence-graph integrity

**Status:** 🟡  
**Depth:** MUST OWN

Own:

- decode/reconstruction is not producer execution;
- exact input digest and source/fact/candidate references;
- shared trace referential integrity;
- malformed/foreign reference refusal;
- structural/byte guard meaning;
- node validity does not imply edge validity.

Real defect: swapped comparison call ID could retain the wrong witness path; repair required proving the compared call occurs at the exact unit/span in that path.

---

# PART D — Native families and Workspace lifecycle

## D1 — `caller_signature_sources`

**Status:** 🟡  
**Depth:** MUST OWN

Own the separation:

`exact source bytes` versus `premises/observations that justify source selection and association`.

Understand operationally: target receipts, dependency declarations/import candidates, release/source association, publisher observations, tag→commit, module request/receipt states, omissions/gaps, transport/work/limits, retention gaps.

Historical retained receipts may be incomplete and must never be upgraded into fresh provider proof.

Real anchor: glyphsLib remains valid for worker/protocol qualification but is not admitted to the source family because ordinary acquisition premises are missing.

## D2 — `caller_signature_comparison`

**Status:** 🟡  
**Depth:** MUST OWN

- comparison family stores the recorded analysis run against exact source material;
- failed analysis is a recorded operation, not `not_evaluated`;
- completed analysis can remain partial;
- source bytes are not duplicated into a second store.

## D3 — codec version vs producer method/version

**Status:** 🟡  
**Depth:** MUST OWN

- codec version = representation contract;
- producer method/version = semantic production contract;
- only admitted exact caller-signature producer pairs are supported;
- do not globally weaken older family version gaps.

## D4 — `NativeInvestigationCapture` + Workspace revision/checkpoint recovery

**Status:** 🟡  
**Depth:** MUST OWN

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

## E1 — Acquisition policy + shared physical-request ledger

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

## E2 — Exact target source context

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

## E3 — Exact dependency source association/module acquisition + partial receipts

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

# PART F — Current next product responsibilities (not yet implemented at this sync)

## F1 — Source-family composition + Workspace source-progress publication

**Status:** ⬜  
**Depth:** MUST OWN when implemented

Expected responsibility:

`AcquiredDependencyInputs/common prefix → target source context + dependency source receipts → CallerSignatureSources → partial Workspace publication BEFORE analysis`

Must preserve the failed-association retention limit unless a compatible representation change is deliberately justified.

## F2 — Normal application/profile composition

**Status:** ⬜  
**Depth:** MUST OWN when implemented

Connect the product-owned acquisition/session/source family/worker/comparison path through normal `investigation.py` composition without turning it into a god-function or refetching the PR prefix.

## F3 — CLI/report/source/save/cold-recovery delivery

**Status:** ⬜  
**Depth:** OPERATIONAL→MUST OWN for evidence claims

Learn the user-facing route only once implemented: profile selection, report/source navigation, saved investigation reopening, and explicit claim/non-claim boundaries.

## F4 — Actual connected product/task qualification + usefulness/adoption

**Status:** ⬜  
**Depth:** MUST OWN

Distinguish controlled/retained/installed component proof from an ordinary connected product attempt and from maintainer usefulness/adoption evidence.

---

# PART G — Scheduled later checkpoint, deliberately deferred now

## G1 — Combined evidence + runtime applicability design checkpoint

**Status:** ⬜ DEFERRED  
**Depth:** MUST OWN only when its plan gate is reached

Current main schedules this checkpoint **after connected product qualification/task disposition**, before optional source expansion/non-required case campaigns.

When reached, learn/design how existing static caller-signature evidence, CI/runtime command-completion state, installed package state, import/dispatch, affected-path exercise and behavior evidence can be combined without strengthening claims beyond exact identity/environment/time/material joins.

Do not pre-study speculative runtime observer design now. Reuse existing CI/static/target-owned evidence first; new runtime observation must be justified by a concrete unresolved proposition.

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

```text
DONE  A1 mental model
DONE  A2 product-kernel transfer
DONE  A3 bindings.py
DONE  A4 analysis.py extraction + compare_arguments

NEXT  B1 correspondence + work admission
      C1 worker/run/result lifecycle
      C2 fixed reconstruction/integrity
      D1 source family
      D2 comparison family
      D3 producer/codec version semantics
      D4 Workspace capture/revision/cold recovery
      E1 acquisition policy/shared ledger
      E2 target source context
      E3 exact dependency source acquisition/partial receipts

THEN, as main implements them:
      F1 source-family composition + source-progress publication
      F2 normal app/profile composition
      F3 CLI/report/source/save/recovery
      F4 connected product/task qualification + usefulness

LATER AT PLAN GATE:
      G1 combined evidence/runtime applicability
```

### Flow understanding and ownership evidence

Flow understanding is established at the demonstrated scope when Ali can trace a real case across:

`PR/input → bounded source acquisition/provenance → source-family publication → bounded analysis → comparison evidence → Workspace recovery → normal user-facing result`

and can explain, for each boundary:

- who owns it;
- what exact evidence enters/leaves;
- what failure/unknown states mean;
- what the evidence proves;
- what it does **not** prove;
- where to inspect or test it when behavior changes.

For ownership-bearing completion at a selected scope, also preserve an actual meaningful practical attempt with its result, assistance and limitations. Relevant evidence can include selecting and interpreting a discriminating test, causal diagnosis, or a justified modification with appropriate verification. Stronger implementation/transfer claims require corresponding action and changed-context or reduced-assistance evidence; explaining where a test lives or proposing a change alone does not establish implementation ownership.

If this evidence remains unavailable, record the ownership gap explicitly while retaining truthful lesson coverage and any justified continuation. No historical checkmark is automatically promoted or erased. Memorizing every helper/API, owning every advanced internal before product work continues, and a new cross-project capability score are not required.
