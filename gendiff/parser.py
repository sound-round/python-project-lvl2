import argparse
import json
import yaml


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (default: "stylish")',
    )
    return parser


def parse_file(file):
    def inner(opened_file):
        if file.endswith('json'):
            return json.load(opened_file)
        return yaml.load(opened_file, Loader=yaml.FullLoader)
    return inner