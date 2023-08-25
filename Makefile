.DEFAULT_GOAL := help ## default target

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# --------------------------------------
# Global Installation
# --------------------------------------

.PHONY: install-poetry install-pre-commit install-black install-isort

install-poetry: ## install poetry
	pipx install poetry

install-pre-commit: ## install pre-commit
	pipx install pre-commit

install-black: ## install black
	pipx install black

install-isort: ## install isort
	pipx install isort

install-ruff: ## install ruff
	pipx install ruff

install-pyment: ## install pyment
	pipx install pyment

install-cookiecutter: ## install cookiecutter
	pipx install cookiecutter

global-install: install-poetry install-pre-commit install-black install-isort install-pyment install-cookiecutter ## install poetry, pre-commit, black, isort, pyment on pipx

# --------------------------------------
# Poetry Installation (TODO)
# --------------------------------------
.PHONY: poetry-demo poetry-init
poetry-demo: ## create poetry demo project in cd
	poetry new poetry-demo
poetry-init: ## init poetry in existing project
	poetry init
poetry-install: ## install poetry dependencies
	poetry add black
	poetry add isort
	poetry add ruff
	poetry add pyment

# --------------------------------------
# Formatting and Linting
# --------------------------------------

.PHONY: codestyle formatting docstring pre-commit
codestyle: ## check codestyle (black, isort, ruff)
	isort --settings-path pyproject.toml ./
	black --config pyproject.toml ./
	ruff check ./

formatting: codestyle ##

docstring:  ## create or update docstring
	pyment -w -o reST ./
#pyment -w -o numpydoc ./
#pyment -w -o google ./

pre-commit: ## run pre-commit in all files
	pre-commit run -a

# --------------------------------------
# Cleaning up the project
# --------------------------------------
.PHONY: clean clean-build clean-pyc clean-test
clean: clean-build clean-pyc clean-linting clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +

clean-linting: ## remove linting artifacts
	find . -name '.ruff_cache' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .pytest_cache
