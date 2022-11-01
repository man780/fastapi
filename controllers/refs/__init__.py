from typing import List, Optional, Type

from controllers.refs.base_ref import BaseRef
from controllers.refs.country import CountryRef

refs = {}


def register_ref(ref_class: Type[BaseRef]):
    global refs

    refs[ref_class().name] = ref_class


def get_ref(name: str) -> Optional[Type[BaseRef]]:
    global refs

    return refs[name]


def get_all_refs() -> List[Type[BaseRef]]:
    global refs

    return list(refs.values())


register_ref(CountryRef)
