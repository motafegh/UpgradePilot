# Two-track operating decision — UpgradePilot and AegisLab

- **Prepared:** 2026-11-22
- **Status:** Recommended four-week initial operating allocation for owner use/review; not a command to change UpgradePilot main or AegisLab implementation
- **Owner context:** Learner's approx. 30-hour/week availability, AI-first learning-by-doing, target AI Security Automation Engineer
- **Authority boundary:** This independent research document records strategic advice. The live UpgradePilot `MEMORY.md` and AegisLab's normative docs remain authoritative in their own repos. AegisLab proposal is not yet its accepted Charter.
- **Related research:** [Project transition discovery and AegisLab rationale](2026-11-22_learning-portfolio-project-discovery.md) and [Independent maintainer utility study](2026-11-22_1911_independent-maintainer-utility-supervision.md)
- **Provenance:** UP-SKILL:upgradepilot-workstream-supervision; UP-SKILL:upgradepilot-working-memory

## 1. Why change the allocation now

UpgradePilot is a mature *learning and engineering corpus*, with extensive evidence/CI/provenance semantics and significant repeated testing. Its November 22 exposed F4 reviews uncovered a report-navigation problem but did **not** establish independent usefulness or time savings. A saved-report comparison at `90601aa156913ed12afe683f27e15fe64990a185` qualified **one bounded deterministic CI first-view Build** for well-bound, successful command observations; neither the Build nor human benefit had been demonstrated in that recorded main state.

AegisLab's long-term canonical identity already matches AI/security operations, but its v1 Core excludes AI and defers the full investigation path behind Docker/VM parity. The AegisLab main branch received **a proposed** [AI-first evolution plan](https://github.com/motafegh/AegisLab/blob/main/docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md) in commit `939225acc7690155d9634dca20efa6a2ba4e67b8`; its Core Charter v1 and original execution documents remain active until explicitly revised. At the November 22 WSL read-only check, local AegisLab `main` was clean but still at `b5f0234840338e2af012c46cfb4ead1ebcec0cad` (one proposal commit behind GitHub). Local UpgradePilot `main` matched `90601aa1` with two pre-existing untracked documents, neither touched.

**Conclusion:** Portfolio/product strength and learning breadth are now distinct allocation problems. Prioritize AegisLab as the *personal learning and security-operations flagship* while preserving UpgradePilot as a *bounded product and portfolio flagship*. Do not start a third primary project or imply the late AI implementation already exists.

## 2. Recommended four-week allocation (Nov 23–Dec 20, 2026)

| Personal focused time | Weekly budget | What counts |
| --- | ---: | --- |
| **AegisLab** | **20 hours** | Direction adoption, new end-to-end security behavior, personally running/debugging Linux/network and local AI cases, technical comprehension and evaluation. AI agent runtime is not counted as personal study hours. |
| **UpgradePilot** | **6 hours maximum** | Product and risk supervision, bounded first-view Build acceptance, maintainer workflow/usefulness follow-up, essential defects and a small evidence-grounded learner/portfolio exercise. |
| **Career / transfer / preparation** | **4 hours protected** | Hands-on independent recall/diagnosis across projects, concise demonstrable portfolio case studies, job-market comparison/applications or interview practice. |

This is an **initial recommended policy**, not a retrospective claim of hours actually worked. Reassess after four weeks or sooner if a real high-severity issue or major learning bottleneck changes priorities.

### UpgradePilot: explicit work-in-progress and scope limits

**One active meaningful product increment at a time; next justified selection:** Build the **qualified deterministic CI first view** over existing typed saved data, with a complete exact job/step/command association guard. Keep installed-version unresolved; no inferred successful pip package consumption. Continue existing detail for unbound, skipped, mixed and failed cases. Verify MapProxy positive cases and missing/skip/ApplyPilot controls, saved/native path and backwards compatible reads as applicable. Do not call this implemented until code and tests exist.

**Next decision after that Build:** use realistic maintainer tasks, preferably at least two independent competent eligible humans with exposure checks, matched inputs and comparable start times, to establish *incremental utility*. If recruitment is impossible, retain development-only results and qualify portfolio claims honestly. An independent pilot is valuable but should not trigger months of packet engineering or a false study.

**Allowed between these gates:** fix severe trust/security or reproducibility defects when evidenced, ensure a clean setup/demo and a concise README/case study, and operate minimal tests/CI. New features are explicitly deferred unless a user-observed task demands them.

**Avoid:** broad new acquisition pipelines, transitive-dependency expansion, speculative ML, new agent frameworks, general UX platform, giant CI matrix rewrites and endless evidence polishing to keep engineers/agents occupied.

**Human ownership:** cap personal UpgradePilot involvement to six hours in an ordinary week even if a separate coding agent can work asynchronously in its own independent workstream. Review its work only at coherent gate receipts; do not confuse agent-compute time with focused human learning time. Keep the parallel main workstream's publication protocol and independent research branch separation intact.

### AegisLab: focus on personally transferable new engineering

In the next month, the **first commitment is direction-adoption work**, not automatic full product completion. The separate AegisLab assistant should read `AGENTS.md`, accepted v1, and the proposed plan, inspect the actual local/remote state, and reconcile an accepted v2 Core and capability-led execution map without throwing away historical learning/evidence. Then begin the earliest truly runnable deterministic end-to-end incident from authorized retained observations, followed by material local AI comparison and live-operations/agent-security learning as prerequisites permit.

