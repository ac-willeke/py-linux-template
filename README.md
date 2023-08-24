# py-linux-template

Modify this `README.md` file, to explain what your software does.

# Good practices

## .gitignore

Add paths and files that you do not want to be committed by adding them to .gitignore.

## pre-commit

`pre-commit` can run tools to check your changes and refactor code (using `black`), to keep your repository clean and avoid common mistakes. The list of actions that are executed are defined in `.pre-commit-config.yaml`.

## Unix shell

See the [cheatsheet](cheatsheet_unix_shell.md) for a quick overview of the Unix shell.

- Check your shell configuration `echo $0`

## Installation

### 1. Install Python

 - Check if and where Python is installed on Windows OS. 

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


- Standard distribution 

   - download and install from [python.org](https://www.python.org/downloads/) 

   - add Python to your PATH.
   - Install `pipx`: `python3 -m pip install pipx`
   - Configure PATH: `pipx ensurepath`
   - Close and open your shell again



- Miniconda Distribution
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

   **Information Table**: 

   | Python Distribution | Python Path | Python Version | 
   | ------------------- | ----------- | -------------- | 
   |standard distribution| `/usr/bin/python3` | `Python 3.10.12` | 
   |miniconda distribution| `/home/username/miniconda3/bin/conda/` | `conda 23.5.2`
   
   **Note**: Solely install pre-commit in the standard distribution, not in the miniconda distribution.
 

## 2. Install tools for enhancing code quality

### Git and GitHub
- Install git: [git-scm.com](https://git-scm.com/download/linux)
- Login to GitHub in vscode
- configure git
   ```shell
   git config --global user.name "John Doe"
   git config --global user.email johndoe@example.com
   git config --global init.defaultBranch main

   # check your settings
   git config --list --show-origin
   ```


### Install pre-commit
** pre-commit** checks certain actions before committing changes to your repository. The list of actions that are executed are defined in `.pre-commit-config.yaml`.
   - Install `pre-commit`: `pipx install pre-commit`
   - Enter into your git repository and install the hooks: `pre-commit install` (optional, but recommended)


**How to use pre-commit:**

In case you executed `pre-commit install`, `pre-commit` hooks will be executed each time you will try to commit (`git commit`). If any of the checks fail or if any files that is going to be committed is changed (because a tool refactored or cleaned it), the commit will fail.

The suggested method to use `pre-commit` is to run it before trying to commit your changes, using `pre-commit run -a`. You can run this command multiple times, to check if the changes are ready to be committed.
After all the tests succeeded, the changes can be staged (`git add`) and committed.

### Install black
**black** is a code formatter that reformats your code to comply with PEP 8. 
- Install it using `pipx install black`

- black (code formatter)

- isort (sorts imports)

- ruff (linter)









### How to use pre-commit 

In case you executed `pre-commit install`, `pre-commit` hooks will be executed each time you will try to commit (`git commit`). If any of the checks fail or if any files that is going to be committed is changed (because a tool refactored or cleaned it), the commit will fail.

The suggested method to use `pre-commit` is to run it before trying to commit your changes, using `pre-commit run -a`. You can run this command multiple times, to check if the changes are ready to be committed.
After all the tests succeeded, the changes can be staged (`git add`) and committed.
