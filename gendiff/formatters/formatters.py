from gendiff.formatters import stylish, plain, json


def format(data, format):
    if format == 'stylish':
        return stylish.format(data)
    elif format == 'plain':
        return plain.format(data)
    elif format == 'json':
        return json.format(data)
    raise ValueError('Unknown output format.')
