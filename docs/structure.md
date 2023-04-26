# Structure

```text
api-server                          Main directory
├── docs                            Documentation site (add more .md files here)
│   └── index.md                    The index page for the docs site
├── .github                         Github metadata for repository
│   ├── ISSUE_TEMPLATE              Templates for creating feature requests and bug reporting
│   └── workflows                   The CI pipeline for Github Actions
├── api                             The main Python package for the project
│   ├── models                      Structures and architectures for main units
│   │   ├── data.py                 Configuration of structures for data units
│   │   └── server.py               The base architecture for the server
│   ├── utils.py                    Collection of miscellaneous helper functions
│   ├── cli.py                      Defining the CLI commands
│   ├── __init__.py                 This tells Python that this is a package
│   ├── __main__.py                 The entry point for the project
│   └── VERSION                     The version for the project is kept in a static file
├── tests                           Unit tests for the project (add mote tests files here)
│   ├── __init__.py                 This tells Python that this is a test package
│   ├── conftest.py                 Configuration, hooks and fixtures for pytest
│   └── test_base.py                The base test case for the project
├── Dockerfile                      The file to build a container using Docker
├── .gitignore                      A list of files to ignore when pushing to Github
├── LICENSE                         The license for the project
├── Makefile                        A collection of utilities to manage the project
├── mkdocs.yml                      Configuration for documentation site
├── pyproject.toml                  Allows for pip-based installation
├── README.md                       The main readme for the project
├── requirements.txt                List requirements for running the project
├── requirements-test.txt           List of requirements for testing and devlopment
└── setup.py                        The setup file for installing and packaging the project
```