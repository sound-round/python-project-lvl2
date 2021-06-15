def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value).lower()


def turn_path_to_str(path):
    return '.'.join(path)


def format(node):  # noqa: C901
    lines = []
    path = []

    def walk(tree, path):

        for node in tree:
            new_path = path.copy()
            new_path.append(node['key'])
            if node['type'] == 'nested':
                walk(node['children'], new_path)

            if node['type'] == 'removed':
                lines.append(
                    "Property '{}' was removed".format(
                        turn_path_to_str(new_path)
                    )
                )

            if node['type'] == 'added':
                lines.append(
                    "Property '{}' was added with value: {}".format(
                        turn_path_to_str(new_path),
                        stringify(node['value'])
                    )
                )

            if node['type'] == 'changed':
                lines.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(new_path),
                        stringify(node['old_value']),
                        stringify(node['new_value'])
                    )
                )
        return '\n'.join(lines)

    return walk(node, path)
