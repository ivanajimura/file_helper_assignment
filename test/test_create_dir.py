import pytest

from shutil import rmtree
from pathlib import Path

from src.helper.file_helper import FileHelper
from test.fixtures import mocked_logger_error, mocked_logger_info, mocked_logger_warning

def test_create_dir_happy_path(mocked_logger_info) -> None:
    path_name = "a_happy_path"
    
    #ensure path does not exist first
    if Path(path_name).exists():
        rmtree(path_name)
    
    FileHelper.create_dir(dir_path = path_name)
        
    if Path(path_name).exists():
        assert True    
    else:
        assert False
    rmtree(path_name)

def test_create_dir_folder_already_exists(mocked_logger_info, mocked_logger_warning, mocked_logger_error ) -> None:
    path_name = "path_already_exists"
    
    #ensure path exists first
    if not Path(path_name).exists():
        FileHelper.create_dir(dir_path = path_name)

    FileHelper.create_dir(dir_path = path_name)
    if Path(path_name).exists():
        assert True    
    else:
        assert False
    rmtree(path_name)
    
@pytest.mark.xfail          # this test is supposed to fail as there is no checking for reserved characters
def test_create_dir_reserved_characters(mocked_logger_info, mocked_logger_warning, mocked_logger_error) -> None:
    path_name = "?:;..,\\//"
    FileHelper.create_dir(dir_path = path_name)
    
    if not Path(path_name).exists():
        assert True    
    else:
        rmtree(path_name)
        assert False
    