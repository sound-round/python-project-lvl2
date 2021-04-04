#!/usr/bin/env python3


import argparse
from gendiff import gendiff
import json


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    return gendiff.generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()



