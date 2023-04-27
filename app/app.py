"""
"""

from typing import Dict
import logging

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hookrouter, testrouter
from .tbotapi.tbotapiwebhook import TbotAPIWebhook


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="twbot.log"
)


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)


app.include_router(hookrouter.router)
app.include_router(testrouter.router)


tb_wh = TbotAPIWebhook()


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.on_event("startup")
async def set_webhook():
    """Register web hook on TG"""
    await tb_wh.set_webhook()
    logging.info("Startup")


@app.on_event("shutdown")
async def unset_webhook():
    """Unregister web hook"""
    await tb_wh.unset_webhook()
    logging.info("Shutdown")
