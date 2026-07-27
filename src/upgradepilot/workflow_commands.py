"""Read a narrow, explicit subset of GitHub Actions workflow commands.

UpgradePilot deliberately does not pretend to implement a complete YAML parser.
This module understands ordinary indentation-based ``jobs`` and ``run`` blocks
well enough for the first CI-authority rule. Richer YAML forms remain unresolved
until evidence justifies either broader deterministic parsing or a YAML library.

The reader is intentionally conservative: it recognizes only structures whose
job and command boundaries can be established from the visible text. Unsupported
indirection is returned as unresolved evidence rather than guessed behavior.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

# ``Literal`` creates a closed, type-checkable status vocabulary. Callers can
# reason about these two evidence states without accepting arbitrary strings.
type WorkflowCommandStatus = Literal["supported", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    """Result of searching one workflow definition for direct exercise evidence.

    The result preserves both the classification and any command text actually
    found. Partial evidence therefore remains inspectable even when the complete
    install-and-execute rule cannot be proven.
    """

    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class _WorkflowJobDefinition:
    """Private intermediate representation of one shallowly parsed workflow job.

    The parser needs only a job key and immutable command collection; retaining a
    small internal record avoids exposing incomplete YAML structure as public API.
    """

    key: str
    commands: tuple[str, ...]


# These patterns are compiled once because they are applied repeatedly while
# scanning workflow lines and shell segments. Named groups make the extracted
# indentation, key, value, and requirement path explicit to the parsing code.
_JOB_KEY_PATTERN = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z0-9_.-]+):\s*(?:#.*)?$")
_RUN_PATTERN = re.compile(r"^(?P<indent>\s*)(?:-\s+)?run:\s*(?P<value>.*)$")
# Recognize common direct pip entry forms while requiring ``install`` as a word.
# The negative lookbehind avoids matching a pip-like token embedded in a name.
_PIP_INSTALL_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
# Capture every ``-r``/``--requirement`` argument. The path stops before shell
# separators so evidence from a later command cannot leak into this argument.
_REQUIREMENT_PATTERN = re.compile(
    r"(?:^|\s)(?:-r|--requirement)(?:=|\s+)(?P<path>[^\s;&|]+)",
    re.IGNORECASE,
)


def inspect_workflow_commands(
    text: str,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Find direct install-and-invoke evidence in one single-job workflow.

    Multiple jobs are intentionally unresolved because combining installation
    from one job with execution from another would create false authority.

    The ``*`` makes the evidence identities keyword-only. This reduces accidental
    argument swaps among three related strings at call sites.
    """

    jobs = _extract_job_definitions(text)
    # ``None`` means the ``jobs`` mapping itself was not statically identifiable;
    # this differs from an identified mapping containing zero direct job entries.
    if jobs is None:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="workflow_jobs_not_statically_readable",
            detail="The shallow workflow reader could not identify the jobs mapping.",
            job_count=0,
        )
    # The first authority rule is deliberately single-job. This prevents evidence
    # from separate machines, environments, or dependency scopes being combined.
    if len(jobs) != 1:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="multiple_or_zero_workflow_jobs",
            detail=(
                "The first rule supports one statically identifiable workflow job; "
                f"observed {len(jobs)} job definitions."
            ),
            job_count=len(jobs),
        )

    commands = jobs[0].commands
    # ``next(generator, None)`` stops at the first matching command without
    # constructing an unnecessary list. ``None`` is the explicit no-match state.
    install_command = next(
        (
            command
            for command in commands
            if _command_installs_source_file(command, source_file)
        ),
        None,
    )
    execution_command = next(
        (
            command
            for command in commands
            if _command_invokes_package(command, package, normalized_package)
        ),
        None,
    )

    if install_command is None or execution_command is None:
        # Build the explanation incrementally so the result states exactly which
        # half of the authority rule was absent while preserving any half found.
        missing: list[str] = []
        if install_command is None:
            missing.append(f"installation of {source_file!r}")
        if execution_command is None:
            missing.append(f"direct invocation of {package!r}")
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="direct_dependency_exercise_not_proven",
            detail="Workflow commands did not prove " + " and ".join(missing) + ".",
            job_count=1,
            install_command=install_command,
            execution_command=execution_command,
        )

    return WorkflowCommandEvidence(
        status="supported",
        reason="source_installed_and_dependency_invoked",
        detail=(
            "The workflow installs the changed requirements file and directly "
            "invokes the changed package."
        ),
        job_count=1,
        install_command=install_command,
        execution_command=execution_command,
    )