**Learning quality check:** select an actual failure/uncertainty, predict expected behavior, run and interpret real output, personally diagnose or intentionally change one consequential case, distinguish assisted from independent understanding, and package concise proof. AI is permitted to code; it does not authoritatively certify learner mastery.

**Critical distinction:** AegisLab's *operational evidence and security-agent runtime* responsibilities must stay distinct from UpgradePilot's dependency-maintainer workflow, even when both use evidence provenance and conditional AI.

## 3. Decision gates and operational rules

**Every week (brief):** one AegisLab working demonstration or specific technical blocker, one concise UpgradePilot main state review, and one personal changed-case/diagnostic account; no repeated full architecture audits unless the evidence actually calls for one.

**At four weeks (~2026-12-20):**
- **AegisLab:** Does the new track show a real running slice, substantial Linux/security/LLM skills and personally understood failures? Did the time allocation give visible progress and interest? What should be dropped or increased?
- **UpgradePilot:** Is qualified first-view behavior implemented and faithfully tested? Can a competent maintainer actually use and compare it to existing tools? If benefit still unestablished, is a small independent pilot feasible, or should the project operate in maintenance/portfolio mode until a concrete task revives investment?
- **Career:** Are there demonstrable interview examples (not claims based solely on generated code), clear explanation of contribution provenance, and at least one new responsibility beyond Python CI/evidence analysis?

**Decisions after review:**
- If UpgradePilot has no established task-level value or eligible evaluation, keep it in a defined maintenance posture (e.g. 2–4 h/week as warranted) and avoid indefinite research; do not delete it or claim it failed.
- If credible maintainer benefit emerges, allow narrowly justified product work—but adjust hours deliberately rather than silently expanding one project.
- If AegisLab becomes AI-generated scaffolding without personally transferable mastery, change learning mechanics or project scope promptly, not simply add features.

## 4. Handoff boundaries

- This record lives only on the **UpgradePilot independent research branch**, not `main`.
- The full AegisLab evolution plan is at `motafegh/AegisLab/docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md`, proposed until accepted.
- Any AegisLab assistant must first reconcile its clean local main (`b5f0234` at read time) with remote main proposal commit `939225ac`, without overwriting user changes, and must verify fresh state.
- A future handoff prompt can explicitly authorize AegisLab-only charter/plan alignment and first Build on its own `main`, subject to safe worktree and consequential-operation authorization. Never grant that assistant authority to modify UpgradePilot main.

## 5. Status and verification

This is a career/project-time policy and handoff recommendation; no time tracker has been observed, no external human usefulness claim is made and no UpgradePilot source, tests or AegisLab accepted charter is changed by this file. Confirmed live UpgradePilot main head: `90601aa1` (2026-11-22); AegisLab remote head: `939225ac` (2026-11-22).


## 6. Historical knowledge recovery, retention and transfer — 2026-11-22

**New owner concern:** After about four months of AI-assisted UpgradePilot engineering, many previously explained concepts may be forgotten, incompletely understood or never demonstrated independently. The learner wants a sustainable way to review and relearn them **while also developing AegisLab, supervising UpgradePilot and preparing for hiring**. This is a real ownership objective, not evidence of a particular personal knowledge deficit. Do not infer mastery from earlier AI-produced notes, approved designs, running tests or the mere presence of 120 source files.

### Existing assets and why not to create a parallel curriculum

The current `learning/README.md` already preserves grounded, commit-pinned learning packages, a fast-relearning route, ownership-depth categories and a distinction between AI-authored study artifacts and proven learner understanding. `OPERATING_GUIDE.md` already defines bounded code/test/evidence learning, a depth-aware AI-first ownership model and Learning-Only work. Use these existing source/learning owners as the learning **material**. Do not create a second canonical live project tracker, duplicate all learning packages, or teach the old chronological milestones one by one. The active `MEMORY.md` continues to own current UpgradePilot status.

The [portfolio presentation strategy](2026-11-22_upgradepilot-public-portfolio-repository-strategy.md) already covers public safety/metadata, entrypoints, provenance-retaining storage, cases and truthful AI contribution. **No duplicate portfolio restructuring decision is needed.** Recovery work should yield personally defensible examples for that strategy, but it does not authorize main changes.

### Selective capability triage, not an exhaustive four-month replay

Select capabilities according to **future relevance × current uncertainty × demonstrated ownership gap**. A first pass is a *hypothesis list for assessment*, not a verified learner-skills evaluation:

| Priority | Capability family | Why/where to test practically |
| --- | --- | --- |
| **P0** | Python code navigation, CLI/package layout, interfaces, tests, debugging, Git and environment boundaries | Trace one real CLI input through modules to a report; identify the focused test; change a fixture; distinguish source checkout and installed wheel |
| **P0** | Evidence / truth / provenance / proof strength / uncertainty | Reopen one MapProxy, ApplyPilot or AV-Tracer report; state exactly what failed/succeeded and what was *not* proven; identify an appropriate next observation |
| **P0** | Linux process, network, permissions and transport fundamentals as needed | Diagnose an AegisLab service, SSH/auth, socket, routing or collector problem; distinguish command outcome, target effect and sensor observation |
| **P1** | Dependency/CI mechanics — pip, uv, requirements, environment selection, GitHub Actions jobs/steps and matrix identity | Compare workflow static declarations, actual command outcome, installed-package observation and import/use; reproduce failed/skip/missing controls |
| **P1** | Data contracts and failure states, persistence/recovery/versioned schema, deterministic replay | Trace saved report/Workspace creation and offline open; inject one missing/invalid/stale version; explain non-proof of recomputation |
| **P1** | AI/LLM engineering and security — prompt/tool boundaries, provider transport, structured semantic output, hallucination/entailment, evaluation design | Compare local model and deterministic baseline on one sourced case; test an injected low-trust string, malformed response or unavailable model |
| **P1** | Architecture judgment, module responsibility, ADRs, refactoring and proportionate verification | Explain why one component owns a proposition, locate a boundary test and critique a proposed cross-layer fix |
| **P2** | Deep package-manager edge cases, every historical CI matrix variant, deferred agent orchestration, all ADRs and every past experiment | Lookup/relearn when selected work truly requires them; recognition is enough in the meantime |

