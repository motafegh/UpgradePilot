# AI-only maintainer-review evaluation — feasibility and design checkpoint

Date: 2026-11-11
Operation: bounded Planning/Design + Learning-by-Doing, not experimental execution
Status: design checkpoint closed after priority reassessment; both proposed AI-reviewer experiments **DEFERRED**; no reviewer execution
Primary reason for adaptation: Ali confirms no independent human reviewers are currently available; separate AI-assistant review sessions are the feasible participant route. This is a practical constraint, **not** evidence that any AI result establishes human maintainer usefulness.

Owner relationships: [current project memory](../MEMORY.md), [maintainer report usefulness plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation), [existing first-view packet](evidence/2026-11-08-maintainer-first-view-review/OPERATOR_PROTOCOL.md), [revision 2 task](evidence/2026-11-08-maintainer-first-view-review/revision-2/REVIEWER_TASK.md), [revision 3 addendum](evidence/2026-11-08-maintainer-first-view-review/revision-3/OPERATOR_PROTOCOL.md), [GitHub AI remote rehearsal](evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/README.md), [AV-Tracer exact same-evidence development comparison](2026-11-11_av-tracer-same-evidence-first-view-comparison_lbd-cycle.md).

UP-SKILL:upgradepilot-planning-design. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## A0/A1 — current state and task orientation

- Existing actual renderer improvement `55bb607e` passed 1,100 product tests. Actual same saved Workspace before/after comparison on AV-Tracer established exactly one additional truthful first-view line, `Rejected keyword: app`; no runtime causal attribution or human time savings.
- The report usefulness plan defines independent **human maintainer** outcomes as a separate gate and permits assistant review as development analysis. Lack of human participants means that human-usefulness gate is **unmet**, not failed. Do not relax/relabel it to pass.
- The November 8 report-first-view work already defines three contrasting tasks, five reviewer questions, candidate report/source identities, slot ordering, rubrics, rev2/rev3 corrections and technical parity requirements. It remains valuable development material, not an executed valid human study.
- The GitHub-connected AI rehearsal exposes both conditions and grading material through broad repository access and has **no original-text source attachments**. The HTTPX packet uses a GitHub-published summary rather than the byte-exact frozen revision 3 view. These are serious limitations for claims of strict blindness, source parity and ordinary-review equivalence. A prompt to avoid opening other files is a procedural instruction, **not** an enforced isolation mechanism.
- No new model invocation, participant answer, protected holdout, reviewer eligibility assessment, isolation proof, or scored evaluation is represented by this checkpoint. Ali's prior reviewer-2 rehearsal in a GitHub-connected session should be treated as **exposed development material**; do not count it as a newly blind independent trial.

## Design decision — two explicitly different questions

**Track A: AI-reader first-view assistance (the feasible next small trial).**
Question: With the *same full report and eligible source evidence*, does showing the actual first-view opening improve a separately scoped AI reviewer's ability to identify the topic-specific finding, its exact source and uncertainty, and a sound next observation without unsupported claims? Condition A: frozen report without first-view block; condition B: identical report with first-view block. Use historical packets as exposed development/calibration only. Exact current AV-Tracer one-line repair is a separate exposure; the November 8 HTTPX case has a different version relation and is not evidence for the AV-Tracer repair unless specifically reframed and frozen. Favor a bounded new, unexposed qualified case when seeking transfer beyond existing cases.

**Track B: AI-reader product assistance relative to ordinary review (later, harder).**
Question: With equal decision-time PR/source/CI material, does adding UpgradePilot's actual report improve **AI reviewer correctness and task completion** versus no report? Source/reference parity must be independently verified. The current GitHub rehearsal's report-only files with absent original-text attachments do not satisfy this condition. Do not infer this result from Track A.

**Not established by either track:** human review time, human decisions, human usability, real-world population generality, historical CI causality or positive maintainer action authorization. Do not call an AI-only evaluation an independent human usefulness pilot or a blinded experiment unless isolation/exposure was checked and meets the stated claim.

## Review isolation and comparability contract

