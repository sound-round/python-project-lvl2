from gendiff.formatters.map_bool import map_bool


def decode_value(value):
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return '[complex value]'
    if value in map_bool.keys():
        return map_bool[value]
    if isinstance(value, str):
        return "'{}'".format(value)
    return value


def turn_path_to_str(path):
    return '.'.join(path)


def format_diff(diff):  # noqa: C901
    lines = []
    path = []

    def walk(diff):

        for node in diff:
            if node['type'] == 'nested':
                path.append(node['key'])
                walk(node['children'])
                path.pop()
            elif node['type'] == 'removed':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was removed".format(turn_path_to_str(path))
                )
                path.pop()
            elif node['type'] == 'added':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was added with value: {}".format(
                        turn_path_to_str(path),
                        decode_value(node['value'])
                    )
                )
                path.pop()
            elif node['type'] == 'changed':
                path.append(node['key'])
                lines.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(path),
                        decode_value(node['old_value']),
                        decode_value(node['new_value'])
                    )
                )
                path.pop()

        return '\n'.join(lines)

    return walk(diff)
