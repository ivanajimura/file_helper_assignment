import pytest
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