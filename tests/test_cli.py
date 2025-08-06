import shutil
import tempfile
from pathlib import Path

from typer.testing import CliRunner

from md_snakeoil.cli import app

runner = CliRunner()


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


def test_single_markdown():
    """Test processing a single markdown."""
    # Make a temporary copy
    copy = Path("tests/examples/test_copy.md")
    shutil.copy(Path("tests/examples/test.md"), copy)

    result = runner.invoke(app, [str(copy)])
    assert result.exit_code == 0
    assert f"Formatted {copy}" in result.output, result

    # clean up
    copy.unlink()

    # another run with different options
    shutil.copy(Path("tests/examples/test.md"), copy)
    result = runner.invoke(
        app, [str(copy), "--line-length", "120", "--rules", "E,F"]
    )
    assert result.exit_code == 0
    assert f"Formatted {copy}" in result.output, result

    # clean up
    copy.unlink()


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
