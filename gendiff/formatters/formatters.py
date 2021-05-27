from gendiff.formatters import stylish_format, plain_format, json_format


def format_diff(diff, format):
    if format == 'stylish':
        return stylish_format.format_diff(diff)
    elif format == 'plain':
        return plain_format.format_diff(diff)
    return json_format.format_diff(diff)
