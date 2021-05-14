"""Main module of gendiff-utility"""


def generate(node1, node2):

    diff = []
    common_keys = node1.keys() & node2.keys()
    removed_keys = node1.keys() - node2.keys()
    added_keys = node2.keys() - node1.keys()

    for key in common_keys:
        if isinstance(node1[key], dict) and isinstance(
                node2[key], dict
        ):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': generate(node1[key], node2[key]),
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

    for key in removed_keys:
        diff.append({
            'key': key,
            'type': 'removed',
            'value': node1[key],
        })

    for key in added_keys:
        diff.append({
            'key': key,
            'type': 'added',
            'value': node2[key],
        })
    return diff
