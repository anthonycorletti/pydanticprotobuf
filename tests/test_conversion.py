from enum import Enum, EnumMeta, IntEnum

from google.cloud.container_v1.types import Cluster  # type: ignore
from google.rpc import code_pb2  # type: ignore
from pydantic.fields import FieldInfo
from pydantic.main import ModelMetaclass

from pydanticprotobuf import pydanticprotobuf
from tests.assets.example_map_pb2 import Payload
from tests.assets.example_pb2 import TestMessage


def test_example_conversion() -> None:
    result = pydanticprotobuf.convert_protobuf(message=TestMessage)
    assert isinstance(result, ModelMetaclass)
    assert result.__name__ == TestMessage.__name__


def test_example_map_conversion() -> None:
    result = pydanticprotobuf.convert_protobuf(message=Payload)
    assert isinstance(result, ModelMetaclass)
    assert result.__name__ == Payload.__name__


def test_gcp_cluster_conversion() -> None:
    result = pydanticprotobuf.convert_protobuf(message=Cluster.pb())
    assert isinstance(result, ModelMetaclass)
    assert result.__name__ == Cluster.__name__


def test_code_conversion() -> None:
    result = pydanticprotobuf.convert_protobuf(code_pb2.Code)
    assert result.__name__ == "Code"
    assert isinstance(result, EnumMeta)
