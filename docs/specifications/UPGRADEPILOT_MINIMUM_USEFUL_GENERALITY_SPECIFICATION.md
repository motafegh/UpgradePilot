# UpgradePilot Minimum Useful Generality Specification

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Prevent fixture-specific or manually interpreted implementations from being accepted as automated product behavior

## 1. Boundary

This specification applies when UpgradePilot admits an automated responsibility whose input
can vary while preserving or changing material meaning, including parsing, semantic
extraction, classification, normalization, evidence interpretation, transformation, and
decision-support behavior.

It does not require universal language, package-manager, repository, dependency, model, or
ecosystem support. The supported domain remains controlled by the Project Charter and the
position-neutral plan selected in `../../MEMORY.md`.

This specification does not record which responsibility is live. `MEMORY.md` alone owns that
position.

## 2. Core rule

> **Bound the supported domain, not the known fixture.**

An implementation does not satisfy an automated responsibility merely because it reproduces
the expected output for one known example. The smallest accepted implementation must process
the real input form owned by the responsibility and demonstrate useful behavior across
representative variations inside the admitted boundary.

### 2.1 Responsibility horizon

The implementation and method-selection horizon is the complete owning product
responsibility, not the next fixture, semantic label, proof case, session, or one or two
visible implementation steps.

An incremental proof may exercise one category first, but that category is a test slice
rather than permission to redefine the product method around it. A phrase list, keyword
table, exact grammar, case-specific regular expression, or separate handcrafted interpreter
per known semantic category MAY be used as an explicitly disposable baseline or test oracle.
It MUST NOT be selected, described, or extended as the product implementation when the owning
responsibility must interpret materially broader and previously unseen natural-language
evidence.

Before recommending or selecting a method, identify:

1. the complete product responsibility that owns the bounded slice;
2. the real variable input space expected inside that responsibility;
3. how the method generalizes to new evidence and semantic categories without a new
   handcrafted interpreter for each one;
4. which stable invariants deterministic code validates without encoding semantic answers;
5. the scaling, maintenance, security, and replacement cliff created by the method.

If a bounded experiment cannot credibly extend to the owning responsibility, it must remain
labelled as a rejected or disposable experiment. Passing local proof cases cannot promote it
into the project path.

## 3. Requirements

| ID | Requirement |
|---|---|
| `GEN-001` | An admitted automated responsibility MUST consume the real input form owned by that responsibility. |
| `GEN-002` | Caller-supplied interpretation MUST NOT substitute for extraction, classification, or other interpretation that the admitted responsibility is supposed to perform. |
| `GEN-003` | Exact known wording, repository names, dependency names, version values, expected answers, or one fixture MUST NOT be the sole basis of accepted behavior. |
| `GEN-004` | Representative input variations that preserve material meaning SHOULD produce equivalent normalized meaning within the supported boundary. |
| `GEN-005` | Changed meaning, including negation, different subjects or versions, deprecation versus removal, future versus present state, and added versus dropped support, MUST remain distinguishable where relevant. |
| `GEN-006` | Unsupported, ambiguous, incomplete, or conflicting meaning MUST remain unresolved, degraded, rejected, or abstained rather than guessed. |
| `GEN-007` | Material extracted or derived meaning MUST remain traceable to source evidence and transformation identity when that responsibility is admitted. |
| `GEN-008` | Machine-generated structured output MUST pass deterministic schema and applicable semantic validation before becoming trusted application evidence. |
| `GEN-009` | A manual fixture MAY define source input, an expected result, a calibration case, or a temporary adapter, but MUST NOT become the product semantic transformation. |
| `GEN-010` | Passing one known case proves only that case. Acceptance of a variable-input responsibility MUST include representative variation evidence. |
| `GEN-011` | A simpler baseline is credible only when it can perform the admitted responsibility without receiving the interpretation or decision it is supposed to produce. |
| `GEN-012` | Generality tests MUST remain bounded to credible variation in the admitted product domain; speculative universalization MUST NOT be required. |
| `GEN-013` | A proof slice, first category, known fixture, or immediate milestone MUST NOT silently redefine the owning product responsibility or method-selection horizon. |
| `GEN-014` | A selected method for variable natural-language evidence MUST provide a credible generalization mechanism beyond enumerating known phrases, keywords, exact grammars, or one handcrafted interpreter per semantic category. |
| `GEN-015` | Deterministic trusted-boundary controls SHOULD validate stable invariants such as schema, provenance, grounding, authority, contradictions, and permitted effects; they MUST NOT substitute fixture-derived semantic answers for the interpretation responsibility. |
| `GEN-016` | A narrow method that cannot credibly extend to the owning responsibility MAY be retained only as an explicitly disposable baseline, oracle, or experiment and MUST NOT be represented as accepted product behavior. |

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

Not every responsibility requires all eight classes. The plan selected in `MEMORY.md` chooses
only those that discriminate real capability from fixture matching.

## 5. Method neutrality

This specification does not select a framework or model family. It excludes phrase
enumeration, exact grammars, case-specific regular expressions, and one handcrafted
interpreter per known category as the accepted semantic architecture when the owning
responsibility requires materially broader natural-language interpretation. Those techniques
may remain disposable baselines, test oracles, or narrow deterministic validation controls
when they do not replace the interpretation responsibility.

Method selection must compare the simplest credible baseline and credible alternatives only
when the choice is consequential or genuinely unresolved. A known-answer hardcode is not a
credible baseline for semantic extraction.

A bounded LLM may be used before later learned-decision stages when natural-language
interpretation is intrinsic to an admitted responsibility, provided that:

- its task and output schema are bounded;
- source content is treated as untrusted data;
- unsupported meaning remains explicit;
- deterministic validation protects the trusted boundary;
- recommendation policy does not silently become model-controlled unless separately admitted and evaluated;
- cost, privacy, security, reproducibility, and failure behavior are addressed proportionally.

## 6. Historical M2 relationship

M2-S01 demonstrated a trusted-contract foundation through a manual eight-field adapter. That
adapter was permissible for the explicit validation and transformation responsibility it
served; it did not perform semantic extraction from natural-language evidence.

The historical adapter MUST NOT be represented as completing source-text interpretation,
evidence acquisition, or the whole automated PR-to-report product flow. Its existence does
not activate M2 work or select a present method.

Any later semantic responsibility selected through `MEMORY.md` must process real source text
into candidate structured meaning, validate that meaning, preserve unresolved states, and
connect accepted facts to the deterministic decision path without requiring callers—or a
growing set of category-specific phrase interpreters—to manually encode the meaning being
extracted.

## 7. Change control

Change this specification only when the project-wide acceptance standard for variable-input
automated behavior changes.

Do not update it for:

- one new phrase or test case;
- one model or provider change;
- ordinary implementation progress;
- a live pass/fail result;
- selection of a stage or plan;
- a new product domain that has not been admitted.