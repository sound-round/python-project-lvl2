#!/usr/bin/env python3


from gendiff import gendiff
from gendiff.parser import parse


def main():
    parser = parse()
    args = parser.parse_args()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.format)
    print(diff)

if __name__ == '__main__':
    main()
