"""
"""

from typing import Dict

from fastapi import FastAPI

from .description import description, title, version, license, contact


app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"Hello": "I am your Bot"}
