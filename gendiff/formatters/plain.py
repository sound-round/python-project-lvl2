from gendiff.formatters import decoder





def turn_path_to_str(path):
    return '.'.join(path)


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
                        decoder.decode_value_plain(node['value'])
                    )
                )
                path.pop()
            elif node['type'] == 'changed':
                path.append(node['key'])
                result.append(
                    "Property '{}' was updated. From {} to {}".format(
                        turn_path_to_str(path),
                        decoder.decode_value_plain(node['old_value']),
                        decoder.decode_value_plain(node['new_value'])
                    )
                )
                path.pop()

        return '\n'.join(sorted(result))

    return walk(diff)
