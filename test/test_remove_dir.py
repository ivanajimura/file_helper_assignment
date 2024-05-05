from shutil import rmtree
import pytest

from pathlib import Path
from src.helper.file_helper import FileHelper
from test.fixtures import mocked_logger_error, mocked_logger_info, mocked_logger_warning

def test_remove_dir_happy_path(mocked_logger_warning, mocked_logger_info):
    path_name = "a_happy_path"

    #ensure path exists
    if not Path(path_name).exists():
        FileHelper.create_dir(dir_path = path_name)

    FileHelper.remove_dir(dir_path=path_name)
    if not Path(path_name).exists():
        assert True
    else:
        assert False


def test_remove_dir_folder_does_not_exist(mocked_logger_warning, mocked_logger_info):
    path_name = "a_happy_path"

    #ensure path does not exist
    if Path(path_name).exists():
        rmtree(path_name)

    FileHelper.remove_dir(dir_path=path_name)
    if not Path(path_name).exists():
        assert True
    else:
        assert False


@pytest.mark.xfail          # this test is supposed to fail as there is no checking for reserved characters
def test_remove_dir_reserved_characters(mocked_logger_warning, mocked_logger_info):
    path_name = "?:;..,\\//"

    #ensure path exists
    if not Path(path_name).exists():
        FileHelper.create_dir(dir_path = path_name)
        
    FileHelper.remove_dir(dir_path=path_name)
    if not Path(path_name).exists():
        assert True
    else:
        assert False
