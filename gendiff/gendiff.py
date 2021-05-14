"""Main module of gendiff-utility"""


from gendiff import parser
from gendiff.formatters import formatters
from gendiff import representation


def generate_diff(path_to_first_file,
                  path_to_second_file,
                  format_name='stylish'):
    """
    This function returns difference between first_file and second_file,
    in different formats (stylish, plain, json).

    """
    first_file_parser = parser.parse_file(path_to_first_file)
    second_file_parser = parser.parse_file(path_to_second_file)
    first_file = first_file_parser(open(path_to_first_file))
    second_file = second_file_parser(open(path_to_second_file))

    diff = representation.generate(first_file, second_file)
    return formatters.map_formatters[format_name].format_diff(diff)
