# Candidate-Discovery Coverage Pressure Test 01

**Date:** 2026-08-12  
**Status:** Completed bounded pressure test; non-controlling discovery/evaluation evidence  
**Branch:** `agent/product-simulation-case-screening-02`  
**Starting shared revision:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Owned question

The mature-system horizon now distinguishes **candidate-discovery coverage** from proposition evidence coverage and candidate path-model coverage.

This pressure test asks one narrower question:

> **When can discovery legitimately stop after finding one or more real impact candidates, and what prevents “we found a valid candidate” from silently becoming “we found all material candidates”?**

The goal is not to define a universal discovery algorithm, completeness score, mechanism taxonomy, or runtime schema.

## 2. Why existing cases are enough for this first pass

No new numbered scenario is needed for the first test because existing untouched real cases already expose the coverage problem from different directions:

- **S008** — one real OpenCV transition was intentionally bounded to artifact serviceability even though the crossed release interval may contain other API/security/runtime mechanisms;
- **S009** — one real pandas transition establishes a repository reproducibility/provenance inconsistency while technical compatibility/numerical-change questions remain separate;
- **grouped Dependabot control from Screening 04** — one PR may contain many dependency transitions, so candidate-discovery scope cannot be inferred from PR identity alone.

This is a reuse-first pressure test of the newly explicit mature-system responsibility.

## 3. Baseline hypothesis under attack

A tempting but unsafe discovery shortcut is:

```text
find one plausible mechanism
→ formulate one candidate
→ evaluate candidate thoroughly
→ stop
→ treat transition as fully understood
```

This shortcut confuses:

```text
CANDIDATE-SPECIFIC DEPTH
with
TRANSITION-LEVEL DISCOVERY BREADTH
```

A candidate may be deeply and correctly evaluated while discovery of other material candidate mechanisms remains incomplete.

## 4. S008 — local stopping can be correct while global discovery remains open

S008 owns the bounded OpenCV artifact transition:

```text
old release:
compatible CPython-3.6 Linux wheel exists

→

new release:
no compatible CPython-3.6 binary wheel
+ source distribution remains
```

For that owned proposition, exact package artifact evidence was sufficient. A native source build was correctly pruned because it would answer a different downstream proposition.

That stopping decision remains correct.

But S008 also explicitly refuses to claim that the full OpenCV transition has no other material mechanisms. Its stop boundary excludes, among other things, general API/security compatibility analysis.

Therefore:

```text
S008 QUESTION RESOLVED
!=
OPEN-CV TRANSITION DISCOVERY COMPLETE
```

and:

```text
candidate investigation stop
!=
candidate discovery stop for a broader transition-level conclusion
```

### S008 pressure-test result

**Supported:** discovery coverage must be relative to the conclusion being attempted.

If the owned conclusion is only:

> Did the Python-3.6 wheel path disappear while source fallback remained?

then S008 has enough discovery because the question already names the mechanism.

If the attempted conclusion were:

> This OpenCV update creates no other material target-relevant technical concerns.

then S008 provides no basis for that stronger claim.

## 5. S009 — context discovery and technical candidate discovery are different coverage planes

S009 establishes, from exact repository state:

```text
repository declares publication reproduction environment
+
publication pin changes
+
reproduction/provenance wording is not reconciled
→
repository-context inconsistency
```

S009 correctly leaves separate questions unresolved:

```text
Does pandas 3 technically break the analysis?
Do published numerical results change?
```

This gives a different coverage failure mode.

A product that discovers the repository-context inconsistency must not conclude:

```text
important context found
→ no technical candidate discovery needed
```

Likewise, a product that finds one technical pandas candidate must not conclude:

```text
technical candidate found
→ repository-purpose/provenance context irrelevant
```

These are different responsibilities.

### S009 pressure-test result

**Supported:** mature synthesis may need both:

```text
TECHNICAL CANDIDATE-DISCOVERY COVERAGE
+
REPOSITORY-CONTEXT DISCOVERY / COVERAGE
```

without forcing context findings into technical impact candidates.

This does **not** justify naming two permanent runtime coverage types today. It establishes a responsibility separation that future design must preserve.

## 6. Grouped Dependabot proposals — establish the discovery unit before measuring coverage

Screening 04 retained a real grouped Dependabot proposal as an input-boundary control.

Its key lesson is:

```text
one PR
!=
one dependency transition
!=
one impact candidate
```

Candidate-discovery coverage is meaningless until the object being covered is explicit.

For a grouped proposal:

```text
PR
├── dependency transition A
│   ├── candidate A1
│   └── candidate A2
├── dependency transition B
│   └── candidate B1
└── dependency transition C
    ├── candidate C1
    └── ...
```

The current B2 input boundary avoids this complexity by admitting one Python dependency transition. That bounded input is valuable because it keeps candidate-discovery coverage scoped to a known transition.

### Grouped-update pressure-test result

**Supported:** discovery coverage requires an explicit **coverage object** before any completeness statement is meaningful.

## 7. Durable findings

### DCF-01 — Finding one valid candidate does not establish discovery completeness

```text
candidate C discovered and grounded
!=
all material candidates discovered
```

Applicability depth for C cannot substitute for breadth across the transition.

### DCF-02 — Candidate-discovery stopping is conclusion-relative

A local candidate question may stop even while broader transition discovery remains open.

```text
owned narrow conclusion resolved
→ local stop can be justified

broader transition-level conclusion attempted
→ additional discovery-coverage argument may be required
```

### DCF-03 — Discovery coverage needs an explicit coverage object

