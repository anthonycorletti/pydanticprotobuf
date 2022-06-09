from typing import Type

from google.protobuf import json_format
from google.protobuf.message import Message
from pydantic import BaseModel


def BaseModelToMessage(basemodel: BaseModel, message: Message) -> Message:
    return json_format.ParseDict(
        js_dict=basemodel.dict(), message=message, ignore_unknown_fields=True
    )


def MessageToBaseModel(
    basemodel: Type[BaseModel],
    message: Message,
    including_default_value_fields: bool = True,
    preserving_proto_field_name: bool = False,
) -> BaseModel:
    return basemodel(
        **json_format.MessageToDict(
            message=message,
            including_default_value_fields=including_default_value_fields,
            preserving_proto_field_name=preserving_proto_field_name,
        )
    )
