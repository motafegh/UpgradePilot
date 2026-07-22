# 08 — Cross-Case Synthesis and Automation Admission

**Depth target:** Implementation-adjacent understanding and early ownership practice.  
**Primary question:** What can two cases justify, what remains conditional or unresolved, and how should manual usefulness influence later automation decisions?

## 1. Why cross-case synthesis is necessary

One case can produce a convincing but overfitted product model.

Cross-case synthesis asks:

- which responsibilities repeated;
- which appeared only under a specific condition;
- which prior assumptions were contradicted;
- where representation drift creates tooling problems;
- which artifact boundaries survived;
- which decisions remain unsupported;
- what next case would provide the highest-value evidence.

S001 and S002 are materially different enough to support comparison, but not broad completeness claims.

## 2. The two-case contrast

| Dimension | S001 | S002 |
|---|---|---|
| Relationship | transitive docs tooling | direct declaration, adapter-mediated test use, production installation |
| Main concern | advisory remediation and target relevance | removed API and framework-adapter compatibility |
| CI | relevant docs build passed | install/build passed, relevant tests skipped |
| Environment | lock-derived | unpinned historical resolver unavailable |
| Decision | normal review | targeted checks |
| Main limitation | complete target-condition exposure unresolved | exact environment and behavioral result missing |

The same artifact family represented both, but individual record shapes drifted.

## 3. Cross-case classification vocabulary

### Repeated stable candidate

A responsibility or pattern appeared materially in multiple cases and deserves continued use and testing.

Examples:

- exact case identity freeze;
- invocation separate from discovered identity;
- dependency path as first-class evidence;
- multi-axis dependency role;
- CI authority at trigger/command/revision/environment depth;
- explicit missing and expired states;
- separate evidence, transformation, findings, decision, reports, follow-up, and review;
- supersession;
- structural validation;
- ownership separate from completion.

“Repeated stable candidate” is not “final production contract.”

### Conditional responsibility

Useful only when the case activates the need.

Examples:

- advisory analysis;
- framework-adapter comparison;
- package artifact verification;
- dynamic execution;
- private or credentialed acquisition;
- platform or compiler analysis;
- causal failure attribution.

A conditional responsibility must not become a mandatory universal stage.

### Contradicted assumption

Real evidence shows a prior simplification is wrong or too broad.

Examples:

- one dependency-role enum is adequate;
- direct imports are the only meaningful use path;
- green CI has global authority;
- workflow color is enough without command coverage;
- advisory presence proves target relevance;
- merge proves correctness;
- every case needs dynamic execution;
- one `CASE.md` simulates the complete runtime;
- artifact counts measure quality;
- manual success proves automation feasibility.

### Unresolved

The current evidence cannot justify a stable answer.

Examples:

- claims and interpretations as one or two physical streams;
- append-only findings versus current-state projection;
- follow-up separate from decision;
- raw capture grouping at scale;
- one or two decision axes;
- real rerun semantics;
- conflict and decision versioning;
- cost when the baseline is sufficient;
- reliable automation boundary;
- Ali independent depth.

## 4. Artifact-family result

The default top-level responsibilities survived both cases.

No evidence currently justifies:

- removing one universal responsibility;
- adding a new universal top-level artifact;
- normalizing old records cosmetically.

The physical representations drifted in:

- envelopes;
- IDs;
- run/time formats;
- JSON formatting;
- limitation and transition shapes;
- validation practices.

The correct next step is to use one prospective S003 profile, not rewrite historical evidence to look consistent.

## 5. Counts are not quality metrics

S001 has more operations and S002 has more physical files. These differences reflect grouping and preservation choices.

Do not rank cases through:

- artifact count;
- operation count;
- evidence count;
- claim count;
- finding count;
- document length.

Better cross-case measures include:

- logical responsibility coverage;
- lineage completeness;
- decision relevance;
- uncertainty honesty;
- replay value;
- duplication and cost;
- reviewability;
- ability to identify a proportionate next action.

## 6. Automation-feasibility classification

A manually performed responsibility can be classified as:

- manually feasible;
- deterministically automatable;
- tool-assisted with interpretation required;
- model-dependent;
- human-review required;
- blocked by inaccessible evidence;
- not yet tested;
- unsuitable for automation.

