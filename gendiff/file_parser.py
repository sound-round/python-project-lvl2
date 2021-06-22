import json
import yaml


INPUT_FORMATS = ['json', 'yaml']


def parse(file_data, format):
    if format == 'json':
        return json.load(file_data)
    if format in ['yaml', 'yml']:
        return yaml.load(file_data, Loader=yaml.FullLoader)
    raise ValueError(
        f'Unknown input format: {format}. '
        f'Choose from {", ".join(INPUT_FORMATS)}.'
    )
