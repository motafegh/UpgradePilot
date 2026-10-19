"""Offline counterexample for the exact SDK's interrupted receive ownership.

No client, websocket, model, tokenization or prediction is created. The installed
SDK queue getter and SyncChannel run against a local asyncio.Queue. Synthetic
terminal events establish event routing only, never actual runtime usage. Run
from the repository root with PYTHONPATH=src:.; select the preserved SDK explicitly.
"""

import argparse
import asyncio
from contextlib import contextmanager
from functools import partial
from hashlib import sha256
import json
from pathlib import Path
import sys
import threading
from types import SimpleNamespace


def runtime_observation(root, activation):
    def read(relative):
        return json.loads((root / relative).read_bytes())

    def digest(relative):
        return sha256((root / relative).read_bytes()).hexdigest()

    summary = read("summary.json")
    row, *unattempted = summary["rows"]
    receipt = read("probe-cancel/call-01.receipt.json")
    request = read("probe-cancel/call-01.request.json")
    attempt = read("probe-cancel/call-01.attempt.json")
    reservation = read("probe-cancel.reservation.json")
    cleanup, client = read("cleanup.json"), read("client-cleanup.json")
    assert [item["role"] for item in summary["rows"]] == activation["roles"]
    assert row == read("probe-cancel.result.json")
    assert row["execution"] == "failed" and row["prediction_attempts"] == 1
    assert row["model_receipts"] == [receipt] and not row["usage_complete"]
    assert all(item["execution"] == "unattempted" for item in unattempted)
    assert all(item["semantic_acceptance"] == "not_evaluated" for item in summary["rows"])
    assert len(list(root.rglob("*.attempt.json"))) == 1
    assert not (root / "probe-cancel/call-01.metadata.json").exists()
    assert row["report_publication"] is None and row["termination_id"]
    assert receipt["usage"] is None and not receipt["complete_response_received"]
    assert receipt["request_sha256"] == attempt["request_sha256"] == digest("probe-cancel/call-01.request.json")
    assert request["packed_input_sha256"] == digest("probe-cancel/call-01.packed-input.json")
    assert request["rendered_sha256"] == digest("probe-cancel/call-01.rendered.txt")
    assert receipt["visible_fragments_sha256"] == digest("probe-cancel/call-01.visible-fragments.txt")
    assert receipt["visible_fragment_bytes"] == 0
    assert request["omitted_events"] == []
    assert 0 < request["rendered_tokens"] == attempt["reserved_input_tokens"] <= 4096
    assert reservation["rendered_tokens"] == row["rendered_tokens"]
    assert row["unknown_usage_reservation"] == {"input": 4096, "generated": 8192}
    control = receipt["control"]
    assert control["cancellation_requested"] and control["channel_released"]
    assert not control["terminal_received"] and control["runtime_quiescence"] == "unconfirmed"
    assert control["primary_problem"] == "PredictionDeadlineExceeded: prediction monotonic deadline reached"
    assert control["secondary_problems"] == [
        "ValueError: prediction channel ended without a terminal response"]
    spend = summary["measured_known_usage"]
    assert spend["known_usage_attempts"] == 0 and spend["unknown_usage_attempts"] == 1
    assert spend["input"] == 0 and spend["generated"] == 0
    assert spend["operations"] == row["charges"]["admission_operations"] == 12
    assert cleanup["confirmed"] and cleanup["remaining_identifiers"] == [] and client["confirmed"]
    assert summary["problem"] == "ValueError: unknown usage; whole remaining cohort withheld"
    assert sha256(Path(activation["reviewer"]["path"]).read_bytes()).hexdigest() == activation["reviewer"]["sha256"]
    return {
        "format": "investigator-activated-diagnostic-result/1",
        "base_commit": activation["base_commit"], "freeze_sha256": activation["freeze_sha256"],
        "diagnostic_root": str(root), "disposition": "incomplete/inconclusive; control gate failed",
        "prediction_attempts": 1, "known_usage_attempts": 0, "unknown_usage_attempts": 1,
        "semantic_cases_attempted": 0, "semantic_cases_reviewable": 0,
        "unattempted_roles": [item["role"] for item in unattempted],
        "problem": summary["problem"], "probe_receipt": receipt,
        "observed_request": {"preliminary_rendered_tokens": row["rendered_tokens"],
                             "callback_rendered_tokens": request["rendered_tokens"],
                             "callback_input_reservation": attempt["reserved_input_tokens"],
                             "role_input_reservation": 4096, "generated_reservation": 8192,
                             "omitted_events": request["omitted_events"]},
        "measured_known_usage": spend, "batch_elapsed_seconds": summary["batch_elapsed_seconds"],
        "owned_runtime_cleanup": cleanup, "client_cleanup": client,
        "artifact_sha256": {str(path.relative_to(root)): sha256(path.read_bytes()).hexdigest()
                            for path in sorted(root.rglob("*")) if path.is_file()},
        "limits": ["Zero known token subtotals are not zero actual consumption.",
                   "No terminal usage/configuration receipt; no semantic verdict.",
                   "Owned unload is confirmed later and does not recover terminal usage.",
                   "No live wire trace was retained; offline queue loss is a sufficient mechanism.",
                   "No retry, resumed cohort or inference repair was performed."]}


