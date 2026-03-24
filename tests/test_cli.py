from click.testing import CliRunner

from llm_sbom import __version__
from llm_sbom.cli import main


def test_version_command_prints_package_version() -> None:
    runner = CliRunner()

    result = runner.invoke(main, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == __version__


def test_scan_empty_directory_table_output() -> None:
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(main, ["scan", ".", "--format", "table"])

    assert result.exit_code == 0
    assert "No model files found." in result.output