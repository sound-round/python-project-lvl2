"""Main module of gendiff-utility"""


import json
import yaml
from gendiff.dictionaries.json_dictionary import get_json_value
from gendiff.dictionaries.yaml_dictionary import get_yaml_value
from gendiff.formatters import stylish


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


def generate_diff(path_to_first_file, path_to_second_file, formatter=stylish):
    """
    This function returns difference between first_file and second_file

    """

    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)
    convert_value = convert(path_to_first_file)

    def inner(node1, node2):


        def walk(node1, node2):

            diff = []
            common_keys = node1.keys() & node2.keys()
            removed_keys = node1.keys() - node2.keys()
            added_keys = node2.keys() - node1.keys()

            for key in common_keys:
                if isinstance(node1[key], dict) and isinstance(node2[key], dict):
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
                            'value': convert_value(node1[key]),
                        })
                    else:
                        diff.append({
                            'key': key,
                            'type': 'changed',
                            'old_value': convert_value(node1[key]),
                            'new_value': convert_value(node2[key]),
                        })

            for key in removed_keys:
                diff.append({
                    'key': key,
                    'type': 'removed',
                    'value': convert_value(node1[key]),
                })

            for key in added_keys:
                diff.append({
                    'key': key,
                    'type': 'added',
                    'value': convert_value(node2[key]),
                })
            return diff

        diff = walk(node1, node2)
        print(formatter.format_diff(diff))
        return formatter.format_diff(diff)

    return inner(first_file, second_file)
