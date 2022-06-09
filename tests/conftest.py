import pytest
from pydantic import BaseModel

from tests.protobuf.examples_pb2 import SimpleItemProto


class SimpleItemModel(BaseModel):
    name: str = "Name"
    amount: int = 2
    active: bool = True


MODELS = [SimpleItemModel]
MODEL_DISPATCH_TABLE = {model.__name__: model() for model in MODELS}

MESSAGES = [SimpleItemProto]
MESSAGE_DISPATCH_TABLE = {message.__name__: message() for message in MESSAGES}


@pytest.fixture()
def simple_item_model() -> SimpleItemModel:
    return MODEL_DISPATCH_TABLE["SimpleItemModel"]


@pytest.fixture()
def simple_item_message() -> SimpleItemProto:
    return MESSAGE_DISPATCH_TABLE["SimpleItemProto"]
