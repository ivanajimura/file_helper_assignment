import os
from shutil import rmtree
from src.helper.file_helper import FileHelper



def test_remove_file_non_existing_file():
    tmp_dir = "empty_testing_dir"
    # Ensure the dir is empty
    if os.path.isdir(tmp_dir):
        rmtree(tmp_dir)
    # Ascertain tmp_dir does not exist at this point
    assert not os.path.isdir(tmp_dir)
    # Create tmp_dir
    os.mkdir(tmp_dir)
    # Ascertain tmp_dir is empty
    assert len(os.listdir(tmp_dir)) == 0
    # Attempt to remove a non-existing file
    non_existing_file = "a_file.txt"
    FileHelper.remove_file(non_existing_file)
    # Assert no errors were thrown and file does not exist
    assert not os.path.isfile(non_existing_file)
    #Clean up test environment
    rmtree(tmp_dir)

def test_remove_file_successfully():
    tmp_dir = "empty_testing_dir"
    # Create tmp_dir if it does not exist
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    # Ascertain tmp_dir exists at this point
    assert os.path.isdir(tmp_dir)
    # Create a file
    file_to_create_and_remove = "a_file.txt"
    if not file_to_create_and_remove in os.listdir(tmp_dir):
        open(os.path.join(tmp_dir, file_to_create_and_remove), 'a').close()
    assert os.path.isfile(os.path.join(tmp_dir, file_to_create_and_remove))
    FileHelper.remove_file(os.path.join(tmp_dir, file_to_create_and_remove))
    assert not os.path.isfile(os.path.join(tmp_dir, file_to_create_and_remove))
    #Clean up test environment
    rmtree(tmp_dir)

def test_remove_file_os_error():
    tmp_dir = "empty_testing_dir"
    # Create tmp_dir if it does not exist
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    # Ascertain tmp_dir exists at this point
    assert os.path.isdir(tmp_dir)
    # Create a file
    file_to_create_and_remove = "a_file.txt"
    try:
        if not file_to_create_and_remove in os.listdir(tmp_dir):
            open(file_to_create_and_remove, 'a')
        assert os.path.isfile(file_to_create_and_remove)
        # this line will thrown an error
        FileHelper.remove_file(file_to_create_and_remove)
    except:
        assert os.path.isfile(file_to_create_and_remove)
    finally:
        #Clean up test environment
        rmtree(tmp_dir)