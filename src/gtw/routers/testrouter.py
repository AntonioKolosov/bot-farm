"""
Test router. You may use it for tests with API
"""


from fastapi import APIRouter

from src.services import services


router = APIRouter()


@router.post("/descr", tags=["TEST"])
async def set_description_req():
    """This method sets descriprion"""
    description = "Hello, I'm new Bot!!!!!!!!!!!!!!!"
    bot_id = "6049337649"
    res = await services.set_description('TG', bot_id, description)
    print(res)
    return {"Descr": f"Set {res}"}


@router.get("/testweb", tags=["MINIAPP"])
async def get_request():
    return {
        "content": [
            {
                "chank": "УИЛЬЯМ ГИБСОН\nТРЯПИЧНАЯ  КУКЛА\n"
            },
            {
                "chank": "- Лихорадка!\n- Лихорадка?\n"
            },
            {
                "chank": "- И простуда!\n- Простуда и лихорадка!\n"
            },
            {
                "chank": "- Ерунда! У нее нет температуры.\n"
            },
            {
                "chank": "- Это высокая температура!\n- Опасная.\n"
            },
            {
                "chank": "- Вовсе нет. У нее тридцать пять и два.\n"
            },
            {
                "chank": "- Это опасно!\n- У нее тридцать шесть и шесть.\n"
            },
            {
                "chank": "- Это нормальная температура.\n"
            },
            {
                "chank": "- Папа, не открывай эту дверь.\n"
            },
            {
                "chank": "- Они все ушли…\n- Она бредит.\n"
            },
            {
                "chank": "- Ей необходим сон.\n"
            },
        ]
    }
