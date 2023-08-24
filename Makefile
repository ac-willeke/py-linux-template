# Variables
PYTHON := python3

# GLOBAL Installation
.PHONY: install-poetry install-pre-commit install-black install-isort

install-poetry:
	pipx install poetry

install-pre-commit:
	pipx install pre-commit

install-black:
	pipx install black

install-isort:
	pipx install isort

install-ruff:
	pipx install ruff

global-install: install-poetry install-pre-commit install-black install-isort


# POETRY Installation

# Global Formatters and Linters
.PHONY: codestyle
codestyle:
	isort --settings-path pyproject.toml ./
	black --config pyproject.toml ./
	ruff check ./

.PHONY: formatting
formatting: codestyle


# Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: cleanup
cleanup: pycache-remove ipynbcheckpoints-remove