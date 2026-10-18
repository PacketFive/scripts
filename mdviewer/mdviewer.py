#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0
import sys
import os
import argparse
import subprocess

try:
    from rich.console import Console
    from rich.markdown import Markdown
except ImportError:
    print("Error: The 'rich' library is required. Install it using: pip install rich", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Render Markdown files cleanly in the terminal.")
    parser.add_argument("file", help="Path to the markdown file to view")
    parser.add_argument("-p", "--pager", action="store_true", help="View output page-by-page using a terminal pager")
    
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Force rich to output with color/ANSI escape codes even when piped
    console = Console(force_terminal=True, color_system="truecolor")
    md = Markdown(content)

    if args.pager:
        # Render markdown to string with formatting intact, then pipe to 'less -R'
        with console.capture() as capture:
            console.print(md)
        rendered_text = capture.get()

        # Run system pager ('less -R' preserves ANSI colors and clears/pages correctly)
        try:
            pager = os.environ.get('PAGER', 'less')
            subprocess.run([pager, '-R'], input=rendered_text, text=True, check=True)
        except (subprocess.SubprocessError, FileNotFoundError):
            # Fallback if less fails: just print normally
            print(rendered_text)
    else:
        # Clear screen and print directly to standard terminal scrollback
        console.clear()
        console.print(md)

if __name__ == '__main__':
    main()
