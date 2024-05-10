import pytest
import json
from src.helper.file_helper import FileHelper

def test_read_json_file_success(tmpdir):
    # Create a sample JSON file with known content
    sample_data = {"key": "value"}
    file_path = tmpdir.join("sample.json")
    file_path.write(json.dumps(sample_data))

    # Read the JSON file using the FileHelper class from the fileHelper module
    result = FileHelper.read_json_file(str(file_path))

    # Assert to check if the read data matches the expected data
    assert result == sample_data, "The read data should match the written data"

def test_read_json_file_nonexistent():
    # Define a path to a non-existent JSON file
    non_existent_file = 'fakepath/fakefile.json'

    # Attempt to read the non-existent JSON file using the FileHelper class
    result = FileHelper.read_json_file(non_existent_file)

    # Assert to check if the result is an empty dictionary (expected behavior for non-existent files)
    assert result == {}, "The result should be an empty dict for a non-existent file"

# Ensure you run pytest in a context where it can find the fileHelper module and the test script
