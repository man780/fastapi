from fastapi import APIRouter

from controllers.yandex import YandexController


router = APIRouter()


@router.get("/health_check/", tags=["system"])
async def health_check():
    return {"success": True}


@router.get("/translate/{text}", tags=["yandex"])
async def translate(text: str = None):
    yandex = YandexController()
    yandex.configure_url(text=text)
    translated = yandex.get_response_data()

    response = {
        "text": text,
        "translation": translated.get("def")
    }
    return response
