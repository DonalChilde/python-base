#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

PROJECT_FILES = {
    "Minimal": [
        "src/{{ cookicutter.project_slug }}/minimal.py",
        "tests/{{ cookicutter.project_slug }}/test_minimal.py",
    ],
    "Library": [
        "src/{{ cookicutter.project_slug }}/library.py",
        "tests/{{ cookicutter.project_slug }}/test_library.py",
    ],
    "Click": [
        "src/{{ cookicutter.project_slug }}/cli/cli_click.py",
        "tests/{{ cookicutter.project_slug }}/test_click.py",
    ],
    "Typer": [
        "src/{{ cookicutter.project_slug }}/cli/cli_typer.py",
        "tests/{{ cookicutter.project_slug }}/test_typer.py",
    ],
    "Argparse": [
        "src/{{ cookicutter.project_slug }}/cli/cli_argparse.py",
        "tests/{{ cookicutter.project_slug }}/test_argparse.py",
    ],
    "Flask": [
        "src/{{ cookicutter.project_slug }}/flask_example.py",
        "tests/{{ cookicutter.project_slug }}/test_flask.py",
    ],
    "FastApi": [
        "src/{{ cookicutter.project_slug }}/fastapi_example.py",
        "tests/{{ cookicutter.project_slug }}/test_fastapi.py",
    ],
}


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    for key, files in PROJECT_FILES.items():
        if key != {{cookiecutter.project_type}}:
            for file in files:
                remove_file(file)
    # if "{{ cookiecutter.create_author_file }}" != "y":
    #     remove_file("AUTHORS.rst")
    #     remove_file("docs/authors.rst")

    # if "no" in "{{ cookiecutter.command_line_interface|lower }}":
    #     cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
    #     remove_file(cli_file)

    # if "Not open source" == "{{ cookiecutter.open_source_license }}":
    #     remove_file("LICENSE")
