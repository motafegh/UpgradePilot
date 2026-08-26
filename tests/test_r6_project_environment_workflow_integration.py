"""R6 regression for workflow-derived R3 -> R4 -> R5 dependency consumption.

The production seam receives workflow text, exact project/lock evidence, and changed-package
context. Tests deliberately do not construct selectors, selection declarations,
reachability results, or CI consumptions.
"""

from __future__ import annotations

import unittest

from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    derive_project_environment_consumptions,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "pydantic/pydantic"
_HEAD_SHA = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"
_CHECKOUT = "actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0"

# Real S001 command spellings from Pydantic's exact PR-head CI definition. The surrounding
# minimal workflow is a deterministic regression carrier; the live verification tool uses
# the complete GitHub-admitted definitions and complete exact uv.lock. Checkout is retained
# because R6 must establish that a repository-relative project command actually refers to
# Pydantic's workspace-root project before composing R3 -> R4/R5 evidence.
_S001_COMMAND_WORKFLOW = f"""name: CI
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - name: Install dependencies
        run: |
          uv sync --all-packages --group linting --all-extras
          uv pip install pip
  docs-build:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - name: Install dependencies
        run: uv sync --all-packages --group docs
      - run: uv run python -c 'import docs.plugins.main'
      - run: PYTHONPATH="$PWD${{PYTHONPATH:+:${{PYTHONPATH}}}}" uv run mkdocs build
  test-memray:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - name: install deps
        run: uv sync --all-packages --group testing-extra
  build-pydantic:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - run: uv sync --only-group build
"""

