"""Read the small workflow-command subset supported by the first authority rule.

Purpose of this file
--------------------
``github_repository.py`` returns the exact-revision workflow file as UTF-8 text.
This module examines that text for two direct facts inside one statically readable
workflow job:

* a supported ``pip install -r <changed file>`` command;
* a supported direct invocation of the changed package.

Why this is not a complete YAML or shell parser
-----------------------------------------------
GitHub Actions YAML can contain anchors, reusable workflows, expressions, matrices,
custom actions, shell scripts, project task runners, and many forms of indirection.
This module intentionally understands only a narrow indentation-based structure and
visible ``run:`` commands. When the visible text cannot establish the required facts,
it returns ``unresolved`` instead of guessing.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
Inputs come from two earlier stages:

* ``RepositoryTextFile.content`` from ``github_repository.py`` supplies the workflow;
* ``PinnedDependencyChange`` from ``dependency_change.py`` supplies the changed
  requirements file and package identity.

``ci_authority.py`` calls ``inspect_workflow_commands`` only after it has selected a
successful exact-head run and successful jobs. A supported command result is one part
of the CI-authority rule; it is not a general claim about test coverage or safety.

Supported processing flow
-------------------------
1. Find a plain ``jobs:`` mapping.
2. Identify its direct child job keys using indentation.
3. Require exactly one statically identifiable job.
4. Extract inline and block ``run:`` command text from that job.
5. Split visible command chains into bounded shell segments.
6. Search for direct installation and package invocation evidence.
7. Return both the classification and the actual matching commands found.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

# ``Literal`` limits this public status to two known strings. A type checker can catch
# accidental spellings and callers can exhaustively handle supported/unresolved.
type WorkflowCommandStatus = Literal["supported", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    """Result of applying the direct command rule to one workflow definition.

    ``reason`` is a stable category for program logic; ``detail`` explains the result
    to a reader. Matching command strings are preserved even for partial evidence, so
    an unresolved result can still show which half of the rule was observed.
    """

    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class _WorkflowJobDefinition:
    """Private intermediate record for one shallowly identified workflow job.

    The reader does not need or claim a complete YAML object model. It preserves only
    the job key and the visible command strings required by the current rule.
    """

    key: str
    commands: tuple[str, ...]


# A job key is accepted only when the whole line is a plain mapping key at one
# indentation level. Named groups expose the indentation and key to the scanner.
_JOB_KEY_PATTERN = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z0-9_.-]+):\s*(?:#.*)?$")

# ``(?:-\s+)?`` supports both ``run: ...`` and list-item ``- run: ...`` forms.
# The remaining text after the colon is captured as ``value``.
_RUN_PATTERN = re.compile(r"^(?P<indent>\s*)(?:-\s+)?run:\s*(?P<value>.*)$")

# Recognize direct pip entry forms such as ``pip install`` and
# ``python -m pip install``. The negative lookbehind prevents a match inside a
# larger token, and ``\b`` requires a word boundary after ``install``.
_PIP_INSTALL_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)

# Capture paths supplied through ``-r`` or ``--requirement``. The path stops before
# whitespace and common shell separators so a later command cannot leak into it.
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
    """Decide whether one workflow directly installs and invokes the dependency.

    Goal:
        Establish the command portion of the first CI-authority rule from visible,
        exact-revision workflow text.

    The ``*`` makes the three evidence identities keyword-only. Their types are all
    strings, so named arguments prevent accidental positional swaps.

    Multiple jobs remain unresolved because installation in job A and invocation in
    job B do not prove that one environment performed both operations.
    """

    jobs = _extract_job_definitions(text)

    # ``None`` means the reader could not identify a supported ``jobs`` mapping.
    # An empty tuple means it found the mapping but no readable direct job children.
    if jobs is None:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="workflow_jobs_not_statically_readable",
            detail="The shallow workflow reader could not identify the jobs mapping.",
            job_count=0,
        )
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

    # ``next(generator, None)`` evaluates commands lazily and stops at the first match.
    # The default ``None`` is the explicit no-match result.
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
        # Build a precise explanation while preserving whichever matching command was
        # found in the returned evidence record.
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
    """Identify direct ``jobs`` children and collect their visible run commands.

    This function reads indentation only; it does not evaluate YAML. The first plain
    ``jobs:`` line establishes the parent indentation, and the first supported child
    key establishes the direct job indentation. Adjacent job starts then define the
    text slice belonging to each job.
    """

    # ``splitlines`` removes newline characters but preserves leading whitespace,
    # which is the structural signal this narrow reader needs.
    lines = text.splitlines()
    jobs_index: int | None = None
    jobs_indent: int | None = None

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "jobs:":
            jobs_index = index
            # Difference between original and left-stripped length equals the number
            # of leading whitespace characters.
            jobs_indent = len(line) - len(line.lstrip())
            break

    if jobs_index is None or jobs_indent is None:
        return None

    # Store line position, indentation, and key first. Positions are later used to
    # slice each job body without constructing a complete syntax tree.
    starts: list[tuple[int, int, str]] = []
    job_indent: int | None = None
    for index in range(jobs_index + 1, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())

        # Returning to the ``jobs:`` indentation or above closes that mapping.
        if indent <= jobs_indent:
            break
        match = _JOB_KEY_PATTERN.match(line)
        if match is None:
            continue

        # The first supported child establishes the sibling-job indentation. Mapping
        # keys nested more deeply are ignored instead of being misclassified as jobs.
        if job_indent is None:
            job_indent = indent
        if indent == job_indent:
            starts.append((index, indent, match.group("key")))

    if not starts:
        return ()

    definitions: list[_WorkflowJobDefinition] = []
    for position, (start, indent, key) in enumerate(starts):
        # The next sibling's start is this job's exclusive end. The final job extends
        # to the end of the file; command indentation still limits accepted run keys.
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        definitions.append(
            _WorkflowJobDefinition(
                key=key,
                commands=_extract_run_commands(lines[start + 1 : end], job_indent=indent),
            )
        )
    return tuple(definitions)


def _extract_run_commands(
    lines: Sequence[str],
    *,
    job_indent: int,
) -> tuple[str, ...]:
    """Extract supported inline and indented-block ``run`` command text.

    ``Sequence`` allows this helper to accept a list or list slice. A manual ``while``
    index is used because one block scalar consumes several subsequent lines; the
    parser must advance past all consumed lines before resuming the outer scan.
    """

    commands: list[str] = []
    index = 0
    while index < len(lines):
        match = _RUN_PATTERN.match(lines[index])
        if match is None:
            index += 1
            continue

        run_indent = len(match.group("indent"))
        if run_indent <= job_indent:
            index += 1
            continue

        value = match.group("value").strip()
        if value and not value.startswith(("|", ">")):
            # Inline command values may be wrapped in one matching quote pair.
            commands.append(_strip_matching_quotes(value))
            index += 1
            continue

        # ``|`` and ``>`` introduce following indented lines. The reader preserves
        # visible command lines but does not emulate every YAML literal/folded-scalar
        # whitespace rule.
        block: list[str] = []
        index += 1
        while index < len(lines):
            candidate = lines[index]
            stripped = candidate.strip()
            indent = len(candidate) - len(candidate.lstrip())
            if stripped and indent <= run_indent:
                break
            if stripped and not stripped.startswith("#"):
                block.append(stripped)
            index += 1
        if block:
            commands.append("\n".join(block))

    return tuple(commands)


def _command_installs_source_file(command: str, source_file: str) -> bool:
    """Return whether visible command text installs the changed requirements file."""

    normalized_source = _normalize_command_path(source_file)
    for segment in _shell_segments(command):
        # Requirement flags count only inside a segment that visibly invokes one of
        # the supported pip install forms.
        if _PIP_INSTALL_PATTERN.search(segment) is None:
            continue
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            # Remove one surrounding shell quote style before path normalization.
            candidate = match.group("path").strip("'\"")
            if _normalize_command_path(candidate) == normalized_source:
                return True
    return False


def _command_invokes_package(
    command: str,
    package: str,
    normalized_package: str,
) -> bool:
    """Return whether a shell segment directly begins with the changed package.

    Supported wrappers still expose the target as the directly named command or
    Python module. Indirect execution through tox, scripts, aliases, functions, custom
    actions, or reusable workflows is not inferred by this function.
    """

    # Lowercase and deduplicate both known package spellings. The grammar check keeps
    # dynamic regex construction within the token subset this reader understands.
    candidates = {
        candidate.lower()
        for candidate in (package, normalized_package)
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", candidate)
    }
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
        # Shell permits leading ``NAME=value`` assignments before a command. Remove
        # those visible assignments without trying to evaluate their values.
        segment = re.sub(
            r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)+",
            "",
            segment.strip(),
        )
        for candidate in candidates:
            for prefix in prefixes:
                expected = f"{prefix}{candidate}"
                if re.match(
                    # ``^`` requires the invocation at segment start. ``re.escape``
                    # makes the dynamic expected text literal, and the lookahead
                    # requires the next position to be whitespace or end-of-string.
                    rf"^{re.escape(expected)}(?=\s|$)",
                    segment,
                    re.IGNORECASE,
                ):
                    return True
    return False


def _shell_segments(command: str) -> tuple[str, ...]:
    """Split visible text at common command-chain boundaries.

    This is not a shell parser. It does not reconstruct quoting, pipelines,
    substitutions, conditions, or working-directory state. It only prevents commands
    separated by ``&&``, ``||``, ``;``, or a newline from being treated as one token.
    """

    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


def _normalize_command_path(path: str) -> str:
    """Normalize superficial path spelling used in direct command comparison.

    Backslashes become forward slashes and repeated leading ``./`` prefixes are
    removed. The function deliberately does not resolve variables, ``..``, symlinks,
    or a working directory because the workflow text does not establish those facts.
    """

    normalized = path.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _strip_matching_quotes(value: str) -> str:
    """Remove one matching outer quote pair without evaluating shell quoting."""

    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value
