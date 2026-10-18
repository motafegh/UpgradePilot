"""Same-thread deadline and cancellation ownership for the WSL experiment runner.

`receive_controlled_prediction` owns one synchronous SDK channel through receipt or
bounded cancellation/drain/release. It does not unload models or infer usage from
elapsed time. SDKBinding captures scalar terminal metadata; its caller validates usage
and blocks reuse after failure. A sent cancel is never a server-completion receipt.

POSIX timers are deliberately scoped to the main thread with no other timer owner.
They interrupt silent SDK queue waits as well as continuous Python fragment handling.
This is handled-process control, not protection from SIGKILL or uninterruptible kernel
I/O. Actual installed-backend cancellation still requires its separately admitted probe.
"""

from __future__ import annotations

import math
import signal
import threading
import time
from contextlib import contextmanager


class PredictionDeadlineExceeded(Exception):
    """The monotonic prediction or finalization allowance was exhausted.

    Deliberately not TimeoutError: SDK 1.5.0 catches that built-in (also the
    concurrent.futures timeout alias) and would relabel this total deadline as idle.
    """


def problem_text(error):
    return f"{type(error).__name__}: {error}"


class MonotonicDeadline:
    """Temporary process timer; UTC/file dates never participate in enforcement.

    The signal wakes blocking receive calls. Explicit checks also make continuously
    available messages obey the same absolute deadline and permit fake-clock proof.
    Existing timer/signal owners are refused rather than overwritten.
    """

    def __init__(self, seconds, *, clock=time.monotonic, label="prediction"):
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError("deadline allowance must be finite and positive")
        self.clock, self.label = clock, label
        self.expires = clock() + seconds

    def check(self):
        remaining = self.expires - self.clock()
        if remaining <= 0:
            raise PredictionDeadlineExceeded(f"{self.label} monotonic deadline reached")
        return remaining

    @contextmanager
    def enforce(self):
        if (
            threading.current_thread() is not threading.main_thread()
            or not hasattr(signal, "setitimer")
        ):
            raise ValueError("prediction deadline requires the POSIX main thread")
        if signal.getitimer(signal.ITIMER_REAL) != (0.0, 0.0):
            raise ValueError("another owner already holds the process timer")
        previous_alarm = signal.getsignal(signal.SIGALRM)
        previous_term = signal.getsignal(signal.SIGTERM)
        if previous_alarm != signal.SIG_DFL:
            raise ValueError("another owner already holds SIGALRM")

        def alarm(signum, frame):
            # An early wake cannot shorten the declared monotonic allowance.
            signal.setitimer(signal.ITIMER_REAL, self.check())

        def terminate(signum, frame):
            raise SystemExit(128 + signum)

        signal.signal(signal.SIGALRM, alarm)
        signal.signal(signal.SIGTERM, terminate)
        try:
            signal.setitimer(signal.ITIMER_REAL, self.check())
            yield self
            self.check()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, previous_alarm)
            signal.signal(signal.SIGTERM, previous_term)


def receive_controlled_prediction(
    channel_context,
    endpoint,
    seconds,
    control,
    *,
    finalization_seconds=60,
    clock=time.monotonic,
):
    """Read an SDK-shaped channel, preserving the primary exception on all exits.

    Endpoint parsing/filtering remains SDKBinding's responsibility. `control` is an
    attempt-local mutable accounting record retained even when BaseException escapes.
    Terminal endpoint completion confirms this prediction's protocol completion only;
    model ownership/unload confirmation remains with the orchestration caller.
    """
    if not 0 < finalization_seconds <= 60:
        raise ValueError("cancel/drain/release allowance must be at most 60 seconds")
    started = clock()
    deadline = MonotonicDeadline(seconds, clock=clock)
    channel = result = primary = traceback = None
    entered = False
    control.update(
        dispatch_reserved=True,
        channel_opened=False,
        cancellation_requested=False,
        terminal_received=False,
        channel_released=False,
        secondary_problems=[],
        deadline_seconds=seconds,
        finalization_allowance_seconds=finalization_seconds,
    )

    def receive(bound):
        for contents in channel.rx_stream():
            # Handle a terminal receipt before the post-message deadline check so a
            # late success preserves known usage without becoming an on-time success.
            for event in endpoint.iter_message_events(contents):
                endpoint.handle_rx_event(event)
            control["terminal_received"] = bool(endpoint.is_finished)
            bound.check()
            if endpoint.is_finished:
                return endpoint.result()
        raise ValueError("prediction channel ended without a terminal response")

    try:
        with deadline.enforce():
            channel = channel_context.__enter__()
            entered = True
            control["channel_opened"] = True
            deadline.check()
            result = receive(deadline)
    except BaseException as error:
        primary, traceback = error, error.__traceback__
        control["primary_problem"] = problem_text(error)
    finally:
        control["prediction_elapsed_seconds"] = clock() - started
        finalizing = clock()
        if entered:
            try:
                with MonotonicDeadline(
                    finalization_seconds, clock=clock, label="cancel/drain/release"
                ).enforce() as finalization:
                    try:
                        if primary is not None and not endpoint.is_finished:
                            control["cancellation_requested"] = True
                            channel.cancel()
                            finalization.check()
                            receive(finalization)
                    except BaseException as error:
                        control["secondary_problems"].append(problem_text(error))
                    finally:
                        # Release is attempted even if cancellation/drain failed. It
                        # shares the same allowance rather than receiving another 60s.
                        finalization.check()
                        channel_context.__exit__(None, None, None)
                        control["channel_released"] = True
            except BaseException as error:
                if primary is None:
                    primary, traceback = error, error.__traceback__
                    control["primary_problem"] = problem_text(error)
                else:
                    control["secondary_problems"].append(problem_text(error))
        control["finalization_elapsed_seconds"] = clock() - finalizing
        control["prediction_elapsed_bound_met"] = (
            control["prediction_elapsed_seconds"] < seconds
        )
        control["runtime_quiescence"] = (
            "terminal_protocol_received"
            if control["terminal_received"]
            else "unconfirmed"
        )
    if primary is not None:
        raise primary.with_traceback(traceback)
    return result
