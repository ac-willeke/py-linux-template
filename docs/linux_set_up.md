# Linux Set Up for Python Development
This document describes how to set up a Linux environment for Python development. The information is based on the documentation from [Python Packages](https://py-pkgs.org/welcome) and [DataCamp](https://www.datacamp.com) course material.
See the [cheatsheet](cheatsheet_unix_shell.md) for a quick overview of the Unix shell.


## Installation

Check your shell configuration using the command `echo $0`.

### 1. Python

 - Check if and where Python is installed.

      ```bash
      # Standard Python Distribution
      which python3
      python3 --version
      which pip
      which pipx

      # Anaconda Distribution
      which conda
      conda --version
      ```


- Standard Python distribution

   - download and install from [python.org](https://www.python.org/downloads/)

   - add Python to your PATH
   - Install `pipx`: `python3 -m pip install pipx`
   - Configure PATH: `pipx ensurepath`
   - Close and open your shell again



- Miniconda distribution
   - download and install from [conda.io](https://docs.conda.io/en/latest/miniconda.html)

      ```bash
      # create a directory
      mkdir -p ~/miniconda3
      cd miniconda3

      # download miniconda
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

      # rename file to miniconda.sh
      mv Miniconda3-latest-Linux-x86_64.sh miniconda.sh

      # install miniconda
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

      # remove installation file
      rm -rf ~/miniconda3/miniconda.sh
      ``````
   - initialize conda

      ```bash
      ~/miniconda3/bin/conda init
      ```
   - close and re-open your shell
   - ensure that conda is up to date `conda update --all`


| Python Distribution | Python Path | Python Version |
| ------------------- | ----------- | -------------- |
|standard distribution| `/usr/bin/python3` | `Python 3.10.12` |
|miniconda distribution| `/home/username/miniconda3/bin/conda/` | `conda 23.5.2`


## 2. Git and Github

- install git: [git-scm.com](https://git-scm.com/download/linux)
- login to GitHub in vscode
- configure git
   ```shell
   git config --global user.name "John Doe"
   git config --global user.email johndoe@example.com
   git config --global init.defaultBranch main

   # check your settings
   git config --list --show-origin
   ```
- create `.gitignore` and add files and directories that should not be tracked by git

## 3. Register for a PyPI account
The Python Package Index (PyPI) is the official online software repository for Python. A software repository is a storage location for downloadable software, like Python packages. Before publishing packages to PyPI, it is typical to “test drive” their publication on TestPyPI, which is a test version of PyPI. It is recommended to register for a TestPyPI account on the TestPyPI website and a PyPI account on the PyPI website.

- Test PyPI: [test.pypi.org](https://test.pypi.org/account/register/)
- PyPI: [pypi.org](https://pypi.org/account/register/)

## 4. Makefile

*Make* is a tool that is used for automating tasks by defining a set of instructions in a `Makefile` which is located in your projects root directory. Install make using: `sudo apt install make`

A template Makefile is provided in this repository. It contains the following targets:
- `make global-install`: installs all dependencies that are not project-specific using pipx
   - pre-commit
   - black
   - isort
   - ruff
   - pyment

- `make poetry-install`: installs all dependencies that are project-specific using poetry
- `make codestyle`: runs all code quality checks (black, isort, ruff, pyment)
- `make docstring`: generates or converts docstrings to the reStructured text style using pyment
- `make cleanup`: removes all temporary files and directories


## 5. Pre-commit
** pre-commit** checks certain actions before committing changes to your repository. The list of actions that are executed are defined in `.pre-commit-config.yaml`.
   - Install `pre-commit`: `pipx install pre-commit`
   - Enter into your git repository and install the hooks: `pre-commit install` (optional, but recommended)
   - de-activate pre-commit:
      - delete or comment out the lines in .pre-commit-config.yaml
      - `pre-commit uninstall`
      - `pre-commit clean`

**How to use pre-commit:**

In case you executed `pre-commit install`, `pre-commit` hooks will be executed each time you will try to commit (`git commit`). If any of the checks fail or if any files that is going to be committed is changed (because a tool refactored or cleaned it), the commit will fail.

The suggested method to use `pre-commit` is to run it before trying to commit your changes, using `pre-commit run -a`. You can run this command multiple times, to check if the changes are ready to be committed.
After all the tests succeeded, the changes can be staged (`git add`) and committed.

**Note**: Solely install pre-commit in the standard distribution, not in the miniconda distribution or project-specific poetry environment.

## 6. Code Formatters and Linter

- black (code formatter)

- isort (sorts imports)

- ruff (linter)

- pyment (docstring formatter)
https://github.com/dadadel/pyment


## 7. Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry also allows you to create a virtual environment for your project, so that your project is isolated from your system.

- documentation: [poetry-docs](https://python-poetry.org/docs/)

- install poetry: `pipx install poetry` or `make install-poetry`




## Project Templates

- cookiecutter (pre-made templates)
 ```shell
 cookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git
 ```



## References

- [Python Packages](https://py-pkgs.org/welcome)
- [Python](https://docs.python.org/3/)
- [Git](https://git-scm.com/doc)
- [GitHub](https://docs.github.com/en)
- [PyPI](https://pypi.org/help/)
- [Poetry](https://python-poetry.org/docs/)
- [Make](https://www.gnu.org/software/make/manual/make.html)
- [Pre-commit](https://pre-commit.com/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Isort](https://pycqa.github.io/isort/)
