#!/bin/bash

black --config .black.toml .
flake8 --config .flake8
mypy . --exclude venv
isort . --settings .isort.cfg

