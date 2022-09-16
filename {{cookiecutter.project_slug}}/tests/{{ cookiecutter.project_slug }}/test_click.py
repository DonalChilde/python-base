from click.testing import CliRunner
from hello import hello


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(hello, ["World"])
    assert result.exit_code == 0
    assert result.output == "Hello World!\n"
