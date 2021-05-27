"""Main module of gendiff-utility"""


from gendiff import cli_args
from gendiff.formatters import formatters
from gendiff import tree


def generate_diff(first_file_path,
                  second_file_path,
                  format='stylish'):
    """
    This function returns difference between first_file and second_file,
    in different formats (stylish, plain, json).

    """
    first_file_parser = cli_args.parse_file(first_file_path)
    second_file_parser = cli_args.parse_file(second_file_path)
    first_file = first_file_parser(open(first_file_path))
    second_file = second_file_parser(open(second_file_path))

    diff = tree.build_diff(first_file, second_file)
    return formatters.format_diff(diff, format)
