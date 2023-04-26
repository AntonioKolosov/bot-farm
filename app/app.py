"""
"""

from typing import Dict
import logging

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hook
from .tbotapi.tbotapiwebhook import TbotAPIWebhook
from .tbotapi.tbotapisetup import TBotAPISetup


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


app.include_router(hook.router)


tb_wh = TbotAPIWebhook()


tb_st = TBotAPISetup()


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}


@app.get("/descr", tags=["ROOT"])
async def set_description():
    """"""
    description = "Hello, I'm new Bot"
    res = await tb_st.set_description(description)
    return {"Descr": f"Set {res}"}


@app.get("/cmd", tags=["ROOT"])
async def set_commands():
    """"""
    cmd_list = [
        {
            "command": "help",
            "description": "How to use this bot"
        }
    ]
    res = await tb_st.set_commands(cmd_list)
    return {"Commands": f"Set {res}"}


@app.get("/del", tags=["ROOT"])
async def delete_commands():
    """"""
    res = await tb_st.delete_commands()
    return {"Commands": f"Deleted {res}"}


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
