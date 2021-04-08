def get_yaml_value(value):
    dict_ = {
        True: 'true',
        False: 'false',
        None: 'null',
        dict: 'map',
        list: 'seq',
    }
    if value in dict_.keys():
        return dict_.get(value)
    return value
