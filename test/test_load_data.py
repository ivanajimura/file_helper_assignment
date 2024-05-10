import pytest
import json
from unittest.mock import patch
from src.helper.file_helper import FileHelper


def test_load_data_success(tmpdir):
    # Prepare a fake data directory and a JSON file within it
    fake_data_dir = tmpdir.mkdir("data")
    data_file = fake_data_dir.join("data.json")
    sample_data = {"key": "value"}

    # Write sample data to the JSON file
    with open(data_file, "w") as f:
        json.dump(sample_data, f)

    # Patch '__get_data_path' to return the path of our fake data directory
    with patch('src.helper.file_helper.FileHelper._FileHelper__get_data_path', return_value=str(fake_data_dir)):
        # Call 'load_data' and capture its output
        result = FileHelper.load_data()

    # Assert to check if the loaded data matches the expected data
    assert result == sample_data, "The loaded data should match the written data"

def test_load_data_non_json_error(tmpdir):
    # Prepare a fake data directory and an improperly formatted JSON file within it
    fake_data_dir = tmpdir.mkdir("data")
    data_file = fake_data_dir.join("data.json")

    # Write non-JSON content to the file (for example, plain text)
    data_file.write("This is not JSON content")

    # Patch '__get_data_path' to return the path of our fake data directory
    with patch('src.helper.file_helper.FileHelper._FileHelper__get_data_path', return_value=str(fake_data_dir)):
        # Attempt to call 'load_data' and expect an exception due to invalid JSON
        with pytest.raises(json.JSONDecodeError):
            _ = FileHelper.load_data()

