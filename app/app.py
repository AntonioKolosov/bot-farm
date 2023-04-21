"""
"""

from typing import Dict

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hook
from .internals.registerwebhook import RegisterWebhook


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)


app.include_router(hook.router)


webhook = RegisterWebhook()


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.on_event("startup")
async def set_webhook():
    """Register web hook on TG"""
    webhook.set_webhook()
    print("Startup")


@app.on_event("shutdown")
def unset_webhook():
    """Unregister web hook"""
    webhook.unset_webhook()
    print("Shutdown")
