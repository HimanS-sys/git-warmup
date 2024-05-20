#!/bin/bash

black --config .black.toml .
pylint --rcfile .pylintrc *.py type_hinting/
flake8 --config .flake8
mypy . --exclude venv
isort . --settings .isort.cfg
