"""
Set webhooks/unset webhooks
"""

from typing import Dict

from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

from .description import description, title, version, license, contact
from src.gtw.routers import inc_data_router, testrouter
from src.internals.tbotlogger import tb_log
from src.services import services

app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)

load_dotenv()

app.include_router(inc_data_router.router)
app.include_router(testrouter.router)

# Temporary - will be moved to DB and loaded via a loader
# app.mount("/prompter",
# StaticFiles(directory="static/prompter",
# html=True))
app.mount("/viewer", StaticFiles(directory="static/viewer", html=True))


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.on_event("startup")
async def set_webhook():
    """Register web hook on TG"""
    await services.startup()
    tb_log.log_info("Startup")
    # Prime the push notification generator
    await testrouter.notifier.generator.asend(None)


@app.on_event("shutdown")
async def unset_webhook():
    """Unregister web hook"""
    await services.shutdown()
    tb_log.log_info("Shutdown")
