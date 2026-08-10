# B2 Transparent Decision Method Plan

**Status:** Superseded — historical/non-controlling  
**Superseded by:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Retention:** Preserved in place as pre-reconciliation and future-Conversation-D source material; this file is **not** itself an accepted Conversation-D plan  
**Live-state authority:** `../MEMORY.md` alone owns current plan selection and continuation  

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Applicable generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

## Purpose

Define and prove the first transparent method that turns UpgradePilot's validated evidence into a bounded maintainer action or honest abstention.

```text
validated PR, dependency, CI, package, and upstream evidence
→ decision-relevant interpretation
→ evidence-sufficiency and stopping evaluation
→ bounded maintainer action or abstention
→ reasons, uncertainty, required checks, and claim limits
```

This plan defines position-neutral scope, sequence, proof, and stop conditions. It does not declare itself active or record progress. `../MEMORY.md` alone selects a plan and states continuation.

## Owning product question

The stable project question remains:

> For an admitted public Python Dependabot dependency-update pull request, what bounded maintainer action is justified by the decision-relevant evidence available for that case?

The controlling charter permits these broad outcome classes:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

This increment may select clearer runtime names, but it must preserve those meanings and must not silently narrow the permanent product responsibility to the S004 pytest control case.

## B2 responsibility horizon

The first method operates only on the evidence domain admitted by the B2 vertical slice:

```text
public GitHub Dependabot PR
+ one trusted canonical exact-version Python dependency transition
  from an admitted representation
+ bounded exact-head CI-authority result
+ exact PyPI package/version evidence
+ bounded project-controlled upstream evidence
```

A case outside that admitted domain must remain unsupported or abstained. The method must not force unsupported cases through S004-specific assumptions or treat the dependency representation as decision meaning.

The dependency transition contract establishes package and version identity only. Representation-specific provenance remains evidence, while direct/transitive role, target usage, CI consumption, compatibility, and safety require their own evidence rules.

## Control-case role

`googlefonts/glyphsLib#1145`, pytest `9.0.2` → `9.0.3`, is the first successful control case. It is used to:

- trace one complete evidence-to-decision path;
- expose missing semantic and sufficiency responsibilities;
- test whether the method can justify normal review without overclaiming safety;
- provide one live proof after controlled behavior is established.

It is not the product scope, a hidden expected answer, or permission to encode pytest, version `9.0.3`, known wording, the historical merge, or the control-case release URL.

## Required conceptual separation

The implementation and explanation must keep these responsibilities distinct:

```text
Acquisition
→ What evidence exists and where did it come from?

Dependency interpretation
→ What exact package/version transition was established, through which representation,
  and with what ambiguity or conflict?

Evidence interpretation
→ What bounded decision-relevant claim does the evidence support?

Sufficiency
→ Is the required evidence present, authoritative enough for its role,
  non-conflicting, and complete enough for a permitted action?

Decision
→ Which bounded maintainer action or abstention follows?

Presentation
→ Why, what remains uncertain, what must happen next, and what is not claimed?
```

“Enough evidence” is always relative to one permitted action. It must not become a generic safety score or an unqualified boolean.

## Work sequence

### Step 1 — Walk through the control case in action

Use one behavior-validated supported evidence chain. For each evidence item, record:

- the factual observation;
- the authority it has;
- the decision question it can answer;
- what it cannot establish;
- whether it is decisive, supporting context, missing, or potentially contradictory.

Begin with concrete evidence and output behavior before introducing new internal terminology or source modules.

### Step 2 — Freeze the first decision contract

Define the smallest input and output contracts needed by the B2 decision responsibility.

The input must consume a trusted canonical dependency transition rather than a source-grammar-specific type. Representation provenance may inform evidence interpretation but must not silently create role, usage, or CI-authority claims.

The output must preserve at least:

- one bounded maintainer-action class or abstention;
- evidence-sufficiency or readiness state;
- decisive reasons grounded in evidence;
- unresolved or conflicting questions;
- required targeted checks when applicable;
- inactive investigations and why they were not activated when material;
- uncertainty and claim limits.

Do not select class names or field shapes merely because historical simulation artifacts used them.

### Step 3 — Define outcome meanings and transition boundaries

For every admitted broad outcome, specify:

- what the outcome means operationally;
- minimum evidence needed to permit it;
- conditions that make it too strong;
- conditions that make it too weak;
- the concrete maintainer action;
- what changed evidence requires a new run or different outcome.

The method must distinguish at least:

```text
ordinary review can proceed
specific targeted check is justified
material concern requires investigation or blocks progress
required condition is unresolved and the PR should be deferred
method cannot responsibly decide and must abstain
```

### Step 4 — Define evidence-sufficiency and stopping behavior

Compare the smallest credible state model. It must distinguish materially different situations such as:

- sufficient for one bounded action;
- insufficient with a known resolvable gap;
- unresolved meaning;
- conflicting decision-critical evidence;
- unsupported case.

For every result, identify:

