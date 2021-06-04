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


def format(data):  # noqa: C901
    lines = []
    path = []

    def walk(tree, path):

        for node in tree:
            if node['type'] == 'nested':
                path.append(node['key'])
                walk(node['children'], path)
                path.pop()

            if node['type'] == 'removed':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was removed".format(turn_path_to_str(path))
                )
                path.pop()

            if node['type'] == 'added':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was added with value: {}".format(
                        turn_path_to_str(path),
                        stringify(node['value'])
                    )
                )
                path.pop()

            if node['type'] == 'changed':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(path),
                        stringify(node['old_value']),
                        stringify(node['new_value'])
                    )
                )
                path.pop()
        return '\n'.join(lines)

    return walk(data, path)
