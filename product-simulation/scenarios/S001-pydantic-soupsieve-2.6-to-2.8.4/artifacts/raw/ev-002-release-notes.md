# Bounded Dependabot release-note capture

**Source:** https://github.com/pydantic/pydantic/pull/13432  
**Acquired:** 2026-07-22T19:03:48Z through GitHub connector `get_pr_info`  
**Preservation:** material excerpt; full PR body remains at the source

## 2.8.4
- **FIX**: Fix another inefficient attribute pattern.
- **FIX**: Limit total number of selectors processed in a pattern to prevent massive selector requests.

## 2.8.3
- **FIX**: Fix inefficient attribute pattern.

## 2.8.2
- **FIX**: Reject non-string custom-selector or namespace keys.
- **FIX**: Fix date-range selector behavior.
- **FIX**: Fix a potential pretty-print infinite loop.

## 2.8.1
- **FIX**: Changes in tests for the latest Python HTML parser.

## 2.8
- **NEW**: Drop support for Python 3.8.
- **NEW**: Add support for Python 3.14.
- **NEW**: Deploy with PyPI Trusted Publisher.

## 2.7
- **NEW**: Add and recognize additional pseudo selectors.
- **FIX**: Typing fixes.

### Baseline-sensitive literal note
The fixed baseline vocabulary contains `dropped support`, `fixed`, `bug fix`, and
`bugfix`. It does not normalize `Drop support` or `FIX`, so this preserved text
produces no literal caution or benefit/security match under baseline v0.1.
