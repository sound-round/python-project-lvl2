"""Main module of gendiff-utility"""


def build_diff(node1, node2):

    diff = []
    all_keys = node1.keys() | node2.keys()
    removed_keys = node1.keys() - node2.keys()
    added_keys = node2.keys() - node1.keys()

    for key in all_keys:
        if key in removed_keys:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': node1[key],
            })
            continue

        elif key in added_keys:
            diff.append({
                'key': key,
                'type': 'added',
                'value': node2[key],
            })
            continue

        if isinstance(node1[key], dict) and isinstance(
                node2[key], dict
        ):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(node1[key], node2[key]),
            })
        elif node1[key] == node2[key]:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': node1[key],
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': node1[key],
                'new_value': node2[key],
            })
    return diff
