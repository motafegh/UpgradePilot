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
