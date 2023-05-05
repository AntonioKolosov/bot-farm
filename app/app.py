"""
"""

from typing import Dict

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hookrouter, testrouter
from app.tapiclient import tapiclientwebhook as t_wh
from .internals.tbotlogger import tb_log


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)


app.include_router(hookrouter.router)
app.include_router(testrouter.router)


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.on_event("startup")
async def set_webhook():
    """Register web hook on TG"""
    await t_wh.set_webhook()
    tb_log.log_info("Startup")


@app.on_event("shutdown")
async def unset_webhook():
    """Unregister web hook"""
    await t_wh.unset_webhook()
    tb_log.log_info("Shutdown")
