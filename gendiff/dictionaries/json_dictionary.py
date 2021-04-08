def get_json_value(value):
    dict_ = {
        True: 'true',
        False: 'false',
        None: 'null',
        dict: 'Object',
        list: 'Array',
        tuple: 'Array',
        str: 'String',
        int: 'Number',
        float: 'Number',
    }
    if value in dict_.keys():
        return dict_.get(value)
    return value
