.PHONY: sync test lint flake8 analyzer validate package

sync:
	uv sync --frozen

test:
	PYTHONPATH=.. uv run python -m unittest discover tests

lint:
	uv run ruff check .

flake8:
	uv run flake8 . --config .flake8

analyzer:
	uv run qgis-analyzer analyze . --max-cc 10

validate:
	uv run qgis-manage validate --strict --repo

ZIP ?= $(shell ls -t dist/*.zip 2>/dev/null | head -1)

package:
	uv run qgis-manage package --repo-check
	uv run qgis-manage validate --zip "$(ZIP)"
