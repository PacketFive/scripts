# mdviewer

Terminal markdown viewer that renders formatted markdown files with syntax highlighting and color support.

## Requirements

Python 3 with the `rich` library. Dependencies are specified in `requirements.txt`.

## Installation

Install dependencies using `pip`:

```sh
pip install -r requirements.txt
```

Optionally make the script executable and copy or symlink it to your `PATH`:

```sh
chmod +x mdviewer.py
cp mdviewer.py ~/.local/bin/mdviewer
```

## Usage

Render a markdown file directly to the terminal:

```sh
python3 mdviewer.py <path-to-markdown-file>
```

View output page by page through the terminal pager:

```sh
python3 mdviewer.py -p <path-to-markdown-file>
```
