from shutil import rmtree
import pytest

from pathlib import Path
from src.helper.file_helper import FileHelper
from unittest.mock import patch, MagicMock

@pytest.fixture
def mocked_logger_warning():
    with patch('src.core.logger.Logger.warning') as mocked_warning:
        yield mocked_warning

@pytest.fixture
def mocked_logger_info():
    with patch('src.core.logger.Logger.info') as mocked_info:
        yield mocked_info

@pytest.fixture
def mocked_logger_error():
    with patch('src.core.logger.Logger.error') as mocked_error:
        yield mocked_error

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
        assert False
    rmtree(path_name)