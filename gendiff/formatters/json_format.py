import json

def sort(diff):
    diff.sort(key=lambda node: node['key'])
    for node in diff:
        if node.get('children'):
            sort(node.get('children'))
    return diff


def format_diff(diff):  # noqa: C901
    return json.dumps(sort(diff), indent=4)
