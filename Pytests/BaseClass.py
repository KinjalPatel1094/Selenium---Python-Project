import inspect
import logging


class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("log_file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        return logger