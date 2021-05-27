#!/usr/bin/env python3


from gendiff import gendiff
from gendiff.cli_args import parse


def main():
    args = parse()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
