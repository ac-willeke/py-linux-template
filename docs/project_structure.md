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
"""
Template for .env file
"""

# Environment variables go here, can be read by `python-dotenv` package as follow:
#
#   `src/config.py`
#   ----------------------------------------------------------------
#    import dotenv
#
#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
#    dotenv_path = os.path.join(project_dir, '.env')
#    dotenv.load_dotenv(dotenv_path)
#   ----------------------------------------------------------------
#
# DO NOT ADD THIS FILE TO VERSION CONTROL!

# project
PROJECT="path/to/the/local/version/of/this/repository"

# data
RAW_DATA="path/to/raw/data/folder"
DATA="path/to/project/folder/which/contains/the/data/folder"
STAND_ALONE_DATA="path/to/data"

# PostGIS connection
PG_HOST=host_adress
PG_DB=database_name
PG_PORT=port_number
PG_USER=user_name
PG_KEY=password

#PyPI credentials
PYPI_USER=__token__
PYPI_KEY=your_token
```
