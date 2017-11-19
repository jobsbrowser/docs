#! /usr/bin/env python

import argparse
import contextlib
import re
import sys
from os import listdir
from os.path import isfile, join


@contextlib.contextmanager
def open_or_stdout(filename):
    if not filename:
        yield sys.stdout
    else:
        with open(filename, "w") as f:
            yield f


def get_directory_content(dirname):
    def node_order(node):
        regexp = r'(\w+\/)*(?P<order>\d+)_[^/]+$'
        match = re.search(regexp, node)
        return match and int(match.groupdict().get("order"))

    nodes = [join(dirname, node) for node in listdir(dirname)
             if node_order(node)]
    return sorted(nodes, key=node_order)


def merge_directory(dirname, output, depth=0):
    directory = get_directory_content(dirname)
    for node in directory:
        if isfile(node):
            merge_file(node, output, depth)
        else:
            merge_directory(node, output, depth + 1)


def adjust_headers(text, depth):
    extra_markdown = "#" * depth
    return re.sub(
        r'(^#+\s)',
        lambda m: extra_markdown + m.group(0),
        text, flags=re.MULTILINE
    )


def merge_file(filename, output, depth):
    with open(filename, "r") as fragment:
        text = adjust_headers(fragment.read(), depth)
        output.write(text)
        # double new line for proper markdown rendering
        output.write("\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sources_root", type=str,
                        help="path to documentation source files")
    parser.add_argument("-o", "--output", type=str, help="path to output file",
                        required=False)
    args = parser.parse_args()

    with open_or_stdout(args.output) as output:
        try:
            merge_directory(args.sources_root, output)
        except FileNotFoundError:
            output.flush()
            sys.exit(f"ERROR: {args.sources_root} is not valid path.")
