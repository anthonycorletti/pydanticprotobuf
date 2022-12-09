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


def test_model_to_message() -> None:
    d = ItemModel(name="name", amount=42, active=True)
    m = BaseModelToMessage(basemodel=d, message=ItemProto)
    assert type(m) == ItemProto
    assert m.name == "name"
    assert m.amount == 42
    assert m.active is True
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModel, message=m)
    assert type(new_d) == ItemModel
    assert new_d.name == "name"
    assert new_d.amount == 42
    assert new_d.active is True


def test_message_to_model() -> None:
    m = ItemProto(name="name", amount=42, active=True)
    d = MessageToBaseModel(basemodel=ItemModel, message=m)
    assert type(d) == ItemModel
    assert d.name == "name"
    assert d.amount == 42
    assert d.active is True

    new_m = BaseModelToMessage(basemodel=d, message=ItemProto)
    assert type(new_m) == ItemProto
    assert new_m.name == "name"
    assert new_m.amount == 42
    assert new_m.active is True
    assert new_m.IsInitialized()


def test_message_with_repeated_to_model() -> None:
    m = ItemProtoWithRepeated(name="name?", amount=42, active=True, extras=["a", "b"])
    d = MessageToBaseModel(basemodel=ItemModelWithList, message=m)
    assert type(d) == ItemModelWithList
    assert d.name == "name?"
    assert d.amount == 42
    assert d.active is True
    assert d.extras == ["a", "b"]

    new_m = BaseModelToMessage(basemodel=d, message=ItemProtoWithRepeated)
    assert type(new_m) == ItemProtoWithRepeated
    assert new_m.name == "name?"
    assert new_m.amount == 42
    assert new_m.active is True
    assert new_m.extras == ["a", "b"]
    assert new_m.IsInitialized()


def test_model_to_message_with_repeated() -> None:
    d = ItemModelWithList(name="name?", amount=42, active=True, extras=["a", "b"])
    m = BaseModelToMessage(basemodel=d, message=ItemProtoWithRepeated)
    assert type(m) == ItemProtoWithRepeated
    assert m.name == "name?"
    assert m.amount == 42
    assert m.active is True
    assert m.extras == ["a", "b"]
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModelWithList, message=m)
    assert type(new_d) == ItemModelWithList
    assert new_d.name == "name?"
    assert new_d.amount == 42
    assert new_d.active is True
    assert new_d.extras == ["a", "b"]


def test_message_with_map_to_model() -> None:
    m = ItemProtoWithMap(name="name?", amount=42, active=True, data={"a": "b"})
    d = MessageToBaseModel(basemodel=ItemModelWithDict, message=m)
    assert type(d) == ItemModelWithDict
    assert d.name == "name?"
    assert d.amount == 42
    assert d.active is True
    assert d.data == {"a": "b"}

    new_m = BaseModelToMessage(basemodel=d, message=ItemProtoWithMap)
    assert type(new_m) == ItemProtoWithMap
    assert new_m.name == "name?"
    assert new_m.amount == 42
    assert new_m.active is True
    assert new_m.data == {"a": "b"}
    assert new_m.IsInitialized()


def test_model_to_message_with_map() -> None:
    d = ItemModelWithDict(name="name?", amount=42, active=True, data={"a": "b"})
    m = BaseModelToMessage(basemodel=d, message=ItemProtoWithMap)
    assert type(m) == ItemProtoWithMap
    assert m.name == "name?"
    assert m.amount == 42
    assert m.active is True
    assert m.data == {"a": "b"}
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModelWithDict, message=m)
    assert type(new_d) == ItemModelWithDict
    assert new_d.name == "name?"
    assert new_d.amount == 42
    assert new_d.active is True
    assert new_d.data == {"a": "b"}


def test_conversion_to_message_with_sub_item() -> None:
    d = ItemModelWithItem(
        name="Name",
        amount=2,
        active=True,
        item=ItemModel(name="SubName", amount=3, active=False),
    )
    m = BaseModelToMessage(basemodel=d, message=ItemProtoWithSubItem)
    assert type(m) == ItemProtoWithSubItem
    assert m.name == "Name"
    assert m.amount == 2
    assert m.active is True
    assert m.item.name == "SubName"
    assert m.item.amount == 3
    assert m.item.active is False
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModelWithItem, message=m)
    assert type(new_d) == ItemModelWithItem
    assert new_d.name == "Name"
    assert new_d.amount == 2
    assert new_d.active is True
    assert new_d.item.name == "SubName"
    assert new_d.item.amount == 3
    assert new_d.item.active is False


