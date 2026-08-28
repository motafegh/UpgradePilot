# Sixth Agent Skill Admission — Deferred

**Recorded:** 2026-08-28  
**Branch:** `agent/skills-governance-evolution-2026-08-27`  
**Status:** Decision recorded; no sixth operation Skill admitted

## Decision

UpgradePilot will keep the current five admitted operation Skills for now:

- `upgradepilot-repository-audit`
- `upgradepilot-planning-design`
- `upgradepilot-build-implement`
- `upgradepilot-learning-by-doing`
- `upgradepilot-learning-only`

No sixth operation Skill is admitted in this governance/Skills evolution cycle.

This is a deferral, not a permanent ban on future Skills. Reassess after the project has progressed further or when repeated real work provides stronger evidence that the current five-Skill system is no longer sufficient.

## Reason

The sixth-Skill review considered the strongest current candidates:

- dedicated Debug/Diagnose;
- Agent Governance / Skill Maintenance;
- Research/Evidence.

None currently clears the admission bar.

### Debug/Diagnose

Debugging is recurring, but the project already has a project-wide debugging method in `OPERATING_GUIDE.md`, Build-specific debugging procedure, and behavioral coverage for both diagnosis-only and diagnosis-during-Build paths. A separate Skill would currently add routing overlap without demonstrated behavioral benefit.

### Agent Governance / Skill Maintenance

Agent governance is a recurring subject area, but it is not a distinct action mode. Governance work still routes cleanly by action:

```text
audit governance
→ Repository Audit

design governance changes
→ Planning / Design

implement approved governance changes
→ Build / Implement
```

The Audit Skill and its conditional governance-system probes already cover governance-specific evaluation needs.

### Research/Evidence

Research and evidence gathering are useful recurring activities, but they normally serve another responsibility such as Audit, Planning, product-simulation/discovery, or Learning. Current evidence does not show a separate operation boundary that would justify another routing surface.

## Admission bar for a future sixth Skill

Reopen the question only when real project evidence supports the following:

1. the responsibility recurs often enough to justify durable procedure;
2. agents materially struggle with it under the current Skills and owners;
3. the procedure is genuinely distinct from Audit, Planning, Build, Learning-by-Doing, and Learning-Only;
4. a conditional reference, existing owner, deterministic tool, or behavioral case cannot solve the problem more simply;
5. the new Skill would reduce ambiguity or context cost rather than create routing collisions;
6. activation and completion boundaries can be stated clearly and tested behaviorally.

Useful evidence for reopening may include repeated misrouting, repeated procedural failure, or an existing Skill/Guide becoming bloated because a stable independent workflow can no longer be kept proportionate through progressive disclosure.

## Current disposition

```text
five admitted operation Skills
→ retain

sixth Skill
→ deferred

future reconsideration
→ evidence-triggered, not schedule-triggered
```

Do not create a sixth Skill merely because an external Skill catalog contains a useful technique or because a recurring subject has a recognizable name.

## Relationship to existing governance

This record does not create a new controlling rule. Root `AGENTS.md` remains the operation-routing owner and already identifies the five admitted Skills. The existing Skill-admission and persistent-agent-machinery principles remain controlling. The Agent Skills evolution proposal remains the design/provenance source for the candidate analysis.

## Next boundary

The final whole-branch audit is intentionally **not started by this record**. Its scope and additional review points will be set after Ali provides the requested points for that audit.