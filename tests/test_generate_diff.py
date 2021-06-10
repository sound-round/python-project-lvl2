from gendiff.comparator import generate_diff
import os
import pathlib


INPUT_FORMATS = ['json', 'yaml']
OUTPUT_FORMATS = ['stylish', 'plain', 'json']
FIXTURES_PATH = 'fixtures'


def read(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    return file


def get_fixture_path(fixture_name):
    return os.path.join(
        pathlib.Path(__file__).absolute().parent,
        FIXTURES_PATH,
        fixture_name
    )


def test_generate_diff_default():
    for input_format in INPUT_FORMATS:
        first_file = get_fixture_path(f'file1.{input_format}')
        second_file = get_fixture_path(f'file2.{input_format}')
        assert generate_diff(
            first_file,
            second_file,
        ) == read(get_fixture_path('result.stylish'))


def test_generate_diff_formats():
    for input_format in INPUT_FORMATS:
        first_file = get_fixture_path(f'file1.{input_format}')
        second_file = get_fixture_path(f'file2.{input_format}')
        for output_format in OUTPUT_FORMATS:
            expected_result = get_fixture_path(f'result.{output_format}')
            assert generate_diff(
                first_file,
                second_file,
                format=f'{output_format}',
            ) == read(expected_result)


def test_generate_diff_yaml_json():
    first_file = get_fixture_path('file1.yaml')
    second_file = get_fixture_path('file2.json')
    for output_format in OUTPUT_FORMATS:
        expected_result = get_fixture_path(f'result.{output_format}')
        assert generate_diff(
            first_file,
            second_file,
            format=f'{output_format}',
        ) == read(expected_result)
