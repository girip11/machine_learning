#!/bin/bash

echo $#

if [[ $# -ne 1 ]]; then
  echo "Usage: script.sh <notebook_file>"
  exit
fi

echo "Running isort"
pipenv run nbqa isort "$1"

echo "Running black"
pipenv run nbqa black "$1"

echo "Running flake8"
pipenv run nbqa flake8 "$1"

echo "Running mypy"
pipenv run nbqa mypy "$1"
