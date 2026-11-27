from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AI customer support")

DASHBOARD_DIR = Path(__file__).resolve().parent.parent / "dashboard" / "dist"


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# Serve the built dashboard at /. Mounted last, so API routes above take priority.
# Build it with `npm run build` in dashboard/, or use Docker, which builds it for you.
if DASHBOARD_DIR.is_dir():
    app.mount("/", StaticFiles(directory=DASHBOARD_DIR, html=True), name="dashboard")
