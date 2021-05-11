from gendiff.gendiff import generate_diff
import pytest
import os


def read(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    return file


def get_fixture_path(fixture_name):
    for root, _, files in os.walk(cwd):
        for name in files:
            if name == fixture_name:
                return os.path.abspath(os.path.join(root, name))


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        #'tests/fixtures/nested/file1_nested.json',
        #'tests/fixtures/nested/file2_nested.json',
        get_fixture_path(('file1_nested.json')),
        get_fixture_path(('file2_nested.json')),
        #'tests/fixtures/result_nested_stylish.txt',
        get_fixture_path(('result_nested_stylish.txt'))
    ),
    (
        'tests/fixtures/nested/file1_nested.yaml',
        'tests/fixtures/nested/file2_nested.yaml',
        'tests/fixtures/result_nested_stylish.txt',
    ),
])
def test_generate_diff_stylish(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
        format_name='stylish',
    ) == read(expected_result)


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/nested/file1_nested.json',
        'tests/fixtures/nested/file2_nested.json',
        'tests/fixtures/result_nested_stylish.txt',
    ),
])
def test_generate_diff_stylish_default(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
    ) == read(expected_result)


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/nested/file1_nested.json',
        'tests/fixtures/nested/file2_nested.json',
        'tests/fixtures/result_nested_plain.txt',
    ),
    (
        'tests/fixtures/nested/file1_nested.yaml',
        'tests/fixtures/nested/file2_nested.yaml',
        'tests/fixtures/result_nested_plain.txt',
    )
])
def test_generate_diff_plain(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
        format_name='plain',
    ) == read(expected_result)


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/nested/file1_nested.json',
        'tests/fixtures/nested/file2_nested.json',
        'tests/fixtures/result_json.json',
    ),
    (
        'tests/fixtures/nested/file1_nested.yaml',
        'tests/fixtures/nested/file2_nested.yaml',
        'tests/fixtures/result_json.json',
    )
])
def test_generate_diff_json(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
        format_name='json',
    ) == read(expected_result)
