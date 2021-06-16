import itertools


REPLACER = '    '
map_type_to_sign = {
    'unchanged': ' ',
    'nested': ' ',
    'removed': '-',
    'added': '+',
}


def stringify(tree, depth):

    if isinstance(tree, dict):
        indent = (REPLACER * (depth + 1))[:-2]
        res = []
        for key, value in tree.items():
            res.append(
                '{}  {}: {}'.format(
                    indent,
                    key,
                    stringify(value, depth + 1),
                )
            )
        return '{{{}}}'.format('\n' + '\n'.join(res) + '\n' + indent[:-2])
    if tree is None:
        return 'null'
    if isinstance(tree, str):
        return tree
    return str(tree).lower()


def format(data):  # noqa: C901
    def walk(tree, depth):

        deep_indent = (REPLACER * (depth + 1))[:-2]
        lines = []
        if not isinstance(tree, list) and not isinstance(tree, dict):
            return str(tree)
        for node in tree:
            if node['type'] == 'nested':
                lines.append('{}{} {}: {}'.format(
                    deep_indent, map_type_to_sign['nested'],
                    node['key'],
                    walk(node['children'], depth + 1)
                ))
                continue
            if node['type'] == 'changed':
                lines.append('{}{} {}: {}'.format(
                    deep_indent,
                    map_type_to_sign['removed'],
                    node['key'],

                    stringify(
                        node['old_value'],
                        depth + 1,
                    )
                ))
                lines.append('{}{} {}: {}'.format(
                    deep_indent,
                    map_type_to_sign['added'],
                    node['key'],
                    stringify(
                        node['new_value'],
                        depth + 1,
                    )
                ))
                continue

            lines.append('{}{} {}: {}'.format(
                deep_indent,
                map_type_to_sign[node['type']],
                node['key'],
                stringify(
                    node['value'],
                    depth + 1
                )
            ))
        current_indent = REPLACER * depth
        formated_diff = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(formated_diff)

    return walk(data, 0)
