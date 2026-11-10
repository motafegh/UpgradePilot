# Build static dependency version request extraction

Ali explicitly selected Build after walking through the OmniMatch YAML, the coverage gap, and the distinction between a version request and a loaded version. Main and origin/main reconciled at `6006cefb`. The [selected plan](../plans/CI_REQUESTED_DEPENDENCY_VERSION_REPORT_PLAN.md#build-sequence-and-proof) sequences extraction before Workspace and report integration. This increment uses the existing parser and proves the first static fact through the CI workflow inspector. The ongoing exchange already covered the continuity and pre-B understanding gates for this scope. The next increment introduces a native versioning responsibility.

UP-SKILL:upgradepilot-build-implement. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

The dependency owner distinguishes positional requirements from option operands. The CI owner attaches workflow revision, job, step and command location. The existing coverage result still answers whether the workflow consumed the changed source. Test the real OmniMatch commands and pedido-service contrast, plus bounded argument-role controls.

## Implementation and evidence

The [dependency operation owner](../src/upgradepilot/dependency/package_manager_operation.py) admits a single unambiguous literal `==` request for the selected normalized package. It walks pip operands in order, consumes a recognized file option and its value, and then interprets actual positional requirement tokens. Dynamic, unfamiliar or contradictory command forms stay outside admission. Equivalent repeated pins retain the first observed token. The [workflow inspector](../src/upgradepilot/ci/workflow_commands.py) applies this only to a sole ordinary top-level parsed command and binds the declaration to its exact workflow revision, job, step and command byte span. It shares the operation parsing with direct requirements inspection for the same step. The existing standalone file-consumption caller can still use the default parse path.

Three anonymous exact-head Contents reads returned HTTP 200. The unchanged OmniMatch workflows matched the previously recorded file digests. The two paths produce one request apiece, with no consumption or invocation facts. The exact pedido-service CI workflow provides a reverse contrast.

| Workflow | Static result |
| --- | --- |
| OmniMatch `.github/workflows/passwordless.yml` | `signatures`, step index 2, command order 0, bytes 0–256. Positional `httpx==0.27.0`. |
| OmniMatch `.github/workflows/advanced-models.yml` | `cpu-models`, step index 4, command order 0, bytes 0–309. Positional `httpx==0.27.0` remains distinct from the separate `-r` operand. |
| pedido-service `.github/workflows/ci.yml` at `4dbfdac075d4c13889f39fae44432593e6b4c78a` | Supported use of `requirements-dev.txt`. No inline HTTPX request. Source SHA-256 `95a7df000a927f3be56b58dfb9b997c2450d200790e674ebeaf4fae5a45458ab`. |

Four focused controls cover exact proposed and other versions, option operands, malformed or ambiguous forms, a skipped YAML step, shell conditional/chaining refusal, normalized extras, duplicate pins, unrelated packages, and one shared pip parse for both fact types. The skipped-step control records the literal declaration while leaving execution outside its scope. One hundred four focused tests passed across parser, CI coverage and runtime, orchestration, topology and reporting. Governance doctor passed.

The declared request now exists at the static CI result boundary. The next increment is to carry the fact through CI coverage and native versioned capture, then the report. The historical codec, saved report, execution and action contracts remain at their earlier evidence horizon. No target code ran.

```text
A0/A1/A2 — Current source and accepted first increment reconciled with the ongoing onboarding.
B — Implemented literal argument-role admission and workflow provenance.
Verification — Three real workflow checks and 104 focused tests passed.
D/E — Explain positional requirement versus file option and static evidence versus execution. Resume at native transport and report integration.
C — Producer decisions, controls, real-case proof, and handoff preserved.
```
