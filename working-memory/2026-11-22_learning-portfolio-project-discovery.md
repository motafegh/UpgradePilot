# Learning portfolio — project discovery and transition evaluation

- **Date:** 2026-11-22
- **Status:** ACTIVE — evidence gathering; no replacement project or time allocation approved
- **Scope:** independent research branch `research/maintainer-utility-independent-supervision-2026-11-22`
- **Previous discussion:** [Independent maintainer utility and learning strategy](2026-11-22_1911_independent-maintainer-utility-supervision.md#12-career-and-learning-portfolio-inflection--2026-11-22)
- **Current main-state owner:** [`MEMORY.md`](../MEMORY.md) on published `main`, not this record
- **Procedure:** read-only GitHub and WSL inventory, analysis and learner-owned discussion; no local repository mutations
- **Provenance:** UP-SKILL:upgradepilot-working-memory; UP-SKILL:upgradepilot-workstream-supervision

## 1. Decision that motivates the discovery

The primary learning goal was repeated *exposure, understanding, hands-on diagnosis and transfer* across new technical and engineering contexts, while creating a credible AI/security-automation-oriented portfolio. After approximately four to five months, the learner reports that some desired competencies were encountered but many were not; repeated UpgradePilot evidence, CI and report refinements may have declining incremental learning breadth. UpgradePilot is not to be abandoned.

**Provisional hypothesis, not a decision:** Keep UpgradePilot as a maintained flagship engineering/product-evaluation asset, and consider another *distinct* project as the primary vehicle for learning uncovered operational/security/deployment capabilities. Evaluate whether **resuming an existing unfinished project** is better than starting another from scratch. Reject the false dichotomy of permanently abandoning UpgradePilot versus continuing it as the exclusive main focus.

## 2. What is actually known and still unknown

**Supported:** UpgradePilot has substantial architecture, Python testing, GitHub/PyPI evidence acquisition, security-aware transport, CI interpretation, deterministic evaluation and source/provenance work. The project's actual independent maintainer benefit remains unproven and is under separate main-workstream evaluation. Other prior projects may already contain the complementary concepts; their existence, state, reason for pause and reusability must be inspected rather than guessed.

**Not yet established:** learner's independent ownership of each technical concept; each prior project's exact implementation/operability; why it was paused; whether the available work is salvageable; whether the role-relevant gaps can be filled more efficiently inside UpgradePilot; measurable local job market demand for a specific tool; and a final project ranking.

Do not equate repository existence, framework names, commits, generated code, successful tests, or accumulated time with acquired transferable skill. An existing repo's apparent technical breadth is only an exposure opportunity until independently exercised and explained.

## 3. Evaluation lenses — compare options on evidence, not enthusiasm

| Lens | Inspect or test | Avoid |
| --- | --- | --- |
| New learning breadth | Which concrete operational/security concepts are absent or underused in UpgradePilot but unavoidable in the candidate? | Novel framework accumulation with no clear task |
| Learning depth and ownership | Can the learner trace, run, change, diagnose, and explain a vertical slice with increasing independence? | More autonomous AI-generated code without human transfer |
| Complementary portfolio signal | Does the repo demonstrate a different realistic problem with clear implementation, measurable tests and reproducible demonstration? | Two large repos that show the same competencies |
| Cost to resume | Existing runnable baseline, quality, dead dependencies, environment, scope, repair time and architectural debt | Sunk-cost reasoning or rewarding only old code volume |
| Operational realism and safety | Benign isolated telemetry, detection, environment failure, observability and human-approved response where relevant | Unrealistic or unsafe autonomous offensive actions |
| Feasible finish | Can one small but coherent end-to-end slice be demonstrated in roughly six to eight weeks, with explicit stop/extension gates? | Another indefinite architecture expansion |
| Evidence of adoption/relevance | Concrete maintainer/analyst task, baseline, independent benefit or realistic operator demonstration | Unsupported market/popularity/production-readiness claims |

**Candidate comparison questions:** What does it do now? What was originally intended? What truly works? What would be needed for a first useful end-to-end demonstration? What new skills would performing those tasks yield? Why did it pause (known statement vs inferred from artifacts)? Should it be **resume**, **repurpose**, **mine for reusable ideas**, **archive**, or **insufficient evidence**?

## 4. Initial recommended portfolio shape (provisional)

- **UpgradePilot:** keep it alive, with evidence-backed maintainer usefulness, readable demonstration, focused defect fixes and concise architecture/portfolio documentation; avoid open-ended duplicate engineering rounds.
- **Potential primary learning project:** a genuine different operating environment, e.g. an isolated defensive security automation lab involving Linux, networking, event ingestion, detection, response approval and deploy/monitor/recover tasks. This is a *hypothesis*, not yet authorization to start such a project; an existing repo might be a superior fit.
- **Individual mastery:** short concrete exercises on tracing, running, modifying, testing and diagnosing; AI-first development can continue, with the learner making and verifying real decisions.
- **Illustrative only:** approximately 20/6/4 hours per 30-hour week (new learning project / UpgradePilot / mastery plus career preparation); no schedule committed.
- **Product-career separation:** UpgradePilot's real user value, personal technical mastery, and CV evidence are three related but distinct outcomes. A scientifically sound negative product evaluation does not erase engineering learning, but engineering excellence alone does not prove product adoption.

## 5. Discovery protocol

1. Preserve this decision context **before** inspecting prior repositories.
2. Read-only inventory authenticated GitHub profile/repositories and WSL `/home/motafeq/projects`; do not dump secret files, environment credentials or unrelated private contents into this public research branch.
3. Identify distinct projects and whether local checkouts match remote repos, their last meaningful work, runnable entrypoints, recorded tests and architecture.
4. Deep-read the most relevant security/AI/ops candidates and reconstruct their actual purpose/progress/reasons for pause only where documented. Treat missing history as unknown, not failure.
5. Compare candidates and challenges to the currently proposed new-project architecture. Prefer **reuse/resume/repurpose** where it gives more genuine learning per hour than a fresh scaffold.
6. Present evidence, trade-offs, and a proposed ranking for user discussion. **Do not finalize portfolio direction or notify/mutate main without explicit decision.**

## 6. Evidence and candidate inventory

**PENDING discovery.** Append vetted project-level facts, citations, comparative observations, uncertainties and recommendation changes here after inspection. For local/private repositories, use public-safe categorical descriptions and generic paths unless the user separately decides they belong in a public record.

## 7. Decision gate

**Not reached.** Need comparable artifacts for existing candidates, user context about why they stopped, a practical ownership-gap assessment, and a bounded first demonstration for the best alternative. A prior project may be the right answer; a new repo is not presumed better.


## 8. First inventory — 2026-11-22 (read-only, provisional)

The authenticated GitHub account `motafegh` lists **24 owned repositories**. The WSL `~/projects` folder includes multiple Git repositories, independent learning folders, and numerous Sentinel worktrees. **A separate worktree is not automatically a distinct portfolio project.** No local project was checked out, edited, built, installed or started. The research-branch-only record contains no raw packet captures, credentials, model artifacts, secrets or local private source excerpts.

### Strongest directly relevant candidates

| Candidate | Inspectable evidence | Actual status and open question | Initial fit |
| --- | --- | --- | --- |
| [AegisLab](https://github.com/motafegh/AegisLab) | 2026-07-18 `PROJECT_STATE.md`, Core Charter, M5 Docker playbook, learning state and worklog. Guided network-namespace SSH authentication success/failure, trust, sockets, process and log correlation; deliberate deferral of remaining formal M4 work as repetitive. | M5 Docker Phase 0/adapter **planned but not yet implemented**; downstream event collector, detection, incident, replay and environment parity remain unbuilt. Repository tracked files are primarily documentation/runbooks. Independent reproduction not demonstrated. Clean local worktree at inventory. | **Highest candidate for a resumed operational-security capstone**, with scope-control risk. |
| [ai-security-engineering-labs](https://github.com/motafegh/ai-security-engineering-labs) | Flexible 2026-07 learning-by-doing ladder; local modified session tracker records the Handshake and Who's Listening experiments with actual source/evidence; local Traffic Inspector has real packet-capture artifacts and a detailed final review. | Public repo tracker is older than the local working copy; local `PROJECT_STATUS.md` still calls Traffic Inspector active, even though its local final review and captures exist. Much practical local work is **uncommitted**, including the small API source. Python security automation/web/API portions remain planned. | **Highest candidate for rapid, varied hands-on foundational micro-labs**, but requires honest status/packaging/ownership reconciliation before a portfolio claim. |
| [CyberSecEngineer](https://github.com/motafegh/CyberSecEngineer) | 2026-07 secure-lab/foundations/distributed/AI-security curriculum, capstone specs, lab evidence, small shell system-auditor; Phase 1 reconciliation explicitly restarted from archived earlier work. | 167 tracked Markdown files, zero tracked Python files, some script/Compose material and local hands-on observations; many uncommitted edits, archive/restarters and ambitious principal-architect roadmap. The Phase-0 capstone README still says not started and has incomplete checklist; individual lab progress may exist elsewhere. | **Useful learning reference and source of selected exercises**, but poor candidate for another large top-level planning vehicle without severe scope reduction. |
| [chainguardian-ai](https://github.com/motafegh/chainguardian-ai) | Old smart-contract security/ML/LLM/chain provenance project; 235 tracked Python files, 21 tracked files under test paths, Docker and application infrastructure; last local commit 2026-01-01. Historical verification report and README advertise strong accuracy/production outcomes. | The advertised metrics and full-stack operability were **not independently rerun or audited here**; scope overlaps Sentinel and may create a high-cost modernization/dependency burden. An untracked `MASTERY_EXECUTION_PLAN.md` explicitly recognizes the need to convert AI-assisted build into personally owned understanding. | Good for *targeted system comprehension/API/MLOps salvage*; not first choice as the new main security-operations learning project. |

### Other relevant projects

- [SENTINEL](https://github.com/motafegh/sentinel-) is already a large evidence/ML/agent/smart-contract research portfolio, not a novel operational-security foundation. Its README explicitly distinguishes earlier learner work from later substantially AI-led R4 continuation.
- [PersianLLM-API](https://github.com/motafegh/PersianLLM-API) provides an existing Python FastAPI/RAG service, container files and a few tests; last local commit 2025-12-08. It could be used for a **small service hardening/deployment exercise**, but the broad RAG/cloud roadmap is not the same as a security-telemetry product. Local source edits are present.
- [JobHunter](https://github.com/motafegh/jobhunter) is a recently active AI-first career intelligence product; substantial existing evidence and application engineering, but similar research/evidence orchestration pressures to UpgradePilot. Not a preferred source of missing Linux/network/defensive-operations exposure.
- [warden](https://github.com/motafegh/warden) is a June 2026 Foundry/contract-scaffold project; the README remains mostly default framework instructions. `learning_warden` is a study mirror, not independent mature product evidence.
- `cybersecurity_learning` and `j_to_s` are local lesson/curriculum workspaces, not automatically deployable portfolio products. The former's written mission favors open-source/local-first lab work without paid/KYC dependencies. `cyberpractice` looked empty in the bounded directory listing.
- [EdgePilot](https://github.com/motafegh/EdgePilot) is presently charter/architecture/trading-research bootstrap, not a security-detection learning candidate. [Document-Processing-Pipeline](https://github.com/motafegh/Document-Processing-Pipeline) exposes a placeholder README in the inspected remote; `hushyar-ai-Persian-RAG` is empty on GitHub but has local source. The remaining account repos include small Git/GitHub Actions/Solidity learning exercises and should not be interpreted as 24 completed products.

### Previously undocumented learning and stoppage context discovered

- **AegisLab:** the owner explicitly advanced from remaining formal M4 namespace tests toward Docker because repetition had lower current learning value; a July 18 worklog also records frustration when the route and learning depth were not visible enough. This explains a *phase transition*, not necessarily the **ultimate reason the entire project paused**.
- **CyberSecEngineer:** a July 7 local reconciliation intentionally archived prior Phase-1 work for a fresh start; this is a clear restart event, not proof that earlier learning never occurred or an explanation for later abandonment.
- **ai-security-engineering-labs:** four recorded sessions on July 12 completed Handshake and Who's Listening; uncommitted Traffic Inspector evidence exists beyond the still-active tracker entry. The reason this project later paused is not established from those artifacts.
- **ChainGuardian:** the local mastery plan says the AI-assisted system needed deeper independent comprehension; this is a documented ownership pressure, not proof of a specific reason for pausing.
- Other project pause reasons must be supplied by the learner or found in exact dated records; commit inactivity alone cannot establish motivation.

### Provisional comparative judgement

**Two credible paths now exist:**
1. **Resume AegisLab** as the one deeper security-detection capstone, preserving its existing observable SSH/network baseline and using a small genuine Docker/telemetry/detection milestone to test renewed learning yield. Its original three-environment contract and sequential gates may be too heavy for a short learning/portfolio cycle, so scope changes would require an explicit owner decision, not silent plan bypass.
2. **Resume ai-security-engineering-labs** as a short-lab execution ladder to cover missing network, web/API security, defensive automation and CI competencies quickly. Prioritize confirming/reconciling locally completed traffic exercises, preserve private captures, and advance only to a bounded next practical lab. Use AegisLab later as a capstone if the foundational exercises surface the need.

Starting an entirely new repository is **not yet warranted** without rejecting these recovery options on concrete grounds. Avoid running both as competing full-time implementations or attempting to combine their governance files automatically.

**Current ranking, not accepted:** AegisLab for cohesive capstone relevance; ai-security-engineering-labs for near-term variety and execution speed; small PersianLLM deployment hardening as a targeted alternate; CyberSecEngineer as a reference; ChainGuardian as optional later salvage. The correct order could reverse depending on *why the learner stopped* and which type of project they will reliably continue.

## 9. Remaining decisive information before switching main learning focus

Need to reconcile at least: the learner's actual reasons for pausing AegisLab, ai-security-engineering-labs, CyberSecEngineer and ChainGuardian; whether an overly structured session style or repetitive steps drove disengagement; which guided concepts can now be reproduced unaided; current local Docker/WSL/packet capture availability if resumption is selected; and how much time can be dedicated to a **single** bounded first deliverable.

**Do not infer that project count equals skill breadth** or that files marked `Complete` equal independent mastery. No candidate has undergone a clean-clone/run acceptance in this read-only review. Local uncommitted changes should be preserved and reviewed before any checkout, pull, branch reset or publication.

## 10. Decision state

**Portfolio transition undecided.** Evidence strongly supports evaluating a **resume/repurpose** route before starting a new repo. Recommend discussing the real stoppage reasons and choosing a concrete 1–2 week recovery/ownership demonstration as the next discriminating check; only then commit to longer weekly allocation or revise AegisLab's existing Core Charter. Continue supervising UpgradePilot `main` separately.


## 11. User clarification and AI-first learning requirements — 2026-11-22

**New user-supplied insight:** The learner is uncertain how to choose or shape a project when AI can perform much of coding, architecture and implementation. The project must plausibly (1) accelerate *personally transferable* technical mastery, (2) improve hiring evidence, (3) sustain interest through **observable progress**, and (4) address an actual useful problem. The learner tentatively recalls pausing AegisLab partly because it **did not include enough AI engineering** and progress was not sufficiently visible. This is **self-reported, uncertain recollection**, not a verified sole or primary cause. Do not erase the documented July experience with repetition, explanation-calibration and scope; the causes could interact.

**Important new factual check (AegisLab governing sources as of July 2026):**
- The accepted [AegisLab Core Charter](https://github.com/motafegh/AegisLab/blob/main/docs/plans/AegisLab%20%E2%80%94%20Core%20Charter%20v1.0.md) expressly excludes ML, LLM investigators/agents, LangGraph/MCP, distributed frameworks, substantial dashboards, autonomous response and cloud deployment from **Core**, deferring these to later charters. It pursues evidence-backed SSH event collection, normalization, detection, incidents, evaluation and replay across **network namespaces, Docker and separate VMs**.
- The [Core Execution Map](https://github.com/motafegh/AegisLab/blob/main/docs/plans/AegisLab%20%E2%80%94%20Core%20Execution%20Map.md) runs M0–M17. The current published stage is **M5 Docker**; the shared evidence pipeline, detection, report, evaluation and resilience are mostly M8–M17, after Docker, VM and three-environment comparison. This sequencing creates a **long value-visibility gap** for someone seeking a working detector or applied AI quickly.
- AegisLab's deferment was a deliberate sound learning/boundary decision for its *original* Core, not proof that security detection or AegisLab is wrong. However, under the new four-part objective, the same sequencing may now be suboptimal. Any new AI-centric outcome would require an **explicit Charter/scope revision** in the AegisLab owning repository after user decision. Our branch does not change it.

**Distinctions to preserve in future discussion:**
1. **AI-assisted engineering:** AI drafts code, analyses, fixes and plans; human defines requirements, controls and proof, then independently explains, tests, diagnoses and can transfer the mechanism. This is a **development method**, not an AI-engineering product skill by itself.
2. **Engineering AI systems:** model/API behavior, retrieval/tool boundaries, structured output, hallucination/semantic evaluation, data quality, latency/cost, fallback, monitoring, prompt/config/version reproducibility and deployment. This is a **technical product responsibility** that should be materially exercised for an AI-engineering career objective.
3. **Security of AI systems:** prompt injection, unsafe tool permissions, evidence laundering, data leakage, evaluation attacks, agent authorization and failure containment. A separate responsibility with strong overlap and a likely demonstrable niche; requires realistic controlled cases and safe target boundaries.
4. **AI applied to security operations:** security telemetry/detection plus bounded AI triage/explanation/next-evidence suggestions. Must preserve deterministic events/evidence, explicit uncertain conclusions, and human control for response.

**Emerging design criterion:** Use a **short time-to-visible-value path**, not 18 successive infrastructure gates before the first meaningful user-facing result. A first demonstration should run an end-to-end task early (e.g. retained SSH logs → deterministic incident → evidence-backed AI triage or explicit refusal), then increase live operational realism. The exact mix remains a hypothesis until compared to other AI-first security options and the learner's intended role. Existing AegisLab can provide network/SSH test fixtures; it need not be retained unchanged or reused solely because code/plans already exist.

**AI-first learning contract to test, not impose as a rigid code-without-AI rule:**
- Human predicts one meaningful input/output/failure condition **before** using AI; AI can design/implement quickly.
- Human can trace the actual code's data flow and evidence/permission boundary, selects acceptance tests, personally runs and interprets a changed or failed case.
- Engineer ownership is sampled through a small **unseen modification or diagnosis** without an AI-provided complete answer; permit documentation and targeted AI guidance after the attempt.
- Every short milestone ends with a demonstrable live behavior, an output artifact, an honest test/proof, and a concise explanation; no ceremony for routine tasks.
- Track not just number of features or LoC but **novel capability demonstrated**, **independent diagnosis/transfer**, **security or AI-specific failure cases handled**, **observable value**, and **time until first end-to-end result**.

**Preliminary direction:** Re-evaluate AegisLab's original Core versus an **explicitly re-chartered AI-security-operations vertical slice** versus a more AI-native **agent/tool security and evaluation** project. Compare genuinely different product tasks and user value, not just technology counts. Avoid copying the UpgradePilot evidence/report architecture or building a generic AI wrapper. This is still strategic analysis, **not authorization to restructure AegisLab, move local files or alter main**.

**Next discriminating discussion:** Which category is intrinsically interesting enough to sustain repeated operation and diagnosis: operating actual Linux/network security events with AI triage, securing AI agent/tool execution, or evaluating hostile prompts and model output? The answer should be checked against a concrete prototype and realistic operator task rather than a preference poll alone.


## 12. Explicit AI-first portfolio options and smallest discriminating trial

**These are options for discussion, not selected execution or an amendment of AegisLab's original Core Charter.**

| Option | AI-engineering depth | Security/system-operations exposure | Fast observable value | Main defect to test |
| --- | --- | --- | --- | --- |
| Resume original AegisLab Core unchanged | Low before post-Core scope; AI is explicitly excluded | Strong Linux, SSH, Docker/VM and telemetry | Slow: environment parity comes before primary detection/report milestones | May reproduce the learner's AI/motivation and slow-progress concerns |
| **Re-charter AegisLab to an AI-assisted security investigation vertical slice** | Moderate/high if LLM grounding, failure handling and evaluation are first-class | Strong if real local telemetry, ingestion, services and diagnosis follow | Possible within 1–2 weeks using retained genuine lab logs and a deterministic baseline | Risk of adding a cosmetic LLM summarizer rather than defensible security decisions; must earn added utility |
| AI agent/tool authorization security evaluator | High for tool interfaces, prompt injection, policy enforcement, adversarial tests and safe sandbox behavior | Medium unless coupled to real Linux/network service operations | Fast if tested with controlled read-only simulated tools | May repeat UpgradePilot's trust/evidence contract work with little actual infrastructure novelty |
| Continue short security micro-labs | Low on explicit AI engineering unless later added | Strong foundation breadth and learner activity | Fast per lab | Disconnected projects may fail to demonstrate one integrated AI security product |

**Four simultaneous success obligations, not one combined arbitrary score:**
1. **Transferable learner skill:** personally run, explain, change and diagnose at least one behavior introduced by the milestone; distinguish AI-authored changes from independent demonstration.
2. **Hiring evidence:** concise reproducible architecture, threat model, clean run, meaningful adversarial/failure tests, measured model-vs-baseline behavior and honest ownership disclosure.
3. **Intrinsic engagement/progress:** demonstrable end-to-end vertical slice and a visible new user-visible result every short cycle; no multi-week preparatory infrastructure as a default.
4. **Actual usefulness hypothesis:** name a plausible operator task and compare with manual source review and a simple deterministic baseline; utility is unproven until independent users/cases support it.

**Proposed narrow, reversible exploration (not authorized Build):** use retained, synthetic-or-authorized-lab SSH authentication event samples as input; establish deterministic event/threshold truth and source identities; ask an optional local LLM to formulate a **bounded, cited triage explanation** including material uncertainty; verify valid/invalid structured response, fabricated event references, a malicious instruction embedded in lower-trust log text, missing events and provider failure. Never let the model authorize response/blocking, execute tools or transform its own output into ground truth. Finish with a simple CLI or report that shows one operator what happened and what still needs verification. Compare raw logs, deterministic baseline, and AI-assisted view on the same cases. An end-to-end demo early would test interest and actual AI engineering before committing to Docker/VM expansion.

**Re-entry / rejection gates:** If a small offline triage slice proves trivial with a deterministic template, does not require meaningful AI capabilities, or reproduces uncomfortable evidence/report repetition without new operations, do not expand it. Consider AI agent/tool-authorization evaluation or a different operational-security problem instead. If the slice is useful and the learner shows ownership, consider formally modifying AegisLab's charter to make one early full loop prior to three-environment parity and admit AI engineering with explicit evaluator and safety requirements.

**Current external reference anchors:** [NIST NICE components 2026](https://www.nist.gov/news-events/news/2026/04/nice-releases-nice-framework-components-v220) ties work to demonstrable tasks/knowledge/skills, [OWASP LLM Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/?lang=us) supplies concrete human/tool authority risks, and [Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/ai) shows high AI uptake alongside developer distrust of AI accuracy. These references motivate **measurement and validation**, not a promise of employment, product adoption, or that AI can independently own every production responsibility.

**Decision state:** open. Discuss interest, employment target, and first practical experiment before modifying AegisLab or assigning weekly hours.


## 13. Learner agreement and selected next discriminating step — 2026-11-22

**Confirmed by user in current session:** The user strongly agrees with the preceding AI-first learning framework and is interested in both (a) operating realistic defensive security environments and using AI to investigate their events and (b) building and securing AI agents. They want a concrete, practical next-step decision after documenting the discussion. This confirms **interest in both subject areas**, not blanket authorization to modify AegisLab, declare the project selected, run infrastructure, or merge into UpgradePilot main. Preserve this nuance.

**Refined provisional recommendation:** Design one coherent **AI security investigation lab** that makes operational security the source of real problems and bounded AI-agent behavior a genuinely testable subsystem. Prefer reusing AegisLab's existing authorized SSH/network experiment and source artifacts where suitable, but its charter **explicitly prohibits AI in the original Core**; any permanent change needs a later explicit AegisLab owner decision and updated charter/execution map. This is a *proposed product learning direction*, not evidence the product helps a real analyst.

### First practical decision experiment (proposed; no Build authorized)

**Question:** Can a small offline local prototype (1–2 focused weeks, subject to actual progress) prove that this project teaches both operational security and AI/security engineering, produces an inspectable end-to-end operator result, and has a testable usefulness hypothesis **without** another preparatory multi-environment program?

**Operator task:** Given a bounded set of retained *authorized-lab* SSH authentication records, explain whether the evidence shows one observed authentication sequence of interest, distinguish the action/source from the sensor's observation, and state what cannot be concluded or what specific next observation matters.

**Minimal experimental path:**
1. **Inspect and choose one permitted preexisting input set.** Prefer AegisLab's recorded SSH success, valid unauthorized-key failure and related host/socket logs with source/time/context. If raw retained material lacks needed fields, disclose that; use explicitly synthetic controlled complements without mislabeling them as observed lab data. No live unsafe scanning or attacking.
2. **Make a tiny runnable baseline quickly.** Parse bounded events (raw/normalized identities and timestamps), implement one deterministic rule such as count of failed authentications within a stated window, render a concise incident/uncertainty result, and test one positive/negative/threshold case. No DB/framework/cloud/VM pipeline before the first demo.
3. **Add one optional local model responsibility.** Local LLM receives typed facts and selected quoted snippets; proposes a structured, evidence-linked triage explanation or justified refusal. The app verifies referential identities, allowed fields, and output status, and keeps rule truth and action authority outside the model. Compare with the same deterministic result, not a richer input packet.
4. **Exercise meaningful AI security boundaries.** Attack the explanation with an adversarial instruction embedded in lower-trust log text; inject missing, false or contradictory event references; force model unavailability/invalid output. Model never executes shell commands or authorizes blocking. If agent/tool-security competence is desired in the trial, add *one controlled read-only tool*, e.g. fetch event by approved ID through an allowlisted validation boundary, then test unauthorized/invalid requests. Do not require a general planner or tool framework.
5. **Show and explain a complete operator result.** One CLI invocation or tiny local view outputs the finding, cited evidence IDs, uncertainty, and observed safety/failure behavior. Show a before/after or model-vs-template comparison with a known limitation; have the learner diagnose one changed-case failure before a completed explanation is supplied.
6. **Decide, do not automatically expand.** Stop if the AI adds no defensible informational value, the prototype is mainly repeated UpgradePilot-style claim normalization, or the learner is not encountering new operational/system concepts. Redirect toward live telemetry and deployment, or a separate agent-tool security lab, depending on the actual learning/engagement evidence.

**First-session deliverable if selected:** a one-page bounded experiment brief describing the operator, one source record set, exact raw-to-output flow, two expected good outcomes, two adversarial/failure cases, known missing evidence, proof of learner ownership, and the exact code location/branch. Then implement only the first runnable baseline. The user-facing demonstration is a concrete acceptance gate, not an assumed consequence of a README.

**Example success evidence (not percentage target):**
- An observable end-to-end baseline with correct cited event/source scope, plus a negative and missing-evidence control.
- AI-assisted output demonstrably differs in a justified way *or* is judged unnecessary with measured evidence and explicit rejection.
- Prompt-injection and invalid/missing evidence never become trusted instructions or unsupported incident facts, including through any single admitted read-only tool.
- The learner can personally trace and diagnose a modified incident or broken boundary with limited assistance; record exactly which actions were personally completed.
- One concise reproducer and comparison fit a credible portfolio narrative while explicitly stating prototype—not production SOC, independent analyst value, or complete AegisLab Core.

**Separately deferred:** permanent AegisLab charter/roadmap changes, public project renaming or splitting, large source imports, Docker/VM three-environment parity, live agentic response actions, external attacks, public cloud, evaluation-population claims, new LLM frameworks, full data platform, autonomous remediation, or recruiting independent users.

### Coordination and current source state

Our independent research and branch-only working memory remain the proper home for this recommendation until the user chooses execution. `UpgradePilot/main` advanced to `90601aa156913ed12afe683f27e15fe64990a185` on 2026-11-22, `Qualify a bounded CI report first view`; this is separate product presentation work and **was not modified** from the research branch. No action is required of that workstream merely because a new career direction is under discussion.

**Next conversational decision:** Select either (i) a bounded prototype conducted without changing AegisLab's accepted Core (with clear isolation and authorized file location), or (ii) a formal AegisLab re-charter **before** a new AI-enabled implementation. Recommend a narrow research prototype first to avoid early architectural lock-in; its eventual incorporation into AegisLab requires an explicit approval and owner change.


## 14. Decision to plan AegisLab evolution rather than run the short experiment — 2026-11-22

**New explicit user direction:** Having considered previous engineering efforts and learning preferences, the learner wants a proper, broader review and evolution of AegisLab's direction **before** executing an isolated short experiment. The requested sequence is: identify what must change and why, produce a real project evolution plan grounded in previous discussions, then use that accepted plan to make deliberate AegisLab adjustments. The user is open to combining real security-system operations and AI-powered investigation with securing agent/tool execution. This supersedes the *short experiment first* recommendation as the selected planning route; earlier experimental-design thoughts remain relevant as implementation slices, not as the project-selection prerequisite.

**AegisLab reinspection:**
- Read the AegisLab v1 Project Definition and its identity, learning/technology, experimental model, capability/module, scenario, safety and success/evolution parts, as well as AGENTS, Core Charter, Initial Journey Plan, Core Execution Map, active July M5 handoff, AI Collaboration Protocol and worklog rules.
- Important correction to avoid repeating an oversimplified explanation: **the accepted long-term AegisLab Project Definition already explicitly includes security ML, AI-assisted investigation, secure agent tools and agent-adversarial scenarios**. It is the **original Core Charter and Core execution order** that postpone AI and delay the full observable detection-to-investigation path. Rewriting the whole identity is unnecessary; a new Core and execution route are material.
- The prior namespace SSH practical baseline was guided; deferred formal M4 remains deferred, Docker M5 pending. AegisLab's local WSL checkout at `/home/motafeq/projects/AegisLab` was verified clean and aligned with GitHub `b5f0234840338e2af012c46cfb4ead1ebcec0cad` immediately before the remote proposal write.
- Preserve the existing AegisLab core invariants (truth-vs-observation, least authority, explicit uncertainty, public-safe lab and evaluation) while reordering delivery to yield early end-to-end results and material AI security work.

**Deliverable created directly in AegisLab repo under its proposal, not normative, owner:**
[AegisLab — AI-First Security Operations Evolution Plan](https://github.com/motafegh/AegisLab/blob/main/docs/proposals/2026-11-22-ai-first-aegislab-evolution-plan.md), published with `939225acc7690155d9634dca20efa6a2ba4e67b8` on November 22.

**Key recommendations in that plan:**
1. Keep AegisLab as the single connected cyber range + defensive investigation platform, not a generic LLM wrapper, not a SOC product claim, and not a second UpgradePilot.
2. Re-charter Core to permit an early deterministic incident and bounded local AI investigation; deliver through capability-led stages, with live controlled SSH operations, agent/tool authorization tests, operational deployment/recovery and a contrasting second scenario following in visible increments.
3. Preserve independent scenario truth, source/event provenance, semantic factual evaluation, AI OFF fallback, and read-only human-controlled agent tools. Deny unauthorized actions at a deterministic policy boundary, not through prompt wording.
4. Treat learner-owned reasoning, changed-case diagnosis, new domain exposure and reproducible demonstrations as release evidence alongside software tests; permit AI code implementation without claiming independent authorship of every component.
5. Compare operator usefulness against raw-log/manual review and a simple deterministic report, and avoid unsupported analyst adoption/production claims.
6. Remove compulsory three-environment parity as a **prerequisite** to completing the first investigator workflow; retain VM and cross-environment comparison as later intentional skills, not secretly discard them.
7. Keep costly infrastructure, high-autonomy agents, malware handling, distributed systems, cloud, substantial UI and heavyweight model pipelines out until a particular responsibility actually warrants them.

**Change-control boundary and next action:** AegisLab's currently accepted Core Charter v1, initial journey, execution map, AGENTS, PROJECT_STATE and code have **not been adjusted** by this planning step. The proposal itself explicitly lays out the later reconciliation order: approve/revise thesis → new accepted Core Charter v2 → revised execution map and entrypoints with stale M5 references time-scoped → implementation stages with actual tests and learner-ownership evidence. The user's instruction is to plan **first**, so a review of the proposal's strategic tradeoffs should precede promotion; no silent policy override. The separate UpgradePilot main workstream remains untouched and its live position belongs to `MEMORY.md`.
