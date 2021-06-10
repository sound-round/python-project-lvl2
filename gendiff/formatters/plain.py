import copy


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
            print(f'path:{path}')
            if node['type'] == 'nested':
                new_path = copy.copy(path)
                new_path.append(node['key'])
                print(f'new_path:{new_path}')
                walk(node['children'], new_path)

            if node['type'] == 'removed':
                new_path = copy.copy(path)
                new_path.append(node['key'])
                lines.append(
                    "Property '{}' was removed".format(
                        turn_path_to_str(new_path)
                    )
                )

            if node['type'] == 'added':
                new_path = copy.copy(path)
                new_path.append(node['key'])
                lines.append(
                    "Property '{}' was added with value: {}".format(
                        turn_path_to_str(new_path),
                        stringify(node['value'])
                    )
                )

            if node['type'] == 'changed':
                new_path = copy.copy(path)
                new_path.append(node['key'])
                lines.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(new_path),
                        stringify(node['old_value']),
                        stringify(node['new_value'])
                    )
                )
        return '\n'.join(lines)

    return walk(data, path)
