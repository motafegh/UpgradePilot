"""Deadline/cancel/interruption proof; no installed backend or model inference."""

import os
import asyncio
import importlib.util
import signal
import threading
import time
import unittest
from contextlib import contextmanager
from types import SimpleNamespace

from experiments.investigator_run_control import (
    MonotonicDeadline,
    PredictionDeadlineExceeded,
    receive_controlled_prediction,
)


class Endpoint:
    def __init__(self):
        self.is_finished = False
        self.metadata = None

    def iter_message_events(self, contents):
        if contents == "success":
            self.is_finished = True
            self.metadata = {"actual_usage": 7}
        return ()

    def result(self):
        return b"complete"


class Channel:
    def __init__(self, receive, *, release_error=None):
        self.receive = receive
        self.cancelled = False
        self.released = False
        self.release_error = release_error

    def rx_stream(self):
        yield from self.receive(self)

    def cancel(self):
        self.cancelled = True

    @contextmanager
    def open(self):
        try:
            yield self
        finally:
            self.released = True
            if self.release_error:
                raise self.release_error


class PredictionControlTests(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec("lmstudio"), "optional preserved SDK not selected")
    def test_sdk_prompt_progress_is_retained_as_scalar_before_interruption(self):
        import lmstudio
        from contextlib import nullcontext
        from unittest.mock import patch
        from experiments.investigator_model_interface import SDKBinding
        model = SimpleNamespace(identifier="synthetic-progress-only",
            _session=SimpleNamespace(_create_channel=lambda endpoint: nullcontext()))
        binding = SDKBinding(model, lmstudio, {})
        measured = SimpleNamespace(messages={"messages": [{"role": "user", "content": "Synthetic progress only"}]}, configuration={"layers": []})
        def observe(context, endpoint, seconds, control, **kwargs):
            for event in endpoint.iter_message_events({"type": "promptProcessingProgress", "progress": .25}):
                endpoint.handle_rx_event(event)
            raise KeyboardInterrupt("after prompt progress")
        with patch("experiments.investigator_model_interface.receive_controlled_prediction", side_effect=observe):
            with self.assertRaisesRegex(KeyboardInterrupt, "after prompt progress"):
                binding.predict(measured, .1, visible_sink=lambda content: None)
        self.assertEqual(binding.last_prediction_control["last_reported_prompt_processing_progress"], .25)

    @unittest.skipUnless(importlib.util.find_spec("lmstudio"), "optional preserved SDK not selected")
    def test_sdk_prediction_restores_rpc_idle_timeout_after_interruption(self):
        import lmstudio
        from types import SimpleNamespace
        from experiments.investigator_model_interface import SDKBinding
        @contextmanager
        def interrupted_channel():
            raise KeyboardInterrupt("channel entry interrupted")
            yield
        model = SimpleNamespace(identifier="synthetic-channel-only",
            _session=SimpleNamespace(_create_channel=lambda endpoint: interrupted_channel()))
        binding = SDKBinding(model, lmstudio, {})
        measured = SimpleNamespace(messages={"messages": [{"role": "user", "content": "Synthetic control only"}]}, configuration={"layers": []})
        previous = lmstudio.get_sync_api_timeout()
        lmstudio.set_sync_api_timeout(17)
        try:
            with self.assertRaisesRegex(KeyboardInterrupt, "channel entry interrupted"):
                binding.predict(measured, .1, visible_sink=lambda content: None)
            self.assertEqual(lmstudio.get_sync_api_timeout(), 17)
            self.assertFalse(binding.last_prediction_control["channel_opened"])
        finally:
            lmstudio.set_sync_api_timeout(previous)

    @unittest.skipUnless(importlib.util.find_spec("lmstudio"), "optional preserved SDK not selected")
    def test_installed_sdk_queue_wait_interrupts_and_cancel_uses_same_channel(self):
        from concurrent.futures import Future
        from lmstudio.sync_api import SyncChannel
        future, sent = Future(), []
        class SDKEndpoint(Endpoint):
            notice_prefix = "deterministic SDK channel control"
            def iter_message_events(self, contents):
                return super().iter_message_events(contents["type"])
        endpoint = SDKEndpoint()
        def send(message):
            sent.append(message)
            future.set_result({"type": "channelSend", "channelId": 1, "message": {"type": "success"}})
        channel = SyncChannel(1, future.result, endpoint, send, {}, timeout=5)
        @contextmanager
        def opened():
            yield channel
        control = {}
        with self.assertRaises(PredictionDeadlineExceeded):
            receive_controlled_prediction(opened(), endpoint, .03, control)
        self.assertEqual(sent, [{"type": "channelSend", "channelId": 1, "message": {"type": "cancel"}}])
        self.assertTrue(control["terminal_received"])

    def test_silence_interrupts_blocking_wait_and_bounded_drain(self):
        def silence(channel):
            if channel.cancelled:
                yield "success"
            else:
                time.sleep(5)
                yield "too late"

        channel, endpoint, control = Channel(silence), Endpoint(), {}
        started = time.monotonic()
        with self.assertRaises(PredictionDeadlineExceeded):
            receive_controlled_prediction(channel.open(), endpoint, .03, control)
        self.assertLess(time.monotonic() - started, 2)
        self.assertTrue(control["cancellation_requested"])
        self.assertTrue(control["terminal_received"])
        self.assertTrue(control["channel_released"])
        self.assertEqual(endpoint.metadata, {"actual_usage": 7})

    def test_continuous_fragments_use_absolute_monotonic_deadline(self):
        now = [100.0]

        def continuous(channel):
            while not channel.cancelled:
                now[0] += .25
                yield "fragment"
            yield "success"

        channel, control = Channel(continuous), {}
        with self.assertRaises(PredictionDeadlineExceeded):
            receive_controlled_prediction(
                channel.open(), Endpoint(), 1, control, clock=lambda: now[0]
            )
        self.assertEqual(control["prediction_elapsed_seconds"], 1)
        self.assertFalse(control["prediction_elapsed_bound_met"])
        self.assertTrue(control["terminal_received"])

    def test_late_success_retains_terminal_fact_but_is_failed(self):
        now = [10.0]

        def late(channel):
            now[0] += 2
            yield "success"

        control, endpoint = {}, Endpoint()
        with self.assertRaises(PredictionDeadlineExceeded):
            receive_controlled_prediction(
                Channel(late).open(), endpoint, 1, control, clock=lambda: now[0]
            )
        self.assertFalse(control["cancellation_requested"])
        self.assertTrue(control["terminal_received"])
        self.assertIsNotNone(endpoint.metadata)

    def test_cancel_without_terminal_receipt_remains_unconfirmed(self):
        def incomplete(channel):
            if not channel.cancelled:
                raise KeyboardInterrupt("operator interrupted")
            return
            yield

        control = {}
        with self.assertRaises(KeyboardInterrupt):
            receive_controlled_prediction(Channel(incomplete).open(), Endpoint(), 1, control)
        self.assertEqual(control["runtime_quiescence"], "unconfirmed")
        self.assertTrue(control["channel_released"])
        self.assertTrue(control["secondary_problems"])

    def test_cancel_drain_has_its_own_finite_bound(self):
        def hung(channel):
            if not channel.cancelled:
                raise KeyboardInterrupt("primary")
            time.sleep(5)
            yield "success"

        control = {}
        started = time.monotonic()
        with self.assertRaisesRegex(KeyboardInterrupt, "primary"):
            receive_controlled_prediction(
                Channel(hung).open(), Endpoint(), 1, control, finalization_seconds=.03
            )
        self.assertLess(time.monotonic() - started, 2)
        self.assertFalse(control["terminal_received"])
        self.assertTrue(control["secondary_problems"])

    def test_sigterm_is_accounted_and_reraised_after_cancel(self):
        previous = signal.getsignal(signal.SIGTERM)

        def stopped(channel):
            if not channel.cancelled:
                os.kill(os.getpid(), signal.SIGTERM)
            yield "success"

        control = {}
        with self.assertRaises(SystemExit) as raised:
            receive_controlled_prediction(Channel(stopped).open(), Endpoint(), 1, control)
        self.assertEqual(raised.exception.code, 143)
        self.assertTrue(control["terminal_received"])
        self.assertEqual(signal.getsignal(signal.SIGTERM), previous)

    def test_primary_interruption_survives_channel_release_failure(self):
        def stopped(channel):
            if not channel.cancelled:
                raise KeyboardInterrupt("primary")
            yield "success"

        control = {}
        with self.assertRaisesRegex(KeyboardInterrupt, "primary"):
            receive_controlled_prediction(
                Channel(stopped, release_error=OSError("release failed")).open(),
                Endpoint(), 1, control,
            )
        self.assertIn("OSError: release failed", control["secondary_problems"])
        self.assertFalse(control["channel_released"])

    def test_success_and_existing_timer_owner_are_distinct(self):
        control = {}
        channel = Channel(lambda channel: iter(["success"]))
        self.assertEqual(
            receive_controlled_prediction(channel.open(), Endpoint(), 1, control),
            b"complete",
        )
        self.assertTrue(control["prediction_elapsed_bound_met"])
        signal.setitimer(signal.ITIMER_REAL, 10)
        try:
            with self.assertRaisesRegex(ValueError, "another owner"):
                with MonotonicDeadline(1).enforce():
                    self.fail("must refuse before disturbing timer owner")
            self.assertGreater(signal.getitimer(signal.ITIMER_REAL)[0], 0)
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)


