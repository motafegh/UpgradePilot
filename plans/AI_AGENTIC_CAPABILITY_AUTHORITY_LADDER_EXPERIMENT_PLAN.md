# AI / agentic capability-authority ladder — discriminating experiment plan

**Recorded:** 2026-10-05  
**Status:** Candidate supporting experiment plan; not activated.  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Authority:** Non-controlling. This plan does not change `MEMORY.md`, accepted specifications/ADRs, the active API-change implementation cycle on `main`, product action authority, or current source/tests.  
**Primary owner relationship:** refinement of the experiment competitions preserved by `AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`, especially model-context breadth, fixed investigation vs bounded planner, planner vs generalist agent, and calibrated model-claim admission.  
**Current baseline relationship:** `UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md` remains the bounded source-only API interpretation/control route. Do not broaden that trial in place to satisfy this plan.  
**Mature-architecture relationship:** `proposals/2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md` remains the broader non-controlling architecture synthesis.

## 1. Question

UpgradePilot currently uses deliberately bounded model roles and deterministic evidence/authority boundaries. That is useful for measurable proof, but it does not establish that a mature system should permanently keep model **capability** narrow.

The discriminating question is:

> When the same dependency-update problem is held sufficiently constant, how much additional product value comes from increasing model/agent investigative capability, and what additional evidentiary authority—if any—does each capability level actually earn?

The experiment must keep two axes separate:

```text
CAPABILITY
what the model/agent can inspect, choose, retrieve, execute, compare, and iterate over

!=

AUTHORITY
which propositions/effects UpgradePilot is justified in accepting from that system
```

A low-authority role need not be artificially low-capability. Conversely, a highly capable agent does not automatically earn stronger authority.

## 2. Why this experiment exists

The completed architecture research already preserved these unresolved competitions:

- narrow model projections vs controlled raw-source retrieval;
- fixed investigation sequence vs bounded planner;
- bounded planner vs generalist agent for long-tail cases;
- binary model authority vs calibrated/selective admission.

The current source-only API interpreter provides a useful bounded control because it isolates one question:

```text
supplied evidence
→ semantic interpretation proposal
```

A future agentic comparison should therefore **preserve that bounded route** and compare broader capabilities against it, rather than gradually adding tools/retries/context until the control disappears.

## 3. Capability-authority ladder

### Level A — bounded semantic interpreter / control

**Capability**

- receives fixed producer-selected source evidence;
- no tools or autonomous retrieval;
- no target-repository context;
- no iterative investigation or hidden correction loop;
- proposes structured semantic observations only.

**Authority candidate**

- proposal-level semantic interpretation only;
- source identity, coverage, grounding, target exposure, compatibility and maintainer action remain externally owned.

**Existing anchor**

- `source-only-api-change-v1` under the active API feasibility plan.

### Level B — evidence-constrained investigative agent

**Capability**

- may use bounded read-only tools over approved public repository/upstream/package/CI evidence;
- may choose which admissible source to inspect next;
- may request additional exact source spans or target files;
- may maintain competing hypotheses and explicitly identify missing premises;
- may stop when additional permitted investigation is not decision-relevant.

**Authority candidate**

- discovery and hypothesis proposals;
- every factual claim must bind to an independently recorded evidence item/source identity;
- tool access does not let the agent self-declare evidence trustworthy, complete, or sufficient;
- no product mutation or maintainer-action self-authorization.

### Level C — broader agentic impact investigator

**Capability**

- may compose upstream change evidence, target source, adapter/framework relationships and dependency context;
- may perform bounded iterative investigation across those views;
- may choose among approved read-only/static/runtime-strengthening tools where the experiment permits them;
- may produce conditional target-impact hypotheses and explicit alternatives.

**Authority candidate**

- stronger cross-evidence proposals may be evaluated for selective admission only when provenance, evaluator independence and case evidence support it;
- missing target version, activation, runtime exercise or source authority remains missing unless established by an admitted producer/tool;
- no automatic merge/remediation/action authority.

### Level D — verifier-backed selective authority candidate

This is **not an assumed next step**. Evaluate only if Levels B/C demonstrate repeatable capability value.

Possible question:

> Are there specific proposition classes for which an agent/model + independent verifier achieves sufficient accuracy, calibration, provenance and replayability to own more than a proposal?

Any such authority must be proposition-specific and evidence-earned. Do not grant a generic “trusted agent” status.

## 4. Evidence substrate rule

More agentic capability should operate over a durable evidence substrate rather than replacing it.

At minimum, retained investigation evidence should identify:

- repository / PR / base / head / package / version transition;
- exact provider/tool/request identity where material;
- source repository/revision/path/range/hash;
- target repository/revision/path/range;
- tool observations and execution/result scope;
- missing, ambiguous, truncated or conflicting evidence;
- agent-selected evidence versus producer-supplied evidence;
- hypothesis/proposal references to supporting and refuting evidence;
- model/deployment/prompt/tool-policy identity sufficient for replay/evaluation.

The mature implementation may use typed records, multiple linkable repository/evidence views, or another independently selected representation. This experiment does not preselect one universal graph.

## 5. Confirmation-loop risk

The main agentic risk is not malformed JSON. It is entanglement of:

```text
hypothesis generation
→ evidence selection
→ evidence interpretation
→ next-step selection
→ self-evaluation
```

A capable agent can accidentally create a confirmation loop by preferentially retrieving evidence that supports its current hypothesis.

Therefore comparative runs should preserve, where feasible:

