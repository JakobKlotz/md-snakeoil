import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from md_snakeoil.cli import app

runner = CliRunner()


@pytest.fixture
def test_file(tmp_path):
    example_markdown = Path("tests/examples/test.md").read_text()

    def _make_test_file(name: str) -> Path:
        f = tmp_path / name
        f.write_text(example_markdown)
        return f

    return _make_test_file


def test_no_path_provided():
    """Test error when no path is provided."""
    result = runner.invoke(app, [])
    assert result.exit_code == 1
    assert (
        "Error: Please provide a path to a file or directory" in result.stderr
    )


def test_non_markdown_file():
    """Test error when non-markdown file is provided."""
    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
        tmp.write(b"some content")
        tmp.flush()

        result = runner.invoke(app, [tmp.name])
        assert result.exit_code == 1
        assert "Error: Please provide a Markdown file" in result.stderr


def test_nonexistent_path():
    """Test error when path doesn't exist."""
    result = runner.invoke(app, ["/nonexistent/path.md"])
    assert result.exit_code == 2  # Typer's default for invalid argument


def test_single_markdown(test_file):
    """Test processing a single markdown."""
    # Make a temporary copy
    file_name = str(test_file("copy.md"))
    result = runner.invoke(app, [file_name])
    assert result.exit_code == 0
    assert f"Formatted: {file_name}" in result.output, result

    # another run with different options
    file_name = str(test_file("another-copy.md"))
    result = runner.invoke(
        app, [file_name, "--line-length", "120", "--rules", "E,F"]
    )
    assert result.exit_code == 0
    assert f"Formatted: {file_name}" in result.output, result


def test_single_markdown_check(test_file):
    """Single markdown using the check option."""
    file_name = str(test_file("_.md"))
    result = runner.invoke(app, [file_name, "--check"])
    assert result.exit_code == 0
    assert f"Would reformat: {file_name}"


def test_directory_processing():
    """Test processing a directory with markdown files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)

        # Create markdown files
        md1 = tmpdir_path / "test1.md"
        md2 = tmpdir_path / "subdir" / "test2.md"
        md2.parent.mkdir()

        md1.write_text("# Test 1\n\n```python\nimport os\n```\n")
        md2.write_text("# Test 2\n\n```python\nimport sys\n```\n")

        # Create non-markdown file (should be ignored)
        (tmpdir_path / "test.txt").write_text("not markdown")

        result = runner.invoke(app, [tmpdir])
        assert result.exit_code == 0
