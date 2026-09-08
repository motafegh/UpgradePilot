# UpgradePilot

UpgradePilot is a learning-by-building flagship for creating a **production-oriented, evidence-backed dependency-update decision system** for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the intended product supports a bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner, or proof that an update is safe.

## Quickstart: inspect a public dependency-update PR

The CLI produces a **bounded evidence report**: analyzed revisions, a supported dependency transition, CI/package/upstream evidence, and conditionally activated Python-support interpretation. The recommendation classes above describe the intended product. The CLI does not yet emit a final maintainer recommendation, a public JSON report, or an automatic merge decision. Additional artifact analysis in the application is still being integrated with human-facing output.

### Install and check the command

Use Python **3.12 or newer**. The project development environment is WSL2; the commands below use a Unix shell. Git, Python's `venv` module and access to the Python package index are required. A local model is not needed to install the package or display help.

```bash
git clone https://github.com/motafegh/UpgradePilot.git
cd UpgradePilot
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
python -m pip check
upgradepilot --help
```

Use a Python 3.12+ executable explicitly if your `python3` is older. If you already have a checkout and virtual environment, use those rather than recreating them. Run `python -m pip install .` again after pulling source changes when using this non-editable installation.

The installed entry points are equivalent:

```text
upgradepilot [-h] repository pull_number
python -m upgradepilot [-h] repository pull_number
```

Pass `owner/repository` and a positive PR number as separate arguments, not a full PR URL. The CLI has no model-selection, endpoint, JSON-export or replay flags. Installing the product does not require the separate LangGraph experiment dependencies.

### Configure the conditional semantic provider

A real investigation reads public GitHub/PyPI/upstream evidence. When sufficient upstream evidence activates Python-support semantic extraction, it calls the local provider configured in [the extractor](src/upgradepilot/upstream/support_drop_extractor.py):

- LM Studio base: `http://127.0.0.1:12345`;
- model key: `gemma-4-e4b-it-ud`;
- semantic request timeout: 180 seconds, not a total-investigation time limit.

