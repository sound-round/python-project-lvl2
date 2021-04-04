import itertools
import json
import gendiff.scripts.gendiff


def generate_diff():
    lines = []
    INDENT = '  '
    first_file = json.load(open(gendiff.scripts.gendiff.args.first_file))
    second_file = json.load(open(gendiff.scripts.gendiff.args.second_file))
    for key, value in first_file.items():
        if first_file.get(key) == second_file.get(key):
            lines.append(f'{INDENT}  {key}: {value}')
        else:
            if key in second_file:
                lines.append(f'{INDENT}- {key}: {value}')
                lines.append(f'{INDENT}+ {key}: {second_file.get(key)}')
            else:
                lines.append(f'{INDENT}- {key}: {value}')

    for key, value in second_file.items():
        if key in first_file:
            continue
        else:
            lines.append(f'{INDENT}+ {key}: {value}')

    result = itertools.chain('{', lines, '}')
    return '\n'.join(result)