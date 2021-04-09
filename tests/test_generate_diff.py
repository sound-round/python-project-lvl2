from gendiff.gendiff import generate_diff
import pytest


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('first_file, second_file, expected_result', [
    (
        'tests/fixtures/file1_plain.json',
        'tests/fixtures/file2_plain.json',
        'tests/fixtures/result_plain.txt',
    ),
    (
        'tests/fixtures/file1_plain.yaml',
        'tests/fixtures/file2_plain.yaml',
        'tests/fixtures/result_plain.txt',
    ),
    (
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        'tests/fixtures/result_nested.txt',
    ),
    (
        'tests/fixtures/file1_nested.yaml',
        'tests/fixtures/file2_nested.yaml',
        'tests/fixtures/result_nested.txt',
    )
])
def test_generate_diff(first_file, second_file, expected_result):
    assert generate_diff(
        first_file,
        second_file,
    ) == str(read(expected_result))
