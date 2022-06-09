from pydanticprotobuf import BaseModelToMessage, MessageToBaseModel
from tests.conftest import SimpleItemModel, SimpleItemProto


def test_simple_conversion_to_message(
    simple_item_model: SimpleItemModel, simple_item_message: SimpleItemProto
) -> None:
    assert type(simple_item_model) == SimpleItemModel
    assert simple_item_model.name == "Name"
    assert simple_item_model.amount == 2
    assert simple_item_model.active is True
    message = BaseModelToMessage(
        basemodel=simple_item_model, message=simple_item_message
    )
    assert type(message) == SimpleItemProto
    assert message.name == "Name"
    assert message.amount == 2
    assert message.active is True


def test_simple_conversion_to_model(simple_item_message: SimpleItemProto) -> None:
    assert type(simple_item_message) == SimpleItemProto
    assert simple_item_message.name == "Name"
    assert simple_item_message.amount == 2
    assert simple_item_message.active is True
    model = MessageToBaseModel(
        basemodel=SimpleItemModel,
        message=simple_item_message,
        including_default_value_fields=True,
        preserving_proto_field_name=False,
    )
    assert type(model) == SimpleItemModel
    assert model.name == "Name"
    assert model.amount == 2
    assert model.active is True
