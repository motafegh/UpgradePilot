# Governance Redesign — Group 7 Consistency, Validation, and Merge-Readiness Record

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated validation / merge-review evidence  
**Controlling redesign plan:** `plans/governance-spec-governance-enhancement-refinement/07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md`  
**Rule migration input:** `plans/governance-spec-governance-enhancement-refinement/00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`

## 1. Result

Group 7 implementation and cross-system review are complete.

The redesign is **MERGE-REVIEW READY WITH ONE ENVIRONMENTAL EXECUTION PROOF OUTSTANDING**:

- the objective predicates implemented by `tools/agent-governance/governance_doctor.py` were reviewed against the branch through GitHub-backed repository evidence and no failing predicate was found;
- the semantic cross-owner audit found no merge-blocking owner conflict or unauthorized product-semantic change;
- the branch is not merged by this record;
- the actual doctor process was **not executed against a materialized checkout in this runtime** because the available shell cannot resolve `github.com` and the GitHub connector exposes repository files/trees but no repository archive/download-to-shell action.

Therefore this record MUST NOT be quoted as an executed `Governance doctor: PASS`.

The remaining proof is mechanical and explicit:

```text
python tools/agent-governance/governance_doctor.py
```

run from a checkout of this branch in a repository-capable environment.

A merge remains a separate explicit user decision even after that command passes.

## 2. Group-7 modifications

### Exact operation routing

`AGENTS.md` and `OPERATING_GUIDE.md` were reconciled after all five operation Skills became real admitted files.

The final routing surfaces now name exact paths:

```text
.agents/skills/upgradepilot-repository-audit/SKILL.md
.agents/skills/upgradepilot-planning-design/SKILL.md
.agents/skills/upgradepilot-build-implement/SKILL.md
.agents/skills/upgradepilot-learning-by-doing/SKILL.md
.agents/skills/upgradepilot-learning-only/SKILL.md
```

The transitional `when present` / `when available` behavior used during staged Groups 1–6 is no longer part of the final operating model.

### Cross-system behavioral bank

Added:

`tools/agent-governance/consistency_cases.json`

It covers:

- canonical owner versus deliberate reinforcement;
- genuine same-responsibility conflict;
- accepted ADR versus active source drift;
- changing state leaking into generic durable governance indexes;
- compact `SECURITY.md` ownership versus root reinforcement.

### Deterministic governance validation

`tools/agent-governance/governance_doctor.py` was expanded from a shallow structural check into the objective validator described by the redesign plan.

### Harness documentation

`tools/agent-governance/README.md` now distinguishes:

- deterministic structural/schema validation;
- behavioral case contracts;
- semantic Audit responsibility;
- the limits of each proof class.

### Plan-family lifecycle reconciliation

`plans/governance-spec-governance-enhancement-refinement/README.md` no longer incorrectly describes the redesign as merely prospective.

It now records that Groups 1–7 were executed on this branch while preserving two boundaries:

```text
plan-family lifecycle/provenance
!= live project continuation
!= merged-to-main status
```

`MEMORY.md` remains live project-state authority and merge remains separately authorized.

## 3. Deterministic predicate review

### 3.1 Required governance surfaces

GitHub tree/file evidence confirms the configured durable surfaces exist, including:

```text
AGENTS.md
PROJECT_CHARTER.md
OPERATING_GUIDE.md
SECURITY.md
ENVIRONMENT.md
MEMORY.md
docs/README.md
docs/specifications/README.md
docs/architecture/README.md
plans/README.md
audits/README.md
audits/LIFECYCLE.md
audits/{active,scheduled,deferred,absorbed}/README.md
tools/agent-governance/README.md
```

The four registered active specifications also exist:

```text
UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md
UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
```

### 3.2 Root responsibility paths

The branch recursive tree confirms the root responsibility destinations used by `AGENTS.md` exist, including:

```text
plans/
docs/specifications/
docs/architecture/
src/upgradepilot/
tests/
experiments/
tools/
.agents/skills/
audits/
examples/
product-simulation/
working-memory/
learning/
proposals/
archive/
chronicle/
```

