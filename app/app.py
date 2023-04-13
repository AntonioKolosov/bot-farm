"""
"""

from typing import Dict

from fastapi import FastAPI

from .description import description, title, version, license, contact
from .routers import hook


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)

app.include_router(hook.router)


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}
