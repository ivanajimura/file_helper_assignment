import os
from src.helper.file_helper import FileHelper

def test_get_data_path():
    expected_path = os.path.abspath('data')
    result = FileHelper._FileHelper__get_data_path()
    assert result == expected_path
 