The doctor checks only `product-simulation/` root existence; it does not traverse its contents for governance validation.

### 3.3 Skills

All five required operation Skill directories contain `SKILL.md` and their frontmatter `name` values match their directory names:

```text
upgradepilot-repository-audit
upgradepilot-planning-design
upgradepilot-build-implement
upgradepilot-learning-by-doing
upgradepilot-learning-only
```

The root router and Operating Guide now each reference every admitted Skill path explicitly.

### 3.4 Behavioral case banks

Six banks exist:

```text
cases.json
audit_cases.json
planning_cases.json
build_cases.json
learning_only_cases.json
consistency_cases.json
```

Their case-ID families are disjoint:

```text
base bank
→ AUTH / STATE / ROUTE / TRUTH / CTX / SEC / CER / ENV / ART / LBD / SCOPE

audit bank
→ AUDIT-001..007

planning bank
→ PLAN-001..009

build bank
→ BUILD-001..010

learning-only bank
→ LEARN-001..011

consistency bank
→ CONSISTENCY-001..005
```

No cross-bank duplicate ID was found in the reviewed branch content. Each scoped bank uses the same required behavioral fields and allowed criticality vocabulary as the base bank.

The doctor now validates schema/ID structure across all banks. That structural validation does **not** mean an AI client executed every behavioral scenario.

### 3.5 Active normative IDs

The active specification definitions reviewed by the doctor use distinct stable ID families.

Core specification includes project-wide IDs such as:

```text
FLOW / RAW / OBS / SNAP / PROV / STATE / TRUST / FAIL / REP / VERSION
ACT / PROOF / JUST / AUTH / CLAIM / GROUND / CORR / CONTENT
```

Minimum Useful Generality owns:

```text
GEN-001..016
```

Naming Clarity owns:

```text
NAME-001..012
```

The Product Decision Model specification currently expresses its accepted semantics through structured normative prose rather than a conflicting stable-ID table family.

No duplicate active specification table-definition ID was found.

### 3.6 Audit lifecycle

The canonical audit records present at repository root are `AUDIT-001` through `AUDIT-007`.

Lifecycle classification is exclusive and complete at reviewed scope:

```text
ACTIVE
→ AUDIT-001
→ AUDIT-006
→ AUDIT-007

SCHEDULED
→ AUDIT-005

DEFERRED
→ AUDIT-004

ABSORBED
→ AUDIT-002
→ AUDIT-003
```

Lifecycle indexes point back to canonical `audits/*.md` records; the canonical files are not moved between lifecycle directories.

The generic `audits/README.md` no longer owns a dated changing classification list.

### 3.7 Narrow state-leak guard

The known problematic heading form:

```text
Current classification (YYYY-MM-DD)
```

is absent from the generic `plans/README.md` and `audits/README.md` surfaces reviewed for this redesign.

The doctor intentionally checks this narrow known failure rather than attempting to prohibit every legitimate occurrence of words like `current`.

### 3.8 Durable links

The new/changed routing, harness, plan-family, audit-lifecycle, and active-specification references inspected through GitHub resolve to existing repository paths.

The doctor is configured to perform the complete repository-relative link walk over the selected durable governance/specification/index/Skill surfaces once executed from a checkout.

No broken target was found in the connector-backed review.

## 4. Semantic cross-owner audit

### 4.1 Root router ↔ Operating Guide ↔ Skills

**Result: consistent.**

Responsibility split is now:

```text
AGENTS.md
→ authorization
→ operation routing
→ responsibility routing
→ high-salience safeguards

OPERATING_GUIDE.md
→ project-wide Learning-by-Doing / reasoning / evidence / proportionality / Source Clarity outcomes

operation Skills
→ reusable task-specific procedure
```

Every Skill explicitly describes itself as procedural/non-controlling and routes semantic authority back to the relevant owners.

Learning-by-Doing remains a normal overlay, while Audit/Planning/Build remain primary operation procedures and Learning-Only remains a distinct no-product-mutation action boundary.

No Skill was found silently granting itself product/specification/live-state authority.

### 4.2 Canonical owner ↔ deliberate reinforcement

