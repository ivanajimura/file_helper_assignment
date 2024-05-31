import os
import pytest

from pathlib import Path
from src.helper.file_helper import FileHelper
from test.fixtures import mocked_logger_error, mocked_logger_info, mocked_logger_warning

def test_remove_file_when_file_exists(mocked_logger_warning, mocked_logger_info):
    file_path = "happy_path_file.txt"
    # Ensure file exists
    if not Path(file_path).exists():
        with open(file_path, 'w') as f:
            f.write('dummy content')

    FileHelper.remove_file(file_path=file_path)
    
    if not Path(file_path).exists():
        assert True
    else:
        assert False


def test_remove_file_when_file_does_not_exist(mocked_logger_warning, mocked_logger_info):
    file_path = "file.txt"

    FileHelper.remove_file(file_path=file_path)
    
    if not Path(file_path).exists():
        assert True
    else:
        assert False

@pytest.mark.xfail 
def test_remove_file_reserved_characters(mocked_logger_warning, mocked_logger_info):
    file_path = "?:;..,\\//.txt"
    #ensure path exists
    if not Path(file_path).exists():
        with open(file_path, 'w') as f:
            f.write('dummy content')

    FileHelper.remove_file(file_path=file_path)
    
    if not Path(file_path).exists():
        assert True
    else:
        assert False
