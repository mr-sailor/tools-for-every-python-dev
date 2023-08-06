curl -sSL https://install.python-poetry.org | python3 - 
export PATH="/Users/myuser/.local/bin:$PATH"

poetry --version

poetry new tools-for-every-python-dev --name lib

poetry add black pre-commit pylint mypy pyflakes isort



pre-commit install