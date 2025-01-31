# Python Project Template

Advanced Python template with strict quality controls and component architecture.

## Features

- 🚀 Component-based architecture
- ✅ Pytest with JUnit reporting
- ✨ Ruff (650+ checks enabled)
- 🔍 Mypy strict type checking
- 🔄 CircleCI pipeline with test visualization

## Component Definition

Components are Python packages within `src/` that:
- Encapsulate specific business logic
- Include type annotations
- Have 100% test coverage
- Follow strict style guidelines

## Quickstart

```bash
pip install uv
uv venv venv
uv pip install -e .[dev]

# Run checks
ruff check .
ruff format .
mypy src
pytest tests