- the full tool/action trajectory;
- evidence considered and evidence omitted because of limits;
- competing hypotheses or explicit absence thereof;
- deterministic/protected evaluator expectations outside the agent input;
- no post-result hidden source reshaping or retry-to-success relabeling;
- separately versioned corrected runs.

## 6. Comparative evaluation

Use the same underlying product questions/cases where technically fair. Do not require identical internal trajectories.

Measure at least:

| Dimension | Question |
| --- | --- |
| Semantic correctness | Are interpreted changes/relationships actually correct? |
| Discovery coverage / recall | Does broader capability find material evidence/candidates the bounded route misses? |
| False relationships | Does autonomy create unsupported source/target/adapter links? |
| Unsupported conclusions | Does the system overclaim completeness, applicability, compatibility or action? |
| Appropriate unresolved/abstention | Does it preserve missing premises instead of forcing an answer? |
| Provenance / grounding | Can each material factual claim be inspected against exact evidence? |
| Reproducibility / replay | Can the important reasoning/evidence path be reconstructed without pretending stochastic output is deterministic? |
| Investigation efficiency | Requests/tool calls/tokens/latency required for useful evidence gain. |
| Long-tail generalization | Does agenticity solve unfamiliar cases that fixed mechanisms cannot? |
| Robustness | Behavior under ambiguous, partial, conflicting, instruction-like or misleading source material. |
| Security | Prompt-injection/tool-manipulation resistance; credential/network/filesystem/mutation boundaries. |
| Maintainer usefulness | Does added capability improve the eventual evidence-informed maintainer task rather than just produce more prose? |

Do not use autonomous-action rate, answer length, apparent confidence, or “agent found something” as primary success measures.

## 7. Case/evaluation discipline

- Preserve the bounded source-only interpreter's frozen cases/results as control evidence; do not retrofit them to make an agent comparison easier.
- Add protected/unseen cases before claiming general agentic benefit.
- Include cases where the correct outcome is unresolved or no additional justified investigation.
- Include at least one case where a tempting evidence path is misleading and another where additional retrieval genuinely changes the result.
- Distinguish development/calibration cases from independent admission and maintainer-usefulness evidence.
- A broader agent may legitimately inspect more evidence than Level A; compare the resulting evidence gain explicitly rather than pretending inputs were identical.
- For direct semantic-method comparisons, provide equivalent source/context where the tested variable is interpretation rather than retrieval.

## 8. Activation triggers

Do not activate this plan merely because agentic systems are interesting.

A Level-B/C experiment becomes justified when at least one is true:

1. the bounded API/source interpreter establishes a usable baseline and a real target case remains unresolved because useful evidence selection is state-dependent;
2. a repeated long-tail case requires manual orchestration across upstream/target/adapter evidence that fixed mechanisms do not handle proportionately;
3. model-context breadth or fixed-vs-adaptive investigation remains a material architecture competition after current controlled trials;
4. external/provider/tool capability changes create a materially stronger testable agentic alternative;
5. the mature architecture reconciliation explicitly selects one of the queued E5/E6/E7 experiments.

## 9. Stop / re-entry rules

Stop and return to design/evaluation if:

- agent tool scope expands materially after evaluation output is seen;
- hidden retries/corrections make failed first passes disappear;
- exact evidence identity cannot be retained;
- evaluation labels or known target diagnosis leak into normal agent inputs;
- the agent needs write/mutation authority to demonstrate the claimed investigation value;
- success depends on package-specific answer mappings;
- agent-selected evidence prevents a fair determination of what was omitted;
- broader autonomy increases persuasive output but not measurable maintainer/evidence value.

## 10. Relationship to current UpgradePilot work

### Current API interpretation Build

The current `UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md` remains the control/baseline route:

```text
acquired source
→ bounded source-only semantic proposal
→ deterministic validation/evaluation
→ later target-exposure composition
```

Do **not** add agent tools, target context, autonomous retrieval, retry loops or action authority to that role merely to pre-empt this future comparison.

### Existing AI/agent architecture research

This plan refines, rather than replaces:

- E5 — model-context breadth comparison;
- E6 — fixed investigation sequence vs bounded planner;
- E7 — bounded planner vs generalist agent for long-tail cases;
- E8 — calibrated model-claim admission.

### Existing LangGraph / EvidenceGapPlanner work

Treat those experiments as prior evidence about orchestration, bounded planning, proposal-vs-authority separation, failure classes and framework cost. They do not prescribe the topology/framework of a future agentic repository investigator.

### Mature proposal

The 2026-09-29 mature proposal's route remains the higher-level hypothesis:

```text
fixed-first investigation
→ bounded planner where state-dependent choice is justified
→ optional runtime strengthening
→ rare generalist escalation
```

This plan supplies the future comparative evidence needed to decide whether that escalation ladder is actually better than the bounded alternatives.

## 11. Decision outcomes

After a properly activated comparison, possible outcomes include:

```text
KEEP BOUNDED
additional agenticity does not justify its cost/risk

ADOPT BOUNDED PLANNER
state-dependent retrieval materially improves coverage with acceptable proof/security cost

ADOPT HYBRID AGENT + EVIDENCE SUBSTRATE
agentic exploration is useful, but accepted claims remain independently grounded/admitted

ADMIT SELECTIVE MODEL/AGENT AUTHORITY
only for specific proposition classes with protected evaluation and calibration evidence

DEFER
current models/tools/cases do not discriminate the architectures credibly
```

Do not select “more agentic” as the winner merely because it is more flexible or modern.

## 12. Current state

**NOT ACTIVATED.**

This plan is preserved as a future discriminating experiment candidate. The active API-change implementation on `main` and the deferred-D learning continuation on the branch proceed independently.
