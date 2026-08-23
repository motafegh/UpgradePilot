# Group 3 — Audit / Review Mode Plan

**Artifact role:** detailed redesign plan for repository/design/implementation/governance audit procedure  
**Primary existing procedural surface:** `.agents/skills/upgradepilot-repository-audit/SKILL.md`  
**Related owners:** `audits/README.md`, root `AGENTS.md`, `OPERATING_GUIDE.md`, relevant specifications/ADRs/plans/source/tests/evidence

---

## 1. Objective

Turn the existing audit Skill into the reliable, reusable procedure for critical review of UpgradePilot work while preserving:

- read-only default for audit/review requests;
- implementation truth from source/tests/evidence;
- clear separation between requirement/design/implementation defects;
- critical evaluation of necessity and ownership, not only correctness;
- cross-owner consistency when relevant;
- proportional durable audit recording.

The audit Skill should become the main procedural entry point for requests such as:

```text
audit this implementation
audit the recent design/code
review this architecture
critically examine what we just built
audit governance/spec files
check whether this implementation is justified
```

---

## 2. Baseline audit

The existing Skill is already structurally sound. It:

- establishes exact scope;
- loads only needed owners;
- separates governance/control from implementation truth;
- inspects smallest sufficient evidence;
- classifies observations/findings/uncertainty;
- checks duplicate ownership, state leakage, proof collapse, unnecessary machinery, and missing deterministic enforcement;
- remains read-only unless a separate change request exists.

The main weaknesses are not basic correctness but **coverage and integration**:

1. it is not explicitly routed as one of the project operation families from root;
2. it does not explicitly define cross-owner consistency traces such as spec → ADR → plan → source/tests;
3. it does not strongly operationalize the newer `JUST-*` producer → integration → consumer retention discipline;
4. it does not explicitly compose with Learning-by-Doing;
5. it can distinguish governance vs implementation, but design/code audits need a more explicit audit lens for correctness, necessity, ownership, complexity, proof strength, maintainability, and source clarity;
6. it does not explicitly distinguish quick bounded review from formal durable audit depth.

---

## 3. Canonical responsibility boundaries

### Audit Skill owns procedure

The Skill should own:

- audit scoping;
- evidence-loading sequence;
- review lenses;
- cross-owner consistency walk;
- finding classification;
- recommendation/disposition structure;
- when to create/reuse an audit record.

### `audits/README.md` owns durable audit artifact conventions

It continues to own:

- what belongs under `audits/`;
- non-controlling authority boundary;
- compact vs formal record modes;
- naming/finding IDs;
- lifecycle mechanics;
- review discipline.

### Specifications/ADRs/plans/source/tests remain their own owners

Audit findings never become automatic authority.

---

## 4. Target audit flow

The Skill should use a scalable flow:

```text
1. exact audit question and exclusions
2. identify relevant responsibility owners
3. identify implementation/evidence truth sources
4. establish observed behavior independently
5. trace requirement/design/implementation relationship
6. apply relevant audit lenses
7. classify findings and uncertainties
8. identify smallest justified disposition
9. preserve durable audit evidence only when warranted
10. stop without mutation unless explicit change intent also exists
```

For a small local review, several steps may be compact. For cross-responsibility design/code audits, expand only the relevant lenses.

---

## 5. Required audit lenses

### 5.1 Correctness

Ask:

- does implementation behavior match the admitted requirement?
- are failure states/edge cases represented correctly?
- do tests protect the intended contract rather than merely current mechanics?

### 5.2 Necessity and retention

Apply Core `JUST-001` through `JUST-005`.

Do not accept:

```text
it already exists
passing tests use it
a caller consumes it
we spent effort on it
an internal function can be called inconsistently
```

as sufficient retention proof.

### 5.3 End-to-end ownership

For a material field/check/transformation/validation:

```text
proposition
→ normal producer
→ integration/composition boundary
→ earliest sufficient owner
→ downstream consumer
→ independent later boundary, if any
→ concrete risk/proof loss if repetition is removed
→ KEEP / MOVE / NARROW / REMOVE
```

This should be a standard audit tool when cross-layer ownership is questioned, not something the assistant must reconstruct from scattered prose.

### 5.4 Proof strength

Distinguish:

- source fact;
- test-protected behavior;
- one-case evidence;
- specification requirement;
- ADR decision;
- inference/judgment;
- unsupported stronger claim.

### 5.5 Complexity/proportionality

Apply Ceremony Tax to both existing and proposed complexity.

### 5.6 Source clarity/maintainability

