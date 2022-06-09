import pytest
from google.protobuf.message import Message
from pydantic import BaseModel

from pydanticprotobuf import BaseModelToMessage, MessageToBaseModel
from tests.conftest import (
    ItemModel,
    ItemModelWithDict,
    ItemModelWithEnum,
    ItemModelWithItem,
    ItemModelWithItemList,
    ItemModelWithList,
    ItemType,
)
from tests.protobuf.examples_pb2 import (
    ItemProto,
    ItemProtoWithEnum,
    ItemProtoWithMap,
    ItemProtoWithRepeated,
    ItemProtoWithRepeatedItems,
    ItemProtoWithSubItem,
)


@pytest.mark.parametrize("model_name", ["ItemModel"])
@pytest.mark.parametrize("message_name", ["ItemProto"])
def test_conversion_to_message(model: BaseModel, message: Message) -> None:
    assert type(model) == ItemModel
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProto
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True


@pytest.mark.parametrize("message_name", ["ItemProto"])
def test_conversion_to_model(message: Message) -> None:
    assert type(message) == ItemProto
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    _model = MessageToBaseModel(basemodel=ItemModel, message=message)
    assert type(_model) == ItemModel
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True


@pytest.mark.parametrize("model_name", ["ItemModelWithList"])
@pytest.mark.parametrize("message_name", ["ItemProtoWithRepeated"])
def test_conversion_to_message_with_repeated(
    model: BaseModel, message: Message
) -> None:
    assert type(model) == ItemModelWithList
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    assert model.extras == ["a", "b"]
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProtoWithRepeated
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True
    assert _message.extras == ["a", "b"]


@pytest.mark.parametrize("message_name", ["ItemProtoWithRepeated"])
def test_conversion_to_model_with_repeated(message: Message) -> None:
    assert type(message) == ItemProtoWithRepeated
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    assert message.extras == ["a", "b"]
    _model = MessageToBaseModel(basemodel=ItemModelWithList, message=message)
    assert type(_model) == ItemModelWithList
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True
    assert _model.extras == ["a", "b"]


@pytest.mark.parametrize("model_name", ["ItemModelWithDict"])
@pytest.mark.parametrize("message_name", ["ItemProtoWithMap"])
def test_conversion_to_message_with_dict(model: BaseModel, message: Message) -> None:
    assert type(model) == ItemModelWithDict
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    assert model.data == {"key": "value", "key2": "value2"}
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProtoWithMap
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True
    assert _message.data == {"key": "value", "key2": "value2"}


@pytest.mark.parametrize("message_name", ["ItemProtoWithMap"])
def test_conversion_to_model_with_dict(message: Message) -> None:
    assert type(message) == ItemProtoWithMap
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    assert message.data == {"key": "value", "key2": "value2"}
    _model = MessageToBaseModel(basemodel=ItemModelWithDict, message=message)
    assert type(_model) == ItemModelWithDict
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True
    assert _model.data == {"key": "value", "key2": "value2"}


@pytest.mark.parametrize("model_name", ["ItemModelWithItem"])
@pytest.mark.parametrize("message_name", ["ItemProtoWithSubItem"])
def test_conversion_to_message_with_sub_item(
    model: BaseModel, message: Message
) -> None:
    assert type(model) == ItemModelWithItem
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    assert model.item.name == "Name"
    assert model.item.amount == 2
    assert model.item.active is True
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProtoWithSubItem
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True
    assert _message.item.name == "Name"
    assert _message.item.amount == 2
    assert _message.item.active is True


@pytest.mark.parametrize("message_name", ["ItemProtoWithSubItem"])
def test_conversion_to_model_with_sub_item(message: Message) -> None:
    assert type(message) == ItemProtoWithSubItem
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    assert message.item.name == "Name"
    assert message.item.amount == 2
    assert message.item.active is True
    _model = MessageToBaseModel(basemodel=ItemModelWithItem, message=message)
    assert type(_model) == ItemModelWithItem
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True
    assert _model.item.name == "Name"
    assert _model.item.amount == 2
    assert _model.item.active is True


@pytest.mark.parametrize("model_name", ["ItemModelWithItemList"])
@pytest.mark.parametrize("message_name", ["ItemProtoWithRepeatedItems"])
def test_conversion_to_message_with_sub_item_list(
    model: BaseModel, message: Message
) -> None:
    assert type(model) == ItemModelWithItemList
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    assert model.items[0].name == "Name"
    assert model.items[0].amount == 2
    assert model.items[0].active is True
    assert model.items[1].name == "Name"
    assert model.items[1].amount == 2
    assert model.items[1].active is True
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProtoWithRepeatedItems
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True
    assert _message.items[0].name == "Name"
    assert _message.items[0].amount == 2
    assert _message.items[0].active is True
    assert _message.items[1].name == "Name"
    assert _message.items[1].amount == 2
    assert _message.items[1].active is True


@pytest.mark.parametrize("message_name", ["ItemProtoWithRepeatedItems"])
def test_conversion_to_model_with_sub_item_list(message: Message) -> None:
    assert type(message) == ItemProtoWithRepeatedItems
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    assert message.items[0].name == "Name"
    assert message.items[0].amount == 2
    assert message.items[0].active is True
    assert message.items[1].name == "Name"
    assert message.items[1].amount == 2
    assert message.items[1].active is True
    _model = MessageToBaseModel(basemodel=ItemModelWithItemList, message=message)
    assert type(_model) == ItemModelWithItemList
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True
    assert _model.items[0].name == "Name"
    assert _model.items[0].amount == 2
    assert _model.items[0].active is True
    assert _model.items[1].name == "Name"
    assert _model.items[1].amount == 2
    assert _model.items[1].active is True


@pytest.mark.parametrize("model_name", ["ItemModelWithEnum"])
@pytest.mark.parametrize("message_name", ["ItemProtoWithEnum"])
def test_conversion_to_message_with_enum(model: BaseModel, message: Message) -> None:
    assert type(model) == ItemModelWithEnum
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
    assert model.type == ItemType.TYPE_1
    _message = BaseModelToMessage(basemodel=model, message=message)
    assert type(_message) == ItemProtoWithEnum
    assert _message.name == "Name"
    assert _message.amount == 2
    assert _message.active is True
    assert _message.type == 1


@pytest.mark.parametrize("message_name", ["ItemProtoWithEnum"])
def test_conversion_to_model_with_enum(message: Message) -> None:
    assert type(message) == ItemProtoWithEnum
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True
    assert message.type == 1
    _model = MessageToBaseModel(basemodel=ItemModelWithEnum, message=message)
    assert type(_model) == ItemModelWithEnum
    assert _model.name == "Name"
    assert _model.amount == 2
    assert _model.active is True
    assert _model.type == ItemType.TYPE_1
