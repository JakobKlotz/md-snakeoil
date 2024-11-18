![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

<p align="center">
    <img src="https://raw.githubusercontent.com/mciwing/md-snakeoil/refs/heads/main/.assets/md-snakeoil.png" width="400" height="400">
</p>

A Python package/CLI to format and lint Python code blocks within Markdown 
files.
Specifically designed for Markdown files used with 
[`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/).

`md-snakeoil` is built on the awesome [`ruff`](https://docs.astral.sh/ruff/)
formatter and linter and helps you to keep your Markdown files looking sharp.

<p align="center">
    <img src="https://raw.githubusercontent.com/mciwing/md-snakeoil/refs/heads/main/.assets/before-after.png">
</p>

<hr>

## Installation

```bash
pip install md-snakeoil
```

## Command Line Interface

The package provides a command-line interface (CLI) using `typer`.
The CLI has two main commands:

1. `file`: Formats and lints Python code blocks in a single Markdown file.
2. `directory`: Recursively formats and lints Python code blocks in all
   Markdown files within a directory.

## Usage

### Help

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

You can pull up the help page for individual commands:

```bash
snakeoil file --help
snakeoil directory --help
```

### Single Markdown

```bash
snakeoil file path/to/file.md
```

### Formatting all files in a directory

```bash
snakeoil directory path/to/directory
```

This will recursively format and lint the Python code blocks in all Markdown
files within `path/to/directory`.
