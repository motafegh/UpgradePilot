# Learning Session — Product Direction, Hybrid Reporting, and Maintainer Utility

**Date/time:** 2026-10-03 19:19 Asia/Tehran
**Session status:** ACTIVE
**Primary responsibility/mode:** Learning/discussion only; no `main` mutation
**Branch:** `learning/product-direction-report-2026-10-03`
**Base:** `main@9b281229d8ac9094aec7c3315003267bdd8f6938`
**Related plan:** [Product Direction and Maintainer Utility Investigation](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md)
**Current live owner remains:** [MEMORY.md](../MEMORY.md)
**Procedure:** UP-SKILL:upgradepilot-working-memory

## Session anchor

Ali explicitly asked to keep the ongoing `main` work untouched and use this separate branch for learning, discussion, discovery, and durable notes that may be useful later.

This record is deliberately non-controlling. It may preserve hypotheses, questions, useful discoveries, and candidate implications, but it does not change the live project position, accepted semantics, selected implementation responsibility, or authorization on `main`.

## Current learning model

### Report is not merely a saved file

The report direction is understood as a product-facing decision-support layer:

```text
internal evidence / findings / uncertainty
        ↓
faithful projection
        ↓
maintainer-readable explanation
        ↓
decision-relevant unknowns
        ↓
justified next checks
        ↓
action or abstention when independently supported
```

Saving a report, preserving raw evidence, replaying analysis, rerunning acquisition, and recovering interrupted execution are separate promises.

### Hybrid direction hypothesis

Ali's current intuition is that action-led alone is unattractive because UpgradePilot cannot always justify a strong action, while hybrid allows useful assistance under uncertainty.

Refined engineering interpretation:

> Advisory usefulness and action permission have different evidence thresholds.

Hybrid should mean: provide the strongest useful decision-support output the evidence truthfully supports, while independently controlling whether a stronger action claim has been earned.

### Evidence strength ladder

```text
observed evidence
      ↓
supported interpretation
      ↓
material unresolved proposition
      ↓
justified discriminating check
      ↓
positively supported maintainer action
```

## Real-case learning anchors

### S014 — already satisfied vs installed by command

- Successful exact requirement execution may support "exact version satisfied/present at command completion."
- It does not necessarily support "this command installed the version."
- Later persistence, later exercise, compatibility, and merge safety remain separate propositions.

### S015 — marker-scoped applicability

- Changed requirements file consumed != changed exact requirement applies in this environment.
- A green sibling matrix row cannot establish a changed marker-scoped dependency when the marker does not apply there.
- Current normal product extraction does not support marker-bearing exact pins.
- Research knowledge must not be projected as current automated product output.

General rule:

```text
useful information exists in reality
        !=
UpgradePilot can currently acquire/derive it
        !=
UpgradePilot can currently present it
```

## Candidate discoveries worth carrying forward

1. Usefulness should be graded by claim strength, not binary action success.
2. Report projection should be decision-relevant rather than evidence-complete.
3. A good abstention should still identify the exact blocker and, when supported, a useful discriminating check.
4. A justified next check is a substantive product outcome and must not degrade into generic "run more tests."
5. Research-case insight and normal product capability must remain separate.
6. User-facing output likely benefits from layered presentation: concise decision support first, deeper provenance/evidence on inspection.

## Refinement — decision-driving prioritization and progressive disclosure

Current plans/specifications already require material, decision-relevant, discriminating output. The new learning is therefore a refinement rather than a missing product direction.

Possible refinement:

> The primary maintainer-facing layer should prioritize the smallest set of decision-driving findings, uncertainties, and next steps needed to make progress on the exact update, while supporting evidence/provenance remains inspectable through progressive disclosure rather than competing for equal prominence.

Open questions:

- How should multiple material findings be ordered?
- What belongs on the primary surface versus supporting detail?
- Can a fact be materially true but not currently decision-driving?
- What stable rule can prioritize content without opaque scoring or hiding relevant uncertainty?

## Learning — requirement declarations are a semantic family

S015 exposed that `package==version` is only the simplest dependency declaration form.

Marker support is already considered: S015 records it as a real future source-support question and freezes this invariant:

```text
package/version + marker + selected runtime environment
        ↓
applicable / non-applicable / unresolved
```

It is not the currently selected Build responsibility. Re-enter when a real finding, check, or action is blocked by the missing capability.

Adjacent forms that may matter:

1. bare exact pin: `pytest==9.0.3`;
2. marker-bearing pin: `pytest==9.0.3 ; python_version == "3.8"`;
3. extras: optional dependency selections such as `requests[security]`;
4. non-exact/range specifiers: `>=`, `<`, `~=`, `!=`, wildcards and compound ranges;
5. direct URL/VCS/archive references, where source/revision/artifact identity becomes part of the proposition;
6. requirements-file composition via included requirements and constraints;
7. editable/local/path forms and install options that affect source, selection, or resolver behavior.

Adjacent applicability/selection pressures outside one requirement line include:

- selected extras/groups/roots, already validated by S016;
- package Python-version compatibility metadata;
- wheel/artifact/platform compatibility;
- exact index/source/binary/hash policy;
- transitive dependency metadata with its own markers/extras.

Important conceptual decomposition:

```text
DECLARED DEPENDENCY PROPOSITION
identity + version constraint/direct source + extras + marker
        ↓
APPLICABILITY / SELECTION
runtime environment + selected extras/groups/roots
        ↓
RESOLUTION CONTEXT
index/source/binary/hash/configuration policy
        ↓
RESOLVED / OBSERVED PACKAGE STATE
exact artifact/version/environment/runtime evidence
```

Syntax recognition is not semantic support. Do not solve this by merely widening one regex.

Current evidence suggests a demand-driven priority:
marker applicability → extras/groups/selected roots → constraints/includes → non-exact ranges → direct references/local/editable forms → resolver/index/binary/hash policy as concrete decision pressure appears.

This taxonomy is a learning hypothesis, not implementation authorization or a new plan.

## Current route

Continue learning/discussion without changing `main`.

Near-term topics:
- distinguish a genuinely useful next check from generic/speculative advice;
- understand which dependency-declaration/applicability forms deserve future support based on real decision pressure;
- preserve any useful refinements here for later promotion through the correct owner if selected.
