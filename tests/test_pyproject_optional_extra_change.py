"""Test the bounded exact ``pyproject.toml`` optional-extra transition rule."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeProblem
from upgradepilot.dependency.pyproject import (
    ExtractedPyprojectOptionalExtraChange,
    PyprojectOptionalExtraNoChange,
    extract_pyproject_optional_extra_change,
)
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_BASE_SHA = "a" * 40
_HEAD_SHA = "b" * 40


def _exact(content: str, *, revision: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path="pyproject.toml",
        revision=revision,
        content=content,
    )


def _project(*, mlx_numpy: str, dev_pytest: str = "pytest>=8", extra_tail: str = "") -> str:
    return f'''[project]
name = "demo"

dependencies = ["numpy>=1.24"]

[project.optional-dependencies]
dev = ["{dev_pytest}"]
mlx = [
  "mlx-metal==0.30.4; sys_platform == 'darwin'",
  "{mlx_numpy}",
  "soundfile>=0.12",
]
{extra_tail}
'''


class PyprojectOptionalExtraChangeTests(unittest.TestCase):
    def test_s011_shape_establishes_exact_pin_change_and_extra(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                _project(mlx_numpy="numpy==1.26.4"),
                revision=_BASE_SHA,
            ),
            _exact(
                _project(mlx_numpy="numpy==2.4.6"),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, ExtractedPyprojectOptionalExtraChange)
        assert isinstance(result, ExtractedPyprojectOptionalExtraChange)
        self.assertEqual(result.extra, "mlx")
        self.assertEqual(result.change.package, "numpy")
        self.assertEqual(result.change.normalized_package, "numpy")
        self.assertEqual(result.change.old_version, "1.26.4")
        self.assertEqual(result.change.proposed_version, "2.4.6")
        evidence = result.change.source_evidence
        self.assertEqual(evidence.path, "pyproject.toml")
        self.assertEqual(evidence.file_format, "pyproject_optional_extra")
        self.assertEqual(evidence.extraction_method, "exact_base_head_files")

    def test_unchanged_general_and_marker_requirements_are_allowed(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                _project(mlx_numpy="Num_Py==1.0"),
                revision=_BASE_SHA,
            ),
            _exact(
                _project(mlx_numpy="num-py==2.0"),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, ExtractedPyprojectOptionalExtraChange)
        assert isinstance(result, ExtractedPyprojectOptionalExtraChange)
        self.assertEqual(result.change.normalized_package, "num-py")
        self.assertEqual(result.extra, "mlx")

    def test_unchanged_optional_surface_is_neutral_for_dependency_analysis(self) -> None:
        base = _project(mlx_numpy="numpy==1.26.4")
        head = base.replace('name = "demo"', 'name = "demo-renamed"')

        result = extract_pyproject_optional_extra_change(
            _exact(base, revision=_BASE_SHA),
            _exact(head, revision=_HEAD_SHA),
        )

        self.assertIsInstance(result, PyprojectOptionalExtraNoChange)

    def test_two_optional_dependency_changes_abstain(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                _project(mlx_numpy="numpy==1.0", dev_pytest="pytest==8.0"),
                revision=_BASE_SHA,
            ),
            _exact(
                _project(mlx_numpy="numpy==2.0", dev_pytest="pytest==9.0"),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")

    def test_added_extra_is_outside_first_rule(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                _project(mlx_numpy="numpy==1.0"),
                revision=_BASE_SHA,
            ),
            _exact(
                _project(
                    mlx_numpy="numpy==2.0",
                    extra_tail='docs = ["mkdocs==1.6"]',
                ),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(
            result.reason,
            "unsupported_pyproject_optional_dependency_change",
        )

    def test_non_exact_changed_specifier_is_not_promoted_to_version_change(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                _project(mlx_numpy="numpy>=1.0"),
                revision=_BASE_SHA,
            ),
            _exact(
                _project(mlx_numpy="numpy>=2.0"),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "unsupported_requirement_format")

    def test_marker_change_is_not_treated_as_only_a_version_change(self) -> None:
        base = '''[project]
name = "demo"
[project.optional-dependencies]
mlx = ["numpy==1.0; python_version < '3.12'"]
'''
        head = '''[project]
name = "demo"
[project.optional-dependencies]
mlx = ["numpy==2.0; python_version >= '3.12'"]
'''
        result = extract_pyproject_optional_extra_change(
            _exact(base, revision=_BASE_SHA),
            _exact(head, revision=_HEAD_SHA),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(
            result.reason,
            "unsupported_pyproject_optional_dependency_change",
        )

    def test_duplicate_package_records_in_one_extra_are_ambiguous(self) -> None:
        base = '''[project]
name = "demo"
[project.optional-dependencies]
mlx = ["numpy==1.0; python_version < '3.12'", "numpy==1.0; python_version >= '3.12'"]
'''
        head = base.replace("numpy==1.0", "numpy==2.0", 1)
        result = extract_pyproject_optional_extra_change(
            _exact(base, revision=_BASE_SHA),
            _exact(head, revision=_HEAD_SHA),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "ambiguous_pyproject_dependency_records")

    def test_malformed_toml_is_explicit(self) -> None:
        result = extract_pyproject_optional_extra_change(
            _exact(
                "[project.optional-dependencies\nmlx = []",
                revision=_BASE_SHA,
            ),
            _exact(
                _project(mlx_numpy="numpy==2.0"),
                revision=_HEAD_SHA,
            ),
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "malformed_dependency_file")


if __name__ == "__main__":
    unittest.main()
