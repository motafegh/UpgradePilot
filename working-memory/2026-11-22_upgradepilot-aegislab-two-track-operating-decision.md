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
