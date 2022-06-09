#!/bin/sh -ex

mypy pydanticprotobuf tests
flake8 pydanticprotobuf tests
black pydanticprotobuf tests --check
isort pydanticprotobuf tests scripts --check-only
