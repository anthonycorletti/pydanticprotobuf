# pydanticprotobuf

Convert [protobuf messages](https://developers.google.com/protocol-buffers/docs/pythontutorial) to [pydantic](https://github.com/samuelcolvin/pydantic) objects and vice versa.

Protobufs must be generated with `proto3` syntax.

## Installation

```bash
pip install pydanticprotobuf
```

## Usage

1. Create your proto file

    ```proto
    // person.proto
    syntax = "proto3";

    package main;

    message Person {
        string name = 1;
        int32 age = 2;
    }
    ```

1. Generate the pb2 files

    ```sh
    python -m grpc_tools.protoc -I . \
    --python_out=. \
    --grpc_python_out=. \
    --mypy_out=. \
    --mypy_grpc_out=. \
    person.proto
    ```

1. Use the `BaseModelToMessage` and `MessageToBaseModel` classes to convert between the two.

    ```python
    from pydantic import BaseModel
    from pydanticprotobuf import BaseModelToMessage, MessageToBaseModel
    from person_pb2 import Person

    class PersonBase(BaseModel):
        name: str = "Anthony"
        age: int = 42

    person = PersonBase()
    assert person.name == "Anthony"
    assert person.age == 42

    message = BaseModelToMessage(basemodel=person, message=Person)
    assert message.name == "Anthony"
    assert message.age == 42

    model = MessageToBaseModel(basemodel=PersonBase, message=message)
    assert model.name == "Anthony"
    assert model.age == 42
    ```

More detailed examples are located in the [tests](tests).
