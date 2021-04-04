import itertools


def generate_diff(first_file, second_file):
    lines = []
    INDENT = '  '

    for key, value in sorted(first_file.items()):
        if first_file.get(key) == second_file.get(key):
            lines.append(f'{INDENT}  {key}: {value}')
        else:
            if key in second_file:
                lines.append(f'{INDENT}- {key}: {value}')
                lines.append(f'{INDENT}+ {key}: {second_file.get(key)}')
            else:
                lines.append(f'{INDENT}- {key}: {value}')

    for key, value in sorted(second_file.items()):
        if key in first_file:
            continue
        else:
            lines.append(f'{INDENT}+ {key}: {value}')

    result = '\n'.join(itertools.chain('{', lines, '}'))
    print(result)
    return result