#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

PROJECT_FILES = {
    "Minimal": [
        "src/{{ cookiecutter.project_slug }}/minimal.py",
        "tests/{{ cookiecutter.project_slug }}/test_minimal.py",
    ],
    "Library": [
        "src/{{ cookiecutter.project_slug }}/library.py",
        "tests/{{ cookiecutter.project_slug }}/test_library.py",
    ],
    "Click": [
        "src/{{ cookiecutter.project_slug }}/cli/cli_click.py",
        "tests/{{ cookiecutter.project_slug }}/test_click.py",
    ],
    "Typer": [
        "src/{{ cookiecutter.project_slug }}/cli/cli_typer.py",
        "tests/{{ cookiecutter.project_slug }}/test_typer.py",
    ],
    "Argparse": [
        "src/{{ cookiecutter.project_slug }}/cli/cli_argparse.py",
        "tests/{{ cookiecutter.project_slug }}/test_argparse.py",
    ],
    "Flask": [
        "src/{{ cookiecutter.project_slug }}/flask_example.py",
        "tests/{{ cookiecutter.project_slug }}/test_flask.py",
    ],
    "FastApi": [
        "src/{{ cookiecutter.project_slug }}/fastapi_example.py",
        "tests/{{ cookiecutter.project_slug }}/test_fastapi.py",
    ],
}


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    for key, files in PROJECT_FILES.items():
        if key != "{{cookiecutter.project_type}}":
            for file in files:
                remove_file(file)
