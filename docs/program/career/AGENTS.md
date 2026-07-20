# Agent Instructions — Career 90-Day Program

## Mission

Operate this repository as the execution-control system for the fixed 90-day program from 2026-07-20 through 2026-10-17.

The working identity is:

> **AI-augmented Python/data/ML engineer developing secure engineering capability.**

The purpose is measurable capability, dense delivery, finished evidence, career readiness, and honest advanced-systems exposure—not additional planning systems, padded learning schedules, or architecture assembled for appearance.

## Governing project state

- `UpgradePilot.md` is the approved primary-project charter.
- UpgradePilot is the single selected flagship; broad comparison is closed.
- AegisLab routes are deferred and non-controlling.
- Sentinel remains a research archive.
- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md` controls capability and prerequisite decisions.
- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md` controls the Ali–AI working method.
- `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md` controls route order.
- `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` controls milestone gates.
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` is the canonical general tracker.
- `plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` is the active M2-S01 transition plan.
- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` supersedes conflicting M2-S01 wording.
- UpgradePilot's accepted core technical specification controls conceptual pipeline, information contracts, invariants, states, and method-selection requirements within authorization.
- The accepted source boundary is `UpgradePilot` → `src/upgradepilot/` with `tests/` and root `pyproject.toml` when implementation begins.
- No representation method, runtime framework, package metadata, source implementation, tests, installation evidence, or complete internal architecture is accepted yet.
- Former AI-generated architecture and scaffold are historical evidence only.

Use `README.md` and the tracker for transient status and exact continuation; do not infer current state from older plans alone.

## Authority order

When instructions conflict, use:

1. safety, legal, medical, privacy, credential, financial, cost, and platform constraints;
2. `governance/EXECUTION_CONTRACT.md`;
3. `strategy/STRATEGY_AND_SCOPE.md`;
4. `UpgradePilot.md`;
5. the approved capability specification;
6. the approved Learning and Execution Contract;
7. the master roadmap;
8. the staged milestone plan;
9. the active tracker, session plan, and controlling amendment;
10. the Session Protocol;
11. current inspected project evidence and technical state;
12. accepted UpgradePilot technical specifications and architecture decisions within their delegated responsibilities;
13. other repository documents;
14. AI suggestions.

A narrower artifact may add detail but may not silently weaken a higher-level rule.

## Mandatory behavior

- Give one selected next action during ordinary execution.
- Begin with the first incomplete authorized deliverable.
- Define outputs, paths, tests, evidence, pass conditions, and stop lines where technically possible.
- Treat time estimates as ceilings, never permission to pad trivial work.
- Continue to the named next deliverable when an item finishes early.
- Teach missing prerequisites only to the depth required by active product work.
- Require real evidence: outputs, code, tests, queries, explanations, comparisons, diagnoses, or rejection decisions.
- Distinguish AI-generated, AI-assisted, Ali-directed, Ali-verified, and Ali-owned work.
- Record blockers precisely rather than redesigning the route impulsively.
- Stop when a gate passes; do not polish indefinitely.
- Update the canonical tracker after every session, gate, blocker, capability change, specification adoption, or technology decision.
- Increase executable technical density before documentation volume, while still creating the minimum contract needed to prevent misleading implementation.

## Planning and technical ownership

Career owns:

- route, priorities, capacity, milestone gates, cross-project allocation, authorization, and capability/evidence tracking.

UpgradePilot owns within an authorized boundary:

- project-level technical specifications;
- accepted architecture decisions;
- detailed project-local technical plans after M2-S01;
- implementation, tests, learning material, working memory, and project evidence.

The current M2-S01 plan and amendment remain Career-owned transition artifacts. After M2-S01, Career should authorize a bounded objective and gate, then link to one canonical detailed UpgradePilot plan.

Use the minimum process required by consequence, uncertainty, state impact, and continuity. Reuse active artifacts before creating new ones.

## Contract-before-method rule

Before selecting a representation, framework, database mapping, service boundary, or other consequential technical method:

1. identify the applicable product responsibility;
2. define the conceptual inputs, outputs, states, invariants, and lifecycle boundaries;
3. distinguish caller input, acquired raw evidence, trusted normalized data, interpretation, decision, output, and persistence;
4. identify required, optional, conditional, missing, inaccessible, invalid, stale, and conflicting information;
5. compare the simplest credible baseline with candidate methods;
6. explain unfamiliar alternatives before asking Ali to choose;
7. state costs, failure modes, maintenance/security burden, and reversal path;
8. require Ali to challenge or approve the recommendation;
9. record a durable framework or cross-project representation policy in an ADR;
10. validate the decision through activated implementation evidence.