def test_conversion_to_model_with_sub_item() -> None:
    m = ItemProtoWithSubItem(
        name="Name",
        amount=2,
        active=True,
        item=ItemProto(name="SubName", amount=3, active=False),
    )
    d = MessageToBaseModel(basemodel=ItemModelWithItem, message=m)
    assert type(d) == ItemModelWithItem
    assert d.name == "Name"
    assert d.amount == 2
    assert d.active is True
    assert d.item.name == "SubName"
    assert d.item.amount == 3
    assert d.item.active is False

    new_m = BaseModelToMessage(basemodel=d, message=ItemProtoWithSubItem)
    assert type(new_m) == ItemProtoWithSubItem
    assert new_m.name == "Name"
    assert new_m.amount == 2
    assert new_m.active is True
    assert new_m.item.name == "SubName"
    assert new_m.item.amount == 3
    assert new_m.item.active is False
    assert new_m.IsInitialized()


def test_conversion_to_message_with_sub_item_list() -> None:
    d = ItemModelWithItemList(
        name="Name",
        amount=2,
        active=True,
        items=[
            ItemModel(name="SubName", amount=3, active=False),
            ItemModel(name="SubName", amount=3, active=False),
        ],
    )
    m = BaseModelToMessage(basemodel=d, message=ItemProtoWithRepeatedItems)
    assert type(m) == ItemProtoWithRepeatedItems
    assert m.name == "Name"
    assert m.amount == 2
    assert m.active is True
    assert m.items[0].name == "SubName"
    assert m.items[0].amount == 3
    assert m.items[0].active is False
    assert m.items[1].name == "SubName"
    assert m.items[1].amount == 3
    assert m.items[1].active is False
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModelWithItemList, message=m)
    assert type(new_d) == ItemModelWithItemList
    assert new_d.name == "Name"
    assert new_d.amount == 2
    assert new_d.active is True
    assert new_d.items[0].name == "SubName"
    assert new_d.items[0].amount == 3
    assert new_d.items[0].active is False
    assert new_d.items[1].name == "SubName"
    assert new_d.items[1].amount == 3
    assert new_d.items[1].active is False


def test_conversion_to_model_with_sub_item_list() -> None:
    m = ItemProtoWithRepeatedItems(
        name="Name",
        amount=2,
        active=True,
        items=[
            ItemProto(name="SubName", amount=3, active=False),
            ItemProto(name="SubName", amount=3, active=False),
        ],
    )
    d = MessageToBaseModel(basemodel=ItemModelWithItemList, message=m)
    assert type(d) == ItemModelWithItemList
    assert d.name == "Name"
    assert d.amount == 2
    assert d.active is True
    assert d.items[0].name == "SubName"
    assert d.items[0].amount == 3
    assert d.items[0].active is False
    assert d.items[1].name == "SubName"
    assert d.items[1].amount == 3
    assert d.items[1].active is False

    new_m = BaseModelToMessage(basemodel=d, message=ItemProtoWithRepeatedItems)
    assert type(new_m) == ItemProtoWithRepeatedItems
    assert new_m.name == "Name"
    assert new_m.amount == 2
    assert new_m.active is True
    assert new_m.items[0].name == "SubName"
    assert new_m.items[0].amount == 3
    assert new_m.items[0].active is False
    assert new_m.items[1].name == "SubName"
    assert new_m.items[1].amount == 3
    assert new_m.items[1].active is False
    assert new_m.IsInitialized()


def test_conversion_to_message_with_enum() -> None:
    d = ItemModelWithEnum(name="Name", amount=2, active=True, type=ItemType.TYPE_1)
    m = BaseModelToMessage(basemodel=d, message=ItemProtoWithEnum)
    assert type(m) == ItemProtoWithEnum
    assert m.name == "Name"
    assert m.amount == 2
    assert m.active is True
    assert m.type == 1
    assert m.IsInitialized()

    new_d = MessageToBaseModel(basemodel=ItemModelWithEnum, message=m)
    assert type(new_d) == ItemModelWithEnum
    assert new_d.name == "Name"
    assert new_d.amount == 2
    assert new_d.active is True
    assert new_d.type == ItemType.TYPE_1


def test_conversion_to_model_with_enum() -> None:
    m = ItemProtoWithEnum(name="Name", amount=2, active=True, type=1)  # type: ignore
    d = MessageToBaseModel(basemodel=ItemModelWithEnum, message=m)
    assert type(d) == ItemModelWithEnum
    assert d.name == "Name"
    assert d.amount == 2
    assert d.active is True
    assert d.type == ItemType.TYPE_1

    new_m = BaseModelToMessage(basemodel=d, message=ItemProtoWithEnum)
    assert type(new_m) == ItemProtoWithEnum
    assert new_m.name == "Name"
    assert new_m.amount == 2
    assert new_m.active is True
    assert new_m.type == 1
    assert new_m.IsInitialized()
