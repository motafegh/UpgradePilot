# UpgradePilot Minimum Useful Generality Specification

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Prevent fixture-specific or manually interpreted implementations from being accepted as automated product behavior

## 1. Boundary

This specification applies when UpgradePilot activates an automated responsibility whose input can vary while preserving or changing material meaning, including parsing, semantic extraction, classification, normalization, evidence interpretation, transformation, and decision-support behavior.

It does not require universal language, package-manager, repository, dependency, model, or ecosystem support. The supported domain remains controlled by the Project Charter and active project plan.

## 2. Core rule

> **Bound the supported domain, not the known fixture.**

An implementation does not satisfy an automated responsibility merely because it reproduces the expected output for one known example. The smallest accepted implementation must process the real input form owned by the responsibility and demonstrate useful behavior across representative variations inside the activated boundary.

## 3. Requirements

| ID | Requirement |
|---|---|
| `GEN-001` | An activated automated responsibility MUST consume the real input form owned by that responsibility. |
| `GEN-002` | Caller-supplied interpretation MUST NOT substitute for extraction, classification, or other interpretation that the activated responsibility is supposed to perform. |
| `GEN-003` | Exact known wording, repository names, dependency names, version values, expected answers, or one fixture MUST NOT be the sole basis of accepted behavior. |
| `GEN-004` | Representative input variations that preserve material meaning SHOULD produce equivalent normalized meaning within the supported boundary. |
| `GEN-005` | Changed meaning, including negation, different subjects or versions, deprecation versus removal, future versus current state, and added versus dropped support, MUST remain distinguishable where relevant. |
| `GEN-006` | Unsupported, ambiguous, incomplete, or conflicting meaning MUST remain unresolved, degraded, rejected, or abstained rather than guessed. |
| `GEN-007` | Material extracted or derived meaning MUST remain traceable to the source evidence and transformation identity when that responsibility is activated. |
| `GEN-008` | Machine-generated structured output MUST pass deterministic schema and applicable semantic validation before becoming trusted application evidence. |
| `GEN-009` | A manual fixture MAY define source input, an expected result, a calibration case, or a temporary adapter, but MUST NOT become the production semantic transformation. |
| `GEN-010` | Passing one known case proves only that case. Acceptance of a variable-input responsibility MUST include representative variation evidence. |
| `GEN-011` | A simpler baseline is credible only when it can perform the activated responsibility without receiving the interpretation or decision it is supposed to produce. |
| `GEN-012` | Generality tests MUST remain bounded to credible variation in the activated product domain; speculative universalization MUST NOT be required. |

## 4. Representative proof classes

When applicable, proof should cover the smallest credible set of:

1. **same-meaning variation** — different wording with materially equivalent meaning;
2. **changed meaning** — changed subject, version, direction, state, or time;
3. **negation** — explicit denial of the candidate fact;
4. **ambiguity or missing detail** — insufficient support for required structured fields;
5. **irrelevant input** — no supported fact should be invented;
6. **untrusted-content behavior** — embedded instructions or misleading text must not redefine system policy;
7. **malformed model or parser output** — deterministic validation rejects or degrades it;
8. **source traceability** — accepted meaning links to its actual source.

Not every responsibility requires all eight classes. The active plan selects only those that discriminate real capability from fixture matching.

## 5. Method neutrality

This specification does not select regular expressions, parsers, classical NLP, fine-tuned models, instruction-following LLMs, agents, or hybrid methods.

Method selection must compare the simplest credible baseline and credible alternatives only when the choice is consequential or genuinely unresolved. A known-answer hardcode is not a credible baseline for semantic extraction.

A bounded LLM may be used before later learned-decision milestones when natural-language interpretation is intrinsic to an activated responsibility, provided that:

- its task and output schema are bounded;
- source content is treated as untrusted data;
- unsupported meaning remains explicit;
- deterministic validation protects the trusted boundary;
- recommendation policy does not silently become model-controlled unless separately activated and evaluated;
- cost, privacy, security, reproducibility, and failure behavior are addressed proportionally.

## 6. Relationship to current M2 work

`M2-S01` remains a trusted-contract foundation. Its manual eight-field adapter is permitted because that sub-responsibility is explicit validation and transformation of supplied case data, not semantic extraction from natural-language evidence.

The adapter MUST NOT be presented as completing source-text interpretation, evidence acquisition, or the whole automated PR-to-report product flow.

The next semantic responsibility must process known source text into candidate structured meaning, validate that meaning, preserve unresolved states, and connect accepted facts to the deterministic decision path without requiring callers to manually construct the fact being extracted.

## 7. Change control

Change this specification only when the project-wide acceptance standard for variable-input automated behavior changes.

Do not update it for:

- one new phrase or test case;
- one model or provider change;
- ordinary implementation progress;
- current pass/fail status;
- a new product domain that is not yet admitted.
