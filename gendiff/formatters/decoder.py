decoding_dict = {
    True: 'true',
    False: 'false',
    None: 'null',
}


BOOL = ['null', 'false', 'true']


def decode_value_stylish(value):
    if isinstance(value, dict):
        return value
    if value in decoding_dict.keys():
        return decoding_dict[value]
    return value


def decode_value_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in decoding_dict.keys():
        return decoding_dict[value]
    if isinstance(value, str):
        return "'{}'".format(value)
    return value