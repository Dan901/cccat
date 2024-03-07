import argparse

from cccat.print import print_from_files, print_from_stdin


def main():
    parser = create_arg_parser()
    args = parser.parse_args()
    files = args.files
    number_lines = args.n or args.b
    skip_numbering_blank_lines = args.b
    if len(files) == 0 or files[0] == "-":
        print_from_stdin(
            number_lines=number_lines,
            skip_numbering_blank_lines=skip_numbering_blank_lines,
        )
        return
    print_from_files(
        files=files,
        number_lines=number_lines,
        skip_numbering_blank_lines=skip_numbering_blank_lines,
    )


def create_arg_parser():
    parser = argparse.ArgumentParser(
        prog="cccat",
        description=(
            "The cccat utility reads files sequentially, writing them to the "
            "standard output. The file operands are processed in command-line "
            "order. If file is a single dash (‘-’) or absent, cat reads from "
            "the standard input."
        ),
    )
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "-n",
        action="store_true",
        help="Number the output lines, starting at 1.",
    )
    parser.add_argument(
        "-b",
        action="store_true",
        help="Number the non-blank output lines, starting at 1.",
    )
    return parser


if __name__ == "__main__":
    main()