The priority order is adjustable: an actual diagnosed deficit or near-term hiring requirement can change it. For each selected **responsibility**, assign one of the existing project's depth labels: **must master/own; understand operationally; recognize/lookup; defer deliberately**. Avoid whole-library or whole-directory mastery targets.

### Repeatable learning recovery session (about 60–90 minutes, not a new governance cycle)

1. **Retrieve without re-reading (5–10 min):** In your own words sketch the actual purpose, inputs/output, important source path, expected failure and what a success result does **not** prove. Record uncertainty; memory lapse is diagnostic, not failure.
2. **Reconnect to current evidence (10–20 min):** Inspect current code, one representative focused test and relevant accepted contract. Use the existing frozen learning note only as a reference, explicitly separating its historical revision from present `main`. Do not read all historical worklogs.
3. **Changed-case practice (25–40 min):** Predict a nontrivial negative/boundary state; reproduce or modify a safe fixture, command or small implementation; run/inspect actual output; identify the responsible layer. AI can scaffold but must not supply the complete diagnosis before the learner attempts.
4. **Teach back and calibrate (5–10 min):** Explain the observed behavior, what data established it, what remained missing and why one alternative explanation is less likely. Label whether the result was guided, assisted, or independently demonstrated; never infer independence from AI-generated prose.
5. **Schedule one small delayed check:** within roughly 2–3 days, after a week and after 3–4 weeks when practical. Revisit the *changed case or question*, not the full document. If the second check fails, relearn the narrow concept instead of rereading months of material.

Stop when the mechanism can be applied to the selected need; do not manufacture deeper obligations for low-relevance historical details. A completed learning note is not a passed ownership gate. For persistent gaps, use the existing Learning-Only and artifact process to record one concise source-linked correction or exercise.

### Workload — include recovery inside the agreed proposal, never add a fourth project

Under the provisional **20 h AegisLab / 6 h UpgradePilot / 4 h career+transfer** allocation:
- **AegisLab 20 h:** majority remains building and running the new project. New Linux/network/AI concepts are learned **in the actual implementation**. Prefer transfer checks over another textbook.
- **UpgradePilot 6 h maximum:** roughly 1–2 hours, *when justified by the current increment*, may include a concrete product-code or CI/evidence ownership exercise. The remainder stays on bounded product supervision, validation and maintainer usefulness. This is a guideline within six hours, not a newly added budget.
- **Career and transfer 4 h:** allocate around **two hours** to spaced knowledge recovery/practical transfer and the other **two hours** to portfolio/interview examples, applications and job-market alignment. Protect this time from agents' open-ended requests for more review.
- On a heavy product week, **one genuinely new transfer exercise across both repositories is sufficient**; do not impose a quiz after every AI commit.
- A worthwhile combined learning exercise is: **review one UpgradePilot evidence/proof issue, then find its analogous source-vs-observation problem in AegisLab**, while ensuring different runtime mechanisms are actually learned (CI/Python in one, Linux/network/telemetry in the other).

### First four-week recovery route (proposed, adaptive; not scored as completed)

| Week | One principal UpgradePilot memory target | Practical proof | AegisLab / portfolio transfer |
| --- | --- | --- | --- |
| 1 | **End-to-end Python product flow and test ownership** | Follow CLI → acquisition → evidence/interpretation → saved report; identify one focused negative test and explain its assertion/non-proof | Trace AegisLab's first input-to-finding flow; sketch a 3-minute interview explanation |
| 2 | **Evidence strength and CI semantics** | On MapProxy and ApplyPilot, distinguish static step, exact executed command, exit status, installed package state, skipped/missing evidence and target use | Explain command/executor/sensor/target distinctions for SSH evidence |
| 3 | **Python environments, dependency resolution and recovery** | Compare an installed wheel/venv with repo source, trace one `pip`/`uv` or version/requirements assumption, and deliberately test a failed or unresolved boundary | Debug one AegisLab runtime/deployment/env discrepancy |
| 4 | **Model/agent trust boundaries and independent diagnosis** | Show why valid citations/structured output do not prove semantic entailment; test one malformed/false/low-trust input or provider failure on an available bounded case | Transfer to an AegisLab local model/agent boundary, or mark transfer blocked if that module is not yet built |

The schedule is a **sampling plan**, not a promise to master these topics in four weeks. Adjust to real AegisLab progress; defer Week 4 hands-on model work if the model is not yet operational. Use existing `learning/` snapshots, `docs/` semantics, `src/` and `tests/` as sources—not new duplicated lessons.

### Minimal progress/ownership evidence (one compact entry per practiced responsibility)

