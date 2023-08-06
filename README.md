# Setting up the project
This is a repo used in the [Cloud Native Consulting Blog Article](https://cloudnativeconsulting.nl/2023/08/06/tools-that-every-python-dev-should-use/).

To set up the project, follow the steps below:

1. **Read about Poetry:** To learn more about Poetry, visit [python-poetry.org](https://python-poetry.org/).

2. **Installing Poetry locally:** Use the following command to install Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Once installed, check the last few lines of the installation prompt, and add Poetry to your `$PATH`:
   ```bash
   export PATH="/Users/myuser/.local/bin:$PATH"
   poetry --version
   ```

3. **Clone the repository:** Clone the repository locally using the following command:
   ```bash
   gh repo clone mr-sailor/tools-for-every-python-dev
   ```

4. **Activate Poetry environment:** Activate the Poetry environment and install the project dependencies:
   ```bash
   poetry shell
   poetry install
   ```

5. **Ensure pre-commit is configured:** Install and configure pre-commit hooks:
   ```bash
   pre-commit install
   ```

The repository is now ready to use. The repository was initially set up using the following commands:
```bash
poetry new tools-for-every-python-dev --name lib
poetry add black pre-commit pylint mypy pyflakes isort
```

By following these steps, you should be able to reproduce the environment used for a demo. Happy coding!