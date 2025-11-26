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
Using environment variables with `.env`:

1. Copy the example file and edit values:

```powershell
cp .env.example .env
# Edit .env with your API keys (for example, GEMINI_API_KEY)
```

2. When running locally, the project will automatically load `.env` variables if `python-dotenv` is installed:

```powershell
# Run CLI (will load GEMINI_API_KEY from .env if present)
python -m python_google_ai "Text to summarize"
```

3. Keep `.env` out of version control (it is ignored by `.gitignore`), and use `.env.example` to share keys structure.


# or using the console script after installation:
python-google-ai "A long text to summarize" --max-len 50
```
