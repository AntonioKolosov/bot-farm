"""
"""

from fastapi import APIRouter

# from ..schemas.tbdata import TBData
from ..tapiclient.tapiclientsetup import TBotAPISetup


router = APIRouter()

tb_st = TBotAPISetup()


@router.post("/descr", tags=["TEST"])
async def set_description():
    """"""
    description = "Hello, I'm new Bot"
    res = await tb_st.set_description(description)
    return {"Descr": f"Set {res}"}


@router.post("/cmd", tags=["TEST"])
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


@router.post("/del", tags=["ROOT"])
async def delete_commands():
    """"""
    res = await tb_st.delete_commands()
    return {"Commands": f"Deleted {res}"}
