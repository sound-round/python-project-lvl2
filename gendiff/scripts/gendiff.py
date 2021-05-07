#!/usr/bin/env python3


import argparse
from gendiff import gendiff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f', '--format',
    default='stylish',
    choices=['stylish', 'plain'],
    help='set format of output (default: "stylish")',
)
args = parser.parse_args()


def main():
    gendiff.generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
