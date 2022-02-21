#!/bin/sh -ex

mypy pydanticprotobuf
flake8 pydanticprotobuf
black pydanticprotobuf tests --check
isort pydanticprotobuf tests scripts --check-only
