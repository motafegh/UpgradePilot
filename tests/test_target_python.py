"""Test exact-head ``requires-python`` interpretation without network access."""

from __future__ import annotations

import unittest

from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    interpret_target_python_declaration,
)


class TargetPythonTests(unittest.TestCase):
    """Protect the admitted source and every target-declaration evidence state."""

    def test_available_declaration_preserves_value_and_provenance(self) -> None:
        result = interpret_target_python_declaration(
            _file('[project]\nrequires-python = ">=3.10, <4"\n')
        )

        self.assertIsInstance(result, TargetPythonDeclaration)
        assert isinstance(result, TargetPythonDeclaration)
        self.assertEqual(result.state, "available")
        self.assertEqual(result.requires_python, ">=3.10, <4")
        self.assertEqual(result.path, "pyproject.toml")
        self.assertEqual(result.revision, "head-sha")
        self.assertEqual(result.blob_sha, "blob-sha")

    def test_file_unavailable_remains_explicit(self) -> None:
        result = interpret_target_python_declaration(
            UnavailableRepositoryFile(
                path="pyproject.toml",
                revision="head-sha",
                reason="not_found_or_inaccessible",
                detail="GitHub returned 404.",
            )
        )

        self.assertIsInstance(result, TargetPythonDeclarationProblem)
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "file_unavailable")
        self.assertIsNone(result.blob_sha)

    def test_malformed_toml_remains_distinct(self) -> None:
        result = interpret_target_python_declaration(_file("[project\n"))
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "malformed_toml")
        self.assertEqual(result.blob_sha, "blob-sha")

    def test_missing_project_table_remains_distinct(self) -> None:
        result = interpret_target_python_declaration(_file('[tool.demo]\nvalue = "x"\n'))
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "project_table_absent")

    def test_missing_requires_python_remains_distinct(self) -> None:
        result = interpret_target_python_declaration(_file('[project]\nname = "demo"\n'))
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "requires_python_absent")

    def test_non_text_requires_python_is_invalid(self) -> None:
        result = interpret_target_python_declaration(
            _file('[project]\nrequires-python = [">=3.12"]\n')
        )
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "invalid_requires_python")

    def test_empty_requires_python_is_invalid(self) -> None:
        result = interpret_target_python_declaration(
            _file('[project]\nrequires-python = "   "\n')
        )
        assert isinstance(result, TargetPythonDeclarationProblem)
        self.assertEqual(result.state, "invalid_requires_python")

    def test_other_repository_path_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            interpret_target_python_declaration(
                RepositoryTextFile(
                    path="setup.cfg",
                    revision="head-sha",
                    blob_sha="blob-sha",
                    content="[metadata]\n",
                )
            )


def _file(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        path="pyproject.toml",
        revision="head-sha",
        blob_sha="blob-sha",
        content=content,
    )


if __name__ == "__main__":
    unittest.main()
