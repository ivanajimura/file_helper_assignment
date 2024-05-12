from datetime import datetime
import os
#from src.GUI.logGUI import LogGUI

#Log file location
LOG_DIRECTORY = os.path.join(os.getcwd(), "logs")
LOG_FILE = os.path.join(LOG_DIRECTORY,"complete.log")

#Empty the log file
if os.path.exists(LOG_FILE):
    open(LOG_FILE, "w")

# Create a directory for logs if it doesn't exist
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

class Logger:
    """
    Implements logging functions
    """
    def __init__(self):
        """
        Nothing defined here, just creates the object instance
        """
        pass

    def get_log_directory():
        """
        Obtains log directory from constant LOG_DIRECTORY
        """
        return LOG_DIRECTORY

    def get_log_file():
        """
        Obtains log file from constant LOG_FILE
        """
        return LOG_FILE

    @staticmethod
    def debug(message):
        """
        Implements debug log
        args:
            message (str): message to log        
        """
        Logger.log('DEBUG', message)


    @staticmethod
    def warning(message):
        """
        Implements warning log
        args:
            message (str): message to log        
        """
        Logger.log('WARNING', message)

    @staticmethod
    def info(message):
        """
        Implements info log
        args:
            message (str): message to log
        """
        Logger.log('INFO', message)

    @staticmethod
    def error(message):
        """
        Implements error log
        args:
            message (str): message to log
        """
        Logger.log('ERROR', message)

    @staticmethod
    def critical(message):
        """
        Implements critical log
        args:
            message (str): message to log
        """
        Logger.log('CRITICAL', message)

    @staticmethod
    def emergency(message):
        """
        Implements emergency log
        args:
            message (str): message to log
        """
        Logger.log('EMERGENCY', message)

    @staticmethod
    def log_to_file(level, message):
        """
        Writes log message to log file
        Args:
            level (string): level of the log message.
            message (string): content of the log message.
        """

        with open(LOG_FILE, "a") as file_writer:
            file_writer.write(f"{datetime.now()}: {level.lower()} - {message}\n")

    @staticmethod
    def log(level, message):
        """
        Implements log regardless of critical level
        args:
        level (str): criticality of the log
        message (str): message itself to log
        """
        log = f"[{datetime.now()}] {level}: {message}"
        #log_box = LogGUI()
        #log_box.insert_text(f'{log}\n')
        Logger.log_to_file(level, message)
