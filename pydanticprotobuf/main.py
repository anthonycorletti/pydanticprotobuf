from enum import IntEnum  # noqa
from functools import partial
from os import linesep
from typing import Any, Dict, Iterable, List, Union  # noqa

from google.protobuf.descriptor import Descriptor, EnumDescriptor, FieldDescriptor
from google.protobuf.duration_pb2 import Duration  # noqa
from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.struct_pb2 import Struct  # noqa
from google.protobuf.timestamp_pb2 import Timestamp  # noqa
from pydantic import BaseModel, Field  # noqa

from pydanticprotobuf.const import FIELD_DESCRIPTOR_TYPE_MAP, GETTER_KEY, ONELINE, TAB


class PydanticProtobuf:
    def _basemodel_statement(self, level: int, message: Descriptor) -> str:
        return f"{level * TAB}class {message.name}(BaseModel):"

    def _field_statements(self, level: int, message: Descriptor) -> Iterable:
        return map(partial(self.convert_protobuf_field, level), message.fields)

    def _basemodel_str(
        self, level: int, message: Union[Descriptor, EnumDescriptor]
    ) -> str:
        if isinstance(message, EnumDescriptor):
            data = self.convert_wrapped_enum_descriptor(level=level, field=message)
            return data
        return linesep.join(
            [
                self._basemodel_statement(level=level, message=message),
                *self._field_statements(level=level, message=message),
            ]
        )

    def _getter_str(self, descriptor: Descriptor) -> str:
        return f"def {GETTER_KEY}(): return {descriptor.name}"

    def _compile_str(self, basemodel_str: str, getter_str: str) -> str:
        return basemodel_str + linesep + getter_str

    def _compile(self, compile_str: str) -> Any:
        return compile(compile_str, "<string>", "exec")

    def convert_protobuf(self, message: GeneratedProtocolMessageType) -> BaseModel:
        descriptor = message.DESCRIPTOR  # type: ignore

        basemodel_str = self._basemodel_str(level=0, message=descriptor)
        compile_code = self._compile(
            compile_str=self._compile_str(
                basemodel_str=basemodel_str,
                getter_str=self._getter_str(descriptor=descriptor),
            )
        )

        _sub_namespace = {k: v for k, v in globals().items() if not k.startswith("__")}
        exec(compile_code, _sub_namespace)
        return _sub_namespace[GETTER_KEY]()

    def _type_statement(self, field: FieldDescriptor) -> str:
        return FIELD_DESCRIPTOR_TYPE_MAP[field.type].__name__

    def convert_wrapped_enum_descriptor(self, level: int, field: EnumDescriptor) -> str:
        class_statement = f"{TAB * level}class {field.name}(IntEnum):"
        field_statements = map(
            lambda value: f"{TAB * (level + 1)}{value.name} = {value.index}",
            field.values,
        )
        extra = linesep.join([class_statement, *field_statements])
        factory = "int"
        default_statement = f" = Field(default_factory={factory})"
        field_statement = (
            f"{TAB * level}{field.name.lower()}: {field.name}{default_statement}"
        )
        return linesep + extra + ONELINE + field_statement

    def convert_protobuf_field(self, level: int, field: FieldDescriptor) -> str:
        level += 1
        _field_type = field.type
        _field_label = field.label
        extra = None

        if _field_type == FieldDescriptor.TYPE_ENUM:
            enum_type: EnumDescriptor = field.enum_type
            type_statement = enum_type.name
            class_statement = f"{TAB * level}class {enum_type.name}(IntEnum):"
            field_statements = map(
                lambda value: f"{TAB * (level + 1)}{value.name} = {value.index}",
                enum_type.values,
            )
            extra = linesep.join([class_statement, *field_statements])
            factory = "int"
        elif _field_type == FieldDescriptor.TYPE_MESSAGE:
            type_statement = field.message_type.name
            if type_statement.endswith("Entry"):
                key, value = field.message_type.fields
                type_statement = (
                    f"Dict[{self._type_statement(key)}, {self._type_statement(value)}]"
                )
                factory = "dict"
            elif type_statement == "Struct":
                type_statement = "Dict[str, Any]"
                factory = "dict"
            else:
                extra = self._basemodel_str(level=level, message=field.message_type)
                factory = type_statement
        else:
            type_statement = self._type_statement(field=field)
            factory = type_statement

        if _field_label == FieldDescriptor.LABEL_REPEATED:
            type_statement = f"List[{type_statement}]"
            factory = "list"

        default_statement = f" = Field(default_factory={factory})"
        if _field_label == FieldDescriptor.LABEL_REQUIRED:
            default_statement = ""

        field_statement = (
            f"{TAB * level}{field.name}: {type_statement}{default_statement}"
        )

        if not extra:
            return field_statement
        return linesep + extra + ONELINE + field_statement
