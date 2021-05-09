import itertools
from gendiff.formatters import decoder


type_ = {
    'unchanged': ' ',
    'nested': ' ',
    'removed': '-',
    'added': '+',
}


REPLACER = '    '


def format_diff(diff):  # noqa: C901
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
                                         type_['nested'], key,
                                         iter_(value, depth + 1)))
        else:

            for string in sorted(diff, key=lambda string: string['key']):
                if string['type'] == 'nested':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent, type_['nested'],
                        string['key'],
                        iter_(string['children'], depth + 1)
                    ))
                elif string['type'] == 'changed':
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        type_['removed'],
                        string['key'],
                        iter_(decoder.decode_value_stylish(string['old_value']), depth + 1)
                    ))
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        type_['added'],
                        string['key'],
                        iter_(decoder.decode_value_stylish(string['new_value']), depth + 1)
                    ))
                else:
                    lines.append('{}{} {}: {}'.format(
                        deep_indent,
                        type_[string['type']],
                        string['key'],
                        iter_(decoder.decode_value_stylish(string['value']), depth + 1)
                    ))

        formated_diff = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(formated_diff)

    return iter_(diff, 0)
