from fastapi import APIRouter

from controllers.refs import get_all_refs

router = APIRouter()


for ref_class in get_all_refs():
    ref = ref_class()

    router.get(
        path=f"/refs/{ref.name}",
        summary=ref.name,
        description=ref.description
    )
