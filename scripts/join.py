#! /usr/bin/env python

import argparse
import contextlib
import logging
import re
import sys
from os import listdir
from os.path import isfile, join, exists

TITLE_FILE_NAME = '__title__.md'

logger = logging.getLogger("Join script")


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
    nodes.sort(key=node_order)

    title_file = join(dirname, TITLE_FILE_NAME)
    if exists(title_file):
        nodes.insert(0, title_file)
    return nodes


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
        if TITLE_FILE_NAME in filename:
            expected_depth = max(0, depth - 1)
        else:
            expected_depth = depth
        text = adjust_headers(fragment.read(), expected_depth)
        output.write(text)
        # double new line for proper markdown rendering
        output.write("\n\n")
        logger.info(f"Parsed file: [{filename}]; Depth: [{expected_depth}]")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
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
