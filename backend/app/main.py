"""Local foundation API; product routes are added behind their release gates."""

import os

from fastapi import FastAPI

if os.environ.get("BUGAI_MODE", "local") != "local":
    raise RuntimeError("Only local mode is supported by the foundation")

app = FastAPI(title="BugAI foundation", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "stage": "foundation"}


@app.get("/ready")
def ready() -> dict[str, str]:
    # No database, broker, or AI adapter is connected at this stage.
    return {"status": "ready", "stage": "foundation"}
