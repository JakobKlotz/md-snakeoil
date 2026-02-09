![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=for-the-badge)

<p align="center">
    <img src="https://raw.githubusercontent.com/mciwing/md-snakeoil/refs/heads/main/.assets/md-snakeoil.png" width="400" height="400">
</p>

Format and lint Python code blocks within Markdown files. Usable as CLI, 
`pre-commit` hook or Python package.

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

With [`uv`](https://docs.astral.sh/uv/getting-started/installation/) install 
it as a tool:

```bash
uv tool install md-snakeoil
```

Format and lint Markdown files within a directory (recursively):

```bash
snakeoil path/to/directory
```

That's it! 🚀

> [!NOTE]
> If, your using [`pipx`](https://pipx.pypa.io/stable/installation/), 
> install it with `pipx install md-snakeoil`

## `pre-commit` hook

To run `md-snakeoil` with `pre-commit` add following to your 
`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/JakobKlotz/md-snakeoil
    rev: v0.1.7
    hooks:
      - id: snakeoil
```

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

For example, format the example files within the `tests/` directory 
(of this repository):

```bash
snakeoil tests/examples
```

```bash
Formatting files... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
         Results for tests\examples
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Directory      ┃ File            ┃ Status ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ tests\examples │ indentation.md  │ ✅     │
│ tests\examples │ info_strings.md │ ✅     │
│ tests\examples │ test.md         │ ✅     │
└────────────────┴─────────────────┴────────┘
All 3 files formatted successfully. ✨
```