@unittest.skipUnless(importlib.util.find_spec("lmstudio"), "optional preserved SDK not selected")
class RetainedSDKQueueTests(unittest.TestCase):
    """Use the actual SDK queue/getter/handler shape, with no network or model."""

    @contextmanager
    def queue_channel(self, reply="success", *, delay=0, initial=(), hook=None):
        from lmstudio._ws_impl import AsyncWebsocketHandler
        from lmstudio.sync_api import SyncChannel
        from experiments.investigator_model_interface import retained_prediction_channel

        loop = asyncio.new_event_loop()
        previous_handlers = {kind: signal.getsignal(kind) for kind in
                             (signal.SIGALRM, signal.SIGINT, signal.SIGTERM)}
        thread = threading.Thread(target=loop.run_forever, daemon=True)
        thread.start()
        sent, control = [], {}

        def submit(coroutine):
            return asyncio.run_coroutine_threadsafe(coroutine, loop)

        handler = object.__new__(AsyncWebsocketHandler)
        handler._task_manager = SimpleNamespace(run_coroutine_threadsafe=submit)
        queue, getter = handler.new_threadsafe_rx_queue()

        def wire(kind):
            if kind == "channelClose":
                return {"type": kind, "channelId": 1}
            return {"type": "channelSend", "channelId": 1, "message": {"type": kind}}

        async def enqueue(kinds, after=0):
            await asyncio.sleep(after)
            for sequence, kind in enumerate(kinds):
                message = wire(kind)
                if kind == "fragment":
                    message["message"]["sequence"] = sequence
                queue.put_nowait(message)

        class SDKEndpoint(Endpoint):
            notice_prefix = "local retained queue proof"
            def iter_message_events(self, contents):
                result = super().iter_message_events(contents["type"])
                if hook:
                    hook(self, contents)
                return result
            def handle_rx_event(self, event):
                pass

        endpoint = SDKEndpoint()
        def send(message):
            sent.append(message)
            if reply:
                kinds = [reply, "channelClose"] if reply != "channelClose" else [reply]
                submit(enqueue(kinds, delay))
        channel = SyncChannel(1, getter, endpoint, send, {}, timeout=.001)
        @contextmanager
        def opened():
            if initial:
                submit(enqueue(initial)).result(1)
            yield channel
        try:
            yield retained_prediction_channel(opened(), control), endpoint, control, sent, channel
        finally:
            async def cleanup():
                current = asyncio.current_task()
                tasks = [task for task in asyncio.all_tasks() if task is not current]
                for task in tasks:
                    task.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
            submit(cleanup()).result(1)
            loop.call_soon_threadsafe(loop.stop)
            thread.join(1)
            self.assertFalse(thread.is_alive())
            loop.close()
            for kind, previous in previous_handlers.items():
                self.assertEqual(signal.getsignal(kind), previous)

    def test_blocked_queue_deadline_retains_reply_for_same_receive(self):
        with self.queue_channel() as (context, endpoint, control, sent, _):
            with self.assertRaises(PredictionDeadlineExceeded):
                receive_controlled_prediction(context, endpoint, .03, control, finalization_seconds=.3)
            self.assertTrue(control["terminal_received"])
            self.assertTrue(control["channel_released"])
            self.assertEqual(control["secondary_problems"], [])
            self.assertEqual(len(sent), 1)
            ownership = control["receive_ownership"]
            self.assertEqual(ownership["submitted"], 1)
            self.assertEqual(ownership["pending_reuses"], 1)
            self.assertEqual(ownership["events"], {"success": 1})
            self.assertTrue(ownership["receiver_stopped"])

    def test_already_dequeued_success_survives_interruption_before_dispatch(self):
        with self.queue_channel(reply=None, initial=("success", "channelClose")) as (context, endpoint, control, _, channel):
            original = channel._api_channel.handle_rx_message
            first = [True]
            def interrupted(message):
                result = original(message)
                if first[0]:
                    first[0] = False
                    raise KeyboardInterrupt("after dequeue, before endpoint")
                return result
            channel._api_channel.handle_rx_message = interrupted
            with self.assertRaisesRegex(KeyboardInterrupt, "after dequeue"):
                receive_controlled_prediction(context, endpoint, .3, control, finalization_seconds=.3)
            self.assertTrue(control["terminal_received"])
            self.assertEqual(endpoint.metadata, {"actual_usage": 7})
            self.assertEqual(control["receive_ownership"]["submitted"], 1)
            self.assertEqual(control["receive_ownership"]["events"], {"success": 1})

    def test_sigint_during_terminal_handoff_preserves_metadata_once(self):
        def interrupt(endpoint, contents):
            if contents["type"] == "success":
                os.kill(os.getpid(), signal.SIGINT)
        with self.queue_channel(reply=None, initial=("success",), hook=interrupt) as (context, endpoint, control, sent, _):
            with self.assertRaises(KeyboardInterrupt):
                receive_controlled_prediction(context, endpoint, .3, control, finalization_seconds=.3)
            self.assertTrue(control["terminal_received"])
            self.assertFalse(control["cancellation_requested"])
            self.assertEqual(control["receive_ownership"]["acknowledged"], 1)
            self.assertEqual(endpoint.metadata, {"actual_usage": 7})
            self.assertEqual(sent, [])

    def test_sigterm_during_terminal_handoff_is_preserved_as_exit(self):
        def interrupt(endpoint, contents):
            if contents["type"] == "success":
                os.kill(os.getpid(), signal.SIGTERM)
        with self.queue_channel(reply=None, initial=("success",), hook=interrupt) as (context, endpoint, control, _, _):
            with self.assertRaises(SystemExit) as raised:
                receive_controlled_prediction(context, endpoint, .3, control, finalization_seconds=.3)
            self.assertEqual(raised.exception.code, 143)
            self.assertTrue(control["terminal_received"])
            self.assertEqual(control["receive_ownership"]["events"], {"success": 1})

    def test_continuous_queue_fragments_are_acknowledged_once_across_deadline(self):
        seen = []
        def fragment(endpoint, contents):
            if contents["type"] == "fragment":
                seen.append(contents["sequence"])
                time.sleep(.002)
        with self.queue_channel(initial=("fragment",) * 20, hook=fragment) as (context, endpoint, control, _, _):
            with self.assertRaises(PredictionDeadlineExceeded):
                receive_controlled_prediction(context, endpoint, .01, control, finalization_seconds=.3)
            self.assertEqual(seen, list(range(20)))
            self.assertTrue(control["terminal_received"])
            self.assertEqual(control["receive_ownership"]["events"], {"fragment": 20, "success": 1})

    def test_delayed_cancel_reply_uses_finalization_bound_not_prediction_idle(self):
        with self.queue_channel(delay=.06) as (context, endpoint, control, _, _):
            with self.assertRaises(PredictionDeadlineExceeded):
                receive_controlled_prediction(context, endpoint, .02, control, finalization_seconds=.3)
            self.assertTrue(control["terminal_received"])
            self.assertGreater(control["finalization_elapsed_seconds"], .04)
            self.assertEqual(control["secondary_problems"], [])

    def test_missing_terminal_stays_unknown_after_channel_close(self):
        with self.queue_channel(reply="channelClose") as (context, endpoint, control, _, _):
            with self.assertRaises(PredictionDeadlineExceeded):
                receive_controlled_prediction(context, endpoint, .02, control, finalization_seconds=.3)
            self.assertFalse(control["terminal_received"])
            self.assertEqual(control["runtime_quiescence"], "unconfirmed")
            self.assertTrue(control["channel_released"])
            self.assertEqual(control["receive_ownership"]["events"], {"channelClose": 1})

    def test_silent_cancel_is_finite_and_pending_receive_cancellation_is_recorded(self):
        with self.queue_channel(reply=None) as (context, endpoint, control, _, _):
            started = time.monotonic()
            with self.assertRaises(PredictionDeadlineExceeded):
                receive_controlled_prediction(context, endpoint, .02, control, finalization_seconds=.03)
            self.assertLess(time.monotonic() - started, .5)
            self.assertFalse(control["terminal_received"])
            self.assertTrue(control["receive_ownership"]["pending_cancel_requested"])
            self.assertTrue(control["secondary_problems"])
