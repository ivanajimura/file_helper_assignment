import os
import pytest
import json
from src.helper.file_helper import FileHelper
from unittest.mock import patch, MagicMock

@pytest.fixture
def mocked_logger_warning():
    with patch('src.core.logger.Logger.warning') as mocked_warning:
        yield mocked_warning


def test_save_data_success(tmpdir):
    test_data = {"key": "value"}
    os.chdir(str(tmpdir))

    FileHelper.save_data(test_data)
    file_path = os.path.join(os.getcwd(), 'data.json')

    with open(file_path, 'r') as file:
        saved_data = json.load(file)
        
    assert saved_data == test_data
    
def test_save_data_returns_error_when_invalid_data(test_dir):
    test_dir = tmpdir.mkdir('new_directory')
    file_path = os.path.join(str(test_dir), 'data.json')

    bad_data = "asd"
    FileHelper.save_data(bad_data)

    with pytest.raises(json.JSONDecodeError):
        with open(file_path, 'r') as file:
            saved_data = json.load(file)
    
