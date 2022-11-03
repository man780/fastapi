from fastapi import APIRouter

from clients import Clients


router = APIRouter()


@router.get("/translate/{text}", tags=["translate"])
async def translate(text: str = None):
    api_key: str = "dict.1.1.20221101T151346Z.8cc25df7c1c42d3f.336df7ad85bdc19d9c7897abdc882a41a135d01b"
    url = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={api_key}&lang=en-ru&text={text}"
    clients = Clients(
        url=url,
        method="GET"
    )
    response_data = clients.get_response_data()

    translated_text = response_data

    response = {
        "text": text,
        "translatedText": translated_text
    }
    return response