1. **Freeze task, case inclusion, outputs, complete allowed files, known source omissions, oracle, forbidden overclaims and stop/budget limits before AI outputs.** Keep both treatment arms byte-bound and correct for case identity and observation horizon. Published first-view vs ordinary report and report-assisted vs ordinary review are different studies.
2. **Use distinct fresh AI reviewer sessions** with a narrow read-only packet, no full repository, memory, prior cases, grading key or other condition; same model/configuration where practical and a different session/model as a robustness check. Do not regard different chat names, session prompts, or one model's multiple samples as independent humans. If repository-wide access, cross-chat memory, prior exposure or response leakage cannot be excluded, mark the assignment *exposed* and restrict claims.
3. **Each case is seen once per reviewer.** To compare conditions on a case, assign different AI sessions to the two arms; rotate cases/order and keep tool/search/source access equivalent. Preserve errors, aborted sessions and timeouts in the denominator.
4. **Use the existing five task questions**: exact dependency/update and SHAs, material supported finding or stop reason, evidence ID and type, material unresolved obligation, bounded next observation or why none is justified. Record exact output, cited source IDs and whether citations really support claims.
5. **Score factual/semantic adequacy before efficiency**: wrong identities, false runtime causality, fabricated citation/evidence, erased uncertainty and invented action permission are critical errors; separate from partial/missing answers and operational failure. Freeze source-grounded answer evidence and use a separately constrained adjudication/verification pass; a second AI grader's vote is not proof of truth. Keep any lack of independent key review explicit.
6. **Efficiency:** measure actual AI tool calls, source opens, failed opens, navigation operations, tokens/latency where observable, and input limits, with consistent logging. Do not interpret AI latency or token reduction as human time savings. Record unknown usage as unknown rather than invent it.
7. **Public/private retention:** keep original third-party source captures, raw prompts/responses and possible sensitive content under their authorized retention boundary. Commit only public-safe manifest, hashes, qualification and redacted aggregate review. Never use a broader GitHub connector as a fiction of strict file isolation.
8. **Adoption/stop:** keep the current deterministic renderer unless the controlled comparison exposes a repeated, decision-relevant, source-backed task failure or unsupported report claim. If packets/source parity/isolated participants fail, report *not comparable* or *inconclusive*; do not build agents/embeddings/summaries to improve a result after seeing the scores without a newly frozen development round.

## Alternatives and recommendation

- **Immediate human independent pilot:** unavailable; leave the original plan's human-usefulness gate OPEN/UNMET rather than redefined.
- **Reuse GitHub rehearsal as definitive blind study:** reject; packet provenance, broad repository access, summary-only HTTPX, and source omissions defeat that claim. Reuse as explicitly exposed rehearsal.
- **Start fresh AI model calls now:** not yet justified until packet/readiness gates are met. Local-only inference and exact model/budget must be separately selected; using another AI chat manually is permissible but cannot guarantee isolation without boundary controls.
- **Selected design recommendation:** a modest **Track A AI-reader evaluation readiness/preflight** first: verify actual frozen report variants and obtainable source packet content, independently check rubric/source support, identify session-isolation mechanism, record eligible case/exposure and run bounds. If feasible, select controlled execution in a subsequent action. Track B needs a new equal-information ordinary-review packet and separate selection. No product code or report schema modification is justified now.

## Learning and status

A0 — DONE: checked current main/previous cycle, controlling report plan and November 8 AI rehearsal artifacts.
A1 — DONE (continuity-compressed): prior dialogue and Ali's new reviewer constraint anchor the real question.
A2 — DONE for this **design**: explained evaluation estimand, assistant/human distinction, isolation and fair-source requirements.
B — DONE as Planning/Design: selected an AI-only development evaluation route and excluded human-utility claim promotion.
Verification — DOCUMENTARY: exact existing protocol/packet boundaries inspected; no execution or suitability verification of isolated AI sessions.
D — DONE: Ali challenged whether either proposed experiment would be decision-relevant or simply add ceremony. The subsequent evidence/experiment audit and existing exact-report comparison favored real-case capability work rather than another readability trial.
E — DONE: Ali explicitly agreed to **defer Track A and Track B**. The controlled protocol and November 8 packets remain retained for later reentry if an unresolved decision cannot be answered more cheaply. No AI-reviewer calls, fresh acquisitions, target execution or product-code changes were performed.
C — DONE: preserved absent human-reviewer eligibility, the design alternative, the later priority challenge, deferral rationale and the selected capability-oriented handoff.

**Current disposition (supersedes the earlier Track A preflight suggestion):** No AI-reviewer packet preflight or execution now. Prioritize a narrowly defined real maintainer evidence gap, starting with an independently bounded *read-only feasibility check for the exact historical AV-Tracer CI job observation* if selected next; determine whether the old run/attempt/job logs and same-run identity could actually discriminate CI causality. Missing/expired evidence is a valid terminal result, not a reason to manufacture proof or build a generic correlation framework. This next investigation is only a proposed handoff, not executed or authorized by this closure.

## Post-design investment reassessment

Ali questioned the value of more AI reviewer exercises after the verified one-line AV-Tracer first-view improvement and the earlier Investigator audits. The project evidence already establishes the conditional source incompatibility, an honest saved-report presentation change, and the unresolved historical CI/runtime linkage. The next Track A model exercise would probably test whether an AI reads one already-visible fact; without a concrete product decision it would be disproportionately ceremonial. Track B is more consequential but needs equal-source ordinary-review packets and a decision its result would actually change; defer until there is a precise, high-value residual uncertainty.

**Decision rule for reentry:** specify (1) the implementation/product choice currently blocked, (2) outcomes that would change it, and (3) why an existing saved artifact, source audit or focused product check cannot answer more cheaply. Retain provenance/contract/regression safeguards regardless. Product-side next proposal: scope the historical AV-Tracer same-job CI observation as a read-only feasibility diagnostic, with exact run/attempt/head/step identity and truthful not-available outcomes before contemplating new runtime instrumentation or model inference.