def _extract_job_definitions(text: str) -> tuple[_WorkflowJobDefinition, ...] | None:
    """Extract direct children of ``jobs`` and their shell commands.

    This is an indentation reader, not a YAML evaluator. It locates the first plain
    ``jobs:`` key, identifies one direct-child indentation level, and slices each
    visible job region using the next job start as its boundary.
    """

    # ``splitlines`` removes line terminators while preserving the indentation that
    # carries the limited structural information used by this reader.
    lines = text.splitlines()
    jobs_index: int | None = None
    jobs_indent: int | None = None

    # Find the first non-comment line whose complete visible content is ``jobs:``.
    # More complex forms such as anchors or expressions intentionally do not match.
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "jobs:":
            jobs_index = index
            # Subtracting left-stripped length is a direct count of leading
            # whitespace without rewriting the original line.
            jobs_indent = len(line) - len(line.lstrip())
            break

    if jobs_index is None or jobs_indent is None:
        return None

    # Each tuple stores the source-line index, indentation, and job key. Keeping
    # source positions makes it possible to slice complete job regions afterward.
    starts: list[tuple[int, int, str]] = []
    job_indent: int | None = None
    for index in range(jobs_index + 1, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        # Returning to the ``jobs`` indentation or above closes that mapping.
        if indent <= jobs_indent:
            break
        match = _JOB_KEY_PATTERN.match(line)
        if match is None:
            continue
        # The first matching child establishes the direct-job indentation. Deeper
        # mapping keys are ignored rather than misclassified as sibling jobs.
        if job_indent is None:
            job_indent = indent
        if indent == job_indent:
            starts.append((index, indent, match.group("key")))

    # An identified ``jobs`` mapping with no readable direct children is an empty
    # tuple, not ``None``; the caller can preserve that different observation.
    if not starts:
        return ()

    definitions: list[_WorkflowJobDefinition] = []
    for position, (start, indent, key) in enumerate(starts):
        # The next sibling job marks this job's exclusive end. The final job extends
        # to the remaining text; indentation checks in command extraction constrain
        # which ``run`` lines are accepted.
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        definitions.append(
            _WorkflowJobDefinition(
                key=key,
                commands=_extract_run_commands(lines[start + 1 : end], job_indent=indent),
            )
        )
    # Freeze the parsed intermediate collection before returning it to the rule.
    return tuple(definitions)


def _extract_run_commands(
    lines: Sequence[str],
    *,
    job_indent: int,
) -> tuple[str, ...]:
    """Extract inline and block ``run`` commands from one workflow job.

    ``Sequence`` accepts a list or slice without requiring a concrete container.
    A manual index is used because block commands consume multiple following lines;
    a simple ``for`` loop could not advance past an already-consumed block.
    """

    commands: list[str] = []
    index = 0
    while index < len(lines):
        # The pattern supports both mapping-style ``run: ...`` and list-item
        # ``- run: ...`` forms while capturing the indentation and remaining value.
        match = _RUN_PATTERN.match(lines[index])
        if match is None:
            index += 1
            continue

        run_indent = len(match.group("indent"))
        # A command must be nested inside the job. Same-level or outer ``run`` keys
        # are outside this job's evidence boundary.
        if run_indent <= job_indent:
            index += 1
            continue

        value = match.group("value").strip()
        # A non-empty value that is not a YAML block marker is treated as one inline
        # shell command. Matching outer quotes are removed only for comparison.
        if value and not value.startswith(("|", ">")):
            commands.append(_strip_matching_quotes(value))
            index += 1
            continue

        # ``|`` and ``>`` introduce following indented lines. This shallow reader
        # joins their visible command lines with newlines; it does not emulate all
        # YAML literal/folded scalar semantics.
        block: list[str] = []
        index += 1
        while index < len(lines):
            candidate = lines[index]
            stripped = candidate.strip()
            indent = len(candidate) - len(candidate.lstrip())
            # The first non-empty line returning to the ``run`` indentation closes
            # the block and is left for the outer loop to inspect.
            if stripped and indent <= run_indent:
                break
            # Blank lines and full-line comments carry no direct command evidence.
            if stripped and not stripped.startswith("#"):
                block.append(stripped)
            index += 1
        if block:
            commands.append("\n".join(block))

    return tuple(commands)


def _command_installs_source_file(command: str, source_file: str) -> bool:
    """Return whether one command directly installs the specified requirements file."""

    # Normalize the expected path once rather than repeating work for every shell
    # segment and every requirement flag found in the command.
    normalized_source = _normalize_command_path(source_file)
    for segment in _shell_segments(command):
        # A requirement flag is relevant only inside a segment that visibly invokes
        # a supported pip install form.
        if _PIP_INSTALL_PATTERN.search(segment) is None:
            continue
        # ``finditer`` handles commands with multiple ``-r`` arguments and retains
        # each captured path independently.
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            candidate = match.group("path").strip("'\"")
            if _normalize_command_path(candidate) == normalized_source:
                return True
    return False


def _command_invokes_package(
    command: str,
    package: str,
    normalized_package: str,
) -> bool:
    """Return whether one shell segment directly starts the changed package.

    Only explicit command/module forms are supported. Tox, project scripts, shell
    functions, aliases, and reusable workflows remain unresolved until their own
    configuration is traced.
    """

    # A set comprehension lowercases and deduplicates the original and normalized
    # names. The full-match guard limits dynamic regex construction to the package
    # token grammar understood by this reader.
    candidates = {
        candidate.lower()
        for candidate in (package, normalized_package)
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", candidate)
    }
    # These prefixes represent direct wrappers whose next token is still the target
    # command or Python module. Indirect runners such as tox are deliberately absent.
    prefixes = (
        "",
        "python -m ",
        "python3 -m ",
        "uv run ",
        "poetry run ",
        "pipenv run ",
        "coverage run -m ",
    )

    for segment in _shell_segments(command):
        # Remove one or more leading ``NAME=value`` environment assignments so a
        # direct command remains recognizable without interpreting shell state.
        segment = re.sub(
            r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)+",
            "",
            segment.strip(),
        )
        for candidate in candidates:
            for prefix in prefixes:
                expected = f"{prefix}{candidate}"
                if re.match(
                    # Anchor at the segment start to require direct invocation.
                    # ``re.escape`` treats the constructed command literally, and
                    # the lookahead requires a token boundary without consuming it.
                    rf"^{re.escape(expected)}(?=\s|$)",
                    segment,
                    re.IGNORECASE,
                ):
                    return True
    return False


def _shell_segments(command: str) -> tuple[str, ...]:
    """Split the supported command text at common shell command boundaries.

    This is intentionally not a shell parser: quoting, substitutions, pipelines,
    and control-flow semantics are not reconstructed. The split only prevents one
    visible command from being conflated with a neighboring ``&&``, ``||``, ``;``,
    or newline-delimited command.
    """

    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


def _normalize_command_path(path: str) -> str:
    """Normalize only superficial command-path spelling for exact comparison.

    Backslashes are treated as separators and leading ``./`` prefixes are removed.
    The function deliberately does not resolve ``..``, variables, symlinks, or the
    working directory because doing so would require evidence not present here.
    """

    normalized = path.strip().replace("\\", "/")
    # A loop handles repeated but equivalent prefixes such as ``././requirements``.
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _strip_matching_quotes(value: str) -> str:
    """Remove one matching pair of outer quotes without parsing shell quoting."""

    # Both ends must contain the same quote character; unmatched or internal quotes
    # remain untouched because their shell meaning cannot be inferred safely.
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value
