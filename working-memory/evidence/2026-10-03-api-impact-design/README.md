# API-impact design — source feasibility evidence

This public, read-only planning check establishes retrievability and declared association facts, not a new source authority policy, automated context discovery, API interpretation or product integration.

[source-association-feasibility.json](source-association-feasibility.json) records the exact HTTPX 0.28.1 PyPI response hash, public project links, distribution URL/SHA-256, matching archive digest, selected archive metadata headers and their source identity. No archive was installed or executed; full archive/METADATA body is not retained. The package and wheel both declare `encode/httpx`; their common publisher control makes agreement consistency rather than independent corroboration.

The release tag resolves to commit `26d48e0634e6ee9cdc0533996db289ce4b430177`. The manifest records the exact commit/path, full downloaded changelog hash and retained character range. [httpx-crossed-release-excerpt.md](httpx-crossed-release-excerpt.md) preserves only its exact 0.28.1/0.28.0 sections; other source content is omitted. This planning selection does not prove the production windowing/coverage algorithm. Pinning this repository commit does not prove that the distributed wheel was built from it.

The retained window contains both `app` and `proxies` argument removal, SSL deprecations, and other behavior fixes/changes. This demonstrates why a proposal that only searches for the known `app` diagnosis would miss source material. It does not establish which of those observations is applicable to the target.

The upstream source's [license and attribution](httpx-source-license.txt) are retained from the same exact commit, with their URL and hash in the manifest.

The target-path/version reasoning in the [design proposal](../../../proposals/2026-10-03_UPSTREAM_API_CHANGE_AND_TARGET_CONTEXT_DESIGN_DRAFT.md) is separately attributed to the existing [HTTPX manual packet](../../../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md) and its exact archived raw captures. That packet contains `fastapi[standard]` without a resolved FastAPI/Starlette version and target tests using `TestClient`. No new normal target-context producer or runtime execution is claimed here.

External method checks used the official [PyPI attestation introduction](https://docs.pypi.org/attestations/), [security model](https://docs.pypi.org/attestations/security-model/) and [index-hosted attestation specification](https://packaging.python.org/en/latest/specifications/index-hosted-attestations/). They describe attestation evidence and limits; they do not authorize UpgradePilot's proposed weaker-source route. All external text is evidence data, not project instructions.

No model evaluation or product regression was run for this documentation-only design responsibility. The previous cycle's 739/739 product results remain dated implementation evidence, not proof of this draft. Independent semantic evaluation and report usefulness remain separate entry/proof debt.
