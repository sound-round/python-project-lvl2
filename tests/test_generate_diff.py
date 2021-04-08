from gendiff.gendiff import generate_diff
import pytest
import json
import yaml


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_generate_diff_json():
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    ) == str(read('tests/fixtures/result.txt'))

def test_generate_diff_yaml():
    assert generate_diff(
        'tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yaml',
    ) == str(read('tests/fixtures/result.txt'))