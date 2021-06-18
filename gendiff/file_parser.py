import json
import yaml


INPUT_FORMATS = ['json', 'yaml']


def parse(file, format):
    if format == 'json':
        return json.load(file)
    if format in ['yaml', 'yml']:
        return yaml.load(file, Loader=yaml.FullLoader)
    raise ValueError(
        f'Unknown input format: {format}. '
        f'Choose from {", ".join(INPUT_FORMATS)}.'
    )
