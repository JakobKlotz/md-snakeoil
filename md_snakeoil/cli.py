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
):
    """Format & lint Markdown files - either a single file or all files
    in a directory."""
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
            try:
                formatter.run(markdown_file, inplace=True)
                typer.echo(f"Formatted {markdown_file}")
            except UnicodeDecodeError:
                typer.echo(
                    f"Error: Could not decode {markdown_file} - skipping file",
                    err=True,
                )
            except Exception as e:
                typer.echo(
                    f"Error processing {markdown_file}: {str(e)}", err=True
                )


if __name__ == "__main__":
    app()
