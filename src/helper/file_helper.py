import json                         # used for json.dump to store a json into a file
import os                           # used to access files in subfolders using os.path.join, os.path.abspath, os.path.dirname
import sys                          # used to find folder of the CDG executable with sys.executable
from shutil import rmtree           # rmtree is used to remove folders

# Import commented as it will not be tested
from core.logger import Logger      # used for logging throughout the program



class FileHelper:
    """ Offers static methods related to creating and removing files and folders.
    Used to generate Data Packages.
    """    
    @staticmethod
    def start_config_files() -> None:
        """ Deprecated in CDG 2.0.
        It was used to load settings from config/data_package_config.json.
        Whenever settings changed, a new executable was needed.
        Settings were moved from json file to shelve and are now editable by the user.
        The file config/data_package_config.json was kept to avoid errors in the legacy code.
        """        
        # Get path of the executable
        dir_path = os.path.join(os.path.dirname(sys.executable), '_internal')
        # Creates subpath to config if needed
        if os.path.exists(dir_path):
            file_path = os.path.join(dir_path, 'data_package_config.json')
        else:
            file_path = os.path.abspath(os.path.join(
                'src', 'config', 'data_package_config.json'))
        # Checks if config file exists
        if os.path.exists(file_path):
            print(f'O arquivo {file_path} já existe.')
        # If file does not exist, creates it in this format
        else:
            json_data = {
                "package_name": "",
                "output_folder": "",
                "versions": [],
                "ticket_ids": [],
                "only_completed_tickets": False
            }
            # saves the JSON into file
            with open(file_path, 'w') as file:
                json.dump(json_data, file, indent=4)

    @staticmethod
    def remove_dir(dir_path: str) -> None:
        """ Removes folder if it exists.
        Used before creating a new Data Package (DP) in app/dataPackage.py (mostly untouched legacy code).
        It ensures files from previously generated DPs are not mixed with the DP being generated.

        Args:
            dir_path (str): path to the folder. Should work with both relative and absolute paths.
        """        
        if not os.path.isdir(dir_path):
            Logger.warning(
                f'Directory [{dir_path}] does not exist. It was not removed.')
            return

        try:
            rmtree(dir_path)
            Logger.info(
                f'Directory [{dir_path}] has been removed successfully.')
        except OSError:
            Logger.warning(f'OS Error removing directory [{dir_path}]')

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
    def read_json_file(file_path: str) -> json:
        """ Reads a JSON file and returns it as a JSON object.
        Used to read config/data_package_stages.json and identify stages of development (untouched legacy code).
        
        The following usage is still present in the code, but does not affect the generated DP:
            - read user credentials and environment settings in config/environment.json
            - read settings related to the data package from config/data_package_config.json
        These responsibilities moved to shelve and handled directly by the user in the UI.
        This change allows the program to persist changes and does not require new executable creation every time a setting is changed.
        
        Args:
            file_path (str): path to the JSON file. Will throw an exception if file is not a JSON.

        Returns:
            json: JSON object contained in file (hopefully)
        """        
        if os.path.isfile(file_path):
            with open(file_path) as f:
                json_structure = json.load(f)   # risky. Will throw an exception if file is not a JSON
                return json_structure
        else:
            Logger.error(f'Json File does not exist [{file_path}]')
            return {}


    @staticmethod
    def save_data(data: json) -> None:
        """ Stores JSON object into a file. Removes any data from file if it already exists.
        Used to store JIRA session cookie (untouched legacy code).

        Args:
            data (json): JSON object. Input is not validated by the function
        """

        # Creates folder if necessary
        data_path = FileHelper.__get_data_path()
        if not os.path.isdir(data_path):
            FileHelper.create_dir(data_path)

        # Dumps JSON into file
        with open('{}/data.json'.format(data_path), 'w+') as file:
            json.dump(data, file)

    @staticmethod
    def load_data() -> json:
        """ Loads data from JSON. Does not validate if data is indeed a JSON file.
        Does not take any input, only checks for data.json file inside 'data' subfolder.
        Unsure if this is part of legacy code still in use.

        Returns:
            json: loaded JSON object
        """        
        data_path = FileHelper.__get_data_path()
        with open('{}/data.json'.format(data_path), 'r') as file:
            return json.load(file)

    @staticmethod
    def __get_data_path() -> str:
        """ Returns the absolute path to the subfolder /data.
        Does not check if the subfolder exists.
        Unsure if this is still in use.

        Returns:
            str: absolute path to the "data" subfolder
        """        
        return os.path.abspath('data')

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