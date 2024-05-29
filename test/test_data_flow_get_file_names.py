import os
from shutil import rmtree
from src.helper.file_helper import FileHelper

def test_get_file_names_not_a_folder():
    not_dir = "not_a_folder"
    # Ensure the dir does not exist
    if os.path.isdir(not_dir):
        rmtree(not_dir)
    # Ascertain tmp_dir does not exist at this point
    assert not os.path.isdir(not_dir)

    returnObj = FileHelper.get_file_names_with_extension_from_dir(directory_path=not_dir, extension="irrelevant")
    assert returnObj == []
    

def test_get_file_names_empty_folder():
    empty_dir = "valid_folder"
    # Ensure empty_dir is empty
    if not os.path.isdir(empty_dir):
        os.mkdir(empty_dir)
    if len(os.listdir(empty_dir)) > 0:
        rmtree(empty_dir)
        os.mkdir(empty_dir)
    assert len(os.listdir(empty_dir)) == 0

    returnObj = FileHelper.get_file_names_with_extension_from_dir(directory_path=empty_dir, extension="irrelevant")
    assert returnObj == []

    #Clean up testing environment
    rmtree(empty_dir)

    
def test_get_file_names_subfolders_only():
    dir_with_subdirs = "valid_folder"
    # Ensure empty_dir is empty
    if not os.path.isdir(dir_with_subdirs):
        os.mkdir(dir_with_subdirs)
    if len(os.listdir(dir_with_subdirs)) > 0:
        rmtree(dir_with_subdirs)
        os.mkdir(dir_with_subdirs)
    
    #Create a subfolder
    subdir = "valid_subfolder"
    os.mkdir(os.path.join(dir_with_subdirs, subdir))

    returnObj = FileHelper.get_file_names_with_extension_from_dir(directory_path=dir_with_subdirs, extension="irrelevant")
    assert returnObj == []

    #Clean up testing environment
    rmtree(dir_with_subdirs)

def test_get_file_names_extension_doesnt_match():
    dir_with_file = "valid_folder"
    file_name = "irrelevant_filename"
    file_extension = ".txt"
    # Ensure empty_dir is empty
    if not os.path.isdir(dir_with_file):
        os.mkdir(dir_with_file)
    if len(os.listdir(dir_with_file)) > 0:
        rmtree(dir_with_file)
        os.mkdir(dir_with_file)
    assert os.path.isdir(dir_with_file)
    assert len(os.listdir(dir_with_file)) == 0
    
    #Create a file
    file_complete_name = file_name + file_extension
    open(os.path.join(dir_with_file, file_complete_name), 'a').close()
    
    assert os.path.isfile(os.path.join(dir_with_file, file_complete_name))

    test_extension = ".h"
    assert test_extension != file_extension
    returnObj = FileHelper.get_file_names_with_extension_from_dir(directory_path=dir_with_file, extension=test_extension)
    assert returnObj == []

    # Clean up
    rmtree(dir_with_file)

def test_get_file_names_one_match():
    dir_with_file = "valid_folder"
    file_name = "irrelevant_filename"
    file_extension = ".h"
    # Ensure empty_dir is empty
    if not os.path.isdir(dir_with_file):
        os.mkdir(dir_with_file)
    if len(os.listdir(dir_with_file)) > 0:
        rmtree(dir_with_file)
        os.mkdir(dir_with_file)
    assert os.path.isdir(dir_with_file)
    assert len(os.listdir(dir_with_file)) == 0
    
    #Create a file
    file_complete_name = file_name + file_extension
    open(os.path.join(dir_with_file, file_complete_name), 'a').close()
    
    assert os.path.isfile(os.path.join(dir_with_file, file_complete_name))

    test_extension = ".h"
    assert test_extension == file_extension
    returnObj = FileHelper.get_file_names_with_extension_from_dir(directory_path=dir_with_file, extension=test_extension)
    assert returnObj == [file_complete_name]
    assert len(returnObj) == 1

    # Clean up
    rmtree(dir_with_file)
