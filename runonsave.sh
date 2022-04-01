#!/bin/bash
FILE=$1

echo "Running autoflake"
poetry run autoflake -i --remove-all-unused-imports "$FILE"

echo "Running pyupgrade"
poetry run pyupgrade "$FILE"
