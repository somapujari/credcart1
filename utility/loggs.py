import inspect
import logging

#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         formatter = logging.Formatter('%(message)s  : %(asctime)s : %(lineno) :')
#         fileHandler = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\crecartproject1\logs\credcartlog.log')
#         fileHandler.setFormatter(formatter)
#         logger.addHandler(fileHandler)
#         return logger


import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger('credcartLogger')

        # Set the logger level
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers (file or console) if they already exist
        if not logger.hasHandlers():
            # Create a file handler to log to a file
            fileHandler = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\crecartproject1\logs\credcartlog.log')

            # Set up a formatter with the desired format
            formatter = logging.Formatter('%(message)s : %(asctime)s : %(lineno)d', datefmt='%Y-%m-%d %H:%M:%S')
            fileHandler.setFormatter(formatter)

            # Add file handler to the logger
            logger.addHandler(fileHandler)

            # Create a console handler to log to the terminal
            consoleHandler = logging.StreamHandler()
            consoleHandler.setFormatter(formatter)

            # Add console handler to the logger
            logger.addHandler(consoleHandler)

        return logger
