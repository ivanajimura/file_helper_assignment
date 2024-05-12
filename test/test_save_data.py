import os
import pytest
import json
from src.helper.file_helper import FileHelper
from test.fixtures import mocked_logger_error, mocked_logger_info, mocked_logger_warning

def test_save_data_success():
    test_data = {"key": "value"}
    file_path = os.path.abspath('data')
    
    FileHelper.save_data(test_data)

    with open(file_path, 'r') as file:
        saved_data = json.load(file)
        print("Saved data:", saved_data)
        assert saved_data == test_data

    os.rmtree(file_path)
    
def test_save_data_returns_error_when_invalid_data(tmp_path):
    file_path = os.path.abspath('data')
    bad_data = "asd"
    FileHelper.save_data(bad_data)

    with pytest.raises(json.JSONDecodeError):
        with open(file_path, 'r') as file:
            saved_data = json.load(file)
            
    os.rmtree(file_path)
