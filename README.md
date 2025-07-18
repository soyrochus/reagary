# REAgent Ingestion Engine POC

This project demonstrates a minimal ingestion pipeline for AngularJS forms. It is designed around protocol-driven components and external configuration.

## Installation

Use [uv](https://github.com/astral-sh/uv) to install dependencies:

```bash
uv pip install -r pyproject.toml
```

## Usage

Run the pipeline on a sample file:

```bash
python cli_runner.py tests/sample_angularjs_form.html
```

## Testing

Execute tests with `pytest`:

```bash
uv pip install -r pyproject.toml -r test
pytest
```
