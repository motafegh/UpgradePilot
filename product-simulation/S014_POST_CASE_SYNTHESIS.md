# S014 Post-Case Synthesis — Dependency State Truth versus Installation Provenance

**Date:** 2026-09-22
**Status:** Completed bounded synthesis; non-controlling Product Simulation evidence
**Scenario:** `scenarios/S014-production-ready-cicd-pip-already-satisfied-vs-installed/README.md`

## 1. Result

S014 gives direct real-world support to the current main B5 wording:

> at successful command completion, the exact requested version was satisfied/present

is defensible across both a true state-changing install and an already-satisfied execution.

The stronger generic statement:

> the proposed version was installed by this command

is false for the PR execution.

## 2. Natural control

The case is unusually strong because the workflow file is identical at base and head and the only PR change is the pip pin in `requirements-tooling.txt`.

Under the same dependency-audit command and CPython 3.12.14:

- base asks for `pip==26.1.2`, finds 26.2.1, uninstalls it, and installs 26.1.2;
- PR asks for `pip==26.2.1`, finds that exact version already present, and leaves it in place.

Both commands succeed.

Therefore success plus exact requirement does not encode installation provenance.

## 3. State proposition versus provenance proposition

S014 separates:

`STATE: exact version is satisfied/present at command completion`

from:

`PROVENANCE: this exact command caused that version to become present`.

The first may be true while the second is false.

This is directly relevant to B5 result naming and downstream explanation/auditability.

## 4. Relationship to B5 P1-P7

The current B5 candidate describes one valid inferential route:

`exact requirement + exact consumption + admitted semantics + exact success + manager guarantee → satisfied/present at completion`.

S014 supports the result of that route.

However, the PR log also exposes a potentially stronger independent route:

`trusted exact runtime observation → Requirement already satisfied: pip==26.2.1 → direct state evidence`.

This matters because a direct state witness and a state-producing-operation proof are not logically identical.

For example, a state-producing semantic defeater such as dry-run could prevent an operation from being credited with producing state while a sufficiently trustworthy direct observation could still establish that the exact state already existed.

S014 does not claim that current pip logs are already an admitted UpgradePilot evidence source. It only says future proof design should not collapse all possible state evidence into one operation-guarantee route.

## 5. Relationship to B4

B4 correctly asks whether package-manager semantics defeat using a command as a state-producing witness.

S014 adds a boundary:

`not eligible as state producer` does not always imply `cannot know state`.

A separate direct state observation may establish state without crediting the command with producing it.

This mirrors B4's demand-driven nearest-witness strategy: when a stronger witness directly resolves the proposition, broader provenance reconstruction may be unnecessary for that proposition.

## 6. Relationship to S013

S013:

`earlier sync produces state → later no-sync command exercises already-formed state`.

S014:

`same command can succeed with or without producing new state → state truth differs from production provenance`.

Together they pressure a clean temporal/evidence model without requiring a generic temporal engine.

## 7. Evaluation implications

S014 is a future regression anchor for:

- overclaiming fresh installation from successful pip execution;
- losing already-satisfied positive state;
- conflating command eligibility with state provenance;
- ignoring stronger direct state observations when available;
- extending command-completion state into later persistence without evidence.

## 8. Main-thread handoff

Immediate conceptual handoff to B5:

1. Keep `satisfied/present at command completion`; do not rename it to `installed by command`.
2. Preserve provenance separately from state truth.
3. Treat P1-P7 as an operation-inference route, not necessarily the only future route to dependency-state evidence.
4. If direct runtime state witnesses are later admitted, define their own trust/identity contract rather than forcing them through state-producing semantics.
5. Keep later persistence/exercise outside this result.

No product implementation is authorized by this case.

## 9. Stop

S014 is complete at the admitted depth. No synthetic reproduction is needed because the real unchanged-workflow base/head pair already discriminates the proposition.