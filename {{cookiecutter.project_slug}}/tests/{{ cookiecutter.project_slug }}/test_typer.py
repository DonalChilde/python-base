from typer.testing import CliRunner

from {{ cookiecutter.project_slug }}.cli.cli_typer import main

runner = CliRunner()


def test_app():
    result = runner.invoke(main, ["hello","World!"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout
