import json
import yaml


def parse(file, format):
    if format == 'json':
        return json.load(file)
    if format in ['yaml', 'yml']:
        return yaml.load(file, Loader=yaml.FullLoader)
    raise ValueError('Unknown file format.')
