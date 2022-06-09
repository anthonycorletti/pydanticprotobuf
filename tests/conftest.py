from enum import Enum, unique
from typing import Dict, List

import pytest
from google.protobuf.message import Message
from pydantic import BaseModel

from tests.protobuf.examples_pb2 import (
    ItemProto,
    ItemProtoWithEnum,
    ItemProtoWithMap,
    ItemProtoWithRepeated,
    ItemProtoWithRepeatedItems,
    ItemProtoWithSubItem,
)


@unique
class ItemType(Enum):
    TYPE_0 = 0
    TYPE_1 = 1


class ItemModel(BaseModel):
    name: str = "Name"
    amount: int = 2
    active: bool = True


class ItemModelWithList(ItemModel):
    extras: List[str] = ["a", "b"]


class ItemModelWithDict(ItemModel):
    data: Dict[str, str] = {"key": "value", "key2": "value2"}


class ItemModelWithItem(ItemModel):
    item: ItemModel = ItemModel()


class ItemModelWithItemList(ItemModel):
    items: List[ItemModel] = [ItemModel(), ItemModel()]


class ItemModelWithEnum(ItemModel):
    type: ItemType = ItemType.TYPE_1


MODELS = [
    ItemModel,
    ItemModelWithList,
    ItemModelWithDict,
    ItemModelWithItem,
    ItemModelWithItemList,
    ItemModelWithEnum,
]
MODEL_DISPATCH_TABLE = {model.__name__: model() for model in MODELS}

MESSAGES = [
    ItemProto,
    ItemProtoWithRepeated,
    ItemProtoWithMap,
    ItemProtoWithSubItem,
    ItemProtoWithRepeatedItems,
    ItemProtoWithEnum,
]
MESSAGE_DISPATCH_TABLE = {message.__name__: message() for message in MESSAGES}


@pytest.fixture()
def model(model_name: str) -> BaseModel:
    return MODEL_DISPATCH_TABLE[model_name]


@pytest.fixture()
def message(message_name: str) -> Message:
    return MESSAGE_DISPATCH_TABLE[message_name]
