#!/bin/sh

set -e

exec uv run fastmcp run main.py:app --transport stdio
