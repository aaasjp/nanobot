from __future__ import annotations

from pathlib import Path

from loguru import logger


def init_logging(
    *,
    log_dir: Path | None = None,
    level: str = "INFO",
    rotation: str = "00:00",
    retention: str = "7 days",
) -> None:
    """
    Initialize global loguru configuration for nanobot.

    - Logs are written to ~/.nanobot/logs by default.
    - One file per day (rotation at midnight), keep recent days only.
    - No logs are printed to the console; all sinks are file-based.
    """
    if log_dir is None:
        log_dir = Path.home() / ".nanobot" / "logs"

    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "nanobot_{time}.log"

    # Remove all existing handlers (including the default stderr sink).
    logger.remove()

    # Add a single file sink with rotation/retention policy.
    logger.add(
        log_path,
        level=level,
        rotation=rotation,
        retention=retention,
        enqueue=True,
        backtrace=True,
        diagnose=False,
    )

