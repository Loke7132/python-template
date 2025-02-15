# Python-template

An advanced Python template repository for building modular projects with testing and CI/CD pipelines.

## Prerequisites

* Python 3.12+ (install via [pyenv](https://github.com/pyenv/pyenv))
* Virtual environment (recommend [venv](https://docs.python.org/3/library/venv.html))
* Add Python to PATH: `export PATH="$HOME/.pyenv/shims:$PATH"`

### Running the code




## Introduction

This project provides a foundational structure for Python applications with:

1) Components: Modular design for Calculator, Logger, and Notifier.

2) Testing: Unit tests, integration tests, and end-to-end tests.

3) Code Quality: Static analysis with mypy and linting with ruff.

4) CI/CD Pipeline: Automated testing and deployment using CircleCI.

### Tools
1. Language: Python@3.12
2. Package Management: pyproject.toml (PEP 621)
3. Code Formatting: ruff@0.1.9
4. Static Analysis: mypy@1.8.0 + ruff@0.1.9
5. CI Tool: CircleCI@2.1

### Structure
``` shell


.
├── .circleci/           # CI configuration
│   └── config.yml
├── .github/             # Templates for issues and PRs
├── src/                 # Source code
│   └── components/
│       ├── calculator.py  # Performs arithmetic operations
│       ├── logger.py      # Records operations performed by Calculator
│       └── notifier.py    # Sends alerts when thresholds are exceeded
├── tests/               # Test files
│   ├── unit/            # Unit tests for individual components
│   ├── integration/     # Integration tests between components
│   └── e2e/             # End-to-end tests for the entire system
├── .gitignore           # Files to ignore in Git
├── pyproject.toml       # Project metadata and dependencies
├── LICENSE              # Open-source license file
└── README.md            # Documentation (this file)

```

### Components Overview



**Calculator Component** 
Performs basic arithmetic operations like addition, subtraction, and multiplication.
``` shell
from components.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8

``` 

**Logger Component** 
Records operations performed by the Calculator.
``` shell
from components.notifier import Notifier

notifier = Notifier(threshold=10)
if notifier.check_threshold(15):
    print(notifier.last_notification)  # Output: "ALERT: Value 15 exceeds threshold 10!"



```
**Notifier Component**
Sends an alert when a calculation result exceeds a specified threshold.

```shell

from components.notifier import Notifier

notifier = Notifier(threshold=10)
if notifier.check_threshold(15):
    print(notifier.last_notification)  # Output: "ALERT: Value 15 exceeds threshold 10!"
```

### CI Pipeline
1. Install Python 3.12 + dependencies
2. Run unit tests with pytest
3. Static analysis with mypy + ruff
4. Code formatting verification
5. Generate test coverage report

## Getting Started

Set up development environment:
    Create a virtual environment:
``` shell
python -m venv .venv
``` 
``` shell
source .venv/bin/activate
```
Install dependencies:
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

Tests Overview
Unit Tests
Calculator: Tests addition, subtraction, multiplication.

Logger: Tests logging of operations.

Notifier: Tests threshold alerts.

Integration Tests
Calculator ↔ Logger: Ensures calculator results are logged properly.

Logger ↔ Notifier: Ensures notifications trigger logging correctly.

End-to-End Test
Performs a calculation, logs it, and sends a notification if the result exceeds the threshold.

## CI Configuration (.circleci/config.yml)
``` shell
version: 2.1

orbs:
  python: circleci/python@2.0.3

jobs:
  build_and_test:
    docker:
      - image: cimg/python:3.12
    steps:
      - checkout
      - python/install-packages:
          args: ".[dev]"
      - run:
          name: Run Static Analysis and Linting
          command: |
            ruff check .
            mypy .
      - run:
          name: Run Unit Tests and Coverage Report
          command: |
            pytest --cov=src --cov-report=xml --junitxml=test-results/results.xml
      - store_test_results:
          path: test-results/
      - store_artifacts:
          path: coverage.xml

workflows:
  test_and_deploy:
    jobs:
      - build_and_test

``` 


## Start Development
1. Clone repository
2. Set up virtual environment
3. Install dev dependencies
4. Create feature branch
5. Submit PR using template

## Contribution Guidelines
1. Follow these guidelines to contribute to the project:

2. Create a feature branch from main.

3. Write unit tests for new features or fixes.

4. Ensure all tests pass before submitting a pull request.

5. Use type hints for all functions/methods.

6. Follow PEP8 style guide for clean code.

7. Submit PRs using the provided template in .github/PULL_REQUEST_TEMPLATE.md
