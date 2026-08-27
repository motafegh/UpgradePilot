# Build Source Clarity Application Heuristics

Use this reference only when the main Build Skill's Source Clarity gate identifies material clarity pressure that needs more detailed application guidance.

`OPERATING_GUIDE.md` §6 remains the canonical owner of the seven Source Clarity acceptance outcomes. `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` remains the naming/terminology owner. This file supplies optional Build-time application heuristics; it does not create another semantic owner.

Apply only the heuristics that materially reduce ambiguity in the selected source responsibility. Do **not** treat this file as a checklist, do not expand a bounded change into a documentation campaign, and return to the main Build procedure after applying the relevant guidance.

## 1. Reader orientation / START-HERE

For a substantial or non-trivial module, make the important reading route discoverable near the top when useful:

```text
RESPONSIBILITY
→ what it deliberately does not own
→ normal upstream/caller
→ primary semantic/public entry point
→ important inputs/shapes
→ main stages
→ output/problem states
→ downstream consumer
→ proof boundary
```

Exact headings are optional. Small files do not need an architecture essay.

## 2. Bidirectional cross-file flow

For important values/evidence crossing modules, make both directions recoverable where needed:

```text
where did this come from?
what owner/type gives it meaning?
where is it transformed?
where does it go next?
what semantic/proof authority changes—or does not change?
```

Use exact source paths/types/functions only when they materially reduce search cost.

## 3. Imports and neighboring modules

Explain an import/library/module role only when its **project-local participation** is non-obvious and material.

Good explanation: why/how the dependency participates in this mechanism.

Avoid encyclopedia definitions and comments on ordinary imports.

## 4. Constants, domain literals, regexes, sentinels, structural devices

Explain when material:

- what domain concept the values/device represent;
- where the device is used;
- what decision it controls;
- why that rule belongs here;
- accepted/rejected shape for an admission regex when that boundary matters.

Do not narrate syntax character by character unless the exact grammar is itself maintenance-critical.

## 5. Decision-boundary “why” comments

Comments are especially valuable where code:

- rejects or abstains;
- short-circuits;
- refuses an inference;
- prefers one evidence source;
- keeps similar-looking states separate;
- applies precedence or a conservative branch.

Explain the ambiguity, failure mode, claim inflation, or ownership error the branch prevents.

## 6. Layer explanation at its narrowest owner

Prefer:

```text
module scope → orientation/data-flow map
callable/type docstring → stable input/output/ownership contract
first relevant domain use → practical terminology meaning
branch → branch-specific reasoning
inline comment → truly local clarification
```

One strong owning explanation plus precise references is better than repeated prose that can drift.

## 7. Semantic/proof transformations

When evidence is parsed, normalized, filtered, correlated, aggregated, narrowed, or promoted, state proportionately what is:

```text
retained
removed
strengthened
weakened
deliberately not inferred
```

Do not let representation change look like increased semantic authority when it is not.

## 8. Callable contracts and representative shapes

For a primary/public callable or non-trivial transformation, make important inputs/outputs/ownership/handoff clear when the signature alone is insufficient.

A small representative shape/example is useful when it reduces ambiguity, but it must illustrate the contract rather than imply only that literal fixture is supported.

## 9. Primary API versus auxiliary APIs

When several public callables coexist, identify the main semantic entry point when ambiguity would otherwise make the file hard to read. Distinguish admission predicates, acquisition gates, formatting helpers, compatibility shims, and other support functions from the primary transformation.

## 10. Structural grouping

For a large module, use names/order/spacing/lightweight section comments to make responsibility groups navigable, for example:

```text
public API
validation/admission
parsing/transformation
comparison/canonicalization
utilities
```

Do not add decorative banners to small files.

## 11. Types and narrowing as domain states

When a union, `Literal`, optional value, alias, protocol, or guard materially expresses evidence states/invariants, explain what **real project states** it represents and what successful narrowing allows later code to assume.

Do not teach generic typing syntax inside production comments.

## 12. Guard clauses as permissions

When semantically accurate, explain both:

```text
why failure stops
+ what passing the guard authorizes the next stage to trust/assume
```

This is valuable when guards form an evidence/proof ladder rather than independent defensive checks.

## 13. Non-obvious algorithms and data structures

Do not comment loops, comprehensions, `Counter`, sorting, sets, etc. merely because they are Python mechanisms.

Explain them when their choice carries a project semantic, invariant, ambiguity-handling strategy, or proof consequence.

## 14. Terminology collisions

Disambiguate only at points where similar words have materially different meanings and confusion could change interpretation.

## 15. Current / transitional / legacy surfaces

When old/new paths, compatibility aliases, projections, migration-only APIs, or transitional code coexist, make visible:

- which surface is current for new code;
- what remains only for compatibility/migration;
- which real responsibility still depends on it;
- removal/migration trigger when known.

Do not delete compatibility only to simplify documentation; retention remains a separate `JUST-*` decision.

## 16. Bounded clarity obligation when touching old code

When modifying older code, improve nearby ambiguity that is materially part of the touched responsibility. Do **not** turn a bounded change into a repository-wide documentation campaign.

## 17. Maintenance

Comments/docstrings are maintained code. Update or delete them when behavior, ownership, type shape, naming, data flow, or proof meaning changes.

Stale explanations are defects.