Track only: **topic and concrete task; dated source revision; first unaided explanation/prediction; observed command/test/result; assistance level; diagnosed or modified changed case; one remaining gap; next delayed recall date**. Store in the current relevant learning cycle or a justified canonical learning artifact, not a global noisy spreadsheet, separate status system or new skill-label taxonomy. A single sentence can suffice for a routine recovery.

The long-term decision is not "have we memorized four months?" It is "can the learner now **operate, challenge, repair and explain** the engineering responsibilities most valuable for future work and hiring, while remaining capable of researching unfamiliar details?" Retain documentation as an external memory rather than requiring comprehensive recall. Reassess the recovery queue monthly and prune low-value topics.


## 7. Cross-project collaboration and future instruction/specification decision — 2026-11-22

**User direction:** Preserve the portfolio/audit recommendations and historical knowledge recovery decisions already recorded, then decide **how to execute each direction** and whether existing assistants need new, targeted instructions or specifications for their distinct jobs. The user has not yet approved a full new cross-project instruction framework; this is a **coordination design for future joint decisions**, not permission to add blanket AI rules, edit main or restart workstreams. Prioritize usable execution over more files.

### Status reconciliation before choosing instructions

- **UpgradePilot `main` checked at `90601aa156913ed12afe683f27e15fe64990a185`** on November 22. The qualified CI first-view design and the exposed F4 development-review limits remain the current observed basis in its `MEMORY.md`; no independent human usefulness or speed effect has been established.
- **AegisLab `main` advanced separately to `feed0b428f94e2e3cf936de89b455ac90537ff1e`** by November 22. Its active `PROJECT_STATE.md` now reports **accepted Core Charter v2** (`docs/plans/AegisLab — Core Charter v2.0.md`) and **Capability Execution Map v2**; this supersedes the previously tentative/awaiting-adoption language in this research document. A first runnable **Stage B synthetic SSH-auth incident CLI** with 15 reported passing tests was committed at `d6abf89da`. This is a *repository handoff report*, not an independent test rerun by this supervising session and not a claim of true live sensor evidence or learner mastery. Latest commit `feed0b428` records **Stage C local model-list HTTP transport reachability**, with an ambient WSL HTTP proxy bypass needed; no loaded model, successful inference, or AI quality result is proven by this connection check.
- This is an example of **parallel-workstream drift**: learning/strategy records must present their facts at the observed commit and defer to the live respective repo owner. Never send a stale “please adopt v2 and begin Stage B” prompt to the assistant that has already done so. Future instructions must begin with current-state reconciliation.

### Distinct workstreams (scope, evidence and limits)

| Workstream | Primary outcome | Existing owner / likely AI role | Next question or gate |
| --- | --- | --- | --- |
| **AegisLab implementation** | Safe, observable Linux security events and evaluated AI-assisted investigation with agent controls | AegisLab `AGENTS.md`, active v2 Charter/stage map, AI Collaboration Protocol; build/debug assistant | Stage B learner changed-case proof; Stage C model result vs baseline; later live Stage D. Avoid letting AI implementation progress be mistaken for personal skill. |
| **UpgradePilot product and usefulness** | Reliable, maintainable evidence-backed dependency update CLI and actual maintainer utility | UpgradePilot `MEMORY.md`, Charter, specifications, selected product plan and `OPERATING_GUIDE.md`; bounded build + independent evaluation | Qualified CI first-view presentation Build with preserved states, then real comparable usability evaluation; stay within six personal hours. |
| **UpgradePilot public portfolio** | Clear employer-facing capability, demonstration and AI attribution without provenance loss | `README.md`, `docs/README.md`, existing `examples/`, proposed `docs/portfolio/`; editor/reviewer posture | Approve security/rights/metadata/license choices, then do short entry-point and reproducible offline walkthrough; do not mass-delete history or claim a release. |
| **Knowledge recovery / transfer** | Retain and independently apply selected four-month engineering concepts while learning new ones | `learning/README.md`, `OPERATING_GUIDE.md`, existing Learning-Only/learning-artifact skills; focused mentor/evaluator posture | Start with one UpgradePilot source-to-report changed-case explanation; use staged recall and cross-apply to AegisLab mechanisms; no exhaustive rereading or new curriculum. |
| **Career and hiring evidence** | Personally defensible project stories, interview-grade diagnostics and honest AI collaboration disclosures | Small curated portfolio artifacts and personal practice; no new repo authority | Show what actually ran, was personally diagnosed, and was independently understood; no unsupported readiness/adoption claims. |
| **Independent supervision / coordination** | Prevent drift, contradictory instructions, unconstrained AI-generated work and time-budget erosion | This research branch; existing per-repo current-state owners; supervisor/reviewer posture | Verify milestone evidence and learning ownership at bounded intervals; keep product and learning state separate; do not silently mutate other workstreams. |

### Decision procedure for new AI instructions, specs or plans

**Use existing governance first.** UpgradePilot already has extensive `AGENTS.md`, `OPERATING_GUIDE.md`, local `.agents/skills/`, `docs/` specifications/ADRs and learning artifacts. AegisLab now has active `AGENTS.md`, Core Charter v2, stage map, AI Collaboration Protocol, Learning Preferences and learning state. Do not create a second root governance file or paste a cross-repo mega-prompt into both repositories merely for apparent consistency.