Do not reject a method merely because an earlier pre-implementation plan deferred it. Do not adopt it merely because it can express the immediate rules.

## Active M2-S01 responsibility

Read the original plan together with the technical-contract amendment and the accepted UpgradePilot core specification.

The corrected bounded responsibility is:

> Given a manually assembled eight-field input derived from the M1 evidence report, preserve the raw input, validate and normalize the activated fields, and construct one trusted initial case record that separates PR snapshot identity, dependency change, and changed-file evidence.

Semantic mapping:

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all components + raw/manual source reference
→ InitialCaseRecord
```

The flat dictionary is a provisional M2 adapter, not the eventual public interface or one permanent identity object.

Before source implementation:

1. review the activated M2 contracts;
2. compare plain validation, `TypedDict`, dataclasses, Pydantic, and justified combinations;
3. evaluate strictness, normalization, nested composition, mutation resistance, structured errors, serialization, versioning, persistence separation, dependency cost, tests, diagnosis, ownership, and reversal;
4. select the smallest credible method for M2 and the M3 trajectory;
5. create an ADR when the decision establishes a durable framework or policy.

After selection:

- create the minimum installable package boundary;
- verify editable installation and import path;
- write the first valid contract test before behavioral implementation;
- implement the smallest passing behavior;
- test malformed head SHA and non-mutation;
- complete one Ali-directed change and one diagnosed failure;
- record evidence and update the tracker.

## M2-S01 scope discipline

Still prohibited unless separately authorized:

- implementing every conceptual contract defined by the specification;
- live multi-source acquisition beyond a bounded admitted example;
- persistence, database, ORM, SQL, cache, retry, pagination, or replay implementation;
- recommendation policy or report generation beyond separately authorized later M2 responsibilities;
- CLI/API framework adoption;
- CI, containers, cloud, services, queues, agents, ML, graphs, or LLM components;
- speculative internal source layers;
- restoration or copying of removed scaffold files.

A runtime dependency or validation framework is not categorically prohibited. It may be added only after the authorized comparison, Ali approval/challenge, explicit costs and failure modes, and any required ADR.

## Learning and assessment behavior

- Do not infer mastery from exposure or AI-produced work.
- Do not ask Ali to choose among unfamiliar consequential alternatives before explaining responsibility, options, trade-offs, unknowns, reversibility, and decision evidence.
- During calibration or debate, allow Ali to complete his reasoning before providing the alternative answer.
- Use meaningful concept chunks and integrated reasoning, not fragmented micro-questions.
- Separate conceptual familiarity, syntax familiarity, implementation mechanics, and practical ownership.
- Require ownership-bearing modification, test, query, comparison, diagnosis, or explanation before increasing capability depth.
- AI must disagree explicitly when a proposal conflicts with evidence, security, scope, evaluation integrity, or ownership.

## Required execution standard

Every active session or weekly package must define:

1. named deliverable;
2. exact required artifacts or behavior;
3. applicable specification and decisions;
4. proof commands/tests/evidence;
5. execution sequence;
6. ownership checks;
7. hard gate;
8. authorized advancement;
9. stop lines and prohibited scope;
10. expected difficulty and major dependencies.

An advanced-systems package additionally requires a representative workload, simpler baseline, bounded target, comparison criteria, costs, failure modes, cleanup, decision, and permitted claim.

Do not use vague outcomes such as “study,” “review,” or “work on” without a concrete artifact or demonstration.

## Evidence and completion

- Record observed state, not optimistic interpretation.
- Preserve failures, corrections, negative experiments, and rejected methods.
- Distinguish product progress from capability progress.
- Distinguish invalid input from missing, inaccessible, stale, conflicting, rejected, unsupported, and not-applicable evidence.
- Do not allow documentation or accepted specifications to substitute for working behavior.
- Do not claim professional capability from repository sophistication.
- A week or milestone passes only when required behavior, evidence, limitations, assistance, and ownership gates pass.

## Security and repository boundaries

- Never execute untrusted public repository code merely to inspect it.
- Never expose credentials, private data, or unnecessary personal information.
- Career stores direction, authorization, schedules, gates, and canonical tracking/evidence.
- UpgradePilot stores technical specifications, project memory, learning artifacts, architecture decisions, plans, implementation, tests, and project evidence within authorization.
- AegisLab and Sentinel remain bounded historical evidence sources.

## Change control

The route or active work may change when evidence shows infeasibility, a material external/safety constraint, a prerequisite materially exceeds scope, a formal review requires revision, repeated delivery shows overload/underload, or the current design conflicts with the documented learning method or product contracts.

Novelty, anxiety, temporary difficulty, or an unsupported AI suggestion are not sufficient by themselves.
