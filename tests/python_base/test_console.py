"""Test cases for the console module."""
import pytest
from click.testing import CliRunner

from python_base import python_base_cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(python_base_cli.main)
    assert result.exit_code == 0