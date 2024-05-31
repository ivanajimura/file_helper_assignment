import pytest

from shutil import rmtree
from pathlib import Path
from unittest import mock

from src.helper.file_helper import FileHelper

def test_create_dir_with_non_existent_folder() -> None:
    path_name = "a_happy_path"

    FileHelper.create_dir(dir_path = path_name)

    assert Path(path_name).exists()

    rmtree(path_name)

def test_create_dir_with_existing_folder() -> None:
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
