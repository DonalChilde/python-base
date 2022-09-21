# Project setup

Download and configure dev-tool.sh bash script

```bash
# From the project root directory, download the script to a subdirectory.
curl --create-dirs -O --output-dir ./scripts https://raw.githubusercontent.com/DonalChilde/dev-tool/main/scripts/dev-tool.sh

# Then make executable
chmod u+x ./scripts/dev-tool.sh

# Generate an .env config file in the script directory,
# and fill in the path to the project directory.
./scripts/dev-tool.sh generate-env ./scripts

```

If this is the first time using dev-tool.sh

```bash
# Install bash completion if desired
./scripts/dev-tool.sh completions ~/.bash_completions

# and add
echo "source ~/.bash_completions/dev-tool.completion" >> ~/.bashrc
# to ~/.bashrc
```

Initialize the project venv

```bash
# This will also update the build tools.
./scripts/dev-tool.sh venv-init
```

```bash
python -m piptools compile --upgrade --resolver backtracking -o requirements.txt pyproject.toml
python -m piptools compile --extra dev --upgrade --resolver backtracking -o requirements_dev.txt pyproject.toml
```
