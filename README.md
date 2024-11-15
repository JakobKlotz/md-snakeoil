# md-snakeoil

A Python package to format and lint Python code blocks within Markdown files.
Specifically designed for Markdown files used with `mkdocs-material`.

`md-snakeoil` is built on the awesome `ruff` formatter and linter and helps you
to keep your Markdown files looking sharp.

## Command Line Interface

The package provides a command-line interface (CLI) using `typer`.
The CLI has two main commands:

1. `file`: Formats and lints Python code blocks in a single Markdown file.
2. `directory`: Recursively formats and lints Python code blocks in all
   Markdown files within a directory.

### Usage

#### Help

```bash
snakeoil --help
```

```                                                                                                                                                   
 Usage: snakeoil [OPTIONS] COMMAND [ARGS]...                                                                                                       
                                                                                                                                                   
 Format and lint Python code blocks in Markdown files.

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                         │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                  │
│ --help                        Show this message and exit.                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ file        Process a single Markdown.                                                                                                          │
│ directory   Format all Markdown files within a directory (recursively!).                                                                        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

By default, the line length is set to 79 characters, and the Ruff rules `W` and
`I` are enabled. You can change these defaults using the `--line-length` and
`--rules` options.

#### Single Markdown

```bash
snakeoil file path/to/file.md
```

#### Formatting all files in a directory

```bash
snakeoil directory path/to/directory
```

This will recursively format and lint the Python code blocks in all Markdown
files within `path/to/directory`.
