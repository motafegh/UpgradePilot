# UpgradePilot Conversation C — Investigation Selection Exploration

**Date opened:** 2026-08-09  
**Status:** Active supporting design exploration; non-controlling; durable accepted conclusions must be consolidated into `2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md` before they become part of the accepted reconciliation model.  
**Parent reconciliation:** `working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`  
**Live-state owner:** `MEMORY.md`  
**Purpose:** Preserve the broad Conversation-C investigation-selection reasoning, terminology, candidate dimensions, pressure-test ideas, and open questions without prematurely converting exploratory design possibilities into runtime architecture or accepted universal rules.

---

## 1. Conversation-C problem

Conversations A and B established that UpgradePilot can reach a materially unresolved applicability proposition without forcing a false positive/negative conclusion.

Representative Kedro/Pluggy anchor:

```text
P6:
Does the exact participating implementation rely on the specific
Pluggy wrapper/result/exception property changed by the transition?

current state:
unresolved because the changed-property → implementation-behavior relation
has not been sufficiently grounded
```

Conversation C asks:

> **What acquisition, analysis, execution, or observation could materially improve UpgradePilot's justified knowledge about a materially unresolved proposition, and which investigation or investigation sequence is worth pursuing?**

Conversation C does not own proposition truth. Its role is to reason about what additional evidence/check is worth acquiring, executing, or recommending, then return new evidence to the proposition-evaluation semantics established in Conversation B.

```text
B:
What proposition state is justified?

C:
What should we investigate to improve that state?
```

---

## 2. Working vocabulary

These distinctions are useful for avoiding a generic `more analysis` concept.

### 2.1 Evidence source

An object/system capable of supplying information, for example:

- exact source file;
- lockfile/resolution metadata;
- CI log;
- runtime environment;
- authoritative documentation;
- tests;
- package metadata;
- issue/maintainer discussion;
- installed-package or entry-point inventory.

### 2.2 Investigation

A deliberate evidence-acquisition, analysis, or execution activity aimed at answering a specific unresolved question.

Example:

```text
inspect all exact kedro.hooks entry points in environment E
```

### 2.3 Check

A more bounded operation with a relatively explicit input/question/result boundary.

Examples:

```text
Does environment E contain plugin X?
```

```text
Does Python 3.8 satisfy >=3.10?
```

### 2.4 Observation/result

The output actually produced by the investigation/check.

Examples:

```text
plugin X is installed
```

```text
ssl.OPENSSL_VERSION = OpenSSL 1.1.1...
```

Current reasoning chain:

```text
SOURCE
↓
INVESTIGATION / CHECK
↓
OBSERVATION
↓
EVIDENCE INTERPRETATION / VALIDATION
↓
PROPOSITION EVALUATION
```

These are working domain distinctions, not accepted runtime types.

---

## 3. Discriminating investigation

A relevant investigation is not automatically a useful investigation.

Buildtest/OpenSSL example:

```text
unresolved proposition:
historical exact target environment used OpenSSL <1.1.1
```

Evidence that the job ran on Perlmutter is relevant to environment context, but it does not discriminate:

```text
OpenSSL <1.1.1
vs
OpenSSL >=1.1.1
```

Recovering exact `ssl.OPENSSL_VERSION` from the relevant frozen/historical environment would be materially more discriminating.

### 3.1 Provisional working definition

> **A discriminating investigation is a bounded, supported evidence-acquisition, analysis, or execution step whose plausible outcomes can materially change the justified state of a specific unresolved proposition or another explicitly identified downstream decision-relevant state.**

Important parts:

- **bounded** — the question/observation target is explicit;
- **supported** — UpgradePilot can legitimately perform/use the check within its authority/safety/evidence boundaries;
- **proposition-specific** — not simply `investigate dependency more`;
- **plausible outcomes** — selection reasoning considers what the check might return before executing it;
- **material change** — interesting information alone is insufficient;
- **justified state** — value means improving evidence-grounded knowledge, not model confidence.

Conceptual outcome shape:

```text
              ┌→ observation O1 → supports/establishes P
investigation ├→ observation O2 → refutes P
              └→ observation O3 → leaves P unresolved
```

---

## 4. Directional discrimination

An investigation need not discriminate equally in positive and negative directions.

Example:

```text
search exact plugin source for @hookimpl(wrapper=True)
```

Finding a concrete affected wrapper may strongly support existence/participation.

Failure to find one may be weak negative evidence if external plugins, generated behavior, dynamic registration, inheritance, or incomplete source coverage remain possible.

Therefore an investigation can have:

```text
strong positive discrimination
+
weak negative discrimination
```

without being useless.

