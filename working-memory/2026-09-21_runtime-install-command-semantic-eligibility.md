# Runtime install-command semantic eligibility — 2026-09-21

**Status:** ACTIVE — first child slice of the Runtime Dependency-State Proof Completion Plan.  
**Master plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Investigation evidence:** `working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`  
**Operation:** Planning/Design + Learning-by-Doing. No product implementation is authorized by this record alone.

## Starting point

The full F6 investigation established that the broad audit wording should be narrowed. Current command parsing already preserves shell syntax, command identity, literal/dynamic arguments, structural context, and bounded runtime correlation.

The immediate problem is not Tree-sitter recognition. It is package-manager semantic interpretation.

Verified current example:

```text
pip install -r requirements.txt
pip install --dry-run -r requirements.txt
```

Both can preserve the same direct requirements-source declaration because `--dry-run` survives parsing as a literal argument but `direct_install.py` currently searches for the requirements source without assigning installation-state meaning to that option.

Short-circuit/conditional/pipeline/asynchronous cases are different: those are shell grammar/structure and are already classified by the Tree-sitter-backed provider.

## This slice's responsibility

Establish the smallest trustworthy semantic eligibility rule for currently supported pip/uv dependency-consuming command shapes before designing any stronger runtime dependency-state inference.

The question is:

> Which parsed command/options positively permit “successful command execution establishes the proposed dependency version was satisfied/present at command completion,” and which options must instead produce non-eligible or unresolved evidence?

## Planned actions

1. Trace the current pip and uv semantic option handling from parsed command atoms to dependency-consumption declarations.
2. Enumerate only material options reachable in today's supported product paths.
3. Classify each relevant option:
   - positive/compatible;
   - non-installing/excluding/retargeting;
   - ambiguous/dynamic/unsupported.
4. Compare the classification with existing tests and real supported scenarios.
5. Decide the earliest owner for the semantic rule and whether current result types can express it without overloading the existing declaration contract.
6. Present the resulting design to Ali before any Build/Implement step.

## Learning focus

Ali should be able to distinguish:

```text
shell syntax/structure
→ Tree-sitter/provider responsibility

package-manager option meaning
→ dependency semantic responsibility

runtime step success
→ CI/runtime evidence responsibility

resulting dependency state
→ stronger composed proof
```

## Acceptance / stop condition

This slice closes when:

- the relevant pip/uv option classes are source-backed and understandable;
- the correct owner/layer is selected;
- the smallest semantic repair is clear;
- positive, negative and unresolved examples are identified;
- no implementation has started without explicit authorization.

If semantic analysis alone cannot support a bounded positive dependency-state inference, stop and hand the result back to the master plan's explicit package-state evidence layer rather than stretching the parser.

**Procedural provenance:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
