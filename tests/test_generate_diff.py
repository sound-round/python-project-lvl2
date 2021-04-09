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
        'tests/fixtures/file1_plain.json',
        'tests/fixtures/file2_plain.json',
    ) == str(read('tests/fixtures/result_plain.txt'))

def test_generate_diff_yaml():
    assert generate_diff(
        'tests/fixtures/file1_plain.yaml',
        'tests/fixtures/file2_plain.yaml',
    ) == str(read('tests/fixtures/result_plain.txt'))