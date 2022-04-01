#!/bin/bash

echo $#

if [[ $# -ne 1 ]]; then
  echo "Usage: script.sh <notebook_file>"
  exit
fi

echo "Running autoflake"
poetry run nbqa autoflake -i --remove-all-unused-imports "$1"

echo "Running isort"
poetry run nbqa isort "$1"

echo "Running black"
poetry run nbqa black "$1"

echo "Running pyupgrade"
poetry run pyupgrade "$1"

echo "Running flake8"
poetry run nbqa flake8 "$1"

echo "Running mypy"
poetry run nbqa mypy "$1"
