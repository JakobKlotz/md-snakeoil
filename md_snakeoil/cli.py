from pathlib import Path

import typer
from typing_extensions import Annotated

from md_snakeoil.apply import Formatter

app = typer.Typer(help="Format and lint Python code blocks in Markdown files.")


@app.command()
def file(
    file_path: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, file_okay=True)
    ],
    line_length: Annotated[
        int,
        typer.Argument(
            help="Maximum line length for the formatted code",
        ),
    ] = 79,
    rules: Annotated[
        str,
        typer.Argument(
            help="Ruff rules to apply (comma-separated)",
        ),
    ] = "I,W",
):
    """Process a single Markdown."""
    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )

    formatter.run(file_path, inplace=True)


@app.command()
def directory(
    directory_path: Annotated[
        Path, typer.Argument(exists=True, dir_okay=True)
    ],
    line_length: Annotated[
        int,
        typer.Argument(
            help="Maximum line length for the formatted code",
        ),
    ] = 79,
    rules: Annotated[
        str,
        typer.Argument(
            help="Ruff rules to apply (comma-separated)",
        ),
    ] = "I,W",
):
    """
    Format all Markdown files within a directory (recursively!).
    """
    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )

    for markdown_file in directory_path.glob("**/*.md"):
        formatter.run(markdown_file, inplace=True)
        typer.echo(f"Formatted {markdown_file}")


if __name__ == "__main__":
    app()
