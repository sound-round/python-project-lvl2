"""Main module of gendiff-utility"""

import itertools
import json
import yaml
from gendiff.dictionaries.json_dictionary import get_json_value
from gendiff.dictionaries.yaml_dictionary import get_yaml_value


INDENT = '  '


def open_file(file):
    if file.endswith('json'):
        return json.load(open(file))
    return yaml.load(open(file), Loader=yaml.FullLoader)


def convert(file):
    def dump(value):
        if file.endswith('json'):
            return get_json_value(value)
        return get_yaml_value(value)

    return dump


def generate_diff(path_to_first_file, path_to_second_file):
    """
    This function returns difference between first_file and second_file

    """

    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)
    lines = []
    converter = convert(path_to_first_file)

    for key, value in sorted(first_file.items()):
        if first_file.get(key) == second_file.get(key):
            lines.append(f'{INDENT}  {key}: {converter(value)}')
        else:
            if key in second_file:
                lines.append(f'{INDENT}- {key}: {converter(value)}')
                lines.append(
                    f'{INDENT}+ {key}: {converter(second_file.get(key))}'
                )
            else:
                lines.append(f'{INDENT}- {key}: {converter(value)}')

    for key, value in sorted(second_file.items()):
        if key in first_file:
            continue
        else:
            lines.append(f'{INDENT}+ {key}: {converter(value)}')

    result = '\n'.join(itertools.chain('{', lines, '}')).replace('"', '')
    print(result)
    return result
