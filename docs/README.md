# docs

Read the [contributing guide](./CONTRIBUTING.md) to get started.

The goal of this originally was to enable the transformation advanced proto message objects from packages such as `google-cloud-container` to pydantic objects so they could be be sent over a simple http request via fastapi.

This is some test code you can use to test it out if you like – it's a deep dive

```python
from typing import Optional, Type

from fastapi import FastAPI
from google.cloud.container_v1.types import Cluster  # type: ignore
from pydantic import BaseModel

from pydanticprotobuf import pydanticprotobuf

app = FastAPI()

MyCluster: BaseModel = pydanticprotobuf.convert_protobuf(message=Cluster.pb())


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/cluster")
def read_item(cluster: Type[MyCluster]):
    return {"cluster": cluster}

```