This classification is evidence about feasibility. It is not architecture admission.

## 7. Current automation evidence

### Strong deterministic candidates

- freezing mechanical PR identity;
- parsing simple version transitions;
- JSON/JSONL parsing and structural validation;
- report rendering after representation contracts stabilize;
- basic inventory and reference checks.

### Tool-assisted but not settled

- dependency-path resolution across ecosystems;
- workflow trigger and command extraction;
- environment and artifact acquisition;
- source comparison.

### Interpretation-heavy and unvalidated

- repository-specific relevance;
- causality;
- evidence proportionality;
- uncertainty calibration;
- bounded decision construction.

### Human authority remains required

- target mutation;
- final merge/block action;
- credentials and private evidence authorization;
- residual-risk acceptance;
- architecture admission;
- Ali capability assessment.

## 8. Manual usefulness versus product admission

Suppose an LLM helps explain a complex workflow.

Possible conclusions:

- useful manual aid;
- requires source-grounding and review;
- may reduce investigation time;
- may generate plausible false interpretations;
- automation reliability remains unmeasured.

Invalid leap:

> The product should use an LLM agent for CI analysis.

Admission would require evidence about:

- benchmark scope;
- false-positive and false-negative costs;
- repeatability;
- grounding and authority controls;
- fallback behavior;
- security and privacy;
- latency and cost;
- auditability;
- comparison with simpler methods;
- human-review requirements.

## 9. Mixed-system hypothesis

The cross-case review suggests a possible mixed system:

- deterministic identity, parsing, retrieval, validation, and rendering;
- tool-assisted dependency, source, workflow, and environment analysis;
- model/human-assisted relevance, causality, proportionality, and uncertainty judgment;
- explicit human authority for external actions.

This remains a discovery hypothesis, not an architecture decision.

## 10. Thesis status

Both cases show:

```text
baseline broad action = full-investigation broad action
+
full investigation materially improves authority, calibration, explanation,
auditability, or actionability
```

The project still needs:

- a wrong-action baseline case;
- a baseline-sufficient case;
- an unresolved comparison;
- a possible overreach or excessive-cost case.

S003 is selected for causal failure attribution, not to force one thesis class.

## 11. Why M2-S03 remains paused

Two retrospective bundles justify better planning, not implementation resumption.

Still missing:

- prospective artifact lifecycle evidence;
- real failing-CI attribution;
- repeated check-execution representation;
- decision-axis testing;
- real rerun and supersession behavior;
- additional contrasting thesis classes;
- Ali review and ownership evidence.

## 12. Read and inspect

- `S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`;
- `SCENARIO_COVERAGE.md`;
- S001 and S002 manifests and validation results;
- `S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`;
- `plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md` for the paused implementation boundary.

## 13. Classification exercise

Classify each statement:

1. Exact head identity must be frozen before evidence is joined.
2. Every case must perform advisory analysis.
3. A green status proves all required checks passed.
4. The physical field names in S002 are the future API schema.
5. Causal attribution should be a dedicated universal artifact.
6. Structural validation appears deterministically automatable.
7. A completed AI case proves Ali can perform the analysis.

Expected classifications:

1. repeated stable candidate;
2. contradicted as universal, conditional responsibility;
3. contradicted assumption;
4. unsupported admission claim;
5. unresolved trial question for S003;
6. deterministic candidate with common-profile work remaining;
7. contradicted ownership inference.

## 14. Ownership checkpoint

1. Name five repeated stable candidates and explain the two-case evidence for each.
2. Name three conditional responsibilities and state their activation condition.
3. Explain why old S001/S002 representations should not be cosmetically normalized.
4. Propose one quality measure better than artifact count.
5. Classify dependency-path analysis, CI-authority interpretation, and report rendering by automation feasibility.
6. Explain what evidence would be required to admit an interpretation-heavy method.
7. Explain why the mixed-system hypothesis is not architecture.
8. State the minimum evidence still needed before implementation planning resumes.

## 15. Current demonstrated depth

The repository supports a disciplined two-case synthesis and a prospective next-case design. It does not establish universal product responsibilities, final schemas, reliable automation, representative frequency, or Ali-owned synthesis capability.
