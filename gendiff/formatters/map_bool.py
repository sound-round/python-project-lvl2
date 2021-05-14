from gendiff.formatters import stylish_format, plain_format, json_format


map_bool = {
    True: 'true',
    False: 'false',
    None: 'null',
}

FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format,
}