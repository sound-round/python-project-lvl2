import itertools
from gendiff.formatters.map_item_input_to_output import map_item_input_to_output


REPLACER = '    '
map_type_to_sign = {
    'unchanged': ' ',
    'nested': ' ',
    'removed': '-',
    'added': '+',
}


def stringify(value):
    if isinstance(value, dict):
        return value
    if value in map_item_input_to_output.keys():
        return map_item_input_to_output[value]
    return value


def format(data):  # noqa: C901
    def walk(tree, depth):

        current_indent = REPLACER * depth
        deep_indent = (REPLACER * (depth + 1))[:-2]
        lines = []
        if not isinstance(tree, list):
            if not isinstance(tree, dict):
                return str(tree)
            for key, value in tree.items():
                lines.append(
                    '{}{} {}: {}'.format(deep_indent,
                                         map_type_to_sign['nested'], key,
                                         walk(value, depth + 1)))
        else:

            for string in tree:
                if string['type'] == 'nested':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent, map_type_to_sign['nested'],
                        string['key'],
                        walk(string['children'], depth + 1)
                    ))
                    continue
                if string['type'] == 'changed':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        map_type_to_sign['removed'],
                        string['key'],
                        walk(
                            stringify(string['old_value']),
                            depth + 1,
                        )
                    ))
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        map_type_to_sign['added'],
                        string['key'],
                        walk(
                            stringify(string['new_value']),
                            depth + 1,
                        )
                    ))
                    continue

                lines.append('{}{} {}: {}'.format(
                    deep_indent,
                    map_type_to_sign[string['type']],
                    string['key'],
                    walk(
                        stringify(string['value']),
                        depth + 1
                    )
                ))

        formated_diff = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(formated_diff)

    return walk(data, 0)
