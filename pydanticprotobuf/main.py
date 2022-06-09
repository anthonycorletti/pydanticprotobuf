from typing import Type

from google.protobuf import json_format
from google.protobuf.message import Message
from pydantic import BaseModel


def BaseModelToMessage(
    basemodel: BaseModel,
    message: Message,
    ignore_unknown_fields: bool = True,
) -> Message:
    """Converts a BaseModel object to a protobuf message.

    Args:
        basemodel (BaseModel): A pydantic object that derives from BaseModel.
        message (Message): The protobuf message to be populated.
        ignore_unknown_fields (bool, optional): Whether or not to ignore unknown fields.
            Defaults to True.

    Returns:
        Message: The populated protobuf message.
    """
    return json_format.Parse(
        text=basemodel.json().encode("utf8"),
        message=message,
        ignore_unknown_fields=ignore_unknown_fields,
    )


def MessageToBaseModel(
    basemodel: Type[BaseModel],
    message: Message,
    including_default_value_fields: bool = True,
    preserving_proto_field_name: bool = False,
    use_integers_for_enums: bool = True,
) -> BaseModel:
    """Converts a protobuf message to a pydantic BaseModel.

    Args:
        basemodel (Type[BaseModel]): The BaseModel class to be populated.
        message (Message): The protobuf message to be converted.
        including_default_value_fields (bool, optional): If True,
            singular primitive fields,
            repeated fields, and map fields will always be serialized.  If
            False, only serialize non-empty fields.  Singular message fields
            and oneof fields are not affected by this option. Defaults to True.
        preserving_proto_field_name (bool, optional): If True, use the
            original proto field names as defined in the .proto file. If False,
            convert the fieldnames to lowerCamelCase. Defaults to False.

    Returns:
        BaseModel: The populated pydantic object.
    """
    return basemodel.parse_raw(
        json_format.MessageToJson(
            message=message,
            including_default_value_fields=including_default_value_fields,
            preserving_proto_field_name=preserving_proto_field_name,
            use_integers_for_enums=use_integers_for_enums,
        )
    )