# Bounded structural snapshot of the S001 facts needed by this regression. It preserves the
# real selected group names and the real positive path. Complete exact-head source is exercised
# by tools/verification/2026-08-25_r6_s001_real_ci_reachability.py through normal production
# acquisition rather than being copied into the unit suite.
_S001_LOCK_SNAPSHOT = '''version = 1
revision = 3

[[package]]
name = "pydantic"
source = { editable = "." }
[package.optional-dependencies]
email = [{ name = "email-validator" }]
timezone = [{ name = "tzdata" }]
[package.dev-dependencies]
linting = [{ name = "pyright" }, { name = "ruff" }]
docs = [{ name = "mkdocs-llmstxt" }]
testing-extra = [{ name = "cloudpickle" }]
build = [{ name = "build" }, { name = "twine" }]
docs-upload = [{ name = "beautifulsoup4" }]

[[package]]
name = "pyright"
version = "1.1.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "ruff"
version = "0.1.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "email-validator"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "tzdata"
version = "2026.1"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "cloudpickle"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "build"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "twine"
version = "6.0.0"
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


def _workflow(content: str = _S001_COMMAND_WORKFLOW) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=".github/workflows/ci.yml",
        revision=_HEAD_SHA,
        content=content,
    )


def _project() -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path="pyproject.toml",
        revision=_HEAD_SHA,
        content='[project]\nname = "pydantic"\n',
    )


def _lock() -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path="uv.lock",
        revision=_HEAD_SHA,
        content=_S001_LOCK_SNAPSHOT,
    )


def _source(lock_file: RepositoryTextFile) -> WorkflowProjectEnvironmentSource:
    evidence = DependencyChangeSourceEvidence(
        path="uv.lock",
        file_format="uv_lock",
        extraction_method="exact_base_head_files",
    )
    return WorkflowProjectEnvironmentSource(
        context=UvLockDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_SHA,
            normalized_package="soupsieve",
            source_evidence=evidence,
        ),
        project_file=_project(),
        lock_file=lock_file,
    )


def _dependency(source: WorkflowProjectEnvironmentSource) -> DependencyVersionChange:
    return DependencyVersionChange(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
        source_evidence=(source.context.source_evidence,),
    )


class R6ProjectEnvironmentWorkflowIntegrationTests(unittest.TestCase):
    def test_real_s001_command_set_derives_docs_witness_without_prebuilt_semantic_evidence(self) -> None:
        consumptions = derive_project_environment_consumptions(
            _workflow(),
            sources=(_source(_lock()),),
            normalized_package="soupsieve",
        )

        by_command = {item.command: item for item in consumptions}
        docs = by_command["uv sync --all-packages --group docs"]
        self.assertEqual(docs.state, "supported")
        self.assertEqual(docs.reachability_kind, "transitive")
        self.assertEqual(
            docs.witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )

        lint = by_command[
            "uv sync --all-packages --group linting --all-extras\nuv pip install pip"
        ]
        self.assertNotEqual(lint.state, "supported")
        self.assertNotEqual(
            by_command["uv sync --all-packages --group testing-extra"].state,
            "supported",
        )
        self.assertNotEqual(by_command["uv sync --only-group build"].state, "supported")

    def test_all_supported_matching_commands_are_preserved(self) -> None:
        workflow = f"""name: CI
jobs:
  docs-a:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - run: uv sync --all-packages --group docs
  docs-b:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - run: uv sync --all-packages --group docs --group docs-upload
"""

        consumptions = derive_project_environment_consumptions(
            _workflow(workflow),
            sources=(_source(_lock()),),
            normalized_package="soupsieve",
        )

        supported = tuple(item for item in consumptions if item.state == "supported")
        self.assertEqual(len(supported), 2)
        self.assertEqual(
            {item.command for item in supported},
            {
                "uv sync --all-packages --group docs",
                "uv sync --all-packages --group docs --group docs-upload",
            },
        )
        self.assertTrue(all(item.witness_path[-1] == "soupsieve" for item in supported))

    def test_dynamic_uv_group_remains_unresolved_through_ci_coverage(self) -> None:
        workflow = f"""name: CI
jobs:
  dynamic-selection:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        group: [docs]
    steps:
      - uses: {_CHECKOUT}
      - run: uv sync --group "${{{{ matrix.group }}}}"
"""
        definition = _workflow(workflow)
        source = _source(_lock())

        consumptions = derive_project_environment_consumptions(
            definition,
            sources=(source,),
            normalized_package="soupsieve",
        )

        self.assertEqual(len(consumptions), 1)
        unresolved = consumptions[0]
        self.assertEqual(unresolved.state, "unresolved")
        self.assertEqual(unresolved.reason, "project_environment_selection_unresolved")
        self.assertEqual(unresolved.command, 'uv sync --group "${{ matrix.group }}"')
        self.assertEqual(unresolved.source_path, "uv.lock")

        run = WorkflowRun(
            run_id=1,
            workflow_id=2,
            name="CI",
            event="pull_request",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )
        job = WorkflowJob(
            job_id=3,
            run_id=run.run_id,
            name="dynamic-selection",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            steps=(),
        )
        coverage = evaluate_dependency_ci_coverage(
            _dependency(source),
            (
                WorkflowDependencyExerciseInput(
                    run=run,
                    jobs=(job,),
                    definition=definition,
                    external_consumptions=consumptions,
                ),
            ),
            source_contexts=(source.context,),
        )

        self.assertEqual(coverage.state, "unresolved")
        workflow_result = coverage.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "unresolved")
        self.assertEqual(
            workflow_result.consumption_reason,
            "project_environment_selection_unresolved",
        )
        self.assertNotEqual(
            workflow_result.consumption_reason,
            "static_dependency_consumption_not_observed",
        )

    def test_third_party_root_checkout_does_not_rebind_external_uv_selection_to_pydantic_lock(self) -> None:
        workflow = f"""name: Third party tests
jobs:
  test-pandera:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Pandera
        uses: {_CHECKOUT}
        with:
          repository: unionai-oss/pandera
          persist-credentials: false
      - name: Checkout Pydantic
        uses: {_CHECKOUT}
        with:
          path: pydantic-latest
          persist-credentials: false
      - name: Install Pandera dependencies
        run: |
          pip install uv
          uv sync --no-progress --extra pandas --extra fastapi --extra pandas --group dev --group testing --group docs
          uv pip uninstall --system pydantic pydantic-core
          uv pip install --system -e ./pydantic-latest
"""

        consumptions = derive_project_environment_consumptions(
            _workflow(workflow),
            sources=(_source(_lock()),),
            normalized_package="soupsieve",
        )

        self.assertEqual(consumptions, ())

    def test_dynamic_checkout_path_preserves_provenance_uncertainty(self) -> None:
        workflow = f"""name: CI
jobs:
  dynamic-checkout:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        checkout-path: [src]
    steps:
      - uses: {_CHECKOUT}
        with:
          path: "${{{{ matrix.checkout-path }}}}"
      - run: uv sync --group docs
"""

        consumptions = derive_project_environment_consumptions(
            _workflow(workflow),
            sources=(_source(_lock()),),
            normalized_package="soupsieve",
        )

        self.assertEqual(len(consumptions), 1)
        unresolved = consumptions[0]
        self.assertEqual(unresolved.state, "unresolved")
        self.assertEqual(
            unresolved.reason,
            "project_environment_checkout_provenance_unresolved",
        )
        self.assertEqual(unresolved.command, "uv sync --group docs")

    def test_other_repository_subpath_does_not_displace_current_root_checkout(self) -> None:
        workflow = f"""name: CI
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: {_CHECKOUT}
      - uses: {_CHECKOUT}
        with:
          repository: example/other
          path: vendor/other
      - run: uv sync --all-packages --group docs
"""

        consumptions = derive_project_environment_consumptions(
            _workflow(workflow),
            sources=(_source(_lock()),),
            normalized_package="soupsieve",
        )

        self.assertEqual(len(consumptions), 1)
        self.assertEqual(consumptions[0].state, "supported")
        self.assertEqual(
            consumptions[0].witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )


if __name__ == "__main__":
    unittest.main()
