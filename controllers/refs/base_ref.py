from enum import Enum
from typing import List, Optional, TypeVar, Generic


T = TypeVar("T")


class BaseRef:
    name: str
    summary: str
    description: Optional[str] = None
    result_type: Generic[T]

    async def generate(
        self,
        query: Optional[str] = None,
        page: Optional[int] = 1,
        limit: Optional[int] = 10
    ):
        pass
