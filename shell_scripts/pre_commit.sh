#!/bin/sh
pytest .
isort -c .
black --check .
flake8 --max-line-length 88
mypy .
