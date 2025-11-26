# python-google-ai

A minimal Python project scaffold for quick experiments and demos. Includes a small CLI for basic text summarization, a package layout, tests, and a PEP 621 `pyproject.toml`.

## Quickstart

Create an environment and install dependencies (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -U pip; pip install -e .[dev]
```

Run tests:

```powershell
pytest -q
```

Run CLI:

```powershell
# using a module runner (preferred to avoid importing submodule directly)
python -m python_google_ai "A long text to summarize"

# or using the console script after installation:
python-google-ai "A long text to summarize" --max-len 50
```