This preserves the Conversation-B asymmetry:

```text
one valid witness may establish existence
but
non-observation does not establish absence without adequate completeness
```

The eventual investigation model should not require every check to be symmetric.

---

## 5. Information gain versus decision-relevant information gain

Useful formal concept: **Value of Information (VoI)** — the value obtained from learning information before deciding what to do.

UpgradePilot should not yet adopt a numerical VoI optimizer, but the concept clarifies an important distinction:

```text
information gain
!=
decision-relevant information gain
```

A large body of dependency history may add substantial information while doing little to resolve the material proposition.

A narrow binary observation may have much higher decision value if it can change applicability or eliminate a required investigation path.

Therefore UpgradePilot should optimize investigation reasoning around **decision-relevant discrimination**, not volume of collected information.

---

## 6. Candidate investigation dimensions

The earlier phrase `smallest sufficiently discriminating investigation` remains useful but is too narrow if interpreted as a single cost ordering. Candidate investigations can differ along multiple dimensions.

Current exploration dimensions include:

### 6.1 Discriminating power

Can plausible results materially change the proposition/decision state?

### 6.2 Scope alignment

Does the investigation examine the exact proposal, revision, dependency version, environment, plugin, runtime context, and proposition that matter?

### 6.3 Authority / evidential quality

Will the resulting observation be admissible evidence for the proposition?

### 6.4 Coverage

How much of the proposition's relevant universe is observed? This is especially important for absence/negative conclusions.

### 6.5 Cost

Potential dimensions include network/API calls, compute, model inference, runtime, developer effort, environment construction, storage, and implementation complexity.

### 6.6 Invasiveness

Distinguish passive reading/inspection from operations that install packages, execute third-party code, modify repository/environment state, run builds, or invoke external services.

### 6.7 Security/safety risk

Examples include untrusted-code execution, credential/data leakage, supply-chain exposure, resource exhaustion, or destructive mutation.

### 6.8 Reproducibility

Can the observation be recreated from exact revisions/environments/commands, or is it a weak one-off observation?

### 6.9 Latency

Interactive PR analysis may value a useful answer available quickly differently from a high-cost reconstruction that takes much longer.

### 6.10 Complementarity

Two individually partial investigations may jointly discriminate much better than either alone.

Example:

```text
source inspection
+
runtime trace
```

Source may establish possible/intended structure while the trace establishes actual execution.

### 6.11 Pruning power

An investigation may have additional value if its result can eliminate downstream branches/checks.

Example:

```text
P3: affected plugin installed?
P6: plugin relies on changed semantics?
```

If P3 is refuted with adequate completeness, deeper P6 semantic investigation may become unnecessary for that path.

Current working relationship:

```text
investigation value
includes
    direct discrimination
    + possible downstream pruning
    + useful complementarity/sequencing
```

No numeric formula, score, or universal ranking is authorized by this exploration.

---

## 7. Investigation sequencing and conditional activation

Investigations may form an adaptive sequence rather than a flat set of competing checks.

Kedro/Pluggy example:

```text
I1 — inspect exact implementation/source/environment presence
↓
enough to close/establish required proposition?
├── yes → stop this branch
└── no
    ↓
I2 — inspect exact tests/docs + bounded semantic comparison
↓
enough?
├── yes → stop this branch
└── no
    ↓
I3 — targeted differential execution if justified
```

### Conditional investigation plan

Working meaning:

> A plan in which later investigations are activated only when earlier results leave material uncertainty that those later checks can still discriminate.

This aligns with existing UpgradePilot conditional activation principles:

```text
do not execute work whose prerequisite question is already resolved
```

Investigation ordering can therefore depend on more than cost. A low-cost structural check with strong pruning potential may rationally precede a more expensive semantic/dynamic investigation.

---

## 8. Exploratory investigation lenses — not fixed taxonomies

Several recurring distinctions may help generate/compare investigations. They are exploration lenses, not accepted exhaustive categories.

### 8.1 Structural investigations

Questions such as:

- does the dependency edge exist?;
- is the plugin installed?;
- is the entry point registered?;
- is the hook reachable?;
- is a platform/version selected?;
- does configuration activate the feature?;
- does the exact resolved graph contain a path?

These are often more mechanically answerable.

### 8.2 Semantic / behavioral investigations

Questions such as:

- does target/plugin behavior rely on the changed contract?;
- will exception/result behavior differ?;
- does generated-artifact meaning change?;
- does target-observable behavior differ across the transition?

These may require semantic interpretation, targeted tests, or differential execution.

Potential recurring strategy to pressure-test:

```text
structural viability first
→ deeper semantic/behavioral investigation only if the path remains viable
```

