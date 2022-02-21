#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports pydanticprotobuf tests scripts

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pydanticprotobuf tests scripts --exclude=__init__.py
black pydanticprotobuf tests scripts
isort pydanticprotobuf tests scripts
