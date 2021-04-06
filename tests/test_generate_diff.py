from gendiff.gendiff import generate_diff
import pytest
import json


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_generate_diff():
    assert generate_diff(
        json.load(open('tests/fixtures/file1.json')),
        json.load(open('tests/fixtures/file2.json')),
    ) == str(read('tests/fixtures/result.txt'))