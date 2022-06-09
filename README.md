# pydanticprotobuf

Convert [protobuf messages](https://developers.google.com/protocol-buffers/docs/pythontutorial) to [pydantic](https://github.com/samuelcolvin/pydantic) objects and vice versa.

Protobufs must be generated with `proto3` syntax.

## Installation

```bash
pip install pydanticprotobuf
```

## Usage

_Generation of `person_message` not shown._

`BaseModel` to `Message`

```proto
syntax = "proto3";

package main;

message Person {
    string name = 1;
    int32 age = 2;
}
```

```python
# assume `person_message` is a protobuf message imported from a generated pb2 file
from pydantic import BaseModel
from pydanticprotobuf import BaseModelToMessage

class Person(BaseModel):
    name: str = "Anthony"
    age: int = 42

person = Person()
assert person.name == "Anthony"
assert person.age == 42

message = BaseModelToMessage(basemodel=model, message=person_message)
assert message.name == "Anthony"
assert message.age == 42
```


`Message` to `BaseModel`

Using the same proto and `BaseModel` as above;

```python
from pydanticprotobuf import MessageToBaseModel

assert message.name == "Anthony"
assert message.age == 42

model = MessageToBaseModel(basemodel=ItemModelWithList, message=message)

assert model.name == "Anthony"
assert model.age == 42
```

More detailed examples are located in the [tests](tests).
