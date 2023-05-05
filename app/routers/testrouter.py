"""
"""

from fastapi import APIRouter

# from ..schemas.tbdata import TBData
from app.tapiclient import tapiclientsetup as t_sp

router = APIRouter()


@router.post("/descr", tags=["TEST"])
async def set_description():
    """"""
    description = "Hello, I'm new Bot"
    res = await t_sp.set_description(description)
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
    res = await t_sp.set_commands(cmd_list)
    return {"Commands": f"Set {res}"}


@router.post("/del", tags=["ROOT"])
async def delete_commands():
    """"""
    res = await t_sp.delete_commands()
    return {"Commands": f"Deleted {res}"}
