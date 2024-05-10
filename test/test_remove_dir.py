import os
import pytest
import json
from src.helper.file_helper import FileHelper
from unittest.mock import patch, MagicMock

@pytest.fixture
def mocked_logger_warning():
    with patch('src.core.logger.Logger.warning') as mocked_warning:
        yield mocked_warning


def test_remove_dir_directory_does_not_exist(tmpdir, caplog):
    dir_path = os.path.join(str(tmpdir), 'non_existent_directory')

    FileHelper.remove_dir(dir_path)

    assert 'Directory' in caplog.text
    assert 'does not exist. It was not removed.' in caplog.text

def test_remove_dir_directory_exists(tmpdir, caplog):
    dir_path = os.path.join(str(tmpdir), 'existing_directory')
    os.makedirs(dir_path)

    FileHelper.remove_dir(dir_path)

    assert 'Directory' in caplog.text
    assert 'has been removed successfully.' in caplog.text

    assert not os.path.exists(dir_path)

def test_remove_dir_os_error(tmpdir, caplog, monkeypatch):
    def mock_rmtree_error(path):
        raise OSError("Mock OS Error")

   #  monkeypatch.setattr(rmtree, 'rmtree', mock_rmtree_error)

    dir_path = os.path.join(str(tmpdir), 'existing_directory')
    os.makedirs(dir_path)

    FileHelper.remove_dir(dir_path)

    assert 'OS Error' in caplog.text
    assert 'removing directory' in caplog.text
    
