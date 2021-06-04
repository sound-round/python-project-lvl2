"""Main module of gendiff-utility"""


def build_diff(node1, node2):

    tree = []
    all_keys = node1.keys() | node2.keys()
    removed_keys = node1.keys() - node2.keys()
    added_keys = node2.keys() - node1.keys()

    for key in sorted(all_keys):
        if key in removed_keys:
            tree.append({
                'key': key,
                'type': 'removed',
                'value': node1[key],
            })
            continue

        if key in added_keys:
            tree.append({
                'key': key,
                'type': 'added',
                'value': node2[key],
            })
            continue

        if isinstance(node1[key], dict) and isinstance(
                node2[key], dict
        ):
            tree.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(node1[key], node2[key]),
            })
            continue
        if node1[key] == node2[key]:
            tree.append({
                'key': key,
                'type': 'unchanged',
                'value': node1[key],
            })
            continue

        tree.append({
            'key': key,
            'type': 'changed',
            'old_value': node1[key],
            'new_value': node2[key],
        })
    return tree
