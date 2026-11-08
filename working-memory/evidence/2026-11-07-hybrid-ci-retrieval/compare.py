"""Replay the offline CI hybrid retrieval and typed evidence exercise."""

import argparse
import json
import os
from pathlib import Path
import runpy
import sqlite3
import sys
from time import perf_counter


HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent
PREVIOUS = EVIDENCE / "2026-11-07-offline-semantic-retrieval"
CI_VIEW = EVIDENCE / "2026-10-21-investigator-native-ci-presentation"
FCI = EVIDENCE / "2026-10-20-current-ci-owner-diagnostic/live/FCI001/result.json"
RENDER = CI_VIEW / "render-repair/case-2.txt"
STRUCTURED = CI_VIEW / "execution/case-2/ci-presentation.json"
RENDER_VERIFICATION = CI_VIEW / "render-repair/verification.json"
PROTOCOL = HERE / "protocol.json"
FREEZE = HERE / "freeze.json"
POOL = 3
LIMIT = 2
FUSION_OFFSET = 10


def load(path):
    return json.loads(path.read_bytes())


def target(identity):
    return tuple(str(identity[key]) for key in ("repository", "pull_number", "base_sha", "head_sha"))


def corpus(protocol, digest):
    verified = load(RENDER_VERIFICATION)["rows"][1]
    assert digest(RENDER) == verified["repair_text_sha256"]
    assert digest(STRUCTURED) == verified["original_json_sha256"]
    lines = RENDER.read_text().splitlines()
    glyphs = target(load(STRUCTURED)["target"])
    assert f"Head: {glyphs[3]}" in lines and f"Base: {glyphs[2]}" in lines
    passages = [(name, glyphs, kind, f"case-2.txt:L{first}–{last}", "\n".join(lines[first - 1:last]))
                for name, kind, first, last in protocol["glyphs_passages"]]

    fci = load(FCI)
    assert fci["case_id"] == "FCI001" and fci["track"] == "separately_fresh"
    identity = target({"repository": "openai/openai-agents-python", "pull_number": 5404, **fci["initial_pr"]})
    job, = fci["jobs"]
    assert identity[3] == job["head_sha"] == fci["selected_run"]["head_sha"]
    assert identity[2:] == (fci["final_pr"]["base_sha"], fci["final_pr"]["head_sha"])
    owner = fci["owner"]
    assert owner["state"] == "correlated"
    steps = owner["step_execution"]
    assert len(steps) == 2 and all(step["runtime_conclusion"] == "skipped" for step in steps)
    passages.extend([
        ("fci-job", identity, "observed_job_result", "FCI001/result.json#/jobs/0",
         f"Job {job['job_id']} {job['name']}: status {job['status']}, conclusion {job['conclusion']}."),
        ("fci-user-steps", identity, "observed_user_steps", "FCI001/result.json#/owner/step_execution",
         "\n".join(f"User step {step['runtime_step_number']} {step['runtime_name']}: "
                   f"{step['runtime_conclusion']}. Successful execution {step['state']}." for step in steps)),
        ("fci-correlation", identity, "observed_correlation", "FCI001/result.json#/owner",
         f"{owner['state']}: {owner['detail']} Matched jobs: {owner['matched_jobs']}."),
        ("fci-run", identity, "observed_run_result", "FCI001/result.json#/selected_run",
         json.dumps(fci["selected_run"], sort_keys=True)),
    ])
    wrong = passages[2]
    passages.append(("synthetic-wrong-head", (*glyphs[:3], "0" * 40), *wrong[2:]))
    return passages, {"glyphs": glyphs, "fci": identity}


def fuse(lexical, semantic):
    scores = {}
    for ranking in (lexical, semantic):
        for rank, name in enumerate(ranking, 1):
            scores[name] = scores.get(name, 0) + 1 / (FUSION_OFFSET + rank)
    return sorted(scores, key=lambda name: (-scores[name], name))[:LIMIT]


