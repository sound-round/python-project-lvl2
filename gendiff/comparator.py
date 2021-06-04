"""Main module of gendiff-utility"""


from gendiff.formatters import formatters
from gendiff import tree
from gendiff import file_parser
import os


def get_format_file(path):
    return os.path.splitext(path)[1][1:]


def generate_diff(first_file_path,
                  second_file_path,
                  format='stylish'):
    """
    This function returns difference between first_file and second_file,
    in different formats (stylish, plain, json).

    """
    first_file_data = open(first_file_path)
    second_file_data = open(second_file_path)
    first_file_format = get_format_file(first_file_path)
    second_file_format = get_format_file(second_file_path)
    parsed_first_file = file_parser.parse(first_file_data, first_file_format)
    parsed_second_file = file_parser.parse(second_file_data, second_file_format)

    diff = tree.build_diff(parsed_first_file, parsed_second_file)
    return formatters.format(diff, format)
