from __future__ import annotations

import unittest

from upgradepilot.github.executable_selection import observe_command_executable_selection
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    StaticCommandAtom,
    StaticCommandOccurrence,
)


def _atom(raw: str, *, state: str = "literal", literal: str | None = None) -> StaticCommandAtom:
    return StaticCommandAtom(
        raw_source=raw,
        literal_value=raw if literal is None and state == "literal" else literal,
        state=state,  # type: ignore[arg-type]
    )


def _occurrence(executable: StaticCommandAtom) -> StaticCommandOccurrence:
    return StaticCommandOccurrence(
        source_order=0,
        source_span=CommandSourceSpan(
            start_byte=0,
            end_byte=len(executable.raw_source),
            start_line=0,
            start_column=0,
            end_line=0,
            end_column=len(executable.raw_source),
        ),
        raw_source=executable.raw_source,
        executable=executable,
        arguments=(),
        structural_context=("straightforward_top_level",),
    )


class CommandExecutableSelectionTests(unittest.TestCase):
    def test_posix_explicit_path_is_established_without_path_lookup(self) -> None:
        result = observe_command_executable_selection(
            _occurrence(_atom("./.venv/bin/python"))
        )

        self.assertEqual(result.state, "established")
        self.assertEqual(result.kind, "explicit_path")
        self.assertEqual(result.executable, "./.venv/bin/python")

    def test_absolute_explicit_path_is_established(self) -> None:
        result = observe_command_executable_selection(
            _occurrence(_atom("/opt/venv/bin/python"))
        )

        self.assertEqual(result.state, "established")
        self.assertEqual(result.kind, "explicit_path")

    def test_windows_style_explicit_path_is_established(self) -> None:
        result = observe_command_executable_selection(
            _occurrence(_atom(r".venv\Scripts\python.exe"))
        )

        self.assertEqual(result.state, "established")
        self.assertEqual(result.kind, "explicit_path")

    def test_bare_python_requires_path_resolution(self) -> None:
        result = observe_command_executable_selection(
            _occurrence(_atom("python"))
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.kind, "path_lookup_required")
        self.assertEqual(
            result.reason,
            "bare_executable_requires_path_resolution",
        )

    def test_dynamic_executable_stays_unresolved(self) -> None:
        result = observe_command_executable_selection(
            _occurrence(
                _atom(
                    "${{ matrix.python }}",
                    state="dynamic",
                    literal=None,
                )
            )
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.kind, "executable_dynamic")
        self.assertIsNone(result.executable)


if __name__ == "__main__":
    unittest.main()
