#!/bin/sh -ex

python -m grpc_tools.protoc -I tests \
--python_out=tests \
--grpc_python_out=tests \
--mypy_out=tests \
--mypy_grpc_out=tests \
tests/protobuf/examples.proto
