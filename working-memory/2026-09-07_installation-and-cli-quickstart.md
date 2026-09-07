# Installation and CLI quickstart

**Date:** 2026-09-07
**Responsibility:** First-user installation and evidence-report walkthrough, parallel to separately owned product implementation.
**Source snapshot:** `dfffdbfe64d7003ac71a6b2002bb1fe7e4769472`.

## Audit and bounded change

The README described the intended recommendation system and controls but had no install/run walkthrough. Traced `pyproject.toml`, CLI argument/error/rendering paths, package entry points, application activation and the local semantic provider. Added a README quickstart using the existing owners; no separate guide directory, new runtime API, configuration flags or implementation plan was introduced.

The quickstart distinguishes intended recommendations from the implemented evidence report; names the Python requirement and real entry points; describes conditional local-model configuration; provides a live public example with anonymous GitHub access; explains output and failure meanings; and links to the existing environment owner for deployment/proxy details. The intended-product-flow heading is now explicit.

## Installation verification

Read the environment owner before checking execution topology. The available shell reported WSL2 (`6.18.33.2-microsoft-standard-WSL2`) and the project interpreter reported Python 3.12.3. This permitted a separate installation smoke, not resumption or closure of the other workstream's deliberately deferred product-validation obligation.

Copied only package source, README and pyproject metadata into `/tmp/upgradepilot-quickstart-joad_cwy/source`, excluding existing egg-info and bytecode. Created a fresh virtual environment under that temporary directory. Installed the copied package normally with public PyPI dependency resolution; no dependencies were inherited from the project environment. Used process-local removal of ambient pip configuration/index variables, Python path overrides, GitHub token and proxy variables. No secret values were printed.

Verified from outside the project checkout:

| Check | Result |
|---|---|
| Normal local-package installation with dependency resolution | Exit 0 |
| Installed `upgradepilot` import | Resolves under the temporary virtual environment's `site-packages` |
| `python -m pip check` | Exit 0, no broken requirements |
| Installed `upgradepilot --help` | Exit 0, `repository pull_number` and help option |
| Installed `python -m upgradepilot --help` | Exit 0, equivalent help |
| Installed `upgradepilot invalid 1` | Exit 2, `Input rejected: Repository must use the supported 'owner/repository' form.` |

Transient install log and captured check results remain at `install.log` and `verification.json` in that temporary directory; their retention is not a product guarantee. The copy approach avoids package-build artifacts or virtual-environment changes in the shared checkout.

## Proof limits

No public target investigation, model inference, model provisioning, workflow execution, product regression suite or experiment suite ran. No live response transcript is fabricated for the README example. Installation/startup success does not prove semantic correctness, usability, reproducible dependency resolution across time or supported operation on other Python/OS versions. Python 3.12+ is the declared package requirement; this run tested 3.12.3 only.

## Learning cycle

A — DONE: oriented around first-user needs and installed/startup versus live-investigation proof.
B — DONE: source audit, isolated package installation and README walkthrough.
C — DONE: recorded commands, outcomes, boundaries and remaining live verification here; live project memory unchanged.
D — explanation supplied; learner review pending, no ownership inferred.
E — next useful check is a first-user walkthrough or separately admitted live invocation; no further infrastructure is needed merely to document startup.

The key distinction for review is that exit 0 means a result was printed, not that the update is compatible. Unsupported or unresolved findings can be successful executions of the evidence-report interface.

Provenance: `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-working-memory`.
