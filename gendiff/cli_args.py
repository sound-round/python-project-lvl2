import argparse
from gendiff.formatters import formatters


def parse():
    parser = argparse.ArgumentParser(description='Generate data')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=formatters.OUTPUT_FORMATS,
        help='set format of output (default: "stylish")',
    )
    return parser.parse_args()
