from gendiff.formatters import stylish, plain, json


OUTPUT_FORMATS = ['stylish', 'plain', 'json']


def format(data, format):
    if format == 'stylish':
        return stylish.format(data)
    if format == 'plain':
        return plain.format(data)
    if format == 'json':
        return json.format(data)
    raise ValueError(
        f'Unknown output format: {format}. '
        f'Choose from {", ".join(OUTPUT_FORMATS)}.'
    )
