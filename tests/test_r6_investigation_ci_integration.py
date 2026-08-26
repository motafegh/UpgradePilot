"""R6 regression for the normal public-PR orchestration path.

The test controls external clients but does not inject a selector, declaration, reachability
result, or consumption. ``investigate_public_pull_request`` must acquire exact project/lock
sources and derive R3 -> R4 -> R5 evidence from the admitted workflow definition itself.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock, call, patch

from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import PackageReleaseProblem

_REPOSITORY = "pydantic/pydantic"
_HEAD_SHA = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"

_WORKFLOW = """name: CI
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: uv sync --all-packages --group linting --all-extras
  docs-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: uv sync --all-packages --group docs
      - run: uv run mkdocs build
"""

_LOCK = '''version = 1
revision = 3
[[package]]
name = "pydantic"
source = { editable = "." }
[package.optional-dependencies]
email = [{ name = "email-validator" }]
[package.dev-dependencies]
linting = [{ name = "ruff" }]
docs = [{ name = "mkdocs-llmstxt" }]
[[package]]
name = "email-validator"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "ruff"
version = "0.1.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "mkdocs-llmstxt"
version = "0.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [{ name = "beautifulsoup4" }]
[[package]]
name = "beautifulsoup4"
version = "4.14.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [{ name = "soupsieve" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''


class R6InvestigationCIIntegrationTests(unittest.TestCase):
    def test_normal_investigation_derives_s001_docs_consumption_from_exact_sources(self) -> None:
        identity = PullRequestIdentity(
            repository=_REPOSITORY,
            number=13432,
            title="Bump soupsieve from 2.6 to 2.8.4",
            state="open",
            merged=False,
            author="dependabot[bot]",
            base_ref="main",
            base_sha="6" * 40,
            head_ref="dependabot/uv/soupsieve-2.8.4",
            head_sha=_HEAD_SHA,
            changed_files=1,
        )
        evidence = DependencyChangeSourceEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        )
        dependency = DependencyVersionChange(
            package="soupsieve",
            normalized_package="soupsieve",
            old_version="2.6",
            proposed_version="2.8.4",
            source_evidence=(evidence,),
        )
        context = UvLockDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_SHA,
            normalized_package="soupsieve",
            source_evidence=evidence,
        )

        pull_client = Mock()
        actions_client = Mock()
        repository_client = Mock()
        package_client = Mock()
        release_index_client = Mock()
        upstream_resolver = Mock()
        tag_client = Mock()
        changelog_client = Mock()
        support_drop_evaluator = Mock()

        pull_client.get_pull_request.return_value = identity
        pull_client.get_changed_files.return_value = ()

        run = WorkflowRun(
            run_id=29127613659,
            workflow_id=52902,
            name="CI",
            event="pull_request",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )
        job = WorkflowJob(
            job_id=1,
            run_id=run.run_id,
            name="docs-build",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            steps=(),
        )
        actions_client.get_exact_head_workflow_runs.return_value = (run,)
        actions_client.get_workflow_jobs.return_value = (job,)

        repository_client.get_exact_head_workflow_file.return_value = RepositoryTextFile(
            repository=_REPOSITORY,
            path=".github/workflows/ci.yml",
            revision=_HEAD_SHA,
            content=_WORKFLOW,
        )

        def exact_head_file(_identity: PullRequestIdentity, path: str):
            if path == "pyproject.toml":
                return RepositoryTextFile(
                    repository=_REPOSITORY,
                    path=path,
                    revision=_HEAD_SHA,
                    content='[project]\nname = "pydantic"\n',
                )
            if path == "uv.lock":
                return RepositoryTextFile(
                    repository=_REPOSITORY,
                    path=path,
                    revision=_HEAD_SHA,
                    content=_LOCK,
                )
            raise AssertionError(f"unexpected exact-head file request: {path}")

        repository_client.get_exact_head_text_file.side_effect = exact_head_file
        package_client.get_release.return_value = PackageReleaseProblem(
            state="version_not_found",
            requested_package="soupsieve",
            normalized_package="soupsieve",
            requested_version="2.8.4",
            source_url="https://pypi.org/pypi/soupsieve/2.8.4/json",
            detail="Stop unrelated upstream work in this orchestration regression.",
        )

        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=DependencyChangeAnalysis(
                dependency=dependency,
                source_contexts=(context,),
            ),
        ):
            result = investigate_public_pull_request(
                _REPOSITORY,
                13432,
                pull_client=pull_client,
                actions_client=actions_client,
                repository_client=repository_client,
                package_client=package_client,
                release_index_client=release_index_client,
                upstream_repository_resolver=upstream_resolver,
                tag_client=tag_client,
                changelog_client=changelog_client,
                support_drop_evaluator=support_drop_evaluator,
            )

        coverage = result.ci_coverage_result
        self.assertIsNotNone(coverage)
        assert coverage is not None
        self.assertEqual(coverage.state, "supported_not_correlated")

        consumptions = coverage.workflows[0].consumptions
        docs = next(
            item
            for item in consumptions
            if item.command == "uv sync --all-packages --group docs"
        )
        self.assertEqual(docs.state, "supported")
        self.assertEqual(
            docs.witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )
        lint = next(
            item
            for item in consumptions
            if item.command == "uv sync --all-packages --group linting --all-extras"
        )
        self.assertNotEqual(lint.state, "supported")

        self.assertEqual(
            repository_client.get_exact_head_text_file.call_args_list,
            [call(identity, "pyproject.toml"), call(identity, "uv.lock")],
        )
        repository_client.get_exact_head_workflow_file.assert_called_once_with(identity, run)


if __name__ == "__main__":
    unittest.main()
