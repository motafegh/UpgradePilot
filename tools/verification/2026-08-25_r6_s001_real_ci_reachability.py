"""Verify R6 against the real S001 PR through the normal production investigation path.

This verification intentionally supplies only the public PR locator. Production acquisition
must discover the changed SoupSieve context, exact pull-request workflow definitions,
pyproject root evidence, and exact head uv.lock. No group, declaration, reachability result,
or consumption is injected here.

Run from the repository root with network access and optional GITHUB_TOKEN:

    python tools/verification/2026-08-25_r6_s001_real_ci_reachability.py

The script is a verification surface, not the R6 integration seam. Product orchestration is
owned by ``upgradepilot.investigation`` and ``upgradepilot.ci.workflow_commands``.
"""

from __future__ import annotations

import os

from upgradepilot.investigation import investigate_public_pull_request

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_DOCS_COMMAND = "uv sync --all-packages --group docs"
_CODSPEED_COMMAND = "uv sync --all-packages --group testing-extra --extra email --frozen"
_EXPECTED_WITNESS = ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve")


def main() -> None:
    result = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=os.getenv("GITHUB_TOKEN"),
    )

    dependency = result.dependency_result
    if getattr(dependency, "normalized_package", None) != "soupsieve":
        raise AssertionError("S001 production analysis did not establish SoupSieve as the change")

    coverage = result.ci_coverage_result
    if coverage is None:
        raise AssertionError("S001 production path did not produce CI coverage evidence")

    consumptions = tuple(
        consumption
        for workflow in coverage.workflows
        for consumption in workflow.consumptions
        if consumption.mechanism == "project_environment"
    )
    supported = tuple(item for item in consumptions if item.state == "supported")

    docs_matches = tuple(item for item in supported if item.command == _DOCS_COMMAND)
    if not docs_matches:
        raise AssertionError("real S001 docs command was not derived as supported consumption")
    if not any(item.witness_path == _EXPECTED_WITNESS for item in docs_matches):
        raise AssertionError("real S001 docs command did not preserve the expected lock witness")

    # Preserve every supported match. The verifier does not assert that docs is uniquely
    # relevant; it prints the complete set so additional real supported commands remain
    # visible rather than being discarded by a first-match policy.
    if not all(item.witness_path and item.witness_path[-1] == "soupsieve" for item in supported):
        raise AssertionError("a supported project-environment consumption lacks a SoupSieve witness")

    codspeed = tuple(item for item in consumptions if item.command == _CODSPEED_COMMAND)
    if codspeed and any(item.state == "supported" for item in codspeed):
        raise AssertionError("real codspeed selector unexpectedly became positive for SoupSieve")

    print(f"dependency: {dependency.normalized_package}")  # type: ignore[union-attr]
    print(f"coverage: {coverage.state}")
    for item in supported:
        print(
            "supported: "
            f"{item.workflow_path} | {item.job_key} | {item.command!r} | "
            f"{' -> '.join(item.witness_path)}"
        )
    for item in codspeed:
        print(f"codspeed selector: {item.state} | {item.reason}")


if __name__ == "__main__":
    main()
