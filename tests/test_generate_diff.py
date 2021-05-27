from gendiff.gendiff import generate_diff
import pytest
import os


FORMATS = ['stylish', 'plain', 'json']


def read(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    return file


def get_fixture_path(fixture_name):
    for root, _, files in os.walk(os.getcwd()):
        for name in files:
            if name == fixture_name:
                return os.path.abspath(os.path.join(root, name))


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        get_fixture_path(('file1.json')),
        get_fixture_path(('file2.json')),
        get_fixture_path(('result.stylish')),
    ),
    (
        get_fixture_path(('file1.yaml')),
        get_fixture_path(('file2.yaml')),
        get_fixture_path(('result.stylish')),
    ),
])
def test_generate_diff_default(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
    ) == read(expected_result)


@pytest.mark.parametrize('first_file, second_file', [
    (
        get_fixture_path(('file1.json')),
        get_fixture_path(('file2.json')),
    ),
    (
        get_fixture_path(('file1.yaml')),
        get_fixture_path(('file2.yaml')),
    ),
])
def test_generate_diff_formats(first_file, second_file):
    for format in FORMATS:
        expected_result = get_fixture_path('result.{}'.format(format))
        assert generate_diff(
            first_file,
            second_file,
            format_name='{}'.format(format),
        ) == read(expected_result)
