map_bool = {
    True: 'true',
    False: 'false',
    None: 'null',
}


def decode_value_stylish(value):
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return value
    if value in map_bool.keys():
        return map_bool[value]
    return value


def decode_value_plain(value):
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return '[complex value]'
    if value in map_bool.keys():
        return map_bool[value]
    if isinstance(value, str):
        return "'{}'".format(value)
    return value