At minimum the evaluator must know whether it is reasoning about:

- one exact dependency transition;
- one mechanism-specific candidate;
- a grouped proposal containing several transitions;
- a broader repository-context synthesis.

Do not infer the coverage object from PR identity alone.

### DCF-04 — Discovery coverage is not universal completeness

The product does not need to prove:

> No conceivable mechanism exists anywhere.

A realistic bounded statement is closer to:

```text
for conclusion Q,
using admitted discovery inputs/channels S,
under exact transition/target/revision context C,
no additional material candidate was justified,
subject to explicit blind spots B
```

This is a **claim-relative coverage argument**, not universal completeness.

### DCF-05 — Candidate discovery should preserve its blind spots

If a discovery pass used only:

- release-note semantic evidence;

it should not silently imply equivalent coverage of:

- package artifact inventories;
- dependency constraints;
- target configuration;
- repository-purpose contracts;
- runtime behavior;
- platform-specific evidence.

The relevant missing channel may or may not matter for the current conclusion, but its absence must not disappear.

### DCF-06 — More discovery channels are not automatically better

This pressure test does not authorize exhaustive acquisition.

```text
possible additional channel
!=
material additional discovery value
```

Discovery should still be bounded by the conclusion being attempted, expected discriminating value, supported evidence boundaries, and cost/complexity.

### DCF-07 — Context findings should not be forced into technical candidate coverage

S009 shows that repository purpose/provenance can be materially decision-relevant while remaining outside mechanism-specific technical applicability.

Therefore a mature system may eventually need to preserve:

```text
technical candidate set
+
material repository-context findings
+
coverage limitations for both
```

without pretending they are one taxonomy.

## 8. Candidate-discovery stop conditions — pressure-tested shape

A discovery pass may legitimately stop when one of these bounded conditions holds.

### 8.1 Narrow owned mechanism already specified

Example: S008's artifact-serviceability question.

```text
mechanism already named
+ evidence sufficient for that mechanism
+ no broader transition-level conclusion attempted
→ stop
```

### 8.2 Additional discovery cannot change the currently owned conclusion

If conclusion Q is already bounded and additional candidate mechanisms cannot change Q, further discovery is unnecessary for Q.

This must not be reused later as evidence for a broader claim.

### 8.3 Supported discovery boundary exhausted but broader claim remains unjustified

```text
material channels attempted
+ no additional justified candidate found
+ known blind spots remain
→ bounded insufficient-discovery / limited-coverage conclusion
```

The correct result may be explicit uncertainty rather than continued searching forever.

### 8.4 Broader synthesis requires more breadth

If later reasoning attempts something like:

```text
no material target-relevant concern remains
```

then candidate-discovery coverage becomes a first-class prerequisite and cannot be inherited merely from candidate-level applicability results.

## 9. What this does NOT justify

Do not derive from this pressure test:

- a numeric candidate-recall score;
- a `DiscoveryCoverageState` enum;
- a universal mechanism checklist;
- exhaustive release-note traversal;
- one scanner per mechanism family;
- a mandatory graph;
- an LLM assertion that discovery is complete;
- automatic reopening of Conversation D;
- automatic implementation work on candidate discovery.

The mature-system horizon correctly leaves the method open.

## 10. Evaluation implications

Future candidate-discovery evaluation should test more than whether one expected candidate was found.

Useful questions include:

1. **Missed-mechanism test** — did discovery stop after the first obvious candidate while another independently material candidate existed?
2. **Unsupported-candidate test** — did broader semantic search invent candidates without sufficient upstream evidence?
3. **Target-filter test** — did discovery distinguish upstream mechanism existence from target relevance/applicability?
4. **Channel-ablation test** — what disappears if package metadata, target context, or semantic upstream evidence is removed?
5. **Context-separation test** — can the system preserve a material repository-context finding without misclassifying it as technical applicability?
6. **Stopping test** — can discovery stop with an explicit limited-coverage state instead of searching indefinitely?

A serious recall-style benchmark would require an independently curated oracle or evaluator isolation. Existing cases can pressure-test hypotheses but should not be treated as complete oracle labels merely because they helped shape the model.

## 11. Next real-world evidence need

The strongest next external-validity case would be an untouched real single-dependency Python Dependabot transition where **at least two independently grounded technical mechanisms are both plausibly target-relevant**.

Ideal shape:

```text
one exact dependency transition
→ mechanism A grounded from one evidence channel
→ mechanism B grounded from a materially different evidence channel
→ both have real target relationships
→ one is easier/more obvious than the other
```

That would test whether discovery:

- finds only the obvious candidate;
- splits materially different mechanisms correctly;
- avoids double-counting semantically equivalent mechanisms;
- preserves unresolved applicability without suppressing further discovery.

This may become S010 only if a real candidate earns admission. Screening should remain low-friction.

## 12. Main-thread handoff decision

**No immediate architecture correction is required.**

Current `main` already recognizes candidate-discovery coverage as a distinct open epistemic problem. This pressure test strengthens and bounds that responsibility rather than contradicting current implementation.

A handoff becomes useful if later real-world evidence shows one of the following:

- the current horizon's discovery/coverage separation is insufficient;
- a repeated cross-case representation emerges;
- an implementation claims transition-level completeness without a coverage argument;
- a concrete discovery method needs an evaluation contract.

## 13. Stop

Pressure Test 01 is complete.

The next productive move is **new real-world screening for the two-mechanism shape**, not more conceptual elaboration of candidate-discovery coverage.