import json                         # used for json.dump to store a json into a file
import os                           # used to access files in subfolders using os.path.join, os.path.abspath, os.path.dirname
import sys                          # used to find folder of the CDG executable with sys.executable
from shutil import rmtree           # rmtree is used to remove folders

# Import commented as it will not be tested
from src.core.logger import Logger      # used for logging throughout the program



class FileHelper:
    """ Offers static methods related to creating and removing files and folders.
    Used to generate Data Packages.
    """    
    
    @staticmethod
    def create_dir(dir_path: str) -> None:
        """ Creates folder.
        Used during creation of a new DP (mostly untouched legacy code).
        Does not sanitize input.
        If reserved characters are present, it will log an error.

        Args:
            dir_path (str): path to the folder to be created. Should work with both relative and absolute paths.
        """        
        if not os.path.isdir(dir_path):
            try:
                os.makedirs(dir_path)
                Logger.info(f'Directory was created [{dir_path}]')
            except OSError:
                Logger.error(f'OS Error creating Directory [{dir_path}]')

        else:
            Logger.warning(
                f'Directory [{dir_path}] already exists. It was not created.')

    
    @staticmethod
    def get_file_names_with_extension_from_dir(directory_path: str, extension: str ='.h') -> list[str]:
        """ Returns a list with absolute path with file name and extension for each file in a folder
        Deprecated. There is no method call in project.

        Args:
            directory_path (str): relative path to a folder
            extension (str, optional): File extension to be checked. Defaults to '.h'. Unable to check multiple extensions at once.

        Returns:
            list[str]: List of absolutePath/fileName.extension of files in folder
        """        
        files = []

        if not os.path.isdir(directory_path):
            Logger.warning(f'Cannot find directory [{directory_path}].')
            return files

        for item in os.listdir(directory_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(directory_path, item)) and item.endswith(extension):
                files.append(item)

        if files == []:
            Logger.warning(f'Cannot find files with [{extension}] in directory [{directory_path}].')

        return files


    @staticmethod
    def remove_file(file_path: str) -> None:
        """ Removes file if it exists
        Used in app/SCI.py (untouched legacy code) to remove files from previous DPs when creating a new DP in the same folder.
        Unsure if necessary, as the code also removes whole folders.
        
        Args:
            file_path (str): path to file. Unsure if it works with relative paths too.
        """        
        if not os.path.isfile(file_path):
            Logger.warning(f'File to be removed does not exist [{file_path}]')
            return
        try:
            os.remove(file_path)
            Logger.info(f'Removed File [{file_path}]')
        except OSError:
            Logger.error(f'OS Error removing File [{file_path}]')