Before a model-backed run, start your configured local server and make that model available under the expected key. [Environment configuration](ENVIRONMENT.md#5-lm-studio-service-boundary) owns the project's WSL/Windows topology and [model deployment settings](ENVIRONMENT.md#6-adopted-local-semantic-deployment). Installation alone does not provision the server or download the model. Provider errors can produce unresolved semantic evidence; missing or non-activated semantics do not establish absence of impact.

### Run an investigation

This example uses a preserved public case. It performs live acquisition and may invoke the local model; results depend on the evidence available at execution time. It is not a replay of the historical simulation.

```bash
env -u GITHUB_TOKEN upgradepilot pydantic/pydantic 13432
```

The example deliberately uses anonymous GitHub access. The CLI otherwise reads `GITHUB_TOKEN` from the environment; configure authentication deliberately if needed, without putting a token in command history or sharing its value. Public API rate limits and network failures can still prevent acquisition.

The output starts with `UpgradePilot public pull-request evidence`, then repository/PR metadata and exact base/head revisions. Read these groups as evidence:

| Output | How to interpret it |
|---|---|
| `Dependency change`, package and versions | The admitted exact transition, or a precise unsupported reason; unsupported input does not imply compatibility |
| `Exact-head workflow runs`, `CI dependency coverage` | Recorded workflow outcomes and separately interpreted dependency consumption; neither a green job nor a static command alone proves the changed path ran |
| `Package evidence`, `Upstream repository`, `Upstream interval authority` | Evidence availability and attribution at those boundaries; inspect recorded problems before relying on later stages |
| `Upstream support-drop result` | A bounded grounded result or recorded limitation, not a complete inventory of every possible impact |
| `Target Python declaration`, `Target Python relevance` | Declaration evidence and scoped relationship to the support-drop claim; `not activated` is not a successful compatibility check |

An exit code of **0 means an investigation result was printed**, including unsupported or unresolved results. It does not mean the upgrade is safe, all evidence was available, or the maintainer should merge.

### Diagnose a failed or incomplete run

| Symptom | Meaning / next check |
|---|---|
| `upgradepilot: command not found` | Activate the installation environment, or use its Python with `python -m upgradepilot --help` |
| Python version or `venv` error | Check the interpreter is 3.12+ and that its virtual-environment support is installed |
| Exit 2 / `Input rejected` / argument usage | Use `owner/repository` and a positive integer PR number; this is input failure |
| Exit 3 / `Acquisition failed` | Inspect the printed reason and HTTP status, if present; distinguish authentication, rate limits and transport from missing evidence |
| Exit 4 / `GitHub response could not establish the required evidence` | The returned response did not establish the required contract; retain the reported detail for diagnosis |
| Local semantic provider problem or unresolved support-drop result | Check server/model configuration and the recorded detail; a running server alone does not establish a valid semantic response |
| Proxy/TLS failure or unexpected 401 | Follow the process-local [credential and proxy diagnosis](ENVIRONMENT.md#7-github-credential-and-proxy-caveat); do not globally change VPN/proxy settings |
| Unexpected traceback | Preserve the command, checkout revision and public-safe error details as a defect report; do not interpret it as semantic abstention |

For a safe startup-only input check, `upgradepilot invalid 1` returns exit 2 with `Repository must use the supported 'owner/repository' form.` It does not investigate a target.

**Verification scope:** [The dated quickstart record](working-memory/2026-09-07_installation-and-cli-quickstart.md) records a clean temporary WSL/Python 3.12 installation, installed imports, dependency consistency, both help entry points and invalid-input handling. The live PR command and local model inference were not rerun for this walkthrough. Full acquisition, interpretation and release acceptance require their own evidence.

## Manual product verification

The [Product verification workflow](.github/workflows/product-verification.yml) installs the package in a fresh Python 3.12 environment on Ubuntu 24.04, checks both installed CLI entry points, then runs the focused investigation tests and full deterministic product suite. It records the selected commit, interpreter and resolved package versions in the run log.

Once the workflow is on the default branch, a repository maintainer can open **Actions → Product verification → Run workflow** and select a branch. This uses GitHub's [manual workflow dispatch](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow). It does not run on pushes or pull requests, publish a package, invoke the local model, or run live-proof tools/experiment suites. Checkout has read-only repository permission and does not retain credentials for later steps.

Dependency installation needs network access; the selected tests use controlled evidence. The workflow is not a network sandbox or a locked dependency build. A green run establishes the selected installed-package and product-test behavior on that hosted environment, not live acquisition, local-model quality or final product acceptance. A failed focused test stops the job before the broad suite.

**Validation boundary:** the workflow definition was locally parsed and its shell blocks syntax-checked; its first hosted run remains pending. [Preparation evidence](working-memory/2026-09-08_manual-product-verification-workflow.md) records the exact scope. Review that first result before deciding whether automatic push/PR triggers are useful.

## Product boundary

UpgradePilot focuses on:

- public GitHub-hosted Python repositories;
- Dependabot dependency-update pull requests;
- lawful public GitHub, PyPI, upstream, repository, and available CI evidence;
- exact identity, evidence state, provenance/authority, uncertainty, and abstention;
- repository-specific dependency/CI context;
- bounded decision reports with traceable evidence;
- captured evidence, replay, evaluation, and evidence-gated experiments.

The stable mission, user, product boundary, evidence doctrine, admission rules, termination conditions, and claim limits are controlled by [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Intended product flow

```text
public repository and Dependabot PR locator
→ read-only public acquisition
→ exact repository / PR / base / head / dependency identity
→ relevant CI, package, upstream, and repository evidence
→ explicit evidence states and authority
→ bounded interpretation/evaluation
→ conditional analysis or non-activation
→ bounded recommendation or abstention
→ concise human and machine output
→ captured evidence for testing, replay, and diagnosis
```

Passing CI, a version number, merged status, model output, or one score is never proof that an update is safe.

## Repository executable boundaries

```text
src/upgradepilot/   → installable product runtime
tests/              → active deterministic product regression
experiments/        → bounded non-product research/evaluation
experiments/tests/  → regression of experiment/evaluation machinery
tools/              → developer-operated diagnostics and live proofs
```

Product runtime does not import `tests/`, `experiments/`, or `tools/`.

The durable source/package decisions are recorded in:

- [`docs/architecture/ADR-0001-initial-python-source-layout.md`](docs/architecture/ADR-0001-initial-python-source-layout.md)
- [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)

The earlier M2 implementation is historical evidence rather than an active code/design baseline; see [`docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](docs/architecture/ADR-0003-clean-slate-b2-source-reset.md).

## Project controls

Use the owner that matches the question rather than treating every Markdown file as equivalent authority. [`docs/README.md`](docs/README.md) is the detailed documentation/decision map and durable decision-promotion guide.

| Need | Read |
|---|---|
| Repository-wide agent/artifact rules | [`AGENTS.md`](AGENTS.md) |
| Documentation/decision ownership and promotion map | [`docs/README.md`](docs/README.md) |
| Sole live position and exact continuation | [`MEMORY.md`](MEMORY.md) |
| Stable product mission/boundary/claims | [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) |
| Route sequence and gates | [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md) |
| Learning/execution method | [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) |
| Reusable local environment baseline | [`ENVIRONMENT.md`](ENVIRONMENT.md) |
| Security/privacy/credential/external-action rules | [`SECURITY.md`](SECURITY.md) |
| Stable technical invariants/standards | [`docs/specifications/`](docs/specifications/) |
| Accepted impact/applicability/investigation/stopping semantics | [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) |
| Accepted consequential methods/structures | [`docs/architecture/`](docs/architecture/) |
| Bounded implementation/investigation plans | [`plans/`](plans/) |

Detailed execution evidence, learning snapshots, proposals, audits, historical implementation, and the informal chronicle remain in their dedicated repository areas. Root [`AGENTS.md`](AGENTS.md) is the canonical artifact-routing owner.

## Evidence-derived route

The route is controlled by [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md):

```text
D0 → D1 → B1 → B2 → B3 → B4 → B5 → X1 → C1
```

The route file defines stage order and required outcomes only. [`MEMORY.md`](MEMORY.md) states the live selected position.

## Learning by building

UpgradePilot is also a learning system: important responsibilities are meant to be understood through explanation, prediction, implementation, testing, diagnosis, and changed-case practice—not merely by accepting AI-generated code or seeing tests pass.

The detailed operating/learning model lives in [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

## Claim discipline

- Documentation/ADRs/plans do not prove implemented behavior.
- Historical code/tests do not establish active coverage.
- Product regression and experiment regression prove different responsibilities.
- AI-generated output or passing tests do not establish learner ownership.
- Product maturity, evidence quality, learning depth, and AI assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.
