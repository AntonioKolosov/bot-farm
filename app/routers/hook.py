from fastapi import APIRouter

from ..schemas.tbdata import TBData


router = APIRouter()


@router.post("/hook", tags=["HOOK"])
def message(data: TBData):
    print(data.message)
    return {"message": "ok"}
