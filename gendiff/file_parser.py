import json
import yaml


yaml_format = ['yaml', 'yml']


def parse(file, format):
    if format == 'json':
        return json.load(file)
    if format in yaml_format:
        return yaml.load(file, Loader=yaml.FullLoader)
    raise ValueError('Unknown file format.')