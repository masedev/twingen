import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir='logs', log_filename='logfile.log', log_level=logging.INFO):
        self.log_dir = log_dir
        self.log_filename = log_filename
        self.log_level = log_level
        self.logger = self.setup_logger()

    def setup_logger(self):
        # Create a logger
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Create a file handler
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        log_file_path = os.path.join(self.log_dir, self.log_filename)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
    
    def info(self, message):
        self.logger.info(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)