"""Main module of gendiff-utility"""


import json
import yaml
from gendiff.formatters import stylish_format, plain_format, json_format


FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format,
}


def open_file(file):
    if file.endswith('json'):
        return json.load(open(file))
    return yaml.load(open(file), Loader=yaml.FullLoader)


def generate_diff(path_to_first_file,  # noqa: C901
                  path_to_second_file,
                  format_name):
    """
    This function returns difference between first_file and second_file,
    in different formats (stylish, plain, json).

    """

    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)

    def walk(node1, node2):

        diff = []
        common_keys = node1.keys() & node2.keys()
        removed_keys = node1.keys() - node2.keys()
        added_keys = node2.keys() - node1.keys()

        for key in common_keys:
            if isinstance(node1[key], dict) and isinstance(
                    node2[key], dict
            ):
                diff.append({
                    'key': key,
                    'type': 'nested',
                    'children': walk(node1[key], node2[key]),
                })
            else:
                if node1[key] == node2[key]:
                    diff.append({
                        'key': key,
                        'type': 'unchanged',
                        'value': node1[key],
                    })
                else:
                    diff.append({
                        'key': key,
                        'type': 'changed',
                        'old_value': node1[key],
                        'new_value': node2[key],
                    })

        for key in removed_keys:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': node1[key],
            })

        for key in added_keys:
            diff.append({
                'key': key,
                'type': 'added',
                'value': node2[key],
            })
        return diff

    diff = walk(first_file, second_file)
    print(FORMATTERS[format_name].format_diff(diff))
    return FORMATTERS[format_name].format_diff(diff)