This is not yet accepted as a universal rule.

### 8.3 Static investigations

Examples:

- source/AST analysis;
- dependency graph;
- metadata/lockfile/config parsing;
- documentation inspection.

Potential strengths: cheap, broad, reproducible, safer.

### 8.4 Dynamic investigations

Examples:

- unit/integration/import tests;
- runtime trace;
- build;
- resolver simulation;
- differential old/new execution.

Potential strengths: direct behavioral discrimination.

Potential weaknesses: narrow coverage, environment sensitivity, cost, nondeterminism, execution risk.

Therefore:

```text
dynamic != universally stronger
static != universally weaker
```

Evidence value remains proposition-relative.

### 8.5 Observational versus interventional investigation

**Observational** — inspect existing facts without deliberately changing the system, e.g. source, logs, lockfiles, environment metadata.

**Interventional** — deliberately alter or execute something to observe consequences, e.g. switch dependency version, run a targeted compatibility probe, alter configuration, construct an experiment.

Because dependency updates are inherently counterfactual, intervention-style checks may be especially valuable in some cases.

---

## 9. Differential testing as a particularly relevant candidate technique

**Differential testing** compares the same target/context/inputs across two versions or implementations and observes differences.

Natural UpgradePilot counterfactual:

```text
same target revision
same relevant environment
same input/context
old dependency
vs
proposed dependency
```

A controlled behavioral difference may provide strong discrimination for an impact candidate.

However differential testing is not magical. Limitations may include:

- affected path not covered by the selected test;
- environment mismatch with real deployment;
- nondeterminism;
- observed difference unrelated to the candidate mechanism;
- setup cost or execution risk.

Therefore it is an important investigation technique to consider, not a universal default.

---

## 10. Investigation generation versus investigation validation/authorization

Conversation B separated semantic interpretation from authority. Conversation C likely needs a similar separation.

A semantic model may be very useful for proposing candidate investigations, for example:

> Inspect the exact plugin wrapper implementation and compare its post-yield result handling against the changed Pluggy semantics.

But model generation alone should not establish that the proposed check is:

- supported by available capabilities;
- correctly scoped;
- authoritative enough to answer the proposition;
- safe to execute;
- non-redundant;
- worth its cost/invasiveness;
- the preferred investigation.

Current conceptual responsibility split:

```text
semantic reasoning
→ propose candidate investigations

capability / evidence / safety reasoning
→ validate feasibility, scope, authority, execution boundary

selection reasoning
→ determine which investigation(s), if any, are worth pursuing
```

No runtime modules/classes are authorized by this exploration.

---

## 11. Investigation-selection failure modes to design against

### 11.1 Evidence hoarding

```text
uncertain
→ collect everything
```

Creates cost/latency/complexity without guaranteed discrimination.

### 11.2 Cheapest-first dogma

Always choosing the cheapest check may repeatedly acquire weak/non-discriminating evidence.

### 11.3 Strongest-test dogma

Always reconstructing full environments or running the strongest imaginable dynamic test wastes effort when simpler evidence is sufficient.

### 11.4 Tool-driven investigation

```text
we have grep
→ grep everything
```

The unresolved proposition should drive tool/check choice, not vice versa.

### 11.5 Fixed checklist investigation

A universal sequence such as:

```text
source → tests → CI → docs
```

is unlikely to match structurally different impact candidates.

### 11.6 Confirmation-seeking

Investigations should not only search for evidence supporting a suspected risk. Useful checks should preserve the ability to refute/close the candidate where possible.

### 11.7 LLM curiosity explosion

Generating dozens of technically interesting questions is not the same as choosing a decision-relevant investigation plan.

### 11.8 Unsafe autonomous execution

Model-proposed package installation, arbitrary code execution, build/test commands, or external interactions require explicit capability/security/isolation boundaries before execution.

### 11.9 Redundant evidence

Repeatedly confirming an already-established proposition adds little value unless it resolves authority/conflict/coverage concerns.

### 11.10 Infinite uncertainty chasing

Some unresolved questions may not justify further investigation. The system must be able to preserve unresolved state rather than treating uncertainty elimination as mandatory.

---

## 12. Two valid Conversation-C outcomes

Conversation C should not define success only as `find another check`.

Two legitimate outcomes are:

```text
A. useful next investigation / investigation sequence identified
```

or:

```text
B. no additional supported investigation is currently justified
```

The second result may occur when available checks are non-discriminating, unsupported, unsafe, disproportionately costly, impossible to scope authoritatively, or incapable of materially changing the downstream decision state.

This does not turn unresolved into not-applicable. It preserves unresolved while explicitly recording that no further justified check is currently available/worth doing.

