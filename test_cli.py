from click.testing import CliRunner
from cli import search


def test_cli():
    runner = CliRunner()
    result = runner.invoke(search, ("--path", ".", "--ftype", "py"))
    assert result.exit_code == 0
    assert ".py" in result.output