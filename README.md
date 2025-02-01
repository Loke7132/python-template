# Python-template

An initial template repository for a Python project

## Prerequisites

* Python 3.12+ (install via [pyenv](https://github.com/pyenv/pyenv))
* Virtual environment (recommend [venv](https://docs.python.org/3/library/venv.html))
* Add Python to PATH: `export PATH="$HOME/.pyenv/shims:$PATH"`

### Running the code


## Introduction

### Tools
1. Language: Python@3.12
2. Package Management: pyproject.toml (PEP 621)
3. Code Formatting: ruff@0.1.9
4. Static Analysis: mypy@1.8.0 + ruff@0.1.9
5. CI Tool: CircleCI@2.1

### Structure
``` shell

.
├── .circleci/ # CI configuration
│ └── config.yml
├── .github/ # Templates
│ ├── ISSUE_TEMPLATE/
├── src/ # Source code
│ └── hello_world/
│ ├── init.py
│ └── main.py
├── tests/ # Unit tests
├── .gitignore
├── .ruff.toml # Lint configuration
├── pyproject.toml # Project metadata
└── PULL_REQUEST_TEMPLATE.md
├── LICENSE
└── README.md
```

### Components Example

**Greeting Component** (src/hello_world/main.py):

``` shell
def get_greeting(name: str = "World") -> str:
return f"Hello, {name}!"

def main() -> None:
print(get_greeting())
``` 

**Validation Component** (tests/test_greeting.py):

``` shell
from hello_world.main import get_greeting

def test_default_greeting():
assert get_greeting() == "Hello, World!"

def test_named_greeting():
assert get_greeting("loki") == "Hello, loki!"

``` 


### CI Pipeline
1. Install Python 3.12 + dependencies
2. Run unit tests with pytest
3. Static analysis with mypy + ruff
4. Code formatting verification
5. Generate test coverage report

## Getting Started

Set up development environment:

``` shell
python -m venv .venv
``` 
``` shell
source .venv/bin/activate
```
``` shell
pip install -e ".[dev]"
``` 


Common development commands:
``` shell
Run tests :

    pytest -v

    Lint code

    ruff check .
``` 
``` shell
Type checking:

    mypy .

    Format code

    ruff format .
``` 


## CI Configuration (.circleci/config.yml)
``` shell
version: 2.1
orbs:
python: circleci/python@2.1.1
jobs:
build_and_test:
docker:
    - image: cimg/python:3.12
    steps:
    - checkout
    - python/install-packages:
args: ".[dev]"
    - run: ruff check .
    - run: mypy .
    - run: pytest --cov=src --cov-report=xml
    - store_test_results:
path: test-results
    - store_artifacts:
path: coverage.xml
``` 


## Start Development
1. Clone repository
2. Set up virtual environment
3. Install dev dependencies
4. Create feature branch
5. Submit PR using template

## Contribution Guidelines
- Follow Python PEP8 style guide
- Include type hints for all functions
- Keep test coverage ≥ 90%
- Use PR template from `PULL_REQUEST_TEMPLATE.md`
- Reference issues in commit messages