- required conditions evaluated;
- satisfied conditions;
- missing or conflicting conditions;
- whether another investigation stage can discriminate among action-relevant alternatives;
- why investigation stops or continues.

Do not use investigation volume, test count, green CI alone, source availability alone, or dependency-representation support alone as sufficiency.

### Step 5 — Resolve the upstream semantic boundary

Bounded official upstream evidence may exist while its decision-relevant meaning remains unresolved.

Determine:

1. the exact structured upstream claim needed by the first decision method;
2. whether one exact proposed-version release body is sufficient or the crossed-version interval is required;
3. whether a separately bound tagged changelog or release document is required;
4. the simplest credible transparent interpretation baseline;
5. credible semantic alternatives and their costs, failure modes, grounding, replacement path, and proof;
6. whether a consequential model or service would require Ali approval and an ADR.

Reject package-specific phrase tables, exact fixture wording, caller-supplied conclusions, and hidden expected actions as accepted product behavior.

### Step 6 — Exercise the design against contrasts

Before implementation, apply the proposed contract and rules to:

- the S004 sufficient control;
- a supported canonical transition established from a different representation;
- relevant CI insufficient or unresolved;
- exact package or upstream evidence unavailable;
- required upstream meaning unresolved;
- decision-critical evidence conflict;
- a case with a specific justified targeted check;
- an unsupported, malformed, multiple, or conflicting dependency case.

The comparison must show that one method can produce materially different outcomes without hardcoded case identity or source-grammar assumptions.

### Step 7 — Present the method for Ali approval

Explain through concrete cases:

- the request-to-decision flow;
- the meaning of every output state;
- the stopping rule;
- why the method is not an S004 detector;
- what dependency representation does and does not establish;
- what remains manual, unsupported, or deferred;
- the proposed source/module boundaries;
- the minimum test and live-proof plan.

Do not implement a consequential semantic or recommendation method before Ali can challenge the choice and approves the bounded method.

### Step 8 — Implement the approved minimum method

Implementation should preserve focused responsibilities, likely resembling:

```text
dependency evidence intake        trusted canonical package/version transition
release-claim interpretation      bounded attributed upstream claims
evidence-sufficiency evaluation   required conditions, gaps, conflicts, stopping
decision evaluation               bounded action and explanation
CLI orchestration                 execution order and concise presentation
```

Names and file count remain implementation decisions. Do not add layers that lack a distinct proven responsibility.

### Step 9 — Prove controlled behavior

Controlled tests must cover the approved outcome and sufficiency states, evidence grounding, claim limits, and non-hardcoding behavior.

At minimum, prove:

1. S004-like sufficient evidence produces the approved ordinary-review outcome;
2. an equivalent canonical dependency transition from another admitted representation does not change downstream meaning merely because its source differs;
3. unresolved semantic evidence cannot silently produce a favorable recommendation;
4. relevant CI insufficiency or conflict changes the result appropriately;
5. a specific resolvable question can produce a grounded targeted-check result;
6. unsupported, malformed, multiple, or conflicting dependency input produces abstention or unsupported behavior rather than guessing;
7. explanations cite the decisive evidence fields;
8. safety, universal compatibility, and automatic merge are never claimed;
9. acquisition problem states remain distinct through the decision boundary.

Run the nearest complete deterministic suite after narrow tests.

### Step 10 — Integrate and run one live read-only proof

Expose the approved decision result through the existing public command without removing the full evidence report.

The live proof may use a supported case only after deterministic contrasts establish that runtime behavior is not fixture-specific or representation-specific. Record exactly what the live result proves and does not prove.

## Acceptance evidence

This increment passes only when:

- the supported decision question remains aligned with the charter rather than one case;
- outcome meanings, sufficiency states, and stopping conditions are explicit;
- the upstream semantic method and authority boundary are accepted;
- deterministic contrasts prove multiple materially different outcomes and at least two admitted dependency representations normalize into the same decision input contract;
- one public command reaches a bounded recommendation or abstention with traceable reasons;
- missing, unresolved, conflicting, unsupported, malformed, and multiple dependency evidence remain visible;
- no package, version, repository, representation, release wording, or historical maintainer action is encoded as the runtime answer;
- no objective-safety, universal-compatibility, or automatic-merge claim is made;
- no unapproved model, service, persistence layer, agent system, or target mutation is introduced;
- Ali receives a concrete request-to-output walkthrough and ownership practice over the central path.

## Stop line

Stop this plan when one transparent B2 decision method is behavior-validated through controlled contrasts and one safe live read-only command.

Do not continue here into:

- broad support for arbitrary dependency syntax or package ecosystems;
- universal release-note understanding;
- repository-wide usage and dependency-graph reasoning beyond an activated B2 decision need;
- persistence, replay infrastructure, evaluation corpus expansion, or B3/B4 breadth;
- automatic approval, merge, commenting, or target mutation;
- models, agents, queues, or services without a separately admitted limitation and comparison.

## Maintenance

Change this plan only when its decision responsibility, admitted input contract, method sequence, proof obligations, or stop line changes. Do not record progress, selected status, latest commits, blockers, or immediate continuation here.
