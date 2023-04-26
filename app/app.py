"""
"""

from typing import Dict

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hook
from .tbotapi.tbotapiconfig import TbotAPIConfig


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)


app.include_router(hook.router)


tb_api = TbotAPIConfig()


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.on_event("startup")
async def set_webhook():
    """Register web hook on TG"""
    await tb_api.set_webhook()
    print("Startup")


@app.on_event("shutdown")
async def unset_webhook():
    """Unregister web hook"""
    await tb_api.unset_webhook()
    print("Shutdown")
