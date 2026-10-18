"""Deadline/cancel/interruption proof; no installed backend or model inference."""

import os
import importlib.util
import signal
import time
import unittest
from contextlib import contextmanager

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
