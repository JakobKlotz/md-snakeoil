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
formatter and linter and helps you to keep your Markdown files looking 
sharp. 🤙🏽

---

<h2 align="center"> before vs. after</h2>

<p align="center">
  <img src="https://raw.githubusercontent.com/mciwing/md-snakeoil/refs/heads/main/.assets/before.png" width="370" alt="Before implementation">
  <img src="https://raw.githubusercontent.com/mciwing/md-snakeoil/refs/heads/main/.assets/after.png" width="370" alt="After implementation">
</p>

<hr>

## Quickstart

Use [`pipx`](https://pipx.pypa.io/stable/installation/): 

```bash
pipx install md-snakeoil
```

Format and lint Markdown files within a directory (recursively):

```bash
snakeoil path/to/directory
```

That's it! 🚀

> [!NOTE]
> If, your using [`uv`](https://docs.astral.sh/uv/getting-started/installation/), install it with `uv tool install md-snakeoil`

## Command Line Interface

The package provides a command-line interface (CLI) using `typer`.

### Help

```bash
snakeoil --help
```

```                                                                                                                                                                                                                                                                                                   
 Usage: snakeoil [OPTIONS] [PATH] COMMAND [ARGS]...                                                                                              
                                                                                                                                                 
 Format and lint Python code blocks in Markdown files.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   path      [PATH]  File or directory to format [default: None]                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --line-length               INTEGER  Maximum line length for the formatted code [default: 79]                                                 │
│ --rules                     TEXT     Ruff rules to apply (comma-separated) [default: I,W]                                                     │
│ --install-completion                 Install completion for the current shell.                                                                │
│ --show-completion                    Show completion for the current shell, to copy it or customize the installation.                         │
│ --help                               Show this message and exit.                                                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

By default, the line length is set to 79 characters, and the Ruff rules `W` and
`I` are enabled. You can change these defaults using the `--line-length` and
`--rules` options.

### Single Markdown

```bash
snakeoil path/to/file.md
```

### Formatting all files in a directory

```bash
snakeoil path/to/directory
```

This will recursively format and lint the Python code blocks in all Markdown
files within `path/to/directory`.
