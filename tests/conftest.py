from enum import Enum, unique
from typing import Dict, List

from pydantic import BaseModel


@unique
class ItemType(Enum):
    TYPE_0 = 0
    TYPE_1 = 1


class ItemModel(BaseModel):
    name: str
    amount: int
    active: bool


class ItemModelWithList(ItemModel):
    extras: List[str]


class ItemModelWithDict(ItemModel):
    data: Dict[str, str]


class ItemModelWithItem(ItemModel):
    item: ItemModel


class ItemModelWithItemList(ItemModel):
    items: List[ItemModel]


class ItemModelWithEnum(ItemModel):
    type: ItemType
