from gendiff.gendiff import generate_diff
import pytest


def read(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    return file


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/simple/file1_simple.json',
        'tests/fixtures/simple/file2_simple.json',
        'tests/fixtures/result_simple.txt',
    ),
    (
        'tests/fixtures/simple/file1_simple.yaml',
        'tests/fixtures/simple/file2_simple.yaml',
        'tests/fixtures/result_simple.txt',
    ),
    (
        'tests/fixtures/nested/file1_nested.json',
        'tests/fixtures/nested/file2_nested.json',
        'tests/fixtures/result_nested_stylish.txt',
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
    ) == str(read(expected_result))


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
    ) == str(read(expected_result))


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
    ) == str(read(expected_result))
