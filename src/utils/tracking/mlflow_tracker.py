"""
DagsHub-hosted MLflow experiment tracking for Decepticon.

Credentials are read from the environment (loaded from .env):
    MLFLOW_TRACKING_URI
    MLFLOW_TRACKING_USERNAME
    MLFLOW_TRACKING_PASSWORD

If MLFLOW_TRACKING_URI is unset, every function here is a safe no-op, so the
application behaves exactly as before when tracking isn't configured.
"""

import os
import sys
import logging
from contextlib import contextmanager

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

_ENABLED = False


def _make_stdio_tolerant():
    """MLflow 3.x prints run/experiment URLs with emoji. On a Windows cp1252
    console those characters raise UnicodeEncodeError and abort end_run(),
    leaving runs stuck in RUNNING. Switch the error handler so unencodable
    characters are escaped instead of crashing (encoding itself is untouched)."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def init_tracking(experiment_name: str = "Decepticon") -> bool:
    """Initialize MLflow tracking against DagsHub. Idempotent; safe to call at startup.

    Returns True if tracking is enabled, False otherwise.
    """
    global _ENABLED

    load_dotenv()
    uri = os.getenv("MLFLOW_TRACKING_URI")
    if not uri:
        logger.info("MLFLOW_TRACKING_URI not set - MLflow tracking disabled")
        _ENABLED = False
        return False

    try:
        import mlflow

        _make_stdio_tolerant()
        mlflow.set_tracking_uri(uri)
        mlflow.set_experiment(experiment_name)

        # Auto-capture LangChain / LangGraph traces (spans, prompts, token usage).
        try:
            mlflow.langchain.autolog()
        except Exception as e:  # autolog is best-effort; never block the app
            logger.warning(f"mlflow.langchain.autolog() unavailable: {e}")

        _ENABLED = True
        logger.info(f"MLflow tracking enabled -> {uri} (experiment: {experiment_name})")
    except Exception as e:
        logger.warning(f"Failed to initialize MLflow tracking, disabling: {e}")
        _ENABLED = False

    return _ENABLED


def is_enabled() -> bool:
    return _ENABLED


def begin_run(run_name=None, params=None, tags=None):
    """Start an MLflow run and log its params/tags. No-op if tracking is disabled."""
    if not _ENABLED:
        return None
    try:
        import mlflow

        run = mlflow.start_run(run_name=run_name)
        if params:
            mlflow.log_params({k: v for k, v in params.items() if v is not None})
        if tags:
            mlflow.set_tags({k: v for k, v in tags.items() if v is not None})
        return run
    except Exception as e:
        logger.warning(f"MLflow begin_run failed: {e}")
        return None


def end_run():
    """End the active MLflow run, if any. No-op if tracking is disabled.

    Guarantees the run is terminated as FINISHED even if MLflow's own URL
    printing raises on a limited console encoding.
    """
    if not _ENABLED:
        return
    try:
        import mlflow

        run = mlflow.active_run()
        if run is None:
            return
        run_id = run.info.run_id
        try:
            mlflow.end_run()
        except Exception as e:
            logger.warning(f"mlflow.end_run() raised (likely console encoding), forcing terminate: {e}")
        # Belt-and-suspenders: ensure the run is marked FINISHED regardless.
        try:
            from mlflow.tracking import MlflowClient

            if MlflowClient().get_run(run_id).info.status != "FINISHED":
                MlflowClient().set_terminated(run_id, status="FINISHED")
        except Exception as e:
            logger.warning(f"MLflow set_terminated failed: {e}")
    except Exception as e:
        logger.warning(f"MLflow end_run failed: {e}")


@contextmanager
def start_run(run_name=None, params=None, tags=None):
    """Context-manager form of begin_run/end_run."""
    begin_run(run_name=run_name, params=params, tags=tags)
    try:
        yield
    finally:
        end_run()


def log_metrics(metrics: dict):
    """Log a dict of numeric metrics. No-op if tracking is disabled."""
    if not _ENABLED:
        return
    try:
        import mlflow

        clean = {k: float(v) for k, v in metrics.items() if v is not None}
        if clean:
            mlflow.log_metrics(clean)
    except Exception as e:
        logger.warning(f"MLflow log_metrics failed: {e}")


def log_artifact(path: str):
    """Attach a file (e.g. a session log) to the active run. No-op if disabled."""
    if not _ENABLED or not path or not os.path.exists(path):
        return
    try:
        import mlflow

        mlflow.log_artifact(path)
    except Exception as e:
        logger.warning(f"MLflow log_artifact failed: {e}")
