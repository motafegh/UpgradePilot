# S001 — Pydantic Soup Sieve 2.6 → 2.8.4

**Scenario status:** Complete, with retrospective execution retrofit  
**Primary decision:** Merge after normal maintainer review  
**Current reading order:** This file → [`EXECUTION_TRACE.md`](EXECUTION_TRACE.md) → [`CASE.md`](CASE.md)

## Files

| File | Purpose |
|---|---|
| [`EXECUTION_TRACE.md`](EXECUTION_TRACE.md) | How the investigation was actually performed: tool operations, reasons, expected and actual outputs, failures, superseded paths, and continuation |
| [`CASE.md`](CASE.md) | Complete evidence model, investigation findings, decision, maintainer report, variants, diagrams, and product implications |

The two records are complementary:

```text
EXECUTION_TRACE.md
= how we reached the result

CASE.md
= what the completed result means
```

## Retrospective status

S001 was originally investigated and then documented as a complete case. It was not maintained progressively from the first lookup.

`EXECUTION_TRACE.md` is therefore a best-effort retrospective reconstruction based on retained tool history and source references. It explicitly marks details that cannot be reconstructed exactly and does not invent a perfect transcript.

Future scenarios must use their active `CASE.md` as the progressive primary record while work occurs.

## Correction notice

Fresh verification of the two official Soup Sieve advisory pages during the execution-log retrofit exposed an error in `CASE.md`.

### Corrected facts

| Topic | Original S001 statement | Current corrected statement |
|---|---|---|
| Advisory publication date | July 9, 2026 | June 1, 2026 |
| Timing relative to PR | one day before the July 10 PR | more than one month before the PR |
| Dependabot trigger inference | strongly suggested security-triggered update | security trigger is plausible but unresolved from public evidence |

The official pages still identify:

- affected versions: `<=2.8.3`;
- patched versions: `>=2.8.4`;
- severity: High;
- relevant attack paths: user-supplied selector strings reaching Soup Sieve compilation or Beautiful Soup selector APIs.

### Decision effect

The correction does **not** change the primary recommendation because the recommendation did not require proof of why Dependabot opened the PR.

The retained decision reasons remain:

- 2.6 is advisory-affected and 2.8.4 is patched;
- target Python support is compatible with the new package floor;
- the package is transitive documentation tooling;
- the proposed official artifact identity matches;
- relevant exact-head documentation CI succeeded;
- no material target-specific conflict was found;
- uncertainty and final human authority remain explicit.

## Current authority within S001

Until `CASE.md` receives a focused full rewrite, use this order for the corrected interpretation:

1. this correction notice controls the advisory date and trigger-inference wording;
2. `EXECUTION_TRACE.md` controls how the investigation was operationally performed;
3. `CASE.md` controls the remaining final evidence model, report, variants, and product implications.

The incorrect original statements are preserved as superseded history rather than silently erased.

## Main lesson from the retrofit

The execution trace exposed both a process gap and a factual error:

```text
clean retrospective result without exact operation lineage
→ harder to audit where a claim came from
→ incorrect timing inference survives into the final report
```

The corrected standard is:

```text
current state
→ selected method and reason
→ exact operation
→ expected output
→ material/raw output
→ interpretation
→ outcome
→ next action and reason
```

This chain must be recorded progressively for S002 onward.
