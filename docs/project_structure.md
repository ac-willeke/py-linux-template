```bash
├── .github
│   └── workflows
│       │── docker.yml           # workflow for building and pushing docker image (TODO)
│       └── python-package.yml   # workflow for building and publishing python package (TODO)

├── .gitignore                   # files and directories that should not be tracked by git
├── .pre-commit-config.yaml      # pre-commit configuration file
├── .readthedocs.yml             # readthedocs configuration file

├── docs
│   ├── cheatsheet_unix_shell.md    # A default Sphinx project; see sphinx-doc.org

├── src
│   ├── test
│   │   ├── test_config.py
│   │   └── test_main.py
│   ├── __init__.py

├── .env
├── config.yaml
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
└── setup.py
```


Python packages are typically structured as follows:
- root directory with the package name.
- `.pyproject.toml` file: contains project information and its dependencies.
- `src` directory: contains the source code of the package.
- `tests` directory: contains the tests for the package.
- `setup.py` file: contains information about the package and its dependencies.
- `README.md` file: contains information about the package and its dependencies.
- `LICENSE` file: contains the license of the package.
- `.gitignore` file: contains files and directories that should not be tracked by git.

Additional files:
- `.pre-commit-config.yaml` file: contains the configuration for pre-commit.
- Makefile: contains the configuration for make.
- `.env` file: contains environment variables.
- `config.yaml` file: contains configuration settings for the package.


The installable version of your package that you distribute to others will typically only contain the Python code in the src/ directory. The rest of the content exists to support development of the package and is not needed by users to actually use the package. This content is typically shared by the developer by some other means, such as GitHub, so that other developers can access and contribute to it if they wish.

It is possible to include arbitrary content in your package that is not Python code. For example, you might want to include a README file, a license file, or even data files that your package uses. To do this, you need to include a MANIFEST.in file in your package. This file is used by the distutils package to determine which files to include in the package. The format of the file is similar to that of a .gitignore file, in that you can specify files to include or exclude using wildcards. For example, to include all files with the .txt extension, you would use the following:

```bash
include *.txt
```

Or you can add it in your tool.poetry
```bash
pyproject.toml
[tool.poetry]
name = "pycounts"
version = "0.1.0"
description = "Calculate word counts in a text file!"
authors = ["Tomas Beuzen"]
license = "MIT"
readme = "README.md"
include = ["tests/*", "CHANGELOG.md"]


```
