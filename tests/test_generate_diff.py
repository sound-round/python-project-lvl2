from gendiff.comparator import generate_diff
import os
import pathlib
import pytest
from gendiff.file_parser import INPUT_FORMATS
from gendiff.formatters.formatters import OUTPUT_FORMATS


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


@pytest.mark.parametrize('input_format', INPUT_FORMATS)
def test_generate_diff_default(input_format):
    first_file_path = get_fixture_path(f'file1.{input_format}')
    second_file_path = get_fixture_path(f'file2.{input_format}')
    assert generate_diff(
        first_file_path,
        second_file_path,
    ) == read(get_fixture_path('result.stylish'))


@pytest.mark.parametrize('input_format', INPUT_FORMATS)
def test_generate_diff_formats(input_format):
    first_file_path = get_fixture_path(f'file1.{input_format}')
    second_file_path = get_fixture_path(f'file2.{input_format}')
    for output_format in OUTPUT_FORMATS:
        expected_result_path = get_fixture_path(f'result.{output_format}')
        assert generate_diff(
            first_file_path,
            second_file_path,
            format=output_format,
        ) == read(expected_result_path)


def test_generate_diff_different_formats():
    first_file_path = get_fixture_path('file1.yaml')
    second_file_path = get_fixture_path('file2.json')
    for output_format in OUTPUT_FORMATS:
        expected_result_path = get_fixture_path(f'result.{output_format}')
        assert generate_diff(
            first_file_path,
            second_file_path,
            format=output_format,
        ) == read(expected_result_path)
