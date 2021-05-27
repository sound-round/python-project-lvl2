import json


def format_diff(diff):  # noqa: C901
    return json.dumps(diff, indent=4)