**Result: consistent.**

The most important example is implementation retention:

```text
Core JUST-001..005
→ canonical normative meaning

OPERATING_GUIDE.md
→ project-wide reasoning method

AGENTS.md
→ short high-salience safeguard

Audit / Planning / Build Skills
→ operation-specific application
```

This is deliberate reinforcement, not competing semantic ownership.

The repeated forms preserve the same direction: current code/callers/tests are evidence and migration pressure, not sufficient architectural-retention authority; cross-layer responsibility requires producer → integration/composition → consumer analysis and an earliest sufficient owner.

### 4.3 Charter → specification → ADR → source/tests sample

A real implemented GitHub Actions static-workflow chain was inspected.

`PROJECT_CHARTER.md` requires evidence-backed, uncertainty-aware conclusions and explicitly rejects deriving an update-safety decision from one build/configuration/model fact.

Core specification preserves:

```text
observation != interpretation != evidence quality != decision
plan/specification/ADR != implementation proof
```

The Product Decision Model specification further requires:

```text
static declaration/configuration evidence
!= runtime execution
!= runtime success
```

`ADR-0008-bounded-static-github-actions-workflow-definition.md` chooses a provider-specific static GitHub Actions IR under `upgradepilot.github`, keeps runtime Actions evidence separate, and explicitly refuses to treat static source structure as runtime success.

`src/upgradepilot/github/workflow_definition.py` implements that bounded static IR with PyYAML representation nodes as private parsing machinery, typed provider objects, controlled problems, duplicate-identity handling, and traversal/depth safeguards.

`tests/test_github_workflow_definition.py` protects the method with focused cases for:

- YAML text/node preservation;
- duplicate keys remaining visible before conversion;
- malformed YAML;
- recursive alias/depth/node guards;
- ordered multi-job structure;
- dynamic values;
- typed run/uses steps and bounded provider structure.

No semantic contradiction was found across this chain. The source/test evidence establishes current implemented behavior at the tested scope; the ADR remains the durable method owner and does not claim runtime proof by itself.

### 4.4 Current selected B2 reconciliation ↔ source/tests

The active `B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md` was checked against present exact-file source/test evidence rather than treated as implementation truth.

The plan says the current provider establishes stronger exact-file guarantees than the nominal internal `RepositoryTextFile` contract and that downstream duplication/metadata retention must be reassessed through `JUST-*` and end-to-end ownership.

Current `src/upgradepilot/github/repository.py` confirms the pressure:

- runtime acquisition populates repository/path/revision/blob/byte-count/time/content provenance;
- `RepositoryTextFile` still permits several strong fields to be `None` for older manual fixtures;
- aliases/compatibility surfaces remain visible;
- GitHub boundary performs strict immutable-revision, path, response, size, base64, UTF-8, and identity checks.

`tests/test_exact_commit_repository_files.py` protects the current provider behavior, including immutable revisions, path ownership, exact provenance, typed unavailability, and byte-count agreement.

This is **not an owner conflict**. It is the legitimate plan→implementation delta the selected reconciliation exists to evaluate and change. Tests establish current behavior/regression pressure but do not pre-decide which metadata/checks/aliases must survive R1.

### 4.5 Audit Skill ↔ audits governance/lifecycle

**Result: consistent.**

The Audit Skill is read-only by default and creates a durable audit record only when future review value justifies it.

`audits/README.md` likewise defines audits as non-controlling critical examination, while `audits/LIFECYCLE.md` and lifecycle indexes own active/scheduled/deferred/absorbed classification.

An audit finding does not authorize implementation or become live state.

### 4.6 Planning Skill ↔ plans governance

**Result: consistent.**

`plans/README.md` owns bounded execution/investigation plan semantics and explicitly excludes stable mission, live state, accepted product semantics, durable ADR method, and implementation truth.

The Planning Skill operationalizes that boundary through P0–P3 proportionality and stops before implementation unless Build intent is separately explicit.

No evidence was found that the Skill turns plans into specifications/ADRs or live-state owners.

### 4.7 Build Skill ↔ Source Clarity ↔ Naming ↔ JUST

