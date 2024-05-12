import os
import pytest
import json
from src.helper.file_helper import FileHelper
from test.fixtures import mocked_logger_error, mocked_logger_info, mocked_logger_warning

def test_remove_dir_directory_is_removed_successfully(tmp_path):
    tmp_dir = tmp_path / "tmp_dir/data.json"
    tmp_dir.parent.mkdir()
    tmp_dir.touch()

    assert len(list(tmp_path.iterdir())) == 1
    
    FileHelper.remove_dir(tmp_dir.parent)

    assert len(list(tmp_path.iterdir())) == 0

def test_remove_dir_directory_is_not_removed_if_it_does_exist(tmp_path):

    assert len(list(tmp_path.iterdir())) == 0
    
    FileHelper.remove_dir("tmp_dir")

    assert len(list(tmp_path.iterdir())) == 0
 
