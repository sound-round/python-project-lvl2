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
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return value
    if value in map_item_input_to_output.keys():
        return map_item_input_to_output[value]
    return value


def format(diff):  # noqa: C901
    def iter_(diff, depth):

        current_indent = REPLACER * depth
        deep_indent = (REPLACER * (depth + 1))[:-2]
        lines = []
        if not isinstance(diff, list):
            if not isinstance(diff, dict):
                return str(diff)
            for key, value in diff.items():
                lines.append(
                    '{}{} {}: {}'.format(deep_indent,
                                         map_type_to_sign['nested'], key,
                                         iter_(value, depth + 1)))
        else:

            for string in diff:
                if string['type'] == 'nested':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent, map_type_to_sign['nested'],
                        string['key'],
                        iter_(string['children'], depth + 1)
                    ))
                elif string['type'] == 'changed':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        map_type_to_sign['removed'],
                        string['key'],
                        iter_(
                            stringify(string['old_value']),
                            depth + 1,
                        )
                    ))
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        map_type_to_sign['added'],
                        string['key'],
                        iter_(
                            stringify(string['new_value']),
                            depth + 1,
                        )
                    ))
                else:
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        map_type_to_sign[string['type']],
                        string['key'],
                        iter_(
                            stringify(string['value']),
                            depth + 1
                        )
                    ))

        formated_diff = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(formated_diff)

    return iter_(diff, 0)