| Artifact type | Use only when… | Proper owner and shape | Do not use for… |
| --- | --- | --- | --- |
| **Agent instruction / working protocol** | A repeated cross-session behavior is currently missing, unclear, contradictory or demonstrably costly | Update relevant existing `AGENTS.md`, assistant protocol or a focused skill; concise precedence, input source, stop/authority, expected output | Redoing accepted project semantics or making every tiny task a ceremony |
| **Product specification / acceptance contract** | An actual implemented behavior requires durable cross-implementation meaning, security invariants or tests | Existing product-spec owner or active AegisLab Charter/module contract; include positive, negative and proof/non-proof cases | Career scheduling, one-off exercise instructions or aspirational future features |
| **Bounded plan / handoff** | A selected next responsibility has multiple steps, dependencies, side effects or proof gates | One short plan with scope, entry, stop, success and ownership; update current status owner only upon real change | Reopening settled design, parallel redundant roadmaps or claiming software has shipped |
| **Learning session / transfer protocol** | User needs to recover a real skill or ownership gap | Existing learning method + minimal practical task/changed case; one assistance and evidence note | Inference of mastery from AI code, forcing hand coding or duplication of historical study artifacts |
| **Portfolio / editorial guide** | Public reviewer cannot readily identify product, proof and personal contribution | README/one curated portfolio path, short demo, factual evidence links | Rewriting source architecture, mass archival or claims of product-market validation |

**Admission gate for ANY new document:** (1) name its distinct durable owner, (2) identify a real current gap that existing artifacts cannot satisfy, (3) define its expected operational decision/test or repeated behavior, (4) keep it smaller than the cost of the problem it solves, and (5) nominate links/status that need reconciliation. Otherwise **use a short prompt or an existing section**, not another file.

### Multi-assistant boundary and review design

- Keep assistants' **roles explicit by task**: builder, learning mentor, independent reviewer, public portfolio editor and strategy supervisor. The roles may share one model, but independence must not be claimed when the assistant has prior case exposure or participated in building the artifact.
- Builders may implement/commit within their authorized repo and current scope; reviewers check claims against observed tests/artifacts and note missing evidence. Reviewers should not silently change active source or invent external independent evaluation.
- Time control is about **learner time**. Additional AI coding does not justify consuming extra learner review hours; supply compact verified milestone receipts, source paths, unresolved issues and one learner-owned exercise.
- For active work, the respective repo's live status and normative docs take priority over this research branch. Strategy records capture past decisions and proposals, not real-time implementation status.
- Reuse code/knowledge across projects deliberately where a shared engineering principle is valuable, but avoid cloning UpGradePilot's long evidence/report/governance infrastructure into AegisLab.

### Recommended next joint decision sequence (not yet authorized for execution)

**Decision 1 — Workstream responsibility/priority:** Confirm the provisional allocation (20 h AegisLab, 6 h UpgradePilot, 4 h career/transfer) and select one specific near-term outcome per direction. The AegisLab assistant is already implementing v2, so supervise from the actual Stage B/C proof state rather than repeating its kickoff.

**Decision 2 — Learning/ownership:** Select the first 60–90-minute diagnostic session, initially UpgradePilot CLI→evidence→report/test flow; record demonstrated vs guided knowledge and one changed case, then decide what must be relearned. Cross-transfer relevant lessons into AegisLab.

**Decision 3 — Product/public presentation:** For UpgradePilot, complete the admitted CI first-view Build or explicitly choose the limited README/portfolio-first alternative. Set the separate security/rights review and true example readability as acceptance gates; don't combine product and marketing claims.

**Decision 4 — AI guidance edits:** After those concrete choices, compare how existing guidance actually supports them. Draft *only* the smallest targeted amendment (likely an AegisLab Stage B learner-ownership handoff, or a concise UpgradePilot public-portfolio editing brief) **if** existing guidance proves insufficient. Never invent a broad second instruction/spec regime without evidence.

**Review cadence:** brief weekly project/learning evidence snapshot and a meaningful four-week reassessment around December 20. Change hours or process sooner on observed safety risk, repeated role confusion, real user value or serious learner block—not because an agent has capacity for more docs.

**Non-actions recorded:** No additional canonical instructions, product specifications, source, root README, branch merges, release, license decision, repository deletion, or main-branch state edits are authorized or performed by this research update. AegisLab live progress is an independently observed source-read snapshot and may change after this date.


## 8. Owner agreement and practical-artifact selection ledger — 2026-11-22

**Decision status: STRATEGIC DIRECTION AGREED; PRACTICAL ARTIFACT SCOPE TO BE SELECTED NEXT.**

After considering the full portfolio audit, four-month recovery strategy, two-project allocation, and differentiated AI-assistance roles, the owner explicitly agreed to the strategy and requested that the decisions be **recorded first**, then used together to select any necessary practical documents, specifications, instructions or execution methods. This section is the consolidated decision and admission ledger—not a newly accepted AegisLab product contract, not a main-branch change, and not authorization to generate a parallel governance hierarchy.

### A. Accepted operating principles, with authority limits