The later maintainer-facing meaning belongs partly to Conversation D.

---

## 13. Current broad Conversation-C reasoning flow

```text
MATERIAL UNRESOLVED PROPOSITION
        ↓
identify observation(s) that could change its justified state
        ↓
generate candidate investigations/checks
        ↓
for each candidate consider:
    - discrimination direction/power
    - scope alignment
    - authority/evidential quality
    - coverage
    - feasibility/capability support
    - cost
    - latency
    - invasiveness
    - security/safety risk
    - reproducibility
    - pruning power
    - complementarity with other checks
        ↓
consider sequencing / conditional activation
        ↓
choose sufficiently useful investigation / investigation set
OR
justify no-further-check
        ↓
acquire observation/evidence
        ↓
return to Conversation-B proposition evaluation semantics
        ↓
repeat only while material uncertainty and justified useful investigation remain
```

This is a discussion/design model only.

---

## 14. Broader provisional selection principle

The earlier phrase:

> smallest sufficiently discriminating investigation

remains a useful anti-overanalysis heuristic but should not be interpreted as `always choose the single cheapest check`.

A broader provisional principle is:

> **Prefer the lower-cost/lower-risk investigation or conditional investigation sequence that provides sufficient decision-relevant discrimination, while allowing stronger or complementary checks when they materially improve coverage, authority, confidence, causal discrimination, or downstream pruning.**

This wording is provisional. It deliberately avoids fake numeric precision and does not establish a universal ranking algorithm.

---

## 15. Case anchors for continued pressure testing

### 15.1 Kedro / Pluggy

Unresolved semantic-heavy proposition:

```text
Does exact implementation I rely on changed Pluggy wrapper/result/exception semantic X?
```

Candidate investigations may include exact implementation/source/environment inspection, exact tests/docs, bounded semantic comparison, targeted runtime tracing, or old/new differential execution.

Pressure points:

- structural viability versus mechanism alignment;
- semantic ambiguity;
- conditional pruning;
- complementary static/dynamic evidence;
- model-generated investigation proposals versus execution authorization.

### 15.2 Buildtest / OpenSSL

Unresolved environment proposition:

```text
Did the exact historical environment use OpenSSL <1.1.1?
```

Potential investigations:

- exact historical environment/module manifest;
- authentic logged `ssl.OPENSSL_VERSION`;
- reproducible frozen environment reconstruction;
- weaker current docs/source searches for comparison.

Pressure points:

- exact-time/context scope;
- authority;
- strong direct observation versus expensive reconstruction;
- when no authoritative historical evidence remains.

### 15.3 pip-audit / CacheControl / urllib3

Potential unresolved proposition:

```text
Does exact resolution R contain a target-relevant path to the incompatible CacheControl/urllib3 interaction?
```

Potential investigations:

- exact resolved graph construction;
- intermediary version verification;
- exact contract/mechanism verification;
- target-source grep as a deliberately weak comparator.

Pressure points:

- graph completeness;
- structural path existence versus semantic mechanism alignment;
- multi-hop traversal/pruning.

---

## 16. Open Conversation-C questions

The next discussion should explore these without forcing premature implementation:

1. **What exactly counts as sufficient discrimination?**
2. **How should candidate investigations be generated from an unresolved proposition and candidate structure?**
3. **How should UpgradePilot compare investigations without fake numeric precision?**
4. **How should conditional sequences/branching investigation plans be represented conceptually?**
5. **How do cost, latency, security, invasiveness, reproducibility, coverage, authority, and pruning interact?**
6. **When are complementary checks better than a single check?**
7. **When is dynamic/differential execution justified over static/observational evidence?**
8. **When should UpgradePilot deliberately stop and preserve unresolved state?**
9. **What may an LLM propose versus what may it authorize/execute/value?**
10. **How do investigation results re-enter proposition evaluation without Conversation C becoming a second applicability engine?**
11. **Do structural-first / semantic-second patterns survive more cases, or are they merely common heuristics?**
12. **How should multi-hop investigation depth be bounded by decision relevance rather than graph depth alone?**

---

## 17. Current continuation

Continue Conversation C with the next foundational design question:

> **What does “sufficiently discriminating” mean for UpgradePilot in practice—when is an investigation result capable of changing enough of the proposition/decision state that the check is worth doing, and how should that threshold differ between positive evidence, negative evidence, semantic ambiguity, and downstream branch pruning?**

Use Kedro/Pluggy, Buildtest/OpenSSL, and pip-audit as the first pressure-test anchors.

Do not yet create a numerical scoring model, universal investigation taxonomy, planner class, autonomous executor, or fixed source/test/CI checklist.