def compare(model_path, protocol, passages, targets, sequence_limit):
    import torch
    from sentence_transformers import SentenceTransformer
    from transformers import AutoConfig, AutoTokenizer

    torch.set_num_threads(2)
    started = perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, trust_remote_code=False)
    config = AutoConfig.from_pretrained(model_path, local_files_only=True, trust_remote_code=False)
    assert sequence_limit <= tokenizer.model_max_length
    assert sequence_limit + config.pad_token_id < config.max_position_embeddings
    model = SentenceTransformer(str(model_path), device="cpu", local_files_only=True,
                                trust_remote_code=False, model_kwargs={"use_safetensors": True})
    model.max_seq_length = sequence_limit
    assert model.tokenizer.model_max_length == sequence_limit
    queries = protocol["queries"]
    texts = [row[-1] for row in passages] + [query[2] for query in queries]
    longest = max(map(len, model.tokenizer(texts, truncation=False)["input_ids"]))
    assert longest <= sequence_limit, longest
    vectors = model.encode(texts, batch_size=8, normalize_embeddings=True, show_progress_bar=False)
    rows = []
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE VIRTUAL TABLE ci USING fts5(name UNINDEXED, scope UNINDEXED, body)")
        db.executemany("INSERT INTO ci VALUES (?, ?, ?)", [(name, json.dumps(key), body)
                       for name, key, _kind, _locator, body in passages])
        for q_index, (q_id, case, _text, expression, expected, kind) in enumerate(queries):
            key = targets[case]
            eligible = {name: (index, label) for index, (name, scope, label, _locator, _body)
                        in enumerate(passages) if key == scope}
            assert "synthetic-wrong-head" not in eligible
            assert expected is None or eligible[expected][1] == kind
            lexical = [row[0] for row in db.execute(
                "SELECT name FROM ci WHERE ci MATCH ? AND scope = ? ORDER BY bm25(ci), name LIMIT ?",
                (expression, json.dumps(key), POOL))]
            query_vector = vectors[len(passages) + q_index]
            semantic = sorted(eligible, key=lambda name: (
                -float(vectors[eligible[name][0]] @ query_vector), name))[:POOL]
            hybrid = fuse(lexical, semantic)
            assert set(lexical + semantic + hybrid) <= eligible.keys()
            selected = [name for name in hybrid if eligible[name][1] == kind]
            rows.append({"query": q_id, "expected": expected, "required_kind": kind,
                         "lexical": lexical[:LIMIT], "embedding": semantic[:LIMIT], "hybrid": hybrid,
                         "accepted": selected, "gate": "matching_kind_returned" if selected else "no_matching_kind"})
    positives = [row for row in rows if row["expected"] is not None]
    return {"rows": rows, "positive_queries": len(positives), "hits_at_2": {
        arm: sum(row["expected"] in row[arm] for row in positives)
        for arm in ("lexical", "embedding", "hybrid", "accepted")},
        "longest_input_tokens": longest, "elapsed_compare_seconds": round(perf_counter() - started, 3)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("freeze", "run"))
    parser.add_argument("model", type=Path)
    args = parser.parse_args()
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", CUDA_VISIBLE_DEVICES="",
                      TOKENIZERS_PARALLELISM="false", HF_HUB_DISABLE_TELEMETRY="1")
    previous = runpy.run_path(str(PREVIOUS / "compare.py"))
    digest = previous["digest"]
    sys.addaudithook(previous["block_network"])
    model_freeze = PREVIOUS / "freeze-successor.json"
    pinned = load(model_freeze)
    assert args.model.name == pinned["snapshot"]
    assert {str(path.relative_to(args.model)): digest(path) for path in sorted(args.model.rglob("*"))
            if path.is_file()} == pinned["model_files"]
    packages = {name: previous["version"](name) for name in pinned["packages"] if not name.startswith("tree-sitter")}
    assert all(pinned["packages"][name] == release for name, release in packages.items())
    protocol = load(PROTOCOL)
    passages, targets = corpus(protocol, digest)
    freeze = {"files": {str(path.relative_to(EVIDENCE)): digest(path) for path in
                        (Path(__file__), PROTOCOL, model_freeze, PREVIOUS / "compare.py", RENDER,
                         STRUCTURED, RENDER_VERIFICATION, FCI)},
              "targets": {name: list(key) for name, key in targets.items()}, "passages": [list(row[:1]) + list(row[2:4]) for row in passages],
              "device": "cpu", "packages": packages, "sqlite": sqlite3.sqlite_version,
              "sequence_limit": pinned["sequence_limit"], "pool": POOL, "limit": LIMIT, "fusion_offset": FUSION_OFFSET}
    if args.mode == "freeze":
        print(json.dumps(freeze, indent=2, sort_keys=True))
        return
    assert load(FREEZE) == freeze, "Hybrid retrieval freeze mismatch"
    result = compare(args.model, protocol, passages, targets, freeze["sequence_limit"])
    print(json.dumps({"freeze_sha256": digest(FREEZE), **result}, indent=2))


if __name__ == "__main__":
    main()