1. **Project identity:** AegisLab is the primary new learning and security-engineering flagship; UpgradePilot remains a serious maintained product, evaluated for actual maintainer utility and presented credibly for hiring. Do not abandon or rewrite the historical work of either.
2. **Personal time:** use **20 h AegisLab / 6 h UpgradePilot / 4 h career-and-transfer** as the agreed **initial planning allocation**, not measured time spent or a permanent obligation; review around **2026-12-20**, changing sooner if actual evidence warrants. Protect the learner's time from unrestricted agent-generated additional work.
3. **AI-first collaboration:** permit AI implementation; require the learner to understand selected responsibilities, predict relevant behavior, diagnose changed cases and defend important decisions. Do not require manual authorship of every line, and do not certify competence from passing tests or generated explanations alone.
4. **Historical knowledge recovery:** prioritize reusable engineering concepts by practical need and demonstrated gaps. Use existing `learning/`/operating-guide assets and short recall → current source/test → changed case → explanation → delayed revisit; no complete chronological four-month relearning, mandatory quiz for every commit, or duplicate global skills ledger.
5. **Portfolio:** preserve source, tests, canonical documentation and historical provenance by default. Create a short hiring entry point, one authentic offline-first demonstration and a few defensible engineering stories. Disclose heavy AI code assistance and unestablished real-user benefit; conduct privacy/third-party-rights review before repackaging historical artifacts. No bulk deletion/history rewriting merely to reduce file count.
6. **Multi-assistant roles:** builders, reviewers, mentors and public portfolio editors operate against task-specific permissions and proof gates. Independent review claims require actual independence from the build/case exposure. Do not confuse implementation verification, user utility and learner mastery.
7. **Instruction economy:** evaluate the *existing per-repo instruction/specification/plan owner* before creating anything. Write a new artifact only when a distinct repeated behavior, tested contract or execution need cannot be handled adequately by an existing file or a bounded task prompt.
8. **Truth, authority and current evidence:** user decisions and each repo's active canonical owners control their responsibilities; these historical research records do not override `UpgradePilot/MEMORY.md` or `AegisLab/PROJECT_STATE.md` and active Charter. Recorded old states remain accurate only for their cited revision.

### B. Reconciled live evidence at decision time

**UpgradePilot:** Published `main` advanced to **`91a824cb4ee35aee92929b288dc0c67c01be6bda`** ("Summarize exactly scoped CI commands in the report opening"). `MEMORY.md` reports the **bounded deterministic CI first view delivered in renderer 6**, with the normal MapProxy seven-command grouping, shared unresolved installed-version explanation, source-facts route, and ApplyPilot/skipped/missing controls retained on the detailed path. The Build reports **1,192 installed product tests passed, zero skips**; this supervising session inspected the repository record but did not rerun them. Independent human maintainer usefulness or speed benefit **remains unestablished**. Earlier passages in this ledger that call the first-view Build `next` are historical and are **superseded by this newer status for selecting next work**. Remaining potential work is usefulness validation, bounded presentation/portfolio changes, and justified defects—not repeating the finished Build.

**AegisLab:** Published `main` at **`feed0b428f94e2e3cf936de89b455ac90537ff1e`** at this decision inspection. AegisLab reports accepted Charter v2 and Stage B deterministic SSH incident CLI on explicitly synthetic fixtures; historical namespace observations were guided and not retained as importable sensor logs. Stage B's learner-owned changed-case diagnosis remains open. Stage C had only tested local model catalog transport and a proxy bypass—not model inference. This is the owning repository's reported evidence horizon, not a claim that this session independently reran tests. Do not redirect that implementation assistant with outdated v2 adoption instructions.

### C. Practical artifact map — **candidate dispositions**, not execution authorization

| Direction / immediate need | Existing document owner | Recommended artifact or instruction action | Status / selection gate |
| --- | --- | --- | --- |
| **AegisLab working milestones** | Active `AGENTS.md`, Charter v2, capability map, AI Collaboration Protocol, learning state | **Reuse existing authority.** Give the other assistant only a short current-state, specific-stage task prompt when needed; modify its learning handoff only if missed learner practice recurs. | **No new cross-project agent specification now.** First inspect Stage B learner gate and Stage C measured evidence. |
| **UpgradePilot actual maintainer usefulness** | `MEMORY.md`, existing usefulness-evaluation plan and technical report owners | **Select a bounded task**: evaluate the delivered first view with a comparable human task or explicitly document why independent review is not presently feasible. Do not redesign the already delivered renderer or invent independent validation. | Needs explicit scope, eligible-reviewer plan and equal exposure/start conditions before claims. |
| **UpgradePilot hiring front door** | `README.md`, `docs/README.md`, `examples/` and relevant evidence | **Likely one bounded implementation/editorial brief** for shorter README entry, small portfolio route and an offline-first case; one focused `docs/portfolio/README.md` only if justified. | First settle what may safely be public, the license decision, current demo selection, and exact supported claims. |
| **UpgradePilot strategic status reconciliation** | `PROJECT_CHARTER.md` for stable identity, `MEMORY.md` for live state | **Targeted amendment to existing Charter / routing** when two-track policy is promoted to UpgradePilot operational authority, preserving the July–October original period as dated history. | Not a separate new charter or a rewriting of old results. Requires explicit accepted scope with existing main workstream. |
| **Historical practical relearning** | `learning/README.md`, `OPERATING_GUIDE.md`, Learning-Only skill and relevant tests/source | **No new spec.** Begin one 60–90-minute source-to-report retrieval/changed-case session, then use existing study materials for actual gaps. | Confirm assistance level, current case revision, source/test trace and delayed transfer; only publish one new grounded note if it has a distinct need. |
| **Hiring/career contribution evidence** | Public README + selected code/tests/case records | **Curated technical narrative**: what runs, what it proves, what AI produced, what the learner actually diagnosed, and limitations. | Requires at least one personally performed/verified exercise before stronger ownership claims. |
| **Cross-project coordination** | **This independent research ledger** plus respective project live owners | **No new root `AGENTS.md`, meta-spec or duplicated tracker.** Use a short weekly comparison and 4-week review; update this record only for material cross-project strategy changes. | A recurring failure in coordination—not hypothetical completeness—would justify a separate working protocol. |

