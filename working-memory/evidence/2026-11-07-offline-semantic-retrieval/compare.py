"""Freeze or replay a local comparison using the retained lexical exercise."""

import argparse
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import runpy
import sqlite3
import sys
from time import perf_counter


HERE = Path(__file__).resolve().parent
LEXICAL = HERE.parent / "2026-11-07-offline-evidence-retrieval" / "replay.py"
QUERIES = HERE / "queries.json"
FREEZE = HERE / "freeze.json"
MODEL_REVISION = "4328cf26390c98c5e3c738b4460a05b95f4911f5"
SEQUENCE_LIMIT = 384
VERSIONS = ("sentence-transformers", "torch", "transformers", "tokenizers", "safetensors",
            "tree-sitter", "tree-sitter-bash")
ROLES = {"any": (None, None), "old": ("old_dependency", "0.27.2"),
         "proposed": ("proposed_dependency", "0.28.1")}
REWRITES = {"backup client": "httpx2", "compile from source": '"source-build outcome"'}


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def block_network(event, _args):
    if event.startswith("socket."):
        raise RuntimeError(f"Offline comparison refused {event}")


def identity(model, passages):
    assert model.name == MODEL_REVISION
    return {
        "model": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        "snapshot": MODEL_REVISION,
        "model_files": {str(path.relative_to(model)): digest(path) for path in sorted(model.rglob("*"))
                        if path.is_file()},
        "packages": {name: version(name) for name in VERSIONS},
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "passages": {row[0]: hashlib.sha256(json.dumps(row, ensure_ascii=False).encode()).hexdigest()
                     for row in passages},
        "queries_sha256": digest(QUERIES), "lexical_sha256": digest(LEXICAL),
        "comparison_sha256": digest(Path(__file__)),
        "device": "cpu", "torch_threads": 2, "limit": 2, "sequence_limit": SEQUENCE_LIMIT,
        "ranking": "FTS5 BM25 or normalized dot product; ties by passage ID",
    }


def compare(model_path, passages, targets, lexical):
    import torch
    from sentence_transformers import SentenceTransformer

    torch.set_num_threads(2)
    start = perf_counter()
    model = SentenceTransformer(str(model_path), device="cpu", local_files_only=True,
                                trust_remote_code=False, model_kwargs={"use_safetensors": True})
    default_sequence_limit = model.max_seq_length
    assert SEQUENCE_LIMIT <= model.tokenizer.model_max_length
    model.max_seq_length = SEQUENCE_LIMIT
    loaded = perf_counter()
    queries = json.loads(QUERIES.read_bytes())
    texts = [row[-1] for row in passages] + [query[3] for query in queries]
    lengths = [len(tokens) for tokens in model.tokenizer(texts, truncation=False)["input_ids"]]
    assert max(lengths) <= model.max_seq_length, (max(lengths), model.max_seq_length)
    vectors = model.encode(texts, batch_size=8, normalize_embeddings=True, show_progress_bar=False)
    encoded = perf_counter()
    assert len(vectors) == len(texts)

    results = []
    with sqlite3.connect(":memory:") as db:
        db.execute("""CREATE VIRTUAL TABLE passages USING fts5(
            passage_id UNINDEXED, repository UNINDEXED, pr UNINDEXED, base UNINDEXED, head UNINDEXED,
            role UNINDEXED, version UNINDEXED, locator UNINDEXED, body)""")
        db.executemany("INSERT INTO passages VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", passages)
        for index, (name, case, requested_role, question, fts, expected) in enumerate(queries):
            target = targets[case]
            role, release = ROLES[requested_role]
            eligible = [i for i, row in enumerate(passages) if row[1:5] == target
                        and (role is None or row[5:7] == (role, release))]
            allowed = {passages[i][0] for i in eligible}
            assert "control-wrong-head" not in allowed
            assert expected is None or expected in allowed
            query_vector = vectors[len(passages) + index]
            scores = [(passages[i][0], float(vectors[i] @ query_vector)) for i in eligible]
            ranked = sorted(scores, key=lambda pair: (-pair[1], pair[0]))[:2]
            hits = {
                "lexical": lexical(db, fts, target, role, release),
                "rewrite": lexical(db, REWRITES.get(question, fts), target, role, release),
                "embedding": [key for key, _score in ranked],
            }
            assert all(set(found) <= allowed for found in hits.values())
            results.append({"query": name, "expected": expected, "hits": hits,
                            "embedding_scores": [round(score, 6) for _key, score in ranked]})

    summary = {}
    for arm in ("lexical", "rewrite", "embedding"):
        judged = [row for row in results if row["expected"] is not None]
        summary[arm] = {f"hits_at_{k}": sum(row["expected"] in row["hits"][arm][:k] for row in judged)
                        for k in (1, 2)}
    return {"summary": summary, "rows": results, "max_input_tokens": max(lengths),
            "default_sequence_limit": default_sequence_limit, "model_sequence_limit": model.max_seq_length,
            "vector_dimensions": int(vectors.shape[1]),
            "seconds": {"load": round(loaded - start, 3), "encode_batch": round(encoded - loaded, 3),
                        "rank_all": round(perf_counter() - encoded, 3)}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("freeze", "run"))
    parser.add_argument("model", type=Path)
    args = parser.parse_args()
    project_site = HERE.parents[2] / ".venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    assert project_site.is_dir(), "UpgradePilot report-decoder dependencies are unavailable"
    sys.path.append(str(project_site))
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", CUDA_VISIBLE_DEVICES="",
                      TOKENIZERS_PARALLELISM="false", HF_HUB_DISABLE_TELEMETRY="1")
    sys.addaudithook(block_network)
    base = runpy.run_path(str(LEXICAL))
    passages, httpx, opencv = base["load_passages"]()
    fallback = next(row for row in passages if row[0] == "httpx-fallback")
    passages.append(("control-wrong-head", *fallback[1:4], "0" * 40, *fallback[5:]))
    observed = identity(args.model, passages)
    if args.mode == "freeze":
        print(json.dumps(observed, indent=2, sort_keys=True))
        return
    assert json.loads(FREEZE.read_bytes()) == observed, "Comparison freeze mismatch"
    result = compare(args.model, passages, {"httpx": httpx, "opencv": opencv}, base["search"])
    print(json.dumps({"freeze_sha256": digest(FREEZE), **result}, indent=2))


if __name__ == "__main__":
    main()