**Result: consistent.**

`OPERATING_GUIDE.md` owns seven Source Clarity outcomes.

The Build Skill retains the high-value detail from the former 22-rule Source Clarity contract as optional implementation heuristics rather than a universal comment-density checklist.

The Naming Clarity specification remains the canonical naming/terminology owner.

Core `JUST-*` remains the canonical retention owner.

The layers complement rather than compete with each other.

### 4.8 Learning-by-Doing ↔ Learning-Only ↔ B2 package

**Result: consistent.**

Global responsibility remains:

```text
OPERATING_GUIDE.md
→ project-wide teaching/ownership/evidence principles

Learning-by-Doing Skill
→ composition procedure while real project work may progress

Learning-Only Skill
→ explicit mastery route with product mutation paused
```

For the B2 package:

```text
00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
→ package-global learning invariants

00_PLAN_MASTERY_AND_DEPTH_INDEX.md
→ package navigation/depth vocabulary

PLAN_XX*.md + depth maps
→ exact local route/depth

LEARNING_MEMORY.md
→ learning continuity

source/tests/evidence
→ implementation truth

MEMORY.md
→ live product/project continuation
```

The universal Skills do not replace this package architecture.

Package-specific `S001 → S011 → S005`, technology-depth assignments, evidence-strength vocabulary, exact package chunk mechanics, and Career overlay rules remain local.

### 4.9 Security final disposition

**Result: retain compact `SECURITY.md`.**

After operation routing was fully separated, `SECURITY.md` still owns a coherent distinct responsibility:

- secrets/private data;
- untrusted external evidence versus project authority;
- unknown target-code execution boundary;
- exact authorization for external mutation;
- deliberate credential use;
- transport/local-inference trust boundary.

`AGENTS.md` deliberately reinforces only the highest-salience subset.

Deleting `SECURITY.md` now would either scatter this responsibility again or require root/operation Skills to absorb too much security-specific context. Its current compact form is therefore justified.

## 5. Rule-traceability reconciliation

The Group-7 audit found no important matrix rule family silently lost.

### Global promotions

The promoted generic rules have real owners, including:

- fact vs rationale vs engineering judgment vs authority;
- never invent rationale;
- `why is X needed?` reasoning;
- fair checkpoints;
- depth rationale;
- focused source↔test ownership;
- technical independence and assistance fading.

### Skill-local application

Operation-specific rules are applied in the relevant Skills, including:

- overlapping-evidence audit;
- Planning proportionality and owner separation;
- Build pre/post-change model inspection;
- old Source Clarity implementation heuristics;
- Learning-Only package routing/example-state truthfulness.

### Deliberate reinforcement

High-salience `JUST-*`, producer→integration→consumer, no-unknown-code, no-secret, no-external-mutation, proof-class, and action-boundary rules remain shorter than their owners and point back to the appropriate canonical responsibility.

### Package-local rules

The B2/Career-specific route/depth/evidence mechanics identified as `RT-LOC-*` remain local. No evidence was found that they were accidentally converted into universal UpgradePilot requirements.

## 6. Branch-scope review

At the final pre-record comparison, the governance branch was:

```text
55 commits ahead of main
0 commits behind main
```

The diff contains governance controls, operation Skills, redesign plans/provenance, governance evaluation tooling/case banks, and dated validation records.

No `src/upgradepilot/` or `tests/` file is changed by this governance branch relative to `main`.

Therefore the redesign changes **how agents are governed and how operations are routed/validated**; it does not change product runtime behavior in this branch.

## 7. Remaining merge gate

Before merge, preserve this exact distinction:

```text
connector-backed deterministic predicate review
→ no failure found

actual governance_doctor.py process execution
→ NOT RUN in this runtime because checkout materialization is network-blocked
```

Recommended final executable check in a normal repository checkout:

```bash
python tools/agent-governance/governance_doctor.py
```

If it returns non-zero, fix the objective defect before merge.

If it passes, the branch is technically ready for the separate explicit merge decision, subject to one final `main` freshness check.

Do not merge automatically from this validation record.