### D. Recommended decision sequence for the next collaboration

**Step 1 — Confirm live priority and a single near-term outcome per direction.** Do not reactivate completed Build work. For AegisLab, the near-term **human** gate is an actual changed-case/diagnosis exercise, while the implementation track can advance to genuinely evaluated local AI as allowed by its Charter. For UpgradePilot, choose whether the next selected limited human block prioritizes **public portfolio accuracy/front door** or **independent product usefulness evaluation**; both remain valid, but not simultaneously as expanding campaigns.

**Step 2 — Diagnose the knowledge recovery baseline.** Do one representative UpgradePilot CLI→evidence→report/test recall and changed-case exercise before prescribing a comprehensive historical curriculum. Select subsequent topics based on actual errors, not the number of historical learning files.

**Step 3 — Validate the public evidence boundary.** Before preparing a recruiter-focused artifact, review whether the chosen saved example, references, private paths, archive contents, third-party rights and AI attribution are safe and accurate. The prior heuristic scan was limited and is not security clearance.

**Step 4 — Specify only the chosen deliverable.** For each actual workstream, write a compact task brief/plan with: owner, exact goal, current evidence horizon, allowed files/targets, non-goals, expected result, verification, learner participation, stop line and reporting. **If** an enduring cross-session semantic behavior is uncovered, promote precisely that requirement to the existing specification/protocol owner—not to another generic plan.

**Step 5 — Reconcile/measure and avoid drift.** Each meaningful AI delivery reports changed files, observed test/proof, what remains unestablished, the next learner-owned check, and the current source revision. Review time budget and whether instructions actually improved the process before retaining them.

### E. What this decision does **not** approve

No new product feature, cross-repository synchronized governance, agent autonomy, historical deletion, Git-history rewrite, license grant, release, public metadata change, new curriculum, expanded 30-hour budget, or unreviewed assistant instructions are authorized by this record. The existing AegisLab implementation authorization remains independent and governed by its accepted v2 documents. This update records agreed goals and the method for choosing **future practical artifacts**, not the artifacts themselves.


## 9. AegisLab readiness audit and immediate workstream assignments — November 22, 2026

**Purpose:** The owner agreed to operationalize the differentiated workstreams and requested an actual AegisLab independent readiness check before more implementation instructions. This is an **inspection and practical responsibility selection**, not source mutation or a new overriding charter.

### AegisLab code and repo status independently observed

- **GitHub/WSL state at check:** `motafegh/AegisLab main@feed0b428f94e2e3cf936de89b455ac90537ff1e`. WSL `/home/motafeq/projects/AegisLab` HEAD and `origin/main` both matched, worktree clean. No AegisLab files edited by this supervisory review.
- **Normative adoption:** `docs/plans/AegisLab — Core Charter v2.0.md` is accepted. `docs/plans/AegisLab — Capability Execution Map v2.md`, `AGENTS.md`, `PROJECT_STATE.md`, learning state and README point to new A→G capabilities; old M0–M17/M5 remains preserved history.
- **Reviewed implemented source:** `src/aegislab/ssh_incident.py`, `src/aegislab/__main__.py`, `tests/test_ssh_incident.py`, `examples/fixtures/` and active handoff/learning docs. Current Stage B is stdlib-only, input-bounded local JSONL; exact source/record/event mapping, typed quarantine and v1 repeated-failure rule; source and time labels are declarations, not attested real telemetry. The parser is intentionally narrow. No Stage C AI inference pipeline is implemented.
- **Independent non-mutating WSL verification, current HEAD:** ran `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v` (via equivalent subprocess/environment): **15 tests passed, exit 0**. Ran both README `python3 -B -m aegislab analyze` synthetic CLI examples: positive: accepted **4** events, finding supported by **3** failed-publickey records; normal: accepted **2** events, `no_finding_observed` with explicit no-safety conclusion. JSON report parsed, schema `aegislab.ssh-incident-report.v1`, four unique event IDs.
- **Additional independently constructed negative/changed scenario:** an **external temporary-file**, not committed or shown as learner-owned work, combined out-of-order UTC observations, differing usernames and an unsupported log message. The importer returned `finding_present_with_gaps`, 4 accepted events, 1 quarantined line, 1 finding tied to exactly 3 `alice` event IDs; all finding IDs were present in accepted events. This is narrow new assurance beyond fixture demos, not broad fuzz/property/security testing.
- **Transport recheck:** `curl -fsS --noproxy 127.0.0.1 --max-time 3 -o /dev/null -w '%{http_code}' http://127.0.0.1:18080/v1/models` returned **HTTP 200**, exit 0. Only catalog reachability, **not** model load, inference quality, structured output, semantic entailment or latency/cost.
- **Current limitations:** No retained raw July sensor logs. Stage B uses **synthetic evidence**, no real live laboratory trace; no Docker/VM, privileged host change, autonomous agent, fresh telemetry or production claims. User's Stage B personally performed prediction/changed-case diagnosis is **still open**. These are explicit scope limitations and learner gates, not misrepresented as defects.
- **Conclusion:** **GREEN** for Stage B local CLI/learner exercise, **CONDITIONAL** for bounded Stage C AI implementation once existing Charter/Stage B semantics are respected, **NOT AUTHORIZED/NOT PROVEN** for any live privileged Stage D or model-led tool action. Existing AegisLab instructions are adequate at this horizon; **no new `AGENTS.md` or specification needed now**.

