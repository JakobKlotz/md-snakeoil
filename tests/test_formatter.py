from pathlib import Path

import pytest

from md_snakeoil import Formatter


@pytest.fixture
def example_markdown():
    return Path("tests/test.md").read_text()


def test_read_markdown(example_markdown):
    formatter = Formatter()
    content = formatter.read_markdown("tests/test.md")
    assert content == example_markdown


def test_format_single_block():
    formatter = Formatter()
    code = "x = [1,2,344,    3]"
    formatted = formatter.format_single_block(code)
    assert formatted == "x = [1, 2, 344, 3]"


def test_format_markdown_content(example_markdown):
    formatter = Formatter()
    formatted_content = formatter.format_markdown_content(example_markdown)

    # check if the formatted content has the expected changes
    assert "x = [1, 2, 344, 3]" in formatted_content

    # check if imports were sorted
    assert (
        "from pathlib import Path\n\nfrom sklearn import datasets"
        in formatted_content
    )
    # previously, the dict spanned multiple lines
    assert '{"a": 1, "b": 2, "f": 323}' in formatted_content


def test_run_inplace(tmp_path, example_markdown):
    formatter = Formatter()
    test_file = tmp_path / "copy.md"
    test_file.write_text(example_markdown)

    formatter.run(test_file, inplace=True)

    # check if the file was updated in-place
    assert test_file.read_text() != example_markdown


def test_run_output_file(tmp_path, example_markdown):
    formatter = Formatter()
    test_file = tmp_path / "copy.md"
    test_file.write_text(example_markdown)

    output_file = tmp_path / "formatted_index.md"
    formatter.run(test_file, output_path=output_file)

    # check if the output file was created with the expected content
    assert output_file.exists()
    assert output_file.read_text() != example_markdown
    assert "x = [1, 2, 344, 3]" in output_file.read_text()
