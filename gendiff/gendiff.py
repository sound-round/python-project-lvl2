"""Main module of gendiff-utility"""

import itertools
import json


INDENT = '  '


def generate_diff(first_file, second_file):
    """
    This function returns difference between first_file and second_file

    Args:
        first_file: path to the first file,

        second-file: path to the second file.

    """
    lines = []

    for key, value in sorted(first_file.items()):
        if first_file.get(key) == second_file.get(key):
            lines.append(f'{INDENT}  {key}: {json.dumps(value)}')
        else:
            if key in second_file:
                lines.append(f'{INDENT}- {key}: {json.dumps(value)}')
                lines.append(f'{INDENT}+ {key}: {second_file.get(key)}')
            else:
                lines.append(f'{INDENT}- {key}: {json.dumps(value)}')

    for key, value in sorted(second_file.items()):
        if key in first_file:
            continue
        else:
            lines.append(f'{INDENT}+ {key}: {json.dumps(value)}')

    result = '\n'.join(itertools.chain('{', lines, '}')).replace('"', '')
    print(result)
    return result