### UpgradePilot reconciliation after last strategy record

At this check UpgradePilot `main@91a824cb4ee35aee92929b288dc0c67c01be6bda` reports the qualified deterministic CI first view **already implemented** in renderer 6, not merely selected for Build. Its Build record cites 39 focused tests, 7 experiment presentation tests, MapProxy frozen CLI replay, saved-facts fidelity, negative controls and **1,192 installed product tests passing**. The supervisor inspected the exact record and main-state handoff, **not** a second full installed-product suite. Human benefit and comparative time savings remain unestablished. UpgradePilot WSL `main` matched published HEAD; two pre-existing unrelated untracked audit/working-memory files were preserved and not touched.

### Concrete role assignment and next two gates

| Workstream | AI job and boundary | Human learner/owner role | Next objectively checkable deliverable |
| --- | --- | --- | --- |
| **AegisLab build (primary, ~20 h human time budget)** | Continue with the existing authorized project assistant under v2. **Stage C** must compare optional bounded local model output to deterministic baseline on the **same source evidence**, with provenance, semantic validity (not just ID shape), error and no-model fallback; no agent tools or privileged lab actions yet. Do not silently claim Stage B learner mastery. | Personally perform Stage B synthetic changed-case prediction, run and diagnose it, then inspect Stage C results at appropriate milestones. | A logged Stage B **learner** check and independently observable Stage C AI OFF/ON controlled comparison. |
| **UpgradePilot product (~6 h total incl practice)** | Existing main assistant operates only bounded product maintenance and evidence-based usefulness evaluation. No repeat of completed renderer-6 Build or speculative expansion. | Review a compact verified milestone receipt; allocate appropriate part of this six-hour envelope to code/test knowledge recovery. | Explicit choice and feasible, honest next maintainer utility assessment; preserve unresolved independent validation. |
| **UpgradePilot public portfolio (inside same six-hour limit)** | A bounded portfolio/editorial assistant may prepare a public-content/third-party-rights checklist and improved hiring path using existing README, example and evidence, without deleting historical data or granting licenses unilaterally. | Approve release/license/public material; personally defend selected design stories. | One safe, accurate short README opening and an offline-first 3–5-minute case walkthrough after the rights/public-safety gate. **Recommended next visible UpgradePilot priority** after renderer delivery, while usefulness remains an evaluation gate. |
| **Historical learning (inside 4 h career+transfer and bounded project study time)** | Learning mentor retrieves minimal source/contract/test context and asks for prediction, hands-on changed case and teach-back. Do not give full diagnosis before learner attempt unless requested or blocked. | Supply own first reasoning; execute safe check, diagnose and revisit. | First 60–90 minute UpgradePilot CLI→evidence→report/test lesson; one demonstrated changed case and assistance-level note. |
| **Independent supervision** | Read-only evidence-first reviewer on both repositories; inspect current HEAD, precise tests, security and proof boundaries; do not claim blind independence after source/case exposure. | Decide scope, prioritize meaningful discrepancies and limit review workload. | Weekly concise two-repo progress and learning checkpoints, monthly 20/6/4 review. |
| **Hiring/career** | Technical editorial assistant only; source-linked achievements with explicit AI assistance and limits. | Test ability to explain one practical diagnostic and select actual applications. | One truthful technical portfolio story with verified example and personally observed skill evidence, not a generic generated resume claim. |

**Important concurrency rule:** AegisLab's builder may continue bounded Stage C software while the owner separately performs Stage B learning, **provided neither labels the Stage B learner gate passed prematurely** and every Stage C claim is separately verified. Stage D external/privileged actions or E agent tool effects require their owning safety/authorization gates.

### Near-term sequencing; no extra governance work yet

1. **Now:** finish AegisLab Stage B learner-owned changed-case exercise using current CLI. The README already supplies the bounded exercise; there is **no need** to create a second curriculum. The supervisor's separate synthetic scenario is not a substitute for the learner's own attempt.
2. **AegisLab builder:** continue bounded Stage C design/implementation consistent with v2. First establish live model availability and whether a complete inference actually succeeds, with direct loopback proxy bypass, without presuming `/v1/models` proves readiness. Require AI OFF parity, strict structured evidence interpretation, adversarial/error controls and a usable fallback before declaring Stage C done.
3. **UpgradePilot:** choose a **small public portfolio P0 (rights/privacy/accuracy) → P1 (brief README/demo)** task as the next reader-visible increment after renderer 6; do not bury this under another multi-month audit. Independent maintainer usefulness is still a distinct valid later comparison; it should be addressed with eligible participants or honestly kept unestablished.
4. **Knowledge recovery:** schedule the first concrete UpgradePilot end-to-end source/test explanation within protected transfer time; use resulting actual gaps to determine the remaining four-week sequence.
5. **Instruction/spec admission:** retain current guides. If agent confusion, repeated omission of learner proof, false AI/evidence claims, or portfolio editing errors appear in **real repeated work**, amend the *specific existing owner*, not a new parallel cross-project manual. A one-task briefing can be drafted for the next session without a permanent document.

**No project-main mutations / promises:** This audit was read-only for both live repos; no new source/test/spec/README, release, license, portfolio assets, automation or privileged operation was performed. This research record is revision-specific and must be rechecked before later task execution.
