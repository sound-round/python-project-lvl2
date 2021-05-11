map_bool_python_to_json = {
    True: 'true',
    False: 'false',
    None: 'null',
}


def decode_value_stylish(value):
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return value
    if value in map_bool_python_to_json.keys():
        return map_bool_python_to_json[value]
    return value


def decode_value_plain(value):
    if str(value) == '0':
        return value
    if isinstance(value, dict):
        return '[complex value]'
    if value in map_bool_python_to_json.keys():
        return map_bool_python_to_json[value]
    if isinstance(value, str):
        return "'{}'".format(value)
    return value
