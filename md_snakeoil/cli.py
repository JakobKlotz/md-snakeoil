from pathlib import Path

import typer
from typing_extensions import Annotated

from md_snakeoil.apply import Formatter

app = typer.Typer(help="Format and lint Python code blocks in Markdown files.")


# default command
@app.callback(invoke_without_command=True)
def main(
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            help="File or directory to format",
        ),
    ] = None,
    line_length: Annotated[
        int,
        typer.Option(
            help="Maximum line length for the formatted code",
        ),
    ] = 79,
    rules: Annotated[
        str,
        typer.Option(
            help="Ruff rules to apply (comma-separated)",
        ),
    ] = "I,W",
    ctx: typer.Context = typer.Context,
):
    """Format & lint Markdown files - either a single file or all files
    in a directory."""
    # skip if a subcommand was invoked or path is None
    if ctx.invoked_subcommand or path is None:
        return

    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )
    # single file
    if path.is_file():
        formatter.run(path, inplace=True)
        typer.echo(f"Formatted {path}")

    # process the directory
    else:
        for markdown_file in path.glob("**/*.md"):
            formatter.run(markdown_file, inplace=True)
            typer.echo(f"Formatted {markdown_file}")


@app.command(deprecated=True)
def file(
    file_path: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, file_okay=True)
    ],
    line_length: Annotated[
        int,
        typer.Option(
            help="Maximum line length for the formatted code",
        ),
    ] = 79,
    rules: Annotated[
        str,
        typer.Option(
            help="Ruff rules to apply (comma-separated)",
        ),
    ] = "I,W",
):
    """Process a single Markdown file (deprecated, use 'snakeoil' without a
    command)."""
    typer.echo("Warning: 'file' command is deprecated")
    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )

    formatter.run(file_path, inplace=True)
    typer.echo(f"Formatted {file_path}")


@app.command(deprecated=True)
def directory(
    directory_path: Annotated[
        Path, typer.Argument(exists=True, dir_okay=True)
    ],
    line_length: Annotated[
        int,
        typer.Option(
            help="Maximum line length for the formatted code",
        ),
    ] = 79,
    rules: Annotated[
        str,
        typer.Option(
            help="Ruff rules to apply (comma-separated)",
        ),
    ] = "I,W",
):
    """Format all Markdown files within a directory
    (deprecated, use 'snakeoil' without a command)."""
    typer.echo("Warning: 'directory' command is deprecated")
    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )

    for markdown_file in directory_path.glob("**/*.md"):
        formatter.run(markdown_file, inplace=True)
        typer.echo(f"Formatted {markdown_file}")


if __name__ == "__main__":
    app()
