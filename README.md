# SmartHome

OOP prototype of a smart home agent. Direction: smart home.

## Structure

```
data/         synthetic sensor readings (smart_home_events_raw.csv)
src/smarthome package source
tests/        pytest stubs
docs/         backlog, kanban, architecture
```

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
```

Creates the virtual environment, resolves `pyproject.toml` and installs the package with
its `dev` extra (`pytest`, `pytest-cov`, `ruff`) in editable mode.

## Run

```bash
python -m smarthome
```

The entry point raises `NotImplementedError` until the agent logic lands.

## Tests and lint

```bash
pytest
pytest --cov
ruff check .
ruff format .
```

## Docs

- [Architecture](docs/architecture.md)