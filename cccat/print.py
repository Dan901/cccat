import sys
from typing import List


def print_from_files(files: List[str], **kwargs):
    for files in files:
        with open(files, "r") as f:
            _print_from_input(f, **kwargs)


def print_from_stdin(**kwargs):
    _print_from_input(sys.stdin, **kwargs)


def _print_from_input(input, **kwargs):
    number_lines = kwargs.get("number_lines", False)
    skip_numbering_blank_lines = kwargs.get("skip_numbering_blank_lines", False)
    line_number = 1
    while True:
        line = input.readline()
        if not line:
            break
        if not line.strip() and skip_numbering_blank_lines:
            print()
            continue
        formatted_line = "%6d  %s" % (line_number, line) if number_lines else line
        print(formatted_line, end="")
        line_number += 1
