"""Main module of gendiff-utility"""


from gendiff.formatters import formatters
from gendiff import tree
import pathlib
from gendiff import file_parser


def generate_diff(first_file_path,
                  second_file_path,
                  format='stylish'):
    """
    This function returns difference between first_file and second_file,
    in different formats (stylish, plain, json).

    """
    first_file = open(first_file_path)
    second_file = open(second_file_path)
    format_first_file = pathlib.PurePath(first_file_path).name.split('.')[1]
    format_second_file = pathlib.PurePath(second_file_path).name.split('.')[1]
    parsed_first_file = file_parser.parse_file(first_file, format_first_file)
    parsed_second_file = file_parser.parse_file(second_file, format_second_file)

    diff = tree.build_diff(parsed_first_file, parsed_second_file)
    return formatters.format_diff(diff, format)