def counterexample(kind):
    from lmstudio._ws_impl import AsyncWebsocketHandler
    from lmstudio.sync_api import SyncChannel
    from experiments.investigator_run_control import receive_controlled_prediction

    loop = asyncio.new_event_loop()
    thread = threading.Thread(target=loop.run_forever, daemon=True)
    thread.start()
    futures, sent, yielded = [], [], []
    started = threading.Event()

    def submit(coroutine):
        async def tracked():
            started.set()
            return await coroutine

        future = asyncio.run_coroutine_threadsafe(tracked(), loop)
        futures.append(future)
        return future

    handler = SimpleNamespace(
        _task_manager=SimpleNamespace(run_coroutine_threadsafe=submit)
    )
    queue = asyncio.Queue()
    getter = partial(AsyncWebsocketHandler._rx_queue_get_threadsafe, handler, queue)
    success = {"type": "channelSend", "channelId": 1,
               "message": {"type": "success"}}
    close = {"type": "channelClose", "channelId": 1}

    async def enqueue():
        queue.put_nowait(success)
        queue.put_nowait(close)

    class Endpoint:
        notice_prefix = "offline synthetic queue counterexample"
        is_finished = False

        def iter_message_events(self, contents):
            yielded.append(contents["type"])
            self.is_finished = contents["type"] == "success"
            return ()

        def result(self):
            return "synthetic terminal only"

    def send(message):
        assert started.is_set(), "receive must be pending before cancellation"
        sent.append(message)
        asyncio.run_coroutine_threadsafe(enqueue(), loop).result(1)

    endpoint = Endpoint()
    channel = SyncChannel(
        1, getter, endpoint, send, {},
        timeout=.02 if kind == "sdk-idle-timeout" else 5,
    )

    @contextmanager
    def opened():
        if kind == "ordinary-terminal":
            asyncio.run_coroutine_threadsafe(enqueue(), loop).result(1)
        yield channel

    control, problem = {}, None
    try:
        try:
            receive_controlled_prediction(
                opened(), endpoint, .08 if kind == "monotonic-interruption" else .5,
                control, finalization_seconds=.5,
            )
        except BaseException as error:
            problem = f"{type(error).__name__}: {error}"
        received = []
        for future in futures:
            if future.cancelled():
                received.append({"state": "cancelled"})
            elif future.done():
                message = future.result()
                received.append({"state": "completed", "wire_type": message["type"],
                                 "message_type": message.get("message", {}).get("type")})
            else:
                received.append({"state": "pending"})
        if kind == "monotonic-interruption":
            assert problem.startswith("PredictionDeadlineExceeded:")
            assert received[0]["message_type"] == "success"
            assert received[1]["wire_type"] == "channelClose"
            assert yielded == [] and not control["terminal_received"]
            assert control["runtime_quiescence"] == "unconfirmed"
            assert control["secondary_problems"] == [
                "ValueError: prediction channel ended without a terminal response"]
        elif kind == "sdk-idle-timeout":
            assert problem.startswith("LMStudioTimeoutError:")
            assert received[0]["state"] == "cancelled"
            assert received[1]["message_type"] == "success"
            assert control["terminal_received"] and yielded == ["success"]
        else:
            assert problem is None and control["terminal_received"]
            assert yielded == ["success"]
        return {"case": kind, "primary_problem": problem, "control": control,
                "sent": sent, "queue_receive_futures": received,
                "events_delivered_to_endpoint": yielded,
                "synthetic_terminal_observed": endpoint.is_finished}
    finally:
        async def cleanup():
            current = asyncio.current_task()
            pending = [task for task in asyncio.all_tasks() if task is not current]
            for task in pending:
                task.cancel()
            await asyncio.gather(*pending, return_exceptions=True)

        asyncio.run_coroutine_threadsafe(cleanup(), loop).result(1)
        loop.call_soon_threadsafe(loop.stop)
        thread.join(1)
        assert not thread.is_alive()
        loop.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-site", required=True, type=Path)
    parser.add_argument("--diagnostic-root", required=True, type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.sdk_site))
    frozen = json.loads((args.diagnostic_root / "executed-freeze.json").read_bytes())
    activation = json.loads((Path(__file__).parent / "diagnostic-activation.json").read_bytes())
    for relative, expected in activation["source_sha256"].items():
        assert sha256(Path(relative).read_bytes()).hexdigest() == expected
    for relative, expected in activation["sdk_source_sha256"].items():
        assert sha256((args.sdk_site / "lmstudio" / relative).read_bytes()).hexdigest() == expected
    assert sha256((Path(activation["freeze_path"])).read_bytes()).hexdigest() == activation["freeze_sha256"]
    assert frozen == json.loads(Path(activation["freeze_path"]).read_bytes())
    result = {"format": "investigator-cancellation-queue-analysis/1",
              "prediction_attempts": 0, "network_connections": 0,
              "source_and_sdk_hashes_match_activation": True,
              "cases": [counterexample(kind) for kind in
                        ("ordinary-terminal", "monotonic-interruption", "sdk-idle-timeout")],
              "limits": [
                  "Synthetic local queue and endpoint; no actual server wire trace or usage.",
                  "Proves a sufficient receive-loss mechanism, not the exact live wire sequence.",
                  "Does not repair implementation, qualify cancellation or authorize another call."]}
    print(json.dumps({"runtime_result": runtime_observation(args.diagnostic_root, activation),
                      "offline_queue_analysis": result}, indent=2))


if __name__ == "__main__":
    main()
