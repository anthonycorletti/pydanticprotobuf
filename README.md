# pydanticprotobuf

Convert [Protobuf messages](https://developers.google.com/protocol-buffers/docs/pythontutorial) to [pydantic](https://github.com/samuelcolvin/pydantic) objects. Protobufs must be generated with `proto3` syntax.

## Usage

An example with Google Cloud's GKE Python Client

```python
from google.cloud.container_v1.types import Cluster
from pydanticprotobuf import pydanticprotobuf

cluster_basemodel = pydanticprotobuf.convert_protobuf(message=Cluster.pb())
c = cluster_basemodel(name="my-cluster")
```