Use the compact Source Clarity outcomes and Naming Clarity rules. Do not reward comment volume. Ask whether a competent developer can recover responsibility/data flow/reasoning/proof limits from the repository itself.

### 5.7 Cross-owner consistency

When relevant, inspect:

```text
Charter / admitted product boundary
→ specification
→ ADR/method
→ selected plan
→ source/tests/evidence
```

Do not require every layer to exist. The audit asks whether the layers that do exist agree within their responsibilities.

### 5.8 Learning/ownership

When Audit is running under Learning-by-Doing, explain enough for Ali to participate in the critique. Do not confuse Ali's agreement with technical validation.

---

## 6. Audit depth levels

Avoid creating separate Skills for small/medium/large audits. One Skill should scale.

### Bounded review

Use when one mechanism/file/design question is under review.

Expected output:

```text
observation
→ issue/assessment
→ evidence
→ consequence
→ smallest disposition
```

No durable audit record unless the finding has future value.

### Cross-responsibility audit

Use when multiple owners/modules or a consequential design boundary is under review.

Add:

- explicit owner map;
- producer/integration/consumer trace;
- spec/ADR/plan/source consistency;
- alternatives/tradeoffs;
- proof gaps.

### Governance-system audit

Use when reviewing controls themselves.

Add:

- instruction ownership;
- activation/context cost;
- duplicate canonical ownership;
- deliberate reinforcement quality;
- state leakage;
- deterministic enforcement possibilities;
- AI-client behavior assumptions where relevant.

---

## 7. Audit output discipline

The Skill should prefer concise evidence-backed findings rather than exhaustive commentary.

Suggested finding fields when material:

```text
ID / severity
observation
owner/evidence
why it matters
confidence/uncertainty
recommended disposition
next discriminating check, only if needed
```

Do not require IDs for tiny bounded reviews.

Severity should reflect project impact, not rhetorical intensity.

---

## 8. Durable audit-record behavior

The Skill should explicitly consult `audits/README.md` only when a finding deserves durable preservation.

Rules:

- reuse an existing audit when the same question already has a durable record;
- do not create a record merely because an audit happened;
- compact audit is default when one bounded durable concern exists;
- formal audit only when several findings/cross-owners/follow-ups justify it;
- audit records remain non-controlling;
- promotion to specification/ADR/plan occurs only through the owning process.

---

## 9. Learning-by-Doing composition

Normal substantive audits should still be educational.

The Skill should:

- orient the actual responsibility before criticizing it;
- explain unfamiliar mechanisms only to the depth needed for the audit;
- let Ali challenge or propose hypotheses;
- evaluate Ali's hypothesis and current code by the same evidence standard;
- explicitly correct earlier assistant assumptions if audit evidence disproves them.

Do not turn every audit into a lesson on every file.

---

## 10. Expected modifications

Likely files:

```text
.agents/skills/upgradepilot-repository-audit/SKILL.md
AGENTS.md
OPERATING_GUIDE.md
audits/README.md
tools/agent-governance/cases.json
```

Potential additional reference updates only when required by the changed routing.

No new second audit Skill should be created unless a distinct future responsibility appears that cannot be handled proportionately by the existing one.

---

## 11. Behavioral regression cases to add

### AUDIT — read-only implementation review

Must not mutate repository.

### AUDIT — caller/test retention pressure

Must trace to admitted responsibility instead of retaining by inertia.

### AUDIT — duplicate downstream validation

Must inspect producer → integration → consumer path and identify earliest sufficient owner.

### AUDIT — spec/implementation mismatch

Must classify whether spec, ADR, plan, or source is inconsistent rather than treating documents as proof.

### AUDIT — small observation

Must not create a durable audit artifact unnecessarily.

### AUDIT + Learning-by-Doing

Must explain material reasoning without turning into a monolithic course.

---

## 12. Acceptance criteria

Group 3 passes when:

- root routing reliably selects the existing audit Skill for evaluative work;
- audit remains read-only by default;
- Skill explicitly applies `JUST-*` and end-to-end ownership analysis where relevant;
- cross-owner consistency has a clear bounded procedure;
- durable audit recording remains proportional;
- Learning-by-Doing composition is explicit;
- audit findings distinguish observation, interpretation, uncertainty, and authority;
- at least the critical regression cases above are represented in governance evaluation.

---

## 13. Stop line

Do not implement fixes discovered by an audit inside the same audit request unless separate explicit change intent exists. The redesigned Skill must preserve this boundary even when the likely fix appears obvious.