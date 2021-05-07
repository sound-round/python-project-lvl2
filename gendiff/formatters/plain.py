BOOL = ['null', 'false', 'true']


def turn_path_to_str(path):
    return '.'.join(path)


def convert_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str) and value not in BOOL:
        return "'{}'".format(value)
    return value


def format_diff(diff):  # noqa: C901
    result = []
    path = []

    def walk(diff):

        for node in sorted(diff, key=lambda node: node['key']):
            if node['type'] == 'nested':
                path.append(node['key'])
                walk(node['children'])
                path.pop()
            elif node['type'] == 'removed':
                path.append(node['key'])
                result.append(
                    "Property '{}' was removed".format(turn_path_to_str(path))
                )
                path.pop()
            elif node['type'] == 'added':
                path.append(node['key'])
                result.append(
                    "Property '{}' was added with value: {}".format(
                        turn_path_to_str(path),
                        convert_value(node['value'])
                    )
                )
                path.pop()
            elif node['type'] == 'changed':
                path.append(node['key'])
                result.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(path),
                        convert_value(node['old_value']),
                        convert_value(node['new_value'])
                    )
                )
                path.pop()

        return '\n'.join(sorted(result))

    return walk(diff)
