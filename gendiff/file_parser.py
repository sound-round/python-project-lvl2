import json
import yaml


def parse_file(file, format):
    if format == 'json':
        return json.load(file)
    if format == 'yaml' or format == 'yml':
        return yaml.load(file, Loader=yaml.FullLoader)
