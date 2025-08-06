from pathlib import Path

import typer
from rich import print as rich_print
from rich.console import Console
from rich.progress import track
from rich.table import Table
from typing_extensions import Annotated

from md_snakeoil.apply import Formatter

app = typer.Typer(help="Format and lint Python code blocks in Markdown files.")


# default command
@app.command()
def main(
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            help="File or directory to process",
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
):
    """Format & lint Markdown files - either a single file or all files
    in a directory."""
    if path is None:
        typer.echo(
            "Error: Please provide a path to a file or directory", err=True
        )
        raise typer.Exit(1)

    if path.is_file() and path.suffix != ".md":
        typer.echo("Error: Please provide a Markdown file", err=True)
        raise typer.Exit(1)

    formatter = Formatter(
        line_length=line_length, rules=tuple(rules.split(","))
    )

    # single file
    if path.is_file():
        formatter.run(path, inplace=True, quiet=True)
        typer.echo(f"Formatted {path}")

    # process the directory
    else:
        files = list(path.glob("**/*.md"))
        if not files:
            typer.echo(f"No Markdown files found in {path}")
            raise typer.Exit(0)

        # track processed files and display overview results as table
        n_errors = 0
        table = Table(
            "Directory",
            "File",
            "Status",
            title=f"Results for {path}",
        )

        for markdown_file in track(files, description="Formatting files..."):
            try:
                formatter.run(markdown_file, inplace=True)
                status = ":white_check_mark:"
            except UnicodeDecodeError:
                status = (":cross_mark: Decode Error",)
                n_errors += 1
            except Exception as e:
                status = f":cross_mark: {str(e)[:30]}..."
                n_errors += 1

            # add processing result to table
            table.add_row(
                str(markdown_file.parent), markdown_file.name, status
            )

        Console().print(table)

        # summary message
        if n_errors > 0:
            rich_print(f"{n_errors} files could not be formatted. :warning:")
        else:
            rich_print(
                f"All {len(files)} files formatted successfully. :sparkles:"
            )


if __name__ == "__main__":
    app()
