from pathlib import Path
from typing import Annotated

import typer

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
    check: Annotated[
        bool,
        typer.Option(
            help="Check if files would be reformatted without writing changes"
        ),
    ] = False,
):
    """
    Format & lint Markdown files. Either a single file or all files in a
    directory,
    """
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
        _, msg = formatter.run(path, inplace=True, check=check)
        typer.echo(msg)

    # process the directory
    else:
        files = list(path.glob("**/*.md"))
        if not files:
            typer.echo(f"No Markdown files found in {path}")
            raise typer.Exit(0)

        files_changed = []
        errors = 0
        for markdown_file in files:
            try:
                has_changed, msg = formatter.run(
                    markdown_file, inplace=True, check=check
                )
                files_changed.append(has_changed)
            except UnicodeDecodeError:
                msg = f"{markdown_file} :cross_mark: Decode Error"
                errors += 1
            except Exception as e:
                msg = f"{markdown_file} :cross_mark: {str(e)[:30]}..."
                errors += 1
            print(msg)

        sum_files_changed, n_files = sum(files_changed), len(files)
        print(
            f"{sum_files_changed} "
            f"{'would be reformatted' if check else 'formatted'}, "
            f"{n_files - sum_files_changed - errors} already formatted."
        )
        if errors:
            print(f"{errors} errors.")
        if sum_files_changed and check:
            raise typer.Exit(1)


if __name__ == "__main__":
    app()
