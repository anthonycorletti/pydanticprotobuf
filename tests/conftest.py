from typing import Dict, List

import pytest
from google.protobuf.message import Message
from pydantic import BaseModel

from tests.protobuf.examples_pb2 import (
    ItemProto,
    ItemProtoWithMap,
    ItemProtoWithRepeated,
    ItemProtoWithRepeatedItems,
    ItemProtoWithSubItem,
)


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


MODELS = [
    ItemModel,
    ItemModelWithList,
    ItemModelWithDict,
    ItemModelWithItem,
    ItemModelWithItemList,
]
MODEL_DISPATCH_TABLE = {model.__name__: model() for model in MODELS}

MESSAGES = [
    ItemProto,
    ItemProtoWithRepeated,
    ItemProtoWithMap,
    ItemProtoWithSubItem,
    ItemProtoWithRepeatedItems,
]
MESSAGE_DISPATCH_TABLE = {message.__name__: message() for message in MESSAGES}


@pytest.fixture()
def model(model_name: str) -> BaseModel:
    return MODEL_DISPATCH_TABLE[model_name]


@pytest.fixture()
def message(message_name: str) -> Message:
    return MESSAGE_DISPATCH_TABLE[message_name]
