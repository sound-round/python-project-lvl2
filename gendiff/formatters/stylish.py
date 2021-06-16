import itertools

CR = '\n'
REPLACER = '    '
HALF_REPLACER = '  '
map_type_to_sign = {
    'unchanged': ' ',
    'nested': ' ',
    'removed': '-',
    'added': '+',
}


def stringify(tree, depth):

    if isinstance(tree, dict):
        current_indent = REPLACER * depth
        deep_indent = current_indent + HALF_REPLACER

        formatted_value = []
        for key, value in tree.items():
            formatted_value.append(
                '{}  {}: {}'.format(
                    deep_indent,
                    key,
                    stringify(value, depth + 1),
                )
            )
        return '{{{}}}'.format(
            CR + CR.join(formatted_value) + CR + current_indent
        )
    if tree is None:
        return 'null'
    if isinstance(tree, str):
        return tree
    return str(tree).lower()


def format(data):

    def walk(tree, depth):
        current_indent = REPLACER * depth
        deep_indent = current_indent + HALF_REPLACER
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

        formated_diff = itertools.chain("{", lines, [current_indent + "}"])
        return CR.join(formated_diff)

    return walk(data, 0)
