from gendiff.gendiff import generate_diff
import pytest


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/file1_simple.json',
        'tests/fixtures/file2_simple.json',
        'tests/fixtures/result_simple.txt',
    ),
    (
        'tests/fixtures/file1_simple.yaml',
        'tests/fixtures/file2_simple.yaml',
        'tests/fixtures/result_simple.txt',
    ),
    (
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        'tests/fixtures/result_nested_stylish.txt',
    ),
    (
        'tests/fixtures/file1_nested.yaml',
        'tests/fixtures/file2_nested.yaml',
        'tests/fixtures/result_nested_stylish.txt',
    )
])
def test_generate_diff(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
    ) == str(read(expected_result))
