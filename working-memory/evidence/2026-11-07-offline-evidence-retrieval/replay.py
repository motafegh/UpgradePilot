"""Replay a small, offline FTS5 retrieval exercise from exact saved evidence."""

import hashlib
import json
import sqlite3
from pathlib import Path

from upgradepilot.report_file import read_report


EVIDENCE = Path(__file__).resolve().parents[1]
HTTPX = EVIDENCE / "2026-11-07-native-proxy-successor"
OPENCV = EVIDENCE / "2026-10-22-opencv-matched-report-source-capture"


def load(path):
    return json.loads(path.read_bytes())


def verified_bytes(path, expected):
    content = path.read_bytes()
    assert hashlib.sha256(content).hexdigest() == expected, path.name
    return content


def target_key(identity):
    return tuple(str(identity[name]) for name in ("repository", "pull_number", "base_sha", "head_sha"))


def make_passage(key, target, role, version, locator, lines, first, last):
    assert 1 <= first <= last <= len(lines), locator
    return (key, *target, role, version, f"{locator}:L{first}–{last}", "\n".join(lines[first - 1:last]))


def load_passages():
    result = load(HTTPX / "results.json")
    binding = load(EVIDENCE / "2026-11-07-pypi-route-repair" / "successor-binding.json")
    httpx_path = Path(binding["destinations"]["product_attempt"]) / "report.json"
    verified_bytes(httpx_path, result["cold_recovery"]["exact_report_sha256"])
    report = read_report(httpx_path)
    httpx_target = target_key({fact.name: fact.value for fact in report.identity})
    assert httpx_target == target_key(result["identity"])
    sources = {source.source_id: source for source in report.sources}

    opencv_receipt = load(OPENCV / "capture-receipt.json")
    opencv_path = OPENCV / "report.json"
    verified_bytes(opencv_path, opencv_receipt["report_sha256"])
    report = read_report(opencv_path)
    opencv_target = target_key({fact.name: fact.value for fact in report.identity})
    assert opencv_target == target_key(load(OPENCV / "contract.json")["expected_identity"])
    text_receipt = next(member for member in load(OPENCV / "verification.json")["private_members"]
                        if member["capture"] == "normal" and member["path"] == "report.txt")
    opencv_lines = verified_bytes(OPENCV / "report.txt", text_receipt["sha256"]).decode().splitlines()

    passages = []
    for key, source_id, first, last in (
        ("httpx-target", "source-27", 1, 10),
        ("httpx-fallback", "source-39", 25, 34),
        ("httpx-forward", "source-39", 475, 484),
        ("httpx-old", "source-35", 628, 652),
        ("httpx-proposed", "source-31", 639, 661),
    ):
        source = sources[source_id]
        identity = {fact.name: str(fact.value) for fact in source.identity}
        passages.append(make_passage(key, httpx_target, identity["role"], identity["version"],
                                     f"{source_id}/{identity['path']}", source.content.splitlines(), first, last))

    for key, first, last in (("opencv-artifacts", 87, 95), ("opencv-target", 97, 110),
                             ("opencv-build", 155, 158), ("opencv-ci", 30, 43)):
        passages.append(make_passage(key, opencv_target, "transition_report", "", "report.txt",
                                     opencv_lines, first, last))
    return passages, httpx_target, opencv_target


def search(connection, query, target, role=None, version=None, limit=2):
    conditions = ["passages MATCH ?"]
    values = [query]
    if target is not None:
        conditions.append("repository = ? AND pr = ? AND base = ? AND head = ?")
        values.extend(target)
    if role is not None:
        conditions.append("role = ? AND version = ?")
        values.extend((role, version))
    rows = connection.execute(
        f"SELECT passage_id FROM passages WHERE {' AND '.join(conditions)} ORDER BY bm25(passages), passage_id LIMIT ?",
        (*values, limit),
    )
    return [row[0] for row in rows]


def main():
    passages, httpx, opencv = load_passages()
    by_id = {row[0]: row for row in passages}
    # Same bytes with a deliberately false head. This fixture tests admission only.
    fallback = by_id["httpx-fallback"]
    wrong_head = ("control-wrong-head", *fallback[1:4], "0" * 40, *fallback[5:])
    cases = (
        ('"ModuleNotFoundError" AND "httpx2"', httpx, None, None, "httpx-fallback"),
        ('"backup client"', httpx, None, None, "httpx-fallback"),
        ('"follow_redirects" AND "cookies"', httpx, "old_dependency", "0.27.2", "httpx-old"),
        ('"follow_redirects" AND "cookies"', httpx, "proposed_dependency", "0.28.1", "httpx-proposed"),
        ('"wheel-tag capabilities"', opencv, None, None, "opencv-artifacts"),
        ('"target source-build outcome"', opencv, None, None, "opencv-build"),
        ('"compile" AND "from source"', opencv, None, None, "opencv-build"),
    )

    with sqlite3.connect(":memory:") as db:
        db.execute("""CREATE VIRTUAL TABLE passages USING fts5(
            passage_id UNINDEXED, repository UNINDEXED, pr UNINDEXED, base UNINDEXED, head UNINDEXED,
            role UNINDEXED, version UNINDEXED, locator UNINDEXED, body)""")
        db.executemany("INSERT INTO passages VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [*passages, wrong_head])
        print(f"SQLite {sqlite3.sqlite_version}. {len(passages)} real passages and one synthetic control.")
        hits = 0
        for query, target, role, version, expected in cases:
            assert by_id[expected][1:5] == target
            if role is not None:
                assert by_id[expected][5:7] == (role, version)
            matched = search(db, query, target, role, version)
            assert all(by_id[passage_id][1:5] == target for passage_id in matched)
            hits += expected in matched
            size = sum(len(by_id[passage_id][-1].encode()) for passage_id in matched)
            print(f"{query} [{role or 'any role'}] -> {matched}, expected {expected}, {size} bytes")
        print(f"Known-address lookup {len(cases)}/{len(cases)}. FTS5 recall@2 {hits}/{len(cases)}.")

        assert "control-wrong-head" in search(db, cases[0][0], None)
        assert search(db, cases[0][0], httpx) == ["httpx-fallback"]
        unscoped_roles = search(db, cases[2][0], httpx, limit=9)
        assert {"httpx-old", "httpx-proposed"} <= set(unscoped_roles)
        assert search(db, cases[2][0], httpx, "proposed_dependency", "0.27.2") == []
        print(f"Role filter control: {unscoped_roles}; wrong role/version pair refused.")
        print("Wrong-head control retrieved without a target filter and excluded with the exact target.")


if __name__ == "__main__":
    main()
