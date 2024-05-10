import pytest
from src.helper.file_helper import FileHelper

def test_demonstration_pass():
    assert True
    
@pytest.mark.xfail 
def test_demonstration_fail():
    assert False